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

from prepare_audit_output import QUALITY_EVIDENCE_ROLES, sha256_file


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
SCORING_VERSION = "materials-review-scoring/1.0"
DIMENSION_MAX_POINTS = {
    "scientific_validity": 35,
    "instruction_answerability": 20,
    "checker_gold_alignment": 25,
    "robustness_discrimination": 15,
    "solution_completeness": 5,
}
CRITICAL_DIMENSIONS = {
    "scientific_validity",
    "instruction_answerability",
    "checker_gold_alignment",
}
ROUTES = {
    "PASS": "PUBLISH_CANDIDATE",
    "CONDITIONAL": "REPAIR_QUEUE",
    "REJECT": "QUARANTINE",
    "NOT_ASSESSABLE": "EVIDENCE_PENDING",
}
HARD_GATE_DEFINITIONS = {
    "NON_MATERIALS_TASK": {
        "trigger_codes": {"NON_MATERIALS_TASK"},
        "description": "The task is not substantive materials science.",
    },
    "SCIENTIFIC_TARGET_INVALID": {
        "trigger_codes": {
            "SCIENTIFIC_TARGET_INVALID",
            "UNRECOVERABLE_TASK_DEFINITION",
        },
        "description": (
            "The scientific target is invalid or lacks an unrecoverable "
            "necessary definition."
        ),
    },
    "CHECKER_CORE_TASK_UNASSESSED": {
        "trigger_codes": {"CHECKER_CORE_TASK_UNASSESSED"},
        "description": (
            "The checker cannot assess the core task without redefining it."
        ),
    },
    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE": {
        "trigger_codes": {"INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"},
        "description": (
            "An indispensable direct input is permanently unavailable and "
            "has no equivalent."
        ),
    },
}
SEVERITY_DEDUCTION_FRACTIONS = {
    "FATAL": 1.0,
    "HIGH": 0.4,
    "MEDIUM": 0.2,
    "LOW": 0.1,
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


def line_for_quote(root: Path, relative: str, quote: str) -> int | None:
    path = root / relative
    if not path.is_file():
        return None
    for number, line in enumerate(
        path.read_text(encoding="utf-8", errors="replace").splitlines(),
        start=1,
    ):
        if quote in line:
            return number
    return None


def evidence_locations(
    root: Path, source: dict[str, Any], affected_files: list[str]
) -> list[dict[str, Any]]:
    locations: list[dict[str, Any]] = []

    def add(relative: Any, quote: Any = None, line: Any = None) -> None:
        if not isinstance(relative, str) or not relative:
            return
        normalized_quote = quote if isinstance(quote, str) and quote else None
        normalized_line = line if isinstance(line, int) and line > 0 else None
        if normalized_quote is not None and normalized_line is None:
            normalized_line = line_for_quote(root, relative, normalized_quote)
        value = {
            "file": relative,
            "line": normalized_line,
            "quote": normalized_quote,
        }
        if value not in locations:
            locations.append(value)

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            add(
                value.get("package_file"),
                value.get("package_quote"),
                value.get("package_line"),
            )
            if value.get("paper_quote"):
                add("paper/paper.md", value.get("paper_quote"))
            add(value.get("file"), value.get("quote"), value.get("line"))
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(source.get("evidence"))
    for relative in affected_files:
        if any(item["file"] == relative for item in locations):
            continue
        path = root / relative
        if path.is_file():
            lines = path.read_text(
                encoding="utf-8", errors="replace"
            ).splitlines()
            first = next(
                (
                    (number, line.strip())
                    for number, line in enumerate(lines, start=1)
                    if line.strip()
                ),
                None,
            )
            add(
                relative,
                first[1] if first is not None else None,
                first[0] if first is not None else None,
            )
        else:
            add(relative)
    return locations


def repair_text(
    source: dict[str, Any], affected_files: list[str]
) -> tuple[str, str, str]:
    code = source["code"]
    files = ", ".join(affected_files) or "the affected audit evidence"
    test_type = source.get("test_type")
    if code == "MISSING_FILE":
        repair = (
            f"Restore {files} with a parseable implementation of the declared "
            "public contract."
        )
        retest = "Run the Review CLI and require every checker probe to complete."
    elif code.startswith("SOLUTION_"):
        repair = (
            "Provide a runnable solution/solve.sh that generates every "
            "contracted output in the isolated Oracle workspace."
        )
        retest = (
            "Run the Review CLI and require positive_oracle to meet the checker "
            "pass threshold without exposing Oracle values."
        )
    elif code == "INDEPENDENT_PUBLIC_FIXTURE_UNAVAILABLE":
        repair = (
            "Construct an independently justified public valid fixture from "
            "instruction/tests evidence without using Oracle values; if that "
            "is not possible, retain the scored limitation."
        )
        retest = (
            "Re-run discrimination and equivalence probes only with the "
            "source-bound non-Oracle fixture and record its hashes."
        )
    elif code == "KNOWN_VALID_OUTPUT_REJECTED":
        repair = (
            "Align the checker target, tolerance, and public contract so the "
            f"{test_type or 'known-valid'} probe passes."
        )
        retest = (
            "Re-run the same independently justified known-valid probe and "
            "require a passing finite reward."
        )
    elif code == "ADVERSARIAL_OUTPUT_PASSES":
        repair = (
            f"Reject the {test_type or 'adversarial'} case by enforcing the "
            "missing completeness or scientific validity condition."
        )
        retest = (
            f"Re-run {test_type or 'the adversarial probe'} and require a "
            "finite score below the pass threshold."
        )
    elif code.startswith("PAPER_"):
        repair = (
            f"Reconcile {files} with the quoted paper/package evidence without "
            "changing the declared reproduction classification."
        )
        retest = (
            "Repeat the triggered paper-grounded Review CLI and verify the same "
            "quoted evidence reaches PASS."
        )
    else:
        repair = (
            f"Correct {files} to eliminate the observed {code} defect: "
            f"{source['message'].rstrip('.')}."
        )
        retest = (
            f"Run the Review CLI and verify {code} is absent while the affected "
            "positive, negative, discrimination, and equivalence probes retain "
            "their expected rewards."
        )
    impact = (
        f"{code} changes the assessed contract at {files}: "
        f"{source['message']}"
    )
    return impact, repair, retest


def normalized_finding(
    root: Path,
    source: dict[str, Any],
    finding_id: str,
    phase: str,
    category: str,
) -> dict[str, Any]:
    source = dict(source)
    source_evidence = source.get("evidence", {})
    if (
        source.get("code") == "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
        and isinstance(source_evidence, dict)
        and source_evidence.get("status") != "PERMANENT_UNAVAILABLE"
    ):
        source["code"] = (
            "INDISPENSABLE_DIRECT_INPUT_"
            + str(source_evidence.get("status", "UNVERIFIED"))
        )
        source["severity"] = "HIGH"
    affected_files = list(source.get("affected_files", []))
    if not affected_files and phase == "E1":
        affected_files = ["tests/checker.py", "tests/grading_spec.json"]
    elif not affected_files and phase == "E0":
        affected_files = ["instruction.md"]
    impact, repair, retest = repair_text(source, affected_files)
    hard_gate = any(
        source["code"] in definition["trigger_codes"]
        for definition in HARD_GATE_DEFINITIONS.values()
    )
    return {
        "finding_id": finding_id,
        "severity": source["severity"],
        "category": category,
        "phase": phase,
        "status": "OPEN",
        "title": source["code"],
        "affected_files": affected_files,
        "affected_locations": evidence_locations(
            root, source, affected_files
        ),
        "observed_fact": source["message"],
        "observation": source["message"],
        "evidence": source.get("evidence", {}),
        "impact": impact,
        "failure_scenario": source.get("test_type", source["code"]),
        "repairable": not hard_gate,
        "minimal_repair": repair,
        "retest": retest,
        "required_fix": repair,
        "verification_after_fix": retest,
        "confidence": "HIGH",
        "judgment_type": "FACT",
    }


def scored_dimension_for(finding: dict[str, Any]) -> str | None:
    code = finding["title"]
    files = finding["affected_files"]
    if code.startswith("SOLUTION_"):
        return "solution_completeness"
    if code in {
        "ADVERSARIAL_OUTPUT_PASSES",
        "CHECKER_CRASH",
        "CHECKER_RESULT_UNUSABLE",
        "INDEPENDENT_PUBLIC_FIXTURE_UNAVAILABLE",
        "SCIENTIFIC_QUALITY_GRADIENT_VIOLATION",
        "SCIENTIFIC_INVARIANCE_VIOLATION",
        "SOLUTION_BOUNDARY_VIOLATION",
    }:
        return "robustness_discrimination"
    if code.startswith("PAPER_"):
        name = code.removeprefix("PAPER_")
        if name.startswith(("INSTRUCTION_", "DATA_", "METHOD_")):
            return "scientific_validity"
        return "checker_gold_alignment"
    if code in {"NON_MATERIALS_TASK", "SCIENTIFIC_TARGET_INVALID"}:
        return "scientific_validity"
    if code == "UNRECOVERABLE_TASK_DEFINITION":
        return "instruction_answerability"
    if code == "KNOWN_VALID_OUTPUT_REJECTED" or any(
        path.startswith("tests/") for path in files
    ):
        return "checker_gold_alignment"
    if "instruction.md" in files or code.startswith("MATERIALS_"):
        return "instruction_answerability"
    return None


def dimension_scores(
    checker_result: dict[str, Any],
    findings: list[dict[str, Any]],
    paper_result: dict[str, Any],
    contract_gaps: list[str] | None = None,
    materials_assessment: dict[str, Any] | None = None,
    paper_trigger_adjudication: list[dict[str, Any]] | None = None,
    root: Path | None = None,
) -> list[dict[str, Any]]:
    unavailable: set[str] = set()
    contract_gaps = contract_gaps or []
    if {
        "authoritative_materials_qualification",
        "triggered_paper_review",
    } & set(contract_gaps):
        unavailable.add("scientific_validity")
    if paper_result["status"] == "NOT_ASSESSABLE":
        unavailable.add("scientific_validity")
    if any(
        item["category"] == "RESOURCE_USABILITY"
        and isinstance(item.get("evidence"), dict)
        and item["evidence"].get("status")
        in {
            "TRANSIENT_FAILURE",
            "RATE_LIMITED",
            "BLOCKED_PRIVATE_NETWORK",
            "REQUIRES_AUTH",
            "REQUIRES_LICENSE",
            "IDENTITY_MISMATCH",
        }
        for item in findings
    ):
        unavailable.add("scientific_validity")
    checker_tests = checker_result.get("tests", [])
    probe_coverage = checker_result.get("probe_coverage", {})
    if checker_tests and checker_result.get("usable_reward_count") == 0:
        unavailable.update(
            {"checker_gold_alignment", "robustness_discrimination"}
        )
    records: list[dict[str, Any]] = []
    root = root or Path(".")
    instruction_lines = (
        (root / "instruction.md")
        .read_text(encoding="utf-8", errors="replace")
        .splitlines()
        if (root / "instruction.md").is_file()
        else []
    )
    instruction_first = next(
        (
            {
                "file": "instruction.md",
                "line": number,
                "quote": line.strip(),
            }
            for number, line in enumerate(instruction_lines, start=1)
            if line.strip()
        ),
        {"file": "instruction.md", "line": None, "quote": None},
    )
    for dimension, maximum in DIMENSION_MAX_POINTS.items():
        relevant = [
            item for item in findings if scored_dimension_for(item) == dimension
        ]
        deductions: list[dict[str, Any]] = []
        deducted = 0.0
        for item in relevant:
            fraction = SEVERITY_DEDUCTION_FRACTIONS[item["severity"]]
            if dimension == "solution_completeness" and item["severity"] in {
                "FATAL",
                "HIGH",
            }:
                fraction = 1.0
            points = round(maximum * fraction, 2)
            deduction_id = f"DEDUCTION-{item['finding_id']}-{dimension}"
            deducted += points
            deductions.append(
                {
                    "deduction_id": deduction_id,
                    "finding_id": item["finding_id"],
                    "points": points,
                    "severity": item["severity"],
                    "observed_fact": item["observed_fact"],
                    "affected_locations": item["affected_locations"],
                }
            )
        if dimension in unavailable:
            earned: float | int | None = None
            normalized: float | None = None
            status = "NOT_ASSESSABLE"
        else:
            earned = round(max(0.0, maximum - deducted), 2)
            if isinstance(earned, float) and earned.is_integer():
                earned = int(earned)
            normalized = round(float(earned) / maximum, 6)
            status = (
                "FAIL"
                if normalized < 0.5
                else "WARNING"
                if normalized < 0.8
                else "PASS"
            )
        evidence = [
            {
                "finding_id": item["finding_id"],
                "observed_fact": item["observed_fact"],
                "affected_locations": item["affected_locations"],
            }
            for item in relevant
        ]
        if dimension == "robustness_discrimination" and probe_coverage:
            evidence.append(
                {
                    "evidence_type": "dynamic_probe_coverage",
                    "observed_fact": (
                        "Dynamic robustness coverage is recorded by probe "
                        "class with non-Oracle provenance."
                    ),
                    "probe_coverage": probe_coverage,
                }
            )
        elif dimension == "scientific_validity":
            if materials_assessment is not None:
                evidence.append(
                    {
                        "evidence_type": (
                            "authoritative_materials_qualification"
                        ),
                        "classification": materials_assessment[
                            "classification"
                        ],
                        "rationale": materials_assessment["rationale"],
                        "source_evidence": materials_assessment["evidence"],
                    }
                )
            if paper_trigger_adjudication:
                evidence.append(
                    {
                        "evidence_type": "paper_trigger_adjudication",
                        "adjudication": paper_trigger_adjudication,
                    }
                )
        elif dimension == "instruction_answerability":
            evidence.append(
                {
                    "evidence_type": "public_instruction_contract",
                    "observed_fact": (
                        "The public instruction is present and was reviewed "
                        "as the answerability contract."
                    ),
                    "source_evidence": [instruction_first],
                }
            )
        elif dimension == "checker_gold_alignment":
            evidence.append(
                {
                    "evidence_type": "real_checker_execution",
                    "observed_fact": (
                        "The persisted checker cases record class, score, "
                        "status, and exit code."
                    ),
                    "checker_cases": [
                        {
                            "test_type": item.get("test_type"),
                            "probe_class": item.get("probe_class"),
                            "observed_score": item.get("observed_score"),
                            "observed_status": item.get("observed_status"),
                            "exit_code": item.get("exit_code"),
                        }
                        for item in checker_tests
                    ],
                }
            )
        elif dimension == "solution_completeness":
            oracle = checker_result.get("solution_oracle", {})
            evidence.append(
                {
                    "evidence_type": "oracle_positive_mock_status",
                    "used": bool(oracle.get("used")),
                    "status": oracle.get("status"),
                    "positive_mock_available": bool(
                        oracle.get("positive_mock_available")
                    ),
                    "scientific_evidence": False,
                }
            )
        records.append(
            {
                "dimension": dimension,
                "max_points": maximum,
                "weight": maximum / 100,
                "critical": dimension in CRITICAL_DIMENSIONS,
                "applicable": True,
                "points_earned": earned,
                "normalized_score": normalized,
                "score": normalized,
                "status": status,
                "deductions": deductions,
                "deduction_ids": [
                    item["deduction_id"] for item in deductions
                ],
                "finding_ids": [item["finding_id"] for item in relevant],
                "evidence": evidence,
            }
        )
    return records


def hard_gate_results(
    root: Path,
    findings: list[dict[str, Any]],
    evidence_gaps: list[str],
) -> list[dict[str, Any]]:
    def non_failure_evidence(
        code: str,
        status: str,
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        preferred_roles = (
            [
                "tests/grading_spec.json",
                "instruction.md",
                "tests/checker.py",
                "tests/test.sh",
            ]
            if code == "CHECKER_CORE_TASK_UNASSESSED"
            else [
                "instruction.md",
                "tests/grading_spec.json",
                "tests/checker.py",
                "tests/test.sh",
            ]
        )
        relative = next(
            (
                candidate
                for candidate in preferred_roles
                if (root / candidate).is_file()
            ),
            preferred_roles[0],
        )
        path = root / relative
        lines = (
            path.read_text(encoding="utf-8", errors="replace").splitlines()
            if path.is_file()
            else []
        )
        first = next(
            (
                (number, line.strip())
                for number, line in enumerate(lines, start=1)
                if line.strip()
            ),
            (None, None),
        )
        location = {
            "file": relative,
            "line": first[0],
            "quote": first[1],
        }
        observations = {
            "NON_MATERIALS_TASK": (
                "The instruction identifies a substantive materials-science "
                "task and no contrary finding was confirmed."
            ),
            "SCIENTIFIC_TARGET_INVALID": (
                "The reviewed instruction/tests define an assessable "
                "scientific target and no invalid-target finding was confirmed."
            ),
            "CHECKER_CORE_TASK_UNASSESSED": (
                "The grading contract and completed checker probes assess the "
                "declared core outputs; no unrecoverable alignment finding was "
                "confirmed."
            ),
            "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE": (
                "The instruction does not establish a permanently unavailable "
                "indispensable direct input with no scientific equivalent."
            ),
        }
        observed_fact = (
            "The checker core-task Hard Gate is not assessable because "
            "checker_gold_alignment remains a critical evidence gap."
            if status == "NOT_ASSESSABLE"
            else observations[code]
        )
        return (
            [
                {
                    "finding_id": None,
                    "observed_fact": observed_fact,
                    "source_evidence": location,
                }
            ],
            [location],
        )

    results = []
    for code, definition in HARD_GATE_DEFINITIONS.items():
        matched = [
            item
            for item in findings
            if item["title"] in definition["trigger_codes"]
        ]
        not_assessable = (
            code == "SCIENTIFIC_TARGET_INVALID"
            and "scientific_validity" in evidence_gaps
        ) or (
            code == "CHECKER_CORE_TASK_UNASSESSED"
            and "checker_gold_alignment" in evidence_gaps
        )
        status = (
            "FAIL"
            if matched
            else "NOT_ASSESSABLE"
            if not_assessable
            else "PASS"
        )
        evidence = [
            {
                "finding_id": item["finding_id"],
                "observed_fact": item["observed_fact"],
                "source_evidence": item["evidence"],
            }
            for item in matched
        ]
        affected_locations = [
            location
            for item in matched
            for location in item["affected_locations"]
        ]
        if status != "FAIL":
            evidence, affected_locations = non_failure_evidence(code, status)
        results.append(
            {
                "code": code,
                "status": status,
                "description": definition["description"],
                "finding_ids": [item["finding_id"] for item in matched],
                "evidence": evidence,
                "affected_locations": affected_locations,
            }
        )
    return results


def scoring_verdict(
    findings: list[dict[str, Any]],
    dimensions: list[dict[str, Any]],
    hard_gates: list[dict[str, Any]],
) -> tuple[str, float | None, bool, str, list[str]]:
    evidence_gaps = [
        item["dimension"]
        for item in dimensions
        if item["points_earned"] is None
    ]
    total = (
        None
        if evidence_gaps
        else round(
            sum(float(item["points_earned"]) for item in dimensions),
            2,
        )
    )
    if total is not None and float(total).is_integer():
        total = int(total)
    failed_gates = [
        item["code"] for item in hard_gates if item["status"] == "FAIL"
    ]
    if failed_gates:
        return (
            "REJECT",
            total,
            True,
            "Confirmed Hard Gate: " + ", ".join(failed_gates),
            evidence_gaps,
        )
    if evidence_gaps:
        return (
            "NOT_ASSESSABLE",
            None,
            False,
            "Critical evidence is temporarily unavailable: "
            + ", ".join(evidence_gaps),
            evidence_gaps,
        )
    if total is None or total < 60:
        return (
            "REJECT",
            total,
            False,
            "The authoritative score is below 60/100.",
            evidence_gaps,
        )
    repairable_high = any(
        item["repairable"] and item["severity"] == "HIGH"
        for item in findings
    )
    if total < 80 or repairable_high:
        return (
            "CONDITIONAL",
            total,
            False,
            "The authoritative score is 60–79/100 or a repairable HIGH remains.",
            evidence_gaps,
        )
    return (
        "PASS",
        total,
        False,
        "The authoritative score is at least 80/100 with no repairable HIGH.",
        evidence_gaps,
    )


def execution_findings(
    execution_evidence: dict[str, Any],
) -> list[dict[str, Any]]:
    if (
        execution_evidence.get("claim") == "SMOKE_RUN"
        and execution_evidence.get("status") == "FAIL"
    ):
        return [
            {
                "severity": "HIGH",
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
                "severity": "HIGH" if status == "FAIL" else "MEDIUM",
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
            "triggers": [],
            "reproduction_type": None,
            "dimensions": {},
        }
    if assessment is None or "dimensions" not in assessment:
        return {
            "status": "NOT_ASSESSED",
            "reason": "No-paper mode does not assess paper fidelity.",
            "triggers": [],
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
        "triggers": assessment["paper_triggers"],
        "reproduction_type": assessment["reproduction_type"],
        "dimensions": assessment["dimensions"],
    }


def markdown_summary(report: dict[str, Any]) -> str:
    summary = report["summary"]
    configuration = report["configuration"]
    finding_lines = (
        "\n".join(
            f"- {item['finding_id']} [{item['severity']}] {item['title']}: "
            f"{item['observed_fact']}\n"
            f"  - Locations: {item['affected_locations']}\n"
            f"  - Impact: {item['impact']}\n"
            f"  - Minimal repair: {item['minimal_repair']}\n"
            f"  - Retest: {item['retest']}"
            for item in report["findings"]
        )
        or "No findings."
    )
    gate_lines = "\n".join(
        f"- {gate['code']}: {gate['status']} "
        f"(locations={gate['affected_locations']})"
        for gate in report["hard_gates"]
    )
    dimension_lines = "\n".join(
        f"- {item['dimension']}: {item['status']} "
        f"({item['points_earned']}/{item['max_points']}, "
        f"normalized={item['normalized_score']}, "
        f"deductions={item['deduction_ids']})"
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
    qualification = report["materials_qualification"]
    qualification_lines = (
        f"- Authoritative: {qualification['authoritative']}\n"
        f"- Classification: {qualification['classification']}\n"
        f"- Rationale: {qualification['rationale']}\n"
        f"- Evidence: {qualification['evidence']}"
    )
    adjudication_lines = (
        "\n".join(
            f"- {item['trigger']}: {item['status']} — {item['rationale']} "
            f"(evidence={item['evidence']})"
            for item in report.get("paper_trigger_adjudication", [])
        )
        or "No no-paper trigger adjudication was supplied."
    )
    contract = report["evidence_contract"]
    evidence_contract_lines = (
        f"- Contract: {contract['version']}\n"
        f"- Fail closed: {contract['fail_closed']}\n"
        f"- Gaps: {contract['gaps']}"
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
    oracle_boundary = (
        "The solution Oracle ran only in an isolated positive-mock workspace; "
        "its values are neither reported nor used as scientific evidence."
        if report["scope"]["solution_oracle_executed"]
        else "No solution Oracle was executed."
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
- Authoritative score (0–100): {summary['total_score']}
- Scoring version: {summary['scoring_version']}
- Core reason: {summary['core_reason']}

## 2. Benchmark Identity

- Root: {report['benchmark']['root']}

## 3. Audit Configuration

- Paper mode: {configuration['paper_mode']}
- Execution level: {configuration['execution_level']}

## 4. Final Verdict

{summary['final_verdict']}: {summary['core_reason']}

{evidence_contract_lines}

## 5. Materials Qualification

- Class: {summary['materials_class']}
{qualification_lines}
{taxonomy_lines}

Taxonomy evidence:
{taxonomy_evidence_lines}

No-paper trigger adjudication:
{adjudication_lines}

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

{oracle_boundary}

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
        "schema_version": "1.0",
        "audit_id": report["audit_id"],
        "scoring_version": summary["scoring_version"],
        "verdict": summary["final_verdict"],
        "total_score": summary["total_score"],
        "dimension_scores": report["dimension_scores"],
        "hard_gates": report["hard_gates"],
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
        "schema_version": "1.0",
        "audit_id": report["audit_id"],
        "benchmark": {
            "name": root.name,
            "root": str(root),
            "cluster_id": manifest_data.get("cluster_id"),
            "paper_id": manifest_data.get("paper_id"),
        },
        "final_verdict": summary["final_verdict"],
        "scoring_version": summary["scoring_version"],
        "total_score": summary["total_score"],
        "hard_gate_triggered": summary["hard_gate_triggered"],
        "hard_gates": report["hard_gates"],
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
    materials_assessment = (
        agent_assessment.get("materials_qualification")
        if agent_assessment is not None
        else None
    )
    materials_class = (
        materials_assessment["classification"]
        if materials_assessment is not None
        else static_result["materials_prescreen"]["classification"]
    )
    materials_gate_sources = []
    if materials_class == "NON_MAT":
        materials_gate_sources.append(
            (
                {
                    "severity": "FATAL",
                    "code": "NON_MATERIALS_TASK",
                    "message": (
                        "The public instruction does not define a substantive "
                        "materials object, operation, and endpoint."
                    ),
                    "affected_files": ["instruction.md"],
                },
                "E0",
                "MATERIALS_ADMISSION",
            )
        )
    oracle_sources = []
    if checker_result.get("solution_oracle", {}).get("status") == "BROKEN":
        oracle_sources.append(
            (
                {
                    "severity": "HIGH",
                    "code": "SOLUTION_ORACLE_BROKEN",
                    "message": (
                        "solution/solve.sh did not generate every contracted "
                        "output for the checker positive path."
                    ),
                    "affected_files": ["solution/solve.sh"],
                },
                "E0",
                "PACKAGE_STATIC",
            )
        )
    static_issues = [
        item
        for item in static_result["issues"]
        if not (
            materials_assessment is not None
            and item.get("code")
            == "MATERIALS_ADMISSIBILITY_REQUIRES_ADJUDICATION"
        )
    ]
    sources = materials_gate_sources + oracle_sources + [
        (item, "E0", "PACKAGE_STATIC")
        for item in static_issues
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
            root,
            source,
            f"FINDING-{index:03d}",
            phase,
            category,
        )
        for index, (source, phase, category) in enumerate(sources, start=1)
    ]
    paper_result = paper_consistency(
        agent_assessment,
        skip_reason=paper_skip_reason,
    )
    contract_gaps = []
    if materials_assessment is None:
        contract_gaps.append("authoritative_materials_qualification")
    paper_trigger_adjudication = (
        agent_assessment.get("paper_trigger_adjudication", [])
        if agent_assessment is not None
        else []
    )
    if (
        paper_skip_reason is None
        and not paper_result.get("dimensions")
        and {
            item.get("trigger")
            for item in paper_trigger_adjudication
            if isinstance(item, dict)
        }
        != {
            "SCIENTIFIC_CONFLICT",
            "NECESSARY_INFORMATION_MISSING",
            "GOLD_PROVENANCE_UNCERTAIN",
            "EXPLICIT_REPRODUCTION_CLAIM",
        }
    ):
        contract_gaps.append("paper_trigger_adjudication")
    if any(
        item.get("status") == "TRIGGERED"
        for item in paper_trigger_adjudication
    ) and not paper_result.get("dimensions"):
        contract_gaps.append("triggered_paper_review")
    dimensions = dimension_scores(
        checker_result,
        findings,
        paper_result,
        contract_gaps,
        materials_assessment,
        paper_trigger_adjudication,
        root,
    )
    provisional_gaps = [
        item["dimension"]
        for item in dimensions
        if item["critical"] and item["points_earned"] is None
    ]
    hard_gates = hard_gate_results(root, findings, provisional_gaps)
    verdict, score, hard_gate, reason, evidence_gaps = scoring_verdict(
        findings,
        dimensions,
        hard_gates,
    )
    disposition = ROUTES[verdict]
    report = read_json(temp_dir / "audit_report.json")
    report["summary"] = {
        "materials_class": materials_class,
        "answer_type": answer_type_for(root),
        "scoring_version": SCORING_VERSION,
        "final_verdict": verdict,
        "total_score": score,
        "hard_gate_triggered": hard_gate,
        "disposition": disposition,
        "core_reason": reason,
    }
    report["materials_qualification"] = {
        "axes": static_result["materials_prescreen"]["axes_present"],
        "prescreen": static_result["materials_prescreen"],
        "authoritative": materials_assessment is not None,
        "classification": materials_class,
        "rationale": (
            materials_assessment["rationale"]
            if materials_assessment is not None
            else "No external materials qualification assessment was supplied."
        ),
        "evidence": (
            materials_assessment["evidence"]
            if materials_assessment is not None
            else []
        ),
    }
    report["evidence_contract"] = {
        "version": "materials-evidence-contract/1.0",
        "fail_closed": True,
        "gaps": contract_gaps,
    }
    report["resources"] = resource_result["resources"]
    report["execution_evidence"] = execution_evidence
    report["paper_consistency"] = paper_result
    report["paper_trigger_adjudication"] = paper_trigger_adjudication
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
    report["hard_gates"] = hard_gates
    compatibility_gate_ids = {
        "NON_MATERIALS_TASK": "MATERIALS_TASK",
        "SCIENTIFIC_TARGET_INVALID": "SCIENTIFIC_VALIDITY",
        "CHECKER_CORE_TASK_UNASSESSED": "CHECKER_CORE_ALIGNMENT",
        "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE": (
            "DIRECT_INPUT_AVAILABILITY"
        ),
    }
    report["gate_results"] = [
        {
            "gate_id": compatibility_gate_ids[item["code"]],
            "hard_gate_code": item["code"],
            "status": item["status"],
            "evidence": item["evidence"],
            "affected_locations": item["affected_locations"],
        }
        for item in hard_gates
    ]
    report["dimension_scores"] = dimensions
    report["checker_tests"] = checker_result["tests"]
    report["findings"] = findings
    report["required_fixes"] = [
        item["required_fix"] for item in findings
    ]
    report["scope"] = {
        "quality_evidence_files": sorted(
            [
                "instruction.md",
                *[
                    path.relative_to(root).as_posix()
                    for path in (root / "tests").rglob("*")
                    if path.is_file()
                ],
            ]
        ),
        "files_reviewed": sorted(
            [
                role
                for role in QUALITY_EVIDENCE_ROLES
                if (root / role).exists()
            ]
            + (
                ["solution/solve.sh (isolated positive mock only)"]
                if checker_result["solution_oracle"]["used"]
                else []
            )
            + (
                ["paper/paper.md", "paper/images_manifest.json"]
                if agent_assessment is not None
                and "dimensions" in agent_assessment
                else []
            )
        ),
        "files_not_reviewed": (
            [
                "manifest.json",
                "resources.json",
                "steps.json",
                "task.toml",
                "environment/**",
                "solution/** except isolated Oracle execution",
            ]
            if agent_assessment is not None
            and "dimensions" in agent_assessment
            else [
                "paper/**",
                "manifest.json",
                "resources.json",
                "steps.json",
                "task.toml",
                "environment/**",
                "solution/** except isolated Oracle execution",
            ]
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
        "solution_oracle_executed": checker_result["solution_oracle"]["used"],
        "solution_content_inspected": False,
    }
    (temp_dir / "audit_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    audit_manifest = read_json(temp_dir / "audit_manifest.json")
    audit_manifest["solution_oracle_executed"] = checker_result[
        "solution_oracle"
    ]["used"]
    audit_manifest["solution_content_inspected"] = False
    audit_manifest["solution_oracle_scientific_evidence"] = False
    (temp_dir / "audit_manifest.json").write_text(
        json.dumps(audit_manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
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
    evidence_contract = report.get("evidence_contract")
    if (
        not isinstance(evidence_contract, dict)
        or evidence_contract.get("version")
        != "materials-evidence-contract/1.0"
        or evidence_contract.get("fail_closed") is not True
        or not isinstance(evidence_contract.get("gaps"), list)
    ):
        raise ValueError("invalid evidence contract")
    if (
        summary["final_verdict"] == "PASS"
        and evidence_contract["gaps"]
    ):
        raise ValueError("PASS has unresolved evidence contract gaps")
    if summary.get("scoring_version") != SCORING_VERSION:
        raise ValueError("invalid scoring version")
    dimensions = report.get("dimension_scores")
    if not isinstance(dimensions, list) or [
        item.get("dimension") for item in dimensions
    ] != list(DIMENSION_MAX_POINTS):
        raise ValueError("dimension score order or membership is invalid")
    for item in dimensions:
        name = item["dimension"]
        maximum = DIMENSION_MAX_POINTS[name]
        if item.get("max_points") != maximum:
            raise ValueError(f"invalid max points for {name}")
        earned = item.get("points_earned")
        normalized = item.get("normalized_score")
        if earned is None:
            if normalized is not None or item.get("status") != "NOT_ASSESSABLE":
                raise ValueError(f"inconsistent unavailable score for {name}")
        elif (
            not isinstance(earned, (int, float))
            or isinstance(earned, bool)
            or not 0 <= earned <= maximum
            or normalized != round(float(earned) / maximum, 6)
        ):
            raise ValueError(f"invalid earned or normalized score for {name}")
        if earned is not None:
            expected_status = (
                "FAIL"
                if normalized < 0.5
                else "WARNING"
                if normalized < 0.8
                else "PASS"
            )
            if item.get("status") != expected_status:
                raise ValueError(f"inconsistent dimension status for {name}")
        if summary["final_verdict"] == "PASS" and (
            not isinstance(item.get("evidence"), list)
            or not item["evidence"]
        ):
            raise ValueError(f"PASS dimension lacks evidence: {name}")
    hard_gates = report.get("hard_gates")
    if not isinstance(hard_gates, list) or [
        item.get("code") for item in hard_gates
    ] != list(HARD_GATE_DEFINITIONS):
        raise ValueError("Hard Gates must be exactly the four confirmed gates")
    if any(
        item.get("status") not in {"PASS", "FAIL", "NOT_ASSESSABLE"}
        or not isinstance(item.get("evidence"), list)
        or not item["evidence"]
        or not isinstance(item.get("affected_locations"), list)
        or not item["affected_locations"]
        or not all(
            isinstance(location, dict)
            and set(location) == {"file", "line", "quote"}
            and isinstance(location["file"], str)
            and bool(location["file"])
            for location in item["affected_locations"]
        )
        for item in hard_gates
    ):
        raise ValueError("invalid Hard Gate evidence schema")
    evidence_gaps = [
        item["dimension"]
        for item in dimensions
        if item["points_earned"] is None
    ]
    expected_total = (
        None
        if evidence_gaps
        else round(sum(item["points_earned"] for item in dimensions), 2)
    )
    if summary.get("total_score") != expected_total:
        raise ValueError("total score does not equal dimension points")
    if expected_total is not None and not 0 <= expected_total <= 100:
        raise ValueError("total score is outside 0–100")
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
    for name, artifact in (
        ("disposition", disposition),
        ("corpus index", index_entry),
    ):
        if artifact.get("scoring_version") != SCORING_VERSION:
            raise ValueError(f"{name} scoring version differs from report")
        if artifact.get("total_score") != summary["total_score"]:
            raise ValueError(f"{name} total differs from report")
        if artifact.get("dimension_scores") != dimensions:
            raise ValueError(f"{name} dimensions differ from report")
        if artifact.get("hard_gates") != hard_gates:
            raise ValueError(f"{name} Hard Gates differ from report")
    if bool(index_entry.get("publishable")) != (
        summary["final_verdict"] == "PASS"
    ):
        raise ValueError("corpus publishable flag does not match verdict")
    if summary["final_verdict"] == "PASS":
        qualification = report.get("materials_qualification", {})
        if (
            qualification.get("authoritative") is not True
            or not qualification.get("evidence")
        ):
            raise ValueError(
                "PASS lacks authoritative materials qualification"
            )
        if report["configuration"]["paper_mode"] == "no_paper":
            adjudication = report.get("paper_trigger_adjudication")
            if (
                not isinstance(adjudication, list)
                or {
                    item.get("trigger")
                    for item in adjudication
                    if isinstance(item, dict)
                }
                != {
                    "SCIENTIFIC_CONFLICT",
                    "NECESSARY_INFORMATION_MISSING",
                    "GOLD_PROVENANCE_UNCERTAIN",
                    "EXPLICIT_REPRODUCTION_CLAIM",
                }
                or any(
                    item.get("status") != "NOT_TRIGGERED"
                    or not item.get("evidence")
                    for item in adjudication
                )
            ):
                raise ValueError(
                    "PASS lacks complete no-paper trigger adjudication"
                )
        coverage = checker.get("probe_coverage", {})
        if set(coverage) != {
            "positive",
            "negative",
            "discrimination",
            "equivalence",
        }:
            raise ValueError("PASS lacks dynamic probe coverage records")
        if any(
            coverage[name].get("status") != "ASSESSED"
            for name in ("positive", "negative")
        ):
            raise ValueError("PASS lacks assessed positive/negative probes")
        for probe_class in ("discrimination", "equivalence"):
            status = coverage[probe_class].get("status")
            provenance = coverage[probe_class].get("provenance", {})
            if status == "ASSESSED" and (
                provenance.get("oracle_used") is not False
                or provenance.get("source_kind")
                != "INDEPENDENT_PUBLIC_FIXTURE"
                or not provenance.get("fixture_hashes")
            ):
                raise ValueError(
                    f"PASS has invalid {probe_class} probe provenance"
                )
            if status == "NOT_ASSESSABLE" and (
                provenance.get("oracle_used") is not False
                or provenance.get("source_kind") != "NONE"
                or provenance.get("fixture_hashes") != {}
            ):
                raise ValueError(
                    f"PASS has dishonest unavailable {probe_class} provenance"
                )
            if status not in {"ASSESSED", "NOT_ASSESSABLE"}:
                raise ValueError(
                    f"PASS has invalid {probe_class} probe status"
                )
    oracle = checker.get("solution_oracle", {})
    if oracle.get("scientific_evidence") is not False:
        raise ValueError("solution Oracle was treated as scientific evidence")
    if checker.get("solution_content_inspected") is not False:
        raise ValueError("solution content escaped the isolated Oracle boundary")
    if report["scope"].get("solution_content_inspected") is not False:
        raise ValueError("report claims solution content inspection")
    if bool(report["scope"].get("solution_oracle_executed")) != bool(
        oracle.get("used")
    ):
        raise ValueError("report solution Oracle execution status is inconsistent")
    expected_ids = [
        f"FINDING-{index:03d}"
        for index in range(1, len(findings) + 1)
    ]
    if [item.get("finding_id") for item in findings] != expected_ids:
        raise ValueError("finding IDs are not consecutive")
    if len(report["findings"]) != len(findings):
        raise ValueError("finding count differs between JSON and JSONL")
    for item in findings:
        if not isinstance(item.get("affected_locations"), list) or not all(
            isinstance(location, dict)
            and set(location) == {"file", "line", "quote"}
            and isinstance(location["file"], str)
            and bool(location["file"])
            for location in item["affected_locations"]
        ):
            raise ValueError("finding lacks exact affected location schema")
        for field in (
            "observed_fact",
            "impact",
            "minimal_repair",
            "retest",
        ):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"finding lacks {field}")
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
