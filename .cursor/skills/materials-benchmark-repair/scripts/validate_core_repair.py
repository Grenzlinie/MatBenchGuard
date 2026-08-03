#!/usr/bin/env python3
"""Validate staged materials benchmark Repair records (v2.3)."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any

SCHEMA = "materials-core-repair/2.3"
STAGES = {"BASELINE_CORRECTNESS", "RESULT_ENHANCEMENT"}
ROUTES = {"REPAIR", "REAUTHOR"}
OUTCOMES = {"BASELINE_REPAIRED", "RESULT_ENHANCED", "BLOCKED", "ROLLED_BACK"}
ACTIONS = {
    "FIX_PARAMETER_CONFLICT", "RESTORE_PAPER_BACKED_CONTENT",
    "RESTORE_WORKFLOW_DEPENDENCY", "MARK_SOLVER_SEARCHABLE",
    "REMOVE_GUESSED_EXECUTION_PARAMETER", "REMOVE_REDUNDANT_GUIDANCE",
    "FIX_GOLD_APPLICABILITY", "FIX_CONDITION_GROUP_COVERAGE",
    "FIX_TOLERANCE", "ADD_EXISTING_RESOURCE_LOCATOR", "FIX_CHECKER",
    "ADD_MINIMAL_RESULT_CHECK", "REDUCE_CHECKER_COST", "SYNC_DERIVED",
    "REWRITE_SCIENTIFIC_TASK",
}
GUIDANCE_ACTIONS = {"KEEP", "ADD_FROM_PAPER", "REMOVE_REDUNDANCY", "REWRITE_BOUNDARY"}
RESULT_CHECK_ACTIONS = {"KEEP", "ADD_MINIMAL_RESULT_CHECK", "NO_AFFORDABLE_RESULT_CHECK"}
ORDER = ["instruction.md", "derived package views", "tests"]


def text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be non-empty text")
    return value.strip()


def finite(value: Any, label: str, *, minimum: float | None = None, maximum: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)):
        raise ValueError(f"{label} must be finite")
    number = float(value)
    if minimum is not None and number < minimum:
        raise ValueError(f"{label} must be >= {minimum}")
    if maximum is not None and number > maximum:
        raise ValueError(f"{label} must be <= {maximum}")
    return number


def review_validator():
    path = Path(__file__).resolve().parents[2] / "materials-benchmark-review/scripts/validate_core_review.py"
    spec = importlib.util.spec_from_file_location("core_review_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load core Review validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve(base: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else base / path


def verify_change_hashes(value: dict[str, Any], *, cwd: Path) -> None:
    source = resolve(cwd, value["source_package"]).resolve()
    candidate = resolve(cwd, value["candidate_package"]).resolve()
    for index, item in enumerate(value["changes"]):
        relative = Path(item["path"])
        before = source / relative
        after = candidate / relative
        if not before.is_file() or not after.is_file():
            raise ValueError(f"changes[{index}] source/candidate file is missing")
        before_hash = "sha256:" + hashlib.sha256(before.read_bytes()).hexdigest()
        after_hash = "sha256:" + hashlib.sha256(after.read_bytes()).hexdigest()
        if item["before_sha256"] != before_hash or item["after_sha256"] != after_hash:
            raise ValueError(f"changes[{index}] hash disagrees with source/candidate files")


def validate(value: Any, *, report_path: Path | None = None) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("schema_version") != SCHEMA:
        raise ValueError(f"schema_version must be {SCHEMA}")
    stage = value.get("repair_stage")
    route = value.get("route")
    if stage not in STAGES or route not in ROUTES:
        raise ValueError("repair_stage/route is invalid")
    if stage == "RESULT_ENHANCEMENT" and route != "REPAIR":
        raise ValueError("RESULT_ENHANCEMENT cannot Reauthor")
    for field in ("source_package", "candidate_package", "processing_root", "source_review", "candidate_review"):
        text(value.get(field), field)
    if value["source_package"] == value["candidate_package"]:
        raise ValueError("source and candidate packages must be distinct")
    if value.get("output_root") != "/app/outputs" or value.get("source_unchanged") is not True or value.get("derivation_order") != ORDER:
        raise ValueError("source/output/derivation contract is invalid")
    if not isinstance(value.get("scientific_target_preserved"), bool) or not isinstance(value.get("baseline_correctness_preserved"), bool):
        raise ValueError("preservation flags must be boolean")
    if route == "REPAIR":
        if not value["scientific_target_preserved"] or value.get("reauthor_rationale") is not None:
            raise ValueError("REPAIR must preserve the scientific target")
    else:
        if value["scientific_target_preserved"]:
            raise ValueError("REAUTHOR cannot claim target preservation")
        text(value.get("reauthor_rationale"), "reauthor_rationale")
    if stage == "RESULT_ENHANCEMENT" and not value["baseline_correctness_preserved"]:
        raise ValueError("RESULT_ENHANCEMENT must preserve baseline correctness")

    targets = value.get("targets")
    if not isinstance(targets, list) or not targets:
        raise ValueError("targets must be non-empty")
    ids: set[str] = set()
    actions: dict[str, str] = {}
    for index, item in enumerate(targets):
        if not isinstance(item, dict) or item.get("action") not in ACTIONS:
            raise ValueError(f"targets[{index}] is invalid")
        fid = text(item.get("finding_id"), f"targets[{index}].finding_id")
        if fid in ids:
            raise ValueError("finding IDs must be unique")
        ids.add(fid)
        actions[fid] = item["action"]
        if not isinstance(item.get("resolved"), bool):
            raise ValueError(f"targets[{index}].resolved must be boolean")
        text(item.get("rationale"), f"targets[{index}].rationale")
    if stage == "RESULT_ENHANCEMENT":
        forbidden = {"REWRITE_SCIENTIFIC_TASK", "RESTORE_PAPER_BACKED_CONTENT", "FIX_GOLD_APPLICABILITY", "MARK_SOLVER_SEARCHABLE"}
        if any(item["action"] in forbidden for item in targets):
            raise ValueError("RESULT_ENHANCEMENT cannot change target, Gold, or parameter semantics")
    if route == "REAUTHOR" and "REWRITE_SCIENTIFIC_TASK" not in actions.values():
        raise ValueError("REAUTHOR requires REWRITE_SCIENTIFIC_TASK")
    if route == "REPAIR" and "REWRITE_SCIENTIFIC_TASK" in actions.values():
        raise ValueError("REPAIR cannot rewrite the scientific task")

    changes = value.get("changes")
    if not isinstance(changes, list) or not changes:
        raise ValueError("changes must be non-empty")
    changed: set[str] = set()
    for index, item in enumerate(changes):
        if not isinstance(item, dict) or item.get("finding_id") not in ids:
            raise ValueError(f"changes[{index}] must bind a target")
        changed.add(item["finding_id"])
        for field in ("path", "before_sha256", "after_sha256", "evidence"):
            text(item.get(field), f"changes[{index}].{field}")
        normalized = item["path"].replace("\\", "/").lstrip("./")
        if normalized == "solution" or normalized.startswith("solution/"):
            raise ValueError("changes must not reference solution/")
        if item["before_sha256"] == item["after_sha256"]:
            raise ValueError("change hashes must differ")

    parameter_resolutions = value.get("parameter_resolutions")
    if not isinstance(parameter_resolutions, list):
        raise ValueError("parameter_resolutions must be a list")
    parameter_ids: set[str] = set()
    for index, item in enumerate(parameter_resolutions):
        if not isinstance(item, dict) or item.get("finding_id") not in ids:
            raise ValueError(f"parameter_resolutions[{index}] is invalid")
        parameter_ids.add(item["finding_id"])
        for field in ("canonical_id", "before", "after", "paper_locator", "resolution", "parameter_class", "selection_policy"):
            text(item.get(field), f"parameter_resolutions[{index}].{field}")
        if not isinstance(item.get("introduced_external_value"), bool):
            raise ValueError("parameter resolution introduced_external_value must be boolean")
        if item["parameter_class"] == "SOLVER_SEARCHABLE" and item["introduced_external_value"]:
            raise ValueError("SOLVER_SEARCHABLE repair must not invent a unique value")

    guidance = value.get("guidance_changes")
    if not isinstance(guidance, list):
        raise ValueError("guidance_changes must be a list")
    guidance_ids: set[str] = set()
    for index, item in enumerate(guidance):
        if not isinstance(item, dict) or item.get("finding_id") not in ids or item.get("action") not in GUIDANCE_ACTIONS:
            raise ValueError(f"guidance_changes[{index}] is invalid")
        guidance_ids.add(item["finding_id"])
        if not isinstance(item.get("paper_supported"), bool) or item.get("workflow_continuity_preserved") is not True:
            raise ValueError("guidance change support/continuity is invalid")
        for field in ("locator", "dependency_effect", "rationale"):
            text(item.get(field), f"guidance_changes[{index}].{field}")

    resources = value.get("resource_changes")
    if not isinstance(resources, list):
        raise ValueError("resource_changes must be a list")
    resource_ids: set[str] = set()
    for index, item in enumerate(resources):
        if not isinstance(item, dict) or item.get("finding_id") not in ids or item.get("invented") is not False:
            raise ValueError(f"resource_changes[{index}] is invalid")
        resource_ids.add(item["finding_id"])
        for field in ("resource_id", "locator", "evidence_origin"):
            text(item.get(field), f"resource_changes[{index}].{field}")

    tolerances = value.get("tolerance_changes")
    if not isinstance(tolerances, list):
        raise ValueError("tolerance_changes must be a list")
    tolerance_ids: set[str] = set()
    for index, item in enumerate(tolerances):
        if not isinstance(item, dict) or item.get("finding_id") not in ids or item.get("gold_center_unchanged") is not True:
            raise ValueError(f"tolerance_changes[{index}] must preserve the Gold center")
        tolerance_ids.add(item["finding_id"])
        for field in ("target_id", "before", "after", "basis", "evidence_path", "boundary_probe"):
            text(item.get(field), f"tolerance_changes[{index}].{field}")

    condition_groups = value.get("condition_group_changes")
    if not isinstance(condition_groups, list):
        raise ValueError("condition_group_changes must be a list")
    group_ids: set[str] = set()
    for index, item in enumerate(condition_groups):
        if not isinstance(item, dict) or item.get("finding_id") not in ids:
            raise ValueError(f"condition_group_changes[{index}] is invalid")
        group_ids.add(item["finding_id"])
        for field in ("condition_group_id", "condition_signature", "public_identifier", "before", "after", "paper_locator", "checker_branch"):
            text(item.get(field), f"condition_group_changes[{index}].{field}")
        if not item["public_identifier"].startswith("/app/outputs/"):
            raise ValueError("condition group public identifier must be under /app/outputs")
        if not isinstance(item.get("gold_target_ids"), list) or not item["gold_target_ids"]:
            raise ValueError("condition group changes require Gold targets")

    result_checks = value.get("result_check_changes")
    if not isinstance(result_checks, list):
        raise ValueError("result_check_changes must be a list")
    result_ids: set[str] = set()
    for index, item in enumerate(result_checks):
        if not isinstance(item, dict) or item.get("finding_id") not in ids or item.get("action") not in RESULT_CHECK_ACTIONS:
            raise ValueError(f"result_check_changes[{index}] is invalid")
        result_ids.add(item["finding_id"])
        for field in ("result_id", "public_contract", "hidden_check", "paper_or_invariant_basis", "cost_class"):
            text(item.get(field), f"result_check_changes[{index}].{field}")
        if item["action"] == "ADD_MINIMAL_RESULT_CHECK" and "/app/outputs/" not in item["public_contract"]:
            raise ValueError("new result check must bind a public /app/outputs artifact")
        if item.get("reads_full_trajectory") is not False or item.get("reruns_primary_science") is not False:
            raise ValueError("result checks must not read full trajectories or rerun primary science")

    for fid, action in actions.items():
        if action in {"FIX_PARAMETER_CONFLICT", "MARK_SOLVER_SEARCHABLE", "REMOVE_GUESSED_EXECUTION_PARAMETER"} and fid not in parameter_ids:
            raise ValueError(f"{action} requires parameter_resolutions")
        if action in {"RESTORE_PAPER_BACKED_CONTENT", "RESTORE_WORKFLOW_DEPENDENCY", "REMOVE_REDUNDANT_GUIDANCE"} and fid not in guidance_ids and fid not in parameter_ids:
            raise ValueError(f"{action} requires typed guidance/parameter evidence")
        if action == "ADD_EXISTING_RESOURCE_LOCATOR" and fid not in resource_ids:
            raise ValueError("ADD_EXISTING_RESOURCE_LOCATOR requires resource_changes")
        if action == "FIX_TOLERANCE" and fid not in tolerance_ids:
            raise ValueError("FIX_TOLERANCE requires tolerance_changes")
        if action == "FIX_CONDITION_GROUP_COVERAGE" and fid not in group_ids:
            raise ValueError("FIX_CONDITION_GROUP_COVERAGE requires condition_group_changes")
        if action == "ADD_MINIMAL_RESULT_CHECK" and fid not in result_ids:
            raise ValueError("ADD_MINIMAL_RESULT_CHECK requires result_check_changes")

    regressions = value.get("regressions")
    if not isinstance(regressions, list) or not regressions:
        raise ValueError("regressions must be non-empty")
    regression_ids: set[str] = set()
    for index, item in enumerate(regressions):
        if not isinstance(item, dict) or item.get("finding_id") not in ids:
            raise ValueError(f"regressions[{index}] must bind a target")
        regression_ids.add(item["finding_id"])
        for field in ("case_id", "specification", "evidence_path"):
            text(item.get(field), f"regressions[{index}].{field}")
        if stage == "BASELINE_CORRECTNESS":
            if item.get("mode") != "FAIL_BEFORE_PASS_AFTER" or item.get("before_passed") is not False or item.get("after_passed") is not True:
                raise ValueError("Stage A regressions must fail before and pass after")
        else:
            if item.get("mode") != "QUALITY_GRADIENT":
                raise ValueError("Stage B regressions must record a quality gradient")
            before_reward = finite(item.get("baseline_reward"), "regression.baseline_reward", minimum=0, maximum=1)
            after_reward = finite(item.get("enhanced_reward"), "regression.enhanced_reward", minimum=0, maximum=1)
            if before_reward == after_reward:
                raise ValueError("Stage B quality-gradient rewards must differ")
            text(item.get("expected_relation"), "regression.expected_relation")
    if not ids.issubset(changed) or not ids.issubset(regression_ids):
        raise ValueError("every target requires a change and regression")

    input_tier = value.get("input_quality_tier")
    candidate_tier = value.get("candidate_quality_tier")
    if input_tier not in {None, "BASELINE_CORRECT", "RESULT_ENHANCED"} or candidate_tier not in {None, "BASELINE_CORRECT", "RESULT_ENHANCED"}:
        raise ValueError("quality tier fields are invalid")
    verdict = value.get("candidate_review_verdict")
    if verdict not in {"PASS", "BLOCKED", "REPAIR_REQUIRED", "REAUTHOR_REQUIRED", "REJECTED"}:
        raise ValueError("candidate_review_verdict is invalid")
    outcome = value.get("outcome")
    if outcome not in OUTCOMES or not isinstance(value.get("publishable"), bool) or not isinstance(value.get("fallback_baseline_publishable"), bool):
        raise ValueError("outcome/publishable is invalid")
    resolved = all(item["resolved"] for item in targets)
    if verdict == "PASS" and resolved:
        expected = "BASELINE_REPAIRED" if stage == "BASELINE_CORRECTNESS" else "RESULT_ENHANCED"
    elif verdict == "BLOCKED":
        expected = "BLOCKED"
    else:
        expected = "ROLLED_BACK"
    if outcome != expected:
        raise ValueError(f"outcome is inconsistent; expected {expected}")
    if stage == "BASELINE_CORRECTNESS" and expected == "BASELINE_REPAIRED" and candidate_tier != "BASELINE_CORRECT":
        raise ValueError("Stage A must produce BASELINE_CORRECT")
    if stage == "RESULT_ENHANCEMENT":
        if input_tier != "BASELINE_CORRECT":
            raise ValueError("Stage B input must be independently reviewed BASELINE_CORRECT")
        if expected == "RESULT_ENHANCED" and candidate_tier != "RESULT_ENHANCED":
            raise ValueError("successful Stage B must produce RESULT_ENHANCED")
    if stage == "RESULT_ENHANCEMENT" and expected in {"ROLLED_BACK", "BLOCKED"}:
        expected_publishable = value["fallback_baseline_publishable"]
        if not expected_publishable or value.get("published_candidate") != "SOURCE_BASELINE":
            raise ValueError("failed Stage B must retain the publishable source Baseline")
    else:
        expected_publishable = expected in {"BASELINE_REPAIRED", "RESULT_ENHANCED"}
        expected_published = "CANDIDATE" if expected_publishable else "NONE"
        if value.get("published_candidate") != expected_published:
            raise ValueError("published_candidate is inconsistent with the staged outcome")
    if value["publishable"] != expected_publishable:
        raise ValueError("publishable is inconsistent with staged outcome")

    if report_path is not None:
        validator = review_validator()
        source = json.loads(resolve(report_path.parent, value["source_review"]).read_text(encoding="utf-8"))
        candidate = json.loads(resolve(report_path.parent, value["candidate_review"]).read_text(encoding="utf-8"))
        validator.validate(source)
        validator.validate(candidate)
        if candidate.get("verdict") != verdict or candidate.get("quality_tier") != candidate_tier:
            raise ValueError("candidate verdict/tier does not match candidate Review")
        if stage == "BASELINE_CORRECTNESS":
            if route == "REPAIR" and source.get("verdict") != "REPAIR_REQUIRED":
                raise ValueError("Stage A REPAIR source must be REPAIR_REQUIRED")
            if route == "REAUTHOR" and source.get("verdict") not in {"REAUTHOR_REQUIRED", "REJECTED"}:
                raise ValueError("Stage A REAUTHOR source must require Reauthor or be eligible rejected")
        else:
            if source.get("verdict") != "PASS" or source.get("quality_tier") != "BASELINE_CORRECT" or not source.get("publishable"):
                raise ValueError("Stage B source Review must be a publishable BASELINE_CORRECT PASS")
            if verdict == "PASS" and candidate.get("correctness_assessment") != source.get("correctness_assessment"):
                raise ValueError("Stage B must preserve the baseline correctness assessment")

    limitations = value.get("limitations")
    if not isinstance(limitations, list) or any(not isinstance(item, str) for item in limitations):
        raise ValueError("limitations must be a list of strings")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--verify-files", action="store_true", help="recompute every declared source/candidate change hash")
    args = parser.parse_args()
    value = json.loads(args.report.read_text(encoding="utf-8"))
    validate(value, report_path=args.report.resolve())
    if args.verify_files:
        verify_change_hashes(value, cwd=Path.cwd())
    print(json.dumps({"valid": True, "stage": value["repair_stage"], "outcome": value["outcome"], "publishable": value["publishable"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
