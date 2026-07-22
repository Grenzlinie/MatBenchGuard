#!/usr/bin/env python3
"""Repair one audited Harbor package through an isolated atomic workflow."""

from __future__ import annotations

import argparse
import ast
from contextvars import ContextVar
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
    REPAIR_BUNDLE_DIRS,
    REPAIR_BUNDLE_EVIDENCE_RECORDS,
    REPAIR_BUNDLE_FILES,
    REPAIR_BUNDLE_LOG_RELATIVE,
    REPAIR_BUNDLE_MANIFEST_NAME,
    REPAIR_BUNDLE_PATCH_INDEX,
    REPAIR_STATUSES,
    SUCCESS_REPAIR_STATUSES,
    canonical_fields,
    validate_repair_bundle_semantics,
)
from agent_contract_wiring import (  # noqa: E402
    resolve_publication_contract,
    validate_agent_contract_assessment,
)
from d1_d2_contract import (  # noqa: E402
    is_structural_auto_fix_operation,
    output_repair_proof,
    structural_auto_fix_operation_error,
)
from deterministic_contract import (  # noqa: E402
    CHECK_IDS,
    DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION,
    EXECUTABLE_REPAIR_PLAN_SCHEMA_VERSION,
    UNAVAILABLE_CHECK_STATUSES,
    finding_lane,
    is_deterministic_repair_plan,
    is_executable_repair_plan,
    validate_deterministic_contract,
    validate_deterministic_plan_binding,
    validate_repair_plan_binding,
)
from artifact_schema import (  # noqa: E402
    AGENT_REPAIR_ASSESSMENT_SCHEMA_VERSION,
    AUDIT_ATTESTATION_SCHEMA_VERSION,
    AUDIT_MANIFEST_SCHEMA_VERSION,
    AUDIT_REPORT_SCHEMA_VERSION,
    DISPOSITION_SCHEMA_VERSION,
    DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
    DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
    AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
    PUBLICATION_CLASSES,
    REPAIR_PLAN_SCHEMA_VERSION,
    SCORING_SCHEMA_VERSION,
    IMPLEMENTATION_HASH_SCHEMA_VERSION,
    IMPLEMENTATION_MANIFEST_SCHEMA_VERSION,
    require_schema,
)
from agent_repair_assessment import (  # noqa: E402
    assessment_decision_by_finding,
    enforce_plan_operations_approved,
    load_agent_repair_assessment,
    report_has_validated_paper_assessment,
    sha256_path as assessment_sha256_path,
    source_open_repair_queue,
    validate_agent_repair_assessment_payload,
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
from review_lock import ReviewOutputLock  # noqa: E402
from prepare_audit_output import (  # noqa: E402
    AGENT_ASSESSMENT_PENDING,
    AGENT_CONTRACT_PENDING,
    AGENT_CONTRACT_REQUEST_RELATIVE_PATH,
    canonical_mapping_hash,
    preparation_artifact_hashes,
    validate_agent_contract_request,
)
from audit_integrity import validate_finalized_audit_bundle  # noqa: E402
from run_context import (  # noqa: E402
    PackageRunLock,
    RunContextError,
    complete,
    load_context,
    transition,
    verify_live_package_matches_snapshot,
    verify_content_root,
    write_content_root,
)

REVIEW_CONTRACT_VERSION = "materials-review-contract/1"
RUN_DIRECTORY: ContextVar[Path | None] = ContextVar("materials_run_directory", default=None)

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
NON_PUBLISHING_REPAIR_STATES = frozenset(
    {
        "PARTIALLY_REPAIRED",
        "ABANDONED",
        "ROLLED_BACK",
        "INFRASTRUCTURE_BLOCKED",
        AGENT_CONTRACT_PENDING,
        AGENT_ASSESSMENT_PENDING,
    }
)
MAX_CONTROL_FAILURES_PER_FINGERPRINT = 2
MAX_CONTROL_FAILURES_PER_SCOPE = 3
PENDING_REPAIR_SCHEMA_VERSION = "materials-repair-agent-contract-pending/1.0"
RELOCATION_IMMUTABLE_ARTIFACTS = frozenset(
    {
        ".benchmark_audit_tmp/agent_quality/assessment.json",
        "agent_quality/assessment.json",
    }
)
OPAQUE_REAUDIT_EVIDENCE_PREFIXES = (
    "deterministic_core/probe_cases/",
    "evidence/checker_tests/",
)


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
    "benchmark_repair_history",
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


def write_attempt_manifest(
    path: Path, manifest: dict[str, Any], *, package_mutated: bool
) -> None:
    """Write a manifest with an explicitly validated mutation state.

    A successful manifest is first staged with ``False`` while publication is
    in progress.  The atomic publication helper is the only caller allowed
    to rewrite that staged manifest to ``True``.
    """

    if not isinstance(package_mutated, bool):
        raise TypeError("package_mutated must be a boolean")
    status = manifest.get("status")
    if package_mutated and status != "REPAIRED":
        raise ValueError(
            "only a REPAIRED attempt may report package_mutated=true"
        )
    if status in NON_PUBLISHING_REPAIR_STATES and package_mutated:
        raise ValueError(
            f"{status} attempt cannot report package_mutated=true"
        )
    payload = dict(manifest)
    payload["package_mutated"] = package_mutated
    write_json(path, payload)


def atomic_publish_candidate(
    *,
    root: Path,
    candidate: Path,
    history: Path,
    generated_outputs: dict[str, str],
    attempt_manifest_path: Path,
) -> None:
    """Publish a candidate and attest mutation only after publication.

    The manifest attestation is part of the rollback window.  If either the
    candidate rename or the final ``package_mutated=true`` write fails, the
    live package and moved package-local outputs are restored before the
    exception escapes.  Consequently an incomplete publication can never
    leave a true mutation claim behind.
    """

    original = history / "original"
    root.rename(original)
    try:
        candidate.rename(root)
        manifest = read_json(attempt_manifest_path)
        if not isinstance(manifest, dict):
            raise ValueError("attempt manifest is not an object")
        write_attempt_manifest(
            attempt_manifest_path, manifest, package_mutated=True
        )
    except Exception:
        if root.exists() and not candidate.exists():
            root.rename(candidate)
        # ``externalize_generated_bundles`` moves only package-local
        # benchmark_repair output.  The re-audit remains external throughout.
        external_repair = generated_outputs.get("benchmark_repair")
        if external_repair is not None:
            external_path = Path(external_repair)
            if external_path.exists():
                external_path.rename(candidate / "benchmark_repair")
        if original.exists():
            original.rename(root)
        raise


def cleanup_repair_workspace(workspace: Path) -> None:
    """Remove the attempt workspace and its empty temporary parent."""

    shutil.rmtree(workspace, ignore_errors=True)
    try:
        workspace.parent.rmdir()
    except OSError:
        # Another attempt may still be using the shared temporary parent.
        pass


def default_source_audit_dir(root: Path) -> Path:
    run_dir = RUN_DIRECTORY.get()
    if run_dir is not None:
        return run_dir / "audit" / "benchmark_audit"
    return canonical_management_path(root, "source_audit")


def source_audit_dir(root: Path, plan: dict[str, Any]) -> Path:
    run_dir = RUN_DIRECTORY.get()
    if run_dir is not None:
        return run_dir / "audit" / "benchmark_audit"
    raw = plan.get("source_audit_dir")
    path = Path(str(raw)).expanduser().resolve() if raw is not None else default_source_audit_dir(root)
    return require_management_path(root, path, purpose="source_audit", label="source audit directory")


def default_repair_output_dir(root: Path) -> Path:
    run_dir = RUN_DIRECTORY.get()
    if run_dir is not None:
        return run_dir / "repair"
    return canonical_management_path(root, "repair")


def repair_output_root(root: Path, plan: dict[str, Any]) -> Path:
    run_dir = RUN_DIRECTORY.get()
    if run_dir is not None:
        return run_dir / "repair"
    raw = plan.get("repair_output_dir")
    path = Path(str(raw)).expanduser().resolve() if raw is not None else default_repair_output_dir(root)
    return require_management_path(root, path, purpose="repair", label="repair output directory")


def reaudit_output_root(root: Path) -> Path:
    run_dir = RUN_DIRECTORY.get()
    if run_dir is not None:
        return run_dir / "reaudit"
    return canonical_management_path(root, "reaudit")


def reaudit_audit_dir(
    root: Path,
    plan: dict[str, Any],
    *,
    anchor_root: Path | None = None,
    audit_output_dir: Path | None = None,
) -> Path:
    """Return the re-audit bundle path anchored to the source package.

    ``candidate`` lives below ``.benchmark_repair_tmp`` during Repair.  Using
    it as the routing root would silently create a second, temporary sibling
    management tree.  Callers that operate on a candidate therefore pass the
    original Harbor root explicitly.
    """

    del plan
    return (
        audit_output_dir / "benchmark_audit"
        if audit_output_dir is not None
        else reaudit_output_root(anchor_root or root) / "benchmark_audit"
    )


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


def source_audit_bundle_hash(root: Path, plan: dict[str, Any]) -> str:
    return sha256_path(source_audit_dir(root, plan))


def assert_source_audit_unchanged(
    root: Path, plan: dict[str, Any], expected: str
) -> None:
    if RUN_DIRECTORY.get() is not None:
        # A0 is frozen by ContentRoot; do not reintroduce a second source-bundle
        # freshness protocol inside one run.
        return
    actual = source_audit_bundle_hash(root, plan)
    if actual != expected:
        raise ValueError(
            "source audit bundle changed during Repair; fresh audit required"
        )


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

    ``spec`` is one entry of a current batch plan's ``findings`` list and
    carries ``repair_class``, ``operations``, ``regression_tests``, and
    ``finding_id``.
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
        publication_class = operation.get("publication_class")
        if publication_class not in PUBLICATION_CLASSES:
            raise ValueError(
                "every executable operation requires publication_class in "
                f"{sorted(PUBLICATION_CLASSES)}"
            )
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

    if plan.get("schema_version") != REPAIR_PLAN_SCHEMA_VERSION:
        if plan.get("schema_version") == DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION:
            raise ValueError(
                "materials-deterministic-repair-plan/1.0 is archival-only; "
                f"active Repair requires {REPAIR_PLAN_SCHEMA_VERSION}"
            )
        raise ValueError(
            "active Repair requires schema_version "
            f"{REPAIR_PLAN_SCHEMA_VERSION}"
        )
    findings = plan["findings"]
    if not findings:
        raise ValueError("batch repair plan requires at least one finding")
    if not isinstance(plan.get("deterministic_contract"), dict):
        raise ValueError(
            "repair plan requires a source deterministic_contract binding"
        )
    assessment_binding = plan.get("agent_repair_assessment")
    if not isinstance(assessment_binding, dict):
        raise ValueError(
            "repair plan requires agent_repair_assessment binding"
        )
    if (
        assessment_binding.get("schema_version")
        != AGENT_REPAIR_ASSESSMENT_SCHEMA_VERSION
    ):
        raise ValueError(
            "repair plan agent_repair_assessment schema_version must be "
            f"{AGENT_REPAIR_ASSESSMENT_SCHEMA_VERSION}"
        )
    if (
        not isinstance(assessment_binding.get("assessment_hash"), str)
        or not str(assessment_binding["assessment_hash"]).startswith("sha256:")
    ):
        raise ValueError(
            "repair plan requires agent_repair_assessment.assessment_hash"
        )
    if (
        not isinstance(assessment_binding.get("path"), str)
        or not assessment_binding["path"].strip()
    ):
        raise ValueError(
            "repair plan requires agent_repair_assessment.path"
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
        lane = finding.get("lane") or finding.get("repair_lane")
        if lane == "agent_quality":
            if finding.get("deterministic_check") is not None:
                raise ValueError(
                    "Agent quality findings may not claim D1-D6 ownership"
                )
            if finding.get("repair_class") == "AUTO_FIX":
                raise ValueError(
                    "Agent quality findings may not become deterministic AUTO_FIX"
                )
        elif finding.get("deterministic_check") not in CHECK_IDS:
            raise ValueError("deterministic repair target check is unknown")
        if (
            not isinstance(finding.get("justification"), str)
            or not finding["justification"].strip()
        ):
            raise ValueError("every batch finding requires a justification")
        finding.setdefault("operations", [])
        finding.setdefault("regression_tests", [])
        finding.setdefault("evidence", [])
        if lane is None and finding.get("deterministic_check") in CHECK_IDS:
            finding["lane"] = "deterministic_core"
        validate_finding_spec(root, finding)
    return plan


def validate_external_plan(root: Path, plan_path: Path) -> dict[str, Any]:
    resolved = plan_path.expanduser().resolve()
    if resolved.is_relative_to(root.resolve()):
        raise ValueError("repair plan must remain outside the Harbor 题包")
    if not resolved.is_file():
        raise FileNotFoundError(f"repair plan is missing: {resolved}")
    plan = read_json(resolved)
    if not isinstance(plan, dict):
        raise ValueError("repair plan must be a JSON object")
    if not is_executable_repair_plan(plan):
        if plan.get("schema_version") == DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION:
            raise ValueError(
                "materials-deterministic-repair-plan/1.0 is archival-only; "
                f"active Repair requires {REPAIR_PLAN_SCHEMA_VERSION}"
            )
        raise ValueError(
            "active Repair requires schema_version "
            f"{REPAIR_PLAN_SCHEMA_VERSION}"
        )
    if not isinstance(plan.get("audit_id"), str) or not plan["audit_id"]:
        raise ValueError("repair plan requires audit_id")
    if not isinstance(plan.get("findings"), list):
        raise ValueError("repair plan must be a complete batch")
    return validate_batch_plan(root, plan)


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
    # Run-local A0 is the one content-integrity gate. Historical per-file
    # manifest hashes remain provenance and must not make an equivalent Review
    # implementation or a harmless artifact rewrite stale.
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
    if not all((audit / relative).is_file() for relative in required):
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit omits required reports",
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
    if manifest.get("review_contract_version", REVIEW_CONTRACT_VERSION) != REVIEW_CONTRACT_VERSION:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "authoritative audit uses an incompatible Review contract",
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
    if RUN_DIRECTORY.get() is not None:
        try:
            validate_deterministic_contract(report.get("deterministic_contract"))
            if is_executable_repair_plan(plan):
                validate_repair_plan_binding(report, plan)
            else:
                validate_deterministic_plan_binding(report, plan)
        except ValueError as exc:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"repair plan binding is invalid: {exc}",
            ) from exc
        return source_audit
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
            if is_executable_repair_plan(plan):
                validate_repair_plan_binding(report, plan)
            else:
                validate_deterministic_plan_binding(report, plan)
        except ValueError as exc:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"repair plan binding is invalid: {exc}",
            ) from exc
    return source_audit


