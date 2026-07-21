#!/usr/bin/env python3
"""Execute isolated submissions against the real Harbor checker."""

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
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from audit_package import instruction_contract_map
from prepare_audit_output import (
    QUALITY_EVIDENCE_ROLES,
    basename,
    locate_root,
    sha256_file,
)
from artifact_schema import (
    CHECKER_TESTS_SCHEMA_VERSION,
    DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
    QUALITY_PROBE_RESULTS_SCHEMA_VERSION,
)
import sandbox_runtime


ORACLE_VENV_TIMEOUT_SECONDS = 60.0
ORACLE_SOLVE_TIMEOUT_SECONDS = 300.0
# Baseline scientific dependencies always provided to the checker sandbox.
# ``pip`` is included so a checker's own in-process ``python -m pip install``
# self-install still succeeds inside the isolated env.
CHECKER_RUN_TIMEOUT_SECONDS = 60.0
CHECKER_UV_BASELINE_PACKAGES = ("numpy", "scipy", "pandas", "pip")
# Host python may be too new for some scientific wheels; pin uv to a broadly
# wheel-compatible interpreter unless the operator overrides it.
CHECKER_UV_DEFAULT_PYTHON = "3.12"
# Map common third-party import names to their PyPI distribution names.
IMPORT_TO_PYPI = {
    "numpy": "numpy",
    "scipy": "scipy",
    "pandas": "pandas",
    "sklearn": "scikit-learn",
    "skimage": "scikit-image",
    "matplotlib": "matplotlib",
    "mpl_toolkits": "matplotlib",
    "ase": "ase",
    "pymatgen": "pymatgen",
    "monty": "monty",
    "spglib": "spglib",
    "phonopy": "phonopy",
    "seekpath": "seekpath",
    "mp_api": "mp-api",
    "cv2": "opencv-python-headless",
    "PIL": "pillow",
    "yaml": "pyyaml",
    "h5py": "h5py",
    "netCDF4": "netCDF4",
    "networkx": "networkx",
    "sympy": "sympy",
    "numba": "numba",
    "numexpr": "numexpr",
    "statsmodels": "statsmodels",
    "sklearn_extra": "scikit-learn-extra",
    "tqdm": "tqdm",
    "torch": "torch",
    "sklearn.linear_model": "scikit-learn",
    "pint": "pint",
    "uncertainties": "uncertainties",
    "lmfit": "lmfit",
}
NEGATIVE_PROBE_CASES = frozenset(
    {
        "missing_outputs",
        "empty_valid_shape",
        "malformed_outputs",
        "random_baseline",
        "minimal_gold_shape",
        "duplicate_gold_rows",
        "nonfinite_values",
    }
)
DETERMINISTIC_CORE_CASES = frozenset(
    {
        "missing_outputs",
        "empty_valid_shape",
        "malformed_outputs",
        "random_baseline",
        "minimal_gold_shape",
        "duplicate_gold_rows",
        "nonfinite_values",
        "positive_oracle",
        "all_wrong",
    }
)
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


def checker_run_timeout() -> float:
    """Return the checker limit, allowing only a stricter operator override."""
    return min(
        configured_timeout(
            "MATERIALS_CHECKER_RUN_TIMEOUT_SECONDS",
            CHECKER_RUN_TIMEOUT_SECONDS,
        ),
        CHECKER_RUN_TIMEOUT_SECONDS,
    )


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


def declared_scoring_components(
    specification: dict[str, Any],
) -> list[dict[str, Any]]:
    """Return every positive-weight declared step without file-level collapse."""
    outputs = {
        basename(item.get("file")): item
        for item in (
            (specification.get("output_contract", {}) or {}).get("outputs", [])
            or []
        )
        if isinstance(item, dict) and basename(item.get("file"))
    }
    components: list[dict[str, Any]] = []
    for step in grading_steps(specification):
        if not isinstance(step, dict):
            continue
        filename = basename(step.get("output_file"))
        weight = finite_number(step.get("weight"))
        if (
            not filename
            or filename not in outputs
            or weight is None
            or weight <= 0
        ):
            continue
        target = step.get("target")
        paths: list[list[str | int]] = []

        def collect_paths(value: Any, prefix: list[str | int]) -> None:
            if isinstance(value, dict):
                for key in sorted(value):
                    collect_paths(value[key], [*prefix, key])
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    collect_paths(item, [*prefix, index])
            else:
                paths.append(prefix)

        if isinstance(target, (dict, list)):
            collect_paths(target, [])
        components.append(
            {
                "component_id": str(step.get("id") or filename),
                "file": filename,
                "declared_weight": weight,
                "format": str(outputs[filename].get("format", "")).lower(),
                "paths": paths,
            }
        )
    return components


