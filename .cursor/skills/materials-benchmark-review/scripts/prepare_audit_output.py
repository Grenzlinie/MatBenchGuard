#!/usr/bin/env python3
"""Discover a Harbor 题包 and prepare its isolated audit workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import time
import uuid
from pathlib import Path
from typing import Any, Iterable

from canonical_status import canonical_fields
from audit_integrity import validate_finalized_audit_bundle
from deterministic_contract import validate_deterministic_contract
from artifact_schema import (
    AGENT_ASSESSMENT_SCHEMA_VERSION,
    AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
    AUDIT_ATTESTATION_SCHEMA_VERSION,
    AUDIT_BUNDLE_SCHEMA_VERSION,
    AUDIT_MANIFEST_SCHEMA_VERSION,
    AUDIT_REPORT_SCHEMA_VERSION,
    AGENT_CONTRACT_ASSESSMENT_SCHEMA_VERSION,
    AGENT_CONTRACT_REQUEST_SCHEMA_VERSION,
    CHECKER_TESTS_SCHEMA_VERSION,
    DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
    DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
    EVIDENCE_CONTRACT_SCHEMA_VERSION,
    IMPLEMENTATION_HASH_SCHEMA_VERSION,
    IMPLEMENTATION_MANIFEST_SCHEMA_VERSION,
    SCORING_SCHEMA_VERSION,
    RESOURCE_CHECKS_SCHEMA_VERSION,
)
from review_path_policy import (
    REVIEW_LANE,
    management_purpose,
    require_external_output_dir,
)


REQUIRED_ROLES = {
    "task.toml": "toml",
    "manifest.json": "json",
    "instruction.md": "text",
    "steps.json": "json",
    "resources.json": "json",
    "environment/Dockerfile": "text",
    "tests/grading_spec.json": "json",
    "tests/checker.py": "text",
    "tests/test.sh": "text",
}
QUALITY_EVIDENCE_ROLES = {
    "instruction.md": "text",
    "tests/grading_spec.json": "json",
    "tests/checker.py": "text",
    "tests/test.sh": "text",
}
PAPER_EVIDENCE_ROLES = {
    "paper/paper.md": "text",
    "paper/images_manifest.json": "json",
}
PRUNED_DIRS = {
    "paper",
    "solution",
    "benchmark_audit",
    "benchmark_audit_history",
    ".benchmark_audit_tmp",
    "review_outputs",
    "review_records",
    "repair_history",
    "benchmark_repair_history",
    "__MACOSX",
}
HASH_NAMES = {
    *QUALITY_EVIDENCE_ROLES,
}
REVIEW_IMPLEMENTATION_FILES_MANIFEST = (
    "references/review-implementation-files.json"
)
AGENT_CONTRACT_REQUEST_RELATIVE_PATH = "agent_contract/request.json"
AGENT_CONTRACT_PENDING = "AGENT_CONTRACT_PENDING"
AGENT_ASSESSMENT_PENDING = "AGENT_ASSESSMENT_PENDING"


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def assets_root() -> Path:
    return skill_root() / "assets"


def basename(value: Any) -> str:
    return str(value or "").replace("\\", "/").split("/")[-1]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def sha256_path(path: Path) -> str:
    if path.is_symlink():
        raise ValueError(f"external evidence may not be a symbolic link: {path}")
    if path.is_file():
        return sha256_file(path)
    if not path.is_dir():
        raise FileNotFoundError(path)
    entries = []
    for child in sorted(path.rglob("*")):
        if child.is_symlink():
            raise ValueError(
                f"external evidence may not contain symbolic links: {child}"
            )
        if child.is_file():
            entries.append(
                (child.relative_to(path).as_posix(), sha256_file(child))
            )
    payload = json.dumps(
        entries, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def new_audit_id(prefix: str = "audit") -> str:
    return (
        f"{prefix}-{time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())}-"
        + uuid.uuid4().hex[:8]
    )


def canonical_mapping_hash(value: dict[str, Any]) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def preparation_artifact_hashes(temp_dir: Path) -> dict[str, dict[str, str | None]]:
    """Hash the persisted static and probe inputs used by a resume."""

    groups = {
        "static": ("evidence/static_checks/audit_static.json",),
        "probes": (
            "checker_tests.json",
            "resource_checks.json",
            "deterministic_core/probe_results.json",
            "deterministic_core/probe_cases",
        ),
    }
    result: dict[str, dict[str, str | None]] = {}
    for group, relatives in groups.items():
        result[group] = {}
        for relative in relatives:
            path = temp_dir / relative
            result[group][relative] = (
                sha256_path(path) if path.exists() else None
            )
    return result


def _requested_package_hashes(
    root: Path, expected: dict[str, str]
) -> dict[str, str]:
    """Recompute exactly the package files bound by a pending request."""

    current: dict[str, str] = {}
    for relative in sorted(expected):
        path = root / relative
        if not path.is_file() or path.is_symlink():
            raise ValueError(
                f"agent contract request package file is unavailable: {relative}"
            )
        current[relative] = sha256_file(path)
    return current


def write_agent_contract_request(
    root: Path,
    temp_dir: Path,
    machine_contract: dict[str, Any],
) -> dict[str, Any]:
    """Persist a source- and artifact-bound contract adjudication request."""

    output_root = (
        temp_dir.parent.parent
        if temp_dir.parent.name == ".benchmark_audit_tmp"
        else temp_dir.parent
    )
    request_path = output_root / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
    if request_path.exists() or request_path.is_symlink():
        raise FileExistsError(
            f"agent contract request already exists: {request_path}"
        )
    manifest = json.loads(
        (temp_dir / "audit_manifest.json").read_text(encoding="utf-8")
    )
    implementation = manifest.get("review_implementation")
    if not isinstance(implementation, dict):
        raise ValueError("audit manifest lacks Review implementation hashes")
    package_hashes = dict(manifest.get("input_hashes", {}))
    artifact_hashes = preparation_artifact_hashes(temp_dir)
    quality_artifact = temp_dir / "agent_quality/assessment.json"
    if not quality_artifact.is_file() or quality_artifact.is_symlink():
        raise ValueError(
            "agent contract preparation is missing agent quality assessment"
        )
    request: dict[str, Any] = {
        "schema_version": AGENT_CONTRACT_REQUEST_SCHEMA_VERSION,
        "status": AGENT_CONTRACT_PENDING,
        "lane": "deterministic_core",
        "benchmark_root": str(root.resolve()),
        "audit_id": manifest.get("audit_id"),
        "audit_temp_dir": str(temp_dir.resolve()),
        "review_lane": REVIEW_LANE,
        "review_contract_version": "materials-review-contract/1",
        "package_hashes": package_hashes,
        "package_hash": canonical_mapping_hash(package_hashes),
        "core_contract_digest": manifest.get("core_contract_digest"),
        "implementation_hash": implementation.get("aggregate_hash"),
        "implementation_manifest": implementation,
        "static_hashes": artifact_hashes["static"],
        "probe_hashes": artifact_hashes["probes"],
        "probe_hash": canonical_mapping_hash(artifact_hashes["probes"]),
        "quality_assessment_hash": (
            sha256_file(quality_artifact)
            if quality_artifact.is_file()
            else None
        ),
        "machine_contract_digest": machine_contract.get("contract_digest"),
        "machine_schema_version": machine_contract.get("schema_version"),
        "machine_registry_version": machine_contract.get("registry_version"),
        "machine_status": {
            "checks": {
                item["check_id"]: item["status"]
                for item in machine_contract.get("checks", [])
                if isinstance(item, dict)
            },
            "repair_summary_state": machine_contract.get(
                "repair_summary", {}
            ).get("state"),
        },
        "assessment_schema_version": AGENT_CONTRACT_ASSESSMENT_SCHEMA_VERSION,
        "assessment_lane": "deterministic_core",
        "assessment_checks": ["D1", "D2", "D3", "D4", "D5", "D6"],
        "assessment_digest": None,
        "request_digest": None,
    }
    request["request_digest"] = canonical_mapping_hash(
        {key: value for key, value in request.items() if key != "request_digest"}
    )
    request_path.parent.mkdir(parents=True, exist_ok=True)
    request_path.write_text(
        json.dumps(request, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return request


def validate_agent_contract_request(
    root: Path,
    temp_dir: Path,
) -> dict[str, Any]:
    """Fail closed when a persisted Review preparation is stale or altered."""

    output_root = (
        temp_dir.parent.parent
        if temp_dir.parent.name == ".benchmark_audit_tmp"
        else temp_dir.parent
    )
    request_path = output_root / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
    if not request_path.is_file() or request_path.is_symlink():
        raise FileNotFoundError(
            f"agent contract request is missing: {request_path}"
        )
    request = json.loads(request_path.read_text(encoding="utf-8"))
    if not isinstance(request, dict):
        raise ValueError("agent contract request must be an object")
    if request.get("schema_version") != AGENT_CONTRACT_REQUEST_SCHEMA_VERSION:
        raise ValueError("agent contract request schema_version is stale")
    if request.get("status") != AGENT_CONTRACT_PENDING:
        raise ValueError("agent contract request status is invalid")
    if (
        request.get("assessment_schema_version")
        != AGENT_CONTRACT_ASSESSMENT_SCHEMA_VERSION
        or request.get("assessment_lane") != "deterministic_core"
        or request.get("assessment_checks")
        != ["D1", "D2", "D3", "D4", "D5", "D6"]
    ):
        raise ValueError("agent contract request assessment schema is invalid")
    expected_digest = canonical_mapping_hash(
        {
            key: value
            for key, value in request.items()
            if key != "request_digest"
        }
    )
    if request.get("request_digest") != expected_digest:
        raise ValueError("agent contract request digest is stale or tampered")
    resolved_root = root.expanduser().resolve()
    expected_output_root = (
        temp_dir.parent.parent
        if temp_dir.parent.name == ".benchmark_audit_tmp"
        else temp_dir.parent
    )
    if (
        temp_dir.parent.name == ".benchmark_audit_tmp"
        and request.get("audit_temp_dir")
        != str(temp_dir.expanduser().resolve())
    ):
        raise ValueError("agent contract request temp workspace is stale")
    if temp_dir.parent.name == ".benchmark_audit_tmp" and (
        temp_dir.parent.parent != expected_output_root
        or temp_dir.name != request.get("audit_id")
    ):
        raise ValueError("agent contract request temp workspace identity is stale")
    if request.get("benchmark_root") != str(resolved_root):
        raise ValueError("agent contract request package root is stale")
    manifest_path = temp_dir / "audit_manifest.json"
    context_path = temp_dir / "audit_context.json"
    if not manifest_path.is_file() or not context_path.is_file():
        raise ValueError("agent contract preparation workspace is incomplete")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    context = json.loads(context_path.read_text(encoding="utf-8"))
    if request.get("audit_id") != manifest.get("audit_id") or request.get(
        "audit_id"
    ) != context.get("audit_id"):
        raise ValueError("agent contract request audit binding is stale")
    package_hashes = request.get("package_hashes")
    if not isinstance(package_hashes, dict) or any(
        not isinstance(key, str) or not isinstance(value, str)
        for key, value in package_hashes.items()
    ):
        raise ValueError("agent contract request package hashes are invalid")
    current_package_hashes = _requested_package_hashes(
        resolved_root, package_hashes
    )
    if current_package_hashes != package_hashes or request.get(
        "package_hash"
    ) != canonical_mapping_hash(package_hashes):
        raise ValueError("agent contract request package hash is stale")
    implementation = collect_review_implementation_hashes()
    if request.get("implementation_hash") != implementation.get(
        "aggregate_hash"
    ) or request.get("implementation_manifest") != implementation:
        raise ValueError("agent contract request implementation hash is stale")
    if request.get("core_contract_digest") != core_contract_digest(
        resolved_root
    ):
        raise ValueError("agent contract request core contract digest is stale")
    artifact_hashes = preparation_artifact_hashes(temp_dir)
    if request.get("static_hashes") != artifact_hashes["static"]:
        raise ValueError("agent contract request static artifact hash is stale")
    if request.get("probe_hashes") != artifact_hashes["probes"] or request.get(
        "probe_hash"
    ) != canonical_mapping_hash(artifact_hashes["probes"]):
        raise ValueError("agent contract request probe hash is stale")
    quality_artifact = temp_dir / "agent_quality/assessment.json"
    if not quality_artifact.is_file() or quality_artifact.is_symlink():
        raise ValueError(
            "agent contract preparation is missing agent quality assessment"
        )
    current_quality_hash = sha256_file(quality_artifact)
    if request.get("quality_assessment_hash") != current_quality_hash:
        raise ValueError("agent contract request quality assessment is stale")
    machine_artifact_path = temp_dir / "deterministic_core/report.json"
    if not machine_artifact_path.is_file():
        raise ValueError("agent contract machine artifact is missing")
    machine_artifact = json.loads(
        machine_artifact_path.read_text(encoding="utf-8")
    )
    machine_contract = machine_artifact.get("contract")
    if not isinstance(machine_contract, dict):
        raise ValueError("agent contract machine contract is missing")
    machine_contract = validate_deterministic_contract(machine_contract)
    if request.get("machine_contract_digest") != machine_contract.get(
        "contract_digest"
    ) or request.get("machine_schema_version") != machine_contract.get(
        "schema_version"
    ) or request.get("machine_registry_version") != machine_contract.get(
        "registry_version"
    ):
        raise ValueError("agent contract machine contract digest is stale")
    machine_status = request.get("machine_status")
    expected_machine_status = {
        "checks": {
            item["check_id"]: item["status"]
            for item in machine_contract.get("checks", [])
            if isinstance(item, dict)
        },
        "repair_summary_state": machine_contract.get(
            "repair_summary", {}
        ).get("state"),
    }
    if machine_status != expected_machine_status:
        raise ValueError("agent contract machine status is stale")
    return request


def archive_agent_contract_request(
    output_root: Path, audit_id: str
) -> Path | None:
    """Retain a completed request without leaving a resumable pending seam."""

    request_path = output_root / AGENT_CONTRACT_REQUEST_RELATIVE_PATH
    if not request_path.is_file():
        return None
    history = request_path.parent / "history"
    history.mkdir(parents=True, exist_ok=True)
    destination = history / f"{audit_id}.json"
    suffix = 1
    while destination.exists():
        destination = history / f"{audit_id}-{suffix}.json"
        suffix += 1
    request_path.rename(destination)
    return destination


def core_contract_snapshot(root: Path) -> dict[str, Any]:
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
        "schema_version": "materials-core-contract/1.0",
        "surface_hashes": {
            path.relative_to(root).as_posix(): sha256_file(path)
            for path in sorted(paths)
        },
    }


def core_contract_digest(root: Path) -> str:
    payload = json.dumps(
        core_contract_snapshot(root),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def bind_external_evidence(
    temp_dir: Path,
    agent_assessment: Path | None,
    agent_contract_assessment: Path | None = None,
) -> dict[str, dict[str, str]]:
    manifest_path = temp_dir / "audit_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    root = Path(manifest["benchmark_root"]).resolve()
    assessment_hashes: dict[str, str] = dict(
        manifest.get("assessment_hashes", {})
    )
    if agent_assessment is not None:
        resolved = agent_assessment.expanduser().resolve()
        if resolved.is_relative_to(root):
            raise ValueError("agent assessment must remain outside the Harbor 题包")
        assessment_hashes["agent_assessment"] = sha256_path(
            resolved
        )
    if agent_contract_assessment is not None:
        resolved = agent_contract_assessment.expanduser().resolve()
        if resolved.is_relative_to(root):
            raise ValueError(
                "agent contract assessment must remain outside the Harbor 题包"
            )
        assessment_hashes["agent_contract_assessment"] = sha256_path(
            resolved
        )
    manifest["assessment_hashes"] = assessment_hashes
    manifest["core_contract_digest"] = core_contract_digest(
        Path(manifest["benchmark_root"])
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return {
        "assessment_hashes": assessment_hashes,
        "core_contract_digest": manifest["core_contract_digest"],
    }


def iter_public_files(root: Path) -> Iterable[Path]:
    """Yield files without entering solution or generated audit directories."""
    for current, directories, filenames in os.walk(root, topdown=True):
        current_path = Path(current)
        for name in directories:
            if (current_path / name).is_symlink():
                raise ValueError(
                    "symbolic-link directories are not allowed in the audit "
                    f"boundary: {current_path / name}"
                )
        directories[:] = [
            name for name in directories if name not in PRUNED_DIRS
        ]
        for filename in filenames:
            path = current_path / filename
            if path.is_symlink():
                raise ValueError(
                    f"symbolic links are not allowed in the audit boundary: {path}"
                )
            yield path


def validate_role_boundary(root: Path) -> None:
    """Reject role paths that escape the 题包 or route through symlinks."""
    root = root.resolve()
    solution = root / "solution"
    if solution.is_symlink():
        raise ValueError("solution/ must not be a symbolic link")
    for role in QUALITY_EVIDENCE_ROLES:
        path = root / role
        if not path.exists():
            continue
        current = path
        while current != root:
            if current.is_symlink():
                raise ValueError(
                    f"required Harbor role routes through a symlink: {role}"
                )
            current = current.parent
        resolved = path.resolve()
        if not resolved.is_relative_to(root):
            raise ValueError(f"required Harbor role escapes 题包 root: {role}")
        if resolved.is_relative_to(solution):
            raise ValueError(f"required Harbor role routes through solution/: {role}")


def locate_root(source: Path) -> Path:
    source = source.expanduser().resolve()
    if not source.is_dir():
        raise ValueError("input must be a Harbor 题包 directory")
    if sum((source / role).exists() for role in QUALITY_EVIDENCE_ROLES) >= 2:
        validate_role_boundary(source)
        return source

    candidates: list[tuple[int, int, Path]] = []
    for current, directories, _ in os.walk(source, topdown=True):
        directories[:] = [
            name for name in directories if name not in PRUNED_DIRS
        ]
        candidate = Path(current)
        score = sum(
            (candidate / role).exists() for role in QUALITY_EVIDENCE_ROLES
        )
        if score:
            candidates.append((-score, len(candidate.parts), candidate))
    if not candidates:
        raise ValueError("could not locate a Harbor 题包 root")
    candidates.sort()
    root = candidates[0][2].resolve()
    validate_role_boundary(root)
    return root


def render_template(source: Path, values: dict[str, str]) -> str:
    text = source.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def collect_input_hashes(root: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    candidates = [root / "instruction.md"]
    tests = root / "tests"
    if tests.is_dir():
        candidates.extend(path for path in tests.rglob("*") if path.is_file())
    for path in candidates:
        if not path.is_file():
            continue
        if path.is_symlink():
            raise ValueError(f"quality evidence cannot be a symlink: {path}")
        relative = path.relative_to(root).as_posix()
        hashes[relative] = sha256_file(path)
    return dict(sorted(hashes.items()))


def collect_source_role_inventory(
    root: Path,
    *,
    skip_paper: bool = False,
) -> dict[str, dict[str, Any]]:
    """Inventory quality roles; paper is in-scope unless NON_MAT skips it."""
    hashes = collect_input_hashes(root)
    if not skip_paper:
        for relative in PAPER_EVIDENCE_ROLES:
            path = root / relative
            if path.is_file():
                hashes[relative] = sha256_file(path)
    role_types = {
        **QUALITY_EVIDENCE_ROLES,
        **PAPER_EVIDENCE_ROLES,
    }
    inventory: dict[str, dict[str, Any]] = {}
    for relative in sorted(set(hashes) | set(role_types)):
        role_type = role_types.get(
            relative,
            "json" if relative.endswith(".json") else "text",
        )
        required = relative in {
            "instruction.md",
            "tests/checker.py",
            "tests/test.sh",
        }
        if relative.startswith("paper/"):
            if skip_paper:
                inventory[relative] = {
                    "status": "NOT_IN_SCOPE",
                    "required": False,
                    "type": role_type,
                    "sha256": None,
                    "size_bytes": None,
                }
                continue
            # Dual-lane default: paper is required when present in-scope.
            required = True
        path = root / relative
        if path.is_file():
            inventory[relative] = {
                "status": "PRESENT",
                "required": required,
                "type": role_type,
                "sha256": hashes[relative],
                "size_bytes": path.stat().st_size,
            }
        else:
            inventory[relative] = {
                "status": "ABSENT",
                "required": required,
                "type": role_type,
                "sha256": None,
                "size_bytes": None,
            }
    return inventory


def review_implementation_files(root: Path | None = None) -> tuple[str, ...]:
    root = root or skill_root()
    manifest_path = root / REVIEW_IMPLEMENTATION_FILES_MANIFEST
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if (
        not isinstance(manifest, dict)
        or manifest.get("schema_version")
        != IMPLEMENTATION_MANIFEST_SCHEMA_VERSION
        or not isinstance(manifest.get("files"), list)
    ):
        raise ValueError("Review implementation file manifest is invalid")
    files = manifest["files"]
    if (
        not files
        or files != sorted(set(files))
        or REVIEW_IMPLEMENTATION_FILES_MANIFEST not in files
        or not all(isinstance(item, str) and item for item in files)
    ):
        raise ValueError("Review implementation file list is not canonical")
    for relative in files:
        relative_path = Path(relative)
        path = root / relative_path
        if (
            relative_path.is_absolute()
            or ".." in relative_path.parts
            or not path.is_file()
            or path.is_symlink()
        ):
            raise ValueError(
                f"Review implementation dependency is unsafe: {relative}"
            )
    return tuple(files)


def collect_review_implementation_hashes(
    root: Path | None = None,
) -> dict[str, Any]:
    root = root or skill_root()
    files = {
        relative: sha256_file(root / relative)
        for relative in review_implementation_files(root)
    }
    payload = json.dumps(
        files, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return {
        "schema_version": IMPLEMENTATION_HASH_SCHEMA_VERSION,
        "root": ".cursor/skills/materials-benchmark-review",
        "files": files,
        "aggregate_hash": "sha256:" + hashlib.sha256(payload).hexdigest(),
    }


def audit_attestation_payload(audit_dir: Path) -> dict[str, Any]:
    manifest_path = audit_dir / "audit_manifest.json"
    report_path = audit_dir / "audit_report.json"
    disposition_path = audit_dir / "disposition.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    report = json.loads(report_path.read_text(encoding="utf-8"))
    disposition = json.loads(disposition_path.read_text(encoding="utf-8"))
    validate_finalized_audit_bundle(
        audit_dir, manifest, report, disposition
    )
    required_artifacts = {
        "audit_report.json": report_path,
        "deterministic_core/report.json": audit_dir
        / "deterministic_core/report.json",
        "deterministic_core/probe_results.json": audit_dir
        / "deterministic_core/probe_results.json",
        "agent_quality/assessment.json": audit_dir
        / "agent_quality/assessment.json",
    }
    artifact_hashes: dict[str, str] = {}
    artifact_values: dict[str, dict[str, Any]] = {}
    for relative, path in required_artifacts.items():
        if not path.is_file() or path.is_symlink():
            raise ValueError(
                f"current audit is missing required artifact: {relative}"
            )
        artifact_hashes[relative] = sha256_file(path)
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError(f"current audit artifact is not an object: {relative}")
        artifact_values[relative] = value
    return {
        "audit_id": manifest["audit_id"],
        "manifest_hash": sha256_file(manifest_path),
        "report_hash": sha256_file(report_path),
        "disposition_hash": sha256_file(disposition_path),
        "assessment_hashes": manifest.get("assessment_hashes", {}),
        "artifact_hashes": artifact_hashes,
        "output_hashes": manifest.get("output_hashes", {}),
        "artifact_schema_versions": {
            "audit_manifest": manifest.get("schema_version"),
            "audit_bundle": manifest.get("bundle_schema_version"),
            "audit_report": report.get("schema_version"),
            "deterministic_core": artifact_values[
                "deterministic_core/report.json"
            ].get("schema_version"),
            "deterministic_probe_results": artifact_values[
                "deterministic_core/probe_results.json"
            ].get("schema_version"),
            "agent_quality": artifact_values[
                "agent_quality/assessment.json"
            ].get("schema_version"),
            "scoring": report.get("summary", {}).get("scoring_version"),
        },
        "scoring_schema_version": SCORING_SCHEMA_VERSION,
    }


def write_audit_attestation(
    benchmark_root: Path,
    output_path: Path,
    audit_dir: Path | None = None,
) -> dict[str, Any]:
    benchmark_root = benchmark_root.expanduser().resolve()
    output_path = output_path.expanduser().resolve()
    if output_path.is_relative_to(benchmark_root):
        raise ValueError("audit attestation must remain outside the Harbor 题包")
    if output_path.exists() or output_path.is_symlink():
        raise FileExistsError(
            "audit attestation output is immutable and must not already exist"
        )
    finalized_audit = (
        audit_dir.expanduser().resolve()
        if audit_dir is not None
        else benchmark_root / "benchmark_audit"
    )
    audit_attestation_payload(finalized_audit)
    manifest_path = finalized_audit / "audit_manifest.json"
    original_manifest = manifest_path.read_bytes()
    manifest = json.loads(original_manifest.decode("utf-8"))
    if manifest.get("immutability_state") == "ATTESTED":
        raise ValueError("audit bundle is already attested and immutable")
    manifest["immutability_state"] = "ATTESTED"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    payload = audit_attestation_payload(finalized_audit)
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    attestation = {
        "schema_version": AUDIT_ATTESTATION_SCHEMA_VERSION,
        **payload,
        "bundle_digest": "sha256:" + hashlib.sha256(encoded).hexdigest(),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with output_path.open("x", encoding="utf-8") as handle:
            handle.write(
                json.dumps(attestation, indent=2, ensure_ascii=False) + "\n"
            )
        created = True
        output_path.chmod(0o444)
        freeze_audit_bundle(
            audit_dir.expanduser().resolve()
            if audit_dir is not None
            else benchmark_root / "benchmark_audit"
        )
    except FileExistsError as exc:
        raise FileExistsError(
            "audit attestation output is immutable and must not already exist"
        ) from exc
    except Exception:
        try:
            manifest_path.write_bytes(original_manifest)
        except OSError:
            pass
        if created:
            try:
                output_path.chmod(0o644)
                output_path.unlink()
            except OSError:
                pass
        raise
    return attestation


def freeze_audit_bundle(audit_dir: Path) -> None:
    """Make a finalized source bundle read-only after attestation."""

    resolved = audit_dir.expanduser().resolve()
    if not resolved.is_dir() or resolved.is_symlink():
        raise ValueError("cannot freeze a missing or symlinked audit bundle")
    paths = sorted(
        (path for path in resolved.rglob("*") if not path.is_symlink()),
        key=lambda path: len(path.parts),
        reverse=True,
    )
    for path in paths:
        try:
            path.chmod(0o444 if path.is_file() else 0o555)
        except OSError as exc:
            raise ValueError(f"could not freeze audit bundle: {path}") from exc
    resolved.chmod(0o555)


def validate_paper_boundary(root: Path) -> None:
    """Ensure bundled paper roles are local files outside solution/."""
    resolved_root = root.resolve()
    solution = resolved_root / "solution"
    paper_dir = root / "paper"
    if paper_dir.is_symlink():
        raise ValueError("paper role routes through a symlink: paper/")
    for relative in ("paper/paper.md", "paper/images_manifest.json"):
        path = root / relative
        if path.is_symlink():
            raise ValueError(
                f"paper role routes through a symlink: {relative}"
            )
        if not path.is_file():
            raise ValueError(
                f"paper_grounded mode requires bundled paper role: {relative}"
            )
        resolved = path.resolve()
        if not resolved.is_relative_to(resolved_root):
            raise ValueError(f"paper role escapes 题包 root: {relative}")
        if resolved.is_relative_to(solution):
            raise ValueError(f"paper role routes through solution/: {relative}")


def record_paper_input_hashes(root: Path, temp_dir: Path) -> None:
    """Bind bundled paper hashes for the dual-lane Agent paper read."""
    validate_paper_boundary(root)
    manifest_path = temp_dir / "audit_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for relative in ("paper/paper.md", "paper/images_manifest.json"):
        path = root / relative
        manifest["input_hashes"][relative] = sha256_file(path)
    manifest["input_hashes"] = dict(
        sorted(manifest["input_hashes"].items())
    )
    manifest["source_role_inventory"] = collect_source_role_inventory(
        root,
        skip_paper=False,
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def prepare_workspace(
    root: Path,
    audit_output_dir: Path | None = None,
    *,
    skip_paper: bool = False,
    run_id: str | None = None,
) -> dict[str, Any]:
    """Prepare a candidate audit under a required external output root."""
    resolved_root = root.expanduser().resolve()
    output_root = require_external_output_dir(
        resolved_root,
        audit_output_dir,
        label="audit output directory",
        purpose=management_purpose(resolved_root, audit_output_dir)
        if audit_output_dir is not None
        else "review",
    )
    parent_audit_id: str | None = None
    previous_manifest = output_root / "benchmark_audit/audit_manifest.json"
    if previous_manifest.is_file():
        previous = json.loads(
            previous_manifest.read_text(encoding="utf-8")
        )
        candidate = previous.get("audit_id")
        if isinstance(candidate, str) and candidate:
            parent_audit_id = candidate
    audit_id = run_id or new_audit_id()
    if not audit_id or Path(audit_id).name != audit_id:
        raise ValueError("audit run ID must be a non-empty leaf name")
    temp_dir = output_root / ".benchmark_audit_tmp" / audit_id
    if temp_dir.exists() or temp_dir.is_symlink():
        raise FileExistsError(
            f"audit run workspace already exists for {audit_id}: {temp_dir}"
        )
    for relative in (
        "evidence/static_checks",
        "evidence/resource_checks",
        "evidence/checker_tests",
        "evidence/paper_checks",
        "deterministic_core",
        "agent_quality",
        "logs",
        "patches",
    ):
        (temp_dir / relative).mkdir(parents=True, exist_ok=True)

    started_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    values = {
        "AUDIT_ID": audit_id,
        "BENCHMARK_NAME": root.name,
        "BENCHMARK_ROOT": str(root),
        "REVIEW_LANE": REVIEW_LANE,
        "STARTED_AT": started_at,
    }
    (temp_dir / "audit_report.md").write_text(
        render_template(assets_root() / "audit_report_template.md", values),
        encoding="utf-8",
    )
    (temp_dir / "audit_report.json").write_text(
        render_template(assets_root() / "audit_report_template.json", values),
        encoding="utf-8",
    )
    shutil.copy2(
        assets_root() / "resource_checks_template.json",
        temp_dir / "resource_checks.json",
    )
    shutil.copy2(
        assets_root() / "checker_tests_template.json",
        temp_dir / "checker_tests.json",
    )
    (temp_dir / "findings.jsonl").write_text("", encoding="utf-8")
    (temp_dir / "logs/audit.log").write_text(
        f"{started_at}\tINFO\taudit workspace prepared\taudit_id={audit_id}\n",
        encoding="utf-8",
    )
    manifest = {
        "schema_version": AUDIT_MANIFEST_SCHEMA_VERSION,
        "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
        "audit_id": audit_id,
        "parent_audit_id": parent_audit_id,
        "review_type": (
            "DUAL_LANE_REAUDIT"
            if parent_audit_id is not None
            else "INITIAL_AUDIT"
        ),
        "generated_at": started_at,
        "completed_at": None,
        "auditor_version": "materials-benchmark-review/2.0",
        "benchmark_root": str(root),
        **canonical_fields("NOT_ASSESSABLE"),
        "review_lane": REVIEW_LANE,
        "input_hashes": collect_input_hashes(root),
        "source_role_inventory": collect_source_role_inventory(
            root,
            skip_paper=skip_paper,
        ),
        "review_implementation": collect_review_implementation_hashes(),
        "core_contract_digest": core_contract_digest(root),
        "assessment_hashes": {},
        "output_hashes": {},
        "bundle_hash": None,
        "resolved_findings": [],
        "new_findings": [],
        "solution_content_inspected": False,
        "artifact_schema_versions": {
            "audit_report": AUDIT_REPORT_SCHEMA_VERSION,
            "checker_tests": CHECKER_TESTS_SCHEMA_VERSION,
            "resource_checks": RESOURCE_CHECKS_SCHEMA_VERSION,
            "agent_assessment": AGENT_ASSESSMENT_SCHEMA_VERSION,
            "deterministic_core": DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
            "deterministic_probe_results": (
                DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION
            ),
            "agent_quality": AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
            "scoring": SCORING_SCHEMA_VERSION,
            "evidence_contract": EVIDENCE_CONTRACT_SCHEMA_VERSION,
        },
    }
    (temp_dir / "audit_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    context = {
        "audit_id": audit_id,
        "benchmark_root": str(root),
        "audit_temp_dir": str(temp_dir),
        "audit_output_root": str(output_root),
        "audit_temp_parent": str(temp_dir.parent),
        "final_audit_dir": str(output_root / "benchmark_audit"),
        "review_lane": REVIEW_LANE,
        "skip_paper": skip_paper,
    }
    (temp_dir / "audit_context.json").write_text(
        json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return context


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument(
        "--audit-output-dir",
        required=True,
        help=(
            "external directory that owns benchmark_audit; must remain outside "
            "the Harbor 题包 (sibling convention: "
            "<topic>/review_outputs/<paper-id>/)"
        ),
    )
    arguments = parser.parse_args()
    try:
        root = locate_root(Path(arguments.input))
        context = prepare_workspace(
            root,
            Path(arguments.audit_output_dir),
        )
        print(json.dumps(context, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"prepare audit output failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