def validate_fresh_audit(
    root: Path,
    plan: dict[str, Any],
    attestation_path: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    audit = source_audit_dir(root, plan)
    if RUN_DIRECTORY.get() is None:
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
    benchmark_root = manifest.get("benchmark_root")
    if (
        not isinstance(benchmark_root, str)
        or Path(benchmark_root).expanduser().resolve() != root
    ):
        raise ValueError(
            "source audit package identity is not bound to the live package"
        )
    report_configuration(report)
    require_validated_paper_assessment(report)
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
    if RUN_DIRECTORY.get() is None:
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
    """Lane-aware repair policy: preserve no-leak / AUTO_FIX wiring rules."""

    quality_finding = is_agent_quality_finding(source_finding, report) or (
        plan_finding.get("lane") in {"agent_quality", "quality_results"}
        or plan_finding.get("judgment_type") == "AGENT_JUDGMENT"
        or plan_finding.get("repair_lane") == "agent_quality"
    )
    if quality_finding:
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
        return
    # Deterministic-core findings: AUTO_FIX remains unique source-bound wiring
    # only. ASSISTED_FIX is allowed when evidence-backed (enforced elsewhere).
    if plan_finding.get("repair_class") == "AUTO_FIX":
        scope = plan_finding.get("repair_scope")
        if scope is not None and scope not in {
            "DETERMINISTIC_WIRING",
            "UNIQUE_SCORING_WIRING",
            None,
        }:
            raise PolicyStop(
                "POLICY_VIOLATION",
                "AUTO_FIX is limited to unique source-bound D wiring scopes",
            )


# Narrow scopes that may publish without equal-depth Review.
DIRECT_DETERMINISTIC_SCOPES = frozenset(
    {"DETERMINISTIC_WIRING", "UNIQUE_SCORING_WIRING"}
)
# Any of these forces the re-audit publication route.
REAUDIT_REQUIRED_SCOPES = frozenset(
    {
        "CHECKER_ROBUSTNESS",
        "INSTRUCTION_CONTRACT",
        "SCORING_SEMANTICS",
        "DIRECT_INPUT_REFERENCE",
        "SCIENCE_SEMANTICS",
    }
)


def iter_plan_findings(plan: dict[str, Any]) -> list[dict[str, Any]]:
    findings = plan.get("findings")
    if isinstance(findings, list) and findings:
        return [item for item in findings if isinstance(item, dict)]
    if isinstance(plan.get("finding_id"), str) and plan["finding_id"]:
        return [plan]
    return []


def iter_executable_operations(plan: dict[str, Any]) -> list[dict[str, Any]]:
    operations: list[dict[str, Any]] = []
    for finding in iter_plan_findings(plan):
        if finding.get("repair_class") == "ABANDON":
            continue
        for operation in finding.get("operations", []):
            if isinstance(operation, dict):
                operations.append(operation)
    return operations


def evaluate_direct_deterministic_eligibility(
    plan: dict[str, Any],
    report: dict[str, Any],
    *,
    unresolved_findings: list[dict[str, Any]] | None = None,
    findings_by_id: dict[str, dict[str, Any]] | None = None,
) -> tuple[bool, str]:
    """Return whether the candidate may skip equal-depth re-audit.

    Eligibility is fail-closed: mixed publication classes, Agent-quality
    findings, ASSISTED_FIX, non-wiring scopes, or unresolved items all take
    the re-audit route. Declaring DIRECT_DETERMINISTIC alone is never enough.
    """

    if unresolved_findings:
        return False, "unresolved findings remain; re-audit required"
    findings = iter_plan_findings(plan)
    if not findings:
        return False, "plan has no findings"
    operations = iter_executable_operations(plan)
    if not operations:
        return False, "no executable operations"
    if any(
        operation.get("publication_class") != "DIRECT_DETERMINISTIC"
        for operation in operations
    ):
        return False, "not every operation declares DIRECT_DETERMINISTIC"
    if plan.get("core_science_change") not in {False, None}:
        return False, "plan core_science_change is not false"
    report_findings = {
        item.get("finding_id"): item
        for item in report.get("findings", [])
        if isinstance(item, dict) and isinstance(item.get("finding_id"), str)
    }
    if findings_by_id:
        report_findings = {**report_findings, **findings_by_id}
    for finding in findings:
        repair_class = finding.get("repair_class")
        if repair_class == "ABANDON":
            return False, "ABANDON findings block direct publication"
        if repair_class != "AUTO_FIX":
            return False, "direct publication requires AUTO_FIX for every finding"
        if finding.get("core_science_change") is not False:
            return False, "direct publication requires core_science_change=false"
        scope = finding.get("repair_scope")
        if scope in REAUDIT_REQUIRED_SCOPES:
            return False, f"repair_scope {scope} requires equal-depth re-audit"
        if scope is not None and scope not in DIRECT_DETERMINISTIC_SCOPES:
            return False, f"repair_scope {scope} is not direct-eligible"
        check = finding.get("deterministic_check")
        if check not in CHECK_IDS:
            return False, "direct publication requires D1-D6 machine findings"
        source = report_findings.get(finding.get("finding_id"), {})
        if is_agent_quality_finding(finding, report) or is_agent_quality_finding(
            source, report
        ):
            return False, "Agent-quality findings require equal-depth re-audit"
        lane = finding.get("lane") or finding.get("repair_lane")
        if lane in {"agent_quality", "quality_results"}:
            return False, "Agent-quality lane requires equal-depth re-audit"
    return True, "all operations are narrowly DIRECT_DETERMINISTIC"


def build_direct_deterministic_comparison(
    *,
    report: dict[str, Any],
    plan: dict[str, Any],
    identity: dict[str, Any],
    resolved_targets: list[str],
    regression_results: list[dict[str, Any]],
) -> dict[str, Any]:
    """Comparison payload for direct publish (no Review re-audit)."""

    reason = (
        "DIRECT_DETERMINISTIC publication: every operation is unique "
        "source-bound D1-D6 AUTO_FIX wiring; equal-depth Review was not invoked."
    )
    source_finding_id = resolved_targets[0] if resolved_targets else None
    return {
        "verification_mode": "DIRECT_DETERMINISTIC",
        "reaudit_performed": False,
        "reaudit_skipped_reason": reason,
        "reason": reason,
        "reaudit_count": 0,
        "reaudit_audit_id": None,
        "reaudit_verdict": None,
        "publication_route": "PUBLISH_CANDIDATE",
        "target_resolved": True,
        "identity_preserved": True,
        "mutation_scope_allowed": True,
        "residual_blocking_finding_ids": [],
        "residual_blocking_findings": [],
        "unresolved_severe_finding_ids": [],
        "resolved_findings": list(resolved_targets),
        "unresolved_findings": [],
        "source_finding": {
            "finding_id": source_finding_id,
            "status": "OPEN",
        },
        "source_configuration": {"review_lane": report_configuration(report)},
        "source_score": authoritative_total_score(
            report, context="source audit"
        ),
        "regression_evidence": regression_results,
        "package_identity": identity,
    }


def resolve_agent_repair_assessment_path(
    root: Path, plan: dict[str, Any], plan_path: Path | None = None
) -> Path:
    """Resolve the Agent repair assessment path from the plan binding."""

    binding = plan.get("agent_repair_assessment")
    if not isinstance(binding, dict):
        raise ValueError("repair plan requires agent_repair_assessment binding")
    raw = binding.get("path")
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError("agent_repair_assessment.path is required")
    path = Path(raw).expanduser()
    if not path.is_absolute() and plan_path is not None:
        path = (plan_path.parent / path).resolve()
    else:
        path = path.resolve()
    if path.is_relative_to(root.resolve()):
        raise ValueError(
            "agent_repair_assessment must remain outside the Harbor 题包"
        )
    run_dir = RUN_DIRECTORY.get()
    if run_dir is not None:
        expected = (run_dir / "repair" / "agent_repair_assessment.json").resolve()
        # Prefer the canonical run-local path when present; otherwise use the
        # explicitly bound external path.
        if expected.is_file():
            return expected
    return path


def load_and_bind_agent_repair_assessment(
    root: Path,
    plan: dict[str, Any],
    report: dict[str, Any],
    *,
    plan_path: Path | None = None,
) -> dict[str, Any]:
    """Load, hash-check, and queue-bind the Agent repair assessment."""

    path = resolve_agent_repair_assessment_path(root, plan, plan_path)
    binding = plan["agent_repair_assessment"]
    actual_hash = assessment_sha256_path(path)
    expected_hash = binding.get("assessment_hash")
    if actual_hash != expected_hash:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            "agent_repair_assessment hash is stale or mismatched",
        )
    a0 = None
    run_dir = RUN_DIRECTORY.get()
    if run_dir is not None:
        content_root = run_dir / "roots" / "A0.json"
        if content_root.is_file():
            try:
                payload = read_json(content_root)
            except (OSError, ValueError, TypeError):
                payload = {}
            if isinstance(payload, dict):
                digest = payload.get("content_root") or payload.get("digest")
                if isinstance(digest, str):
                    a0 = digest
    identity = plan.get("package_identity")
    if not isinstance(identity, dict):
        identity = package_identity(root)
    assessment = load_agent_repair_assessment(
        path,
        report=report,
        expected_audit_id=plan.get("audit_id"),
        expected_a0=a0,
        expected_package_identity=identity,
    )
    enforce_plan_operations_approved(plan, assessment)
    plan["_loaded_agent_repair_assessment"] = assessment
    plan["_agent_repair_assessment_path"] = str(path)
    return assessment