def _flip_categorical(value: str) -> str | None:
    """Return another valid-looking categorical token when possible."""
    lowered = value.strip().lower()
    catalog = {
        "true": "false",
        "false": "true",
        "yes": "no",
        "no": "yes",
        "pass": "fail",
        "fail": "pass",
        "positive": "negative",
        "negative": "positive",
        "metal": "insulator",
        "insulator": "metal",
        "stable": "unstable",
        "unstable": "stable",
        "a": "b",
        "b": "a",
    }
    if lowered in catalog:
        flipped = catalog[lowered]
        if value.isupper():
            return flipped.upper()
        if value[:1].isupper():
            return flipped[:1].upper() + flipped[1:]
        return flipped
    if value.isdigit():
        return str((int(value) + 1) % 10)
    return None


def _mutate_json_value(value: Any, *, all_wrong: bool = False) -> tuple[Any, bool]:
    """Mutate scored JSON values while preserving contracted shape/types.

    ``all_wrong`` mutates every mutable leaf. Partial mode mutates the first
    mutable leaf only.
    """
    if isinstance(value, bool):
        if all_wrong:
            return (not value), True
        return value, False
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if not math.isfinite(float(value)):
            return value, False
        if isinstance(value, int) and not isinstance(value, bool):
            delta = 1 if all_wrong else 1
            return value + delta, True
        number = float(value)
        delta = (1.0 if all_wrong else 0.25) * max(abs(number), 1.0)
        return number + delta, True
    if isinstance(value, str):
        flipped = _flip_categorical(value)
        if flipped is not None and flipped != value:
            return flipped, True
        return value, False
    if isinstance(value, list):
        if not all_wrong:
            for index, item in enumerate(value):
                mutated, changed = _mutate_json_value(item, all_wrong=False)
                if changed:
                    result = list(value)
                    result[index] = mutated
                    return result, True
            return value, False
        result = list(value)
        changed_any = False
        for index, item in enumerate(result):
            mutated, changed = _mutate_json_value(item, all_wrong=True)
            if changed:
                result[index] = mutated
                changed_any = True
        return result, changed_any
    if isinstance(value, dict):
        if not all_wrong:
            for key in sorted(value):
                mutated, changed = _mutate_json_value(value[key], all_wrong=False)
                if changed:
                    result = dict(value)
                    result[key] = mutated
                    return result, True
            return value, False
        result = dict(value)
        changed_any = False
        for key in sorted(result):
            mutated, changed = _mutate_json_value(result[key], all_wrong=True)
            if changed:
                result[key] = mutated
                changed_any = True
        return result, changed_any
    return value, False


