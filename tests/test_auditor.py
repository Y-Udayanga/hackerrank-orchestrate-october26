import csv
import json
from collections import defaultdict
from pathlib import Path
from types import SimpleNamespace
import pytest
from ghosttrace.engine import Auditor
from ghosttrace.ingest import Corpus
from ghosttrace.identity import IdentityGraph
from ghosttrace.intent import classify
from ghosttrace.types import Observation, validate_steps

EARLY='2026-01-01T00:00:00Z'
LATE='2026-01-20T00:00:00Z'
CUTOFF='2026-01-15T00:00:00Z'


def write_csv(path,fields,rows):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)


@pytest.fixture
def setup(tmp_path):
    ids=[dict(user_id='user_test',name='Alex Doe',email='alex@example.test',phone='+12345678901',email_hash='',updated_at=EARLY),
         dict(user_id='user_other',name='Alex Doe',email='other@example.test',phone='+12345678902',email_hash='',updated_at=EARLY)]
    write_csv(tmp_path/'user_identities.csv',list(ids[0]),ids)
    write_csv(tmp_path/'user_audit_log.csv',['audit_id','user_id','event_time','field_name','old_value','new_value'],[])
    # Test policy is independent of the challenge records and answers.
    rules=[('USER_PROFILE','Always','DELETE'),('SUPPORT_ATTACHMENT','Attachment belongs only to the deletion subject','DELETE'),
           ('ANALYTICS_PROFILE','Record is still attributable to a user','ANONYMIZE'),
           ('SECURITY_AUDIT_LOG','Record is within the supplied retention period','RETAIN'),
           ('BACKUP_ARCHIVE','Restore access can be blocked','RETAIN'),
           ('ACCOUNT_TOMBSTONE','Account is deleted and only a stable internal user_id is needed to preserve references to retained records','REDACT')]
    write_csv(tmp_path/'deletion_rules.csv',['rule_id','data_category','condition','required_action'],
              [dict(rule_id=str(i),data_category=c,condition=q,required_action=a) for i,(c,q,a) in enumerate(rules)])
    return tmp_path


def obs(resource='profile-test',category='USER_PROFILE',state='PRESENT',ids=None,time=EARLY,capture=EARLY,fields=None,eid='proof-early',system='account_service'):
    return Observation(evidence_id=eid,source='fixture',location='test',system_id=system,resource_id=resource,
        category=category,state=state,event_time=time,captured_at=capture,
        identifiers=['alex@example.test'] if ids is None else ids,fields=fields or {},method='json')


def run(root,observations,text='Please delete my account.',email='alex@example.test'):
    by_resource=defaultdict(list);by_identifier=defaultdict(set)
    for o in observations:
        key=(o.system_id,o.resource_id);by_resource[key].append(o)
        for ident in o.identifiers:by_identifier[ident].add(key)
    corpus=SimpleNamespace(manifest=[{'file_id':o.evidence_id} for o in observations],activities=[],catalog_links=[],
        by_resource=by_resource,by_identifier=by_identifier,errors=[])
    auditor=Auditor(root,corpus)
    r=auditor.predict(dict(case_id='independent-case',email=email,audit_at=CUTOFF,request_text=text))
    return r['deletion_status'],json.loads(r['steps_json']),auditor


def test_access_is_not_deletion(setup):
    assert run(setup,[obs()],text='Please send a copy of my data.')[0:2]==('NOT_APPLICABLE',[])


def test_explicit_negation(setup):
    assert run(setup,[obs()],text='Please do not delete my account.')[0:2]==('NOT_APPLICABLE',[])


def test_present_profile_requires_three_steps(setup):
    status,steps,_=run(setup,[obs()])
    assert status=='INCOMPLETE'
    assert [s['operation'] for s in steps]==['REPORT_REMAINING_RECORD','DELETE_RECORD','VERIFY_RECORD_ABSENT']
    assert [s['evidence_id'] for s in steps]==['proof-early','','']