def require_validated_paper_assessment(report: dict[str, Any]) -> None:
    """Reject incomplete / NOT_SUPPLIED dual-lane audits at Repair ingress."""

    if report_has_validated_paper_assessment(report):
        return
    raise PolicyStop(
        "BLOCKED_EVIDENCE",
        "Repair requires a complete dual-lane REVIEWED source audit that "
        "binds a validated paper Agent assessment; incomplete or "
        "NOT_SUPPLIED assessments are rejected (migrate via ticket 01)",
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


def materialize_inherited_paper_assessment(
    candidate: Path,
    report: dict[str, Any],
    plan: dict[str, Any],
    scratch_dir: Path,
) -> tuple[Path | None, str | None]:
    """Resolve the source paper assessment for equal-depth re-audit.

    Prefer an explicit external plan path; otherwise reuse the validated
    assessment already bound into the source audit. Absence/invalid binding
    pauses as assessment-pending rather than falling back to deterministic-only
    Review.
    """

    raw = plan.get("agent_assessment")
    if raw is not None:
        external = Path(str(raw)).expanduser().resolve()
        if external.is_relative_to(candidate.resolve()):
            return None, "agent_assessment must remain external to the candidate"
        if not external.is_file():
            return None, f"inherited paper Agent assessment is missing: {external}"
        return external, None

    quality = report.get("agent_quality")
    assessment = quality.get("assessment") if isinstance(quality, dict) else None
    if not isinstance(assessment, dict) or not assessment.get(
        "materials_qualification"
    ):
        return (
            None,
            "equal-depth re-audit requires the inherited paper Agent assessment; "
            "deterministic-only fallback is not permitted",
        )
    scratch_dir.mkdir(parents=True, exist_ok=True)
    path = scratch_dir / "inherited_agent_assessment.json"
    path.write_text(
        json.dumps(assessment, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if path.is_relative_to(candidate.resolve()):
        return None, "inherited assessment materialization escaped the candidate"
    return path, None


def run_equal_depth_review(
    candidate: Path,
    report: dict[str, Any],
    source_manifest_or_plan: dict[str, Any],
    plan: dict[str, Any] | None = None,
    *,
    original_root: Path | None = None,
    agent_contract_assessment_path: Path | None = None,
    audit_output_dir: Path | None = None,
) -> dict[str, Any]:
    if plan is None:
        plan = source_manifest_or_plan
        source_manifest = {}
    else:
        source_manifest = source_manifest_or_plan
    # Re-review is an internal stage, not a second public CLI invocation. This
    # keeps the public Review seam strictly run-dir based.
    review_engine_path = review_skill_root() / "scripts" / "run_review.py"
    # Legacy fixture stubs are executable scripts and parse argv at import;
    # identify them without importing. Production Review exports run_review.
    review_source = review_engine_path.read_text(encoding="utf-8", errors="replace")
    if "def run_review(" in review_source:
        from run_review import run_review as run_review_engine  # noqa: E402
        from run_review import (  # noqa: E402
            AGENT_ASSESSMENT_PENDING as REVIEW_ASSESSMENT_PENDING,
        )
    else:
        run_review_engine = None
        REVIEW_ASSESSMENT_PENDING = AGENT_ASSESSMENT_PENDING
    source_lane = report_configuration(report)
    external_binding_hashes(candidate, plan, source_manifest)
    target_output_dir = (
        audit_output_dir
        or reaudit_audit_dir(
            candidate,
            plan,
            anchor_root=original_root,
        ).parent
    )
    review_output_dir = (
        target_output_dir
        if audit_output_dir is not None
        else reaudit_output_root(candidate)
    )
    assessment_scratch = review_output_dir / ".inherited_assessment"
    agent_assessment_path, assessment_error = materialize_inherited_paper_assessment(
        candidate,
        report,
        plan,
        assessment_scratch,
    )
    if agent_assessment_path is None:
        return {
            "benchmark_root": str(candidate),
            "audit_output_dir": str(review_output_dir),
            "status": REVIEW_ASSESSMENT_PENDING,
            "review_status": REVIEW_ASSESSMENT_PENDING,
            "verdict": "NOT_ASSESSABLE",
            "publishable": False,
            "deterministic_status": "NOT_APPLICABLE",
            "attempt_consumed": False,
            "message": assessment_error
            or "inherited paper Agent assessment is required",
        }
    if agent_contract_assessment_path is not None:
        external = agent_contract_assessment_path.expanduser().resolve()
        if external.is_relative_to(candidate.resolve()):
            raise ValueError(
                "agent_contract_assessment must remain external to the candidate"
            )
        if external.is_symlink() or not external.is_file():
            raise FileNotFoundError(
                f"agent_contract_assessment is missing or unsafe: {external}"
            )
        agent_contract_assessment_path = external
    if run_review_engine is None:
        # Compatibility is intentionally internal-only for old fixture
        # harnesses that provide an executable review stub but no engine.
        # Public Review remains ``--run-dir`` only.
        command = [
            sys.executable,
            str(review_engine_path),
            str(candidate),
            "--audit-output-dir",
            str(review_output_dir),
            "--output-purpose",
            "reaudit",
            "--agent-assessment",
            str(agent_assessment_path),
        ]
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
        if completed.returncode != 0:
            raise RuntimeError(f"internal fixture re-review failed: {completed.stderr.strip()}")
        result = {}
    else:
        result = run_review_engine(
            candidate,
            agent_assessment_path=agent_assessment_path,
            agent_contract_assessment_path=agent_contract_assessment_path,
            audit_output_dir=review_output_dir,
            output_purpose="reaudit",
            require_agent_assessment=True,
        )
    if isinstance(result, dict) and result.get("status") == REVIEW_ASSESSMENT_PENDING:
        result.setdefault("audit_output_dir", str(review_output_dir))
        result.setdefault("attempt_consumed", False)
        return result
    if review_output_dir != target_output_dir:
        if target_output_dir.exists() or target_output_dir.is_symlink():
            shutil.rmtree(target_output_dir)
        shutil.copytree(review_output_dir, target_output_dir)
    if isinstance(result, dict) and result.get("status") == AGENT_CONTRACT_PENDING:
        if review_output_dir != target_output_dir:
            _rewrite_pending_review_workspace(
                target_output_dir,
                old_candidate=candidate,
                new_candidate=candidate,
                old_output=review_output_dir,
                new_output=target_output_dir,
            )
        result.setdefault("audit_output_dir", str(target_output_dir))
        result.setdefault(
            "request_path",
            str(
                target_output_dir
                / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
            ),
        )
        return result
    reaudit = read_json(
        target_output_dir / "benchmark_audit/audit_report.json"
    )
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
    finding_id = finding.get("finding_id")
    if not isinstance(finding_id, str) or not finding_id:
        finding_id = "<missing-finding-id>"
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
        "finding_id": finding_id,
        "finding_code": code,
        "finding_fingerprint": canonical_json_hash(payload),
        "deterministic_check": finding.get("deterministic_check"),
        "severity": finding.get("severity"),
        "lane": finding.get("lane"),
        "blocking": finding.get("blocking"),
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


def unresolved_severe_references(
    findings: Iterable[dict[str, Any]],
    *,
    audit_id: str | None,
) -> list[dict[str, Any]]:
    """Return stable references for every unresolved severe re-audit finding."""

    resolved = {"RESOLVED", "CLOSED", "FIXED"}
    references: list[dict[str, Any]] = []
    for finding in findings:
        if (
            not isinstance(finding, dict)
            or finding.get("severity") not in {"HIGH", "FATAL"}
            or finding.get("status", "OPEN") in resolved
        ):
            continue
        references.append(
            {
                **finding_reference(finding, audit_id=audit_id),
                "reason": (
                    "unresolved HIGH/FATAL finding prevents PASS after "
                    "equal-depth re-audit"
                ),
            }
        )
    return references


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
    try:
        deterministic = resolve_publication_contract(
            reaudit.get("deterministic_contract"),
            reaudit.get("effective_deterministic_contract"),
            reaudit.get("agent_contract_assessment"),
        )
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
    original_root: Path | None = None,
    audit_output_dir: Path | None = None,
) -> dict[str, Any]:
    summary = reaudit.get("summary", {})
    disposition_path = reaudit_audit_dir(
        candidate,
        plan,
        anchor_root=original_root,
        audit_output_dir=audit_output_dir,
    ) / "disposition.json"
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
    manifest_path = reaudit_audit_dir(
        candidate,
        plan,
        anchor_root=original_root,
        audit_output_dir=audit_output_dir,
    ) / "audit_manifest.json"
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


def is_opaque_reaudit_evidence(relative: Path) -> bool:
    """Return whether a generated case payload must remain byte-identical."""

    normalized = relative.as_posix()
    temporary_prefix = ".benchmark_audit_tmp/"
    if normalized.startswith(temporary_prefix):
        normalized = normalized[len(temporary_prefix):]
        if (
            "/" in normalized
            and normalized.split("/", 1)[0].startswith("audit-")
        ):
            normalized = normalized.split("/", 1)[1]
    return any(
        normalized.startswith(prefix)
        for prefix in OPAQUE_REAUDIT_EVIDENCE_PREFIXES
    )


def is_relocation_immutable_artifact(relative: Path) -> bool:
    normalized = relative.as_posix()
    prefix = ".benchmark_audit_tmp/"
    if (
        normalized.startswith(prefix)
        and "/" in normalized[len(prefix):]
        and normalized[len(prefix):].split("/", 1)[0].startswith("audit-")
    ):
        normalized = (
            prefix
            + normalized[len(prefix):].split("/", 1)[1]
        )
    return normalized in RELOCATION_IMMUTABLE_ARTIFACTS


def refresh_audit_manifest_hashes(
    audit: Path,
    *,
    benchmark_root: str | None = None,
) -> dict[str, Any]:
    """Refresh authoritative output hashes after all relocation writes.

    ``audit_manifest.json`` is intentionally excluded from ``output_hashes``:
    including it would make the manifest's ``bundle_hash`` self-referential.
    Callers must invoke this only after rewriting path-bearing artifacts.
    """

    manifest_path = audit / "audit_manifest.json"
    manifest = read_json(manifest_path)
    if manifest.get("immutability_state") == "ATTESTED":
        raise ValueError(
            "attested source audit is immutable; fresh Review is required"
        )
    if benchmark_root is not None:
        manifest["benchmark_root"] = benchmark_root
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
    return manifest


def rebase_audit_paths(
    candidate: Path,
    final_root: Path,
    plan: dict[str, Any],
    *,
    audit_output_dir: Path | None = None,
) -> None:
    audit = reaudit_audit_dir(
        candidate,
        plan,
        anchor_root=final_root,
        audit_output_dir=audit_output_dir,
    )
    old = str(candidate)
    new = str(final_root)
    updates: dict[Path, bytes] = {}
    for path in audit.rglob("*"):
        if not path.is_file() or path.name == "audit_manifest.json":
            continue
        relative = path.relative_to(audit)
        if is_opaque_reaudit_evidence(relative):
            continue
        if relative.as_posix() in RELOCATION_IMMUTABLE_ARTIFACTS:
            continue
        if path.suffix == ".json":
            value = replace_paths(read_json(path), old, new)
            updates[path] = (
                json.dumps(value, indent=2, ensure_ascii=False) + "\n"
            ).encode("utf-8")
        elif path.suffix == ".jsonl":
            lines = [
                json.dumps(
                    replace_paths(json.loads(line), old, new), ensure_ascii=False
                )
                for line in path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
            updates[path] = "".join(
                line + "\n" for line in lines
            ).encode("utf-8")
        elif path.suffix in {".md", ".log"}:
            updates[path] = path.read_text(encoding="utf-8").replace(
                old, new
            ).encode("utf-8")
    manifest_path = audit / "audit_manifest.json"
    if manifest_path.is_file():
        manifest = replace_paths(read_json(manifest_path), old, new)
        if manifest.get("immutability_state") == "ATTESTED":
            raise ValueError(
                "attested source audit cannot be rebased or rewritten"
            )
        for path, content in updates.items():
            path.write_bytes(content)
        # The staged writes above must land before this refresh.  Otherwise
        # hashes can describe the pre-rebase bytes while the manifest itself
        # records the post-rebase paths.
        write_json(manifest_path, manifest)
        refresh_audit_manifest_hashes(audit, benchmark_root=new)


def externalize_generated_bundles(
    candidate: Path,
    root: Path,
    plan: dict[str, Any],
    *,
    audit_output_dir: Path | None = None,
    require_reaudit: bool = True,
) -> dict[str, str]:
    """Record externally generated repair bundles.

    Equal-depth re-audit writes under
    ``<repair_output_dir>/repair_reaudit/benchmark_audit``. Direct
    deterministic publication may omit that bundle. Optional package-local
    ``benchmark_repair`` artifacts are moved beside the repair output root.
    """
    output = repair_output_root(root, plan)
    published: dict[str, str] = {}
    reaudit = reaudit_audit_dir(
        candidate,
        plan,
        anchor_root=root,
        audit_output_dir=audit_output_dir,
    )
    if reaudit.is_dir():
        published["benchmark_audit"] = str(reaudit.parent)
    elif require_reaudit:
        raise FileNotFoundError(
            "generated repair_reaudit/benchmark_audit bundle is missing "
            "before publication"
        )
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


def reaudit_bundle_reference_fields(
    bundle: dict[str, Any] | None,
) -> dict[str, Any]:
    """Expose stable, non-content references for a retained re-audit bundle."""

    if not isinstance(bundle, dict):
        return {}
    return {
        "reaudit_bundle": bundle,
        "reaudit_bundle_dir": bundle.get("bundle_dir"),
        "reaudit_audit_dir": bundle.get("audit_dir"),
        "reaudit_audit_id": bundle.get("audit_id"),
        "reaudit_report_hash": bundle.get("report_hash"),
        "reaudit_manifest_hash": bundle.get("manifest_hash"),
        "reaudit_bundle_hash": bundle.get("bundle_hash"),
    }


def archive_reaudit_bundle(
    candidate: Path,
    root: Path,
    plan: dict[str, Any],
    history_dir: Path,
    *,
    audit_output_dir: Path | None = None,
) -> dict[str, Any]:
    """Retain and authenticate the complete canonical re-audit bundle.

    Review writes to the canonical sibling workspace, while this copy is
    attempt-specific and therefore survives later attempts overwriting that
    workspace.  The manifest's per-file hashes are checked both before and
    after copying; the directory hash then binds the complete retained
    bundle.
    """

    audit = reaudit_audit_dir(
        candidate,
        plan,
        anchor_root=root,
        audit_output_dir=audit_output_dir,
    )
    if not audit.is_dir():
        raise FileNotFoundError(
            "completed re-audit did not create repair_reaudit/benchmark_audit"
        )
    # Rebase generated paths before archiving so history never points into the
    # temporary candidate workspace.
    rebase_audit_paths(
        candidate,
        root,
        plan,
        audit_output_dir=audit_output_dir,
    )
    manifest_path = audit / "audit_manifest.json"
    report_path = audit / "audit_report.json"
    disposition_path = audit / "disposition.json"
    if not all(path.is_file() and not path.is_symlink() for path in (
        manifest_path,
        report_path,
        disposition_path,
    )):
        raise ValueError("re-audit bundle is incomplete")
    report = read_json(report_path)
    manifest = read_json(manifest_path)
    disposition = read_json(disposition_path)
    authenticate_audit_bundle(
        root, report, manifest, disposition, audit=audit
    )
    source_bundle_hash = sha256_path(audit)
    destination = history_dir / "repair_reaudit" / "benchmark_audit"
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(
            f"retained re-audit bundle already exists: {destination}"
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(audit, destination)
    archived_report = read_json(destination / "audit_report.json")
    archived_manifest = read_json(destination / "audit_manifest.json")
    archived_disposition = read_json(destination / "disposition.json")
    authenticate_audit_bundle(
        root,
        archived_report,
        archived_manifest,
        archived_disposition,
        audit=destination,
    )
    archived_bundle_hash = sha256_path(destination)
    if archived_bundle_hash != source_bundle_hash:
        raise ValueError("retained re-audit bundle changed during archival")
    output_hashes = archived_manifest.get("output_hashes")
    if not isinstance(output_hashes, dict) or not output_hashes:
        raise ValueError("re-audit manifest lacks output hashes")
    return {
        "bundle_dir": str(destination.parent),
        "audit_dir": str(destination),
        "audit_id": archived_manifest.get("audit_id"),
        "report_hash": sha256_file(destination / "audit_report.json"),
        "manifest_hash": sha256_file(destination / "audit_manifest.json"),
        "bundle_hash": archived_bundle_hash,
        "manifest_output_hashes": dict(output_hashes),
    }


def _pending_workspace_hashes(
    snapshot: Path, candidate: Path, audit_output_dir: Path
) -> dict[str, str]:
    return {
        "snapshot": sha256_path(snapshot),
        "candidate": sha256_path(candidate),
        "reaudit_workspace": sha256_path(audit_output_dir),
    }


def _rewrite_pending_review_workspace(
    audit_output_dir: Path,
    *,
    old_candidate: Path,
    new_candidate: Path,
    old_output: Path,
    new_output: Path,
) -> dict[str, Any]:
    """Relocate a prepared Review request without rerunning its probes."""

    request_path = (
        audit_output_dir / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
    )
    if not request_path.is_file():
        raise ValueError("pending re-audit request is missing")
    original_request = read_json(request_path)
    raw_temp_dir = original_request.get("audit_temp_dir")
    temp_dir = (
        Path(str(raw_temp_dir)).expanduser().resolve()
        if isinstance(raw_temp_dir, str) and raw_temp_dir
        else old_output / ".benchmark_audit_tmp"
    )
    if (
        temp_dir.parent != old_output / ".benchmark_audit_tmp"
        and temp_dir != old_output / ".benchmark_audit_tmp"
    ):
        raise ValueError("pending re-audit temp workspace is stale")
    quality_path = temp_dir / "agent_quality/assessment.json"
    original_quality_hash = (
        sha256_file(quality_path) if quality_path.is_file() else None
    )
    if original_request.get("quality_assessment_hash") != original_quality_hash:
        raise ValueError(
            "pending re-audit quality assessment hash is stale or tampered"
        )

    for path in audit_output_dir.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(audit_output_dir).as_posix()
        if is_opaque_reaudit_evidence(Path(relative)):
            continue
        if is_relocation_immutable_artifact(Path(relative)):
            # This artifact is content-addressed by the pending request. Its
            # contents must stay byte-identical across workspace relocation;
            # path-bearing evidence belongs in relative-path fields.
            continue
        if path.suffix == ".json":
            write_json(
                path,
                replace_paths(
                    replace_paths(
                        read_json(path),
                        str(old_candidate),
                        str(new_candidate),
                    ),
                    str(old_output),
                    str(new_output),
                ),
            )
        elif path.suffix in {".jsonl", ".md", ".log", ".txt"}:
            text = path.read_text(encoding="utf-8")
            path.write_text(
                text.replace(str(old_candidate), str(new_candidate)).replace(
                    str(old_output), str(new_output)
                ),
                encoding="utf-8",
            )

    request = read_json(request_path)
    raw_temp_dir = request.get("audit_temp_dir")
    temp_dir = (
        Path(str(raw_temp_dir)).expanduser().resolve()
        if isinstance(raw_temp_dir, str) and raw_temp_dir
        else audit_output_dir / ".benchmark_audit_tmp"
    )
    if (
        temp_dir != audit_output_dir / ".benchmark_audit_tmp"
        and temp_dir.parent != audit_output_dir / ".benchmark_audit_tmp"
    ) or not temp_dir.is_dir():
        raise ValueError("pending re-audit temp workspace is stale")
    request["benchmark_root"] = str(new_candidate.resolve())
    request["static_hashes"] = preparation_artifact_hashes(temp_dir)["static"]
    request["probe_hashes"] = preparation_artifact_hashes(temp_dir)["probes"]
    request["probe_hash"] = canonical_mapping_hash(request["probe_hashes"])
    request["request_digest"] = canonical_mapping_hash(
        {
            key: value
            for key, value in request.items()
            if key != "request_digest"
        }
    )
    quality_path = temp_dir / "agent_quality/assessment.json"
    if request.get("quality_assessment_hash") != (
        sha256_file(quality_path) if quality_path.is_file() else None
    ):
        raise ValueError(
            "pending re-audit quality assessment changed during relocation"
        )
    write_json(request_path, request)
    validate_agent_contract_request(new_candidate, temp_dir)
    return request


def persist_pending_repair(
    *,
    root: Path,
    plan: dict[str, Any],
    plan_path: Path,
    report: dict[str, Any],
    audit_manifest: dict[str, Any],
    findings_by_id: dict[str, dict[str, Any]] | None,
    source_finding: dict[str, Any] | None,
    root_cause: str,
    attempt_number: int,
    repair_id: str,
    workspace: Path,
    snapshot: Path,
    candidate: Path,
    audit_output_dir: Path,
    changes: list[dict[str, Any]],
    regression_results: list[dict[str, Any]],
    resolved_targets: list[str],
    unresolved_findings: list[dict[str, Any]],
    evidence: list[dict[str, Any]],
    workflow_kind: str,
    identity: dict[str, Any],
) -> dict[str, Any]:
    """Persist a resumable semantic attempt without consuming its budget."""

    if attempt_number < 0:
        raise ValueError("an Agent-contract pause has an invalid attempt number")
    history = history_root_for(root, plan) / repair_id
    if history.exists():
        raise FileExistsError(f"pending repair history already exists: {history}")
    source_bundle_hash = source_audit_bundle_hash(root, plan)
    history.mkdir(parents=True)
    history_snapshot = history / "snapshot"
    history_candidate = history / "candidate"
    history_output = history / "reaudit_workspace"
    shutil.copytree(snapshot, history_snapshot)
    shutil.copytree(candidate, history_candidate)
    shutil.copytree(audit_output_dir, history_output)
    request = _rewrite_pending_review_workspace(
        history_output,
        old_candidate=candidate,
        new_candidate=history_candidate,
        old_output=audit_output_dir,
        new_output=history_output,
    )
    context = {
        "schema_version": PENDING_REPAIR_SCHEMA_VERSION,
        "workflow_kind": workflow_kind,
        "repair_id": repair_id,
        "root_cause": root_cause,
        "attempt_number": attempt_number,
        "audit_id": report.get("audit_id"),
        "plan": plan,
        "plan_path": str(plan_path.expanduser().resolve()),
        "plan_hash": sha256_file(plan_path.expanduser().resolve()),
        "report": report,
        "audit_manifest": audit_manifest,
        "findings_by_id": findings_by_id or {},
        "source_finding": source_finding,
        "changes": changes,
        "regression_results": regression_results,
        "resolved_targets": resolved_targets,
        "unresolved_findings": unresolved_findings,
        "evidence": evidence,
        "identity": identity,
        "source_report_hash": sha256_file(
            source_audit_dir(root, plan) / "audit_report.json"
        ),
        "source_manifest_hash": sha256_file(
            source_audit_dir(root, plan) / "audit_manifest.json"
        ),
        "source_audit_bundle_hash": source_bundle_hash,
    }
    write_json(history / "repair_context.json", context)
    context_hash = sha256_file(history / "repair_context.json")
    state = {
        "schema_version": PENDING_REPAIR_SCHEMA_VERSION,
        "status": AGENT_CONTRACT_PENDING,
        "repair_id": repair_id,
        "resume_id": repair_id,
        "pending_state_path": str(history / "pending_state.json"),
        "workflow_kind": workflow_kind,
        "root_cause": root_cause,
        "audit_id": report.get("audit_id"),
        "attempt_number": attempt_number,
        "attempt_consumed": False,
        "package_mutated": False,
        "package_identity": identity,
        "source_core_contract_digest": plan.get("core_contract_digest"),
        "plan_hash": context["plan_hash"],
        "context_hash": context_hash,
        "request": request,
        "request_path": str(
            history_output / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
        ),
        "original_workspace_dir": str(workspace),
        "candidate_dir": str(history_candidate),
        "snapshot_dir": str(history_snapshot),
        "reaudit_workspace_dir": str(history_output),
        "workspace_hashes": _pending_workspace_hashes(
            history_snapshot, history_candidate, history_output
        ),
        "candidate_package_hashes": package_hashes(history_candidate),
        "snapshot_package_hashes": package_hashes(history_snapshot),
        "source_audit_bundle_hash": source_bundle_hash,
        "machine_contract_digest": request.get("machine_contract_digest"),
        "machine_schema_version": request.get("machine_schema_version"),
        "machine_registry_version": request.get("machine_registry_version"),
        "probe_hashes": request.get("probe_hashes"),
        "probe_hash": request.get("probe_hash"),
        "implementation_hash": request.get("implementation_hash"),
        "assessment_schema_version": request.get(
            "assessment_schema_version"
        ),
        "prepared_review_audit_id": request.get("audit_id"),
        "recorded_at": timestamp(),
    }
    state["state_digest"] = canonical_json_hash(
        {key: value for key, value in state.items() if key != "state_digest"}
    )
    write_json(history / "pending_state.json", state)
    return {
        "repair_id": repair_id,
        "resume_id": repair_id,
        "status": AGENT_CONTRACT_PENDING,
        "review_status": AGENT_CONTRACT_PENDING,
        "review_verdict": "NOT_ASSESSABLE",
        "disposition": "NOT_ASSESSABLE",
        "publishability": "EVIDENCE_PENDING",
        "publishable": False,
        "repair_state": AGENT_CONTRACT_PENDING,
        "attempt_number": attempt_number,
        "attempt_consumed": False,
        "package_mutated": False,
        "history_root": str(history_root_for(root, plan)),
        "history_dir": str(history),
        "pending_state": str(history / "pending_state.json"),
        "request_path": str(
            history_output / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
        ),
        "candidate_dir": str(history_candidate),
        "snapshot_dir": str(history_snapshot),
        "reaudit_workspace_dir": str(history_output),
        "machine_contract_digest": request.get("machine_contract_digest"),
        "probe_hash": request.get("probe_hash"),
        "message": (
            "Repair is paused. Supply --resume-repair-id "
            f"{repair_id} with a fresh --agent-contract-assessment."
        ),
    }


def _read_pending_repair(
    root: Path,
    plan: dict[str, Any],
    repair_id: str,
    plan_path: Path,
    agent_contract_assessment_path: Path | None,
) -> tuple[dict[str, Any], dict[str, Any], Path, Path, Path]:
    if (
        not isinstance(repair_id, str)
        or not repair_id
        or Path(repair_id).name != repair_id
        or repair_id in {".", ".."}
    ):
        raise ValueError("resume repair ID is invalid")
    history = history_root_for(root, plan) / repair_id
    state_path = history / "pending_state.json"
    context_path = history / "repair_context.json"
    if not state_path.is_file() or not context_path.is_file():
        raise FileNotFoundError(
            f"pending repair state is missing for repair ID {repair_id}"
        )
    state = read_json(state_path)
    context = read_json(context_path)
    if state.get("schema_version") != PENDING_REPAIR_SCHEMA_VERSION:
        raise ValueError("pending repair state schema is stale")
    if state.get("status") != AGENT_CONTRACT_PENDING:
        raise ValueError("repair ID is not resumable")
    expected_state_digest = canonical_json_hash(
        {key: value for key, value in state.items() if key != "state_digest"}
    )
    if state.get("state_digest") != expected_state_digest:
        raise ValueError("pending repair state is stale or tampered")
    if sha256_file(context_path) != state.get("context_hash"):
        raise ValueError("pending repair context hash is stale or tampered")
    resolved_plan = plan_path.expanduser().resolve()
    if sha256_file(resolved_plan) != state.get("plan_hash"):
        raise ValueError("pending repair plan hash is stale or tampered")
    if context.get("plan_hash") != state.get("plan_hash"):
        raise ValueError("pending repair context plan hash is stale")
    if context.get("audit_id") != plan.get("audit_id"):
        raise ValueError("pending repair audit binding is stale")
    if context.get("workflow_kind") != (
        "batch" if isinstance(plan.get("findings"), list) else "single"
    ):
        raise ValueError("pending repair plan shape is stale")
    if package_identity(root) != state.get("package_identity"):
        raise ValueError("pending repair package identity is stale")
    expected_source_bundle_hash = state.get("source_audit_bundle_hash")
    if not isinstance(expected_source_bundle_hash, str):
        raise ValueError("pending repair source audit hash is missing")
    assert_source_audit_unchanged(
        root, plan, expected_source_bundle_hash
    )
    if plan.get("core_contract_digest") != state.get(
        "source_core_contract_digest"
    ):
        raise ValueError("pending repair core contract binding is stale")
    snapshot = Path(state["snapshot_dir"])
    candidate = Path(state["candidate_dir"])
    audit_output_dir = Path(state["reaudit_workspace_dir"])
    if not snapshot.is_dir() or not candidate.is_dir() or not audit_output_dir.is_dir():
        raise ValueError("pending repair workspace is incomplete")
    if package_hashes(snapshot) != state.get("snapshot_package_hashes"):
        raise ValueError("pending repair snapshot is stale or tampered")
    if package_hashes(candidate) != state.get("candidate_package_hashes"):
        raise ValueError("pending repair candidate is stale or tampered")
    if _pending_workspace_hashes(snapshot, candidate, audit_output_dir) != state.get(
        "workspace_hashes"
    ):
        raise ValueError("pending repair prepared workspace is stale or tampered")
    request_preview = read_json(
        audit_output_dir / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
    )
    raw_temp_dir = request_preview.get("audit_temp_dir")
    temp_dir = (
        Path(str(raw_temp_dir)).expanduser().resolve()
        if isinstance(raw_temp_dir, str) and raw_temp_dir
        else audit_output_dir / ".benchmark_audit_tmp"
    )
    if (
        temp_dir != audit_output_dir / ".benchmark_audit_tmp"
        and temp_dir.parent != audit_output_dir / ".benchmark_audit_tmp"
    ) or not temp_dir.is_dir():
        raise ValueError("pending repair temp workspace is stale")
    request = validate_agent_contract_request(candidate, temp_dir)
    if request.get("request_digest") != state.get("request", {}).get(
        "request_digest"
    ):
        raise ValueError("pending repair request binding is stale")
    assessment = agent_contract_assessment_path
    if assessment is None:
        raise ValueError(
            "resume requires a fresh --agent-contract-assessment"
        )
    assessment = assessment.expanduser().resolve()
    if assessment.is_symlink() or not assessment.is_file():
        raise ValueError("agent contract assessment is missing or unsafe")
    if assessment.is_relative_to(candidate.resolve()):
        raise ValueError(
            "agent contract assessment must remain external to the candidate"
        )
    machine_artifact = read_json(temp_dir / "deterministic_core/report.json")
    machine_contract = machine_artifact.get("contract")
    normalized_assessment = validate_agent_contract_assessment(
        read_json(assessment), machine_contract
    )
    expected_artifact_digests = {
        *request.get("static_hashes", {}).values(),
        *request.get("probe_hashes", {}).values(),
        request.get("probe_hash"),
    }
    for check in normalized_assessment["checks"]:
        for evidence in check.get("evidence", []):
            artifact_digest = evidence.get("artifact_digest") or evidence.get(
                "sha256"
            )
            if (
                artifact_digest is not None
                and artifact_digest not in expected_artifact_digests
            ):
                raise ValueError(
                    "agent contract assessment probe binding is stale"
                )
    return state, context, snapshot, candidate, audit_output_dir


def _pending_agent_contract_not_proven(reaudit: dict[str, Any]) -> bool:
    assessment = reaudit.get("agent_contract_assessment")
    machine = reaudit.get("deterministic_contract")
    if not isinstance(assessment, dict) or not isinstance(machine, dict):
        return False
    machine_statuses = {
        item.get("check_id"): item.get("status")
        for item in machine.get("checks", [])
        if isinstance(item, dict)
    }
    return any(
        isinstance(item, dict)
        and item.get("status") == "NOT_PROVEN"
        and machine_statuses.get(item.get("check_id"))
        in UNAVAILABLE_CHECK_STATUSES
        for item in assessment.get("checks", [])
    )


def _promote_pending_reaudit_output(
    audit_output_dir: Path, root: Path
) -> Path:
    """Make a resumed audit visible at the canonical external path."""

    canonical_output = reaudit_output_root(root)
    if canonical_output == audit_output_dir:
        return canonical_output
    if canonical_output.exists() or canonical_output.is_symlink():
        shutil.rmtree(canonical_output)
    canonical_output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(audit_output_dir, canonical_output)
    source_hash = sha256_path(audit_output_dir)
    promoted_hash = sha256_path(canonical_output)
    if promoted_hash != source_hash:
        raise ValueError("promoted re-audit bundle changed during publication")
    promoted_audit = canonical_output / "benchmark_audit"
    report = read_json(promoted_audit / "audit_report.json")
    manifest = read_json(promoted_audit / "audit_manifest.json")
    disposition = read_json(promoted_audit / "disposition.json")
    authenticate_audit_bundle(
        root,
        report,
        manifest,
        disposition,
        audit=promoted_audit,
    )
    return canonical_output


def _close_pending_repair_state(
    state: dict[str, Any],
    *,
    terminal_status: str,
    attempt_consumed: bool,
    history_dir: Path,
) -> None:
    state["status"] = "COMPLETED"
    state["terminal_status"] = terminal_status
    state["attempt_number"] = (
        int(state.get("attempt_number", 0)) + 1
        if attempt_consumed
        else int(state.get("attempt_number", 0))
    )
    state["attempt_consumed"] = attempt_consumed
    state["package_mutated"] = terminal_status == "REPAIRED"
    state["completed_at"] = timestamp()
    state["state_digest"] = canonical_json_hash(
        {key: value for key, value in state.items() if key != "state_digest"}
    )
    write_json(history_dir / "pending_state.json", state)


def _resume_pending_repair_attempt(
    *,
    root: Path,
    plan: dict[str, Any],
    report: dict[str, Any],
    audit_manifest: dict[str, Any],
    findings_by_id: dict[str, dict[str, Any]] | None,
    source_finding: dict[str, Any] | None,
    root_cause: str,
    source_verdict: str | None,
    state: dict[str, Any],
    context: dict[str, Any],
    snapshot: Path,
    candidate: Path,
    audit_output_dir: Path,
    agent_contract_assessment_path: Path,
    is_batch: bool,
) -> dict[str, Any]:
    """Resume the persisted candidate and finalize exactly one re-audit."""

    history = Path(state["pending_state_path"]).parent
    expected_source_bundle_hash = state.get("source_audit_bundle_hash")
    if not isinstance(expected_source_bundle_hash, str):
        raise ValueError("pending repair source audit hash is missing")
    assert_source_audit_unchanged(
        root, plan, expected_source_bundle_hash
    )
    semantic_attempt_number = int(state.get("attempt_number", 0)) + 1
    plan = context["plan"]
    operational_output_dir = reaudit_output_root(candidate)
    if operational_output_dir != audit_output_dir:
        if operational_output_dir.exists() or operational_output_dir.is_symlink():
            shutil.rmtree(operational_output_dir)
        shutil.copytree(audit_output_dir, operational_output_dir)
        _rewrite_pending_review_workspace(
            operational_output_dir,
            old_candidate=candidate,
            new_candidate=candidate,
            old_output=audit_output_dir,
            new_output=operational_output_dir,
        )
        audit_output_dir = operational_output_dir
    reaudit = run_equal_depth_review(
        candidate,
        report,
        audit_manifest,
        plan,
        original_root=root,
        agent_contract_assessment_path=agent_contract_assessment_path,
        audit_output_dir=audit_output_dir,
    )
    assert_source_audit_unchanged(
        root, plan, expected_source_bundle_hash
    )
    if reaudit.get("status") == AGENT_CONTRACT_PENDING:
        # A valid fresh assessment should never produce another preparation
        # pause.  Preserve the state and fail closed if Review does so anyway.
        raise ValueError(
            "agent contract assessment did not finalize the prepared re-audit"
        )
    if reaudit.get("status") == AGENT_ASSESSMENT_PENDING:
        return {
            "status": AGENT_ASSESSMENT_PENDING,
            "review_status": AGENT_ASSESSMENT_PENDING,
            "review_verdict": "NOT_ASSESSABLE",
            "disposition": "NOT_ASSESSABLE",
            "publishability": "EVIDENCE_PENDING",
            "publishable": False,
            "repair_state": AGENT_ASSESSMENT_PENDING,
            "attempt_consumed": False,
            "package_mutated": False,
            "message": reaudit.get(
                "message",
                "equal-depth re-audit paused for inherited paper assessment",
            ),
        }

    reaudit_score: float | None
    try:
        reaudit_score = authoritative_total_score(
            reaudit, context="re-audit"
        )
    except PolicyStop:
        reaudit_score = None
    effective_contract: dict[str, Any] | None = None
    try:
        effective_contract = resolve_publication_contract(
            reaudit.get("deterministic_contract"),
            reaudit.get("effective_deterministic_contract"),
            reaudit.get("agent_contract_assessment"),
        )
    except (TypeError, ValueError) as exc:
        raise ValueError(
            "re-audit effective deterministic contract is stale"
        ) from exc

    summary = reaudit.get("summary", {})
    verdict = summary.get("final_verdict")
    disposition_path = (
        reaudit_audit_dir(
            candidate,
            plan,
            audit_output_dir=audit_output_dir,
        )
        / "disposition.json"
    )
    disposition = (
        read_json(disposition_path) if disposition_path.is_file() else {}
    )
    route = (
        disposition.get("route")
        or summary.get("publication_route")
        or summary.get("publishability")
    )
    reaudit_findings = [
        item for item in reaudit.get("findings", []) if isinstance(item, dict)
    ]
    reaudit_audit_id = reaudit.get("audit_id")
    audit_id = reaudit_audit_id if isinstance(reaudit_audit_id, str) else None
    unresolved_severe = unresolved_severe_references(
        reaudit_findings,
        audit_id=audit_id,
    )
    residual_blocking = blocking_finding_references(
        reaudit_findings,
        audit_id=audit_id,
    )
    target_ids = (
        list(context.get("resolved_targets", []))
        if is_batch
        else (
            [source_finding["finding_id"]]
            if isinstance(source_finding, dict)
            and isinstance(source_finding.get("finding_id"), str)
            else []
        )
    )
    target_codes = {
        finding_key(item)
        for item in (findings_by_id or {}).values()
        if isinstance(item, dict)
    }
    targets_still_open = [
        target_id
        for target_id in target_ids
        if any(
            finding_key(item) in target_codes
            and finding_key(item) == finding_key(
                (findings_by_id or {}).get(target_id, {})
            )
            for item in reaudit_findings
        )
    ]
    hard_gate_free = (
        reaudit_has_no_hard_gate(reaudit)
        if "hard_gates" in reaudit
        else False
    )
    pass_evidence: dict[str, Any]
    try:
        pass_evidence = validate_authoritative_pass(reaudit)
    except ValueError as exc:
        pass_evidence = {
            "authoritative_pass": False,
            "authoritative_pass_error": str(exc),
        }
    deterministic_state = (
        effective_contract["repair_summary"]["state"]
        if effective_contract is not None
        else "INVALID"
    )
    not_proven = _pending_agent_contract_not_proven(reaudit)
    comparison = {
        "target_resolved": False,
        "reaudit_audit_id": reaudit_audit_id,
        "reaudit_count": 1,
        "reaudit_verdict": verdict,
        "publication_route": route,
        "deterministic_state": deterministic_state,
        "effective_deterministic_contract": (
            reaudit.get("effective_deterministic_contract")
        ),
        "hard_gate_free": hard_gate_free,
        "identity_preserved": (
            package_identity(candidate, directory_name=root.name)
            == context["identity"]
        ),
        "mutation_scope_allowed": True,
        "residual_blocking_finding_ids": [
            item.get("finding_id") for item in residual_blocking
        ],
        "unresolved_severe_finding_ids": [
            item.get("finding_id") for item in unresolved_severe
        ],
        "resolved_findings": target_ids,
        "targets_still_open": targets_still_open,
        "source_finding": {
            "finding_id": (
                source_finding.get("finding_id")
                if isinstance(source_finding, dict)
                else None
            ),
            "status": "OPEN",
        },
        "source_configuration": {"review_lane": report_configuration(report)},
        "reaudit_configuration": {
            "review_lane": report_configuration(reaudit)
        },
        "agent_contract_status": (
            "NOT_PROVEN" if not_proven else "APPLIED"
        ),
        "attempt_consumed": True,
        **pass_evidence,
    }
    if reaudit_score is not None:
        comparison["source_score"] = authoritative_total_score(
            report, context="source audit"
        )
        comparison["reaudit_score"] = reaudit_score
        comparison["repair_delta"] = compute_repair_delta(report, reaudit)
    else:
        comparison["repair_delta"] = compute_repair_delta(report, reaudit)

    full_pass = (
        not not_proven
        and reaudit_score is not None
        and reaudit_score >= PUBLICATION_SCORE
        and verdict == "PASS"
        and route == "PUBLISH_CANDIDATE"
        and pass_evidence.get("authoritative_pass") is True
        and deterministic_state == "CLEAN"
        and hard_gate_free
        and not context.get("unresolved_findings")
        and not targets_still_open
        and not unresolved_severe
        and package_identity(candidate, directory_name=root.name)
        == context["identity"]
    )

    assert_source_audit_unchanged(
        root, plan, expected_source_bundle_hash
    )
    reaudit_bundle = archive_reaudit_bundle(
        candidate,
        root,
        plan,
        history,
        audit_output_dir=audit_output_dir,
    )
    _promote_pending_reaudit_output(audit_output_dir, root)
    assert_source_audit_unchanged(
        root, plan, expected_source_bundle_hash
    )

    if not full_pass:
        repair_state = "PARTIALLY_REPAIRED"
        decision = "ASSISTED_FIX"
        if (
            not not_proven
            and (
                (reaudit_score is not None and reaudit_score < MINIMUM_REPAIR_SCORE)
                or not hard_gate_free
                or bool(unresolved_severe)
            )
        ):
            repair_state = "ABANDONED"
            decision = "ABANDON"
        unresolved = list(context.get("unresolved_findings", []))
        unresolved.extend(residual_blocking)
        unresolved.extend(unresolved_severe)
        if not_proven:
            unresolved.append(
                {
                    "finding_id": "__agent_contract__",
                    "reason": (
                        "Agent returned NOT_PROVEN; deterministic contract "
                        "evidence remains pending."
                    ),
                }
            )
        archive_report = reaudit
        if not_proven:
            # The retained Review bundle remains authoritative, but the
            # repair-history record must use the canonical NOT_ASSESSABLE
            # route rather than treating an evidence pause as CONDITIONAL.
            archive_report = dict(reaudit)
            archive_summary = dict(reaudit.get("summary", {}))
            archive_summary.update(
                {
                    "final_verdict": "NOT_ASSESSABLE",
                    "publication_route": "EVIDENCE_PENDING",
                    "publishability": "EVIDENCE_PENDING",
                }
            )
            archive_report["summary"] = archive_summary
            archive_report["review_verdict"] = "NOT_ASSESSABLE"
            archive_report["publishability"] = "EVIDENCE_PENDING"
        result = archive_batch_attempt(
            root=root,
            report=archive_report if not_proven else report,
            plan=plan,
            root_cause=root_cause,
            attempt_number=semantic_attempt_number,
            repair_state=repair_state,
            decision=decision,
            changes=[],
            unresolved=unresolved
            or [{"finding_id": "__batch__", "reason": "re-audit did not PASS"}],
            regressions=context.get("regression_results", []),
            comparison=comparison,
            evidence=context.get("evidence", []),
            reason=(
                "Agent contract assessment returned NOT_PROVEN; evidence "
                "pending."
                if not_proven
                else "Equal-depth re-audit did not reach PASS."
            ),
            history_dir=history,
            source_verdict=(
                "NOT_ASSESSABLE" if not_proven else source_verdict
            ),
            attempt_kind="SEMANTIC_REAUDIT",
            attempt_consumed=True,
            reaudit_bundle=reaudit_bundle,
        )
        if not_proven:
            result.update(
                {
                    "status": "NOT_ASSESSABLE",
                    "review_verdict": "NOT_ASSESSABLE",
                    "disposition": "NOT_ASSESSABLE",
                    "publishability": "EVIDENCE_PENDING",
                    "publishable": False,
                    "attempt_consumed": True,
                    "attempt_number": semantic_attempt_number,
                    "repair_state": repair_state,
                    "agent_contract_status": "NOT_PROVEN",
                }
            )
        result["repair_delta"] = comparison["repair_delta"]
        _close_pending_repair_state(
            state,
            terminal_status=result["status"],
            attempt_consumed=True,
            history_dir=history,
        )
        original_workspace = Path(state.get("original_workspace_dir", ""))
        if original_workspace.is_dir():
            cleanup_repair_workspace(original_workspace)
        return result

    repair_decision = "ASSISTED_FIX"
    repair_canonical = canonical_fields(
        "PASS",
        publishability="PUBLISH_CANDIDATE",
        repair_decision=repair_decision,
        repair_status="REPAIRED",
    )
    candidate_digest = core_contract_digest(candidate)
    repair_manifest = {
        "schema_version": "0.1",
        **repair_canonical,
        **terminal_fields("REPAIRED"),
        "repair_id": state["repair_id"],
        "status": "REPAIRED",
        "decision": repair_decision,
        "root_cause": root_cause,
        "attempt_number": semantic_attempt_number,
        "max_attempts": 2,
        "attempt_kind": "SEMANTIC_REAUDIT",
        "attempt_consumed": True,
        "finding_id": None,
        "finding_ids": target_ids,
        "repair_class": repair_decision,
        "package_identity": context["identity"],
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
            finding.get("justification", "")
            for finding in plan.get("findings", [])
            if isinstance(finding, dict)
        )
        or plan.get("justification", ""),
        "evidence": context.get("evidence", []),
        "changes": context.get("changes", []),
        "regression_tests": context.get("regression_results", []),
        "unresolved": [],
        "re_audit_comparison": {
            **comparison,
            "target_resolved": True,
        },
        "repair_delta": comparison["repair_delta"],
        "reaudit": {
            "audit_id": reaudit["audit_id"],
            "review_lane": report_configuration(reaudit),
            "verdict": verdict,
            "disposition": route,
        },
        "atomic_publish": True,
        "published_at": timestamp(),
        "reaudit_bundle": reaudit_bundle,
    }
    write_repair_reports(candidate, repair_manifest, plan, history)
    write_history_bundle(
        history,
        plan=plan,
        changes=context.get("changes", []),
        unresolved=[],
        regressions=context.get("regression_results", []),
        comparison=repair_manifest["re_audit_comparison"],
        evidence=context.get("evidence", []),
        root_cause=root_cause,
        attempt_number=semantic_attempt_number,
        status="REPAIRED",
        decision=repair_decision,
        review_verdict="PASS",
        publishability="PUBLISH_CANDIDATE",
        reaudit_bundle=reaudit_bundle,
    )
    write_attempt_manifest(
        history / "attempt_manifest.json",
        {
            "schema_version": "0.1",
            "repair_id": state["repair_id"],
            "root_cause": root_cause,
            "attempt_number": semantic_attempt_number,
            "max_attempts": 2,
            "status": "REPAIRED",
            "decision": repair_decision,
            **repair_canonical,
            "attempt_kind": "SEMANTIC_REAUDIT",
            "attempt_consumed": True,
            "audit_id": report["audit_id"],
            "finding_ids": target_ids,
            "recorded_at": timestamp(),
            **reaudit_bundle_reference_fields(reaudit_bundle),
        },
        package_mutated=False,
    )
    generated_outputs = externalize_generated_bundles(
        candidate, root, plan
    )
    atomic_publish_candidate(
        root=root,
        candidate=candidate,
        history=history,
        generated_outputs=generated_outputs,
        attempt_manifest_path=history / "attempt_manifest.json",
    )
    _close_pending_repair_state(
        state,
        terminal_status="REPAIRED",
        attempt_consumed=True,
        history_dir=history,
    )
    original_workspace = Path(state.get("original_workspace_dir", ""))
    if original_workspace.is_dir():
        cleanup_repair_workspace(original_workspace)
    return {
        "repair_id": state["repair_id"],
        "status": "REPAIRED",
        "decision": repair_decision,
        **repair_canonical,
        **terminal_fields("REPAIRED"),
        "benchmark_root": str(root),
        "history_dir": str(history),
        "history_root": str(history_root_for(root, plan)),
        "package_mutated": True,
        "root_cause": root_cause,
        "attempt_number": semantic_attempt_number,
        "attempt_consumed": True,
        "audit_id": reaudit["audit_id"],
        "resolved_findings": target_ids,
        "repair_delta": comparison["repair_delta"],
        "generated_outputs": generated_outputs,
        **reaudit_bundle_reference_fields(reaudit_bundle),
    }


def root_cause_id(report: dict[str, Any], plan: dict[str, Any]) -> str:
    value = f"{report['audit_id']}:{plan['finding_id']}"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:20]


def history_root_for(root: Path, plan: dict[str, Any] | None = None) -> Path:
    if plan is not None:
        output = repair_output_root(root, plan)
        if output is not None:
            return output / "benchmark_repair_history"
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


def write_jsonl(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        for item in rows
    ]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def read_jsonl(path: Path) -> list[Any]:
    rows: list[Any] = []
    text_value = path.read_text(encoding="utf-8")
    for line_no, line in enumerate(text_value.splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_no} is not a JSON object")
        rows.append(value)
    return rows


def collect_bundle_member_hashes(directory: Path) -> dict[str, str]:
    """Hash canonical bundle members only (not snapshot/attempt sidecars)."""

    hashes: dict[str, str] = {}
    for name in REPAIR_BUNDLE_FILES:
        if name == REPAIR_BUNDLE_MANIFEST_NAME:
            continue
        path = directory / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"bundle member missing for hash: {name}")
        hashes[name] = sha256_file(path)
    for dirname in REPAIR_BUNDLE_DIRS:
        root = directory / dirname
        if root.is_symlink() or not root.is_dir():
            raise ValueError(f"bundle directory missing for hash: {dirname}")
        for child in sorted(root.rglob("*")):
            if child.is_symlink():
                raise ValueError(f"bundle member may not be a symlink: {child}")
            if child.is_file():
                relative = child.relative_to(directory).as_posix()
                hashes[relative] = sha256_file(child)
    return hashes


def normalize_comparison_for_bundle(
    comparison: Any,
    *,
    identity: dict[str, Any],
) -> dict[str, Any]:
    """Attach identity and tolerate current re-audit or future direct mode."""

    if not isinstance(comparison, dict):
        comparison = {}
    bound = {**comparison, **identity}
    source_finding = bound.get("source_finding")
    if isinstance(source_finding, dict):
        bound["source_finding"] = {**source_finding, **identity}
    # Current path always re-audits; ticket 04 may set reaudit_performed=false.
    if "reaudit_performed" not in bound:
        if bound.get("reaudit_count") == 1 or isinstance(
            bound.get("reaudit_audit_id"), str
        ):
            bound["reaudit_performed"] = True
            bound.setdefault("verification_mode", "EQUAL_DEPTH_REAUDIT")
        elif not bound:
            bound["reaudit_performed"] = False
            bound.setdefault(
                "reaudit_skipped_reason",
                "No equal-depth re-audit was performed for this terminal attempt.",
            )
        elif bound.get("verification_mode") == "DIRECT_DETERMINISTIC":
            bound["reaudit_performed"] = False
            bound.setdefault(
                "reaudit_skipped_reason",
                "DIRECT_DETERMINISTIC publication does not invoke equal-depth re-audit.",
            )
    return bound


def render_repair_plan_markdown(plan: dict[str, Any]) -> str:
    findings = plan.get("findings") if isinstance(plan.get("findings"), list) else []
    lines = [
        "# Repair Plan",
        "",
        f"- Schema: {plan.get('schema_version')}",
        f"- Audit ID: {plan.get('audit_id')}",
        f"- Repair decision: {plan.get('repair_decision')}",
        f"- Repair status: {plan.get('repair_status')}",
        f"- Findings in batch: {len(findings)}",
        "",
        "## Assessment binding",
        "",
    ]
    assessment = plan.get("agent_repair_assessment")
    if isinstance(assessment, dict):
        lines.extend(
            [
                f"- Schema: {assessment.get('schema_version')}",
                f"- Path: {assessment.get('path')}",
                f"- Hash: {assessment.get('assessment_hash')}",
                "",
            ]
        )
    else:
        lines.extend(["- (none)", ""])
    lines.append("## Findings")
    lines.append("")
    if not findings:
        lines.append("- (none)")
    for finding in findings:
        if not isinstance(finding, dict):
            continue
        lines.append(
            f"- `{finding.get('finding_id')}` "
            f"lane={finding.get('lane') or finding.get('repair_lane')} "
            f"decision={finding.get('repair_class') or finding.get('decision')} "
            f"ops={len(finding.get('operations') or [])}"
        )
    lines.append("")
    return "\n".join(lines)


def render_repair_summary_markdown(
    *,
    manifest: dict[str, Any],
    plan: dict[str, Any],
    changes: list[Any],
    unresolved: list[Any],
    regressions: list[Any],
    comparison: dict[str, Any],
) -> str:
    reaudit = comparison.get("reaudit_performed")
    mode = comparison.get("verification_mode") or (
        "EQUAL_DEPTH_REAUDIT" if reaudit is not False else "DIRECT_DETERMINISTIC"
    )
    score = comparison.get("score")
    source_score = comparison.get("source_score")
    delta = comparison.get("score_delta")
    if delta is None and isinstance(score, (int, float)) and isinstance(
        source_score, (int, float)
    ):
        delta = round(float(score) - float(source_score), 4)
    lines = [
        "# Benchmark Repair Report",
        "",
        "## 1. Repair Summary",
        "",
        f"- Repair ID: {manifest.get('repair_id')}",
        f"- Decision: {manifest.get('decision') or manifest.get('repair_decision')}",
        f"- Status: {manifest.get('status') or manifest.get('repair_status')}",
        f"- Publishable: {manifest.get('repair_status') in SUCCESS_REPAIR_STATUSES}",
        f"- Verification mode: {mode}",
        f"- Re-audit performed: {reaudit}",
        f"- Score: {score}",
        f"- Score delta: {delta}",
        "",
        "## 2. Input Audit",
        "",
        f"- Source audit: {manifest.get('source_audit_id') or plan.get('audit_id')}",
        f"- Package identity: {json.dumps(plan.get('package_identity') or {}, ensure_ascii=False, sort_keys=True)}",
        "",
        "## 3. Repair Configuration",
        "",
        f"- Attempt: {manifest.get('attempt_number')}",
        f"- Root cause: {manifest.get('root_cause')}",
        f"- Repair class: {manifest.get('repair_class')}",
        "",
        "## 4. Findings Selected",
        "",
    ]
    findings = plan.get("findings") if isinstance(plan.get("findings"), list) else []
    if findings:
        for finding in findings:
            if isinstance(finding, dict):
                lines.append(f"- `{finding.get('finding_id')}`")
    elif manifest.get("finding_id"):
        lines.append(f"- `{manifest.get('finding_id')}`")
    else:
        lines.append("- (none)")
    lines.extend(["", "## 5. Applied Changes", ""])
    if changes:
        for change in changes:
            if isinstance(change, dict):
                lines.append(
                    f"- `{change.get('operation_id')}` {change.get('file')} "
                    f"({change.get('operation')})"
                )
    else:
        lines.append("- (none)")
    lines.extend(["", "## 6. Abandoned or Unrepairable Findings", ""])
    if unresolved:
        for item in unresolved:
            if isinstance(item, dict):
                lines.append(f"- `{item.get('finding_id')}`: {item.get('reason')}")
    else:
        lines.append("- (none)")
    lines.extend(["", "## 7. Regression Test Results", ""])
    if regressions:
        for item in regressions:
            if not isinstance(item, dict):
                continue
            spec = item.get("specification") if isinstance(item.get("specification"), dict) else {}
            lines.append(
                f"- `{spec.get('id')}` before={item.get('before_passed')} "
                f"after={item.get('after_passed')}"
            )
    else:
        lines.append("- (none)")
    lines.extend(
        [
            "",
            "## 8. Re-audit Comparison",
            "",
            f"- Verdict: {comparison.get('reaudit_verdict')}",
            f"- Route: {comparison.get('publication_route')}",
            f"- Reason: {comparison.get('reaudit_skipped_reason') or comparison.get('reason') or '(n/a)'}",
            "",
            "## 9. Unresolved Findings",
            "",
            f"- Count: {len(unresolved)}",
            "",
            "## 10. Rollback Status",
            "",
            f"- Rolled back: {manifest.get('status') in {'ROLLED_BACK', 'INFRASTRUCTURE_BLOCKED'}}",
            "",
            "## 11. Scope and Limitations",
            "",
            "- Harbor packages never receive generated repair artifacts.",
            "- Bundle and history remain run-local under repair/.",
            "",
            "## 12. Repair Log Summary",
            "",
            f"- Operations applied: {len(changes)}",
            f"- Regressions recorded: {len(regressions)}",
            "",
        ]
    )
    return "\n".join(lines)


def write_bundle_sidecar_dirs(
    destination: Path,
    *,
    changes: list[Any],
    evidence_items: list[Any],
    published: bool,
    log_text: str,
) -> None:
    patches = destination / "patches"
    evidence_dir = destination / "evidence"
    logs = destination / "logs"
    patches.mkdir(parents=True, exist_ok=True)
    evidence_dir.mkdir(parents=True, exist_ok=True)
    logs.mkdir(parents=True, exist_ok=True)
    write_json(
        destination / REPAIR_BUNDLE_PATCH_INDEX,
        {
            "schema_version": "0.1",
            "files": changes,
            "atomic_publish": published,
        },
    )
    for change in changes:
        if not isinstance(change, dict):
            continue
        operation_id = str(change.get("operation_id") or "operation")
        safe_name = "".join(
            ch if ch.isalnum() or ch in {"-", "_"} else "_"
            for ch in operation_id
        )
        patch_path = patches / f"{safe_name}.patch"
        patch_path.write_text(
            "\n".join(
                [
                    f"--- a/{change.get('file')}",
                    f"+++ b/{change.get('file')}",
                    f"# operation_id: {operation_id}",
                    f"# operation: {change.get('operation')}",
                    f"# before_hash: {change.get('before_hash')}",
                    f"# after_hash: {change.get('after_hash')}",
                    f"# applied: {published or True}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    write_json(destination / REPAIR_BUNDLE_EVIDENCE_RECORDS, evidence_items)
    (destination / REPAIR_BUNDLE_LOG_RELATIVE).write_text(log_text, encoding="utf-8")


def emit_repair_bundle(
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
    report_payload: dict[str, Any] | None = None,
    history_dir: Path | None = None,
    reaudit_bundle: dict[str, Any] | None = None,
) -> None:
    """Write the canonical run-local repair bundle tree and validate it."""

    destination.mkdir(parents=True, exist_ok=True)
    repair_status = status if status in REPAIR_STATUSES else "ABANDONED"
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
    change_rows = list(changes) if isinstance(changes, list) else []
    unresolved_rows = list(unresolved) if isinstance(unresolved, list) else []
    regression_rows = list(regressions) if isinstance(regressions, list) else []
    bound_unresolved = [{**item, **identity} for item in unresolved_rows]
    bound_comparison = normalize_comparison_for_bundle(comparison, identity=identity)
    bound_plan = {**plan, **canonical, **identity}
    evidence_items = (
        list(evidence.values()) if isinstance(evidence, dict) else list(evidence or [])
    )
    if not evidence_items:
        reason = (
            bound_unresolved[0].get("reason")
            if bound_unresolved and isinstance(bound_unresolved[0], dict)
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
    published = repair_status in SUCCESS_REPAIR_STATUSES
    report = dict(report_payload or {})
    report.update(canonical)
    report.update(identity)
    report.setdefault("schema_version", "0.1")
    report["root_cause"] = root_cause
    report["attempt_number"] = attempt_number
    report["status"] = status
    report["decision"] = decision
    report["changes"] = change_rows
    report["unresolved"] = bound_unresolved
    report["regression_tests"] = regression_rows
    report["re_audit_comparison"] = bound_comparison
    report["evidence"] = evidence_items
    if history_dir is not None:
        report["history_dir"] = str(history_dir)
    report.update(reaudit_bundle_reference_fields(reaudit_bundle))

    write_json(destination / "repair_plan.json", bound_plan)
    write_jsonl(destination / "changes.jsonl", change_rows)
    write_jsonl(destination / "unresolved_findings.jsonl", bound_unresolved)
    write_json(destination / "regression_tests.json", regression_rows)
    write_json(destination / "re_audit_comparison.json", bound_comparison)
    write_json(destination / "repair_report.json", report)
    (destination / "repair_plan.md").write_text(
        render_repair_plan_markdown(bound_plan), encoding="utf-8"
    )
    (destination / "repair_summary.md").write_text(
        render_repair_summary_markdown(
            manifest=report,
            plan=bound_plan,
            changes=change_rows,
            unresolved=bound_unresolved,
            regressions=regression_rows,
            comparison=bound_comparison,
        ),
        encoding="utf-8",
    )
    log_text = (
        f"{timestamp()}\tINFO\tdecision={decision}\tstatus={status}"
        f"\trepair_status={repair_status}\n"
    )
    write_bundle_sidecar_dirs(
        destination,
        changes=change_rows,
        evidence_items=evidence_items,
        published=published,
        log_text=log_text,
    )
    # Drop any legacy deliverable names if a prior writer left them behind.
    for legacy in (
        "changes.json",
        "unresolved.json",
        "regression_results.json",
        "patch.json",
        "evidence.json",
        "repair.log",
        "history.json",
        "repair_report.md",
    ):
        legacy_path = destination / legacy
        if legacy_path.is_file() and not legacy_path.is_symlink():
            legacy_path.unlink()

    source_audit = plan.get("source_audit") if isinstance(plan.get("source_audit"), dict) else {}
    assessment = (
        plan.get("agent_repair_assessment")
        if isinstance(plan.get("agent_repair_assessment"), dict)
        else {}
    )
    a0 = plan.get("a0_content_root") or plan.get("content_root") or source_audit.get(
        "a0_content_root"
    )
    # Finalize the machine-readable report before hashing so the manifest can
    # bind stable bytes for every member except itself.
    report["bundle_files"] = list(REPAIR_BUNDLE_FILES)
    report["bundle_complete"] = True
    report["history_dir"] = (
        str(history_dir) if history_dir is not None else str(destination)
    )
    write_json(destination / "repair_report.json", report)
    member_hashes = collect_bundle_member_hashes(destination)
    manifest = {
        "schema_version": "1.0",
        **canonical,
        **identity,
        "root_cause": root_cause,
        "attempt_number": attempt_number,
        "status": status,
        "decision": decision,
        "bundle_files": list(REPAIR_BUNDLE_FILES),
        "bundle_dirs": list(REPAIR_BUNDLE_DIRS),
        "bundle_complete": True,
        "bundle_hashes": member_hashes,
        "bundle_digest": canonical_json_hash(member_hashes),
        "history_dir": report["history_dir"],
        "a0_binding": a0,
        "source_audit_binding": {
            "audit_id": plan.get("audit_id"),
            "source_audit": source_audit,
        },
        "assessment_binding": assessment,
        "publication_record": {
            "repair_status": repair_status,
            "publishability": publishability,
            "atomic_publish": published,
            "verification_mode": bound_comparison.get("verification_mode"),
            "reaudit_performed": bound_comparison.get("reaudit_performed"),
        },
        "history_link": {
            "history_dir": report["history_dir"],
        },
    }
    manifest.update(reaudit_bundle_reference_fields(reaudit_bundle))
    if report_payload and isinstance(report_payload.get("repair_id"), str):
        manifest["repair_id"] = report_payload["repair_id"]
    write_json(destination / REPAIR_BUNDLE_MANIFEST_NAME, manifest)
    validate_fixed_bundle(destination)


def validate_fixed_bundle(directory: Path) -> None:
    missing = [
        name
        for name in REPAIR_BUNDLE_FILES
        if not (directory / name).is_file() or (directory / name).is_symlink()
    ]
    if missing:
        raise ValueError(f"incomplete fixed repair bundle: {missing}")
    missing_dirs = [
        name
        for name in REPAIR_BUNDLE_DIRS
        if not (directory / name).is_dir() or (directory / name).is_symlink()
    ]
    if missing_dirs:
        raise ValueError(f"incomplete fixed repair bundle dirs: {missing_dirs}")
    legacy = [
        name
        for name in (
            "changes.json",
            "unresolved.json",
            "regression_results.json",
            "patch.json",
            "evidence.json",
            "repair.log",
            "history.json",
        )
        if (directory / name).exists()
    ]
    if legacy:
        raise ValueError(f"legacy repair bundle deliverables present: {legacy}")
    log_path = directory / REPAIR_BUNDLE_LOG_RELATIVE
    if not log_path.is_file() or log_path.is_symlink():
        raise ValueError(f"missing {REPAIR_BUNDLE_LOG_RELATIVE}")
    values: dict[str, Any] = {
        "repair_summary.md": (directory / "repair_summary.md").read_text(
            encoding="utf-8"
        ),
        "repair_plan.md": (directory / "repair_plan.md").read_text(encoding="utf-8"),
        "repair_report.json": read_json(directory / "repair_report.json"),
        "repair_plan.json": read_json(directory / "repair_plan.json"),
        "changes.jsonl": read_jsonl(directory / "changes.jsonl"),
        "unresolved_findings.jsonl": read_jsonl(
            directory / "unresolved_findings.jsonl"
        ),
        "regression_tests.json": read_json(directory / "regression_tests.json"),
        "re_audit_comparison.json": read_json(
            directory / "re_audit_comparison.json"
        ),
        REPAIR_BUNDLE_PATCH_INDEX: read_json(
            directory / REPAIR_BUNDLE_PATCH_INDEX
        ),
        REPAIR_BUNDLE_EVIDENCE_RECORDS: read_json(
            directory / REPAIR_BUNDLE_EVIDENCE_RECORDS
        ),
        "repair_manifest.json": read_json(
            directory / REPAIR_BUNDLE_MANIFEST_NAME
        ),
    }
    expected_types = {
        "repair_report.json": dict,
        "repair_plan.json": dict,
        "changes.jsonl": list,
        "unresolved_findings.jsonl": list,
        "regression_tests.json": list,
        "re_audit_comparison.json": dict,
        REPAIR_BUNDLE_PATCH_INDEX: dict,
        REPAIR_BUNDLE_EVIDENCE_RECORDS: list,
        "repair_manifest.json": dict,
    }
    invalid_types = [
        name
        for name, expected in expected_types.items()
        if not isinstance(values.get(name), expected)
    ]
    if invalid_types:
        raise ValueError(f"fixed repair bundle has invalid types: {invalid_types}")
    repair_log = log_path.read_text(encoding="utf-8")
    validate_repair_bundle_semantics(values, repair_log=repair_log)
    manifest = values["repair_manifest.json"]
    if (
        manifest.get("bundle_complete") is not True
        or manifest.get("bundle_files") != list(REPAIR_BUNDLE_FILES)
    ):
        raise ValueError(
            "fixed repair repair_manifest.json does not attest completeness"
        )
    expected_hashes = collect_bundle_member_hashes(directory)
    if manifest.get("bundle_hashes") != expected_hashes:
        raise ValueError("fixed repair bundle hashes are stale or incomplete")
    if manifest.get("bundle_digest") != canonical_json_hash(expected_hashes):
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
    reaudit_bundle: dict[str, Any] | None = None,
) -> None:
    emit_repair_bundle(
        destination,
        plan=plan,
        changes=changes,
        unresolved=unresolved,
        regressions=regressions,
        comparison=comparison,
        evidence=evidence,
        root_cause=root_cause,
        attempt_number=attempt_number,
        status=status,
        decision=decision,
        review_verdict=review_verdict,
        publishability=publishability,
        history_dir=destination,
        reaudit_bundle=reaudit_bundle,
    )


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
        unresolved=[{
            "finding_id": plan.get("finding_id") or "__control__",
            "reason": stop.reason,
        }],
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
        "recorded_at": timestamp(),
    }
    write_attempt_manifest(
        destination / "attempt_manifest.json",
        manifest,
        package_mutated=False,
    )
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
        "package_mutated": False,
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
    emit_repair_bundle(
        report_dir,
        plan=plan,
        changes=manifest.get("changes", []),
        unresolved=manifest.get("unresolved", []),
        regressions=manifest.get("regression_tests", []),
        comparison=manifest.get("re_audit_comparison", {}),
        evidence=manifest.get("evidence", []),
        root_cause=str(manifest.get("root_cause") or ""),
        attempt_number=int(manifest.get("attempt_number") or 0),
        status=str(manifest.get("status") or manifest.get("repair_status")),
        decision=str(manifest.get("decision") or manifest.get("repair_decision")),
        review_verdict=str(manifest["review_verdict"]),
        publishability=str(manifest["publishability"]),
        report_payload=manifest,
        history_dir=history_dir,
        reaudit_bundle=manifest.get("reaudit_bundle"),
    )
    # Refresh caller-visible comparison with normalized fields.
    written = read_json(report_dir / "repair_report.json")
    manifest.update(
        {
            key: written[key]
            for key in (
                "review_verdict",
                "publishability",
                "repair_decision",
                "repair_status",
                "evidence",
                "re_audit_comparison",
                "bundle_files",
                "bundle_complete",
                "history_dir",
            )
            if key in written
        }
    )
    written_manifest = read_json(report_dir / REPAIR_BUNDLE_MANIFEST_NAME)
    for key in ("bundle_hashes", "bundle_digest"):
        if key in written_manifest:
            manifest[key] = written_manifest[key]




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

    reject_removed_fixture_fields(plan, context="repair plan")
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
    if RUN_DIRECTORY.get() is not None:
        try:
            validate_deterministic_contract(report.get("deterministic_contract"))
            validate_repair_plan_binding(
                report, deterministic_binding_view(plan)
            )
        except ValueError as exc:
            raise PolicyStop(
                "BLOCKED_EVIDENCE",
                f"repair plan binding is invalid: {exc}",
            ) from exc
        return source_audit
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
    try:
        validate_deterministic_contract(report.get("deterministic_contract"))
        validate_repair_plan_binding(
            report, deterministic_binding_view(plan)
        )
    except ValueError as exc:
        raise PolicyStop(
            "BLOCKED_EVIDENCE",
            f"repair plan binding is invalid: {exc}",
        ) from exc
    return source_audit


def validate_fresh_audit_batch(
    root: Path,
    plan: dict[str, Any],
    attestation_path: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]]]:
    audit = source_audit_dir(root, plan)
    if RUN_DIRECTORY.get() is None:
        validate_audit_attestation(root, audit, attestation_path)
    report = read_json(audit / "audit_report.json")
    manifest = read_json(audit / "audit_manifest.json")
    disposition = read_json(audit / "disposition.json")
    authenticate_audit_bundle(
        root, report, manifest, disposition, audit=audit
    )
    require_validated_paper_assessment(report)
    report_configuration(report)
    if plan["audit_id"] != report.get("audit_id"):
        raise ValueError("stale audit: plan audit_id is not authoritative")
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
            finding["finding_id"] not in findings_by_id
            or findings_by_id[finding["finding_id"]].get("status") != "OPEN"
        ):
            raise ValueError(
                f"repair plan finding is not open in the audit: "
                f"{finding['finding_id']}"
            )
    if RUN_DIRECTORY.get() is None:
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
    reaudit_bundle: dict[str, Any] | None = None,
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
        reaudit_bundle=reaudit_bundle,
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
    write_attempt_manifest(
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
            "reason": reason,
            "recorded_at": timestamp(),
            **reaudit_bundle_reference_fields(reaudit_bundle),
        },
        package_mutated=False,
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
        "package_mutated": False,
        "unresolved": unresolved,
        "repair_delta": comparison.get("repair_delta")
        if isinstance(comparison, dict)
        else None,
        "reason": reason,
        **reaudit_bundle_reference_fields(reaudit_bundle),
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
        "package_mutated": False,
        "unresolved": read_jsonl(history_dir / "unresolved_findings.jsonl"),
        "repair_delta": None,
        "reason": manifest.get("reason"),
    }


