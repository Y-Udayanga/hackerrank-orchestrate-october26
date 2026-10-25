from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


def timestamp(value: str) -> datetime:
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('Timezone required')
    return result.astimezone(timezone.utc)


class Observation(BaseModel):
    model_config = ConfigDict(extra='forbid')
    evidence_id: str
    source: str
    location: str
    system_id: str
    resource_id: str
    category: str
    state: str
    event_time: str
    captured_at: str
    identifiers: list[str] = Field(default_factory=list)
    fields: dict[str, Any] = Field(default_factory=dict)
    method: str
    confidence: float = 1.0

    def available(self, cutoff: str) -> bool:
        return max(timestamp(self.event_time), timestamp(self.captured_at)) <= timestamp(cutoff)


class Intent(BaseModel):
    model_config = ConfigDict(extra='forbid')
    intent: Literal['DELETE_REQUEST', 'NON_DELETION_REQUEST', 'AMBIGUOUS_REQUEST']
    quote: str
    reason: str


class IntentItem(Intent):
    request_index: int


class IntentBatch(BaseModel):
    model_config = ConfigDict(extra='forbid')
    requests: list[IntentItem]


class VisualRecord(BaseModel):
    model_config = ConfigDict(extra='forbid')
    system_id: str
    resource_id: str = Field(pattern=r'^[a-z][a-z_]*_[0-9]+$')
    category: str
    state: Literal['PRESENT', 'ABSENT', 'REDACTED', 'ANONYMIZED', 'ACTIVE', 'DISABLED', 'BLOCKED']
    identifiers: list[str]
    supporting_text: str


class VisualExtraction(BaseModel):
    model_config = ConfigDict(extra='forbid')
    records: list[VisualRecord]
    uncertainty: str


OPERATIONS = {
    'FINDING': [('REPORT_REMAINING_RECORD', 'PRESENT'), ('REPORT_EXPOSED_PII', 'PRESENT'),
                ('REPORT_ACTIVE_DATA_FLOW', 'ACTIVE'), ('REPORT_RESTORE_RISK', 'ACTIVE')],
    'REMEDIATION': [('DISABLE_DATA_FLOW', 'DISABLED'), ('BLOCK_RESTORE', 'BLOCKED'),
                    ('DELETE_RECORD', 'ABSENT'), ('REDACT_RECORD', 'REDACTED'), ('ANONYMIZE_RECORD', 'ANONYMIZED')],
    'VERIFICATION': [('VERIFY_RECORD_ABSENT', 'ABSENT'), ('VERIFY_RECORD_PRESENT', 'PRESENT'),
                     ('VERIFY_RECORD_REDACTED', 'REDACTED'), ('VERIFY_RECORD_ANONYMIZED', 'ANONYMIZED'),
                     ('VERIFY_DATA_FLOW_DISABLED', 'DISABLED'), ('VERIFY_RESTORE_BLOCKED', 'BLOCKED')],
}


class Step(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    step_no: int = Field(ge=1)
    phase: Literal['FINDING', 'REMEDIATION', 'VERIFICATION']
    system_id: str = Field(min_length=1)
    resource_id: str = Field(min_length=1)
    operation: str
    state: str
    evidence_id: str


def step_key(step: dict) -> tuple:
    phase = step['phase']
    return (list(OPERATIONS).index(phase), [o for o, _ in OPERATIONS[phase]].index(step['operation']),
            step['system_id'], step['resource_id'])


def validate_steps(status: str, steps: list[dict], known_evidence: set[str]) -> None:
    if status not in {'COMPLETE', 'INCOMPLETE', 'NOT_APPLICABLE'}:
        raise ValueError('Invalid status')
    if status == 'NOT_APPLICABLE' and steps:
        raise ValueError('Unauthorized steps')
    seen = set()
    for n, raw in enumerate(steps, 1):
        s = Step.model_validate(raw)
        if s.step_no != n or (s.operation, s.state) not in OPERATIONS[s.phase]:
            raise ValueError('Invalid step numbering or operation/state')
        key = (s.phase, s.system_id, s.resource_id, s.operation)
        if key in seen:
            raise ValueError('Duplicate step')
        seen.add(key)
        if status == 'COMPLETE' and s.phase != 'VERIFICATION':
            raise ValueError('Complete cases may only verify')
        proof = status == 'COMPLETE' or s.phase == 'FINDING'
        if proof and s.evidence_id not in known_evidence:
            raise ValueError('Missing evidence')
        if not proof and s.evidence_id:
            raise ValueError('Future work must not cite evidence')
    if steps != sorted(steps, key=step_key):
        raise ValueError('Incorrect phase/operation order')
    if status == 'COMPLETE' and not steps:
        raise ValueError('Completion requires proof')
    if status == 'INCOMPLETE':
        pairs={'REPORT_REMAINING_RECORD':('DELETE_RECORD','VERIFY_RECORD_ABSENT'),
               'REPORT_EXPOSED_PII':(('REDACT_RECORD','VERIFY_RECORD_REDACTED'),('ANONYMIZE_RECORD','VERIFY_RECORD_ANONYMIZED')),
               'REPORT_ACTIVE_DATA_FLOW':('DISABLE_DATA_FLOW','VERIFY_DATA_FLOW_DISABLED'),
               'REPORT_RESTORE_RISK':('BLOCK_RESTORE','VERIFY_RESTORE_BLOCKED')}
        for s in steps:
            if s['phase']=='FINDING':
                options=pairs[s['operation']]
                if isinstance(options[0],str):options=(options,)
                if not any(('REMEDIATION',s['system_id'],s['resource_id'],r) in seen and
                           ('VERIFICATION',s['system_id'],s['resource_id'],v) in seen for r,v in options):
                    raise ValueError('Finding lacks required remediation and verification')
