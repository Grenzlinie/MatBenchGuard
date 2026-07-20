"""Deterministic D3 checker-health and D4 weight analysis.

This module deliberately contains only mechanically provable facts.  It does
not choose scoring semantics, Gold values, tolerances, thresholds, or scorer
algorithms.  Those changes remain assisted repairs.
"""

from __future__ import annotations

import ast
import math
from typing import Any, Iterable


D3_AUTO_RETURN_CODES = frozenset(
    {"SCORER_MISSING_RETURN", "SCORER_RETURN_NOT_TOTAL"}
)
D3_AUTO_WIRING_CODES = frozenset({"SCORER_WIRING_MISSING"})
D4_AUTO_CODES = frozenset({"WEIGHTS_NOT_ONE"})


def direct_returns(
    function: ast.FunctionDef | ast.AsyncFunctionDef,
) -> list[ast.Return]:
    """Return return statements owned by a function, excluding nested defs."""

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


def statements_guarantee_exit(statements: list[ast.stmt]) -> bool:
    """Conservatively prove that a statement list cannot fall through."""

    for statement in statements:
        if isinstance(statement, (ast.Return, ast.Raise)):
            return True
        if isinstance(statement, ast.If):
            if (
                statement.orelse
                and statements_guarantee_exit(statement.body)
                and statements_guarantee_exit(statement.orelse)
            ):
                return True
        if isinstance(statement, ast.Try):
            if statement.finalbody and statements_guarantee_exit(
                statement.finalbody
            ):
                return True
            handlers_exit = bool(statement.handlers) and all(
                statements_guarantee_exit(handler.body)
                for handler in statement.handlers
            )
            body_exit = statements_guarantee_exit(statement.body)
            else_exit = (
                statements_guarantee_exit(statement.orelse)
                if statement.orelse
                else body_exit
            )
            if body_exit and handlers_exit and else_exit:
                return True
    return False


def return_status(
    function: ast.FunctionDef | ast.AsyncFunctionDef,
) -> tuple[str, list[ast.Return]]:
    """Classify whether a scorer has a total, value-returning path."""

    returns = direct_returns(function)
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
    if not statements_guarantee_exit(function.body):
        return "PARTIAL_RETURN_PATHS", returns
    return "STATIC_RETURN_CANDIDATE", returns


def _return_proof(
    status: str, returns: Iterable[ast.Return]
) -> dict[str, Any]:
    """Return an exact append-return proof when the expression is unique."""

    if status != "PARTIAL_RETURN_PATHS":
        return {
            "auto_fix_provable": False,
            "reason": "return expression is not uniquely established",
        }
    expressions = [
        ast.unparse(item.value)
        for item in returns
        if item.value is not None
    ]
    if not expressions or len(set(expressions)) != 1:
        return {
            "auto_fix_provable": False,
            "reason": "multiple return expressions are possible",
        }
    return {
        "auto_fix_provable": True,
        "return_expression": expressions[0],
        "repair": f"append `return {expressions[0]}` to the unique fall-through path",
    }


def _scorer_candidate(name: str, step_id: str) -> bool:
    lowered = name.casefold()
    step = step_id.casefold()
    return (
        lowered == step
        or lowered == f"score_{step}"
        or lowered == f"scorer_{step}"
        or "score" in lowered
    )


def _literal_number(node: ast.AST) -> int | float | complex | None:
    try:
        value = ast.literal_eval(node)
    except (ValueError, TypeError, SyntaxError):
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float, complex)):
        return None
    return value


def _is_literal_zero(node: ast.AST) -> bool:
    value = _literal_number(node)
    return value is not None and value == 0