def publish_direct_deterministic_batch(
    *,
    root: Path,
    plan: dict[str, Any],
    report: dict[str, Any],
    audit_manifest: dict[str, Any],
    identity: dict[str, Any],
    root_cause: str,
    attempt_number: int,
    repair_id: str,
    workspace: Path,
    snapshot: Path,
    candidate: Path,
    history: Path,
    changes: list[dict[str, Any]],
    regression_results: list[dict[str, Any]],
    resolved_targets: list[str],
    evidence: list[dict[str, Any]],
    candidate_digest: str,
    expected_source_bundle_hash: str,
    eligibility_reason: str,
) -> dict[str, Any]:
    """Atomically publish a narrowly eligible D-only AUTO_FIX candidate.

    Does not invoke equal-depth Review and does not consume the two-attempt
    re-audit budget. Fail-closed on stale source audit, identity drift,
    mutation boundary escape, or atomic swap failure.
    """

    assert_source_audit_unchanged(root, plan, expected_source_bundle_hash)
    if package_identity(candidate, directory_name=root.name) != identity:
        raise ValueError("repair changed the Harbor package identity")
    operation_files = {
        item["file"] for item in changes if isinstance(item, dict)
    }
    assert_mutation_boundary(snapshot, candidate, operation_files)
    if not regression_results or not all(
        item.get("before_passed") is False and item.get("after_passed") is True
        for item in regression_results
        if isinstance(item, dict)
    ):
        raise ValueError(
            "DIRECT_DETERMINISTIC publisher requires fail-before/pass-after "
            "regression evidence"
        )
    comparison = build_direct_deterministic_comparison(
        report=report,
        plan=plan,
        identity=identity,
        resolved_targets=resolved_targets,
        regression_results=regression_results,
    )
    comparison["eligibility_reason"] = eligibility_reason
    repair_canonical = canonical_fields(
        "PASS",
        publishability="PUBLISH_CANDIDATE",
        repair_decision="AUTO_FIX",
        repair_status="REPAIRED",
    )
    repair_manifest = {
        "schema_version": "0.1",
        **repair_canonical,
        "repair_id": repair_id,
        "status": "REPAIRED",
        "decision": "AUTO_FIX",
        **terminal_fields("REPAIRED"),
        "root_cause": root_cause,
        "attempt_number": attempt_number,
        "max_attempts": 2,
        "attempt_kind": "DIRECT_DETERMINISTIC",
        "attempt_consumed": False,
        "verification_mode": "DIRECT_DETERMINISTIC",
        "finding_id": None,
        "finding_ids": resolved_targets,
        "repair_class": "AUTO_FIX",
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
            finding["justification"]
            for finding in plan.get("findings", [])
            if isinstance(finding, dict)
        ),
        "evidence": evidence,
        "changes": changes,
        "regression_tests": regression_results,
        "unresolved": [],
        "re_audit_comparison": comparison,
        "repair_delta": {
            "source_score": comparison.get("source_score"),
            "reaudit_score": None,
            "score_delta": None,
            "verification_mode": "DIRECT_DETERMINISTIC",
        },
        "reaudit": {
            "audit_id": None,
            "review_lane": None,
            "verdict": None,
            "disposition": None,
            "performed": False,
            "skipped_reason": comparison["reaudit_skipped_reason"],
        },
        "atomic_publish": True,
        "published_at": timestamp(),
    }
    history.mkdir(parents=True, exist_ok=True)
    write_repair_reports(candidate, repair_manifest, plan, history)
    if snapshot.exists():
        snapshot.rename(history / "snapshot")
    write_history_bundle(
        history,
        plan=plan,
        changes=changes,
        unresolved=[],
        regressions=regression_results,
        comparison=comparison,
        evidence=evidence,
        root_cause=root_cause,
        attempt_number=attempt_number,
        status="REPAIRED",
        decision="AUTO_FIX",
        review_verdict="PASS",
        publishability="PUBLISH_CANDIDATE",
        reaudit_bundle=None,
    )
    write_attempt_manifest(
        history / "attempt_manifest.json",
        {
            "schema_version": "0.1",
            "repair_id": repair_id,
            "root_cause": root_cause,
            "attempt_number": attempt_number,
            "max_attempts": 2,
            "status": "REPAIRED",
            "decision": "AUTO_FIX",
            **repair_canonical,
            "attempt_kind": "DIRECT_DETERMINISTIC",
            "attempt_consumed": False,
            "verification_mode": "DIRECT_DETERMINISTIC",
            "audit_id": report["audit_id"],
            "finding_ids": resolved_targets,
            "error": None,
            "snapshot_preserved": True,
            "candidate_preserved": False,
            "recorded_at": timestamp(),
        },
        package_mutated=False,
    )
    assert_source_audit_unchanged(root, plan, expected_source_bundle_hash)
    generated_outputs = externalize_generated_bundles(
        candidate, root, plan, require_reaudit=False
    )
    atomic_publish_candidate(
        root=root,
        candidate=candidate,
        history=history,
        generated_outputs=generated_outputs,
        attempt_manifest_path=history / "attempt_manifest.json",
    )
    if workspace.exists():
        cleanup_repair_workspace(workspace)
    return {
        "repair_id": repair_id,
        "status": "REPAIRED",
        "decision": "AUTO_FIX",
        **repair_canonical,
        **terminal_fields("REPAIRED"),
        "benchmark_root": str(root),
        "history_dir": str(history),
        "history_root": str(history_root_for(root, plan)),
        "package_mutated": True,
        "root_cause": root_cause,
        "attempt_number": attempt_number,
        "attempt_consumed": False,
        "attempt_kind": "DIRECT_DETERMINISTIC",
        "verification_mode": "DIRECT_DETERMINISTIC",
        "resolved_findings": resolved_targets,
        "repair_delta": repair_manifest["repair_delta"],
        "generated_outputs": generated_outputs,
        "reaudit_performed": False,
    }


