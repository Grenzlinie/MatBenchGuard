"""D5 package-role and entrypoint completeness rules.

D5 is deliberately narrower than the complete Harbor package inventory.  Only
the public instruction, checker contract, verifier entrypoint, and privileged
Oracle entrypoint participate in this check.  Metadata/environment files are
never quality evidence here.
"""

from __future__ import annotations

import ast
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any


QUALITY_ROLE_PATHS = (
    "instruction.md",
    "tests/grading_spec.json",
    "tests/checker.py",
    "tests/test.sh",
)
METADATA_ROLE_PATHS = (
    "task.toml",
    "manifest.json",
    "steps.json",
    "resources.json",
    "environment",
)
ORACLE_ROLE_PATH = "solution/"
ORACLE_ENTRYPOINT_PATH = "solution/solve.sh"
VERIFIER_ENTRYPOINT_PATH = "tests/test.sh"

D5_FINDING_CODES = frozenset(
    {
        "MISSING_FILE",
        "PARSE_ERROR",
        "INVALID_GRADING_SPEC_SCHEMA",
        "QUALITY_ROLE_INVALID",
        "VERIFIER_ENTRYPOINT_MISSING",
        "VERIFIER_ENTRYPOINT_INVALID",
        "SOLUTION_ROLE_MISSING",
        "SOLUTION_ORACLE_MISSING",
        "SOLUTION_ORACLE_BROKEN",
    }
)

# These are deterministic candidates.  The operation policy still proves the
# exact transformation against the candidate package before mutation.
D5_AUTO_FIX_CODES = frozenset(
    {
        "PARSE_ERROR",
        "QUALITY_ROLE_INVALID",
        "VERIFIER_ENTRYPOINT_INVALID",
        "SOLUTION_ORACLE_MISSING",
    }
)

_IMPLEMENTATION_SUFFIXES = frozenset(
    {
        ".c",
        ".cc",
        ".cpp",
        ".f",
        ".f90",
        ".go",
        ".java",
        ".jl",
        ".js",
        ".m",
        ".py",
        ".r",
        ".R",
        ".rb",
        ".sh",
        ".swift",
        ".ts",
    }
)
_INLINE_OR_GENERATION_MARKERS = (
    "<<",
    "python -c",
    "python3 -c",
    "python - <<",
    "python3 - <<",
    "perl -e",
    "ruby -e",
    "eval ",
    "base64 -d",
    "cat >",
    "tee ",
)


def _raw_status(value: Any) -> str:
    if isinstance(value, dict):
        for key in ("status", "parse_status", "state", "entrypoint"):
            if key in value:
                return _raw_status(value[key])
        return "UNKNOWN"
    if value is None:
        return "MISSING"
    text = str(value).strip().lower()
    if text in {
        "ok",
        "valid",
        "present",
        "present_not_inspected",
        "parseable",
        "available",
        "pass",
    }:
        return "OK"
    if "missing" in text or text in {"absent", "not_present"}:
        return "MISSING"
    if (
        "error" in text
        or "invalid" in text
        or "broken" in text
        or "unparseable" in text
        or text in {"fail", "failed"}
    ):
        return "INVALID"
    return "UNKNOWN"


def _role_mapping(package_roles: Any) -> dict[str, Any] | None:
    if not isinstance(package_roles, dict) or not package_roles:
        return None
    nested = package_roles.get("quality_roles")
    if isinstance(nested, dict):
        return nested
    return {
        role: package_roles[role]
        for role in QUALITY_ROLE_PATHS
        if role in package_roles
    }


