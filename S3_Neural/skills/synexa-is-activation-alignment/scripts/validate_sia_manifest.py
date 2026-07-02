#!/usr/bin/env python3
"""Light validator for SIA data source manifests."""
from __future__ import annotations
import sys
from pathlib import Path

REQUIRED = [
    "Active Files",
    "Outdated Files",
    "Misplaced Files",
    "Conflict Risks",
    "Required Updates",
]

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_sia_manifest.py <manifest.md>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Missing file: {path}", file=sys.stderr)
        return 2
    text = path.read_text(encoding="utf-8")
    missing = [item for item in REQUIRED if item.lower() not in text.lower()]
    if missing:
        print("Manifest missing sections: " + ", ".join(missing), file=sys.stderr)
        return 1
    print("SIA manifest structure OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
