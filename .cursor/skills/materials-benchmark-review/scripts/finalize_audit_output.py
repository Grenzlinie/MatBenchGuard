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
    "corpus_index_entry.json",
    "disposition.json",
    "findings.jsonl",
    "resource_checks.json",
    "checker_tests.json",
    "audit_manifest.json",
    "logs/audit.log",
}
DIMENSION_WEIGHTS = {
    "materials_admission": 0.15,
    "core_scientific_contract": 0.20,
    "resource_availability": 0.15,
    "task_answerability": 0.15,
    "checker_validity": 0.25,
    "paper_consistency": 0.10,
}
CRITICAL_DIMENSIONS = set(DIMENSION_WEIGHTS)
ROUTES = {
    "PASS": "PUBLISH_CANDIDATE",
    "CONDITIONAL": "REPAIR_QUEUE",
    "REJECT": "QUARANTINE",
    "NOT_ASSESSABLE": "EVIDENCE_PENDING",
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
    if policies & {"set_match", "set_equality", "unordered_set"}:
        return "SET_VALUED"
    if policies & {"ranking", "rank_correlation", "ordered_list"}:
        return "RANKING_BASED"
    if policies & {"structural_audit", "evidence_match"}:
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


def severity_score(findings: list[dict[str, Any]]) -> float:
    maximum = max(
        (SEVERITY_RANK[item["severity"]] for item in findings), default=0
    )
    if maximum >= SEVERITY_RANK["FATAL"]:
        return 0.0
    if maximum >= SEVERITY_RANK["HIGH"]:
        return 0.4
    if maximum >= SEVERITY_RANK["MEDIUM"]:
        return 0.7
    if maximum >= SEVERITY_RANK["LOW"]:
        return 0.9
    return 1.0


def dimension_record(
    dimension: str,
    score: float | None,
    evidence: list[str],
    *,
    applicable: bool = True,
) -> dict[str, Any]:
    if not applicable:
        status = "NOT_ASSESSED"
    elif score is None:
        status = "NOT_ASSESSABLE"
    elif score < 0.5:
        status = "FAIL"
    elif score < 0.8:
        status = "WARNING"
    else:
        status = "PASS"
    return {
        "dimension": dimension,
        "weight": DIMENSION_WEIGHTS[dimension],
        "critical": dimension in CRITICAL_DIMENSIONS,
        "applicable": applicable,
        "score": score,
        "status": status,
        "evidence": evidence,
    }


def weighted_dimensions(
    static_result: dict[str, Any],
    checker_result: dict[str, Any],
    resource_result: dict[str, Any],
    findings: list[dict[str, Any]],
    paper_result: dict[str, Any],
) -> list[dict[str, Any]]:
    by_category: dict[str, list[dict[str, Any]]] = {}
    for item in findings:
        by_category.setdefault(item["category"], []).append(item)
    materials_scores = {
        "MAT_CORE": 1.0,
        "MAT_METHOD": 0.9,
        "MAT_WRAPPER": 0.6,
        "AMBIGUOUS": 0.4,
        "NON_MAT": 0.0,
    }
    materials_class = static_result["materials_prescreen"]["classification"]
    checker_executed = bool(checker_result["tests"])
    checker_usable = (
        checker_executed
        and checker_result["usable_reward_count"]
        == len(checker_result["tests"])
    )
    checker_findings = by_category.get("CHECKER_ROBUSTNESS", [])
    static_findings = by_category.get("PACKAGE_STATIC", [])
    resource_findings = by_category.get("RESOURCE_USABILITY", [])
    task_findings = [
        item
        for item in [*static_findings, *checker_findings]
        if item["title"]
        in {
            "KNOWN_VALID_OUTPUT_REJECTED",
            "MISSING_FILE",
            "OUTPUT_SET_MISMATCH",
            "INVALID_GRADING_SPEC_SCHEMA",
        }
    ]
    if not checker_executed:
        checker_score: float | None = None
        contract_score: float | None = severity_score(static_findings)
        task_score: float | None = severity_score(task_findings)
    elif not checker_usable:
        checker_score = None
        contract_score = None
        task_score = None
    else:
        checker_score = severity_score(checker_findings)
        contract_score = severity_score(
            [*static_findings, *checker_findings]
        )
        task_score = severity_score(task_findings)

    resource_score: float | None
    if resource_result["status"] == "NOT_ASSESSED":
        resource_score = None
    else:
        resource_severity = max(
            (
                SEVERITY_RANK[item["severity"]]
                for item in resource_findings
            ),
            default=0,
        )
        resource_score = (
            0.0
            if resource_severity >= SEVERITY_RANK["FATAL"]
            else 0.5
            if resource_severity >= SEVERITY_RANK["HIGH"]
            else 0.7
            if resource_severity >= SEVERITY_RANK["MEDIUM"]
            else 0.9
            if resource_severity >= SEVERITY_RANK["LOW"]
            else 1.0
        )

    paper_status = paper_result["status"]
    paper_applicable = paper_status != "NOT_ASSESSED"
    paper_score = {
        "PASS": 1.0,
        "WARNING": 0.7,
        "FAIL": 0.0,
        "NOT_ASSESSABLE": None,
        "NOT_ASSESSED": None,
    }[paper_status]
    return [
        dimension_record(
            "materials_admission",
            materials_scores[materials_class],
            [f"materials_class={materials_class}"],
        ),
        dimension_record(
            "core_scientific_contract",
            contract_score,
            [item["finding_id"] for item in [*static_findings, *checker_findings]],
        ),
        dimension_record(
            "resource_availability",
            resource_score,
            [item["finding_id"] for item in resource_findings],
        ),
        dimension_record(
            "task_answerability",
            task_score,
            [item["finding_id"] for item in task_findings],
        ),
        dimension_record(
            "checker_validity",
            checker_score,
            [item["finding_id"] for item in checker_findings],
            applicable=checker_executed,
        ),
        dimension_record(
            "paper_consistency",
            paper_score,
            [f"paper_status={paper_status}"],
            applicable=paper_applicable,
        ),
    ]


def weighted_verdict(
    findings: list[dict[str, Any]],
    dimensions: list[dict[str, Any]],
) -> tuple[str, float | None, bool, str, list[str]]:
    fatal = any(item["severity"] == "FATAL" for item in findings)
    failed_critical = [
        item["dimension"]
        for item in dimensions
        if item["applicable"]
        and item["critical"]
        and item["score"] is not None
        and item["score"] < 0.5
    ]
    evidence_gaps = [
        item["dimension"]
        for item in dimensions
        if item["applicable"] and item["critical"] and item["score"] is None
    ]
    applicable = [
        item
        for item in dimensions
        if item["applicable"] and item["score"] is not None
    ]
    weight = sum(item["weight"] for item in applicable)
    total = (
        round(
            sum(item["score"] * item["weight"] for item in applicable)
            / weight,
            6,
        )
        if weight
        else None
    )
    if fatal:
        return (
            "REJECT",
            total,
            True,
            "A FATAL finding triggered a Hard gate.",
            evidence_gaps,
        )
    if failed_critical:
        return (
            "REJECT",
            total,
            True,
            "Critical dimensions below 0.50 triggered a Hard gate: "
            + ", ".join(failed_critical),
            evidence_gaps,
        )
    if evidence_gaps:
        return (
            "NOT_ASSESSABLE",
            None,
            False,
            "Critical evidence is unavailable: " + ", ".join(evidence_gaps),
            evidence_gaps,
        )
    if total is None or total < 0.60:
        return (
            "REJECT",
            total,
            False,
            "The weighted score is below 0.60.",
            evidence_gaps,
        )
    unresolved_high = any(item["severity"] == "HIGH" for item in findings)
    if total < 0.80 or unresolved_high:
        return (
            "CONDITIONAL",
            total,
            False,
            "The weighted score is below 0.80 or a repairable HIGH remains.",
            evidence_gaps,
        )
    return (
        "PASS",
        total,
        False,
        "All critical dimensions pass and the weighted score is at least 0.80.",
        evidence_gaps,
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


def paper_assessment_findings(
    assessment: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    if assessment is None or "dimensions" not in assessment:
        return []
    findings: list[dict[str, Any]] = []
    for name, value in assessment["dimensions"].items():
        status = value["status"]
        if status in {"PASS", "NOT_ASSESSABLE"}:
            continue
        affected_files = ["paper/paper.md"]
        affected_files.extend(
            item["package_file"] for item in value["evidence"]
        )
        findings.append(
            {
                "severity": "FATAL" if status == "FAIL" else "HIGH",
                "code": f"PAPER_{name.upper()}_{status}",
                "message": value["rationale"],
                "test_type": name,
                "evidence": value["evidence"],
                "affected_files": list(dict.fromkeys(affected_files)),
            }
        )
    return findings


def paper_consistency(
    assessment: dict[str, Any] | None,
    skip_reason: str | None = None,
) -> dict[str, Any]:
    if skip_reason is not None:
        return {
            "status": "NOT_ASSESSED",
            "reason": skip_reason,
            "reproduction_type": None,
            "dimensions": {},
        }
    if assessment is None or "dimensions" not in assessment:
        return {
            "status": "NOT_ASSESSED",
            "reason": "No-paper mode does not assess paper fidelity.",
            "reproduction_type": None,
            "dimensions": {},
        }
    statuses = {
        value["status"] for value in assessment["dimensions"].values()
    }
    status = (
        "FAIL"
        if "FAIL" in statuses
        else "NOT_ASSESSABLE"
        if "NOT_ASSESSABLE" in statuses
        else "WARNING"
        if "WARNING" in statuses
        else "PASS"
    )
    return {
        "status": status,
        "reason": (
            "Agent evidence validates every required paper-grounded dimension."
            if status == "PASS"
            else "One or more paper-grounded dimensions require attention."
        ),
        "reproduction_type": assessment["reproduction_type"],
        "dimensions": assessment["dimensions"],
    }


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
    dimension_lines = "\n".join(
        f"- {item['dimension']}: {item['status']} "
        f"(score={item['score']}, weight={item['weight']})"
        for item in report["dimension_scores"]
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
    paper = report["paper_consistency"]
    paper_assessment = (
        f"- Status: {paper['status']}\n"
        f"- Reproduction type: {paper['reproduction_type']}\n"
        f"- Reason: {paper['reason']}"
        if paper["status"] != "NOT_ASSESSED"
        else f"Status: NOT_ASSESSED\nReason: {paper['reason']}"
    )
    taxonomy = report["taxonomy_labels"]
    taxonomy_lines = (
        f"- Computation task: {taxonomy['computation_task']}\n"
        f"- Research domain: {taxonomy['research_domain']}\n"
        f"- Material system: {taxonomy['material_system']}"
    )
    taxonomy_evidence_lines = (
        "\n".join(
            f"- {item['dimension']}={item['label']}: "
            f"{item['package_file']} — {item['package_quote']}"
            for item in report["taxonomy_evidence"]
        )
        or "No evidence-backed taxonomy labels were supplied."
    )
    gold = paper["dimensions"].get("gold_provenance")
    gold_assessment = (
        f"Status: {gold['status']}\nReason: {gold['rationale']}"
        if gold is not None
        else "Status: NOT_ASSESSED\n"
        "Reason: Gold provenance requires paper-grounded review."
    )
    scope_mode = (
        f"paper-grounded {configuration['execution_level']}"
        if configuration["paper_mode"] == "paper_grounded"
        else f"no-paper {configuration['execution_level']}"
    )
    next_step = (
        "Run task-family-specific probes before production admission."
        if configuration["paper_mode"] == "paper_grounded"
        else "Run paper-grounded and task-family-specific slices before "
        "production admission."
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
- Disposition: {summary['disposition']}
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
{taxonomy_lines}

Taxonomy evidence:
{taxonomy_evidence_lines}

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

{gold_assessment}

## 12. Execution Feasibility

{execution_assessment}

## 13. Reproducibility and Leakage

Solution content was not inspected or copied into the checker runtime.

## 14. Paper Consistency

{paper_assessment}

## 15. Dimension Scores

{dimension_lines}

## 16. Findings

{finding_lines}

## 17. Required Fixes

See each finding's required_fix field.

## 18. Recommended Improvements

{next_step}

## 19. Audit Scope and Limitations

This audit covers {scope_mode} behavior only.

## 20. Audit Log Summary

The fixed bundle was synthesized, validated, and published with rollback.
"""


def write_disposition_artifacts(
    root: Path,
    temp_dir: Path,
    report: dict[str, Any],
    evidence_gaps: list[str],
) -> None:
    summary = report["summary"]
    route = summary["disposition"]
    disposition = {
        "schema_version": "0.1",
        "audit_id": report["audit_id"],
        "verdict": summary["final_verdict"],
        "route": route,
        "publishable": route == "PUBLISH_CANDIDATE",
        "non_destructive": True,
        "original_preserved": True,
        "core_package_roles_mutated": False,
        "evidence_bundle": "benchmark_audit",
        "evidence_gaps": evidence_gaps,
        "reason": summary["core_reason"],
    }
    manifest_data: dict[str, Any] = {}
    try:
        raw_manifest = read_json(root / "manifest.json")
        if isinstance(raw_manifest, dict):
            manifest_data = raw_manifest
    except (OSError, ValueError, json.JSONDecodeError):
        pass
    severities = {
        severity: sum(
            item["severity"] == severity for item in report["findings"]
        )
        for severity in ("FATAL", "HIGH", "MEDIUM", "LOW")
    }
    categories: dict[str, int] = {}
    for item in report["findings"]:
        category = item["category"]
        categories[category] = categories.get(category, 0) + 1
    index_entry = {
        "schema_version": "0.1",
        "audit_id": report["audit_id"],
        "benchmark": {
            "name": root.name,
            "root": str(root),
            "cluster_id": manifest_data.get("cluster_id"),
            "paper_id": manifest_data.get("paper_id"),
        },
        "final_verdict": summary["final_verdict"],
        "total_score": summary["total_score"],
        "hard_gate_triggered": summary["hard_gate_triggered"],
        "route": route,
        "publishable": disposition["publishable"],
        "paper_mode": report["configuration"]["paper_mode"],
        "execution_level": report["configuration"]["execution_level"],
        "taxonomy_labels": report["taxonomy_labels"],
        "finding_summary": {
            "total": len(report["findings"]),
            "by_severity": severities,
            "by_category": dict(sorted(categories.items())),
            "codes": [item["title"] for item in report["findings"]],
        },
        "dimension_scores": report["dimension_scores"],
        "evidence_gaps": evidence_gaps,
    }
    (temp_dir / "disposition.json").write_text(
        json.dumps(disposition, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (temp_dir / "corpus_index_entry.json").write_text(
        json.dumps(index_entry, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def synthesize_report(
    root: Path,
    temp_dir: Path,
    static_result: dict[str, Any],
    checker_result: dict[str, Any],
    resource_result: dict[str, Any] | None = None,
    execution_evidence: dict[str, Any] | None = None,
    agent_assessment: dict[str, Any] | None = None,
    paper_skip_reason: str | None = None,
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
    ] + [
        (item, "PAPER", "PAPER_FIDELITY")
        for item in paper_assessment_findings(agent_assessment)
    ]
    findings = [
        normalized_finding(
            source, f"FINDING-{index:03d}", phase, category
        )
        for index, (source, phase, category) in enumerate(sources, start=1)
    ]
    paper_result = paper_consistency(
        agent_assessment,
        skip_reason=paper_skip_reason,
    )
    dimensions = weighted_dimensions(
        static_result,
        checker_result,
        resource_result,
        findings,
        paper_result,
    )
    verdict, score, hard_gate, reason, evidence_gaps = weighted_verdict(
        findings,
        dimensions,
    )
    disposition = ROUTES[verdict]
    report = read_json(temp_dir / "audit_report.json")
    report["summary"] = {
        "materials_class": static_result["materials_prescreen"][
            "classification"
        ],
        "answer_type": answer_type_for(root),
        "final_verdict": verdict,
        "total_score": score,
        "hard_gate_triggered": hard_gate,
        "disposition": disposition,
        "core_reason": reason,
    }
    report["materials_qualification"] = {
        "axes": static_result["materials_prescreen"]["axes_present"],
        "prescreen": static_result["materials_prescreen"],
    }
    report["resources"] = resource_result["resources"]
    report["execution_evidence"] = execution_evidence
    report["paper_consistency"] = paper_result
    report["taxonomy_labels"] = (
        agent_assessment["taxonomy"]
        if agent_assessment is not None
        else {
            "computation_task": [],
            "research_domain": [],
            "material_system": {"primary": None, "secondary": []},
        }
    )
    report["taxonomy_source"] = (
        agent_assessment["taxonomy_source"]
        if agent_assessment is not None
        else None
    )
    report["taxonomy_evidence"] = (
        agent_assessment["taxonomy_evidence"]
        if agent_assessment is not None
        else []
    )
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
        {
            "gate_id": "PAPER_CONSISTENCY",
            "status": (
                "NOT_ASSESSED"
                if paper_result["status"] == "NOT_ASSESSED"
                else "WARNING"
                if paper_result["status"] == "NOT_ASSESSABLE"
                else gate_status(findings, "PAPER")
            ),
        },
    ]
    report["dimension_scores"] = dimensions
    report["checker_tests"] = checker_result["tests"]
    report["findings"] = findings
    report["required_fixes"] = [
        item["required_fix"] for item in findings
    ]
    report["scope"] = {
        "files_reviewed": sorted(
            [
                role for role in REQUIRED_ROLES if (root / role).exists()
            ]
            + (
                ["paper/paper.md", "paper/images_manifest.json"]
                if agent_assessment is not None
                and "dimensions" in agent_assessment
                else []
            )
        ),
        "files_not_reviewed": (
            ["solution/**"]
            if agent_assessment is not None
            and "dimensions" in agent_assessment
            else ["paper/paper.md", "solution/**"]
        ),
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
            *(
                ["paper fidelity"]
                if agent_assessment is None
                or "dimensions" not in agent_assessment
                else []
            ),
            *(
                ["scientific workflow execution"]
                if execution_evidence["claim"] != "SMOKE_RUN"
                else []
            ),
            *(
                ["task-family-specific scientific probes"]
                if not any(
                    item["test_type"]
                    == "metamorphic_equivalent_representation"
                    for item in checker_result["tests"]
                )
                else []
            ),
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
    write_disposition_artifacts(
        root,
        temp_dir,
        report,
        evidence_gaps,
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
    disposition = read_json(temp_dir / "disposition.json")
    index_entry = read_json(temp_dir / "corpus_index_entry.json")
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
    expected_route = ROUTES[summary["final_verdict"]]
    if summary.get("disposition") != expected_route:
        raise ValueError("summary disposition does not match verdict")
    if disposition.get("route") != expected_route:
        raise ValueError("disposition artifact does not match verdict")
    if index_entry.get("route") != expected_route:
        raise ValueError("corpus index route does not match verdict")
    if bool(index_entry.get("publishable")) != (
        summary["final_verdict"] == "PASS"
    ):
        raise ValueError("corpus publishable flag does not match verdict")
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
