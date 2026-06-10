#!/usr/bin/env python3
"""
Validate a Synexa iS cross-workspace handoff package.

Version: v0.1.2
Effective Date: 2026-06-10
Maintainer: iS-Matrix

Usage:
    python scripts/validate_handoff.py path/to/handoff.md
"""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "Task Name",
    "Original User Intent",
    "Current Workspace Judgment",
    "Collaboration Trigger",
    "Main Owner",
    "Collaborators",
    "Completed Inputs",
    "Downstream Tasks",
    "Output Requirements",
    "Return Feedback Requirement",
]


def normalize_heading(line: str) -> str:
    """Return a markdown heading text without leading # characters."""
    stripped = line.strip()
    while stripped.startswith("#"):
        stripped = stripped[1:].strip()
    return stripped.rstrip(":").strip()


def extract_headings(markdown_text: str) -> list[str]:
    """Extract markdown headings from text."""
    headings = []
    for line in markdown_text.splitlines():
        if line.lstrip().startswith("#"):
            headings.append(normalize_heading(line))
    return headings


def validate_handoff(path: Path) -> list[str]:
    """Return a list of missing required fields."""
    text = path.read_text(encoding="utf-8")
    headings = extract_headings(text)

    missing = []
    for field in REQUIRED_FIELDS:
        if not any(field.lower() in heading.lower() for heading in headings):
            missing.append(field)

    return missing


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python validate_handoff.py path/to/handoff.md")
        return 2

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"error: file not found: {path}")
        return 2

    if not path.is_file():
        print(f"error: not a file: {path}")
        return 2

    try:
        missing = validate_handoff(path)
    except UnicodeDecodeError:
        print("error: file must be utf-8 encoded markdown")
        return 2
    except OSError as exc:
        print(f"error: unable to read file: {exc}")
        return 2

    if missing:
        print("missing fields:")
        for field in missing:
            print(f"- {field}")
        return 1

    print("validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
