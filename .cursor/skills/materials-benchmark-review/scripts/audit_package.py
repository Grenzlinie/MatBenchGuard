#!/usr/bin/env python3
"""Run deterministic E0 checks for one materials Harbor 题包."""

from __future__ import annotations

import argparse
import ast
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

from prepare_audit_output import (
    QUALITY_EVIDENCE_ROLES,
    REQUIRED_ROLES,
    basename,
    locate_root,
)


SEVERITY_RANK = {"FATAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
# Materials admissibility (C01) is decided by the Agent reading the
# instruction's structured fields (## Problem background / ## Approach /
# ## Reproduction target).  The deterministic layer no longer owns a keyword
# term list: it only records that a classification is required and validates the
# Agent's authoritative quotes elsewhere (validate_materials_qualification).
INSTRUCTION_CLASSIFICATION_FIELDS = (
    "Problem background",
    "Approach",
    "Reproduction target",
)
CORE_ROLE_NAMES = {
    "core",
    "core_output",
    "final",
    "final_output",
    "scored",
    "scored_output",
}
PROCESS_ROLE_NAMES = {
    "diagnostic",
    "intermediate",
    "process",
    "process_artifact",
    "process_evidence",
}
LOAD_BEARING_ARTIFACTS = (
    "crystal structure",
    "mesh",
    "model",
    "prediction artifact",
    "prediction field",
    "predictive field",
    "structure",
    "trajectory",
)
OUTPUT_PATH_PATTERN = re.compile(
    r"/app/outputs/([A-Za-z0-9_.-]+)", re.IGNORECASE
)


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


def _classify_declaration_role(
    requirement: dict[str, Any], declaration: dict[str, Any]
) -> str:
    if _is_load_bearing_artifact(requirement, declaration):
        return "CORE_OUTPUT"
    role = re.sub(
        r"[\s-]+",
        "_",
        str(requirement.get("role") or "").strip().lower(),
    )
    if any(
        role == name or role.startswith(name + "_")
        for name in PROCESS_ROLE_NAMES
    ):
        return "PROCESS_ONLY"
    if any(
        role == name or role.startswith(name + "_")
        for name in CORE_ROLE_NAMES
    ):
        return "CORE_OUTPUT"
    if role:
        return "UNCLASSIFIED"
    if declaration.get("kind") == "process_evidence":
        return "PROCESS_ONLY"
    if declaration.get("kind") == "scored_output":
        return "CORE_OUTPUT"
    return "UNCLASSIFIED"


def _is_load_bearing_artifact(
    requirement: dict[str, Any], declaration: dict[str, Any]
) -> bool:
    context = " ".join(
        str(requirement.get(key) or "")
        for key in ("title", "agent_work")
    )
    context += " " + str(declaration.get("quote") or "")
    lowered = context.lower()
    return any(
        re.search(
            rf"\b(?:complete|full|load-bearing)\b"
            rf"(?:\s+[a-z0-9_-]+){{0,4}}\s+{re.escape(artifact)}\b",
            lowered,
        )
        for artifact in LOAD_BEARING_ARTIFACTS
    )


def _has_process_annotation(
    requirement: dict[str, Any], declaration: dict[str, Any]
) -> bool:
    role = re.sub(
        r"[\s-]+",
        "_",
        str(requirement.get("role") or "").strip().lower(),
    )
    core_role = any(
        role == name or role.startswith(name + "_")
        for name in CORE_ROLE_NAMES
    )
    process_role = any(
        role == name or role.startswith(name + "_")
        for name in PROCESS_ROLE_NAMES
    )
    return process_role or (
        not core_role and declaration.get("kind") == "process_evidence"
    )


def materials_classification_stub(text: str) -> dict[str, Any]:
    """Record that materials admissibility must be Agent-adjudicated.

    The deterministic layer no longer classifies packages from a keyword term
    list.  Classification (C01) is decided by the Agent reading the
    instruction's ``## Problem background`` / ``## Approach`` /
    ``## Reproduction target`` fields and is validated as authoritative quotes
    by ``validate_materials_qualification`` in ``run_review.py``.  When the
    Agent supplies no authoritative classification the package is
    ``NOT_ASSESSABLE`` (it is never passed via keywords).
    """
    present_fields = [
        field
        for field in INSTRUCTION_CLASSIFICATION_FIELDS
        if re.search(
            rf"^#{{1,6}}\s+{re.escape(field)}\s*$",
            text,
            re.IGNORECASE | re.MULTILINE,
        )
    ]
    return {
        "classification": "NOT_PROVIDED",
        "authoritative": False,
        "method": "agent_structured_fields",
        "structured_fields_present": present_fields,
        "structured_fields_expected": list(INSTRUCTION_CLASSIFICATION_FIELDS),
        "note": (
            "Materials admissibility is decided by the Agent from the "
            "instruction's structured fields; no keyword prescreen is applied."
        ),
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


def _append_unique(values: list[str], value: str) -> None:
    if value and value not in values:
        values.append(value)


def _output_name_from_path_match(path_match: re.Match[str]) -> str:
    """Return a declared output name without adjacent prose punctuation.

    The permissive path pattern intentionally accepts dots within filenames,
    but that also captures a sentence-final period in an unquoted reference
    such as ``/app/outputs/result.csv.``.  A period immediately followed by a
    closing backtick is part of an explicitly quoted path; otherwise trailing
    periods are prose punctuation rather than part of the Harbor output name.
    """
    output_name = path_match.group(1)
    following_text = path_match.string[path_match.end() :]
    if output_name.endswith(".") and not following_text.startswith("`"):
        return output_name.rstrip(".")
    return output_name


def instruction_contract_map(instruction: str) -> dict[str, Any]:
    """Extract the role-aware instruction-to-output contract.

    Harbor instructions commonly name process artifacts alongside final
    submissions.  A path-only scan cannot distinguish those roles, so this
    parser keeps the workflow step, agent action, role, and declared outputs
    together for later checker mapping.
    """
    requirements: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    all_outputs: list[str] = []

    def flush() -> None:
        nonlocal current
        if current is not None:
            requirements.append(current)
        current = None

    for line_number, raw_line in enumerate(instruction.splitlines(), start=1):
        line = raw_line.strip()
        heading = re.match(r"^###\s+Step\s+(\d+)\s*(.*)$", line)
        if heading:
            flush()
            current = {
                "step": f"Step {heading.group(1)}",
                "title": heading.group(2).strip(),
                "line": line_number,
                "quote": line,
                "role": None,
                "agent_work": None,
                "declared_outputs": [],
                "evidence": [],
                "classification": "UNCLASSIFIED",
            }
            continue
        if re.match(r"^#{1,6}\s+", line):
            flush()
            continue
        role_match = re.match(r"^-\s*Role:\s*(.+?)\s*$", line, re.IGNORECASE)
        if role_match and current is not None:
            current["role"] = role_match.group(1).strip()
            continue
        action_match = re.match(
            r"^-\s*Action:\s*(.+?)\s*$", line, re.IGNORECASE
        )
        if action_match and current is not None:
            current["agent_work"] = action_match.group(1).strip()
            continue
        path_matches = list(OUTPUT_PATH_PATTERN.finditer(line))
        if not path_matches:
            continue
        for path_match in path_matches:
            output_name = _output_name_from_path_match(path_match)
            _append_unique(all_outputs, output_name)
            if current is None:
                continue
            declaration_kind = (
                "process_evidence"
                if re.match(r"^-\s*Evidence:", line, re.IGNORECASE)
                else "scored_output"
                if re.match(r"^-\s*Output file:", line, re.IGNORECASE)
                else "output_reference"
            )
            declaration = {
                "file": output_name,
                "kind": declaration_kind,
                "line": line_number,
                "quote": line,
            }
            current["evidence"].append(declaration)
            _append_unique(current["declared_outputs"], output_name)

    flush()
    requirements = [
        item
        for item in requirements
        if item["role"] or item["agent_work"] or item["evidence"]
    ]
    process_evidence: list[str] = []
    scored_outputs: list[str] = []
    load_bearing_outputs: list[str] = []
    role_conflicts: list[dict[str, Any]] = []
    for requirement in requirements:
        declaration_roles: list[str] = []
        requirement_conflict = False
        for declaration in requirement["evidence"]:
            output_name = declaration["file"]
            load_bearing = _is_load_bearing_artifact(
                requirement, declaration
            )
            role_classification = _classify_declaration_role(
                requirement, declaration
            )
            declaration["role_classification"] = role_classification
            if load_bearing and _has_process_annotation(
                requirement, declaration
            ):
                requirement_conflict = True
                declaration["annotation_conflict"] = (
                    "PROCESS_ANNOTATION_CONTRADICTS_CORE_SEMANTICS"
                )
                role_conflicts.append(
                    {
                        "file": output_name,
                        "line": declaration["line"],
                        "quote": declaration["quote"],
                        "declared_role": requirement.get("role"),
                        "resolved_role": "CORE_OUTPUT",
                        "semantic_context": {
                            "title": requirement.get("title"),
                            "agent_work": requirement.get("agent_work"),
                        },
                    }
                )
            declaration_roles.append(role_classification)
            if role_classification == "CORE_OUTPUT":
                _append_unique(scored_outputs, output_name)
                if load_bearing:
                    _append_unique(load_bearing_outputs, output_name)
            elif role_classification == "PROCESS_ONLY":
                _append_unique(process_evidence, output_name)
        if requirement_conflict:
            requirement["classification"] = "UNCLASSIFIED"
        else:
            requirement["classification"] = (
                declaration_roles[0]
                if declaration_roles
                and all(
                    item == declaration_roles[0]
                    for item in declaration_roles
                )
                else "UNCLASSIFIED"
            )
    unclassified = [
        name
        for name in all_outputs
        if name not in process_evidence
        and name not in scored_outputs
        and name not in load_bearing_outputs
    ]
    return {
        "requirements": requirements,
        "instruction_outputs": sorted(all_outputs),
        "process_evidence": sorted(process_evidence),
        "scored_outputs": sorted(scored_outputs),
        "load_bearing_outputs": sorted(load_bearing_outputs),
        "core_outputs": sorted(
            set(scored_outputs) | set(load_bearing_outputs)
        ),
        "unclassified_outputs": sorted(unclassified),
        "role_conflicts": role_conflicts,
    }


def _instruction_sections(instruction: str) -> dict[str, str]:
    """Split an instruction into its top-level ``## `` sections."""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for raw_line in instruction.splitlines():
        heading = re.match(r"^##\s+(.+?)\s*$", raw_line)
        if heading and not raw_line.startswith("###"):
            current = heading.group(1).strip().lower()
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(raw_line)
    return {name: "\n".join(body) for name, body in sections.items()}


def _section_output_basenames(body: str, *, scored_only: bool = False) -> set[str]:
    names: set[str] = set()
    for line in body.splitlines():
        if scored_only and not re.match(
            r"^\s*-\s*Output file\s*:", line, re.IGNORECASE
        ):
            continue
        for match in OUTPUT_PATH_PATTERN.finditer(line):
            names.add(_output_name_from_path_match(match))
    return names


def _selfcheck_output_basenames(body: str) -> set[str]:
    names: set[str] = set()
    for match in re.finditer(r"\"file\"\s*:\s*\"([^\"]+)\"", body):
        names.add(basename(match.group(1)))
    names.update(_section_output_basenames(body))
    return names


def instruction_internal_consistency(
    instruction: str, issues: list[dict[str, Any]]
) -> dict[str, Any]:
    """D2: check instruction sections declare the same scored outputs.

    Compares the scored/declared output filenames across the ``Workflow
    steps``, ``Output files``, ``Output contract``, and optional
    ``Self-check`` sections.  A mismatch between any two present, non-empty
    sections is a repairable ``INSTRUCTION_INTERNAL_INCONSISTENCY`` finding.
    """
    sections = _instruction_sections(instruction)

    def find_section(*keywords: str) -> str | None:
        for name, body in sections.items():
            if all(keyword in name for keyword in keywords):
                return body
        return None

    workflow_body = find_section("workflow")
    output_files_body = find_section("output", "files")
    output_contract_body = find_section("output", "contract")
    selfcheck_body = find_section("self-check") or find_section("self", "check")

    declared: dict[str, set[str]] = {}
    if workflow_body is not None:
        declared["Workflow steps"] = _section_output_basenames(
            workflow_body, scored_only=True
        )
    if output_files_body is not None:
        declared["Output files"] = _section_output_basenames(output_files_body)
    if output_contract_body is not None:
        declared["Output contract"] = _section_output_basenames(
            output_contract_body
        )
    if selfcheck_body is not None:
        declared["Self-check"] = _selfcheck_output_basenames(selfcheck_body)

    present = {name: values for name, values in declared.items() if values}
    mismatches: list[dict[str, Any]] = []
    section_names = sorted(present)
    for index, left in enumerate(section_names):
        for right in section_names[index + 1 :]:
            if present[left] != present[right]:
                mismatches.append(
                    {
                        "left_section": left,
                        "right_section": right,
                        "only_in_left": sorted(present[left] - present[right]),
                        "only_in_right": sorted(present[right] - present[left]),
                    }
                )
    if mismatches:
        add_issue(
            issues,
            "MEDIUM",
            "INSTRUCTION_INTERNAL_INCONSISTENCY",
            "instruction sections declare inconsistent scored outputs across "
            "Workflow steps / Output files / Output contract / Self-check",
            {"mismatches": mismatches},
            ["instruction.md"],
        )
    return {
        "sections_present": sorted(sections),
        "declared_outputs_by_section": {
            name: sorted(values) for name, values in declared.items()
        },
        "consistent": not mismatches,
        "mismatches": mismatches,
    }


def _direct_returns(function: ast.FunctionDef | ast.AsyncFunctionDef) -> list[ast.Return]:
    """Return return statements owned by a function, excluding nested funcs."""
    returns: list[ast.Return] = []

    def visit(node: ast.AST) -> None:
        for child in ast.iter_child_nodes(node):
            if isinstance(
                child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
            ):
                continue
            if isinstance(child, ast.Return):
                returns.append(child)
                continue
            visit(child)

    visit(function)
    return returns


def _statements_guarantee_exit(statements: list[ast.stmt]) -> bool:
    """Conservatively prove that a statement list cannot fall through."""
    for statement in statements:
        if isinstance(statement, (ast.Return, ast.Raise)):
            return True
        if isinstance(statement, ast.If):
            if (
                statement.orelse
                and _statements_guarantee_exit(statement.body)
                and _statements_guarantee_exit(statement.orelse)
            ):
                return True
        if isinstance(statement, ast.Try):
            if statement.finalbody and _statements_guarantee_exit(
                statement.finalbody
            ):
                return True
            handlers_exit = bool(statement.handlers) and all(
                _statements_guarantee_exit(handler.body)
                for handler in statement.handlers
            )
            body_exit = _statements_guarantee_exit(statement.body)
            else_exit = (
                _statements_guarantee_exit(statement.orelse)
                if statement.orelse
                else body_exit
            )
            if body_exit and handlers_exit and else_exit:
                return True
    return False


def _return_status(
    function: ast.FunctionDef | ast.AsyncFunctionDef,
) -> tuple[str, list[ast.Return]]:
    returns = _direct_returns(function)
    if not returns:
        return "MISSING_DIRECT_RETURN", returns
    none_returns = [
        item
        for item in returns
        if item.value is None
        or (
            isinstance(item.value, ast.Constant)
            and item.value.value is None
        )
    ]
    if len(none_returns) == len(returns):
        return "ALWAYS_RETURNS_NONE", returns
    if none_returns:
        return "MAY_RETURN_NONE", returns
    if not _statements_guarantee_exit(function.body):
        return "PARTIAL_RETURN_PATHS", returns
    return "STATIC_RETURN_CANDIDATE", returns


def _requirement_chains(
    contract_map: dict[str, Any], checker_outputs: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    by_file = {item["file"]: item for item in checker_outputs}
    chains: list[dict[str, Any]] = []
    for requirement_index, requirement in enumerate(
        contract_map["requirements"]
    ):
        declarations = requirement["evidence"] or [None]
        for declaration_index, declaration in enumerate(declarations):
            if declaration is None:
                chains.append(
                    {
                        "requirement_index": requirement_index,
                        "declaration_index": None,
                        "instruction_requirement": {
                            "step": requirement.get("step"),
                            "title": requirement.get("title"),
                            "role": requirement.get("role"),
                            "line": requirement.get("line"),
                            "quote": requirement.get("quote"),
                        },
                        "agent_work": requirement.get("agent_work"),
                        "core_output": None,
                        "output_role": "unclassified",
                        "checker_read": "UNKNOWN_NO_DECLARED_OUTPUT",
                        "checker_score": {
                            "checker_scores": "UNKNOWN_NO_DECLARED_OUTPUT",
                            "runtime_score_proven": False,
                        },
                    }
                )
                continue
            output_name = declaration["file"]
            checker = by_file.get(output_name, {})
            chains.append(
                {
                    "requirement_index": requirement_index,
                    "declaration_index": declaration_index,
                    "instruction_requirement": {
                        "step": requirement.get("step"),
                        "title": requirement.get("title"),
                        "role": requirement.get("role"),
                        "line": declaration.get("line"),
                        "quote": declaration.get("quote"),
                    },
                    "agent_work": requirement.get("agent_work"),
                    "core_output": output_name,
                    "output_role": checker.get("role", "unclassified"),
                    "checker_read": checker.get(
                        "checker_reads", "UNKNOWN_NOT_ESTABLISHED"
                    ),
                    "checker_score": checker.get("checker_scoring")
                    or {
                        "checker_scores": "UNKNOWN_NOT_ESTABLISHED",
                        "runtime_score_proven": False,
                    },
                }
            )
    return chains


def checker_contract_analysis(
    checker_source: str,
    specification: dict[str, Any],
    contract_map: dict[str, Any],
    issues: list[dict[str, Any]],
) -> dict[str, Any]:
    """Map declared outputs to checker reads and runtime scoring functions."""
    tree: ast.AST | None = None
    parse_error: str | None = None
    analysis_available = bool(checker_source.strip())
    try:
        tree = ast.parse(checker_source)
    except SyntaxError as exc:
        parse_error = str(exc)

    scorer_functions: dict[str, ast.FunctionDef | ast.AsyncFunctionDef] = {}
    scorer_bindings: dict[str, str] = {}
    scorer_registry_declared = False
    if tree is not None:
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                scorer_functions[node.name] = node
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                targets = (
                    node.targets
                    if isinstance(node, ast.Assign)
                    else [node.target]
                )
                if not any(
                    isinstance(target, ast.Name) and target.id == "_SCORERS"
                    for target in targets
                ):
                    continue
                scorer_registry_declared = True
                value = node.value
                if not isinstance(value, ast.Dict):
                    continue
                for key, item in zip(value.keys, value.values):
                    if isinstance(key, ast.Constant) and isinstance(
                        key.value, str
                    ) and isinstance(item, ast.Name):
                        scorer_bindings[key.value] = item.id

    function_status: dict[str, dict[str, Any]] = {}
    missing_returns: list[str] = []
    incomplete_returns: list[str] = []
    always_zero: list[str] = []
    always_pass: list[str] = []
    division_by_zero: list[str] = []
    for scorer_id, function_name in scorer_bindings.items():
        function = scorer_functions.get(function_name)
        if function is None:
            function_status[scorer_id] = {
                "function": function_name,
                "status": "FUNCTION_MISSING",
            }
            continue
        status, returns = _return_status(function)
        if status == "MISSING_DIRECT_RETURN":
            missing_returns.append(scorer_id)
        elif status in {
            "ALWAYS_RETURNS_NONE",
            "MAY_RETURN_NONE",
            "PARTIAL_RETURN_PATHS",
        }:
            incomplete_returns.append(scorer_id)
        constants = [
            item.value
            for item in returns
            if isinstance(item.value, ast.Constant)
            and isinstance(item.value.value, (int, float))
            and not isinstance(item.value.value, bool)
        ]
        if status == "STATIC_RETURN_CANDIDATE" and len(constants) == len(returns):
            if all(value == 0 for value in constants):
                always_zero.append(scorer_id)
                status = "STATIC_ALWAYS_ZERO"
            elif all(value == 1 for value in constants):
                always_pass.append(scorer_id)
                status = "STATIC_ALWAYS_ONE"
        literal_zero_divisions = sum(
            isinstance(node, ast.BinOp)
            and isinstance(node.op, ast.Div)
            and isinstance(node.right, ast.Constant)
            and node.right.value == 0
            for node in ast.walk(function)
        )
        dynamic_divisions = sum(
            isinstance(node, ast.BinOp)
            and isinstance(node.op, ast.Div)
            and not (
                isinstance(node.right, ast.Constant)
                and isinstance(node.right.value, (int, float))
            )
            for node in ast.walk(function)
        )
        if literal_zero_divisions:
            division_by_zero.append(scorer_id)
        function_status[scorer_id] = {
            "function": function_name,
            "status": status,
            "direct_return_count": len(returns),
            "return_status": status,
            "finite_return_runtime_proven": False,
            "division_status": (
                "LITERAL_ZERO_DENOMINATOR"
                if literal_zero_divisions
                else "DYNAMIC_DENOMINATOR_REQUIRES_PROBE"
                if dynamic_divisions
                else "NO_DIVISION_FOUND_STATIC"
            ),
        }

    if analysis_available and parse_error is not None:
        add_issue(
            issues,
            "HIGH",
            "CHECKER_STATIC_ANALYSIS_UNAVAILABLE",
            "checker.py cannot be parsed for contract mapping",
            {"parse_error": parse_error},
            ["tests/checker.py"],
        )
    if analysis_available and missing_returns:
        add_issue(
            issues,
            "HIGH",
            "SCORER_MISSING_RETURN",
            "bound scoring functions do not return their computed score: "
            + ", ".join(sorted(missing_returns)),
            {
                "scorer_ids": sorted(missing_returns),
                "root_cause": "checker_scorer_runtime_contract",
            },
            ["tests/checker.py"],
        )
    if analysis_available and incomplete_returns:
        add_issue(
            issues,
            "HIGH",
            "SCORER_RETURN_NOT_TOTAL",
            "bound scoring functions may return None or fall through without "
            "a score: " + ", ".join(sorted(incomplete_returns)),
            {
                "scorer_ids": sorted(incomplete_returns),
                "statuses": {
                    scorer_id: function_status[scorer_id]["return_status"]
                    for scorer_id in sorted(incomplete_returns)
                },
                "root_cause": "checker_scorer_return_contract",
            },
            ["tests/checker.py"],
        )
    if analysis_available and always_zero:
        add_issue(
            issues,
            "HIGH",
            "ALWAYS_ZERO_SCORER",
            "bound scoring functions always return zero: "
            + ", ".join(sorted(always_zero)),
            {"scorer_ids": sorted(always_zero)},
            ["tests/checker.py"],
        )
    if analysis_available and always_pass:
        add_issue(
            issues,
            "HIGH",
            "ALWAYS_PASS_SCORER",
            "bound scoring functions always return one: "
            + ", ".join(sorted(always_pass)),
            {"scorer_ids": sorted(always_pass)},
            ["tests/checker.py"],
        )
    if analysis_available and division_by_zero:
        add_issue(
            issues,
            "HIGH",
            "DIVISION_BY_ZERO_LITERAL",
            "bound scoring functions contain literal division by zero: "
            + ", ".join(sorted(division_by_zero)),
            {"scorer_ids": sorted(division_by_zero)},
            ["tests/checker.py"],
        )

    grading_steps = specification.get("steps", []) or []
    process_outputs = set(contract_map.get("process_evidence", []))
    core_outputs = set(contract_map.get("core_outputs", []))
    grading_steps = [
        step
        for step in grading_steps
        if basename(step.get("output_file")) not in process_outputs
        or basename(step.get("output_file")) in core_outputs
    ]
    scorer_registry_present = scorer_registry_declared
    grading_by_file = {
        basename(step.get("output_file")): step
        for step in grading_steps
        if basename(step.get("output_file"))
    }
    contract_items = {
        basename(item.get("file")): item
        for item in (
            specification.get("output_contract", {}).get("outputs", [])
            or []
        )
        if basename(item.get("file"))
    }
    generic_loader = (
        tree is not None
        and "load_artifact" in checker_source
        and "output_file" in checker_source
        and "outputs_dir" in checker_source
    )
    outputs: list[dict[str, Any]] = []
    output_names = set(contract_map["instruction_outputs"])
    output_names.update(contract_items)
    for output_name in sorted(output_names):
        step = grading_by_file.get(output_name)
        contract_item = contract_items.get(output_name, {})
        if output_name in contract_map["process_evidence"]:
            role = "process_evidence"
        elif output_name in contract_map["scored_outputs"] or step is not None:
            role = "scored_output"
        else:
            role = str(contract_item.get("purpose") or "unclassified")
        step_id = str(step.get("id") or "") if step else None
        source_bound = (
            bool(step_id and step_id in scorer_bindings)
            if scorer_registry_present
            else False
        )
        scorer_function_exists = bool(
            step_id
            and scorer_bindings.get(step_id) in scorer_functions
        )
        declared_weight = step.get("weight") if step else None
        numeric_weight = _finite_number(declared_weight)
        if step is None:
            effective_weight_status = "NOT_APPLICABLE"
        elif numeric_weight is None:
            effective_weight_status = "UNKNOWN_INVALID_DECLARED_WEIGHT"
        elif numeric_weight == 0:
            effective_weight_status = "STATIC_ZERO_DECLARED_WEIGHT"
        elif source_bound and scorer_function_exists:
            effective_weight_status = (
                "STATIC_NONZERO_CANDIDATE_RUNTIME_NOT_PROVEN"
            )
        elif scorer_registry_present:
            effective_weight_status = "STATIC_UNBOUND_CANDIDATE_ZERO"
        else:
            effective_weight_status = "UNKNOWN_DIRECT_CHECKER"
        if not analysis_available:
            read_status = "UNKNOWN_CHECKER_MISSING"
        elif parse_error is not None:
            read_status = "UNKNOWN_CHECKER_UNPARSEABLE"
        elif generic_loader and step is not None:
            read_status = "STATIC_GENERIC_LOADER_CANDIDATE"
        elif re.search(
            rf"(?:open|read_text|read_bytes|load_artifact)"
            rf"[^\n]*{re.escape(output_name)}",
            checker_source,
            re.IGNORECASE,
        ) or re.search(
            rf"{re.escape(output_name)}[^\n]*"
            rf"(?:open|read_text|read_bytes|load_artifact)",
            checker_source,
            re.IGNORECASE,
        ):
            read_status = "STATIC_EXPLICIT_READ_CANDIDATE"
        elif output_name in checker_source:
            read_status = "STATIC_FILENAME_REFERENCE_ONLY"
        else:
            read_status = "UNKNOWN_NOT_ESTABLISHED"
        runtime_status = (
            function_status.get(step_id, {}).get(
                "status", "STATIC_BINDING_NOT_ESTABLISHED"
            )
            if scorer_registry_present
            else "RUNTIME_NOT_PROVEN"
        )
        outputs.append(
            {
                "file": output_name,
                "role": role,
                "instruction_declared": output_name
                in contract_map["instruction_outputs"],
                "structured_contract": output_name in contract_items,
                "checker_reads": read_status,
                "checker_read_runtime_proven": False,
                "checker_scoring": (
                    {
                        "step_id": step_id,
                        "declared_weight": declared_weight,
                        "effective_weight": (
                            0.0
                            if effective_weight_status
                            == "STATIC_ZERO_DECLARED_WEIGHT"
                            else None
                        ),
                        "effective_weight_status": effective_weight_status,
                        "scorer_bound": source_bound and scorer_function_exists,
                        "scorer_binding_status": (
                            "STATIC_SOURCE_BOUND"
                            if source_bound and scorer_function_exists
                            else "STATIC_FUNCTION_MISSING"
                            if source_bound
                            else "STATIC_NOT_BOUND"
                            if scorer_registry_present
                            else "UNKNOWN_DIRECT_CHECKER"
                        ),
                        "runtime_status": runtime_status,
                        "checker_scores": (
                            "STATIC_SCORER_CANDIDATE_RUNTIME_NOT_PROVEN"
                            if source_bound and scorer_function_exists
                            else "UNKNOWN_NOT_ESTABLISHED"
                        ),
                        "runtime_score_proven": False,
                    }
                    if step is not None
                    else None
                ),
            }
        )

    semantic_validation: dict[str, str] = {}
    for output in outputs:
        output_name = output["file"]
        if output_name not in core_outputs:
            continue
        read_status = output["checker_reads"]
        if not analysis_available or parse_error is not None:
            status = "UNKNOWN_CHECKER_UNAVAILABLE"
        elif not grading_steps and not contract_items:
            status = "UNKNOWN_GRADING_CONTRACT_UNAVAILABLE"
        elif read_status == "STATIC_FILENAME_REFERENCE_ONLY":
            existence_pattern = re.compile(
                rf"(?:exists|isfile|stat|access)[^\n]*"
                rf"{re.escape(output_name)}|"
                rf"{re.escape(output_name)}[^\n]*"
                rf"(?:exists|isfile|stat|access)",
                re.IGNORECASE,
            )
            status = (
                "EXISTENCE_ONLY"
                if existence_pattern.search(checker_source)
                else "STATIC_INDIRECT_REFERENCE_CANDIDATE"
            )
        elif read_status in {
            "STATIC_GENERIC_LOADER_CANDIDATE",
            "STATIC_EXPLICIT_READ_CANDIDATE",
        }:
            status = "STATIC_CONTENT_READ_CANDIDATE"
        elif read_status == "UNKNOWN_NOT_ESTABLISHED":
            status = "NOT_REFERENCED"
        elif read_status == "UNKNOWN_CHECKER_MISSING":
            status = "NOT_REFERENCED"
        else:
            status = "REFERENCE_ONLY"
        semantic_validation[output_name] = status
        output["semantic_validation"] = status
        if status in {"NOT_REFERENCED", "EXISTENCE_ONLY"}:
            add_issue(
                issues,
                "FATAL",
                "CHECKER_CORE_TASK_UNASSESSED",
                "load-bearing core output is ignored or only checked for "
                f"existence: {output_name}",
                {
                    "output": output_name,
                    "semantic_validation": status,
                    "role": "core_output",
                },
                ["instruction.md", "tests/checker.py", "tests/grading_spec.json"],
            )

    missing_bindings = [
        str(step.get("id") or basename(step.get("output_file")))
        for step in grading_steps
        if str(step.get("id") or basename(step.get("output_file")))
        not in scorer_bindings
        or scorer_bindings.get(
            str(step.get("id") or basename(step.get("output_file")))
        )
        not in scorer_functions
    ] if analysis_available and parse_error is None and scorer_registry_present else []
    if analysis_available and missing_bindings:
        add_issue(
            issues,
            "HIGH",
            "SCORING_COMPONENT_NOT_BOUND",
            "grading components are not bound to runtime scorers: "
            + ", ".join(sorted(missing_bindings)),
            {"component_ids": sorted(missing_bindings)},
            ["tests/checker.py", "tests/grading_spec.json"],
        )
    zero_weight = [
        str(step.get("id") or basename(step.get("output_file")))
        for step in grading_steps
        if _finite_number(step.get("weight")) == 0
    ] if analysis_available else []
    if analysis_available and zero_weight:
        add_issue(
            issues,
            "MEDIUM",
            "ZERO_WEIGHT_SCORING_COMPONENT",
            "declared grading components have no effect on the final score: "
            + ", ".join(sorted(zero_weight)),
            {"component_ids": sorted(zero_weight)},
            ["tests/grading_spec.json"],
        )
    return {
        "outputs": outputs,
        "scorer_bindings": scorer_bindings,
        "scorer_status": function_status,
        "semantic_validation": semantic_validation,
        "all_scoring_items_source_bound": bool(
            analysis_available
            and parse_error is None
            and scorer_registry_present
            and grading_steps
            and not missing_bindings
        ),
        "all_scoring_items_runtime_bound": False,
        "runtime_binding_status": (
            "STATIC_BINDINGS_RESOLVED_RUNTIME_NOT_PROVEN"
            if analysis_available
            and parse_error is None
            and scorer_registry_present
            and grading_steps
            and not missing_bindings
            else "CHECKER_MISSING"
            if not analysis_available
            else "CHECKER_UNPARSEABLE"
            if parse_error is not None
            else "STATIC_BINDINGS_INCOMPLETE"
        ),
        "dynamic_checks_required": [
            {
                "check": name,
                "status": "REQUIRED_NOT_RUN",
                "reason": "static analysis cannot prove runtime behavior",
            }
            for name in (
                "component_isolation",
                "always_pass",
                "always_zero",
                "division_by_zero",
                "direction_reversal",
                "positive_contract",
                "scientifically_wrong_but_format_valid",
            )
        ],
        "process_evidence_policy": {
            "status": "NOT_APPLICABLE",
            "reason": (
                "process evidence is not a dynamic fixture or "
                "checker-probe target"
            ),
            "files": {},
            "instrumentation": "NONE",
            "provenance": {
                "source_kind": "NONE",
                "oracle_used": False,
            },
        },
        "parse_status": (
            "ERROR"
            if parse_error
            else "OK"
            if analysis_available
            else "NOT_RUN"
        ),
    }


def _finite_number(value: Any) -> float | None:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def parse_roles(
    root: Path, issues: list[dict[str, Any]]
) -> tuple[dict[str, Any], dict[str, str]]:
    values: dict[str, Any] = {}
    status: dict[str, str] = {}
    for role, role_type in QUALITY_EVIDENCE_ROLES.items():
        path = root / role
        if not path.exists():
            severity = "FATAL" if role == "instruction.md" else "HIGH"
            add_issue(
                issues,
                severity,
                (
                    "UNRECOVERABLE_TASK_DEFINITION"
                    if role == "instruction.md"
                    else "MISSING_FILE"
                ),
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
    for role in set(REQUIRED_ROLES) - set(QUALITY_EVIDENCE_ROLES):
        status[role] = "ancillary_not_scored"
    if not (root / "solution").is_dir():
        add_issue(
            issues,
            "HIGH",
            "SOLUTION_ROLE_MISSING",
            "solution role is absent; presence can be confirmed without inspection",
            affected_files=["solution/"],
        )
    elif not (root / "solution/solve.sh").is_file():
        add_issue(
            issues,
            "HIGH",
            "SOLUTION_ORACLE_MISSING",
            "solution/solve.sh is absent; the checker positive path is repairable",
            affected_files=["solution/solve.sh"],
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
    checker_source: str,
    issues: list[dict[str, Any]],
    contract_map: dict[str, Any] | None = None,
) -> dict[str, Any]:
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
    contract_map = contract_map or instruction_contract_map(instruction)
    process_evidence = set(contract_map["process_evidence"])
    core_outputs = set(contract_map.get("core_outputs", []))
    instruction_outputs = (
        set(contract_map["instruction_outputs"])
        - process_evidence
        - core_outputs
    )
    checker_outputs = {
        item.get("file"): item
        for item in (
            contract_map.get("checker_analysis", {}).get("outputs", [])
            if isinstance(contract_map.get("checker_analysis"), dict)
            else []
        )
    }
    process_evidence_status = {
        name: "CONTRACT_MAP_ONLY" for name in sorted(process_evidence)
    }
    for name in sorted(step_outputs - contract_outputs - process_evidence):
        add_issue(
            issues,
            "HIGH",
            "OUTPUT_NOT_CONTRACTED",
            f"workflow output is absent from output contract: {name}",
            affected_files=["steps.json", "tests/grading_spec.json"],
        )
    for name in sorted(contract_outputs - grading_outputs - process_evidence):
        add_issue(
            issues,
            "HIGH",
            "OUTPUT_NOT_SCORED",
            f"contract output is not referenced by grading steps: {name}",
            affected_files=["tests/grading_spec.json"],
        )
    for name in sorted(step_evidence - contract_outputs - process_evidence):
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
        "process_evidence": sorted(process_evidence),
        "process_evidence_status": process_evidence_status,
        "unverified_process_evidence": [],
        "contract_outputs": sorted(contract_outputs),
        "grading_outputs": sorted(grading_outputs),
        "instruction_outputs": sorted(contract_map["instruction_outputs"]),
        "scored_instruction_outputs": sorted(
            contract_map["scored_outputs"]
        ),
        "unclassified_instruction_outputs": sorted(
            contract_map["unclassified_outputs"]
        ),
    }


def grading_checks(
    specification: dict[str, Any],
    issues: list[dict[str, Any]],
    contract_map: dict[str, Any] | None = None,
) -> None:
    grading_steps = (
        specification.get("steps", specification.get("checks", [])) or []
    )
    process_evidence = set((contract_map or {}).get("process_evidence", []))
    core_outputs = set((contract_map or {}).get("core_outputs", []))
    grading_steps = [
        step
        for step in grading_steps
        if basename(step.get("output_file")) not in process_evidence
        or basename(step.get("output_file")) in core_outputs
    ]
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
            "MEDIUM",
            "SINGLE_COMPONENT_THRESHOLD_REACHABLE",
            "one component's weight reaches the pass threshold; proving a "
            "load-bearing bypass requires a component-isolation probe",
            {
                "largest_weight": max(weights),
                "pass_threshold": threshold,
                "bypass_proven": False,
            },
            ["tests/grading_spec.json"],
        )


def gold_provenance_analysis(
    specification: dict[str, Any],
    checker_source: str,
    contract_map: dict[str, Any],
) -> dict[str, Any]:
    outputs = sorted(
        {
            basename(item.get("file"))
            for item in (
                (specification.get("output_contract", {}) or {}).get(
                    "outputs", []
                )
                or []
            )
            if basename(item.get("file"))
        }
        | set(contract_map.get("core_outputs", []))
    )
    return {
        "status": "NOT_ASSESSABLE",
        "mode": "no_paper",
        "reason": (
            "No independent Gold source is available within the no-paper "
            "instruction/tests evidence boundary."
        ),
        "outputs": outputs,
        "oracle_used": False,
        "provenance": {
            "source_kind": "NONE",
            "independent": False,
            "checker_source_inspected": bool(checker_source),
        },
    }


def static_audit(root: Path, output: Path) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    role_values, parse_status = parse_roles(root, issues)
    instruction = str(role_values.get("instruction.md", ""))
    specification = normalize_grading_specification(
        role_values.get("tests/grading_spec.json", {}), issues
    )
    contract_map = instruction_contract_map(instruction)
    if contract_map["role_conflicts"]:
        add_issue(
            issues,
            "HIGH",
            "CONTRADICTORY_OUTPUT_ROLE",
            "process annotations contradict load-bearing core-output semantics: "
            + ", ".join(
                sorted(
                    conflict["file"]
                    for conflict in contract_map["role_conflicts"]
                )
            ),
            {"role_conflicts": contract_map["role_conflicts"]},
            ["instruction.md"],
        )
    qualification = materials_classification_stub(instruction)
    add_issue(
        issues,
        "HIGH",
        "MATERIALS_ADMISSIBILITY_REQUIRES_ADJUDICATION",
        "materials admissibility must be decided by the Agent from the "
        "instruction's structured fields; no keyword prescreen is applied",
        {
            "structured_fields_present": qualification[
                "structured_fields_present"
            ],
            "structured_fields_expected": qualification[
                "structured_fields_expected"
            ],
        },
        ["instruction.md"],
    )
    checker_contract = checker_contract_analysis(
        str(role_values.get("tests/checker.py", "")),
        specification if isinstance(specification, dict) else {},
        contract_map,
        issues,
    )
    contract_map["checker_analysis"] = checker_contract
    contract_map["requirement_chains"] = _requirement_chains(
        contract_map, checker_contract["outputs"]
    )
    cross_file_sets = cross_file_checks(
        instruction,
        [],
        specification if isinstance(specification, dict) else {},
        str(role_values.get("tests/checker.py", "")),
        issues,
        contract_map,
    )
    instruction_consistency = instruction_internal_consistency(
        instruction, issues
    )
    gold_provenance = gold_provenance_analysis(
        specification if isinstance(specification, dict) else {},
        str(role_values.get("tests/checker.py", "")),
        contract_map,
    )
    contract_map["gold_provenance"] = gold_provenance
    grading_checks(
        specification if isinstance(specification, dict) else {},
        issues,
        contract_map,
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
        "instruction_consistency": instruction_consistency,
        "gold_provenance": gold_provenance,
        "cross_file_sets": cross_file_sets,
        "contract_map": {
            **contract_map,
            "checker_analysis": checker_contract,
        },
        "issues": sorted(
            issues,
            key=lambda item: (-SEVERITY_RANK[item["severity"]], item["code"]),
        ),
        "static_verdict": static_verdict,
        "limitations": [
            "materials classification (C01) is decided by the Agent from the "
            "instruction structured fields; no keyword prescreen is applied",
            "resource reachability is not tested in this slice",
            "paper fidelity is not tested in no-paper mode",
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
