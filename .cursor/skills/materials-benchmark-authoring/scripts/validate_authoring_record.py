#!/usr/bin/env python3
"""Validate the external materials-benchmark authoring record."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path, PurePath, PurePosixPath
from typing import Any

SCHEMA = "materials-benchmark-authoring/1.1"
STATUSES = {
    "DRAFT",
    "BLOCKED_SOURCE_PARSE",
    "BLOCKED_RESOURCE",
    "BLOCKED_ORACLE_VALIDATION",
    "NO_ENHANCED_CANDIDATE",
    "READY_FOR_REVIEW",
    "REVIEW_FAILED",
    "REVIEW_PASSED_ENHANCED",
}
PARAMETER_CLASSES = {
    "PAPER_FIXED",
    "SOLVER_SEARCHABLE",
    "TARGET_DEFINING",
    "INDISPENSABLE_ASSET",
}
GOLD_POLICIES = {"PAPER_DIRECT", "UNIQUE_DERIVATION", "PAPER_SUPPORTED_RELATION"}
TOLERANCE_BASES = {
    "reported_uncertainty",
    "reported_precision",
    "digitization",
    "independent_recompute",
    "convergence",
    "cross_implementation",
    "reviewer_reasoned",
}
BASELINE_PROBES = {
    "valid_positive",
    "tolerance_boundary",
    "missing_or_malformed",
    "non_finite_and_duplicate",
    "wrong_science",
}
ENHANCED_PROBES = {
    "minimal_fabrication",
    "quality_gradient",
    "cross_condition_group_mismatch",
}
REVIEW_VALIDATOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "materials-benchmark-review"
    / "scripts"
    / "validate_core_review.py"
)


def load_review_validator() -> Any:
    spec = importlib.util.spec_from_file_location(
        "materials_core_review_v33_for_authoring", REVIEW_VALIDATOR_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load Review validator: {REVIEW_VALIDATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def is_canonical_output_path(value: Any) -> bool:
    if not isinstance(value, str) or "\\" in value:
        return False
    path = PurePosixPath(value)
    return (
        path.is_absolute()
        and path.parts[:3] == ("/", "app", "outputs")
        and len(path.parts) > 3
        and ".." not in path.parts
    )


class Validator:
    def __init__(self, data: dict[str, Any], path: Path, stage: str) -> None:
        self.data = data
        self.path = path
        self.stage = stage
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def require_list(self, name: str) -> list[Any]:
        value = self.data.get(name)
        if not isinstance(value, list):
            self.error(f"{name} must be a list")
            return []
        return value

    def ids(self, name: str, key: str) -> dict[str, dict[str, Any]]:
        result: dict[str, dict[str, Any]] = {}
        for index, item in enumerate(self.require_list(name)):
            if not isinstance(item, dict):
                self.error(f"{name}[{index}] must be an object")
                continue
            item_id = item.get(key)
            if not isinstance(item_id, str) or not item_id:
                self.error(f"{name}[{index}].{key} must be a non-empty string")
            elif item_id in result:
                self.error(f"duplicate {name}.{key}: {item_id}")
            else:
                result[item_id] = item
        return result

    def validate(self) -> list[str]:
        if self.data.get("schema_version") != SCHEMA:
            self.error(f"schema_version must be {SCHEMA}")
        if self.data.get("status") not in STATUSES:
            self.error(f"status must be one of {sorted(STATUSES)}")
        if not self.data.get("authoring_id"):
            self.error("authoring_id is required")

        source = self.data.get("source")
        if not isinstance(source, dict):
            self.error("source must be an object")
            source = {}
        pdf_hash = source.get("pdf_sha256")
        if not isinstance(pdf_hash, str) or len(pdf_hash) != 64:
            self.error("source.pdf_sha256 must be a 64-character SHA-256")
        for key in ("pdf_path", "markdown_path"):
            if not isinstance(source.get(key), str) or not source[key]:
                self.error(f"source.{key} is required")

        candidates = self.ids("candidate_records", "candidate_id")
        parameters = self.ids("parameter_records", "parameter_id")
        conditions = self.ids("condition_group_records", "condition_group_id")
        resources = self.ids("resource_records", "resource_id")
        gold = self.ids("gold_records", "target_id")
        tolerances = self.ids("tolerance_records", "target_id")
        workflows = self.ids("workflow_records", "workflow_id")
        outputs = self.ids("output_contract", "output_id")

        for item_id, item in parameters.items():
            if item.get("parameter_class") not in PARAMETER_CLASSES:
                self.error(f"parameter {item_id} has invalid parameter_class")
            for flag in (
                "paper_reports_unique_value",
                "instruction_requires_unique_value",
                "checker_requires_unique_value",
            ):
                if not isinstance(item.get(flag), bool):
                    self.error(f"parameter {item_id}.{flag} must be boolean")
            if item.get("parameter_class") == "INDISPENSABLE_ASSET":
                resource_id = item.get("resource_id")
                if resource_id not in resources:
                    self.error(f"indispensable parameter {item_id} references missing resource")

        for target_id, item in gold.items():
            if item.get("policy") not in GOLD_POLICIES:
                self.error(f"Gold {target_id} has invalid policy")
            group_ids = item.get("condition_group_ids")
            if not isinstance(group_ids, list) or not group_ids:
                self.error(f"Gold {target_id} needs condition_group_ids")
            else:
                for group_id in group_ids:
                    if group_id not in conditions:
                        self.error(f"Gold {target_id} references missing condition {group_id}")
            provenance = item.get("provenance")
            if not isinstance(provenance, list) or not provenance:
                self.error(f"Gold {target_id} needs provenance")
            if target_id not in tolerances:
                self.error(f"Gold {target_id} has no tolerance record")
            if not item.get("independent_check"):
                self.error(f"Gold {target_id} needs independent_check")

        for target_id, item in tolerances.items():
            if target_id not in gold:
                self.error(f"tolerance {target_id} references missing Gold")
            if item.get("basis") not in TOLERANCE_BASES:
                self.error(f"tolerance {target_id} has invalid basis")
            if item.get("boundary_policy") not in {"inclusive", "exclusive"}:
                self.error(f"tolerance {target_id} needs boundary_policy")
            evidence = item.get("boundary_evidence")
            if not isinstance(evidence, list) or len(evidence) < 3:
                self.error(f"tolerance {target_id} needs T-epsilon/T/T+epsilon boundary_evidence")

        for group_id, item in conditions.items():
            targets = item.get("required_target_ids")
            if not isinstance(targets, list) or not targets:
                self.error(f"condition {group_id} needs required_target_ids")
            else:
                for target_id in targets:
                    if target_id not in gold:
                        self.error(f"condition {group_id} references missing Gold {target_id}")
            if not item.get("condition_signature"):
                self.error(f"condition {group_id} needs condition_signature")

        for resource_id, item in resources.items():
            if item.get("indispensable") is True and item.get("availability") != "READY":
                self.error(f"indispensable resource {resource_id} is not READY")
            filename = item.get("filename")
            if filename is not None and PurePath(str(filename)).name != filename:
                self.error(f"resource {resource_id}.filename must be a basename")

        for output_id, item in outputs.items():
            path = item.get("path")
            if not is_canonical_output_path(path):
                self.error(
                    f"output {output_id}.path must be a canonical path under /app/outputs/"
                )
            target_ids = item.get("target_ids", [])
            if not isinstance(target_ids, list):
                self.error(f"output {output_id}.target_ids must be a list")
            else:
                for target_id in target_ids:
                    if target_id not in gold:
                        self.error(f"output {output_id} references missing Gold {target_id}")

        selected = self.data.get("selected_candidate_id")
        if selected is not None and selected not in candidates:
            self.error("selected_candidate_id does not reference candidate_records")

        package_path = str(self.data.get("package_path", ""))
        if not package_path:
            self.error("package_path is required")

        if self.stage in {"review-ready", "publish"}:
            self.validate_review_ready(candidates, resources, gold, workflows, outputs)
        if self.stage == "publish":
            review = self.data.get("independent_review")
            if not isinstance(review, dict):
                self.error("independent_review must be an object")
            else:
                if review.get("schema_version") != "materials-core-review/3.3":
                    self.error("publish requires independent_review.schema_version = materials-core-review/3.3")
                if review.get("verdict") != "PASS":
                    self.error("publish requires independent_review.verdict = PASS")
                if review.get("quality_tier") != "RESULT_ENHANCED":
                    self.error("publish requires quality_tier = RESULT_ENHANCED")
                if review.get("publishable") is not True:
                    self.error("publish requires independent_review.publishable = true")
                artifact_path = review.get("artifact_path")
                if not artifact_path:
                    self.error("publish requires independent_review.artifact_path")
                else:
                    resolved = Path(str(artifact_path))
                    if not resolved.is_absolute():
                        resolved = self.path.parent / resolved
                    package_root = Path(package_path)
                    if not package_root.is_absolute():
                        package_root = self.path.parent / package_root
                    grading_path = package_root / "tests" / "grading_spec.json"
                    try:
                        grading = json.loads(grading_path.read_text(encoding="utf-8"))
                    except (OSError, json.JSONDecodeError) as exc:
                        self.error(f"publish grading_spec is not readable JSON: {exc}")
                    else:
                        if not isinstance(grading, dict):
                            self.error("publish grading_spec root must be an object")
                        else:
                            if grading.get("quality_tier") != "RESULT_ENHANCED":
                                self.error(
                                    "publish requires grading_spec.quality_tier = RESULT_ENHANCED"
                                )
                            if "scoring_tier" in grading:
                                self.error(
                                    "publish grading_spec must not use legacy scoring_tier"
                                )
                    try:
                        resolved.resolve().relative_to(package_root.resolve())
                    except ValueError:
                        pass
                    else:
                        self.error("review artifact must stay outside the candidate package")
                    try:
                        artifact = json.loads(resolved.read_text(encoding="utf-8"))
                    except (OSError, json.JSONDecodeError) as exc:
                        self.error(f"review artifact is not readable JSON: {exc}")
                    else:
                        if not isinstance(artifact, dict):
                            self.error("review artifact root must be an object")
                        else:
                            try:
                                review_validator = load_review_validator()
                                review_validator.validate(artifact)
                                review_validator.validate_package_facts(
                                    artifact, package_root.resolve()
                                )
                            except (OSError, RuntimeError, TypeError, ValueError, KeyError) as exc:
                                self.error(f"Review 3.3 validation failed: {exc}")
                            for field in (
                                "schema_version",
                                "verdict",
                                "quality_tier",
                                "publishable",
                            ):
                                if artifact.get(field) != review.get(field):
                                    self.error(
                                        f"review artifact {field} does not match independent_review summary"
                                    )
            if self.data.get("status") != "REVIEW_PASSED_ENHANCED":
                self.error("publish requires status REVIEW_PASSED_ENHANCED")
        return self.errors

    def validate_review_ready(
        self,
        candidates: dict[str, dict[str, Any]],
        resources: dict[str, dict[str, Any]],
        gold: dict[str, dict[str, Any]],
        workflows: dict[str, dict[str, Any]],
        outputs: dict[str, dict[str, Any]],
    ) -> None:
        parse_quality = self.data.get("parse_quality")
        if not isinstance(parse_quality, dict) or parse_quality.get("status") != "PASS":
            self.error("review-ready requires parse_quality.status = PASS")
        selected = self.data.get("selected_candidate_id")
        if selected not in candidates:
            self.error("review-ready requires a selected candidate")
        else:
            candidate = candidates[selected]
            if candidate.get("decision") != "SELECTED":
                self.error("selected candidate decision must be SELECTED")
            if candidate.get("q0_status") != "PASS":
                self.error("selected candidate must pass Q0")
            checkpoints = candidate.get("checkpoint_ids")
            if not isinstance(checkpoints, list) or not checkpoints:
                self.error("selected candidate needs an enhanced checkpoint")
        if self.data.get("blockers"):
            self.error("review-ready requires no blockers")
        if not gold:
            self.error("review-ready requires Gold records")
        if not outputs:
            self.error("review-ready requires output_contract")
        if not workflows:
            self.error("review-ready requires workflow_records")
        for workflow_id, item in workflows.items():
            if not item.get("producer") or not item.get("consumer"):
                self.error(f"workflow {workflow_id} needs producer and consumer")

        for resource_id, item in resources.items():
            if item.get("indispensable") and item.get("availability") != "READY":
                self.error(f"resource {resource_id} blocks review readiness")

        enhancement = self.data.get("enhancement")
        if not isinstance(enhancement, dict):
            self.error("enhancement must be an object")
        else:
            gold_weight = enhancement.get("gold_weight")
            result_weight = enhancement.get("result_weight")
            if not isinstance(gold_weight, (int, float)) or not 0.60 <= gold_weight <= 0.80:
                self.error("enhancement.gold_weight must be 0.60--0.80")
            if not isinstance(result_weight, (int, float)) or not 0.20 <= result_weight <= 0.40:
                self.error("enhancement.result_weight must be 0.20--0.40")
            if (
                isinstance(gold_weight, (int, float))
                and isinstance(result_weight, (int, float))
                and not math.isclose(gold_weight + result_weight, 1.0, abs_tol=1e-9)
            ):
                self.error("Gold and result weights must sum to 1.0")
            checks = enhancement.get("result_checks")
            if not isinstance(checks, list) or not checks:
                self.error("review-ready requires at least one result check")

        probe_types = {
            item.get("probe_type")
            for item in self.require_list("probe_records")
            if isinstance(item, dict) and item.get("status") == "PASS"
        }
        missing = BASELINE_PROBES - probe_types
        if missing:
            self.error(f"missing passing Baseline probes: {sorted(missing)}")
        if not (ENHANCED_PROBES & probe_types):
            self.error("missing passing enhancement probe")

        oracle = self.data.get("oracle_validation")
        if not isinstance(oracle, dict):
            self.error("review-ready requires oracle_validation")
        else:
            if oracle.get("purpose") != "CHECKER_FULL_SCORE_FIXTURE":
                self.error(
                    "oracle_validation.purpose must be CHECKER_FULL_SCORE_FIXTURE"
                )
            if oracle.get("scientific_execution_performed") is not False:
                self.error(
                    "oracle_validation.scientific_execution_performed must be false"
                )
            if oracle.get("status") != "PASS":
                self.error("oracle_validation.status must be PASS")
            for field in ("expected_reward", "actual_reward"):
                value = oracle.get(field)
                if (
                    isinstance(value, bool)
                    or not isinstance(value, (int, float))
                    or not math.isclose(float(value), 1.0, abs_tol=1e-12)
                ):
                    self.error(f"oracle_validation.{field} must be 1.0")
            if oracle.get("all_components_full_score") is not True:
                self.error(
                    "oracle_validation.all_components_full_score must be true"
                )
            command = oracle.get("command")
            if not isinstance(command, str) or "-a oracle" not in command:
                self.error("oracle_validation.command must record a Harbor oracle run")
            evidence = oracle.get("evidence")
            if not isinstance(evidence, list) or not evidence or not all(
                isinstance(item, str) and item.strip() for item in evidence
            ):
                self.error("oracle_validation.evidence must contain external run evidence")

        cost = self.data.get("checker_cost_record")
        if not isinstance(cost, dict) or cost.get("status") != "PASS":
            self.error("checker_cost_record.status must be PASS")
            return
        if cost.get("real_scale_input") is not True:
            self.error("checker cost must use real-scale input")
        if cost.get("uses_full_trajectory") is True:
            self.error("checker must not use full large trajectory")
        if cost.get("performs_new_simulation") is True:
            self.error("checker must not perform a new primary simulation")
        for field in (
            "measured_wall_seconds",
            "peak_memory_mb",
            "input_bytes_read",
        ):
            value = cost.get(field)
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or value < 0
            ):
                self.error(f"checker {field} must be a non-negative finite number")
        wall_seconds = cost.get("measured_wall_seconds")
        if (
            isinstance(wall_seconds, (int, float))
            and not isinstance(wall_seconds, bool)
            and math.isfinite(wall_seconds)
            and wall_seconds > 600
        ):
            self.error("checker wall time exceeds 600 seconds")
        rationale = cost.get("cost_rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            self.error("checker cost_rationale must be non-empty text")
        hardware_class = cost.get("hardware_class")
        if hardware_class not in {"CPU", "SINGLE_GPU"}:
            self.error("checker hardware_class must be CPU or SINGLE_GPU")
        cpu_cores = cost.get("cpu_cores")
        gpu_count = cost.get("gpu_count")
        if (
            isinstance(cpu_cores, bool)
            or not isinstance(cpu_cores, (int, float))
            or not math.isfinite(cpu_cores)
            or cpu_cores < 0
        ):
            self.error("checker cpu_cores must be a non-negative finite number")
        if (
            isinstance(gpu_count, bool)
            or not isinstance(gpu_count, (int, float))
            or not math.isfinite(gpu_count)
            or gpu_count < 0
        ):
            self.error("checker gpu_count must be a non-negative finite number")
            gpu_count = 0
        if hardware_class == "CPU":
            if gpu_count != 0 or cost.get("gpu_type") is not None:
                self.error("CPU checker must use gpu_count=0 and gpu_type=null")
        elif hardware_class == "SINGLE_GPU":
            if gpu_count != 1:
                self.error("SINGLE_GPU checker must use exactly one GPU")
            if not isinstance(cost.get("gpu_type"), str) or not cost["gpu_type"].strip():
                self.error("SINGLE_GPU checker requires gpu_type")
            if cost.get("h100_equivalent_or_less") is not True:
                self.error("SINGLE_GPU checker must attest h100_equivalent_or_less=true")
        if isinstance(cpu_cores, (int, float)) and not isinstance(cpu_cores, bool) and cpu_cores > 32:
            self.error("checker CPU cores exceed 32")
        if isinstance(gpu_count, (int, float)) and not isinstance(gpu_count, bool) and gpu_count > 1:
            self.error("checker GPU count exceeds 1")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("--stage", choices=("draft", "review-ready", "publish"), default="draft")
    args = parser.parse_args()
    try:
        data = json.loads(args.record.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, indent=2))
        return 1
    if not isinstance(data, dict):
        print(json.dumps({"valid": False, "errors": ["record root must be an object"]}, indent=2))
        return 1
    errors = Validator(data, args.record, args.stage).validate()
    print(json.dumps({"valid": not errors, "stage": args.stage, "errors": errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
