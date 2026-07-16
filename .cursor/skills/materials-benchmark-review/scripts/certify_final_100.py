#!/usr/bin/env python3
"""Certify a persisted, source-bound materials E1 batch.

The certifier is intentionally independent from the batch runner's in-memory
objects.  It reads only persisted bytes, authenticates every selected audit,
and writes the final index only after all selected records pass validation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from canonical_status import (  # noqa: E402
    PUBLISHABILITY_ROUTES,
    REPAIR_DECISIONS,
    REPAIR_STATUSES,
    REVIEW_VERDICTS,
    canonical_fields,
)
from prepare_audit_output import (  # noqa: E402
    collect_review_implementation_hashes,
)


SCHEMA_VERSION = "materials-final-100-index/1.0"
CERTIFIER_VERSION = "materials-final-100-certifier/1.0"
EXECUTION_LEVEL = "E1"
SCORING_VERSION = "materials-review-scoring/1.0"
FIVE_PROBE_CLASSES = (
    "positive",
    "negative",
    "discrimination",
    "equivalence",
    "component_isolation",
)
QA_AXES = (
    "factual_accuracy",
    "answer_leakage",
    "instruction_completeness",
    "checker_instruction_consistency",
)
DIMENSION_MAX_POINTS = {
    "scientific_validity": 35,
    "instruction_answerability": 20,
    "checker_gold_alignment": 25,
    "robustness_discrimination": 15,
    "solution_completeness": 5,
}
HARD_GATES = (
    "NON_MATERIALS_TASK",
    "SCIENTIFIC_TARGET_INVALID",
    "CHECKER_CORE_TASK_UNASSESSED",
    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
)
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


class CertificationError(ValueError):
    """Raised when persisted evidence cannot support certification."""


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
) -> Path:
    if not isinstance(raw, str) or not raw.strip():
        raise CertificationError(f"{context} path is absent")
    candidate = Path(raw).expanduser()
    resolved = (
        candidate.resolve()
        if candidate.is_absolute()
        else (base / candidate).resolve()
    )
    if must_exist and not resolved.exists():
        raise CertificationError(f"{context} bytes are absent: {resolved}")
    if resolved.is_symlink():
        raise CertificationError(f"{context} may not be a symlink")
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
        raw_source, base=source_base, context="source", must_exist=True
    )
    declared = manifest.get("input_hashes")
    verify_hash_map(source, declared, context="source")
    if binding.get("source_role_hashes") != declared:
        raise CertificationError("source binding hashes differ from manifest")


def verify_external_bytes(
    record: dict[str, Any],
    manifest: dict[str, Any],
    *,
    batch: Path,
) -> None:
    evidence = record.get("evidence")
    if not isinstance(evidence, dict):
        raise CertificationError("record evidence is absent")
    for field, path_field in (
        ("assessment_hashes", "assessment_paths"),
        ("fixture_hashes", "fixture_paths"),
    ):
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
        path = report_path.parent / relative
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
        fields = canonical_fields(
            value["review_verdict"],
            publishability=value["publishability"],
            repair_decision=value["repair_decision"],
            repair_status=value["repair_status"],
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise CertificationError(f"{context} canonical fields are invalid") from exc
    if expected_decision is not None and fields["repair_decision"] != expected_decision:
        raise CertificationError(f"{context} repair decision is inconsistent")
    if expected_status is not None and fields["repair_status"] != expected_status:
        raise CertificationError(f"{context} repair status is inconsistent")
    return fields


def validate_qa_axes(report: dict[str, Any]) -> None:
    axes = report.get("qa_axes")
    if not isinstance(axes, dict) or tuple(axes) != QA_AXES:
        raise CertificationError("QA axes are missing or not exactly four")
    for name in QA_AXES:
        axis = axes[name]
        if not isinstance(axis, dict) or axis.get("status") not in {
            "PASS",
            "WARNING",
            "FAIL",
            "NOT_ASSESSABLE",
        }:
            raise CertificationError(f"invalid QA axis: {name}")
        if not isinstance(axis.get("evidence"), list) or not axis["evidence"]:
            raise CertificationError(f"QA axis evidence is missing: {name}")
        if axis["status"] == "NOT_ASSESSABLE" and not axis.get("limitations"):
            raise CertificationError(f"QA axis limitation is missing: {name}")


def validate_dimensions(report: dict[str, Any]) -> None:
    dimensions = report.get("dimension_scores")
    if not isinstance(dimensions, list) or [
        item.get("dimension") for item in dimensions
    ] != list(DIMENSION_MAX_POINTS):
        raise CertificationError("weighted dimensions are missing or reordered")
    for item in dimensions:
        name = item["dimension"]
        if item.get("max_points") != DIMENSION_MAX_POINTS[name]:
            raise CertificationError(f"invalid weighted dimension maximum: {name}")
        earned = item.get("points_earned")
        if earned is not None and (
            isinstance(earned, bool)
            or not isinstance(earned, (int, float))
            or not 0 <= earned <= DIMENSION_MAX_POINTS[name]
        ):
            raise CertificationError(f"invalid weighted dimension score: {name}")
        if not isinstance(item.get("evidence"), list) or not item["evidence"]:
            raise CertificationError(f"weighted dimension evidence is missing: {name}")


def validate_hard_gates(report: dict[str, Any]) -> None:
    gates = report.get("hard_gates")
    if not isinstance(gates, list) or [
        item.get("code") for item in gates
    ] != list(HARD_GATES):
        raise CertificationError("Hard Gates are missing or not exactly four")
    for gate in gates:
        if gate.get("status") not in {"PASS", "FAIL", "NOT_ASSESSABLE"}:
            raise CertificationError("Hard Gate status is invalid")
        if not isinstance(gate.get("evidence"), list) or not gate["evidence"]:
            raise CertificationError("Hard Gate evidence is missing")
        if not isinstance(gate.get("affected_locations"), list) or not gate[
            "affected_locations"
        ]:
            raise CertificationError("Hard Gate affected locations are missing")


def validate_probes(checker: dict[str, Any]) -> None:
    coverage = checker.get("probe_coverage")
    if not isinstance(coverage, dict) or tuple(coverage) != FIVE_PROBE_CLASSES:
        raise CertificationError("probe provenance is incomplete")
    for name in FIVE_PROBE_CLASSES:
        probe = coverage[name]
        if not isinstance(probe, dict) or not isinstance(
            probe.get("provenance"), dict
        ):
            raise CertificationError(f"probe provenance is incomplete: {name}")
        provenance = probe["provenance"]
        if name == "positive":
            if provenance.get("oracle_used") is not True:
                raise CertificationError("positive probe is not Oracle-bound")
        elif provenance.get("oracle_used") is not False:
            raise CertificationError(f"non-positive probe crossed Oracle boundary: {name}")


def validate_boundaries(report: dict[str, Any], checker: dict[str, Any]) -> None:
    oracle = checker.get("solution_oracle")
    if not isinstance(oracle, dict) or oracle.get("scientific_evidence") is not False:
        raise CertificationError("Oracle scientific evidence boundary is invalid")
    if checker.get("solution_content_inspected") is not False:
        raise CertificationError("Oracle content boundary is invalid")
    if report.get("scope", {}).get("solution_content_inspected") is not False:
        raise CertificationError("report crosses Oracle content boundary")
    gold = report.get("gold_provenance")
    if not isinstance(gold, dict) or gold.get("oracle_used") is not False:
        raise CertificationError("Gold provenance crosses Oracle boundary")


def validate_paper_parent(
    report: dict[str, Any],
    manifest: dict[str, Any],
    cli_evidence: dict[str, Any],
) -> None:
    configuration = report.get("configuration", {})
    mode = configuration.get("paper_mode")
    parent = manifest.get("parent_audit_id")
    binding = report.get("audit_binding", {})
    if mode == "paper_grounded":
        if not isinstance(parent, str) or not parent:
            raise CertificationError("paper parent binding is absent")
        if binding.get("parent_audit_id") != parent:
            raise CertificationError("paper parent binding is stale")
        stage = cli_evidence.get("stage_binding", {})
        if stage.get("no_paper_audit_id") != parent:
            raise CertificationError("paper no-paper parent binding is stale")
    elif mode == "no_paper":
        if parent not in {None, ""}:
            raise CertificationError("no-paper audit has an unexpected parent")
    else:
        raise CertificationError("E1 paper mode is invalid")


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
    if repair_manifest.get("source_audit_id") != source_audit_id:
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
    missing = [name for name in REPAIR_BUNDLE_FILES if not (bundle_dir / name).is_file()]
    if missing:
        raise CertificationError(f"repair bundle is incomplete: {missing}")
    history = read_json(bundle_dir / "history.json", "repair history")
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
    if repair_status == "PUBLISHED":
        reaudit_path = resolve_external(
            repair.get("reaudit_report_path"),
            base=batch,
            context="repair re-audit report",
        )
        reaudit = read_json(reaudit_path, "repair re-audit report")
        reaudit_fields = validate_canonical(reaudit, context="repair re-audit")
        if reaudit_fields["review_verdict"] != "PASS":
            raise CertificationError("published repair re-audit is not PASS")
        if reaudit_fields["publishability"] != review_fields["publishability"]:
            raise CertificationError("repaired PASS publishability differs")


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
    report = read_json(report_path, "audit report")
    manifest = read_json(manifest_path, "audit manifest")
    checker = read_json(checker_path, "checker tests")
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
    if report.get("summary", {}).get("final_verdict") != fields["review_verdict"]:
        raise CertificationError("report verdict is not canonical")
    if report.get("summary", {}).get("disposition") != fields["publishability"]:
        raise CertificationError("report publishability is not canonical")
    if manifest.get("configuration", {}).get("execution_level", EXECUTION_LEVEL) != EXECUTION_LEVEL:
        raise CertificationError("E1 configuration is absent or stale")
    if report.get("configuration", {}).get("execution_level") != EXECUTION_LEVEL:
        raise CertificationError("E1 configuration is absent or stale")
    implementation = manifest.get("review_implementation")
    if implementation != collect_review_implementation_hashes():
        raise CertificationError("stale Review implementation hash")
    if evidence.get("cli_evidence", {}).get("review_implementation") != implementation:
        raise CertificationError("persisted implementation binding is stale")
    source_binding = evidence.get("source_binding", {})
    if source_binding.get("source_role_hashes") != manifest.get("input_hashes"):
        raise CertificationError("source hashes are absent or stale")
    verify_source_bytes(record, manifest, batch=batch, source_root=source_root)
    verify_external_bytes(record, manifest, batch=batch)
    cli_evidence = evidence.get("cli_evidence")
    if not isinstance(cli_evidence, dict):
        raise CertificationError("persisted CLI evidence is absent")
    bundle_hash = verify_bundle_files(
        batch, report_path, manifest_path, checker_path, manifest, cli_evidence
    )
    validate_qa_axes(report)
    validate_dimensions(report)
    validate_hard_gates(report)
    validate_probes(checker)
    validate_boundaries(report, checker)
    validate_paper_parent(report, manifest, cli_evidence)
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
    }


def validate_selection(index: dict[str, Any], expected_count: int) -> list[dict[str, Any]]:
    if index.get("schema_version") not in {
        SCHEMA_VERSION,
        "materials-fast-e1-index/0.2",
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
    if "deterministic" not in ordering and "round_robin" not in ordering:
        raise CertificationError("deterministic first-N selection is absent")
    selected = records[:expected_count]
    ranks = [
        item.get("selection_rank", item.get("discovery_rank"))
        for item in selected
    ]
    if any(not isinstance(rank, int) for rank in ranks) or ranks != sorted(ranks):
        raise CertificationError("first-N selection order is not deterministic")
    if len({item.get("package_id") for item in selected}) != expected_count:
        raise CertificationError("first-N selection contains duplicate packages")
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
    selected = validate_selection(index, expected_count)
    packages = [
        validate_record(record, batch=batch, source_root=source_root)
        for record in selected
    ]
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
        "legacy_v8_role": "IDENTITY_ORDER_SOURCE_BINDING_BASELINE_ONLY",
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
