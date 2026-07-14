#!/usr/bin/env python3
"""Validate the fixed-format benchmark repair output."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED = (
    "repair_summary.md",
    "repair_report.json",
    "repair_plan.md",
    "repair_plan.json",
    "changes.jsonl",
    "unresolved_findings.jsonl",
    "regression_tests.json",
    "re_audit_comparison.json",
    "logs/repair.log",
)
STATUSES = {"REPAIRED", "PARTIALLY_REPAIRED", "ABANDONED", "ROLLED_BACK"}
HEADINGS = [
    "# Benchmark Repair Report",
    "## 1. Repair Summary",
    "## 2. Input Audit",
    "## 3. Repair Configuration",
    "## 4. Findings Selected",
    "## 5. Applied Changes",
    "## 6. Abandoned or Unrepairable Findings",
    "## 7. Regression Test Results",
    "## 8. Re-audit Comparison",
    "## 9. Unresolved Findings",
    "## 10. Rollback Status",
    "## 11. Scope and Limitations",
    "## 12. Repair Log Summary",
]


def parse_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_jsonl(path: Path) -> None:
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if line.strip():
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise ValueError(f"{path}:{line_no} is not a JSON object")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repair_dir", type=Path)
    parser.add_argument("--expected-status", choices=sorted(STATUSES))
    args = parser.parse_args()
    root = args.repair_dir.resolve()

    errors: list[str] = []
    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing {rel}")
    for directory in ("patches", "evidence", "logs"):
        if not (root / directory).is_dir():
            errors.append(f"missing directory {directory}")

    if not errors:
        try:
            report = parse_json(root / "repair_report.json")
            parse_json(root / "repair_plan.json")
            parse_json(root / "regression_tests.json")
            parse_json(root / "re_audit_comparison.json")
            validate_jsonl(root / "changes.jsonl")
            validate_jsonl(root / "unresolved_findings.jsonl")
            status = report.get("summary", {}).get("repair_status")
            if status not in STATUSES:
                errors.append(f"invalid repair_status {status!r}")
            if args.expected_status and status != args.expected_status:
                errors.append(
                    f"repair_status {status!r} != expected {args.expected_status!r}"
                )
            if status == "ABANDONED" and not (root / "abandoned_findings.jsonl").is_file():
                errors.append("ABANDONED output requires abandoned_findings.jsonl")
            if status == "REPAIRED" and not report.get("summary", {}).get("publishable"):
                errors.append("REPAIRED output must set publishable=true")
            if status in {"ABANDONED", "ROLLED_BACK"} and report.get("summary", {}).get("publishable"):
                errors.append(f"{status} output must set publishable=false")
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(str(exc))

        summary = (root / "repair_summary.md").read_text(encoding="utf-8")
        positions = []
        for heading in HEADINGS:
            pos = summary.find(heading)
            if pos < 0:
                errors.append(f"missing heading {heading}")
            positions.append(pos)
        valid_positions = [p for p in positions if p >= 0]
        if valid_positions != sorted(valid_positions):
            errors.append("repair_summary.md headings are out of order")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(json.dumps({"valid": True, "repair_dir": str(root)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
