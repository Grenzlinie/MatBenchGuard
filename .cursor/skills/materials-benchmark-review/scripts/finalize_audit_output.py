#!/usr/bin/env python3
"""Synthesize, validate, and safely replace a materials audit bundle."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from audit_package import SEVERITY_RANK
from prepare_audit_output import REQUIRED_ROLES, sha256_file


VERDICTS = {"PASS", "CONDITIONAL", "REJECT", "NOT_ASSESSABLE"}
MATERIALS_CLASSES = {
    "MAT_CORE",
    "MAT_METHOD",
    "MAT_WRAPPER",
    "NON_MAT",
    "AMBIGUOUS",
}
ANSWER_TYPES = {
    "DETERMINISTIC_EXACT",
    "TOLERANCE_BASED",
    "SET_VALUED",
    "RANKING_BASED",
    "EVIDENCE_BASED",
    "OPEN_ENDED",
}
REQUIRED_AUDIT_FILES = {
    "audit_report.md",
    "audit_report.json",
    "findings.jsonl",
    "resource_checks.json",
    "checker_tests.json",
    "audit_manifest.json",
    "logs/audit.log",
}
REQUIRED_HEADINGS = [
    "# Materials Benchmark Audit Report",
    "## 1. Audit Summary",
    "## 2. Benchmark Identity",
    "## 3. Audit Configuration",
    "## 4. Final Verdict",
    "## 5. Materials Qualification",
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


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def answer_type_for(root: Path) -> str:
    try:
        specification = read_json(root / "tests/grading_spec.json")
    except (OSError, ValueError, json.JSONDecodeError):
        return "OPEN_ENDED"
    if not isinstance(specification, dict):
        return "OPEN_ENDED"
    contract = specification.get("output_contract", {})
    if not isinstance(contract, dict):
        return "OPEN_ENDED"
    outputs = contract.get("outputs", [])
    if not isinstance(outputs, list):
        return "OPEN_ENDED"
    policies = {
        str(item.get("target_policy", ""))
        for item in outputs
        if isinstance(item, dict)
    }
    if "metric_recompute" in policies or "reference_match" in policies:
        return "TOLERANCE_BASED"
    if "exact_match" in policies:
        return "DETERMINISTIC_EXACT"
    if "structural_audit" in policies:
        return "EVIDENCE_BASED"
    return "OPEN_ENDED"


def normalized_finding(
    source: dict[str, Any], finding_id: str, phase: str, category: str
) -> dict[str, Any]:
    affected_files = source.get("affected_files", [])
    if not affected_files and phase == "E1":
        affected_files = ["tests/checker.py", "tests/grading_spec.json"]
    return {
        "finding_id": finding_id,
        "severity": source["severity"],
        "category": category,
        "phase": phase,
        "status": "OPEN",
        "title": source["code"],
        "affected_files": affected_files,
        "observation": source["message"],
        "evidence": source.get("evidence", {}),
        "impact": "The Harbor 题包 may be invalid, unfair, or unreliable.",
        "failure_scenario": source.get("test_type", source["code"]),
        "required_fix": "Resolve the observed contract or checker defect.",
        "verification_after_fix": "Re-run the failing check at the same evidence depth.",
        "confidence": "HIGH",
        "judgment_type": "FACT",
    }


def classify_verdict(
    findings: list[dict[str, Any]],
    usable_reward_count: int,
    checker_test_count: int,
) -> tuple[str, float | None, str]:
    maximum = max(
        (SEVERITY_RANK[item["severity"]] for item in findings), default=0
    )
    if maximum >= SEVERITY_RANK["FATAL"]:
        return (
            "REJECT",
            0.0,
            "A FATAL no-paper E1 finding triggered a Hard gate.",
        )
    if usable_reward_count != checker_test_count:
        return (
            "NOT_ASSESSABLE",
            None,
            "At least one checker probe lacks usable finite numeric E1 evidence.",
        )
    if maximum >= SEVERITY_RANK["MEDIUM"]:
        return (
            "CONDITIONAL",
            0.7,
            "Repairable no-paper E1 findings remain.",
        )
    return (
        "PASS",
        0.9,
        "No blocking no-paper E1 finding was detected.",
    )


def gate_status(
    findings: list[dict[str, Any]], phase: str
) -> str:
    relevant = [item for item in findings if item["phase"] == phase]
    if any(item["severity"] == "FATAL" for item in relevant):
        return "FAIL"
    if relevant:
        return "WARNING"
    return "PASS"


def execution_findings(
    execution_evidence: dict[str, Any],
) -> list[dict[str, Any]]:
    if (
        execution_evidence.get("claim") == "SMOKE_RUN"
        and execution_evidence.get("status") == "FAIL"
    ):
        return [
            {
                "severity": "FATAL",
                "code": "E2_SMOKE_FAILED",
                "message": execution_evidence.get(
                    "reason", "The E2 smoke failed."
                ),
                "test_type": "E2_SMOKE",
                "evidence": execution_evidence,
                "affected_files": [],
            }
        ]
    return []


def markdown_summary(report: dict[str, Any]) -> str:
    summary = report["summary"]
    configuration = report["configuration"]
    finding_lines = (
        "\n".join(
            f"- {item['finding_id']} [{item['severity']}] {item['title']}: "
            f"{item['observation']}"
            for item in report["findings"]
        )
        or "No findings."
    )
    gate_lines = "\n".join(
        f"- {gate['gate_id']}: {gate['status']}"
        for gate in report["gate_results"]
    )
    execution = report["execution_evidence"]
    if execution["claim"] == "SMOKE_RUN":
        checker_assessment = (
            "The real checker executed before the E2 smoke."
        )
        execution_assessment = (
            f"Status: E2_SMOKE\nReason: {execution['reason']}"
        )
    elif report["checker_tests"]:
        checker_assessment = (
            "The real checker executed in a solution-free runtime."
        )
        execution_assessment = (
            "Status: E1_ONLY\n"
            "Reason: The checker ran, but the scientific workflow did not."
        )
    else:
        checker_assessment = (
            "Status: NOT_ASSESSED\n"
            "Reason: An E0 FATAL gate prevented checker execution."
        )
        execution_assessment = (
            "Status: E0_ONLY\n"
            "Reason: E1 was skipped after an E0 FATAL gate."
        )
    resource_lines = (
        "\n".join(
            f"- {item['resource_id']}: {item['status']} "
            f"({item['verified_level']}/{item['required_level']})"
            for item in report["resources"]
        )
        or "No resources were declared."
    )
    return f"""# Materials Benchmark Audit Report

