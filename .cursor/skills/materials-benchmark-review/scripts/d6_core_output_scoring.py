"""D6 core-output-to-final-reward tracing.

D6 is intentionally separate from the broader static checker parser.  The
parser discovers candidates; this module states what was actually established
for each load-bearing output and keeps lexical filename references out of the
content-read state.
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import re
from typing import Any, Iterable


D6_SCHEMA_VERSION = "materials-d6-core-output-scoring/1.0"
PROVEN = "PROVEN"
FAILED = "FAILED"
UNKNOWN = "UNKNOWN"
CHAIN_STATES = (
    "content_read",
    "scorer_binding",
    "positive_effective_weight",
    "finite_return",
    "final_reward",
)

_UNSAFE_SCORER_STATUSES = {
    "FUNCTION_MISSING",
    "MISSING_DIRECT_RETURN",
    "ALWAYS_RETURNS_NONE",
    "MAY_RETURN_NONE",
    "PARTIAL_RETURN_PATHS",
    "STATIC_ALWAYS_ZERO",
    "STATIC_ALWAYS_ONE",
}


def finite_number(value: Any) -> float | None:
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError):
        return None
    return result if math.isfinite(result) else None


def _runtime_payload(result: Any) -> dict[str, Any] | None:
    if not isinstance(result, dict):
        return None
    evidence = result.get("evidence")
    return evidence if isinstance(evidence, dict) else result


def usable_runtime_result(result: Any) -> bool:
    payload = _runtime_payload(result)
    if payload is None or payload.get("crashed"):
        return False
    reward = finite_number(payload.get("reward"))
    breakdown = payload.get("breakdown")
    if reward is None or not isinstance(breakdown, dict):
        return False
    errors = breakdown.get("_errors", {})
    return isinstance(errors, dict) and not errors


def _status_detail(state: str, reason: str, **evidence: Any) -> dict[str, Any]:
    return {
        "state": state,
        "status": state,
        "reason": reason,
        **evidence,
    }


def _step_id(step: dict[str, Any] | None, output_name: str) -> str | None:
    if not isinstance(step, dict):
        return None
    value = str(step.get("id") or "").strip()
    return value or output_name


def _function_names(checker_source: str) -> set[str]:
    try:
        tree = ast.parse(checker_source)
    except SyntaxError:
        return set()
    return {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def _unique_scorer_candidate(
    step_id: str | None,
    output_name: str,
    checker_source: str,
    scorer_bindings: dict[str, str],
) -> str | None:
    if not step_id or step_id in scorer_bindings:
        return None
    names = _function_names(checker_source)
    normalized = "".join(
        character if character.isalnum() else "_"
        for character in (step_id, output_name.rsplit(".", 1)[0])
    )
    candidates = {
        name
        for name in names
        if name in {
            f"score_{step_id}",
            f"score_{normalized}",
            f"score_{output_name.rsplit('.', 1)[0]}",
            f"scorer_{step_id}",
            f"scorer_{normalized}",
        }
    }
    return next(iter(candidates)) if len(candidates) == 1 else None


def _output_string_matches(value: str, output_name: str) -> bool:
    normalized = value.replace("\\", "/").strip("`'\"").rstrip("/")
    target = output_name.replace("\\", "/").strip("`'\"").rstrip("/")
    if not normalized or not target:
        return False
    if normalized == target or _basename(normalized) == _basename(target):
        return True
    # Permit a descriptive literal such as ``read /app/outputs/result.json``,
    # but do not let ``not_result.json`` satisfy the target by substring.
    return bool(
        re.search(
            rf"(?<![A-Za-z0-9_.-]){re.escape(target)}(?![A-Za-z0-9_.-])",
            normalized,
        )
    )


def _basename(value: str) -> str:
    return value.rsplit("/", 1)[-1]


def _source_has_direct_content_read(
    checker_source: str, output_name: str
) -> bool:
    """Prove a current path alias flows into a content-reading call.

    This deliberately walks statements in source order.  A path alias is
    invalidated when a later assignment gives it an unrelated value, so an
    old assignment cannot satisfy a read after the alias has been reused.
    """

    try:
        tree = ast.parse(checker_source)
    except SyntaxError:
        return False

    def string_values(node: ast.AST) -> list[str]:
        return [
            str(item.value)
            for item in ast.walk(node)
            if isinstance(item, ast.Constant) and isinstance(item.value, str)
        ]

    def expression_is_output_path(
        node: ast.AST | None, aliases: set[str]
    ) -> bool:
        if node is None:
            return False
        if isinstance(node, ast.Name):
            return node.id in aliases
        return any(
            _output_string_matches(item, output_name)
            for item in string_values(node)
        )

    def call_reads_content(node: ast.Call, aliases: set[str]) -> bool:
        function = node.func
        if isinstance(function, ast.Name) and function.id == "open":
            mode: str | None = None
            if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                mode = node.args[1].value if isinstance(node.args[1].value, str) else None
            for keyword in node.keywords:
                if (
                    keyword.arg == "mode"
                    and isinstance(keyword.value, ast.Constant)
                    and isinstance(keyword.value.value, str)
                ):
                    mode = keyword.value.value
            if mode is not None and mode[:1] in {"w", "a", "x"}:
                return False
            return bool(node.args) and expression_is_output_path(node.args[0], aliases)
        if isinstance(function, ast.Attribute) and function.attr in {
            "open",
            "read_text",
            "read_bytes",
            "read",
        }:
            if function.attr == "open":
                mode: str | None = None
                if node.args and isinstance(node.args[0], ast.Constant):
                    mode = node.args[0].value if isinstance(node.args[0].value, str) else None
                for keyword in node.keywords:
                    if (
                        keyword.arg == "mode"
                        and isinstance(keyword.value, ast.Constant)
                        and isinstance(keyword.value.value, str)
                    ):
                        mode = keyword.value.value
                if mode is not None and mode[:1] in {"w", "a", "x"}:
                    return False
            return expression_is_output_path(function.value, aliases)
        return False

    def target_names(node: ast.AST) -> set[str]:
        return {
            item.id
            for item in ast.walk(node)
            if isinstance(item, ast.Name) and isinstance(item.ctx, ast.Store)
        }

    def expression_reads(node: ast.AST | None, aliases: set[str]) -> bool:
        return node is not None and any(
            call_reads_content(candidate, aliases)
            for candidate in ast.walk(node)
            if isinstance(candidate, ast.Call)
        )

    def merged_aliases(paths: list[set[str]], fallback: set[str]) -> set[str]:
        return set.intersection(*paths) if paths else set(fallback)

    def walk_statements(
        statements: list[ast.stmt], aliases: set[str]
    ) -> tuple[bool, set[str]]:
        current = set(aliases)
        for statement in statements:
            if isinstance(statement, ast.Assign):
                if expression_reads(statement.value, current):
                    return True, current
                value_is_output = expression_is_output_path(
                    statement.value, current
                )
                for target in target_names(statement):
                    if value_is_output:
                        current.add(target)
                    else:
                        current.discard(target)
                continue
            if isinstance(statement, ast.AnnAssign):
                if expression_reads(statement.value, current):
                    return True, current
                value_is_output = expression_is_output_path(
                    statement.value, current
                )
                for target in target_names(statement.target):
                    if value_is_output:
                        current.add(target)
                    else:
                        current.discard(target)
                continue
            if isinstance(statement, ast.AugAssign):
                if expression_reads(statement.value, current):
                    return True, current
                current.difference_update(target_names(statement.target))
                continue
            if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if any(
                    expression_reads(value, current)
                    for value in (
                        list(statement.decorator_list)
                        + list(statement.args.defaults)
                        + [
                            item
                            for item in statement.args.kw_defaults
                            if item is not None
                        ]
                    )
                ):
                    return True, current
                nested_found, _ = walk_statements(statement.body, set())
                if nested_found:
                    return True, current
                current.discard(statement.name)
                continue
            if isinstance(statement, ast.If):
                if expression_reads(statement.test, current):
                    return True, current
                body_found, body_aliases = walk_statements(
                    statement.body, current
                )
                else_found, else_aliases = walk_statements(
                    statement.orelse, current
                )
                if body_found or else_found:
                    return True, current
                current = (
                    body_aliases & else_aliases
                    if statement.orelse
                    else current & body_aliases
                )
                continue
            if isinstance(statement, (ast.For, ast.AsyncFor, ast.While)):
                loop_expression = (
                    statement.iter
                    if isinstance(statement, (ast.For, ast.AsyncFor))
                    else statement.test
                )
                if expression_reads(loop_expression, current):
                    return True, current
                loop_aliases = set(current)
                if isinstance(statement, (ast.For, ast.AsyncFor)):
                    loop_aliases.difference_update(target_names(statement.target))
                body_found, body_aliases = walk_statements(
                    statement.body, loop_aliases
                )
                if body_found:
                    return True, current
                if statement.orelse:
                    else_found, else_aliases = walk_statements(
                        statement.orelse, current
                    )
                    if else_found:
                        return True, current
                    current = merged_aliases(
                        [current, body_aliases, else_aliases], current
                    )
                else:
                    current &= body_aliases
                if isinstance(statement, (ast.For, ast.AsyncFor)):
                    current.difference_update(target_names(statement.target))
                continue
            if isinstance(statement, ast.Try):
                paths = [
                    statement.body,
                    *[handler.body for handler in statement.handlers],
                ]
                path_results = [
                    walk_statements(path, current) for path in paths
                ]
                if any(found for found, _ in path_results):
                    return True, current
                current = merged_aliases(
                    [path_aliases for _, path_aliases in path_results],
                    current,
                )
                if statement.orelse:
                    else_found, else_aliases = walk_statements(
                        statement.orelse, current
                    )
                    if else_found:
                        return True, current
                    current &= else_aliases
                if statement.finalbody:
                    final_found, final_aliases = walk_statements(
                        statement.finalbody, current
                    )
                    if final_found:
                        return True, current
                    current = final_aliases
                continue
            if isinstance(statement, (ast.With, ast.AsyncWith)):
                if any(
                    expression_reads(item.context_expr, current)
                    for item in statement.items
                ):
                    return True, current
                body_aliases = set(current)
                for item in statement.items:
                    if item.optional_vars is not None:
                        body_aliases.difference_update(
                            target_names(item.optional_vars)
                        )
                body_found, _ = walk_statements(statement.body, body_aliases)
                if body_found:
                    return True, current
                continue
            if isinstance(statement, ast.Delete):
                for target in statement.targets:
                    current.difference_update(target_names(target))
                continue
            if expression_reads(statement, current):
                return True, current
            for named in (
                node
                for node in ast.walk(statement)
                if isinstance(node, ast.NamedExpr)
            ):
                current.difference_update(target_names(named.target))
                continue
        return False, current

    found, _ = walk_statements(tree.body, set())
    return found


def _source_final_reward_state(
    checker_source: str,
    step_id: str | None,
    *,
    single_core_output: bool = False,
) -> tuple[str, dict[str, Any]]:
    """Find flow-sensitive source proof of scalar reward dependence."""

    if not step_id:
        return UNKNOWN, {"reason": "scoring component identifier is absent"}
    try:
        tree = ast.parse(checker_source)
    except SyntaxError:
        return UNKNOWN, {"reason": "checker source is not parseable"}

    component_tag = "target_component"
    aggregate_tag = "all_breakdown_components"

    def literal_string(node: ast.AST | None) -> str | None:
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        return None

    def target_names(node: ast.AST) -> set[str]:
        return {
            item.id
            for item in ast.walk(node)
            if isinstance(item, ast.Name) and isinstance(item.ctx, ast.Store)
        }

    target_is_inserted = any(
        (
            isinstance(node, ast.Subscript)
            and literal_string(node.slice) == step_id
            and isinstance(node.value, ast.Name)
            and node.value.id == "breakdown"
        )
        or (
            isinstance(node, ast.Dict)
            and any(literal_string(key) == step_id for key in node.keys)
        )
        for node in ast.walk(tree)
    )

    def expression_tags(
        node: ast.AST | None, environment: dict[str, set[str]]
    ) -> set[str]:
        if node is None:
            return set()
        if isinstance(node, ast.Name):
            return set(environment.get(node.id, set()))
        if isinstance(node, ast.Subscript):
            tags = expression_tags(node.value, environment)
            key = literal_string(node.slice)
            if (
                key == step_id
                and isinstance(node.value, ast.Name)
                and node.value.id == "breakdown"
            ):
                tags.add(component_tag)
            return tags | expression_tags(node.slice, environment)
        if isinstance(node, ast.Call):
            tags: set[str] = set()
            if isinstance(node.func, ast.Name) and node.func.id in {
                "abs",
                "float",
                "int",
                "max",
                "min",
                "round",
                "str",
                "sum",
            }:
                tags.update(
                    tag
                    for argument in node.args
                    for tag in expression_tags(argument, environment)
                )
                tags.update(
                    tag
                    for keyword in node.keywords
                    for tag in expression_tags(keyword.value, environment)
                )
            if isinstance(node.func, ast.Attribute):
                receiver = node.func.value
                if (
                    node.func.attr == "get"
                    and isinstance(receiver, ast.Name)
                    and receiver.id == "breakdown"
                    and node.args
                    and literal_string(node.args[0]) == step_id
                ):
                    tags.add(component_tag)
                if (
                    node.func.attr in {"values", "items"}
                    and isinstance(receiver, ast.Name)
                    and receiver.id == "breakdown"
                ):
                    tags.add(aggregate_tag)
                if node.func.attr in {"get", "values", "items"}:
                    tags.update(expression_tags(receiver, environment))
                    tags.update(
                        tag
                        for argument in node.args
                        for tag in expression_tags(argument, environment)
                    )
                    tags.update(
                        tag
                        for keyword in node.keywords
                        for tag in expression_tags(keyword.value, environment)
                    )
            return tags
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp)):
            local = {name: set(tags) for name, tags in environment.items()}
            for generator in node.generators:
                iterator_tags = expression_tags(generator.iter, local)
                if aggregate_tag in iterator_tags and target_is_inserted:
                    iterator_tags.add(component_tag)
                for name in target_names(generator.target):
                    local[name] = set(iterator_tags)
                for condition in generator.ifs:
                    iterator_tags.update(expression_tags(condition, local))
            return expression_tags(node.elt, local)
        if isinstance(node, ast.DictComp):
            local = {name: set(tags) for name, tags in environment.items()}
            for generator in node.generators:
                iterator_tags = expression_tags(generator.iter, local)
                if aggregate_tag in iterator_tags and target_is_inserted:
                    iterator_tags.add(component_tag)
                for name in target_names(generator.target):
                    local[name] = set(iterator_tags)
            return expression_tags(node.key, local) | expression_tags(
                node.value, local
            )
        tags: set[str] = set()
        for child in ast.iter_child_nodes(node):
            tags.update(expression_tags(child, environment))
        return tags

    reward_returns: list[tuple[set[str], bool]] = []

    def reward_expression(value: ast.AST | None) -> ast.AST | None:
        if not isinstance(value, ast.Dict):
            return None
        for key, item in zip(value.keys, value.values):
            if literal_string(key) == "reward":
                return item
        return None

    def merge_environments(
        left: dict[str, set[str]], right: dict[str, set[str]]
    ) -> dict[str, set[str]]:
        return {
            name: set(left[name]) & set(right[name])
            for name in set(left) & set(right)
        }

    def component_assignment_tags(
        value: ast.AST | None, environment: dict[str, set[str]]
    ) -> set[str]:
        """Tag only values actually placed under the target component key."""

        tags = expression_tags(value, environment)
        if not isinstance(value, ast.Dict):
            return tags
        if not any(literal_string(key) == step_id for key in value.keys):
            return tags
        tags.add(component_tag)
        for item in ast.walk(value):
            if isinstance(item, ast.Name) and isinstance(item.ctx, ast.Load):
                environment.setdefault(item.id, set()).add(component_tag)
        return tags

    def walk_statements(
        statements: list[ast.stmt], environment: dict[str, set[str]]
    ) -> dict[str, set[str]]:
        current = {name: set(tags) for name, tags in environment.items()}
        for statement in statements:
            if isinstance(statement, ast.Assign):
                tags = component_assignment_tags(statement.value, current)
                for target in statement.targets:
                    if (
                        isinstance(target, ast.Subscript)
                        and isinstance(target.value, ast.Name)
                        and target.value.id == "breakdown"
                        and literal_string(target.slice) == step_id
                    ):
                        for item in ast.walk(statement.value):
                            if isinstance(item, ast.Name) and isinstance(
                                item.ctx, ast.Load
                            ):
                                current.setdefault(item.id, set()).add(
                                    component_tag
                                )
                    for name in target_names(target):
                        current[name] = set(tags)
                continue
            if isinstance(statement, ast.AnnAssign):
                tags = component_assignment_tags(statement.value, current)
                for name in target_names(statement.target):
                    current[name] = set(tags)
                continue
            if isinstance(statement, ast.AugAssign):
                tags = expression_tags(statement.target, current) | expression_tags(
                    statement.value, current
                )
                for name in target_names(statement.target):
                    current[name] = set(tags)
                continue
            if isinstance(statement, ast.Return):
                reward = reward_expression(statement.value)
                if reward is not None:
                    reward_returns.append(
                        (
                            expression_tags(reward, current),
                            isinstance(reward, ast.Constant)
                            and isinstance(reward.value, (int, float))
                            and not isinstance(reward.value, bool),
                        )
                    )
                continue
            if isinstance(statement, ast.If):
                body = walk_statements(statement.body, current)
                other = (
                    walk_statements(statement.orelse, current)
                    if statement.orelse
                    else current
                )
                current = merge_environments(body, other)
                continue
            if isinstance(statement, (ast.For, ast.AsyncFor, ast.While)):
                body_environment = {
                    name: set(tags) for name, tags in current.items()
                }
                if isinstance(statement, (ast.For, ast.AsyncFor)):
                    iterator_tags = expression_tags(statement.iter, current)
                    for name in target_names(statement.target):
                        body_environment[name] = set(iterator_tags)
                body = walk_statements(statement.body, body_environment)
                current = merge_environments(current, body)
                if statement.orelse:
                    current = merge_environments(
                        current, walk_statements(statement.orelse, current)
                    )
                continue
            if isinstance(statement, ast.Try):
                paths = [
                    walk_statements(statement.body, current),
                    *[
                        walk_statements(handler.body, current)
                        for handler in statement.handlers
                    ],
                ]
                merged = paths[0] if paths else current
                for path in paths[1:]:
                    merged = merge_environments(merged, path)
                if statement.orelse:
                    merged = walk_statements(statement.orelse, merged)
                if statement.finalbody:
                    merged = walk_statements(statement.finalbody, merged)
                current = merged
                continue
            if isinstance(statement, (ast.With, ast.AsyncWith)):
                current = walk_statements(statement.body, current)
                continue
            if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)):
                walk_statements(statement.body, {})
                current.pop(statement.name, None)
                continue
            if isinstance(statement, ast.Delete):
                for target in statement.targets:
                    for name in target_names(target):
                        current.pop(name, None)
        return current

    walk_statements(tree.body, {})
    def sink_name(node: ast.AST | None) -> str | None:
        if isinstance(node, ast.Name):
            return node.id
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"str", "float"}
            and len(node.args) == 1
        ):
            return sink_name(node.args[0])
        return None

    reward_sink_names: set[str] = set()
    breakdown_sink_names: dict[str, set[str]] = {}
    for node in ast.walk(tree):
        if (
            not isinstance(node, ast.Call)
            or not isinstance(node.func, ast.Attribute)
            or node.func.attr != "write_text"
            or not node.args
        ):
            continue
        receiver_strings = {
            str(item.value)
            for item in ast.walk(node.func.value)
            if isinstance(item, ast.Constant) and isinstance(item.value, str)
        }
        if "reward.txt" in receiver_strings:
            name = sink_name(node.args[0])
            if name:
                reward_sink_names.add(name)
        if "breakdown.json" not in receiver_strings:
            continue
        dictionaries = [
            item for item in ast.walk(node.args[0]) if isinstance(item, ast.Dict)
        ]
        for dictionary in dictionaries:
            for key, value in zip(dictionary.keys, dictionary.values):
                key_name = literal_string(key)
                name = sink_name(value)
                if key_name and key_name != "_errors" and name:
                    breakdown_sink_names.setdefault(name, set()).add(key_name)

    shared_sinks = reward_sink_names & set(breakdown_sink_names)
    bound_sink = next(
        (
            name
            for name in sorted(shared_sinks)
            if step_id in breakdown_sink_names[name]
            or (
                single_core_output
                and sum(
                    len(keys) for keys in breakdown_sink_names.values()
                )
                == 1
            )
        ),
        None,
    )
    if bound_sink is not None:
        constants: set[float] = set()
        nonconstant = False
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = (
                node.targets if isinstance(node, ast.Assign) else [node.target]
            )
            if not any(
                isinstance(target, ast.Name) and target.id == bound_sink
                for target in targets
            ):
                continue
            value = node.value
            if (
                isinstance(value, ast.Constant)
                and isinstance(value.value, (int, float))
                and not isinstance(value.value, bool)
            ):
                constants.add(float(value.value))
            else:
                nonconstant = True
        if len(constants) <= 1 and not nonconstant:
            return FAILED, {
                "reason": "The persisted scalar final reward is statically constant.",
                "step_id": step_id,
                "reward_variable": bound_sink,
            }
        return PROVEN, {
            "reason": (
                "The checker writes the same varying source variable to the "
                "scalar reward and the uniquely bound breakdown component."
            ),
            "step_id": step_id,
            "reward_variable": bound_sink,
            "breakdown_keys": sorted(breakdown_sink_names[bound_sink]),
            "source_bound": True,
        }
    if not reward_returns:
        return UNKNOWN, {
            "reason": "No scalar reward return is statically available.",
            "step_id": step_id,
        }
    if all(is_constant for _, is_constant in reward_returns):
        return FAILED, {
            "reason": "The scalar final reward is statically constant.",
            "step_id": step_id,
        }
    if all(component_tag in tags for tags, _ in reward_returns):
        return PROVEN, {
            "reason": (
                "Every scalar reward return has source-level data dependence "
                "on the target component."
            ),
            "step_id": step_id,
            "source_bound": True,
        }
    return UNKNOWN, {
        "reason": (
            "A scalar reward is returned, but target-component dependence is "
            "not proven on every return path."
        ),
        "step_id": step_id,
    }


def _runtime_final_reward_dependence(
    observations: list[dict[str, Any]],
) -> tuple[str, dict[str, Any]]:
    usable = [
        item
        for item in observations
        if item.get("score") is not None and item.get("reward") is not None
    ]
    if len(usable) < 2:
        return UNKNOWN, {
            "reason": "At least two finite component/reward observations are required."
        }
    scores = {item["score"] for item in usable}
    rewards = {item["reward"] for item in usable}
    if len(scores) < 2:
        return UNKNOWN, {
            "reason": "Observed component score did not vary across usable cases."
        }
    if len(rewards) == 1:
        return FAILED, {
            "reason": "The scalar final reward is constant while the component varies.",
            "cases": [item.get("case") for item in usable],
        }
    for index, left in enumerate(usable):
        for right in usable[index + 1 :]:
            if (
                left.get("other_components") == right.get("other_components")
                and left.get("weight") == right.get("weight")
                and left.get("score") != right.get("score")
                and left.get("reward") != right.get("reward")
            ):
                return PROVEN, {
                    "reason": (
                        "A controlled runtime pair changes the scalar reward "
                        "when only the target component score changes."
                    ),
                    "cases": [left.get("case"), right.get("case")],
                    "scores": [left.get("score"), right.get("score")],
                    "rewards": [left.get("reward"), right.get("reward")],
                    "weight": left.get("weight"),
                    "source_bound": True,
                }
    return UNKNOWN, {
        "reason": (
            "Component and reward both vary, but no controlled pair isolates "
            "the target component from all other breakdown components."
        ),
        "cases": [item.get("case") for item in usable],
    }


def _unique_wiring_proof(
    checker_source: str, step_id: str | None, candidate_function: str | None
) -> dict[str, Any] | None:
    if not step_id or not candidate_function:
        return None
    try:
        tree = ast.parse(checker_source)
    except SyntaxError:
        return None
    registries = [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        and any(
            isinstance(target, ast.Name) and target.id == "_SCORERS"
            for target in (
                node.targets if isinstance(node, ast.Assign) else [node.target]
            )
        )
    ]
    if len(registries) != 1:
        return None
    registry_assignment = registries[0]
    registry = registry_assignment.value
    if not isinstance(registry, ast.Dict):
        return None
    existing_keys = {
        key.value
        for key in registry.keys
        if isinstance(key, ast.Constant) and isinstance(key.value, str)
    }
    if step_id in existing_keys:
        return None
    if any(
        isinstance(value, ast.Name) and value.id == candidate_function
        for value in registry.values
    ):
        # Reusing a scorer already bound to another component is ambiguous.
        return None
    return {
        "proof_status": "PROVEN",
        "source_file": "tests/checker.py",
        "checker_source_hash": "sha256:"
        + hashlib.sha256(checker_source.encode("utf-8")).hexdigest(),
        "registry_name": "_SCORERS",
        "registry_source": ast.get_source_segment(
            checker_source, registry_assignment
        ),
        "component_id": step_id,
        "candidate_function": candidate_function,
        "expected_binding": {step_id: candidate_function},
    }


def _scorer_registry(source: str) -> tuple[dict[str, str], ast.AST | None]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return {}, None
    assignments = [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        and any(
            isinstance(target, ast.Name) and target.id == "_SCORERS"
            for target in (
                node.targets if isinstance(node, ast.Assign) else [node.target]
            )
        )
    ]
    if len(assignments) != 1 or not isinstance(assignments[0].value, ast.Dict):
        return {}, tree
    registry: dict[str, str] = {}
    for key, value in zip(assignments[0].value.keys, assignments[0].value.values):
        if (
            isinstance(key, ast.Constant)
            and isinstance(key.value, str)
            and isinstance(value, ast.Name)
        ):
            registry[key.value] = value.id
    return registry, tree


def unique_wiring_auto_fix_operation_error(
    finding: dict[str, Any],
    operation: dict[str, Any],
    checker_source: str,
) -> str | None:
    """Validate a D6 AUTO_FIX against an exact source-bound wiring proof."""

    evidence = finding.get("evidence")
    proof = evidence.get("source_bound_unique_proof") if isinstance(evidence, dict) else None
    if (
        not isinstance(evidence, dict)
        or evidence.get("repair_class") != "AUTO_FIX"
        or evidence.get("repair_scope") != "UNIQUE_SCORING_WIRING"
        or evidence.get("unique_wiring") is not True
        or not isinstance(proof, dict)
        or proof.get("proof_status") != "PROVEN"
    ):
        return "D6 AUTO_FIX lacks a complete unique source-bound wiring proof"
    required = {
        "source_file",
        "checker_source_hash",
        "registry_name",
        "registry_source",
        "component_id",
        "candidate_function",
        "expected_binding",
    }
    if not required.issubset(proof):
        return "D6 unique wiring proof is incomplete"
    if (
        proof.get("source_file") != "tests/checker.py"
        or proof.get("registry_name") != "_SCORERS"
        or not isinstance(proof.get("registry_source"), str)
        or proof.get("expected_binding")
        != {str(proof["component_id"]): str(proof["candidate_function"])}
    ):
        return "D6 unique wiring proof is ambiguous"
    expected_hash = "sha256:" + hashlib.sha256(
        checker_source.encode("utf-8")
    ).hexdigest()
    if proof.get("checker_source_hash") != expected_hash:
        return "D6 unique wiring proof is stale"
    if operation.get("file") != "tests/checker.py" or operation.get(
        "type"
    ) not in {"replace_text", "text_replace"}:
        return "D6 unique wiring AUTO_FIX must replace checker source text"
    old = operation.get("old")
    new = operation.get("new")
    if not isinstance(old, str) or not isinstance(new, str) or not old:
        return "D6 unique wiring AUTO_FIX lacks an exact checker replacement"
    if old != proof["registry_source"]:
        return "D6 unique wiring AUTO_FIX old source is not the proven registry"
    if checker_source.count(old) != 1:
        return "D6 unique wiring AUTO_FIX old source is not uniquely bound"
    candidate_source = checker_source.replace(old, new, 1)
    before, before_tree = _scorer_registry(checker_source)
    after, after_tree = _scorer_registry(candidate_source)
    component = str(proof["component_id"])
    candidate = str(proof["candidate_function"])
    if before_tree is None or after_tree is None:
        return "D6 unique wiring AUTO_FIX produces unparsable checker source"
    if component in before:
        return "D6 unique wiring proof targets an already-bound component"
    expected_after = dict(before)
    expected_after[component] = candidate
    if after != expected_after:
        return (
            "D6 unique wiring AUTO_FIX must add exactly the proven "
            "component-to-scorer registry entry"
        )
    function_names = {
        node.name
        for node in ast.walk(after_tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    if candidate not in function_names:
        return "D6 unique wiring AUTO_FIX candidate scorer is missing"
    return None


def _source_has_generic_content_loader(checker_source: str) -> bool:
    """Detect a called loader without claiming which output it consumes."""

    try:
        tree = ast.parse(checker_source)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        function = node.func
        name = (
            function.id
            if isinstance(function, ast.Name)
            else function.attr
            if isinstance(function, ast.Attribute)
            else ""
        )
        if name in {"load_artifact", "read_text", "read_bytes"}:
            return True
    return False


def _static_content_state(
    output: dict[str, Any], checker_source: str
) -> tuple[str, dict[str, Any]]:
    output_name = str(output.get("file") or "")
    read_status = output.get("checker_reads")
    semantic_status = output.get("semantic_validation")
    has_direct_read = _source_has_direct_content_read(
        checker_source, output_name
    )
    if has_direct_read:
        return PROVEN, _status_detail(
            PROVEN,
            "Static path data flow reaches a content-reading operation.",
            checker_reads=read_status,
            semantic_validation=semantic_status,
        )
    has_generic_loader = _source_has_generic_content_loader(checker_source)
    if (
        semantic_status == "EXISTENCE_ONLY"
        or read_status == "STATIC_FILENAME_REFERENCE_ONLY"
    ) and not has_generic_loader:
        return FAILED, _status_detail(
            FAILED,
            "The checker only references or tests the output path.",
            checker_reads=read_status,
            semantic_validation=semantic_status,
        )
    if (
        semantic_status == "EXISTENCE_ONLY"
        or read_status == "STATIC_FILENAME_REFERENCE_ONLY"
    ):
        return UNKNOWN, _status_detail(
            UNKNOWN,
            "A generic loader is present, but the output content data flow "
            "requires runtime evidence.",
            checker_reads=read_status,
            semantic_validation=semantic_status,
        )
    if semantic_status in {
        "UNKNOWN_CHECKER_UNAVAILABLE",
        "UNKNOWN_GRADING_CONTRACT_UNAVAILABLE",
    }:
        return UNKNOWN, _status_detail(
            UNKNOWN,
            "The checker or grading contract is unavailable for content-read "
            "assessment.",
            checker_reads=read_status,
            semantic_validation=semantic_status,
        )
    if semantic_status == "NOT_REFERENCED" or read_status == (
        "UNKNOWN_NOT_ESTABLISHED"
    ):
        return FAILED, _status_detail(
            FAILED,
            "The checker does not establish a read of the core output.",
            checker_reads=read_status,
            semantic_validation=semantic_status,
        )
    if read_status == "STATIC_EXPLICIT_READ_CANDIDATE":
        if _source_has_direct_content_read(checker_source, output_name):
            return PROVEN, _status_detail(
                PROVEN,
                "Static analysis found a content-reading operation for the output.",
                checker_reads=read_status,
            )
        return UNKNOWN, _status_detail(
            UNKNOWN,
            "The filename is near a read candidate, but content data flow is "
            "not statically established.",
            checker_reads=read_status,
        )
    if read_status == "STATIC_GENERIC_LOADER_CANDIDATE":
        return UNKNOWN, _status_detail(
            UNKNOWN,
            "A generic loader is present; runtime content sensitivity is required.",
            checker_reads=read_status,
        )
    if read_status in {"UNKNOWN_CHECKER_MISSING", "UNKNOWN_CHECKER_UNPARSEABLE"}:
        return UNKNOWN, _status_detail(
            UNKNOWN,
            "Checker content reads are unavailable for assessment.",
            checker_reads=read_status,
        )
    return UNKNOWN, _status_detail(
        UNKNOWN,
        "The checker content-read path is not established.",
        checker_reads=read_status,
    )


def _static_chain(
    output: dict[str, Any],
    *,
    step: dict[str, Any] | None,
    checker_source: str,
    scorer_bindings: dict[str, str],
    scorer_status: dict[str, dict[str, Any]],
    single_core_output: bool,
) -> dict[str, Any]:
    output_name = str(output.get("file") or "")
    step_id = _step_id(step, output_name)
    content_state, content_detail = _static_content_state(
        output, checker_source
    )
    scoring = output.get("checker_scoring")
    scoring = dict(scoring) if isinstance(scoring, dict) else {}
    if step is not None:
        if "weight" in step:
            scoring["declared_weight"] = step.get("weight")
        if "scorer_bound" in step:
            scoring["scorer_bound"] = step.get("scorer_bound")
        elif step_id in scorer_bindings:
            scoring["scorer_bound"] = True
            scoring["scorer_binding_status"] = "STATIC_SOURCE_BOUND"
        elif scoring.get("scorer_binding_status") == "STATIC_NOT_BOUND":
            scoring["scorer_bound"] = False
        else:
            scoring["scorer_bound"] = None
            scoring["scorer_binding_status"] = "UNKNOWN_DIRECT_CHECKER"

    if step is None:
        binding_state = UNKNOWN
        binding_detail = _status_detail(
            UNKNOWN,
            "No grading step is available for this core output.",
        )
    elif not scoring.get("scorer_bound") and scoring.get(
        "scorer_binding_status"
    ) == "STATIC_NOT_BOUND":
        candidate = _unique_scorer_candidate(
            step_id, output_name, checker_source, scorer_bindings
        )
        proof = _unique_wiring_proof(checker_source, step_id, candidate)
        if candidate is not None and proof is not None:
            binding_state = FAILED
            binding_detail = _status_detail(
                FAILED,
                "The unique scorer function is not wired into the scorer registry.",
                step_id=step_id,
                candidate_function=candidate,
                unique_wiring=True,
                repair_scope="UNIQUE_SCORING_WIRING",
                repair_class="AUTO_FIX",
                source_bound_unique_proof=proof,
            )
        else:
            binding_state = FAILED
            binding_detail = _status_detail(
                FAILED,
                "The grading component is not bound to a runtime scorer.",
                step_id=step_id,
                unique_wiring=False,
                repair_scope="SCORING_SEMANTICS",
                repair_class="ASSISTED_FIX",
            )
    elif scoring.get("scorer_bound") is True:
        binding_state = PROVEN
        binding_detail = _status_detail(
            PROVEN,
            "The grading step is source-bound to a scorer function.",
            step_id=step_id,
            binding_status=scoring.get("scorer_binding_status"),
        )
    else:
        binding_state = UNKNOWN
        binding_detail = _status_detail(
            UNKNOWN,
            "Direct checker scoring requires runtime evidence.",
            step_id=step_id,
            binding_status=scoring.get("scorer_binding_status"),
        )

    declared_weight = scoring.get("declared_weight")
    numeric_weight = finite_number(declared_weight)
    if numeric_weight is None:
        weight_state = UNKNOWN
        weight_detail = _status_detail(
            UNKNOWN,
            "The declared scoring weight is unavailable or non-finite.",
            declared_weight=declared_weight,
        )
    elif numeric_weight <= 0:
        weight_state = FAILED
        weight_detail = _status_detail(
            FAILED,
            "The core output has no positive declared scoring weight.",
            declared_weight=numeric_weight,
        )
    else:
        weight_state = UNKNOWN
        weight_detail = _status_detail(
            UNKNOWN,
            "The declared weight is positive; final-reward effectiveness needs runtime evidence.",
            declared_weight=numeric_weight,
        )

    scorer_id = step_id
    scorer = scorer_status.get(scorer_id or "", {})
    return_status = scorer.get("return_status", scorer.get("status"))
    if return_status in _UNSAFE_SCORER_STATUSES:
        finite_state = FAILED
        finite_detail = _status_detail(
            FAILED,
            "Static scorer analysis found a missing, partial, or non-finite return path.",
            step_id=scorer_id,
            return_status=return_status,
        )
    elif scoring.get("scorer_bound") is True:
        finite_state = UNKNOWN
        finite_detail = _status_detail(
            UNKNOWN,
            "Static return analysis does not prove runtime finite values.",
            step_id=scorer_id,
            return_status=return_status,
        )
    else:
        finite_state = UNKNOWN
        finite_detail = _status_detail(
            UNKNOWN,
            "A scorer return value is not available for assessment.",
            step_id=scorer_id,
            return_status=return_status,
        )

    final_state, final_detail = _source_final_reward_state(
        checker_source,
        step_id,
        single_core_output=single_core_output,
    )
    final_detail = dict(final_detail)
    final_detail.update({"state": final_state, "status": final_state})
    chain = {
        "file": output_name,
        "step_id": step_id,
        "content_read": content_state,
        "scorer_binding": binding_state,
        "positive_effective_weight": weight_state,
        "finite_return": finite_state,
        "final_reward": final_state,
        "content_read_state": content_state,
        "scorer_binding_state": binding_state,
        "positive_effective_weight_state": weight_state,
        "finite_return_state": finite_state,
        "final_reward_state": final_state,
        "states": {
            "content_read": content_state,
            "scorer_binding": binding_state,
            "positive_effective_weight": weight_state,
            "finite_return": finite_state,
            "final_reward": final_state,
        },
        "evidence": {
            "content_read": content_detail,
            "scorer_binding": binding_detail,
            "positive_effective_weight": weight_detail,
            "finite_return": finite_detail,
            "final_reward": final_detail,
        },
        "repair_class": (
            "AUTO_FIX"
            if binding_detail.get("repair_class") == "AUTO_FIX"
            else "ASSISTED_FIX"
        ),
        "repair_scope": binding_detail.get(
            "repair_scope", "SCORING_SEMANTICS"
        ),
    }
    return chain


def _runtime_component_observations(
    tests: Iterable[dict[str, Any]], step_id: str | None
) -> list[dict[str, Any]]:
    if not step_id:
        return []
    observations: list[dict[str, Any]] = []
    for result in tests:
        if not usable_runtime_result(result):
            continue
        payload = _runtime_payload(result)
        if payload is None:
            continue
        breakdown = payload["breakdown"]
        component = breakdown.get(step_id)
        component_key = step_id
        if isinstance(component, dict):
            score = finite_number(component.get("score"))
            weight = finite_number(component.get("weight"))
        else:
            scalar = finite_number(component)
            if scalar is None:
                scalar_items = [
                    (str(key), finite_number(value))
                    for key, value in breakdown.items()
                    if key != "_errors" and finite_number(value) is not None
                ]
                if len(scalar_items) != 1:
                    continue
                component_key, scalar = scalar_items[0]
            score = scalar
            weight = None
        other_components = {
            str(key): value
            for key, value in breakdown.items()
            if key not in {component_key, "_errors"}
        }
        observations.append(
            {
                "case": payload.get("case") or result.get("test_type"),
                "reward": finite_number(payload.get("reward")),
                "score": score,
                "weight": weight,
                "component_key": component_key,
                "errors": breakdown.get("_errors", {}),
                "other_components": json.dumps(
                    other_components,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                    default=str,
                ),
            }
        )
    return observations


def _runtime_content_sensitive(
    tests: Iterable[dict[str, Any]], step_id: str | None
) -> bool:
    if not step_id:
        return False
    usable = _runtime_component_observations(tests, step_id)
    baseline = next(
        (
            result
            for result in usable
            if result.get("case") in {"known_valid_public", "positive_oracle"}
        ),
        None,
    )
    if baseline is None:
        return False
    baseline_pair = (
        finite_number(baseline.get("reward")),
        finite_number(baseline.get("score")),
    )
    for result in usable:
        if result.get("case") in {
            "known_valid_public",
            "positive_oracle",
            "component_isolation__" + str(step_id),
        }:
            continue
        pair = (
            finite_number(result.get("reward")),
            finite_number(result.get("score")),
        )
        if pair != baseline_pair:
            return True
    return False


def _refresh_aliases(chain: dict[str, Any]) -> None:
    for name in CHAIN_STATES:
        value = chain[name]
        chain[f"{name}_state"] = value
        chain["states"][name] = value


def merge_runtime_evidence(
    trace: dict[str, Any], checker_result: dict[str, Any] | None
) -> dict[str, Any]:
    """Merge E1 runtime observations into a previously static D6 trace."""

    if not isinstance(checker_result, dict):
        return trace
    tests = checker_result.get("tests", [])
    if not isinstance(tests, list):
        return trace
    for chain in trace.get("core_outputs", []):
        if not isinstance(chain, dict):
            continue
        observations = _runtime_component_observations(
            tests, chain.get("step_id")
        )
        valid_observations = [
            item for item in observations if item.get("score") is not None
        ]
        if valid_observations:
            if all(item.get("score") is not None for item in observations):
                chain["finite_return"] = PROVEN
                chain["evidence"]["finite_return"] = _status_detail(
                    PROVEN,
                    "Every observed component return is finite and error-free.",
                    cases=[item["case"] for item in observations],
                )
            weights = [item.get("weight") for item in valid_observations]
            if weights and all(
                weight is not None and weight > 0 for weight in weights
            ):
                chain["positive_effective_weight"] = PROVEN
                chain["evidence"]["positive_effective_weight"] = _status_detail(
                    PROVEN,
                    "The runtime breakdown records a positive component weight.",
                    weights=weights,
                )
            elif any(weight == 0 for weight in weights):
                chain["positive_effective_weight"] = FAILED
                chain["evidence"]["positive_effective_weight"] = _status_detail(
                    FAILED,
                    "The runtime breakdown records zero effective weight.",
                    weights=weights,
                )
            runtime_state, runtime_detail = _runtime_final_reward_dependence(
                valid_observations
            )
            if runtime_state == FAILED or (
                runtime_state == PROVEN and chain["final_reward"] != FAILED
            ):
                chain["final_reward"] = runtime_state
                chain["evidence"]["final_reward"] = _status_detail(
                    runtime_state,
                    runtime_detail["reason"],
                    **{
                        key: value
                        for key, value in runtime_detail.items()
                        if key != "reason"
                    },
                )
            if runtime_state == PROVEN or chain["final_reward"] == PROVEN:
                if chain["scorer_binding"] == UNKNOWN:
                    chain["scorer_binding"] = PROVEN
                    chain["evidence"]["scorer_binding"] = _status_detail(
                        PROVEN,
                        "Controlled E1 observations bind the direct checker "
                        "component to the scalar reward.",
                        component_keys=sorted(
                            {
                                str(item.get("component_key"))
                                for item in valid_observations
                            }
                        ),
                        source="runtime_component_isolation",
                    )
                declared_weight = finite_number(
                    chain["evidence"]["positive_effective_weight"].get(
                        "declared_weight"
                    )
                )
                if (
                    chain["positive_effective_weight"] == UNKNOWN
                    and declared_weight is not None
                    and declared_weight > 0
                ):
                    chain["positive_effective_weight"] = PROVEN
                    chain["evidence"]["positive_effective_weight"] = (
                        _status_detail(
                            PROVEN,
                            "A positive declared weight is effective in the "
                            "controlled scalar-reward dependence proof.",
                            declared_weight=declared_weight,
                            source="runtime_component_isolation",
                        )
                    )
        if (
            chain["content_read"] == UNKNOWN
            and _runtime_content_sensitive(tests, chain.get("step_id"))
        ):
            chain["content_read"] = PROVEN
            chain["evidence"]["content_read"] = _status_detail(
                PROVEN,
                "E1 content mutations changed the component/reward outcome.",
                source="runtime_content_sensitivity",
            )
    for chain in trace.get("core_outputs", []):
        if not isinstance(chain, dict):
            continue
        _refresh_aliases(chain)
        if chain["final_reward"] == FAILED:
            output = str(chain.get("file") or "")
            already_reported = any(
                item.get("code") == "CHECKER_RESULT_UNUSABLE"
                and item.get("evidence", {}).get("output") == output
                for item in trace.get("findings", [])
                if isinstance(item, dict)
            )
            if not already_reported:
                trace.setdefault("findings", []).append(
                    _finding(
                        "HIGH",
                        "CHECKER_RESULT_UNUSABLE",
                        "core output is not proven to affect the scalar final reward: "
                        + output,
                        {
                            "output": output,
                            "d6_state": chain["final_reward"],
                            "final_reward": chain["evidence"].get(
                                "final_reward"
                            ),
                            "d6_core_output": True,
                        },
                        ["tests/checker.py", "tests/grading_spec.json"],
                    )
                )
    trace["runtime"] = {
        "tests_available": len(tests),
        "usable_test_count": sum(usable_runtime_result(item) for item in tests),
        "source": "E1_checker_tests",
    }
    _refresh_trace_status(trace)
    return trace


def _refresh_trace_status(trace: dict[str, Any]) -> None:
    chains = [
        item for item in trace.get("core_outputs", []) if isinstance(item, dict)
    ]
    if not chains:
        trace["status"] = UNKNOWN
        trace["assessable"] = False
        return
    values = [chain[name] for chain in chains for name in CHAIN_STATES]
    trace["status"] = (
        FAILED
        if FAILED in values
        else PROVEN
        if all(value == PROVEN for value in values)
        else UNKNOWN
    )
    trace["assessable"] = trace["status"] == PROVEN


def _finding(
    severity: str,
    code: str,
    message: str,
    evidence: dict[str, Any],
    affected_files: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "severity": severity,
        "code": code,
        "message": message,
        "affected_files": affected_files
        or ["instruction.md", "tests/checker.py", "tests/grading_spec.json"],
        "evidence": evidence,
    }


def _basename(value: Any) -> str:
    return str(value or "").replace("\\", "/").rsplit("/", 1)[-1]


def _preferred_step(
    candidates: list[dict[str, Any]], output_name: str
) -> dict[str, Any] | None:
    matching = [
        step
        for step in candidates
        if _basename(step.get("output_file")) == _basename(output_name)
    ]
    if not matching:
        return None

    def priority(step: dict[str, Any]) -> tuple[bool, float, bool]:
        weight = finite_number(step.get("weight"))
        return (
            weight is not None and weight > 0,
            weight if weight is not None else float("-inf"),
            bool(step.get("scorer_bound")),
        )

    return max(matching, key=priority)


def analyze_static(
    *,
    contract_map: dict[str, Any],
    checker_analysis: dict[str, Any],
    grading_contract: dict[str, Any],
    checker_source: str,
) -> dict[str, Any]:
    """Create the static D6 trace and its deterministic findings."""

    steps = grading_contract.get("steps", grading_contract.get("checks", []))
    steps = steps if isinstance(steps, list) else []
    by_output = {
        _basename(item.get("file")): item
        for item in checker_analysis.get("outputs", [])
        if isinstance(item, dict) and item.get("file")
    }
    step_candidates = [
        step
        for step in steps
        if isinstance(step, dict) and step.get("output_file")
    ]
    scorer_bindings = checker_analysis.get("scorer_bindings", {})
    scorer_bindings = scorer_bindings if isinstance(scorer_bindings, dict) else {}
    scorer_status = checker_analysis.get("scorer_status", {})
    scorer_status = scorer_status if isinstance(scorer_status, dict) else {}
    core_outputs = set(contract_map.get("core_outputs", []))
    chains: list[dict[str, Any]] = []
    findings: list[dict[str, Any]] = []
    for output_name in sorted(core_outputs):
        output = by_output.get(_basename(output_name), {"file": output_name})
        chain = _static_chain(
            output,
            step=_preferred_step(step_candidates, output_name),
            checker_source=checker_source,
            scorer_bindings=scorer_bindings,
            scorer_status=scorer_status,
            single_core_output=len(core_outputs) == 1,
        )
        chains.append(chain)
        if chain["content_read"] == FAILED:
            findings.append(
                _finding(
                    "FATAL",
                    "CHECKER_CORE_TASK_UNASSESSED",
                    "load-bearing core output is not content-assessed: "
                    + output_name,
                    {
                        "output": output_name,
                        "d6_state": chain["content_read"],
                        "content_read": chain["evidence"]["content_read"],
                        "semantic_validation": output.get(
                            "semantic_validation"
                        ),
                    },
                )
            )
        if chain["scorer_binding"] == FAILED:
            binding = chain["evidence"]["scorer_binding"]
            findings.append(
                _finding(
                    "HIGH",
                    "SCORING_COMPONENT_NOT_BOUND",
                    "core output is not bound to a runtime scorer: "
                    + output_name,
                    {
                        "output": output_name,
                        **binding,
                        "d6_core_output": True,
                    },
                    ["tests/checker.py", "tests/grading_spec.json"],
                )
            )
        if chain["final_reward"] == FAILED:
            findings.append(
                _finding(
                    "HIGH",
                    "CHECKER_RESULT_UNUSABLE",
                    "core output is not proven to affect the scalar final reward: "
                    + output_name,
                    {
                        "output": output_name,
                        "d6_state": chain["final_reward"],
                        "final_reward": chain["evidence"]["final_reward"],
                        "d6_core_output": True,
                    },
                    ["tests/checker.py", "tests/grading_spec.json"],
                )
            )
    trace: dict[str, Any] = {
        "schema_version": D6_SCHEMA_VERSION,
        "status": UNKNOWN,
        "assessable": False,
        "core_outputs": chains,
        "findings": findings,
        "runtime": {
            "tests_available": 0,
            "usable_test_count": 0,
            "source": "NOT_RUN",
        },
    }
    _refresh_trace_status(trace)
    return trace


def analyze(
    *,
    contract_map: dict[str, Any],
    checker_analysis: dict[str, Any],
    grading_contract: dict[str, Any],
    checker_source: str,
    checker_result: dict[str, Any] | None = None,
) -> dict[str, Any]:
    trace = analyze_static(
        contract_map=contract_map,
        checker_analysis=checker_analysis,
        grading_contract=grading_contract,
        checker_source=checker_source,
    )
    return merge_runtime_evidence(trace, checker_result)
