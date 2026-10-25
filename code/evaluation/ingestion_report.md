# Ingestion report

2443 observations.

Errors:


Notes:
- evidence_04: excluded 1 links to records outside the displayed view
- evidence_04: excluded 1 links to records outside the displayed view
- evidence_04: The artifact displays order IDs (e.g., ORD-20265762) which do not match the required resource_id pattern (e.g., account_<number>, support_<number>), so they were excluded. Only account_5762 and support_9538 were clearly identifiable as valid resource IDs.
- evidence_09: None. The records were clearly identified in the search results table.
- evidence_14: The records 'Order notifications' and 'Delivery tracking' were excluded because they do not contain a visible resource ID matching the required pattern (e.g., data_flow_<number>).
- evidence_19: The artifact displays event-level telemetry (e.g., 'Order completed', 'Product viewed'), but these individual events do not have unique, visible resource IDs (e.g., event_123) that conform to the required pattern. Therefore, only the primary analytics profile record is extracted.
- No actionable resource observations in evidence_21
- evidence_23: None. All records were clearly visible in the data export table.
- No actionable resource observations in evidence_27
- evidence_28: The artifact displays a support ticket (CS-5034) and an order (ORD-20265034), but only the support ticket contains a visible resource ID (support_1034) that conforms to the required format. The order ID 'ORD-20265034' does not match the required resource_id pattern (e.g., account_<number>, support_<number>) and is therefore excluded.
- evidence_32: None. All records were clearly visible in the table.
- evidence_37: None. All records were clearly visible in the audit log table.
- evidence_42: The artifact displays a 'Customer Reference Registry' for 'user_17'. While the prompt asks for ACCOUNT_TOMBSTONE and SECONDARY_IDENTIFIER, the displayed records (ORD-20263245, CS-3245, CS-3378, FIN-7742) are linked references rather than the primary records themselves, and do not match the required resource_id pattern (e.g., account_<number>). Therefore, only the primary subject 'user_17' is extracted as the account record.
- evidence_46: rejected 7 ungrounded visual resource IDs after repair
- evidence_46: Resource IDs were derived by mapping the visible file names (e.g., 'delivery_confirmation_19.pdf') to the required resource_id pattern (e.g., 'support_19') as the system does not explicitly display a unique database key for these objects.
- No actionable resource observations in evidence_48
- evidence_60: The artifact displays a single marketing profile record (marketing_001). While there are activity logs and audience membership details visible, these are attributes or sub-components of the primary marketing_001 record rather than distinct, independently addressable resource records with their own unique resource IDs.
- No actionable resource observations in evidence_90