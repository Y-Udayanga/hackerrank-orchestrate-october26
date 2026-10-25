"""Evaluation only: never imported by inference modules."""
from collections import Counter
import json

FIELDS=['phase','system_id','resource_id','operation','state','evidence_id','step_no']


def semantic(step):
    return tuple(step[f] for f in FIELDS if f!='step_no')


def evaluate(predictions,references):
    predicted={r['case_id']:r for r in predictions}
    expected={r['case_id']:r for r in references}
    if len(predicted)!=len(predictions) or set(predicted)!=set(expected):raise ValueError('Evaluation case coverage differs')
    confusion=Counter();correct=exact=ordering=tp=fp=fn=0
    field_correct=Counter();field_total=0;failures=[]
    operation_counts=Counter()
    for case in sorted(expected):
        p,e=predicted[case],expected[case]
        ps,es=json.loads(p['steps_json']),json.loads(e['steps_json'])
        pc,ec=Counter(map(semantic,ps)),Counter(map(semantic,es))
        common=pc&ec;extra=pc-ec;missing=ec-pc
        tp+=sum(common.values());fp+=sum(extra.values());fn+=sum(missing.values())
        confusion[(e['deletion_status'],p['deletion_status'])]+=1
        correct+=int(e['deletion_status']==p['deletion_status'])
        exact+=int(ps==es)
        ordering+=int(pc==ec and ps!=es)
        # Field accuracy aligns by semantic resource/operation identity, not array
        # position (so one extra early step does not cascade across every field).
        index={(s['phase'],s['system_id'],s['resource_id'],s['operation']):s for s in ps}
        for s in es:
            match=index.get((s['phase'],s['system_id'],s['resource_id'],s['operation']),{})
            field_total+=1
            for f in FIELDS:field_correct[f]+=int(match.get(f)==s[f])
        for step,n in missing.items():operation_counts['missing '+step[3]]+=n
        for step,n in extra.items():operation_counts['extra '+step[3]]+=n
        if ps!=es or p['deletion_status']!=e['deletion_status']:
            failures.append(dict(case_id=case,expected=e['deletion_status'],predicted=p['deletion_status'],
                missing=[dict(zip(FIELDS[:-1],s)) for s in missing.elements()],
                extra=[dict(zip(FIELDS[:-1],s)) for s in extra.elements()],ordering_only=pc==ec and ps!=es))
    precision=tp/(tp+fp) if tp+fp else 0
    recall=tp/(tp+fn) if tp+fn else 0
    return dict(cases=len(expected),status_correct=correct,status_accuracy=correct/len(expected),
        exact_sequences=exact,sequence_accuracy=exact/len(expected),ordering_only_errors=ordering,
        step_tp=tp,step_fp=fp,step_fn=fn,step_precision=precision,step_recall=recall,
        step_f1=2*precision*recall/(precision+recall) if precision+recall else 0,
        fields={f:field_correct[f]/field_total if field_total else 1 for f in FIELDS},
        confusion={f'{a} -> {b}':n for (a,b),n in confusion.items()},
        operations=dict(operation_counts),failures=failures)