def test_complete_retained_security(setup):
    status,steps,_=run(setup,[obs(state='ABSENT'),obs('security-test','SECURITY_AUDIT_LOG',fields={'retention_until':LATE},system='security_service')])
    assert status=='COMPLETE'
    assert [s['operation'] for s in steps]==['VERIFY_RECORD_ABSENT','VERIFY_RECORD_PRESENT']
    assert all(s['evidence_id']=='proof-early' for s in steps)


def test_historical_email(setup):
    change=dict(audit_id='audit-test',user_id='user_test',event_time=EARLY,field_name='email',old_value='old@example.test',new_value='alex@example.test')
    write_csv(setup/'user_audit_log.csv',list(change),[change])
    assert run(setup,[obs(ids=['old@example.test'])],email='old@example.test')[0]=='INCOMPLETE'


def test_recreation_and_flow_first(setup):
    observations=[obs(state='ABSENT'),obs(time='2026-01-10T00:00:00Z',eid='proof-new'),
        obs('connector-test','DATA_FLOW','ACTIVE',system='integration_service')]
    status,steps,_=run(setup,observations)
    assert status=='INCOMPLETE'
    assert [s['operation'] for s in steps if s['phase']=='REMEDIATION']==['DISABLE_DATA_FLOW','DELETE_RECORD']


def test_old_screenshot_superseded(setup):
    older=obs();older.method='gemini-vision'
    status,steps,_=run(setup,[older,obs(state='ABSENT',time='2026-01-10T00:00:00Z',eid='proof-new')])
    assert status=='COMPLETE' and steps[0]['evidence_id']=='proof-new'


def test_capture_after_cutoff_ignored(setup):
    status,steps,_=run(setup,[obs(),obs(state='ABSENT',time='2026-01-10T00:00:00Z',capture=LATE,eid='future')])
    assert status=='INCOMPLETE' and steps[0]['evidence_id']=='proof-early'


def test_event_after_cutoff_ignored(setup):
    assert run(setup,[obs(),obs(state='ABSENT',time=LATE,capture=EARLY,eid='future')])[0]=='INCOMPLETE'


def test_backup_risk(setup):
    status,steps,_=run(setup,[obs('archive-test','BACKUP_ARCHIVE','ACTIVE',system='backup_service')])
    assert status=='INCOMPLETE'
    assert [s['operation'] for s in steps]==['REPORT_RESTORE_RISK','BLOCK_RESTORE','VERIFY_RESTORE_BLOCKED']


def test_tombstone_forbidden_identifiers(setup):
    status,steps,_=run(setup,[obs('reference-test','ACCOUNT_TOMBSTONE',fields={'email':'alex@example.test'},system='identity_service')])
    assert status=='INCOMPLETE'
    assert [s['operation'] for s in steps]==['REPORT_EXPOSED_PII','REDACT_RECORD','VERIFY_RECORD_REDACTED']


def test_clean_tombstone(setup):
    status,steps,_=run(setup,[obs('reference-test','ACCOUNT_TOMBSTONE','REDACTED',ids=['user_test'],fields={'subject_reference':'user_test'},system='identity_service')])
    assert status=='COMPLETE' and steps[0]['operation']=='VERIFY_RECORD_REDACTED'


def test_primary_replica_disagreement(setup):
    primary=obs(state='ABSENT');primary.location='primary'
    replica=obs(eid='replica-proof');replica.location='replica';replica.method='sqlite'
    status,steps,_=run(setup,[primary,replica])
    assert status=='INCOMPLETE' and steps[0]['evidence_id']=='replica-proof'


def test_unrelated_customer_document(setup):
    status,steps,_=run(setup,[obs(state='ABSENT'),obs('other-attachment','SUPPORT_ATTACHMENT',ids=['other@example.test'],system='support_platform')])
    assert status=='COMPLETE' and len(steps)==1


def test_identical_names_are_not_identity_links(setup):
    status,steps,_=run(setup,[obs(state='ABSENT'),obs('other-profile',ids=['Alex Doe'])])
    assert status=='COMPLETE' and len(steps)==1