## 1. Audit Summary

- Audit ID: {report['audit_id']}
- Benchmark: {report['benchmark']['name']}
- Paper mode: {configuration['paper_mode']}
- Execution level: {configuration['execution_level']}
- Materials class: {summary['materials_class']}
- Answer type: {summary['answer_type']}
- Final verdict: {summary['final_verdict']}
- Weighted score: {summary['total_score']}
- Core reason: {summary['core_reason']}

## 2. Benchmark Identity

- Root: {report['benchmark']['root']}

## 3. Audit Configuration

- Paper mode: {configuration['paper_mode']}
- Execution level: {configuration['execution_level']}

## 4. Final Verdict

{summary['final_verdict']}: {summary['core_reason']}

## 5. Materials Qualification

- Class: {summary['materials_class']}
- Prescreen evidence is recorded in the static evidence.

## 6. Capability Alignment

Status: PARTIAL
Reason: This slice checks declared outputs and grading references.

## 7. Gate Results

{gate_lines}

## 8. Resource Reachability

{resource_lines}

## 9. Instruction and Task Design

Cross-file output consistency was checked statically.

## 10. Checker Assessment

{checker_assessment}

## 11. Gold Standard Assessment

Status: NOT_ASSESSED
Reason: Gold provenance requires paper-grounded review.

## 12. Execution Feasibility

{execution_assessment}

## 13. Reproducibility and Leakage

Solution content was not inspected or copied into the checker runtime.

## 14. Paper Consistency

Status: NOT_ASSESSED
Reason: No-paper mode does not assess paper fidelity.

## 15. Dimension Scores

Initial slice only; complete weighted dimensions are implemented later.

## 16. Findings

{finding_lines}

## 17. Required Fixes

See each finding's required_fix field.

## 18. Recommended Improvements

Run paper-grounded and task-family-specific slices before production admission.

## 19. Audit Scope and Limitations

This audit covers no-paper E1 behavior only.

## 20. Audit Log Summary

