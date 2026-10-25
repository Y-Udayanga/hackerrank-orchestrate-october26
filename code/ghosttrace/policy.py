"""Compile only the supplied policy CSV; no model-written policy."""
from .identity import read_csv
from .types import timestamp

CONDITIONS = {
    'Always',
    'Conversation contains shared customer, agent, or order context that must be retained',
    'Attachment belongs only to the deletion subject',
    'Record is still attributable to a user',
    'Log contains a user email address',
    'Record is within the supplied retention period',
    'A supplied legal hold is active',
    'Restore access can be blocked',
    'Account is deleted and only a stable internal user_id is needed to preserve references to retained records',
}


class Policy:
    def __init__(self, path):
        self.rules={}
        for row in read_csv(path):
            if row['condition'] not in CONDITIONS or row['required_action'] not in {'DELETE','REDACT','ANONYMIZE','RETAIN'}:
                raise ValueError('Unsupported policy condition/action; explicit implementation required')
            if row['data_category'] in self.rules:raise ValueError('Conflicting category rules')
            self.rules[row['data_category']]=row

    def required(self,obs,cutoff):
        if obs.category=='DATA_FLOW':return 'DISABLE_DATA_FLOW','DISABLED','VERIFY_DATA_FLOW_DISABLED','REPORT_ACTIVE_DATA_FLOW'
        rule=self.rules.get(obs.category)
        if not rule:raise ValueError('No policy rule for '+obs.category)
        fields=obs.fields
        if obs.category=='BACKUP_ARCHIVE':
            if fields.get('can_block_restore') is False:raise ValueError('Backup cannot be safely blocked under supplied rule')
            return 'BLOCK_RESTORE','BLOCKED','VERIFY_RESTORE_BLOCKED','REPORT_RESTORE_RISK'
        if obs.category=='SUPPORT_ATTACHMENT' and fields.get('shared_context') is True:
            raise ValueError('Shared attachment outside subject-only delete condition')
        if obs.category=='SECURITY_AUDIT_LOG':
            until=fields.get('retention_until',fields.get('retained_until'))
            if until and timestamp(until)<timestamp(cutoff):
                raise ValueError('Expired retention has no supplied disposition rule')
        if obs.category=='LEGAL_HOLD_RECORD' and fields.get('legal_hold_active') is False:
            raise ValueError('Inactive legal hold has no supplied disposition rule')
        if obs.category=='ACCOUNT_TOMBSTONE' and fields.get('account_status','DELETED')!='DELETED':
            raise ValueError('Active profile does not satisfy tombstone condition')
        return {
            'DELETE':('DELETE_RECORD','ABSENT','VERIFY_RECORD_ABSENT','REPORT_REMAINING_RECORD'),
            'REDACT':('REDACT_RECORD','REDACTED','VERIFY_RECORD_REDACTED','REPORT_EXPOSED_PII'),
            'ANONYMIZE':('ANONYMIZE_RECORD','ANONYMIZED','VERIFY_RECORD_ANONYMIZED','REPORT_EXPOSED_PII'),
            'RETAIN':(None,'PRESENT','VERIFY_RECORD_PRESENT',None),
        }[rule['required_action']]
