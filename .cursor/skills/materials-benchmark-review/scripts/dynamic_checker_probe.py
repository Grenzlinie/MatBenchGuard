#!/usr/bin/env python3
"""Execute isolated E1 submissions against the real Harbor checker."""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import math
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from prepare_audit_output import (
    QUALITY_EVIDENCE_ROLES,
    basename,
    locate_root,
    sha256_file,
)


ORACLE_VENV_TIMEOUT_SECONDS = 60.0
ORACLE_SOLVE_TIMEOUT_SECONDS = 300.0
NEGATIVE_PROBE_CASES = frozenset(
    {
        "missing_outputs",
        "empty_valid_shape",
        "malformed_outputs",
        "random_baseline",
        "minimal_gold_shape",
        "duplicate_gold_rows",
        "nonfinite_values",
        "sparse_known_valid",
    }
)
FIXTURE_MANIFEST_NAME = "fixture_manifest.json"
FIXTURE_MANIFEST_SCHEMA = "materials-known-valid-fixture/1.0"
FORBIDDEN_FIXTURE_PARTS = {
    "solution",
    "tests",
    "paper",
    "benchmark_audit",
    "benchmark_audit_history",
    ".benchmark_audit_tmp",
}
TASK_FAMILY_CASES = {
    "materials_constant_or_all_zero": "constant_or_all_zero",
    "materials_all_positive": "all_positive_or_negative",
    "materials_all_negative": "all_positive_or_negative",
    "materials_conflicting_records": "conflicting_or_irrelevant_records",
    "materials_threshold_boundary": "threshold_boundary",
    "materials_unit_error": "unit_error",
    "materials_element_phase_error": "element_or_phase_error",
    "materials_coordinate_lattice_error": "coordinate_or_lattice_error",
    "materials_duplicate_structure": "duplicate_structure",
    "materials_wrong_objective_endpoint": "wrong_objective_or_endpoint",
    "materials_missing_core_model": "missing_core_model",
}
TASK_FAMILY_MODES = {
    "materials_constant_or_all_zero": "constant_zero",
    "materials_all_positive": "all_positive",
    "materials_all_negative": "all_negative",
    "materials_conflicting_records": "conflict",
    "materials_threshold_boundary": "threshold",
    "materials_unit_error": "unit_error",
    "materials_element_phase_error": "element_phase_error",
    "materials_coordinate_lattice_error": "coordinate_lattice_error",
    "materials_duplicate_structure": "duplicate_structure",
    "materials_wrong_objective_endpoint": "wrong_endpoint",
    "materials_missing_core_model": "missing_core_model",
}
TASK_FAMILY_ATTACKS = (
    "constant_or_all_zero",
    "all_positive_or_negative",
    "conflicting_or_irrelevant_records",
    "threshold_boundary",
    "unit_error",
    "element_or_phase_error",
    "coordinate_or_lattice_error",
    "duplicate_structure",
    "wrong_objective_or_endpoint",
    "missing_core_model",
)


def configured_timeout(name: str, default: float) -> float:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        value = float(raw)
    except ValueError:
        return default
    return value if value > 0 else default


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def grading_steps(specification: dict[str, Any]) -> list[dict[str, Any]]:
    return specification.get("steps", specification.get("checks", [])) or []


def matching_step(
    specification: dict[str, Any], filename: str
) -> dict[str, Any] | None:
    for step in grading_steps(specification):
        if basename(step.get("output_file")) == filename:
            return step
    return None


def table_value(column: str, mode: str) -> Any:
    normalized = column.lower()
    if normalized == "direction":
        return "100"
    if normalized == "mode":
        return "L"
    if mode == "nonfinite":
        return "nan"
    if mode == "random":
        return random.uniform(-1000, 1000)
    if mode in {"all_positive", "unit_error"}:
        return 1000.0 if mode == "unit_error" else 1.0
    if mode == "all_negative":
        return -1.0
    if mode in {
        "constant_zero",
        "conflict",
        "threshold",
        "element_phase_error",
        "coordinate_lattice_error",
        "wrong_endpoint",
    }:
        if normalized in {"element", "species", "phase", "material"}:
            return "wrong_phase"
        if normalized in {"x", "y", "z", "a", "b", "c", "lattice"}:
            return 999.0
        return 0.0
    return 0


def write_synthetic_outputs(
    output_dir: Path, specification: dict[str, Any], mode: str
) -> list[str]:
    created: list[str] = []
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    for output in outputs:
        filename = basename(output.get("file"))
        if not filename:
            continue
        if mode == "missing_core_model":
            continue
        path = output_dir / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        output_format = str(output.get("format", "")).lower()
        schema = output.get("schema", {}) or {}
        step = matching_step(specification, filename)
        if output_format == "json":
            required = schema.get("required", {}) or {}
            fields = (
                list(required.keys())
                if isinstance(required, dict)
                else list(required)
            )
            value = {
                field: (
                    float("nan")
                    if mode == "nonfinite"
                    else random.uniform(-1000, 1000)
                    if mode == "random"
                    else table_value(field, mode)
                    if mode
                    in {
                        "constant_zero",
                        "all_positive",
                        "all_negative",
                        "threshold",
                        "unit_error",
                        "element_phase_error",
                        "coordinate_lattice_error",
                        "wrong_endpoint",
                    }
                    else (step or {}).get("target_value", 0)
                )
                for field in fields
            }
            path.write_text(
                json.dumps(value, allow_nan=True), encoding="utf-8"
            )
        elif output_format in {"csv", "tsv"}:
            raw_columns = schema.get("required_columns", []) or []
            columns = [
                item.get("name") if isinstance(item, dict) else str(item)
                for item in raw_columns
            ]
            delimiter = "\t" if output_format == "tsv" else ","
            rows: list[dict[str, Any]] = []
            if mode in {
                "random",
                "minimal",
                "nonfinite",
                "duplicate",
                "constant_zero",
                "all_positive",
                "all_negative",
                "conflict",
                "threshold",
                "unit_error",
                "element_phase_error",
                "coordinate_lattice_error",
                "duplicate_structure",
                "wrong_endpoint",
            }:
                rows = [
                    {
                        column: table_value(column, mode)
                        for column in columns
                    }
                ]
                if mode in {"duplicate", "duplicate_structure"}:
                    rows *= 2
                elif mode == "conflict" and rows:
                    conflicting = dict(rows[0])
                    candidate = next(
                        (
                            column
                            for column in reversed(columns)
                            if isinstance(conflicting.get(column), (int, float))
                        ),
                        None,
                    )
                    if candidate is not None:
                        conflicting[candidate] = 1.0
                    rows.append(conflicting)
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle, fieldnames=columns, delimiter=delimiter
                )
                writer.writeheader()
                writer.writerows(rows)
        else:
            path.write_text(
                "" if mode == "empty" else "synthetic\n", encoding="utf-8"
            )
        created.append(filename)
    return created


def write_malformed_outputs(
    output_dir: Path, specification: dict[str, Any]
) -> list[str]:
    created: list[str] = []
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    for output in outputs:
        filename = basename(output.get("file"))
        if not filename:
            continue
        path = output_dir / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        output_format = str(output.get("format", "")).lower()
        if output_format == "json":
            path.write_text('{"malformed": ', encoding="utf-8")
        elif output_format in {"csv", "tsv"}:
            path.write_text("\x00not_the_required_schema\n", encoding="utf-8")
        else:
            path.write_bytes(b"\x00\xffmalformed")
        created.append(filename)
    return created