The fixed bundle was synthesized, validated, and published with rollback.
"""


def synthesize_report(
    root: Path,
    temp_dir: Path,
    static_result: dict[str, Any],
    checker_result: dict[str, Any],
    resource_result: dict[str, Any] | None = None,
    execution_evidence: dict[str, Any] | None = None,
) -> dict[str, Any]:
    resource_result = resource_result or {
        "status": "NOT_ASSESSED",
        "resources": [],
        "findings": [],
        "limitations": [],
    }
    execution_evidence = execution_evidence or {
        "status": "NOT_ASSESSED",
        "claim": "E1_CHECKER_ONLY",
        "scientific_reproduction": False,
        "reason": "Scientific workflow execution was not assessed.",
    }
    sources = [
        (item, "E0", "PACKAGE_STATIC")
        for item in static_result["issues"]
    ] + [
        (item, "E1", "CHECKER_ROBUSTNESS")
        for item in checker_result["findings"]
    ] + [
        (item, "RESOURCE", "RESOURCE_USABILITY")
        for item in resource_result["findings"]
    ] + [
        (item, "E2", "EXECUTION_FEASIBILITY")
        for item in execution_findings(execution_evidence)
    ]
    findings = [
        normalized_finding(
            source, f"FINDING-{index:03d}", phase, category
        )
        for index, (source, phase, category) in enumerate(sources, start=1)
    ]
    verdict, score, reason = classify_verdict(
        findings,
        checker_result["usable_reward_count"],
        len(checker_result["tests"]),
    )
    report = read_json(temp_dir / "audit_report.json")
    report["summary"] = {
        "materials_class": static_result["materials_prescreen"][
            "classification"
        ],
        "answer_type": answer_type_for(root),
        "final_verdict": verdict,
        "total_score": score,
        "hard_gate_triggered": any(
            item["severity"] == "FATAL" for item in findings
        ),
        "core_reason": reason,
    }
    report["materials_qualification"] = {
        "axes": static_result["materials_prescreen"]["axes_present"],
        "prescreen": static_result["materials_prescreen"],
    }
    report["paper_consistency"] = {
        "status": "NOT_ASSESSED",
        "reason": "No-paper mode does not assess paper fidelity.",
    }
    report["resources"] = resource_result["resources"]
    report["execution_evidence"] = execution_evidence
    e0_status = gate_status(findings, "E0")
    e1_status = (
        gate_status(findings, "E1")
        if checker_result["tests"]
        else "NOT_ASSESSED"
    )
    report["gate_results"] = [
        {"gate_id": "PACKAGE_STRUCTURE", "status": e0_status},
        {
            "gate_id": "MATERIALS_PRESCREEN",
            "status": (
                "WARNING"
                if report["summary"]["materials_class"]
                in {"NON_MAT", "AMBIGUOUS"}
                else "PASS"
            ),
        },
        {"gate_id": "CHECKER_ROBUSTNESS", "status": e1_status},
        {
            "gate_id": "RESOURCE_USABILITY",
            "status": (
                "NOT_ASSESSED"
                if resource_result["status"] == "NOT_ASSESSED"
                else gate_status(findings, "RESOURCE")
            ),
        },
        {
            "gate_id": "EXECUTION_FEASIBILITY",
            "status": (
                gate_status(findings, "E2")
                if execution_evidence["claim"] == "SMOKE_RUN"
                else "NOT_ASSESSED"
            ),
        },
        {"gate_id": "PAPER_CONSISTENCY", "status": "NOT_ASSESSED"},
    ]
    report["dimension_scores"] = [
        {
            "dimension": "package_integrity",
            "score": 1.0 if e0_status == "PASS" else 0.5,
        },
        {
            "dimension": "checker_robustness",
            "score": (
                "NOT_ASSESSED"
                if e1_status == "NOT_ASSESSED"
                else 1.0
                if e1_status == "PASS"
                else 0.0
            ),
        },
    ]
    report["checker_tests"] = checker_result["tests"]
    report["findings"] = findings
    report["required_fixes"] = [
        item["required_fix"] for item in findings
    ]
    report["scope"] = {
        "files_reviewed": sorted(
            role for role in REQUIRED_ROLES if (root / role).exists()
        ),
        "files_not_reviewed": ["paper/paper.md", "solution/**"],
        "tests_executed": [
            *[item["test_type"] for item in checker_result["tests"]],
            *(
                ["E2_SMOKE"]
                if execution_evidence["claim"] == "SMOKE_RUN"
                else []
            ),
        ],
        "tests_skipped": [
            *(
                ["checker dynamic probes due to an E0 FATAL gate"]
                if not checker_result["tests"]
                else []
            ),
            "paper fidelity",
            *(
                ["scientific workflow execution"]
                if execution_evidence["claim"] != "SMOKE_RUN"
                else []
            ),
            "task-family-specific metamorphic tests",
        ],
        "limitations": [
            *static_result["limitations"],
            *checker_result["limitations"],
            *resource_result["limitations"],
        ],
        "assumptions": [
            "known-valid output, when supplied, is independently justified"
        ],
        "solution_content_inspected": False,
    }
    (temp_dir / "audit_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (temp_dir / "audit_report.md").write_text(
        markdown_summary(report), encoding="utf-8"
    )
    (temp_dir / "findings.jsonl").write_text(
        "".join(
            json.dumps(item, ensure_ascii=False) + "\n"
            for item in findings
        ),
        encoding="utf-8",
    )
    return report


def markdown_value(text: str, label: str) -> str | None:
    match = re.search(
        rf"^\s*[-*]?\s*{re.escape(label)}\s*:\s*(.+?)\s*$",
        text,
        re.IGNORECASE | re.MULTILINE,
    )
    return match.group(1).strip() if match else None


def validate_bundle(temp_dir: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    present = {
        path.relative_to(temp_dir).as_posix()
        for path in temp_dir.rglob("*")
        if path.is_file()
    }
    missing = sorted(REQUIRED_AUDIT_FILES - present)
    if missing:
        raise ValueError(f"missing required audit files: {missing}")
    report = read_json(temp_dir / "audit_report.json")
    checker = read_json(temp_dir / "checker_tests.json")
    read_json(temp_dir / "resource_checks.json")
    read_json(temp_dir / "audit_manifest.json")
    markdown = (temp_dir / "audit_report.md").read_text(encoding="utf-8")
    findings = [
        json.loads(line)
        for line in (temp_dir / "findings.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    last_position = -1
    for heading in REQUIRED_HEADINGS:
        position = markdown.find(heading)
        if position <= last_position:
            raise ValueError(f"missing or out-of-order heading: {heading}")
        last_position = position
    summary = report["summary"]
    if summary["final_verdict"] not in VERDICTS:
        raise ValueError("invalid verdict")
    if summary["materials_class"] not in MATERIALS_CLASSES:
        raise ValueError("invalid materials class")
    if summary["answer_type"] not in ANSWER_TYPES:
        raise ValueError("invalid answer type")
    if checker.get("solution_content_inspected") is not False:
        raise ValueError("checker evidence crossed the solution boundary")
    if report["scope"].get("solution_content_inspected") is not False:
        raise ValueError("report crossed the solution boundary")
    expected_ids = [
        f"FINDING-{index:03d}"
        for index in range(1, len(findings) + 1)
    ]
    if [item.get("finding_id") for item in findings] != expected_ids:
        raise ValueError("finding IDs are not consecutive")
    if len(report["findings"]) != len(findings):
        raise ValueError("finding count differs between JSON and JSONL")
    for label, expected in {
        "Audit ID": report["audit_id"],
        "Materials class": summary["materials_class"],
        "Answer type": summary["answer_type"],
        "Final verdict": summary["final_verdict"],
    }.items():
        if markdown_value(markdown, label) != str(expected):
            raise ValueError(f"Markdown/JSON mismatch for {label}")
    return report, findings


def previous_audit_destination(root: Path, audit_id: str) -> Path:
    history = root / "benchmark_audit_history"
    history.mkdir(exist_ok=True)
    destination = history / audit_id
    suffix = 1
    while destination.exists():
        destination = history / f"{audit_id}-{suffix}"
        suffix += 1
    return destination


def finalize_audit(root: Path) -> dict[str, Any]:
    temp_dir = root / ".benchmark_audit_tmp"
    final_dir = root / "benchmark_audit"
    if not temp_dir.is_dir():
        raise FileNotFoundError(temp_dir)
    report, findings = validate_bundle(temp_dir)
    manifest = read_json(temp_dir / "audit_manifest.json")
    completed_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    report["configuration"]["completed_at"] = completed_at
    (temp_dir / "audit_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    with (temp_dir / "logs/audit.log").open(
        "a", encoding="utf-8"
    ) as audit_log:
        audit_log.write(
            f"{completed_at}\tINFO\taudit finalized\t"
            f"verdict={report['summary']['final_verdict']}\n"
        )
    manifest["completed_at"] = completed_at
    manifest["new_findings"] = [
        item["finding_id"] for item in findings
    ]
    manifest["output_hashes"] = dict(
        sorted(
            (
                path.relative_to(temp_dir).as_posix(),
                sha256_file(path),
            )
            for path in temp_dir.rglob("*")
            if path.is_file()
            and path.name not in {"audit_manifest.json", "audit_context.json"}
        )
    )
    (temp_dir / "audit_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    context_path = temp_dir / "audit_context.json"
    if context_path.exists():
        context_path.unlink()

    archived: Path | None = None
    if final_dir.exists():
        previous_manifest = final_dir / "audit_manifest.json"
        previous_id = "legacy-" + time.strftime(
            "%Y%m%dT%H%M%SZ", time.gmtime()
        )
        if previous_manifest.exists():
            try:
                previous_id = str(
                    read_json(previous_manifest).get(
                        "audit_id", previous_id
                    )
                )
            except (OSError, ValueError, json.JSONDecodeError):
                pass
        archived = previous_audit_destination(root, previous_id)
        final_dir.rename(archived)
    try:
        temp_dir.rename(final_dir)
    except Exception:
        if archived is not None and not final_dir.exists():
            archived.rename(final_dir)
        raise
    return {
        "benchmark_root": str(root),
        "audit_dir": str(final_dir),
        "verdict": report["summary"]["final_verdict"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark_root")
    arguments = parser.parse_args()
    try:
        result = finalize_audit(Path(arguments.benchmark_root).resolve())
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"finalize audit output failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
