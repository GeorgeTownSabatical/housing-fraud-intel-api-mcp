from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.property_due_diligence import official_record_intake

REPORT_DIR = ROOT / "reports" / "property_due_diligence"
TRACKED_PACKET = ROOT / "exports" / "tracked_surname_intersection_document_request_packet.json"
PULL_LIST = ROOT / "outputs" / "gis_model" / "assessor_office_pull_list.csv"
INTAKE_STATUS = REPORT_DIR / "official_record_intake_status.json"


def load_tracked_documents(path: Path = TRACKED_PACKET) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("documents", []))


def load_pull_list_row(apn: str, path: Path = PULL_LIST) -> dict[str, str]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("apn") == apn:
                return {key: str(value or "") for key, value in row.items()}
    return {}


def load_intake_status(path: Path = INTAKE_STATUS) -> dict[str, Any]:
    if not path.exists():
        return official_record_intake.build_status()
    return json.loads(path.read_text(encoding="utf-8"))


def write_tracked_recorder_handoff(path: Path = REPORT_DIR / "tracked_recorder_official_copy_handoff.md") -> None:
    docs = load_tracked_documents()
    status = load_intake_status().get("tracked_recorder_documents", {})
    lines = [
        "# Tracked Recorder Official Copy Handoff",
        "",
        "Status: blocked until official Orange County Recorder document images/details are obtained.",
        f"Intake status: `{status.get('matched_count', 0)}` of `{status.get('required_count', len(docs))}` required document numbers matched in `public_records/`.",
        "Scanner report: `reports/property_due_diligence/official_record_intake_status.md`",
        "",
        "Purpose: obtain source documents for PEPPER/LARSON intersection rows without treating index hits as identity, title, APN, ownership, or fraud proof.",
        "",
        "Request source: Orange County Clerk-Recorder official record copies.",
        "",
        "Documents to request:",
    ]
    for row in docs:
        lines.append(
            "- `{doc}` `{date}` `{type}` group=`{group}` portal_doc_id=`{portal}` parties=`{parties}`".format(
                doc=row.get("document_number", ""),
                date=row.get("recording_date", ""),
                type=row.get("document_type", ""),
                group=row.get("priority_group", ""),
                portal=row.get("portal_doc_id", ""),
                parties=row.get("indexed_parties", ""),
            )
        )
    lines.extend(
        [
            "",
            "Extraction checklist:",
            "- APN if present.",
            "- Full legal description.",
            "- Tract, lot, block, and map references.",
            "- Vesting and capacity language.",
            "- Related instruments.",
            "- Lender, beneficiary, trustee, title company, escrow, preparer, and notary details.",
            "- Correction, rerecording, release, reconveyance, or assignment language.",
            "",
            "Guardrail: no conclusions until official copies are attached and extracted.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_apn_401_handoff(path: Path = REPORT_DIR / "apn_40128307_official_records_handoff.md") -> None:
    row = load_pull_list_row("401-283-07")
    status = load_intake_status().get("apn_40128307", {})
    lines = [
        "# APN 401-283-07 Official Records Handoff",
        "",
        "Status: blocked until official assessor, recorder, and tax-default records are obtained.",
        f"Intake status: matched records `{status.get('matched_record_count', 0)}`, missing categories `{', '.join(status.get('missing_categories', [])) or 'none'}`.",
        "Scanner report: `reports/property_due_diligence/official_record_intake_status.md`",
        "",
        f"Local priority score: `{row.get('priority_score', 'UNKNOWN')}`",
        f"Local pull reasons: {row.get('pull_reason', 'UNKNOWN')}",
        "",
        "Records to request:",
    ]
    for record in [part.strip() for part in row.get("requested_records", "").split("|") if part.strip()]:
        lines.append(f"- {record}")
    lines.extend(
        [
            "",
            "Known local sources:",
            f"- {row.get('known_sources', 'UNKNOWN')}",
            "",
            "Open questions:",
            f"- {row.get('unresolved_questions', 'UNKNOWN')}",
            "",
            "Guardrail: local generated artifacts organize the request; they are not official proof of title, ownership, APN lineage, or tax disposition.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_encrypted_report_requirements(path: Path = REPORT_DIR / "encrypted_project_report_requirements.md") -> None:
    lines = [
        "# Encrypted Project Report Requirements",
        "",
        "Status: blocked until encryption inputs are supplied.",
        "",
        "Required before generating an encrypted report:",
        "- Recipient public key or approved encryption command.",
        "- Report scope: repo-only, cross-project, Bridge-only, or evidence-only.",
        "- Output target path and whether local-only or Bridge-publishable.",
        "- Redaction requirements for names, APNs, local paths, and operational details.",
        "- Confirmation that no private keys, tokens, credentials, or recovery material should be included.",
        "",
        "Default if no inputs are supplied: do not generate encrypted output.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_next_actions(path: Path = REPORT_DIR / "blocked_work_next_actions.md") -> None:
    status = load_intake_status()
    tracked = status.get("tracked_recorder_documents", {})
    apn = status.get("apn_40128307", {})
    lines = [
        "# Blocked Work Next Actions",
        "",
        "These are the only remaining blocked Bridge/property items after local implementation and validation.",
        "",
        "## 1. Tracked PEPPER/LARSON Recorder Documents",
        "",
        "- Blocked request IDs: `codex-pull-tracked-surname-intersection-docs-20260531`, `property-followup-tracked_surname_intersection_packet-20260531`",
        "- Handoff packet: `reports/property_due_diligence/tracked_recorder_official_copy_handoff.md`",
        "- Required external action: obtain official Orange County Recorder copies or document detail images for the 21 listed document numbers.",
        f"- Current intake status: `{tracked.get('matched_count', 0)}` of `{tracked.get('required_count', 21)}` required document numbers matched in `public_records/`.",
        "- Validation after receipt: extract APN, legal description, capacity language, parties, related instruments, and notary/title details.",
        "- Guardrail: index rows remain `UNKNOWN` until official copies are attached and extracted.",
        "",
        "## 2. APN 401-283-07 Official Records",
        "",
        "- Blocked request ID: `property-followup-apn_40128307_review_packet-20260531`",
        "- Handoff packet: `reports/property_due_diligence/apn_40128307_official_records_handoff.md`",
        "- Required external action: obtain official assessor parcel card/history, recorder instrument chain, and tax-default disposition records.",
        f"- Current intake status: matched records `{apn.get('matched_record_count', 0)}`, missing categories `{', '.join(apn.get('missing_categories', [])) or 'none'}`.",
        "- Validation after receipt: attach source files, hash them, then rerun `make property-due-diligence PYTHON=./.venv/bin/python`.",
        "- Guardrail: local packets organize questions; they do not establish title, ownership, APN lineage, or tax disposition.",
        "",
        "## 3. Encrypted Cross-Project Report",
        "",
        "- Blocked request ID: `bridge-encrypted-project-report-20260531-001`",
        "- Requirements stub: `reports/property_due_diligence/encrypted_project_report_requirements.md`",
        "- Required external action: provide recipient public key or approved encryption command, report scope, output target, and redaction rules.",
        "- Guardrail: do not generate encrypted output without explicit encryption inputs.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_summary(path: Path = REPORT_DIR / "blocked_work_handoff_summary.json") -> None:
    docs = load_tracked_documents()
    status = load_intake_status()
    summary = {
        "schema": "blocked_work_handoff_summary.v1",
        "tracked_recorder_documents": len(docs),
        "official_record_intake": {
            "apn_40128307_ready": status.get("apn_40128307", {}).get("ready_for_extraction", False),
            "status_path": "reports/property_due_diligence/official_record_intake_status.json",
            "extraction_queue_path": "reports/property_due_diligence/official_record_extraction_queue.jsonl",
            "tracked_recorder_ready": status.get("tracked_recorder_documents", {}).get("ready_for_extraction", False),
        },
        "outputs": [
            "reports/property_due_diligence/official_record_intake_status.json",
            "reports/property_due_diligence/official_record_intake_status.md",
            "reports/property_due_diligence/official_record_extraction_queue.jsonl",
            "reports/property_due_diligence/official_record_extraction_queue.md",
            "reports/property_due_diligence/blocked_work_next_actions.md",
            "reports/property_due_diligence/tracked_recorder_official_copy_handoff.md",
            "reports/property_due_diligence/apn_40128307_official_records_handoff.md",
            "reports/property_due_diligence/encrypted_project_report_requirements.md",
        ],
        "guardrail": "Handoff files request external records or encryption inputs; they do not resolve the underlying facts.",
    }
    path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    official_record_intake.write_outputs()
    write_tracked_recorder_handoff()
    write_apn_401_handoff()
    write_encrypted_report_requirements()
    write_next_actions()
    write_summary()
    print(REPORT_DIR / "blocked_work_handoff_summary.json")


if __name__ == "__main__":
    main()
