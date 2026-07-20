#!/usr/bin/env python3
"""Synthesize, validate, and safely replace a materials audit bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from prepare_audit_output import (
    QUALITY_EVIDENCE_ROLES,
    collect_review_implementation_hashes,
    sha256_file,
)
from canonical_status import canonical_fields
from deterministic_contract import (
    annotate_findings,
    apply_deterministic_gate,
    deterministic_repair_summary,
    evaluate_deterministic_contract,
    validate_deterministic_contract,
)


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
QA_AXIS_NAMES = (
    "factual_accuracy",
    "answer_leakage",
    "instruction_completeness",
    "checker_instruction_consistency",
)
QA_AXIS_STATUSES = {"PASS", "WARNING", "FAIL", "NOT_ASSESSABLE"}
QA_EVIDENCE_SEMANTICS = {
    "PASS": "supports_pass",
    "WARNING": "supports_warning",
    "FAIL": "supports_failure",
    "NOT_ASSESSABLE": "supports_limitation",
}


def canonical_json_hash(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()
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
SEVERITY_RANK = {"FATAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}

# ---------------------------------------------------------------------------
# v11 seven-dimension model (C01-C07).
#
# The canonical weights and definitions live in
# ``references/scoring-rubric.md`` (single source of truth); the numeric
# mirror below MUST stay in sync with that document.  Each dimension's
# ``max_points`` equals its weight so the weighted total reduces to the sum of
# earned points on a 0-100 scale.
# ---------------------------------------------------------------------------
V11_SCORING_VERSION = "materials-review-scoring/1.1"
V11_DIMENSIONS = ("C01", "C02", "C03", "C04", "C05", "C06", "C07")
V11_DIMENSION_WEIGHTS = {
    "C01": 10,
    "C02": 20,
    "C03": 20,
    "C04": 20,
    "C05": 10,
    "C06": 10,
    "C07": 10,
}
V11_DIMENSION_TITLES = {
    "C01": "domain_admission",
    "C02": "task_design_and_file_consistency",
    "C03": "scientific_validity_and_solvability",
    "C04": "scoring_semantics",
    "C05": "answer_leakage",
    "C06": "reproducibility",
    "C07": "difficulty_and_auditability",
}
V11_DIMENSION_FAMILY = {
    "C01": "admission",
    "C02": "deterministic",
    "C03": "scientific",
    "C04": "deterministic",
    "C05": "scientific",
    "C06": "scientific",
    "C07": "deterministic_scientific",
}
# Key (gate-bound) dimensions may escalate the whole package to
# NOT_ASSESSABLE when their evidence is missing.  Non-key dimensions (e.g.
# C07 discrimination gaps) only lose points inside their own dimension.
V11_KEY_DIMENSIONS = {"C01", "C03", "C04", "C06"}
# Hard gate code -> bound dimension (plan sec 3.1 / 7.1 step 3).
V11_HARD_GATE_DIMENSION = {
    "NON_MATERIALS_TASK": "C01",
    "SCIENTIFIC_TARGET_INVALID": "C03",
    "UNRECOVERABLE_TASK_DEFINITION": "C03",
    "CHECKER_CORE_TASK_UNASSESSED": "C04",
    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE": "C06",
}
HARD_GATE_CODE_DIMENSION = {
    "NON_MATERIALS_TASK": "C01",
    "SCIENTIFIC_TARGET_INVALID": "C03",
    "CHECKER_CORE_TASK_UNASSESSED": "C04",
    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE": "C06",
}
# Explicit finding-code -> C0x attribution (finding-attribution dimensions).
V11_C01_CODES = {
    "NON_MATERIALS_TASK",
    "MATERIALS_ADMISSIBILITY_REQUIRES_ADJUDICATION",
}
V11_C02_CODES = {
    "INSTRUCTION_INTERNAL_INCONSISTENCY",
    "OUTPUT_DECLARATION_MISMATCH",
    "OUTPUT_NOT_CONTRACTED",
    "OUTPUT_NOT_SCORED",
    "EVIDENCE_NOT_ENFORCED",
    "INSTRUCTION_ONLY_OUTPUT",
    "INVALID_WEIGHT",
    "WEIGHTS_NOT_ONE",
    "MISSING_FILE",
    "PARSE_ERROR",
    "SOLUTION_ROLE_MISSING",
    "SOLUTION_ORACLE_MISSING",
    "SOLUTION_ORACLE_BROKEN",
    "INVALID_GRADING_SPEC_SCHEMA",
    "CONTRADICTORY_OUTPUT_ROLE",
}
V11_C03_CODES = {
    "SCIENTIFIC_TARGET_INVALID",
    "UNRECOVERABLE_TASK_DEFINITION",
}
V11_C04_CODES = {
    "CHECKER_STATIC_ANALYSIS_UNAVAILABLE",
    "SCORER_MISSING_RETURN",
    "SCORER_RETURN_NOT_TOTAL",
    "ALWAYS_ZERO_SCORER",
    "ALWAYS_PASS_SCORER",
    "DIVISION_BY_ZERO_LITERAL",
    "CHECKER_CORE_TASK_UNASSESSED",
    "SCORING_COMPONENT_NOT_BOUND",
    "ZERO_WEIGHT_SCORING_COMPONENT",
    "INVALID_PASS_THRESHOLD",
    "CHECKER_CRASH",
    "CHECKER_RESULT_UNUSABLE",
    "ADVERSARIAL_OUTPUT_PASSES",
    "ORACLE_POSITIVE_MOCK_REJECTED",
    "KNOWN_VALID_OUTPUT_REJECTED",
}
V11_C05_CODES = {
    "SOLUTION_BOUNDARY_VIOLATION",
    "ANSWER_LEAKAGE",
    "ORACLE_VALUE_LEAKED",
}
V11_C06_CODES = {"E2_SMOKE_FAILED"}
V11_C07_CODES = {
    "SCIENTIFIC_QUALITY_GRADIENT_VIOLATION",
    "SCIENTIFIC_INVARIANCE_VIOLATION",
    "SINGLE_COMPONENT_CAN_PASS",
    "INDEPENDENT_PUBLIC_FIXTURE_UNAVAILABLE",
}
V11_FROM_LEGACY_DIMENSION = {
    "scientific_validity": "C03",
    "instruction_answerability": "C02",
    "checker_gold_alignment": "C04",
    "robustness_discrimination": "C07",
    "solution_completeness": "C02",
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
    elif code == "ORACLE_POSITIVE_MOCK_REJECTED":
        repair = (
            "Diagnose and correct the checker/Gold contract that rejects the "
            "successfully generated isolated Oracle mock. Do not alter the "
            "Oracle producer unless separate execution evidence shows that it "
            "failed to generate the contracted files."
        )
        retest = (
            "Run the Review CLI and require positive_oracle to meet the checker "
            "pass threshold without exposing or using Oracle values as "
            "scientific evidence."
        )
    elif code in {
        "SCORER_MISSING_RETURN",
        "SCORER_RETURN_NOT_TOTAL",
        "SCORING_COMPONENT_NOT_BOUND",
        "ALWAYS_ZERO_SCORER",
        "ALWAYS_PASS_SCORER",
        "DIVISION_BY_ZERO_LITERAL",
    }:
        repair = (
            "Correct the checker scorer runtime contract so every declared "
            "scoring component is bound, returns a finite score, and evaluates "
            "the intended direction without changing the scientific task."
        )
        retest = (
            "Re-run positive, negative, component-isolation, malformed, "
            "always-zero, always-pass, division, and direction probes; verify "
            "each declared component changes the final score as specified."
        )
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
    confirmed_direct_input_barriers = {
        "PERMANENT_UNAVAILABLE",
        "REQUIRES_AUTH",
        "REQUIRES_LICENSE",
        "IDENTITY_MISMATCH",
    }
    if (
        source.get("code") == "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
        and isinstance(source_evidence, dict)
        and source_evidence.get("status")
        not in confirmed_direct_input_barriers
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
    code = source["code"]
    deduction_group = source.get("deduction_group") or source.get("root_cause")
    if not deduction_group and isinstance(source.get("evidence"), dict):
        deduction_group = source["evidence"].get(
            "deduction_group"
        ) or source["evidence"].get("root_cause")
    if not deduction_group:
        deduction_group = finding_id
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
        "deduction_group": deduction_group,
    }


def scored_dimension_for(finding: dict[str, Any]) -> str | None:
    code = finding["title"]
    files = finding["affected_files"]
    if code == "SINGLE_COMPONENT_THRESHOLD_REACHABLE":
        return None
    if code == "ORACLE_POSITIVE_MOCK_REJECTED":
        return "checker_gold_alignment"
    if code in {
        "SCORER_MISSING_RETURN",
        "SCORER_RETURN_NOT_TOTAL",
        "SCORING_COMPONENT_NOT_BOUND",
        "ALWAYS_ZERO_SCORER",
        "ALWAYS_PASS_SCORER",
        "DIVISION_BY_ZERO_LITERAL",
    }:
        return "checker_gold_alignment"
    if code.startswith("SOLUTION_"):
        return "solution_completeness"
    if code in {
        "ADVERSARIAL_OUTPUT_PASSES",
        "CHECKER_CRASH",
        "CHECKER_RESULT_UNUSABLE",
        "INDEPENDENT_PUBLIC_FIXTURE_UNAVAILABLE",
        "SCIENTIFIC_QUALITY_GRADIENT_VIOLATION",
        "SCIENTIFIC_INVARIANCE_VIOLATION",
        "SINGLE_COMPONENT_CAN_PASS",
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
    if "gold_provenance" in contract_gaps:
        unavailable.add("checker_gold_alignment")
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
        group_representatives: dict[str, str] = {}
        for group in {
            item.get("deduction_group", item["finding_id"])
            for item in relevant
        }:
            members = [
                item
                for item in relevant
                if item.get("deduction_group", item["finding_id"]) == group
            ]
            representative = sorted(
                members,
                key=lambda item: (
                    -SEVERITY_RANK[item["severity"]],
                    item["finding_id"],
                ),
            )[0]
            group_representatives[group] = representative["finding_id"]
        for item in relevant:
            deduction_group = item.get("deduction_group", item["finding_id"])
            fraction = SEVERITY_DEDUCTION_FRACTIONS[item["severity"]]
            if dimension == "solution_completeness" and item["severity"] in {
                "FATAL",
                "HIGH",
            }:
                fraction = 1.0
            deduction_applied = (
                group_representatives[deduction_group] == item["finding_id"]
            )
            points = round(maximum * fraction, 2) if deduction_applied else 0.0
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
                    "deduction_group": deduction_group,
                    "deduction_applied": deduction_applied,
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
                    "attempted": bool(oracle.get("attempted")),
                    "setup_prepared": bool(oracle.get("setup_prepared")),
                    "producer_started": bool(oracle.get("producer_started")),
                    "executed": bool(oracle.get("executed")),
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
    checker_structurally_unavailable = any(
        item.get("title")
        in {
            "MISSING_FILE",
            "PARSE_ERROR",
            "CHECKER_STATIC_ANALYSIS_UNAVAILABLE",
        }
        and any(
            location.get("file") == "tests/checker.py"
            for location in item.get("affected_locations", [])
            if isinstance(location, dict)
        )
        for item in findings
    )
    direct_input_temporary_gap = any(
        item.get("title", "").startswith(
            "INDISPENSABLE_DIRECT_INPUT_"
        )
        and item.get("title")
        != "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
        and isinstance(item.get("evidence"), dict)
        and item["evidence"].get("status")
        in {
            "TRANSIENT_FAILURE",
            "RATE_LIMITED",
            "BLOCKED_PRIVATE_NETWORK",
            "UNVERIFIED",
        }
        for item in findings
    )
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
            (
                "The required checker is missing or unparseable; this is a "
                "repairable structural defect, not a confirmed unrecoverable "
                "core-task alignment failure."
                if checker_structurally_unavailable
                else "The checker core-task Hard Gate is not assessable because "
                "checker_gold_alignment remains a temporary evidence gap."
            )
            if status == "NOT_ASSESSABLE"
            and code == "CHECKER_CORE_TASK_UNASSESSED"
            else (
                "Direct-input availability is not assessable because the "
                "audit host encountered a temporary access limitation."
            )
            if status == "NOT_ASSESSABLE"
            and code == "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
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
            and (
                "checker_gold_alignment" in evidence_gaps
                or checker_structurally_unavailable
            )
        ) or (
            code == "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
            and direct_input_temporary_gap
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


def scored_dimension_v11_for(finding: dict[str, Any]) -> str | None:
    """Attribute a finding to a C01-C07 dimension (plan sec 7 mapping)."""
    code = finding["title"]
    if code == "SINGLE_COMPONENT_THRESHOLD_REACHABLE":
        return None
    if code in V11_C01_CODES:
        return "C01"
    if code in V11_C05_CODES:
        return "C05"
    if code in V11_C07_CODES:
        return "C07"
    if code in V11_C04_CODES:
        return "C04"
    if code in V11_C03_CODES:
        return "C03"
    if code in V11_C02_CODES:
        return "C02"
    if code.startswith("INDISPENSABLE_DIRECT_INPUT_"):
        return "C06"
    if finding.get("category") == "RESOURCE_USABILITY":
        return "C06"
    if code in V11_C06_CODES:
        return "C06"
    if code.startswith("PAPER_"):
        name = code[len("PAPER_"):]
        if name.startswith(("INSTRUCTION_", "DATA_", "METHOD_")):
            return "C03"
        if "GOLD" in name:
            return "C04"
        if "LEAK" in name or "IDENTITY" in name:
            return "C05"
        return "C06"
    if code.startswith("SOLUTION_"):
        return "C02"
    if code.startswith("MATERIALS_"):
        return "C01"
    legacy = scored_dimension_for(finding)
    if legacy is None:
        return "C02"
    return V11_FROM_LEGACY_DIMENSION.get(legacy, "C02")


def dimensions_v11_scores(
    findings: list[dict[str, Any]],
    unavailable: set[str],
) -> list[dict[str, Any]]:
    """Compute the C01-C07 records: earned/normalized/status/finding_ids.

    ``unavailable`` holds the *key* dimensions whose evidence is temporarily
    missing.  Only those dimensions become NOT_ASSESSABLE; every other
    dimension keeps scoring (non-key gaps only deduct within their own
    dimension, never escalating the whole package).
    """
    records: list[dict[str, Any]] = []
    for dimension in V11_DIMENSIONS:
        maximum = V11_DIMENSION_WEIGHTS[dimension]
        relevant = [
            item
            for item in findings
            if scored_dimension_v11_for(item) == dimension
        ]
        group_representatives: dict[str, str] = {}
        for group in {
            item.get("deduction_group", item["finding_id"])
            for item in relevant
        }:
            members = [
                item
                for item in relevant
                if item.get("deduction_group", item["finding_id"]) == group
            ]
            representative = sorted(
                members,
                key=lambda item: (
                    -SEVERITY_RANK[item["severity"]],
                    item["finding_id"],
                ),
            )[0]
            group_representatives[group] = representative["finding_id"]
        deductions: list[dict[str, Any]] = []
        deducted = 0.0
        for item in relevant:
            deduction_group = item.get("deduction_group", item["finding_id"])
            fraction = SEVERITY_DEDUCTION_FRACTIONS[item["severity"]]
            deduction_applied = (
                group_representatives[deduction_group] == item["finding_id"]
            )
            points = round(maximum * fraction, 2) if deduction_applied else 0.0
            deducted += points
            deductions.append(
                {
                    "deduction_id": (
                        f"V11-DEDUCTION-{item['finding_id']}-{dimension}"
                    ),
                    "finding_id": item["finding_id"],
                    "points": points,
                    "severity": item["severity"],
                    "deduction_group": deduction_group,
                    "deduction_applied": deduction_applied,
                }
            )
        if dimension in unavailable and dimension in V11_KEY_DIMENSIONS:
            earned: float | int | None = None
            normalized: float | None = None
            status = "NOT_ASSESSABLE"
        else:
            earned = round(max(0.0, maximum - deducted), 2)
            if isinstance(earned, float) and earned.is_integer():
                earned = int(earned)
            normalized = round(float(earned) / maximum * 100, 4)
            status = (
                "FAIL"
                if normalized < 50
                else "WARNING"
                if normalized < 80
                else "PASS"
            )
        records.append(
            {
                "dimension": dimension,
                "title": V11_DIMENSION_TITLES[dimension],
                "family": V11_DIMENSION_FAMILY[dimension],
                "weight": maximum,
                "max_points": maximum,
                "points_earned": earned,
                "normalized": normalized,
                "key_dimension": dimension in V11_KEY_DIMENSIONS,
                "status": status,
                "finding_ids": [item["finding_id"] for item in relevant],
                "deductions": deductions,
            }
        )
    return records


def v11_weighted_total(
    dimensions_v11: list[dict[str, Any]],
) -> tuple[float | None, list[str]]:
    """Weighted 0-100 total; None when a key dimension is NOT_ASSESSABLE."""
    key_gaps = [
        item["dimension"]
        for item in dimensions_v11
        if item["points_earned"] is None
    ]
    if key_gaps:
        return None, key_gaps
    weight_sum = sum(item["weight"] for item in dimensions_v11)
    if weight_sum == 0:
        return None, key_gaps
    weighted = sum(
        item["weight"] * float(item["normalized"])
        for item in dimensions_v11
    )
    total = round(weighted / weight_sum, 2)
    if float(total).is_integer():
        total = int(total)
    return total, key_gaps


def scoring_verdict_v11(
    findings: list[dict[str, Any]],
    dimensions_v11: list[dict[str, Any]],
    hard_gates: list[dict[str, Any]],
) -> tuple[str, float | None, bool, str, list[str]]:
    """Stage 3 disposition on the C01-C07 weighted total (plan sec 7.1)."""
    total, evidence_gaps = v11_weighted_total(dimensions_v11)
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
            "Key-dimension evidence is temporarily unavailable: "
            + ", ".join(evidence_gaps),
            evidence_gaps,
        )
    if total is None or total < 60:
        return (
            "REJECT",
            total,
            False,
            "The authoritative C01-C07 weighted score is below 60/100.",
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
            "The C01-C07 weighted score is 60-79/100 or a repairable HIGH "
            "with sufficient evidence remains.",
            evidence_gaps,
        )
    return (
        "PASS",
        total,
        False,
        "The C01-C07 weighted score is at least 80/100 with no unresolved "
        "HIGH/FATAL and no Hard Gate.",
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


def _qa_locations(
    findings: list[dict[str, Any]], codes: set[str]
) -> list[dict[str, Any]]:
    locations: list[dict[str, Any]] = []
    for item in findings:
        if item.get("title") not in codes:
            continue
        for location in item.get("affected_locations", []):
            if location not in locations:
                locations.append(location)
    return locations


def _qa_evidence(
    findings: list[dict[str, Any]], codes: set[str]
) -> list[dict[str, Any]]:
    return [
        {
            "finding_id": item.get("finding_id"),
            "observed_fact": item.get("observed_fact"),
            "semantic": "supports_failure",
        }
        for item in findings
        if item.get("title") in codes
    ]


def _qa_base_location(root: Path) -> list[dict[str, Any]]:
    instruction = root / "instruction.md"
    if not instruction.is_file():
        return []
    for number, line in enumerate(
        instruction.read_text(encoding="utf-8", errors="replace").splitlines(),
        start=1,
    ):
        if line.strip():
            return [
                {
                    "file": "instruction.md",
                    "line": number,
                    "quote": line.strip(),
                }
            ]
    return []


def derive_qa_axes(
    root: Path,
    findings: list[dict[str, Any]],
    checker_result: dict[str, Any],
    contract_map: dict[str, Any],
    paper_result: dict[str, Any],
    materials_assessment: dict[str, Any] | None,
) -> dict[str, dict[str, Any]]:
    """Derive four non-scoring QA conclusions from bounded evidence."""
    scientific_codes = {
        "NON_MATERIALS_TASK",
        "SCIENTIFIC_TARGET_INVALID",
    }
    paper_scientific_codes = {
        item.get("title")
        for item in findings
        if str(item.get("title", "")).startswith("PAPER_")
        and any(
            marker in str(item.get("title", ""))
            for marker in ("INSTRUCTION_", "DATA_", "METHOD_")
        )
    }
    scientific_codes.update(
        item for item in paper_scientific_codes if isinstance(item, str)
    )
    completeness_codes = {
        "UNRECOVERABLE_TASK_DEFINITION",
        "INSTRUCTION_ONLY_OUTPUT",
    }
    consistency_codes = {
        "OUTPUT_NOT_CONTRACTED",
        "OUTPUT_NOT_SCORED",
        "EVIDENCE_NOT_ENFORCED",
        "SCORING_COMPONENT_NOT_BOUND",
        "SCORER_MISSING_RETURN",
        "SCORER_RETURN_NOT_TOTAL",
        "CHECKER_CORE_TASK_UNASSESSED",
    }
    leakage_codes = {
        "ANSWER_LEAKAGE",
        "ORACLE_VALUE_LEAKED",
        "SOLUTION_BOUNDARY_VIOLATION",
    }
    base_location = _qa_base_location(root)

    def entry(
        status: str,
        evidence: list[dict[str, Any]],
        locations: list[dict[str, Any]],
        *limitations: str,
    ) -> dict[str, Any]:
        default_semantic = QA_EVIDENCE_SEMANTICS[status]
        semantic_evidence = []
        for item in evidence:
            value = dict(item)
            value.setdefault(
                "semantic",
                (
                    "supports_failure"
                    if "finding_id" in value
                    else default_semantic
                ),
            )
            semantic_evidence.append(value)
        return {
            "status": status,
            "evidence": semantic_evidence,
            "locations": locations,
            "limitations": list(limitations),
        }

    scientific_evidence = _qa_evidence(findings, scientific_codes)
    scientific_locations = _qa_locations(findings, scientific_codes)
    if scientific_evidence:
        factual = entry("FAIL", scientific_evidence, scientific_locations)
    elif materials_assessment is None or paper_result.get("status") == "NOT_ASSESSED":
        factual = entry(
            "NOT_ASSESSABLE",
            [{"source": "instruction/tests", "fact": "No independent factual adjudication was supplied."}],
            base_location,
            "E1 checks the public contract and does not independently verify scientific facts.",
        )
    elif paper_result.get("status") == "NOT_ASSESSABLE":
        factual = entry(
            "NOT_ASSESSABLE",
            [
                {
                    "source": "paper_grounded_review",
                    "fact": (
                        "Paper-grounded factual accuracy could not be assessed."
                    ),
                }
            ],
            base_location,
            "Unavailable paper evidence cannot support a factual-accuracy PASS.",
        )
    elif paper_result.get("status") == "FAIL":
        factual = entry(
            "FAIL",
            [{"source": "paper_grounded_review", "fact": "Paper-grounded evidence contains a factual inconsistency."}],
            base_location,
        )
    elif paper_result.get("status") == "WARNING":
        factual = entry(
            "WARNING",
            [{"source": "paper_grounded_review", "fact": "Paper-grounded factual evidence requires attention."}],
            base_location,
        )
    else:
        factual = entry(
            "PASS",
            [{"source": "paper_grounded_review", "fact": "Paper-grounded factual evidence passed."}],
            base_location,
        )

    leakage_evidence = _qa_evidence(findings, leakage_codes)
    leakage_locations = _qa_locations(findings, leakage_codes)
    runtime_has_solution = any(
        item.get("evidence", {}).get("runtime_package_contains_solution") is True
        for item in checker_result.get("tests", [])
    )
    if checker_result.get("solution_content_inspected") is True or runtime_has_solution:
        leakage_evidence.append(
            {
                "source": "checker_runtime",
                "fact": "The isolated checker runtime contained solution content.",
            }
        )
        leakage_locations = leakage_locations or [
            {"file": "solution/", "line": None, "quote": None}
        ]
    if leakage_evidence:
        leakage = entry("FAIL", leakage_evidence, leakage_locations)
    elif checker_result.get("solution_oracle", {}).get("executed") is True:
        leakage = entry(
            "PASS",
            [
                {
                    "source": "oracle_boundary",
                    "fact": "The Oracle was used only to create a positive mock and its content was not inspected.",
                }
            ],
            [{"file": "solution/solve.sh", "line": None, "quote": None}],
        )
    else:
        leakage = entry(
            "NOT_ASSESSABLE",
            [{"source": "oracle_boundary", "fact": "No isolated Oracle execution established the leakage boundary."}],
            base_location,
            "Answer leakage requires an isolated Oracle boundary or an explicit leakage finding.",
        )

    completeness_evidence = _qa_evidence(findings, completeness_codes)
    completeness_locations = _qa_locations(findings, completeness_codes)
    unclassified = contract_map.get("unclassified_outputs", [])
    if completeness_evidence:
        completeness = entry(
            "FAIL", completeness_evidence, completeness_locations
        )
    elif unclassified:
        completeness = entry(
            "WARNING",
            [
                {
                    "source": "instruction_contract",
                    "fact": (
                        "Instruction outputs remain unclassified: "
                        + ", ".join(sorted(unclassified))
                    ),
                }
            ],
            base_location,
            "Unclassified outputs require human adjudication before a completeness PASS.",
        )
    elif contract_map.get("requirements"):
        completeness = entry(
            "PASS",
            [
                {
                    "source": "instruction_contract",
                    "fact": "All parsed workflow requirements have a contract row.",
                }
            ],
            base_location,
        )
    else:
        completeness = entry(
            "NOT_ASSESSABLE",
            [{"source": "instruction_contract", "fact": "No workflow requirements were parsed."}],
            base_location,
            "Instruction completeness requires at least one parsed workflow requirement.",
        )

    consistency_evidence = _qa_evidence(findings, consistency_codes)
    consistency_locations = _qa_locations(findings, consistency_codes)
    runtime = checker_result.get("runtime") or {}
    if consistency_evidence:
        consistency = entry(
            "FAIL", consistency_evidence, consistency_locations
        )
    elif (
        runtime.get("status") == "NOT_ASSESSABLE"
        or (
            checker_result.get("tests")
            and all(
                item.get("runtime_not_assessable") is True
                for item in checker_result["tests"]
            )
        )
    ):
        consistency = entry(
            "NOT_ASSESSABLE",
            [
                {
                    "source": "checker_runtime",
                    "fact": "The Harbor verifier could not be assessed in the available runtime.",
                }
            ],
            base_location,
            "Audit-host dependency failures do not establish checker/instruction consistency.",
        )
    elif checker_result.get("tests"):
        consistency = entry(
            "PASS",
            [
                {
                    "source": "checker_runtime",
                    "fact": "The Harbor verifier entrypoint produced checker cases for the declared contract.",
                }
            ],
            base_location,
        )
    else:
        consistency = entry(
            "NOT_ASSESSABLE",
            [{"source": "checker_runtime", "fact": "No checker cases established runtime consistency."}],
            base_location,
            "Checker/Instruction consistency requires an assessable verifier run.",
        )
    return {
        "factual_accuracy": factual,
        "answer_leakage": leakage,
        "instruction_completeness": completeness,
        "checker_instruction_consistency": consistency,
    }


def markdown_summary(report: dict[str, Any]) -> str:
    summary = report["summary"]
    configuration = report["configuration"]
    deterministic = report["deterministic_contract"]
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
    v11_lines = "\n".join(
        f"- {item['dimension']} {item['title']} "
        f"[{item['family']}]: {item['status']} "
        f"({item['points_earned']}/{item['max_points']}, "
        f"normalized={item['normalized']}%, "
        f"findings={item['finding_ids']})"
        for item in report.get("dimensions_v11", [])
    ) or "No C01-C07 dimension scores were computed."
    dimension_lines = (
        "### C01-C07 (authoritative)\n\n"
        f"{v11_lines}\n\n"
        f"- Weighted total (0-100): {report['summary']['total_score']}\n"
        "- Weights: "
        + ", ".join(
            f"{name}={weight}"
            for name, weight in V11_DIMENSION_WEIGHTS.items()
        )
        + "\n\n### Legacy internal dimensions (compatibility)\n\n"
        + (
            "\n".join(
                f"- {item['dimension']}: {item['status']} "
                f"({item['points_earned']}/{item['max_points']}, "
                f"normalized={item['normalized_score']}, "
                f"deductions={item['deduction_ids']})"
                for item in report["dimension_scores"]
            )
            or "No legacy dimension scores were computed."
        )
        + f"\n- Legacy total (0-100, legacy): "
        f"{report['summary'].get('legacy_total_score')}"
    )
    execution = report["execution_evidence"]
    checker_runtime = report["checker_runtime"]
    checker_runtime_summary = (
        f"Verifier entrypoint: {checker_runtime['verifier_entrypoint']}\n"
        f"Runtime provenance: {checker_runtime['runtime_provenance']}\n"
        f"Runtime status: {checker_runtime['status']}"
    )
    if execution["claim"] == "SMOKE_RUN":
        checker_assessment = (
            "The real checker executed before the E2 smoke."
        )
        execution_assessment = (
            f"Status: E2_SMOKE\nReason: {execution['reason']}"
        )
    elif (
        report["checker_tests"]
        and checker_runtime["status"] == "ASSESSED"
    ):
        checker_assessment = (
            "The real checker executed in a solution-free runtime.\n"
            + checker_runtime_summary
        )
        execution_assessment = (
            "Status: E1_ONLY\n"
            "Reason: The checker ran, but the scientific workflow did not."
        )
    else:
        unavailable_reason = checker_runtime.get("reason") or (
            "The verifier did not produce assessable runtime evidence."
        )
        checker_assessment = (
            "Status: NOT_ASSESSED\n"
            f"Reason: {unavailable_reason}\n"
            + checker_runtime_summary
        )
        execution_assessment = (
            "Status: E1_NOT_ASSESSABLE\n"
            "Reason: The scientific workflow did not run and verifier evidence was unavailable."
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
    contract_map = report.get("contract_map", {})
    requirement_chains = (
        contract_map.get("requirement_chains", [])
        if isinstance(contract_map, dict)
        else []
    )
    contract_map_lines = (
        "\n".join(
            "- [requirement={requirement_index}; declaration={declaration_index}] "
            "{step} {title}: requirement={quote}; agent_work={work}; "
            "core_output={output} ({role}); checker_read={read}; "
            "checker_score={score}".format(
                requirement_index=item.get("requirement_index"),
                declaration_index=item.get("declaration_index"),
                step=item.get("instruction_requirement", {}).get("step"),
                title=item.get("instruction_requirement", {}).get("title"),
                quote=item.get("instruction_requirement", {}).get("quote"),
                work=item.get("agent_work"),
                output=item.get("core_output"),
                role=item.get("output_role"),
                read=item.get("checker_read"),
                score=item.get("checker_score"),
            )
            for item in requirement_chains
        )
        or "No requirement-linked mapping was established."
    )
    gold = report.get("gold_provenance")
    if not isinstance(gold, dict):
        gold = paper["dimensions"].get("gold_provenance")
    gold_assessment = (
        f"Status: {gold['status']}\nReason: "
        f"{gold.get('rationale', gold.get('reason'))}"
        if gold is not None
        else "Status: NOT_ASSESSED\n"
        "Reason: Gold provenance was not assessed."
    )
    scope_mode = (
        f"paper-grounded {configuration['execution_level']}"
        if configuration["paper_mode"] == "paper_grounded"
        else f"no-paper {configuration['execution_level']}"
    )
    next_step = (
        "Use the fixed verdict and route for production disposition."
        if configuration["paper_mode"] == "paper_grounded"
        else "Continue survivors with the source-bound paper-grounded E1."
    )
    oracle_boundary = (
        "The solution Oracle ran only in an isolated positive-mock workspace; "
        "its values are neither reported nor used as scientific evidence."
        if report["scope"]["solution_oracle_executed"]
        else "No solution Oracle producer process was executed."
    )
    qa_axis_lines = "\n".join(
        f"- {name}: {axis['status']}; evidence={axis['evidence']}; "
        f"locations={axis['locations']}; limitations={axis['limitations']}"
        for name, axis in report["qa_axes"].items()
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
- Deterministic D1-D6 status: {summary['deterministic_status']}
- Deterministic repair state: {summary['repair_state']}
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

### 7.1 Deterministic D1-D6 Contract

- Schema: {deterministic['schema_version']}
- Registry: {deterministic['registry_version']}
- Repair summary: {deterministic['repair_summary']}
- Checks:
{chr(10).join(
    f"  - {item['check_id']}: {item['status']} "
    f"(blocking={item['blocking_finding_ids']}; "
    f"advisory={item['advisory_finding_ids']})"
    for item in deterministic['checks']
)}

## 8. Resource Reachability

{resource_lines}

## 9. Instruction and Task Design

The audit records process artifacts only in the contract map; they do not
affect scoring, gates, routes, verdicts, or probes.

Instruction → Agent work → declared output → checker read → checker score:
{contract_map_lines}

## 10. Checker Assessment

{checker_assessment}

## 11. Gold Standard Assessment

{gold_assessment}

## 12. Execution Feasibility

{execution_assessment}

## 13. Reproducibility and Leakage

{oracle_boundary}

First-class QA axes (not weighted dimensions):
{qa_axis_lines}

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
    route = ROUTES[summary["final_verdict"]]
    canonical = canonical_fields(
        summary["final_verdict"],
        publishability=route,
        repair_decision=summary.get("repair_decision", "NOT_REQUIRED"),
        repair_status=summary.get("repair_status", "NOT_APPLICABLE"),
    )
    disposition = {
        "schema_version": "1.0",
        "audit_id": report["audit_id"],
        **canonical,
        "scoring_version": summary["scoring_version"],
        "verdict": summary["final_verdict"],
        "disposition": summary["final_verdict"],
        "repair_state": summary.get("repair_state", "NOT_REQUIRED"),
        "total_score": summary["total_score"],
        "legacy_total_score": summary.get("legacy_total_score"),
        "dimension_scores": report["dimension_scores"],
        "dimensions_v11": report.get("dimensions_v11", []),
        "hard_gates": report["hard_gates"],
        "route": route,
        "publishable": route == "PUBLISH_CANDIDATE",
        "non_destructive": True,
        "original_preserved": True,
        "core_package_roles_mutated": False,
        "evidence_bundle": "benchmark_audit",
        "evidence_gaps": evidence_gaps,
        "deterministic_contract": report["deterministic_contract"],
        "deterministic_repair": report["deterministic_repair"],
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
        **canonical,
        "benchmark": {
            "name": root.name,
            "root": str(root),
            "cluster_id": manifest_data.get("cluster_id"),
            "paper_id": manifest_data.get("paper_id"),
        },
        "final_verdict": summary["final_verdict"],
        "disposition": summary["final_verdict"],
        "scoring_version": summary["scoring_version"],
        "total_score": summary["total_score"],
        "legacy_total_score": summary.get("legacy_total_score"),
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
        "dimensions_v11": report.get("dimensions_v11", []),
        "evidence_gaps": evidence_gaps,
        "deterministic_contract": report["deterministic_contract"],
        "deterministic_repair": report["deterministic_repair"],
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
    external_bindings: dict[str, Any] | None = None,
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
        "environment": None,
        "environment_verified": False,
        "runtime_provenance": "sandbox",
        "verifies_resources": [],
        "returncode": None,
        "stdout": "",
        "stderr": "",
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
        else "AMBIGUOUS"
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
    findings = annotate_findings(findings)
    deterministic_contract = evaluate_deterministic_contract(
        normalized_instruction_contract=static_result.get("contract_map"),
        grading_contract=static_result.get("grading_contract"),
        checker_analysis=static_result.get("contract_map", {}).get(
            "checker_analysis"
        ),
        package_roles=static_result.get("package_roles"),
        findings=findings,
    )
    paper_result = paper_consistency(
        agent_assessment,
        skip_reason=paper_skip_reason,
    )
    qa_axes = derive_qa_axes(
        root,
        findings,
        checker_result,
        static_result.get("contract_map", {}),
        paper_result,
        materials_assessment,
    )
    contract_gaps = []
    if materials_assessment is None:
        contract_gaps.append("authoritative_materials_qualification")
    static_gold = static_result.get("gold_provenance", {})
    if (
        isinstance(static_gold, dict)
        and static_gold.get("status") != "ASSESSED"
        and not (
            agent_assessment is not None
            and agent_assessment.get("dimensions", {})
            .get("gold_provenance", {})
            .get("status")
            in {"PASS", "WARNING", "FAIL"}
        )
    ):
        contract_gaps.append("gold_provenance")
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
    for gate in hard_gates:
        gate["dimension"] = HARD_GATE_CODE_DIMENSION.get(gate["code"])
    legacy_by_dimension = {item["dimension"]: item for item in dimensions}
    transient_resource_statuses = {
        "TRANSIENT_FAILURE",
        "RATE_LIMITED",
        "BLOCKED_PRIVATE_NETWORK",
        "UNVERIFIED",
    }
    v11_unavailable: set[str] = set()
    if materials_assessment is None:
        v11_unavailable.add("C01")
    if legacy_by_dimension["scientific_validity"]["points_earned"] is None:
        v11_unavailable.add("C03")
    if legacy_by_dimension["checker_gold_alignment"]["points_earned"] is None:
        v11_unavailable.add("C04")
    if any(
        (
            item.get("category") == "RESOURCE_USABILITY"
            or item.get("title", "").startswith("INDISPENSABLE_DIRECT_INPUT_")
        )
        and item.get("title") != "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
        and isinstance(item.get("evidence"), dict)
        and item["evidence"].get("status") in transient_resource_statuses
        for item in findings
    ):
        v11_unavailable.add("C06")
    dimensions_v11 = dimensions_v11_scores(findings, v11_unavailable)
    legacy_gaps = [
        item["dimension"]
        for item in dimensions
        if item["points_earned"] is None
    ]
    legacy_total = (
        None
        if legacy_gaps
        else round(
            sum(float(item["points_earned"]) for item in dimensions), 2
        )
    )
    if legacy_total is not None and float(legacy_total).is_integer():
        legacy_total = int(legacy_total)
    verdict, score, hard_gate, reason, evidence_gaps = scoring_verdict_v11(
        findings,
        dimensions_v11,
        hard_gates,
    )
    verdict, deterministic_reason = apply_deterministic_gate(
        verdict=verdict,
        score=score,
        hard_gate=hard_gate,
        evidence_gaps=evidence_gaps,
        contract=deterministic_contract,
    )
    deterministic_required = (
        deterministic_contract["repair_summary"]["state"] == "REQUIRED"
    )
    if deterministic_reason is not None:
        reason = deterministic_reason
    route = ROUTES[verdict]
    repair_state = (
        "DETERMINISTIC_REPAIR_REQUIRED"
        if deterministic_required
        and verdict == "CONDITIONAL"
        and not hard_gate
        and not evidence_gaps
        and score is not None
        and score >= 60
        else "NOT_REQUIRED"
    )
    audit_route = (
        "PAPER_GROUNDED_E1"
        if (
            read_json(temp_dir / "audit_report.json")["configuration"][
                "paper_mode"
            ]
            == "no_paper"
            and not hard_gate
        )
        else route
    )
    report = read_json(temp_dir / "audit_report.json")
    report["summary"] = {
        "materials_class": materials_class,
        "answer_type": answer_type_for(root),
        "scoring_version": V11_SCORING_VERSION,
        "legacy_scoring_version": SCORING_VERSION,
        "final_verdict": verdict,
        "disposition": verdict,
        "publishable": verdict == "PASS",
        "repair_state": repair_state,
        "deterministic_status": deterministic_contract["repair_summary"][
            "state"
        ],
        "deterministic_repair_required": (
            repair_state == "DETERMINISTIC_REPAIR_REQUIRED"
        ),
        "total_score": score,
        "legacy_total_score": legacy_total,
        "hard_gate_triggered": hard_gate,
        "route": audit_route,
        "publication_route": route,
        "core_reason": reason,
    }
    canonical = canonical_fields(
        verdict,
        publishability=route,
        repair_status=(
            repair_state
            if repair_state == "DETERMINISTIC_REPAIR_REQUIRED"
            else "NOT_APPLICABLE"
        ),
    )
    report.update(canonical)
    report["summary"].update(canonical)
    report["materials_qualification"] = {
        "axes": [],
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
    report["deterministic_contract"] = deterministic_contract
    report["deterministic_repair"] = deterministic_repair_summary(
        deterministic_contract
    )
    report["source_bindings"] = external_bindings or {
        "fixture_hashes": {},
        "assessment_hashes": {},
        "core_contract_digest": None,
    }
    report["resources"] = resource_result["resources"]
    report["execution_evidence"] = execution_evidence
    report["qa_axes"] = qa_axes
    report["paper_consistency"] = paper_result
    report["paper_trigger_adjudication"] = paper_trigger_adjudication
    contract_map = json.loads(json.dumps(static_result.get(
        "contract_map",
        {
            "requirements": [],
            "requirement_chains": [],
            "instruction_outputs": [],
            "process_evidence": [],
            "scored_outputs": [],
            "load_bearing_outputs": [],
            "core_outputs": [],
            "unclassified_outputs": [],
            "role_conflicts": [],
            "checker_analysis": {},
        },
    )))
    component_coverage = checker_result.get("probe_coverage", {}).get(
        "component_isolation"
    )
    checker_analysis = contract_map.get("checker_analysis", {})
    if isinstance(component_coverage, dict) and isinstance(
        checker_analysis, dict
    ):
        for check in checker_analysis.get("dynamic_checks_required", []):
            if (
                isinstance(check, dict)
                and check.get("check") == "component_isolation"
            ):
                check["status"] = component_coverage.get("status", "NOT_RUN")
                check["reason"] = component_coverage.get("reason")
                check["provenance"] = component_coverage.get("provenance", {})
    report["contract_map"] = contract_map
    paper_gold = paper_result.get("dimensions", {}).get("gold_provenance")
    if isinstance(paper_gold, dict):
        report["gold_provenance"] = {
            **paper_gold,
            "mode": "paper_grounded",
            "reason": paper_gold.get("rationale"),
            "outputs": contract_map.get("core_outputs", []),
            "oracle_used": False,
            "provenance": {
                "source_kind": "PAPER_AND_PACKAGE_EVIDENCE",
                "independent": True,
                "evidence": paper_gold.get("evidence", []),
            },
        }
    else:
        report["gold_provenance"] = (
            static_result.get("gold_provenance")
            or contract_map.get("gold_provenance")
            or {
                "status": "NOT_ASSESSABLE",
                "mode": "no_paper",
                "reason": "Gold provenance was not assessed.",
                "oracle_used": False,
            }
        )
    manifest = read_json(temp_dir / "audit_manifest.json")
    report["audit_binding"] = {
        "parent_audit_id": manifest.get("parent_audit_id"),
        "source_hashes": manifest.get("input_hashes", {}),
        "implementation_hash": manifest.get(
            "review_implementation", {}
        ).get("aggregate_hash"),
        "deterministic_contract_digest": deterministic_contract[
            "contract_digest"
        ],
    }
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
    report["dimensions_v11"] = dimensions_v11
    report["scoring_model"] = {
        "version": V11_SCORING_VERSION,
        "weights": dict(V11_DIMENSION_WEIGHTS),
        "severity_deduction_fractions": dict(SEVERITY_DEDUCTION_FRACTIONS),
        "weighted_total": score,
        "legacy_total_score": legacy_total,
        "key_dimensions": sorted(V11_KEY_DIMENSIONS),
        "hard_gate_dimensions": dict(HARD_GATE_CODE_DIMENSION),
    }
    report["checker_runtime"] = checker_result["runtime"]
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
        ],
        "limitations": [
            *static_result["limitations"],
            *checker_result["limitations"],
            *resource_result["limitations"],
        ],
        "assumptions": [
            "known-valid output, when supplied, is independently justified"
        ],
        "solution_oracle_executed": checker_result["solution_oracle"].get(
            "executed", False
        ),
        "solution_content_inspected": False,
    }
    (temp_dir / "audit_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    audit_manifest = read_json(temp_dir / "audit_manifest.json")
    audit_manifest.update(canonical)
    audit_manifest["deterministic_contract_schema_version"] = (
        deterministic_contract["schema_version"]
    )
    audit_manifest["deterministic_contract_digest"] = (
        deterministic_contract["contract_digest"]
    )
    audit_manifest["execution_level"] = report["configuration"][
        "execution_level"
    ]
    audit_manifest["solution_oracle_executed"] = checker_result[
        "solution_oracle"
    ].get("executed", False)
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


def validate_requirement_chains(
    contract_map: dict[str, Any], markdown: str
) -> None:
    requirements = contract_map.get("requirements")
    chains = contract_map.get("requirement_chains")
    if not isinstance(requirements, list) or not isinstance(chains, list):
        raise ValueError("contract map lacks requirement-linked chains")
    expected: dict[tuple[int, int | None], tuple[dict[str, Any], Any]] = {}
    for requirement_index, requirement in enumerate(requirements):
        if not isinstance(requirement, dict):
            raise ValueError("contract map requirement is not an object")
        declarations = requirement.get("evidence", [])
        if not isinstance(declarations, list):
            raise ValueError("contract map requirement evidence is not a list")
        if not declarations:
            expected[(requirement_index, None)] = (requirement, None)
        else:
            for declaration_index, declaration in enumerate(declarations):
                if not isinstance(declaration, dict):
                    raise ValueError(
                        "contract map output declaration is not an object"
                    )
                expected[(requirement_index, declaration_index)] = (
                    requirement,
                    declaration,
                )
    actual: dict[tuple[int, int | None], dict[str, Any]] = {}
    for chain in chains:
        if not isinstance(chain, dict):
            raise ValueError("contract requirement chain is not an object")
        key = (
            chain.get("requirement_index"),
            chain.get("declaration_index"),
        )
        if (
            not isinstance(key[0], int)
            or isinstance(key[0], bool)
            or key in actual
        ):
            raise ValueError("contract requirement chains are incomplete")
        actual[key] = chain
    if set(actual) != set(expected):
        raise ValueError("contract requirement chains are incomplete")
    for key, (requirement, declaration) in expected.items():
        chain = actual[key]
        instruction_requirement = chain.get("instruction_requirement")
        if not isinstance(instruction_requirement, dict):
            raise ValueError("contract chain lacks instruction requirement")
        expected_instruction = {
            "step": requirement.get("step"),
            "title": requirement.get("title"),
            "role": requirement.get("role"),
            "line": (
                declaration.get("line")
                if declaration is not None
                else requirement.get("line")
            ),
            "quote": (
                declaration.get("quote")
                if declaration is not None
                else requirement.get("quote")
            ),
        }
        if instruction_requirement != expected_instruction:
            raise ValueError("contract chain requirement evidence differs")
        expected_output = (
            declaration.get("file") if declaration is not None else None
        )
        if (
            chain.get("agent_work") != requirement.get("agent_work")
            or chain.get("core_output") != expected_output
            or not isinstance(chain.get("output_role"), str)
            or not isinstance(chain.get("checker_read"), str)
            or not isinstance(chain.get("checker_score"), dict)
        ):
            raise ValueError("contract requirement chain is incomplete")
        if declaration is None and (
            chain["output_role"] != "unclassified"
            or chain["checker_read"] != "UNKNOWN_NO_DECLARED_OUTPUT"
            or chain["checker_score"].get("checker_scores")
            != "UNKNOWN_NO_DECLARED_OUTPUT"
            or chain["checker_score"].get("runtime_score_proven") is not False
        ):
            raise ValueError(
                "output-free requirement chain overclaims checker evidence"
            )
        marker = (
            f"[requirement={key[0]}; declaration={key[1]}]"
        )
        if marker not in markdown:
            raise ValueError("Markdown omits a contract requirement chain")


def validate_pass_probe_coverage(coverage: Any) -> None:
    required_coverage = {
        "positive",
        "negative",
        "discrimination",
        "equivalence",
        "component_isolation",
    }
    if not isinstance(coverage, dict) or not required_coverage.issubset(
        coverage
    ):
        raise ValueError("PASS lacks dynamic probe coverage records")
    if any(
        coverage[name].get("status") != "ASSESSED"
        for name in ("positive", "negative")
    ):
        raise ValueError("PASS lacks assessed positive/negative probes")
    for probe_class in ("discrimination", "equivalence"):
        status = coverage[probe_class].get("status")
        provenance = coverage[probe_class].get("provenance", {})
        if status == "ASSESSED":
            if (
                provenance.get("oracle_used") is not False
                or provenance.get("source_kind")
                != "INDEPENDENT_PUBLIC_FIXTURE"
                or not provenance.get("fixture_hashes")
                or not provenance.get("source_role_hashes")
                or not str(
                    provenance.get("fixture_manifest_hash", "")
                ).startswith("sha256:")
            ):
                raise ValueError(
                    f"PASS has invalid {probe_class} probe provenance"
                )
        elif status == "NOT_ASSESSABLE":
            if (
                provenance.get("oracle_used") is not False
                or provenance.get("source_kind") != "NONE"
                or provenance.get("fixture_hashes") != {}
                or provenance.get("source_role_hashes", {}) != {}
                or provenance.get("fixture_manifest_hash") is not None
            ):
                raise ValueError(
                    f"PASS has dishonest unavailable {probe_class} provenance"
                )
        else:
            raise ValueError(
                f"PASS has invalid {probe_class} probe status"
            )
    component_isolation = coverage["component_isolation"]
    component_status = component_isolation.get("status")
    component_provenance = component_isolation.get("provenance", {})
    if (
        component_provenance.get("oracle_used") is not False
        or any(
            "ORACLE" in value.upper()
            for value in _provenance_strings(component_provenance)
        )
    ):
        raise ValueError(
            "PASS component-isolation provenance must be non-Oracle"
        )
    if component_status not in {
        "ASSESSED",
        "NOT_RUN",
        "NOT_ASSESSABLE",
    }:
        raise ValueError("PASS has invalid component-isolation status")
    if component_status == "ASSESSED" and (
        component_provenance.get("source_kind")
        != "INDEPENDENT_PUBLIC_FIXTURE"
        or component_provenance.get("oracle_used") is not False
        or component_provenance.get("source_bindings_verified") is not True
        or component_provenance.get("runtime_bindings_verified") is not True
        or not component_provenance.get("cases_executed")
    ):
        raise ValueError("PASS has invalid component-isolation provenance")
    if (
        component_status in {"NOT_RUN", "NOT_ASSESSABLE"}
        and not component_isolation.get("reason")
    ):
        raise ValueError(
            f"PASS component-isolation {component_status} lacks a reason"
        )
    if component_status == "NOT_RUN" and (
        component_provenance.get("source_kind") != "NONE"
        or component_provenance.get("oracle_used") is not False
        or component_provenance.get("cases_executed") != 0
    ):
        raise ValueError("PASS component-isolation NOT_RUN has invalid provenance")
    task_attacks = (
        coverage["negative"].get("subcoverage", {}).get(
            "task_family_attacks"
        )
    )
    if not isinstance(task_attacks, dict) or not task_attacks:
        raise ValueError("PASS lacks task-family materials attacks")
    for attack, entry in task_attacks.items():
        provenance = entry.get("provenance", {}) if isinstance(entry, dict) else {}
        if (
            not isinstance(entry, dict)
            or entry.get("status")
            not in {"ASSESSED", "NOT_ASSESSABLE", "NOT_APPLICABLE"}
            or not isinstance(provenance, dict)
            or provenance.get("oracle_used") is not False
        ):
            raise ValueError(
                f"PASS has invalid task-family attack coverage: {attack}"
            )


def _provenance_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [
            item
            for child in value.values()
            for item in _provenance_strings(child)
        ]
    if isinstance(value, (list, tuple, set)):
        return [
            item
            for child in value
            for item in _provenance_strings(child)
        ]
    return []


def validate_contract_probe_consistency(
    report: dict[str, Any], checker: dict[str, Any]
) -> None:
    runtime = checker.get("runtime")
    if (
        not isinstance(runtime, dict)
        or runtime.get("verifier_entrypoint") != "tests/test.sh"
        or runtime.get("runtime_provenance")
        not in {"sandbox"}
        or not isinstance(runtime.get("direct_checker_harness"), bool)
        or runtime.get("status")
        not in {"ASSESSED", "NOT_ASSESSABLE"}
    ):
        raise ValueError("checker runtime provenance is invalid")
    if report.get("checker_runtime") != runtime:
        raise ValueError("report/checker runtime provenance mismatch")
    for test in checker.get("tests", []):
        evidence = test.get("evidence")
        if (
            not isinstance(evidence, dict)
            or evidence.get("verifier_entrypoint") != "tests/test.sh"
            or evidence.get("runtime_provenance")
            not in {"sandbox"}
            or evidence.get("direct_checker_harness") is not False
        ):
            raise ValueError("checker test runtime provenance is invalid")
    coverage = checker.get("probe_coverage")
    required = {
        "positive",
        "negative",
        "discrimination",
        "equivalence",
        "component_isolation",
    }
    if not isinstance(coverage, dict) or set(coverage) != required:
        raise ValueError(
            "checker probe coverage must contain exactly five core classes"
        )
    allowed_statuses = {
        "positive": {"ASSESSED", "NOT_ASSESSABLE"},
        "negative": {"ASSESSED", "NOT_ASSESSABLE"},
        "discrimination": {"ASSESSED", "NOT_ASSESSABLE"},
        "equivalence": {"ASSESSED", "NOT_ASSESSABLE"},
        "component_isolation": {
            "ASSESSED",
            "NOT_RUN",
            "NOT_ASSESSABLE",
        },
    }
    tests_by_class: dict[str, list[dict[str, Any]]] = {
        name: [] for name in required
    }
    tests_by_type = {
        test.get("test_type"): test
        for test in checker.get("tests", [])
        if isinstance(test, dict)
    }
    for test in checker.get("tests", []):
        probe_class = test.get("probe_class")
        if probe_class not in tests_by_class:
            raise ValueError("checker test has an unknown probe class")
        tests_by_class[probe_class].append(test)
    for name in required:
        entry = coverage[name]
        if (
            not isinstance(entry, dict)
            or entry.get("status") not in allowed_statuses[name]
            or not isinstance(entry.get("provenance", {}), dict)
        ):
            raise ValueError(f"invalid {name} probe coverage")
        class_tests = tests_by_class[name]
        if entry["status"] == "ASSESSED" and (
            not class_tests
            or any(
                test.get("observed_status") != "COMPLETED"
                for test in class_tests
            )
        ):
            raise ValueError(f"ASSESSED {name} probe lacks usable tests")
        if entry["status"] in {"NOT_RUN", "NOT_APPLICABLE"} and class_tests:
            raise ValueError(f"{name} probe status contradicts executed tests")
    task_attacks = (
        coverage["negative"].get("subcoverage", {}).get(
            "task_family_attacks"
        )
    )
    if not isinstance(task_attacks, dict) or not task_attacks:
        raise ValueError("invalid task-family attack subcoverage")
    for attack, attack_entry in task_attacks.items():
        provenance = (
            attack_entry.get("provenance", {})
            if isinstance(attack_entry, dict)
            else {}
        )
        if (
            not isinstance(attack_entry, dict)
            or attack_entry.get("status")
            not in {"ASSESSED", "NOT_ASSESSABLE", "NOT_APPLICABLE"}
            or not isinstance(provenance, dict)
            or provenance.get("oracle_used") is not False
        ):
            raise ValueError(
                f"invalid task-family attack coverage: {attack}"
            )
        cases = provenance.get("cases", [])
        if (
            not isinstance(cases, list)
            or attack_entry["status"] == "ASSESSED"
            and (
                not cases
                or any(
                    case not in tests_by_type
                    or tests_by_type[case].get("probe_class") != "negative"
                    or tests_by_type[case].get("observed_status") != "COMPLETED"
                    for case in cases
                )
            )
            or attack_entry["status"] == "NOT_APPLICABLE"
            and cases
        ):
            raise ValueError(
                f"task-family attack evidence mismatch: {attack}"
            )
    for name in ("discrimination", "equivalence"):
        entry = coverage[name]
        provenance = entry.get("provenance", {})
        if entry["status"] == "ASSESSED" and (
            provenance.get("oracle_used") is not False
            or provenance.get("source_kind")
            != "INDEPENDENT_PUBLIC_FIXTURE"
            or not provenance.get("fixture_hashes")
            or not provenance.get("source_role_hashes")
            or not str(
                provenance.get("fixture_manifest_hash", "")
            ).startswith("sha256:")
        ):
            raise ValueError(f"invalid assessed {name} provenance")
        if entry["status"] == "NOT_ASSESSABLE" and (
            provenance.get("oracle_used") is not False
            or provenance.get("source_kind") != "NONE"
            or provenance.get("fixture_hashes", {}) != {}
            or provenance.get("source_role_hashes", {}) != {}
            or provenance.get("fixture_manifest_hash") is not None
        ):
            raise ValueError(f"invalid unavailable {name} provenance")
    component_provenance = coverage["component_isolation"].get(
        "provenance", {}
    )
    if (
        component_provenance.get("oracle_used") is not False
        or any(
            "ORACLE" in value.upper()
            for value in _provenance_strings(component_provenance)
        )
    ):
        raise ValueError("component-isolation provenance is Oracle-bound")
    contract_map = report["contract_map"]
    checker_analysis = contract_map["checker_analysis"]
    checks = {
        item.get("check"): item
        for item in checker_analysis.get("dynamic_checks_required", [])
        if isinstance(item, dict)
    }
    component_check = checks.get("component_isolation")
    if (
        not isinstance(component_check, dict)
        or component_check.get("status")
        != coverage["component_isolation"].get("status")
        or component_check.get("reason")
        != coverage["component_isolation"].get("reason")
        or component_check.get("provenance")
        != coverage["component_isolation"].get("provenance", {})
    ):
        raise ValueError("component-isolation contract/probe mismatch")
    outputs = {
        item.get("file"): item
        for item in checker_analysis.get("outputs", [])
        if isinstance(item, dict)
    }
    for chain in contract_map.get("requirement_chains", []):
        output = outputs.get(chain.get("core_output"))
        if output is not None and chain.get("checker_read") != output.get(
            "checker_reads"
        ):
            raise ValueError("requirement-chain checker-read mismatch")


def validate_qa_axes(qa_axes: Any) -> None:
    if not isinstance(qa_axes, dict) or set(qa_axes) != set(QA_AXIS_NAMES):
        raise ValueError("QA axes must contain exactly the four first-class axes")
    for name in QA_AXIS_NAMES:
        axis = qa_axes[name]
        if not isinstance(axis, dict) or set(axis) != {
            "status",
            "evidence",
            "locations",
            "limitations",
        }:
            raise ValueError(f"invalid QA axis schema: {name}")
        if axis["status"] not in QA_AXIS_STATUSES:
            raise ValueError(f"invalid QA axis status: {name}")
        if not isinstance(axis["evidence"], list):
            raise ValueError(f"QA axis evidence must be a list: {name}")
        if not isinstance(axis["locations"], list):
            raise ValueError(f"QA axis locations must be a list: {name}")
        if not isinstance(axis["limitations"], list) or not all(
            isinstance(item, str) and item.strip()
            for item in axis["limitations"]
        ):
            raise ValueError(f"QA axis limitations must be strings: {name}")
        evidence_semantics: list[str] = []
        for evidence in axis["evidence"]:
            finding_evidence = (
                isinstance(evidence, dict)
                and set(evidence)
                == {"finding_id", "observed_fact", "semantic"}
                and isinstance(evidence["finding_id"], str)
                and bool(evidence["finding_id"].strip())
                and isinstance(evidence["observed_fact"], str)
                and bool(evidence["observed_fact"].strip())
                and evidence["semantic"] == "supports_failure"
            )
            source_evidence = (
                isinstance(evidence, dict)
                and set(evidence) == {"source", "fact", "semantic"}
                and isinstance(evidence["source"], str)
                and bool(evidence["source"].strip())
                and isinstance(evidence["fact"], str)
                and bool(evidence["fact"].strip())
                and evidence["semantic"]
                in set(QA_EVIDENCE_SEMANTICS.values())
            )
            if not (finding_evidence or source_evidence):
                raise ValueError(f"invalid QA axis evidence item: {name}")
            evidence_semantics.append(evidence["semantic"])
        expected_semantic = QA_EVIDENCE_SEMANTICS[axis["status"]]
        if any(
            semantic != expected_semantic
            for semantic in evidence_semantics
        ):
            conflict = (
                "failure evidence"
                if "supports_failure" in evidence_semantics
                else "contradictory evidence status"
            )
            raise ValueError(
                f"{axis['status']} QA axis cannot use {conflict}: {name}"
            )
        for location in axis["locations"]:
            if (
                not isinstance(location, dict)
                or set(location) != {"file", "line", "quote"}
                or not isinstance(location["file"], str)
                or not location["file"]
                or (
                    location["line"] is not None
                    and (
                        not isinstance(location["line"], int)
                        or isinstance(location["line"], bool)
                        or location["line"] < 1
                    )
                )
                or (
                    location["quote"] is not None
                    and not isinstance(location["quote"], str)
                )
            ):
                raise ValueError(f"invalid QA axis location: {name}")
        if axis["status"] in {"FAIL", "WARNING"} and (
            not axis["evidence"] or not axis["locations"]
        ):
            raise ValueError(
                f"{axis['status']} QA axis requires evidence and locations: {name}"
            )
        if axis["status"] == "PASS" and (
            not axis["evidence"] or not axis["locations"]
        ):
            raise ValueError(
                f"PASS QA axis requires evidence and locations: {name}"
            )
        if axis["status"] == "NOT_ASSESSABLE":
            if not axis["limitations"]:
                raise ValueError(
                    f"NOT_ASSESSABLE QA axis requires limitations: {name}"
                )


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
    manifest = read_json(temp_dir / "audit_manifest.json")
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
    if manifest.get(
        "review_implementation"
    ) != collect_review_implementation_hashes():
        raise ValueError("audit Review implementation hashes are stale")
    source_bindings = report.get("source_bindings")
    if not isinstance(source_bindings, dict):
        raise ValueError("audit lacks source evidence bindings")
    if (
        source_bindings.get("fixture_hashes")
        != manifest.get("fixture_hashes", {})
        or source_bindings.get("assessment_hashes")
        != manifest.get("assessment_hashes", {})
        or source_bindings.get("core_contract_digest")
        != manifest.get("core_contract_digest")
    ):
        raise ValueError("audit source bindings differ from its manifest")
    binding = report.get("audit_binding")
    if (
        not isinstance(binding, dict)
        or binding.get("parent_audit_id")
        != manifest.get("parent_audit_id")
        or binding.get("source_hashes")
        != manifest.get("input_hashes", {})
        or binding.get("implementation_hash")
        != manifest.get("review_implementation", {}).get("aggregate_hash")
        or binding.get("deterministic_contract_digest")
        != manifest.get("deterministic_contract_digest")
    ):
        raise ValueError("audit binding differs from its manifest")
    last_position = -1
    for heading in REQUIRED_HEADINGS:
        position = markdown.find(heading)
        if position <= last_position:
            raise ValueError(f"missing or out-of-order heading: {heading}")
        last_position = position
    summary = report["summary"]
    deterministic_contract = validate_deterministic_contract(
        report.get("deterministic_contract")
    )
    if report.get("deterministic_repair") != deterministic_repair_summary(
        deterministic_contract
    ):
        raise ValueError("deterministic repair summary differs from contract")
    if (
        summary.get("deterministic_status")
        != deterministic_contract["repair_summary"]["state"]
        or summary.get("deterministic_repair_required")
        is not (
            summary.get("repair_state")
            == "DETERMINISTIC_REPAIR_REQUIRED"
        )
    ):
        raise ValueError("summary deterministic status is inconsistent")
    if (
        manifest.get("deterministic_contract_schema_version")
        != deterministic_contract["schema_version"]
        or manifest.get("deterministic_contract_digest")
        != deterministic_contract["contract_digest"]
    ):
        raise ValueError("manifest deterministic binding is stale")
    for artifact_name, artifact in (
        ("disposition", disposition),
        ("corpus index", index_entry),
    ):
        if (
            artifact.get("deterministic_contract") != deterministic_contract
            or artifact.get("deterministic_repair")
            != deterministic_repair_summary(deterministic_contract)
        ):
            raise ValueError(
                f"{artifact_name} deterministic contract differs from report"
            )
    try:
        canonical = canonical_fields(
            summary["final_verdict"],
            publishability=ROUTES[summary["final_verdict"]],
            repair_decision=summary.get("repair_decision", "NOT_REQUIRED"),
            repair_status=summary.get("repair_status", "NOT_APPLICABLE"),
        )
    except ValueError as exc:
        raise ValueError(
            "report verdict is inconsistent with canonical routing"
        ) from exc
    if any(report.get(key) != value for key, value in canonical.items()):
        raise ValueError("audit canonical fields are missing or inconsistent")
    if any(summary.get(key) != value for key, value in canonical.items()):
        raise ValueError("summary canonical fields are missing or inconsistent")
    if any(disposition.get(key) != value for key, value in canonical.items()):
        raise ValueError("disposition canonical fields are missing or inconsistent")
    if any(index_entry.get(key) != value for key, value in canonical.items()):
        raise ValueError("index canonical fields are missing or inconsistent")
    if any(manifest.get(key) != value for key, value in canonical.items()):
        raise ValueError("manifest canonical fields are missing or inconsistent")
    validate_qa_axes(report.get("qa_axes"))
    configuration = report.get("configuration", {})
    if configuration.get("execution_level") != "E1":
        raise ValueError("authoritative report execution level must be E1")
    execution = report.get("execution_evidence", {})
    if (
        not isinstance(execution, dict)
        or execution.get("claim") != "E1_CHECKER_ONLY"
        or execution.get("scientific_reproduction") is not False
        or execution.get("runtime_provenance")
        not in {"sandbox"}
    ):
        raise ValueError("invalid E1 runtime provenance")
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
    contract_map = report.get("contract_map")
    if (
        not isinstance(contract_map, dict)
        or not isinstance(contract_map.get("requirements"), list)
        or not isinstance(contract_map.get("requirement_chains"), list)
        or not isinstance(contract_map.get("instruction_outputs"), list)
        or not isinstance(contract_map.get("process_evidence"), list)
        or not isinstance(contract_map.get("scored_outputs"), list)
        or not isinstance(contract_map.get("load_bearing_outputs"), list)
        or not isinstance(contract_map.get("core_outputs"), list)
        or not isinstance(contract_map.get("role_conflicts"), list)
        or not isinstance(contract_map.get("checker_analysis"), dict)
    ):
        raise ValueError("invalid instruction-to-checker contract map")
    validate_requirement_chains(contract_map, markdown)
    validate_contract_probe_consistency(report, checker)
    runtime_provenance = checker.get("runtime_provenance")
    if (
        not isinstance(runtime_provenance, dict)
        or runtime_provenance.get("status")
        not in {"ASSESSED", "NOT_ASSESSABLE"}
        or runtime_provenance.get("entrypoint") != "tests/test.sh"
        or runtime_provenance.get("runtime_provenance") != "sandbox"
    ):
        raise ValueError("invalid Harbor verifier runtime provenance")
    if runtime_provenance["status"] == "ASSESSED" and (
        runtime_provenance.get("cases_executed") != len(checker.get("tests", []))
    ):
        raise ValueError("Harbor verifier runtime case count is inconsistent")
    if runtime_provenance["status"] == "NOT_ASSESSABLE" and (
        checker.get("tests")
        or not runtime_provenance.get("reason")
        or runtime_provenance.get("runtime_provenance") != "sandbox"
    ):
        raise ValueError("unavailable Harbor verifier runtime is not truthful")
    gold = report.get("gold_provenance")
    if (
        not isinstance(gold, dict)
        or gold.get("status")
        not in {
            "ASSESSED",
            "NOT_ASSESSABLE",
            "PASS",
            "WARNING",
            "FAIL",
        }
        or gold.get("mode") not in {"no_paper", "paper_grounded"}
        or gold.get("oracle_used") is not False
        or not isinstance(gold.get("provenance", {}), dict)
    ):
        raise ValueError("invalid Gold provenance")
    if summary.get("scoring_version") != V11_SCORING_VERSION:
        raise ValueError("invalid scoring version")
    if summary.get("legacy_scoring_version") != SCORING_VERSION:
        raise ValueError("invalid legacy scoring version")
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
    legacy_gaps = [
        item["dimension"]
        for item in dimensions
        if item["points_earned"] is None
    ]
    expected_legacy_total = (
        None
        if legacy_gaps
        else round(sum(item["points_earned"] for item in dimensions), 2)
    )
    if expected_legacy_total is not None and float(
        expected_legacy_total
    ).is_integer():
        expected_legacy_total = int(expected_legacy_total)
    if summary.get("legacy_total_score") != expected_legacy_total:
        raise ValueError("legacy total score does not equal dimension points")
    dimensions_v11 = report.get("dimensions_v11")
    if not isinstance(dimensions_v11, list) or [
        item.get("dimension") for item in dimensions_v11
    ] != list(V11_DIMENSIONS):
        raise ValueError("v11 dimension order or membership is invalid")
    for item in dimensions_v11:
        name = item["dimension"]
        maximum = V11_DIMENSION_WEIGHTS[name]
        if item.get("max_points") != maximum or item.get("weight") != maximum:
            raise ValueError(f"invalid v11 weight for {name}")
        earned = item.get("points_earned")
        normalized = item.get("normalized")
        if earned is None:
            if (
                normalized is not None
                or item.get("status") != "NOT_ASSESSABLE"
                or name not in V11_KEY_DIMENSIONS
            ):
                raise ValueError(f"inconsistent unavailable v11 score for {name}")
        elif (
            not isinstance(earned, (int, float))
            or isinstance(earned, bool)
            or not 0 <= earned <= maximum
            or normalized != round(float(earned) / maximum * 100, 4)
        ):
            raise ValueError(f"invalid earned or normalized v11 score for {name}")
    expected_total, expected_gaps = v11_weighted_total(dimensions_v11)
    if summary.get("total_score") != expected_total:
        raise ValueError("total score does not equal v11 weighted total")
    if expected_total is not None and not 0 <= expected_total <= 100:
        raise ValueError("total score is outside 0–100")
    (
        expected_verdict,
        recomputed_total,
        expected_gate_triggered,
        expected_reason,
        recomputed_gaps,
    ) = scoring_verdict_v11(findings, dimensions_v11, hard_gates)
    expected_verdict, deterministic_reason = apply_deterministic_gate(
        verdict=expected_verdict,
        score=recomputed_total,
        hard_gate=expected_gate_triggered,
        evidence_gaps=recomputed_gaps,
        contract=deterministic_contract,
    )
    if deterministic_reason is not None:
        expected_reason = deterministic_reason
    if (
        summary.get("final_verdict") != expected_verdict
        or summary.get("total_score") != recomputed_total
        or summary.get("hard_gate_triggered") != expected_gate_triggered
        or summary.get("core_reason") != expected_reason
    ):
        raise ValueError("report verdict is inconsistent with authoritative scoring")
    if summary["materials_class"] not in MATERIALS_CLASSES:
        raise ValueError("invalid materials class")
    if summary["answer_type"] not in ANSWER_TYPES:
        raise ValueError("invalid answer type")
    expected_route = ROUTES[summary["final_verdict"]]
    if summary.get("disposition") != summary["final_verdict"]:
        raise ValueError("summary disposition does not match verdict")
    if summary.get("publishable") is not (
        summary["final_verdict"] == "PASS"
    ):
        raise ValueError("summary publishable flag does not match verdict")
    if summary.get("publication_route") != expected_route:
        raise ValueError("summary publication route does not match verdict")
    expected_audit_route = (
        "PAPER_GROUNDED_E1"
        if (
            report["configuration"]["paper_mode"] == "no_paper"
            and not expected_gate_triggered
        )
        else expected_route
    )
    if summary.get("route") != expected_audit_route:
        raise ValueError("summary route does not match audit sequence")
    if disposition.get("route") != expected_route:
        raise ValueError("disposition artifact does not match verdict")
    if index_entry.get("route") != expected_route:
        raise ValueError("corpus index route does not match verdict")
    for name, artifact in (
        ("disposition", disposition),
        ("corpus index", index_entry),
    ):
        if artifact.get("scoring_version") != V11_SCORING_VERSION:
            raise ValueError(f"{name} scoring version differs from report")
        if artifact.get("total_score") != summary["total_score"]:
            raise ValueError(f"{name} total differs from report")
        if artifact.get("dimension_scores") != dimensions:
            raise ValueError(f"{name} dimensions differ from report")
        if artifact.get("hard_gates") != hard_gates:
            raise ValueError(f"{name} Hard Gates differ from report")
        if artifact.get("evidence_gaps") != recomputed_gaps:
            raise ValueError(f"{name} evidence gaps differ from scoring")
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
        validate_pass_probe_coverage(checker.get("probe_coverage", {}))
    oracle = checker.get("solution_oracle", {})
    if oracle.get("scientific_evidence") is not False:
        raise ValueError("solution Oracle was treated as scientific evidence")
    if checker.get("solution_content_inspected") is not False:
        raise ValueError("solution content escaped the isolated Oracle boundary")
    if report["scope"].get("solution_content_inspected") is not False:
        raise ValueError("report claims solution content inspection")
    if bool(report["scope"].get("solution_oracle_executed")) != bool(
        oracle.get("executed")
    ):
        raise ValueError("report solution Oracle execution status is inconsistent")
    if (
        oracle.get("executed") is True
        and (
            oracle.get("producer_started") is not True
            or oracle.get("setup_prepared") is not True
            or oracle.get("attempted") is not True
        )
    ):
        raise ValueError("solution Oracle execution stages are inconsistent")
    expected_ids = [
        f"FINDING-{index:03d}"
        for index in range(1, len(findings) + 1)
    ]
    if [item.get("finding_id") for item in findings] != expected_ids:
        raise ValueError("finding IDs are not consecutive")
    if report.get("findings") != findings:
        raise ValueError("findings JSONL content differs from report")
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
    manifest["bundle_hash"] = canonical_json_hash(manifest["output_hashes"])
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
