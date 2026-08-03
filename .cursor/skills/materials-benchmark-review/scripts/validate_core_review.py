#!/usr/bin/env python3
"""Validate baseline-first materials benchmark Review records (v3.3)."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

SCHEMA = "materials-core-review/3.3"
STATUSES = {"PASS", "FAIL", "BLOCKED"}
VERDICTS = {"PASS", "REPAIR_REQUIRED", "REAUTHOR_REQUIRED", "REJECTED", "BLOCKED"}
QUALITY_TIERS = {"BASELINE_CORRECT", "RESULT_ENHANCED"}
OPERATIONAL_STATUSES = {"PASS", "FAIL", "BLOCKED", "NOT_ASSESSED"}
QUESTION_GATES = {
    "Q0_COMPUTATIONAL_SCIENCE_ADMISSION", "Q1_PAPER_ALIGNMENT",
    "Q2_TARGET_DEFINITION", "Q3_INSTRUCTION_COMPLETE", "Q4_OUTPUT_CONTRACT",
    "Q5_DERIVED_CONSISTENCY", "Q6_RESOURCE_SUFFICIENCY",
}
ANSWER_GATES = {
    "A1_PUBLIC_TO_HIDDEN_MAPPING", "A2_GOLD_PROVENANCE",
    "A3_REFERENCE_APPLICABILITY", "A4_CHECKER_COVERAGE",
    "A5_CHECKER_ROBUSTNESS", "A6_REWARD_BEHAVIOR",
}
ADMISSION_FAILURE_MODES = {
    "PURE_INFORMATION_EXTRACTION", "PURE_ALGEBRAIC_COMPUTATION",
    "EXPERIMENTAL_OPERATION_REQUIRED", "TRIVIAL_EXPERIMENTAL_DATA_REDUCTION",
}
REJECTION_FAILURE_MODES = ADMISSION_FAILURE_MODES | {
    "INDISPENSABLE_DATASET_UNAVAILABLE", "INDISPENSABLE_CODE_UNAVAILABLE",
    "INDISPENSABLE_MODEL_UNAVAILABLE", "INDISPENSABLE_POTENTIAL_UNAVAILABLE",
    "INDISPENSABLE_STRUCTURE_UNAVAILABLE",
}
PARAMETER_CLASSES = {"PAPER_FIXED", "SOLVER_SEARCHABLE", "TARGET_DEFINING", "INDISPENSABLE_ASSET"}
SELECTION_POLICIES = {"PAPER_VALUE", "MESH_SEARCH", "CONVERGENCE", "OPTIMIZATION", "SOLVER_JUSTIFIED", "RESOURCE"}
ITEM_KINDS = {"FORMULA", "WORKFLOW_STEP", "INFORMATION"}
ITEM_ROLES = {"REQUIRED_SCIENTIFIC_DEFINITION", "REQUIRED_WORKFLOW_DEPENDENCY", "OPTIONAL_GUIDANCE", "SOLUTION_RECIPE"}
ITEM_ACTIONS = {"KEEP", "ADD_FROM_PAPER", "REMOVE_REDUNDANCY", "REWRITE_BOUNDARY"}
RESOURCE_KINDS = {"DATASET", "CODE", "MODEL", "POTENTIAL", "STRUCTURE", "SOFTWARE"}
RESOURCE_DELIVERY = {"BUNDLED", "PUBLIC_URL", "RUNTIME_PROVIDED", "GENERIC_EQUIVALENT", "NONE"}
RESOURCE_AVAILABILITY = {"READY", "UNAVAILABLE", "BLOCKED"}
GOLD_POLICIES = {"PAPER_DIRECT", "UNIQUE_DERIVATION", "PAPER_SUPPORTED_RELATION"}
COMPARISON_KINDS = {"NUMERIC", "RELATION"}
TOLERANCE_BASES = {"reported_uncertainty", "reported_precision", "digitization", "independent_recompute", "convergence", "cross_implementation", "reviewer_reasoned"}
RESULT_CHECK_ACTIONS = {"GOLD_ONLY_SUFFICIENT", "KEEP_RESULT_CHECK", "ADD_MINIMAL_RESULT_CHECK", "NO_AFFORDABLE_RESULT_CHECK"}
BASELINE_PROBES = {"valid_positive", "tolerance_boundary", "missing_or_malformed", "non_finite_and_duplicate", "wrong_science"}
ENHANCEMENT_PROBES = {"minimal_fabrication", "quality_gradient", "cross_condition_group_mismatch"}
PROBE_CLASSES = BASELINE_PROBES | ENHANCEMENT_PROBES
ROUTES = {"REPAIR", "REAUTHOR", "REJECT", "BLOCKED", "REPAIR_CHECKER_COST", "ENHANCE_OPTIONAL"}


def text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be non-empty text")
    return value.strip()


def finite(value: Any, label: str, *, minimum: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label} must be finite")
    result = float(value)
    if minimum is not None and result < minimum:
        raise ValueError(f"{label} must be >= {minimum}")
    return result


def evidence(value: Any, label: str) -> None:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} requires evidence")
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise ValueError(f"{label}[{index}] must be an object")
        for key in ("path", "locator", "result"):
            text(item.get(key), f"{label}[{index}].{key}")
        normalized = item["path"].replace("\\", "/").lstrip("./")
        if normalized == "solution" or normalized.startswith("solution/"):
            raise ValueError(f"{label} must not reference solution/")


def aggregate(gates: list[dict[str, Any]]) -> str:
    statuses = {item["status"] for item in gates}
    return "FAIL" if "FAIL" in statuses else "BLOCKED" if "BLOCKED" in statuses else "PASS"


def gate_block(value: Any, expected: set[str], label: str) -> list[dict[str, Any]]:
    if not isinstance(value, dict) or value.get("status") not in STATUSES:
        raise ValueError(f"{label}.status is invalid")
    gates = value.get("gates")
    if not isinstance(gates, list) or len(gates) != len(expected):
        raise ValueError(f"{label}.gates must contain every canonical gate")
    seen: set[str] = set()
    for index, item in enumerate(gates):
        if not isinstance(item, dict) or item.get("code") not in expected or item.get("status") not in STATUSES:
            raise ValueError(f"{label}.gates[{index}] is invalid")
        if item["code"] in seen:
            raise ValueError(f"{label}.gates contains duplicate codes")
        seen.add(item["code"])
        text(item.get("rationale"), f"{label}.gates[{index}].rationale")
        evidence(item.get("evidence"), f"{label}.gates[{index}].evidence")
    if seen != expected or value["status"] != aggregate(gates):
        raise ValueError(f"{label} gate aggregate is inconsistent")
    return gates


def gate_status(gates: list[dict[str, Any]], code: str) -> str:
    return next(item["status"] for item in gates if item["code"] == code)


def validate_cost(value: Any) -> tuple[str, bool]:
    if not isinstance(value, dict):
        raise ValueError("checker_cost_record must be an object")
    if value.get("hardware_class") not in {"CPU", "SINGLE_GPU"}:
        raise ValueError("checker_cost_record.hardware_class is invalid")
    cpu = finite(value.get("cpu_cores"), "checker_cost_record.cpu_cores", minimum=0)
    gpu = finite(value.get("gpu_count"), "checker_cost_record.gpu_count", minimum=0)
    wall = finite(value.get("measured_wall_seconds"), "checker_cost_record.measured_wall_seconds", minimum=0)
    finite(value.get("peak_memory_mb"), "checker_cost_record.peak_memory_mb", minimum=0)
    finite(value.get("input_bytes_read"), "checker_cost_record.input_bytes_read", minimum=0)
    for field in ("uses_full_trajectory", "performs_new_simulation", "real_scale_input"):
        if not isinstance(value.get(field), bool):
            raise ValueError(f"checker_cost_record.{field} must be boolean")
    text(value.get("cost_rationale"), "checker_cost_record.cost_rationale")
    gpu_type = value.get("gpu_type")
    if value["hardware_class"] == "CPU":
        if gpu != 0 or gpu_type is not None:
            raise ValueError("CPU cost record must use gpu_count=0 and gpu_type=null")
    else:
        if gpu != 1:
            raise ValueError("SINGLE_GPU publication budget permits exactly one GPU")
        text(gpu_type, "checker_cost_record.gpu_type")
    within = cpu <= 32 and gpu <= 1 and wall <= 600 and not value["uses_full_trajectory"] and not value["performs_new_simulation"] and value["real_scale_input"]
    expected = "PASS" if within else "FAIL"
    if value.get("status") != expected:
        raise ValueError(f"checker_cost_record.status is inconsistent; expected {expected}")
    return expected, within


def validate(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("schema_version") != SCHEMA:
        raise ValueError(f"schema_version must be {SCHEMA}")
    text(value.get("package_id"), "package_id")
    text(value.get("source_package"), "source_package")
    scope = value.get("reviewed_scope")
    if not isinstance(scope, list) or not scope:
        raise ValueError("reviewed_scope must be non-empty")
    for item in scope:
        normalized = text(item, "reviewed_scope item").replace("\\", "/").lstrip("./")
        if normalized == "solution" or normalized.startswith("solution/"):
            raise ValueError("reviewed_scope must not include solution/")

    contract = value.get("instruction_contract")
    if not isinstance(contract, dict) or contract.get("solver_visible_file") != "instruction.md" or contract.get("output_root") != "/app/outputs":
        raise ValueError("instruction_contract must use instruction.md and /app/outputs")
    for field in ("derived_files_consistent", "assets_use_generic_roles", "paper_reading_language_absent"):
        if not isinstance(contract.get(field), bool):
            raise ValueError(f"instruction_contract.{field} must be boolean")
    headings = contract.get("required_headings")
    if not isinstance(headings, list) or len(headings) < 9:
        raise ValueError("required_headings must record the stable instruction skeleton")
    outputs = contract.get("public_outputs")
    if not isinstance(outputs, list) or not outputs:
        raise ValueError("instruction_contract.public_outputs must be non-empty")
    output_paths: set[str] = set()
    for index, item in enumerate(outputs):
        if not isinstance(item, dict):
            raise ValueError(f"public_outputs[{index}] is invalid")
        path = text(item.get("path"), f"public_outputs[{index}].path")
        if not path.startswith("/app/outputs/"):
            raise ValueError("public output paths must be under /app/outputs")
        output_paths.add(path)
        text(item.get("format"), f"public_outputs[{index}].format")
        if item.get("purpose") not in {"scored", "checked_result", "unscored"} or not isinstance(item.get("contract_complete"), bool):
            raise ValueError(f"public_outputs[{index}] purpose/contract is invalid")
    groups = contract.get("required_condition_groups")
    if not isinstance(groups, list) or not groups:
        raise ValueError("required_condition_groups must be non-empty")
    group_map: dict[str, dict[str, Any]] = {}
    identifiers: set[str] = set()
    for index, item in enumerate(groups):
        if not isinstance(item, dict):
            raise ValueError(f"required_condition_groups[{index}] is invalid")
        gid = text(item.get("condition_group_id"), f"required_condition_groups[{index}].condition_group_id")
        signature = text(item.get("condition_signature"), f"required_condition_groups[{index}].condition_signature")
        identifier = text(item.get("public_identifier"), f"required_condition_groups[{index}].public_identifier")
        if gid in group_map or identifier in identifiers:
            raise ValueError("condition group IDs and public identifiers must be unique")
        if not any(identifier == path or identifier.startswith(path + ":") or identifier.startswith(path + "#") for path in output_paths):
            raise ValueError("condition group public identifier must bind a public output")
        identifiers.add(identifier)
        group_map[gid] = {"condition_signature": signature, "public_identifier": identifier}

    admission = value.get("scientific_task_admission")
    if not isinstance(admission, dict) or admission.get("status") not in STATUSES:
        raise ValueError("scientific_task_admission is invalid")
    modes = admission.get("failure_modes")
    if not isinstance(modes, list) or any(mode not in ADMISSION_FAILURE_MODES for mode in modes) or len(modes) != len(set(modes)):
        raise ValueError("scientific_task_admission.failure_modes is invalid")
    if not isinstance(admission.get("computer_reproducible"), bool) or not isinstance(admission.get("requires_physical_experiment"), bool):
        raise ValueError("scientific_task_admission booleans are required")
    text(admission.get("rationale"), "scientific_task_admission.rationale")
    evidence(admission.get("evidence"), "scientific_task_admission.evidence")
    if admission["status"] == "PASS" and (modes or not admission["computer_reproducible"] or admission["requires_physical_experiment"]):
        raise ValueError("admission PASS is inconsistent")
    if admission["status"] == "FAIL" and not modes:
        raise ValueError("admission FAIL requires a canonical failure mode")

    analysis = value.get("instruction_analysis")
    if not isinstance(analysis, dict):
        raise ValueError("instruction_analysis must be an object")
    coverage = analysis.get("paper_parameter_coverage")
    if not isinstance(coverage, dict) or coverage.get("status") not in STATUSES:
        raise ValueError("paper_parameter_coverage is invalid")
    evidence(coverage.get("evidence"), "paper_parameter_coverage.evidence")
    parameters = analysis.get("parameter_records")
    if not isinstance(parameters, list):
        raise ValueError("parameter_records must be a list")
    for index, item in enumerate(parameters):
        if not isinstance(item, dict) or item.get("parameter_class") not in PARAMETER_CLASSES or item.get("selection_policy") not in SELECTION_POLICIES:
            raise ValueError(f"parameter_records[{index}] is invalid")
        for field in ("canonical_id", "symbol", "meaning", "value_or_range", "unit", "scope", "source_locator", "introduced_at"):
            text(item.get(field), f"parameter_records[{index}].{field}")
        for field in ("paper_reports_unique_value", "instruction_requires_unique_value", "checker_requires_unique_value"):
            if not isinstance(item.get(field), bool):
                raise ValueError(f"parameter_records[{index}].{field} must be boolean")
        used = item.get("used_at")
        if not isinstance(used, list) or not used:
            raise ValueError(f"parameter_records[{index}].used_at must be non-empty")
        if item["parameter_class"] == "PAPER_FIXED" and item["selection_policy"] != "PAPER_VALUE":
            raise ValueError("PAPER_FIXED parameters require PAPER_VALUE")
        if item["parameter_class"] == "INDISPENSABLE_ASSET" and item["selection_policy"] != "RESOURCE":
            raise ValueError("INDISPENSABLE_ASSET requires RESOURCE")
        if item["parameter_class"] == "SOLVER_SEARCHABLE":
            if item["paper_reports_unique_value"]:
                raise ValueError("SOLVER_SEARCHABLE cannot claim a unique paper value")
            if item["selection_policy"] not in {"MESH_SEARCH", "CONVERGENCE", "OPTIMIZATION", "SOLVER_JUSTIFIED"}:
                raise ValueError("SOLVER_SEARCHABLE requires a search/justification policy")
            if item["checker_requires_unique_value"]:
                raise ValueError("checker must not secretly fix a SOLVER_SEARCHABLE parameter")
    conflicts = analysis.get("parameter_conflicts")
    if not isinstance(conflicts, list):
        raise ValueError("parameter_conflicts must be a list")
    for index, item in enumerate(conflicts):
        if not isinstance(item, dict) or item.get("status") not in {"OPEN", "RESOLVED"}:
            raise ValueError(f"parameter_conflicts[{index}] is invalid")
        for field in ("conflict_id", "canonical_id", "rationale"):
            text(item.get(field), f"parameter_conflicts[{index}].{field}")
        for field in ("locators", "affected_targets"):
            if not isinstance(item.get(field), list) or not item[field]:
                raise ValueError(f"parameter_conflicts[{index}].{field} must be non-empty")
    formula_steps = analysis.get("formula_step_records")
    if not isinstance(formula_steps, list) or not formula_steps:
        raise ValueError("formula_step_records must be non-empty")
    for index, item in enumerate(formula_steps):
        if not isinstance(item, dict) or item.get("kind") not in ITEM_KINDS or item.get("role") not in ITEM_ROLES or item.get("action") not in ITEM_ACTIONS:
            raise ValueError(f"formula_step_records[{index}] is invalid")
        for field in ("locator", "dependency_effect", "rationale"):
            text(item.get(field), f"formula_step_records[{index}].{field}")
        if not isinstance(item.get("paper_supported"), bool):
            raise ValueError(f"formula_step_records[{index}].paper_supported must be boolean")
        evidence(item.get("evidence"), f"formula_step_records[{index}].evidence")
    continuity = analysis.get("workflow_continuity")
    if not isinstance(continuity, dict) or continuity.get("status") not in STATUSES:
        raise ValueError("workflow_continuity is invalid")
    evidence(continuity.get("evidence"), "workflow_continuity.evidence")

    resources = value.get("resource_records")
    if not isinstance(resources, list):
        raise ValueError("resource_records must be a list")
    for index, item in enumerate(resources):
        if not isinstance(item, dict) or item.get("kind") not in RESOURCE_KINDS or item.get("delivery") not in RESOURCE_DELIVERY or item.get("availability") not in RESOURCE_AVAILABILITY:
            raise ValueError(f"resource_records[{index}] is invalid")
        text(item.get("resource_id"), f"resource_records[{index}].resource_id")
        if not isinstance(item.get("indispensable"), bool) or not isinstance(item.get("equivalent_allowed"), bool):
            raise ValueError(f"resource_records[{index}] booleans are required")
        if item["delivery"] == "NONE" and item.get("locator") is not None:
            raise ValueError("NONE resource delivery requires null locator")
        if item["delivery"] != "NONE":
            text(item.get("locator"), f"resource_records[{index}].locator")
        evidence(item.get("evidence"), f"resource_records[{index}].evidence")

    q_gates = gate_block(value.get("question_correctness"), QUESTION_GATES, "question_correctness")
    if gate_status(q_gates, "Q0_COMPUTATIONAL_SCIENCE_ADMISSION") != admission["status"]:
        raise ValueError("Q0 must match scientific_task_admission")
    derived_q3 = "BLOCKED" if "BLOCKED" in {coverage["status"], continuity["status"]} else "FAIL" if coverage["status"] == "FAIL" or continuity["status"] == "FAIL" or any(item["status"] == "OPEN" for item in conflicts) or any(item["role"] == "SOLUTION_RECIPE" for item in formula_steps) else "PASS"
    if gate_status(q_gates, "Q3_INSTRUCTION_COMPLETE") != derived_q3:
        raise ValueError("Q3 must match instruction_analysis")
    unavailable = [item for item in resources if item["indispensable"] and item["availability"] == "UNAVAILABLE"]
    blocked_resources = [item for item in resources if item["indispensable"] and item["availability"] == "BLOCKED"]
    derived_q6 = "FAIL" if unavailable else "BLOCKED" if blocked_resources else "PASS"
    if gate_status(q_gates, "Q6_RESOURCE_SUFFICIENCY") != derived_q6:
        raise ValueError("Q6 must match indispensable resource records")

    answer = value.get("answer_correctness")
    if not isinstance(answer, dict):
        raise ValueError("answer_correctness must be an object")
    answer_not_assessed = answer.get("status") == "NOT_ASSESSED"
    a_gates: list[dict[str, Any]] = []
    if answer_not_assessed:
        for field in ("gates", "condition_group_records", "gold_records", "tolerance_records", "result_check_assessment"):
            if answer.get(field) not in ([], None):
                raise ValueError("NOT_ASSESSED answer fields must be empty")
    else:
        a_gates = gate_block(answer, ANSWER_GATES, "answer_correctness")
        condition_groups = answer.get("condition_group_records")
        if not isinstance(condition_groups, list) or not condition_groups:
            raise ValueError("condition_group_records must be non-empty")
        declared: dict[str, set[str]] = {}
        for index, item in enumerate(condition_groups):
            if not isinstance(item, dict) or item.get("coverage_status") not in STATUSES:
                raise ValueError(f"condition_group_records[{index}] is invalid")
            gid = text(item.get("condition_group_id"), f"condition_group_records[{index}].condition_group_id")
            if gid not in group_map or gid in declared:
                raise ValueError("condition_group_records must cover every public required condition group exactly")
            if text(item.get("condition_signature"), "condition_signature") != group_map[gid]["condition_signature"] or text(item.get("public_identifier"), "public_identifier") != group_map[gid]["public_identifier"]:
                raise ValueError("condition group signature/public identifier mismatch")
            targets = item.get("required_target_ids")
            if not isinstance(targets, list) or not targets or len(targets) != len(set(targets)):
                raise ValueError("condition group target IDs must be non-empty and unique")
            declared[gid] = set(targets)
            evidence(item.get("provenance"), f"condition_group_records[{index}].provenance")
        if set(declared) != set(group_map):
            raise ValueError("condition_group_records must cover every public required condition group exactly")
        gold = answer.get("gold_records")
        if not isinstance(gold, list) or not gold:
            raise ValueError("gold_records must be non-empty")
        actual = {gid: set() for gid in declared}
        numeric: set[str] = set()
        target_ids: set[str] = set()
        for index, item in enumerate(gold):
            if not isinstance(item, dict) or item.get("policy") not in GOLD_POLICIES or item.get("comparison_kind") not in COMPARISON_KINDS or item.get("role") not in {"CORE", "SUPPORTING", "REPORT_ONLY"}:
                raise ValueError(f"gold_records[{index}] is invalid")
            target = text(item.get("target_id"), f"gold_records[{index}].target_id")
            if target in target_ids:
                raise ValueError("gold target IDs must be unique")
            target_ids.add(target)
            memberships = item.get("condition_group_ids")
            if not isinstance(memberships, list) or not memberships or any(gid not in declared for gid in memberships):
                raise ValueError(f"gold_records[{index}].condition_group_ids is invalid")
            if item["policy"] == "PAPER_DIRECT" and (item["comparison_kind"] != "NUMERIC" or len(memberships) != 1):
                raise ValueError("numeric PAPER_DIRECT Gold must bind exactly one condition group")
            if item["policy"] == "PAPER_SUPPORTED_RELATION" and item["comparison_kind"] != "RELATION":
                raise ValueError("PAPER_SUPPORTED_RELATION must use RELATION")
            for field in ("value_or_relation", "applicability", "units", "independent_check"):
                text(item.get(field), f"gold_records[{index}].{field}")
            evidence(item.get("provenance"), f"gold_records[{index}].provenance")
            for gid in memberships:
                actual[gid].add(target)
            if item["comparison_kind"] == "NUMERIC":
                numeric.add(target)
        if actual != declared:
            raise ValueError("condition group target coverage must match Gold memberships")
        tolerances = answer.get("tolerance_records")
        if not isinstance(tolerances, list):
            raise ValueError("tolerance_records must be a list")
        tolerance_targets: set[str] = set()
        for index, item in enumerate(tolerances):
            if not isinstance(item, dict) or item.get("status") not in {"EVIDENCED", "BLOCKED"} or item.get("metric") not in {"absolute_error", "relative_error", "normalized_residual"}:
                raise ValueError(f"tolerance_records[{index}] is invalid")
            target = text(item.get("target_id"), f"tolerance_records[{index}].target_id")
            tolerance_targets.add(target)
            text(item.get("units"), f"tolerance_records[{index}].units")
            text(item.get("public_result"), f"tolerance_records[{index}].public_result")
            evidence(item.get("evidence"), f"tolerance_records[{index}].evidence")
            if item["status"] == "EVIDENCED":
                if item.get("basis") not in TOLERANCE_BASES or item.get("boundary_policy") not in {"inclusive", "exclusive"}:
                    raise ValueError("EVIDENCED tolerance requires basis and boundary policy")
                finite(item.get("atol"), "tolerance.atol", minimum=0)
                finite(item.get("rtol"), "tolerance.rtol", minimum=0)
            elif item.get("blocker_code") != "BLOCKED_TOLERANCE_EVIDENCE":
                raise ValueError("BLOCKED tolerance requires BLOCKED_TOLERANCE_EVIDENCE")
        if tolerance_targets != numeric:
            raise ValueError("every numeric Gold requires exactly one tolerance record")
        result_checks = answer.get("result_check_assessment")
        if not isinstance(result_checks, list):
            raise ValueError("result_check_assessment must be a list")
        for index, item in enumerate(result_checks):
            if not isinstance(item, dict) or item.get("action") not in RESULT_CHECK_ACTIONS:
                raise ValueError(f"result_check_assessment[{index}] is invalid")
            for field in ("result_id", "scientific_basis", "rationale"):
                text(item.get(field), f"result_check_assessment[{index}].{field}")
            evidence(item.get("evidence"), f"result_check_assessment[{index}].evidence")

    correctness = value.get("correctness_assessment")
    if not isinstance(correctness, dict):
        raise ValueError("correctness_assessment must be an object")
    for field in ("question_correct", "answer_correct", "core_outputs_covered", "correct_answer_accepted", "obviously_wrong_rejected"):
        if not isinstance(correctness.get(field), bool):
            raise ValueError(f"correctness_assessment.{field} must be boolean")
    text(correctness.get("rationale"), "correctness_assessment.rationale")
    evidence(correctness.get("evidence"), "correctness_assessment.evidence")
    baseline_correct = all(correctness[field] for field in ("question_correct", "answer_correct", "core_outputs_covered", "correct_answer_accepted", "obviously_wrong_rejected"))
    if baseline_correct != (value["question_correctness"]["status"] == "PASS" and not answer_not_assessed and answer["status"] == "PASS"):
        raise ValueError("correctness_assessment conflicts with Q/A gate aggregates")

    enhancement = value.get("enhancement_assessment")
    if not isinstance(enhancement, dict) or enhancement.get("status") not in {"PASS", "FAIL", "NOT_ASSESSED"}:
        raise ValueError("enhancement_assessment is invalid")
    for field in ("minimal_result_checks", "quality_gradient", "risk_based_probes", "baseline_preserved"):
        if not isinstance(enhancement.get(field), bool):
            raise ValueError(f"enhancement_assessment.{field} must be boolean")
    weights = enhancement.get("weights")
    if not isinstance(weights, dict):
        raise ValueError("enhancement_assessment.weights must be an object")
    gold_weight = finite(weights.get("gold"), "enhancement_assessment.weights.gold", minimum=0)
    result_weight = finite(weights.get("result_checks"), "enhancement_assessment.weights.result_checks", minimum=0)
    if enhancement["status"] == "PASS":
        if not baseline_correct or not all(enhancement[field] for field in ("minimal_result_checks", "quality_gradient", "risk_based_probes", "baseline_preserved")):
            raise ValueError("enhancement PASS requires baseline plus all enhancement elements")
        if not (0.6 <= gold_weight <= 0.8 and 0.2 <= result_weight <= 0.4 and math.isclose(gold_weight + result_weight, 1.0)):
            raise ValueError("RESULT_ENHANCED weights must be Gold 60-80% and result checks 20-40%")
    elif enhancement["status"] == "NOT_ASSESSED" and (gold_weight != 1.0 or result_weight != 0.0):
        raise ValueError("unassessed enhancement must retain Gold-only baseline weights")

    threshold = finite(value.get("pass_threshold"), "pass_threshold", minimum=0)
    if threshold > 1:
        raise ValueError("pass_threshold must be <= 1")
    probes = value.get("probes")
    if not isinstance(probes, list):
        raise ValueError("probes must be a list")
    seen: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(probes):
        if not isinstance(item, dict) or item.get("class") not in PROBE_CLASSES or item.get("status") not in STATUSES:
            raise ValueError(f"probes[{index}] is invalid")
        text(item.get("case_id"), f"probes[{index}].case_id")
        if item["class"] in seen:
            raise ValueError("probe classes must be unique")
        seen[item["class"]] = item
        if item.get("reward") is not None:
            finite(item["reward"], f"probes[{index}].reward")
        text(item.get("expectation"), f"probes[{index}].expectation")
        text(item.get("evidence_path"), f"probes[{index}].evidence_path")
    if baseline_correct:
        if not BASELINE_PROBES.issubset(seen) or any(seen[cls]["status"] != "PASS" for cls in BASELINE_PROBES):
            raise ValueError("BASELINE_CORRECT requires the five baseline probe classes")
        if seen["valid_positive"].get("reward") is None or seen["valid_positive"]["reward"] < threshold:
            raise ValueError("valid_positive must meet pass_threshold")
        for cls in {"missing_or_malformed", "non_finite_and_duplicate", "wrong_science"}:
            if seen[cls].get("reward") is None or seen[cls]["reward"] >= threshold:
                raise ValueError(f"{cls} must fail below pass_threshold")
    if enhancement["status"] == "PASS":
        if not ENHANCEMENT_PROBES.issubset(seen) or any(seen[cls]["status"] != "PASS" for cls in ENHANCEMENT_PROBES):
            raise ValueError("RESULT_ENHANCED requires enhancement probe evidence")

    cost_status, cost_within = validate_cost(value.get("checker_cost_record"))
    operational_status = value.get("operational_status")
    if operational_status not in OPERATIONAL_STATUSES or operational_status != cost_status:
        raise ValueError("operational_status must match checker_cost_record.status")

    findings = value.get("findings")
    if not isinstance(findings, list):
        raise ValueError("findings must be a list")
    failed_codes = {item["code"] for item in q_gates + a_gates if item["status"] == "FAIL"}
    finding_codes: set[str] = set()
    routes: set[str] = set()
    ids: set[str] = set()
    for index, item in enumerate(findings):
        if not isinstance(item, dict) or item.get("layer") not in {"ADMISSION", "QUESTION", "ANSWER", "PACKAGE", "OPERATIONAL", "ENHANCEMENT"} or item.get("severity") not in {"FATAL", "HIGH", "MEDIUM", "LOW"} or item.get("route") not in ROUTES:
            raise ValueError(f"findings[{index}] is invalid")
        fid = text(item.get("finding_id"), f"findings[{index}].finding_id")
        if fid in ids:
            raise ValueError("finding IDs must be unique")
        ids.add(fid)
        codes = item.get("gate_codes")
        if not isinstance(codes, list) or any(code not in QUESTION_GATES | ANSWER_GATES for code in codes):
            raise ValueError(f"findings[{index}].gate_codes is invalid")
        finding_codes.update(codes)
        routes.add(item["route"])
        text(item.get("title"), f"findings[{index}].title")
        text(item.get("rationale"), f"findings[{index}].rationale")
        evidence(item.get("evidence"), f"findings[{index}].evidence")
    if failed_codes - finding_codes:
        raise ValueError("every failed gate requires a matching finding")
    hard_rejection = admission["status"] == "FAIL" or bool(unavailable)
    if hard_rejection:
        expected_verdict = "REJECTED"
    elif any(item["status"] == "BLOCKED" for item in q_gates + a_gates) or "BLOCKED" in routes:
        expected_verdict = "BLOCKED"
    elif "REAUTHOR" in routes:
        expected_verdict = "REAUTHOR_REQUIRED"
    elif baseline_correct:
        expected_verdict = "PASS"
    else:
        expected_verdict = "REPAIR_REQUIRED"
    if value.get("verdict") != expected_verdict:
        raise ValueError(f"verdict is inconsistent; expected {expected_verdict}")

    quality_tier = value.get("quality_tier")
    if expected_verdict == "PASS":
        expected_tier = "RESULT_ENHANCED" if enhancement["status"] == "PASS" else "BASELINE_CORRECT"
        if quality_tier != expected_tier:
            raise ValueError(f"quality_tier is inconsistent; expected {expected_tier}")
    elif quality_tier is not None:
        raise ValueError("quality_tier must be null unless verdict is PASS")
    publishable = value.get("publishable")
    if not isinstance(publishable, bool):
        raise ValueError("publishable must be boolean")
    expected_publishable = expected_verdict == "PASS" and cost_within
    if publishable != expected_publishable:
        raise ValueError("publishable must require scientific PASS and checker cost PASS")
    if expected_verdict == "PASS" and not cost_within and "REPAIR_CHECKER_COST" not in routes:
        raise ValueError("cost failure must route REPAIR_CHECKER_COST")

    rejection = value.get("rejection")
    if expected_verdict == "REJECTED":
        if not isinstance(rejection, dict) or not answer_not_assessed or probes:
            raise ValueError("REJECTED requires rejection, NOT_ASSESSED answer, and no probes")
        modes2 = rejection.get("failure_modes")
        if not isinstance(modes2, list) or not modes2 or any(mode not in REJECTION_FAILURE_MODES for mode in modes2):
            raise ValueError("rejection.failure_modes is invalid")
        if not isinstance(rejection.get("reauthor_eligible"), bool):
            raise ValueError("rejection.reauthor_eligible must be boolean")
        text(rejection.get("rationale"), "rejection.rationale")
        evidence(rejection.get("evidence"), "rejection.evidence")
    elif rejection is not None:
        raise ValueError("rejection must be null unless verdict is REJECTED")

    limitations = value.get("limitations")
    if not isinstance(limitations, list) or any(not isinstance(item, str) for item in limitations):
        raise ValueError("limitations must be a list of strings")
    return value


def validate_package_facts(value: dict[str, Any], package: Path) -> None:
    """Cross-check Review claims that have a machine-readable package source."""
    spec_path = package / "tests/grading_spec.json"
    if not spec_path.is_file():
        raise ValueError("package-aware validation requires tests/grading_spec.json")
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    tier = value.get("quality_tier")
    declared_tier = spec.get("quality_tier") or spec.get("scoring_tier")
    if tier and declared_tier in {"BASELINE_CORRECT", "RESULT_ENHANCED"} and tier != declared_tier:
        raise ValueError("Review quality_tier disagrees with grading_spec")
    if tier == "RESULT_ENHANCED":
        weights = spec.get("weights")
        if not isinstance(weights, dict):
            steps = spec.get("steps", [])
            if isinstance(steps, list):
                result_weight = sum(float(item.get("weight", 0)) for item in steps if isinstance(item, dict) and item.get("target_policy") == "recomputed_invariant")
                total_weight = sum(float(item.get("weight", 0)) for item in steps if isinstance(item, dict))
                weights = {"result_checks": result_weight, "gold": total_weight - result_weight}
        review_weights = value["enhancement_assessment"]["weights"]
        if not isinstance(weights, dict) or any(abs(float(weights[key]) - float(review_weights[key])) > 1e-12 for key in ("gold", "result_checks")):
            raise ValueError("Review enhancement weights disagree with grading_spec")
    contract = spec.get("tolerance_contract")
    if isinstance(contract, dict) and value.get("answer_correctness", {}).get("status") != "NOT_ASSESSED":
        declared = {item["target_id"]: float(item["atol"]) for item in value["answer_correctness"]["tolerance_records"] if item.get("status") == "EVIDENCED"}
        expected = {str(key): float(number) for key, number in contract.items()}
        if declared != expected:
            raise ValueError("Review tolerance records disagree with grading_spec tolerance_contract")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("review", type=Path)
    parser.add_argument("--package", type=Path, help="cross-check weights, tier, and tolerance contract against a candidate package")
    args = parser.parse_args()
    value = json.loads(args.review.read_text(encoding="utf-8"))
    validate(value)
    if args.package is not None:
        validate_package_facts(value, args.package.resolve())
    print(json.dumps({"valid": True, "verdict": value["verdict"], "quality_tier": value.get("quality_tier"), "publishable": value["publishable"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
