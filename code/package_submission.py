"""Build a dataset/cache/credential-free allowlisted code archive and validate it."""
from pathlib import Path
import json
import csv
import zipfile
from ghosttrace.types import validate_steps
from ghosttrace.identity import read_csv

ROOT=Path(__file__).resolve().parents[1]


def main():
    required=['README.md','ARCHITECTURE.md','requirements.txt','code/evaluation/evaluation_report.md','code/evaluation/usage_report.md']
    for name in required:
        if not (ROOT/name).is_file():raise FileNotFoundError(name)
    rows=read_csv(ROOT/'output.csv')
    requests=read_csv(ROOT/'dataset/deletion_requests.csv')
    if list(rows[0])!=['case_id','deletion_status','steps_json']:raise ValueError('Wrong CSV header')
    ids=[r['case_id'] for r in rows]
    if len(ids)!=518 or len(set(ids))!=518 or ids!=sorted(r['case_id'] for r in requests):
        raise ValueError('Wrong output case coverage/order')
    evidence={r['file_id'] for r in read_csv(ROOT/'dataset/evidence_files.csv')}
    evidence|={r['activity_id'] for r in read_csv(ROOT/'dataset/system_activity.csv')}
    evidence|={r['audit_id'] for r in read_csv(ROOT/'dataset/user_audit_log.csv')}
    for row in rows:validate_steps(row['deletion_status'],json.loads(row['steps_json']),evidence)
    files=[ROOT/name for name in ['README.md','ARCHITECTURE.md','requirements.txt','.env.example']]
    import shutil
    (ROOT/'evaluation').mkdir(exist_ok=True)
    for name in ['evaluation_report.md','usage_report.md']:
        shutil.copyfile(ROOT/'code/evaluation'/name,ROOT/'evaluation'/name)
    for folder in ['code','tests']:
        files += [p for p in (ROOT/folder).rglob('*') if p.is_file() and p.suffix in {'.py','.md','.ps1'} and '__pycache__' not in p.parts]
    # Compare with the actual local credential without printing it or storing it.
    from dotenv import dotenv_values
    secret=dotenv_values(ROOT/'.env').get('GEMINI_API_KEY','')
    for p in files:
        if secret and secret.encode() in p.read_bytes():raise ValueError('Credential found in package candidate')
    tmp=ROOT/'code.zip.tmp'
    with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as archive:
        for p in sorted(files):archive.write(p,p.relative_to(ROOT).as_posix())
        for name in ['evaluation_report.md','usage_report.md']:
            archive.write(ROOT/'code/evaluation'/name,'evaluation/'+name)
    with zipfile.ZipFile(tmp) as archive:
        if archive.testzip():raise ValueError('Archive integrity failed')
        names=archive.namelist()
        if any(n.startswith(('dataset/','.cache/','.deps/','.venv/')) or n.endswith(('.zip','.env','.jsonl','.sql')) for n in names):
            raise ValueError('Forbidden archive content')
    tmp.replace(ROOT/'code.zip')
    print(f'Packaged {len(names)} allowlisted files; validated 518 output rows.')


if __name__=='__main__':main()
