#!/usr/bin/env python3
"""Repair one audited Harbor package through an isolated atomic workflow."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
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

_REVIEW_SCRIPTS = (
    Path(__file__).resolve().parents[2]
    / "materials-benchmark-review"
    / "scripts"
)
if str(_REVIEW_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_REVIEW_SCRIPTS))

from canonical_status import (  # noqa: E402
    REPAIR_BUNDLE_FILES,
    REPAIR_STATUSES,
    SUCCESS_REPAIR_STATUSES,
    canonical_fields,
    validate_repair_bundle_semantics,
)
from d1_d2_contract import (  # noqa: E402
    is_structural_auto_fix_operation,
    output_repair_proof,
    structural_auto_fix_operation_error,
)
from deterministic_contract import (  # noqa: E402
    CHECK_IDS,
    DETERMINISTIC_REPAIR_PLAN_SCHEMA_ALIASES,
    DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION,
    finding_lane,
    is_deterministic_repair_plan,
    validate_deterministic_contract,
    validate_deterministic_plan_binding,
)
from artifact_schema import (  # noqa: E402
    AUDIT_ATTESTATION_SCHEMA_VERSION,
    AUDIT_MANIFEST_SCHEMA_VERSION,
    AUDIT_REPORT_SCHEMA_VERSION,
    DISPOSITION_SCHEMA_VERSION,
    DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
    DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
    AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
    SCORING_SCHEMA_VERSION,
    IMPLEMENTATION_HASH_SCHEMA_VERSION,
    IMPLEMENTATION_MANIFEST_SCHEMA_VERSION,
    require_schema,
)
from d5_package_completeness import validate_auto_fix_operation  # noqa: E402
from d3_d4_checker import auto_fix_operation_error  # noqa: E402
from d6_core_output_scoring import (  # noqa: E402
    unique_wiring_auto_fix_operation_error,
)
import sandbox_runtime  # noqa: E402
from review_path_policy import (  # noqa: E402
    REVIEW_LANE,
    canonical_management_path,
    require_management_path,
)

DECISIONS = {"AUTO_FIX", "ASSISTED_FIX", "ABANDON"}
# The batch five-state lifecycle mapped onto the unified terminal fields
# (disposition, publishable, repair_state).  ``ROLLED_BACK`` keeps the source
# verdict because the authoritative package is restored unchanged.
TERMINAL_STATE_FIELDS = {
    "REPAIRED": ("PASS", True),
    "PARTIALLY_REPAIRED": ("CONDITIONAL", False),
    "ABANDONED": ("REJECT", False),
    "ROLLED_BACK": (None, False),
    "INFRASTRUCTURE_BLOCKED": (None, False),
}
MAX_CONTROL_FAILURES_PER_FINGERPRINT = 2
MAX_CONTROL_FAILURES_PER_SCOPE = 3


def terminal_fields(
    repair_state: str, *, source_verdict: str | None = None
) -> dict[str, Any]:
    disposition, publishable = TERMINAL_STATE_FIELDS.get(
        repair_state, (None, False)
    )
    if disposition is None:
        disposition = source_verdict or "CONDITIONAL"
    return {
        "disposition": disposition,
        "publishable": publishable,
        "repair_state": repair_state,
    }
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
    "review_outputs",
    "review_records",
    "repair_history",
}
EVIDENCE_SOURCE_PREFIX = "benchmark_audit:"
REMOVED_FIXTURE_FIELDS = frozenset(
    {"known_valid_output", "fixture_hashes", "repair_reaudit_lineage"}
)
METADATA_ROOTS = {
    "manifest.json",
    "resources.json",
    "steps.json",
    "task.toml",
    "environment",
}
CORE_CONTRACT_SCHEMA = "materials-core-contract/1.0"
CURRENT_SCORING_VERSION = SCORING_SCHEMA_VERSION
MINIMUM_REPAIR_SCORE = 60.0
PUBLICATION_SCORE = 80.0
HARD_GATE_CODES = (
    "NON_MATERIALS_TASK",
    "SCIENTIFIC_TARGET_INVALID",
    "CHECKER_CORE_TASK_UNASSESSED",
    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
)
REVIEW_IMPLEMENTATION_FILES_MANIFEST = (
    "references/review-implementation-files.json"
)
PRECISION_RULES = {
    "json_key": ("key", "type", "required", "unit", "value"),
    "csv_column": (
        "column",
        "type",
        "required",
        "unit",
        "value",
        "replacement",
    ),
    "npy_array": (
        "shape",
        "dtype",
        "axis_semantics",
        "unit",
        "required",
        "value",
        "replacement",
    ),
    "gold": (
        "field",
        "value",
        "type",
        "unit",
        "required",
        "source_or_derivation",
    ),
    "tolerance": (
        "field",
        "value",
        "type",
        "unit",
        "required",
        "error_basis",
        "direction",
        "mode",
    ),
    "scoring_contract": (
        "field",
        "value",
        "type",
        "unit",
        "required",
        "scoring_contract",
        "mathematical_proof",
    ),
    "scientific_method": ("claim", "replacement"),
    "exception_guard": (
        "stack_trace",
        "existing_reading_code",
        "replacement",
    ),
    "harbor_path": ("official_contract", "existing_path_code", "replacement"),
}
ASSISTED_SOURCE_KINDS = frozenset(
    {
        "PACKAGE_PAPER",
        "PACKAGE_DIRECT_SOURCE",
        "AUTHORITATIVE_PRIMARY_WEB",
    }
)
WEB_SOURCE_KIND = "AUTHORITATIVE_PRIMARY_WEB"
WEB_AUTHORITIES = frozenset(
    {
        "OFFICIAL_STANDARD",
        "OFFICIAL_SOFTWARE_DOCUMENTATION",
        "PEER_REVIEWED_PRIMARY",
        "AUTHORITATIVE_PRIMARY",
    }
)
DIRECT_SOURCE_ROOTS = frozenset(
    {"data", "direct_sources", "inputs", "reference", "references", "resources", "sources"}
)
DIRECT_SOURCE_FILES = frozenset({"instruction.md", "resources.json"})


class PolicyStop(Exception):
    """A non-mutating policy stop reported through the CLI result."""

    def __init__(self, status: str, reason: str) -> None:
        super().__init__(reason)
        self.status = status
        self.reason = reason


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def reject_removed_fixture_fields(value: Any, *, context: str) -> None:
    """Reject pre-split fixture lineage instead of silently ignoring it."""

    found: set[str] = set()

    def visit(node: Any) -> None:
        if isinstance(node, dict):
            for key, child in node.items():
                if key in REMOVED_FIXTURE_FIELDS:
                    found.add(key)
                visit(child)
        elif isinstance(node, list):
            for child in node:
                visit(child)

    visit(value)
    if found:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"{context} contains removed fixture fields: "
            + ", ".join(sorted(found)),
        )


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def default_source_audit_dir(root: Path) -> Path:
    return canonical_management_path(root, "source_audit")


def source_audit_dir(root: Path, plan: dict[str, Any]) -> Path:
    raw = plan.get("source_audit_dir")
    path = Path(str(raw)).expanduser().resolve() if raw is not None else default_source_audit_dir(root)
    return require_management_path(root, path, purpose="source_audit", label="source audit directory")


def default_repair_output_dir(root: Path) -> Path:
    return canonical_management_path(root, "repair")


def repair_output_root(root: Path, plan: dict[str, Any]) -> Path:
    raw = plan.get("repair_output_dir")
    path = Path(str(raw)).expanduser().resolve() if raw is not None else default_repair_output_dir(root)
    return require_management_path(root, path, purpose="repair", label="repair output directory")


def reaudit_output_root(root: Path) -> Path:
    return canonical_management_path(root, "reaudit")


def reaudit_audit_dir(root: Path, plan: dict[str, Any]) -> Path:
    del plan
    return reaudit_output_root(root) / "benchmark_audit"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def canonical_json_hash(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


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


def review_skill_root() -> Path:
    return (
        Path(__file__).resolve().parents[2] / "materials-benchmark-review"
    )


def collect_review_implementation_hashes() -> dict[str, Any]:
    root = review_skill_root()
    manifest_path = root / REVIEW_IMPLEMENTATION_FILES_MANIFEST
    manifest = read_json(manifest_path)
    files_list = manifest.get("files") if isinstance(manifest, dict) else None
    if (
        not isinstance(manifest, dict)
        or manifest.get("schema_version")
        != IMPLEMENTATION_MANIFEST_SCHEMA_VERSION
        or not isinstance(files_list, list)
        or files_list != sorted(set(files_list))
        or REVIEW_IMPLEMENTATION_FILES_MANIFEST not in files_list
        or not all(isinstance(item, str) and item for item in files_list)
    ):
        raise ValueError("Review implementation file manifest is invalid")
    files: dict[str, str] = {}
    for relative in files_list:
        relative_path = Path(relative)
        path = root / relative_path
        if (
            relative_path.is_absolute()
            or ".." in relative_path.parts
            or not path.is_file()
            or path.is_symlink()
        ):
            raise ValueError(f"current Review implementation is missing: {relative}")
        files[relative] = sha256_file(path)
    payload = json.dumps(
        files, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return {
        "schema_version": IMPLEMENTATION_HASH_SCHEMA_VERSION,
        "root": ".cursor/skills/materials-benchmark-review",
        "files": files,
        "aggregate_hash": "sha256:" + hashlib.sha256(payload).hexdigest(),
    }


def contract_surface_hashes(root: Path) -> dict[str, str]:
    paths: list[Path] = []
    instruction = root / "instruction.md"
    if instruction.is_file():
        paths.append(instruction)
    for role in ("tests", "solution"):
        directory = root / role
        if directory.is_symlink():
            raise ValueError(f"core contract role may not be a symlink: {role}")
        if directory.is_dir():
            for path in sorted(directory.rglob("*")):
                if path.is_symlink():
                    raise ValueError(
                        f"core contract surface may not be a symlink: {path}"
                    )
                if path.is_file():
                    paths.append(path)
    return {
        path.relative_to(root).as_posix(): sha256_file(path)
        for path in sorted(paths)
    }


def core_contract_snapshot(root: Path) -> dict[str, Any]:
    """Freeze every instruction/tests/solution path and byte hash."""
    return {
        "schema_version": CORE_CONTRACT_SCHEMA,
        "surface_hashes": contract_surface_hashes(root),
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


def regression_semantically_asserts(
    operation: dict[str, Any],
    specification: dict[str, Any],
) -> bool:
    operation_file = Path(str(operation.get("file", ""))).as_posix()
    regression_file = Path(str(specification.get("file", ""))).as_posix()
    if operation_file != regression_file:
        return False
    operation_type = operation.get("type")
    regression_type = specification.get("type")
    if operation_type == "write_file":
        return (
            regression_type == "text_contains"
            and specification.get("expected") == operation.get("content")
        )
    if operation_type in {"replace_text", "text_replace"}:
        replacement = operation.get("new")
        if replacement:
            return (
                regression_type == "text_contains"
                and specification.get("expected") == replacement
            )
        return (
            regression_type == "text_not_contains"
            and specification.get("expected") == operation.get("old")
        )
    if operation_type == "json_set":
        return (
            regression_type == "json_path_equals"
            and specification.get("path") == operation.get("path")
            and specification.get("expected") == operation.get("value")
        )
    if operation_type == "delete_file":
        return regression_type == "file_absent"
    return False


def validate_finding_spec(root: Path, spec: dict[str, Any]) -> None:
    """Validate one finding's operation/regression schema.

    ``spec`` is either a legacy single-finding plan or one entry of a batch
    plan's ``findings`` list; both carry ``repair_class``, ``operations``,
    ``regression_tests``, and ``finding_id``.
    """

    finding_id = spec["finding_id"]
    operations = spec.get("operations")
    regressions = spec.get("regression_tests")
    if not isinstance(operations, list):
        raise ValueError("repair plan operations must be a list")
    if not isinstance(regressions, list):
        raise ValueError("repair plan regression_tests must be a list")
    if spec.get("repair_class") != "ABANDON" and not operations:
        raise ValueError("repair plan requires at least one operation")
    if spec.get("repair_class") != "ABANDON" and not regressions:
        raise ValueError("repair plan requires regression tests")
    if spec.get("repair_class") == "ABANDON" and (operations or regressions):
        raise ValueError("ABANDON plans require operations=[] and regression_tests=[]")
    operation_ids: set[str] = set()
    operations_by_id: dict[str, dict[str, Any]] = {}
    for operation in operations:
        if not isinstance(operation, dict):
            raise ValueError("every repair operation must be an object")
        operation_id = operation.get("id")
        if not isinstance(operation_id, str) or not operation_id:
            raise ValueError("every repair operation requires a stable id")
        if operation_id in operation_ids:
            raise ValueError(f"duplicate repair operation id: {operation_id}")
        operation_ids.add(operation_id)
        operations_by_id[operation_id] = operation
        if operation.get("type") not in OPERATION_TYPES:
            raise ValueError(f"unsupported repair operation: {operation.get('type')}")
        repair_target(root, operation.get("file"))
    causally_covered: set[str] = set()
    semantically_covered: set[str] = set()
    for index, specification in enumerate(regressions, start=1):
        if not isinstance(specification, dict):
            raise ValueError("every regression test must be an object")
        if specification.get("type") not in REGRESSION_TYPES:
            raise ValueError(
                f"unsupported regression test type: {specification.get('type')}"
            )
        if spec.get("repair_class") == "ABANDON":
            raise ValueError("ABANDON plans may not carry regressions")
        if not isinstance(specification.get("id"), str) or not specification["id"]:
            raise ValueError(f"regression test {index} requires a stable id")
        if specification.get("finding_id") != finding_id:
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
        causally_covered.update(causal)
        if len(causal) == 1 and regression_semantically_asserts(
            operations_by_id[causal[0]], specification
        ):
            semantically_covered.add(causal[0])
        if specification["type"] == "command":
            observed_paths = {
                Path(item).as_posix()
                for item in specification.get("command", [])
                if isinstance(item, str)
            }
        else:
            observed_paths = {Path(str(specification.get("file", ""))).as_posix()}
        mismatched = [
            operation_id
            for operation_id in causal
            if Path(str(operations_by_id[operation_id].get("file", ""))).as_posix()
            not in observed_paths
        ]
        if mismatched:
            raise ValueError(
                f"regression test {index} does not observe causal operation "
                f"targets: {mismatched}"
            )
        if specification.get("expected_before", False) is not False:
            raise ValueError("regressions must fail before the repair")
        if specification.get("expected_after", True) is not True:
            raise ValueError("regressions must pass after the repair")
    if spec.get("repair_class") != "ABANDON" and causally_covered != operation_ids:
        uncovered = sorted(operation_ids - causally_covered)
        raise ValueError(
            f"every operation requires causal regression coverage: {uncovered}"
        )
    if (
        spec.get("repair_class") != "ABANDON"
        and semantically_covered != operation_ids
    ):
        uncovered = sorted(operation_ids - semantically_covered)
        raise ValueError(
            "every operation requires its own exact semantic regression "
            f"assertion: {uncovered}"
        )


def validate_batch_plan(root: Path, plan: dict[str, Any]) -> dict[str, Any]:
    """Validate a batch plan carrying ``audit_id`` + ``findings[]``."""

    findings = plan["findings"]
    if not findings:
        raise ValueError("batch repair plan requires at least one finding")
    deterministic_plan = is_deterministic_repair_plan(plan)
    if (
        plan.get("schema_version") in DETERMINISTIC_REPAIR_PLAN_SCHEMA_ALIASES
        and not isinstance(plan.get("deterministic_contract"), dict)
    ):
        raise ValueError(
            "deterministic repair plan requires a source contract binding"
        )
    seen: set[str] = set()
    for finding in findings:
        if not isinstance(finding, dict):
            raise ValueError("every batch finding must be an object")
        finding_id = finding.get("finding_id")
        if not isinstance(finding_id, str) or not finding_id:
            raise ValueError("every batch finding requires finding_id")
        if finding_id in seen:
            raise ValueError(f"duplicate finding_id in batch plan: {finding_id}")
        seen.add(finding_id)
        if finding.get("repair_class") not in DECISIONS:
            raise ValueError(
                "every batch finding requires a repair_class of "
                "AUTO_FIX, ASSISTED_FIX, or ABANDON"
            )
        if deterministic_plan and finding.get("deterministic_check") not in CHECK_IDS:
            raise ValueError("deterministic repair target check is unknown")
        if (
            not isinstance(finding.get("justification"), str)
            or not finding["justification"].strip()
        ):
            raise ValueError("every batch finding requires a justification")
        finding.setdefault("operations", [])
        finding.setdefault("regression_tests", [])
        finding.setdefault("evidence", [])
        validate_finding_spec(root, finding)
    return plan


def validate_external_plan(root: Path, plan_path: Path) -> dict[str, Any]:
    resolved = plan_path.expanduser().resolve()
    if resolved.is_relative_to(root.resolve()):
        raise ValueError("repair plan must remain outside the Harbor 题包")
    if not resolved.is_file():
        raise FileNotFoundError(f"repair plan is missing: {resolved}")
    plan = read_json(resolved)
    if not isinstance(plan, dict) or plan.get("schema_version") not in (
        {"0.1"} | set(DETERMINISTIC_REPAIR_PLAN_SCHEMA_ALIASES)
    ):
        raise ValueError(
            "repair plan must use schema_version 0.1 or the deterministic "
            "repair-plan schema"
        )
    if not isinstance(plan.get("audit_id"), str) or not plan["audit_id"]:
        raise ValueError("repair plan requires audit_id")
    if isinstance(plan.get("findings"), list):
        return validate_batch_plan(root, plan)
    if is_deterministic_repair_plan(plan):
        raise ValueError("deterministic repair plan must be a complete batch")
    if "repair_class" not in plan and plan.get("decision") in DECISIONS:
        plan["repair_class"] = plan["decision"]
    if plan.get("repair_class") not in DECISIONS:
        raise ValueError(
            "repair_class must be AUTO_FIX, ASSISTED_FIX, or ABANDON"
        )
    if not isinstance(plan.get("justification"), str) or not plan[
        "justification"
    ].strip():
        raise ValueError("repair plan requires a justification")
    if not isinstance(plan.get("finding_id"), str) or not plan["finding_id"]:
        raise ValueError("repair plan requires finding_id")
    validate_finding_spec(root, plan)
    return plan


def external_binding_hashes(
    root: Path, plan: dict[str, Any], authoritative_manifest: dict[str, Any]
) -> tuple[dict[str, str], dict[str, str]]:
    assessment_hashes: dict[str, str] = {}
    for key, target in (("agent_assessment", assessment_hashes),):
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
                f"authoritative audit {field} must be a hash mapping",
            )
        normalized: dict[str, str] = {}
        for name, raw_hash in value.items():
            if isinstance(raw_hash, dict):
                raw_hash = raw_hash.get("hash")
            if not isinstance(name, str) or not isinstance(raw_hash, str):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    f"authoritative audit {field} contains an invalid hash",
                )
            normalized[name] = raw_hash
        return normalized

    expected_assessments = normalize(
        authoritative_manifest.get("assessment_hashes"), "assessment_hashes"
    )
    if expected_assessments != assessment_hashes:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit assessment hashes do not bind the supplied "
            "assessment",
        )
    return {}, assessment_hashes


def authenticate_audit_bundle(
    root: Path,
    report: dict[str, Any],
    manifest: dict[str, Any],
    disposition: dict[str, Any],
    audit: Path | None = None,
) -> None:
    audit = audit or (root / "benchmark_audit")
    report = require_schema(
        report, AUDIT_REPORT_SCHEMA_VERSION, "authoritative audit report"
    )
    manifest = require_schema(
        manifest, AUDIT_MANIFEST_SCHEMA_VERSION, "authoritative audit manifest"
    )
    disposition = require_schema(
        disposition, DISPOSITION_SCHEMA_VERSION, "audit disposition"
    )
    audit_id = manifest.get("audit_id")
    if (
        not isinstance(audit_id, str)
        or report.get("audit_id") != audit_id
        or disposition.get("audit_id", audit_id) != audit_id
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit identities are inconsistent",
        )
    output_hashes = manifest.get("output_hashes")
    if not isinstance(output_hashes, dict) or not output_hashes:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit lacks authenticated output hashes",
        )
    required = {
        "audit_report.json",
        "disposition.json",
        "corpus_index_entry.json",
        "checker_tests.json",
        "resource_checks.json",
        "deterministic_core/report.json",
        "deterministic_core/probe_results.json",
        "agent_quality/assessment.json",
    }
    if not required.issubset(output_hashes):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit output hashes omit required reports",
        )
    for relative, expected in output_hashes.items():
        try:
            path, relative_path = package_path(
                audit, relative, context="audit output path"
            )
        except (TypeError, ValueError) as exc:
            raise PolicyStop("BLOCKED_EVIDENCE", str(exc)) from exc
        if relative_path.name in {"audit_manifest.json", "audit_context.json"}:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "audit output hashes may not self-authenticate manifest/context",
            )
        if (
            not isinstance(expected, str)
            or not path.is_file()
            or sha256_file(path) != expected
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"authoritative audit output is tampered or stale: {relative}",
            )
    for relative, expected_schema in {
        "deterministic_core/report.json": DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
        "deterministic_core/probe_results.json": (
            DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION
        ),
        "agent_quality/assessment.json": AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
    }.items():
        artifact = require_schema(
            read_json(audit / relative), expected_schema, relative
        )
        if relative == "deterministic_core/report.json" and report.get(
            "deterministic_core"
        ) != artifact:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "deterministic core artifact differs from audit report",
            )
        if relative == "deterministic_core/probe_results.json" and report.get(
            "deterministic_core", {}
        ).get("probe_results") != artifact:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "deterministic probe artifact differs from audit report",
            )
        if relative == "agent_quality/assessment.json" and report.get(
            "agent_quality"
        ) != artifact:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "agent quality artifact differs from audit report",
            )
    if report.get("summary", {}).get("scoring_version") != CURRENT_SCORING_VERSION:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit uses an unsupported scoring schema",
        )
    try:
        current_implementation = collect_review_implementation_hashes()
    except (OSError, ValueError) as exc:
        raise PolicyStop("BLOCKED_EVIDENCE", str(exc)) from exc
    if manifest.get("review_implementation") != current_implementation:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit was produced by a stale Review implementation",
        )


def validate_audit_attestation(
    root: Path,
    audit: Path,
    attestation_path: Path,
) -> dict[str, Any]:
    supplied = attestation_path.expanduser()
    if supplied.is_symlink():
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source-audit attestation may not be a symbolic link",
        )
    resolved = supplied.resolve()
    if resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source-audit attestation must be an external regular file",
        )
    if resolved.stat().st_mode & 0o222:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source-audit attestation must be immutable/read-only",
        )
    try:
        attestation = read_json(resolved)
        manifest = read_json(audit / "audit_manifest.json")
        report = read_json(audit / "audit_report.json")
        disposition = read_json(audit / "disposition.json")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"source-audit attestation is unreadable: {exc}",
        ) from exc
    if not isinstance(attestation, dict) or not isinstance(manifest, dict):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source-audit attestation and manifest must be objects",
        )
    reject_removed_fixture_fields(attestation, context="source-audit attestation")
    reject_removed_fixture_fields(manifest, context="source-audit manifest")
    reject_removed_fixture_fields(report, context="source-audit report")
    reject_removed_fixture_fields(
        disposition, context="source-audit disposition"
    )
    manifest = require_schema(
        manifest, AUDIT_MANIFEST_SCHEMA_VERSION, "source-audit manifest"
    )
    report = require_schema(
        report, AUDIT_REPORT_SCHEMA_VERSION, "source-audit report"
    )
    try:
        artifact_paths = {
            "audit_report.json": audit / "audit_report.json",
            "deterministic_core/report.json": audit
            / "deterministic_core/report.json",
            "deterministic_core/probe_results.json": audit
            / "deterministic_core/probe_results.json",
            "agent_quality/assessment.json": audit
            / "agent_quality/assessment.json",
        }
        artifact_hashes = {
            relative: sha256_file(path)
            for relative, path in artifact_paths.items()
            if path.is_file() and not path.is_symlink()
        }
        payload = {
            "audit_id": manifest.get("audit_id"),
            "manifest_hash": sha256_file(audit / "audit_manifest.json"),
            "report_hash": sha256_file(audit / "audit_report.json"),
            "disposition_hash": sha256_file(audit / "disposition.json"),
            "assessment_hashes": manifest.get("assessment_hashes", {}),
            "artifact_hashes": artifact_hashes,
            "output_hashes": manifest.get("output_hashes", {}),
            "artifact_schema_versions": {
                "audit_manifest": manifest.get("schema_version"),
                "audit_bundle": manifest.get("bundle_schema_version"),
                "audit_report": report.get("schema_version"),
                "deterministic_core": report.get(
                    "deterministic_core", {}
                ).get("schema_version"),
                "deterministic_probe_results": report.get(
                    "deterministic_core", {}
                ).get("probe_results", {}).get("schema_version"),
                "agent_quality": report.get("agent_quality", {}).get(
                    "schema_version"
                ),
                "scoring": report.get("summary", {}).get("scoring_version"),
            },
            "scoring_schema_version": CURRENT_SCORING_VERSION,
        }
    except OSError as exc:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"source-audit attestation target is incomplete: {exc}",
        ) from exc
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    expected = {
        "schema_version": AUDIT_ATTESTATION_SCHEMA_VERSION,
        **payload,
        "bundle_digest": "sha256:" + hashlib.sha256(encoded).hexdigest(),
    }
    if attestation != expected:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source-audit attestation does not bind the authoritative bytes",
        )
    return attestation


def validate_source_audit_binding(
    root: Path,
    report: dict[str, Any],
    manifest: dict[str, Any],
    finding: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, Any]:
    reject_removed_fixture_fields(plan, context="repair plan")
    source_audit = plan.get("source_audit")
    if not isinstance(source_audit, dict):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "Repair requires a complete source-audit binding.",
        )
    reject_removed_fixture_fields(source_audit, context="repair source-audit binding")
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
    configuration = report.get("configuration")
    if not isinstance(configuration, dict):
        raise PolicyStop(
            "BLOCKED_EVIDENCE", "authoritative audit lacks configuration"
        )
    if (
        source_audit.get("review_lane") != REVIEW_LANE
        or configuration.get("review_lane") != REVIEW_LANE
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "Repair source audit and re-audit must use review_lane='dual'",
        )
    digest = core_contract_digest(root)
    bound_digest = source_audit.get("core_contract_digest")
    if bound_digest is None and isinstance(source_audit.get("core_contract"), dict):
        bound_digest = source_audit["core_contract"].get("digest")
    if (
        plan.get("core_contract_digest") != digest
        or bound_digest != digest
        or manifest.get("core_contract_digest") != digest
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "frozen core-contract digest is stale or incomplete",
        )
    external_binding_hashes(root, plan, manifest)
    if plan.get("deterministic_contract") is not None:
        try:
            validate_deterministic_contract(report.get("deterministic_contract"))
            validate_deterministic_plan_binding(report, plan)
        except ValueError as exc:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"deterministic repair binding is invalid: {exc}",
            ) from exc
    return source_audit


def validate_fresh_audit(
    root: Path,
    plan: dict[str, Any],
    attestation_path: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    audit = source_audit_dir(root, plan)
    validate_audit_attestation(root, audit, attestation_path)
    report = require_schema(
        read_json(audit / "audit_report.json"),
        AUDIT_REPORT_SCHEMA_VERSION,
        "authoritative audit report",
    )
    manifest = require_schema(
        read_json(audit / "audit_manifest.json"),
        AUDIT_MANIFEST_SCHEMA_VERSION,
        "authoritative audit manifest",
    )
    disposition = require_schema(
        read_json(audit / "disposition.json"),
        DISPOSITION_SCHEMA_VERSION,
        "authoritative audit disposition",
    )
    authenticate_audit_bundle(
        root, report, manifest, disposition, audit=audit
    )
    report_configuration(report)
    if plan["audit_id"] != report.get("audit_id"):
        raise ValueError("stale audit: plan audit_id is not authoritative")
    if plan.get("repair_class") != "ABANDON":
        enforce_source_score_gate(report)
    route = disposition.get("route") or canonical_publish_route(report)
    if route != "REPAIR_QUEUE":
        raise ValueError("authoritative audit is not routed to REPAIR_QUEUE")
    findings = {
        item.get("finding_id"): item
        for item in report.get("findings", [])
        if isinstance(item, dict) and isinstance(item.get("finding_id"), str)
    }
    if plan["finding_id"] not in findings:
        raise ValueError("repair plan finding_id is not open in the audit")
    enforce_repair_lane_boundary(
        plan, findings[plan["finding_id"]], report
    )
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


def authoritative_total_score(
    report: dict[str, Any], *, context: str
) -> float:
    """Read the Review-owned C01-C07 total, failing closed on bad input."""

    summary = report.get("summary")
    raw = summary.get("total_score") if isinstance(summary, dict) else None
    if isinstance(raw, bool) or not isinstance(raw, (int, float)):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"{context} is missing the authoritative C01-C07 total score.",
        )
    score = float(raw)
    if not math.isfinite(score) or not 0 <= score <= 100:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"{context} has a non-finite or out-of-range total score.",
        )
    return score


def enforce_source_score_gate(report: dict[str, Any]) -> float:
    """A source audit below 60 is never eligible to enter Repair."""

    score = authoritative_total_score(report, context="source audit")
    if score < MINIMUM_REPAIR_SCORE:
        raise PolicyStop(
            "ABANDONED",
            f"source audit total score {score:g} is below "
            f"{MINIMUM_REPAIR_SCORE:g}; Repair is not eligible",
        )
    return score


def is_agent_quality_finding(
    finding: dict[str, Any], report: dict[str, Any]
) -> bool:
    quality_ids = (
        report.get("agent_quality", {}).get("finding_ids", [])
        if isinstance(report.get("agent_quality"), dict)
        else []
    )
    return (
        finding_lane(finding) in {"agent_quality", "quality_results"}
        or finding.get("judgment_type") == "AGENT_JUDGMENT"
        or finding.get("finding_id") in quality_ids
    )


def enforce_repair_lane_boundary(
    plan_finding: dict[str, Any],
    source_finding: dict[str, Any],
    report: dict[str, Any],
) -> None:
    """Keep Agent-quality findings out of deterministic AUTO_FIX."""

    quality_finding = is_agent_quality_finding(source_finding, report) or (
        plan_finding.get("lane") in {"agent_quality", "quality_results"}
        or plan_finding.get("judgment_type") == "AGENT_JUDGMENT"
    )
    if not quality_finding:
        return
    if plan_finding.get("repair_class") == "AUTO_FIX":
        raise PolicyStop(
            "POLICY_VIOLATION",
            "Agent quality findings may not become deterministic AUTO_FIX",
        )
    if plan_finding.get("deterministic_check") is not None:
        raise PolicyStop(
            "POLICY_VIOLATION",
            "Agent quality findings may not claim D1-D6 ownership",
        )


def validate_assisted_evidence_metadata(
    item: dict[str, Any],
    *,
    source_kind: str,
    source: str,
) -> str:
    """Validate the untrusted Agent evidence envelope.

    The content hash and quote are checked by ``evidence_index`` for local
    files.  This function checks the additional provenance required before an
    Agent-authored semantic change can be considered.
    """

    exact_quote = item.get("exact_quote")
    if not isinstance(exact_quote, str) or not exact_quote.strip():
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"assisted evidence for {source} requires exact_quote",
        )
    if "quote" in item and item.get("quote") != exact_quote:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"assisted evidence quote aliases conflict for {source}",
        )
    if source_kind not in ASSISTED_SOURCE_KINDS:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"unsupported assisted evidence source_kind: {source_kind}",
        )
    supplied_hash = item.get("source_hash")
    if (
        not isinstance(supplied_hash, str)
        or re.fullmatch(r"sha256:[0-9a-fA-F]{64}", supplied_hash) is None
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"assisted evidence for {source} requires a valid source_hash",
        )
    for field in ("applicability", "derivation"):
        value = item.get(field)
        if not isinstance(value, str) or not value.strip():
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"assisted evidence for {source} requires {field}",
            )
    if "core_science_change" not in item:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"assisted evidence for {source} requires "
            "core_science_change=false",
        )
    if item.get("core_science_change") is not False:
        raise PolicyStop(
            "POLICY_VIOLATION",
            f"assisted evidence for {source} must declare "
            "core_science_change=false",
        )
    if source_kind == WEB_SOURCE_KIND:
        if not re.fullmatch(r"https://[^\s]+", source):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "authoritative web evidence requires an HTTPS URL",
            )
        if item.get("url") != source:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "web evidence url must exactly match source",
            )
        retrieved_at = item.get("retrieved_at")
        metadata = item.get("retrieval_metadata")
        if not isinstance(retrieved_at, str) or not retrieved_at.strip():
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "web evidence requires retrieved_at metadata",
            )
        if not isinstance(metadata, dict) or not metadata:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "web evidence requires retrieval_metadata",
            )
        metadata_time = metadata.get("retrieved_at")
        if metadata_time is not None and metadata_time != retrieved_at:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "web evidence retrieval timestamps conflict",
            )
        approval = item.get("approval")
        if not isinstance(approval, dict):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "web evidence requires an explicit approval object",
            )
        if (
            approval.get("approved") is not True
            or approval.get("primary") is not True
            or approval.get("authority") not in WEB_AUTHORITIES
            or not isinstance(approval.get("reference"), str)
            or not approval["reference"].strip()
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "web evidence approval must identify an authoritative primary "
                "source and approval reference",
            )
        content_hash = metadata.get("content_hash")
        if content_hash is not None and content_hash != supplied_hash:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "web retrieval content_hash conflicts with source_hash",
            )
    return exact_quote


def local_assisted_source_kind(relative: Path) -> str | None:
    """Return the admissible Agent evidence kind for a package path."""

    if relative.parts and relative.parts[0] == "paper":
        return "PACKAGE_PAPER"
    if relative.as_posix() in DIRECT_SOURCE_FILES:
        return "PACKAGE_DIRECT_SOURCE"
    if relative.parts and relative.parts[0] in DIRECT_SOURCE_ROOTS:
        return "PACKAGE_DIRECT_SOURCE"
    return None


def evidence_index(
    root: Path,
    report: dict[str, Any],
    manifest: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    raw = plan.get("evidence")
    repair_class = plan.get("repair_class")
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
        quote = item.get("exact_quote", item.get("quote"))
        if not all(isinstance(value, str) and value.strip() for value in (evidence_id, source, quote)):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "Each evidence item requires non-empty id, source, and quote.",
            )
        if evidence_id in indexed:
            raise PolicyStop(
                "BLOCKED_EVIDENCE", f"Duplicate evidence id: {evidence_id}"
            )
        source_kind = item.get("source_kind")
        if repair_class == "ASSISTED_FIX":
            if not isinstance(source_kind, str):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    f"assisted evidence {evidence_id} requires source_kind",
                )
            quote = validate_assisted_evidence_metadata(
                item, source_kind=source_kind, source=source
            )
        if source_kind == WEB_SOURCE_KIND:
            if repair_class != "ASSISTED_FIX":
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "web evidence is only admissible for ASSISTED_FIX",
                )
            local = None
            source_category = "authoritative_primary_web"
        elif "://" in source or source.startswith(("file:", "http:", "https:")):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "Evidence sources must be local package files.",
            )
        elif source.startswith(EVIDENCE_SOURCE_PREFIX):
            if source != f"{EVIDENCE_SOURCE_PREFIX}{plan['finding_id']}":
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "Audit evidence must bind the selected finding.",
                )
            local = source_audit_dir(root, plan) / "audit_report.json"
            source_category = "audit_finding"
        else:
            try:
                local, relative = package_path(
                    root, source, context="evidence source"
                )
            except (TypeError, ValueError) as exc:
                raise PolicyStop("BLOCKED_EVIDENCE", str(exc)) from exc
            top = relative.parts[0] if relative.parts else ""
            if top == "solution":
                source_category = "solution_oracle"
            elif top == "paper":
                source_category = "paper"
            elif (
                source_kind == "PACKAGE_DIRECT_SOURCE"
                and local_assisted_source_kind(relative) == "PACKAGE_DIRECT_SOURCE"
            ):
                source_category = "direct_source"
            elif top == "tests":
                source_category = "checker_contract"
            elif relative.as_posix() == "instruction.md":
                source_category = "public_instruction"
            elif top in METADATA_ROOTS:
                source_category = "metadata"
            else:
                source_category = "unsupported"
        if local is not None and not local.is_file():
            raise PolicyStop(
                "BLOCKED_EVIDENCE", f"Evidence source does not exist: {source}"
            )
        if local is not None and (local.is_symlink() or (
            source_category != "audit_finding"
            and not local.resolve().is_relative_to(root.resolve())
        )):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"Evidence source escapes the Harbor 题包: {source}",
            )
        if local is not None:
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
        actual_hash = sha256_file(local) if local is not None else None
        if source_category == "paper":
            # Review is always paper-grounded now (the only non-paper path is a
            # NON_MAT fail-fast that never enters Repair).  Paper evidence is
            # therefore always admissible, but each item must bind the exact
            # paper/** file the source audit hashed (mismatch/unbound →
            # BLOCKED_EVIDENCE).
            input_hashes = manifest.get("input_hashes", {})
            if (
                not isinstance(input_hashes, dict)
                or input_hashes.get(relative.as_posix()) != actual_hash
            ):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "paper evidence must bind the source-audit-hashed paper file",
                )
        if (
            repair_class == "ASSISTED_FIX"
            and source_category == "direct_source"
        ):
            input_hashes = manifest.get("input_hashes", {})
            if (
                not isinstance(input_hashes, dict)
                or input_hashes.get(relative.as_posix()) != actual_hash
            ):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "direct package evidence must bind the "
                    "source-audit-hashed file",
                )
        if repair_class == "ASSISTED_FIX":
            expected_kind = (
                WEB_SOURCE_KIND
                if source_category == "authoritative_primary_web"
                else local_assisted_source_kind(relative)
                if local is not None
                else None
            )
            if source_kind != expected_kind:
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    f"assisted evidence source_kind does not match {source}",
                )
        if supplied_hash != actual_hash and not (
            repair_class == "ASSISTED_FIX"
            and source_category == "authoritative_primary_web"
            and actual_hash is None
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"Evidence hash does not match {source}.",
            )
        normalized = dict(item)
        declared_category = item.get("source_category")
        if declared_category is not None and declared_category != source_category:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"Evidence source category is false for {source}.",
            )
        normalized["source_category"] = source_category
        normalized["source_hash"] = (
            actual_hash if actual_hash is not None else supplied_hash
        )
        normalized["quote"] = quote
        if repair_class == "ASSISTED_FIX":
            normalized["exact_quote"] = quote
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
    linked = [evidence[item] for item in evidence_ids]
    if any(
        item.get("conflict") is True
        or item.get("conflicting") is True
        or item.get("conflicts_with")
        for item in linked
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"Operation {operation.get('id')} links explicitly conflicting evidence.",
        )
    claims: set[str] = set()
    for item in linked:
        _, precision = normalized_precision(item)
        if not precision:
            continue
        claim = {
            key: precision.get(key)
            for key in (
                "key",
                "field",
                "value",
                "replacement",
                "type",
                "unit",
                "required",
                "shape",
                "dtype",
                "axis_semantics",
                "direction",
                "mode",
                "scoring_contract",
                "mathematical_proof",
            )
            if precision.get(key) is not None
        }
        if claim:
            claims.add(
                json.dumps(claim, ensure_ascii=False, sort_keys=True, default=str)
            )
    if len(claims) > 1:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"Operation {operation.get('id')} links ambiguous evidence claims.",
        )
    return linked


def precision_kind_for(operation: dict[str, Any]) -> str | None:
    relative = Path(str(operation.get("file", ""))).as_posix()
    if operation.get("type") == "json_set":
        tokens = operation.get("path")
        final = str(tokens[-1]).lower() if isinstance(tokens, list) and tokens else ""
        if "threshold" in final or "weight" in final:
            return "scoring_contract"
        if "tolerance" in final or "error" in final:
            return "tolerance"
        if any(term in final for term in ("gold", "target", "reference")):
            return "gold"
        return "json_key"
    if relative.lower().endswith(".json") and operation.get("type") in {
        "replace_text",
        "text_replace",
        "write_file",
    }:
        return "json_key"
    if relative.lower().endswith(".csv"):
        return "csv_column"
    if relative.lower().endswith(".npy"):
        return "npy_array"
    if relative == "instruction.md":
        return "scientific_method"
    if relative.startswith("tests/"):
        patch = proposed_text(operation)
        if any(token in patch for token in ("try:", "except ", "except:")):
            return "exception_guard"
        return "harbor_path"
    if relative.startswith("solution/"):
        return None
    return "harbor_path"


def json_type_name(value: Any) -> str:
    return (
        "boolean"
        if isinstance(value, bool)
        else "number"
        if isinstance(value, (int, float))
        else "string"
        if isinstance(value, str)
        else "array"
        if isinstance(value, list)
        else "object"
        if isinstance(value, dict)
        else "null"
    )


def normalized_precision(item: dict[str, Any]) -> tuple[str | None, dict[str, Any]]:
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
    return precision.get("kind") or item.get("kind"), precision


def quote_supports_precision(
    item: dict[str, Any],
    precision: dict[str, Any],
    fields: tuple[str, ...],
) -> bool:
    quote = str(item.get("quote", "")).casefold()
    for field in fields:
        value = precision.get(field)
        if value is None or value == "":
            continue
        if field == "required" and isinstance(value, bool):
            token = "required" if value else "optional"
        elif isinstance(value, bool):
            token = str(value).lower()
        else:
            token = str(value).casefold()
        if token not in quote:
            return False
    return True


def validate_precision_matrix(
    operation: dict[str, Any],
    linked: list[dict[str, Any]],
    repair_class: str,
    repair_scope: str | None = None,
) -> None:
    expected = precision_kind_for(operation)
    if (
        repair_class == "ASSISTED_FIX"
        and repair_scope == "SCORING_SEMANTICS"
        and Path(str(operation.get("file"))).as_posix()
        == "tests/checker.py"
    ):
        expected = "scoring_contract"
    if repair_class == "ASSISTED_FIX" and expected is None:
        expected = "harbor_path"
    if expected is None:
        return
    if repair_class == "AUTO_FIX" and Path(str(operation["file"])).as_posix() != (
        "instruction.md"
    ):
        # Deterministic AUTO_FIX operations use a Harbor contract/finding rather
        # than inventing scientific precision.  Core targets are rejected below.
        return
    valid: list[dict[str, Any]] = []
    valid_items: list[dict[str, Any]] = []
    for item in linked:
        kind, precision = normalized_precision(item)
        if kind != expected:
            if repair_class == "ASSISTED_FIX":
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    f"Evidence precision does not match {expected} for "
                    f"{operation.get('file')}.",
                )
            continue
        valid.append(precision)
        valid_items.append(item)
    if not valid:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"Evidence precision does not match {expected} for "
            f"{operation.get('file')}.",
        )
    required = PRECISION_RULES[expected]
    if not all(
        all(
            field in precision
            and precision[field] is not None
            and precision[field] != ""
            for field in required
        )
        for precision in valid
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"{expected} evidence lacks the required typed precision fields.",
        )
    if not all(
        quote_supports_precision(item, precision, required)
        for item, precision in zip(valid_items, valid)
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"{expected} quote does not substantively support the exact "
            "field/type/unit/requiredness/value.",
        )
    if expected in {
        "csv_column",
        "npy_array",
        "scientific_method",
        "exception_guard",
        "harbor_path",
    } and any(
        precision.get("replacement") != proposed_text(operation)
        for precision in valid
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"{expected} evidence does not match the exact operation patch.",
        )
    if expected == "json_key":
        operation_path = operation.get("path")
        operation_key = None
        operation_value: Any = None
        if isinstance(operation_path, list) and operation_path:
            operation_key = str(operation_path[-1])
            operation_value = operation.get("value")
        elif operation.get("type") in {
            "replace_text",
            "text_replace",
            "write_file",
        }:
            try:
                if operation.get("type") == "write_file":
                    old_document = {}
                    new_document = json.loads(operation.get("content", ""))
                else:
                    old_document = json.loads(operation.get("old", ""))
                    new_document = json.loads(operation.get("new", ""))
            except (TypeError, ValueError, json.JSONDecodeError):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "JSON text operation must contain complete valid JSON values.",
                )
            if not isinstance(old_document, dict) or not isinstance(new_document, dict):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "JSON text operation requires object-level typed evidence.",
                )
            changed_keys = {
                key
                for key in set(old_document) | set(new_document)
                if old_document.get(key) != new_document.get(key)
            }
            evidenced_keys = {str(precision.get("key")) for precision in valid}
            if changed_keys != evidenced_keys:
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "JSON replacement evidence must cover every changed field.",
                )
            for precision in valid:
                key = str(precision["key"])
                if precision.get("value") != new_document.get(key):
                    raise PolicyStop(
                        "BLOCKED_EVIDENCE",
                        "JSON evidence value differs from the replacement value.",
                    )
                if (
                    str(precision.get("type")).casefold()
                    != json_type_name(new_document.get(key))
                ):
                    raise PolicyStop(
                        "BLOCKED_EVIDENCE",
                        "JSON evidence type differs from the replacement value type.",
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
        if operation_key is not None and any(
            precision.get("value") != operation_value for precision in valid
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "JSON evidence value differs from the operation value.",
            )
        expected_value = (
            operation_value
            if operation_key is not None
            else None
        )
        if operation_key is not None:
            if any(
                str(precision.get("type")).casefold()
                != json_type_name(expected_value)
                for precision in valid
            ):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "JSON evidence type differs from the operation value type.",
                )
    if expected in {"tolerance", "scoring_contract"}:
        tokens = operation.get("path")
        operation_field = (
            str(tokens[-1]) if isinstance(tokens, list) and tokens else None
        )
        if expected == "scoring_contract" and operation_field is None:
            if any(
                precision.get("replacement") != proposed_text(operation)
                for precision in valid
            ):
                raise PolicyStop(
                    "BLOCKED_EVIDENCE",
                    "scoring-contract evidence must bind the exact checker "
                    "replacement.",
                )
            return
        if operation_field is None or any(
            precision.get("field") != operation_field
            or precision.get("value") != operation.get("value")
            or str(precision.get("type")).casefold()
            != json_type_name(operation.get("value"))
            for precision in valid
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"{expected} evidence does not match the exact field and value.",
            )
    if expected == "gold":
        tokens = operation.get("path")
        operation_field = (
            str(tokens[-1]) if isinstance(tokens, list) and tokens else None
        )
        if operation_field is None or any(
            precision.get("field") != operation_field
            or precision.get("value") != operation.get("value")
            or str(precision.get("type")).casefold()
            != json_type_name(operation.get("value"))
            for precision in valid
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "Gold evidence does not match the exact field and value.",
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
        item.get("source_category")
        not in {
            "public_instruction",
            "paper",
            "direct_source",
            "authoritative_primary_web",
        }
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


_D3_RETURN_AUTO_CODES = frozenset(
    {"SCORER_MISSING_RETURN", "SCORER_RETURN_NOT_TOTAL"}
)
_D4_NORMALIZATION_AUTO_CODES = frozenset({"WEIGHTS_NOT_ONE"})


def _nested_dicts(value: Any) -> Iterable[dict[str, Any]]:
    """Yield JSON object descendants without trusting a report shape."""

    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _nested_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from _nested_dicts(child)


def _return_proofs(evidence: Any) -> list[dict[str, Any]]:
    """Return unique nested-wrapper proofs from Review evidence."""

    proofs: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in _nested_dicts(evidence):
        direct = item.get("return_proof")
        candidates: Iterable[Any]
        if isinstance(direct, dict):
            if "return_expression" in direct or "proof_status" in direct:
                candidates = (direct,)
            else:
                candidates = direct.values()
        else:
            candidates = ()
        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            if "return_expression" not in candidate:
                continue
            marker = json.dumps(
                candidate, ensure_ascii=False, sort_keys=True, default=str
            )
            if marker not in seen:
                seen.add(marker)
                proofs.append(candidate)
        if "return_expression" in item and "proof_status" in item:
            marker = json.dumps(
                item, ensure_ascii=False, sort_keys=True, default=str
            )
            if marker not in seen:
                seen.add(marker)
                proofs.append(item)
    return proofs


def _proof_span(proof: dict[str, Any]) -> dict[str, int] | None:
    """Normalize the source span spellings emitted by Review."""

    raw = (
        proof.get("function_span")
        or proof.get("source_span")
        or proof.get("span")
    )
    if not isinstance(raw, dict):
        return None
    if all(
        key in raw
        for key in ("lineno", "end_lineno", "col_offset", "end_col_offset")
    ):
        values = {
            key: raw.get(key)
            for key in ("lineno", "end_lineno", "col_offset", "end_col_offset")
        }
    elif all(key in raw for key in ("lineno", "end_lineno")):
        values = {
            "lineno": raw.get("lineno"),
            "end_lineno": raw.get("end_lineno"),
            "col_offset": raw.get("col_offset"),
            "end_col_offset": raw.get("end_col_offset"),
        }
    elif all(key in raw for key in ("start_line", "end_line")):
        values = {
            "lineno": raw.get("start_line"),
            "end_lineno": raw.get("end_line"),
            "col_offset": raw.get("start_col", raw.get("col_offset")),
            "end_col_offset": raw.get(
                "end_col", raw.get("end_col_offset")
            ),
        }
    elif isinstance(raw.get("start"), dict) and isinstance(
        raw.get("end"), dict
    ):
        start = raw["start"]
        end = raw["end"]
        values = {
            "lineno": start.get("line"),
            "end_lineno": end.get("line"),
            "col_offset": start.get("column", start.get("col")),
            "end_col_offset": end.get("column", end.get("col")),
        }
    else:
        return None
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in values.values()
        if value is not None
    ):
        return None
    if values["col_offset"] is None or values["end_col_offset"] is None:
        # Line-only proofs are still source-bound, but a supplied partial
        # column span is not.  This keeps malformed spans fail-closed.
        if raw.keys() & {"col_offset", "end_col_offset", "start_col", "end_col"}:
            return None
        values.pop("col_offset")
        values.pop("end_col_offset")
    return values  # type: ignore[return-value]


def _function_name(proof: dict[str, Any]) -> str | None:
    for key in ("function_name", "outer_function", "function"):
        value = proof.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return None


def _source_hash(proof: dict[str, Any]) -> str | None:
    for key in ("source_hash", "checker_source_hash"):
        value = proof.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return None


def _node_span(node: ast.AST) -> dict[str, int]:
    return {
        key: getattr(node, key)
        for key in ("lineno", "end_lineno", "col_offset", "end_col_offset")
        if getattr(node, key, None) is not None
    }


def _proof_matches_function(
    function: ast.FunctionDef | ast.AsyncFunctionDef,
    proof: dict[str, Any],
) -> bool:
    span = _proof_span(proof)
    if span is None:
        return False
    actual = _node_span(function)
    return all(actual.get(key) == value for key, value in span.items())


def _owned_returns(
    function: ast.FunctionDef | ast.AsyncFunctionDef,
) -> list[ast.Return]:
    """Return statements owned by a function, excluding nested definitions."""

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


def _parse_expression(value: Any) -> ast.expr | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = ast.parse(value, mode="eval")
    except SyntaxError:
        return None
    return parsed.body


def _unique_function(
    tree: ast.AST, name: str
) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    matches = [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == name
    ]
    return matches[0] if len(matches) == 1 else None


def _d3_proof_is_structurally_bound(evidence: Any) -> bool:
    proofs = _return_proofs(evidence)
    return bool(
        proofs
        and any(
            proof.get("proof_status") == "PROVEN"
            and proof.get("auto_fix_provable", True) is True
            and _function_name(proof)
            and _source_hash(proof)
            and _proof_span(proof) is not None
            and _parse_expression(proof.get("return_expression")) is not None
            for proof in proofs
        )
    )


def _d4_proof_is_structurally_bound(evidence: Any) -> bool:
    if not isinstance(evidence, dict):
        return False
    return (
        evidence.get("ratio_preserving_normalization") is True
        and isinstance(evidence.get("weights"), list)
        and isinstance(evidence.get("normalized_weights"), list)
        and bool(evidence["weights"])
        and len(evidence["weights"]) == len(evidence["normalized_weights"])
    )


def is_proof_bound_d3_d4_auto_fix(
    repair_class: str,
    deterministic_check: str | None,
    finding_code: str | None,
    evidence: Any,
) -> bool:
    """Return whether a D3/D4 AUTO_FIX may bypass patch precision."""

    if repair_class != "AUTO_FIX":
        return False
    if deterministic_check == "D3":
        return (
            finding_code in _D3_RETURN_AUTO_CODES
            and _d3_proof_is_structurally_bound(evidence)
        )
    if deterministic_check == "D4":
        return (
            finding_code in _D4_NORMALIZATION_AUTO_CODES
            and _d4_proof_is_structurally_bound(evidence)
        )
    return False


def _validate_d3_return_operation(
    root: Path, evidence: Any, operation: dict[str, Any]
) -> str | None:
    if operation.get("file") != "tests/checker.py":
        return "D3 return AUTO_FIX must target tests/checker.py"
    if operation.get("type") not in {"replace_text", "text_replace"}:
        return "D3 return AUTO_FIX must replace checker source text"
    checker = root / "tests/checker.py"
    if not checker.is_file() or checker.is_symlink():
        return "D3 return AUTO_FIX checker source is missing"
    source = checker.read_text(encoding="utf-8")
    source_hash = sha256_file(checker)
    old = operation.get("old")
    new = operation.get("new")
    count = operation.get("count", 1)
    if (
        not isinstance(old, str)
        or not old
        or not isinstance(new, str)
        or not isinstance(count, int)
        or count != 1
        or source.count(old) != 1
    ):
        return "D3 return AUTO_FIX replacement is not unique in current source"
    try:
        before_tree = ast.parse(source)
        after_tree = ast.parse(source.replace(old, new, 1))
    except SyntaxError:
        return "D3 return AUTO_FIX would leave checker.py unparseable"

    matches: list[
        tuple[
            dict[str, Any],
            ast.FunctionDef | ast.AsyncFunctionDef,
            ast.FunctionDef | ast.AsyncFunctionDef,
            ast.expr,
        ]
    ] = []
    for proof in _return_proofs(evidence):
        if proof.get("proof_status") != "PROVEN":
            continue
        if proof.get("auto_fix_provable", True) is not True:
            continue
        if _source_hash(proof) != source_hash:
            continue
        name = _function_name(proof)
        if not name:
            continue
        before_function = _unique_function(before_tree, name)
        after_function = _unique_function(after_tree, name)
        expression = _parse_expression(proof.get("return_expression"))
        if (
            before_function is None
            or after_function is None
            or expression is None
            or not _proof_matches_function(before_function, proof)
            or not after_function.body
        ):
            continue
        appended = after_function.body[-1]
        if (
            isinstance(appended, ast.Return)
            and appended.value is not None
            and ast.dump(appended.value, include_attributes=False)
            == ast.dump(expression, include_attributes=False)
            and len(_owned_returns(after_function))
            == len(_owned_returns(before_function)) + 1
        ):
            matches.append(
                (proof, before_function, after_function, expression)
            )
    if len(matches) != 1:
        return "D3 return AUTO_FIX source/function proof is stale or ambiguous"
    proof, before_function, after_function, expression = matches[0]
    before_returns = _owned_returns(before_function)
    if before_function.body and isinstance(before_function.body[-1], ast.Return):
        return "D3 return AUTO_FIX targets a function that already returns"

    appended = after_function.body[-1]
    if not isinstance(appended, ast.Return) or appended.value is None:
        return "D3 return AUTO_FIX must append a value return"
    if ast.dump(appended.value, include_attributes=False) != ast.dump(
        expression, include_attributes=False
    ):
        return "D3 return AUTO_FIX operation differs from return proof"
    if len(_owned_returns(after_function)) != len(before_returns) + 1:
        return "D3 return AUTO_FIX changes more than the proven return path"

    # Remove only the appended return and compare the complete AST.  This
    # rejects threshold/Gold/scoring edits hidden in the same text operation.
    after_function.body.pop()
    if ast.dump(before_tree, include_attributes=False) != ast.dump(
        after_tree, include_attributes=False
    ):
        return "D3 return AUTO_FIX contains an unproven semantic change"
    return None


def _d4_component_id(value: Any, index: int) -> str | None:
    if not isinstance(value, dict):
        return None
    candidate = value.get("id") or value.get("output_file") or f"step-{index}"
    return str(candidate)


def _validate_d4_normalization_operation(
    root: Path, evidence: Any, operation: dict[str, Any]
) -> str | None:
    if operation.get("file") != "tests/grading_spec.json":
        return "D4 normalization AUTO_FIX must target tests/grading_spec.json"
    if operation.get("type") != "json_set":
        return "D4 normalization AUTO_FIX must use json_set"
    path = operation.get("path")
    if (
        not isinstance(path, list)
        or len(path) < 3
        or path[-1] != "weight"
        or not isinstance(path[-2], int)
        or isinstance(path[-2], bool)
    ):
        return "D4 normalization AUTO_FIX must target a step weight"
    weights = evidence.get("weights") if isinstance(evidence, dict) else None
    normalized = (
        evidence.get("normalized_weights") if isinstance(evidence, dict) else None
    )
    if not isinstance(weights, list) or not isinstance(normalized, list):
        return "D4 normalization AUTO_FIX lacks typed weight proof"
    raw_values: dict[str, float] = {}
    for item in weights:
        if not isinstance(item, dict):
            return "D4 normalization AUTO_FIX has malformed source weights"
        component_id = item.get("component_id")
        value = item.get("value")
        if (
            not isinstance(component_id, str)
            or component_id in raw_values
            or isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(float(value))
            or float(value) <= 0
        ):
            return "D4 normalization AUTO_FIX has invalid source weights"
        raw_values[component_id] = float(value)
    expected = {
        item.get("component_id"): item.get("value")
        for item in normalized
        if isinstance(item, dict)
    }
    if len(expected) != len(normalized):
        return "D4 normalization AUTO_FIX has duplicate normalized components"
    if set(expected) != set(raw_values):
        return "D4 normalization AUTO_FIX source/normalized components differ"
    total = sum(raw_values.values())
    if not math.isfinite(total) or total <= 0:
        return "D4 normalization AUTO_FIX source weights are not normalizable"
    for component_id, value in expected.items():
        if (
            not isinstance(value, (int, float))
            or isinstance(value, bool)
            or not math.isfinite(float(value))
            or float(value) <= 0
            or not math.isclose(
                float(value),
                raw_values[component_id] / total,
                rel_tol=1e-12,
                abs_tol=1e-12,
            )
        ):
            return "D4 normalization AUTO_FIX proof is not ratio-preserving"
    document_path = root / "tests/grading_spec.json"
    try:
        document = read_json(document_path)
        present, steps = json_path_value(document, path[:-2])
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return "D4 normalization AUTO_FIX grading source is unavailable"
    if not present or not isinstance(steps, list):
        return "D4 normalization AUTO_FIX path does not resolve to steps"
    index = path[-2]
    if index < 0 or index >= len(steps):
        return "D4 normalization AUTO_FIX step index is out of range"
    if not isinstance(steps[index], dict):
        return "D4 normalization AUTO_FIX step is not an object"
    component = _d4_component_id(steps[index], index)
    if component not in expected:
        return "D4 normalization AUTO_FIX component is not in proof"
    raw = next(
        (
            item.get("value")
            for item in weights
            if isinstance(item, dict) and item.get("component_id") == component
        ),
        None,
    )
    if raw is None or steps[index].get("weight") != raw:
        return "D4 normalization AUTO_FIX source/proof values drifted"
    replacement = operation.get("value")
    if replacement != expected[component]:
        return "D4 normalization AUTO_FIX does not preserve the proven ratios"
    if (
        isinstance(replacement, bool)
        or not isinstance(replacement, (int, float))
        or not math.isfinite(float(replacement))
    ):
        return "D4 normalization AUTO_FIX replacement is not finite"
    return None


def proof_bound_auto_fix_operation_error(
    root: Path,
    finding: dict[str, Any],
    operation: dict[str, Any],
) -> str | None:
    """Validate a proof-bound D3/D4 operation before it reaches apply."""

    check_id = finding.get("deterministic_check")
    code = finding.get("title", finding.get("code"))
    evidence = finding.get("evidence")
    if not is_proof_bound_d3_d4_auto_fix(
        "AUTO_FIX", check_id, code, evidence
    ):
        return "D3/D4 AUTO_FIX is not bound to a complete deterministic proof"
    if check_id == "D3":
        error = _validate_d3_return_operation(root, evidence, operation)
    else:
        error = _validate_d4_normalization_operation(root, evidence, operation)
    if error:
        return error

    # Keep the established Review-side validator in the path.  Older Review
    # reports classified SCORER_MISSING_RETURN conservatively; the source/AST
    # proof above is the narrower Repair-side authorization for that one code.
    legacy_error = auto_fix_operation_error(finding, operation)
    if (
        legacy_error
        and not (
            check_id == "D3"
            and code == "SCORER_MISSING_RETURN"
            and legacy_error == "AUTO_FIX is not proven safe for this D3/D4 finding"
        )
    ):
        return legacy_error
    return None


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
    manifest: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    if plan.get("core_science_change") is not False:
        raise PolicyStop(
            "POLICY_VIOLATION",
            "Plan must declare core_science_change=false; Repair may not "
            "redefine the Harbor package's core science.",
        )
    evidence = evidence_index(root, report, manifest, plan)
    deterministic_evidence = plan.get("deterministic_evidence")
    if not isinstance(deterministic_evidence, dict):
        deterministic_evidence = next(
            (
                item.get("evidence", {})
                for item in report.get("findings", [])
                if isinstance(item, dict)
                and item.get("finding_id") == plan.get("finding_id")
            ),
            {},
        )
    if plan.get("deterministic_check") in {"D1", "D2"}:
        deterministic_evidence = dict(
            deterministic_evidence
            if isinstance(deterministic_evidence, dict)
            else {}
        )
        deterministic_evidence["source_bound_output_proof"] = (
            output_repair_proof(report.get("contract_map"))
        )
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
    unique_scoring_wiring_auto_fix = (
        plan.get("deterministic_check") == "D6"
        and plan.get("repair_class") == "AUTO_FIX"
        and plan.get("repair_scope") == "UNIQUE_SCORING_WIRING"
    )
    structural_auto_fix = (
        plan.get("repair_class") == "AUTO_FIX"
        and plan.get("deterministic_check") in {"D1", "D2"}
        and bool(plan["operations"])
        and all(
            is_structural_auto_fix_operation(operation)
            for operation in plan["operations"]
        )
    )
    proof_bound_auto_fix = is_proof_bound_d3_d4_auto_fix(
        plan.get("repair_class"),
        plan.get("deterministic_check"),
        plan.get("finding_code"),
        deterministic_evidence,
    )
    if (
        plan["repair_class"] == "AUTO_FIX"
        and target_roles & {"instruction", "tests"}
        and not (
            unique_scoring_wiring_auto_fix
            or structural_auto_fix
            or proof_bound_auto_fix
        )
    ):
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
        if plan["repair_class"] == "AUTO_FIX":
            try:
                if plan.get("deterministic_check") in {"D1", "D2"}:
                    error = structural_auto_fix_operation_error(
                        operation,
                        deterministic_evidence.get(
                            "source_bound_output_proof"
                        ),
                    )
                    if error:
                        raise ValueError(error)
                elif plan.get("deterministic_check") in {"D3", "D4"}:
                    error = proof_bound_auto_fix_operation_error(
                        root,
                        {
                            "deterministic_check": plan.get("deterministic_check"),
                            "title": plan.get("finding_code"),
                            "evidence": deterministic_evidence,
                        },
                        operation,
                    )
                    if error:
                        raise ValueError(error)
                elif plan.get("deterministic_check") == "D5":
                    validate_auto_fix_operation(
                        root,
                        operation,
                        plan.get("finding_code")
                        or (
                            "PARSE_ERROR"
                            if plan.get("deterministic_check") == "D5"
                            else None
                        ),
                    )
                elif (
                    plan.get("deterministic_check") == "D6"
                    and plan.get("repair_scope") == "UNIQUE_SCORING_WIRING"
                ):
                    checker_path = root / "tests/checker.py"
                    checker_source = (
                        checker_path.read_text(encoding="utf-8")
                        if checker_path.is_file()
                        else ""
                    )
                    error = unique_wiring_auto_fix_operation_error(
                        {
                            "deterministic_check": plan.get(
                                "deterministic_check"
                            ),
                            "title": plan.get("finding_code"),
                            "evidence": deterministic_evidence,
                        },
                        operation,
                        checker_source,
                    )
                    if error:
                        raise ValueError(error)
            except ValueError as exc:
                raise PolicyStop("POLICY_VIOLATION", str(exc)) from exc
        linked = linked_evidence(operation, evidence)
        _, relative = repair_target(root, operation["file"])
        if relative.parts and relative.parts[0] != "solution" and any(
            item.get("source_category") == "solution_oracle" for item in linked
        ):
            raise PolicyStop(
                "POLICY_VIOLATION",
                "Oracle/solution content cannot support public or checker "
                "contract changes.",
            )
        if relative.as_posix() == "instruction.md":
            addition = proposed_text(operation)
            if any(fragment in addition for fragment in hidden_fragments):
                raise PolicyStop(
                    "POLICY_VIOLATION",
                    "Repair would leak hidden solution content into instruction.md.",
                )
        if not (
            plan["repair_class"] == "AUTO_FIX"
            and (
                plan.get("deterministic_check") in {"D1", "D2"}
                or proof_bound_auto_fix
            )
        ):
            validate_precision_matrix(
                operation,
                linked,
                plan["repair_class"],
                plan.get("repair_scope"),
            )
        expected_precision = precision_kind_for(operation)
        allowed_categories = (
            {
                "public_instruction",
                "paper",
                "direct_source",
                "authoritative_primary_web",
            }
            if expected_precision == "scientific_method"
            else {
                "audit_finding",
                "public_instruction",
                "checker_contract",
                "paper",
                "direct_source",
                "authoritative_primary_web",
            }
        )
        if any(
            item.get("source_category") not in allowed_categories
            for item in linked
        ):
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                "Evidence source role cannot support this scientific/schema/"
                "scoring change.",
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
            process = sandbox_runtime.run_in_sandbox(
                command,
                mounts=[(root, "/workspace", "rw")],
                workdir="/workspace",
                timeout=timeout,
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


def ensure_command_regression_env(
    specifications: Iterable[dict[str, Any]],
) -> None:
    """Abort before mutation when a command regression needs the sandbox."""
    if any(
        isinstance(specification, dict)
        and specification.get("type") == "command"
        for specification in specifications
    ):
        sandbox_runtime.ensure_env()


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


def report_configuration(report: dict[str, Any]) -> str:
    configuration = report.get("configuration")
    if not isinstance(configuration, dict):
        raise ValueError("Review report requires configuration")
    if configuration.get("review_lane") != REVIEW_LANE:
        raise ValueError("Review report must use review_lane='dual'")
    return REVIEW_LANE


def run_equal_depth_review(
    candidate: Path,
    report: dict[str, Any],
    source_manifest_or_plan: dict[str, Any],
    plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if plan is None:
        plan = source_manifest_or_plan
        source_manifest = {}
    else:
        source_manifest = source_manifest_or_plan
    runner = (
        Path(__file__).resolve().parents[2]
        / "materials-benchmark-review/scripts/run_review.py"
    )
    if not runner.is_file():
        raise FileNotFoundError(f"Review runner is missing: {runner}")
    source_lane = report_configuration(report)
    external_binding_hashes(candidate, plan, source_manifest)
    audit_output_dir = reaudit_output_root(candidate)
    command = [
        sys.executable,
        str(runner),
        str(candidate),
        "--audit-output-dir",
        str(audit_output_dir),
        "--output-purpose",
        "reaudit",
    ]
    for key, flag in {"agent_assessment": "--agent-assessment"}.items():
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
    reaudit = read_json(audit_output_dir / "benchmark_audit/audit_report.json")
    if report_configuration(reaudit) != source_lane:
        raise ValueError("re-audit review lane differs from the source audit")
    return reaudit


def finding_key(finding: dict[str, Any]) -> str | None:
    for key in ("code", "title", "finding_code"):
        value = finding.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def finding_reference(
    finding: dict[str, Any],
    *,
    audit_id: str | None,
) -> dict[str, Any]:
    code = finding_key(finding)
    payload = {
        "finding_code": code,
        "deterministic_check": finding.get("deterministic_check"),
        "affected_files": sorted(
            str(item)
            for item in finding.get("affected_files", [])
            if isinstance(item, str)
        ),
        "root_cause": (
            finding.get("evidence", {}).get("root_cause")
            if isinstance(finding.get("evidence"), dict)
            else None
        ),
    }
    return {
        "finding_id": finding.get("finding_id"),
        "finding_code": code,
        "finding_fingerprint": canonical_json_hash(payload),
        "deterministic_check": finding.get("deterministic_check"),
        "severity": finding.get("severity"),
        "audit_id": audit_id,
    }


def blocking_finding_references(
    findings: list[dict[str, Any]],
    *,
    audit_id: str | None,
) -> list[dict[str, Any]]:
    return [
        finding_reference(item, audit_id=audit_id)
        for item in findings
        if item.get("blocking") is True
    ]


def canonical_publish_route(report: dict[str, Any]) -> str | None:
    """Return the publish route from a Review report, never the verdict.

    In v11 ``summary.disposition`` holds the VERDICT; the route lives in the
    top-level ``publishability`` and ``summary.publication_route`` /
    ``summary.publishability`` fields.  Returns ``None`` when no route field is
    present so ``canonical_fields`` can derive it from the verdict.
    """

    if not isinstance(report, dict):
        return None
    summary = report.get("summary", {})
    if not isinstance(summary, dict):
        summary = {}
    return (
        report.get("publishability")
        or summary.get("publication_route")
        or summary.get("publishability")
    )


def reaudit_has_no_hard_gate(reaudit: dict[str, Any]) -> bool:
    """Return the persisted Review hard-gate result, fail-closed."""

    summary = reaudit.get("summary", {})
    if not isinstance(summary, dict):
        return False
    if summary.get("hard_gate") is True or summary.get("hard_gate_triggered") is True:
        return False
    gates = reaudit.get("hard_gates")
    if not isinstance(gates, list):
        return False
    return not any(
        isinstance(gate, dict) and gate.get("status") == "FAIL"
        for gate in gates
    )


def unresolved_severe_finding_ids(
    findings: Iterable[dict[str, Any]],
) -> list[str]:
    resolved = {"RESOLVED", "CLOSED", "FIXED"}
    return [
        str(item.get("finding_id") or "<missing-finding-id>")
        for item in findings
        if isinstance(item, dict)
        and item.get("severity") in {"HIGH", "FATAL"}
        and item.get("status", "OPEN") not in resolved
    ]


def validate_authoritative_pass(reaudit: dict[str, Any]) -> dict[str, Any]:
    """Validate every evidence obligation required for publication."""

    if not isinstance(reaudit, dict):
        raise ValueError("re-audit report is not an object")
    summary = reaudit.get("summary")
    if not isinstance(summary, dict):
        raise ValueError("re-audit summary is absent")
    if summary.get("final_verdict") != "PASS":
        raise ValueError("re-audit authoritative verdict is not PASS")
    if summary.get("scoring_version") != CURRENT_SCORING_VERSION:
        raise ValueError(
            "re-audit scoring schema is stale: "
            f"{summary.get('scoring_version')!r}"
        )
    if canonical_publish_route(reaudit) != "PUBLISH_CANDIDATE":
        raise ValueError("re-audit authoritative route is not PUBLISH_CANDIDATE")
    if summary.get("hard_gate_triggered") is not False:
        raise ValueError("re-audit has a triggered Hard Gate")
    score = summary.get("total_score")
    try:
        numeric_score = float(score)
    except (TypeError, ValueError, OverflowError):
        numeric_score = float("nan")
    if (
        not math.isfinite(numeric_score)
        or not PUBLICATION_SCORE <= numeric_score <= 100
    ):
        raise ValueError("re-audit authoritative score is below 80 or non-finite")
    evidence_contract = reaudit.get("evidence_contract")
    if (
        not isinstance(evidence_contract, dict)
        or evidence_contract.get("fail_closed") is not True
        or evidence_contract.get("gaps") != []
    ):
        raise ValueError("re-audit evidence contract is incomplete")
    gates = reaudit.get("hard_gates")
    if not isinstance(gates, list) or [
        item.get("code") for item in gates if isinstance(item, dict)
    ] != list(HARD_GATE_CODES):
        raise ValueError("re-audit Hard Gates are incomplete")
    if any(
        not isinstance(gate, dict)
        or gate.get("status") != "PASS"
        or not isinstance(gate.get("evidence"), list)
        or not gate["evidence"]
        for gate in gates
    ):
        raise ValueError("all four re-audit Hard Gates must PASS with evidence")
    deterministic = reaudit.get("deterministic_contract")
    try:
        deterministic = validate_deterministic_contract(deterministic)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            "equal-depth re-audit lacks valid deterministic CLEAN evidence"
        ) from exc
    if deterministic["repair_summary"]["state"] != "CLEAN":
        raise ValueError("equal-depth re-audit did not return deterministic CLEAN")
    residual = [
        item.get("finding_id")
        for item in reaudit.get("findings", [])
        if isinstance(item, dict)
        and item.get("blocking") is True
        and item.get("status", "OPEN") not in {"RESOLVED", "CLOSED", "FIXED"}
    ]
    if residual:
        raise ValueError(
            "re-audit has residual blocking findings: " + ", ".join(residual)
        )
    severe = unresolved_severe_finding_ids(
        item for item in reaudit.get("findings", []) if isinstance(item, dict)
    )
    if severe:
        raise ValueError(
            "re-audit has unresolved severe findings: " + ", ".join(severe)
        )
    return {
        "authoritative_pass": True,
        "score": numeric_score,
        "evidence_contract_fail_closed": True,
        "evidence_contract_gaps": [],
        "hard_gate_codes": list(HARD_GATE_CODES),
        "hard_gate_statuses": ["PASS"] * len(HARD_GATE_CODES),
        "hard_gate_evidence": True,
        "deterministic_state": "CLEAN",
        "residual_blocking_finding_ids": [],
    }


def validate_reaudit(
    candidate: Path,
    reaudit: dict[str, Any],
    source_finding: dict[str, Any],
    source_report: dict[str, Any],
    plan: dict[str, Any],
    *,
    require_deterministic: bool = True,
) -> dict[str, Any]:
    summary = reaudit.get("summary", {})
    disposition_path = reaudit_audit_dir(candidate, plan) / "disposition.json"
    disposition = read_json(disposition_path) if disposition_path.is_file() else {}
    verdict = summary.get("final_verdict") or disposition.get("verdict")
    # The publish route lives in disposition.json ``route`` (and the finalizer's
    # ``summary.publication_route`` / ``summary.publishability``).  In v11
    # ``summary.disposition`` holds the VERDICT, so it must never be read as the
    # route (mirrors repair_batch and read_ext_disposition).
    route = (
        disposition.get("route")
        or summary.get("publication_route")
        or summary.get("publishability")
    )
    if verdict != "PASS" or route != "PUBLISH_CANDIDATE":
        raise ValueError("equal-depth re-audit did not route PASS to PUBLISH_CANDIDATE")
    source_key = finding_key(source_finding)
    if source_key and any(
        finding_key(item) == source_key
        for item in reaudit.get("findings", [])
        if isinstance(item, dict)
    ):
        raise ValueError("target finding remains open after re-audit")
    pass_evidence = validate_authoritative_pass(reaudit)
    configuration = reaudit.get("configuration", {})
    manifest_path = reaudit_audit_dir(candidate, plan) / "audit_manifest.json"
    manifest = read_json(manifest_path) if manifest_path.is_file() else {}
    if configuration.get("review_lane") != REVIEW_LANE:
        raise ValueError("re-audit review lane is not dual")
    if source_report.get("configuration", {}).get("review_lane") != REVIEW_LANE:
        raise ValueError("source audit review lane is not dual")
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
        "source_configuration": {"review_lane": REVIEW_LANE},
        "reaudit_configuration": {"review_lane": REVIEW_LANE},
        "reaudit_audit_id": reaudit.get("audit_id"),
        "reaudit_count": 1,
        "reaudit_verdict": verdict,
        "publication_route": route,
        **pass_evidence,
        "hard_gate_free": True,
        "identity_preserved": True,
        "mutation_scope_allowed": True,
        "residual_blocking_finding_ids": [],
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


def rebase_audit_paths(
    candidate: Path, final_root: Path, plan: dict[str, Any]
) -> None:
    audit = reaudit_audit_dir(candidate, plan)
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
        manifest["bundle_hash"] = canonical_json_hash(manifest["output_hashes"])
        write_json(manifest_path, manifest)


def externalize_generated_bundles(
    candidate: Path,
    root: Path,
    plan: dict[str, Any],
) -> dict[str, str]:
    """Record externally generated repair bundles.

    Equal-depth re-audit already writes under
    ``<repair_output_dir>/repair_reaudit/benchmark_audit``. Optional
    package-local ``benchmark_repair`` artifacts are moved beside it.
    """
    output = repair_output_root(root, plan)
    published: dict[str, str] = {}
    reaudit = reaudit_audit_dir(candidate, plan)
    if not reaudit.is_dir():
        raise FileNotFoundError(
            "generated repair_reaudit/benchmark_audit bundle is missing "
            "before publication"
        )
    published["benchmark_audit"] = str(reaudit.parent)
    repair_bundle = candidate / "benchmark_repair"
    if repair_bundle.is_dir():
        destination = output / "benchmark_repair"
        if destination.exists() or destination.is_symlink():
            raise FileExistsError(
                f"external repair output already exists: {destination}"
            )
        destination.parent.mkdir(parents=True, exist_ok=True)
        repair_bundle.rename(destination)
        published["benchmark_repair"] = str(destination)
    return published


def root_cause_id(report: dict[str, Any], plan: dict[str, Any]) -> str:
    value = f"{report['audit_id']}:{plan['finding_id']}"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:20]


def history_root_for(root: Path, plan: dict[str, Any] | None = None) -> Path:
    if plan is not None:
        output = repair_output_root(root, plan)
        if output is not None:
            return output / "repair_history"
    return root.parent / ".benchmark_repair_history"


def docker_image_identity() -> str:
    docker = shutil.which("docker")
    tag = sandbox_runtime.image_tag()
    if docker is None:
        return f"docker-cli-unavailable:{tag}"
    try:
        result = subprocess.run(
            [docker, "image", "inspect", "--format", "{{.Id}}", tag],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return f"docker-image-unavailable:{tag}"
    image_id = result.stdout.strip()
    return image_id if result.returncode == 0 and image_id else f"unavailable:{tag}"


def control_scope_id(report: dict[str, Any]) -> str:
    try:
        review_hash = collect_review_implementation_hashes().get(
            "aggregate_hash"
        )
    except (OSError, ValueError):
        review_hash = None
    dockerfile = getattr(sandbox_runtime, "DOCKERFILE", None)
    return canonical_json_hash(
        {
            "audit_id": report.get("audit_id"),
            "review_implementation_hash": review_hash,
            "repair_implementation_hash": sha256_file(Path(__file__)),
            "docker_image_identity": docker_image_identity(),
            "dockerfile_hash": (
                sha256_file(dockerfile)
                if isinstance(dockerfile, Path) and dockerfile.is_file()
                else None
            ),
        }
    )


def control_failure_fingerprint(
    exc: Exception,
    *,
    stage: str,
    root: Path,
) -> str:
    reason = str(exc).replace(str(root), "<ROOT>")
    reason = re.sub(
        r"(repair|audit)-\\d{8}T\\d{6}Z-[0-9a-f]+",
        r"\\1-<ID>",
        reason,
    )
    reason = re.sub(r"\\s+", " ", reason).strip()
    return canonical_json_hash(
        {
            "stage": stage,
            "exception_type": type(exc).__name__,
            "reason": reason,
        }
    )


def control_failure_retryable(exc: Exception) -> bool:
    reason = str(exc).lower()
    deterministic_fragments = (
        "attestation",
        "source-bound and immutable",
        "tampered or stale",
        "stale audit",
        "evidence source",
    )
    return not any(fragment in reason for fragment in deterministic_fragments)


def control_failure_decision(
    prior_controls: list[tuple[Path, dict[str, Any]]],
    fingerprint: str,
    *,
    transient: bool,
) -> dict[str, Any]:
    same_fingerprint = (
        sum(
            1
            for _, item in prior_controls
            if item.get("control_failure_fingerprint") == fingerprint
        )
        + 1
    )
    number = len(prior_controls) + 1
    blocked = (
        not transient
        or same_fingerprint >= MAX_CONTROL_FAILURES_PER_FINGERPRINT
        or number >= MAX_CONTROL_FAILURES_PER_SCOPE
    )
    return {
        "number": number,
        "same_fingerprint": same_fingerprint,
        "blocked": blocked,
        "retryable": not blocked,
    }


def prior_control_failures(
    root: Path,
    root_cause: str,
    scope_id: str,
    plan: dict[str, Any] | None = None,
) -> list[tuple[Path, dict[str, Any]]]:
    history_root = history_root_for(root, plan)
    if not history_root.is_dir():
        return []
    failures: list[tuple[Path, dict[str, Any]]] = []
    for path in history_root.glob("*/attempt_manifest.json"):
        try:
            value = read_json(path)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        if (
            isinstance(value, dict)
            and value.get("root_cause") == root_cause
            and value.get("attempt_kind") == "CONTROL_FAILURE"
            and value.get("control_scope_id") == scope_id
        ):
            validate_fixed_bundle(path.parent)
            failures.append((path.parent, value))
    return sorted(
        failures,
        key=lambda item: str(item[1].get("recorded_at", "")),
    )


def prior_failed_attempts(
    root: Path,
    root_cause: str,
    plan: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    history_root = history_root_for(root, plan)
    if not history_root.is_dir():
        return []
    attempts: list[dict[str, Any]] = []
    for path in history_root.glob("*/attempt_manifest.json"):
        try:
            value = read_json(path)
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        if not isinstance(value, dict) or value.get("root_cause") != root_cause:
            continue
        consumes_attempt = value.get("attempt_consumed")
        if consumes_attempt is None:
            # Backward compatibility: old bundles had no explicit attempt
            # kind. Only an archived, completed re-audit is a semantic attempt;
            # ROLLED_BACK control/setup failures never consume the budget.
            try:
                comparison = read_json(
                    path.parent / "re_audit_comparison.json"
                )
            except (OSError, ValueError, json.JSONDecodeError):
                comparison = {}
            consumes_attempt = (
                value.get("status")
                in {"PARTIALLY_REPAIRED", "ABANDONED"}
                and comparison.get("reaudit_count") == 1
                and isinstance(comparison.get("reaudit_audit_id"), str)
            )
        if (
            consumes_attempt is True
            and value.get("status")
            in {"ABANDONED", "PARTIALLY_REPAIRED"}
            and isinstance(value.get("attempt_number"), int)
            and value["attempt_number"] > 0
        ):
            validate_fixed_bundle(path.parent)
            attempts.append(value)
    return sorted(attempts, key=lambda item: item["attempt_number"])


def validate_fixed_bundle(directory: Path) -> None:
    missing = [
        name
        for name in REPAIR_BUNDLE_FILES
        if not (directory / name).is_file() or (directory / name).is_symlink()
    ]
    if missing:
        raise ValueError(f"incomplete fixed repair bundle: {missing}")
    values: dict[str, Any] = {}
    for name in REPAIR_BUNDLE_FILES:
        if name.endswith(".json"):
            try:
                values[name] = read_json(directory / name)
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(f"invalid fixed repair bundle file: {name}") from exc
    expected_types = {
        "repair_plan.json": dict,
        "changes.json": list,
        "unresolved.json": list,
        "regression_results.json": list,
        "re_audit_comparison.json": dict,
        "patch.json": dict,
        "evidence.json": list,
        "history.json": dict,
    }
    invalid_types = [
        name
        for name, expected in expected_types.items()
        if not isinstance(values.get(name), expected)
    ]
    if invalid_types:
        raise ValueError(f"fixed repair bundle has invalid types: {invalid_types}")
    history = values["history.json"]
    values["repair.log"] = (directory / "repair.log").read_text(
        encoding="utf-8"
    )
    validate_repair_bundle_semantics(
        values,
        repair_log=values["repair.log"],
    )
    if (
        history.get("bundle_complete") is not True
        or history.get("bundle_files") != list(REPAIR_BUNDLE_FILES)
    ):
        raise ValueError("fixed repair history.json does not attest completeness")
    expected_hashes = {
        name: sha256_file(directory / name)
        for name in REPAIR_BUNDLE_FILES
        if name != "history.json"
    }
    if history.get("bundle_hashes") != expected_hashes:
        raise ValueError("fixed repair bundle hashes are stale or incomplete")
    if history.get("bundle_digest") != canonical_json_hash(expected_hashes):
        raise ValueError("fixed repair bundle digest is stale")


def write_history_bundle(
    destination: Path,
    *,
    plan: dict[str, Any],
    changes: Any,
    unresolved: Any,
    regressions: Any,
    comparison: Any,
    evidence: Any,
    root_cause: str,
    attempt_number: int,
    status: str,
    decision: str,
    review_verdict: str,
    publishability: str,
) -> None:
    repair_status = (
        status if status in REPAIR_STATUSES else "ABANDONED"
    )
    canonical = canonical_fields(
        review_verdict,
        publishability=publishability,
        repair_decision=decision,
        repair_status=repair_status,
    )
    identity = {
        "audit_id": plan["audit_id"],
        "package_identity": plan["package_identity"],
    }
    if isinstance(plan.get("finding_id"), str) and plan["finding_id"]:
        identity["finding_id"] = plan["finding_id"]
    bundle_plan = {**plan, **canonical}
    bound_unresolved = [
        {**item, **identity} for item in unresolved
    ]
    bound_comparison = (
        {
            **comparison,
            **identity,
            "source_finding": {
                **comparison.get("source_finding", {}),
                **identity,
            },
        }
        if isinstance(comparison, dict) and comparison
        else comparison
    )
    write_json(destination / "repair_plan.json", bundle_plan)
    write_json(destination / "changes.json", changes)
    write_json(destination / "unresolved.json", bound_unresolved)
    write_json(destination / "regression_results.json", regressions)
    write_json(destination / "re_audit_comparison.json", bound_comparison)
    write_json(
        destination / "patch.json",
        {
            "schema_version": "0.1",
            "files": changes,
            "atomic_publish": status in SUCCESS_REPAIR_STATUSES,
        },
    )
    evidence_items = (
        list(evidence.values()) if isinstance(evidence, dict) else list(evidence)
    )
    if not evidence_items:
        reason = (
            unresolved[0].get("reason")
            if isinstance(unresolved, list)
            and unresolved
            and isinstance(unresolved[0], dict)
            else "No admissible repair evidence was available."
        )
        evidence_items = [
            {
                "evidence_id": "CONTROL-STOP",
                "source": "repair-policy",
                "status": "UNAVAILABLE",
                "reason": reason,
            }
        ]
    evidence_items = [{**item, **identity} for item in evidence_items]
    write_json(destination / "evidence.json", evidence_items)
    (destination / "repair.log").write_text(
        f"{timestamp()}\tINFO\tdecision={decision}\tstatus={status}"
        f"\trepair_status={repair_status}\n",
        encoding="utf-8",
    )
    bundle_hashes = {
        name: sha256_file(destination / name)
        for name in REPAIR_BUNDLE_FILES
        if name != "history.json"
    }
    write_json(
        destination / "history.json",
        {
            **canonical,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "status": status,
            "decision": decision,
            **identity,
            "bundle_files": list(REPAIR_BUNDLE_FILES),
            "bundle_complete": True,
            "bundle_hashes": bundle_hashes,
            "bundle_digest": canonical_json_hash(bundle_hashes),
        },
    )
    validate_fixed_bundle(destination)


def record_control_stop(
    root: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
    root_cause: str,
    stop: PolicyStop,
) -> dict[str, Any]:
    repair_id = unique_id("repair-stop")
    history_root = history_root_for(root, plan)
    destination = history_root / repair_id
    destination.mkdir(parents=True)
    write_history_bundle(
        destination,
        plan=plan,
        changes=[],
        unresolved=[{"finding_id": plan.get("finding_id"), "reason": stop.reason}],
        regressions=[],
        comparison={},
        evidence=plan.get("evidence", []),
        root_cause=root_cause,
        attempt_number=0,
        status=stop.status,
        decision="ABANDON",
        review_verdict=report.get(
            "review_verdict", report.get("summary", {}).get("final_verdict")
        ),
        publishability=canonical_publish_route(report),
    )
    manifest = {
        "schema_version": "0.1",
        **canonical_fields(
            report.get(
                "review_verdict", report.get("summary", {}).get("final_verdict")
            ),
            publishability=canonical_publish_route(report),
            repair_decision="ABANDON",
            repair_status="ABANDONED",
        ),
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
        **terminal_fields(
            "ABANDONED",
            source_verdict=report.get("summary", {}).get("final_verdict"),
        ),
        **{
            key: manifest[key]
            for key in (
                "review_verdict",
                "publishability",
                "repair_decision",
                "repair_status",
            )
        },
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
    canonical = canonical_fields(
        manifest["review_verdict"],
        publishability=manifest["publishability"],
        repair_decision=manifest["repair_decision"],
        repair_status=manifest["repair_status"],
    )
    manifest.update(canonical)
    identity = {
        "audit_id": manifest["source_audit_id"],
        "package_identity": manifest["package_identity"],
    }
    if isinstance(manifest.get("finding_id"), str) and manifest["finding_id"]:
        identity["finding_id"] = manifest["finding_id"]
    bound_plan = {**plan, **canonical, **identity}
    bound_evidence = [
        {**item, **identity} for item in manifest.get("evidence", [])
    ]
    comparison = manifest.get("re_audit_comparison", {})
    bound_comparison = {
        **comparison,
        **identity,
        "source_finding": {
            **comparison.get("source_finding", {}),
            **identity,
        },
    }
    manifest["evidence"] = bound_evidence
    manifest["re_audit_comparison"] = bound_comparison
    write_json(report_dir / "repair_manifest.json", manifest)
    write_json(report_dir / "repair_report.json", manifest)
    write_json(report_dir / "repair_plan.json", bound_plan)
    write_json(report_dir / "changes.json", manifest.get("changes", []))
    write_json(report_dir / "unresolved.json", manifest.get("unresolved", []))
    write_json(
        report_dir / "regression_results.json",
        manifest.get("regression_tests", []),
    )
    write_json(
        report_dir / "re_audit_comparison.json",
        bound_comparison,
    )
    write_json(
        report_dir / "patch.json",
        {
            "schema_version": "0.1",
            "files": manifest.get("changes", []),
            "atomic_publish": manifest.get("atomic_publish", False),
        },
    )
    write_json(report_dir / "evidence.json", bound_evidence)
    write_json(
        report_dir / "history.json",
        {
            **canonical,
            "root_cause": manifest.get("root_cause"),
            "attempt_number": manifest.get("attempt_number"),
            "status": manifest.get("status"),
            "decision": manifest.get("decision"),
            **identity,
            "history_dir": str(history_dir),
            "snapshot_preserved": True,
            "bundle_files": list(REPAIR_BUNDLE_FILES),
            "bundle_complete": True,
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
    bundle_hashes = {
        name: sha256_file(report_dir / name)
        for name in REPAIR_BUNDLE_FILES
        if name != "history.json"
    }
    history = read_json(report_dir / "history.json")
    history["bundle_hashes"] = bundle_hashes
    history["bundle_digest"] = canonical_json_hash(bundle_hashes)
    write_json(report_dir / "history.json", history)
    validate_fixed_bundle(report_dir)


V11_DIMENSION_KEYS = ("C01", "C02", "C03", "C04", "C05", "C06", "C07")


def batch_root_cause(report: dict[str, Any], plan: dict[str, Any]) -> str:
    finding_ids = sorted(
        str(finding.get("finding_id"))
        for finding in plan.get("findings", [])
        if isinstance(finding, dict)
    )
    value = f"{report['audit_id']}:batch:" + ",".join(finding_ids)
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:20]


def build_fplan(plan: dict[str, Any], finding: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "0.1",
        "audit_id": plan["audit_id"],
        "finding_id": finding["finding_id"],
        "deterministic_check": finding.get("deterministic_check"),
        "finding_code": finding.get(
            "finding_code", finding.get("title", finding.get("code"))
        ),
        "primary_finding_id": finding.get(
            "primary_finding_id", plan.get("primary_finding_id")
        ),
        "repair_scope": finding.get(
            "repair_scope", plan.get("repair_scope")
        ),
        "repair_class": finding["repair_class"],
        "justification": finding["justification"],
        "core_science_change": finding.get(
            "core_science_change", plan.get("core_science_change", False)
        ),
        "evidence": finding.get("evidence", []),
        "operations": finding.get("operations", []),
        "regression_tests": finding.get("regression_tests", []),
        "source_audit": plan.get("source_audit"),
        "core_contract_digest": plan.get("core_contract_digest"),
        "package_identity": plan.get("package_identity"),
        "agent_assessment": plan.get("agent_assessment"),
        "source_audit_dir": plan.get("source_audit_dir"),
        "repair_output_dir": plan.get("repair_output_dir"),
    }


def deterministic_binding_view(plan: dict[str, Any]) -> dict[str, Any]:
    """Represent proof-bound D6 consequences by their source queue class."""

    view = json.loads(json.dumps(plan))
    findings = {
        item.get("finding_id"): item
        for item in view.get("findings", [])
        if isinstance(item, dict)
    }
    for item in findings.values():
        if (
            item.get("deterministic_check") != "D6"
            or item.get("repair_class") != "AUTO_FIX"
        ):
            continue
        primary_ids = {
            operation.get("primary_finding_id")
            for operation in item.get("operations", [])
            if isinstance(operation, dict)
        }
        primary = findings.get(next(iter(primary_ids), None))
        if (
            len(primary_ids) == 1
            and primary is not None
            and primary.get("deterministic_check") in {"D3", "D4"}
            and primary.get("repair_class") == "AUTO_FIX"
        ):
            item["repair_class"] = "ASSISTED_FIX"
    return view


def validate_source_audit_binding_batch(
    root: Path,
    report: dict[str, Any],
    manifest: dict[str, Any],
    plan: dict[str, Any],
) -> dict[str, Any]:
    """Audit-level binding for a batch plan (no single finding_id)."""

    source_audit = plan.get("source_audit")
    if not isinstance(source_audit, dict):
        raise PolicyStop(
            "BLOCKED_EVIDENCE", "Repair requires a complete source-audit binding."
        )
    expected_audit_id = report.get("audit_id")
    if (
        source_audit.get("audit_id") != expected_audit_id
        or source_audit.get("audit_id") != manifest.get("audit_id")
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source audit identity is not bound to the authoritative audit",
        )
    input_hashes = manifest.get("input_hashes")
    if not isinstance(input_hashes, dict) or not input_hashes:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit lacks complete package input hashes",
        )
    bound_input_hashes = (
        source_audit.get("input_hashes")
        or source_audit.get("package_hashes")
        or source_audit.get("source_hashes")
    )
    if bound_input_hashes != input_hashes:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "source audit package hashes differ from the authoritative audit",
        )
    configuration = report.get("configuration")
    if not isinstance(configuration, dict):
        raise PolicyStop(
            "BLOCKED_EVIDENCE", "authoritative audit lacks configuration"
        )
    if (
        source_audit.get("review_lane") != REVIEW_LANE
        or configuration.get("review_lane") != REVIEW_LANE
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "Repair source audit and re-audit must use review_lane='dual'",
        )
    digest = core_contract_digest(root)
    bound_digest = source_audit.get("core_contract_digest")
    if bound_digest is None and isinstance(source_audit.get("core_contract"), dict):
        bound_digest = source_audit["core_contract"].get("digest")
    if (
        plan.get("core_contract_digest") != digest
        or bound_digest != digest
        or manifest.get("core_contract_digest") != digest
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "frozen core-contract digest is stale or incomplete",
        )
    external_binding_hashes(root, plan, manifest)
    if plan.get("deterministic_contract") is not None:
        try:
            validate_deterministic_contract(report.get("deterministic_contract"))
            validate_deterministic_plan_binding(
                report, deterministic_binding_view(plan)
            )
        except ValueError as exc:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"deterministic repair binding is invalid: {exc}",
            ) from exc
    return source_audit


def validate_fresh_audit_batch(
    root: Path,
    plan: dict[str, Any],
    attestation_path: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]]]:
    audit = source_audit_dir(root, plan)
    validate_audit_attestation(root, audit, attestation_path)
    report = read_json(audit / "audit_report.json")
    manifest = read_json(audit / "audit_manifest.json")
    disposition = read_json(audit / "disposition.json")
    authenticate_audit_bundle(
        root, report, manifest, disposition, audit=audit
    )
    report_configuration(report)
    if plan["audit_id"] != report.get("audit_id"):
        raise ValueError("stale audit: plan audit_id is not authoritative")
    if any(
        finding.get("repair_class") != "ABANDON"
        for finding in plan.get("findings", [])
        if isinstance(finding, dict)
    ):
        enforce_source_score_gate(report)
    route = disposition.get("route") or canonical_publish_route(report)
    if route != "REPAIR_QUEUE":
        raise ValueError("authoritative audit is not routed to REPAIR_QUEUE")
    findings_by_id = {
        item.get("finding_id"): item
        for item in report.get("findings", [])
        if isinstance(item, dict) and isinstance(item.get("finding_id"), str)
    }
    for finding in plan["findings"]:
        source_finding = findings_by_id.get(finding["finding_id"])
        if source_finding is not None:
            enforce_repair_lane_boundary(finding, source_finding, report)
        if (
            finding.get("repair_class") != "ABANDON"
            and (
                finding["finding_id"] not in findings_by_id
                or findings_by_id[finding["finding_id"]].get("status")
                != "OPEN"
            )
        ):
            raise ValueError(
                f"repair plan finding is not open in the audit: "
                f"{finding['finding_id']}"
            )
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
    validate_source_audit_binding_batch(root, report, manifest, plan)
    return report, manifest, findings_by_id


def operation_primary_finding(
    fplan: dict[str, Any], operation: dict[str, Any]
) -> str | None:
    value = operation.get("primary_finding_id")
    if value is None:
        value = fplan.get("primary_finding_id")
    return value if isinstance(value, str) and value else None


def is_shared_operation_reference(
    fplan: dict[str, Any], operation: dict[str, Any]
) -> bool:
    primary = operation_primary_finding(fplan, operation)
    return primary is not None and primary != fplan.get("finding_id")


def check_operation_policy(
    root: Path,
    operation: dict[str, Any],
    evidence: dict[str, dict[str, Any]],
    hidden_fragments: set[str],
    repair_class: str,
    *,
    deterministic_check: str | None = None,
    finding_code: str | None = None,
    deterministic_evidence: dict[str, Any] | None = None,
    repair_scope: str | None = None,
    shared_operation_reference: bool = False,
) -> None:
    """Per-operation evidence-precision policy (raises PolicyStop on failure)."""

    linked = linked_evidence(operation, evidence)
    _, relative = repair_target(root, operation["file"])
    structural_auto_fix = (
        repair_class == "AUTO_FIX"
        and deterministic_check in {"D1", "D2"}
        and is_structural_auto_fix_operation(operation)
    )
    proof_bound_auto_fix = is_proof_bound_d3_d4_auto_fix(
        repair_class,
        deterministic_check,
        finding_code,
        deterministic_evidence,
    )
    if shared_operation_reference and repair_class != "AUTO_FIX":
        raise PolicyStop(
            "POLICY_VIOLATION",
            "shared operation references must remain AUTO_FIX",
        )
    if structural_auto_fix:
        error = structural_auto_fix_operation_error(
            operation,
            (deterministic_evidence or {}).get(
                "source_bound_output_proof"
            ),
        )
        if error:
            raise PolicyStop("POLICY_VIOLATION", error)
    if (
        repair_class == "AUTO_FIX"
        and deterministic_check in {"D1", "D2"}
        and not structural_auto_fix
    ):
        raise PolicyStop(
            "POLICY_VIOLATION",
            "D1/D2 AUTO_FIX is limited to unambiguous output path/file "
            "synchronization.",
        )
    if (
        repair_class == "AUTO_FIX"
        and not structural_auto_fix
        and not shared_operation_reference
    ):
        try:
            if deterministic_check in {"D3", "D4"}:
                error = proof_bound_auto_fix_operation_error(
                    root,
                    {
                        "deterministic_check": deterministic_check,
                        "title": finding_code,
                        "evidence": deterministic_evidence or {},
                    },
                    operation,
                )
                if error:
                    raise ValueError(error)
            elif (
                deterministic_check == "D6"
                and repair_scope == "UNIQUE_SCORING_WIRING"
            ):
                checker_path = root / "tests/checker.py"
                checker_source = (
                    checker_path.read_text(encoding="utf-8")
                    if checker_path.is_file()
                    else ""
                )
                error = unique_wiring_auto_fix_operation_error(
                    {
                        "deterministic_check": deterministic_check,
                        "title": finding_code,
                        "evidence": deterministic_evidence or {},
                    },
                    operation,
                    checker_source,
                )
                if error:
                    raise ValueError(error)
            elif deterministic_check == "D5":
                validate_auto_fix_operation(
                    root,
                    operation,
                    finding_code
                    or ("PARSE_ERROR" if deterministic_check == "D5" else None),
                )
        except ValueError as exc:
            raise PolicyStop("POLICY_VIOLATION", str(exc)) from exc
    if relative.parts and relative.parts[0] != "solution" and any(
        item.get("source_category") == "solution_oracle" for item in linked
    ):
        raise PolicyStop(
            "POLICY_VIOLATION",
            "Oracle/solution content cannot support public or checker "
            "contract changes.",
        )
    if relative.as_posix() == "instruction.md":
        addition = proposed_text(operation)
        if any(fragment in addition for fragment in hidden_fragments):
            raise PolicyStop(
                "POLICY_VIOLATION",
                "Repair would leak hidden solution content into instruction.md.",
            )
    if not (
        repair_class == "AUTO_FIX"
        and (proof_bound_auto_fix or shared_operation_reference)
    ) and not structural_auto_fix:
        validate_precision_matrix(
            operation,
            linked,
            repair_class,
            repair_scope,
        )
    expected_precision = precision_kind_for(operation)
    allowed_categories = (
        {
            "audit_finding",
            "public_instruction",
            "checker_contract",
            "paper",
            "direct_source",
            "authoritative_primary_web",
        }
        if structural_auto_fix
        else {
            "public_instruction",
            "paper",
            "direct_source",
            "authoritative_primary_web",
        }
        if expected_precision == "scientific_method"
        else {
            "audit_finding",
            "public_instruction",
            "checker_contract",
            "paper",
            "direct_source",
        }
    )
    if any(
        item.get("source_category") not in allowed_categories for item in linked
    ):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "Evidence source role cannot support this scientific/schema/"
            "scoring change.",
        )
    if relative.as_posix() == "instruction.md" and not structural_auto_fix and any(
        Path(str(item["source"])).parts[:1] == ("solution",) for item in linked
    ):
        raise PolicyStop(
            "POLICY_VIOLATION",
            "Solution content cannot be evidence for public instruction.",
        )


def classify_finding(
    root: Path,
    report: dict[str, Any],
    manifest: dict[str, Any],
    fplan: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """Classify one finding's operations without blocking siblings.

    Returns ``(evidence, valid_operations, blocked_operations)``.  Raises
    ``PolicyStop`` for finding-level violations that block the whole finding.
    """

    if fplan.get("core_science_change") is not False:
        raise PolicyStop(
            "POLICY_VIOLATION",
            "Plan must declare core_science_change=false; Repair may not "
            "redefine the Harbor package's core science.",
        )
    evidence = evidence_index(root, report, manifest, fplan)
    hidden_fragments = solution_fragments(root)
    target_roles: set[str] = set()
    for operation in fplan["operations"]:
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
        if relative.parts and relative.parts[0] == "solution":
            hidden_fragments.update(
                line.strip()
                for line in proposed_text(operation).splitlines()
                if len(line.strip()) >= 12
            )
    if (
        fplan["repair_class"] == "AUTO_FIX"
        and target_roles & {"instruction", "tests"}
        and not (
            (
                fplan.get("deterministic_check") == "D6"
                and fplan.get("repair_scope") == "UNIQUE_SCORING_WIRING"
            )
            or (
                fplan.get("deterministic_check") in {"D1", "D2"}
                and bool(fplan["operations"])
                and all(
                    is_structural_auto_fix_operation(operation)
                    for operation in fplan["operations"]
                )
            )
            or (
                all(
                    is_proof_bound_d3_d4_auto_fix(
                        fplan["repair_class"],
                        fplan.get("deterministic_check"),
                        fplan.get("finding_code"),
                        fplan.get("deterministic_evidence"),
                    )
                    or is_shared_operation_reference(fplan, operation)
                    for operation in fplan["operations"]
                )
                and bool(fplan["operations"])
            )
        )
    ):
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
    valid_operations: list[dict[str, Any]] = []
    blocked_operations: list[dict[str, Any]] = []
    for operation in fplan["operations"]:
        try:
            check_operation_policy(
                root,
                operation,
                evidence,
                hidden_fragments,
                fplan["repair_class"],
                deterministic_check=fplan.get("deterministic_check"),
                finding_code=fplan.get("finding_code"),
                deterministic_evidence=fplan.get("deterministic_evidence"),
                repair_scope=fplan.get("repair_scope"),
                shared_operation_reference=is_shared_operation_reference(
                    fplan, operation
                ),
            )
        except PolicyStop as stop:
            blocked_operations.append(
                {
                    "operation_id": operation["id"],
                    "reason": f"{stop.status}: {stop.reason}",
                }
            )
            continue
        valid_operations.append(operation)
    return evidence, valid_operations, blocked_operations


def _operation_semantics(operation: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in operation.items()
        if key not in {"id", "evidence_ids", "primary_finding_id"}
    }


def shared_operation_is_safe(
    owner_fplan: dict[str, Any],
    owner_operation: dict[str, Any],
    consequence_fplan: dict[str, Any],
    consequence_operation: dict[str, Any],
) -> bool:
    """Allow only an explicitly owned, identical proof-bound operation."""

    if (
        owner_fplan.get("repair_class") != "AUTO_FIX"
        or consequence_fplan.get("repair_class") != "AUTO_FIX"
        or owner_fplan.get("deterministic_check") not in {"D3", "D4"}
        or consequence_fplan.get("deterministic_check")
        not in {"D3", "D4", "D6"}
    ):
        return False
    owner_id = owner_fplan.get("finding_id")
    primary_id = operation_primary_finding(
        consequence_fplan, consequence_operation
    )
    if not isinstance(owner_id, str) or primary_id != owner_id:
        return False
    owner_primary = operation_primary_finding(owner_fplan, owner_operation)
    if owner_primary not in {None, owner_id}:
        return False
    return _operation_semantics(owner_operation) == _operation_semantics(
        consequence_operation
    )


def compute_repair_delta(
    before: dict[str, Any], after: dict[str, Any]
) -> dict[str, Any]:
    def dims(report: dict[str, Any]) -> dict[str, Any]:
        summary = report.get("summary", {}) if isinstance(report, dict) else {}
        value = summary.get("dimensions_v11") or report.get("dimensions_v11")
        if isinstance(value, dict):
            return value
        if isinstance(value, list):
            return {
                item["dimension"]: item
                for item in value
                if isinstance(item, dict) and item.get("dimension")
            }
        return {}

    before_dims = dims(before)
    after_dims = dims(after)
    delta: dict[str, Any] = {}
    for key in V11_DIMENSION_KEYS:
        before_value = (before_dims.get(key) or {}).get("normalized")
        after_value = (after_dims.get(key) or {}).get("normalized")
        delta_pp = (
            round(after_value - before_value, 4)
            if isinstance(before_value, (int, float))
            and isinstance(after_value, (int, float))
            else None
        )
        delta[key] = {
            "before_normalized": before_value,
            "after_normalized": after_value,
            "delta_pp": delta_pp,
        }
    return delta


def archive_batch_attempt(
    *,
    root: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
    root_cause: str,
    attempt_number: int,
    repair_state: str,
    decision: str,
    changes: list[dict[str, Any]],
    unresolved: list[dict[str, Any]],
    regressions: list[dict[str, Any]],
    comparison: dict[str, Any],
    evidence: list[dict[str, Any]],
    reason: str,
    history_dir: Path | None = None,
    source_verdict: str | None = None,
    attempt_kind: str = "CONTROL",
    attempt_consumed: bool = False,
    control_failure: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Archive a non-publishing batch attempt and return its result payload."""

    repair_id = history_dir.name if history_dir is not None else unique_id("repair")
    destination = history_dir or (history_root_for(root, plan) / repair_id)
    destination.mkdir(parents=True, exist_ok=True)
    review_verdict = report.get(
        "review_verdict", report.get("summary", {}).get("final_verdict")
    )
    publishability = canonical_publish_route(report)
    write_history_bundle(
        destination,
        plan=plan,
        changes=changes,
        unresolved=unresolved or [{"finding_id": "__batch__", "reason": reason}],
        regressions=regressions,
        comparison=comparison,
        evidence=evidence,
        root_cause=root_cause,
        attempt_number=attempt_number,
        status=repair_state,
        decision=decision,
        review_verdict=review_verdict,
        publishability=publishability,
    )
    control_fields = (
        {
            "control_scope_id": control_failure.get("scope_id"),
            "control_failure_fingerprint": control_failure.get("fingerprint"),
            "control_failure_number": control_failure.get("number"),
            "control_failure_same_fingerprint": control_failure.get(
                "same_fingerprint"
            ),
            "retryable": control_failure.get("retryable"),
        }
        if isinstance(control_failure, dict)
        else {}
    )
    write_json(
        destination / "attempt_manifest.json",
        {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "attempt_kind": attempt_kind,
            "attempt_consumed": attempt_consumed,
            **control_fields,
            "status": repair_state,
            "decision": decision,
            "audit_id": report["audit_id"],
            "finding_ids": [
                finding.get("finding_id") for finding in plan.get("findings", [])
            ],
            "package_mutated": False,
            "reason": reason,
            "recorded_at": timestamp(),
        },
    )
    return {
        "repair_id": repair_id,
        "status": repair_state,
        "decision": decision,
        **terminal_fields(repair_state, source_verdict=source_verdict),
        "root_cause": root_cause,
        "attempt_number": attempt_number,
        "attempt_kind": attempt_kind,
        "attempt_consumed": attempt_consumed,
        **control_fields,
        "history_root": str(history_root_for(root, plan)),
        "history_dir": str(destination),
        "attempt_manifest": str(destination / "attempt_manifest.json"),
        "unresolved": unresolved,
        "repair_delta": comparison.get("repair_delta")
        if isinstance(comparison, dict)
        else None,
        "reason": reason,
    }