def analyze_checker_health(
    checker_source: str,
    scorer_bindings: dict[str, str] | None = None,
    *,
    scorer_registry_present: bool = False,
    scoring_step_ids: Iterable[str] = (),
) -> dict[str, Any]:
    """Analyze syntax, bound scorer paths, literal constants, and wiring.

    The return value is JSON-serializable so the Review report can preserve the
    exact proof used for D3 without serializing an AST.
    """

    scorer_bindings = dict(scorer_bindings or {})
    parse_error: str | None = None
    tree: ast.AST | None = None
    try:
        tree = ast.parse(checker_source)
    except SyntaxError as exc:
        parse_error = str(exc)

    functions: dict[str, ast.FunctionDef | ast.AsyncFunctionDef] = {}
    if tree is not None:
        functions = {
            node.name: node
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }

    function_status: dict[str, dict[str, Any]] = {}
    missing_returns: list[str] = []
    incomplete_returns: list[str] = []
    always_zero: list[str] = []
    always_pass: list[str] = []
    division_by_zero: list[str] = []
    for scorer_id, function_name in scorer_bindings.items():
        function = functions.get(function_name)
        if function is None:
            function_status[scorer_id] = {
                "function": function_name,
                "status": "FUNCTION_MISSING",
            }
            continue
        status, returns = return_status(function)
        if status == "MISSING_DIRECT_RETURN":
            missing_returns.append(scorer_id)
        elif status in {
            "ALWAYS_RETURNS_NONE",
            "MAY_RETURN_NONE",
            "PARTIAL_RETURN_PATHS",
        }:
            incomplete_returns.append(scorer_id)
        constants = [
            item.value.value
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
            and _is_literal_zero(node.right)
            for node in ast.walk(function)
        )
        dynamic_divisions = sum(
            isinstance(node, ast.BinOp)
            and isinstance(node.op, ast.Div)
            and not (
                _literal_number(node.right) is not None
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
            "return_proof": _return_proof(
                status if status == "PARTIAL_RETURN_PATHS" else return_status(function)[0],
                returns,
            ),
        }

    if tree is not None:
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.BinOp)
                and isinstance(node.op, ast.Div)
                and _is_literal_zero(node.right)
            ):
                owner = "<module>"
                for function_name, function in functions.items():
                    if any(candidate is node for candidate in ast.walk(function)):
                        owner = function_name
                        break
                if owner not in division_by_zero:
                    division_by_zero.append(owner)

    missing_wiring: list[dict[str, Any]] = []
    if tree is not None and scorer_registry_present:
        bound_functions = set(scorer_bindings.values())
        for step_id in sorted(set(str(item) for item in scoring_step_ids)):
            if step_id in scorer_bindings:
                continue
            candidates = sorted(
                name
                for name in functions
                if name not in bound_functions
                and _scorer_candidate(name, step_id)
            )
            if len(candidates) == 1:
                missing_wiring.append(
                    {
                        "component_id": step_id,
                        "candidate_function": candidates[0],
                        "candidate_count": 1,
                        "auto_fix_provable": True,
                        "proof": (
                            "exactly one unbound scorer-like function remains "
                            "for the unbound scoring component"
                        ),
                    }
                )

    return {
        "parse_status": "ERROR"
        if parse_error
        else "OK"
        if checker_source.strip()
        else "NOT_RUN",
        "parse_error": parse_error,
        "function_names": sorted(functions),
        "scorer_status": function_status,
        "missing_returns": sorted(missing_returns),
        "incomplete_returns": sorted(incomplete_returns),
        "always_zero": sorted(always_zero),
        "always_pass": sorted(always_pass),
        "division_by_zero": sorted(set(division_by_zero)),
        "missing_wiring": missing_wiring,
    }