def repair_batch(
    root: Path,
    plan: dict[str, Any],
    attestation_path: Path,
    plan_path: Path,
    *,
    resume_repair_id: str | None = None,
    agent_contract_assessment_path: Path | None = None,
) -> dict[str, Any]:
    plan["package_identity"] = package_identity(root)
    pending_state: tuple[
        dict[str, Any], dict[str, Any], Path, Path, Path
    ] | None = None
    if resume_repair_id is not None:
        # Check resumability before validating the mutable live package.  A
        # completed resume must fail closed even if publication changed the
        # package hashes since the original pending snapshot.
        pending_state = _read_pending_repair(
            root,
            plan,
            resume_repair_id,
            plan_path,
            agent_contract_assessment_path,
        )
    try:
        report, audit_manifest, findings_by_id = validate_fresh_audit_batch(
            root, plan, attestation_path
        )
        load_and_bind_agent_repair_assessment(
            root, plan, report, plan_path=plan_path
        )
    except PolicyStop as stop:
        raise ValueError(
            "repair plan or source audit authentication failed: "
            f"{stop.status}: {stop.reason}"
        ) from stop
    except FileNotFoundError as exc:
        raise ValueError(
            f"repair plan or source audit authentication failed: "
            f"BLOCKED_EVIDENCE: {exc}"
        ) from exc
    root_cause = batch_root_cause(report, plan)
    source_verdict = report.get("summary", {}).get("final_verdict")
    if resume_repair_id is not None:
        assert pending_state is not None
        state, context, snapshot, candidate, audit_output_dir = pending_state
        if state.get("root_cause") != root_cause:
            raise ValueError("pending repair root-cause binding is stale")
        return _resume_pending_repair_attempt(
            root=root,
            plan=plan,
            report=report,
            audit_manifest=audit_manifest,
            findings_by_id=findings_by_id,
            source_finding=None,
            root_cause=root_cause,
            source_verdict=source_verdict,
            state=state,
            context=context,
            snapshot=snapshot,
            candidate=candidate,
            audit_output_dir=audit_output_dir,
            agent_contract_assessment_path=(
                agent_contract_assessment_path  # type: ignore[arg-type]
            ),
            is_batch=True,
        )
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
    reaudit_started = False
    reaudit_bundle: dict[str, Any] | None = None
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
        expected_source_bundle_hash = source_audit_bundle_hash(root, plan)
        assert_source_audit_unchanged(
            root, plan, expected_source_bundle_hash
        )
        assert_mutation_boundary(snapshot, candidate, operation_files)
        if package_identity(candidate, directory_name=root.name) != identity:
            raise ValueError("repair changed the Harbor package identity")
        direct_ok, direct_reason = evaluate_direct_deterministic_eligibility(
            plan,
            report,
            unresolved_findings=unresolved_findings,
            findings_by_id=findings_by_id,
        )
        if direct_ok:
            control_stage = "direct_deterministic_publish"
            return publish_direct_deterministic_batch(
                root=root,
                plan=plan,
                report=report,
                audit_manifest=audit_manifest,
                identity=identity,
                root_cause=root_cause,
                attempt_number=attempt_number,
                repair_id=repair_id,
                workspace=workspace,
                snapshot=snapshot,
                candidate=candidate,
                history=history,
                changes=changes,
                regression_results=regression_results,
                resolved_targets=resolved_targets,
                evidence=list(evidence_all.values()),
                candidate_digest=candidate_digest,
                expected_source_bundle_hash=expected_source_bundle_hash,
                eligibility_reason=direct_reason,
            )
        control_stage = "equal_depth_reaudit"
        reaudit_started = True
        reaudit = run_equal_depth_review(
            candidate,
            report,
            audit_manifest,
            plan,
            original_root=root,
        )
        assert_source_audit_unchanged(
            root, plan, expected_source_bundle_hash
        )
        if reaudit.get("status") == AGENT_CONTRACT_PENDING:
            return persist_pending_repair(
                root=root,
                plan=plan,
                plan_path=plan_path,
                report=report,
                audit_manifest=audit_manifest,
                findings_by_id=findings_by_id,
                source_finding=None,
                root_cause=root_cause,
                attempt_number=attempt_number - 1,
                repair_id=repair_id,
                workspace=workspace,
                snapshot=snapshot,
                candidate=candidate,
                audit_output_dir=Path(reaudit["audit_output_dir"]),
                changes=changes,
                regression_results=regression_results,
                resolved_targets=resolved_targets,
                unresolved_findings=unresolved_findings,
                evidence=list(evidence_all.values()),
                workflow_kind="batch",
                identity=identity,
            )
        if reaudit.get("status") == AGENT_ASSESSMENT_PENDING:
            if workspace.exists():
                cleanup_repair_workspace(workspace)
            return {
                "repair_id": repair_id,
                "status": AGENT_ASSESSMENT_PENDING,
                "review_status": AGENT_ASSESSMENT_PENDING,
                "review_verdict": "NOT_ASSESSABLE",
                "disposition": "NOT_ASSESSABLE",
                "publishability": "EVIDENCE_PENDING",
                "publishable": False,
                "repair_state": AGENT_ASSESSMENT_PENDING,
                "attempt_number": max(attempt_number - 1, 0),
                "attempt_consumed": False,
                "package_mutated": False,
                "message": reaudit.get(
                    "message",
                    "equal-depth re-audit paused for inherited paper assessment",
                ),
            }
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
        if history.exists() and not (history / "attempt_manifest.json").exists():
            shutil.rmtree(history)
        history.mkdir(parents=True, exist_ok=True)
        if reaudit_started and reaudit_audit_dir(
            candidate, plan, anchor_root=root
        ).is_dir():
            reaudit_bundle = archive_reaudit_bundle(
                candidate, root, plan, history
            )
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
            reaudit_bundle=reaudit_bundle,
        )
        if workspace.exists():
            cleanup_repair_workspace(workspace)
        return result

    summary = reaudit.get("summary", {})
    verdict = summary.get("final_verdict")
    # The publish route lives in disposition.json ``route`` (and the
    # finalizer's ``summary.publication_route`` / ``summary.publishability``).
    # ``summary.disposition`` holds the VERDICT, not the route, so it must not
    # be used here (mirrors read_ext_disposition and finalize_audit_output).
    reaudit_disposition_path = reaudit_audit_dir(
        candidate, plan, anchor_root=root
    ) / "disposition.json"
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
    severe_residuals = unresolved_severe_references(
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
    try:
        deterministic = resolve_publication_contract(
            reaudit.get("deterministic_contract"),
            reaudit.get("effective_deterministic_contract"),
            reaudit.get("agent_contract_assessment"),
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
        "verification_mode": "EQUAL_DEPTH_REAUDIT",
        "reaudit_performed": True,
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
        existing_residual_ids = {
            item.get("finding_id")
            for item in reaudit_unresolved
            if isinstance(item, dict)
        }
        for severe_residual in severe_residuals:
            if severe_residual["finding_id"] not in existing_residual_ids:
                reaudit_unresolved.append(severe_residual)
                existing_residual_ids.add(severe_residual["finding_id"])
        history.mkdir(parents=True, exist_ok=True)
        reaudit_bundle = archive_reaudit_bundle(
            candidate, root, plan, history
        )
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
            reaudit_bundle=reaudit_bundle,
        )
        result["repair_delta"] = repair_delta
        if workspace.exists():
            cleanup_repair_workspace(workspace)
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
    assert_source_audit_unchanged(
        root, plan, expected_source_bundle_hash
    )
    rebase_audit_paths(candidate, root, plan)
    reaudit_report_path = reaudit_audit_dir(
        candidate, plan, anchor_root=root
    ) / "audit_report.json"
    reaudit_manifest_path = reaudit_audit_dir(
        candidate, plan, anchor_root=root
    ) / "audit_manifest.json"
    repair_manifest.update(
        {
            "reaudit_audit_id": reaudit["audit_id"],
            "reaudit_report_hash": sha256_file(reaudit_report_path),
            "reaudit_manifest_hash": sha256_file(reaudit_manifest_path),
        }
    )
    history.mkdir(parents=True)
    reaudit_bundle = archive_reaudit_bundle(
        candidate, root, plan, history
    )
    repair_manifest["reaudit_bundle"] = reaudit_bundle
    write_repair_reports(candidate, repair_manifest, plan, history)
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
        reaudit_bundle=reaudit_bundle,
    )
    write_attempt_manifest(
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
            **reaudit_bundle_reference_fields(reaudit_bundle),
        },
        package_mutated=False,
    )
    generated_outputs = externalize_generated_bundles(candidate, root, plan)
    atomic_publish_candidate(
        root=root,
        candidate=candidate,
        history=history,
        generated_outputs=generated_outputs,
        attempt_manifest_path=history / "attempt_manifest.json",
    )
    assert_source_audit_unchanged(
        root, plan, expected_source_bundle_hash
    )
    cleanup_repair_workspace(workspace)
    return {
        "repair_id": repair_id,
        "status": "REPAIRED",
        "decision": "ASSISTED_FIX",
        **repair_canonical,
        **terminal_fields("REPAIRED"),
        "benchmark_root": str(root),
        "history_dir": str(history),
        "history_root": str(history_root_for(root, plan)),
        "package_mutated": True,
        "root_cause": root_cause,
        "attempt_number": attempt_number,
        "audit_id": reaudit["audit_id"],
        "resolved_findings": resolved_targets,
        "repair_delta": repair_delta,
        "generated_outputs": generated_outputs,
        **reaudit_bundle_reference_fields(reaudit_bundle),
    }


