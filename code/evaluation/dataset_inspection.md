# Participant dataset inspection

No organizer files inspected. Values below are schema/enums, not answer lookups.

## deletion_requests.csv

Rows: 518. Columns: case_id, email, requested_at, reported_status, reported_at, audit_at, request_text.

| Column | Observed type | Missing | Values or range |
|---|---|---:|---|
| case_id | string | 0 | 518 distinct values |
| email | string | 0 | 517 distinct values |
| requested_at | UTC timestamp | 0 | 2026-01-05T06:00:00Z to 2026-09-24T08:00:00Z |
| reported_status | string | 0 | COMPLETE; NOT_STARTED; PARTIALLY_COMPLETE |
| reported_at | UTC timestamp | 0 | 2026-01-06T06:00:00Z to 2026-09-26T02:00:00Z |
| audit_at | UTC timestamp | 0 | 2026-01-29T12:00:00Z to 2026-10-01T12:00:00Z |
| request_text | string | 0 | 375 distinct values |

## deletion_rules.csv

Rows: 15. Columns: rule_id, data_category, condition, required_action.

| Column | Observed type | Missing | Values or range |
|---|---|---:|---|
| rule_id | string | 0 | 15 distinct values |
| data_category | string | 0 | ACCOUNT_TOMBSTONE; ANALYTICS_PROFILE; BACKUP_ARCHIVE; CACHE_ENTRY; EMAIL_DELIVERY_LOG; LEGAL_HOLD_RECORD; MARKETING_PROFILE; PRODUCT_TELEMETRY; SEARCH_INDEX_ENTRY; SECONDARY_IDENTIFIER; SECURITY_AUDIT_LOG; SUPPORT_ATTACHMENT; SUPPORT_MESSAGE; USER_EXPORT; USER_PROFILE |
| condition | string | 0 | A supplied legal hold is active; Account is deleted and only a stable internal user_id is needed to preserve references to retained records; Always; Attachment belongs only to the deletion subject; Conversation contains shared customer, agent, or order context that must be retained; Log contains a user email address; Record is still attributable to a user; Record is within the supplied retention period; Restore access can be blocked |
| required_action | string | 0 | ANONYMIZE; DELETE; REDACT; RETAIN |

## evidence_files.csv

Rows: 94. Columns: file_id, file_path, origin, captured_at.

| Column | Observed type | Missing | Values or range |
|---|---|---:|---|
| file_id | string | 0 | 94 distinct values |
| file_path | string | 0 | 94 distinct values |
| origin | string | 0 | account_admin_portal; account_history_service; analytics_platform; backup_service; central_observability_export; customer_account_failover_replica_capture; customer_account_service; customer_data_failover_replica_capture; customer_data_inventory_capture; customer_data_read_replica_capture; customer_data_regional_replicas_capture; customer_data_reporting_replica_capture; customer_export_service; customer_search_primary_capture; downstream_delivery_service; export_service; identity_service; integration_admin; integration_management_service; legal_retention_service; marketing_platform; object_storage; records_assurance_snapshot_bundle; search_index_admin; search_index_service; security_audit_service; security_service; service_readback_logs; service_resource_export; support_platform |
| captured_at | UTC timestamp | 0 | 2026-01-29T11:44:59Z to 2026-10-01T12:00:00Z |

## output.csv

Rows: 0. Columns: case_id, deletion_status, steps_json.

| Column | Observed type | Missing | Values or range |
|---|---|---:|---|
| case_id | string | 0 | 0 distinct values |
| deletion_status | string | 0 |  |
| steps_json | JSON array in CSV field | 0 | 0 distinct values |

## sample_deletion_requests.csv

Rows: 32. Columns: case_id, email, requested_at, reported_status, reported_at, audit_at, request_text.

| Column | Observed type | Missing | Values or range |
|---|---|---:|---|
| case_id | string | 0 | 32 distinct values |
| email | string | 0 | 32 distinct values |
| requested_at | UTC timestamp | 0 | 2026-08-17T12:00:00Z to 2026-09-13T11:00:00Z |
| reported_status | string | 0 | COMPLETE; NOT_STARTED; PARTIALLY_COMPLETE |
| reported_at | UTC timestamp | 0 | 2026-08-19T12:00:00Z to 2026-09-15T11:00:00Z |
| audit_at | UTC timestamp | 0 | 2026-09-03T11:30:00Z to 2026-10-01T12:00:00Z |
| request_text | string | 0 | 32 distinct values |

## sample_output.csv

Rows: 32. Columns: case_id, deletion_status, steps_json.

| Column | Observed type | Missing | Values or range |
|---|---|---:|---|
| case_id | string | 0 | 32 distinct values |
| deletion_status | string | 0 | COMPLETE; INCOMPLETE |
| steps_json | JSON array in CSV field | 0 | 32 distinct values |

