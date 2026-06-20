#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

if [[ -z "${VIRTUAL_ENV:-}" ]]; then
  "${PYTHON_BIN}" -m venv .venv
  PYTHON_BIN=".venv/bin/python"
fi

"${PYTHON_BIN}" -m pip install -e ".[dev]"
"${PYTHON_BIN}" -m pytest