@pytest.mark.parametrize('content',[None,'{corrupt'])
def test_missing_or_corrupt_evidence_fails_closed(tmp_path,content):
    (tmp_path/'evidence').mkdir()
    if content is not None:(tmp_path/'evidence/bad.json').write_text(content)
    write_csv(tmp_path/'evidence_files.csv',['file_id','file_path','origin','captured_at'],
              [dict(file_id='bad',file_path='evidence/bad.json',origin='test',captured_at=EARLY)])
    write_csv(tmp_path/'system_activity.csv',['activity_id','event_time','event_type','source_system','target_system','resource_id','reported_result','details'],[])
    with pytest.raises(RuntimeError):Corpus(tmp_path).load()


def test_future_identity_link_does_not_leak(setup):
    status,steps,_=run(setup,[obs(ids=[],state='ABSENT'),obs(time=LATE,capture=LATE)])
    assert status=='INCOMPLETE' and steps==[]


def test_no_resource_proof_is_not_complete(setup):
    status,steps,auditor=run(setup,[])
    assert status=='INCOMPLETE' and steps==[] and auditor.diagnostics[0]['gaps']


def test_log_trace_join_and_debug_noise(tmp_path):
    corpus=Corpus.__new__(Corpus);corpus.observations=[];corpus.notes=[]
    meta=dict(file_id='log-proof',file_path='evidence/test.log',captured_at=EARLY)
    text=f'''{EARLY} level=DEBUG service=account_service trace_id=t event=profile_lookup_started lookup_key=alex@example.test
{EARLY} level=DEBUG service=account_service trace_id=t resource_id=wrong event=cache_lookup result=miss
{EARLY} level=INFO service=account_service trace_id=t resource_id=profile-test event=profile_lookup_completed rows=0 http_status=404'''
    corpus.log_file(meta,text)
    assert len(corpus.observations)==1
    assert corpus.observations[0].identifiers==['alex@example.test']
    assert corpus.observations[0].state=='ABSENT'


def test_sql_attach_is_rejected():
    corpus=Corpus.__new__(Corpus);corpus.observations=[];corpus.notes=[]
    with pytest.raises(Exception):corpus.sql_file(dict(file_id='sql',file_path='test.sql',captured_at=EARLY),"ATTACH DATABASE 'outside.db' AS outside;")


def test_nested_sql_json_is_parsed():
    corpus=Corpus.__new__(Corpus);corpus.observations=[];corpus.notes=[]
    script="""CREATE TABLE records(resource_id TEXT, origin_system TEXT,collection_name TEXT,record_json TEXT);
    INSERT INTO records VALUES('a','analytics_platform','customer_analytics_reports','{"resource_id":"a","email":null,"user_id":null}');"""
    corpus.sql_file(dict(file_id='sql',file_path='test.sql',captured_at=EARLY),script)
    assert corpus.observations[0].state=='ANONYMIZED'


def test_future_email_change_does_not_match():
    snapshot=dict(user_id='u',email='new@example.test',phone='',email_hash='',updated_at=LATE)
    change=dict(user_id='u',event_time=LATE,field_name='email',old_value='old@example.test',new_value='new@example.test',audit_id='change')
    graph=IdentityGraph([snapshot],[change])
    assert graph.resolve('old@example.test',CUTOFF).user_id=='u'
    with pytest.raises(ValueError):graph.resolve('new@example.test',CUTOFF)


def test_quoted_request_is_not_authorization():
    assert classify('What does "delete my account" mean?').intent!='DELETE_REQUEST'


def test_new_primary_absence_does_not_clear_known_replica(setup):
    replica=obs();replica.method='sqlite';replica.location='customer_profiles_failover_replica'
    primary=obs(state='ABSENT',time='2026-01-10T00:00:00Z',eid='primary-new')
    assert run(setup,[replica,primary])[0]=='INCOMPLETE'


def test_missing_verification_is_rejected():
    steps=[dict(step_no=1,phase='FINDING',system_id='account_service',resource_id='p',
                operation='REPORT_REMAINING_RECORD',state='PRESENT',evidence_id='proof')]
    with pytest.raises(ValueError,match='remediation and verification'):validate_steps('INCOMPLETE',steps,{'proof'})


