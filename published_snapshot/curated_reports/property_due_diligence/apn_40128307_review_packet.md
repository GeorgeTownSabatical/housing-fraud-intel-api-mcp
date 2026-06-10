# APN 401-283-07 Review Packet

Status: UNKNOWN pending assessor, recorder, tax-default, title, and GIS source artifacts.

Required pulls:
- Official assessor parcel detail for APN 401-283-07.
- Official recorder instrument chain tied by APN or legal description.
- Official tax-default or delinquency records where available.
- GIS/legal-description cross-check for any related APN cluster.

Guardrail: do not infer ownership or fraud from the retrieval playbook alone.

Current score: 105
Signals:
- seed_apn_present
- related_apn_cluster_present
- requires_official_parcel_and_recorder_pulls
- local_assessor_packet_present
- local_gis_cluster_report_present
- local_timeline_present

Attached local artifacts:
- record_retrieval_playbook: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/docs/RECORD_RETRIEVAL_PLAYBOOK.md)
- apn_40128307_assessor_packet: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/outputs/assessor_packets/apn_40128307_assessor_packet.md)
- apn_40128307_cluster_packet: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/outputs/assessor_packets/apn_40128307_cluster_packet.csv)
- apn_40128307_gis_cluster_report: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/outputs/gis_model/apn_40128307_cluster_report.md)
- apn_40128307_timeline: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/outputs/timelines/401-283-07_timeline.md)
- apn_40128307_local_api_snapshot: PASS (/Users/ALISTAIRE/housing-fraud-intel-api/exports/gis_model_api_responses/local_40128307.json)