def mutate_declared_component(
    output_dir: Path,
    component: dict[str, Any],
    *,
    all_wrong: bool = False,
    specification: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Deterministically make declared component(s) wrong in an Oracle copy."""
    filename = str(component["file"])
    path = output_dir / filename
    output_format = str(component.get("format") or "").lower()
    if not output_format and specification is not None:
        for output in (
            (specification.get("output_contract", {}) or {}).get("outputs", [])
            or []
        ):
            if basename(output.get("file")) == filename:
                output_format = str(output.get("format", "")).lower()
                break
    detail: dict[str, Any] = {
        "component_id": component["component_id"],
        "file": filename,
        "operation": "schema_derived_wrong_component",
        "all_wrong": all_wrong,
    }
    if output_format == "json":
        value = read_json(path)
        paths = component.get("paths") or []
        mutated = json.loads(json.dumps(value))
        changed = False
        selected = paths if all_wrong else paths[:1]
        for declared_path in selected:
            parent = mutated
            try:
                for segment in declared_path[:-1]:
                    parent = parent[segment]
                key = declared_path[-1]
                replacement, did_change = _mutate_json_value(
                    parent[key], all_wrong=True
                )
                if did_change:
                    parent[key] = replacement
                    changed = True
            except (KeyError, IndexError, TypeError):
                continue
        if not selected:
            mutated, changed = _mutate_json_value(value, all_wrong=all_wrong)
        if not changed:
            detail["mutation"] = "not_assessable"
            detail["not_assessable_reason"] = (
                "schema cannot support a meaningful wrong mutation while "
                "preserving contracted JSON shape/types"
            )
            return detail
        path.write_text(
            json.dumps(mutated, ensure_ascii=False),
            encoding="utf-8",
        )
        detail["mutation"] = (
            "all_scored_json_leaves" if all_wrong else "first_mutable_json_leaf"
        )
        return detail
    if output_format in {"csv", "tsv"}:
        delimiter = "\t" if output_format == "tsv" else ","
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle, delimiter=delimiter)
            fieldnames = list(reader.fieldnames or [])
            rows = list(reader)
        required_columns: list[str] = []
        if specification is not None:
            for output in (
                (specification.get("output_contract", {}) or {}).get("outputs", [])
                or []
            ):
                if basename(output.get("file")) != filename:
                    continue
                schema = output.get("schema", {}) or {}
                required_columns = list(schema.get("required_columns", []) or [])
        mutable_columns = [
            column
            for column in (required_columns or fieldnames)
            if column
            and any(finite_number(row.get(column)) is not None for row in rows)
        ]
        if not mutable_columns:
            # Preserve categorical/format-valid labels by flipping known tokens.
            categorical_columns = [
                column
                for column in (required_columns or fieldnames)
                if column
                and any(
                    isinstance(row.get(column), str)
                    and _flip_categorical(str(row.get(column))) is not None
                    for row in rows
                )
            ]
            mutable_columns = categorical_columns
        anchor_names = {
            "id",
            "index",
            "true",
            "true_value",
            "label",
            "target",
            "ground_truth",
        }
        scored_columns = [
            column
            for column in mutable_columns
            if column is not None
            and column.strip().lower() not in anchor_names
            and not column.strip().lower().startswith("true_")
        ]
        if all_wrong:
            target_columns = scored_columns or mutable_columns
        else:
            column = response_column(fieldnames, rows)
            if column is not None and column in (scored_columns or mutable_columns):
                target_columns = [column]
            else:
                target_columns = (scored_columns or mutable_columns)[:1]
        changed = 0
        for column_index, column in enumerate(target_columns):
            if column is None:
                continue
            for row in rows:
                number = finite_number(row.get(column))
                if number is not None:
                    # Distinct per-column deltas keep relationships from
                    # remaining accidentally correct after all_wrong.
                    multiplier = (
                        (1.0 + 0.5 * column_index) if all_wrong else 0.25
                    )
                    row[column] = (
                        f"{number + multiplier * max(abs(number), 1.0):.12g}"
                    )
                    changed += 1
                    continue
                raw = row.get(column)
                if isinstance(raw, str):
                    flipped = _flip_categorical(raw)
                    if flipped is not None and flipped != raw:
                        row[column] = flipped
                        changed += 1
        if changed == 0:
            detail["mutation"] = "not_assessable"
            detail["not_assessable_reason"] = (
                "schema cannot support a meaningful wrong mutation while "
                "preserving contracted tabular shape/types"
            )
            return detail
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle, fieldnames=fieldnames, delimiter=delimiter
            )
            writer.writeheader()
            writer.writerows(rows)
        detail["mutation"] = (
            "all_mutable_columns" if all_wrong else "numeric_response_column"
        )
        detail["response_columns"] = target_columns
        detail["changed_values"] = changed
        return detail
    if output_format in {"txt", "text", "number", "numeric"}:
        raw = path.read_text(encoding="utf-8").strip()
        number = finite_number(raw)
        if number is None:
            detail["mutation"] = "not_assessable"
            detail["not_assessable_reason"] = (
                "declared scalar text is not parseable numeric text"
            )
            return detail
        delta = max(abs(number), 1.0) * (1.0 if all_wrong else 0.25)
        path.write_text(f"{number + delta:.12g}\n", encoding="utf-8")
        detail["mutation"] = "parseable_numeric_text"
        return detail
    detail["mutation"] = "not_assessable"
    detail["not_assessable_reason"] = (
        f"unsupported contracted format {output_format!r} for shape-preserving "
        "wrong mutation"
    )
    return detail


def schema_derived_probe_plan(
    specification: dict[str, Any],
    oracle_output: Path | None,
) -> tuple[list[dict[str, Any]], str | None]:
    """Plan full/partial/all-wrong cases from the declared schema and steps."""
    components = declared_scoring_components(specification)
    if oracle_output is None:
        return [], "the isolated Oracle did not produce a full contracted output"
    if not components:
        return [], "no independently declared positive-weight component is available"
    return (
        [
            {
                "case": "all_wrong",
                "mode": "all_wrong",
                "components": components,
                "probe_origin": "SCHEMA_DERIVED_DETERMINISTIC",
            },
            *[
                {
                    "case": f"partial__{re.sub(r'[^A-Za-z0-9_.-]+', '_', component['component_id'])}",
                    "mode": "partial",
                    "components": [component],
                    "probe_origin": "SCHEMA_DERIVED_DETERMINISTIC",
                }
                for component in components
            ],
        ],
        None,
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
    return {
        "positive": any(
            usable_probe_result(by_case[case]) for case in positive_cases
        ),
        "negative": bool(negative_cases)
        and all(usable_probe_result(result) for result in negative_cases),
        "discrimination": False,
        "equivalence": False,
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


def copy_public_package(root: Path, destination: Path) -> None:
    """Copy only instruction/tests into the isolated checker runtime."""
    destination.mkdir(parents=True, exist_ok=True)
    instruction = root / "instruction.md"
    if instruction.is_file():
        shutil.copy2(instruction, destination / "instruction.md")
    if (root / "tests").is_dir():
        shutil.copytree(root / "tests", destination / "tests")


def copy_oracle_outputs(
    source_dir: Path,
    output_dir: Path,
    specification: dict[str, Any],
) -> list[str]:
    """Copy only the isolated Oracle's contracted outputs into a probe case."""
    created: list[str] = []
    outputs = (
        (specification.get("output_contract", {}) or {}).get("outputs", []) or []
    )
    source_dir = source_dir.resolve()
    for output in outputs:
        filename = basename(output.get("file"))
        if not filename:
            continue
        source = source_dir / filename
        if source.parent != source_dir or not source.is_file():
            raise FileNotFoundError(
                f"isolated Oracle output is missing contracted file: {filename}"
            )
        destination = output_dir / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        created.append(filename)
    return created


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


def uv_python_version() -> str:
    """Return the interpreter version uv should provision for checkers."""
    value = os.environ.get("MATERIALS_CHECKER_UV_PYTHON", "").strip()
    return value or CHECKER_UV_DEFAULT_PYTHON


def extra_uv_packages() -> list[str]:
    """Operator-supplied extra packages via MATERIALS_CHECKER_UV_WITH."""
    raw = os.environ.get("MATERIALS_CHECKER_UV_WITH", "")
    return [token for token in re.split(r"[,\s]+", raw) if token]


def detect_import_packages(text: str) -> set[str]:
    """Return PyPI names for third-party imports found in Python source text."""
    packages: set[str] = set()
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return packages
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split(".")[0]
                if top in IMPORT_TO_PYPI:
                    packages.add(IMPORT_TO_PYPI[top])
                elif top not in sys.stdlib_module_names:
                    packages.add(top)
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:
                top = node.module.split(".")[0]
                if top in IMPORT_TO_PYPI:
                    packages.add(IMPORT_TO_PYPI[top])
                elif top not in sys.stdlib_module_names:
                    packages.add(top)
    return packages


def detect_pip_install_packages(text: str) -> set[str]:
    """Extract explicit ``pip install <names>`` distributions from any text."""
    names: set[str] = set()
    for match in re.finditer(
        r"pip['\"\s,]+install\b(.*?)(?:\]|\n|;)", text, re.DOTALL
    ):
        segment = match.group(1)
        for quoted, bare in re.findall(r"""['"]([^'"]+)['"]|(\S+)""", segment):
            candidate = (quoted or bare).strip().strip(",")
            if not candidate or candidate.startswith("-"):
                continue
            if "/" in candidate or ":" in candidate:
                continue
            base = re.split(r"[<>=!~\[; ]", candidate)[0].strip()
            if base and re.fullmatch(r"[A-Za-z][A-Za-z0-9_.\-]*", base):
                names.add(base)
    return names


def checker_uv_packages(root: Path, checker_text: str) -> list[str]:
    """Derive the ``--with`` package set for the uv-managed checker runtime."""
    detected: set[str] = set()
    texts = [checker_text]
    solution_dir = root / "solution"
    if solution_dir.is_dir():
        solve_script = solution_dir / "solve.sh"
        if solve_script.is_file():
            texts.append(
                solve_script.read_text(encoding="utf-8", errors="replace")
            )
        for python_file in sorted(solution_dir.glob("*.py")):
            if python_file.is_file():
                texts.append(
                    python_file.read_text(encoding="utf-8", errors="replace")
                )
    for text in texts:
        detected |= detect_import_packages(text)
        detected |= detect_pip_install_packages(text)
    ordered: list[str] = []
    for name in (
        *CHECKER_UV_BASELINE_PACKAGES,
        *sorted(detected),
        *extra_uv_packages(),
    ):
        if name not in ordered:
            ordered.append(name)
    return ordered


def write_python_shim(
    bin_dir: Path,
    uv_path: str,
    packages: list[str],
    python_version: str,
) -> None:
    """Write ``python``/``python3`` shims that exec through a uv ephemeral env.

    Any ``python``/``python3`` invocation (including a checker's own child
    ``python -m pip install X``) then runs inside an isolated, network-capable
    uv environment that already has the scientific dependencies, without
    polluting the audit host interpreter.
    """
    with_args = " ".join(f"--with {shlex.quote(pkg)}" for pkg in packages)
    script = (
        "#!/bin/sh\n"
        f"exec {shlex.quote(uv_path)} run "
        f"--python {shlex.quote(python_version)} "
        f"{with_args} python \"$@\"\n"
    )
    for name in ("python", "python3"):
        target = bin_dir / name
        target.write_text(script, encoding="utf-8")
        target.chmod(0o755)


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
        current_stage = "venv"
        uv_path = shutil.which("uv")
        if uv_path is not None:
            oracle_bin = Path(temporary.name) / "bin"
            oracle_bin.mkdir()
            checker_source = root / "tests/checker.py"
            checker_text = (
                checker_source.read_text(encoding="utf-8", errors="replace")
                if checker_source.is_file()
                else ""
            )
            write_python_shim(
                oracle_bin,
                uv_path,
                checker_uv_packages(root, checker_text),
                uv_python_version(),
            )
            solve_bin = str(oracle_bin)
        else:
            virtualenv = Path(temporary.name) / "venv"
            subprocess.run(
                [sys.executable, "-m", "venv", str(virtualenv)],
                capture_output=True,
                text=True,
                timeout=venv_timeout,
                check=True,
            )
            solve_bin = str(virtualenv / "bin")
        setup_prepared = True
        environment = {
            **os.environ,
            "OUTPUT_DIR": str(outputs),
            "PATH": solve_bin
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


def probe_lane(case_name: str) -> str:
    """Return the owning lane for an executed probe case."""
    if case_name in DETERMINISTIC_CORE_CASES or case_name.startswith("partial__"):
        return "deterministic_core"
    return "quality_results"


def run_checker_case(
    root: Path,
    checker_text: str,
    specification: dict[str, Any],
    case_name: str,
    mode: str,
    oracle_output: Path | None,
    probe_workspace: Path,
    component: dict[str, Any] | None = None,
) -> dict[str, Any]:
    safe_case_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", case_name)
    base = probe_workspace / safe_case_name
    if base.exists():
        shutil.rmtree(base)
    base.mkdir(parents=True, exist_ok=True)
    try:
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
        if mode == "positive_oracle":
            if oracle_output is None:
                raise ValueError(f"{mode} probe requires an isolated Oracle output")
            created = copy_oracle_outputs(oracle_output, outputs_dir, specification)
        elif mode == "malformed":
            created = write_malformed_outputs(outputs_dir, specification)
        elif mode in {"partial", "all_wrong"}:
            if oracle_output is None or (mode == "partial" and component is None):
                raise ValueError(
                    f"{mode} schema probe requires an isolated Oracle output"
                )
            created = copy_oracle_outputs(
                oracle_output,
                outputs_dir,
                specification,
            )
            components = (
                [component]
                if mode == "partial" and component is not None
                else declared_scoring_components(specification)
            )
            transformations = [
                mutate_declared_component(
                    outputs_dir,
                    component,
                    all_wrong=mode == "all_wrong",
                    specification=specification,
                )
                for component in components
            ]
            if any(
                item.get("mutation") == "not_assessable"
                for item in transformations
            ):
                reason = next(
                    item.get("not_assessable_reason")
                    for item in transformations
                    if item.get("mutation") == "not_assessable"
                )
                return {
                    "case": case_name,
                    "mode": mode,
                    "created_outputs": created,
                    "transformations": transformations,
                    "returncode": None,
                    "reward": None,
                    "breakdown": None,
                    "stdout": "",
                    "stderr": str(reason),
                    "crashed": False,
                    "runtime_not_assessable": True,
                    "runtime_not_assessable_reason": str(reason),
                    "runtime_provenance": "sandbox",
                    "checker_dependency_env": "sandbox",
                    "verifier_entrypoint": "tests/test.sh",
                    "direct_checker_harness": False,
                    "runtime_package_contains_solution": (
                        package_dir / "solution"
                    ).exists(),
                    "component": component,
                    "lane": probe_lane(case_name),
                }
        elif mode != "missing":
            created = write_synthetic_outputs(
                outputs_dir, specification, mode
            )

        patched = patch_harbor_paths(
            checker_text,
            Path("/tests"),
            Path("/app/outputs"),
            Path("/logs/verifier"),
        )
        checker_path = tests_dir / "checker.py"
        checker_path.write_text(patched, encoding="utf-8")
        verifier_source = root / "tests/test.sh"
        verifier_path = base / "test.sh"
        runtime_provenance = "sandbox"
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
                "runtime_provenance": runtime_provenance,
                "checker_dependency_env": runtime_provenance,
                "verifier_entrypoint": "tests/test.sh",
                "direct_checker_harness": False,
                "runtime_package_contains_solution": (
                    package_dir / "solution"
                ).exists(),
                "component": component,
                "lane": probe_lane(case_name),
            }
        verifier_path.write_text(
            patch_harbor_paths(
                verifier_source.read_text(encoding="utf-8", errors="replace"),
                Path("/tests"),
                Path("/app/outputs"),
                Path("/logs/verifier"),
            ),
            encoding="utf-8",
        )
        # Checker execution is a regression boundary: callers may tighten
        # its timeout, but must never extend the contractual 60-second limit.
        run_timeout = checker_run_timeout()
        process = sandbox_runtime.run_in_sandbox(
            ["/bin/bash", "/workspace/test.sh"],
            mounts=[
                (base, "/workspace", "rw"),
                (tests_dir, "/workspace/tests", "rw"),
                (tests_dir, "/tests", "rw"),
                (outputs_dir, "/app/outputs", "rw"),
                (logs_dir, "/logs/verifier", "rw"),
            ],
            workdir="/workspace",
            timeout=run_timeout,
            packages=checker_uv_packages(root, checker_text),
            python_version=uv_python_version(),
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
            "crashed": process.returncode != 0,
            "runtime_not_assessable": False,
            "runtime_not_assessable_reason": None,
            "runtime_provenance": runtime_provenance,
            "checker_dependency_env": runtime_provenance,
            "verifier_entrypoint": "tests/test.sh",
            "direct_checker_harness": False,
            "runtime_package_contains_solution": (
                package_dir / "solution"
            ).exists(),
            "component": component,
            "lane": probe_lane(case_name),
            "probe_origin": (
                "SCHEMA_DERIVED_DETERMINISTIC"
                if probe_lane(case_name) == "deterministic_core"
                else "SCHEMA_SHAPED_SYNTHETIC_ATTACK"
            ),
            "runtime_outputs_dir": str(outputs_dir),
            "runtime_entrypoint": "tests/test.sh",
        }
    finally:
        pass


def finding(
    severity: str,
    code: str,
    message: str,
    test_type: str,
    evidence: dict[str, Any],
) -> dict[str, Any]:
    lane = (
        "deterministic_core"
        if test_type in DETERMINISTIC_CORE_CASES
        or test_type.startswith("partial__")
        else "quality_results"
    )
    return {
        "severity": severity,
        "code": code,
        "message": message,
        "test_type": test_type,
        "evidence": evidence,
        "lane": lane,
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
            core_runtime = probe_lane(case) == "deterministic_core"
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
            if core_runtime:
                crash_evidence["deterministic_core"] = True
            findings.append(
                finding(
                    "HIGH",
                    (
                        "CORE_RUNTIME_CHECKER_CRASH"
                        if core_runtime
                        else "CHECKER_CRASH"
                    ),
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
            core_runtime = probe_lane(case) == "deterministic_core"
            if core_runtime:
                unusable_evidence["deterministic_core"] = True
            findings.append(
                finding(
                    "HIGH",
                    (
                        "CORE_RUNTIME_RESULT_UNUSABLE"
                        if core_runtime
                        else "CHECKER_RESULT_UNUSABLE"
                    ),
                    "checker did not emit a usable reward/breakdown result "
                    f"for {case}",
                    case,
                    unusable_evidence,
                )
            )
            continue
        assert isinstance(reward, float)
        if case == "malformed_outputs" and reward >= pass_threshold:
            findings.append(
                finding(
                    "HIGH",
                    "CORE_RUNTIME_MALFORMED_INPUT_PASSES",
                    "schema-derived malformed input receives a passing reward",
                    case,
                    {
                        "reward": reward,
                        "pass_threshold": pass_threshold,
                        "deterministic_core": True,
                    },
                )
            )
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
        if case == "positive_oracle" and reward < pass_threshold:
            findings.append(
                finding(
                    "HIGH",
                    "CORE_RUNTIME_ORACLE_REJECTED",
                    "isolated solution positive mock does not pass the checker",
                    case,
                    {"status": "REJECTED", "deterministic_core": True},
                )
            )
    def usable_score(case: str) -> float | None:
        result = by_case.get(case)
        return result["reward"] if usable_probe_result(result) else None

    full = usable_score("positive_oracle")
    partial_scores = [
        result["reward"]
        for result in results
        if result["case"].startswith("partial__")
        and usable_probe_result(result)
    ]
    all_wrong = usable_score("all_wrong")
    if (
        full is not None
        and partial_scores
        and all_wrong is not None
        and not (
            full > max(partial_scores) + 1e-6
            and min(partial_scores) > all_wrong + 1e-6
        )
    ):
        by_case["all_wrong"]["ordering_assessment"] = {
            "status": "NOT_ASSESSABLE",
            "reason": (
                "declared scoring semantics do not establish strict "
                "full > partial > all_wrong ordering"
            ),
        }
    return findings


def sanitized_oracle_evidence(
    result: dict[str, Any], pass_threshold: float
) -> dict[str, Any]:
    """Persist Oracle status/provenance without checker-controlled values."""
    usable = usable_probe_result(result)
    return {
        "case": "positive_oracle",
        "mode": "positive_oracle",
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
        "probe_origin": "ORACLE_POSITIVE_MOCK",
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
    root: Path, output: Path
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
    random.seed(17)
    probe_workspace = (
        output.parent
        / "deterministic_core"
        / "probe_cases"
        / output.stem
    )
    probe_workspace.mkdir(parents=True, exist_ok=True)
    attack_applicability = task_family_applicability(root, specification)
    oracle_temporary, oracle_output, oracle_evidence = prepare_solution_oracle(
        root, specification
    )
    cases: list[tuple[str, str, Path | None, dict[str, Any] | None]] = [
        ("missing_outputs", "missing", None, None),
        ("empty_valid_shape", "empty", None, None),
        ("malformed_outputs", "malformed", None, None),
        ("random_baseline", "random", None, None),
        ("minimal_gold_shape", "minimal", None, None),
        ("duplicate_gold_rows", "duplicate", None, None),
        ("nonfinite_values", "nonfinite", None, None),
        *(
            (
                case_name,
                mode,
                None,
                None,
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
                "positive_oracle",
                oracle_output,
                None,
            )
        )
        schema_probe_plan, schema_probe_reason = schema_derived_probe_plan(
            specification, oracle_output
        )
        cases.extend(
            (
                item["case"],
                item["mode"],
                oracle_output,
                item["components"][0] if item["mode"] == "partial" else None,
            )
            for item in schema_probe_plan
        )
    else:
        schema_probe_plan, schema_probe_reason = [], (
            "the isolated Oracle did not produce a full contracted output"
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
                probe_workspace,
                isolated_component,
            )
            for (
                case_name,
                mode,
                source_output,
                isolated_component,
            ) in cases
        ]
    finally:
        if oracle_temporary is not None:
            oracle_temporary.cleanup()
    findings = evaluate_results(results, pass_threshold)
    task_attacks = task_family_attack_coverage(
        results, pass_threshold, attack_applicability
    )
    expected = {
        "missing_outputs": "score below pass threshold without crashing",
        "empty_valid_shape": "score below pass threshold without crashing",
        "malformed_outputs": "score below pass threshold without crashing",
        "random_baseline": "score below pass threshold",
        "minimal_gold_shape": "score below pass threshold",
        "duplicate_gold_rows": "duplicates do not create a passing score",
        "nonfinite_values": "non-finite values score below pass threshold",
        "positive_oracle": (
            "isolated solution mock passes without becoming scientific evidence"
        ),
        "all_wrong": (
            "a schema-derived mutation of every declared component scores "
            "no higher than the full Oracle integration case"
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
            if result["case"].startswith("partial__")
        }
    )
    tests = []
    probe_classes = {
        "positive_oracle": "positive",
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
            "negative"
            if result["case"] in TASK_FAMILY_CASES
            else probe_classes.get(result["case"], "negative")
        )
        tests.append(
            {
                "test_id": f"CHECKER-{index:03d}",
                "test_type": result["case"],
                "probe_class": probe_class,
                "lane": result.get("lane", probe_lane(result["case"])),
                "probe_origin": result.get("probe_origin"),
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
        "schema_version": CHECKER_TESTS_SCHEMA_VERSION,
        "benchmark_root": str(root),
        "checker_path": "tests/checker.py",
        "runtime": {
            "verifier_entrypoint": "tests/test.sh",
            "runtime_provenance": "sandbox",
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
        "deterministic_core": {
            "schema_version": DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
            "probe_origin": "SCHEMA_DERIVED_DETERMINISTIC",
            "case_names": [
                result["case"]
                for result in results
                if probe_lane(result["case"]) == "deterministic_core"
            ],
            "ordering_assertions": [
                {
                    "cases": [
                        "positive_oracle",
                        *[
                            result["case"]
                            for result in results
                            if result["case"].startswith("partial__")
                        ],
                        "all_wrong",
                    ],
                    "assertion": "full >= partial >= all_wrong",
                    "status": (
                        "NOT_ASSESSABLE"
                        if not any(
                            result["case"].startswith("partial__")
                            for result in results
                        )
                        else "RECORDED"
                    ),
                }
            ],
            "not_applicable_reason": schema_probe_reason,
            "agent_authored": False,
        },
        "quality_results": {
            "schema_version": QUALITY_PROBE_RESULTS_SCHEMA_VERSION,
            "case_names": [],
            "agent_authored": False,
        },
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
                    else "discrimination is Agent-quality evidence and has no deterministic fixture API"
                ),
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "external_result_directory_accepted": False,
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
                    else "equivalence is Agent-quality evidence and has no deterministic fixture API"
                ),
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "external_result_directory_accepted": False,
                },
            },
            "component_isolation": {
                "status": "NOT_APPLICABLE",
                "reason": "component isolation is quality evidence and has no deterministic fixture API",
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "external_result_directory_accepted": False,
                    "cases_planned": 0,
                    "cases_executed": 0,
                },
            },
        },
        "runtime_provenance": {
            "status": "ASSESSED",
            "entrypoint": "tests/test.sh",
            "runtime_provenance": "sandbox",
            "execution_mode": "DISPOSABLE_DOCKER_SANDBOX",
            "cases_executed": len(results),
        },
        "limitations": [
            "schema-shaped synthetic outputs do not establish scientific correctness",
            "discrimination, equivalence, and component isolation remain Agent-quality assessments",
            "generated probe cases are stored only in the external audit workspace",
            "checker cases run in the disposable qa-checker Docker sandbox",
            "checker execution has Docker network disabled; long-tail dependencies must be available as wheels during sandbox preparation",
            *(
                [
                    "The Harbor verifier entrypoint was unavailable: "
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
    arguments = parser.parse_args()
    try:
        result = dynamic_checker_probe(
            locate_root(Path(arguments.input)),
            Path(arguments.output).expanduser().resolve(),
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
