#!/usr/bin/env python3
"""Create a deterministic initial repair plan from audit findings."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

AUTO_TERMS = {
    "structure", "path", "schema", "syntax", "format", "weight",
    "nan", "inf", "duplicate", "boundary", "security", "unsafe",
    "version", "checksum", "dependency", "package", "solver",
}
ABANDON_TERMS = {
    "non_bio", "not biological", "gold provenance", "gold source",
    "unavailable core data", "private data", "controlled data",
    "underdetermined", "insufficient input", "missing manual curation",
    "historical database", "cannot define fair scoring",
}


def read_jsonl(path: Path) -> list[dict]:
    output: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            stripped = line.strip()
            if not stripped:
                continue
            value = json.loads(stripped)
            if not isinstance(value, dict):
                raise ValueError(f"Line {line_no} is not an object")
            output.append(value)
    return output


def newest_work(root: Path) -> Path:
    parent = root / ".benchmark_repair_tmp"
    candidates = [p for p in parent.iterdir() if p.is_dir()]
    if not candidates:
        raise FileNotFoundError("No prepared repair workspace")
    return max(candidates, key=lambda p: p.stat().st_mtime)


def classify(finding: dict) -> tuple[str, str]:
    text = " ".join(
        str(finding.get(key, ""))
        for key in ("category", "title", "observation", "impact", "required_fix")
    ).lower()
    severity = str(finding.get("severity", "")).upper()
    if any(term in text for term in ABANDON_TERMS):
        return "ABANDON", "The root cause lacks a reliable evidence-based repair path."
    if severity == "FATAL" and any(term in text for term in ("gold", "core data", "underdetermined")):
        return "ABANDON", "A FATAL scientific-definition or core-data failure should not be guessed."
    if any(re.search(rf"\b{re.escape(term)}\b", text) for term in AUTO_TERMS):
        return "AUTO_FIX", "The intended correction is deterministic and regression-testable."
    return "ASSISTED_FIX", "The issue appears repairable but requires evidence-guided interpretation."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark_root", type=Path)
    parser.add_argument("--work-dir", type=Path)
    args = parser.parse_args()

    root = args.benchmark_root.resolve()
    work = args.work_dir.resolve() if args.work_dir else newest_work(root)
    findings = read_jsonl(root / "benchmark_audit" / "findings.jsonl")
    context = json.loads((work / ".repair_context.json").read_text(encoding="utf-8"))

    items = []
    for index, finding in enumerate(findings, 1):
        disposition, reason = classify(finding)
        finding_id = str(finding.get("finding_id") or f"FINDING-{index:03d}")
        items.append(
            {
                "finding_id": finding_id,
                "severity": str(finding.get("severity", "UNKNOWN")),
                "category": str(finding.get("category", "unknown")),
                "title": str(finding.get("title", "")),
                "disposition": disposition,
                "reason": reason,
                "target_files": finding.get("affected_files", []),
                "depends_on": [],
                "tests": [],
                "status": "PLANNED",
            }
        )

    plan = {
        "schema_version": "1.0",
        "repair_id": context["repair_id"],
        "parent_audit_id": context["parent_audit_id"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "items": items,
    }
    (work / "repair_plan.json").write_text(
        json.dumps(plan, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Benchmark Repair Plan",
        "",
        f"- Repair ID: `{context['repair_id']}`",
        f"- Parent audit: `{context['parent_audit_id']}`",
        f"- Findings: {len(items)}",
        "",
        "| Finding | Severity | Category | Disposition | Reason |",
        "|---|---|---|---|---|",
    ]
    for item in items:
        title = item["title"].replace("|", "\\|")
        reason = item["reason"].replace("|", "\\|")
        lines.append(
            f"| {item['finding_id']} | {item['severity']} | {item['category']} | "
            f"{item['disposition']} | {title}: {reason} |"
        )
    (work / "repair_plan.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    report_path = work / "repair_report.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["selected_findings"] = [item["finding_id"] for item in items]
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"work_dir": str(work), "finding_count": len(items)}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
