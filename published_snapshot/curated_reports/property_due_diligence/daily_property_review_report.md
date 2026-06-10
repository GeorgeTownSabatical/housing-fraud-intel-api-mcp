# Daily Property Due-Diligence Review

This report ranks review candidates and preserves UNKNOWN status until official records are attached.

## apn_40128307_review_packet

- Score: 105
- Validation status: UNKNOWN
- APN: 401-283-07
- Rank reasons: seed APN review, related APN cluster review, local assessor packet already generated, local GIS cluster report already generated, local mutation timeline already generated, parcel and recorder verification required, validation remains UNKNOWN and needs manual review, official-source gap remains open
- Signals: seed_apn_present, related_apn_cluster_present, requires_official_parcel_and_recorder_pulls, local_assessor_packet_present, local_gis_cluster_report_present, local_timeline_present

Evidence boundary: index rows, queue entries, and playbooks are not title, ownership, APN, or fraud proof.

Source records:
- record_retrieval_playbook: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/docs/RECORD_RETRIEVAL_PLAYBOOK.md)
- apn_40128307_assessor_packet: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/outputs/assessor_packets/apn_40128307_assessor_packet.md)
- apn_40128307_cluster_packet: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/outputs/assessor_packets/apn_40128307_cluster_packet.csv)
- apn_40128307_gis_cluster_report: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/outputs/gis_model/apn_40128307_cluster_report.md)
- apn_40128307_timeline: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/outputs/timelines/401-283-07_timeline.md)
- apn_40128307_local_api_snapshot: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/exports/gis_model_api_responses/local_40128307.json)

Uncertainty notes:
- Local artifacts organize observations and office-pull questions; they are not official assessor or recorder copies.
- Official parcel card, recorder chain, and tax-default disposition remain required.
- Source support is UNKNOWN until official records or source artifacts are attached.

## tracked_surname_intersection_packet

- Score: 85
- Validation status: UNKNOWN
- APN: UNKNOWN
- Rank reasons: tracked surname intersections, official recorder copy pull required, validation remains UNKNOWN and needs manual review, official-source gap remains open
- Signals: priority_document_count=21, tracked_surname_intersections_present, official_copy_pull_required

Evidence boundary: index rows, queue entries, and playbooks are not title, ownership, APN, or fraud proof.

Source records:
- tracked_intersection_request_packet: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/exports/tracked_surname_intersection_document_request_packet.json)

Uncertainty notes:
- Document images/details have not been pulled.
- APNs and legal descriptions are UNKNOWN.
- Source support is UNKNOWN until official records or source artifacts are attached.

## record_reference_451_identification

- Score: 35
- Validation status: UNKNOWN
- APN: UNKNOWN
- Rank reasons: unresolved 451 reference, validation remains UNKNOWN and needs manual review, official-source gap remains open
- Signals: unresolved_reference_451

Evidence boundary: index rows, queue entries, and playbooks are not title, ownership, APN, or fraud proof.

Source records:
- estate_task_catalog_rank_451_probe: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/exports/estate_investigation_task_catalog_6000_ranked.csv)

Uncertainty notes:
- Local artifact search found `priority_rank=451` in the estate investigation task catalog.
- That match does not identify an APN, parcel number, recorder document, or official source row.
- Source support is UNKNOWN until official records or source artifacts are attached.
