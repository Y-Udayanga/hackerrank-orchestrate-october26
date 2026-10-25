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
- status_correct: 22
- status_accuracy: 0.6875
- exact_sequences: 8
- sequence_accuracy: 0.25
- ordering_only_errors: 0
- step_tp: 137
- step_fp: 15
- step_fn: 56
- step_precision: 0.9013157894736842
- step_recall: 0.7098445595854922
- step_f1: 0.7942028985507247
- fields: {"phase": 0.7823834196891192, "system_id": 0.7823834196891192, "resource_id": 0.7823834196891192, "operation": 0.7823834196891192, "state": 0.7823834196891192, "evidence_id": 0.7098445595854922, "step_no": 0.5803108808290155}
- confusion: {"COMPLETE -> INCOMPLETE": 8, "COMPLETE -> NOT_APPLICABLE": 2, "INCOMPLETE -> INCOMPLETE": 22}
- operations: {"missing VERIFY_RECORD_ABSENT": 23, "missing VERIFY_RECORD_PRESENT": 14, "missing VERIFY_RECORD_ANONYMIZED": 7, "extra VERIFY_RECORD_ABSENT": 2, "extra VERIFY_RECORD_PRESENT": 6, "missing REPORT_REMAINING_RECORD": 1, "missing DELETE_RECORD": 1, "missing VERIFY_RECORD_REDACTED": 4, "missing VERIFY_DATA_FLOW_DISABLED": 3, "missing VERIFY_RESTORE_BLOCKED": 3, "extra VERIFY_RECORD_REDACTED": 3, "extra VERIFY_DATA_FLOW_DISABLED": 2, "extra VERIFY_RESTORE_BLOCKED": 2}
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
Investigation gaps: ["No grounded resource state available by audit cutoff", "Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_02: expected COMPLETE, predicted NOT_APPLICABLE

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
Investigation gaps: []

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_03: expected COMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_7566",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": "evidence_94"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_2016",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": "evidence_94"
  },
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
[
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_7566",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_2016",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

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
Investigation gaps: ["No grounded resource state available by audit cutoff", "Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_10: expected INCOMPLETE, predicted INCOMPLETE

Missing steps:
```json
[
  {
    "phase": "FINDING",
    "system_id": "support_platform",
    "resource_id": "support_002",
    "operation": "REPORT_REMAINING_RECORD",
    "state": "PRESENT",
    "evidence_id": "evidence_61"
  },
  {
    "phase": "REMEDIATION",
    "system_id": "support_platform",
    "resource_id": "support_002",
    "operation": "DELETE_RECORD",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "account_service",
    "resource_id": "account_010",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "support_platform",
    "resource_id": "support_002",
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
Investigation gaps: ["No grounded resource state available by audit cutoff", "Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_21: expected COMPLETE, predicted INCOMPLETE

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
    "system_id": "security_service",
    "resource_id": "audit_record_3737",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
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
[
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_3737",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_25: expected COMPLETE, predicted INCOMPLETE

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
    "system_id": "security_service",
    "resource_id": "audit_record_451",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
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
[
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_451",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  }
]
```
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

### case_26: expected COMPLETE, predicted NOT_APPLICABLE

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
    "system_id": "security_service",
    "resource_id": "audit_record_5416",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "support_platform",
    "resource_id": "support_4715",
    "operation": "VERIFY_RECORD_REDACTED",
    "state": "REDACTED",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_4566",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "integration_service",
    "resource_id": "data_flow_6244",
    "operation": "VERIFY_DATA_FLOW_DISABLED",
    "state": "DISABLED",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "backup_service",
    "resource_id": "backup_3120",
    "operation": "VERIFY_RESTORE_BLOCKED",
    "state": "BLOCKED",
    "evidence_id": "evidence_92"
  }
]
```
Extra/incorrect steps:
```json
[]
```
Investigation gaps: ["Deletion authorization ambiguous; no destructive plan authorized"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_27: expected COMPLETE, predicted INCOMPLETE

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
    "system_id": "security_service",
    "resource_id": "audit_record_3830",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "support_platform",
    "resource_id": "support_4707",
    "operation": "VERIFY_RECORD_REDACTED",
    "state": "REDACTED",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_4574",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "integration_service",
    "resource_id": "data_flow_2295",
    "operation": "VERIFY_DATA_FLOW_DISABLED",
    "state": "DISABLED",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "backup_service",
    "resource_id": "backup_5970",
    "operation": "VERIFY_RESTORE_BLOCKED",
    "state": "BLOCKED",
    "evidence_id": "evidence_92"
  }
]
```
Extra/incorrect steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_3830",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "support_platform",
    "resource_id": "support_4707",
    "operation": "VERIFY_RECORD_REDACTED",
    "state": "REDACTED",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "integration_service",
    "resource_id": "data_flow_2295",
    "operation": "VERIFY_DATA_FLOW_DISABLED",
    "state": "DISABLED",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "backup_service",
    "resource_id": "backup_5970",
    "operation": "VERIFY_RESTORE_BLOCKED",
    "state": "BLOCKED",
    "evidence_id": ""
  }
]
```
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

### case_28: expected COMPLETE, predicted INCOMPLETE

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
    "system_id": "security_service",
    "resource_id": "audit_record_9265",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "support_platform",
    "resource_id": "support_2351",
    "operation": "VERIFY_RECORD_REDACTED",
    "state": "REDACTED",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "analytics_platform",
    "resource_id": "analytics_6077",
    "operation": "VERIFY_RECORD_ANONYMIZED",
    "state": "ANONYMIZED",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "integration_service",
    "resource_id": "data_flow_2337",
    "operation": "VERIFY_DATA_FLOW_DISABLED",
    "state": "DISABLED",
    "evidence_id": "evidence_92"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "backup_service",
    "resource_id": "backup_838",
    "operation": "VERIFY_RESTORE_BLOCKED",
    "state": "BLOCKED",
    "evidence_id": "evidence_92"
  }
]
```
Extra/incorrect steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_9265",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "support_platform",
    "resource_id": "support_2351",
    "operation": "VERIFY_RECORD_REDACTED",
    "state": "REDACTED",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "integration_service",
    "resource_id": "data_flow_2337",
    "operation": "VERIFY_DATA_FLOW_DISABLED",
    "state": "DISABLED",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "backup_service",
    "resource_id": "backup_838",
    "operation": "VERIFY_RESTORE_BLOCKED",
    "state": "BLOCKED",
    "evidence_id": ""
  }
]
```
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

### case_31: expected COMPLETE, predicted INCOMPLETE

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
  },
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_6909",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": "evidence_51"
  },
  {
    "phase": "VERIFICATION",
    "system_id": "identity_service",
    "resource_id": "tombstone_440",
    "operation": "VERIFY_RECORD_REDACTED",
    "state": "REDACTED",
    "evidence_id": "evidence_51"
  }
]
```
Extra/incorrect steps:
```json
[
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_6909",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "identity_service",
    "resource_id": "tombstone_440",
    "operation": "VERIFY_RECORD_REDACTED",
    "state": "REDACTED",
    "evidence_id": ""
  }
]
```
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

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
Investigation gaps: ["Evidence coverage incomplete; inspect ingestion report"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