def add_checker_health_issues(
    issues: list[dict[str, Any]],
    health: dict[str, Any],
    *,
    scorer_bindings: dict[str, str] | None = None,
    scoring_step_ids: Iterable[str] = (),
) -> None:
    """Append D3 source findings to the existing static-audit issue list."""

    def add(code: str, message: str, evidence: Any) -> None:
        issues.append(
            {
                "severity": "HIGH",
                "code": code,
                "message": message,
                "affected_files": ["tests/checker.py"],
                "evidence": evidence,
            }
        )

    if health.get("parse_status") == "ERROR":
        add(
            "CHECKER_STATIC_ANALYSIS_UNAVAILABLE",
            "checker.py cannot be parsed for contract mapping",
            {"parse_error": health.get("parse_error")},
        )
    if health.get("missing_returns"):
        add(
            "SCORER_MISSING_RETURN",
            "bound scoring functions do not return their computed score: "
            + ", ".join(health["missing_returns"]),
            {
                "scorer_ids": health["missing_returns"],
                "root_cause": "checker_scorer_runtime_contract",
                "auto_fix_provable": False,
            },
        )
    if health.get("incomplete_returns"):
        proof = {
            scorer_id: health["scorer_status"][scorer_id].get("return_proof", {})
            for scorer_id in health["incomplete_returns"]
        }
        add(
            "SCORER_RETURN_NOT_TOTAL",
            "bound scoring functions may return None or fall through without "
            "a score: " + ", ".join(health["incomplete_returns"]),
            {
                "scorer_ids": health["incomplete_returns"],
                "statuses": {
                    scorer_id: health["scorer_status"][scorer_id]["return_status"]
                    for scorer_id in health["incomplete_returns"]
                },
                "return_proof": proof,
                "root_cause": "checker_scorer_return_contract",
            },
        )
    if health.get("always_zero"):
        add(
            "ALWAYS_ZERO_SCORER",
            "bound scoring functions always return zero: "
            + ", ".join(health["always_zero"]),
            {"scorer_ids": health["always_zero"]},
        )
    if health.get("always_pass"):
        add(
            "ALWAYS_PASS_SCORER",
            "bound scoring functions always return one: "
            + ", ".join(health["always_pass"]),
            {"scorer_ids": health["always_pass"]},
        )
    if health.get("division_by_zero"):
        add(
            "DIVISION_BY_ZERO_LITERAL",
            "checker code contains literal division by zero in: "
            + ", ".join(health["division_by_zero"]),
            {"scorer_ids": health["division_by_zero"]},
        )
    for wiring in health.get("missing_wiring", []):
        add(
            "SCORER_WIRING_MISSING",
            "one scoring component has exactly one provable existing scorer "
            f"candidate: {wiring['component_id']}",
            wiring,
        )