def test_visual_schema_rejects_email_resource():
    from ghosttrace.types import VisualRecord
    with pytest.raises(ValueError):VisualRecord(system_id='account_service',resource_id='alex@example.test',category='USER_PROFILE',
        state='PRESENT',identifiers=['alex@example.test'],supporting_text='Email alex@example.test')


def test_intent_batch_coverage_and_grounding():
    from ghosttrace.intent import classify_many
    from ghosttrace.types import IntentBatch,IntentItem
    class Fake:
        def generate(self,*args):
            return IntentBatch(requests=[IntentItem(request_index=7,intent='DELETE_REQUEST',quote='invented',reason='test')])
    with pytest.raises(ValueError):classify_many([{'request_text':'Could you verify the earlier removal?'}],Fake())


def test_explicit_later_negation_defeats_fast_path():
    assert classify('Please delete my account. Actually, do not delete it.').intent!='DELETE_REQUEST'


def test_alias_association_time_is_enforced():
    evidence=obs(fields={'identity_link_time':LATE})
    assert not evidence.available(CUTOFF)


def test_catalog_cannot_override_another_person(setup):
    _,_,auditor=run(setup,[obs(state='ABSENT')])
    other=obs('different-profile',ids=['other@example.test'])
    auditor.corpus.by_resource[('account_service','different-profile')].append(other)
    auditor.corpus.catalog_links=[('different-profile',{'alex@example.test'},EARLY,'catalog-proof')]
    subject=auditor.identities.resolve('alex@example.test',CUTOFF)
    assert ('account_service','different-profile') not in auditor.retrieve(subject,CUTOFF)
    assert auditor.link_conflicts


def test_filename_resolves_only_through_explicit_catalog():
    from ghosttrace.types import VisualExtraction,VisualRecord
    corpus=Corpus.__new__(Corpus);corpus.observations=[];corpus.notes=[];corpus.unresolved=[];corpus.known_names=set()
    corpus.alias_links={'receipt.pdf':[dict(resource_id='object_876',target_system='object_storage',
        details='receipt.pdf belongs to alex@example.test',event_time=LATE,activity_id='catalog-proof')]}
    class Fake:
        def generate(self,*args):
            return VisualExtraction(records=[VisualRecord(resource_id='support_999',system_id='support_platform',
                category='SUPPORT_ATTACHMENT',state='PRESENT',identifiers=['receipt.pdf'],supporting_text='receipt.pdf')],uncertainty='')
    corpus.gemini=Fake()
    corpus.visual(dict(file_id='image-proof',file_path='image.png',origin='object_storage',captured_at=EARLY),b'fake fixture','image')
    assert corpus.observations[0].resource_id=='object_876'
    assert corpus.observations[0].fields['identity_link_evidence']=='catalog-proof'
    assert not corpus.observations[0].available(CUTOFF)


def test_deletion_proof_requirement_is_not_english_only(setup):
    status,_,auditor=run(setup,[obs('retained','SECURITY_AUDIT_LOG',system='security_service')],
        text='Je demande la suppression définitive du compte.')
    assert status=='INCOMPLETE' and auditor.diagnostics[0]['gaps']


def test_visible_stable_tombstone_is_not_exposed_pii():
    from ghosttrace.types import VisualExtraction,VisualRecord
    corpus=Corpus.__new__(Corpus);corpus.observations=[];corpus.notes=[];corpus.unresolved=[];corpus.known_names=set()
    corpus.alias_links={'user_88':[dict(resource_id='tombstone_456',target_system='identity_service',
        details='Reference belongs to user_88',event_time=EARLY,activity_id='catalog-proof')]}
    class Fake:
        def generate(self,*args):
            return VisualExtraction(records=[VisualRecord(resource_id='user_88',system_id='identity_service',
                category='ACCOUNT_TOMBSTONE',state='PRESENT',identifiers=['user_88'],supporting_text='user_88 retained reference')],uncertainty='')
    corpus.gemini=Fake()
    # No invented suffix mapping; only the explicit alias association is valid.
    corpus.visual(dict(file_id='image-proof',file_path='image.png',origin='identity_service',captured_at=EARLY),b'fixture','image')
    assert corpus.observations[0].state=='REDACTED'
