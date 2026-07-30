#!/usr/bin/env python3
"""Validate Agent-authored materials quality records without inferring science."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

SCHEMA = "materials-agent-final-decision/2.3"
CRITERIA = {
    "2.1": "materials_qualification",
    "2.2": "prompt_contract",
    "2.3": "scientific_validity",
    "2.4": "checker_core_coverage",
    "2.5": "checker_discrimination",
    "2.6": "gold_and_tolerance",
    "2.7": "no_leakage_or_exploit",
    "2.8": "inputs_and_reproducibility",
}
DIMENSIONS = {
    "C01": 10,
    "C02": 20,
    "C03": 20,
    "C04": 20,
    "C05": 10,
    "C06": 10,
    "C07": 10,
}
HARD_GATES = {
    "NON_MATERIALS_TASK",
    "SCIENTIFIC_TARGET_INVALID",
    "SCIENTIFIC_REASONING_ABSENT",
    "CHECKER_CORE_TASK_UNASSESSED",
    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
    "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE",
}
PROBES = {
    "valid_positive",
    "missing_output",
    "empty_output",
    "malformed_output",
    "random_or_constant",
    "duplicate_records",
    "non_finite_values",
    "minimal_exploit",
    "quality_gradient",
    "semantic_equivalence",
    "component_isolation",
}
READINESS = {"data", "model", "software", "environment", "license_access"}
SCIENTIFIC_PATTERNS = {
    "CROSS_STEP_PARAMETER_CONTRADICTION": ("2.2", "C02"),
    "METHOD_REFERENCE_MISMATCH": ("2.3", "C03"),
    "UNSUPPORTED_SYNTHETIC_GOLD": ("2.6", "C04"),
    "MISSING_TARGET_DEFINING_INPUTS": ("2.3", "C03"),
    "CRYSTALLOGRAPHIC_SELF_CONTRADICTION": ("2.3", "C03"),
    "UNSPECIFIED_MD_CONDITIONS": ("2.3", "C03"),
    "INCOMPLETE_CELL_BOUNDARY_DEFINITION": ("2.3", "C03"),
    "AMBIGUOUS_OBSERVABLE_DEFINITION": ("2.2", "C02"),
    "AMBIGUOUS_LOAD_SEMANTICS": ("2.2", "C02"),
    "OUTPUT_SCORING_CONTRACT_CONTRADICTION": ("2.2", "C02"),
    "UNVERIFIABLE_COMPUTATION_CLAIM": ("2.4", "C04"),
    "ANALYSIS_PROTOCOL_UNDERSPECIFIED": ("2.2", "C02"),
    "SIMULATION_CONTRACT_UNDERDETERMINED": ("2.3", "C03"),
    "SIMULATION_PARAMETER_DEPENDENCY_BROKEN": ("2.3", "C03"),
}
STATUSES = {"PASS", "FAIL", "NOT_ASSESSABLE"}
PROBE_STATUSES = STATUSES | {"NOT_APPLICABLE"}
PATTERN_STATUSES = STATUSES | {"NOT_APPLICABLE"}
READY_STATUSES = {"READY", "NOT_REQUIRED", "NOT_READY", "NOT_ASSESSABLE"}
VERDICTS = {"PASS", "CONDITIONAL", "REJECT", "NOT_ASSESSABLE"}
DIAGNOSTICS = {"CONFIRMED", "DISMISSED_FALSE_POSITIVE", "AUTOMATION_LIMITATION"}
DISPOSITIONS = {"NONE", "REPAIR", "ABANDON"}
REASONING_FAILURE_MODES = {"PURE_INFORMATION_EXTRACTION", "PURE_ALGEBRAIC_COMPUTATION"}
PARAMETER_BUCKETS = {
    "fixed_or_source_required",
    "derived_or_coupled",
    "representation_equivalent",
    "solver_selectable",
}
PARAMETER_SOURCE_STATUSES = {
    "PAPER_EXPLICIT",
    "PAPER_DERIVED",
    "PACKAGE_DEFINED",
    "REPRESENTATION_EQUIVALENT",
    "SOLVER_SELECTABLE",
    "MISSING",
}
PARAMETER_RESOLUTIONS = {
    "FIXED_TO_SOURCE",
    "UNIQUE_DERIVATION",
    "PACKAGE_SELF_CONTAINED",
    "EQUIVALENCE_TRANSFORM",
    "SOLVER_CHOICE_JUSTIFIED",
    "UNRESOLVED",
}


def _text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be non-empty text")
    return value.strip()


def _evidence(value: Any, label: str) -> list[dict[str, str]]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} requires evidence")
    result = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise ValueError(f"{label}[{index}] must be an object")
        record = {
            key: _text(item.get(key), f"{label}[{index}].{key}")
            for key in ("source_kind", "path", "locator", "quote_or_result")
        }
        normalized = record["path"].replace("\\", "/").lstrip("./")
        if normalized == "solution" or normalized.startswith("solution/"):
            raise ValueError(f"{label}[{index}].path must not reference solution/")
        result.append(record)
    return result


def _status_record(value: Any, statuses: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("status") not in statuses:
        raise ValueError(f"{label} has invalid status")
    return {
        **value,
        "rationale": _text(value.get("rationale"), f"{label}.rationale"),
        "evidence": _evidence(value.get("evidence"), f"{label}.evidence"),
    }


def _failure_modes(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or any(
        mode not in REASONING_FAILURE_MODES for mode in value
    ):
        raise ValueError(f"{label} must contain valid failure modes")
    if len(value) != len(set(value)):
        raise ValueError(f"{label} contains duplicates")
    return value


def _text_list(value: Any, label: str, *, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list) or (not allow_empty and not value):
        raise ValueError(f"{label} must be a {'list' if allow_empty else 'non-empty list'}")
    return [_text(item, f"{label}[{index}]") for index, item in enumerate(value)]


def _validate_parameter_assessment(value: Any) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    if not isinstance(value, dict) or set(value) != PARAMETER_BUCKETS:
        raise ValueError(
            "parameter_assessment requires fixed_or_source_required, "
            "derived_or_coupled, representation_equivalent, and solver_selectable"
        )
    records: dict[str, dict[str, Any]] = {}
    items: list[dict[str, Any]] = []
    for bucket in sorted(PARAMETER_BUCKETS):
        record = _status_record(value[bucket], STATUSES, f"parameter_assessment.{bucket}")
        raw_items = record.get("items")
        if not isinstance(raw_items, list):
            raise ValueError(f"parameter_assessment.{bucket}.items must be a list")
        records[bucket] = record
        for index, item in enumerate(raw_items):
            label = f"parameter_assessment.{bucket}.items[{index}]"
            if not isinstance(item, dict):
                raise ValueError(f"{label} must be an object")
            parameter_id = _text(item.get("parameter_id"), f"{label}.parameter_id")
            if any(existing["parameter_id"] == parameter_id for existing in items):
                raise ValueError(f"duplicate parameter_id: {parameter_id}")
            source_status = item.get("source_status")
            resolution = item.get("resolution")
            if source_status not in PARAMETER_SOURCE_STATUSES:
                raise ValueError(f"{label}.source_status is invalid")
            if resolution not in PARAMETER_RESOLUTIONS:
                raise ValueError(f"{label}.resolution is invalid")
            scoring_sensitive = item.get("scoring_sensitive")
            execution_required = item.get("execution_required")
            paper_reference_required = item.get("paper_reference_required")
            if not isinstance(scoring_sensitive, bool):
                raise ValueError(f"{label}.scoring_sensitive must be boolean")
            if not isinstance(execution_required, bool):
                raise ValueError(f"{label}.execution_required must be boolean")
            if not isinstance(paper_reference_required, bool):
                raise ValueError(f"{label}.paper_reference_required must be boolean")
            normalized = {
                **item,
                "parameter_id": parameter_id,
                "category": _text(item.get("category"), f"{label}.category"),
                "introduced_at": _text_list(
                    item.get("introduced_at"), f"{label}.introduced_at"
                ),
                "source_status": source_status,
                "value_or_rule": _text(item.get("value_or_rule"), f"{label}.value_or_rule"),
                "depends_on": _text_list(
                    item.get("depends_on"), f"{label}.depends_on", allow_empty=True
                ),
                "downstream_consumers": _text_list(
                    item.get("downstream_consumers"),
                    f"{label}.downstream_consumers",
                    allow_empty=True,
                ),
                "affects_scored_outputs": _text_list(
                    item.get("affects_scored_outputs"),
                    f"{label}.affects_scored_outputs",
                    allow_empty=True,
                ),
                "scoring_sensitive": scoring_sensitive,
                "execution_required": execution_required,
                "paper_reference_required": paper_reference_required,
                "resolution": resolution,
                "evidence": _evidence(item.get("evidence"), f"{label}.evidence"),
                "bucket": bucket,
            }
            if source_status == "MISSING" and resolution != "UNRESOLVED":
                raise ValueError(f"{label} MISSING requires resolution UNRESOLVED")
            if source_status == "PAPER_DERIVED" and resolution != "UNIQUE_DERIVATION":
                raise ValueError(
                    f"{label} PAPER_DERIVED requires resolution UNIQUE_DERIVATION"
                )
            if (
                source_status == "REPRESENTATION_EQUIVALENT"
                and resolution != "EQUIVALENCE_TRANSFORM"
            ):
                raise ValueError(
                    f"{label} REPRESENTATION_EQUIVALENT requires EQUIVALENCE_TRANSFORM"
                )
            if (
                source_status == "SOLVER_SELECTABLE"
                and resolution != "SOLVER_CHOICE_JUSTIFIED"
            ):
                raise ValueError(
                    f"{label} SOLVER_SELECTABLE requires SOLVER_CHOICE_JUSTIFIED"
                )
            if scoring_sensitive and not normalized["affects_scored_outputs"]:
                raise ValueError(
                    f"{label} scoring_sensitive requires affects_scored_outputs"
                )
            items.append(normalized)
        if any(
            item["bucket"] == bucket and item["resolution"] == "UNRESOLVED"
            for item in items
        ) and record["status"] != "FAIL":
            raise ValueError(
                f"parameter_assessment.{bucket} requires FAIL for unresolved items"
            )

    ids = {item["parameter_id"] for item in items}
    for item in items:
        unknown = set(item["depends_on"]) - ids
        if unknown:
            raise ValueError(
                f"parameter {item['parameter_id']} depends on unknown ids: "
                + ", ".join(sorted(unknown))
            )

    graph = {item["parameter_id"]: item["depends_on"] for item in items}
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(parameter_id: str) -> None:
        if parameter_id in visiting:
            raise ValueError("parameter dependency graph contains a cycle")
        if parameter_id in visited:
            return
        visiting.add(parameter_id)
        for dependency in graph[parameter_id]:
            visit(dependency)
        visiting.remove(parameter_id)
        visited.add(parameter_id)

    for parameter_id in graph:
        visit(parameter_id)
    return records, items


def validate(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("schema_version") != SCHEMA:
        raise ValueError(f"decision schema_version must be {SCHEMA}")
    if value.get("mode") not in {"REVIEW", "REPAIR_REAUDIT"}:
        raise ValueError("mode must be REVIEW or REPAIR_REAUDIT")
    if value.get("reproduction_intent") not in {
        "EXACT_REPRODUCTION",
        "METHOD_REIMPLEMENTATION",
        "SCIENTIFIC_EXTENSION",
    }:
        raise ValueError("invalid reproduction_intent")
    _text(value.get("package_id"), "package_id")
    reviewed_scope = value.get("reviewed_scope")
    limitations = value.get("limitations")
    if not isinstance(reviewed_scope, list) or not reviewed_scope:
        raise ValueError("reviewed_scope must be a non-empty list")
    for index, item in enumerate(reviewed_scope):
        scope_item = _text(item, f"reviewed_scope[{index}]")
        normalized = scope_item.replace("\\", "/").lstrip("./")
        if normalized == "solution" or normalized.startswith("solution/"):
            raise ValueError("reviewed_scope must not include solution/")
    if not isinstance(limitations, list):
        raise ValueError("limitations must be a list")
    for index, item in enumerate(limitations):
        _text(item, f"limitations[{index}]")

    criteria = value.get("criteria")
    if not isinstance(criteria, dict) or set(criteria) != set(CRITERIA):
        raise ValueError("criteria must contain exactly 2.1 through 2.8")
    for key, name in CRITERIA.items():
        record = _status_record(criteria[key], STATUSES, f"criteria.{key}")
        if record.get("name") != name:
            raise ValueError(f"criteria.{key}.name must be {name}")

    patterns = value.get("scientific_risk_patterns")
    if not isinstance(patterns, dict) or set(patterns) != set(SCIENTIFIC_PATTERNS):
        raise ValueError(
            "scientific_risk_patterns must contain every canonical pattern"
        )
    pattern_status: dict[str, str] = {}
    for pattern_id, (criterion, dimension) in SCIENTIFIC_PATTERNS.items():
        record = _status_record(
            patterns[pattern_id],
            PATTERN_STATUSES,
            f"scientific_risk_patterns.{pattern_id}",
        )
        if record.get("criterion") != criterion or record.get("dimension") != dimension:
            raise ValueError(
                f"scientific_risk_patterns.{pattern_id} must map to "
                f"{criterion}/{dimension}"
            )
        if record["status"] == "FAIL" and criteria[criterion]["status"] != "FAIL":
            raise ValueError(
                f"scientific_risk_patterns.{pattern_id} FAIL requires "
                f"criteria.{criterion} FAIL"
            )
        pattern_status[pattern_id] = record["status"]

    dimensions = value.get("dimensions")
    if not isinstance(dimensions, list) or len(dimensions) != len(DIMENSIONS):
        raise ValueError("dimensions must contain C01 through C07")
    seen_dimensions: set[str] = set()
    calculated = 0.0
    for index, item in enumerate(dimensions):
        if not isinstance(item, dict) or item.get("dimension") not in DIMENSIONS:
            raise ValueError(f"dimensions[{index}] is invalid")
        dim = item["dimension"]
        if dim in seen_dimensions or item.get("weight") != DIMENSIONS[dim]:
            raise ValueError(f"dimension {dim} is duplicated or has wrong weight")
        seen_dimensions.add(dim)
        score = item.get("normalized")
        if (
            isinstance(score, bool)
            or not isinstance(score, (int, float))
            or not math.isfinite(score)
            or not 0 <= score <= 100
        ):
            raise ValueError(f"dimension {dim} normalized must be finite 0..100")
        _evidence(item.get("evidence"), f"dimension.{dim}.evidence")
        calculated += DIMENSIONS[dim] * float(score) / 100
    if seen_dimensions != set(DIMENSIONS):
        raise ValueError("dimensions must contain each C01 through C07 once")
    total = value.get("weighted_score")
    if (
        isinstance(total, bool)
        or not isinstance(total, (int, float))
        or abs(float(total) - round(calculated, 2)) > 1e-6
    ):
        raise ValueError(
            f"weighted_score is inconsistent; expected {round(calculated, 2)}"
        )

    gates = value.get("hard_gates")
    if not isinstance(gates, list) or len(gates) != len(HARD_GATES):
        raise ValueError(f"hard_gates must contain exactly {len(HARD_GATES)} records")
    gate_status: dict[str, str] = {}
    gate_disposition: dict[str, str] = {}
    gate_modes: dict[str, list[str]] = {}
    for index, item in enumerate(gates):
        record = _status_record(item, STATUSES, f"hard_gates[{index}]")
        code = record.get("code")
        if code not in HARD_GATES or code in gate_status:
            raise ValueError("hard_gates must contain each canonical code once")
        disposition = record.get("disposition")
        if disposition not in DISPOSITIONS:
            raise ValueError(f"hard_gates[{index}].disposition is invalid")
        if record["status"] == "PASS" and disposition != "NONE":
            raise ValueError(f"hard_gates[{index}] PASS requires disposition NONE")
        if record["status"] == "FAIL" and disposition == "NONE":
            raise ValueError(f"hard_gates[{index}] FAIL requires REPAIR or ABANDON")
        modes = _failure_modes(
            item.get("failure_modes"), f"hard_gates[{index}].failure_modes"
        )
        if code == "SCIENTIFIC_REASONING_ABSENT":
            if record["status"] == "FAIL" and not modes:
                raise ValueError(
                    "SCIENTIFIC_REASONING_ABSENT FAIL requires failure_modes"
                )
            if record["status"] != "FAIL" and modes:
                raise ValueError("SCIENTIFIC_REASONING_ABSENT modes require FAIL")
        elif modes:
            raise ValueError(
                f"hard_gates[{index}].failure_modes is only valid for SCIENTIFIC_REASONING_ABSENT"
            )
        gate_status[code] = record["status"]
        gate_disposition[code] = disposition
        gate_modes[code] = modes
    if set(gate_status) != HARD_GATES:
        raise ValueError("hard_gates are incomplete")

    probes = value.get("checker_probes")
    if not isinstance(probes, dict) or set(probes) != PROBES:
        raise ValueError("checker_probes must contain all required classes")
    for name in PROBES:
        _status_record(probes[name], PROBE_STATUSES, f"checker_probes.{name}")
    if probes["valid_positive"]["status"] == "NOT_APPLICABLE":
        raise ValueError("valid_positive cannot be NOT_APPLICABLE")

    readiness = value.get("readiness")
    if not isinstance(readiness, dict) or set(readiness) != READINESS:
        raise ValueError(
            "readiness must contain data/model/software/environment/license_access"
        )
    for name in READINESS:
        record = _status_record(readiness[name], READY_STATUSES, f"readiness.{name}")
        resources = record.get("resources")
        if not isinstance(resources, list):
            raise ValueError(f"readiness.{name}.resources must be a list")
        if record["status"] == "READY" and not resources:
            raise ValueError(f"readiness.{name} READY requires resource records")
        for index, resource in enumerate(resources):
            if not isinstance(resource, dict):
                raise ValueError(
                    f"readiness.{name}.resources[{index}] must be an object"
                )
            for field in (
                "resource_id",
                "role",
                "identity_version",
                "locator",
                "access_result",
                "sufficiency",
                "allowed_alternative",
            ):
                _text(
                    resource.get(field), f"readiness.{name}.resources[{index}].{field}"
                )

    parameters, parameter_items = _validate_parameter_assessment(
        value.get("parameter_assessment")
    )

    diagnostics = value.get("diagnostic_adjudications", [])
    if not isinstance(diagnostics, list):
        raise ValueError("diagnostic_adjudications must be a list")
    for index, item in enumerate(diagnostics):
        if not isinstance(item, dict) or item.get("disposition") not in DIAGNOSTICS:
            raise ValueError(f"diagnostic_adjudications[{index}] is invalid")
        _text(item.get("diagnostic"), f"diagnostic_adjudications[{index}].diagnostic")
        _text(item.get("reason"), f"diagnostic_adjudications[{index}].reason")
        _evidence(item.get("evidence"), f"diagnostic_adjudications[{index}].evidence")

    findings = value.get("open_confirmed_findings")
    if not isinstance(findings, list):
        raise ValueError("open_confirmed_findings must be a list")
    for index, item in enumerate(findings):
        if not isinstance(item, dict):
            raise ValueError(f"open_confirmed_findings[{index}] must be an object")
        for field in ("finding_id", "title"):
            _text(item.get(field), f"open_confirmed_findings[{index}].{field}")
        pattern_id = item.get("pattern_id")
        if pattern_id is not None and pattern_id not in SCIENTIFIC_PATTERNS:
            raise ValueError(
                f"open_confirmed_findings[{index}].pattern_id is invalid"
            )
        if (
            item.get("severity") not in {"FATAL", "HIGH", "MEDIUM", "LOW"}
            or item.get("dimension") not in DIMENSIONS
        ):
            raise ValueError(
                f"open_confirmed_findings[{index}] has invalid severity/dimension"
            )
        if (
            pattern_id is not None
            and item.get("dimension") != SCIENTIFIC_PATTERNS[pattern_id][1]
        ):
            raise ValueError(
                f"open_confirmed_findings[{index}].dimension conflicts with pattern"
            )
        if not isinstance(item.get("repairable"), bool) or not isinstance(
            item.get("hard_gate"), bool
        ):
            raise ValueError(
                f"open_confirmed_findings[{index}] requires boolean repairable/hard_gate"
            )
        disposition = item.get("disposition")
        if disposition not in {"REPAIR", "ABANDON"}:
            raise ValueError(f"open_confirmed_findings[{index}].disposition is invalid")
        if (disposition == "REPAIR") != item["repairable"]:
            raise ValueError(
                f"open_confirmed_findings[{index}] disposition conflicts with repairable"
            )
        hard_gate_code = item.get("hard_gate_code")
        if item["hard_gate"]:
            if hard_gate_code not in HARD_GATES:
                raise ValueError(
                    f"open_confirmed_findings[{index}].hard_gate_code is invalid"
                )
        elif hard_gate_code is not None:
            raise ValueError(
                f"open_confirmed_findings[{index}].hard_gate_code must be null when hard_gate is false"
            )
        modes = _failure_modes(
            item.get("failure_modes"), f"open_confirmed_findings[{index}].failure_modes"
        )
        if hard_gate_code == "SCIENTIFIC_REASONING_ABSENT":
            if not modes:
                raise ValueError(
                    "SCIENTIFIC_REASONING_ABSENT finding requires failure_modes"
                )
        elif modes:
            raise ValueError(
                f"open_confirmed_findings[{index}].failure_modes is only valid for SCIENTIFIC_REASONING_ABSENT"
            )
        _evidence(item.get("evidence"), f"open_confirmed_findings[{index}].evidence")

    failed_patterns = {
        pattern_id for pattern_id, status in pattern_status.items() if status == "FAIL"
    }
    finding_patterns = {
        item["pattern_id"]
        for item in findings
        if item.get("pattern_id") is not None
    }
    missing_pattern_findings = failed_patterns - finding_patterns
    if missing_pattern_findings:
        raise ValueError(
            "failed scientific patterns require matching confirmed findings: "
            + ", ".join(sorted(missing_pattern_findings))
        )
    inconsistent_pattern_findings = {
        pattern_id
        for pattern_id in finding_patterns
        if pattern_status[pattern_id] != "FAIL"
    }
    if inconsistent_pattern_findings:
        raise ValueError(
            "pattern-linked findings require the pattern status FAIL: "
            + ", ".join(sorted(inconsistent_pattern_findings))
        )

    reasoning_gate_failed = gate_status["SCIENTIFIC_REASONING_ABSENT"] == "FAIL"
    if reasoning_gate_failed:
        if gate_disposition["SCIENTIFIC_REASONING_ABSENT"] != "ABANDON":
            raise ValueError(
                "SCIENTIFIC_REASONING_ABSENT FAIL requires disposition ABANDON"
            )
        if criteria["2.3"]["status"] != "FAIL":
            raise ValueError(
                "SCIENTIFIC_REASONING_ABSENT FAIL requires criteria.2.3 FAIL"
            )
        matches = [
            item
            for item in findings
            if item.get("hard_gate_code") == "SCIENTIFIC_REASONING_ABSENT"
        ]
        if not matches:
            raise ValueError(
                "SCIENTIFIC_REASONING_ABSENT FAIL requires a matching finding"
            )
        for item in matches:
            if item["repairable"] or item["disposition"] != "ABANDON":
                raise ValueError(
                    "SCIENTIFIC_REASONING_ABSENT finding must be non-repairable ABANDON"
                )
            if set(item["failure_modes"]) != set(
                gate_modes["SCIENTIFIC_REASONING_ABSENT"]
            ):
                raise ValueError(
                    "SCIENTIFIC_REASONING_ABSENT finding modes must match the Gate"
                )

    essential_parameter_code = "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE"
    essential_missing = [
        item
        for item in parameter_items
        if item["source_status"] == "MISSING"
        and item["paper_reference_required"]
        and (item["execution_required"] or item["scoring_sensitive"])
    ]
    essential_gate_failed = gate_status[essential_parameter_code] == "FAIL"
    if bool(essential_missing) != essential_gate_failed:
        raise ValueError(
            "paper-required essential MISSING parameters and "
            "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE Gate must agree"
        )
    if essential_gate_failed:
        if gate_disposition[essential_parameter_code] != "ABANDON":
            raise ValueError(
                "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE FAIL requires "
                "disposition ABANDON"
            )
        if criteria["2.3"]["status"] != "FAIL":
            raise ValueError(
                "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE FAIL requires "
                "criteria.2.3 FAIL"
            )
        if pattern_status["SIMULATION_CONTRACT_UNDERDETERMINED"] != "FAIL":
            raise ValueError(
                "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE FAIL requires "
                "SIMULATION_CONTRACT_UNDERDETERMINED FAIL"
            )
        matches = [
            item
            for item in findings
            if item.get("hard_gate_code") == essential_parameter_code
        ]
        if not matches:
            raise ValueError(
                "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE FAIL requires "
                "a matching finding"
            )
        for item in matches:
            if item["repairable"] or item["disposition"] != "ABANDON":
                raise ValueError(
                    "essential simulation parameter finding must be "
                    "non-repairable ABANDON"
                )

    criterion_statuses = [criteria[key]["status"] for key in CRITERIA]
    probe_statuses = [probes[name]["status"] for name in PROBES]
    readiness_statuses = [readiness[name]["status"] for name in READINESS]
    parameter_statuses = [parameters[name]["status"] for name in parameters]
    scientific_pattern_statuses = list(pattern_status.values())
    hard_fail = "FAIL" in gate_status.values() or any(
        item.get("hard_gate") for item in findings
    )
    unrecoverable_fatal = any(
        item.get("severity") == "FATAL" and not item.get("repairable")
        for item in findings
    )
    evidence_gap = (
        "NOT_ASSESSABLE" in criterion_statuses
        or "NOT_ASSESSABLE" in gate_status.values()
        or "NOT_ASSESSABLE" in probe_statuses
        or "NOT_ASSESSABLE" in readiness_statuses
        or "NOT_ASSESSABLE" in parameter_statuses
        or "NOT_ASSESSABLE" in scientific_pattern_statuses
    )
    quality_fail = (
        "FAIL" in criterion_statuses
        or "FAIL" in probe_statuses
        or "NOT_READY" in readiness_statuses
        or "FAIL" in parameter_statuses
        or "FAIL" in scientific_pattern_statuses
    )
    blocking_finding = any(
        item.get("severity") in {"HIGH", "FATAL"} for item in findings
    )
    expected = (
        "REJECT"
        if hard_fail or unrecoverable_fatal or float(total) < 60
        else "NOT_ASSESSABLE"
        if evidence_gap
        else "CONDITIONAL"
        if quality_fail or blocking_finding or float(total) < 80
        else "PASS"
    )
    verdict = value.get("verdict")
    if verdict not in VERDICTS or verdict != expected:
        raise ValueError(f"verdict {verdict!r} is inconsistent; expected {expected}")
    return value


def validate_probe_observations(
    decision: dict[str, Any],
    observation_paths: list[Path],
) -> None:
    """Cross-check Agent probe claims against executed mechanical observations.

    This check deliberately does not infer whether a reward is scientifically
    good or bad. It only prevents a decision from declaring an applicable probe
    PASS/FAIL when the cited probe class was never executed successfully.
    """
    if not observation_paths:
        raise ValueError("at least one --probe-observations file is required")

    by_class: dict[str, list[dict[str, Any]]] = {name: [] for name in PROBES}
    path_labels: set[str] = set()
    for path in observation_paths:
        resolved = path.expanduser().resolve()
        path_labels.update({str(path), str(resolved), path.name})
        try:
            payload = json.loads(resolved.read_text(encoding="utf-8"))
        except Exception as exc:
            raise ValueError(f"cannot read probe observations {path}: {exc}") from exc
        if not isinstance(payload, dict) or not isinstance(
            payload.get("observations"), list
        ):
            raise ValueError(f"probe observations {path} has invalid shape")
        for index, item in enumerate(payload["observations"]):
            if not isinstance(item, dict):
                raise ValueError(
                    f"probe observations {path} item {index} is not an object"
                )
            case_id = _text(
                item.get("case_id"), f"{path}.observations[{index}].case_id"
            )
            probe_class = str(item.get("probe_class") or case_id.split(":", 1)[0])
            if probe_class in by_class:
                by_class[probe_class].append(item)

    probes = decision["checker_probes"]
    for probe_class in sorted(PROBES):
        declared = probes[probe_class]
        declared_status = declared["status"]
        if declared_status == "NOT_APPLICABLE":
            continue

        records = by_class[probe_class]
        if declared_status in {"PASS", "FAIL"}:
            usable = [item for item in records if item.get("status") == "OBSERVED"]
            if not usable:
                statuses = sorted({str(item.get("status")) for item in records}) or [
                    "MISSING"
                ]
                raise ValueError(
                    f"checker_probes.{probe_class} {declared_status} requires an executed "
                    f"OBSERVED case; raw statuses={statuses}"
                )
            cited_case_ids = {str(item["case_id"]) for item in usable}
        else:
            unavailable = [
                item
                for item in records
                if item.get("status") in {"NOT_ASSESSED", "UNUSABLE"}
            ]
            if not unavailable:
                raise ValueError(
                    f"checker_probes.{probe_class} NOT_ASSESSABLE requires a matching "
                    "NOT_ASSESSED or UNUSABLE raw observation"
                )
            cited_case_ids = {str(item["case_id"]) for item in unavailable}

        probe_evidence = [
            item
            for item in declared.get("evidence", [])
            if item.get("source_kind") == "PROBE"
            and any(
                str(item.get("path", "")).endswith(label)
                or label.endswith(str(item.get("path", "")))
                for label in path_labels
            )
        ]
        if not any(
            any(case_id in str(item.get("locator", "")) for case_id in cited_case_ids)
            for item in probe_evidence
        ):
            raise ValueError(
                f"checker_probes.{probe_class} must cite an executed raw case id "
                f"from --probe-observations; available={sorted(cited_case_ids)}"
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("decision", type=Path)
    parser.add_argument(
        "--probe-observations",
        type=Path,
        action="append",
        required=True,
        help="raw checker observation JSON; repeat for builtin and task-specific evidence",
    )
    args = parser.parse_args()
    value = json.loads(args.decision.read_text(encoding="utf-8"))
    validate(value)
    validate_probe_observations(value, args.probe_observations)
    print(
        json.dumps(
            {
                "valid": True,
                "verdict": value["verdict"],
                "weighted_score": value["weighted_score"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
