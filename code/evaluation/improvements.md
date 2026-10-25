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
