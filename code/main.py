"""Terminal entry point; evidence is read-only, output is an audit plan."""
from __future__ import annotations
import argparse
import csv
import json
import logging
import os
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if (ROOT/'.deps').is_dir():sys.path.insert(0,str(ROOT/'.deps'))
from dotenv import load_dotenv
from ghosttrace.identity import read_csv
from ghosttrace.ingest import Corpus
from ghosttrace.engine import Auditor


def write_output(path,rows,expected_ids):
    rows=sorted(rows,key=lambda r:r['case_id'])
    ids=[r['case_id'] for r in rows]
    if len(ids)!=len(set(ids)) or set(ids)!=set(expected_ids):raise ValueError('Output case coverage invalid')
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix('.tmp')
    with tmp.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=['case_id','deletion_status','steps_json'])
        writer.writeheader();writer.writerows(rows)
    tmp.replace(path)


def usage_report(path,gemini,count,mode,errors):
    usage=gemini.usage if gemini else dict(provider='None (offline)',model='None',calls=0,failed_calls=0,
        input_tokens=0,output_tokens=0,thinking_tokens=0,cached_input_tokens=0,cache_hits=0,discovery_calls=0)
    total=usage['input_tokens']+usage['output_tokens']+usage['thinking_tokens']
    cost=gemini.cost() if gemini else 0.0
    price='Unknown: configure verified model prices; no fabricated estimate.' if cost is None else f'USD {cost:.8f}; USD {cost/max(1,count):.8f} per request'
    report=f'''# Final run usage report

Mode: {mode}. Requests: {count}. Evidence ingestion failures: {errors}.

| Metric | Actual value |
|---|---:|
'''+''.join(f'| {k} | {v} |\n' for k,v in usage.items())+f'''
Total generated/request tokens including reported thinking: {total}.
Average per request: {total/max(1,count):.3f}.
Estimated total and per-request cost: {price}

Price source: https://ai.google.dev/gemini-api/docs/pricing (verified 2026-10-25).
The standard text/image rates used for Gemini 3.1 Flash-Lite are USD 0.25 input
and USD 1.50 output (including thinking) per million tokens. Gemini 3.8 Flash
introductory rates expire 2026-12-31; reverify them for later runs.

One provider/model only; the table also represents overall totals. Cache hits make
no model call and incur no new tokens. Discovery is separately counted. Failed
calls with no usage metadata have unknown provider-side token usage; recorded
tokens are the actual returned metadata, not estimates of unreported usage.
Inference is serial (concurrency 1), with bounded retry and per-call timeout.
Thinking tokens are reported separately and included once in total and output cost.
Development model usage is not available through this application and is excluded.
'''
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(report,encoding='utf-8')


def main():
    parser=argparse.ArgumentParser(description='GhostTrace AI evidence-driven deletion auditor')
    parser.add_argument('--dataset',type=Path,default=ROOT/'dataset')
    parser.add_argument('--requests',default='deletion_requests.csv')
    parser.add_argument('--output',type=Path,default=ROOT/'output.csv')
    parser.add_argument('--offline',action='store_true',help='Explicit reduced capability, no Gemini calls')
    parser.add_argument('--allow-evidence-errors',action='store_true',help='Continue with reported coverage gaps')
    parser.add_argument('--list-models',action='store_true')
    parser.add_argument('--model',help='Override GEMINI_MODEL; still verified against API access')
    args=parser.parse_args()
    logging.basicConfig(level=logging.INFO,format='%(levelname)s %(message)s')
    load_dotenv(ROOT/'.env',override=False)
    if args.model:os.environ['GEMINI_MODEL']=args.model
    gemini=None
    if not args.offline:
        from ghosttrace.gemini import Gemini
        gemini=Gemini(ROOT/'.cache/gemini')
        logging.info('Verified Gemini model: %s',gemini.model)
        if args.list_models:
            print('\n'.join(gemini.available_models));return
    elif args.list_models:parser.error('--list-models requires API access')
    if args.offline:logging.warning('REDUCED CAPABILITY: offline intent; image evidence unavailable')
    requests=read_csv(args.dataset/args.requests)
    if args.requests=='deletion_requests.csv' and len(requests)!=518:raise ValueError('Expected 518 target requests')
    corpus=Corpus(args.dataset,gemini,strict=not args.allow_evidence_errors).load()
    logging.info('Indexed %d observations; %d evidence errors',len(corpus.observations),len(corpus.errors))
    auditor=Auditor(args.dataset,corpus,gemini)
    from ghosttrace.intent import classify_many
    auditor.intent_cache=classify_many(requests,gemini)
    rows=[]
    for i,request in enumerate(sorted(requests,key=lambda r:r['case_id']),1):
        rows.append(auditor.predict(request))
        if i%50==0:logging.info('Audited %d/%d requests',i,len(requests))
    write_output(args.output,rows,[r['case_id'] for r in requests])
    report_dir=ROOT/'code/evaluation'
    report_dir.mkdir(exist_ok=True)
    run_dir=ROOT/'.cache/run';run_dir.mkdir(parents=True,exist_ok=True)
    (run_dir/'diagnostics.json').write_text(json.dumps(auditor.diagnostics,ensure_ascii=False,indent=2),encoding='utf-8')
    (run_dir/'ledger.json').write_text(json.dumps([o.model_dump() for o in corpus.observations],ensure_ascii=False),encoding='utf-8')
    (report_dir/'ingestion_report.md').write_text('# Ingestion report\n\n'+f'{len(corpus.observations)} observations.\n\nErrors:\n'+
        '\n'.join('- '+json.dumps(e) for e in corpus.errors)+'\n\nNotes:\n'+'\n'.join('- '+n for n in corpus.notes),encoding='utf-8')
    if args.requests=='deletion_requests.csv':
        usage_report(report_dir/'usage_report.md',gemini,len(requests),'offline' if args.offline else 'Gemini hybrid',len(corpus.errors))
    logging.info('Wrote %d validated rows to %s',len(rows),args.output)


if __name__=='__main__':
    main()
