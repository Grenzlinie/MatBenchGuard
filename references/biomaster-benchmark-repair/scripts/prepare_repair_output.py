#!/usr/bin/env python3
"""Prepare an isolated benchmark repair output workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

REQUIRED_AUDIT = ("audit_report.json", "findings.jsonl")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return f"sha256:{h.hexdigest()}"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark_root", type=Path)
    parser.add_argument(
        "--mode",
        choices=("PLAN_ONLY", "SAFE_AUTO_FIX", "ASSISTED_FIX"),
        default="SAFE_AUTO_FIX",
    )
    args = parser.parse_args()

    root = args.benchmark_root.resolve()
    audit_dir = root / "benchmark_audit"
    missing = [name for name in REQUIRED_AUDIT if not (audit_dir / name).is_file()]
    if missing:
        raise SystemExit(f"Missing required audit files: {', '.join(missing)}")

    audit_report = load_json(audit_dir / "audit_report.json")
    audit_id = str(audit_report.get("audit_id") or "unknown")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    repair_id = f"repair-{stamp}-{uuid.uuid4().hex[:8]}"
    temp_parent = root / ".benchmark_repair_tmp"
    work = temp_parent / repair_id
    work.mkdir(parents=True, exist_ok=False)
    for directory in ("patches", "evidence", "logs"):
        (work / directory).mkdir()

    skill_root = Path(__file__).resolve().parents[1]
    assets = skill_root / "assets"
    shutil.copy2(assets / "repair_summary_template.md", work / "repair_summary.md")
    shutil.copy2(assets / "repair_report_template.json", work / "repair_report.json")
    shutil.copy2(assets / "regression_tests_template.json", work / "regression_tests.json")
    shutil.copy2(
        assets / "re_audit_comparison_template.json",
        work / "re_audit_comparison.json",
    )

    for name in (
        "repair_plan.md",
        "changes.jsonl",
        "unresolved_findings.jsonl",
    ):
        (work / name).write_text("", encoding="utf-8")
    (work / "repair_plan.json").write_text("{}\n", encoding="utf-8")

    context = {
        "schema_version": "1.0",
        "repair_id": repair_id,
        "parent_audit_id": audit_id,
        "benchmark_root": str(root),
        "mode": args.mode,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "audit_hashes": {
            name: sha256_file(audit_dir / name)
            for name in REQUIRED_AUDIT
        },
    }
    (work / ".repair_context.json").write_text(
        json.dumps(context, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (work / "logs" / "repair.log").write_text(
        f"{context['started_at']} prepared {repair_id} mode={args.mode}\n",
        encoding="utf-8",
    )

    report_path = work / "repair_report.json"
    report = load_json(report_path)
    report["repair_id"] = repair_id
    report["parent_audit_id"] = audit_id
    report["benchmark"] = {"name": root.name, "root": str(root)}
    report["configuration"] = {
        "mode": args.mode,
        "started_at": context["started_at"],
        "completed_at": "",
    }
    before_verdict = audit_report.get("summary", {}).get("final_verdict", "")
    report["summary"]["before_verdict"] = before_verdict
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps({"repair_id": repair_id, "work_dir": str(work)}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
