import json

from housing_fraud_intel_mcp import server


def test_compact_bridge_summary_reads_expected_artifacts(tmp_path, monkeypatch):
    root = tmp_path
    (root / "exports/bridge_status").mkdir(parents=True)
    (root / "exports/bridge_status/latest_bridge_run.json").write_text(
        json.dumps(
            {
                "generated_at": "2026-06-07T00:00:00Z",
                "repo": "aevespers2/Bridge",
                "imported_count": 1,
                "processed_count": 1,
                "accepted_count": 1,
                "rejected_count": 0,
                "blocked_count": 0,
                "routine_check": {"exit_status": "success", "counts": {"succeeded": 1}},
                "validation_summary": {"status_counts": {"UNKNOWN": 1}},
                "identity_attestation": {"verification_summary": {"hash_chain_present": True}},
            }
        )
    )
    (root / "exports/bridge_status/bridge_queue_workboard.json").write_text(
        json.dumps({"summary": {"completed": 1}})
    )
    monkeypatch.setenv("HFI_ROOT", str(root))

    summary = server.compact_bridge_summary()

    assert summary["repo"] == "aevespers2/Bridge"
    assert summary["counts"]["accepted"] == 1
    assert summary["identity"]["hash_chain_present"] is True
