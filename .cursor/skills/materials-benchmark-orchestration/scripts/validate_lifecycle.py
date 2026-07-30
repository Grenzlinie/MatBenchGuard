#!/usr/bin/env python3
"""Validate one package lifecycle before queue completion."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
from typing import Any

MATRIX_SCHEMA = "materials-simulation-parameter-matrix/1.0"
SIMULATION_PATTERNS = {
    "SIMULATION_CONTRACT_UNDERDETERMINED",
    "SIMULATION_PARAMETER_DEPENDENCY_BROKEN",
}
PARAMETER_FIELDS = {
    "parameter_id",
    "category",
    "introduced_at",
    "source_status",
    "value_or_rule",
    "depends_on",
    "downstream_consumers",
    "affects_scored_outputs",
    "scoring_sensitive",
    "execution_required",
    "paper_reference_required",
    "resolution",
    "evidence",
}


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load validator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _validators():
    skills = Path(__file__).resolve().parents[2]
    review = _load_module(
        "materials_review_lifecycle",
        skills
        / "materials-benchmark-review/scripts/validate_agent_decision.py",
    )
    repair = _load_module(
        "materials_repair_lifecycle",
        skills
        / "materials-benchmark-repair/scripts/validate_repair_report.py",
    )
    return review, repair


def _json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"cannot read required JSON {path}: {exc}") from exc


def _simulation_matrix_required(decision: dict[str, Any]) -> bool:
    patterns = decision.get("scientific_risk_patterns", {})
    return any(
        patterns.get(pattern_id, {}).get("status") != "NOT_APPLICABLE"
        for pattern_id in SIMULATION_PATTERNS
    )


def _validate_matrix(output: Path, decision: dict[str, Any]) -> None:
    if not _simulation_matrix_required(decision):
        return
    matrix_path = output / "evidence/simulation_parameter_matrix.json"
    matrix = _json(matrix_path)
    if (
        not isinstance(matrix, dict)
        or matrix.get("schema_version") != MATRIX_SCHEMA
        or not isinstance(matrix.get("parameters"), list)
        or not matrix["parameters"]
    ):
        raise ValueError(
            "simulation lifecycle requires a completed "
            "evidence/simulation_parameter_matrix.json"
        )

    matrix_by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(matrix["parameters"]):
        if not isinstance(item, dict) or item.get("bucket") not in decision[
            "parameter_assessment"
        ]:
            raise ValueError(f"simulation parameter matrix item {index} is invalid")
        missing = PARAMETER_FIELDS - set(item)
        if missing:
            raise ValueError(
                f"simulation parameter matrix item {index} lacks "
                + ", ".join(sorted(missing))
            )
        parameter_id = item.get("parameter_id")
        if not isinstance(parameter_id, str) or not parameter_id.strip():
            raise ValueError(f"simulation parameter matrix item {index} has no ID")
        if parameter_id in matrix_by_id:
            raise ValueError(f"duplicate simulation parameter ID: {parameter_id}")
        matrix_by_id[parameter_id] = item

    decision_by_id: dict[str, dict[str, Any]] = {}
    for bucket, record in decision["parameter_assessment"].items():
        for item in record["items"]:
            decision_by_id[item["parameter_id"]] = {**item, "bucket": bucket}
    if set(matrix_by_id) != set(decision_by_id):
        raise ValueError(
            "simulation parameter matrix IDs must match decision parameter_assessment"
        )
    for parameter_id, matrix_item in matrix_by_id.items():
        decision_item = decision_by_id[parameter_id]
        compared_fields = PARAMETER_FIELDS | {"bucket"}
        if any(
            matrix_item.get(field) != decision_item.get(field)
            for field in compared_fields
        ):
            raise ValueError(
                f"simulation parameter {parameter_id} differs between matrix and decision"
            )


def validate_package_lifecycle(output: Path) -> str:
    review_validator, repair_validator = _validators()
    decision_path = output / "agent_final_decision.json"
    decision = _json(decision_path)
    review_validator.validate(decision)
    _validate_matrix(output, decision)

    if decision.get("verdict") == "NOT_ASSESSABLE":
        raise ValueError("NOT_ASSESSABLE must be released, not marked DONE")

    controlling_abandon = any(
        gate.get("status") == "FAIL" and gate.get("disposition") == "ABANDON"
        for gate in decision.get("hard_gates", [])
    ) or any(
        finding.get("hard_gate") and finding.get("disposition") == "ABANDON"
        for finding in decision.get("open_confirmed_findings", [])
    )
    repair_report_path = output / "repair_report.json"
    candidate_path = output / "candidate"

    if controlling_abandon:
        if decision.get("verdict") != "REJECT":
            raise ValueError("controlling ABANDON requires Review verdict REJECT")
        if repair_report_path.exists() or candidate_path.exists():
            raise ValueError(
                "SCREENED_OUT package must not contain candidate or repair_report.json"
            )
        return "SCREENED_OUT"

    if decision.get("verdict") == "PASS":
        if repair_report_path.exists():
            raise ValueError("PASS source decision must not contain a repair report")
        return "PASS"

    repair_findings = [
        finding
        for finding in decision.get("open_confirmed_findings", [])
        if finding.get("disposition") == "REPAIR"
    ]
    if not repair_findings:
        raise ValueError(
            "non-terminal Review requires a REPAIR finding or release for more evidence"
        )
    report = _json(repair_report_path)
    repair_validator.validate(report, report_path=repair_report_path)
    return str(report["outcome"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", help="package id relative to QA_ROOT")
    args = parser.parse_args()
    root = Path(os.environ.get("QA_ROOT", "/personal/qa_review"))
    state = validate_package_lifecycle(root / args.package)
    print(json.dumps({"valid": True, "lifecycle_state": state}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
