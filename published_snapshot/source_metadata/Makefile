PYTHON ?= python3

.PHONY: run test lint evaluate seed-demo demo export-demo discover-sources validate-sources import-real-demo validate-real-data recorder-campaign-validate recorder-campaign-distress-report recorder-campaign-spike-audit tracked-intersection-request-packet export-source-inventory generate-cpra-request check-oc-apn-cache rank-apn-recovery-candidates bridge-enqueue-dry-run bridge-normalization-audit bridge-rejection-report bridge-requeue-rejections bridge-queue-workboard bridge-queue-claim property-source-inventory property-official-intake property-due-diligence property-blocker-handoff property-bridge-state bridge-queue-append-dry-run

run:
	uvicorn app.main:app --reload

test:
	pytest -q

lint:
	ruff check app tests scripts

evaluate:
	$(PYTHON) scripts/run_local_demo.py --evaluate

seed-demo:
	$(PYTHON) scripts/seed_demo_data.py

demo:
	$(PYTHON) scripts/run_local_demo.py

export-demo:
	$(PYTHON) scripts/export_demo_packet.py

discover-sources:
	$(PYTHON) scripts/discover_sources.py

validate-sources:
	$(PYTHON) scripts/discover_sources.py

import-real-demo:
	$(PYTHON) scripts/import_real_data.py --source irvine_general_plan_zoning_arcgis --input data/raw/irvine_general_plan_zoning_arcgis/manual_input.json --mode append --terms-reviewed --override-manual-review

validate-real-data:
	$(PYTHON) scripts/validate_real_data.py --source irvine_general_plan_zoning_arcgis --input data/raw/irvine_general_plan_zoning_arcgis/manual_input.json

recorder-campaign-validate:
	$(PYTHON) scripts/recorder_campaign_status.py --tail-lines 3 --sample-limit 1 > /tmp/recorder_status.json
	python3 -m json.tool /tmp/recorder_status.json >/dev/null
	$(PYTHON) scripts/recorder_campaign_status.py --text --tail-lines 5 --sample-limit 1
	$(PYTHON) -m pytest -q tests/test_recorder_campaign_status.py tests/test_run_recorder_docnum_campaign_until_done.py

recorder-campaign-distress-report:
	$(PYTHON) scripts/build_recorder_campaign_distress_report.py

recorder-campaign-spike-audit:
	$(PYTHON) scripts/audit_recorder_distress_spikes.py

tracked-intersection-request-packet:
	$(PYTHON) scripts/build_tracked_intersection_request_packet.py

export-source-inventory:
	$(PYTHON) scripts/discover_sources.py

generate-cpra-request:
	$(PYTHON) scripts/generate_cpra_request.py --agency "Orange County Clerk-Recorder" --dataset recorder_index

check-oc-apn-cache:
	$(PYTHON) scripts/check_orange_county_apn_cache.py

rank-apn-recovery-candidates:
	$(PYTHON) scripts/rank_recorder_apn_recovery_candidates.py --output-prefix recorder_apn_recovery_candidates_ranked

bridge-enqueue-dry-run:
	$(PYTHON) scripts/enqueue_bridge_request.py --title "Bridge enqueue dry run" --dry-run

bridge-normalization-audit:
	$(PYTHON) scripts/audit_bridge_queue_normalization.py

bridge-rejection-report:
	$(PYTHON) scripts/format_bridge_rejections.py

bridge-requeue-rejections:
	$(PYTHON) scripts/requeue_bridge_rejections.py --publish

bridge-queue-workboard:
	$(PYTHON) scripts/bridge_queue_workboard.py

bridge-queue-claim:
	@test -n "$(REQUEST_ID)" || (echo "REQUEST_ID is required" >&2; exit 2)
	$(PYTHON) scripts/bridge_queue_update.py "$(REQUEST_ID)" --state in_progress --responsible "$${RESPONSIBLE:-codex}" --note "$${NOTE:-claimed from make bridge-queue-claim}"
	$(PYTHON) scripts/bridge_queue_workboard.py

property-source-inventory:
	$(PYTHON) scripts/property_due_diligence/source_inventory.py

property-official-intake:
	$(PYTHON) scripts/property_due_diligence/official_record_intake.py

property-due-diligence:
	$(PYTHON) scripts/property_due_diligence/run_daily_check.py

property-blocker-handoff:
	$(PYTHON) scripts/property_due_diligence/official_record_intake.py
	$(PYTHON) scripts/property_due_diligence/generate_blocker_handoff.py
	$(PYTHON) scripts/property_due_diligence/generate_hash_manifest.py

property-bridge-state:
	$(PYTHON) scripts/property_due_diligence/reconcile_bridge_state.py
	$(PYTHON) scripts/export_bridge_status.py

bridge-queue-append-dry-run:
	$(PYTHON) scripts/queue_append.py --queue exports/chatgpt_request_queue.jsonl --input reports/property_due_diligence/followup_queue_entries.jsonl --dry-run
