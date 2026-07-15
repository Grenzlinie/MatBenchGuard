#!/usr/bin/env python3
"""Run deterministic E0 checks for one materials Harbor 题包."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None

from prepare_audit_output import REQUIRED_ROLES, basename, locate_root


SEVERITY_RANK = {"FATAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
MATERIAL_TERMS = {
    "object": (
        "material",
        "crystal",
        "lattice",
        "alloy",
        "metal",
        "ceramic",
        "polymer",
        "surface",
        "interface",
        "defect",
        "copper",
        "graphene",
        "phonon",
    ),
    "data": (
        "cif",
        "poscar",
        "structure",
        "elastic constant",
        "density",
        "lattice parameter",
        "dispersion",
        "stress-strain",
        "trajectory",
        "phase diagram",
    ),
    "operation": (
        "compute",
        "calculate",
        "simulation",
        "density functional",
        "dft",
        "molecular dynamics",
        "phonopy",
        "calphad",
        "neb",
        "numerical",
        "recompute",
    ),
    "endpoint": (
        "frequency",
        "energy",
        "band gap",
        "modulus",
        "thermal conductivity",
        "migration barrier",
        "phase stability",
        "adsorption",
        "strength",
        "material property",
        "dispersion curve",
    ),
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_role(path: Path, role_type: str) -> Any:
    if role_type == "json":
        return read_json(path)
    if role_type == "toml":
        if tomllib is None:
            raise RuntimeError("tomllib is unavailable")
        with path.open("rb") as handle:
            return tomllib.load(handle)
    return path.read_text(encoding="utf-8", errors="replace")


def has_term(text: str, term: str) -> bool:
    if " " in term or "-" in term or len(term) > 4:
        return term in text
    return (
        re.search(
            r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])", text
        )
        is not None
    )


def materials_prescreen(text: str) -> dict[str, Any]:
    lowered = text.lower()
    evidence = {
        axis: sorted({term for term in terms if has_term(lowered, term)})[:16]
        for axis, terms in MATERIAL_TERMS.items()
    }
    present_axes = [axis for axis, hits in evidence.items() if hits]
    if all(evidence[axis] for axis in ("object", "operation", "endpoint")):
        classification = "MAT_CORE"
    elif evidence["operation"] and evidence["endpoint"] and len(present_axes) >= 2:
        classification = "MAT_METHOD"
    elif evidence["object"] and len(present_axes) == 1:
        classification = "MAT_WRAPPER"
    elif not evidence["object"] and not evidence["endpoint"]:
        classification = "NON_MAT"
    else:
        classification = "AMBIGUOUS"
    return {
        "classification": classification,
        "axes_present": present_axes,
        "evidence": evidence,
        "authoritative": False,
    }


def add_issue(
    issues: list[dict[str, Any]],
    severity: str,
    code: str,
    message: str,
    evidence: Any = None,
    affected_files: list[str] | None = None,
) -> None:
    issue: dict[str, Any] = {
        "severity": severity,
        "code": code,
        "message": message,
        "affected_files": affected_files or [],
    }
    if evidence is not None:
        issue["evidence"] = evidence
    issues.append(issue)


def parse_roles(
    root: Path, issues: list[dict[str, Any]]
) -> tuple[dict[str, Any], dict[str, str]]:
    values: dict[str, Any] = {}
    status: dict[str, str] = {}
    for role, role_type in REQUIRED_ROLES.items():
        path = root / role
        if not path.exists():
            severity = (
                "FATAL"
                if role
                in {
                    "instruction.md",
                    "tests/grading_spec.json",
                    "tests/checker.py",
                }
                else "HIGH"
            )
            add_issue(
                issues,
                severity,
                "MISSING_FILE",
                f"missing required Harbor role: {role}",
                affected_files=[role],
            )
            status[role] = "missing"
            continue
        try:
            values[role] = read_role(path, role_type)
            status[role] = "ok"
        except Exception as exc:  # noqa: BLE001
            status[role] = f"error: {exc}"
            add_issue(
                issues,
                "FATAL",
                "PARSE_ERROR",
                f"cannot parse required Harbor role: {role}",
                repr(exc),
                [role],
            )
    if not (root / "solution").is_dir():
        add_issue(
            issues,
            "HIGH",
            "SOLUTION_ROLE_MISSING",
            "solution role is absent; presence can be confirmed without inspection",
            affected_files=["solution/"],
        )
    status["solution/"] = (
        "present_not_inspected"
        if (root / "solution").is_dir()
        else "missing"
    )
    return values, status


def normalize_grading_specification(
    value: Any, issues: list[dict[str, Any]]
) -> dict[str, Any]:
    violations: list[str] = []
    if not isinstance(value, dict):
        violations.append("root must be an object")
        specification: dict[str, Any] = {}
    else:
        specification = dict(value)

    contract = specification.get("output_contract", {})
    if not isinstance(contract, dict):
        violations.append("output_contract must be an object")
        contract = {}
    outputs = contract.get("outputs", [])
    if not isinstance(outputs, list) or not all(
        isinstance(item, dict) for item in outputs
    ):
        violations.append("output_contract.outputs must be a list of objects")
        outputs = []
    specification["output_contract"] = {"outputs": outputs}

    raw_steps = specification.get(
        "steps", specification.get("checks", [])
    )
    if not isinstance(raw_steps, list) or not all(
        isinstance(item, dict) for item in raw_steps
    ):
        violations.append("steps or checks must be a list of objects")
        raw_steps = []
    specification["steps"] = raw_steps
    if violations:
        add_issue(
            issues,
            "FATAL",
            "INVALID_GRADING_SPEC_SCHEMA",
            "grading specification has invalid structural types",
            violations,
            ["tests/grading_spec.json"],
        )
    return specification


def cross_file_checks(
    instruction: str,
    steps: list[dict[str, Any]],
    specification: dict[str, Any],
    issues: list[dict[str, Any]],
) -> dict[str, list[str]]:
    grading_steps = (
        specification.get("steps", specification.get("checks", [])) or []
    )
    contract_outputs = {
        basename(item.get("file"))
        for item in (
            (specification.get("output_contract", {}) or {}).get("outputs", [])
            or []
        )
        if basename(item.get("file"))
    }
    step_outputs = {
        basename(item.get("output_file"))
        for item in steps
        if basename(item.get("output_file"))
    }
    step_evidence = {
        basename(item.get("evidence"))
        for item in steps
        if basename(item.get("evidence"))
    }
    grading_outputs = {
        basename(item.get("output_file"))
        for item in grading_steps
        if basename(item.get("output_file"))
    }
    instruction_outputs = set(
        re.findall(r"/app/outputs/([A-Za-z0-9_.-]+)", instruction)
    )
    for name in sorted(step_outputs - contract_outputs):
        add_issue(
            issues,
            "HIGH",
            "OUTPUT_NOT_CONTRACTED",
            f"workflow output is absent from output contract: {name}",
            affected_files=["steps.json", "tests/grading_spec.json"],
        )
    for name in sorted(contract_outputs - grading_outputs):
        add_issue(
            issues,
            "HIGH",
            "OUTPUT_NOT_SCORED",
            f"contract output is not referenced by grading steps: {name}",
            affected_files=["tests/grading_spec.json"],
        )
    for name in sorted(step_evidence - contract_outputs):
        add_issue(
            issues,
            "HIGH",
            "EVIDENCE_NOT_ENFORCED",
            f"declared evidence is absent from output contract: {name}",
            affected_files=["steps.json", "tests/grading_spec.json"],
        )
    for name in sorted(
        instruction_outputs - (contract_outputs | step_outputs | step_evidence)
    ):
        add_issue(
            issues,
            "MEDIUM",
            "INSTRUCTION_ONLY_OUTPUT",
            f"instruction output is absent from structured contracts: {name}",
            affected_files=["instruction.md"],
        )
    return {
        "step_outputs": sorted(step_outputs),
        "step_evidence": sorted(step_evidence),
        "contract_outputs": sorted(contract_outputs),
        "grading_outputs": sorted(grading_outputs),
        "instruction_outputs": sorted(instruction_outputs),
    }


def grading_checks(
    specification: dict[str, Any], issues: list[dict[str, Any]]
) -> None:
    grading_steps = (
        specification.get("steps", specification.get("checks", [])) or []
    )
    weights: list[float] = []
    for step in grading_steps:
        try:
            weights.append(float(step.get("weight", 0)))
        except (TypeError, ValueError):
            add_issue(
                issues,
                "HIGH",
                "INVALID_WEIGHT",
                "grading weight is not numeric",
                step.get("weight"),
                ["tests/grading_spec.json"],
            )
    if weights and abs(sum(weights) - 1.0) > 1e-6:
        add_issue(
            issues,
            "HIGH",
            "WEIGHTS_NOT_ONE",
            "grading weights do not sum to one",
            sum(weights),
            ["tests/grading_spec.json"],
        )
    raw_threshold = specification.get("pass_threshold")
    threshold: float | None = None
    try:
        threshold = float(raw_threshold)
        if not math.isfinite(threshold) or not 0 <= threshold <= 1:
            raise ValueError
    except (TypeError, ValueError):
        add_issue(
            issues,
            "FATAL",
            "INVALID_PASS_THRESHOLD",
            "pass threshold must be a finite number between zero and one",
            raw_threshold,
            ["tests/grading_spec.json"],
        )
    if (
        len(weights) > 1
        and threshold is not None
        and max(weights) >= threshold
    ):
        add_issue(
            issues,
            "HIGH",
            "SINGLE_COMPONENT_CAN_PASS",
            "one of several grading components can pass the 题包 alone",
            {"largest_weight": max(weights), "pass_threshold": threshold},
            ["tests/grading_spec.json"],
        )


def static_audit(root: Path, output: Path) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    role_values, parse_status = parse_roles(root, issues)
    instruction = str(role_values.get("instruction.md", ""))
    steps = role_values.get("steps.json", [])
    resources = role_values.get("resources.json", {})
    manifest = role_values.get("manifest.json", {})
    specification = normalize_grading_specification(
        role_values.get("tests/grading_spec.json", {}), issues
    )
    combined = "\n".join(
        (
            instruction,
            json.dumps(steps, ensure_ascii=False),
            json.dumps(resources, ensure_ascii=False),
            json.dumps(manifest, ensure_ascii=False),
        )
    )
    qualification = materials_prescreen(combined)
    if qualification["classification"] in {"NON_MAT", "AMBIGUOUS"}:
        add_issue(
            issues,
            "HIGH",
            "MATERIALS_ADMISSIBILITY_REQUIRES_ADJUDICATION",
            "lexical evidence cannot authoritatively decide materials admissibility",
            qualification["evidence"],
        )
    cross_file_sets = cross_file_checks(
        instruction,
        steps if isinstance(steps, list) else [],
        specification if isinstance(specification, dict) else {},
        issues,
    )
    grading_checks(
        specification if isinstance(specification, dict) else {}, issues
    )
    maximum = max(
        (SEVERITY_RANK[item["severity"]] for item in issues), default=0
    )
    static_verdict = (
        "REJECT"
        if maximum >= SEVERITY_RANK["FATAL"]
        else "CONDITIONAL"
        if maximum >= SEVERITY_RANK["MEDIUM"]
        else "PASS"
    )
    result = {
        "schema_version": "0.1",
        "benchmark_root": str(root),
        "solution_content_inspected": False,
        "parse_status": parse_status,
        "materials_prescreen": qualification,
        "cross_file_sets": cross_file_sets,
        "issues": sorted(
            issues,
            key=lambda item: (-SEVERITY_RANK[item["severity"]], item["code"]),
        ),
        "static_verdict": static_verdict,
        "limitations": [
            "materials classification is lexical evidence for Agent adjudication",
            "resource reachability is not tested in this slice",
            "paper fidelity is not tested in no-paper mode",
            "task-family-specific attacks are implemented in later slices",
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output", default="audit_static.json")
    arguments = parser.parse_args()
    try:
        result = static_audit(
            locate_root(Path(arguments.input)),
            Path(arguments.output).expanduser().resolve(),
        )
        print(
            json.dumps(
                {
                    "static_verdict": result["static_verdict"],
                    "issue_count": len(result["issues"]),
                    "output": arguments.output,
                },
                indent=2,
            )
        )
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"static audit failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