def _repair_locked(
    root: Path,
    plan_path: Path,
    attestation_path: Path,
    audit_dir: Path | None = None,
    repair_output_dir: Path | None = None,
    *,
    resume_repair_id: str | None = None,
    agent_contract_assessment_path: Path | None = None,
) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.is_dir() or not (root / "instruction.md").is_file() or not (
        root / "tests"
    ).is_dir():
        raise ValueError("input must be a Harbor 题包 with instruction.md and tests/")
    if agent_contract_assessment_path is not None and resume_repair_id is None:
        raise ValueError(
            "--agent-contract-assessment requires --resume-repair-id"
        )
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
        return repair_batch(
            root,
            plan,
            attestation_path,
            plan_path,
            resume_repair_id=resume_repair_id,
            agent_contract_assessment_path=agent_contract_assessment_path,
        )
    pending_state: tuple[
        dict[str, Any], dict[str, Any], Path, Path, Path
    ] | None = None
    if resume_repair_id is not None:
        pending_state = _read_pending_repair(
            root,
            plan,
            resume_repair_id,
            plan_path,
            agent_contract_assessment_path,
        )
    try:
        report, audit_manifest, finding = validate_fresh_audit(
            root, plan, attestation_path
        )
    except PolicyStop as stop:
        if resume_repair_id is not None:
            raise ValueError(
                "pending repair live package or source audit is stale"
            ) from stop
        report = read_json(source_audit_dir(root, plan) / "audit_report.json")
        root_cause = root_cause_id(report, plan)
        return record_control_stop(root, report, plan, root_cause, stop)
    expected_source_bundle_hash = source_audit_bundle_hash(root, plan)
    root_cause = root_cause_id(report, plan)
    if resume_repair_id is not None:
        assert pending_state is not None
        state, context, snapshot, candidate, audit_output_dir = pending_state
        if state.get("root_cause") != root_cause:
            raise ValueError("pending repair root-cause binding is stale")
        return _resume_pending_repair_attempt(
            root=root,
            plan=plan,
            report=report,
            audit_manifest=audit_manifest,
            findings_by_id=None,
            source_finding=finding,
            root_cause=root_cause,
            source_verdict=report.get("summary", {}).get("final_verdict"),
            state=state,
            context=context,
            snapshot=snapshot,
            candidate=candidate,
            audit_output_dir=audit_output_dir,
            agent_contract_assessment_path=(
                agent_contract_assessment_path  # type: ignore[arg-type]
            ),
            is_batch=False,
        )
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
            "package_mutated": False,
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
    reaudit_started = False
    reaudit_bundle: dict[str, Any] | None = None
    reaudit: dict[str, Any] | None = None
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
        reaudit_started = True
        reaudit = run_equal_depth_review(
            candidate,
            report,
            audit_manifest,
            plan,
            original_root=root,
        )
        if reaudit.get("status") == AGENT_CONTRACT_PENDING:
            return persist_pending_repair(
                root=root,
                plan=plan,
                plan_path=plan_path,
                report=report,
                audit_manifest=audit_manifest,
                findings_by_id=None,
                source_finding=finding,
                root_cause=root_cause,
                attempt_number=attempt_number - 1,
                repair_id=repair_id,
                workspace=workspace,
                snapshot=snapshot,
                candidate=candidate,
                audit_output_dir=Path(reaudit["audit_output_dir"]),
                changes=changes,
                regression_results=regression_tests,
                resolved_targets=[],
                unresolved_findings=[],
                evidence=list(evidence.values()),
                workflow_kind="single",
                identity=identity,
            )
        if reaudit.get("status") == AGENT_ASSESSMENT_PENDING:
            if workspace.exists():
                cleanup_repair_workspace(workspace)
            return {
                "repair_id": repair_id,
                "status": AGENT_ASSESSMENT_PENDING,
                "review_status": AGENT_ASSESSMENT_PENDING,
                "review_verdict": "NOT_ASSESSABLE",
                "disposition": "NOT_ASSESSABLE",
                "publishability": "EVIDENCE_PENDING",
                "publishable": False,
                "repair_state": AGENT_ASSESSMENT_PENDING,
                "attempt_number": max(attempt_number - 1, 0),
                "attempt_consumed": False,
                "package_mutated": False,
                "message": reaudit.get(
                    "message",
                    "equal-depth re-audit paused for inherited paper assessment",
                ),
            }
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
        re_audit_comparison = validate_reaudit(
            candidate,
            reaudit,
            finding,
            report,
            plan,
            require_deterministic=is_deterministic_repair_plan(plan),
            original_root=root,
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
        assert_source_audit_unchanged(
            root, plan, expected_source_bundle_hash
        )
        rebase_audit_paths(candidate, root, plan)
        reaudit_report_path = reaudit_audit_dir(
            candidate, plan, anchor_root=root
        ) / "audit_report.json"
        reaudit_manifest_path = reaudit_audit_dir(
            candidate, plan, anchor_root=root
        ) / "audit_manifest.json"
        repair_manifest.update(
            {
                "reaudit_audit_id": reaudit["audit_id"],
                "reaudit_report_hash": sha256_file(reaudit_report_path),
                "reaudit_manifest_hash": sha256_file(reaudit_manifest_path),
            }
        )
        history.mkdir(parents=True)
        reaudit_bundle = archive_reaudit_bundle(
            candidate, root, plan, history
        )
        repair_manifest["reaudit_bundle"] = reaudit_bundle
        write_repair_reports(candidate, repair_manifest, plan, history)
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
            reaudit_bundle=reaudit_bundle,
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
            **reaudit_bundle_reference_fields(reaudit_bundle),
        }
        write_attempt_manifest(
            history / "attempt_manifest.json",
            attempt_manifest,
            package_mutated=False,
        )
        generated_outputs = externalize_generated_bundles(
            candidate, root, plan
        )
        atomic_publish_candidate(
            root=root,
            candidate=candidate,
            history=history,
            generated_outputs=generated_outputs,
            attempt_manifest_path=history / "attempt_manifest.json",
        )
        assert_source_audit_unchanged(
            root, plan, expected_source_bundle_hash
        )
        cleanup_repair_workspace(workspace)
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
            "package_mutated": True,
            "generated_outputs": generated_outputs,
            **reaudit_bundle_reference_fields(reaudit_bundle),
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
        structured_unresolved = unresolved_severe_references(
            reaudit.get("findings", [])
            if isinstance(reaudit, dict)
            else [],
            audit_id=(
                reaudit.get("audit_id")
                if isinstance(reaudit, dict)
                and isinstance(reaudit.get("audit_id"), str)
                else None
            ),
        )
        failed_unresolved = structured_unresolved or [
            {"finding_id": plan["finding_id"], "reason": str(exc)}
        ]
        if history.exists() and not (history / "attempt_manifest.json").exists():
            shutil.rmtree(history)
        history.mkdir(parents=True, exist_ok=True)
        if reaudit_started and reaudit_audit_dir(
            candidate, plan, anchor_root=root
        ).is_dir():
            reaudit_bundle = archive_reaudit_bundle(
                candidate, root, plan, history
            )
        if snapshot.exists():
            snapshot.rename(history / "snapshot")
        if candidate.exists():
            candidate.rename(history / "candidate")
        write_history_bundle(
            history,
            plan=plan,
            changes=changes if "changes" in locals() else [],
            unresolved=failed_unresolved,
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
            reaudit_bundle=reaudit_bundle,
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
            and reaudit is not None,
            "error": str(exc),
            "snapshot_preserved": (history / "snapshot").is_dir(),
            "candidate_preserved": (history / "candidate").is_dir(),
            "recorded_at": timestamp(),
            **reaudit_bundle_reference_fields(reaudit_bundle),
        }
        write_attempt_manifest(
            history / "attempt_manifest.json",
            attempt_manifest,
            package_mutated=False,
        )
        if workspace.exists():
            cleanup_repair_workspace(workspace)
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
            "package_mutated": False,
            "reason": str(exc),
            **reaudit_bundle_reference_fields(reaudit_bundle),
        }


