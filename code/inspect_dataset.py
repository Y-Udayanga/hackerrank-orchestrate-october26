"""Read-only schema inventory of participant-facing files, excluding reference data values."""
import csv
import json
import re
import sqlite3
from collections import Counter,defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def main():
    lines=['# Participant dataset inspection','', 'No organizer files inspected. Values below are schema/enums, not answer lookups.','']
    for path in sorted((ROOT/'dataset').glob('*.csv')):
        with path.open(encoding='utf-8-sig',newline='') as f:
            reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
        lines += [f'## {path.name}', '',f'Rows: {len(rows)}. Columns: {", ".join(fields)}.','', '| Column | Observed type | Missing | Values or range |','|---|---|---:|---|']
        for field in fields:
            values=[r[field] for r in rows if r[field]];unique=set(values)
            kind='string';detail=f'{len(unique)} distinct values'
            if values and all(re.fullmatch(r'\d{4}-\d\d-\d\dT.*Z',v) for v in values):kind='UTC timestamp';detail=f'{min(values)} to {max(values)}'
            elif field in {'reported_status','deletion_status','event_type','field_name','required_action','data_category','condition','source_system','target_system','origin'}:
                detail='; '.join(sorted(unique))
            elif field=='steps_json':kind='JSON array in CSV field'
            lines.append(f'| {field} | {kind} | {len(rows)-len(values)} | {detail} |')
        lines.append('')
    manifest=list(csv.DictReader((ROOT/'dataset/evidence_files.csv').open(encoding='utf-8')))
    lines+=['## Evidence manifest coverage','',str(dict(Counter(Path(r['file_path']).suffix for r in manifest))),'']
    for row in manifest:
        path=ROOT/'dataset'/row['file_path']
        lines += [f"### {row['file_id']}: {path.name}", '',f"Origin: {row['origin']}. Capture: {row['captured_at']}. Size: {path.stat().st_size} bytes.",'']
        if path.suffix=='.sql':
            db=sqlite3.connect(':memory:');db.executescript(path.read_text(encoding='utf-8'))
            for name,schema in db.execute("SELECT name,sql FROM sqlite_master WHERE type='table'"):
                escaped=name.replace('"','""')
                count=db.execute(f'SELECT COUNT(*) FROM "{escaped}"').fetchone()[0]
                lines += [f'{name}: {count} rows.','```sql',schema,'```','']
            db.close()
        elif path.suffix=='.json':
            patterns=defaultdict(Counter)
            def walk(obj,where='$'):
                if isinstance(obj,dict):
                    for key,value in obj.items():patterns[where][key]+=1;walk(value,where+'.'+key)
                elif isinstance(obj,list):
                    for value in obj:walk(value,where+'[]')
            walk(json.loads(path.read_text(encoding='utf-8')))
            for where,keys in patterns.items():lines.append(f'- {where}: '+', '.join(keys))
            lines.append('')
    lines+=['## Relationships and acceptance risks','',
        '- Stable user_id links identity changes; exact current/historic email, hashes and normalized phones link resources.',
        '- file_id cites a file, not a case; manifest origin never establishes ownership.',
        '- activity_id is a claim unless details provide an explicit identity relationship or direct observation.',
        '- resource IDs join snapshots; trace IDs join lookup starts to completions within a log.',
        '- Subject-free anonymized records and negative lookups need a separate grounded identity link.',
        '- Both event and capture timestamps must be within audit cutoff.',
        '- SQL snapshot_scope lists systems, not an explicit exhaustive set of subject resources; absence is not inferred from missing rows.',
        '- Output must have 518 unique string-sorted target cases; samples are evaluation only.']
    (ROOT/'code/evaluation/dataset_inspection.md').write_text('\n'.join(lines),encoding='utf-8')
    print('Wrote participant schema inventory')


if __name__=='__main__':main()