def reject_package_fixture(root: Path, source_dir: Path) -> Path:
    source_dir = source_dir.expanduser().resolve()
    root = root.resolve()
    if source_dir == root or source_dir.is_relative_to(root):
        raise ValueError(
            "known-valid fixture must be external to every Harbor package role"
        )
    if any(part in FORBIDDEN_FIXTURE_PARTS for part in source_dir.parts):
        raise ValueError(
            "known-valid fixture must be external to package and audit roles"
        )
    for ancestor in (source_dir, *source_dir.parents):
        if (
            (ancestor / "instruction.md").is_file()
            and (ancestor / "tests").is_dir()
        ):
            raise ValueError(
                "known-valid fixture cannot be nested under another Harbor package"
            )
    if not source_dir.is_dir():
        raise ValueError(f"known-valid output is not a directory: {source_dir}")
    return source_dir


def fixture_hashes(
    fixture: Path, specification: dict[str, Any]
) -> dict[str, str]:
    hashes: dict[str, str] = {}
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    for output in outputs:
        filename = basename(output.get("file"))
        path = fixture / filename
        if (
            not filename
            or path.parent != fixture
            or not path.is_file()
            or path.is_symlink()
        ):
            raise ValueError(
                "known-valid fixture requires a regular contracted file: "
                f"{filename}"
            )
        hashes[filename] = sha256_file(path)
    return hashes


def validate_known_valid_fixture(
    root: Path,
    source_dir: Path,
    specification: dict[str, Any],
) -> dict[str, Any]:
    """Require an external public fixture bound to current quality sources."""
    fixture = reject_package_fixture(root, source_dir)
    manifest_path = fixture / FIXTURE_MANIFEST_NAME
    if not manifest_path.is_file() or manifest_path.is_symlink():
        raise ValueError(
            f"known-valid fixture manifest is missing: {FIXTURE_MANIFEST_NAME}"
        )
    manifest = read_json(manifest_path)
    if not isinstance(manifest, dict):
        raise ValueError("known-valid fixture manifest must be an object")
    current_source_hashes = {
        role: sha256_file(root / role)
        for role in sorted(QUALITY_EVIDENCE_ROLES)
        if (root / role).is_file()
    }
    current_fixture_hashes = fixture_hashes(fixture, specification)
    if (
        manifest.get("schema_version") != FIXTURE_MANIFEST_SCHEMA
        or manifest.get("source_kind") != "INDEPENDENT_PUBLIC_FIXTURE"
        or manifest.get("public") is not True
        or manifest.get("oracle_used") is not False
        or manifest.get("source_role_hashes") != current_source_hashes
        or manifest.get("fixture_hashes") != current_fixture_hashes
    ):
        raise ValueError(
            "known-valid fixture manifest is not source-bound and immutable"
        )
    return {
        "source_kind": "INDEPENDENT_PUBLIC_FIXTURE",
        "public": True,
        "oracle_used": False,
        "fixture_hashes": current_fixture_hashes,
        "source_role_hashes": current_source_hashes,
        "fixture_manifest_hash": sha256_file(manifest_path),
    }


def copy_known_valid_outputs(
    root: Path,
    source_dir: Path,
    output_dir: Path,
    specification: dict[str, Any],
) -> list[str]:
    source_dir = reject_package_fixture(root, source_dir)
    created: list[str] = []
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    for output in outputs:
        filename = basename(output.get("file"))
        if not filename:
            continue
        source = (source_dir / filename).resolve()
        if source.parent != source_dir or not source.is_file():
            raise FileNotFoundError(
                f"known-valid output is missing contracted file: {filename}"
            )
        destination = output_dir / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        created.append(filename)
    return created


