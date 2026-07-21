from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from unittest import mock
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]

def external_audit_dir(package: Path) -> Path:
    paper_id = (
        package.name[len("paper-"):]
        if package.name.startswith("paper-")
        else package.name
    )
    path = package.parent / "review_outputs" / paper_id / "benchmark_audit"
    path.mkdir(parents=True, exist_ok=True)
    return path


def external_repair_dir(package: Path) -> Path:
    paper_id = package.name.removeprefix("paper-")
    return package.parent / "review_outputs" / paper_id / "repair"


def external_reaudit_dir(package: Path) -> Path:
    paper_id = package.name.removeprefix("paper-")
    return (
        package.parent
        / "review_outputs"
        / paper_id
        / "repair_reaudit"
        / "benchmark_audit"
    )


REPAIR_RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
    / "run_repair.py"
)
REVIEW_SKILL_ROOT = (
    REPO_ROOT / ".cursor" / "skills" / "materials-benchmark-review"
)
sys.path.insert(0, str(REVIEW_SKILL_ROOT / "scripts"))
from artifact_schema import (  # noqa: E402
    AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
    AUDIT_ATTESTATION_SCHEMA_VERSION,
    AUDIT_BUNDLE_SCHEMA_VERSION,
    AUDIT_MANIFEST_SCHEMA_VERSION,
    AUDIT_REPORT_SCHEMA_VERSION,
    DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
    DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
    DISPOSITION_SCHEMA_VERSION,
    SCORING_SCHEMA_VERSION,
)
import deterministic_contract  # noqa: E402
AUDIT_ID = "audit-source-001"
FINDING_ID = "finding-missing-solve"


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def write_audit_attestation(package: Path) -> Path:
    audit = external_audit_dir(package)
    manifest = json.loads(
        (audit / "audit_manifest.json").read_text(encoding="utf-8")
    )
    report = json.loads((audit / "audit_report.json").read_text(encoding="utf-8"))
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
        relative: sha256_file(path) for relative, path in artifact_paths.items()
    }
    payload = {
        "audit_id": manifest["audit_id"],
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
            "deterministic_core": report["deterministic_core"]["schema_version"],
            "deterministic_probe_results": report["deterministic_core"][
                "probe_results"
            ]["schema_version"],
            "agent_quality": report["agent_quality"]["schema_version"],
            "scoring": report["summary"]["scoring_version"],
        },
        "scoring_schema_version": SCORING_SCHEMA_VERSION,
    }
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    attestation = {
        "schema_version": AUDIT_ATTESTATION_SCHEMA_VERSION,
        **payload,
        "bundle_digest": "sha256:" + hashlib.sha256(encoded).hexdigest(),
    }
    path = package.parent / "audit-attestation.json"
    if path.exists():
        path.chmod(0o644)
    write_json(path, attestation)
    path.chmod(0o444)
    return path


