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
- status_correct: 24
- status_accuracy: 0.75
- exact_sequences: 8
- sequence_accuracy: 0.25
- ordering_only_errors: 0
- step_tp: 144
- step_fp: 18
- step_fn: 49
- step_precision: 0.8888888888888888
- step_recall: 0.7461139896373057
- step_f1: 0.8112676056338027
- fields: {"phase": 0.8186528497409327, "system_id": 0.8186528497409327, "resource_id": 0.8186528497409327, "operation": 0.8186528497409327, "state": 0.8186528497409327, "evidence_id": 0.7461139896373057, "step_no": 0.5854922279792746}
- confusion: {"COMPLETE -> INCOMPLETE": 8, "COMPLETE -> COMPLETE": 2, "INCOMPLETE -> INCOMPLETE": 22}
- operations: {"missing VERIFY_RECORD_ABSENT": 21, "missing VERIFY_RECORD_ANONYMIZED": 7, "extra REPORT_REMAINING_RECORD": 1, "extra DELETE_RECORD": 1, "extra VERIFY_RECORD_ABSENT": 1, "missing VERIFY_RECORD_PRESENT": 12, "extra VERIFY_RECORD_REDACTED": 4, "extra VERIFY_RECORD_PRESENT": 5, "missing VERIFY_RECORD_REDACTED": 3, "missing VERIFY_DATA_FLOW_DISABLED": 3, "missing VERIFY_RESTORE_BLOCKED": 3, "extra VERIFY_DATA_FLOW_DISABLED": 3, "extra VERIFY_RESTORE_BLOCKED": 3}
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

Resource-level root-cause investigation:

- account_service / account_001: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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

Resource-level root-cause investigation:

- account_service / account_002: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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

Resource-level root-cause investigation:

- analytics_platform / analytics_9406: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.

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

Resource-level root-cause investigation:

- account_service / account_004: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.
- analytics_platform / analytics_901: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_006: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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
[
  {
    "phase": "FINDING",
    "system_id": "object_storage",
    "resource_id": "object_19",
    "operation": "REPORT_REMAINING_RECORD",
    "state": "PRESENT",
    "evidence_id": "evidence_46"
  },
  {
    "phase": "REMEDIATION",
    "system_id": "object_storage",
    "resource_id": "object_19",
    "operation": "DELETE_RECORD",
    "state": "ABSENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "object_storage",
    "resource_id": "object_19",
    "operation": "VERIFY_RECORD_ABSENT",
    "state": "ABSENT",
    "evidence_id": ""
  }
]
```
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_007: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_008: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_3960: Available observations were captured or occurred after this audit cutoff; using them would leak future information.
- security_service / audit_record_4902: Available observations were captured or occurred after this audit cutoff; using them would leak future information.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_010: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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
    "system_id": "identity_service",
    "resource_id": "tombstone_17",
    "operation": "VERIFY_RECORD_REDACTED",
    "state": "REDACTED",
    "evidence_id": ""
  }
]
```
Investigation gaps: []

Resource-level root-cause investigation:


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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_5521: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.
- security_service / audit_record_6645: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_5037: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.
- security_service / audit_record_5569: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

Resource-level root-cause investigation:

- account_service / account_6440: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.
- security_service / audit_record_3737: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- analytics_platform / analytics_5335: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_4990: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_410: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.
- security_service / audit_record_4128: Available observations were captured or occurred after this audit cutoff; using them would leak future information.

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

Resource-level root-cause investigation:

- security_service / audit_record_7095: Available observations were captured or occurred after this audit cutoff; using them would leak future information.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

Resource-level root-cause investigation:

- account_service / account_3136: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.
- security_service / audit_record_451: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- analytics_platform / analytics_1895: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.

