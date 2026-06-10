# APN 401-283-07 Official Records Handoff

Status: blocked until official assessor, recorder, and tax-default records are obtained.
Intake status: matched records `0`, missing categories `assessor, recorder, tax`.
Scanner report: `reports/property_due_diligence/official_record_intake_status.md`

Local priority score: `102.00`
Local pull reasons: address unavailable | improved parcel with unavailable address | tax-default signal | long tax-default period | low minimum bid | related APN cluster | sparse situs history

Records to request:
- assessor parcel detail
- value history
- parcel mutation history
- tax-default disposition
- recorder instrument chain

Known local sources:
- local_tustin_arcgis_snapshot; user_grounding_note:OC tax-default/BOS snippets; local_tustin_arcgis_snapshot; chatgpt_manual_review_queue

Open questions:
- Manual review request chatgpt-0788558255793eae (request_office_pull, priority=critical): Primary seed anomaly. Pull parcel mutation history, assessed-owner chronology, situs history, grantor-grantee chain, easement history, and tax-default disposition. | Manual review request chatgpt-7a50077e85f7579c (link_apns, priority=high): Seed/pull-list priority cluster. Do not call these literal top three ranked rows; distinguish from ranked anomaly order.

Guardrail: local generated artifacts organize the request; they are not official proof of title, ownership, APN lineage, or tax disposition.
