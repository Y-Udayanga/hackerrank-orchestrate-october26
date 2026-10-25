"""Run AFTER closing the relevant Codex session; never copy auth/config files."""
import argparse
import json
import re
import zipfile
from pathlib import Path
from dotenv import dotenv_values

ROOT=Path(__file__).resolve().parents[1]


def redact(value,secrets):
    if isinstance(value,dict):return {k:('[REDACTED]' if re.search(r'^(api_key|access_token|password|authorization)$',k,re.I) else redact(v,secrets)) for k,v in value.items()}
    if isinstance(value,list):return [redact(v,secrets) for v in value]
    if not isinstance(value,str):return value
    for secret in secrets:
        if secret:value=value.replace(secret,'[REDACTED]')
    value=re.sub(r'AIza[\w-]{20,}','[REDACTED]',value)
    value=re.sub(r'(?im)(Gemini API\s*=\s*)[^\r\n]+',r'\1[REDACTED]',value)
    return value


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('rollout',type=Path,nargs='+',help='Only rollout JSONL files for this challenge')
    p.add_argument('--session-closed',action='store_true',required=True,help='Confirm relevant app/CLI sessions have ended')
    args=p.parse_args()
    secrets=[v for k,v in dotenv_values(ROOT/'.env').items() if re.search('KEY|TOKEN|SECRET|PASSWORD',k)]
    target=ROOT/'agent-trace/codex';target.mkdir(parents=True,exist_ok=True)
    for source in args.rollout:
        if source.suffix!='.jsonl' or not source.name.startswith('rollout-'):raise ValueError('Expected a Codex rollout JSONL')
        dest=target/source.name
        if dest.exists():raise FileExistsError('Do not overwrite a staged trace')
        with source.open(encoding='utf-8') as inp,dest.open('w',encoding='utf-8',newline='\n') as out:
            for line in inp:
                out.write(json.dumps(redact(json.loads(line),secrets),ensure_ascii=False)+'\n')
    with zipfile.ZipFile(ROOT/'agent-trace.zip','w',zipfile.ZIP_DEFLATED) as z:
        for file in target.glob('rollout-*.jsonl'):z.write(file,file.relative_to(ROOT))
    print('Trace staged and archived. Review for unrelated/private information before upload.')


if __name__=='__main__':main()