## system_activity.csv

Rows: 4011. Columns: activity_id, event_time, event_type, source_system, target_system, resource_id, reported_result, details.

| Column | Observed type | Missing | Values or range |
|---|---|---:|---|
| activity_id | string | 0 | 4011 distinct values |
| event_time | UTC timestamp | 0 | 2026-01-04T14:56:29Z to 2026-10-01T10:18:34Z |
| event_type | string | 0 | ANONYMIZE_RECORD; BLOCK_RESTORE; CHECK_DATA_FLOW; CHECK_RESTORE_ACCESS; CLASSIFY_REQUEST; CREATE_EXPORT; DELETE_RECORD; DISABLE_DATA_FLOW; INDEX_RECORD; LINK_RESOURCE_IDENTITY; REDACT_RECORD; REFRESH_CACHE; RESTORE_BACKUP; RETAIN_RECORD; SEND_EMAIL; SYNC_RECORD; UPDATE_RECORD |
| source_system | string | 0 | account_service; backup_service; data_catalog; deletion_worker; export_service; integration_service; notification_service; privacy_intake; profile_service; security_service; support_platform |
| target_system | string | 0 | account_failover_replica; account_replication_cluster; account_service; analytics_platform; archive_service; backup_service; cache_service; email_delivery_service; export_service; identity_service; integration_service; legal_service; marketing_platform; object_storage; object_store; privacy_case_management; search_service; security_service; support_platform |
| resource_id | string | 0 | 3948 distinct values |
| reported_result | string | 0 | 3 distinct values |
| details | string | 0 | 4011 distinct values |

## user_audit_log.csv

Rows: 306. Columns: audit_id, user_id, event_time, field_name, old_value, new_value.

| Column | Observed type | Missing | Values or range |
|---|---|---:|---|
| audit_id | string | 0 | 306 distinct values |
| user_id | string | 0 | 196 distinct values |
| event_time | UTC timestamp | 0 | 2024-12-14T16:31:44Z to 2026-06-03T08:42:31Z |
| field_name | string | 0 | email; email_hash; phone |
| old_value | string | 0 | 306 distinct values |
| new_value | string | 0 | 306 distinct values |

## user_identities.csv

Rows: 850. Columns: user_id, name, email, phone, email_hash, updated_at.

| Column | Observed type | Missing | Values or range |
|---|---|---:|---|
| user_id | string | 0 | 850 distinct values |
| name | string | 0 | 847 distinct values |
| email | string | 0 | 850 distinct values |
| phone | string | 0 | 850 distinct values |
| email_hash | string | 0 | 850 distinct values |
| updated_at | UTC timestamp | 0 | 2023-06-22T10:59:00Z to 2026-08-30T01:02:00Z |

## Evidence manifest coverage

{'.log': 26, '.json': 28, '.txt': 1, '.png': 11, '.sql': 24, '.pdf': 4}

### evidence_01: service_events_ap_south_20260915.log

Origin: central_observability_export. Capture: 2026-09-15T11:59:39Z. Size: 22237 bytes.

### evidence_02: customer_data_snapshot_bundle_20260917.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-09-17T12:00:00Z. Size: 17941 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, customer_reference, full_name, email, phone, account_status, signup_channel, index_name, document, user_id, email_hash, reporting_window, metrics, recent_activity, archive_path, subject_reference, restore_allowed, encryption, owner_email, file_name, created_at, expires_at, download_available, included_sections, connector_name, destination, subject_selector, enabled, mode, event_name, actor_type, integrity_seal, ticket_id, channel, message_text
- $.snapshots[].records[].document: display_name, email, customer_reference
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity

### evidence_03: customer_account_handover_20261001.txt

Origin: customer_account_service. Capture: 2026-10-01T12:00:00Z. Size: 4534 bytes.

### evidence_04: account_admin_console_20260926.png

Origin: account_admin_portal. Capture: 2026-09-26T11:00:00Z. Size: 124989 bytes.

### evidence_05: customer_data_read_replica_20260921.sql

Origin: customer_data_read_replica_capture. Capture: 2026-09-21T10:00:00Z. Size: 24740 bytes.

