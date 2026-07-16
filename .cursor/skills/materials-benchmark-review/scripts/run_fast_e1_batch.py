#!/usr/bin/env python3
"""Build a resumable, review-only E1 candidate index for a Harbor corpus."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import shutil
import subprocess
import sys
import time
from collections import Counter, deque
from pathlib import Path
from typing import Any, Callable

sys.dont_write_bytecode = True

from prepare_audit_output import (
    QUALITY_EVIDENCE_ROLES,
    collect_input_hashes,
    collect_review_implementation_hashes,
)
from canonical_status import canonical_fields


SCHEMA_VERSION = "materials-fast-e1-index/0.2"
IDENTITY_MANIFEST_SCHEMA = "materials-fast-e1-sample-identities/1.0"
EVIDENCE_TIER = "E1_USABLE_CANDIDATE"
SCORING_VERSION = "materials-review-scoring/1.0"
RUNNER = Path(__file__).resolve().with_name("run_review.py")
TERMINAL_STATES = {"E1_USABLE_CANDIDATE", "E1_EXCLUDED"}
IDENTITY_FIELDS = (
    "package_id",
    "cluster",
    "theme",
    "paper",
    "source_relative_path",
    "discovery_rank",
)
FORBIDDEN_MANUAL_SCORING_FIELDS = {
    "score",
    "total_score",
    "verdict",
    "final_verdict",
    "dimension_scores",
    "hard_gates",
    "gate_results",
}
DIMENSION_MAX_POINTS = {
    "scientific_validity": 35,
    "instruction_answerability": 20,
    "checker_gold_alignment": 25,
    "robustness_discrimination": 15,
    "solution_completeness": 5,
}
PAPER_SOURCE_ROLES = ("paper/paper.md", "paper/images_manifest.json")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def discover_packages(corpus: Path) -> list[dict[str, Any]]:
    """Discover only the fixed cluster/theme/paper levels.

    Discovery deliberately does not walk a package root, so it cannot enter
    solution/ or any other package role.
    """
    corpus = corpus.expanduser().resolve()
    if not corpus.is_dir():
        raise ValueError(f"corpus is not a directory: {corpus}")
    by_cluster: dict[str, deque[dict[str, Any]]] = {}
    for cluster in sorted(
        path
        for path in corpus.iterdir()
        if path.is_dir() and path.name.startswith("cluster-")
    ):
        packages: list[dict[str, Any]] = []
        for theme in sorted(path for path in cluster.iterdir() if path.is_dir()):
            for paper in sorted(
                path
                for path in theme.iterdir()
                if path.is_dir() and path.name.startswith("paper-")
            ):
                relative = paper.relative_to(corpus).as_posix()
                packages.append(
                    {
                        "package_id": relative,
                        "cluster": cluster.name,
                        "theme": theme.name,
                        "paper": paper.name,
                        "source_relative_path": relative,
                    }
                )
        if packages:
            by_cluster[cluster.name] = deque(packages)

    # Round-robin clusters before taking a second package from any cluster.
    ordered: list[dict[str, Any]] = []
    cluster_names = sorted(by_cluster)
    while any(by_cluster.values()):
        for cluster_name in cluster_names:
            queue = by_cluster[cluster_name]
            if queue:
                record = queue.popleft()
                record["discovery_rank"] = len(ordered)
                ordered.append(record)
    return ordered


def load_identity_manifest(
    path: Path, corpus: Path
) -> list[dict[str, Any]]:
    manifest = json.loads(path.expanduser().resolve().read_text(encoding="utf-8"))
    if (
        manifest.get("schema_version") != IDENTITY_MANIFEST_SCHEMA
        or manifest.get("manifest_role") != "AUTHORITATIVE_SAMPLE_IDENTITY"
        or manifest.get("identity_set_authoritative") is not True
    ):
        raise ValueError("identity manifest does not use the authoritative schema")
    package_ids = manifest.get("package_ids")
    if (
        not isinstance(package_ids, list)
        or not all(isinstance(item, str) and item for item in package_ids)
        or len(package_ids) != manifest.get("sample_count")
    ):
        raise ValueError("identity manifest package_ids/sample_count is invalid")
    if len(set(package_ids)) != len(package_ids):
        raise ValueError("identity manifest contains duplicate package IDs")
    records: list[dict[str, Any]] = []
    for rank, package_id in enumerate(package_ids):
        parts = Path(package_id).parts
        if (
            len(parts) != 3
            or not parts[0].startswith("cluster-")
            or not parts[2].startswith("paper-")
            or not (corpus / package_id).is_dir()
        ):
            raise ValueError(f"invalid or missing frozen package: {package_id}")
        records.append(
            {
                "package_id": package_id,
                "cluster": parts[0],
                "theme": parts[1],
                "paper": parts[2],
                "source_relative_path": package_id,
                "discovery_rank": rank,
            }
        )
    return records


def assessment_paper_mode(path: Path | None) -> str:
    if path is None:
        return "no_paper"
    assessment = json.loads(path.read_text(encoding="utf-8"))
    triggers = assessment.get("paper_triggers")
    return "paper_grounded" if isinstance(triggers, list) and triggers else "no_paper"


def write_no_paper_assessment(source: Path, destination: Path) -> Path:
    assessment = json.loads(source.read_text(encoding="utf-8"))
    for key in ("paper_triggers", "reproduction_type", "dimensions"):
        assessment.pop(key, None)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(assessment, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return destination


def collect_review_source_hashes(root: Path, paper_mode: str) -> dict[str, str]:
    hashes = collect_input_hashes(root)
    if paper_mode == "paper_grounded":
        for relative in PAPER_SOURCE_ROLES:
            path = root / relative
            if not path.is_file() or path.is_symlink():
                raise ValueError(
                    f"paper-grounded source role is missing or unsafe: {relative}"
                )
            hashes[relative] = file_hash(path)
    return dict(sorted(hashes.items()))


def copy_review_package(
    source: Path, destination: Path, paper_mode: str = "no_paper"
) -> None:
    """Copy the confirmed quality evidence into an isolated review package."""
    destination.mkdir(parents=True, exist_ok=True)
    instruction = source / "instruction.md"
    if instruction.is_file():
        shutil.copy2(instruction, destination / "instruction.md")
    if (source / "tests").is_dir():
        shutil.copytree(source / "tests", destination / "tests")
    if (source / "solution/solve.sh").is_file():
        shutil.copytree(source / "solution", destination / "solution")
    else:
        (destination / "solution").mkdir()
    if paper_mode == "paper_grounded":
        shutil.copytree(source / "paper", destination / "paper")


def obvious_resource_failures(resources: Any) -> list[str]:
    """Return only declaration failures that need no network adjudication."""
    if not isinstance(resources, dict):
        return ["RESOURCE_ROOT_NOT_OBJECT"]
    declarations = resources.get("resources")
    if not isinstance(declarations, list):
        return ["RESOURCE_LIST_MISSING_OR_INVALID"]
    failures: list[str] = []
    for position, resource in enumerate(declarations):
        prefix = f"RESOURCE_{position + 1}"
        if not isinstance(resource, dict):
            failures.append(f"{prefix}_NOT_OBJECT")
            continue
        if resource.get("required") is not True:
            continue
        access = resource.get("access")
        if not isinstance(access, dict):
            failures.append(f"{prefix}_REQUIRED_ACCESS_MISSING")
            continue
        method = str(access.get("method", "")).strip().lower()
        if not method:
            failures.append(f"{prefix}_REQUIRED_METHOD_MISSING")
            continue
        values = {
            key: str(access.get(key, "")).strip()
            for key in (
                "url",
                "doi",
                "accession",
                "package",
                "path",
                "query",
                "notes",
            )
        }
        if any(
            part == "solution" or part.startswith("solution/")
            for part in (
                values["package"].replace("\\", "/"),
                values["path"].replace("\\", "/"),
            )
        ):
            failures.append(f"{prefix}_ROUTES_THROUGH_SOLUTION")
        notes = values["notes"] or str(resource.get("notes", "")).strip()
        if method == "inline":
            if not notes:
                failures.append(f"{prefix}_INLINE_VALUE_MISSING")
        elif not any(values.values()):
            failures.append(f"{prefix}_REQUIRED_LOCATOR_MISSING")
    return failures


def compact_checker_evidence(checker: dict[str, Any]) -> dict[str, Any]:
    tests = []
    for case in checker.get("tests", []):
        tests.append(
            {
                "test_type": case.get("test_type"),
                "observed_score": case.get("observed_score"),
                "observed_status": case.get("observed_status"),
                "exit_code": case.get("exit_code"),
                "hard_gate_triggered": case.get("hard_gate_triggered"),
                "runtime_package_contains_solution": (
                    case.get("evidence", {}).get(
                        "runtime_package_contains_solution"
                    )
                ),
            }
        )
    return {
        "pass_threshold": checker.get("pass_threshold"),
        "usable_reward_count": checker.get("usable_reward_count"),
        "test_count": len(tests),
        "runtime": checker.get("runtime", {}),
        "tests": tests,
        "runtime_provenance": checker.get("runtime_provenance", {}),
        "findings": [
            {
                "severity": item.get("severity"),
                "code": item.get("code"),
                "test_type": item.get("test_type"),
            }
            for item in checker.get("findings", [])
        ],
        "solution_content_inspected": checker.get(
            "solution_content_inspected"
        ),
    }


def canonical_json_hash(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def authoritative_cli_scoring(report: dict[str, Any]) -> dict[str, Any]:
    summary = report.get("summary", {})
    execution_level = report.get("configuration", {}).get(
        "execution_level"
    )
    if execution_level != "E1":
        raise ValueError("authoritative CLI snapshot requires execution_level=E1")
    dimensions = report.get("dimension_scores")
    gates = report.get("hard_gates")
    if summary.get("scoring_version") != SCORING_VERSION:
        raise ValueError("CLI report uses an unsupported scoring version")
    if not isinstance(dimensions, list) or {
        item.get("dimension"): item.get("max_points") for item in dimensions
    } != DIMENSION_MAX_POINTS:
        raise ValueError("CLI report dimension schema is invalid")
    if not isinstance(gates, list) or len(gates) != 4:
        raise ValueError("CLI report must contain exactly four Hard Gates")
    total = summary.get("total_score")
    available_points = [item.get("points_earned") for item in dimensions]
    if all(isinstance(item, (int, float)) for item in available_points):
        if total != round(sum(available_points), 2):
            raise ValueError("CLI total does not equal dimension points")
    elif total is not None:
        raise ValueError("CLI total must be null when a dimension is unavailable")
    snapshot = {
        "scoring_version": SCORING_VERSION,
        "execution_level": execution_level,
        "final_verdict": summary.get("final_verdict"),
        "total_score": total,
        "hard_gate_triggered": summary.get("hard_gate_triggered"),
        "dimension_scores": dimensions,
        "hard_gates": gates,
    }
    snapshot["snapshot_hash"] = canonical_json_hash(snapshot)
    return snapshot


def hard_gate_exclusion_reasons(
    hard_gates: list[dict[str, Any]] | None,
) -> list[str]:
    return [
        f"HARD_GATE_{gate['code']}"
        for gate in hard_gates or []
        if gate.get("status") == "FAIL"
        and isinstance(gate.get("code"), str)
    ]


def validate_authoritative_candidate_state(
    record: dict[str, Any], scoring: dict[str, Any]
) -> None:
    if scoring.get("execution_level") != "E1":
        raise ValueError("batch candidate scoring is not bound to E1")
    failed_reasons = hard_gate_exclusion_reasons(
        scoring.get("hard_gates")
    )
    if failed_reasons and record.get("state") != "E1_EXCLUDED":
        raise ValueError("failed Hard Gate cannot be a usable candidate")
    if failed_reasons and not set(failed_reasons).issubset(
        record.get("exclusion_reasons", [])
    ):
        raise ValueError("failed Hard Gate is absent from exclusion reasons")


def reject_manual_scoring_fields(record: dict[str, Any]) -> None:
    forbidden = FORBIDDEN_MANUAL_SCORING_FIELDS & set(record)
    evidence = record.get("evidence")
    if isinstance(evidence, dict):
        forbidden.update(
            FORBIDDEN_MANUAL_SCORING_FIELDS
            & (set(evidence) - {"cli_scoring"})
        )
    if forbidden:
        raise ValueError(
            "manual score/verdict fields are forbidden outside "
            f"evidence.cli_scoring: {sorted(forbidden)}"
        )


def source_binding(
    identity: dict[str, Any],
    source_role_hashes: dict[str, str],
    cli_audit_identity: dict[str, Any] | None = None,
    source_path: Path | None = None,
) -> dict[str, Any]:
    binding = {
        "package_id": identity["package_id"],
        "source_relative_path": identity["source_relative_path"],
        "source_role_hashes": source_role_hashes,
        "cli_audit_identity": cli_audit_identity
        or {
            "status": "NOT_CREATED",
            "package_id": identity["package_id"],
            "source_relative_path": identity["source_relative_path"],
            "audit_id": None,
            "manifest_audit_id": None,
            "benchmark_root": None,
            "manifest_benchmark_root": None,
            "scoring_snapshot_hash": None,
            "report_path": None,
            "manifest_path": None,
        },
    }
    if source_path is not None:
        binding["source_path"] = str(source_path)
    return binding


def validate_record_source_binding(
    record: dict[str, Any],
    identity: dict[str, Any],
    corpus: Path,
    output_dir: Path,
) -> None:
    package_id = identity["package_id"]
    errors: list[str] = []
    reject_manual_scoring_fields(record)
    for field in IDENTITY_FIELDS:
        if record.get(field) != identity[field]:
            errors.append(f"{field} does not match frozen identity")

    evidence = record.get("evidence")
    if not isinstance(evidence, dict):
        errors.append("evidence is missing")
        evidence = {}
    paper_mode = evidence.get("review_paper_mode", "no_paper")
    if paper_mode not in {"no_paper", "paper_grounded"}:
        errors.append("review paper mode is invalid")
        paper_mode = "no_paper"
    source = corpus / identity["source_relative_path"]
    expected_hashes = collect_review_source_hashes(source, paper_mode)
    if evidence.get("input_hashes") != expected_hashes:
        errors.append("CLI input hashes do not exactly match source roles")

    binding = evidence.get("source_binding")
    if not isinstance(binding, dict):
        errors.append("source_binding is missing")
        binding = {}
    if binding.get("package_id") != package_id:
        errors.append("source binding package_id is mismatched")
    if (
        binding.get("source_relative_path")
        != identity["source_relative_path"]
    ):
        errors.append("source binding path is mismatched")
    if binding.get("source_role_hashes") != expected_hashes:
        errors.append("source binding hashes do not exactly match source roles")

    cli_identity = binding.get("cli_audit_identity")
    if not isinstance(cli_identity, dict):
        errors.append("CLI audit identity is missing")
        cli_identity = {}
    if cli_identity.get("package_id") != package_id:
        errors.append("CLI audit package_id is mismatched")
    if (
        cli_identity.get("source_relative_path")
        != identity["source_relative_path"]
    ):
        errors.append("CLI audit source path is mismatched")
    if cli_identity.get("status") == "VALIDATED":
        audit_id = cli_identity.get("audit_id")
        if not audit_id or audit_id != cli_identity.get("manifest_audit_id"):
            errors.append("CLI report/manifest audit IDs differ")
        expected_root = str(
            (
                output_dir
                / ".work"
                / identity["source_relative_path"]
                / "package"
            ).resolve()
        )
        if cli_identity.get("benchmark_root") != expected_root:
            errors.append("CLI benchmark root is not bound to frozen identity")
        if cli_identity.get("manifest_benchmark_root") != expected_root:
            errors.append("CLI manifest root is not bound to frozen identity")
        expected_report_path = (
            Path("cli_reports")
            / identity["source_relative_path"]
            / "audit_report.json"
        ).as_posix()
        expected_manifest_path = (
            Path("cli_reports")
            / identity["source_relative_path"]
            / "audit_manifest.json"
        ).as_posix()
        if cli_identity.get("report_path") != expected_report_path:
            errors.append("CLI report path is not bound to frozen identity")
        if cli_identity.get("manifest_path") != expected_manifest_path:
            errors.append("CLI manifest path is not bound to frozen identity")
        scoring = evidence.get("cli_scoring")
        if not isinstance(scoring, dict):
            errors.append("authoritative CLI scoring snapshot is missing")
        else:
            try:
                validate_authoritative_candidate_state(record, scoring)
            except ValueError as exc:
                errors.append(str(exc))
            snapshot_hash = scoring.get("snapshot_hash")
            unhashed = {
                key: value
                for key, value in scoring.items()
                if key != "snapshot_hash"
            }
            if snapshot_hash != canonical_json_hash(unhashed):
                errors.append("CLI scoring snapshot hash is invalid")
            if cli_identity.get("scoring_snapshot_hash") != snapshot_hash:
                errors.append("CLI scoring snapshot identity is inconsistent")
            report_path = output_dir / expected_report_path
            manifest_path = output_dir / expected_manifest_path
            try:
                persisted_report = json.loads(
                    report_path.read_text(encoding="utf-8")
                )
                persisted_manifest = json.loads(
                    manifest_path.read_text(encoding="utf-8")
                )
                if authoritative_cli_scoring(persisted_report) != scoring:
                    errors.append(
                        "CLI scoring snapshot differs from persisted report"
                    )
                if (
                    persisted_report.get("audit_id") != audit_id
                    or persisted_manifest.get("audit_id") != audit_id
                    or persisted_manifest.get("input_hashes") != expected_hashes
                    or persisted_report.get("configuration", {}).get(
                        "paper_mode"
                    )
                    != paper_mode
                    or persisted_manifest.get("review_implementation")
                    != collect_review_implementation_hashes()
                ):
                    errors.append(
                        "persisted CLI report identity or source hashes differ"
                    )
                if (
                    not isinstance(persisted_manifest.get("bundle_hash"), str)
                    or persisted_manifest.get("bundle_hash")
                    != canonical_json_hash(
                        persisted_manifest.get("output_hashes")
                    )
                ):
                    errors.append("persisted CLI audit bundle hash is absent or stale")
                canonical = canonical_fields(
                    persisted_report.get("summary", {}).get("final_verdict"),
                    publishability=persisted_report.get("summary", {}).get(
                        "disposition"
                    ),
                )
                if any(record.get(key) != value for key, value in canonical.items()):
                    errors.append("persisted CLI canonical fields are inconsistent")
                assessment_hashes = persisted_manifest.get(
                    "assessment_hashes", {}
                )
                if assessment_hashes:
                    assessment_paths = evidence.get("assessment_paths")
                    if (
                        not isinstance(assessment_paths, dict)
                        or set(assessment_paths) != set(assessment_hashes)
                    ):
                        errors.append(
                            "persisted assessment paths are absent or incomplete"
                        )
                    else:
                        for name, expected in assessment_hashes.items():
                            path = output_dir / assessment_paths[name]
                            if not path.is_file() or file_hash(path) != expected:
                                errors.append(
                                    f"persisted assessment bytes are stale: {name}"
                                )
            except (OSError, ValueError, json.JSONDecodeError):
                errors.append("persisted CLI report or manifest is unavailable")
        cli_evidence = evidence.get("cli_evidence")
        if not isinstance(cli_evidence, dict):
            errors.append("persisted CLI evidence snapshot is missing")
        else:
            unhashed_evidence = {
                key: value
                for key, value in cli_evidence.items()
                if key != "snapshot_hash"
            }
            expected_checker_path = (
                Path("cli_reports")
                / identity["source_relative_path"]
                / "checker_tests.json"
            ).as_posix()
            try:
                persisted_checker = json.loads(
                    (output_dir / expected_checker_path).read_text(
                        encoding="utf-8"
                    )
                )
                evidence_matches = (
                    cli_evidence.get("snapshot_hash")
                    == canonical_json_hash(unhashed_evidence)
                    and cli_evidence.get("report_path")
                    == expected_report_path
                    and cli_evidence.get("manifest_path")
                    == expected_manifest_path
                    and cli_evidence.get("checker_tests_path")
                    == expected_checker_path
                    and cli_evidence.get("report_hash")
                    == file_hash(output_dir / expected_report_path)
                    and cli_evidence.get("manifest_hash")
                    == file_hash(output_dir / expected_manifest_path)
                    and cli_evidence.get("checker_tests_hash")
                    == file_hash(output_dir / expected_checker_path)
                    and cli_evidence.get("contract_version")
                    == persisted_report.get("evidence_contract", {}).get(
                        "version"
                    )
                    and cli_evidence.get("materials_qualification")
                    == persisted_report.get("materials_qualification")
                    and cli_evidence.get("paper_trigger_adjudication")
                    == persisted_report.get("paper_trigger_adjudication", [])
                    and cli_evidence.get("paper_mode") == paper_mode
                    and cli_evidence.get("paper_consistency")
                    == persisted_report.get("paper_consistency", {})
                    and cli_evidence.get("qa_axes")
                    == persisted_report.get("qa_axes", {})
                    and cli_evidence.get("probe_coverage")
                    == persisted_checker.get("probe_coverage", {})
                    and cli_evidence.get("review_implementation")
                    == persisted_manifest.get("review_implementation")
                    == collect_review_implementation_hashes()
                    and cli_evidence.get("assessment_paths")
                    == evidence.get("assessment_paths", {})
                )
                if not evidence_matches:
                    errors.append(
                        "persisted CLI evidence snapshot differs from artifacts"
                    )
            except (OSError, ValueError, json.JSONDecodeError):
                errors.append(
                    "persisted CLI evidence snapshot differs from artifacts"
                )
    elif record.get("state") != "E1_EXCLUDED":
        errors.append("terminal candidate lacks a validated CLI audit identity")

    if errors:
        raise ValueError(
            f"source binding validation failed for {package_id}: "
            + "; ".join(errors)
        )


def exclusion_reasons(
    static: dict[str, Any],
    checker: dict[str, Any],
    resource_failures: list[str],
    materials_class: str | None = None,
    hard_gates: list[dict[str, Any]] | None = None,
) -> list[str]:
    reasons: list[str] = []
    parse_status = static.get("parse_status", {})
    missing_or_invalid = [
        role
        for role in QUALITY_EVIDENCE_ROLES
        if parse_status.get(role) != "ok"
    ]
    if missing_or_invalid:
        reasons.append("REQUIRED_ROLES_NOT_PARSEABLE")

    materials_class = materials_class or static.get(
        "materials_prescreen", {}
    ).get("classification")
    if materials_class in {"MAT_WRAPPER", "NON_MAT", "AMBIGUOUS"}:
        reasons.append(f"MATERIALS_{materials_class}")
    elif materials_class not in {"MAT_CORE", "MAT_METHOD"}:
        reasons.append("MATERIALS_CLASS_UNAVAILABLE")

    static_fatal = any(
        item.get("severity") == "FATAL" for item in static.get("issues", [])
    )
    checker_fatal = any(
        item.get("severity") == "FATAL"
        for item in checker.get("findings", [])
    )
    if static_fatal:
        reasons.append("STATIC_FATAL")
    if checker_fatal:
        reasons.append("CHECKER_FATAL")

    tests = checker.get("tests", [])
    usable = checker.get("usable_reward_count")
    if not tests or usable != len(tests):
        reasons.append("CHECKER_REWARD_UNUSABLE")
    if any(item.get("observed_status") != "COMPLETED" for item in tests):
        reasons.append("CHECKER_CASE_CRASHED")
    if checker.get("solution_content_inspected") is not False or any(
        item.get("evidence", {}).get("runtime_package_contains_solution")
        is not False
        for item in tests
    ):
        reasons.append("SOLUTION_BOUNDARY_UNPROVEN")
    if resource_failures:
        reasons.append("CRITICAL_RESOURCE_DECLARATION_FAILURE")
    reasons.extend(hard_gate_exclusion_reasons(hard_gates))
    return list(dict.fromkeys(reasons))


def review_one(
    corpus: Path,
    output_dir: Path,
    identity: dict[str, Any],
    timeout_seconds: int | None,
    assessment_dir: Path | None = None,
) -> dict[str, Any]:
    started = time.monotonic()
    package_id = identity["package_id"]
    source = corpus / identity["source_relative_path"]
    assessment_path = (
        assessment_dir / f"{package_id}.json"
        if assessment_dir is not None
        else None
    )
    requested_paper_mode = assessment_paper_mode(assessment_path)
    paper_mode = "no_paper"
    source_hashes = collect_review_source_hashes(source, paper_mode)
    assessment_hash = (
        "sha256:" + hashlib.sha256(assessment_path.read_bytes()).hexdigest()
        if assessment_path is not None
        else None
    )
    workspace = output_dir / ".work" / package_id
    if workspace.exists():
        shutil.rmtree(workspace)
    package_copy = workspace / "package"
    base = {
        **identity,
        "schema_version": SCHEMA_VERSION,
        **canonical_fields("NOT_ASSESSABLE"),
        "paper_grounded_status": "NOT_ASSESSED",
        "scientifically_confirmed": False,
        "solution_content_inspected": False,
        "evidence": {
            "input_hashes": source_hashes,
            "source_binding": source_binding(identity, source_hashes),
            "taxonomy_assessment_hash": assessment_hash,
            "review_paper_mode": paper_mode,
        },
    }
    try:
        copy_review_package(source, package_copy, "no_paper")

        def execute_review(
            mode: str, assessment: Path | None
        ) -> subprocess.CompletedProcess[str]:
            command = [
                sys.executable,
                str(RUNNER),
                str(package_copy),
                "--paper-mode",
                mode,
                "--execution-level",
                "E1",
            ]
            if assessment is not None:
                command.extend(["--agent-assessment", str(assessment)])
            return subprocess.run(
                command,
                cwd=RUNNER.parent.parent,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                check=False,
            )

        no_paper_assessment = (
            write_no_paper_assessment(
                assessment_path, workspace / "no-paper-assessment.json"
            )
            if assessment_path is not None
            else None
        )
        completed = execute_review("no_paper", no_paper_assessment)
        if completed.returncode != 0:
            return {
                **base,
                "state": "E1_EXCLUDED",
                "evidence_tier": "E1_EXCLUDED",
                "exclusion_reasons": ["REVIEW_RUNNER_FAILED"],
                "runner_error": completed.stderr[-4000:],
                "runtime_seconds": round(time.monotonic() - started, 3),
            }
        audit = package_copy / "benchmark_audit"
        no_paper_report = json.loads(
            (audit / "audit_report.json").read_text(encoding="utf-8")
        )
        no_paper_audit_id = no_paper_report["audit_id"]
        if (
            requested_paper_mode == "paper_grounded"
            and not no_paper_report.get("summary", {}).get(
                "hard_gate_triggered", False
            )
        ):
            for relative in PAPER_SOURCE_ROLES:
                source_path = source / relative
                destination = package_copy / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_path, destination)
            source_hashes.update(
                collect_review_source_hashes(source, "paper_grounded")
            )
            paper_mode = "paper_grounded"
            base["evidence"]["review_paper_mode"] = paper_mode
            completed = execute_review(paper_mode, assessment_path)
            if completed.returncode != 0:
                return {
                    **base,
                    "state": "E1_EXCLUDED",
                    "evidence_tier": "E1_EXCLUDED",
                    "exclusion_reasons": ["PAPER_REVIEW_RUNNER_FAILED"],
                    "runner_error": completed.stderr[-4000:],
                    "runtime_seconds": round(time.monotonic() - started, 3),
                }
        report = json.loads(
            (audit / "audit_report.json").read_text(encoding="utf-8")
        )
        checker = json.loads(
            (audit / "checker_tests.json").read_text(encoding="utf-8")
        )
        static = json.loads(
            (
                audit / "evidence/static_checks/audit_static.json"
            ).read_text(encoding="utf-8")
        )
        audit_manifest = json.loads(
            (audit / "audit_manifest.json").read_text(encoding="utf-8")
        )
        assessment_paths: dict[str, str] = {}
        assessment_hashes = audit_manifest.get("assessment_hashes", {})
        if assessment_hashes:
            if assessment_path is None:
                raise ValueError("CLI assessment source is absent")
            assessment_source = (
                no_paper_assessment
                if paper_mode == "no_paper"
                else assessment_path
            )
            if assessment_source is None or not assessment_source.is_file():
                raise ValueError("CLI assessment bytes are absent")
            assessment_relative = (
                Path("cli_reports")
                / package_id
                / "external"
                / "agent_assessment.json"
            )
            assessment_destination = output_dir / assessment_relative
            assessment_destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(assessment_source, assessment_destination)
            if set(assessment_hashes) != {"agent_assessment"} or (
                file_hash(assessment_destination)
                != assessment_hashes["agent_assessment"]
            ):
                raise ValueError("CLI assessment bytes are stale")
            assessment_paths["agent_assessment"] = assessment_relative.as_posix()
        bundle_hash = audit_manifest.get("bundle_hash")
        if not isinstance(bundle_hash, str):
            raise ValueError("CLI audit bundle hash is absent")
        if bundle_hash != canonical_json_hash(
            audit_manifest.get("output_hashes")
        ):
            raise ValueError("CLI audit bundle hash is stale")
        review_implementation = audit_manifest.get("review_implementation")
        if review_implementation != collect_review_implementation_hashes():
            raise ValueError(
                "CLI audit Review implementation hashes are stale"
            )
        copied_hashes = collect_review_source_hashes(package_copy, paper_mode)
        manifest_hashes = audit_manifest.get("input_hashes")
        expected_cli_root = str(package_copy.resolve())
        if copied_hashes != source_hashes or manifest_hashes != source_hashes:
            raise ValueError(
                "review copy or CLI audit hashes do not match source roles"
            )
        if (
            report.get("audit_id") != audit_manifest.get("audit_id")
            or report.get("benchmark", {}).get("root") != expected_cli_root
            or audit_manifest.get("benchmark_root") != expected_cli_root
        ):
            raise ValueError("CLI audit identity is not bound to review copy")
        resource_failures: list[str] = []
        materials_class = report.get("summary", {}).get("materials_class")
        reasons = exclusion_reasons(
            static,
            checker,
            resource_failures,
            materials_class=materials_class,
            hard_gates=report.get("hard_gates", []),
        )
        if paper_mode != "paper_grounded" and not report.get(
            "summary", {}
        ).get("hard_gate_triggered", False):
            reasons.append("PAPER_GROUNDED_STAGE_REQUIRED")
        checker_evidence = compact_checker_evidence(checker)
        cli_scoring = authoritative_cli_scoring(report)
        report_relative = (
            Path("cli_reports") / package_id / "audit_report.json"
        )
        manifest_relative = (
            Path("cli_reports") / package_id / "audit_manifest.json"
        )
        checker_relative = (
            Path("cli_reports") / package_id / "checker_tests.json"
        )
        (output_dir / report_relative).parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(
            audit,
            output_dir / report_relative.parent,
            dirs_exist_ok=True,
        )
        cli_evidence = {
            "contract_version": report.get("evidence_contract", {}).get(
                "version"
            ),
            "audit_id": report.get("audit_id"),
            "fail_closed": report.get("evidence_contract", {}).get(
                "fail_closed"
            ),
            "gaps": report.get("evidence_contract", {}).get("gaps", []),
            "materials_qualification": report.get(
                "materials_qualification", {}
            ),
            "paper_trigger_adjudication": report.get(
                "paper_trigger_adjudication", []
            ),
            "paper_mode": paper_mode,
            "paper_consistency": report.get("paper_consistency", {}),
            "qa_axes": report.get("qa_axes", {}),
            "probe_coverage": checker.get("probe_coverage", {}),
            "review_implementation": review_implementation,
            "stage_binding": {
                "status": (
                    "PAPER_GROUNDED_BOUND_TO_NO_PAPER"
                    if paper_mode == "paper_grounded"
                    else "NO_PAPER_ONLY"
                ),
                "no_paper_audit_id": no_paper_audit_id,
                "paper_grounded_audit_id": (
                    report["audit_id"]
                    if paper_mode == "paper_grounded"
                    else None
                ),
            },
            "solution_oracle": {
                key: checker.get("solution_oracle", {}).get(key)
                for key in (
                    "used",
                    "status",
                    "positive_mock_available",
                    "attempted",
                    "setup_attempted",
                    "setup_prepared",
                    "producer_started",
                    "executed",
                    "scientific_evidence",
                )
            },
            "report_path": report_relative.as_posix(),
            "manifest_path": manifest_relative.as_posix(),
            "checker_tests_path": checker_relative.as_posix(),
            "report_hash": file_hash(output_dir / report_relative),
            "manifest_hash": file_hash(output_dir / manifest_relative),
            "checker_tests_hash": file_hash(output_dir / checker_relative),
            "audit_bundle_hash": bundle_hash,
            "assessment_paths": assessment_paths,
        }
        cli_evidence["snapshot_hash"] = canonical_json_hash(cli_evidence)
        cli_identity = {
            "status": "VALIDATED",
            "package_id": package_id,
            "source_relative_path": identity["source_relative_path"],
            "audit_id": report["audit_id"],
            "manifest_audit_id": audit_manifest["audit_id"],
            "benchmark_root": report["benchmark"]["root"],
            "manifest_benchmark_root": audit_manifest["benchmark_root"],
            "scoring_snapshot_hash": cli_scoring["snapshot_hash"],
            "report_path": report_relative.as_posix(),
            "manifest_path": manifest_relative.as_posix(),
        }
        return {
            **base,
            **canonical_fields(
                report["summary"]["final_verdict"],
                publishability=report["summary"]["disposition"],
            ),
            "paper_grounded_status": report.get(
                "paper_consistency", {}
            ).get("status", "NOT_ASSESSED"),
            "scientifically_confirmed": (
                report.get("paper_consistency", {}).get("status") == "PASS"
            ),
            "state": "E1_EXCLUDED" if reasons else EVIDENCE_TIER,
            "evidence_tier": "E1_EXCLUDED" if reasons else EVIDENCE_TIER,
            "exclusion_reasons": reasons,
            "evidence": {
                "required_role_status": static.get("parse_status", {}),
                "materials_prescreen": static.get(
                    "materials_prescreen", {}
                ),
                "materials_qualification": report.get(
                    "materials_qualification", {}
                ),
                "static_verdict": static.get("static_verdict"),
                "static_findings": [
                    {
                        "severity": item.get("severity"),
                        "code": item.get("code"),
                    }
                    for item in static.get("issues", [])
                ],
                "checker": checker_evidence,
                "resource_declaration": {
                    "status": "NOT_QUALITY_EVIDENCE",
                    "failure_codes": [],
                    "reachability_assessed": False,
                },
                "cli_scoring": cli_scoring,
                "cli_evidence": cli_evidence,
                "qa_axes": report.get("qa_axes", {}),
                "stage_binding": cli_evidence["stage_binding"],
                "answer_type": report.get("summary", {}).get("answer_type"),
                "input_hashes": source_hashes,
                "source_binding": source_binding(
                    identity,
                    source_hashes,
                    cli_identity,
                    source,
                ),
                "assessment_paths": assessment_paths,
                "taxonomy_assessment_hash": assessment_hash,
                "review_paper_mode": paper_mode,
            },
            "runtime_seconds": round(time.monotonic() - started, 3),
        }
    except subprocess.TimeoutExpired:
        return {
            **base,
            "state": "E1_EXCLUDED",
            "evidence_tier": "E1_EXCLUDED",
            "exclusion_reasons": ["REVIEW_TIMEOUT"],
            "runtime_seconds": round(time.monotonic() - started, 3),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            **base,
            "state": "E1_EXCLUDED",
            "evidence_tier": "E1_EXCLUDED",
            "exclusion_reasons": ["REVIEW_EXCEPTION"],
            "runner_error": repr(exc),
            "runtime_seconds": round(time.monotonic() - started, 3),
        }
    finally:
        if workspace.exists():
            shutil.rmtree(workspace)


def load_ledger(path: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return records
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if record.get("state") in TERMINAL_STATES:
            records[record["package_id"]] = record
    return records


def append_ledger(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        handle.flush()


def summarize(
    all_discovered: list[dict[str, Any]],
    selected_for_screening: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
    target: int,
    screening_wall_clock_seconds: float,
    last_invocation_seconds: float,
    identity_baseline: list[dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any]]:
    records = [
        records_by_id[item["package_id"]]
        for item in selected_for_screening
        if item["package_id"] in records_by_id
    ]
    candidates = [
        item for item in records if item["state"] == EVIDENCE_TIER
    ][:target]
    excluded = [item for item in records if item["state"] == "E1_EXCLUDED"]
    reason_counts: Counter[str] = Counter()
    for record in excluded:
        reason_counts.update(record.get("exclusion_reasons", []))
    diversity = {
        "clusters": len({item["cluster"] for item in candidates}),
        "themes": len({item["theme"] for item in candidates}),
        "answer_types": dict(
            sorted(
                Counter(
                    item.get("evidence", {}).get(
                        "answer_type", "UNAVAILABLE"
                    )
                    for item in candidates
                ).items()
            )
        ),
        "materials_classes": dict(
            sorted(
                Counter(
                    item.get("evidence", {})
                    .get("materials_qualification", {})
                    .get(
                        "classification",
                        item.get("evidence", {})
                        .get("materials_prescreen", {})
                        .get("classification", "UNAVAILABLE"),
                    )
                    for item in candidates
                ).items()
            )
        ),
    }
    counts = {
        "corpus_discovered": len(all_discovered),
        "selected_for_screening": len(selected_for_screening),
        "screened": len(records),
        "excluded": len(excluded),
        "e1_usable_candidates_available": sum(
            item["state"] == EVIDENCE_TIER for item in records
        ),
        "e1_usable_candidates_selected": len(candidates),
        "paper_grounded_confirmed": sum(
            bool(item.get("scientifically_confirmed")) for item in records
        ),
        "excluded_by_reason": dict(sorted(reason_counts.items())),
        "exclusion_reason_counts_overlap": True,
        "candidate_diversity": diversity,
    }
    policy = {
        "ordering": "cluster_round_robin_then_theme_and_paper_lexicographic",
        "candidate_tier": EVIDENCE_TIER,
        "candidate_requirements": [
            "all required Harbor roles parse",
            "authoritative materials qualification, when supplied, or prescreen is MAT_CORE or MAT_METHOD",
            "all real-checker probes emit finite numeric rewards and complete",
            "no static or checker FATAL",
            "no obvious critical resource declaration failure",
            "solution boundary remains uninspected and absent from runtime",
            "paper-grounded E1 is bound to its no-paper parent audit",
        ],
        "claim_boundary": (
            "E1_USABLE_CANDIDATE is a bound paper-grounded audit result; it "
            "does not claim scientific workflow execution or reproduction."
        ),
    }
    index = {
        "schema_version": SCHEMA_VERSION,
        "solution_content_inspected": False,
        "screening_wall_clock_seconds": round(
            screening_wall_clock_seconds, 3
        ),
        "last_invocation_seconds": round(last_invocation_seconds, 3),
        "selection_policy": policy,
        "repair_gate": (
            "READY_FOR_REPAIR"
            if all(
                item["package_id"] in records_by_id
                for item in identity_baseline
            )
            else "BLOCKED_REVIEW_BASELINE_INCOMPLETE"
        ),
        "counts": counts,
        "records": records,
    }
    sample_ids = [
        item["package_id"] for item in identity_baseline
    ]
    manifest = {
        "schema_version": IDENTITY_MANIFEST_SCHEMA,
        "manifest_role": "AUTHORITATIVE_SAMPLE_IDENTITY",
        "identity_set_authoritative": True,
        "sample_count": len(sample_ids),
        "ordering": "deterministic_selected_prefix",
        "package_ids": sample_ids,
    }
    return index, manifest


def discovery_index(
    discovered: list[dict[str, Any]], limit: int | None
) -> dict[str, Any]:
    selected = discovered[:limit]
    return {
        "schema_version": SCHEMA_VERSION,
        "solution_content_inspected": False,
        "selection_policy": {
            "ordering": (
                "cluster_round_robin_then_theme_and_paper_lexicographic"
            )
        },
        "counts": {
            "discovered": len(discovered),
            "indexed": len(selected),
        },
        "records": [
            {
                **item,
                "schema_version": SCHEMA_VERSION,
                "state": "DISCOVERED",
                "solution_content_inspected": False,
            }
            for item in selected
        ],
    }


def run_batch(
    corpus: Path,
    output_dir: Path,
    workers: int,
    max_packages: int | None,
    target: int,
    timeout_seconds: int,
    identity_manifest: Path | None = None,
    assessment_dir: Path | None = None,
    reviewer: Callable[
        [Path, Path, dict[str, Any], int], dict[str, Any]
    ] = review_one,
) -> tuple[dict[str, Any], dict[str, Any]]:
    started = time.monotonic()
    corpus = corpus.expanduser().resolve()
    output_dir = output_dir.expanduser().resolve()
    if output_dir.is_relative_to(corpus):
        raise ValueError("output directory must be outside the source corpus")
    discovered = (
        load_identity_manifest(identity_manifest, corpus)
        if identity_manifest is not None
        else discover_packages(corpus)
    )
    if assessment_dir is not None:
        assessment_dir = assessment_dir.expanduser().resolve()
        if assessment_dir.is_relative_to(corpus):
            raise ValueError("assessment directory must be outside the source corpus")
        missing = [
            item["package_id"]
            for item in discovered[:max_packages]
            if not (assessment_dir / f"{item['package_id']}.json").is_file()
        ]
        if missing:
            raise ValueError(f"taxonomy assessment is missing: {missing[0]}")
    identity_baseline = discovered[:target]
    selected = discovered[:max_packages]
    ledger = output_dir / "results.jsonl"
    completed = load_ledger(ledger)
    for identity in discovered:
        record = completed.get(identity["package_id"])
        if record is not None:
            validate_record_source_binding(
                record,
                identity,
                corpus,
                output_dir,
            )
            expected_assessment_hash = None
            if assessment_dir is not None:
                assessment_path = assessment_dir / f"{identity['package_id']}.json"
                expected_assessment_hash = (
                    "sha256:"
                    + hashlib.sha256(assessment_path.read_bytes()).hexdigest()
                )
            if (
                record.get("evidence", {}).get("taxonomy_assessment_hash")
                != expected_assessment_hash
            ):
                raise ValueError(
                    "completed record taxonomy assessment is missing or stale: "
                    + identity["package_id"]
                )
            expected_paper_mode = assessment_paper_mode(
                assessment_path if assessment_dir is not None else None
            )
            if (
                record.get("evidence", {}).get("review_paper_mode")
                != expected_paper_mode
            ):
                raise ValueError(
                    "completed record paper mode is missing or stale: "
                    + identity["package_id"]
                )
    prior_screening_seconds = 0.0
    prior_index = output_dir / "index.json"
    if prior_index.is_file():
        previous = json.loads(prior_index.read_text(encoding="utf-8"))
        prior_screening_seconds = float(
            previous.get(
                "screening_wall_clock_seconds",
                previous.get("runtime_seconds", 0.0),
            )
        )
    pending = [
        item for item in selected if item["package_id"] not in completed
    ]
    output_dir.mkdir(parents=True, exist_ok=True)
    new_records: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=workers
    ) as executor:
        futures = {
            executor.submit(
                reviewer,
                corpus,
                output_dir,
                item,
                timeout_seconds,
                *([assessment_dir] if reviewer is review_one else []),
            ): item
            for item in pending
        }
        for future in concurrent.futures.as_completed(futures):
            record = future.result()
            identity = futures[future]
            validate_record_source_binding(
                record,
                identity,
                corpus,
                output_dir,
            )
            completed[record["package_id"]] = record
            new_records[record["package_id"]] = record
    for identity in pending:
        append_ledger(ledger, new_records[identity["package_id"]])
    invocation_seconds = time.monotonic() - started
    index, manifest = summarize(
        discovered,
        selected,
        completed,
        target,
        (
            prior_screening_seconds + invocation_seconds
            if pending
            else prior_screening_seconds
        ),
        invocation_seconds,
        identity_baseline,
    )
    write_json(output_dir / "index.json", index)
    write_json(output_dir / "candidate_manifest.json", manifest)
    return index, manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", help="materials_science_questions directory")
    parser.add_argument(
        "--output-dir",
        required=True,
        help="artifact directory outside the source corpus",
    )
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--max-packages", type=int)
    parser.add_argument("--target", type=int, default=100)
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        help="optional whole-review deadline; internal phases retain their own deadlines",
    )
    parser.add_argument(
        "--identity-manifest",
        help="frozen authoritative sample identity manifest",
    )
    parser.add_argument(
        "--assessment-dir",
        help="external package-id-shaped directory of evidence assessments",
    )
    parser.add_argument(
        "--discover-only",
        action="store_true",
        help="write deterministic discovery index without reviewing packages",
    )
    return parser


def main() -> int:
    arguments = build_parser().parse_args()
    try:
        if arguments.workers < 1:
            raise ValueError("workers must be positive")
        if arguments.target < 1:
            raise ValueError("target must be positive")
        corpus = Path(arguments.corpus)
        output_dir = Path(arguments.output_dir).expanduser().resolve()
        if arguments.discover_only:
            discovered = discover_packages(corpus)
            index = discovery_index(discovered, arguments.max_packages)
            write_json(output_dir / "index.json", index)
            print(json.dumps(index["counts"], sort_keys=True))
            return 0
        index, _ = run_batch(
            corpus,
            output_dir,
            workers=arguments.workers,
            max_packages=arguments.max_packages,
            target=arguments.target,
            timeout_seconds=arguments.timeout_seconds,
            identity_manifest=(
                Path(arguments.identity_manifest)
                if arguments.identity_manifest
                else None
            ),
            assessment_dir=(
                Path(arguments.assessment_dir)
                if arguments.assessment_dir
                else None
            ),
        )
        print(json.dumps(index["counts"], sort_keys=True))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"fast E1 batch failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
