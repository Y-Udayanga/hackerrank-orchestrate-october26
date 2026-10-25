# Public sample evaluation

This is public-sample measurement, not a prediction of hidden leaderboard score.
No reference answer is accessible from the inference modules.

Unordered semantic steps match all six non-number fields exactly, using multiset
intersection; precision=TP/(TP+FP), recall=TP/(TP+FN), F1 is their harmonic mean.
Ordered sequence accuracy requires the entire JSON array, including step numbers,
to match. Ordering-only errors have equal semantic multisets but unequal arrays.
Field accuracy aligns expected steps by phase/system/resource/operation; missing
matches score zero. Extra steps are penalized in precision, not field denominators.

## Measured results

- cases: 32
- status_correct: 29
- status_accuracy: 0.90625
- exact_sequences: 8
- sequence_accuracy: 0.25
- ordering_only_errors: 0
- step_tp: 158
- step_fp: 1
- step_fn: 35
- step_precision: 0.9937106918238994
- step_recall: 0.8186528497409327
- step_f1: 0.8977272727272727
- fields: {"phase": 0.8186528497409327, "system_id": 0.8186528497409327, "resource_id": 0.8186528497409327, "operation": 0.8186528497409327, "state": 0.8186528497409327, "evidence_id": 0.8186528497409327, "step_no": 0.5906735751295337}
- confusion: {"COMPLETE -> INCOMPLETE": 3, "COMPLETE -> COMPLETE": 7, "INCOMPLETE -> INCOMPLETE": 22}
- operations: {"missing VERIFY_RECORD_ABSENT": 21, "missing VERIFY_RECORD_ANONYMIZED": 7, "missing VERIFY_RECORD_PRESENT": 7, "extra VERIFY_RECORD_ABSENT": 1}
- format_invalid: []

## Every sample failure

### case_01: expected COMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_001",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_54"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: ["No grounded resource state available by audit cutoff"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_02: expected COMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_002",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_54"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: ["No grounded resource state available by audit cutoff"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_03: expected COMPLETE, predicted COMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_9406",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_94"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_04: expected COMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_004",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_54"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_901",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_56"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: ["No grounded resource state available by audit cutoff"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_06: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_006",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_07: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_007",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_08: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_008",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_09: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_3960",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_4902",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_10: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_010",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_17: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[]
```
Extra/incorrect steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_6523",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  }
]
```
Investigation gaps: []

### case_18: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_5521",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_6645",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_20: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_5037",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_5569",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_21: expected COMPLETE, predicted COMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_6440",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_5335",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_92"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_22: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_4990",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_23: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_410",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_4128",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_24: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_7095",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_25: expected COMPLETE, predicted COMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_3136",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_1895",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_92"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_26: expected COMPLETE, predicted COMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_5684",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_4566",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_92"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_27: expected COMPLETE, predicted COMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_3866",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_4574",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_92"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_28: expected COMPLETE, predicted COMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_5482",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_6077",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_92"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_29: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_7012",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_3954",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_30: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_4163",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_1707",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_31: expected COMPLETE, predicted COMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_4857",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_51"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_32: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_8858",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.


## Independent manually reasoned evaluation cases

These synthetic fixtures are generated under pytest temporary directories and never
inserted into the challenge dataset. Expected decisions are authored independently
of the public answers. See tests/test_auditor.py for executable evidence and assertions.

| Scenario | Expected reasoning/result |
|---|---|
| Data access request | NOT_APPLICABLE, no steps |
| Explicit do-not-delete | NOT_APPLICABLE, no steps |
| Profile remains | INCOMPLETE, finding/delete/verify absent |
| Profile absent; security retained | COMPLETE, verify absent and present |
| Historical email | Old exact address resolves to same stable subject |
| Recreation with active sync | INCOMPLETE; disable flow before delete |
| Old screenshot, newer absence | COMPLETE using newer direct evidence |
| Capture after cutoff | Ignore later capture; existing violation remains |
| Event after cutoff | Ignore later event even with inconsistent earlier capture |
| Active restore access | Report risk, block restore, verify blocked |
| Tombstone exposes email | Redact; do not delete stable internal reference |
| Clean tombstone | COMPLETE, verify redacted |
| Primary absent, replica present | INCOMPLETE; replica presence defeats absence |
| Unrelated customer attachment | Excluded from subject plan |
| Missing/corrupt evidence | Strict ingestion fails visibly |
| Identical names | Name does not join resources |
| Future identity association | Cannot link an earlier anonymous resource |
| No evidence | INCOMPLETE with explicit investigation gap |
| Debug cache miss | Not proof of profile absence; completed lookup required |
| SQL attachment attempt | Denied by SQLite authorizer |
| SQL nested JSON | Parsed into typed observed state |
| Future email change | New email cannot resolve a past subject |
| Quoted deletion phrase | Not deletion authorization |