def repair_module() -> Any:
    spec = importlib.util.spec_from_file_location(
        "materials_repair_runner", REPAIR_RUNNER
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bind_plan_to_package(package: Path, value: dict[str, Any]) -> None:
    manifest_path = external_audit_dir(package) / "audit_manifest.json"
    if not manifest_path.is_file():
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    report = json.loads(
        (external_audit_dir(package) / "audit_report.json").read_text(encoding="utf-8")
    )
    digest = repair_module().core_contract_digest(package)
    value.setdefault("core_contract_digest", digest)
    contract = report.get("deterministic_contract")
    if (
        value.get("schema_version")
        == deterministic_contract.DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION
        and isinstance(contract, dict)
    ):
        binding = {
            "schema_version": contract["schema_version"],
            "registry_version": contract["registry_version"],
            "contract_digest": contract["contract_digest"],
            "audit_id": report["audit_id"],
            "required_finding_ids": contract["repair_summary"][
                "required_finding_ids"
            ],
        }
        value["deterministic_contract"] = binding
    value.setdefault(
        "source_audit",
        {
            "audit_id": value["audit_id"],
            "finding_id": value["finding_id"],
            "finding_status": "OPEN",
            "input_hashes": manifest.get("input_hashes", {}),
            "review_implementation": manifest.get("review_implementation", {}),
            "review_lane": report["configuration"]["review_lane"],
            "core_contract_digest": digest,
            "assessment_hashes": {},
        },
    )
    if isinstance(contract, dict) and value.get("deterministic_contract"):
        value["source_audit"]["deterministic_contract"] = value[
            "deterministic_contract"
        ]
    for item in value.get("evidence", []):
        source = item.get("source")
        if not isinstance(source, str) or "source_hash" in item:
            continue
        if source.startswith("benchmark_audit:"):
            local = external_audit_dir(package) / "audit_report.json"
        else:
            local = package / source
        if local.is_file():
            item["source_hash"] = sha256_file(local)
    if value.get("findings"):
        value["findings"][0]["evidence"] = json.loads(
            json.dumps(value.get("evidence", []))
        )


def install_repair_harness(workspace: Path) -> Path:
    harness_root = workspace / "harness"
    shutil.copytree(
        REVIEW_SKILL_ROOT,
        harness_root / "materials-benchmark-review",
    )
    implementation_manifest = (
        harness_root
        / "materials-benchmark-review/references/review-implementation-files.json"
    )
    manifest = json.loads(implementation_manifest.read_text(encoding="utf-8"))
    manifest["files"] = sorted(set(manifest["files"]))
    implementation_manifest.write_text(
        json.dumps(manifest), encoding="utf-8"
    )
    harness_runner = (
        harness_root / "materials-benchmark-repair/scripts/run_repair.py"
    )
    harness_runner.parent.mkdir(parents=True)
    shutil.copy2(REPAIR_RUNNER, harness_runner)
    review_runner = (
        workspace
        / "harness/materials-benchmark-review/scripts/run_review.py"
    )
    review_runner.parent.mkdir(parents=True, exist_ok=True)
    review_runner.write_text(
        textwrap.dedent(
            """\
            import argparse
            import hashlib
            import json
            import sys
            from pathlib import Path

            sys.path.insert(0, str(Path(__file__).resolve().parent))
            from deterministic_contract import evaluate_deterministic_contract
            from artifact_schema import (
                AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
                AUDIT_BUNDLE_SCHEMA_VERSION,
                AUDIT_MANIFEST_SCHEMA_VERSION,
                AUDIT_REPORT_SCHEMA_VERSION,
                DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
                DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
                DISPOSITION_SCHEMA_VERSION,
                SCORING_SCHEMA_VERSION,
            )

            def file_hash(path):
                return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()

            def review_implementation():
                skill = Path(__file__).resolve().parent.parent
                manifest = json.loads(
                    (skill / "references/review-implementation-files.json").read_text()
                )
                files = {
                    name: file_hash(skill / name)
                    for name in manifest["files"]
                }
                payload = json.dumps(
                    files, ensure_ascii=False, sort_keys=True, separators=(",", ":")
                ).encode()
                return {
                    "schema_version": "materials-review-implementation/1.0",
                    "root": ".cursor/skills/materials-benchmark-review",
                    "files": files,
                    "aggregate_hash": "sha256:" + hashlib.sha256(payload).hexdigest(),
                }

            def core_digest(root):
                paths = []
                if (root / "instruction.md").is_file():
                    paths.append(root / "instruction.md")
                for role in ("tests", "solution"):
                    if (root / role).is_dir():
                        paths.extend(
                            path for path in sorted((root / role).rglob("*"))
                            if path.is_file()
                        )
                snapshot = {
                    "schema_version": "materials-core-contract/1.0",
                    "surface_hashes": {
                        path.relative_to(root).as_posix(): file_hash(path)
                        for path in sorted(paths)
                    },
                }
                payload = json.dumps(
                    snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":")
                ).encode()
                return "sha256:" + hashlib.sha256(payload).hexdigest()

            parser = argparse.ArgumentParser()
            parser.add_argument("root")
            parser.add_argument("--audit-output-dir", required=True)
            parser.add_argument("--output-purpose", choices=["reaudit"], required=True)
            parser.add_argument("--agent-assessment")
            args = parser.parse_args()
            root = Path(args.root)
            audit = Path(args.audit_output_dir) / "benchmark_audit"
            if audit.exists():
                import shutil
                shutil.rmtree(audit)
            audit.mkdir(parents=True, exist_ok=True)
            instruction_text = (root / "instruction.md").read_text()
            residual_target = "STILL_LISTS_TARGET" in instruction_text
            malformed_probe_payload = (
                "MALFORMED_PROBE_PAYLOAD" in instruction_text
            )
            findings = (
                [{"finding_id": "reaudit-residual", "status": "OPEN",
                  "title": "SOLUTION_ORACLE_MISSING", "severity": "LOW"}]
                if residual_target else []
            )
            deterministic_contract = evaluate_deterministic_contract(
                normalized_instruction_contract={},
                grading_contract={},
                checker_analysis={
                    "d6_core_output_scoring": {"status": "PROVEN"}
                },
                package_roles={
                    "instruction.md": "ok",
                    "tests/grading_spec.json": "ok",
                    "tests/checker.py": "ok",
                    "tests/test.sh": "ok",
                    "oracle_entrypoint": "ok",
                },
                findings=[],
            )
            probe_results = {
                "schema_version": DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
                "probe_origin": "SCHEMA_DERIVED_DETERMINISTIC",
                "cases": [],
                "status": "ASSESSED",
            }
            deterministic_core = {
                "schema_version": DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
                "contract": deterministic_contract,
                "probe_results": probe_results,
            }
            agent_quality = {
                "schema_version": AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
                "finding_ids": [],
                "probe_cases_are_code_defined": True,
            }
            report = {
                "schema_version": AUDIT_REPORT_SCHEMA_VERSION,
                "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
                "audit_id": "audit-reaudit-001",
                "configuration": {"review_lane": "dual"},
                "findings": findings,
                "deterministic_core": deterministic_core,
                "agent_quality": agent_quality,
                # v11 layout: ``disposition`` holds the VERDICT; the publish
                # route lives in ``publication_route`` / ``publishability`` and
                # disposition.json ``route``.
                "summary": {
                    "final_verdict": "PASS",
                    "disposition": "PASS",
                    "publication_route": "PUBLISH_CANDIDATE",
                    "publishability": "PUBLISH_CANDIDATE",
                    "scoring_version": SCORING_SCHEMA_VERSION,
                    "total_score": 90,
                    "hard_gate_triggered": False,
                },
                "publishability": "PUBLISH_CANDIDATE",
                "evidence_contract": {
                    "fail_closed": True,
                    "gaps": [],
                },
                "hard_gates": [
                    {
                        "code": code,
                        "status": "PASS",
                        "evidence": [{"fact": "source-bound audit evidence"}],
                    }
                    for code in (
                        "NON_MATERIALS_TASK",
                        "SCIENTIFIC_TARGET_INVALID",
                        "CHECKER_CORE_TASK_UNASSESSED",
                        "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
                    )
                ],
                "deterministic_contract": deterministic_contract,
            }
            report_path = audit / "audit_report.json"
            report_path.write_text(json.dumps(report))
            disposition_path = audit / "disposition.json"
            disposition_path.write_text(json.dumps({
                "schema_version": DISPOSITION_SCHEMA_VERSION,
                "audit_id": report["audit_id"],
                "route": "PUBLISH_CANDIDATE",
                "verdict": "PASS",
            }))
            artifact_paths = {
                "deterministic_core/report.json": audit
                / "deterministic_core/report.json",
                "deterministic_core/probe_results.json": audit
                / "deterministic_core/probe_results.json",
                "agent_quality/assessment.json": audit
                / "agent_quality/assessment.json",
            }
            artifact_paths["deterministic_core/report.json"].parent.mkdir(
                parents=True, exist_ok=True
            )
            artifact_paths["deterministic_core/report.json"].write_text(
                json.dumps(deterministic_core)
            )
            artifact_paths["deterministic_core/probe_results.json"].write_text(
                json.dumps(probe_results)
            )
            artifact_paths["agent_quality/assessment.json"].parent.mkdir(
                parents=True, exist_ok=True
            )
            artifact_paths["agent_quality/assessment.json"].write_text(
                json.dumps(agent_quality)
            )
            if malformed_probe_payload:
                relative = (
                    "deterministic_core/probe_cases/checker_tests/"
                    "malformed_outputs/app/outputs/metrics.json"
                )
                artifact_paths[relative] = audit / relative
                artifact_paths[relative].parent.mkdir(
                    parents=True, exist_ok=True
                )
                artifact_paths[relative].write_bytes(b'{"metrics": [}')
            for relative in (
                "corpus_index_entry.json",
                "checker_tests.json",
                "resource_checks.json",
            ):
                (audit / relative).write_text("{}")
            hashes = {}
            for relative in (
                "instruction.md",
                "tests/checker.py",
                "tests/grading_spec.json",
                "solution/solve.sh",
                "paper/paper.md",
            ):
                path = root / relative
                if path.is_file():
                    hashes[relative] = "sha256:" + hashlib.sha256(
                        path.read_bytes()
                    ).hexdigest()
            (audit / "audit_manifest.json").write_text(json.dumps({
                "schema_version": AUDIT_MANIFEST_SCHEMA_VERSION,
                "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
                "audit_id": report["audit_id"],
                "benchmark_root": str(root),
                "input_hashes": hashes,
                "review_implementation": review_implementation(),
                "core_contract_digest": core_digest(root),
                "assessment_hashes": (
                    {"agent_assessment": file_hash(Path(args.agent_assessment))}
                    if args.agent_assessment else {}
                ),
                "output_hashes": {
                    "audit_report.json": file_hash(report_path),
                    "disposition.json": file_hash(disposition_path),
                    **{
                        relative: file_hash(path)
                        for relative, path in artifact_paths.items()
                    },
                    **{
                        relative: file_hash(audit / relative)
                        for relative in (
                            "corpus_index_entry.json",
                            "checker_tests.json",
                            "resource_checks.json",
                        )
                    },
                },
            }))
            print(json.dumps(report))
            """
        ),
        encoding="utf-8",
    )
    return harness_runner


def initial_repair_context(
    workspace: Path,
    *,
    review_lane: str = "dual",
    residual_target: bool = False,
    malformed_probe_payload: bool = False,
) -> tuple[Path, dict[str, Any], str, Path]:
    runner = install_repair_harness(workspace)
    package = workspace / "paper-fixture"
    (package / "tests").mkdir(parents=True)
    (package / "solution").mkdir()
    (package / "paper").mkdir()
    (package / "solution/producer.py").write_text(
        "print('fixture producer')\n", encoding="utf-8"
    )
    instruction = "Compute the evidence-backed quantity.\n"
    if residual_target:
        instruction += "STILL_LISTS_TARGET\n"
    if malformed_probe_payload:
        instruction += "MALFORMED_PROBE_PAYLOAD\n"
    (package / "instruction.md").write_text(instruction, encoding="utf-8")
    (package / "tests/checker.py").write_text(
        "raise SystemExit(0)\n", encoding="utf-8"
    )
    (package / "tests/test.sh").write_text(
        "#!/bin/sh\nexit 0\n", encoding="utf-8"
    )
    (package / "tests/test.sh").chmod(0o755)
    write_json(package / "tests/grading_spec.json", {"pass_threshold": 0.8})
    (package / "paper/paper.md").write_text(
        "The published method computes the evidence-backed quantity.\n"
        "The exact public replacement is paper-supported quantity.\n",
        encoding="utf-8",
    )
    write_json(package / "manifest.json", {"id": "paper-fixture"})
    contract = deterministic_contract.evaluate_deterministic_contract(
        normalized_instruction_contract={},
        grading_contract={},
        checker_analysis={"d6_core_output_scoring": {"status": "PROVEN"}},
        package_roles={
            "instruction.md": "ok",
            "tests/grading_spec.json": "ok",
            "tests/checker.py": "ok",
            "tests/test.sh": "ok",
            "oracle_entrypoint": "ok",
        },
        findings=[
            {
                "finding_id": FINDING_ID,
                "title": "SOLUTION_ORACLE_MISSING",
                "status": "OPEN",
                "repairable": True,
                "affected_files": ["solution/solve.sh"],
                "evidence": {},
            }
        ],
    )
    probe_results = {
        "schema_version": DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
        "probe_origin": "SCHEMA_DERIVED_DETERMINISTIC",
        "cases": [],
        "status": "ASSESSED",
    }
    deterministic_core = {
        "schema_version": DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
        "contract": contract,
        "probe_results": probe_results,
    }
    agent_quality = {
        "schema_version": AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
        "finding_ids": [],
        "probe_cases_are_code_defined": True,
    }
    report = {
        "schema_version": AUDIT_REPORT_SCHEMA_VERSION,
        "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
        "audit_id": AUDIT_ID,
        "configuration": {"review_lane": review_lane},
        "findings": [
            {
                "finding_id": FINDING_ID,
                "status": "OPEN",
                "title": "SOLUTION_ORACLE_MISSING",
                "severity": "HIGH",
            }
        ],
        "summary": {
            "final_verdict": "CONDITIONAL",
            "disposition": "REPAIR_QUEUE",
            "total_score": 70,
            "hard_gate_triggered": False,
            "scoring_version": SCORING_SCHEMA_VERSION,
        },
        "deterministic_core": deterministic_core,
        "agent_quality": agent_quality,
        "deterministic_contract": contract,
        "evidence_contract": {"fail_closed": True, "gaps": []},
        "hard_gates": [],
    }
    write_json(external_audit_dir(package) / "audit_report.json", report)
    write_json(
        external_audit_dir(package) / "disposition.json",
        {
            "schema_version": DISPOSITION_SCHEMA_VERSION,
            "audit_id": AUDIT_ID,
            "route": "REPAIR_QUEUE",
            "verdict": "CONDITIONAL",
        },
    )
    write_json(
        external_audit_dir(package) / "deterministic_core/report.json",
        deterministic_core,
    )
    write_json(
        external_audit_dir(package) / "deterministic_core/probe_results.json",
        probe_results,
    )
    write_json(
        external_audit_dir(package) / "agent_quality/assessment.json",
        agent_quality,
    )
    for relative in (
        "corpus_index_entry.json",
        "checker_tests.json",
        "resource_checks.json",
    ):
        write_json(external_audit_dir(package) / relative, {})
    input_hashes = {
        relative: sha256_file(package / relative)
        for relative in (
            "instruction.md",
            "tests/checker.py",
            "tests/grading_spec.json",
            "paper/paper.md",
            "manifest.json",
            "tests/test.sh",
        )
    }
    module_spec = importlib.util.spec_from_file_location("harness_repair", runner)
    assert module_spec is not None and module_spec.loader is not None
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    write_json(
        external_audit_dir(package) / "audit_manifest.json",
        {
            "schema_version": AUDIT_MANIFEST_SCHEMA_VERSION,
            "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
            "audit_id": AUDIT_ID,
            "benchmark_root": str(package),
            "input_hashes": input_hashes,
            "review_implementation": module.collect_review_implementation_hashes(),
            "core_contract_digest": module.core_contract_digest(package),
            "assessment_hashes": {},
            "output_hashes": {
                "audit_report.json": sha256_file(
                    external_audit_dir(package) / "audit_report.json"
                ),
                "disposition.json": sha256_file(
                    external_audit_dir(package) / "disposition.json"
                ),
                "corpus_index_entry.json": sha256_file(
                    external_audit_dir(package) / "corpus_index_entry.json"
                ),
                "checker_tests.json": sha256_file(
                    external_audit_dir(package) / "checker_tests.json"
                ),
                "resource_checks.json": sha256_file(
                    external_audit_dir(package) / "resource_checks.json"
                ),
                "deterministic_core/report.json": sha256_file(
                    external_audit_dir(package) / "deterministic_core/report.json"
                ),
                "deterministic_core/probe_results.json": sha256_file(
                    external_audit_dir(package) / "deterministic_core/probe_results.json"
                ),
                "agent_quality/assessment.json": sha256_file(
                    external_audit_dir(package) / "agent_quality/assessment.json"
                ),
            },
        },
    )
    write_audit_attestation(package)
    return package, report, FINDING_ID, runner


def current_single_finding_plan(plan: dict[str, Any]) -> dict[str, Any]:
    finding = json.loads(
        json.dumps(
            {
                key: plan[key]
                for key in (
                    "finding_id",
                    "repair_class",
                    "justification",
                    "evidence",
                    "operations",
                    "regression_tests",
                )
            }
        )
    )
    finding.update(
        {
            "deterministic_check": "D5",
            "finding_code": "SOLUTION_ORACLE_MISSING",
            "core_science_change": False,
        }
    )
    plan["findings"] = [finding]
    plan["deterministic_contract"] = {}
    return plan


def safe_plan(audit_id: str, finding_id: str) -> dict[str, Any]:
    return current_single_finding_plan({
        "schema_version": deterministic_contract.DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION,
        "audit_id": audit_id,
        "finding_id": finding_id,
        "repair_class": "AUTO_FIX",
        "justification": "Restore the missing deterministic solution entrypoint.",
        "core_science_change": False,
        "evidence": [
            {
                "id": "audit-finding",
                "source": f"benchmark_audit:{finding_id}",
                "quote": "SOLUTION_ORACLE_MISSING",
            }
        ],
        "operations": [
            {
                "id": "restore-solve",
                "type": "write_file",
                "file": "solution/solve.sh",
                "content": "#!/bin/sh\nexec python3 solution/producer.py\n",
                "executable": True,
                "evidence_ids": ["audit-finding"],
            }
        ],
        "regression_tests": [
            {
                "id": "solve-content",
                "finding_id": finding_id,
                "causal_operation_ids": ["restore-solve"],
                "type": "text_contains",
                "file": "solution/solve.sh",
                "expected": "#!/bin/sh\nexec python3 solution/producer.py\n",
            },
            {
                "id": "solve-exists",
                "finding_id": finding_id,
                "causal_operation_ids": ["restore-solve"],
                "type": "file_exists",
                "file": "solution/solve.sh",
            },
            {
                "id": "solve-runs",
                "finding_id": finding_id,
                "causal_operation_ids": ["restore-solve"],
                "type": "command",
                "command": ["sh", "solution/solve.sh"],
                "expected_returncode": 0,
            },
        ],
    })


def write_plan(path: Path, value: dict[str, Any]) -> None:
    if (
        value.get("schema_version")
        == deterministic_contract.DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION
        and isinstance(value.get("findings"), list)
        and value["findings"]
    ):
        # Keep mutation-focused tests readable while ensuring the serialized
        # executable plan is always a complete current-schema batch.
        finding = value["findings"][0]
        for key in (
            "finding_id",
            "repair_class",
            "justification",
            "core_science_change",
            "evidence",
            "operations",
            "regression_tests",
        ):
            if key in value:
                finding[key] = json.loads(json.dumps(value[key]))
    packages = [
        candidate
        for candidate in path.parent.iterdir()
        if candidate.is_dir()
        and (external_audit_dir(candidate) / "audit_report.json").is_file()
    ]
    if (
        len(packages) == 1
        and value.get("schema_version")
        == deterministic_contract.DETERMINISTIC_REPAIR_PLAN_SCHEMA_VERSION
    ):
        bind_plan_to_package(packages[0], value)
    write_json(path, value)


def run_repair(
    package: Path, plan: Path, runner: Path
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(runner),
            str(package),
            "--plan",
            str(plan),
            "--audit-attestation",
            str(package.parent / "audit-attestation.json"),
            "--audit-dir",
            str(external_audit_dir(package)),
            "--repair-output-dir",
            str(external_repair_dir(package)),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )


class MaterialsSafeRepairTests(unittest.TestCase):
    def test_equal_depth_review_uses_real_cli_path_policy(self) -> None:
        module = repair_module()
        real_subprocess_run = subprocess.run
        with tempfile.TemporaryDirectory() as temporary_name:
            package = Path(temporary_name) / "theme/paper-42"
            package.mkdir(parents=True)
            (package / "instruction.md").write_text("materials task\n")
            (package / "tests").mkdir()
            captured: list[str] = []

            def validate_then_materialize(command, **kwargs):
                del kwargs
                captured[:] = command
                validated = real_subprocess_run(
                    [*command, "--validate-output-policy-only"],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if validated.returncode == 0:
                    output = Path(
                        command[command.index("--audit-output-dir") + 1]
                    )
                    write_json(
                        output / "benchmark_audit/audit_report.json",
                        {"configuration": {"review_lane": "dual"}},
                    )
                return validated

            with mock.patch.object(
                module.subprocess, "run", side_effect=validate_then_materialize
            ):
                result = module.run_equal_depth_review(
                    package,
                    {"configuration": {"review_lane": "dual"}},
                    {"assessment_hashes": {}},
                    {},
                )

            expected = (
                package.parent
                / "review_outputs/42/repair_reaudit"
            ).resolve()
            self.assertEqual(result["configuration"]["review_lane"], "dual")
            self.assertEqual(
                Path(captured[captured.index("--audit-output-dir") + 1]),
                expected,
            )
            self.assertEqual(
                captured[captured.index("--output-purpose") + 1],
                "reaudit",
            )
            self.assertFalse((package / "benchmark_audit").exists())

            normal_review = captured[:]
            purpose_index = normal_review.index("--output-purpose")
            del normal_review[purpose_index : purpose_index + 2]
            rejected = real_subprocess_run(
                [*normal_review, "--validate-output-policy-only"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(rejected.returncode, 2)

            runner = captured[:]
            for invalid in (
                package / "benchmark_audit",
                package.parent / "wrong/review_outputs/42/repair_reaudit",
            ):
                runner[runner.index("--audit-output-dir") + 1] = str(invalid)
                rejected = real_subprocess_run(
                    [*runner, "--validate-output-policy-only"],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(rejected.returncode, 2)
                self.assertIn("must", rejected.stderr)

    def test_repair_paths_are_canonical_theme_siblings(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary_name:
            package = Path(temporary_name) / "theme/paper-42"
            package.mkdir(parents=True)
            management = (package.parent / "review_outputs/42").resolve()
            self.assertEqual(
                module.source_audit_dir(package, {}),
                management / "benchmark_audit",
            )
            self.assertEqual(
                module.repair_output_root(package, {}),
                management / "repair",
            )
            self.assertEqual(
                module.reaudit_audit_dir(package, {}),
                management / "repair_reaudit/benchmark_audit",
            )
            with self.assertRaisesRegex(ValueError, "must equal"):
                module.source_audit_dir(
                    package,
                    {"source_audit_dir": str(package / "benchmark_audit")},
                )
            with self.assertRaisesRegex(ValueError, "must equal"):
                module.repair_output_root(
                    package,
                    {"repair_output_dir": str(package.parent / "wrong")},
                )

    def test_rebase_refreshes_manifest_after_path_bearing_writes(self) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            candidate = workspace / "candidate"
            final_root = workspace / "final"
            audit = workspace / "reaudit/benchmark_audit"
            audit.mkdir(parents=True)
            old_report = {
                "audit_id": "audit-rebase-regression",
                "benchmark_root": str(candidate),
                "nested_path": str(candidate / "solution"),
            }
            write_json(audit / "audit_report.json", old_report)
            write_json(
                audit / "disposition.json",
                {"benchmark_root": str(candidate)},
            )
            manifest = {
                "audit_id": old_report["audit_id"],
                "benchmark_root": str(candidate),
                "source_path": str(candidate / "instruction.md"),
                "output_hashes": {
                    "audit_report.json": sha256_file(
                        audit / "audit_report.json"
                    ),
                    "disposition.json": sha256_file(
                        audit / "disposition.json"
                    ),
                },
                "bundle_hash": "sha256:" + "0" * 64,
            }
            write_json(audit / "audit_manifest.json", manifest)

            module.rebase_audit_paths(
                candidate,
                final_root,
                {},
                audit_output_dir=audit.parent,
            )

            rebased_report = json.loads(
                (audit / "audit_report.json").read_text(encoding="utf-8")
            )
            rebased_manifest = json.loads(
                (audit / "audit_manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(rebased_report["benchmark_root"], str(final_root))
            self.assertEqual(
                rebased_report["nested_path"],
                str(final_root / "solution"),
            )
            self.assertEqual(
                rebased_manifest["source_path"],
                str(final_root / "instruction.md"),
            )
            self.assertEqual(
                rebased_manifest["bundle_hash"],
                module.canonical_json_hash(
                    rebased_manifest["output_hashes"]
                ),
            )
            for relative, expected in rebased_manifest[
                "output_hashes"
            ].items():
                self.assertEqual(sha256_file(audit / relative), expected)
            self.assertNotIn(
                "audit_manifest.json",
                rebased_manifest["output_hashes"],
            )

    def test_missing_solution_entrypoint_is_repaired_and_atomically_published(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            plan = workspace / "repair-plan.json"
            write_plan(plan, safe_plan(report["audit_id"], finding_id))
            manifest_before = sha256_file(package / "manifest.json")
            paper_before = sha256_file(package / "paper/paper.md")

            completed = run_repair(package, plan, runner)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            result = json.loads(completed.stdout)
            repair_manifest = json.loads(
                ((external_repair_dir(package) / "benchmark_repair") / "repair_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(repair_manifest["status"], "REPAIRED")
            self.assertEqual(repair_manifest["repair_state"], "REPAIRED")
            self.assertEqual(repair_manifest["disposition"], "PASS")
            self.assertTrue(repair_manifest["publishable"])
            self.assertTrue(result["package_mutated"])
            self.assertEqual(repair_manifest["finding_ids"], [finding_id])
            self.assertEqual(
                [item["before_passed"] for item in repair_manifest["regression_tests"]],
                [False, False, False],
            )
            self.assertTrue(
                all(
                    item["after_passed"]
                    for item in repair_manifest["regression_tests"]
                )
            )
            self.assertEqual(
                repair_manifest["reaudit"]["review_lane"], "dual"
            )
            self.assertTrue((package / "solution/solve.sh").is_file())
            self.assertEqual(sha256_file(package / "manifest.json"), manifest_before)
            self.assertEqual(sha256_file(package / "paper/paper.md"), paper_before)
            self.assertEqual(package.name, "paper-fixture")
            history = Path(result["history_dir"])
            self.assertTrue((history / "snapshot").is_dir())
            self.assertTrue((history / "original").is_dir())
            self.assertTrue((history / "repair_plan.json").is_file())
            self.assertTrue((history / "attempt_manifest.json").is_file())
            canonical_audit = external_reaudit_dir(package)
            retained_audit = history / "repair_reaudit/benchmark_audit"
            self.assertTrue(canonical_audit.is_dir())
            self.assertTrue(retained_audit.is_dir())
            for audit in (canonical_audit, retained_audit):
                audit_manifest = json.loads(
                    (audit / "audit_manifest.json").read_text(
                        encoding="utf-8"
                    )
                )
                self.assertEqual(
                    audit_manifest["bundle_hash"],
                    repair_module().canonical_json_hash(
                        audit_manifest["output_hashes"]
                    ),
                )
                for relative, expected in audit_manifest[
                    "output_hashes"
                ].items():
                    self.assertEqual(
                        sha256_file(audit / relative),
                        expected,
                    )
            self.assertEqual(
                repair_module().sha256_path(canonical_audit),
                repair_module().sha256_path(retained_audit),
            )
            reaudit_refs = repair_manifest["reaudit_bundle"]
            self.assertEqual(
                reaudit_refs["report_hash"],
                sha256_file(retained_audit / "audit_report.json"),
            )
            self.assertEqual(
                reaudit_refs["manifest_hash"],
                sha256_file(retained_audit / "audit_manifest.json"),
            )
            self.assertEqual(
                reaudit_refs["bundle_hash"],
                repair_module().sha256_path(retained_audit),
            )
            attempt = json.loads(
                (history / "attempt_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertTrue(attempt["package_mutated"])
            self.assertEqual(attempt["repair_status"], "REPAIRED")
            self.assertEqual(attempt["review_verdict"], "PASS")
            self.assertEqual(
                attempt["publishability"], "PUBLISH_CANDIDATE"
            )
            repair_module().validate_fixed_bundle(
                external_repair_dir(package) / "benchmark_repair"
            )
            repair_module().validate_fixed_bundle(history)

    def test_legacy_reaudit_still_listing_target_blocks_publish(self) -> None:
        # Item 4 regression: the legacy single-finding path must read the
        # publish route from disposition.json route / publication_route (NOT
        # summary.disposition, which is the verdict in v11) AND must refuse to
        # publish when the target finding is still listed in the re-audit.
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace,
                residual_target=True,
                malformed_probe_payload=True,
            )
            plan = workspace / "repair-plan.json"
            write_plan(plan, safe_plan(report["audit_id"], finding_id))

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "PARTIALLY_REPAIRED")
            self.assertFalse(result["publishable"])
            self.assertFalse(result["package_mutated"])
            self.assertIn("re-audit did not reach PASS", result["reason"])
            # Authoritative package preserved unchanged, no publish.
            self.assertFalse((package / "solution/solve.sh").is_file())
            self.assertFalse((package / "benchmark_repair").exists())
            self.assertEqual(package.name, "paper-fixture")
            history = Path(result["history_dir"])
            archived = history / "repair_reaudit/benchmark_audit"
            canonical = external_reaudit_dir(package)
            self.assertTrue(archived.is_dir())
            self.assertTrue(canonical.is_dir())
            attempt = json.loads(
                (history / "attempt_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertFalse(attempt["package_mutated"])
            references = attempt["reaudit_bundle"]
            self.assertEqual(references["audit_dir"], str(archived))
            manifest = json.loads(
                (archived / "audit_manifest.json").read_text(encoding="utf-8")
            )
            opaque_relative = (
                "deterministic_core/probe_cases/checker_tests/"
                "malformed_outputs/app/outputs/metrics.json"
            )
            self.assertEqual(
                (archived / opaque_relative).read_bytes(),
                b'{"metrics": [}',
            )
            self.assertEqual(
                manifest["output_hashes"][opaque_relative],
                sha256_file(archived / opaque_relative),
            )
            for relative, expected in manifest["output_hashes"].items():
                self.assertEqual(
                    sha256_file(archived / relative),
                    expected,
                )
            self.assertEqual(references["audit_id"], manifest["audit_id"])
            self.assertEqual(
                references["bundle_hash"], repair_module().sha256_path(archived)
            )
            self.assertIn(
                "oracle",
                (history / "evidence.json").read_text(encoding="utf-8").lower(),
            )
            repair_module().validate_fixed_bundle(history)

    def test_repair_rejects_targets_outside_instruction_tests_and_solution(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            value = safe_plan(report["audit_id"], finding_id)
            value["operations"][0]["file"] = "paper/paper.md"
            plan = workspace / "repair-plan.json"
            write_plan(plan, value)
            before = sha256_file(package / "paper/paper.md")

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("unsupported repair target", completed.stderr)
            self.assertEqual(sha256_file(package / "paper/paper.md"), before)

    def test_stale_audit_is_rejected_before_repair_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            plan = workspace / "repair-plan.json"
            write_plan(plan, safe_plan(report["audit_id"], finding_id))
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8") + "changed\n",
                encoding="utf-8",
            )

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn("stale audit", completed.stderr)
            self.assertFalse((package / "benchmark_repair").exists())

    def test_repair_reaudit_rejects_non_dual_source_audit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, report, finding_id, runner = initial_repair_context(
                workspace
            )
            report["configuration"]["review_lane"] = "experimental"
            write_json(external_audit_dir(package) / "audit_report.json", report)
            manifest_path = external_audit_dir(package) / "audit_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["output_hashes"]["audit_report.json"] = sha256_file(
                external_audit_dir(package) / "audit_report.json"
            )
            write_json(manifest_path, manifest)
            plan = workspace / "repair-plan.json"
            write_plan(plan, safe_plan(report["audit_id"], finding_id))

            completed = run_repair(package, plan, runner)

            self.assertEqual(completed.returncode, 2)
            self.assertIn(
                "source-audit attestation does not bind the authoritative bytes",
                completed.stderr,
            )
            self.assertFalse((package / "benchmark_repair").exists())


if __name__ == "__main__":
    unittest.main()