def component_isolation_plan(
    specification: dict[str, Any],
    source_dir: Path | None,
    checker_text: str,
) -> tuple[list[dict[str, str]], str | None]:
    """Build only source-bound isolation cases; never synthesize valid values."""
    if source_dir is None:
        return [], "no independent source-bound fixture is available"
    try:
        tree = ast.parse(checker_text)
    except SyntaxError as exc:
        return [], f"checker source cannot be parsed: {exc}"
    functions = {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    scorer_bindings: dict[str, str] = {}
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if not any(
            isinstance(target, ast.Name) and target.id == "_SCORERS"
            for target in targets
        ) or not isinstance(node.value, ast.Dict):
            continue
        current_bindings: dict[str, str] = {}
        for key, value in zip(node.value.keys, node.value.values):
            if (
                isinstance(key, ast.Constant)
                and isinstance(key.value, str)
                and isinstance(value, ast.Name)
            ):
                current_bindings[key.value] = value.id
        scorer_bindings = current_bindings
    contract_files = {
        basename(item.get("file"))
        for item in (
            (specification.get("output_contract", {}) or {}).get("outputs", [])
            or []
        )
        if basename(item.get("file"))
    }
    candidates: list[dict[str, str]] = []
    seen_files: set[str] = set()
    for step in grading_steps(specification):
        filename = basename(step.get("output_file"))
        step_id = str(step.get("id") or filename)
        weight = finite_number(step.get("weight"))
        if (
            not filename
            or filename in seen_files
            or filename not in contract_files
            or weight is None
            or weight <= 0
            or step_id not in scorer_bindings
            or scorer_bindings[step_id] not in functions
        ):
            continue
        seen_files.add(filename)
        candidates.append(
            {
                "step_id": step_id,
                "file": filename,
                "scorer_function": scorer_bindings[step_id],
            }
        )
    if len(candidates) < 2:
        return [], (
            "fewer than two distinct positive-weight contracted components "
            "have verified checker source bindings"
        )
    missing = [
        item["file"]
        for item in candidates
        if not (source_dir / item["file"]).is_file()
    ]
    if missing:
        return [], "positive fixture lacks component files: " + ", ".join(missing)
    return candidates, None


def component_isolation_coverage(
    plan: list[dict[str, str]],
    not_run_reason: str | None,
    results: list[dict[str, Any]],
) -> dict[str, Any]:
    provenance: dict[str, Any] = {
        "source_kind": "INDEPENDENT_PUBLIC_FIXTURE" if plan else "NONE",
        "oracle_used": False,
        "source_bindings_verified": bool(plan),
        "runtime_bindings_verified": False,
        "cases_planned": len(plan),
        "cases_executed": 0,
    }
    if not plan:
        return {
            "status": "NOT_RUN",
            "reason": not_run_reason
            or "component isolation could not be planned safely",
            "provenance": provenance,
        }
    isolation_results = [
        result
        for result in results
        if result["case"].startswith("component_isolation__")
    ]
    provenance["cases_executed"] = len(isolation_results)
    runtime_bound = component_runtime_bindings_verified(plan, results)
    cases_usable = (
        len(isolation_results) == len(plan)
        and all(
            usable_probe_result(result)
            for result in isolation_results
        )
    )
    provenance["runtime_bindings_verified"] = bool(
        runtime_bound and cases_usable
    )
    if provenance["runtime_bindings_verified"]:
        return {
            "status": "ASSESSED",
            "reason": None,
            "provenance": provenance,
        }
    return {
        "status": "NOT_ASSESSABLE",
        "reason": (
            "component-isolation runtime scorer bindings or case rewards "
            "could not be verified"
        ),
        "provenance": provenance,
    }


def component_runtime_bindings_verified(
    plan: list[dict[str, str]], results: list[dict[str, Any]]
) -> bool:
    public_fixture = next(
        (
            result
            for result in results
            if result["case"] == "known_valid_public"
        ),
        None,
    )
    breakdown = (
        public_fixture.get("breakdown")
        if isinstance(public_fixture, dict)
        else None
    )
    return bool(
        isinstance(public_fixture, dict)
        and usable_probe_result(public_fixture)
        and isinstance(breakdown, dict)
        and all(
            isinstance(breakdown.get(component["step_id"]), dict)
            and finite_number(
                breakdown[component["step_id"]].get("score")
            )
            is not None
            for component in plan
        )
    )


def usable_probe_result(result: Any) -> bool:
    if not isinstance(result, dict) or result.get("crashed"):
        return False
    reward = result.get("reward")
    breakdown = result.get("breakdown")
    if (
        not isinstance(reward, float)
        or not math.isfinite(reward)
        or not isinstance(breakdown, dict)
    ):
        return False
    errors = breakdown.get("_errors", {})
    return isinstance(errors, dict) and not errors


def probe_assessment_flags(
    results: list[dict[str, Any]],
) -> dict[str, bool]:
    by_case = {result["case"]: result for result in results}
    positive_cases = ["positive_oracle"] if "positive_oracle" in by_case else []
    negative_cases = [
        result
        for result in results
        if result["case"] in NEGATIVE_PROBE_CASES
    ]
    discrimination_cases = (
        "known_valid_public",
        "quality_gradient_small_error",
        "quality_gradient_large_error",
    )
    equivalence_cases = (
        "known_valid_public",
        "metamorphic_equivalent_representation",
    )
    return {
        "positive": any(
            usable_probe_result(by_case[case]) for case in positive_cases
        ),
        "negative": bool(negative_cases)
        and all(usable_probe_result(result) for result in negative_cases),
        "discrimination": all(
            case in by_case and usable_probe_result(by_case[case])
            for case in discrimination_cases
        ),
        "equivalence": all(
            case in by_case and usable_probe_result(by_case[case])
            for case in equivalence_cases
        ),
    }


def task_family_attack_coverage(
    results: list[dict[str, Any]],
    pass_threshold: float,
    applicability: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    by_case = {result["case"]: result for result in results}
    coverage: dict[str, Any] = {}
    for attack in TASK_FAMILY_ATTACKS:
        applicability_entry = applicability[attack]
        if not applicability_entry["applicable"]:
            coverage[attack] = {
                "status": "NOT_APPLICABLE",
                "reason": applicability_entry["reason"],
                "provenance": {
                    "source_kind": "INSTRUCTION_CONTRACT_CLASSIFICATION",
                    "oracle_used": False,
                    "cases": [],
                    "modes": [],
                },
            }
            continue
        cases = [
            case
            for case, declared_attack in TASK_FAMILY_CASES.items()
            if declared_attack == attack
        ]
        attack_results = [by_case[case] for case in cases if case in by_case]
        provenance = {
            "source_kind": "SCHEMA_SHAPED_SYNTHETIC_ATTACKS",
            "oracle_used": False,
            "cases": cases,
            "modes": [TASK_FAMILY_MODES[case] for case in cases],
        }
        if len(attack_results) != len(cases):
            coverage[attack] = {
                "status": "NOT_ASSESSABLE",
                "reason": "task-family attack was not executed",
                "provenance": provenance,
            }
            continue
        if all(usable_probe_result(result) for result in attack_results):
            coverage[attack] = {
                "status": "ASSESSED",
                "reason": (
                    "checker returned a usable result for the declared "
                    "materials attack"
                ),
                "provenance": {
                    **provenance,
                    "rewards": {
                        result["case"]: result.get("reward")
                        for result in attack_results
                    },
                    "pass_threshold": pass_threshold,
                },
            }
        else:
            coverage[attack] = {
                "status": "NOT_ASSESSABLE",
                "reason": "checker result was not usable",
                "provenance": provenance,
            }
    return coverage


def task_family_applicability(
    root: Path, specification: dict[str, Any]
) -> dict[str, dict[str, Any]]:
    instruction = (root / "instruction.md").read_text(
        encoding="utf-8", errors="replace"
    )
    contract_map = instruction_contract_map(instruction)
    core_requirements = [
        requirement
        for requirement in contract_map.get("requirements", [])
        if any(
            declaration.get("role_classification") == "CORE_OUTPUT"
            for declaration in requirement.get("evidence", [])
        )
    ]
    grading_outputs = [
        output
        for output in (
            (specification.get("output_contract", {}) or {}).get("outputs", [])
            or []
        )
        if not str(output.get("purpose") or "").lower().startswith(
            ("process", "intermediate", "diagnostic")
        )
    ]
    grading_outputs.extend(
        {
            "file": basename(step.get("output_file")),
            "step_id": step.get("id"),
            "weight": step.get("weight"),
        }
        for step in grading_steps(specification)
        if basename(step.get("output_file"))
        and step.get("weight", 1) != 0
    )
    context = (
        json.dumps(core_requirements, ensure_ascii=False)
        + "\n"
        + json.dumps(
            sorted(contract_map.get("core_outputs", [])),
            ensure_ascii=False,
        )
        + "\n"
        + json.dumps(grading_outputs, ensure_ascii=False)
    ).lower()
    specialized = {
        "element_or_phase_error": (
            ("element", "species", "phase", "composition"),
            "the public contract has no element, species, phase, or composition field",
        ),
        "coordinate_or_lattice_error": (
            ("coordinate", "lattice", "geometry", "position", "cif", "poscar"),
            "the public contract has no coordinate, lattice, or structure field",
        ),
        "duplicate_structure": (
            ("structure", "geometry", "cif", "poscar"),
            "the public contract does not submit structures",
        ),
        "missing_core_model": (
            ("model", "structure", "trajectory", "prediction field"),
            "the public contract does not submit a load-bearing model artifact",
        ),
    }
    applicability: dict[str, dict[str, Any]] = {}
    for attack in TASK_FAMILY_ATTACKS:
        if attack not in specialized:
            applicability[attack] = {"applicable": True, "reason": None}
            continue
        terms, reason = specialized[attack]
        applicability[attack] = {
            "applicable": any(term in context for term in terms),
            "reason": (
                None if any(term in context for term in terms) else reason
            ),
        }
    return applicability


def retain_one_known_valid_row(
    output_dir: Path, specification: dict[str, Any]
) -> None:
    """Turn a public valid table into a sparse but value-correct submission."""
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    for output in outputs:
        output_format = str(output.get("format", "")).lower()
        if output_format not in {"csv", "tsv"}:
            continue
        path = output_dir / basename(output.get("file"))
        delimiter = "\t" if output_format == "tsv" else ","
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle, delimiter=delimiter))
        if not rows:
            continue
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle, fieldnames=list(rows[-1]), delimiter=delimiter
            )
            writer.writeheader()
            writer.writerow(rows[-1])


