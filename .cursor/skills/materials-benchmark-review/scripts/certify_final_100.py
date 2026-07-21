#!/usr/bin/env python3
"""Certify a persisted, source-bound materials dual-lane batch.

Validates status, score, and byte-integrity consistency only. It does not
certify dimension evidence presence or synthetic probe evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from canonical_status import (  # noqa: E402
    REPAIR_BUNDLE_FILES,
    require_canonical_fields,
    validate_repair_bundle_semantics,
)
from agent_contract_wiring import (  # noqa: E402
    resolve_publication_contract,
)
from finalize_audit_output import validate_qa_axes as validate_review_qa_axes
from prepare_audit_output import (  # noqa: E402
    collect_review_implementation_hashes,
)
from review_path_policy import (  # noqa: E402
    REVIEW_LANE,
)
from artifact_schema import (  # noqa: E402
    SCORING_SCHEMA_VERSION,
    AUDIT_REPORT_SCHEMA_VERSION,
    AUDIT_MANIFEST_SCHEMA_VERSION,
    CHECKER_TESTS_SCHEMA_VERSION,
    require_schema,
)


SCHEMA_VERSION = "materials-final-100-index/1.0"
CERTIFIER_VERSION = "materials-final-100-certifier/1.0"
SCORING_VERSION = SCORING_SCHEMA_VERSION
FIVE_PROBE_CLASSES = (
    "positive",
    "negative",
    "discrimination",
    "equivalence",
    "component_isolation",
)
DIMENSION_MAX_POINTS = {
    "C01": 10,
    "C02": 20,
    "C03": 20,
    "C04": 20,
    "C05": 10,
    "C06": 10,
    "C07": 10,
}
HARD_GATES = (
    "NON_MATERIALS_TASK",
    "SCIENTIFIC_TARGET_INVALID",
    "CHECKER_CORE_TASK_UNASSESSED",
    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
)
PASS_THRESHOLD = 80
PROBE_STATUSES = frozenset(
    {"ASSESSED", "NOT_ASSESSABLE", "NOT_RUN", "NOT_APPLICABLE"}
)
ORACLE_FIELDS = frozenset(
    {
        "used",
        "status",
        "positive_mock_available",
        "attempted",
        "setup_attempted",
        "setup_prepared",
        "producer_started",
        "executed",
        "scientific_evidence",
    }
)
CONTRACT_ROLE_TYPES = {
    "instruction.md": "text",
    "tests/test.sh": "text",
    "tests/checker.py": "text",
    "tests/grading_spec.json": "json",
    "paper/paper.md": "text",
    "paper/images_manifest.json": "json",
}


class CertificationError(ValueError):
    """Raised when persisted evidence cannot support certification."""


def validate_report_canonical_fields(
    report: dict[str, Any],
    fields: dict[str, str],
) -> None:
    """Keep verdict fields separate from publication-route fields."""

    summary = report.get("summary")
    if not isinstance(summary, dict):
        raise CertificationError("report summary is absent")
    if (
        summary.get("final_verdict") != fields["review_verdict"]
        or summary.get("disposition") != fields["review_verdict"]
    ):
        raise CertificationError("report verdict is not canonical")
    if (
        report.get("publishability") != fields["publishability"]
        or summary.get("publication_route") != fields["publishability"]
        or summary.get("publishability") != fields["publishability"]
    ):
        raise CertificationError("report publication route is not canonical")


def reaudit_has_no_hard_gate_for_certification(report: dict[str, Any]) -> bool:
    summary = report.get("summary", {})
    if not isinstance(summary, dict):
        return False
    if summary.get("hard_gate") is True or summary.get("hard_gate_triggered") is True:
        return False
    gates = report.get("hard_gates")
    return isinstance(gates, list) and not any(
        isinstance(gate, dict) and gate.get("status") == "FAIL"
        for gate in gates
    )


def validate_persisted_reaudit_pass(report: dict[str, Any]) -> None:
    summary = report.get("summary")
    try:
        fields = require_canonical_fields(report)
    except (TypeError, ValueError) as exc:
        raise CertificationError(
            "published re-audit canonical fields are invalid"
        ) from exc
    validate_report_canonical_fields(report, fields)
    if (
        not isinstance(summary, dict)
        or summary.get("scoring_version") != SCORING_VERSION
        or fields["review_verdict"] != "PASS"
        or fields["publishability"] != "PUBLISH_CANDIDATE"
        or summary.get("hard_gate_triggered") is not False
    ):
        raise CertificationError("published re-audit is not an authoritative PASS")
    score = summary.get("total_score")
    try:
        numeric_score = float(score)
    except (TypeError, ValueError, OverflowError):
        numeric_score = float("nan")
    if not math.isfinite(numeric_score) or not 80 <= numeric_score <= 100:
        raise CertificationError("published re-audit score is below 80 or non-finite")
    validate_dimensions(report)
    validate_hard_gates(report)
    try:
        deterministic = resolve_publication_contract(
            report.get("deterministic_contract"),
            report.get("effective_deterministic_contract"),
            report.get("agent_contract_assessment"),
        )
    except (TypeError, ValueError) as exc:
        raise CertificationError(
            "published re-audit lacks deterministic CLEAN evidence"
        ) from exc
    if deterministic["repair_summary"]["state"] != "CLEAN":
        raise CertificationError("published re-audit is not deterministically CLEAN")
    if any(
        isinstance(item, dict)
        and item.get("blocking") is True
        and item.get("status", "OPEN") not in {"RESOLVED", "CLOSED", "FIXED"}
        for item in report.get("findings", [])
    ):
        raise CertificationError("published re-audit has residual blockers")


def canonical_json_hash(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def file_hash(path: Path) -> str:
    try:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as exc:
        raise CertificationError(f"artifact bytes are unavailable: {path}") from exc
    return "sha256:" + digest


def path_hash(path: Path) -> str:
    if path.is_symlink():
        raise CertificationError(f"source path may not be a symlink: {path}")
    if path.is_file():
        return file_hash(path)
    if not path.is_dir():
        raise CertificationError(f"source path is missing: {path}")
    entries = []
    for child in sorted(path.rglob("*")):
        if child.is_symlink():
            raise CertificationError(f"source path contains a symlink: {child}")
        if child.is_file():
            entries.append((child.relative_to(path).as_posix(), file_hash(child)))
    return canonical_json_hash(entries)


def reject_symlink_components(path: Path, *, boundary: Path) -> None:
    absolute = path if path.is_absolute() else Path.cwd() / path
    resolved = absolute.resolve()
    resolved_boundary = boundary.resolve()
    common_parts: list[str] = []
    for left, right in zip(resolved.parts, resolved_boundary.parts):
        if left != right:
            break
        common_parts.append(left)
    resolved_common = Path(*common_parts) if common_parts else Path("/")
    current = absolute
    while True:
        if current.is_symlink():
            raise CertificationError(
                f"path contains a symlink component: {current}"
            )
        if current.resolve() == resolved_common or current.parent == current:
            break
        current = current.parent


def read_json(path: Path, context: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise CertificationError(f"{context} is unreadable: {path}") from exc


def resolve_external(
    raw: Any,
    *,
    base: Path,
    context: str,
    must_exist: bool = True,
    allow_outside: bool = False,
) -> Path:
    if not isinstance(raw, str) or not raw.strip():
        raise CertificationError(f"{context} path is absent")
    candidate = Path(raw).expanduser()
    unresolved = candidate if candidate.is_absolute() else base / candidate
    reject_symlink_components(unresolved, boundary=base)
    resolved = unresolved.resolve()
    resolved_base = base.resolve()
    if not allow_outside and not resolved.is_relative_to(resolved_base):
        raise CertificationError(f"{context} path escapes its bound root")
    if must_exist and not resolved.exists():
        raise CertificationError(f"{context} bytes are absent: {resolved}")
    return resolved


def verify_hash_map(
    root: Path,
    declared: Any,
    *,
    context: str,
) -> None:
    if not isinstance(declared, dict) or not declared:
        raise CertificationError(f"{context} hash map is absent")
    for relative, expected in sorted(declared.items()):
        if (
            not isinstance(relative, str)
            or not isinstance(expected, str)
            or Path(relative).is_absolute()
            or ".." in Path(relative).parts
        ):
            raise CertificationError(f"{context} hash map is invalid")
        actual_path = root / relative
        reject_symlink_components(actual_path, boundary=root)
        if not actual_path.is_file() or file_hash(actual_path) != expected:
            raise CertificationError(
                f"{context} bytes do not match declared hash: {relative}"
            )


def verify_source_bytes(
    record: dict[str, Any],
    manifest: dict[str, Any],
    *,
    batch: Path,
    source_root: Path | None,
) -> None:
    binding = record.get("evidence", {}).get("source_binding", {})
    raw_source = binding.get("source_path") or record.get("source_path")
    if raw_source is None and source_root is not None:
        raw_source = record.get("source_relative_path")
    if raw_source is None:
        raise CertificationError("source bytes are not bound")
    source_base = source_root or batch
    source = resolve_external(
        raw_source,
        base=source_base,
        context="source",
        must_exist=True,
        allow_outside=source_root is None and Path(raw_source).is_absolute(),
    )
    relative_source = Path(record.get("source_relative_path", ""))
    if (
        not relative_source.parts
        or relative_source.is_absolute()
        or ".." in relative_source.parts
        or source.parts[-len(relative_source.parts) :] != relative_source.parts
    ):
        raise CertificationError("source path escapes its package identity binding")
    declared = manifest.get("input_hashes")
    verify_hash_map(source, declared, context="source")
    if binding.get("source_role_hashes") != declared:
        raise CertificationError("source binding hashes differ from manifest")
    validate_source_role_inventory(source, manifest, binding)

def validate_source_role_inventory(
    source: Path,
    manifest: dict[str, Any],
    binding: dict[str, Any],
) -> None:
    """Verify declared source-role bytes without review routing semantics."""
    declared = manifest.get("input_hashes")
    inventory = manifest.get("source_role_inventory")
    if (
        not isinstance(declared, dict)
        or not isinstance(inventory, dict)
        or binding.get("source_role_inventory") != inventory
    ):
        raise CertificationError("source role inventory is absent or stale")
    for relative, expected_hash in declared.items():
        path = source / relative
        if not path.is_file() or path.is_symlink():
            raise CertificationError(f"source role is missing or unsafe: {relative}")
        if sha256_file(path) != expected_hash:
            raise CertificationError(f"source role bytes changed: {relative}")
        item = inventory.get(relative)
        if not isinstance(item, dict) or item.get("sha256") != expected_hash:
            raise CertificationError(f"source role inventory differs: {relative}")


def verify_external_bytes(
    record: dict[str, Any],
    manifest: dict[str, Any],
    *,
    batch: Path,
) -> None:
    evidence = record.get("evidence")
    if not isinstance(evidence, dict):
        raise CertificationError("record evidence is absent")
    for field, path_field in (("assessment_hashes", "assessment_paths"),):
        declared = manifest.get(field, {})
        if declared is None:
            declared = {}
        if not isinstance(declared, dict):
            raise CertificationError(f"manifest {field} is invalid")
        if not declared:
            paths = evidence.get(path_field, {})
            if paths:
                raise CertificationError(
                    f"{field} declarations are absent but paths are present"
                )
            continue
        paths = evidence.get(path_field)
        if not isinstance(paths, dict) or set(paths) != set(declared):
            raise CertificationError(f"{field} paths are absent or incomplete")
        for name, expected in sorted(declared.items()):
            external = resolve_external(
                paths[name], base=batch, context=f"{field} {name}"
            )
            actual = path_hash(external)
            if actual != expected:
                raise CertificationError(f"{field} bytes are stale: {name}")


def verify_bundle_files(
    batch: Path,
    report_path: Path,
    manifest_path: Path,
    checker_path: Path,
    manifest: dict[str, Any],
    cli_evidence: dict[str, Any],
) -> str:
    output_hashes = manifest.get("output_hashes")
    if not isinstance(output_hashes, dict) or not output_hashes:
        raise CertificationError("audit bundle hashes are absent")
    declared_bundle_hash = manifest.get("bundle_hash")
    if not isinstance(declared_bundle_hash, str):
        raise CertificationError("audit bundle hash is absent")
    if declared_bundle_hash != canonical_json_hash(output_hashes):
        raise CertificationError("audit bundle hash is stale")
    if cli_evidence.get("audit_bundle_hash") != declared_bundle_hash:
        raise CertificationError("persisted audit bundle hash is stale")
    for relative, expected in sorted(output_hashes.items()):
        if not isinstance(relative, str):
            raise CertificationError("audit bundle hash path is invalid")
        relative_path = Path(relative)
        if (
            relative_path.is_absolute()
            or ".." in relative_path.parts
            or not isinstance(expected, str)
        ):
            raise CertificationError("audit bundle hash path is invalid")
        path = report_path.parent / relative
        reject_symlink_components(path, boundary=report_path.parent)
        if not path.is_file() or file_hash(path) != expected:
            raise CertificationError(
                f"audit bundle bytes do not match declared hash: {relative}"
            )
    expected_paths = {
        "report_path": report_path,
        "manifest_path": manifest_path,
        "checker_tests_path": checker_path,
    }
    for name, path in expected_paths.items():
        expected = cli_evidence.get(
            {
                "report_path": "report_hash",
                "manifest_path": "manifest_hash",
                "checker_tests_path": "checker_tests_hash",
            }[name]
        )
        if not isinstance(expected, str) or file_hash(path) != expected:
            raise CertificationError(f"{name} bytes are stale")
    return declared_bundle_hash


def validate_canonical(
    value: Any,
    *,
    context: str,
    expected_decision: str | None = None,
    expected_status: str | None = None,
) -> dict[str, str]:
    try:
        fields = require_canonical_fields(
            value,
            expected_repair_decision=expected_decision,
            expected_repair_status=expected_status,
        )
    except (TypeError, ValueError) as exc:
        raise CertificationError(f"{context} canonical fields are invalid") from exc
    return fields


def validate_dimensions(report: dict[str, Any]) -> None:
    dimensions = report.get("dimensions_v11")
    if not isinstance(dimensions, list) or [
        item.get("dimension") for item in dimensions
    ] != list(DIMENSION_MAX_POINTS):
        raise CertificationError("v11 dimensions are missing or reordered")
    for item in dimensions:
        name = item["dimension"]
        if (
            item.get("weight") != DIMENSION_MAX_POINTS[name]
            or item.get("max_points") != DIMENSION_MAX_POINTS[name]
        ):
            raise CertificationError(f"invalid v11 dimension maximum: {name}")
        earned = item.get("points_earned")
        if earned is not None and (
            isinstance(earned, bool)
            or not isinstance(earned, (int, float))
            or not 0 <= earned <= DIMENSION_MAX_POINTS[name]
        ):
            raise CertificationError(f"invalid v11 dimension score: {name}")
        normalized = item.get("normalized")
        if earned is None or normalized != round(
            float(earned) / DIMENSION_MAX_POINTS[name] * 100, 4
        ):
            raise CertificationError(f"v11 dimension normalization is invalid: {name}")
        expected_status = (
            "FAIL"
            if normalized < 50
            else "WARNING"
            if normalized < 80
            else "PASS"
        )
        if item.get("status") != expected_status:
            raise CertificationError(f"v11 dimension status is invalid: {name}")


def validate_score(report: dict[str, Any], cli_scoring: Any) -> None:
    summary = report.get("summary")
    if not isinstance(summary, dict):
        raise CertificationError("PASS score summary is absent")
    score = summary.get("total_score")
    if (
        isinstance(score, bool)
        or not isinstance(score, (int, float))
        or not math.isfinite(float(score))
        or not PASS_THRESHOLD <= float(score) <= 100
    ):
        raise CertificationError("PASS score is absent, out of bounds, or below threshold")
    dimensions = report.get("dimensions_v11")
    expected_score = round(
        sum(
            float(item["weight"]) * float(item["normalized"])
            for item in dimensions
        )
        / sum(float(item["weight"]) for item in dimensions),
        2,
    )
    if expected_score != score:
        raise CertificationError("PASS score does not equal v11 dimensions")
    if (
        not isinstance(cli_scoring, dict)
        or cli_scoring.get("total_score") != score
        or cli_scoring.get("final_verdict") != "PASS"
        or cli_scoring.get("dimensions_v11") != dimensions
        or cli_scoring.get("hard_gates") != report.get("hard_gates")
    ):
        raise CertificationError("persisted PASS scoring snapshot is stale")
    snapshot = {
        key: value for key, value in cli_scoring.items() if key != "snapshot_hash"
    }
    if cli_scoring.get("snapshot_hash") != canonical_json_hash(snapshot):
        raise CertificationError("persisted PASS scoring snapshot hash is stale")


def validate_hard_gate_schema(
    report: dict[str, Any],
    *,
    require_all_pass: bool,
) -> None:
    gates = report.get("hard_gates")
    if not isinstance(gates, list) or [
        item.get("code") for item in gates
    ] != list(HARD_GATES):
        raise CertificationError("Hard Gates are missing or not exactly four")
    for gate in gates:
        if gate.get("status") not in {"PASS", "FAIL", "NOT_ASSESSABLE"}:
            raise CertificationError("Hard Gate status is invalid")
        if require_all_pass and gate.get("status") != "PASS":
            raise CertificationError("all four Hard Gates must explicitly PASS")


def validate_hard_gates(report: dict[str, Any]) -> None:
    validate_hard_gate_schema(report, require_all_pass=True)


def validate_repair(
    record: dict[str, Any],
    *,
    batch: Path,
    source_audit_id: str,
    review_fields: dict[str, str],
) -> None:
    fields = validate_canonical(record, context="record")
    repair_status = fields["repair_status"]
    repair_decision = fields["repair_decision"]
    if repair_status == "NOT_APPLICABLE":
        if repair_decision != "NOT_REQUIRED":
            raise CertificationError("original entry has a repair decision")
        return
    repair = record.get("evidence", {}).get("repair_binding")
    if not isinstance(repair, dict):
        raise CertificationError("repaired entry lacks repair binding")
    raw_manifest = repair.get("repair_manifest_path")
    repair_manifest_path = resolve_external(
        raw_manifest, base=batch, context="repair manifest"
    )
    repair_manifest = read_json(repair_manifest_path, "repair manifest")
    if (
        repair_manifest.get("schema_version") != "0.1"
        or repair_manifest.get("source_audit_id") != source_audit_id
        or not isinstance(repair_manifest.get("repair_id"), str)
        or not repair_manifest["repair_id"]
    ):
        raise CertificationError("repair source audit binding is stale")
    validate_canonical(
        repair_manifest,
        context="repair manifest",
        expected_decision=repair_decision,
        expected_status=repair_status,
    )
    bundle_dir = resolve_external(
        repair.get("bundle_path"), base=batch, context="repair bundle"
    )
    if not bundle_dir.is_dir():
        raise CertificationError("repair bundle is absent")
    missing = [
        name
        for name in REPAIR_BUNDLE_FILES
        if not (bundle_dir / name).is_file()
    ]
    if missing:
        raise CertificationError(f"repair bundle is incomplete: {missing}")
    values: dict[str, Any] = {}
    for name in REPAIR_BUNDLE_FILES:
        path = bundle_dir / name
        reject_symlink_components(path, boundary=bundle_dir)
        if name.endswith(".json"):
            values[name] = read_json(path, f"repair bundle {name}")
    repair_log = (bundle_dir / "repair.log").read_text(encoding="utf-8")
    values["repair.log"] = repair_log
    try:
        semantic_fields = validate_repair_bundle_semantics(
            values,
            repair_log=repair_log,
        )
    except ValueError as exc:
        raise CertificationError(f"repair bundle semantic schema: {exc}") from exc
    if semantic_fields != fields:
        raise CertificationError("repair bundle canonical fields are stale")
    history = values["history.json"]
    plan = values["repair_plan.json"]
    comparison = values["re_audit_comparison.json"]
    package_identity = plan.get("package_identity", {})
    package_id = record.get("package_id")
    package_matches = (
        package_identity.get("package_id") == package_id
        if "package_id" in package_identity
        else package_identity.get("directory_name") == Path(package_id).name
        if isinstance(package_id, str)
        else False
    )
    if (
        repair_manifest.get("finding_id") != plan.get("finding_id")
        or repair_manifest.get("package_identity")
        != plan.get("package_identity")
        or history.get("audit_id") != source_audit_id
        or repair.get("source_audit_id") != source_audit_id
        or repair.get("finding_id") != plan.get("finding_id")
        or repair.get("package_identity") != plan.get("package_identity")
        or not package_matches
    ):
        raise CertificationError(
            "repair manifest/index audit/finding/package identity is stale"
        )
    if history.get("bundle_complete") is not True:
        raise CertificationError("repair history does not attest completeness")
    if history.get("bundle_files") != list(REPAIR_BUNDLE_FILES):
        raise CertificationError("repair history bundle schema is stale")
    if history.get("repair_status", repair_status) != repair_status:
        raise CertificationError("repair history status is stale")
    history_fields = validate_canonical(history, context="repair history")
    if history_fields != fields:
        raise CertificationError("repair history canonical fields are stale")
    bundle_hashes = history.get("bundle_hashes")
    if not isinstance(bundle_hashes, dict) or set(bundle_hashes) != {
        name for name in REPAIR_BUNDLE_FILES if name != "history.json"
    }:
        raise CertificationError("repair bundle hashes are absent")
    for name, expected in sorted(bundle_hashes.items()):
        if file_hash(bundle_dir / name) != expected:
            raise CertificationError(f"repair bundle bytes are stale: {name}")
    if history.get("bundle_digest") != canonical_json_hash(bundle_hashes):
        raise CertificationError("repair bundle digest is stale")
    if repair_status == "REPAIRED":
        reaudit_path = resolve_external(
            repair.get("reaudit_report_path"),
            base=batch,
            context="repair re-audit report",
        )
        reaudit_manifest_path = resolve_external(
            repair.get("reaudit_manifest_path"),
            base=batch,
            context="repair re-audit manifest",
        )
        if (
            file_hash(reaudit_path) != repair.get("reaudit_report_hash")
            or file_hash(reaudit_manifest_path)
            != repair.get("reaudit_manifest_hash")
            or repair_manifest.get("reaudit_report_hash")
            != repair.get("reaudit_report_hash")
            or repair_manifest.get("reaudit_manifest_hash")
            != repair.get("reaudit_manifest_hash")
        ):
            raise CertificationError("repair re-audit hashes are stale")
        reaudit = read_json(reaudit_path, "repair re-audit report")
        reaudit_manifest = read_json(
            reaudit_manifest_path,
            "repair re-audit manifest",
        )
        reaudit_id = comparison.get("reaudit_audit_id")
        if (
            not isinstance(reaudit_id, str)
            or reaudit.get("audit_id") != reaudit_id
            or reaudit_manifest.get("audit_id") != reaudit_id
            or repair_manifest.get("reaudit_audit_id") != reaudit_id
            or repair.get("reaudit_audit_id") != reaudit_id
        ):
            raise CertificationError("repair re-audit identity is forged")
        reaudit_output_hashes = reaudit_manifest.get("output_hashes")
        if (
            not isinstance(reaudit_output_hashes, dict)
            or reaudit_manifest.get("bundle_hash")
            != canonical_json_hash(reaudit_output_hashes)
            or reaudit_output_hashes.get("audit_report.json")
            != file_hash(reaudit_path)
        ):
            raise CertificationError("repair re-audit bundle is stale")
        if (
            reaudit_manifest.get("review_implementation")
            != collect_review_implementation_hashes()
            or reaudit.get("audit_binding", {}).get("source_hashes")
            != reaudit_manifest.get("input_hashes")
            or reaudit.get("audit_binding", {}).get("implementation_hash")
            != reaudit_manifest.get("review_implementation", {}).get(
                "aggregate_hash"
            )
        ):
            raise CertificationError("repair re-audit source binding is stale")
        for relative, expected_hash in reaudit_output_hashes.items():
            artifact = reaudit_path.parent / relative
            reject_symlink_components(
                artifact,
                boundary=reaudit_path.parent,
            )
            if not artifact.is_file() or file_hash(artifact) != expected_hash:
                raise CertificationError("repair re-audit bundle bytes are stale")
        validate_persisted_reaudit_pass(reaudit)
        reaudit_fields = validate_canonical(reaudit, context="repair re-audit")
        if reaudit_fields["review_verdict"] != "PASS":
            raise CertificationError("published repair re-audit is not PASS")
        if reaudit_fields["publishability"] != review_fields["publishability"]:
            raise CertificationError("repaired PASS publishability differs")
        if repair_status == "REPAIRED":
            try:
                deterministic = resolve_publication_contract(
                    reaudit.get("deterministic_contract"),
                    reaudit.get("effective_deterministic_contract"),
                    reaudit.get("agent_contract_assessment"),
                )
            except (TypeError, ValueError) as exc:
                raise CertificationError(
                    "REPAIRED re-audit lacks valid deterministic CLEAN evidence"
                ) from exc
            if deterministic["repair_summary"]["state"] != "CLEAN":
                raise CertificationError(
                    "REPAIRED re-audit is not deterministically CLEAN"
                )
            if not reaudit_has_no_hard_gate_for_certification(reaudit):
                raise CertificationError(
                    "REPAIRED re-audit contains a failed Hard Gate"
                )


def validate_record(
    record: dict[str, Any],
    *,
    batch: Path,
    source_root: Path | None,
) -> dict[str, Any]:
    if not isinstance(record, dict):
        raise CertificationError("batch record is not an object")
    fields = validate_canonical(record, context="record")
    evidence = record.get("evidence")
    if not isinstance(evidence, dict):
        raise CertificationError("record evidence is absent")
    identity = evidence.get("source_binding", {}).get("cli_audit_identity", {})
    if identity.get("status") != "VALIDATED":
        raise CertificationError("source audit identity is not validated")
    source_binding = evidence.get("source_binding", {})
    package_id = record.get("package_id")
    source_relative_path = record.get("source_relative_path")
    if (
        not isinstance(package_id, str)
        or not package_id.strip()
        or not isinstance(source_relative_path, str)
        or not source_relative_path.strip()
        or source_binding.get("package_id") != package_id
        or source_binding.get("source_relative_path") != source_relative_path
        or identity.get("package_id") != package_id
        or identity.get("source_relative_path") != source_relative_path
    ):
        raise CertificationError("package/source/audit identity binding is stale")
    report_path = resolve_external(
        identity.get("report_path"), base=batch, context="audit report"
    )
    manifest_path = resolve_external(
        identity.get("manifest_path"), base=batch, context="audit manifest"
    )
    checker_path = resolve_external(
        evidence.get("cli_evidence", {}).get("checker_tests_path"),
        base=batch,
        context="checker tests",
    )
    try:
        report = require_schema(
            read_json(report_path, "audit report"),
            AUDIT_REPORT_SCHEMA_VERSION,
            "audit report",
        )
        manifest = require_schema(
            read_json(manifest_path, "audit manifest"),
            AUDIT_MANIFEST_SCHEMA_VERSION,
            "audit manifest",
        )
        checker = require_schema(
            read_json(checker_path, "checker tests"),
            CHECKER_TESTS_SCHEMA_VERSION,
            "checker tests",
        )
    except (TypeError, ValueError) as exc:
        raise CertificationError("audit artifacts use an unsupported schema") from exc
    if not isinstance(report.get("evidence_contract"), dict):
        raise CertificationError("evidence contract is absent")
    if report.get("audit_id") != identity.get("audit_id"):
        raise CertificationError("report audit identity is stale")
    if manifest.get("audit_id") != identity.get("audit_id"):
        raise CertificationError("manifest audit identity is stale")
    report_fields = validate_canonical(report, context="audit report")
    disposition_path = report_path.with_name("disposition.json")
    disposition = read_json(disposition_path, "disposition")
    disposition_fields = validate_canonical(disposition, context="disposition")
    if fields != report_fields or fields != disposition_fields:
        raise CertificationError("canonical fields differ across artifacts")
    validate_report_canonical_fields(report, fields)
    summary = report.get("summary", {})
    if (
        summary.get("scoring_version") != SCORING_VERSION
        or summary.get("final_verdict") != "PASS"
        or summary.get("hard_gate_triggered") is not False
    ):
        raise CertificationError("report does not contain an authoritative PASS")
    if manifest.get("review_lane") != REVIEW_LANE:
        raise CertificationError("dual-lane configuration is absent or stale")
    if report.get("configuration", {}).get("review_lane") != REVIEW_LANE:
        raise CertificationError("dual-lane configuration is absent or stale")
    implementation = manifest.get("review_implementation")
    if implementation != collect_review_implementation_hashes():
        raise CertificationError("stale Review implementation hash")
    if evidence.get("cli_evidence", {}).get("review_implementation") != implementation:
        raise CertificationError("persisted implementation binding is stale")
    if source_binding.get("source_role_hashes") != manifest.get("input_hashes"):
        raise CertificationError("source hashes are absent or stale")
    verify_source_bytes(record, manifest, batch=batch, source_root=source_root)
    verify_external_bytes(record, manifest, batch=batch)
    cli_evidence = evidence.get("cli_evidence")
    if not isinstance(cli_evidence, dict):
        raise CertificationError("persisted CLI evidence is absent")
    evidence_snapshot = {
        key: value for key, value in cli_evidence.items() if key != "snapshot_hash"
    }
    if cli_evidence.get("snapshot_hash") != canonical_json_hash(evidence_snapshot):
        raise CertificationError("persisted CLI evidence snapshot is stale")
    if (
        report.get("audit_binding", {}).get("source_hashes")
        != manifest.get("input_hashes")
        or report.get("audit_binding", {}).get("implementation_hash")
        != implementation.get("aggregate_hash")
    ):
        raise CertificationError("report source/implementation binding is stale")
    bundle_hash = verify_bundle_files(
        batch, report_path, manifest_path, checker_path, manifest, cli_evidence
    )
    validate_dimensions(report)
    validate_hard_gates(report)
    try:
        deterministic = resolve_publication_contract(
            report.get("deterministic_contract"),
            report.get("effective_deterministic_contract"),
            report.get("agent_contract_assessment"),
        )
    except (TypeError, ValueError) as exc:
        raise CertificationError(
            "certified PASS lacks valid deterministic CLEAN evidence"
        ) from exc
    if deterministic["repair_summary"]["state"] != "CLEAN":
        raise CertificationError(
            "certified PASS is not deterministically CLEAN"
        )
    validate_score(report, evidence.get("cli_scoring"))
    validate_repair(
        record,
        batch=batch,
        source_audit_id=identity["audit_id"],
        review_fields=report_fields,
    )
    return {
        "package_id": record.get("package_id"),
        "source_relative_path": record.get("source_relative_path"),
        "review_verdict": fields["review_verdict"],
        "publishability": fields["publishability"],
        "repair_decision": fields["repair_decision"],
        "repair_status": fields["repair_status"],
        "audit_id": identity["audit_id"],
        "audit_bundle_hash": bundle_hash,
        "review_implementation_hash": implementation["aggregate_hash"],
        "selection_rank": record.get("selection_rank", record.get("discovery_rank")),
        "global_rank": record.get("global_rank"),
    }


def recompute_record_eligibility(
    record: dict[str, Any],
    *,
    batch: Path,
    source_root: Path | None,
) -> bool:
    evidence = record.get("evidence")
    if not isinstance(evidence, dict):
        raise CertificationError("ordered universe record evidence is absent")
    identity = evidence.get("source_binding", {}).get("cli_audit_identity")
    if not isinstance(identity, dict) or identity.get("status") != "VALIDATED":
        raise CertificationError("ordered universe audit evidence is absent")
    report_path = resolve_external(
        identity.get("report_path"),
        base=batch,
        context="ordered universe audit report",
    )
    manifest_path = resolve_external(
        identity.get("manifest_path"),
        base=batch,
        context="ordered universe audit manifest",
    )
    checker_path = resolve_external(
        evidence.get("cli_evidence", {}).get("checker_tests_path"),
        base=batch,
        context="ordered universe checker evidence",
    )
    report = read_json(report_path, "ordered universe audit report")
    manifest = read_json(manifest_path, "ordered universe audit manifest")
    read_json(checker_path, "ordered universe checker evidence")
    if (
        report.get("audit_id") != identity.get("audit_id")
        or manifest.get("audit_id") != identity.get("audit_id")
    ):
        raise CertificationError("ordered universe audit identity is stale")
    if manifest.get(
        "review_implementation"
    ) != collect_review_implementation_hashes():
        raise CertificationError("stale Review implementation hash")
    cli_evidence = evidence.get("cli_evidence")
    if not isinstance(cli_evidence, dict):
        raise CertificationError("ordered universe CLI evidence is absent")
    snapshot = {
        key: value for key, value in cli_evidence.items() if key != "snapshot_hash"
    }
    if cli_evidence.get("snapshot_hash") != canonical_json_hash(snapshot):
        raise CertificationError("ordered universe CLI evidence is stale")
    verify_source_bytes(
        record,
        manifest,
        batch=batch,
        source_root=source_root,
    )
    verify_external_bytes(record, manifest, batch=batch)
    verify_bundle_files(
        batch,
        report_path,
        manifest_path,
        checker_path,
        manifest,
        cli_evidence,
    )
    validate_qa_axes(report)
    validate_hard_gate_schema(report, require_all_pass=False)
    score = report.get("summary", {}).get("total_score")
    gates = report.get("hard_gates")
    gate_pass = (
        isinstance(gates, list)
        and [item.get("code") for item in gates] == list(HARD_GATES)
        and all(item.get("status") == "PASS" for item in gates)
    )
    unresolved_high = any(
        isinstance(item, dict)
        and item.get("severity") == "HIGH"
        and item.get("status", "OPEN") not in {"RESOLVED", "CLOSED", "FIXED"}
        for item in report.get("findings", [])
    )
    qa_pass = all(
        axis.get("status") in {"PASS", "WARNING"}
        for axis in report.get("qa_axes", {}).values()
    )
    eligible = (
        not isinstance(score, bool)
        and isinstance(score, (int, float))
        and math.isfinite(float(score))
        and PASS_THRESHOLD <= float(score) <= 100
        and gate_pass
        and not unresolved_high
        and qa_pass
    )
    if eligible or record.get("review_verdict") == "PASS":
        validate_record(record, batch=batch, source_root=source_root)
    return eligible


def validate_selection(
    index: dict[str, Any],
    *,
    batch: Path,
    expected_count: int,
    source_root: Path | None,
) -> list[dict[str, Any]]:
    if index.get("schema_version") not in {
        SCHEMA_VERSION,
        "materials-dual-lane-index/1.0",
    }:
        raise CertificationError(
            "batch index schema is unsupported; evidence contract is absent"
        )
    records = index.get("records")
    if not isinstance(records, list) or len(records) < expected_count:
        raise CertificationError("batch has fewer records than expected")
    policy = index.get("selection_policy")
    if not isinstance(policy, dict):
        raise CertificationError(
            "evidence contract or deterministic selection policy is absent"
        )
    ordering = str(policy.get("ordering", ""))
    if ordering != "deterministic_selected_prefix":
        raise CertificationError("deterministic first-N selection is absent")
    universe_path = resolve_external(
        policy.get("universe_path"),
        base=batch,
        context="ordered universe",
    )
    if file_hash(universe_path) != policy.get("universe_hash"):
        raise CertificationError("ordered universe bytes are stale")
    universe = read_json(universe_path, "ordered universe")
    universe_records = universe.get("records") if isinstance(universe, dict) else None
    if (
        universe.get("schema_version")
        != "materials-final-100-universe/1.0"
        or not isinstance(universe_records, list)
        or not universe_records
    ):
        raise CertificationError("ordered universe schema is invalid")
    universe_ranks: list[int] = []
    universe_ids: list[str] = []
    for item in universe_records:
        if (
            not isinstance(item, dict)
            or not isinstance(item.get("global_rank"), int)
            or isinstance(item.get("global_rank"), bool)
            or item["global_rank"] < 1
            or not isinstance(item.get("package_id"), str)
            or not item["package_id"].strip()
            or not isinstance(item.get("eligible"), bool)
            or item.get("review_verdict")
            not in {"PASS", "CONDITIONAL", "REJECT", "NOT_ASSESSABLE"}
        ):
            raise CertificationError("ordered universe record is malformed")
        universe_ranks.append(item["global_rank"])
        universe_ids.append(item["package_id"])
    if any(
        current >= following
        for current, following in zip(universe_ranks, universe_ranks[1:])
    ):
        raise CertificationError(
            "global ranks must be unique and strictly increasing"
        )
    if len(set(universe_ids)) != len(universe_ids):
        raise CertificationError("ordered universe contains duplicate packages")
    records_by_id = {
        item.get("package_id"): item
        for item in records
        if isinstance(item, dict)
    }
    if set(records_by_id) != set(universe_ids):
        raise CertificationError(
            "first-N ordered universe is missing persisted record evidence"
        )
    package_ids = [item.get("package_id") for item in records]
    if (
        any(not isinstance(item, str) or not item.strip() for item in package_ids)
        or len(set(package_ids)) != len(package_ids)
    ):
        raise CertificationError("first-N selection contains duplicate packages")
    audit_ids = [
        item.get("evidence", {})
        .get("source_binding", {})
        .get("cli_audit_identity", {})
        .get("audit_id")
        for item in records
        if "selection_rank" in item
    ]
    if (
        any(not isinstance(item, str) or not item.strip() for item in audit_ids)
        or len(set(audit_ids)) != len(audit_ids)
    ):
        raise CertificationError("duplicate or absent source audit identity")
    recomputed: list[dict[str, Any]] = []
    for universe_item in universe_records:
        record = records_by_id[universe_item["package_id"]]
        if record.get("global_rank") != universe_item["global_rank"]:
            raise CertificationError("ordered universe rank binding is stale")
        eligible = recompute_record_eligibility(
            record,
            batch=batch,
            source_root=source_root,
        )
        if (
            universe_item.get("eligible") is not eligible
            or universe_item.get("review_verdict")
            != record.get("review_verdict")
        ):
            raise CertificationError(
                "ordered universe eligibility/status label contradicts evidence"
            )
        if eligible:
            recomputed.append(universe_item)
    expected = recomputed[:expected_count]
    if len(expected) != expected_count:
        raise CertificationError("ordered universe has too few eligible PASS records")
    candidate_records = [
        item
        for item in records
        if "selection_rank" in item
    ]
    selected = candidate_records[:expected_count]
    if len(selected) != expected_count:
        raise CertificationError("batch has fewer eligible PASS records than expected")
    selection_ranks = [item.get("selection_rank") for item in selected]
    if selection_ranks != list(range(expected_count)):
        raise CertificationError("first-N selection order is not deterministic")
    selected_pairs = [
        (item.get("global_rank"), item.get("package_id")) for item in selected
    ]
    expected_pairs = [
        (item["global_rank"], item["package_id"]) for item in expected
    ]
    if selected_pairs != expected_pairs:
        raise CertificationError(
            "first-N selection omitted an earlier eligible PASS"
        )
    return selected


def certify(
    batch: Path,
    output: Path,
    *,
    expected_count: int,
    source_root: Path | None = None,
) -> dict[str, Any]:
    batch = batch.expanduser().resolve()
    output = output.expanduser().resolve()
    if not batch.is_dir():
        raise CertificationError(f"batch is not a directory: {batch}")
    if output.exists():
        raise CertificationError(f"certification output already exists: {output}")
    index = read_json(batch / "index.json", "batch index")
    selected = validate_selection(
        index,
        batch=batch,
        expected_count=expected_count,
        source_root=source_root,
    )
    packages = [
        validate_record(record, batch=batch, source_root=source_root)
        for record in selected
    ]
    if len({item["audit_id"] for item in packages}) != len(packages):
        raise CertificationError("certified records reuse a source audit identity")
    implementation_hashes = collect_review_implementation_hashes()
    result = {
        "schema_version": SCHEMA_VERSION,
        "certifier_version": CERTIFIER_VERSION,
        "certified_count": len(packages),
        "expected_count": expected_count,
        "all_evidence_contracts_valid": True,
        "selection_policy": {
            "ordering": index["selection_policy"]["ordering"],
            "selected_prefix": expected_count,
            "first_n_deterministic": True,
        },
        "review_implementation": implementation_hashes,
        "review_implementation_hash": implementation_hashes["aggregate_hash"],
        "packages": packages,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(
        tempfile.mkdtemp(prefix=".materials-final-certification-", dir=output.parent)
    )
    try:
        (temporary / "final_100_pass_index.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        temporary.rename(output)
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--expected-count", type=int, default=100)
    parser.add_argument(
        "--source-root",
        help="optional root for source_relative_path package bytes",
    )
    return parser


def main() -> int:
    arguments = build_parser().parse_args()
    try:
        result = certify(
            Path(arguments.batch),
            Path(arguments.output),
            expected_count=arguments.expected_count,
            source_root=(
                Path(arguments.source_root) if arguments.source_root else None
            ),
        )
        print(json.dumps({"certified_count": result["certified_count"]}))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"final 100 certification failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
