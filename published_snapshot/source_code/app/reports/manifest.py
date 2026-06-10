from pathlib import Path

from app.utils.hashing import stable_hash


def build_manifest(paths: list[Path]) -> dict:
    return {
        "files": [
            {"path": str(path), "hash": stable_hash(path.read_text(encoding="utf-8", errors="ignore"))}
            for path in paths
        ]
    }