def package_role_snapshot(package_roles: Any) -> dict[str, Any]:
    """Normalize legacy and structured package-role input for D5 evidence."""

    quality = _role_mapping(package_roles)
    if quality is None:
        return {
            "available": False,
            "quality_roles": {},
            "metadata_roles_excluded": list(METADATA_ROLE_PATHS),
            "oracle_entrypoint": {"status": "UNKNOWN"},
        }

    quality_roles = {
        role: {
            "status": _raw_status(quality.get(role)),
            "quality_evidence": True,
        }
        for role in QUALITY_ROLE_PATHS
    }
    oracle = package_roles.get("oracle_entrypoint")
    if oracle is None:
        oracle = package_roles.get("oracle")
    if oracle is None:
        oracle = package_roles.get(ORACLE_ROLE_PATH)
    oracle_status = _raw_status(oracle)
    return {
        "available": True,
        "quality_roles": quality_roles,
        "metadata_roles_excluded": list(METADATA_ROLE_PATHS),
        "oracle_entrypoint": {
            "path": ORACLE_ENTRYPOINT_PATH,
            "status": oracle_status,
            "quality_evidence": True,
        },
    }


def d5_role_failures(package_roles: Any) -> list[str]:
    """Return quality-role paths that are missing or invalid."""

    snapshot = package_role_snapshot(package_roles)
    if not snapshot["available"]:
        return []
    failures = [
        role
        for role, state in snapshot["quality_roles"].items()
        if state["status"] in {"MISSING", "INVALID"}
    ]
    oracle_status = snapshot["oracle_entrypoint"]["status"]
    if oracle_status in {"MISSING", "INVALID"}:
        failures.append(ORACLE_ENTRYPOINT_PATH)
    return sorted(failures)


def repair_class_for_finding(
    title: Any, affected_files: Any = None, evidence: Any = None
) -> str | None:
    """Return D5's safe default class for a finding.

    Missing/broken scientific producers are never promoted to AUTO_FIX.
    A missing ``solve.sh`` is an AUTO_FIX candidate only because the Repair
    policy separately proves that it is a thin wrapper around one existing
    implementation.
    """

    if not isinstance(title, str) or title not in D5_FINDING_CODES:
        return None
    if title in {"SOLUTION_ROLE_MISSING", "SOLUTION_ORACLE_BROKEN"}:
        return "ASSISTED_FIX"
    if title == "MISSING_FILE":
        files = affected_files if isinstance(affected_files, list) else []
        if ORACLE_ENTRYPOINT_PATH in files:
            return "AUTO_FIX"
        return "ASSISTED_FIX"
    if title in D5_AUTO_FIX_CODES:
        return "AUTO_FIX"
    return "ASSISTED_FIX"


def _implementation_candidates(root: Path, role: str = "solution") -> list[Path]:
    directory = root / role
    if not directory.is_dir() or directory.is_symlink():
        return []
    candidates: list[Path] = []
    for path in sorted(directory.iterdir()):
        if (
            not path.is_file()
            or path.is_symlink()
            or path.name in {"solve.sh", "test.sh"}
            or path.name.startswith(".")
        ):
            continue
        if path.suffix in _IMPLEMENTATION_SUFFIXES or os.access(
            path, os.X_OK
        ):
            candidates.append(path)
    return candidates


def _referenced_candidate(content: str, candidates: list[Path]) -> list[Path]:
    return [
        candidate
        for candidate in candidates
        if re.search(rf"(?<![\w.-]){re.escape(candidate.name)}(?![\w.-])", content)
    ]