### case_26: expected COMPLETE, predicted INCOMPLETE

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
[
  {
    "phase": "VERIFICATION",
    "system_id": "security_service",
    "resource_id": "audit_record_5416",
    "operation": "VERIFY_RECORD_PRESENT",
    "state": "PRESENT",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "support_platform",
    "resource_id": "support_4715",
    "operation": "VERIFY_RECORD_REDACTED",
    "state": "REDACTED",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "integration_service",
    "resource_id": "data_flow_6244",
    "operation": "VERIFY_DATA_FLOW_DISABLED",
    "state": "DISABLED",
    "evidence_id": ""
  },
  {
    "phase": "VERIFICATION",
    "system_id": "backup_service",
    "resource_id": "backup_3120",
    "operation": "VERIFY_RESTORE_BLOCKED",
    "state": "BLOCKED",
    "evidence_id": ""
  }
]
```
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

Resource-level root-cause investigation:

- account_service / account_5684: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.
- security_service / audit_record_5416: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- support_platform / support_4715: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- analytics_platform / analytics_4566: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.
- integration_service / data_flow_6244: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- backup_service / backup_3120: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

Resource-level root-cause investigation:

- account_service / account_3866: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.
- security_service / audit_record_3830: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- support_platform / support_4707: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- analytics_platform / analytics_4574: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.
- integration_service / data_flow_2295: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- backup_service / backup_5970: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: shared operations differ in state or evidence provenance; inspect timeline and source precedence.

Resource-level root-cause investigation:

- account_service / account_5482: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.
- security_service / audit_record_9265: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- support_platform / support_2351: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- analytics_platform / analytics_6077: Eligible state exists, but no exact subject identifier is present on these observations. Anonymous/absent resources need an independent grounded link.
- integration_service / data_flow_2337: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.
- backup_service / backup_838: Resource is grounded: inspect selected category, scope, timestamp and citation against the expected operation; see per-case diagnostic ledger.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_7012: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.
- security_service / audit_record_3954: Available observations were captured or occurred after this audit cutoff; using them would leak future information.

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
Investigation gaps: ["Account deletion audit lacks a grounded profile or tombstone state"]

Diagnosis: expected resources/operations absent from prediction; inspect grounded identity links, cutoff eligibility and category policy. No answer-derived identity link was inserted.

Resource-level root-cause investigation:

- account_service / account_4163: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.
- security_service / audit_record_1707: Available observations were captured or occurred after this audit cutoff; using them would leak future information.

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

Resource-level root-cause investigation:

- account_service / account_4857: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.

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

Resource-level root-cause investigation:

- account_service / account_8858: No explicit resource state was recovered from participant evidence; a workflow claim or absent row is not sufficient proof.


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

## Failures found and general improvements

1. Initial offline baseline: image coverage gaps caused conservative incomplete
   decisions, and Spanish negation matching was too broad. Narrowed negation and
   added actual Gemini multilingual classification. Never used answer-based intent tables.
2. The SDK's response_schema conversion sent unsupported additional_properties.
   Switched to JSON Schema and then the recommended stateless Interactions API.
3. Model discovery was not equivalent to generation entitlement. Gemini 3.8 Flash
   returned overload/timeouts; listed Gemini 2.5 Flash rejected new users. Gemini
   3.1 Flash-Lite produced successful structured text and image responses.
4. Initial vision extraction confused user IDs, emails and UI labels with resource
   IDs. Added a resource-key schema, grounding checks, bounded repair, and exclusion
   of incidental links outside the displayed business view. Cached outputs are
   schema-validated again before use.
5. Added the observed contact_query_completed log variant with trace-based identity
   joins. Debug cache misses still cannot establish record absence.
6. An old, already-absent resource predating a new deletion request introduced an
   unnecessary verification. Exclude resources whose only observed states are
   absence before the new request; preserve any actual remaining copy.
7. A new primary-only absence must not suppress an independently observed replica.
   Added per-replica state timelines and a regression test.
8. Prevented COMPLETE based only on retained security records when an account audit
   has no grounded profile/tombstone state. This deliberately trades optimistic
   public-sample status matches for the user's evidence requirement. Any measured
   regression is retained only with this explicit correctness rationale.
9. Batched difficult intent requests and indexed email candidate owners to reduce
   calls and repeated identity scans. Provider usage is recorded from actual metadata.
10. Resolve business filenames and document references only through explicit catalog
    aliases, recording the association time. Rejected model-derived filename suffix
    IDs. A catalog association conflicting with visible subject identifiers is an
    investigation gap, not authority to delete another person's record.
11. Normalize business lifecycle ACTIVE labels to record existence; a stable-only
    account tombstone is not exposed direct PII merely because the reference exists.

Unresolved gaps must remain visible: some reference verification resources have no
pre-cutoff subject link, or rely on an absent record in a snapshot without an
explicit resource lookup. Mapping them by numeric suffix, case ID, answer lookup,
future evidence or ambiguous workflow timing would violate the requested contract.
The per-failure report distinguishes these from extraction and policy defects.

## Final independent test result

36 tests passed on Python 3.13.3, including all 15 requested scenarios, API retry/cache/schema validation, SQL isolation and temporal identity-link checks.
