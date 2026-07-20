"""Shared D1/D2 output-contract comparison helpers.

This module owns only deterministic declaration handling.  It deliberately
does not decide scientific values, units, requiredness, or definitions; any
disagreement in those fields is surfaced as an assisted repair finding.
"""

from __future__ import annotations

import itertools
import json
import re
from typing import Any, Iterable


OUTPUT_PATH_PATTERN = re.compile(
    r"/app/outputs/([^\s<>'\"`]+)", re.IGNORECASE
)
_FILE_FIELD_PATTERN = re.compile(
    r"""["']file["']\s*:\s*["']([^"']+)["']""", re.IGNORECASE
)
_TRAILING_SENTENCE_PUNCTUATION = ".,;:!?。！？；："
_PROCESS_PURPOSES = {
    "diagnostic",
    "intermediate",
    "process",
    "process_artifact",
    "process_evidence",
}

D1_AUTO_CODES = frozenset(
    {
        "OUTPUT_DECLARATION_MISMATCH",
        "OUTPUT_NOT_CONTRACTED",
        "OUTPUT_NOT_SCORED",
        "INSTRUCTION_ONLY_OUTPUT",
    }
)
D2_AUTO_CODES = frozenset({"INSTRUCTION_INTERNAL_INCONSISTENCY"})
D1_D2_SEMANTIC_CODES = frozenset(
    {
        "OUTPUT_FIELD_MISMATCH",
        "OUTPUT_UNIT_MISMATCH",
        "OUTPUT_REQUIREDNESS_MISMATCH",
        "OUTPUT_DEFINITION_AMBIGUITY",
    }
)


def _token_is_literal(text: str, start: int, end: int) -> bool:
    """Return whether a path token is quoted or inside a fenced code block."""

    before = text[:start]
    after = text[end:]
    if before.count("```") % 2 == 1:
        return True
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    if line_end < 0:
        line_end = len(text)
    line = text[line_start:line_end]
    token = text[start:end]
    return (
        f"`{token}`" in line
        or f"'{token}'" in line
        or f'"{token}"' in line
        or (before.rstrip().endswith(("`", "'", '"')) and after.lstrip().startswith(("`", "'", '"')))
    )


def _strip_prose_punctuation(text: str) -> str:
    """Strip punctuation only after a recognizable filename extension."""

    while text and text[-1] in _TRAILING_SENTENCE_PUNCTUATION:
        candidate = text[:-1]
        if not re.search(r"\.[A-Za-z0-9][A-Za-z0-9_-]*$", candidate):
            break
        text = candidate
    return text


def normalize_output_name(value: Any, *, literal: bool = False) -> str:
    """Return a stable output basename, preserving literal filename tokens."""

    if value is None:
        return ""
    text = str(value).strip().replace("\\", "/")
    text = text.strip("`'\"<>")
    if not literal:
        text = _strip_prose_punctuation(text.rstrip())
    return text.rsplit("/", 1)[-1]


def normalize_output_path_match(match: re.Match[str]) -> str:
    """Normalize a matched output path using its quoting/fence context."""

    return normalize_output_name(
        match.group(1),
        literal=_token_is_literal(
            match.string, match.start(0), match.end(1)
        ),
    )


def normalized_output_names(
    values: Iterable[Any], *, literal: bool = False
) -> set[str]:
    return {
        normalized
        for value in values
        if (normalized := normalize_output_name(value, literal=literal))
    }


def _scored_output_contract_items(grading_contract: Any) -> list[dict[str, Any]]:
    if not isinstance(grading_contract, dict):
        return []
    output_contract = grading_contract.get("output_contract", {})
    if not isinstance(output_contract, dict):
        return []
    outputs = output_contract.get("outputs", [])
    if not isinstance(outputs, list):
        return []
    result: list[dict[str, Any]] = []
    for item in outputs:
        if not isinstance(item, dict):
            continue
        purpose = str(item.get("purpose") or "").strip().lower()
        if item.get("scored") is False or purpose in _PROCESS_PURPOSES:
            continue
        result.append(item)
    return result


def scored_output_names(grading_contract: Any) -> set[str]:
    return normalized_output_names(
        (item.get("file") for item in _scored_output_contract_items(grading_contract)),
        literal=True,
    )


def grading_step_output_names(grading_contract: Any) -> set[str]:
    if not isinstance(grading_contract, dict):
        return set()
    raw_steps = grading_contract.get("steps", grading_contract.get("checks", []))
    if not isinstance(raw_steps, list):
        return set()
    names: list[str] = []
    for step in raw_steps:
        if not isinstance(step, dict):
            continue
        kind = str(step.get("kind") or step.get("purpose") or "").lower()
        if any(token in kind for token in _PROCESS_PURPOSES):
            continue
        names.append(step.get("output_file", step.get("file")))
    return normalized_output_names(names, literal=True)


