# GhostTrace AI: inspected contract and architecture

Only participant-facing files under dataset/ are used. The corpus has 518 target
requests, 32 public sample requests, 850 identity snapshots, 306 identity changes,
4,011 activity claims, 15 policy rules, and 94 manifest entries. Evidence consists
of 28 JSON files, 26 logs, 24 SQLite-compatible SQL exports, 11 PNG screenshots,
4 PDFs, and one text handover. No CSV evidence files currently occur inside evidence/;
the adapter also accepts CSV records. All input timestamps are ISO UTC strings.
Requests span January–September 2026 and audits extend through October 1.

JSON includes nested business snapshots, service readbacks, and flat observations.
SQL includes typed inventories with snapshot_scope and primary/replica tables with
JSON payloads. Logs include key/value, bracketed application logs, structured JSON,
syslog, cloud message envelopes, and trace-correlated lookup starts/completions.
PDFs and screenshots contain ordinary business records, including unrelated
customers; a document title or origin is never sufficient to assign ownership.

The eight logical agents are ordinary Python components: intent classification,
time-aware exact identity resolution, evidence adapters/index, resource timelines,
CSV-compiled policy evaluation, flow/restore evaluation, remediation planning, and
strict output validation. There is no framework dependency or autonomous deletion.
Gemini handles structured multilingual intent and visual extraction. Python handles
identity, timestamps, policy, ordering and serialization. Gemini does not author
final steps or modify policy. API credentials are environment-only. Missing API
access is explicit; offline mode has reduced intent and vision capability.

Every observation carries its file ID, event time, manifest capture time, original
fields and location. Both clocks must be at/before audit_at. Resource links must
also be established by the cutoff. Names alone never identify a person. Current
identity fields are rolled back through audit changes and historical values are
included only when they existed by the cutoff. Exact email matching ignores case
but preserves dots and plus tags. Conflicting owners are rejected.

State is selected from direct readbacks and captured business records, never a
successful delete claim. Newer observed states supersede older ones; replica
presence at the same snapshot defeats primary absence. Missing rows in a partial
snapshot do not imply global absence. An unresolved subject or unsupported final
state is surfaced as an investigation gap rather than invented proof.

The output validator checks exact fields, operation/state pairs, phase ordering,
duplicates, numbering, provenance, cutoff, and complete remediation/verification
coverage. Incomplete cases verify retained and already compliant resources too.
Public answers are loaded only by the evaluation entry point. No case IDs or
reference answers enter the prediction modules.

Acceptance: 518 unique sorted target cases; valid UTF-8/JSON; tests of all requested
edge cases; sample status, unordered semantic step, ordered sequence and field
metrics; honest usage accounting; reproducible CLI; dataset-free code.zip.
The complete raw agent trace must be exported after this session is closed, per
agent_trace_instructions.md. log.txt is the live append-only submission transcript.
