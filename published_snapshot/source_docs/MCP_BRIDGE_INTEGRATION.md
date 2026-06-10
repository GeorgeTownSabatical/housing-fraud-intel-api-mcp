# MCP Bridge Integration

MCP is now treated as a Bridge transport and context layer.

The rule is simple:

```text
MCP may read Bridge/evidence status and write proposed requests to Bridge.
Codex still validates, processes, attests, and publishes.
```

## GitHub MCP

The GitHub MCP connector can read:

```text
https://github.com/aevespers2/Bridge/blob/main/exports/chatgpt_request_queue.jsonl
https://github.com/aevespers2/Bridge/blob/main/reports/latest_bridge_run.json
```

It may update:

```text
aevespers2/Bridge/exports/chatgpt_request_queue.jsonl
```

`queues/chatgpt_codex_work_queue.jsonl` is legacy context only. The canonical intake rule is defined upstream in
`aevespers2/Bridge/docs/BRIDGE_INTAKE_CANONICAL.md`; actionable requests must enter through
`exports/chatgpt_request_queue.jsonl`.

MCP clients should append structured queue requests rather than changing evidence outputs.

Codex may also append structured requests through:

```bash
python scripts/enqueue_bridge_request.py --title "Bridge follow-up" --instructions "Describe the task." --publish
```

The script validates the canonical envelope before writing and records Codex as `provenance.producer`.

## Local MCP Context Export

Generate the MCP-readable context packet:

```bash
python scripts/export_mcp_bridge_context.py
```

Output:

```text
exports/bridge_status/mcp_bridge_context.json
```

The context includes:

- Bridge read targets.
- Bridge queue write target.
- latest queue/status counts.
- command result counts.
- UVIP attestation summary.
- local artifact paths.
- safety rules.

## Trust Boundary

MCP is not an evidence authority. It does not prove parcel facts, identity links, misconduct, or title conclusions. It only improves transport, status visibility, and structured request handoff.

All MCP-originated writes must pass:

- Bridge queue schema validation.
- local request processing.
- safe command allowlist if commands are requested.
- UVIP attestation during routine checks.
