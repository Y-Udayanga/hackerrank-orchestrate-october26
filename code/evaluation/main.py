"""Run public reference evaluation independently from prediction."""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ghosttrace.identity import read_csv
from ghosttrace.identity import IdentityGraph
from ghosttrace.types import timestamp
from ghosttrace.types import validate_steps
from metrics import evaluate

ROOT=Path(__file__).resolve().parents[2]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--predictions',type=Path,default=ROOT/'.cache/sample_output.csv')
    parser.add_argument('--label',default='current')
    args=parser.parse_args()
    predictions=read_csv(args.predictions)
    reference=read_csv(ROOT/'dataset/sample_output.csv')
    results=evaluate(predictions,reference)
    known={r['file_id'] for r in read_csv(ROOT/'dataset/evidence_files.csv')}
    known|={r['activity_id'] for r in read_csv(ROOT/'dataset/system_activity.csv')}
    known|={r['audit_id'] for r in read_csv(ROOT/'dataset/user_audit_log.csv')}
    invalid=[]
    for row in predictions:
        try:validate_steps(row['deletion_status'],json.loads(row['steps_json']),known)
        except ValueError as e:invalid.append(row['case_id']+': '+str(e))
    results['format_invalid']=invalid
    diagnostics_path=ROOT/'.cache/run/diagnostics.json'
    diagnostics={r['case_id']:r for r in json.loads(diagnostics_path.read_text(encoding='utf-8'))} if diagnostics_path.exists() else {}
    ledger_path=ROOT/'.cache/run/ledger.json'
    ledger=json.loads(ledger_path.read_text(encoding='utf-8')) if ledger_path.exists() else []
    requests={r['case_id']:r for r in read_csv(ROOT/'dataset/sample_deletion_requests.csv')}
    identities=IdentityGraph(read_csv(ROOT/'dataset/user_identities.csv'),read_csv(ROOT/'dataset/user_audit_log.csv'))
    report='''# Public sample evaluation

This is public-sample measurement, not a prediction of hidden leaderboard score.
No reference answer is accessible from the inference modules.

Unordered semantic steps match all six non-number fields exactly, using multiset
intersection; precision=TP/(TP+FP), recall=TP/(TP+FN), F1 is their harmonic mean.
Ordered sequence accuracy requires the entire JSON array, including step numbers,
to match. Ordering-only errors have equal semantic multisets but unequal arrays.
Field accuracy aligns expected steps by phase/system/resource/operation; missing
matches score zero. Extra steps are penalized in precision, not field denominators.

## Measured results

'''
    for k,v in results.items():
        if k!='failures':report+=f'- {k}: {json.dumps(v,ensure_ascii=False)}\n'
    report+='\n## Every sample failure\n\n'
    for failure in results['failures']:
        diagnostic=diagnostics.get(failure['case_id'],{})
        report+=f"### {failure['case_id']}: expected {failure['expected']}, predicted {failure['predicted']}\n\n"
        report+='Missing steps:\n```json\n'+json.dumps(failure['missing'],indent=2)+'\n```\n'
        report+='Extra/incorrect steps:\n```json\n'+json.dumps(failure['extra'],indent=2)+'\n```\n'
        report+='Investigation gaps: '+json.dumps(diagnostic.get('gaps',[]))+'\n\n'
        missing_keys={(s['system_id'],s['resource_id'],s['operation']) for s in failure['missing']}
        extra_keys={(s['system_id'],s['resource_id'],s['operation']) for s in failure['extra']}
        if missing_keys & extra_keys:report+='Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.\n\n'
        elif failure['missing']:report+='Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.\n\n'
        if failure['ordering_only']:report+='Diagnosis: ordering/step numbering differs.\n\n'
        report+='Resource-level root-cause investigation:\n\n'
        investigated=set()
        for step in failure['missing']:
            key=(step['system_id'],step['resource_id'])
            if key in investigated:continue
            investigated.add(key)
            request=requests[failure['case_id']]
            observations=[o for o in ledger if (o['system_id'],o['resource_id'])==key]
            eligible=[o for o in observations if max(timestamp(o['event_time']),timestamp(o['captured_at']))<=timestamp(request['audit_at'])]
            try:subject=identities.resolve(request['email'],request['audit_at'])
            except ValueError:subject=None
            linked=bool(subject and any(set(o['identifiers']) & subject.identifiers for o in eligible))
            if not observations:reason='No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.'
            elif not eligible:reason='Available observations were captured or occurred after this audit cutoff; using them would leak future information.'
            elif not linked:reason='Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.'
            else:reason='Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.'
            report+=f'- {key[0]} / {key[1]}: {reason}\n'
        report+='\n'
    custom=ROOT/'code/evaluation/custom_cases.md'
    if custom.exists():report+='\n'+custom.read_text(encoding='utf-8')
    improvements=ROOT/'code/evaluation/improvements.md'
    if improvements.exists():report+='\n'+improvements.read_text(encoding='utf-8')
    (ROOT/'code/evaluation/evaluation_report.md').write_text(report,encoding='utf-8')
    history=ROOT/'code/evaluation/history.md'
    with history.open('a',encoding='utf-8') as f:
        f.write(f"\n## {datetime.now(timezone.utc).isoformat()} — {args.label}\n\n"+
                json.dumps({k:v for k,v in results.items() if k!='failures'},ensure_ascii=False)+'\n')
    print(f"Status {results['status_correct']}/{results['cases']} ({results['status_accuracy']:.1%}); "
          f"step P/R/F1 {results['step_precision']:.1%}/{results['step_recall']:.1%}/{results['step_f1']:.1%}; "
          f"exact sequences {results['exact_sequences']}/{results['cases']}; invalid rows {len(invalid)}")


if __name__=='__main__':main()