def validate_unique_wrapper(
    root: Path, operation: dict[str, Any], *, target: str = ORACLE_ENTRYPOINT_PATH
) -> None:
    """Prove that a new entrypoint is a thin wrapper around one implementation."""

    if operation.get("type") != "write_file":
        raise ValueError("AUTO_FIX entrypoint repair must write a new wrapper")
    if Path(str(operation.get("file", ""))).as_posix() != target:
        raise ValueError("AUTO_FIX wrapper target is not a supported entrypoint")
    content = operation.get("content")
    if not isinstance(content, str) or not content.strip():
        raise ValueError("AUTO_FIX wrapper must contain shell text")
    if operation.get("executable") is not True:
        raise ValueError("AUTO_FIX wrapper must preserve an executable entrypoint")
    lowered = content.lower()
    if any(marker in lowered for marker in _INLINE_OR_GENERATION_MARKERS):
        raise ValueError(
            "AUTO_FIX wrapper may not embed or generate scientific producer logic"
        )

    role = "solution" if target == ORACLE_ENTRYPOINT_PATH else "tests"
    candidates = _implementation_candidates(root, role)
    if len(candidates) != 1:
        raise ValueError(
            "AUTO_FIX wrapper requires exactly one existing implementation"
        )
    references = _referenced_candidate(content, candidates)
    if references != candidates:
        raise ValueError(
            "AUTO_FIX wrapper must invoke the unique existing implementation"
        )
    if operation.get("implementation") not in {None, candidates[0].name}:
        raise ValueError("AUTO_FIX wrapper implementation binding is ambiguous")
    invocation_lines = [
        line
        for line in content.splitlines()
        if candidates[0].name in line
        and not line.lstrip().startswith("#")
    ]
    if len(invocation_lines) != 1:
        raise ValueError("AUTO_FIX wrapper must invoke one implementation once")
    if not re.search(
        r"(?:^|\s)(?:exec\s+)?(?:python3?|bash|sh|ruby|node|julia|Rscript)"
        r"(?:\s+|$)",
        invocation_lines[0],
    ):
        raise ValueError("AUTO_FIX wrapper does not contain a standard invocation")


def _json_syntax_candidates(text: str) -> list[str]:
    values = [text, re.sub(r",(\s*[}\]])", r"\1", text)]
    bases = list(values)
    for base in bases:
        stripped = base.rstrip()
        for suffix in ("}", "]", "}", "]}", "}]"):
            values.append(stripped + suffix)
    return values


def _same_json_value(before: str, after: str) -> bool:
    try:
        return json.loads(before) == json.loads(after)
    except (TypeError, ValueError, json.JSONDecodeError):
        return False


def _same_python_tree(before: str, after: str) -> bool:
    try:
        before_tree = ast.parse(before)
        after_tree = ast.parse(after)
    except (SyntaxError, TypeError, ValueError):
        return False
    return ast.dump(before_tree) == ast.dump(after_tree)


def _delimiter_only_repair(before: str, after: str) -> bool:
    if after.rstrip() in {before.rstrip() + suffix for suffix in (":", ")", "]", "}")}:
        return True
    return False


def is_structural_syntax_repair(root: Path, operation: dict[str, Any]) -> bool:
    """Accept only parser-preserving or delimiter-only syntax repairs."""

    relative = Path(str(operation.get("file", ""))).as_posix()
    if relative not in {
        "tests/grading_spec.json",
        "tests/checker.py",
        "tests/test.sh",
    }:
        return False
    if operation.get("type") not in {"replace_text", "text_replace"}:
        return False
    before = operation.get("old")
    after = operation.get("new")
    if not isinstance(before, str) or not isinstance(after, str):
        return False
    if relative.endswith(".json"):
        return _same_json_value(before, after) or any(
            _same_json_value(candidate, after)
            for candidate in _json_syntax_candidates(before)
        )
    if relative.endswith(".py"):
        if _same_python_tree(before, after):
            return True
        if not _delimiter_only_repair(before, after):
            return False
        try:
            ast.parse(after)
        except (SyntaxError, TypeError, ValueError):
            return False
        return True
    if relative.endswith(".sh"):
        if not _delimiter_only_repair(before, after):
            return False
        result = subprocess.run(
            ["bash", "-n"],
            input=after,
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode == 0
    return False


def validate_auto_fix_operation(
    root: Path, operation: dict[str, Any], finding_code: str | None
) -> None:
    """Validate the D5-specific portion of an AUTO_FIX operation."""

    relative = Path(str(operation.get("file", ""))).as_posix()
    if relative == ORACLE_ENTRYPOINT_PATH:
        validate_unique_wrapper(root, operation)
        return
    if finding_code in D5_AUTO_FIX_CODES and is_structural_syntax_repair(
        root, operation
    ):
        return
    raise ValueError(
        "D5 AUTO_FIX is limited to a unique entrypoint wrapper or "
        "deterministically recoverable structural syntax"
    )