customer_data_primary: 30 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_read_replica: 31 rows.
```sql
CREATE TABLE customer_data_read_replica (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_06: structured_service_events_eu_west_20260918.log

Origin: central_observability_export. Capture: 2026-09-18T11:55:24Z. Size: 31311 bytes.

### evidence_07: customer_data_snapshot_bundle_20260913.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-09-13T08:00:00Z. Size: 12514 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, index_name, document, user_id, email, phone, email_hash, reporting_window, metrics, recent_activity, archive_path, subject_reference, restore_allowed, encryption, connector_name, destination, subject_selector, enabled, mode, event_name, actor_type, integrity_seal, ticket_id, channel, message_text, customer_reference, full_name, account_status, signup_channel
- $.snapshots[].records[].document: display_name, email, customer_reference
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity

### evidence_08: search_index_diagnostic_20260906.log

Origin: search_index_service. Capture: 2026-09-06T07:00:00Z. Size: 8049 bytes.

### evidence_09: search_index_inspector_20260901.png

Origin: search_index_admin. Capture: 2026-09-01T06:00:00Z. Size: 121101 bytes.

### evidence_10: customer_data_read_replica_20260827.sql

Origin: customer_data_read_replica_capture. Capture: 2026-08-27T12:00:00Z. Size: 23657 bytes.

customer_data_primary: 29 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_read_replica: 30 rows.
```sql
CREATE TABLE customer_data_read_replica (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_11: syslog_archive_us_east_20260824.log

Origin: central_observability_export. Capture: 2026-08-24T13:56:43Z. Size: 26532 bytes.

### evidence_12: customer_data_snapshot_bundle_20260819.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-08-19T10:00:00Z. Size: 13456 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, customer_reference, full_name, email, phone, account_status, signup_channel, user_id, email_hash, reporting_window, metrics, recent_activity, archive_path, subject_reference, restore_allowed, encryption, owner_email, file_name, created_at, expires_at, download_available, included_sections, connector_name, destination, subject_selector, enabled, mode, index_name, document, event_name, actor_type, integrity_seal, ticket_id, uploaded_by, storage_class, channel, message_text
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity
- $.snapshots[].records[].document: display_name, email, customer_reference

### evidence_13: connector_configurations_20260812.json

Origin: integration_management_service. Capture: 2026-08-12T09:00:00Z. Size: 10107 bytes.

- $: exported_at, origin, record_count, records
- $.records[]: recorded_at, system, resource_id, record_type, result, subject_reference

### evidence_14: connector_management_console_20260807.png

Origin: integration_admin. Capture: 2026-08-07T08:00:00Z. Size: 130271 bytes.

### evidence_15: customer_data_read_replica_20260802.sql

Origin: customer_data_read_replica_capture. Capture: 2026-08-02T07:00:00Z. Size: 19383 bytes.

customer_data_primary: 24 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_read_replica: 25 rows.
```sql
CREATE TABLE customer_data_read_replica (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_16: application_trace_ap_northeast_20260730.log

Origin: central_observability_export. Capture: 2026-07-30T08:53:12Z. Size: 18932 bytes.

### evidence_17: customer_data_snapshot_bundle_20260725.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-07-25T15:00:00Z. Size: 15789 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, customer_reference, full_name, email, phone, account_status, signup_channel, user_id, email_hash, reporting_window, metrics, recent_activity, archive_path, subject_reference, restore_allowed, encryption, owner_email, file_name, created_at, expires_at, download_available, included_sections, connector_name, destination, subject_selector, enabled, mode, index_name, document, event_name, actor_type, integrity_seal, ticket_id, uploaded_by, storage_class, channel, message_text
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity
- $.snapshots[].records[].document: display_name, email, customer_reference

### evidence_18: account_history_report_20260718.pdf

Origin: account_history_service. Capture: 2026-07-18T11:00:00Z. Size: 65704 bytes.

### evidence_19: analytics_profile_view_20260713.png

Origin: analytics_platform. Capture: 2026-07-13T10:00:00Z. Size: 129362 bytes.

### evidence_20: customer_data_read_replica_20260708.sql

Origin: customer_data_read_replica_capture. Capture: 2026-07-08T09:00:00Z. Size: 23632 bytes.

customer_data_primary: 31 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_read_replica: 32 rows.
```sql
CREATE TABLE customer_data_read_replica (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_21: operations_stream_eu_central_20260705.log

Origin: central_observability_export. Capture: 2026-07-05T07:54:27Z. Size: 26326 bytes.

### evidence_22: customer_data_snapshot_bundle_20260630.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-06-30T07:00:00Z. Size: 24337 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, customer_reference, full_name, email, phone, account_status, signup_channel, user_id, email_hash, reporting_window, metrics, recent_activity, archive_path, subject_reference, restore_allowed, encryption, owner_email, file_name, created_at, expires_at, download_available, included_sections, connector_name, destination, subject_selector, enabled, mode, index_name, document, event_name, actor_type, integrity_seal, ticket_id, channel, message_text, uploaded_by, storage_class, recorded_at, system, record_type, result, lookup_value
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity
- $.snapshots[].records[].document: display_name, email, customer_reference

### evidence_23: customer_export_console_20260618.png

Origin: export_service. Capture: 2026-06-18T12:00:00Z. Size: 134597 bytes.

### evidence_24: customer_data_read_replica_20260613.sql

Origin: customer_data_read_replica_capture. Capture: 2026-06-13T11:00:00Z. Size: 19683 bytes.

customer_data_primary: 24 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_read_replica: 26 rows.
```sql
CREATE TABLE customer_data_read_replica (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_25: cloud_runtime_export_us_west_20260608.log

Origin: central_observability_export. Capture: 2026-06-08T09:58:28Z. Size: 32394 bytes.

### evidence_26: customer_data_snapshot_bundle_20260605.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-06-05T12:00:00Z. Size: 14243 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, customer_reference, full_name, email, phone, account_status, signup_channel, user_id, email_hash, reporting_window, metrics, recent_activity, archive_path, subject_reference, restore_allowed, encryption, connector_name, destination, subject_selector, enabled, mode, index_name, document, event_name, actor_type, integrity_seal, ticket_id, file_name, uploaded_by, storage_class, channel, message_text
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity
- $.snapshots[].records[].document: display_name, email, customer_reference

### evidence_27: legal_retention_register_20260529.pdf

Origin: legal_retention_service. Capture: 2026-05-29T08:00:00Z. Size: 65857 bytes.

### evidence_28: support_ticket_console_20260524.png

Origin: support_platform. Capture: 2026-05-24T07:00:00Z. Size: 135008 bytes.

### evidence_29: customer_data_regional_replicas_20260519.sql

Origin: customer_data_regional_replicas_capture. Capture: 2026-05-19T06:00:00Z. Size: 32282 bytes.

customer_data_primary: 28 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_replica_ap_south: 29 rows.
```sql
CREATE TABLE customer_data_replica_ap_south (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_replica_eu_west: 28 rows.
```sql
CREATE TABLE customer_data_replica_eu_west (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_30: service_events_sa_east_20260516.log

Origin: central_observability_export. Capture: 2026-05-16T11:58:25Z. Size: 23591 bytes.

### evidence_31: customer_data_snapshot_bundle_20260511.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-05-11T11:00:00Z. Size: 25927 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, customer_reference, full_name, email, phone, account_status, signup_channel, user_id, email_hash, reporting_window, metrics, recent_activity, archive_path, subject_reference, restore_allowed, encryption, connector_name, destination, subject_selector, enabled, mode, index_name, document, event_name, actor_type, integrity_seal, ticket_id, channel, message_text, recorded_at, system, record_type, result, lookup_value
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity
- $.snapshots[].records[].document: display_name, email, customer_reference

### evidence_32: backup_restore_console_20260429.png

Origin: backup_service. Capture: 2026-04-29T09:00:00Z. Size: 155587 bytes.

### evidence_33: customer_data_regional_replicas_20260424.sql

Origin: customer_data_regional_replicas_capture. Capture: 2026-04-24T08:00:00Z. Size: 36128 bytes.

customer_data_primary: 29 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_replica_ap_south: 29 rows.
```sql
CREATE TABLE customer_data_replica_ap_south (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_replica_eu_west: 31 rows.
```sql
CREATE TABLE customer_data_replica_eu_west (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_34: structured_service_events_ca_central_20260419.log

Origin: central_observability_export. Capture: 2026-04-19T06:59:43Z. Size: 38796 bytes.

### evidence_35: customer_data_snapshot_bundle_20260416.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-04-16T06:00:00Z. Size: 13423 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, customer_reference, full_name, email, phone, account_status, signup_channel, user_id, email_hash, reporting_window, metrics, recent_activity, connector_name, destination, subject_selector, enabled, mode, index_name, document, subject_reference, event_name, actor_type, integrity_seal, ticket_id, channel, message_text
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity
- $.snapshots[].records[].document: display_name, email, customer_reference

### evidence_36: customer_export_manifest_20260409.json

Origin: customer_export_service. Capture: 2026-04-09T12:00:00Z. Size: 11837 bytes.

- $: exported_at, origin, record_count, records
- $.records[]: recorded_at, system, resource_id, record_type, result, subject_reference

### evidence_37: security_audit_explorer_20260905.png

Origin: security_service. Capture: 2026-09-05T07:00:00Z. Size: 147699 bytes.

### evidence_38: customer_data_regional_replicas_20260330.sql

Origin: customer_data_regional_replicas_capture. Capture: 2026-03-30T10:00:00Z. Size: 35620 bytes.

customer_data_primary: 28 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_replica_ap_south: 29 rows.
```sql
CREATE TABLE customer_data_replica_ap_south (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_replica_eu_west: 28 rows.
```sql
CREATE TABLE customer_data_replica_eu_west (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_39: syslog_archive_ap_southeast_20260325.log

Origin: central_observability_export. Capture: 2026-03-25T08:59:44Z. Size: 26082 bytes.

### evidence_40: customer_data_snapshot_bundle_20260322.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-03-22T08:00:00Z. Size: 13647 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, customer_reference, full_name, email, phone, account_status, signup_channel, index_name, document, user_id, email_hash, reporting_window, metrics, recent_activity, owner_email, file_name, created_at, expires_at, download_available, included_sections, connector_name, destination, subject_selector, enabled, mode, subject_reference, order_reference, retention_reason, retained_until, event_name, actor_type, integrity_seal, ticket_id, uploaded_by, storage_class, channel, message_text
- $.snapshots[].records[].document: display_name, email, customer_reference
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity

### evidence_41: notification_delivery_20260315.log

Origin: downstream_delivery_service. Capture: 2026-03-15T07:00:00Z. Size: 9011 bytes.

### evidence_42: deleted_account_reference_20260310.png

Origin: identity_service. Capture: 2026-03-10T06:00:00Z. Size: 136696 bytes.

### evidence_43: customer_data_reporting_replica_20260305.sql

Origin: customer_data_reporting_replica_capture. Capture: 2026-03-05T12:00:00Z. Size: 20348 bytes.

customer_data_primary: 25 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_reporting_replica: 26 rows.
```sql
CREATE TABLE customer_data_reporting_replica (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_44: application_trace_eu_north_20260302.log

Origin: central_observability_export. Capture: 2026-03-02T10:59:23Z. Size: 25010 bytes.

### evidence_45: customer_data_snapshot_bundle_20260223.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-02-23T10:00:00Z. Size: 24885 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, index_name, document, customer_reference, full_name, email, phone, account_status, signup_channel, user_id, email_hash, reporting_window, metrics, recent_activity, recorded_at, system, record_type, result, lookup_value, archive_path, subject_reference, restore_allowed, encryption, connector_name, destination, subject_selector, enabled, mode, order_reference, retention_reason, retained_until, event_name, actor_type, integrity_seal, ticket_id, channel, message_text, file_name, uploaded_by, storage_class
- $.snapshots[].records[].document: display_name, email, customer_reference
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity

### evidence_46: object_storage_browser_20260213.png

Origin: object_storage. Capture: 2026-02-13T08:00:00Z. Size: 154193 bytes.

### evidence_47: customer_data_reporting_replica_20260208.sql

Origin: customer_data_reporting_replica_capture. Capture: 2026-02-08T07:00:00Z. Size: 19302 bytes.

customer_data_primary: 24 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_reporting_replica: 25 rows.
```sql
CREATE TABLE customer_data_reporting_replica (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_48: operations_stream_me_central_20260203.log

Origin: central_observability_export. Capture: 2026-02-03T05:59:42Z. Size: 21302 bytes.

### evidence_49: customer_data_snapshot_bundle_20260131.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-01-31T15:00:00Z. Size: 15256 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, customer_reference, full_name, email, phone, account_status, signup_channel, user_id, email_hash, reporting_window, metrics, recent_activity, archive_path, subject_reference, restore_allowed, encryption, owner_email, file_name, created_at, expires_at, download_available, included_sections, connector_name, destination, subject_selector, enabled, mode, index_name, document, event_name, actor_type, integrity_seal, ticket_id, uploaded_by, storage_class, channel, message_text
- $.snapshots[].records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.snapshots[].records[].recent_activity[]: event, product, quantity
- $.snapshots[].records[].document: display_name, email, customer_reference

### evidence_50: security_audit_ledger_20261001.json

Origin: security_audit_service. Capture: 2026-10-01T12:00:00Z. Size: 5152 bytes.

- $: exported_at, origin, record_count, records
- $.records[]: recorded_at, system, resource_id, record_type, result, subject_reference

### evidence_51: customer_data_snapshot_bundle_20260915.json

Origin: records_assurance_snapshot_bundle. Capture: 2026-09-15T12:00:00Z. Size: 1901 bytes.

- $: exported_at, source, snapshots
- $.snapshots[]: captured_at, data_store, collection, records
- $.snapshots[].records[]: resource_id, subject_reference, name, email, phone, email_hash, account_status, event_name, actor_type, integrity_seal

### evidence_52: customer_data_failover_replica_20260920.sql

Origin: customer_data_failover_replica_capture. Capture: 2026-09-20T12:00:00Z. Size: 12304 bytes.

customer_data_failover_replica: 16 rows.
```sql
CREATE TABLE customer_data_failover_replica (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

customer_data_primary: 16 rows.
```sql
CREATE TABLE customer_data_primary (
            resource_id TEXT PRIMARY KEY,
            origin_system TEXT NOT NULL,
            collection_name TEXT NOT NULL,
            record_json TEXT NOT NULL CHECK (json_valid(record_json)),
            updated_at TEXT NOT NULL
        )
```

### evidence_53: cloud_runtime_export_af_south_20260930.log

Origin: central_observability_export. Capture: 2026-09-30T11:59:44Z. Size: 94823 bytes.

### evidence_54: customer_accounts_failover_replica_20260902.sql

Origin: customer_account_failover_replica_capture. Capture: 2026-09-02T23:00:00Z. Size: 2077 bytes.

customer_profiles_failover_replica: 4 rows.
```sql
CREATE TABLE customer_profiles_failover_replica (
                resource_id TEXT PRIMARY KEY, user_id TEXT NOT NULL,
                full_name TEXT NOT NULL, email TEXT NOT NULL, phone TEXT NOT NULL,
                account_status TEXT NOT NULL, updated_at TEXT NOT NULL
            )
```

customer_profiles_primary: 3 rows.
```sql
CREATE TABLE customer_profiles_primary (
                resource_id TEXT PRIMARY KEY, user_id TEXT NOT NULL,
                full_name TEXT NOT NULL, email TEXT NOT NULL, phone TEXT NOT NULL,
                account_status TEXT NOT NULL, updated_at TEXT NOT NULL
            )
```

### evidence_55: security_retention_extract.pdf

Origin: security_service. Capture: 2026-09-05T06:30:00Z. Size: 64847 bytes.

### evidence_56: customer_analytics_report_20260907.json

Origin: analytics_platform. Capture: 2026-09-07T09:45:00Z. Size: 1404 bytes.

- $: captured_at, source, collection, records
- $.records[]: resource_id, user_id, email, phone, email_hash, reporting_window, metrics, recent_activity
- $.records[].metrics: sessions_30d, products_viewed_30d, orders_completed_90d, revenue_90d_usd
- $.records[].recent_activity[]: event, product, quantity

### evidence_57: customer_search_primary_20260910.sql

Origin: customer_search_primary_capture. Capture: 2026-09-10T08:45:00Z. Size: 838 bytes.

search_documents_primary: 3 rows.
```sql
CREATE TABLE search_documents_primary (resource_id TEXT PRIMARY KEY, display_name TEXT, email TEXT, source_resource_id TEXT, indexed_at TEXT)
```

### evidence_58: delivery_correction_attachment.pdf

Origin: support_platform. Capture: 2026-09-12T07:30:00Z. Size: 66039 bytes.

### evidence_59: customer_export_jobs_20260914.json

Origin: export_service. Capture: 2026-09-14T15:40:00Z. Size: 848 bytes.

- $: captured_at, source, collection, records
- $.records[]: resource_id, owner_email, file_name, created_at, expires_at, download_available, included_sections

### evidence_60: marketing_profile_console.png

Origin: marketing_platform. Capture: 2026-09-16T07:20:00Z. Size: 129711 bytes.

### evidence_61: support_replica.log

Origin: support_platform. Capture: 2026-09-17T22:00:19Z. Size: 1873 bytes.

### evidence_62: service_resource_export_20260129_114459.json

Origin: service_resource_export. Capture: 2026-01-29T11:44:59Z. Size: 10720 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, export_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.account_service.profile_lookups[].profile: customer_reference, email, email_hash, full_name, phone
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.export_service: exports
- $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_63: customer_data_inventory_20260213.sql

Origin: customer_data_inventory_capture. Capture: 2026-02-13T07:43:27Z. Size: 5478 bytes.

snapshot_scope: 7 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 2 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 4 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 3 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 2 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 0 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 1 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 1 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 4 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_64: resource_lookup_trace_20260218_083911.log

Origin: service_readback_logs. Capture: 2026-02-18T08:39:11Z. Size: 11049 bytes.

### evidence_65: service_resource_export_20260228_103637.json

Origin: service_resource_export. Capture: 2026-02-28T10:36:37Z. Size: 9689 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, export_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.account_service.profile_lookups[].profile: customer_reference, email, email_hash, full_name, phone
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.export_service: exports
- $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_66: customer_data_inventory_20260310.sql

Origin: customer_data_inventory_capture. Capture: 2026-03-10T05:38:48Z. Size: 6594 bytes.

snapshot_scope: 8 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 0 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 7 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 5 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 3 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 1 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 4 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 1 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 2 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_67: resource_lookup_trace_20260310_061801.log

Origin: service_readback_logs. Capture: 2026-03-10T06:18:01Z. Size: 548 bytes.

### evidence_68: service_resource_export_20260320_072349.json

Origin: service_resource_export. Capture: 2026-03-20T07:23:49Z. Size: 9296 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, export_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.account_service.profile_lookups[].profile: customer_reference, email, email_hash, full_name, phone
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.export_service: exports
- $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_69: customer_data_inventory_20260404.sql

Origin: customer_data_inventory_capture. Capture: 2026-04-04T10:04:19Z. Size: 5765 bytes.

snapshot_scope: 8 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 0 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 5 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 4 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 2 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 1 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 2 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 1 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 3 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_70: resource_lookup_trace_20260414_054007.log

Origin: service_readback_logs. Capture: 2026-04-14T05:40:07Z. Size: 9886 bytes.

### evidence_71: service_resource_export_20260429_083222.json

Origin: service_resource_export. Capture: 2026-04-29T08:32:22Z. Size: 10005 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, export_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.export_service: exports
- $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_72: customer_data_inventory_20260504.sql

Origin: customer_data_inventory_capture. Capture: 2026-05-04T09:41:47Z. Size: 6130 bytes.

snapshot_scope: 7 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 1 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 6 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 3 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 3 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 0 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 4 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 1 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 3 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_73: resource_lookup_trace_20260509_104353.log

Origin: service_readback_logs. Capture: 2026-05-09T10:43:53Z. Size: 13670 bytes.

### evidence_74: service_resource_export_20260514_114454.json

Origin: service_resource_export. Capture: 2026-05-14T11:44:54Z. Size: 9017 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_75: customer_data_inventory_20260524.sql

Origin: customer_data_inventory_capture. Capture: 2026-05-24T06:39:55Z. Size: 6651 bytes.

snapshot_scope: 8 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 0 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 5 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 6 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 3 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 1 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 4 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 1 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 4 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_76: resource_lookup_trace_20260529_074313.log

Origin: service_readback_logs. Capture: 2026-05-29T07:43:13Z. Size: 9674 bytes.

### evidence_77: service_resource_export_20260603_083457.json

Origin: service_resource_export. Capture: 2026-06-03T08:34:57Z. Size: 9775 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.account_service.profile_lookups[].profile: customer_reference, email, email_hash, full_name, phone
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_78: customer_data_inventory_20260618.sql

Origin: customer_data_inventory_capture. Capture: 2026-06-18T11:44:03Z. Size: 5831 bytes.

snapshot_scope: 7 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 2 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 6 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 4 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 3 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 1 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 1 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 0 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 2 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_79: resource_lookup_trace_20260623_053726.log

Origin: service_readback_logs. Capture: 2026-06-23T05:37:26Z. Size: 12074 bytes.

### evidence_80: service_resource_export_20260628_062556.json

Origin: service_resource_export. Capture: 2026-06-28T06:25:56Z. Size: 9028 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, export_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.account_service.profile_lookups[].profile: customer_reference, email, email_hash, full_name, phone
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.export_service: exports
- $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_81: customer_data_inventory_20260703.sql

Origin: customer_data_inventory_capture. Capture: 2026-07-03T07:43:56Z. Size: 6676 bytes.

snapshot_scope: 8 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 0 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 5 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 5 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 5 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 1 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 2 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 1 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 5 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_82: resource_lookup_trace_20260713_093359.log

Origin: service_readback_logs. Capture: 2026-07-13T09:33:59Z. Size: 10716 bytes.

### evidence_83: service_resource_export_20260718_104335.json

Origin: service_resource_export. Capture: 2026-07-18T10:43:35Z. Size: 11127 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, export_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.account_service.profile_lookups[].profile: customer_reference, email, email_hash, full_name, phone
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.export_service: exports
- $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_84: customer_data_inventory_20260723.sql

Origin: customer_data_inventory_capture. Capture: 2026-07-23T11:43:30Z. Size: 7046 bytes.

snapshot_scope: 8 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 1 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 7 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 5 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 5 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 1 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 4 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 1 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 2 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_85: resource_lookup_trace_20260728_054417.log

Origin: service_readback_logs. Capture: 2026-07-28T05:44:17Z. Size: 9098 bytes.

### evidence_86: service_resource_export_20260807_074104.json

Origin: service_resource_export. Capture: 2026-08-07T07:41:04Z. Size: 8619 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, export_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.export_service: exports
- $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_87: customer_data_inventory_20260817.sql

Origin: customer_data_inventory_capture. Capture: 2026-08-17T09:42:50Z. Size: 5967 bytes.

snapshot_scope: 8 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 1 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 5 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 4 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 4 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 1 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 1 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 1 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 2 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_88: resource_lookup_trace_20260822_103910.log

Origin: service_readback_logs. Capture: 2026-08-22T10:39:10Z. Size: 9105 bytes.

### evidence_89: service_resource_export_20260901_053316.json

Origin: service_resource_export. Capture: 2026-09-01T05:33:16Z. Size: 9695 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, export_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.account_service.profile_lookups[].profile: customer_reference, email, email_hash, full_name, phone
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.export_service: exports
- $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_90: customer_data_inventory_20260905.sql

Origin: customer_data_inventory_capture. Capture: 2026-09-05T07:18:01Z. Size: 2333 bytes.

snapshot_scope: 1 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 0 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 0 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 0 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 0 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 0 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 0 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 0 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 0 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_91: resource_lookup_trace_20260911_074253.log

Origin: service_readback_logs. Capture: 2026-09-11T07:42:53Z. Size: 12310 bytes.

### evidence_92: service_resource_export_20260915_114455.json

Origin: service_resource_export. Capture: 2026-09-15T11:44:55Z. Size: 12177 bytes.

- $: exported_at, region, service_exports, source
- $.service_exports: account_service, analytics_platform, backup_service, export_service, integration_service, search_service, security_service, support_platform
- $.service_exports.account_service: profile_lookups
- $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- $.service_exports.account_service.profile_lookups[].profile: customer_reference, email, email_hash, full_name, phone
- $.service_exports.analytics_platform: profiles
- $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- $.service_exports.backup_service: restore_entries
- $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- $.service_exports.export_service: exports
- $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- $.service_exports.integration_service: connectors
- $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- $.service_exports.search_service: index_queries
- $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- $.service_exports.search_service.index_queries[].hits: documents, total
- $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- $.service_exports.security_service: audit_records
- $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- $.service_exports.support_platform: tickets
- $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id

### evidence_93: customer_data_inventory_20260916.sql

Origin: customer_data_inventory_capture. Capture: 2026-09-16T08:37:39Z. Size: 5593 bytes.

snapshot_scope: 8 rows.
```sql
CREATE TABLE snapshot_scope (origin_system TEXT PRIMARY KEY, captured_at TEXT NOT NULL)
```

customer_profiles: 1 rows.
```sql
CREATE TABLE customer_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, full_name TEXT, email TEXT, phone TEXT, email_hash TEXT, account_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_search_documents: 3 rows.
```sql
CREATE TABLE customer_search_documents (resource_id TEXT PRIMARY KEY, customer_reference TEXT, display_name TEXT, email TEXT, phone TEXT, email_hash TEXT, index_name TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_analytics_profiles: 2 rows.
```sql
CREATE TABLE customer_analytics_profiles (resource_id TEXT PRIMARY KEY, customer_reference TEXT, email TEXT, phone TEXT, email_hash TEXT, audience_cohort TEXT NOT NULL, updated_at TEXT NOT NULL)
```

support_records: 3 rows.
```sql
CREATE TABLE support_records (resource_id TEXT PRIMARY KEY, customer_reference TEXT, requester_name TEXT, requester_email TEXT, requester_phone TEXT, message_excerpt TEXT NOT NULL, updated_at TEXT NOT NULL)
```

customer_exports: 1 rows.
```sql
CREATE TABLE customer_exports (resource_id TEXT PRIMARY KEY, customer_reference TEXT, owner_email TEXT, owner_phone TEXT, object_key TEXT NOT NULL, updated_at TEXT NOT NULL)
```

connector_subscriptions: 2 rows.
```sql
CREATE TABLE connector_subscriptions (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, connector_name TEXT NOT NULL, enabled INTEGER NOT NULL CHECK (enabled IN (0,1)), last_delivery_status TEXT NOT NULL, updated_at TEXT NOT NULL)
```

backup_restore_entries: 2 rows.
```sql
CREATE TABLE backup_restore_entries (resource_id TEXT PRIMARY KEY, customer_reference TEXT, customer_email TEXT, archive_key TEXT NOT NULL, restore_allowed INTEGER NOT NULL CHECK (restore_allowed IN (0,1)), updated_at TEXT NOT NULL)
```

security_audit_records: 3 rows.
```sql
CREATE TABLE security_audit_records (resource_id TEXT PRIMARY KEY, subject_reference TEXT NOT NULL, event_code TEXT NOT NULL, retention_until TEXT NOT NULL, updated_at TEXT NOT NULL)
```

### evidence_94: resource_lookup_trace_20260926_103856.log

Origin: service_readback_logs. Capture: 2026-09-26T10:38:56Z. Size: 11801 bytes.

## Relationships and acceptance risks

- Stable user_id links identity changes; exact current/historic email, hashes and normalized phones link resources.
- file_id cites a file, not a case; manifest origin never establishes ownership.
- activity_id is a claim unless details provide an explicit identity relationship or direct observation.
- resource IDs join snapshots; trace IDs join lookup starts to completions within a log.
- Subject-free anonymized records and negative lookups need a separate grounded identity link.
- Both event and capture timestamps must be within audit cutoff.
- SQL snapshot_scope lists systems, not an explicit exhaustive set of subject resources; absence is not inferred from missing rows.
- Output must have 518 unique string-sorted target cases; samples are evaluation only.