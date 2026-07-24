#!/usr/bin/env python3
"""Validate Agent-authored materials quality records without inferring science."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

SCHEMA = "materials-agent-final-decision/2.1"
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
DIMENSIONS = {"C01": 10, "C02": 20, "C03": 20, "C04": 20, "C05": 10, "C06": 10, "C07": 10}
HARD_GATES = {
    "NON_MATERIALS_TASK",
    "SCIENTIFIC_TARGET_INVALID",
    "SCIENTIFIC_REASONING_ABSENT",
    "CHECKER_CORE_TASK_UNASSESSED",
    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
}
PROBES = {
    "valid_positive", "missing_output", "empty_output", "malformed_output",
    "random_or_constant", "duplicate_records", "non_finite_values",
    "minimal_exploit", "quality_gradient", "semantic_equivalence",
    "component_isolation",
}
READINESS = {"data", "model", "software", "environment", "license_access"}
STATUSES = {"PASS", "FAIL", "NOT_ASSESSABLE"}
PROBE_STATUSES = STATUSES | {"NOT_APPLICABLE"}
READY_STATUSES = {"READY", "NOT_REQUIRED", "NOT_READY", "NOT_ASSESSABLE"}
VERDICTS = {"PASS", "CONDITIONAL", "REJECT", "NOT_ASSESSABLE"}
DIAGNOSTICS = {"CONFIRMED", "DISMISSED_FALSE_POSITIVE", "AUTOMATION_LIMITATION"}
DISPOSITIONS = {"NONE", "REPAIR", "ABANDON"}
REASONING_FAILURE_MODES = {"PURE_INFORMATION_EXTRACTION", "PURE_ALGEBRAIC_COMPUTATION"}


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
        result.append({key: _text(item.get(key), f"{label}[{index}].{key}") for key in (
            "source_kind", "path", "locator", "quote_or_result"
        )})
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
    if not isinstance(value, list) or any(mode not in REASONING_FAILURE_MODES for mode in value):
        raise ValueError(f"{label} must contain valid failure modes")
    if len(value) != len(set(value)):
        raise ValueError(f"{label} contains duplicates")
    return value


def validate(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("schema_version") != SCHEMA:
        raise ValueError(f"decision schema_version must be {SCHEMA}")
    if value.get("mode") not in {"REVIEW", "REPAIR_REAUDIT"}:
        raise ValueError("mode must be REVIEW or REPAIR_REAUDIT")
    if value.get("reproduction_intent") not in {
        "EXACT_REPRODUCTION", "METHOD_REIMPLEMENTATION", "SCIENTIFIC_EXTENSION"
    }:
        raise ValueError("invalid reproduction_intent")
    _text(value.get("package_id"), "package_id")
    reviewed_scope = value.get("reviewed_scope")
    limitations = value.get("limitations")
    if not isinstance(reviewed_scope, list) or not reviewed_scope:
        raise ValueError("reviewed_scope must be a non-empty list")
    for index, item in enumerate(reviewed_scope):
        _text(item, f"reviewed_scope[{index}]")
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
        if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score) or not 0 <= score <= 100:
            raise ValueError(f"dimension {dim} normalized must be finite 0..100")
        _evidence(item.get("evidence"), f"dimension.{dim}.evidence")
        calculated += DIMENSIONS[dim] * float(score) / 100
    if seen_dimensions != set(DIMENSIONS):
        raise ValueError("dimensions must contain each C01 through C07 once")
    total = value.get("weighted_score")
    if isinstance(total, bool) or not isinstance(total, (int, float)) or abs(float(total) - round(calculated, 2)) > 1e-6:
        raise ValueError(f"weighted_score is inconsistent; expected {round(calculated, 2)}")

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
        modes = _failure_modes(item.get("failure_modes"), f"hard_gates[{index}].failure_modes")
        if code == "SCIENTIFIC_REASONING_ABSENT":
            if record["status"] == "FAIL" and not modes:
                raise ValueError("SCIENTIFIC_REASONING_ABSENT FAIL requires failure_modes")
            if record["status"] != "FAIL" and modes:
                raise ValueError("SCIENTIFIC_REASONING_ABSENT modes require FAIL")
        elif modes:
            raise ValueError(f"hard_gates[{index}].failure_modes is only valid for SCIENTIFIC_REASONING_ABSENT")
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
        raise ValueError("readiness must contain data/model/software/environment/license_access")
    for name in READINESS:
        record = _status_record(readiness[name], READY_STATUSES, f"readiness.{name}")
        resources = record.get("resources")
        if not isinstance(resources, list):
            raise ValueError(f"readiness.{name}.resources must be a list")
        if record["status"] == "READY" and not resources:
            raise ValueError(f"readiness.{name} READY requires resource records")
        for index, resource in enumerate(resources):
            if not isinstance(resource, dict):
                raise ValueError(f"readiness.{name}.resources[{index}] must be an object")
            for field in ("resource_id", "role", "identity_version", "locator", "access_result", "sufficiency", "allowed_alternative"):
                _text(resource.get(field), f"readiness.{name}.resources[{index}].{field}")

    parameters = value.get("parameter_assessment")
    if not isinstance(parameters, dict) or set(parameters) != {"fixed_or_source_required", "solver_selectable"}:
        raise ValueError("parameter_assessment requires fixed_or_source_required and solver_selectable")
    for name in parameters:
        record = _status_record(parameters[name], STATUSES, f"parameter_assessment.{name}")
        if not isinstance(record.get("items"), list):
            raise ValueError(f"parameter_assessment.{name}.items must be a list")

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
        if item.get("severity") not in {"FATAL", "HIGH", "MEDIUM", "LOW"} or item.get("dimension") not in DIMENSIONS:
            raise ValueError(f"open_confirmed_findings[{index}] has invalid severity/dimension")
        if not isinstance(item.get("repairable"), bool) or not isinstance(item.get("hard_gate"), bool):
            raise ValueError(f"open_confirmed_findings[{index}] requires boolean repairable/hard_gate")
        disposition = item.get("disposition")
        if disposition not in {"REPAIR", "ABANDON"}:
            raise ValueError(f"open_confirmed_findings[{index}].disposition is invalid")
        if (disposition == "REPAIR") != item["repairable"]:
            raise ValueError(f"open_confirmed_findings[{index}] disposition conflicts with repairable")
        hard_gate_code = item.get("hard_gate_code")
        if item["hard_gate"]:
            if hard_gate_code not in HARD_GATES:
                raise ValueError(f"open_confirmed_findings[{index}].hard_gate_code is invalid")
        elif hard_gate_code is not None:
            raise ValueError(f"open_confirmed_findings[{index}].hard_gate_code must be null when hard_gate is false")
        modes = _failure_modes(item.get("failure_modes"), f"open_confirmed_findings[{index}].failure_modes")
        if hard_gate_code == "SCIENTIFIC_REASONING_ABSENT":
            if not modes:
                raise ValueError("SCIENTIFIC_REASONING_ABSENT finding requires failure_modes")
        elif modes:
            raise ValueError(f"open_confirmed_findings[{index}].failure_modes is only valid for SCIENTIFIC_REASONING_ABSENT")
        _evidence(item.get("evidence"), f"open_confirmed_findings[{index}].evidence")

    reasoning_gate_failed = gate_status["SCIENTIFIC_REASONING_ABSENT"] == "FAIL"
    if reasoning_gate_failed:
        if gate_disposition["SCIENTIFIC_REASONING_ABSENT"] != "ABANDON":
            raise ValueError("SCIENTIFIC_REASONING_ABSENT FAIL requires disposition ABANDON")
        if criteria["2.3"]["status"] != "FAIL":
            raise ValueError("SCIENTIFIC_REASONING_ABSENT FAIL requires criteria.2.3 FAIL")
        matches = [
            item for item in findings
            if item.get("hard_gate_code") == "SCIENTIFIC_REASONING_ABSENT"
        ]
        if not matches:
            raise ValueError("SCIENTIFIC_REASONING_ABSENT FAIL requires a matching finding")
        for item in matches:
            if item["repairable"] or item["disposition"] != "ABANDON":
                raise ValueError("SCIENTIFIC_REASONING_ABSENT finding must be non-repairable ABANDON")
            if set(item["failure_modes"]) != set(gate_modes["SCIENTIFIC_REASONING_ABSENT"]):
                raise ValueError("SCIENTIFIC_REASONING_ABSENT finding modes must match the Gate")

    criterion_statuses = [criteria[key]["status"] for key in CRITERIA]
    probe_statuses = [probes[name]["status"] for name in PROBES]
    readiness_statuses = [readiness[name]["status"] for name in READINESS]
    parameter_statuses = [parameters[name]["status"] for name in parameters]
    hard_fail = "FAIL" in gate_status.values() or any(item.get("hard_gate") for item in findings)
    unrecoverable_fatal = any(item.get("severity") == "FATAL" and not item.get("repairable") for item in findings)
    evidence_gap = (
        "NOT_ASSESSABLE" in criterion_statuses
        or "NOT_ASSESSABLE" in gate_status.values()
        or "NOT_ASSESSABLE" in probe_statuses
        or "NOT_ASSESSABLE" in readiness_statuses
        or "NOT_ASSESSABLE" in parameter_statuses
    )
    quality_fail = (
        "FAIL" in criterion_statuses
        or "FAIL" in probe_statuses
        or "NOT_READY" in readiness_statuses
        or "FAIL" in parameter_statuses
    )
    blocking_finding = any(item.get("severity") in {"HIGH", "FATAL"} for item in findings)
    expected = (
        "REJECT" if hard_fail or unrecoverable_fatal or float(total) < 60
        else "NOT_ASSESSABLE" if evidence_gap
        else "CONDITIONAL" if quality_fail or blocking_finding or float(total) < 80
        else "PASS"
    )
    verdict = value.get("verdict")
    if verdict not in VERDICTS or verdict != expected:
        raise ValueError(f"verdict {verdict!r} is inconsistent; expected {expected}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("decision", type=Path)
    args = parser.parse_args()
    value = json.loads(args.decision.read_text(encoding="utf-8"))
    validate(value)
    print(json.dumps({"valid": True, "verdict": value["verdict"], "weighted_score": value["weighted_score"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
