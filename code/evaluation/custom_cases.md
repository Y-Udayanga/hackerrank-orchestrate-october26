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

Final independent test run: **38 passed** (pytest, Python 3.13.3). Additional tests cover Gemini retry bounds, structured-response rejection, content-cache behavior, secret redaction, catalog identity conflicts, and alias availability time.