def compare_scored_outputs(
    instruction_contract: Any, grading_contract: Any
) -> dict[str, Any]:
    """Compare instruction, structured, and grading scored output sets."""

    if not isinstance(instruction_contract, dict):
        instruction_contract = {}
    instruction_names = normalized_output_names(
        instruction_contract.get("scored_outputs", []),
        # This is already a structured contract field, not prose.  A valid
        # quoted filename may itself end in punctuation.
        literal=True,
    )
    structured_names = scored_output_names(grading_contract)
    grading_names = grading_step_output_names(grading_contract)
    declared = {
        "instruction": sorted(instruction_names),
        "output_contract": sorted(structured_names),
        "grading_steps": sorted(grading_names),
    }
    mismatches: list[dict[str, Any]] = []
    for left, right in itertools.combinations(declared, 2):
        left_values = set(declared[left])
        right_values = set(declared[right])
        if left_values == right_values:
            continue
        mismatches.append(
            {
                "left": left,
                "right": right,
                "only_in_left": sorted(left_values - right_values),
                "only_in_right": sorted(right_values - left_values),
            }
        )
    return {
        "declared_outputs": declared,
        "consistent": not mismatches,
        "mismatches": mismatches,
    }


def _instruction_sections(instruction: str) -> dict[str, str]:
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


def _section_for(
    sections: dict[str, str], *keywords: str
) -> tuple[str, str] | None:
    for name, body in sections.items():
        if all(keyword in name for keyword in keywords):
            return name, body
    return None


def _path_names(body: str) -> set[str]:
    return normalized_output_names(
        normalize_output_path_match(match)
        for match in OUTPUT_PATH_PATTERN.finditer(body)
    )


def _workflow_names(body: str) -> set[str]:
    names: list[str] = []
    for line in body.splitlines():
        if not re.match(r"^\s*-\s*Output file\s*:", line, re.IGNORECASE):
            continue
        match = OUTPUT_PATH_PATTERN.search(line)
        if match:
            names.append(normalize_output_path_match(match))
        else:
            names.append(line.split(":", 1)[1].strip())
    return normalized_output_names(names)


def _contract_names(body: str) -> set[str]:
    return _path_names(body) | normalized_output_names(
        (match.group(1) for match in _FILE_FIELD_PATTERN.finditer(body)),
        literal=True,
    )


def _self_check_names(body: str) -> set[str]:
    return _contract_names(body)


def _json_contract_values(body: str) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    for match in re.finditer(r"```(?:json)?\s*(.*?)```", body, re.IGNORECASE | re.DOTALL):
        try:
            candidate = json.loads(match.group(1))
        except (TypeError, ValueError, json.JSONDecodeError):
            continue
        if isinstance(candidate, dict):
            outputs = candidate.get("outputs", [])
            if isinstance(outputs, list):
                values.extend(item for item in outputs if isinstance(item, dict))
    return values


def _signature(item: dict[str, Any]) -> dict[str, Any]:
    schema = item.get("schema", {})
    if not isinstance(schema, dict):
        schema = {}
    columns = schema.get("required_columns", [])
    if not isinstance(columns, list):
        columns = []
    fields = schema.get("required", [])
    if isinstance(fields, dict):
        requiredness = {
            str(name): bool(value) for name, value in fields.items()
        }
        fields = list(fields)
    elif isinstance(fields, list):
        requiredness = {str(name): True for name in fields}
    else:
        fields = []
        requiredness = {}
    normalized_fields = [
        str(item.get("name") if isinstance(item, dict) else item)
        for item in columns or fields
        if str(item.get("name") if isinstance(item, dict) else item)
    ]
    units = schema.get("units", {})
    if not isinstance(units, dict):
        units = {}
    return {
        "fields": sorted(set(normalized_fields)),
        "units": {
            str(name): str(value)
            for name, value in sorted(units.items())
        },
        "requiredness": dict(sorted(requiredness.items())),
        "description": " ".join(str(item.get("description") or "").split()),
    }


