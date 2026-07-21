"""Integrity checks shared by Review attestation and Repair authentication."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from artifact_schema import IMPLEMENTATION_HASH_SCHEMA_VERSION


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


def actual_output_hashes(audit_dir: Path) -> dict[str, str]:
    """Hash every finalized bundle file except the self-referential manifest."""

    return dict(
        sorted(
            (
                path.relative_to(audit_dir).as_posix(),
                sha256_file(path),
            )
            for path in audit_dir.rglob("*")
            if path.is_file()
            and not path.is_symlink()
            and path.name != "audit_manifest.json"
        )
    )


def implementation_aggregate(files: dict[str, str]) -> str:
    payload = json.dumps(
        files, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def validate_implementation_manifest(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("Review implementation manifest must be an object")
    if value.get("schema_version") != IMPLEMENTATION_HASH_SCHEMA_VERSION:
        raise ValueError("Review implementation hash schema is stale")
    files = value.get("files")
    if (
        not isinstance(files, dict)
        or not files
        or list(files) != sorted(files)
        or not all(
            isinstance(relative, str)
            and relative
            and isinstance(digest, str)
            and digest
            for relative, digest in files.items()
        )
    ):
        raise ValueError("Review implementation file hashes are invalid")
    aggregate = value.get("aggregate_hash")
    if aggregate != implementation_aggregate(files):
        raise ValueError("Review implementation aggregate hash is stale")
    return value


def validate_finalized_audit_bundle(
    audit_dir: Path,
    manifest: dict[str, Any],
    report: dict[str, Any],
    disposition: dict[str, Any],
) -> dict[str, str]:
    """Require exact output membership and cross-artifact implementation binding."""

    output_hashes = manifest.get("output_hashes")
    if not isinstance(output_hashes, dict) or not output_hashes:
        raise ValueError("audit manifest output_hashes must be a non-empty object")
    actual = actual_output_hashes(audit_dir)
    if set(actual) != set(output_hashes):
        missing = sorted(set(output_hashes) - set(actual))
        extra = sorted(set(actual) - set(output_hashes))
        raise ValueError(
            "audit output file set differs from manifest: "
            f"missing={missing} extra={extra}"
        )
    if any(
        not isinstance(relative, str)
        or Path(relative).is_absolute()
        or ".." in Path(relative).parts
        or not isinstance(expected, str)
        or expected != actual[relative]
        for relative, expected in output_hashes.items()
    ):
        raise ValueError("audit output hashes are stale or invalid")
    if (
        manifest.get("bundle_hash") is not None
        and manifest.get("bundle_hash") != canonical_json_hash(output_hashes)
    ):
        raise ValueError("audit manifest bundle hash is stale")

    implementation = validate_implementation_manifest(
        manifest.get("review_implementation")
    )
    binding = report.get("audit_binding")
    if isinstance(binding, dict) and (
        binding.get("implementation_hash")
        != implementation["aggregate_hash"]
    ):
        raise ValueError(
            "audit report implementation aggregate differs from manifest"
        )
    if (
        not isinstance(binding, dict)
        and manifest.get("immutability_state") == "ATTESTED"
    ):
        raise ValueError("attested audit report lacks implementation aggregate")
    if disposition.get("audit_id") != manifest.get("audit_id"):
        raise ValueError("audit disposition identity differs from manifest")
    return actual
