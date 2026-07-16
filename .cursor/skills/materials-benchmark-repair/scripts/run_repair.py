#!/usr/bin/env python3
"""Repair one audited Harbor package through an isolated atomic workflow."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any, Iterable

sys.dont_write_bytecode = True

DECISIONS = {"AUTO_FIX", "ASSISTED_FIX", "ABANDON"}
REPAIR_CLASSES = {"AUTO_FIX", "ASSISTED_FIX"}
OPERATION_TYPES = {"write_file", "replace_text", "text_replace", "json_set", "delete_file"}
REGRESSION_TYPES = {
    "file_exists",
    "file_absent",
    "file_executable",
    "text_contains",
    "text_not_contains",
    "json_path_equals",
    "command",
}
GENERATED_TOP_LEVEL = {
    "benchmark_audit",
    "benchmark_audit_history",
    "benchmark_repair",
    ".benchmark_audit_tmp",
    ".benchmark_repair_tmp",
}
EVIDENCE_SOURCE_PREFIX = "benchmark_audit:"
REQUIRED_AUDIT_EXECUTION_LEVEL = "E1"
CORE_CONTRACT_SCHEMA = "materials-core-contract/1.0"
REPAIR_BUNDLE_FILES = (
    "repair_plan.json",
    "changes.json",
    "unresolved.json",
    "regression_results.json",
    "re_audit_comparison.json",
    "patch.json",
    "evidence.json",
    "repair.log",
    "history.json",
)
PRECISION_RULES = {
    "json_key": ("key", "type", "required", "unit"),
    "csv_column": ("column", "type", "required", "unit"),
    "npy_array": ("shape", "dtype", "axis_semantics", "unit"),
    "gold": ("value", "unit", "source_or_derivation"),
    "tolerance": ("error_basis", "direction", "mode"),
    "weight": ("scoring_contract", "mathematical_proof"),
    "scientific_method": ("claim",),
    "exception_guard": ("stack_trace", "existing_reading_code"),
    "harbor_path": ("official_contract", "existing_path_code"),
}


class PolicyStop(Exception):
    """A non-mutating policy stop reported through the CLI result."""

    def __init__(self, status: str, reason: str) -> None:
        super().__init__(reason)
        self.status = status
        self.reason = reason


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def sha256_path(path: Path) -> str:
    """Hash an external file or directory without following symlink entries."""
    if path.is_symlink():
        raise ValueError(f"external evidence may not be a symbolic link: {path}")
    if path.is_file():
        return sha256_file(path)
    if not path.is_dir():
        raise FileNotFoundError(path)
    entries: list[tuple[str, str]] = []
    for child in sorted(path.rglob("*")):
        if child.is_symlink():
            raise ValueError(
                f"external evidence may not contain symbolic links: {child}"
            )
        if child.is_file():
            entries.append((child.relative_to(path).as_posix(), sha256_file(child)))
    payload = json.dumps(
        entries, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def core_contract_snapshot(root: Path) -> dict[str, Any]:
    """Return the frozen public contract used to bind a repair plan."""
    values: dict[str, Any] = {}
    for relative in ("instruction.md", "tests/checker.py"):
        path = root / relative
        values[relative] = (
            path.read_text(encoding="utf-8", errors="replace")
            if path.is_file()
            else None
        )
    specification_path = root / "tests/grading_spec.json"
    if specification_path.is_file():
        try:
            specification = read_json(specification_path)
        except (OSError, ValueError, json.JSONDecodeError):
            specification = None
    else:
        specification = None
    values["grading_contract"] = specification
    return {
        "schema_version": CORE_CONTRACT_SCHEMA,
        "instruction": values["instruction.md"],
        "checker": values["tests/checker.py"],
        "grading_contract": values["grading_contract"],
    }


def core_contract_digest(root: Path) -> str:
    payload = json.dumps(
        core_contract_snapshot(root),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def timestamp() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def unique_id(prefix: str) -> str:
    return (
        time.strftime(f"{prefix}-%Y%m%dT%H%M%SZ-", time.gmtime())
        + uuid.uuid4().hex[:8]
    )


def validated_relative(relative: Any, *, context: str) -> Path:
    if not isinstance(relative, str) or not relative.strip():
        raise ValueError(f"{context} must be a non-empty relative path")
    if "://" in relative or relative.startswith(("file:", "http:", "https:")):
        raise ValueError(f"{context} may not be a URL")
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or path.as_posix().startswith("/"):
        raise ValueError(f"{context} escapes the Harbor 题包")
    return path


def is_modifiable(relative: Path) -> bool:
    parts = relative.parts
    return (
        relative.as_posix() == "instruction.md"
        or (len(parts) >= 2 and parts[0] in {"tests", "solution"})
    )


def repair_target(root: Path, relative: Any) -> tuple[Path, Path]:
    relative_path = validated_relative(relative, context="operation file")
    if not is_modifiable(relative_path):
        raise ValueError(
            "unsupported repair target; only instruction.md, tests/**, and "
            "solution/** are modifiable"
        )
    current = root
    for part in relative_path.parts:
        current = current / part
        if current.exists() and current.is_symlink():
            raise ValueError("repair target may not traverse a symbolic link")
    return root / relative_path, relative_path


def package_path(root: Path, relative: Any, *, context: str) -> tuple[Path, Path]:
    relative_path = validated_relative(relative, context=context)
    current = root
    for part in relative_path.parts:
        current = current / part
        if current.exists() and current.is_symlink():
            raise ValueError(f"{context} may not traverse a symbolic link")
    path = root / relative_path
    if path.exists() and not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"{context} escapes the Harbor 题包")
    return path, relative_path


def validate_external_plan(root: Path, plan_path: Path) -> dict[str, Any]:
    resolved = plan_path.expanduser().resolve()
    if resolved.is_relative_to(root.resolve()):
        raise ValueError("repair plan must remain outside the Harbor 题包")
    if not resolved.is_file():
        raise FileNotFoundError(f"repair plan is missing: {resolved}")
    plan = read_json(resolved)
    if isinstance(plan, dict) and "repair_class" not in plan:
        if plan.get("decision") in DECISIONS:
            plan["repair_class"] = plan["decision"]
    if not isinstance(plan, dict) or plan.get("schema_version") != "0.1":
        raise ValueError("repair plan must use schema_version 0.1")
    if "source_audit" not in plan and isinstance(plan.get("audit_binding"), dict):
        plan["source_audit"] = plan["audit_binding"]
    if plan.get("repair_class") not in DECISIONS:
        raise ValueError(
            "repair_class must be AUTO_FIX, ASSISTED_FIX, or ABANDON"
        )
    if not isinstance(plan.get("justification"), str) or not plan[
        "justification"
    ].strip():
        raise ValueError("repair plan requires a justification")
    if not isinstance(plan.get("audit_id"), str) or not plan["audit_id"]:
        raise ValueError("repair plan requires audit_id")
    if not isinstance(plan.get("finding_id"), str) or not plan["finding_id"]:
        raise ValueError("repair plan requires finding_id")
    operations = plan.get("operations")
    regressions = plan.get("regression_tests")
    if not isinstance(operations, list):
        raise ValueError("repair plan operations must be a list")
    if not isinstance(regressions, list):
        raise ValueError("repair plan regression_tests must be a list")
    if plan.get("repair_class") != "ABANDON" and not operations:
        raise ValueError("repair plan requires at least one operation")
    if plan.get("repair_class") != "ABANDON" and not regressions:
        raise ValueError("repair plan requires regression tests")
    operation_ids: set[str] = set()
    for operation in operations:
        if not isinstance(operation, dict):
            raise ValueError("every repair operation must be an object")
        operation_id = operation.get("id")
        if not isinstance(operation_id, str) or not operation_id:
            raise ValueError("every repair operation requires a stable id")
        if operation_id in operation_ids:
            raise ValueError(f"duplicate repair operation id: {operation_id}")
        operation_ids.add(operation_id)
        if operation.get("type") not in OPERATION_TYPES:
            raise ValueError(f"unsupported repair operation: {operation.get('type')}")
        repair_target(root, operation.get("file"))
    for index, specification in enumerate(regressions, start=1):
        if not isinstance(specification, dict):
            raise ValueError("every regression test must be an object")
        if specification.get("type") not in REGRESSION_TYPES:
            raise ValueError(
                f"unsupported regression test type: {specification.get('type')}"
            )
        if plan.get("repair_class") == "ABANDON":
            raise ValueError("ABANDON plans may not carry regressions")
        if not isinstance(specification.get("id"), str) or not specification["id"]:
            raise ValueError(f"regression test {index} requires a stable id")
        if specification.get("finding_id") != plan["finding_id"]:
            raise ValueError(
                f"regression test {index} must bind the target finding"
            )
        causal = specification.get("causal_operation_ids")
        if not isinstance(causal, list) or not causal:
            raise ValueError(
                f"regression test {index} requires causal_operation_ids"
            )
        if not all(
            isinstance(item, str) and item in operation_ids for item in causal
        ):
            raise ValueError(
                f"regression test {index} links an unknown causal operation"
            )
        if specification.get("expected_before", False) is not False:
            raise ValueError("regressions must fail before the repair")
        if specification.get("expected_after", True) is not True:
            raise ValueError("regressions must pass after the repair")
    return plan


def external_binding_hashes(
    root: Path, plan: dict[str, Any], source_audit: dict[str, Any]
) -> tuple[dict[str, str], dict[str, str]]:
    fixture_hashes: dict[str, str] = {}
    assessment_hashes: dict[str, str] = {}
    for key, target in (
        ("known_valid_output", fixture_hashes),
        ("agent_assessment", assessment_hashes),
    ):
        raw = plan.get(key)
        if raw is None:
            continue
        external = Path(str(raw)).expanduser()
        resolved = external.resolve()
        if resolved.is_relative_to(root.resolve()):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"{key} must remain outside the Harbor 题包",
            )
        try:
            target[key] = sha256_path(resolved)
        except (OSError, ValueError) as exc:
            raise PolicyStop(
                "BLOCKED_EVIDENCE", f"{key} is not valid external evidence: {exc}"
            ) from exc

    def normalize(value: Any, field: str) -> dict[str, str]:
        if value is None:
            return {}
        if not isinstance(value, dict):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"source_audit.{field} must be a hash mapping",
            )
        normalized: dict[str, str] = {}
        for name, raw_hash in value.items():
            if isinstance(raw_hash, dict):
                raw_hash = raw_hash.get("hash")
            if not isinstance(name, str) or not isinstance(raw_hash, str):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    f"source_audit.{field} contains an invalid hash",
                )
            normalized[name] = raw_hash
        return normalized

    expected_fixtures = normalize(source_audit.get("fixture_hashes"), "fixture_hashes")
    expected_assessments = normalize(
        source_audit.get("assessment_hashes"), "assessment_hashes"
    )
    if expected_fixtures != fixture_hashes:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source audit fixture hashes do not bind the supplied fixture",
        )
    if expected_assessments != assessment_hashes:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source audit assessment hashes do not bind the supplied assessment",
        )
    return fixture_hashes, assessment_hashes


def validate_source_audit_binding(
    root: Path,
    report: dict[str, Any],
    manifest: dict[str, Any],
    finding: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, Any]:
    source_audit = plan.get("source_audit")
    if not isinstance(source_audit, dict):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "Repair requires a complete source-audit binding.",
        )
    expected_audit_id = report.get("audit_id")
    if (
        source_audit.get("audit_id") != expected_audit_id
        or source_audit.get("audit_id") != manifest.get("audit_id")
        or source_audit.get("finding_id") != plan.get("finding_id")
        or source_audit.get("finding_id") != finding.get("finding_id")
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source audit identity is not bound to the authoritative audit",
        )
    if finding.get("status") != "OPEN":
        raise PolicyStop(
            "ABANDON",
            "The selected finding is not OPEN and cannot be repaired.",
        )
    if source_audit.get("finding_status") != "OPEN":
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source audit must explicitly bind an OPEN finding",
        )
    input_hashes = manifest.get("input_hashes")
    if not isinstance(input_hashes, dict) or not input_hashes:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit lacks complete package input hashes",
        )
    bound_input_hashes = source_audit.get("input_hashes")
    if bound_input_hashes is None:
        bound_input_hashes = source_audit.get("package_hashes")
    if bound_input_hashes is None:
        bound_input_hashes = source_audit.get("source_hashes")
    if bound_input_hashes != input_hashes:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source audit package hashes differ from the authoritative audit",
        )
    implementation = manifest.get("review_implementation")
    if not isinstance(implementation, dict) or not implementation:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit lacks Review implementation hashes",
        )
    bound_implementation = source_audit.get("review_implementation")
    if bound_implementation is None:
        bound_implementation = source_audit.get("review_implementation_hash")
    if bound_implementation != implementation:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source audit Review implementation hash is stale",
        )
    configuration = report.get("configuration")
    if not isinstance(configuration, dict):
        raise PolicyStop(
            "BLOCKED_EVIDENCE", "authoritative audit lacks configuration"
        )
    if (
        source_audit.get("paper_mode", source_audit.get("paper_review_mode"))
        != configuration.get("paper_mode")
        or source_audit.get(
            "execution_level", source_audit.get("evidence_depth")
        )
        != REQUIRED_AUDIT_EXECUTION_LEVEL
        or configuration.get("execution_level") != REQUIRED_AUDIT_EXECUTION_LEVEL
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "Repair source audit and re-audit must be fixed at E1 depth",
        )
    digest = core_contract_digest(root)
    bound_digest = source_audit.get("core_contract_digest")
    if bound_digest is None and isinstance(source_audit.get("core_contract"), dict):
        bound_digest = source_audit["core_contract"].get("digest")
    if plan.get("core_contract_digest") != digest or bound_digest != digest:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "frozen core-contract digest is stale or incomplete",
        )
    external_binding_hashes(root, plan, source_audit)
    return source_audit


def validate_fresh_audit(
    root: Path, plan: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    audit = root / "benchmark_audit"
    report = read_json(audit / "audit_report.json")
    manifest = read_json(audit / "audit_manifest.json")
    disposition = read_json(audit / "disposition.json")
    if plan["audit_id"] != report.get("audit_id"):
        raise ValueError("stale audit: plan audit_id is not authoritative")
    route = disposition.get("route") or report.get("summary", {}).get("disposition")
    if route != "REPAIR_QUEUE":
        raise ValueError("authoritative audit is not routed to REPAIR_QUEUE")
    findings = {
        item.get("finding_id"): item
        for item in report.get("findings", [])
        if isinstance(item, dict) and isinstance(item.get("finding_id"), str)
    }
    if plan["finding_id"] not in findings:
        raise ValueError("repair plan finding_id is not open in the audit")
    input_hashes = manifest.get("input_hashes")
    if not isinstance(input_hashes, dict):
        raise ValueError("audit manifest input_hashes must be an object")
    for relative, expected in input_hashes.items():
        source, relative_path = package_path(
            root, relative, context="audit manifest input path"
        )
        if relative_path.parts[0] in GENERATED_TOP_LEVEL:
            raise ValueError("audit manifest hashes a generated report path")
        if not source.is_file() or sha256_file(source) != expected:
            raise ValueError(f"stale audit: input changed since review: {relative}")
    finding = findings[plan["finding_id"]]
    if plan.get("repair_class") != "ABANDON":
        validate_source_audit_binding(root, report, manifest, finding, plan)
    elif finding.get("status") != "OPEN":
        raise PolicyStop(
            "ABANDON",
            "The selected finding is not OPEN and cannot be repaired.",
        )
    return report, manifest, finding


def evidence_index(
    root: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    raw = plan.get("evidence")
    if not isinstance(raw, list) or not raw:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "External Agent repair plans require non-empty evidence.",
        )
    indexed: dict[str, dict[str, Any]] = {}
    for item in raw:
        if not isinstance(item, dict):
            raise PolicyStop("BLOCKED_EVIDENCE", "Evidence items must be objects.")
        evidence_id = item.get("id")
        source = item.get("source")
        quote = item.get("quote")
        if not all(isinstance(value, str) and value.strip() for value in (evidence_id, source, quote)):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "Each evidence item requires non-empty id, source, and quote.",
            )
        if evidence_id in indexed:
            raise PolicyStop(
                "BLOCKED_EVIDENCE", f"Duplicate evidence id: {evidence_id}"
            )
        if "://" in source or source.startswith(("file:", "http:", "https:")):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "Evidence sources must be local package files.",
            )
        if source.startswith(EVIDENCE_SOURCE_PREFIX):
            if source != f"{EVIDENCE_SOURCE_PREFIX}{plan['finding_id']}":
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "Audit evidence must bind the selected finding.",
                )
            local = root / "benchmark_audit/audit_report.json"
            source_kind = "audit"
        else:
            try:
                local, relative = package_path(
                    root, source, context="evidence source"
                )
            except (TypeError, ValueError) as exc:
                raise PolicyStop("BLOCKED_EVIDENCE", str(exc)) from exc
            if relative.parts and relative.parts[0] in {"solution"}:
                source_kind = "solution"
            else:
                source_kind = "package"
        if not local.is_file():
            raise PolicyStop(
                "BLOCKED_EVIDENCE", f"Evidence source does not exist: {source}"
            )
        if local.is_symlink() or not local.resolve().is_relative_to(root.resolve()):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"Evidence source escapes the Harbor 题包: {source}",
            )
        text = local.read_text(encoding="utf-8", errors="replace")
        if quote not in text:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"Evidence quote is absent from {source}.",
            )
        supplied_hash = next(
            (
                item.get(name)
                for name in ("source_hash", "sha256", "hash")
                if item.get(name) is not None
            ),
            None,
        )
        actual_hash = sha256_file(local)
        if supplied_hash != actual_hash:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"Evidence hash does not match {source}.",
            )
        normalized = dict(item)
        normalized["source_kind"] = source_kind
        normalized["source_hash"] = actual_hash
        indexed[evidence_id] = normalized
    return indexed


def linked_evidence(
    operation: dict[str, Any],
    evidence: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    evidence_ids = operation.get("evidence_ids")
    if not isinstance(evidence_ids, list) or not evidence_ids:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"Operation {operation.get('id')} requires linked evidence.",
        )
    if not all(isinstance(item, str) and item in evidence for item in evidence_ids):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"Operation {operation.get('id')} links unknown evidence.",
        )
    return [evidence[item] for item in evidence_ids]


def precision_kind_for(operation: dict[str, Any]) -> str | None:
    explicit = operation.get("precision_kind")
    if isinstance(explicit, str) and explicit:
        return explicit
    relative = Path(str(operation.get("file", ""))).as_posix()
    if operation.get("type") == "json_set":
        tokens = operation.get("path")
        final = str(tokens[-1]).lower() if isinstance(tokens, list) and tokens else ""
        if "threshold" in final or "tolerance" in final:
            return "tolerance"
        if "weight" in final:
            return "weight"
        if any(term in final for term in ("gold", "target", "reference")):
            return "gold"
        return "json_key"
    if relative.lower().endswith(".csv"):
        return "csv_column"
    if relative.lower().endswith(".npy"):
        return "npy_array"
    if relative == "instruction.md":
        return "scientific_method"
    if relative.startswith("tests/"):
        return "harbor_path"
    if relative.startswith("solution/"):
        return None
    return "harbor_path"


def validate_precision_matrix(
    operation: dict[str, Any],
    linked: list[dict[str, Any]],
    repair_class: str,
) -> None:
    expected = precision_kind_for(operation)
    if expected is None:
        return
    if repair_class == "AUTO_FIX" and Path(str(operation["file"])).as_posix() != (
        "instruction.md"
    ):
        # Deterministic AUTO_FIX operations use a Harbor contract/finding rather
        # than inventing scientific precision.  Core targets are rejected below.
        return
    valid: list[dict[str, Any]] = []
    for item in linked:
        precision = item.get("precision")
        if not isinstance(precision, dict):
            precision = {}
        precision = dict(precision)
        for canonical, aliases in {
            "required": ("requiredness",),
            "unit": ("units",),
            "axis_semantics": ("axes", "axis"),
            "source_or_derivation": ("derivation", "source"),
            "error_basis": ("basis",),
            "mode": ("abs_rel", "absolute_or_relative"),
            "stack_trace": ("stack", "traceback"),
            "existing_reading_code": ("reading_code",),
        }.items():
            if canonical not in precision:
                for alias in aliases:
                    if alias in precision:
                        precision[canonical] = precision[alias]
                        break
        kind = precision.get("kind") or item.get("kind")
        if kind != expected:
            continue
        valid.append(precision)
    if not valid:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"Evidence precision does not match {expected} for "
            f"{operation.get('file')}.",
        )
    required = PRECISION_RULES[expected]
    if not all(all(field in precision for field in required) for precision in valid):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"{expected} evidence lacks the required typed precision fields.",
        )
    if expected == "json_key":
        operation_path = operation.get("path")
        operation_key = (
            str(operation_path[-1])
            if isinstance(operation_path, list) and operation_path
            else None
        )
        if any(
            precision.get("key") != operation_key
            for precision in valid
            if operation_key is not None
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "JSON evidence key does not match the operation path.",
            )
    method_items = [
        item
        for item in linked
        if (
            (item.get("precision") or {}).get("kind") == expected
            if isinstance(item.get("precision"), dict)
            else item.get("kind") == expected
        )
        or item.get("kind") == expected
    ]
    if expected == "scientific_method" and any(
        item.get("source_kind") not in {"package"}
        or not str(item.get("source", "")).startswith(("instruction.md", "paper/"))
        for item in method_items
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "Scientific method evidence must be a local instruction/paper quote.",
        )


def proposed_text(operation: dict[str, Any]) -> str:
    if operation["type"] == "write_file":
        value = operation.get("content")
    elif operation["type"] in {"replace_text", "text_replace"}:
        value = operation.get("new")
    elif operation["type"] == "json_set":
        value = json.dumps(operation.get("value"), ensure_ascii=False)
    else:
        return ""
    return value if isinstance(value, str) else ""


def solution_fragments(root: Path) -> set[str]:
    solution = root / "solution"
    if not solution.is_dir():
        return set()
    fragments: set[str] = set()
    for path in solution.rglob("*"):
        if not path.is_file() or path.is_symlink() or path.stat().st_size > 2_000_000:
            continue
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            stripped = line.strip()
            if len(stripped) >= 12:
                fragments.add(stripped)
    return fragments


def validate_policy(
    root: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    if plan.get("core_science_change") is not False:
        raise PolicyStop(
            "POLICY_VIOLATION",
            "Plan must declare core_science_change=false; Repair may not "
            "redefine the Harbor package's core science.",
        )
    evidence = evidence_index(root, report, plan)
    hidden_fragments = solution_fragments(root)
    target_roles: set[str] = set()
    for operation in plan["operations"]:
        _, relative = repair_target(root, operation["file"])
        target_roles.add(
            "solution"
            if relative.parts and relative.parts[0] == "solution"
            else "instruction"
            if relative.as_posix() == "instruction.md"
            else "tests"
            if relative.parts and relative.parts[0] == "tests"
            else "other"
        )
        if relative.parts[0] != "solution":
            continue
        hidden_fragments.update(
            line.strip()
            for line in proposed_text(operation).splitlines()
            if len(line.strip()) >= 12
        )
    if plan["repair_class"] == "AUTO_FIX" and target_roles & {
        "instruction",
        "tests",
    }:
        raise PolicyStop(
            "POLICY_VIOLATION",
            "AUTO_FIX may not change the frozen core scientific contract.",
        )
    if "solution" in target_roles and target_roles & {"instruction", "tests"}:
        raise PolicyStop(
            "POLICY_VIOLATION",
            "A repair may not rewrite checker/instruction and solution "
            "protocols together.",
        )
    for operation in plan["operations"]:
        linked = linked_evidence(operation, evidence)
        _, relative = repair_target(root, operation["file"])
        validate_precision_matrix(operation, linked, plan["repair_class"])
        if relative.parts and relative.parts[0] != "solution" and any(
            item.get("source_kind") == "solution" for item in linked
        ):
            raise PolicyStop(
                "POLICY_VIOLATION",
                "Oracle/solution content cannot support public or checker "
                "contract changes.",
            )
        if relative.as_posix() == "instruction.md":
            if any(
                Path(str(item["source"])).parts[:1] == ("solution",)
                for item in linked
            ):
                raise PolicyStop(
                    "POLICY_VIOLATION",
                    "Solution content cannot be evidence for public instruction.",
                )
            addition = proposed_text(operation)
            if any(fragment in addition for fragment in hidden_fragments):
                raise PolicyStop(
                    "POLICY_VIOLATION",
                    "Repair would leak hidden solution content into instruction.md.",
                )
    return evidence


def json_path_value(value: Any, tokens: Any) -> tuple[bool, Any]:
    if not isinstance(tokens, list) or not tokens:
        raise ValueError("JSON path must be a non-empty token list")
    current = value
    for token in tokens:
        if isinstance(token, int) and isinstance(current, list):
            if token < 0 or token >= len(current):
                return False, None
            current = current[token]
        elif isinstance(token, str) and isinstance(current, dict):
            if token not in current:
                return False, None
            current = current[token]
        else:
            return False, None
    return True, current


def set_json_path(value: Any, tokens: Any, replacement: Any) -> Any:
    if not isinstance(tokens, list) or not tokens:
        raise ValueError("JSON operation path must be a non-empty token list")
    current = value
    for token in tokens[:-1]:
        if isinstance(token, int) and isinstance(current, list):
            if token < 0 or token >= len(current):
                raise ValueError("JSON operation path index is out of range")
            current = current[token]
        elif isinstance(token, str) and isinstance(current, dict):
            if token not in current:
                raise ValueError("JSON operation parent path is missing")
            current = current[token]
        else:
            raise ValueError("JSON operation path does not match the document")
    final = tokens[-1]
    if isinstance(final, int) and isinstance(current, list):
        if final < 0 or final >= len(current):
            raise ValueError("JSON operation final index is out of range")
        current[final] = replacement
    elif isinstance(final, str) and isinstance(current, dict):
        current[final] = replacement
    else:
        raise ValueError("JSON operation final token is invalid")
    return value


def file_state(path: Path) -> str | None:
    return sha256_file(path) if path.is_file() else None


def apply_operation(candidate: Path, operation: dict[str, Any]) -> dict[str, Any]:
    path, relative = repair_target(candidate, operation["file"])
    before_hash = file_state(path)
    operation_type = operation["type"]
    if operation_type == "write_file":
        content = operation.get("content")
        if not isinstance(content, str):
            raise ValueError("write_file content must be a string")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        if operation.get("executable") is True:
            path.chmod(path.stat().st_mode | 0o111)
    elif operation_type in {"replace_text", "text_replace"}:
        if not path.is_file():
            raise FileNotFoundError(path)
        old = operation.get("old")
        new = operation.get("new")
        if not isinstance(old, str) or not old or not isinstance(new, str):
            raise ValueError("replace_text requires non-empty old and string new")
        content = path.read_text(encoding="utf-8")
        count = operation.get("count", 1)
        if not isinstance(count, int) or count <= 0:
            raise ValueError("replace_text count must be a positive integer")
        if content.count(old) != count:
            raise ValueError(
                "replace_text old content does not occur the declared number of times"
            )
        path.write_text(content.replace(old, new, count), encoding="utf-8")
    elif operation_type == "json_set":
        if not path.is_file():
            raise FileNotFoundError(path)
        document = read_json(path)
        tokens = operation.get("path")
        present, before_value = json_path_value(document, tokens)
        replacement = operation.get("value")
        if (
            any(
                isinstance(token, str) and "threshold" in token.lower()
                for token in tokens
            )
            and present
            and isinstance(before_value, (int, float))
            and isinstance(replacement, (int, float))
            and replacement < before_value
            and not operation.get("evidence_ids")
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "Lowering a scoring threshold requires linked evidence.",
            )
        write_json(path, set_json_path(document, tokens, replacement))
    elif operation_type == "delete_file":
        if not path.is_file():
            raise FileNotFoundError(path)
        path.unlink()
    else:  # guarded by plan validation
        raise ValueError(f"unsupported repair operation: {operation_type}")
    after_hash = file_state(path)
    if before_hash == after_hash:
        raise ValueError(f"operation {operation['id']} made no change")
    return {
        "operation_id": operation["id"],
        "operation": operation_type,
        "file": relative.as_posix(),
        "before_hash": before_hash,
        "after_hash": after_hash,
        "evidence_ids": operation["evidence_ids"],
    }


def regression_result(
    root: Path, specification: dict[str, Any]
) -> tuple[bool, dict[str, Any]]:
    kind = specification["type"]
    detail: dict[str, Any] = {}
    try:
        if kind == "command":
            command = specification.get("command")
            if (
                not isinstance(command, list)
                or not command
                or not all(isinstance(item, str) and item for item in command)
            ):
                raise ValueError("command regression requires a string argv list")
            timeout = specification.get("timeout_seconds", 30)
            if not isinstance(timeout, (int, float)) or not 0 < timeout <= 60:
                raise ValueError("command regression timeout must be in (0, 60]")
            process = subprocess.run(
                command,
                cwd=root,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
            )
            expected = specification.get("expected_returncode", 0)
            passed = process.returncode == expected
            if "stdout_contains" in specification:
                passed = passed and specification["stdout_contains"] in process.stdout
            if "stderr_contains" in specification:
                passed = passed and specification["stderr_contains"] in process.stderr
            detail = {
                "returncode": process.returncode,
                "stdout": process.stdout[-2000:],
                "stderr": process.stderr[-2000:],
            }
            return passed, detail
        path, _ = package_path(root, specification.get("file"), context="regression file")
        if kind == "file_exists":
            return path.is_file(), detail
        if kind == "file_absent":
            return not path.exists(), detail
        if kind == "file_executable":
            return path.is_file() and os.access(path, os.X_OK), detail
        if kind == "text_contains":
            return (
                path.is_file()
                and str(specification.get("expected", ""))
                in path.read_text(encoding="utf-8", errors="replace")
            ), detail
        if kind == "text_not_contains":
            return (
                path.is_file()
                and str(specification.get("expected", ""))
                not in path.read_text(encoding="utf-8", errors="replace")
            ), detail
        if kind == "json_path_equals":
            if not path.is_file():
                return False, detail
            present, value = json_path_value(read_json(path), specification.get("path"))
            return present and value == specification.get("expected"), detail
    except (OSError, subprocess.SubprocessError, ValueError, json.JSONDecodeError) as exc:
        return False, {"error": str(exc)}
    raise ValueError(f"unsupported regression test type: {kind}")


def run_regressions(
    root: Path,
    specifications: list[dict[str, Any]],
    phase: str,
    prior: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    results = prior or [{"specification": item} for item in specifications]
    for item in results:
        passed, detail = regression_result(root, item["specification"])
        item[f"{phase}_passed"] = passed
        item[f"{phase}_detail"] = detail
        expected = item["specification"].get(
            f"expected_{phase}", phase == "after"
        )
        if passed is not expected:
            raise ValueError(
                f"regression test {phase} result was {passed}, expected {expected}"
            )
    return results


def iter_package_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root)
        if relative.parts and relative.parts[0] in GENERATED_TOP_LEVEL:
            continue
        yield path


def package_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): sha256_file(path)
        for path in iter_package_files(root)
    }


def assert_mutation_boundary(
    snapshot: Path,
    candidate: Path,
    operation_files: set[str],
) -> None:
    before = package_hashes(snapshot)
    after = package_hashes(candidate)
    changed = {
        relative
        for relative in set(before) | set(after)
        if before.get(relative) != after.get(relative)
    }
    if not changed.issubset(operation_files):
        raise ValueError(f"repair escaped the modifiable target boundary: {sorted(changed)}")
    if any(not is_modifiable(Path(relative)) for relative in changed):
        raise ValueError("repair modified a read-only package role")


def report_configuration(report: dict[str, Any]) -> tuple[str, str]:
    configuration = report.get("configuration")
    if not isinstance(configuration, dict):
        raise ValueError("Review report requires configuration")
    paper_mode = configuration.get("paper_mode")
    execution_level = configuration.get("execution_level")
    if paper_mode not in {"no_paper", "paper_grounded"}:
        raise ValueError("Review report has an unsupported paper_mode")
    if not isinstance(execution_level, str) or not execution_level:
        raise ValueError("Review report requires execution_level")
    return paper_mode, execution_level


def run_equal_depth_review(
    candidate: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, Any]:
    runner = (
        Path(__file__).resolve().parents[2]
        / "materials-benchmark-review/scripts/run_review.py"
    )
    if not runner.is_file():
        raise FileNotFoundError(f"Review runner is missing: {runner}")
    paper_mode, execution_level = report_configuration(report)
    if execution_level != REQUIRED_AUDIT_EXECUTION_LEVEL:
        raise ValueError("Repair equal-depth re-audit is fixed at E1")
    source_audit = plan.get("source_audit")
    if not isinstance(source_audit, dict):
        raise ValueError("re-audit lacks source-audit binding")
    external_binding_hashes(candidate, plan, source_audit)
    command = [
        sys.executable,
        str(runner),
        str(candidate),
        "--paper-mode",
        paper_mode,
        "--execution-level",
        execution_level,
    ]
    for key, flag in {
        "known_valid_output": "--known-valid-output",
        "agent_assessment": "--agent-assessment",
        "e2_smoke_plan": "--e2-smoke-plan",
    }.items():
        raw = plan.get(key)
        if raw is None:
            continue
        external = Path(str(raw)).expanduser().resolve()
        if external.is_relative_to(candidate.resolve()):
            raise ValueError(f"{key} must remain external to the candidate")
        if not external.exists():
            raise FileNotFoundError(f"{key} is missing: {external}")
        command.extend([flag, str(external)])
    process = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    if process.returncode != 0:
        raise ValueError("equal-depth re-audit failed: " + process.stderr[-2000:])
    reaudit = read_json(candidate / "benchmark_audit/audit_report.json")
    if report_configuration(reaudit) != (paper_mode, execution_level):
        raise ValueError("re-audit evidence depth differs from the source audit")
    return reaudit


def finding_key(finding: dict[str, Any]) -> str | None:
    for key in ("code", "title", "finding_code"):
        value = finding.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def validate_reaudit(
    candidate: Path,
    reaudit: dict[str, Any],
    source_finding: dict[str, Any],
    source_report: dict[str, Any],
) -> dict[str, Any]:
    summary = reaudit.get("summary", {})
    disposition_path = candidate / "benchmark_audit/disposition.json"
    disposition = read_json(disposition_path) if disposition_path.is_file() else {}
    verdict = summary.get("final_verdict") or disposition.get("verdict")
    route = summary.get("disposition") or disposition.get("route")
    if verdict != "PASS" or route != "PUBLISH_CANDIDATE":
        raise ValueError("equal-depth re-audit did not route PASS to PUBLISH_CANDIDATE")
    source_key = finding_key(source_finding)
    if source_key and any(
        finding_key(item) == source_key
        for item in reaudit.get("findings", [])
        if isinstance(item, dict)
    ):
        raise ValueError("target finding remains open after re-audit")
    configuration = reaudit.get("configuration", {})
    manifest_path = candidate / "benchmark_audit/audit_manifest.json"
    manifest = read_json(manifest_path) if manifest_path.is_file() else {}
    if configuration.get("execution_level") != REQUIRED_AUDIT_EXECUTION_LEVEL:
        raise ValueError("re-audit execution level is not E1")
    manifest_hashes = manifest.get("input_hashes")
    current_hashes = (
        {
            relative: sha256_file(candidate / relative)
            for relative in manifest_hashes
            if (candidate / relative).is_file()
        }
        if isinstance(manifest_hashes, dict)
        else {}
    )
    if manifest_hashes != current_hashes:
        raise ValueError("re-audit package hashes are not bound to the candidate")
    return {
        "source_finding": {
            "finding_id": source_finding.get("finding_id"),
            "status": source_finding.get("status", "OPEN"),
        },
        "target_resolved": True,
        "source_configuration": {
            "paper_mode": source_report.get("configuration", {}).get("paper_mode"),
            "execution_level": source_report.get("configuration", {}).get(
                "execution_level"
            ),
        },
        "reaudit_configuration": {
            "paper_mode": configuration.get("paper_mode"),
            "execution_level": configuration.get("execution_level"),
        },
        "reaudit_audit_id": reaudit.get("audit_id"),
        "reaudit_finding_ids": [
            item.get("finding_id")
            for item in reaudit.get("findings", [])
            if isinstance(item, dict)
        ],
    }


def replace_paths(value: Any, old: str, new: str) -> Any:
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [replace_paths(item, old, new) for item in value]
    if isinstance(value, dict):
        return {key: replace_paths(item, old, new) for key, item in value.items()}
    return value


def rebase_audit_paths(candidate: Path, final_root: Path) -> None:
    audit = candidate / "benchmark_audit"
    old = str(candidate)
    new = str(final_root)
    for path in audit.rglob("*"):
        if not path.is_file() or path.name == "audit_manifest.json":
            continue
        if path.suffix == ".json":
            write_json(path, replace_paths(read_json(path), old, new))
        elif path.suffix == ".jsonl":
            lines = [
                json.dumps(
                    replace_paths(json.loads(line), old, new), ensure_ascii=False
                )
                for line in path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            path.write_text("".join(line + "\n" for line in lines), encoding="utf-8")
        elif path.suffix in {".md", ".log"}:
            path.write_text(
                path.read_text(encoding="utf-8").replace(old, new),
                encoding="utf-8",
            )
    manifest_path = audit / "audit_manifest.json"
    if manifest_path.is_file():
        manifest = replace_paths(read_json(manifest_path), old, new)
        manifest["benchmark_root"] = new
        manifest["output_hashes"] = dict(
            sorted(
                (
                    path.relative_to(audit).as_posix(),
                    sha256_file(path),
                )
                for path in audit.rglob("*")
                if path.is_file()
                and path.name not in {"audit_manifest.json", "audit_context.json"}
            )
        )
        write_json(manifest_path, manifest)


def root_cause_id(report: dict[str, Any], plan: dict[str, Any]) -> str:
    value = f"{report['audit_id']}:{plan['finding_id']}"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:20]


def history_root_for(root: Path) -> Path:
    return root.parent / ".benchmark_repair_history"


def prior_failed_attempts(root: Path, root_cause: str) -> list[dict[str, Any]]:
    history_root = history_root_for(root)
    if not history_root.is_dir():
        return []
    attempts: list[dict[str, Any]] = []
    for path in history_root.glob("*/attempt_manifest.json"):
        try:
            value = read_json(path)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        if (
            isinstance(value, dict)
            and value.get("root_cause") == root_cause
            and value.get("status") in {"ROLLED_BACK", "ABANDONED"}
            and isinstance(value.get("attempt_number"), int)
            and value["attempt_number"] > 0
        ):
            attempts.append(value)
    return sorted(attempts, key=lambda item: item["attempt_number"])


def record_control_stop(
    root: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
    root_cause: str,
    stop: PolicyStop,
) -> dict[str, Any]:
    repair_id = unique_id("repair-stop")
    history_root = history_root_for(root)
    destination = history_root / repair_id
    destination.mkdir(parents=True)
    write_json(destination / "repair_plan.json", plan)
    write_json(destination / "changes.json", [])
    write_json(
        destination / "unresolved.json",
        [{"finding_id": plan.get("finding_id"), "reason": stop.reason}],
    )
    write_json(destination / "regression_results.json", [])
    write_json(destination / "re_audit_comparison.json", {})
    write_json(destination / "patch.json", {"files": []})
    write_json(destination / "evidence.json", plan.get("evidence", []))
    (destination / "repair.log").write_text(
        f"{timestamp()}\tINFO\tdecision=ABANDON\tstatus={stop.status}\n",
        encoding="utf-8",
    )
    manifest = {
        "schema_version": "0.1",
        "repair_id": repair_id,
        "root_cause": root_cause,
        "attempt_number": 0,
        "status": stop.status,
        "decision": "ABANDON",
        "audit_id": report["audit_id"],
        "finding_id": plan["finding_id"],
        "repair_class": plan["repair_class"],
        "reason": stop.reason,
        "package_mutated": False,
        "recorded_at": timestamp(),
    }
    write_json(destination / "attempt_manifest.json", manifest)
    return {
        "status": stop.status,
        "decision": "ABANDON",
        "root_cause": root_cause,
        "history_root": str(history_root),
        "history_dir": str(destination),
        "attempt_manifest": str(destination / "attempt_manifest.json"),
        "reason": stop.reason,
    }


def package_identity(
    root: Path, *, directory_name: str | None = None
) -> dict[str, Any]:
    identity: dict[str, Any] = {
        "directory_name": directory_name if directory_name is not None else root.name
    }
    manifest = root / "manifest.json"
    if manifest.is_file():
        identity["manifest_hash"] = sha256_file(manifest)
    return identity


def write_repair_reports(
    candidate: Path,
    manifest: dict[str, Any],
    plan: dict[str, Any],
    history_dir: Path,
) -> None:
    report_dir = candidate / "benchmark_repair"
    write_json(report_dir / "repair_manifest.json", manifest)
    write_json(report_dir / "repair_report.json", manifest)
    write_json(report_dir / "repair_plan.json", plan)
    write_json(report_dir / "changes.json", manifest.get("changes", []))
    write_json(report_dir / "unresolved.json", manifest.get("unresolved", []))
    write_json(
        report_dir / "regression_results.json",
        manifest.get("regression_tests", []),
    )
    write_json(
        report_dir / "re_audit_comparison.json",
        manifest.get("re_audit_comparison", {}),
    )
    write_json(
        report_dir / "patch.json",
        {
            "schema_version": "0.1",
            "files": manifest.get("changes", []),
            "atomic_publish": manifest.get("atomic_publish", False),
        },
    )
    write_json(report_dir / "evidence.json", manifest.get("evidence", []))
    write_json(
        report_dir / "history.json",
        {
            "root_cause": manifest.get("root_cause"),
            "attempt_number": manifest.get("attempt_number"),
            "history_dir": str(history_dir),
            "snapshot_preserved": True,
        },
    )
    report_dir.joinpath("repair.log").write_text(
        "\n".join(
            [
                f"{timestamp()}\tINFO\trepair decision={manifest['decision']}",
                f"{timestamp()}\tINFO\tstatus={manifest['status']}",
                f"{timestamp()}\tINFO\toperations={len(manifest.get('changes', []))}",
                f"{timestamp()}\tINFO\tregressions={len(manifest.get('regression_tests', []))}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    report_dir.joinpath("repair_report.md").write_text(
        "\n".join(
            [
                "# Materials Benchmark Repair",
                "",
                f"- Repair ID: {manifest['repair_id']}",
                f"- Decision: {manifest['decision']}",
                f"- Status: {manifest['status']}",
                f"- Repair class: {manifest['repair_class']}",
                f"- Source audit: {manifest['source_audit_id']}",
                f"- Finding: {manifest['finding_id']}",
                f"- Attempts used: {manifest['attempt_number']} of 2",
                f"- Equal-depth verdict: {manifest['reaudit']['verdict']}",
                "",
            ]
        ),
        encoding="utf-8",
    )


def repair(root: Path, plan_path: Path) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.is_dir() or not (root / "instruction.md").is_file() or not (
        root / "tests"
    ).is_dir():
        raise ValueError("input must be a Harbor 题包 with instruction.md and tests/")
    plan = validate_external_plan(root, plan_path)
    try:
        report, audit_manifest, finding = validate_fresh_audit(root, plan)
    except PolicyStop as stop:
        report = read_json(root / "benchmark_audit/audit_report.json")
        root_cause = root_cause_id(report, plan)
        return record_control_stop(root, report, plan, root_cause, stop)
    root_cause = root_cause_id(report, plan)
    if plan.get("repair_class") == "ABANDON":
        return record_control_stop(
            root,
            report,
            plan,
            root_cause,
            PolicyStop("ABANDON", plan["justification"]),
        )
    prior = prior_failed_attempts(root, root_cause)
    if len(prior) >= 2 or any(item["status"] == "ABANDONED" for item in prior):
        return {
            "status": "ABANDONED",
            "decision": "ABANDON",
            "root_cause": root_cause,
            "history_root": str(history_root_for(root)),
            "attempts": len(prior),
            "reason": "Two failed attempts exhausted the root-cause limit.",
        }
    try:
        evidence = validate_policy(root, report, plan)
    except PolicyStop as stop:
        return record_control_stop(root, report, plan, root_cause, stop)

    attempt_number = len(prior) + 1
    repair_id = unique_id("repair")
    workspace = root.parent / ".benchmark_repair_tmp" / repair_id
    history = history_root_for(root) / repair_id
    if workspace.exists() or history.exists():
        raise FileExistsError("repair workspace already exists")
    workspace.parent.mkdir(exist_ok=True)
    workspace.mkdir()
    snapshot = workspace / "snapshot"
    candidate = workspace / "candidate"
    identity = package_identity(root)
    try:
        shutil.copytree(root, snapshot)
        shutil.copytree(snapshot, candidate)
        regression_tests = run_regressions(
            snapshot, plan["regression_tests"], "before"
        )
        changes = [
            apply_operation(candidate, operation) for operation in plan["operations"]
        ]
        operation_files = {item["file"] for item in changes}
        assert_mutation_boundary(snapshot, candidate, operation_files)
        candidate_digest = core_contract_digest(candidate)
        if plan["repair_class"] == "AUTO_FIX" and candidate_digest != plan[
            "core_contract_digest"
        ]:
            raise PolicyStop(
                "POLICY_VIOLATION",
                "AUTO_FIX changed the frozen core-contract digest.",
            )
        run_regressions(
            candidate, plan["regression_tests"], "after", regression_tests
        )
        reaudit = run_equal_depth_review(candidate, report, plan)
        re_audit_comparison = validate_reaudit(
            candidate, reaudit, finding, report
        )
        assert_mutation_boundary(snapshot, candidate, operation_files)
        if package_identity(candidate, directory_name=root.name) != identity:
            raise ValueError("repair changed the Harbor package identity")
        paper_mode, execution_level = report_configuration(reaudit)
        repair_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "status": "PUBLISHED",
            "decision": plan["repair_class"],
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "finding_id": plan["finding_id"],
            "finding_code": finding_key(finding),
            "repair_class": plan["repair_class"],
            "package_identity": identity,
            "source_audit_id": report["audit_id"],
            "source_audit_input_hashes": audit_manifest["input_hashes"],
            "source_audit_review_implementation": audit_manifest[
                "review_implementation"
            ],
            "source_audit_fixture_hashes": audit_manifest.get(
                "fixture_hashes", {}
            ),
            "source_audit_assessment_hashes": audit_manifest.get(
                "assessment_hashes", {}
            ),
            "core_contract_digest_before": plan["core_contract_digest"],
            "core_contract_digest_after": candidate_digest,
            "justification": plan["justification"],
            "evidence": list(evidence.values()),
            "changes": changes,
            "regression_tests": regression_tests,
            "unresolved": [],
            "re_audit_comparison": re_audit_comparison,
            "reaudit": {
                "audit_id": reaudit["audit_id"],
                "paper_mode": paper_mode,
                "execution_level": execution_level,
                "verdict": reaudit["summary"]["final_verdict"],
                "disposition": reaudit["summary"].get("disposition"),
            },
            "atomic_publish": True,
            "published_at": timestamp(),
        }
        write_repair_reports(candidate, repair_manifest, plan, history)
        rebase_audit_paths(candidate, root)

        history.mkdir(parents=True)
        snapshot.rename(history / "snapshot")
        write_json(history / "repair_plan.json", plan)
        attempt_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "status": "PUBLISHED",
            "decision": plan["repair_class"],
            "audit_id": report["audit_id"],
            "finding_id": plan["finding_id"],
            "repair_class": plan["repair_class"],
            "error": None,
            "snapshot_preserved": True,
            "candidate_preserved": False,
            "recorded_at": timestamp(),
        }
        write_json(history / "attempt_manifest.json", attempt_manifest)
        original = history / "original"
        root.rename(original)
        try:
            candidate.rename(root)
        except Exception:
            original.rename(root)
            raise
        shutil.rmtree(workspace, ignore_errors=True)
        return {
            "repair_id": repair_id,
            "status": "PUBLISHED",
            "decision": plan["repair_class"],
            "benchmark_root": str(root),
            "history_dir": str(history),
            "history_root": str(history_root_for(root)),
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "audit_id": reaudit["audit_id"],
        }
    except Exception as exc:  # noqa: BLE001
        status = "ROLLED_BACK" if attempt_number == 1 else "ABANDONED"
        decision = plan["repair_class"] if status == "ROLLED_BACK" else "ABANDON"
        history.mkdir(parents=True, exist_ok=True)
        if snapshot.exists():
            snapshot.rename(history / "snapshot")
        if candidate.exists():
            candidate.rename(history / "candidate")
        write_json(history / "repair_plan.json", plan)
        write_json(
            history / "changes.json",
            changes if "changes" in locals() else [],
        )
        write_json(
            history / "unresolved.json",
            [{"finding_id": plan["finding_id"], "reason": str(exc)}],
        )
        write_json(
            history / "regression_results.json",
            regression_tests if "regression_tests" in locals() else [],
        )
        write_json(
            history / "re_audit_comparison.json",
            re_audit_comparison if "re_audit_comparison" in locals() else {},
        )
        write_json(
            history / "patch.json",
            {
                "files": changes if "changes" in locals() else [],
                "atomic_publish": False,
            },
        )
        write_json(history / "evidence.json", evidence if "evidence" in locals() else [])
        (history / "repair.log").write_text(
            f"{timestamp()}\tINFO\tdecision={decision}\tstatus={status}\n",
            encoding="utf-8",
        )
        attempt_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "status": status,
            "decision": decision,
            "audit_id": report["audit_id"],
            "finding_id": plan["finding_id"],
            "repair_class": plan["repair_class"],
            "error": str(exc),
            "snapshot_preserved": (history / "snapshot").is_dir(),
            "candidate_preserved": (history / "candidate").is_dir(),
            "package_mutated": False,
            "recorded_at": timestamp(),
        }
        write_json(history / "attempt_manifest.json", attempt_manifest)
        if workspace.exists():
            shutil.rmtree(workspace, ignore_errors=True)
        return {
            "repair_id": repair_id,
            "status": status,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "history_dir": str(history),
            "history_root": str(history_root_for(root)),
            "attempt_manifest": str(history / "attempt_manifest.json"),
            "reason": str(exc),
        }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Repair one audited materials-science Harbor 题包."
    )
    parser.add_argument("benchmark_root")
    parser.add_argument("--plan", required=True)
    arguments = parser.parse_args()
    try:
        result = repair(Path(arguments.benchmark_root), Path(arguments.plan))
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["status"] == "PUBLISHED" else 3
    except Exception as exc:  # noqa: BLE001
        print(f"materials repair failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