def _section_signatures(
    body: str, *, include_workflow_text: bool = False
) -> dict[str, dict[str, Any]]:
    signatures: dict[str, dict[str, Any]] = {}
    for item in _json_contract_values(body):
        name = normalize_output_name(item.get("file"), literal=True)
        if name:
            signatures[name] = _signature(item)
    if include_workflow_text:
        for line in body.splitlines():
            match = re.search(
                r"columns?\s*:\s*(.+)$", line, re.IGNORECASE
            )
            if not match:
                continue
            fields: list[str] = []
            units: dict[str, str] = {}
            for raw_field in match.group(1).split(","):
                field = raw_field.strip()
                field_match = re.match(r"([A-Za-z_][\w-]*)\s*(?:\(([^)]*)\))?", field)
                if not field_match:
                    continue
                name, details = field_match.groups()
                fields.append(name)
                if details and "in " in details:
                    units[name] = details.split("in ", 1)[1].strip()
            if fields:
                signatures["__workflow__"] = {
                    "fields": sorted(set(fields)),
                    "units": dict(sorted(units.items())),
                    "requiredness": {},
                    "description": "",
                }
    return signatures


def compare_instruction_sections(instruction: str) -> dict[str, Any]:
    """Compare D2 section declarations and semantic contract signatures."""

    sections = _instruction_sections(instruction)
    selected: dict[str, str] = {}
    for label, keywords in (
        ("Workflow", ("workflow",)),
        ("Output files", ("output", "files")),
        ("Output contract", ("output", "contract")),
        ("Self-check", ("self-check",)),
    ):
        found = _section_for(sections, *keywords)
        if found is None and label == "Self-check":
            found = _section_for(sections, "self", "check")
        if found is not None:
            selected[label] = found[1]

    declarations: dict[str, set[str]] = {}
    for label, body in selected.items():
        if label == "Workflow":
            declarations[label] = _workflow_names(body)
        elif label == "Self-check":
            declarations[label] = _self_check_names(body)
        else:
            declarations[label] = _contract_names(body)

    mismatches: list[dict[str, Any]] = []
    for left, right in itertools.combinations(declarations, 2):
        if declarations[left] == declarations[right]:
            continue
        mismatches.append(
            {
                "left_section": left,
                "right_section": right,
                "only_in_left": sorted(declarations[left] - declarations[right]),
                "only_in_right": sorted(declarations[right] - declarations[left]),
            }
        )

    signatures: dict[str, dict[str, dict[str, Any]]] = {}
    for label, body in selected.items():
        signatures[label] = _section_signatures(
            body, include_workflow_text=label == "Workflow"
        )
    semantic_mismatches: list[dict[str, Any]] = []
    signature_sources = list(signatures)
    for left, right in itertools.combinations(signature_sources, 2):
        common = set(signatures[left]) & set(signatures[right])
        for output_name in sorted(common):
            left_signature = signatures[left][output_name]
            right_signature = signatures[right][output_name]
            for field, code in (
                ("fields", "OUTPUT_FIELD_MISMATCH"),
                ("units", "OUTPUT_UNIT_MISMATCH"),
                ("requiredness", "OUTPUT_REQUIREDNESS_MISMATCH"),
            ):
                if left_signature[field] != right_signature[field]:
                    semantic_mismatches.append(
                        {
                            "code": code,
                            "left_section": left,
                            "right_section": right,
                            "output": output_name,
                            "left": left_signature[field],
                            "right": right_signature[field],
                        }
                    )
            if (
                left_signature["description"]
                and right_signature["description"]
                and left_signature["description"]
                != right_signature["description"]
            ):
                semantic_mismatches.append(
                    {
                        "code": "OUTPUT_DEFINITION_AMBIGUITY",
                        "left_section": left,
                        "right_section": right,
                        "output": output_name,
                        "left": left_signature["description"],
                        "right": right_signature["description"],
                    }
                )
    return {
        "sections_present": sorted(selected),
        "declared_outputs_by_section": {
            name: sorted(values) for name, values in declarations.items()
        },
        "consistent": not mismatches and not semantic_mismatches,
        "mismatches": mismatches,
        "semantic_mismatches": semantic_mismatches,
    }


def repair_class_for_code(code: Any, evidence: Any = None) -> str | None:
    """Return the D1/D2 repair class for a finding code."""

    if code in D1_D2_SEMANTIC_CODES:
        return "ASSISTED_FIX"
    if code in D1_AUTO_CODES or code in D2_AUTO_CODES:
        if isinstance(evidence, dict) and evidence.get("ambiguous") is True:
            return "ASSISTED_FIX"
        return "AUTO_FIX"
    return None


def _replace_output_tokens(value: str) -> str:
    value = re.sub(
        r"/app/outputs/[^\s<>'\"`]+",
        "/app/outputs/<output>",
        value,
        flags=re.IGNORECASE,
    )
    return re.sub(
        r"\b[A-Za-z0-9_.-]+\.(?:csv|tsv|json|txt|dat|npy|npz|xyz|tar\.gz)\b",
        "<output>",
        value,
        flags=re.IGNORECASE,
    )