def repair(
    root: Path,
    plan_path: Path,
    attestation_path: Path,
    audit_dir: Path | None = None,
    repair_output_dir: Path | None = None,
    *,
    resume_repair_id: str | None = None,
    agent_contract_assessment_path: Path | None = None,
) -> dict[str, Any]:
    resolved_root = root.expanduser().resolve()
    output_root = canonical_management_path(resolved_root, "review")
    with ReviewOutputLock(output_root, unique_id("repair")):
        return _repair_locked(
            resolved_root,
            plan_path,
            attestation_path,
            audit_dir=audit_dir,
            repair_output_dir=repair_output_dir,
            resume_repair_id=resume_repair_id,
            agent_contract_assessment_path=agent_contract_assessment_path,
        )


def repair_context(run_dir: Path) -> dict[str, Any]:
    """Repair only the candidate associated with one completed review run.

    The plan is intentionally part of the run record: callers cannot splice an
    audit, attestation, or output directory from another package into Repair.
    """

    run_dir = run_dir.expanduser().resolve()
    context = load_context(run_dir)
    current = json.loads((run_dir / "status.json").read_text(encoding="utf-8"))
    state = current.get("state")
    if state not in {"REVIEWED", "AGENT_CONTRACT_PENDING"}:
        raise RunContextError("Repair requires a REVIEWED run or its pending re-review")
    verify_content_root(run_dir, "A0")
    plan_path = run_dir / "plan.json"
    if not plan_path.is_file():
        raise RunContextError("Repair requires the run-local plan.json")
    # The established repair engine still owns all scientific and publication
    # checks. Its legacy path policy is temporarily mapped to this run only.
    plan = read_json(plan_path)
    if not isinstance(plan, dict):
        raise RunContextError("run-local plan must be a JSON object")
    verify_live_package_matches_snapshot(run_dir)
    resume_repair_id: str | None = None
    contract_assessment: Path | None = None
    if state == "AGENT_CONTRACT_PENDING":
        previous = current.get("repair_result")
        if not isinstance(previous, dict):
            raise RunContextError("pending Repair is missing its run-local result")
        resume_repair_id = previous.get("repair_id")
        if not isinstance(resume_repair_id, str) or not resume_repair_id:
            raise RunContextError("pending Repair is missing its resume identity")
        assessment = run_dir / "agent_contract" / "assessment.json"
        try:
            supplied = read_json(assessment)
        except (OSError, json.JSONDecodeError) as exc:
            raise RunContextError("pending Repair requires a valid contract assessment") from exc
        if not supplied:
            raise RunContextError("pending Repair requires its same-run contract assessment")
        contract_assessment = assessment
    with PackageRunLock(run_dir):
        transition(run_dir, "REPAIRING")
        try:
            root = Path(context["package_path"])
            token = RUN_DIRECTORY.set(run_dir)
            try:
                # Call the engine directly so it does not acquire the old
                # sibling-output lock; PackageRunLock is the sole run lock.
                result = _repair_locked(
                    root,
                    plan_path,
                    run_dir / "audit_attestation.json",
                    audit_dir=run_dir / "audit" / "benchmark_audit",
                    repair_output_dir=run_dir / "repair",
                    resume_repair_id=resume_repair_id,
                    agent_contract_assessment_path=contract_assessment,
                )
            finally:
                RUN_DIRECTORY.reset(token)
            if result.get("status") == AGENT_CONTRACT_PENDING:
                write_json(run_dir / "repair_result.json", result)
                transition(run_dir, "AGENT_CONTRACT_PENDING", repair_result=result)
                return result
            if result.get("status") == AGENT_ASSESSMENT_PENDING:
                write_json(run_dir / "repair_result.json", result)
                transition(
                    run_dir,
                    "AGENT_ASSESSMENT_PENDING",
                    repair_result=result,
                )
                return result
            history_dir = Path(result["history_dir"]) if result.get("history_dir") else None
            if history_dir and history_dir.is_dir():
                for source_name, target_name in (("candidate", "candidate"), ("reaudit", "reaudit")):
                    source = history_dir / source_name
                    target = run_dir / target_name
                    if source.is_dir() and not target.exists():
                        shutil.copytree(source, target)
            # A published candidate has been atomically renamed to the live
            # package. Preserve an immutable run-local copy for R0/A1.
            if result.get("package_mutated") and not (run_dir / "candidate").exists():
                shutil.copytree(root, run_dir / "candidate")
            write_json(run_dir / "repair_result.json", result)
            write_content_root(run_dir, "R0")
            if (run_dir / "candidate").is_dir() and (run_dir / "reaudit").is_dir():
                write_content_root(run_dir, "A1")
            complete(
                run_dir,
                outcome=result.get("status", "ABANDONED"),
                repair_result=result,
                repair_status=result.get("status"),
            )
            return result
        except Exception as exc:
            transition(run_dir, "FAILED", error=str(exc))
            raise


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Repair one audited materials-science Harbor 题包."
    )
    parser.add_argument("--run-dir", required=True, help="the sole public run context for Repair")
    arguments = parser.parse_args()
    try:
        result = repair_context(Path(arguments.run_dir))
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["status"] == "REPAIRED" else 3
    except Exception as exc:  # noqa: BLE001
        print(f"materials repair failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
