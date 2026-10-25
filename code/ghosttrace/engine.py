from __future__ import annotations

import json
from collections import defaultdict
from .identity import IdentityGraph, read_csv
from .intent import classify
from .policy import Policy
from .types import step_key, validate_steps, timestamp


class Auditor:
    def __init__(self, dataset, corpus, gemini=None):
        self.corpus=corpus
        self.identities=IdentityGraph(read_csv(dataset/'user_identities.csv'),read_csv(dataset/'user_audit_log.csv'))
        self.policy=Policy(dataset/'deletion_rules.csv')
        self.gemini=gemini
        self.intent_cache={}
        self.diagnostics=[]
        self.known_evidence={m['file_id'] for m in corpus.manifest}|{a['activity_id'] for a in corpus.activities}
        self.known_evidence|={r['audit_id'] for r in read_csv(dataset/'user_audit_log.csv')}

    def retrieve(self,subject,cutoff):
        keys=set()
        for ident in subject.identifiers:
            for key in self.corpus.by_identifier.get(ident,()):
                if any(o.available(cutoff) and ident in o.identifiers for o in self.corpus.by_resource[key]):
                    keys.add(key)
        for resource,identifiers,time,proof in self.corpus.catalog_links:
            if timestamp(time)<=timestamp(cutoff) and identifiers & subject.identifiers:
                keys.update(k for k in self.corpus.by_resource if k[1]==resource)
        return {key:[o for o in self.corpus.by_resource[key] if o.available(cutoff)] for key in sorted(keys)}

    @staticmethod
    def latest(observations):
        # Recency first; at identical observation times an actual remaining copy
        # beats a clear primary. File order/IDs do not influence semantic state.
        rank={'sqlite':4,'json':4,'gemini-vision':4,'pdf-text':4,'text':3,'log-readback':3,'csv':4}
        selected=max(observations,key=lambda o:(timestamp(o.event_time),o.state in {'PRESENT','ACTIVE'},
                   rank.get(o.method,0),timestamp(o.captured_at),o.evidence_id))
        # A later primary lookup cannot erase a proven replica copy. Keep a
        # separate timeline for each explicitly named replica table.
        replicas=defaultdict(list)
        for o in observations:
            if o.method=='sqlite' and 'replica' in o.location:replicas[o.location].append(o)
        for scope,history in replicas.items():
            replica=max(history,key=lambda o:timestamp(o.event_time))
            if replica.state in {'PRESENT','ACTIVE'} and selected.state not in {'PRESENT','ACTIVE'}:
                selected=replica
        return selected

    def predict(self,request):
        cutoff=request['audit_at']
        intent=self.intent_cache.get(request['request_text']) or classify(request['request_text'],self.gemini)
        diagnostic={'case_id':request['case_id'],'intent':intent.model_dump(),'gaps':[], 'resources':[]}
        self.diagnostics.append(diagnostic)
        if intent.intent!='DELETE_REQUEST':
            if intent.intent=='AMBIGUOUS_REQUEST':diagnostic['gaps'].append('Deletion authorization ambiguous; no destructive plan authorized')
            return {'case_id':request['case_id'],'deletion_status':'NOT_APPLICABLE','steps_json':'[]'}
        try:subject=self.identities.resolve(request['email'],cutoff)
        except ValueError as exc:
            diagnostic['gaps'].append(str(exc))
            return {'case_id':request['case_id'],'deletion_status':'INCOMPLETE','steps_json':'[]'}
        diagnostic['user_id']=subject.user_id
        resources=self.retrieve(subject,cutoff)
        desired=[];violations=[]
        for key,observations in resources.items():
            if not observations:continue
            obs=self.latest(observations)
            try:remedy,state,verify,finding=self.policy.required(obs,cutoff)
            except ValueError as exc:
                diagnostic['gaps'].append(f'{key}: {exc}');continue
            diagnostic['resources'].append({'system_id':key[0],'resource_id':key[1],'state':obs.state,
                'category':obs.category,'evidence_id':obs.evidence_id,'event_time':obs.event_time,
                'captured_at':obs.captured_at,'required_state':state,'observations':len(observations)})
            desired.append((obs,verify,state))
            compliant=obs.state==state
            # A removed non-retained record does not expose personal information.
            if obs.state=='ABSENT' and remedy in {'REDACT_RECORD','ANONYMIZE_RECORD'} and obs.category!='ACCOUNT_TOMBSTONE':
                compliant=True
                desired[-1]=(obs,'VERIFY_RECORD_ABSENT','ABSENT')
            if not compliant:
                if not remedy or not finding:
                    diagnostic['gaps'].append('Required retained record missing: '+obs.resource_id)
                    continue
                violations.append((obs,remedy,state,finding))
        if not desired:diagnostic['gaps'].append('No grounded resource state available by audit cutoff')
        elif 'account' in request['request_text'].casefold() and not any(
                o.category in {'USER_PROFILE','ACCOUNT_TOMBSTONE'} for o,_,_ in desired):
            diagnostic['gaps'].append('Account deletion audit lacks a grounded profile or tombstone state')
        if self.corpus.errors:diagnostic['gaps'].append('Evidence coverage incomplete; inspect ingestion report')
        status='INCOMPLETE' if violations or diagnostic['gaps'] else 'COMPLETE'
        steps=[]
        def add(obs,phase,op,state,evidence):
            steps.append(dict(step_no=1,phase=phase,system_id=obs.system_id,resource_id=obs.resource_id,
                              operation=op,state=state,evidence_id=evidence))
        for obs,remedy,state,finding in violations:
            add(obs,'FINDING',finding,'ACTIVE' if obs.category in {'DATA_FLOW','BACKUP_ARCHIVE'} else 'PRESENT',obs.evidence_id)
            add(obs,'REMEDIATION',remedy,state,'')
        for obs,verify,state in desired:
            add(obs,'VERIFICATION',verify,state,obs.evidence_id if status=='COMPLETE' else '')
        steps.sort(key=step_key)
        for i,step in enumerate(steps,1):step['step_no']=i
        validate_steps(status,steps,self.known_evidence)
        # Provenance validation includes actual resource/state and temporal cutoff.
        for s in steps:
            if not s['evidence_id']:continue
            matches=[o for o in self.corpus.by_resource[(s['system_id'],s['resource_id'])]
                     if o.evidence_id==s['evidence_id'] and o.available(cutoff)]
            if not matches:raise ValueError('Ungrounded or future citation')
            if s['phase']=='VERIFICATION' and not any(o.state==s['state'] for o in matches):
                raise ValueError('Evidence does not prove asserted verification state')
        return {'case_id':request['case_id'],'deletion_status':status,
                'steps_json':json.dumps(steps,ensure_ascii=False,separators=(',',':'))}