def finite_number(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def response_column(
    fieldnames: list[str], rows: list[dict[str, Any]]
) -> str | None:
    numeric = [
        field
        for field in fieldnames
        if any(finite_number(row.get(field)) is not None for row in rows)
    ]
    if not numeric:
        return None
    coordinate_names = {
        "id",
        "index",
        "step",
        "iteration",
        "frame",
        "time",
        "x",
        "y",
        "z",
        "k",
        "q",
    }
    responses = [
        field for field in numeric if field.strip().lower() not in coordinate_names
    ]
    return (responses or numeric)[-1]


def perturb_json(value: Any, fraction: float) -> Any:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
        number = float(value)
        return number + fraction * max(abs(number), 1.0)
    if isinstance(value, list):
        return [perturb_json(item, fraction) for item in value]
    if isinstance(value, dict):
        return {
            key: perturb_json(item, fraction)
            for key, item in value.items()
        }
    return value


def transform_known_valid_outputs(
    output_dir: Path,
    specification: dict[str, Any],
    mode: str,
) -> list[dict[str, Any]]:
    transformations: list[dict[str, Any]] = []
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    for output in outputs:
        filename = basename(output.get("file"))
        if not filename:
            continue
        path = output_dir / filename
        output_format = str(output.get("format", "")).lower()
        if output_format in {"csv", "tsv"}:
            delimiter = "\t" if output_format == "tsv" else ","
            with path.open(newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle, delimiter=delimiter)
                fieldnames = list(reader.fieldnames or [])
                rows = list(reader)
            detail: dict[str, Any] = {
                "file": filename,
                "format": output_format,
            }
            if mode == "metamorphic":
                rows.reverse()
                fieldnames.reverse()
                detail["operation"] = "reverse_rows_and_columns"
            else:
                column = response_column(fieldnames, rows)
                fraction = 0.05 if mode == "quality_small" else 0.5
                changed = 0
                if column is not None:
                    for row in rows:
                        number = finite_number(row.get(column))
                        if number is None:
                            continue
                        row[column] = f"{number + fraction * max(abs(number), 1.0):.12g}"
                        changed += 1
                detail.update(
                    {
                        "operation": "perturb_numeric_materials_response",
                        "response_column": column,
                        "fraction": fraction,
                        "changed_values": changed,
                    }
                )
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle, fieldnames=fieldnames, delimiter=delimiter
                )
                writer.writeheader()
                writer.writerows(rows)
            transformations.append(detail)
        elif output_format == "json":
            value = read_json(path)
            if mode == "metamorphic":
                operation = "canonical_key_order_and_indentation"
                transformed = value
            else:
                fraction = 0.05 if mode == "quality_small" else 0.5
                operation = "perturb_numeric_materials_response"
                transformed = perturb_json(value, fraction)
            path.write_text(
                json.dumps(
                    transformed,
                    indent=4 if mode == "metamorphic" else None,
                    sort_keys=mode == "metamorphic",
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            transformations.append(
                {
                    "file": filename,
                    "format": output_format,
                    "operation": operation,
                    **(
                        {}
                        if mode == "metamorphic"
                        else {"fraction": fraction}
                    ),
                }
            )
    return transformations


def copy_public_package(root: Path, destination: Path) -> None:
    """Copy only instruction/tests into the isolated checker runtime."""
    destination.mkdir(parents=True, exist_ok=True)
    instruction = root / "instruction.md"
    if instruction.is_file():
        shutil.copy2(instruction, destination / "instruction.md")
    if (root / "tests").is_dir():
        shutil.copytree(root / "tests", destination / "tests")


def patch_harbor_paths(
    text: str,
    tests_dir: Path,
    outputs_dir: Path,
    logs_dir: Path,
) -> str:
    """Run the Harbor verifier entrypoint against an isolated host copy."""
    replacements = {
        "/tests/grading_spec.json": str(tests_dir / "grading_spec.json"),
        "/tests/": str(tests_dir) + os.sep,
        "/tests": str(tests_dir),
        "/app/outputs": str(outputs_dir),
        "/logs/verifier": str(logs_dir),
    }
    pattern = re.compile(
        r"/tests/grading_spec\.json|/app/outputs|/logs/verifier|/tests/|/tests"
    )
    return pattern.sub(lambda match: replacements[match.group(0)], text)


def audit_host_dependency_failure(stdout: str, stderr: str) -> str | None:
    """Return a reason when the audit host cannot provide verifier dependencies."""
    combined = f"{stdout}\n{stderr}".lower()
    patterns = (
        "modulenotfounderror",
        "no module named",
        "command not found",
        "cannot import name",
        "could not find a version that satisfies",
        "unable to locate package",
        "temporary failure resolving",
        "could not resolve host",
        "network is unreachable",
    )
    if any(pattern in combined for pattern in patterns):
        return (
            "The Harbor verifier entrypoint could not run on the audit host "
            "because a runtime dependency was unavailable; this is not a "
            "package defect."
        )
    return None


def rebase_oracle_mount_paths(solution: Path, outputs: Path) -> None:
    """Map canonical Harbor mounts into the disposable Oracle workspace."""
    replacements = {
        "/app/outputs": str(outputs),
        "/solution": str(solution),
    }
    for path in solution.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rebased = text
        for canonical, replacement in replacements.items():
            rebased = re.sub(
                re.escape(canonical) + r"(?=$|[/\"'\s])",
                lambda _match: replacement,
                rebased,
            )
        if rebased != text:
            path.write_text(rebased, encoding="utf-8")


def prepare_solution_oracle(
    root: Path,
    specification: dict[str, Any],
) -> tuple[tempfile.TemporaryDirectory[str] | None, Path | None, dict[str, Any]]:
    solve_script = root / "solution/solve.sh"
    if not solve_script.is_file():
        return (
            None,
            None,
            {
                "used": False,
                "status": "MISSING",
                "positive_mock_available": False,
                "attempted": False,
                "setup_attempted": False,
                "setup_prepared": False,
                "producer_started": False,
                "executed": False,
                "scientific_evidence": False,
            },
        )
    temporary: tempfile.TemporaryDirectory[str] | None = None
    outputs: Path | None = None
    attempted = True
    setup_attempted = False
    setup_prepared = False
    producer_started = False
    executed = False
    returncode: int | None = None
    failure_stage: str | None = None
    failure_reason: str | None = None
    timeout_seconds: float | None = None
    current_stage = "setup"
    venv_timeout = configured_timeout(
        "MATERIALS_ORACLE_VENV_TIMEOUT_SECONDS",
        ORACLE_VENV_TIMEOUT_SECONDS,
    )
    solve_timeout = configured_timeout(
        "MATERIALS_ORACLE_SOLVE_TIMEOUT_SECONDS",
        ORACLE_SOLVE_TIMEOUT_SECONDS,
    )
    try:
        setup_attempted = True
        temporary = tempfile.TemporaryDirectory(prefix="materials_oracle_")
        runtime = Path(temporary.name) / "package"
        copy_public_package(root, runtime)
        runtime_solution = runtime / "solution"
        shutil.copytree(root / "solution", runtime_solution)
        outputs = Path(temporary.name) / "outputs"
        outputs.mkdir()
        rebase_oracle_mount_paths(runtime_solution, outputs)
        virtualenv = Path(temporary.name) / "venv"
        current_stage = "venv"
        subprocess.run(
            [sys.executable, "-m", "venv", str(virtualenv)],
            capture_output=True,
            text=True,
            timeout=venv_timeout,
            check=True,
        )
        setup_prepared = True
        environment = {
            **os.environ,
            "OUTPUT_DIR": str(outputs),
            "PATH": str(virtualenv / "bin")
            + os.pathsep
            + os.environ.get("PATH", ""),
        }
        current_stage = "solve"
        process = subprocess.run(
            ["bash", str(runtime_solution / "solve.sh")],
            cwd=runtime,
            env=environment,
            capture_output=True,
            text=True,
            timeout=solve_timeout,
            check=False,
        )
        producer_started = True
        executed = True
        returncode = process.returncode
        if returncode != 0:
            failure_stage = "solve"
            failure_reason = "NONZERO_EXIT"
    except subprocess.TimeoutExpired:
        failure_stage = current_stage
        failure_reason = "TIMEOUT"
        timeout_seconds = (
            venv_timeout if failure_stage == "venv" else solve_timeout
        )
        if current_stage == "solve":
            producer_started = True
            executed = True
    except subprocess.CalledProcessError:
        failure_stage = current_stage
        failure_reason = "NONZERO_EXIT"
    except (subprocess.SubprocessError, OSError):
        failure_stage = (
            "producer_launch" if current_stage == "solve" else current_stage
        )
        failure_reason = "PROCESS_ERROR"
    contracted = [
        basename(item.get("file"))
        for item in (
            (specification.get("output_contract", {}) or {}).get("outputs", [])
            or []
        )
        if basename(item.get("file"))
    ]
    available = bool(
        executed
        and returncode == 0
        and outputs is not None
        and all((outputs / filename).is_file() for filename in contracted)
    )
    if (
        executed
        and returncode == 0
        and not available
        and failure_stage is None
    ):
        failure_stage = "output_collection"
        failure_reason = "CONTRACTED_OUTPUTS_MISSING"
    return (
        temporary,
        outputs if available else None,
        {
            "used": attempted,
            "status": "PASS" if available else "BROKEN",
            "positive_mock_available": available,
            "attempted": attempted,
            "setup_attempted": setup_attempted,
            "setup_prepared": setup_prepared,
            "producer_started": producer_started,
            "executed": executed,
            "returncode": returncode,
            **(
                {
                    "failure_stage": failure_stage,
                    "failure_reason": failure_reason,
                    **(
                        {"timeout_seconds": timeout_seconds}
                        if timeout_seconds is not None
                        else {}
                    ),
                }
                if not available and failure_stage is not None
                else {}
            ),
            "scientific_evidence": False,
        },
    )


def run_checker_case(
    root: Path,
    checker_text: str,
    specification: dict[str, Any],
    case_name: str,
    mode: str,
    known_valid_output: Path | None,
    isolated_component: dict[str, str] | None = None,
    fixture_source_kind: str | None = None,
) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix=f"materials_checker_{case_name}_") as tmp:
        base = Path(tmp)
        package_dir = base / "package"
        tests_dir = base / "tests"
        outputs_dir = base / "app" / "outputs"
        logs_dir = base / "logs" / "verifier"
        copy_public_package(root, package_dir)
        shutil.copytree(root / "tests", tests_dir)
        outputs_dir.mkdir(parents=True)
        logs_dir.mkdir(parents=True)
        specification_path = tests_dir / "grading_spec.json"
        specification_path.write_text(
            json.dumps(specification, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        created: list[str] = []
        transformations: list[dict[str, Any]] = []
        known_valid_modes = {
            "known_valid",
            "sparse_known_valid",
            "quality_small",
            "quality_large",
            "metamorphic",
            "component_isolation",
        }
        if mode in known_valid_modes:
            if known_valid_output is None:
                raise ValueError("known-valid case requires an output directory")
            created = copy_known_valid_outputs(
                root, known_valid_output, outputs_dir, specification
            )
            if mode == "sparse_known_valid":
                retain_one_known_valid_row(outputs_dir, specification)
            elif mode in {"quality_small", "quality_large", "metamorphic"}:
                transformations = transform_known_valid_outputs(
                    outputs_dir, specification, mode
                )
            elif mode == "component_isolation":
                if isolated_component is None:
                    raise ValueError("component isolation requires a component")
                retained = isolated_component["file"]
                for filename in created:
                    if filename != retained:
                        (outputs_dir / filename).unlink(missing_ok=True)
                created = [filename for filename in created if filename == retained]
        elif mode == "malformed":
            created = write_malformed_outputs(outputs_dir, specification)
        elif mode != "missing":
            created = write_synthetic_outputs(
                outputs_dir, specification, mode
            )

        patched = patch_harbor_paths(
            checker_text, tests_dir, outputs_dir, logs_dir
        )
        checker_path = tests_dir / "checker.py"
        checker_path.write_text(patched, encoding="utf-8")
        verifier_source = root / "tests/test.sh"
        verifier_path = base / "test.sh"
        runtime_provenance = "audit-host-copy"
        if not verifier_source.is_file():
            return {
                "case": case_name,
                "mode": mode,
                "created_outputs": created,
                "transformations": transformations,
                "returncode": None,
                "reward": None,
                "breakdown": None,
                "stdout": "",
                "stderr": "tests/test.sh is missing",
                "crashed": False,
                "runtime_not_assessable": True,
                "runtime_not_assessable_reason": (
                    "Harbor verifier entrypoint tests/test.sh is missing."
                ),
                "runtime_provenance": "not-assessable",
                "verifier_entrypoint": "tests/test.sh",
                "direct_checker_harness": False,
                "runtime_package_contains_solution": (
                    package_dir / "solution"
                ).exists(),
                "isolated_component": isolated_component,
                "fixture_source_kind": fixture_source_kind,
            }
        verifier_path.write_text(
            patch_harbor_paths(
                verifier_source.read_text(encoding="utf-8", errors="replace"),
                tests_dir,
                outputs_dir,
                logs_dir,
            ),
            encoding="utf-8",
        )
        tool_dir = base / "bin"
        tool_dir.mkdir()
        (tool_dir / "python").symlink_to(sys.executable)
        runtime_environment = {
            **os.environ,
            "PATH": str(tool_dir)
            + os.pathsep
            + os.environ.get("PATH", ""),
        }
        process = subprocess.run(
            ["/bin/bash", str(verifier_path)],
            cwd=package_dir,
            env=runtime_environment,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
        dependency_failure = (
            audit_host_dependency_failure(process.stdout, process.stderr)
            if process.returncode != 0
            else None
        )
        reward: float | str | None = None
        reward_path = logs_dir / "reward.txt"
        if reward_path.exists():
            raw_reward = reward_path.read_text(
                encoding="utf-8", errors="replace"
            ).strip()
            try:
                reward = float(raw_reward)
            except ValueError:
                reward = raw_reward
        breakdown: Any = None
        breakdown_path = logs_dir / "breakdown.json"
        if breakdown_path.exists():
            try:
                breakdown = read_json(breakdown_path)
            except json.JSONDecodeError:
                breakdown = breakdown_path.read_text(
                    encoding="utf-8", errors="replace"
                )
        return {
            "case": case_name,
            "mode": mode,
            "created_outputs": created,
            "transformations": transformations,
            "returncode": process.returncode,
            "reward": reward,
            "breakdown": breakdown,
            "stdout": process.stdout[-4000:],
            "stderr": process.stderr[-4000:],
            "crashed": process.returncode != 0 and dependency_failure is None,
            "runtime_not_assessable": dependency_failure is not None,
            "runtime_not_assessable_reason": dependency_failure,
            "runtime_provenance": (
                "not-assessable"
                if dependency_failure is not None
                else runtime_provenance
            ),
            "verifier_entrypoint": "tests/test.sh",
            "direct_checker_harness": False,
            "runtime_package_contains_solution": (
                package_dir / "solution"
            ).exists(),
            "isolated_component": isolated_component,
            "fixture_source_kind": fixture_source_kind,
            "runtime_outputs_dir": str(outputs_dir),
            "runtime_entrypoint": "tests/test.sh",
        }


def finding(
    severity: str,
    code: str,
    message: str,
    test_type: str,
    evidence: dict[str, Any],
) -> dict[str, Any]:
    return {
        "severity": severity,
        "code": code,
        "message": message,
        "test_type": test_type,
        "evidence": evidence,
    }


def normalize_runtime_failure_value(value: Any) -> Any:
    if isinstance(value, dict):
        normalized_items: dict[str, Any] = {}
        for key, item in sorted(value.items(), key=lambda pair: str(pair[0])):
            normalized_key = str(
                normalize_runtime_failure_value(str(key))
            )
            normalized_items[normalized_key] = (
                normalize_runtime_failure_value(item)
            )
        return normalized_items
    if isinstance(value, list):
        return [normalize_runtime_failure_value(item) for item in value]
    if not isinstance(value, str):
        return value
    normalized = value.replace("\\", "/")
    normalized = re.sub(
        r"(?:/private)?/var/folders/[^\s'\"():]+",
        "<TEMP_PATH>",
        normalized,
    )
    normalized = re.sub(
        r"(?:/tmp|/var/tmp)/[^\s'\"():]+",
        "<TEMP_PATH>",
        normalized,
    )
    normalized = re.sub(
        r"/[^\s'\"():]*/materials_(?:checker|oracle)_[^\s'\"():]+",
        "<TEMP_PATH>",
        normalized,
    )
    normalized = re.sub(
        r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-"
        r"[89ab][0-9a-f]{3}-[0-9a-f]{12}\b",
        "<UUID>",
        normalized,
        flags=re.IGNORECASE,
    )
    normalized = re.sub(
        r"\b0x[0-9a-f]+\b", "<MEMORY_ADDRESS>", normalized, flags=re.IGNORECASE
    )
    normalized = re.sub(
        r"\b(?:pid|process(?:\s+id)?)(?:\s*[=:]\s*|\s+)\d+\b",
        "pid=<PID>",
        normalized,
        flags=re.IGNORECASE,
    )
    return " ".join(normalized.split())


def runtime_failure_root(
    result: dict[str, Any],
) -> tuple[str, str, str | None]:
    stderr = str(result.get("stderr") or "")
    stderr_lines = [line.strip() for line in stderr.splitlines() if line.strip()]
    terminal_error = normalize_runtime_failure_value(
        stderr_lines[-1] if stderr_lines else ""
    )
    checker_frames = re.findall(
        r'File "[^"]*checker_patched\.py", line (\d+), in ([^\n]+)',
        stderr,
    )
    source_binding = (
        f"tests/checker.py:{checker_frames[-1][0]}:{checker_frames[-1][1].strip()}"
        if checker_frames
        else None
    )
    breakdown = result.get("breakdown")
    breakdown_errors = normalize_runtime_failure_value(
        breakdown.get("_errors", {})
        if isinstance(breakdown, dict)
        else {
            "_malformed_breakdown": breakdown,
            "_breakdown_type": type(breakdown).__name__,
        }
    )
    signature_payload = {
        "returncode": result.get("returncode"),
        "source_binding": source_binding,
        "terminal_error": terminal_error,
        "breakdown_errors": breakdown_errors,
        "reward_type": type(result.get("reward")).__name__,
        "reward": normalize_runtime_failure_value(repr(result.get("reward"))),
    }
    signature = hashlib.sha256(
        json.dumps(
            signature_payload, sort_keys=True, ensure_ascii=False
        ).encode("utf-8")
    ).hexdigest()[:16]
    return (
        f"checker_runtime_failure:{signature}",
        signature,
        source_binding,
    )


def evaluate_results(
    results: list[dict[str, Any]], pass_threshold: float
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    by_case = {result["case"]: result for result in results}
    negative_results = [
        result
        for result in results
        if result["case"] in NEGATIVE_PROBE_CASES
    ]
    negative_class_usable = bool(negative_results) and all(
        usable_probe_result(result) for result in negative_results
    )
    isolation_results = [
        result
        for result in results
        if result["case"].startswith("component_isolation__")
    ]
    evaluated_isolation_plan = [
        result["isolated_component"]
        for result in isolation_results
        if isinstance(result.get("isolated_component"), dict)
    ]
    isolation_class_usable = (
        bool(isolation_results)
        and len(evaluated_isolation_plan) == len(isolation_results)
        and all(usable_probe_result(result) for result in isolation_results)
        and component_runtime_bindings_verified(
            evaluated_isolation_plan, results
        )
    )
    for result in results:
        case = result["case"]
        if result.get("runtime_not_assessable") is True:
            continue
        runtime_root, failure_signature, source_binding = (
            runtime_failure_root(result)
        )
        if result["runtime_package_contains_solution"]:
            findings.append(
                finding(
                    "HIGH",
                    "SOLUTION_BOUNDARY_VIOLATION",
                    "isolated checker runtime contains solution content",
                    case,
                    {},
                )
            )
        if result["crashed"]:
            crash_evidence = (
                {
                    "status": "CRASH",
                    "failure_signature": failure_signature,
                    "source_binding": source_binding,
                    "root_cause": runtime_root,
                }
                if case == "positive_oracle"
                else {
                    "stderr": result["stderr"],
                    "failure_signature": failure_signature,
                    "source_binding": source_binding,
                    "root_cause": runtime_root,
                }
            )
            findings.append(
                finding(
                    "HIGH",
                    "CHECKER_CRASH",
                    f"checker crashed for {case}",
                    case,
                    crash_evidence,
                )
            )
        reward = result.get("reward")
        if not usable_probe_result(result):
            breakdown = result.get("breakdown")
            breakdown_errors = (
                breakdown.get("_errors", {})
                if isinstance(breakdown, dict)
                else {
                    "_malformed_breakdown": breakdown,
                    "_breakdown_type": type(breakdown).__name__,
                }
            )
            unusable_evidence = (
                {
                    "status": "UNUSABLE",
                    "failure_signature": failure_signature,
                    "source_binding": source_binding,
                    "root_cause": runtime_root,
                }
                if case == "positive_oracle"
                else {
                    "reward": reward,
                    "breakdown_errors": breakdown_errors,
                    "failure_signature": failure_signature,
                    "source_binding": source_binding,
                    "root_cause": runtime_root,
                }
            )
            findings.append(
                finding(
                    "HIGH",
                    "CHECKER_RESULT_UNUSABLE",
                    "checker did not emit a usable reward/breakdown result "
                    f"for {case}",
                    case,
                    unusable_evidence,
                )
            )
            continue
        assert isinstance(reward, float)
        if (
            (
                (case in NEGATIVE_PROBE_CASES and negative_class_usable)
                or case in TASK_FAMILY_CASES
            )
            and reward >= pass_threshold
        ):
            findings.append(
                finding(
                    "HIGH",
                    "ADVERSARIAL_OUTPUT_PASSES",
                    f"{case} receives a passing checker reward",
                    case,
                    {
                        "reward": reward,
                        "pass_threshold": pass_threshold,
                    },
                )
            )
        if case == "known_valid_public" and reward < pass_threshold:
            findings.append(
                finding(
                    "HIGH",
                    "KNOWN_VALID_OUTPUT_REJECTED",
                    "independently justified public output does not pass",
                    case,
                    {
                        "reward": reward,
                        "pass_threshold": pass_threshold,
                    },
                )
            )
        if case == "positive_oracle" and reward < pass_threshold:
            findings.append(
                finding(
                    "HIGH",
                    "ORACLE_POSITIVE_MOCK_REJECTED",
                    "isolated solution positive mock does not pass the checker",
                    case,
                    {"status": "REJECTED"},
                )
            )
        if (
            case.startswith("component_isolation__")
            and isolation_class_usable
            and reward >= pass_threshold
        ):
            component = result.get("isolated_component") or {}
            findings.append(
                finding(
                    "HIGH",
                    "SINGLE_COMPONENT_CAN_PASS",
                    "a source-bound component-isolation submission reaches "
                    "the checker pass threshold",
                    case,
                    {
                        "component_id": component.get("step_id"),
                        "retained_output": component.get("file"),
                        "reward": reward,
                        "pass_threshold": pass_threshold,
                        "fixture_source_kind": result.get(
                            "fixture_source_kind"
                        ),
                        "root_cause": "checker_component_aggregation_contract",
                    },
                )
            )
    def usable_score(case: str) -> float | None:
        result = by_case.get(case)
        return result["reward"] if usable_probe_result(result) else None

    valid = usable_score("known_valid_public")
    small = usable_score("quality_gradient_small_error")
    large = usable_score("quality_gradient_large_error")
    if (
        valid is not None
        and small is not None
        and large is not None
        and (small > valid + 1e-6 or large > small + 1e-6)
    ):
        findings.append(
            finding(
                "HIGH",
                "SCIENTIFIC_QUALITY_GRADIENT_VIOLATION",
                "checker reward is not monotonic as scientific numeric error increases",
                "materials_quality_gradient",
                {
                    "known_valid_reward": valid,
                    "small_error_reward": small,
                    "large_error_reward": large,
                    "expected_order": "known_valid >= small_error >= large_error",
                },
            )
        )
    equivalent = usable_score("metamorphic_equivalent_representation")
    if (
        valid is not None
        and equivalent is not None
        and abs(valid - equivalent) > 1e-6
    ):
        findings.append(
            finding(
                "HIGH",
                "SCIENTIFIC_INVARIANCE_VIOLATION",
                "equivalent row/key ordering or serialization changes the checker reward",
                "metamorphic_equivalent_representation",
                {
                    "known_valid_reward": valid,
                    "equivalent_representation_reward": equivalent,
                    "absolute_difference": abs(valid - equivalent),
                    "allowed_difference": 1e-6,
                },
            )
        )
    return findings


def sanitized_oracle_evidence(
    result: dict[str, Any], pass_threshold: float
) -> dict[str, Any]:
    """Persist Oracle status/provenance without checker-controlled values."""
    usable = usable_probe_result(result)
    return {
        "case": "positive_oracle",
        "mode": "known_valid",
        "returncode": result.get("returncode"),
        "crashed": bool(result.get("crashed")),
        "runtime_not_assessable": bool(
            result.get("runtime_not_assessable")
        ),
        "runtime_not_assessable_reason": result.get(
            "runtime_not_assessable_reason"
        ),
        "runtime_provenance": result.get("runtime_provenance"),
        "verifier_entrypoint": result.get("verifier_entrypoint"),
        "direct_checker_harness": result.get("direct_checker_harness"),
        "runtime_package_contains_solution": result.get(
            "runtime_package_contains_solution"
        ),
        "fixture_source_kind": "ORACLE_POSITIVE_MOCK",
        "usable_result": usable,
        "positive_mock_accepted": bool(
            usable
            and isinstance(result.get("reward"), float)
            and result["reward"] >= pass_threshold
        ),
        "contracted_outputs_generated": bool(
            result.get("created_outputs")
        ),
    }


def dynamic_checker_probe(
    root: Path, output: Path, known_valid_output: Path | None = None
) -> dict[str, Any]:
    checker_text = (root / "tests/checker.py").read_text(
        encoding="utf-8", errors="replace"
    )
    specification = read_json(root / "tests/grading_spec.json")
    pass_threshold = float(specification.get("pass_threshold", 1.0))
    if not math.isfinite(pass_threshold) or not 0 <= pass_threshold <= 1:
        raise ValueError(
            "pass threshold must be a finite number between zero and one"
        )
    fixture_provenance = (
        validate_known_valid_fixture(root, known_valid_output, specification)
        if known_valid_output is not None
        else None
    )
    random.seed(17)
    attack_applicability = task_family_applicability(root, specification)
    oracle_temporary, oracle_output, oracle_evidence = prepare_solution_oracle(
        root, specification
    )
    cases: list[
        tuple[
            str,
            str,
            Path | None,
            dict[str, str] | None,
            str | None,
        ]
    ] = [
        ("missing_outputs", "missing", None, None, None),
        ("empty_valid_shape", "empty", None, None, None),
        ("malformed_outputs", "malformed", None, None, None),
        ("random_baseline", "random", None, None, None),
        ("minimal_gold_shape", "minimal", None, None, None),
        ("duplicate_gold_rows", "duplicate", None, None, None),
        ("nonfinite_values", "nonfinite", None, None, None),
        *(
            (
                case_name,
                mode,
                None,
                None,
                "SCHEMA_SHAPED_SYNTHETIC_ATTACK",
            )
            for case_name, mode in TASK_FAMILY_MODES.items()
            if attack_applicability[TASK_FAMILY_CASES[case_name]][
                "applicable"
            ]
        ),
    ]
    if oracle_output is not None:
        cases.append(
            (
                "positive_oracle",
                "known_valid",
                oracle_output,
                None,
                "ORACLE_POSITIVE_MOCK",
            )
        )
    if known_valid_output is not None:
        cases.extend(
            (
                (
                    "known_valid_public",
                    "known_valid",
                    known_valid_output,
                    None,
                    "INDEPENDENT_PUBLIC_FIXTURE",
                ),
                (
                    "sparse_known_valid",
                    "sparse_known_valid",
                    known_valid_output,
                    None,
                    "INDEPENDENT_PUBLIC_FIXTURE",
                ),
                (
                    "quality_gradient_small_error",
                    "quality_small",
                    known_valid_output,
                    None,
                    "INDEPENDENT_PUBLIC_FIXTURE",
                ),
                (
                    "quality_gradient_large_error",
                    "quality_large",
                    known_valid_output,
                    None,
                    "INDEPENDENT_PUBLIC_FIXTURE",
                ),
                (
                    "metamorphic_equivalent_representation",
                    "metamorphic",
                    known_valid_output,
                    None,
                    "INDEPENDENT_PUBLIC_FIXTURE",
                ),
            )
        )
    isolation_source = known_valid_output
    isolation_source_kind = (
        "INDEPENDENT_PUBLIC_FIXTURE"
        if known_valid_output is not None
        else None
    )
    source_isolation_plan, isolation_not_run_reason = component_isolation_plan(
        specification, isolation_source, checker_text
    )
    try:
        results = [
            run_checker_case(
                root,
                checker_text,
                specification,
                case_name,
                mode,
                source_output,
                isolated_component,
                source_kind,
            )
            for (
                case_name,
                mode,
                source_output,
                isolated_component,
                source_kind,
            ) in cases
        ]
        isolation_plan: list[dict[str, str]] = []
        if source_isolation_plan and component_runtime_bindings_verified(
            source_isolation_plan, results
        ):
            isolation_plan = source_isolation_plan
            for component in isolation_plan:
                safe_id = re.sub(
                    r"[^A-Za-z0-9_.-]+", "_", component["step_id"]
                )
                results.append(
                    run_checker_case(
                        root,
                        checker_text,
                        specification,
                        f"component_isolation__{safe_id}",
                        "component_isolation",
                        isolation_source,
                        component,
                        isolation_source_kind,
                    )
                )
        elif source_isolation_plan:
            isolation_not_run_reason = (
                "independent fixture did not establish every checker runtime "
                "scorer binding"
            )
        if fixture_provenance is not None:
            for result in results:
                if (
                    result.get("fixture_source_kind")
                    == "INDEPENDENT_PUBLIC_FIXTURE"
                ):
                    result["fixture_provenance"] = fixture_provenance
    finally:
        if oracle_temporary is not None:
            oracle_temporary.cleanup()
    findings = evaluate_results(results, pass_threshold)
    isolation_coverage = component_isolation_coverage(
        isolation_plan, isolation_not_run_reason, results
    )
    task_attacks = task_family_attack_coverage(
        results, pass_threshold, attack_applicability
    )
    if known_valid_output is None:
        findings.append(
            finding(
                "MEDIUM",
                "INDEPENDENT_PUBLIC_FIXTURE_UNAVAILABLE",
                (
                    "discrimination and equivalence probes were not executed "
                    "because no independently justified public valid output "
                    "was supplied"
                ),
                "probe_coverage",
                {
                    "unassessed_probe_classes": [
                        "discrimination",
                        "equivalence",
                    ],
                    "oracle_used": False,
                },
            )
        )
    bound_fixture_hashes = (
        fixture_provenance["fixture_hashes"]
        if fixture_provenance is not None
        else {}
    )
    expected = {
        "missing_outputs": "score below pass threshold without crashing",
        "empty_valid_shape": "score below pass threshold without crashing",
        "malformed_outputs": "score below pass threshold without crashing",
        "random_baseline": "score below pass threshold",
        "minimal_gold_shape": "score below pass threshold",
        "duplicate_gold_rows": "duplicates do not create a passing score",
        "nonfinite_values": "non-finite values score below pass threshold",
        "known_valid_public": "independently justified output passes",
        "positive_oracle": (
            "isolated solution mock passes without becoming scientific evidence"
        ),
        "sparse_known_valid": "a sparse subset cannot pass the full task",
        "quality_gradient_small_error": (
            "small scientific numeric error scores no higher than known-valid"
        ),
        "quality_gradient_large_error": (
            "larger scientific numeric error scores no higher than small error"
        ),
        "metamorphic_equivalent_representation": (
            "equivalent ordering and serialization preserve the reward"
        ),
    }
    expected.update(
        {
            case_name: (
                "task-family materials attack does not receive a passing "
                "reward without semantic validation"
            )
            for case_name in TASK_FAMILY_CASES
        }
    )
    expected.update(
        {
            result["case"]: (
                "a submission retaining only the named scoring component "
                "stays below the pass threshold"
            )
            for result in results
            if result["case"].startswith("component_isolation__")
        }
    )
    tests = []
    probe_classes = {
        "positive_oracle": "positive",
        "known_valid_public": "discrimination",
        "quality_gradient_small_error": "discrimination",
        "quality_gradient_large_error": "discrimination",
        "metamorphic_equivalent_representation": "equivalence",
    }
    results_by_case = {result["case"]: result for result in results}
    assessment_flags = probe_assessment_flags(results)
    positive_assessed = assessment_flags["positive"]
    negative_assessed = assessment_flags["negative"]
    discrimination_assessed = assessment_flags["discrimination"]
    equivalence_assessed = assessment_flags["equivalence"]
    for index, result in enumerate(results, start=1):
        oracle_case = result["case"] == "positive_oracle"
        probe_class = (
            "component_isolation"
            if result["case"].startswith("component_isolation__")
            else "negative"
            if result["case"] in TASK_FAMILY_CASES
            else probe_classes.get(result["case"], "negative")
        )
        tests.append(
            {
                "test_id": f"CHECKER-{index:03d}",
                "test_type": result["case"],
                "probe_class": probe_class,
                "description": result["case"].replace("_", " "),
                "expected_behavior": expected[result["case"]],
                "observed_score": (
                    None if oracle_case else result.get("reward")
                ),
                "observed_status": (
                    "CRASH"
                    if result["crashed"]
                    else (
                        "COMPLETED"
                        if usable_probe_result(result)
                        else "UNUSABLE"
                    )
                ),
                "exit_code": result.get("returncode"),
                "hard_gate_triggered": any(
                    item["severity"] == "FATAL"
                    and item["test_type"] == result["case"]
                    for item in findings
                ),
                "evidence": (
                    sanitized_oracle_evidence(result, pass_threshold)
                    if oracle_case
                    else result
                ),
            }
        )
    runtime_not_assessable = [
        result
        for result in results
        if result.get("runtime_not_assessable") is True
    ]
    checker_result = {
        "schema_version": "0.1",
        "benchmark_root": str(root),
        "checker_path": "tests/checker.py",
        "runtime": {
            "verifier_entrypoint": "tests/test.sh",
            "runtime_provenance": (
                "not-assessable"
                if runtime_not_assessable
                else "audit-host-copy"
            ),
            "direct_checker_harness": False,
            "status": (
                "NOT_ASSESSABLE"
                if runtime_not_assessable
                else "ASSESSED"
            ),
            "reason": (
                runtime_not_assessable[0].get(
                    "runtime_not_assessable_reason"
                )
                if runtime_not_assessable
                else None
            ),
        },
        "solution_content_inspected": False,
        "solution_oracle": oracle_evidence,
        "pass_threshold": pass_threshold,
        "tests": tests,
        "findings": findings,
        "usable_reward_count": sum(
            usable_probe_result(result) for result in results
        ),
        "probe_coverage": {
            "positive": {
                "status": (
                    "ASSESSED" if positive_assessed else "NOT_ASSESSABLE"
                ),
                "reason": (
                    None
                    if positive_assessed
                    else "no positive control produced a usable probe result"
                ),
                "provenance": {
                    "source_kinds": [
                        *(
                            ["ORACLE_POSITIVE_MOCK"]
                            if usable_probe_result(
                                results_by_case.get("positive_oracle")
                            )
                            else []
                        ),
                    ],
                    "oracle_scientific_evidence": False,
                },
            },
            "negative": {
                "status": (
                    "ASSESSED" if negative_assessed else "NOT_ASSESSABLE"
                ),
                "reason": (
                    None
                    if negative_assessed
                    else "one or more negative probes produced unusable results"
                ),
                "provenance": {
                    "source_kind": "SCHEMA_SHAPED_SYNTHETIC_ATTACKS",
                    "oracle_used": False,
                },
                "subcoverage": {
                    "task_family_attacks": task_attacks,
                },
            },
            "discrimination": {
                "status": (
                    "ASSESSED"
                    if discrimination_assessed
                    else "NOT_ASSESSABLE"
                ),
                "reason": (
                    None
                    if discrimination_assessed
                    else "discrimination requires usable known-valid, small-error, and large-error results"
                ),
                "provenance": {
                    "source_kind": (
                        "INDEPENDENT_PUBLIC_FIXTURE"
                        if discrimination_assessed
                        else "NONE"
                    ),
                    "fixture_hashes": (
                        bound_fixture_hashes
                        if discrimination_assessed
                        else {}
                    ),
                    "fixture_manifest_hash": (
                        fixture_provenance["fixture_manifest_hash"]
                        if discrimination_assessed
                        and fixture_provenance is not None
                        else None
                    ),
                    "source_role_hashes": (
                        fixture_provenance["source_role_hashes"]
                        if discrimination_assessed
                        and fixture_provenance is not None
                        else {}
                    ),
                    "oracle_used": False,
                },
            },
            "equivalence": {
                "status": (
                    "ASSESSED"
                    if equivalence_assessed
                    else "NOT_ASSESSABLE"
                ),
                "reason": (
                    None
                    if equivalence_assessed
                    else "equivalence requires usable known-valid and transformed results"
                ),
                "provenance": {
                    "source_kind": (
                        "INDEPENDENT_PUBLIC_FIXTURE"
                        if equivalence_assessed
                        else "NONE"
                    ),
                    "fixture_hashes": (
                        bound_fixture_hashes if equivalence_assessed else {}
                    ),
                    "fixture_manifest_hash": (
                        fixture_provenance["fixture_manifest_hash"]
                        if equivalence_assessed
                        and fixture_provenance is not None
                        else None
                    ),
                    "source_role_hashes": (
                        fixture_provenance["source_role_hashes"]
                        if equivalence_assessed
                        and fixture_provenance is not None
                        else {}
                    ),
                    "oracle_used": False,
                },
            },
            "component_isolation": {
                **isolation_coverage,
            },
        },
        "runtime_provenance": {
            "status": "ASSESSED",
            "entrypoint": "tests/test.sh",
            "execution_mode": "ISOLATED_REBASED_HARBOR_VERIFIER",
            "cases_executed": len(results),
        },
        "limitations": [
            "schema-shaped synthetic outputs do not establish scientific correctness",
            "scientific gradients and metamorphic probes require an independently justified public valid output",
            *(
                [
                    "component isolation requires an independent source-bound "
                    f"fixture and verified scorer bindings: "
                    f"{isolation_coverage['reason']}"
                ]
                if isolation_coverage["status"] != "ASSESSED"
                else []
            ),
            "external-service or compiled checker dependencies may require container execution",
            *(
                [
                    "The Harbor verifier could not be assessed on the audit host: "
                    + str(
                        runtime_not_assessable[0].get(
                            "runtime_not_assessable_reason"
                        )
                    )
                ]
                if runtime_not_assessable
                else []
            ),
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(checker_result, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return checker_result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output", default="checker_tests.json")
    parser.add_argument("--known-valid-output")
    arguments = parser.parse_args()
    try:
        result = dynamic_checker_probe(
            locate_root(Path(arguments.input)),
            Path(arguments.output).expanduser().resolve(),
            (
                Path(arguments.known_valid_output)
                if arguments.known_valid_output
                else None
            ),
        )
        print(
            json.dumps(
                {
                    "tests": len(result["tests"]),
                    "findings": len(result["findings"]),
                    "output": arguments.output,
                },
                indent=2,
            )
        )
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"checker probe failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