def _structural_text(value: str) -> str:
    masked = _replace_output_tokens(value)
    lines: list[str] = []
    for line in masked.splitlines():
        declaration = re.sub(
            r"^\s*(?:[-*]\s*)?(?:output\s+file\s*:\s*)?"
            r"`?/app/outputs/<output>`?[.,;:!?。！？；：]?\s*$",
            "",
            line,
            flags=re.IGNORECASE,
        )
        declaration = declaration.replace("<output>", "")
        if declaration.strip("`'\"[]{}(),:;.- \t"):
            lines.append(declaration.rstrip())
    return "\n".join(lines).strip()


def is_structural_auto_fix_operation(operation: dict[str, Any]) -> bool:
    """Allow only path/file-token synchronization for D1/D2 AUTO_FIX."""

    operation_type = operation.get("type")
    relative = str(operation.get("file") or "").replace("\\", "/")
    if relative not in {"instruction.md", "tests/grading_spec.json"}:
        return False
    if operation_type in {"replace_text", "text_replace"}:
        old = operation.get("old")
        new = operation.get("new")
        if not isinstance(old, str) or not isinstance(new, str) or not old or not new:
            return False
        return _structural_text(old) == _structural_text(new)
    if operation_type == "json_set":
        path = operation.get("path")
        value = operation.get("value")
        return (
            isinstance(path, list)
            and bool(path)
            and str(path[-1]).lower() in {"file", "output_file"}
            and isinstance(value, str)
            and bool(normalize_output_name(value))
        )
    return False


def output_repair_proof(contract_map: Any) -> dict[str, Any]:
    """Build the unique source-bound output token proof for AUTO_FIX."""

    if not isinstance(contract_map, dict):
        return {"proof_status": "INCOMPLETE", "expected_output_names": []}
    source_sets: list[set[str]] = []
    source_sets.append(
        normalized_output_names(
            contract_map.get("instruction_outputs", []), literal=True
        )
    )
    cross_file = contract_map.get("cross_file_sets")
    if isinstance(cross_file, dict):
        for key in ("contract_outputs", "grading_outputs"):
            source_sets.append(
                normalized_output_names(cross_file.get(key, []), literal=True)
            )
    if isinstance(contract_map.get("checker_analysis"), dict):
        checker = contract_map["checker_analysis"]
        source_sets.append(
            normalized_output_names(
                (
                    item.get("file")
                    for item in checker.get("outputs", [])
                    if isinstance(item, dict)
                ),
                literal=True,
            )
        )
    counts: dict[str, int] = {}
    for values in source_sets:
        for value in values:
            counts[value] = counts.get(value, 0) + 1
    expected = sorted(name for name, count in counts.items() if count >= 2)
    return {
        "proof_status": "PROVEN" if len(expected) == 1 else "INCOMPLETE",
        "expected_output_names": expected,
        "source_sets": [sorted(values) for values in source_sets if values],
    }


def structural_auto_fix_operation_error(
    operation: dict[str, Any], proof: Any
) -> str | None:
    """Require D1/D2 AUTO_FIX values to match the source-bound proof."""

    if not is_structural_auto_fix_operation(operation):
        return "D1/D2 AUTO_FIX is not a structural output synchronization"
    if not isinstance(proof, dict) or proof.get("proof_status") != "PROVEN":
        return "D1/D2 AUTO_FIX lacks a unique source-bound output proof"
    expected = {
        normalize_output_name(item, literal=True)
        for item in proof.get("expected_output_names", [])
        if normalize_output_name(item, literal=True)
    }
    if len(expected) != 1:
        return "D1/D2 AUTO_FIX output proof is ambiguous"
    value = operation.get("value")
    if operation.get("type") == "json_set":
        path = operation.get("path")
        if (
            not isinstance(path, list)
            or not path
            or str(path[-1]).lower() not in {"file", "output_file"}
            or not isinstance(value, str)
            or normalize_output_name(value, literal=True) not in expected
            or not (
                len(path) >= 3
                and str(path[0]) in {"steps", "checks", "output_contract"}
            )
        ):
            return "D1/D2 AUTO_FIX JSON path/value is not source-bound"
        return None
    new = operation.get("new")
    if not isinstance(new, str):
        return "D1/D2 AUTO_FIX replacement text is absent"
    new_names = {
        normalize_output_path_match(match)
        for match in OUTPUT_PATH_PATTERN.finditer(new)
    }
    new_names.update(
        normalize_output_name(match.group(1), literal=True)
        for match in _FILE_FIELD_PATTERN.finditer(new)
    )
    if new_names != expected:
        return "D1/D2 AUTO_FIX replacement value is not source-bound"
    return None