def existing_infrastructure_block(
    history_dir: Path,
    manifest: dict[str, Any],
    *,
    source_verdict: str | None,
) -> dict[str, Any]:
    return {
        "repair_id": manifest.get("repair_id"),
        "status": "INFRASTRUCTURE_BLOCKED",
        "decision": "ASSISTED_FIX",
        **terminal_fields(
            "INFRASTRUCTURE_BLOCKED",
            source_verdict=source_verdict,
        ),
        "root_cause": manifest.get("root_cause"),
        "attempt_number": manifest.get("attempt_number", 0),
        "attempt_kind": "CONTROL_FAILURE",
        "attempt_consumed": False,
        "control_scope_id": manifest.get("control_scope_id"),
        "control_failure_fingerprint": manifest.get(
            "control_failure_fingerprint"
        ),
        "control_failure_number": manifest.get("control_failure_number"),
        "control_failure_same_fingerprint": manifest.get(
            "control_failure_same_fingerprint"
        ),
        "retryable": False,
        "history_root": str(history_dir.parent),
        "history_dir": str(history_dir),
        "attempt_manifest": str(history_dir / "attempt_manifest.json"),
        "unresolved": read_json(history_dir / "unresolved.json"),
        "repair_delta": None,
        "reason": manifest.get("reason"),
    }


