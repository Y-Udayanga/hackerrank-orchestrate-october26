from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import csv
import hashlib
import re
import unicodedata
from pathlib import Path
from .types import timestamp


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def normalize(value: str) -> str:
    return unicodedata.normalize('NFKC', str(value)).strip().casefold()


def tokens(value) -> set[str]:
    """Exact strong identifiers; names are intentionally never a join key."""
    if isinstance(value, dict):
        return set().union(*(tokens(v) for v in value.values())) if value else set()
    if isinstance(value, (list, tuple)):
        return set().union(*(tokens(v) for v in value)) if value else set()
    if not isinstance(value, str):
        return set()
    result = set(re.findall(r'[\w.+-]+@[\w.-]+\.[\w-]+|\buser_[\w-]+\b|\b[a-fA-F0-9]{64}\b', value))
    if value.strip().startswith('+') and len(re.sub(r'\D', '', value)) >= 8:
        result.add('+' + re.sub(r'\D', '', value))
    return {normalize(v).rstrip('.,;') for v in result}


@dataclass
class Subject:
    user_id: str
    identifiers: set[str]
    provenance: dict[str, list[str]]


class IdentityGraph:
    def __init__(self, snapshots: list[dict], changes: list[dict]):
        self.snapshots = {r['user_id']: r for r in snapshots}
        self.changes = defaultdict(list)
        self.email_candidates = defaultdict(set)
        for row in snapshots:self.email_candidates[normalize(row['email'])].add(row['user_id'])
        for r in sorted(changes, key=lambda r: timestamp(r['event_time'])):
            self.changes[r['user_id']].append(r)
            if r['field_name']=='email':
                for value in (r['old_value'],r['new_value']):self.email_candidates[normalize(value)].add(r['user_id'])

    def subject(self, user_id: str, cutoff: str) -> Subject:
        snapshot = dict(self.snapshots[user_id])
        changes = self.changes[user_id]
        # Reconstruct current-at-cutoff fields before adding historic aliases.
        for change in reversed(changes):
            if timestamp(change['event_time']) > timestamp(cutoff):
                snapshot[change['field_name']] = change['old_value']
        ids = {normalize(user_id)}
        provenance = {normalize(user_id): ['user_identities.csv']}
        for key in ('email', 'phone', 'email_hash'):
            for token in tokens(snapshot.get(key, '')):
                ids.add(token)
                provenance[token] = ['user_identities.csv']
        for change in changes:
            if timestamp(change['event_time']) <= timestamp(cutoff):
                for token in tokens([change['old_value'], change['new_value']]):
                    ids.add(token)
                    provenance.setdefault(token, []).append(change['audit_id'])
        for email in list(ids):
            if '@' in email:
                digest = hashlib.sha256(email.encode()).hexdigest()
                ids.add(digest)
                provenance[digest] = ['sha256(normalized email)']
        return Subject(user_id, ids, provenance)

    def resolve(self, email: str, cutoff: str) -> Subject:
        value = normalize(email)
        matches = [s for user in self.email_candidates.get(value,()) if value in (s := self.subject(user, cutoff)).identifiers]
        if len(matches) != 1:
            raise ValueError(f'Identity resolution requires one exact owner; found {len(matches)}')
        return matches[0]
