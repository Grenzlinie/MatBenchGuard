#!/usr/bin/env python3
"""Validate and atomically publish a benchmark audit bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

REQUIRED_FILES = [
    "audit_report.md",
    "audit_report.json",
    "findings.jsonl",
    "resource_checks.json",
    "checker_tests.json",
    "audit_manifest.json",
    "logs/audit.log",
]
REQUIRED_HEADINGS = [
    "# Benchmark Audit Report",
    "## 1. Audit Summary",
    "## 2. Benchmark Identity",
    "## 3. Audit Configuration",
    "## 4. Final Verdict",
    "## 5. Biology Qualification",
    "## 6. Capability Alignment",
    "## 7. Gate Results",
    "## 8. Resource Reachability",
    "## 9. Instruction and Task Design",
    "## 10. Checker Assessment",
    "## 11. Gold Standard Assessment",
    "## 12. Execution Feasibility",
    "## 13. Reproducibility and Leakage",
    "## 14. Paper Consistency",
    "## 15. Dimension Scores",
    "## 16. Findings",
    "## 17. Required Fixes",
    "## 18. Recommended Improvements",
    "## 19. Audit Scope and Limitations",
    "## 20. Audit Log Summary",
]
VERDICTS = {"PASS", "CONDITIONAL", "REJECT", "NOT_ASSESSABLE"}
BIOLOGY = {"BIO_CORE", "BIO_METHOD", "BIO_WRAPPER", "NON_BIO", "AMBIGUOUS"}
ANSWER_TYPES = {"DETERMINISTIC_EXACT", "TOLERANCE_BASED", "SET_VALUED", "RANKING_BASED", "EVIDENCE_BASED", "OPEN_ENDED"}
GATE_STATES = {"PASS", "FAIL", "WARNING", "SKIPPED", "NOT_ASSESSED"}
SEVERITIES = {"FATAL", "HIGH", "MEDIUM", "LOW"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def parse_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def parse_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path.name}:{number} is not a JSON object")
        rows.append(value)
    return rows


def markdown_value(text: str, label: str) -> str | None:
    pattern = re.compile(rf"^\s*[-*]?\s*{re.escape(label)}\s*:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(text)
    return match.group(1).strip() if match else None


def collect_evidence_paths(value: Any, paths: list[str]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"evidence_path", "artifact_path", "log_path"} and isinstance(item, str):
                paths.append(item)
            collect_evidence_paths(item, paths)
    elif isinstance(value, list):
        for item in value:
            collect_evidence_paths(item, paths)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark_root", help="benchmark root containing .benchmark_audit_tmp")
    args = parser.parse_args()

    try:
        root = Path(args.benchmark_root).expanduser().resolve()
        temp_dir = root / ".benchmark_audit_tmp"
        final_dir = root / "benchmark_audit"
        if not temp_dir.is_dir():
            raise FileNotFoundError(temp_dir)
        if final_dir.exists():
            raise FileExistsError(f"final audit directory already exists: {final_dir}")

        missing = [name for name in REQUIRED_FILES if not (temp_dir / name).exists()]
        if missing:
            raise ValueError(f"missing required audit files: {missing}")

        report = parse_json(temp_dir / "audit_report.json")
        resources = parse_json(temp_dir / "resource_checks.json")
        checker = parse_json(temp_dir / "checker_tests.json")
        findings = parse_jsonl(temp_dir / "findings.jsonl")
        manifest = parse_json(temp_dir / "audit_manifest.json")
        markdown = (temp_dir / "audit_report.md").read_text(encoding="utf-8")

        last = -1
        for heading in REQUIRED_HEADINGS:
            pos = markdown.find(heading)
            if pos < 0:
                raise ValueError(f"missing Markdown heading: {heading}")
            if pos <= last:
                raise ValueError(f"Markdown heading is out of order: {heading}")
            last = pos

        summary = report.get("summary", {})
        verdict = summary.get("final_verdict")
        biology = summary.get("biology_class")
        answer_type = summary.get("answer_type")
        if verdict not in VERDICTS:
            raise ValueError(f"invalid final verdict: {verdict}")
        if biology not in BIOLOGY:
            raise ValueError(f"invalid biology class: {biology}")
        if answer_type not in ANSWER_TYPES:
            raise ValueError(f"invalid answer type: {answer_type}")

        for gate in report.get("gate_results", []):
            if gate.get("status") not in GATE_STATES:
                raise ValueError(f"invalid gate status: {gate}")
        for finding in findings:
            if finding.get("severity") not in SEVERITIES:
                raise ValueError(f"invalid finding severity: {finding.get('finding_id')}")

        report_findings = report.get("findings", [])
        if len(report_findings) != len(findings):
            raise ValueError("finding count differs between audit_report.json and findings.jsonl")
        expected_ids = [f"FINDING-{i:03d}" for i in range(1, len(findings) + 1)]
        actual_ids = [str(item.get("finding_id")) for item in findings]
        if actual_ids != expected_ids:
            raise ValueError(f"finding IDs must be consecutive: expected {expected_ids}, got {actual_ids}")

        md_checks = {
            "Audit ID": report.get("audit_id"),
            "Final verdict": verdict,
            "Biology class": biology,
            "Answer type": answer_type,
        }
        for label, expected in md_checks.items():
            observed = markdown_value(markdown, label)
            if observed is None:
                raise ValueError(f"audit_report.md must include '{label}: ...' in the summary")
            if str(observed) != str(expected):
                raise ValueError(f"Markdown/JSON mismatch for {label}: {observed!r} != {expected!r}")

        evidence_paths: list[str] = []
        collect_evidence_paths(report, evidence_paths)
        collect_evidence_paths(resources, evidence_paths)
        collect_evidence_paths(checker, evidence_paths)
        collect_evidence_paths(findings, evidence_paths)
        for value in sorted(set(evidence_paths)):
            path = Path(value)
            candidate = path if path.is_absolute() else temp_dir / path
            if not candidate.exists():
                raise ValueError(f"referenced evidence path does not exist: {value}")

        completed_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        report.setdefault("configuration", {})["completed_at"] = completed_at
        (temp_dir / "audit_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

        manifest["completed_at"] = completed_at
        output_hashes: dict[str, str] = {}
        for path in temp_dir.rglob("*"):
            if not path.is_file() or path.name in {"audit_manifest.json", "audit_context.json"}:
                continue
            rel = path.relative_to(temp_dir).as_posix()
            output_hashes[rel] = sha256_file(path)
        manifest["output_hashes"] = dict(sorted(output_hashes.items()))
        manifest["new_findings"] = actual_ids
        (temp_dir / "audit_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

        with (temp_dir / "logs/audit.log").open("a", encoding="utf-8") as log:
            log.write(f"{completed_at}\tINFO\taudit validated and finalized\tverdict={verdict}\n")

        context = temp_dir / "audit_context.json"
        if context.exists():
            context.unlink()
        temp_dir.rename(final_dir)
        print(json.dumps({"benchmark_root": str(root), "audit_dir": str(final_dir), "verdict": verdict}, indent=2))
        return 0
    except Exception as exc:
        print(f"finalize audit output failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