def repair_batch(
    root: Path,
    plan: dict[str, Any],
    attestation_path: Path,
) -> dict[str, Any]:
    plan["package_identity"] = package_identity(root)
    try:
        report, audit_manifest, findings_by_id = validate_fresh_audit_batch(
            root, plan, attestation_path
        )
    except PolicyStop as stop:
        report = read_json(source_audit_dir(root, plan) / "audit_report.json")
        root_cause = batch_root_cause(report, plan)
        return archive_batch_attempt(
            root=root,
            report=report,
            plan=plan,
            root_cause=root_cause,
            attempt_number=0,
            repair_state="ABANDONED",
            decision="ABANDON",
            changes=[],
            unresolved=[
                {"finding_id": "__batch__", "reason": f"{stop.status}: {stop.reason}"}
            ],
            regressions=[],
            comparison={},
            evidence=[],
            reason=f"{stop.status}: {stop.reason}",
        )
    root_cause = batch_root_cause(report, plan)
    source_verdict = report.get("summary", {}).get("final_verdict")
    prior = prior_failed_attempts(root, root_cause, plan)
    if len(prior) >= 2 or any(item["status"] == "ABANDONED" for item in prior):
        return archive_batch_attempt(
            root=root,
            report=report,
            plan=plan,
            root_cause=root_cause,
            attempt_number=len(prior),
            repair_state="ABANDONED",
            decision="ABANDON",
            changes=[],
            unresolved=[
                {
                    "finding_id": "__batch__",
                    "reason": "Two failed batch attempts exhausted the limit.",
                }
            ],
            regressions=[],
            comparison={},
            evidence=[],
            reason="Two failed batch attempts exhausted the root-cause limit.",
            source_verdict=source_verdict,
        )
    scope_id = control_scope_id(report)
    prior_controls = prior_control_failures(
        root, root_cause, scope_id, plan
    )
    blocked_control = next(
        (
            (path, manifest)
            for path, manifest in reversed(prior_controls)
            if manifest.get("status") == "INFRASTRUCTURE_BLOCKED"
            or manifest.get("retryable") is False
        ),
        None,
    )
    if blocked_control is not None:
        return existing_infrastructure_block(
            blocked_control[0],
            blocked_control[1],
            source_verdict=source_verdict,
        )

    abandoned: list[dict[str, Any]] = []
    blocked: list[dict[str, Any]] = []
    resolved_targets: list[str] = []
    valid_ops: list[dict[str, Any]] = []
    operation_owners: dict[
        str, tuple[dict[str, Any], dict[str, Any]]
    ] = {}
    planned_regressions: list[dict[str, Any]] = []
    evidence_all: dict[str, dict[str, Any]] = {}
    for finding in plan["findings"]:
        finding_id = finding["finding_id"]
        fplan = build_fplan(plan, finding)
        if finding["repair_class"] == "ABANDON":
            abandoned.append(
                {"finding_id": finding_id, "reason": finding["justification"]}
            )
            continue
        finding_obj = findings_by_id.get(finding_id)
        if finding_obj is None or finding_obj.get("status") != "OPEN":
            blocked.append(
                {
                    "finding_id": finding_id,
                    "reason": "finding is not OPEN in the authoritative audit",
                }
            )
            continue
        fplan["deterministic_evidence"] = dict(
            finding_obj.get("evidence", {})
            if isinstance(finding_obj.get("evidence"), dict)
            else {}
        )
        if finding.get("deterministic_check") in {"D1", "D2"}:
            fplan["deterministic_evidence"]["source_bound_output_proof"] = (
                output_repair_proof(report.get("contract_map"))
            )
        try:
            evidence, finding_valid_ops, finding_blocked_ops = classify_finding(
                root, report, audit_manifest, fplan
            )
        except PolicyStop as stop:
            blocked.append(
                {
                    "finding_id": finding_id,
                    "reason": f"{stop.status}: {stop.reason}",
                }
            )
            continue
        for blocked_op in finding_blocked_ops:
            blocked.append(
                {
                    "finding_id": finding_id,
                    "operation_id": blocked_op["operation_id"],
                    "reason": blocked_op["reason"],
                }
            )
        if not finding_valid_ops:
            blocked.append(
                {
                    "finding_id": finding_id,
                    "reason": "all operations were blocked by evidence precision",
                }
            )
            continue
        valid_ids: set[str] = set()
        for operation in finding_valid_ops:
            for evidence_id in operation.get("evidence_ids", []):
                evidence_all[evidence_id] = evidence[evidence_id]
            operation_id = operation["id"]
            owner = operation_owners.get(operation_id)
            if owner is None:
                operation_owners[operation_id] = (fplan, operation)
                valid_ops.append(operation)
                valid_ids.add(operation_id)
                continue
            owner_fplan, owner_operation = owner
            if shared_operation_is_safe(
                owner_fplan, owner_operation, fplan, operation
            ):
                # The primary proof-bound operation is applied once.  The
                # consequence finding still gets its own causal regression and
                # remains a targeted re-audit closure requirement.
                valid_ids.add(operation_id)
                continue
            blocked.append(
                {
                    "finding_id": finding_id,
                    "operation_id": operation_id,
                    "reason": (
                        "POLICY_VIOLATION: duplicate operation id is not an "
                        "identical, explicitly owned proof-bound consequence"
                    ),
                }
            )
        for specification in fplan["regression_tests"]:
            causal = specification.get("causal_operation_ids", [])
            if set(causal).issubset(valid_ids):
                planned_regressions.append(specification)
        if valid_ids:
            resolved_targets.append(finding_id)
        else:
            blocked.append(
                {
                    "finding_id": finding_id,
                    "reason": "all operations were blocked by operation ownership",
                }
            )

    unresolved_findings = blocked + abandoned
    if not valid_ops:
        return archive_batch_attempt(
            root=root,
            report=report,
            plan=plan,
            root_cause=root_cause,
            attempt_number=len(prior) + 1,
            repair_state="ABANDONED",
            decision="ABANDON",
            changes=[],
            unresolved=unresolved_findings
            or [{"finding_id": "__batch__", "reason": "No fixable operations."}],
            regressions=[],
            comparison={},
            evidence=list(evidence_all.values()),
            reason="No fixable operations in the batch.",
            source_verdict=source_verdict,
        )

    attempt_number = len(prior) + 1
    repair_id = unique_id("repair")
    workspace = root.parent / ".benchmark_repair_tmp" / repair_id
    history = history_root_for(root, plan) / repair_id
    if workspace.exists() or history.exists():
        raise FileExistsError("repair workspace already exists")
    workspace.parent.mkdir(exist_ok=True)
    workspace.mkdir()
    snapshot = workspace / "snapshot"
    candidate = workspace / "candidate"
    identity = package_identity(root)
    # Explicit sentinel: ``regression_results`` is a function-local for the
    # whole scope, so gate the rollback branch on an unambiguous ``is not None``
    # test rather than fragile ``in dir()`` introspection.
    regression_results: list[dict[str, Any]] | None = None
    control_stage = "sandbox_preflight"
    try:
        ensure_command_regression_env(planned_regressions)
        control_stage = "workspace_setup"
        shutil.copytree(root, snapshot)
        shutil.copytree(snapshot, candidate)
        control_stage = "before_regressions"
        regression_results = run_regressions(
            snapshot, planned_regressions, "before"
        )
        control_stage = "apply_operations"
        changes = [apply_operation(candidate, operation) for operation in valid_ops]
        operation_files = {item["file"] for item in changes}
        assert_mutation_boundary(snapshot, candidate, operation_files)
        candidate_digest = core_contract_digest(candidate)
        control_stage = "after_regressions"
        run_regressions(
            candidate, planned_regressions, "after", regression_results
        )
        control_stage = "equal_depth_reaudit"
        reaudit = run_equal_depth_review(candidate, report, audit_manifest, plan)
        reaudit_score = authoritative_total_score(
            reaudit, context="re-audit"
        )
        reaudit_below_repair_gate = reaudit_score < MINIMUM_REPAIR_SCORE
        try:
            pass_evidence = validate_authoritative_pass(reaudit)
        except ValueError as exc:
            pass_evidence = {
                "authoritative_pass": False,
                "authoritative_pass_error": str(exc),
            }
        else:
            pass_evidence["authoritative_pass"] = True
        assert_mutation_boundary(snapshot, candidate, operation_files)
    except Exception as exc:  # noqa: BLE001
        # Setup, regression harness, apply, and Review invocation failures do
        # not constitute an authoritative semantic assessment. Preserve them
        # as control failures without consuming the two-attempt package budget.
        fingerprint = control_failure_fingerprint(
            exc, stage=control_stage, root=root
        )
        transient = control_failure_retryable(exc)
        control_decision = control_failure_decision(
            prior_controls,
            fingerprint,
            transient=transient,
        )
        blocked = control_decision["blocked"]
        repair_state = (
            "INFRASTRUCTURE_BLOCKED" if blocked else "ROLLED_BACK"
        )
        decision = "ASSISTED_FIX"
        history.mkdir(parents=True, exist_ok=True)
        if snapshot.exists():
            snapshot.rename(history / "snapshot")
        if candidate.exists():
            candidate.rename(history / "candidate")
        result = archive_batch_attempt(
            root=root,
            report=report,
            plan=plan,
            root_cause=root_cause,
            attempt_number=attempt_number,
            repair_state=repair_state,
            decision=decision,
            changes=[],
            unresolved=unresolved_findings
            + [{"finding_id": "__batch__", "reason": str(exc)}],
            regressions=(
                regression_results if regression_results is not None else []
            ),
            comparison={},
            evidence=list(evidence_all.values()),
            reason=str(exc),
            history_dir=history,
            source_verdict=source_verdict,
            attempt_kind="CONTROL_FAILURE",
            attempt_consumed=False,
            control_failure={
                "scope_id": scope_id,
                "fingerprint": fingerprint,
                "number": control_decision["number"],
                "same_fingerprint": control_decision[
                    "same_fingerprint"
                ],
                "retryable": control_decision["retryable"],
            },
        )
        if workspace.exists():
            shutil.rmtree(workspace, ignore_errors=True)
        return result

    summary = reaudit.get("summary", {})
    verdict = summary.get("final_verdict")
    # The publish route lives in disposition.json ``route`` (and the
    # finalizer's ``summary.publication_route`` / ``summary.publishability``).
    # ``summary.disposition`` holds the VERDICT, not the route, so it must not
    # be used here (mirrors read_ext_disposition and finalize_audit_output).
    reaudit_disposition_path = reaudit_audit_dir(candidate, plan) / "disposition.json"
    reaudit_disposition = (
        read_json(reaudit_disposition_path)
        if reaudit_disposition_path.is_file()
        else {}
    )
    route = (
        reaudit_disposition.get("route")
        or summary.get("publication_route")
        or summary.get("publishability")
    )
    reaudit_findings = [
        item for item in reaudit.get("findings", []) if isinstance(item, dict)
    ]
    unresolved_severe = unresolved_severe_finding_ids(reaudit_findings)
    # Every targeted finding must be absent/closed in the fresh re-audit before
    # the batch may publish (§8.4); mirrors the legacy single-finding closure
    # guard in validate_reaudit.
    reaudit_finding_keys = {
        finding_key(item) for item in reaudit_findings if finding_key(item)
    }
    targets_still_open = [
        finding_id
        for finding_id in resolved_targets
        if (target_key := finding_key(findings_by_id.get(finding_id, {})))
        is not None
        and target_key in reaudit_finding_keys
    ]
    reaudit_audit_id = reaudit.get("audit_id")
    residual_blocking = blocking_finding_references(
        reaudit_findings,
        audit_id=(
            reaudit_audit_id
            if isinstance(reaudit_audit_id, str)
            else None
        ),
    )
    has_fatal = any(
        item.get("severity") == "FATAL" for item in reaudit_findings
    ) or bool(summary.get("hard_gate"))
    require_deterministic = is_deterministic_repair_plan(plan)
    hard_gate_free = (
        reaudit_has_no_hard_gate(reaudit)
        if require_deterministic or "hard_gates" in reaudit
        else True
    )
    if not hard_gate_free:
        has_fatal = True
    deterministic_clean = False
    deterministic = None
    if isinstance(reaudit.get("deterministic_contract"), dict):
        try:
            deterministic = validate_deterministic_contract(
                reaudit["deterministic_contract"]
            )
        except (TypeError, ValueError):
            deterministic = None
        deterministic_clean = (
            deterministic is not None
            and deterministic["repair_summary"]["state"] == "CLEAN"
        )
    fully_passed = (
        not reaudit_below_repair_gate
        and verdict == "PASS"
        and route == "PUBLISH_CANDIDATE"
        and pass_evidence.get("authoritative_pass") is True
        and deterministic_clean
        and hard_gate_free
        and not unresolved_findings
        and not targets_still_open
        and not unresolved_severe
        and package_identity(candidate, directory_name=root.name) == identity
    )
    repair_delta = compute_repair_delta(report, reaudit)
    review_lane = report_configuration(reaudit)
    comparison = {
        "target_resolved": fully_passed,
        "reaudit_audit_id": reaudit.get("audit_id"),
        "reaudit_count": 1,
        "reaudit_verdict": verdict,
        "publication_route": route,
        "deterministic_state": (
            deterministic["repair_summary"]["state"]
            if deterministic is not None
            else "LEGACY_UNBOUND"
        ),
        "hard_gate_free": hard_gate_free,
        "identity_preserved": (
            package_identity(candidate, directory_name=root.name) == identity
        ),
        "mutation_scope_allowed": True,
        "residual_blocking_finding_ids": (
            [item["finding_id"] for item in residual_blocking]
        ),
        "residual_blocking_findings": residual_blocking,
        "unresolved_severe_finding_ids": unresolved_severe,
        "resolved_findings": resolved_targets,
        "unresolved_findings": unresolved_findings,
        "source_finding": {
            "finding_id": resolved_targets[0] if resolved_targets else None,
            "status": "OPEN",
        },
        "source_configuration": {"review_lane": report_configuration(report)},
        "reaudit_configuration": {"review_lane": review_lane},
        "repair_delta": repair_delta,
        "source_score": authoritative_total_score(
            report, context="source audit"
        ),
        "reaudit_score": reaudit_score,
        "repair_score_gate": (
            "ABANDONED"
            if reaudit_below_repair_gate
            else "ELIGIBLE"
        ),
        **pass_evidence,
    }

    if not fully_passed:
        if has_fatal or reaudit_below_repair_gate or attempt_number >= 2:
            repair_state = "ABANDONED"
            decision = "ABANDON"
        else:
            repair_state = "PARTIALLY_REPAIRED"
            decision = "ASSISTED_FIX"
        reaudit_unresolved = [
            {
                **item,
                "reason": "blocking finding remains after equal-depth re-audit",
            }
            for item in residual_blocking
        ]
        residual_codes = {
            item.get("finding_code") for item in residual_blocking
        }
        for source_finding_id in targets_still_open:
            source_key = finding_key(
                findings_by_id.get(source_finding_id, {})
            )
            if source_key in residual_codes:
                continue
            matching = next(
                (
                    item
                    for item in reaudit_findings
                    if finding_key(item) == source_key
                ),
                {},
            )
            reaudit_unresolved.append(
                {
                    **finding_reference(
                        matching,
                        audit_id=(
                            reaudit_audit_id
                            if isinstance(reaudit_audit_id, str)
                            else None
                        ),
                    ),
                    "source_finding_id": source_finding_id,
                    "reason": (
                        "targeted finding remains after equal-depth re-audit"
                    ),
                }
            )
        history.mkdir(parents=True, exist_ok=True)
        if snapshot.exists():
            snapshot.rename(history / "snapshot")
        if candidate.exists():
            candidate.rename(history / "candidate")
        result = archive_batch_attempt(
            root=root,
            report=report,
            plan=plan,
            root_cause=root_cause,
            attempt_number=attempt_number,
            repair_state=repair_state,
            decision=decision,
            changes=[],
            unresolved=unresolved_findings + reaudit_unresolved
            or [{"finding_id": "__batch__", "reason": "re-audit did not reach PASS"}],
            regressions=regression_results,
            comparison=comparison,
            evidence=list(evidence_all.values()),
            reason=(
                "Equal-depth re-audit did not reach PASS; the authoritative "
                "package is preserved unchanged."
            ),
            history_dir=history,
            source_verdict=source_verdict,
            attempt_kind="SEMANTIC_REAUDIT",
            attempt_consumed=True,
        )
        result["repair_delta"] = repair_delta
        if workspace.exists():
            shutil.rmtree(workspace, ignore_errors=True)
        return result

    # REPAIRED: full re-audit PASS with every batch finding resolved.
    repair_canonical = canonical_fields(
        "PASS",
        publishability="PUBLISH_CANDIDATE",
        repair_decision="ASSISTED_FIX",
        repair_status="REPAIRED",
    )
    repair_manifest = {
        "schema_version": "0.1",
        **repair_canonical,
        "repair_id": repair_id,
        "status": "REPAIRED",
        "decision": "ASSISTED_FIX",
        **terminal_fields("REPAIRED"),
        "root_cause": root_cause,
        "attempt_number": attempt_number,
        "max_attempts": 2,
        "attempt_kind": "SEMANTIC_REAUDIT",
        "attempt_consumed": True,
        "finding_id": None,
        "finding_ids": resolved_targets,
        "repair_class": "ASSISTED_FIX",
        "package_identity": identity,
        "source_audit_id": report["audit_id"],
        "source_audit_input_hashes": audit_manifest["input_hashes"],
        "source_audit_review_implementation": audit_manifest[
            "review_implementation"
        ],
        "source_audit_assessment_hashes": audit_manifest.get(
            "assessment_hashes", {}
        ),
        "core_contract_digest_before": plan["core_contract_digest"],
        "core_contract_digest_after": candidate_digest,
        "justification": "; ".join(
            finding["justification"] for finding in plan["findings"]
        ),
        "evidence": list(evidence_all.values()),
        "changes": changes,
        "regression_tests": regression_results,
        "unresolved": [],
        "re_audit_comparison": comparison,
        "repair_delta": repair_delta,
        "reaudit": {
            "audit_id": reaudit["audit_id"],
            "review_lane": review_lane,
            "verdict": verdict,
            "disposition": route,
        },
        "atomic_publish": True,
        "published_at": timestamp(),
    }
    rebase_audit_paths(candidate, root, plan)
    reaudit_report_path = reaudit_audit_dir(candidate, plan) / "audit_report.json"
    reaudit_manifest_path = reaudit_audit_dir(candidate, plan) / "audit_manifest.json"
    repair_manifest.update(
        {
            "reaudit_audit_id": reaudit["audit_id"],
            "reaudit_report_hash": sha256_file(reaudit_report_path),
            "reaudit_manifest_hash": sha256_file(reaudit_manifest_path),
        }
    )
    write_repair_reports(candidate, repair_manifest, plan, history)
    history.mkdir(parents=True)
    snapshot.rename(history / "snapshot")
    write_history_bundle(
        history,
        plan=plan,
        changes=changes,
        unresolved=[],
        regressions=regression_results,
        comparison=comparison,
        evidence=evidence_all,
        root_cause=root_cause,
        attempt_number=attempt_number,
        status="REPAIRED",
        decision="ASSISTED_FIX",
        review_verdict=repair_canonical["review_verdict"],
        publishability=repair_canonical["publishability"],
    )
    write_json(
        history / "attempt_manifest.json",
        {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "status": "REPAIRED",
            "decision": "ASSISTED_FIX",
            **repair_canonical,
            "audit_id": report["audit_id"],
            "finding_ids": resolved_targets,
            "error": None,
            "snapshot_preserved": True,
            "candidate_preserved": False,
            "recorded_at": timestamp(),
        },
    )
    generated_outputs = externalize_generated_bundles(candidate, root, plan)
    original = history / "original"
    root.rename(original)
    try:
        candidate.rename(root)
    except Exception:
        for name, external in generated_outputs.items():
            external_path = Path(external)
            if external_path.exists():
                external_path.rename(candidate / name)
        original.rename(root)
        raise
    shutil.rmtree(workspace, ignore_errors=True)
    return {
        "repair_id": repair_id,
        "status": "REPAIRED",
        "decision": "ASSISTED_FIX",
        **repair_canonical,
        **terminal_fields("REPAIRED"),
        "benchmark_root": str(root),
        "history_dir": str(history),
        "history_root": str(history_root_for(root, plan)),
        "root_cause": root_cause,
        "attempt_number": attempt_number,
        "audit_id": reaudit["audit_id"],
        "resolved_findings": resolved_targets,
        "repair_delta": repair_delta,
        "generated_outputs": generated_outputs,
    }