def _strict_number(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    try:
        number = float(value)
    except OverflowError:
        return None
    return number if math.isfinite(number) else None


def analyze_weights(
    specification: dict[str, Any],
    *,
    process_outputs: Iterable[str] = (),
    checker_analysis: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Return D4 weight records and proven weight findings."""

    process = set(process_outputs)
    steps = [
        step
        for step in (specification.get("steps", []) or [])
        if isinstance(step, dict)
        and str(step.get("output_file") or "").split("/")[-1] not in process
    ]
    records: list[dict[str, Any]] = []
    invalid: list[dict[str, Any]] = []
    non_finite: list[dict[str, Any]] = []
    zero: list[dict[str, Any]] = []
    ineffective: list[dict[str, Any]] = []
    numeric_values: list[tuple[str, float]] = []
    positive_values: list[tuple[str, float]] = []
    outputs_by_id = {
        str(item.get("step_id")): item
        for item in (checker_analysis or {}).get("outputs", [])
        if isinstance(item, dict) and item.get("step_id") is not None
    }
    unique_wiring_ids = {
        item.get("component_id")
        for item in (checker_analysis or {}).get("d3_health", {}).get(
            "missing_wiring", []
        )
        if isinstance(item, dict) and item.get("component_id")
    }
    for index, step in enumerate(steps):
        component_id = str(
            step.get("id") or step.get("output_file") or f"step-{index}"
        )
        raw = step.get("weight")
        record: dict[str, Any] = {
            "component_id": component_id,
            "raw_weight": raw,
            "finite": False,
            "positive": False,
            "effective": None,
        }
        if isinstance(raw, bool) or not isinstance(raw, (int, float)):
            invalid.append(
                {
                    "component_id": component_id,
                    "value": raw,
                    "reason": "weight is not a JSON number",
                }
            )
        else:
            try:
                numeric = float(raw)
            except OverflowError:
                numeric = None
            if numeric is None:
                record["finite"] = False
                record["positive"] = False
                non_finite.append(
                    {
                        "component_id": component_id,
                        "value": raw,
                        "reason": "weight conversion overflowed",
                    }
                )
                records.append(record)
                continue
            record["finite"] = math.isfinite(numeric)
            record["positive"] = math.isfinite(numeric) and numeric > 0
            if not math.isfinite(numeric):
                non_finite.append(
                    {"component_id": component_id, "value": raw}
                )
            elif numeric < 0:
                invalid.append(
                    {
                        "component_id": component_id,
                        "value": raw,
                        "reason": "weight is negative",
                    }
                )
            elif numeric == 0:
                zero.append({"component_id": component_id, "value": raw})
            else:
                numeric_values.append((component_id, numeric))
                if numeric > 0:
                    positive_values.append((component_id, numeric))
        checker_item = outputs_by_id.get(component_id)
        if checker_item is not None:
            scoring = checker_item.get("checker_scoring") or {}
            record["effective"] = scoring.get("scorer_bound")
            if (
                record["positive"]
                and scoring.get("scorer_bound") is False
                and component_id not in unique_wiring_ids
            ):
                ineffective.append(
                    {
                        "component_id": component_id,
                        "value": raw,
                        "reason": "positive declared weight has no bound scorer",
                    }
                )
        records.append(record)

    findings: list[dict[str, Any]] = []
    if invalid:
        findings.append(
            {
                "severity": "HIGH",
                "code": "INVALID_WEIGHT",
                "message": "grading weights contain invalid values",
                "evidence": {"weights": invalid},
                "affected_files": ["tests/grading_spec.json"],
            }
        )
    if non_finite:
        findings.append(
            {
                "severity": "HIGH",
                "code": "NON_FINITE_WEIGHT",
                "message": "grading weights contain non-finite values",
                "evidence": {"weights": non_finite},
                "affected_files": ["tests/grading_spec.json"],
            }
        )
    if zero:
        findings.append(
            {
                "severity": "MEDIUM",
                "code": "ZERO_WEIGHT_SCORING_COMPONENT",
                "message": "declared grading components have no effect on the final score",
                "evidence": {"weights": zero},
                "affected_files": ["tests/grading_spec.json"],
            }
        )
    if ineffective:
        findings.append(
            {
                "severity": "HIGH",
                "code": "INEFFECTIVE_WEIGHT_SCORING_COMPONENT",
                "message": "positive grading weights are ineffective because their scorers are not bound",
                "evidence": {"weights": ineffective},
                "affected_files": [
                    "tests/grading_spec.json",
                    "tests/checker.py",
                ],
            }
        )

    all_numeric_finite = not invalid and not non_finite
    total = (
        sum(value for _, value in numeric_values)
        if all_numeric_finite
        else None
    )
    if total is not None and abs(total - 1.0) > 1e-6:
        normalized = [
            {"component_id": component_id, "value": value / total}
            for component_id, value in positive_values
        ] if (
            len(positive_values) == len(numeric_values)
            and len(positive_values) == len(steps) - len(zero)
            and total > 0
        ) else []
        findings.append(
            {
                "severity": "HIGH",
                "code": "WEIGHTS_NOT_ONE",
                "message": "grading weights do not sum to one",
                "evidence": {
                    "sum": total,
                    "weights": [
                        {"component_id": component_id, "value": value}
                        for component_id, value in numeric_values
                    ],
                    "ratio_preserving_normalization": bool(normalized),
                    "normalized_weights": normalized,
                },
                "affected_files": ["tests/grading_spec.json"],
            }
        )
    return {
        "steps": records,
        "findings": findings,
        "weight_sum": total,
        "ratio_preserving_normalization": bool(
            total is not None
            and total > 0
            and positive_values
            and len(positive_values) == len(numeric_values)
            and len(positive_values) == len(steps) - len(zero)
        ),
        "valid_weights": [
            {"component_id": component_id, "value": value}
            for component_id, value in numeric_values
        ],
    }


def expected_repair_class(
    check_id: Any, code: Any, evidence: Any
) -> str | None:
    """Return the only safe class for a D3/D4 finding, if applicable."""

    if check_id == "D3":
        if code in D3_AUTO_WIRING_CODES:
            return "AUTO_FIX"
        if code in D3_AUTO_RETURN_CODES:
            proof = evidence.get("return_proof", {}) if isinstance(evidence, dict) else {}
            if any(
                isinstance(item, dict) and item.get("auto_fix_provable") is True
                for item in proof.values()
            ):
                return "AUTO_FIX"
        return "ASSISTED_FIX"
    if check_id == "D4":
        if code in D4_AUTO_CODES and isinstance(evidence, dict):
            if evidence.get("ratio_preserving_normalization") is True:
                return "AUTO_FIX"
        return "ASSISTED_FIX"
    return None


def auto_fix_operation_error(
    finding: dict[str, Any], operation: dict[str, Any]
) -> str | None:
    """Validate the proof-to-operation link for a D3/D4 AUTO_FIX."""

    check_id = finding.get("deterministic_check")
    code = finding.get("title", finding.get("code"))
    evidence = finding.get("evidence")
    if expected_repair_class(check_id, code, evidence) != "AUTO_FIX":
        return "AUTO_FIX is not proven safe for this D3/D4 finding"
    file_name = str(operation.get("file", ""))
    if check_id == "D3" and file_name != "tests/checker.py":
        return "D3 AUTO_FIX must target tests/checker.py"
    if check_id == "D3" and code in D3_AUTO_RETURN_CODES:
        proofs = evidence.get("return_proof", {}) if isinstance(evidence, dict) else {}
        expressions = [
            str(proof.get("return_expression"))
            for proof in proofs.values()
            if isinstance(proof, dict)
            and proof.get("auto_fix_provable") is True
        ]
        new_text = str(operation.get("new", operation.get("content", "")))
        if not any(f"return {expression}" in new_text for expression in expressions):
            return "D3 return AUTO_FIX does not apply the unique return proof"
    if check_id == "D3" and code in D3_AUTO_WIRING_CODES:
        candidate = str((evidence or {}).get("candidate_function", ""))
        new_text = str(operation.get("new", operation.get("content", "")))
        if not candidate or candidate not in new_text:
            return "D3 wiring AUTO_FIX does not apply the unique scorer proof"
    if check_id == "D4":
        if file_name != "tests/grading_spec.json":
            return "D4 normalization AUTO_FIX must target tests/grading_spec.json"
        if str(operation.get("type")) != "json_set":
            return "D4 normalization AUTO_FIX must use json_set"
        path = operation.get("path")
        if not isinstance(path, list) or not path or path[-1] != "weight":
            return "D4 normalization AUTO_FIX must target a weight field"
        expected = {
            item.get("component_id"): item.get("value")
            for item in (evidence or {}).get("normalized_weights", [])
            if isinstance(item, dict)
        }
        component_index = path[-2] if len(path) >= 2 else None
        weights = (evidence or {}).get("weights", [])
        component = (
            weights[component_index].get("component_id")
            if isinstance(component_index, int)
            and 0 <= component_index < len(weights)
            and isinstance(weights[component_index], dict)
            else None
        )
        if component not in expected or operation.get("value") != expected[component]:
            return "D4 normalization AUTO_FIX does not preserve the proven ratios"
    return None