def repair(
    root: Path,
    plan_path: Path,
    attestation_path: Path,
    audit_dir: Path | None = None,
    repair_output_dir: Path | None = None,
) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.is_dir() or not (root / "instruction.md").is_file() or not (
        root / "tests"
    ).is_dir():
        raise ValueError("input must be a Harbor 题包 with instruction.md and tests/")
    plan = validate_external_plan(root, plan_path)
    if audit_dir is not None:
        plan["source_audit_dir"] = str(audit_dir.expanduser().resolve())
    if repair_output_dir is not None:
        plan["repair_output_dir"] = str(
            repair_output_dir.expanduser().resolve()
        )
    source_audit_dir(root, plan)
    repair_output_root(root, plan)
    plan["package_identity"] = package_identity(root)
    if isinstance(plan.get("findings"), list):
        return repair_batch(root, plan, attestation_path)
    try:
        report, audit_manifest, finding = validate_fresh_audit(
            root, plan, attestation_path
        )
    except PolicyStop as stop:
        report = read_json(source_audit_dir(root, plan) / "audit_report.json")
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
    prior = prior_failed_attempts(root, root_cause, plan)
    if len(prior) >= 2 or any(item["status"] == "ABANDONED" for item in prior):
        return {
            "status": "ABANDONED",
            "decision": "ABANDON",
            **canonical_fields(
                report.get(
                    "review_verdict",
                    report.get("summary", {}).get("final_verdict"),
                ),
                publishability=canonical_publish_route(report),
                repair_decision="ABANDON",
                repair_status="ABANDONED",
            ),
            "root_cause": root_cause,
            "history_root": str(history_root_for(root, plan)),
            "attempts": len(prior),
            "reason": "Two failed attempts exhausted the root-cause limit.",
        }
    try:
        evidence = validate_policy(root, report, audit_manifest, plan)
    except PolicyStop as stop:
        return record_control_stop(root, report, plan, root_cause, stop)

    ensure_command_regression_env(plan["regression_tests"])
    attempt_number = len(prior) + 1
    repair_id = unique_id("repair")
    workspace = root.parent / ".benchmark_repair_tmp" / repair_id
    history = history_root_for(root, plan) / repair_id
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
        run_regressions(
            candidate, plan["regression_tests"], "after", regression_tests
        )
        reaudit = run_equal_depth_review(candidate, report, audit_manifest, plan)
        reaudit_score = authoritative_total_score(
            reaudit, context="re-audit"
        )
        if reaudit_score < MINIMUM_REPAIR_SCORE:
            raise PolicyStop(
                "ABANDONED",
                f"re-audit total score {reaudit_score:g} is below "
                f"{MINIMUM_REPAIR_SCORE:g}; Repair cannot continue",
            )
        if reaudit_score < PUBLICATION_SCORE:
            raise PolicyStop(
                "PARTIALLY_REPAIRED",
                f"re-audit total score {reaudit_score:g} permits only a "
                "partial, non-published repair",
            )
        re_audit_comparison = validate_reaudit(candidate, reaudit, finding, report, plan,
            require_deterministic=is_deterministic_repair_plan(plan),
        )
        assert_mutation_boundary(snapshot, candidate, operation_files)
        if package_identity(candidate, directory_name=root.name) != identity:
            raise ValueError("repair changed the Harbor package identity")
        review_lane = report_configuration(reaudit)
        repair_canonical = canonical_fields(
            reaudit.get(
                "review_verdict",
                reaudit.get("summary", {}).get("final_verdict"),
            ),
            publishability=canonical_publish_route(reaudit),
            repair_decision=plan["repair_class"],
            repair_status="REPAIRED",
        )
        repair_manifest = {
            "schema_version": "0.1",
            **repair_canonical,
            **terminal_fields("REPAIRED"),
            "repair_id": repair_id,
            "status": "REPAIRED",
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
                "review_lane": review_lane,
                "verdict": reaudit["summary"]["final_verdict"],
                "disposition": reaudit["summary"].get("disposition"),
            },
            "atomic_publish": True,
            "published_at": timestamp(),
        }
        rebase_audit_paths(candidate, root, plan)
        reaudit_report_path = reaudit_audit_dir(candidate, plan) / "audit_report.json"
        reaudit_manifest_path = reaudit_audit_dir(candidate, plan) / "audit_manifest.json"
        repair_manifest.update(
            {
                "reaudit_audit_id": reaudit["audit_id"],
                "reaudit_report_hash": sha256_file(reaudit_report_path),
                "reaudit_manifest_hash": sha256_file(reaudit_manifest_path),
            }
        )
        write_repair_reports(candidate, repair_manifest, plan, history)

        history.mkdir(parents=True)
        snapshot.rename(history / "snapshot")
        write_history_bundle(
            history,
            plan=plan,
            changes=changes,
            unresolved=[],
            regressions=regression_tests,
            comparison=re_audit_comparison,
            evidence=evidence,
            root_cause=root_cause,
            attempt_number=attempt_number,
            status="REPAIRED",
            decision=plan["repair_class"],
            review_verdict=repair_canonical["review_verdict"],
            publishability=repair_canonical["publishability"],
        )
        attempt_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "status": "REPAIRED",
            "decision": plan["repair_class"],
            **repair_canonical,
            "audit_id": report["audit_id"],
            "finding_id": plan["finding_id"],
            "repair_class": plan["repair_class"],
            "error": None,
            "snapshot_preserved": True,
            "candidate_preserved": False,
            "recorded_at": timestamp(),
        }
        write_json(history / "attempt_manifest.json", attempt_manifest)
        generated_outputs = externalize_generated_bundles(
            candidate, root, plan
        )
        original = history / "original"
        root.rename(original)
        try:
            candidate.rename(root)
        except Exception:
            for name, external in generated_outputs.items():
                external_path = Path(external)
                if external_path.exists():
                    external_path.rename(candidate / name)
            original.rename(root)
            raise
        shutil.rmtree(workspace, ignore_errors=True)
        return {
            "repair_id": repair_id,
            "status": "REPAIRED",
            "decision": plan["repair_class"],
            **repair_canonical,
            **terminal_fields("REPAIRED"),
            "benchmark_root": str(root),
            "history_dir": str(history),
            "history_root": str(history_root_for(root, plan)),
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "audit_id": reaudit["audit_id"],
            "generated_outputs": generated_outputs,
        }
    except Exception as exc:  # noqa: BLE001
        policy_status = (
            exc.status
            if isinstance(exc, PolicyStop)
            and exc.status in {"ABANDONED", "PARTIALLY_REPAIRED"}
            else None
        )
        status = policy_status or (
            "ROLLED_BACK" if attempt_number == 1 else "ABANDONED"
        )
        decision = plan["repair_class"] if status == "ROLLED_BACK" else "ABANDON"
        failed_canonical = canonical_fields(
            report.get(
                "review_verdict",
                report.get("summary", {}).get("final_verdict"),
            ),
            publishability=canonical_publish_route(report),
            repair_decision=decision,
            repair_status=status,
        )
        history.mkdir(parents=True, exist_ok=True)
        if snapshot.exists():
            snapshot.rename(history / "snapshot")
        if candidate.exists():
            candidate.rename(history / "candidate")
        write_history_bundle(
            history,
            plan=plan,
            changes=changes if "changes" in locals() else [],
            unresolved=[{"finding_id": plan["finding_id"], "reason": str(exc)}],
            regressions=regression_tests if "regression_tests" in locals() else [],
            comparison=(
                re_audit_comparison if "re_audit_comparison" in locals() else {}
            ),
            evidence=evidence if "evidence" in locals() else [],
            root_cause=root_cause,
            attempt_number=attempt_number,
            status=status,
            decision=decision,
            review_verdict=failed_canonical["review_verdict"],
            publishability=failed_canonical["publishability"],
        )
        attempt_manifest = {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "status": status,
            "decision": decision,
            **failed_canonical,
            "audit_id": report["audit_id"],
            "finding_id": plan["finding_id"],
            "repair_class": plan["repair_class"],
            "attempt_consumed": status
            in {"PARTIALLY_REPAIRED", "ABANDONED"}
            and "reaudit" in locals(),
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
            **terminal_fields(
                status,
                source_verdict=report.get("summary", {}).get("final_verdict"),
            ),
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "history_dir": str(history),
            "history_root": str(history_root_for(root, plan)),
            "attempt_manifest": str(history / "attempt_manifest.json"),
            "reason": str(exc),
        }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Repair one audited materials-science Harbor 题包."
    )
    parser.add_argument("benchmark_root")
    parser.add_argument("--plan", required=True)
    parser.add_argument("--audit-attestation", required=True)
    parser.add_argument(
        "--audit-dir",
        help="authoritative source audit directory outside the Harbor 题包",
    )
    parser.add_argument(
        "--repair-output-dir",
        help="external directory for repair, re-audit, and history bundles",
    )
    arguments = parser.parse_args()
    try:
        result = repair(
            Path(arguments.benchmark_root),
            Path(arguments.plan),
            Path(arguments.audit_attestation),
            audit_dir=(
                Path(arguments.audit_dir) if arguments.audit_dir else None
            ),
            repair_output_dir=(
                Path(arguments.repair_output_dir)
                if arguments.repair_output_dir
                else None
            ),
        )
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["status"] == "REPAIRED" else 3
    except Exception as exc:  # noqa: BLE001
        print(f"materials repair failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
