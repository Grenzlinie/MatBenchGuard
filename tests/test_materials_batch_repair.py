"""Batch repair (§8.4) tests: multi-finding apply, partial-fix, publish-only-on-
PASS, per-audit attempt limit, per-op BLOCKED_EVIDENCE that does not block
siblings, and the five-state -> unified terminal field mapping."""

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
from pathlib import Path
from typing import Any
from unittest.mock import patch


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
    return package.parent / ".review_records/fixture/theme" / package.name / "runs/repair-test/repair"


def external_reaudit_dir(package: Path) -> Path:
    paper_id = package.name.removeprefix("paper-")
    return package.parent / ".review_records/fixture/theme" / package.name / "runs/repair-test/reaudit/benchmark_audit"


REPAIR_RUNNER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
    / "run_repair.py"
)
REVIEW_SKILL_ROOT = REPO_ROOT / ".cursor" / "skills" / "materials-benchmark-review"
sys.path.insert(0, str(REVIEW_SKILL_ROOT / "scripts"))
from artifact_schema import (  # noqa: E402
    AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
    AGENT_REPAIR_ASSESSMENT_SCHEMA_VERSION,
    AUDIT_ATTESTATION_SCHEMA_VERSION,
    AUDIT_BUNDLE_SCHEMA_VERSION,
    AUDIT_MANIFEST_SCHEMA_VERSION,
    AUDIT_REPORT_SCHEMA_VERSION,
    DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
    DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
    DISPOSITION_SCHEMA_VERSION,
    REPAIR_PLAN_SCHEMA_VERSION,
    SCORING_SCHEMA_VERSION,
)
import deterministic_contract  # noqa: E402
import agent_contract_wiring  # noqa: E402
import run_context  # noqa: E402
from prepare_audit_output import (  # noqa: E402
    prepare_workspace,
    write_agent_contract_request,
)
from tests.test_materials_safe_repair import (  # noqa: E402
    build_agent_repair_assessment_for_plan,
    fixture_paper_assessment,
    materialize_run_assessment,
)
AUDIT_ID = "audit-batch-001"
FINDING_A = "finding-missing-solve"
FINDING_B = "finding-missing-helper"


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def repair_module() -> Any:
    spec = importlib.util.spec_from_file_location(
        "materials_batch_repair_runner", REPAIR_RUNNER
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


REVIEW_STUB = """\
import argparse
import hashlib
import json
import shutil
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
    files = {name: file_hash(skill / name) for name in manifest["files"]}
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
                p for p in sorted((root / role).rglob("*")) if p.is_file()
            )
    snapshot = {
        "schema_version": "materials-core-contract/1.0",
        "surface_hashes": {
            p.relative_to(root).as_posix(): file_hash(p) for p in sorted(paths)
        },
    }
    payload = json.dumps(
        snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode()
    return "sha256:" + hashlib.sha256(payload).hexdigest()

def dims(all_full):
    out = {}
    for key in ("C01", "C02", "C03", "C04", "C05", "C06", "C07"):
        out[key] = {"normalized": 100.0 if all_full else 100.0}
    return out

parser = argparse.ArgumentParser()
parser.add_argument("root")
parser.add_argument("--audit-output-dir", required=True)
parser.add_argument("--output-purpose", choices=["reaudit"], required=True)
parser.add_argument("--agent-assessment")
args = parser.parse_args()
root = Path(args.root)
instruction_text = (root / "instruction.md").read_text()
broken = "STILL_BROKEN" in instruction_text
residual_target = "STILL_LISTS_TARGET" in instruction_text
low_score = "LOW_SCORE" in instruction_text
agent_quality_residual = "AGENT_HIGH" in instruction_text
malformed_probe_payload = "MALFORMED_PROBE_PAYLOAD" in instruction_text
audit = Path(args.audit_output_dir) / "benchmark_audit"
if audit.exists():
    shutil.rmtree(audit)
audit.mkdir(parents=True, exist_ok=True)
if broken:
    verdict, route = "CONDITIONAL", "REPAIR_QUEUE"
    findings = [{"finding_id": "reaudit-open", "status": "OPEN",
                 "title": "STILL_BROKEN", "severity": "HIGH"}]
    dimensions = {k: {"normalized": 60.0} for k in
                  ("C01","C02","C03","C04","C05","C06","C07")}
elif residual_target:
    # Re-audit routes PASS/PUBLISH_CANDIDATE yet still lists a targeted
    # finding code as a residual low-severity finding.
    verdict, route = "PASS", "PUBLISH_CANDIDATE"
    findings = [{"finding_id": "reaudit-residual", "status": "OPEN",
                 "title": "SOLUTION_ORACLE_MISSING", "severity": "LOW"}]
    dimensions = {k: {"normalized": 100.0} for k in
                  ("C01","C02","C03","C04","C05","C06","C07")}
else:
    verdict, route = "PASS", "PUBLISH_CANDIDATE"
    findings = []
    dimensions = {k: {"normalized": 100.0} for k in
                  ("C01","C02","C03","C04","C05","C06","C07")}
if agent_quality_residual:
    findings.append({
        "finding_id": "agent-quality-high",
        "status": "OPEN",
        "title": "PAPER_METHOD_CONFLICT",
        "severity": "HIGH",
        "lane": "agent_quality",
        "blocking": False,
    })
deterministic_contract = evaluate_deterministic_contract(
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
    "audit_id": "audit-reaudit-batch",
    "configuration": {"review_lane": "dual"},
    "findings": findings,
    "deterministic_core": deterministic_core,
    "agent_quality": agent_quality,
    # v11 layout: ``disposition`` holds the VERDICT; the publish route lives in
    # ``publication_route``/``publishability`` and disposition.json ``route``.
    "summary": {"final_verdict": verdict, "disposition": verdict,
                "publication_route": route, "publishability": route,
                "dimensions_v11": dimensions,
                "scoring_version": SCORING_SCHEMA_VERSION,
                "total_score": 50 if low_score else 90 if verdict == "PASS" else 70,
                "hard_gate_triggered": False},
    "publishability": route,
    "evidence_contract": {"fail_closed": True, "gaps": []},
    "hard_gates": [
        {"code": code, "status": "PASS",
         "evidence": [{"fact": "source-bound audit evidence"}]}
        for code in (
            "NON_MATERIALS_TASK",
            "SCIENTIFIC_TARGET_INVALID",
            "CHECKER_CORE_TASK_UNASSESSED",
            "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
        )
    ],
    "deterministic_contract": deterministic_contract,
}
if malformed_probe_payload:
    report["workspace_path"] = str(root)
report_path = audit / "audit_report.json"
report_path.write_text(json.dumps(report))
disposition_path = audit / "disposition.json"
disposition_path.write_text(json.dumps({
    "schema_version": DISPOSITION_SCHEMA_VERSION,
    "audit_id": report["audit_id"],
    "route": route,
    "verdict": verdict,
}))
artifact_paths = {
    "deterministic_core/report.json": audit / "deterministic_core/report.json",
    "deterministic_core/probe_results.json": audit / "deterministic_core/probe_results.json",
    "agent_quality/assessment.json": audit / "agent_quality/assessment.json",
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
    artifact_paths[relative].parent.mkdir(parents=True, exist_ok=True)
    artifact_paths[relative].write_bytes(b'{"metrics": [}')
    artifact_paths["audit_report.md"] = audit / "audit_report.md"
    artifact_paths["audit_report.md"].write_text(
        f"# Re-audit\\n\\nWorkspace: {root}\\n"
    )
for relative in ("corpus_index_entry.json", "checker_tests.json", "resource_checks.json"):
    (audit / relative).write_text("{}")
hashes = {}
for relative in ("instruction.md", "tests/checker.py", "tests/grading_spec.json",
                 "solution/solve.sh", "solution/helper.sh", "paper/paper.md"):
    p = root / relative
    if p.is_file():
        hashes[relative] = file_hash(p)
(audit / "audit_manifest.json").write_text(json.dumps({
    "schema_version": AUDIT_MANIFEST_SCHEMA_VERSION,
    "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
    "audit_id": report["audit_id"],
    "benchmark_root": str(root),
    "input_hashes": hashes,
    "review_implementation": review_implementation(),
    "core_contract_digest": core_digest(root),
    "assessment_hashes": {},
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


def install_harness(workspace: Path) -> Path:
    harness_root = workspace / "harness"
    shutil.copytree(
        REVIEW_SKILL_ROOT, harness_root / "materials-benchmark-review"
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
        harness_root / "materials-benchmark-review/scripts/run_review.py"
    )
    review_runner.write_text(REVIEW_STUB, encoding="utf-8")
    return harness_runner


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
    payload = {
        "audit_id": manifest["audit_id"],
        "manifest_hash": sha256_file(audit / "audit_manifest.json"),
        "report_hash": sha256_file(audit / "audit_report.json"),
        "disposition_hash": sha256_file(audit / "disposition.json"),
        "assessment_hashes": manifest.get("assessment_hashes", {}),
        "artifact_hashes": {
            relative: sha256_file(path)
            for relative, path in artifact_paths.items()
        },
        "output_hashes": manifest.get("output_hashes", {}),
        "artifact_schema_versions": {
            "audit_manifest": manifest.get("schema_version"),
            "audit_bundle": manifest.get("bundle_schema_version"),
            "audit_report": report.get("schema_version"),
            "deterministic_core": report["deterministic_core"][
                "schema_version"
            ],
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


def batch_context(
    workspace: Path,
    *,
    marker: bool = False,
    residual_target: bool = False,
    low_score: bool = False,
    precreate_solve: bool = False,
    agent_quality_residual: bool = False,
    malformed_probe_payload: bool = False,
) -> tuple[Path, Path]:
    runner = install_harness(workspace)
    spec = importlib.util.spec_from_file_location("harness_batch_ctx", runner)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    package = workspace / "batch-fixture"
    (package / "tests").mkdir(parents=True)
    (package / "solution").mkdir()
    (package / "paper").mkdir()
    (package / "solution/producer.py").write_text(
        "print('fixture producer')\n", encoding="utf-8"
    )
    if precreate_solve:
        # Pre-seed the operation target with the exact content the plan writes
        # so the "before" regression already passes and run_regressions raises
        # BEFORE regression_results is assigned (exercises the sentinel branch).
        (package / "solution/solve.sh").write_text(
            "#!/bin/sh\nexec python3 solution/producer.py\n", encoding="utf-8"
        )
    instruction = (
        "Compute the evidence-backed quantity.\n"
        "The package declares solution/producer.py as the existing "
        "implementation and restores solution/helper.sh with replacement "
        "#!/bin/sh\nexit 0\n"
    )
    if marker:
        instruction += "STILL_BROKEN\n"
    if residual_target:
        instruction += "STILL_LISTS_TARGET\n"
    if low_score:
        instruction += "LOW_SCORE\n"
    if agent_quality_residual:
        instruction += "AGENT_HIGH\n"
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
        "The published method computes the evidence-backed quantity.\n",
        encoding="utf-8",
    )
    write_json(package / "manifest.json", {"id": "batch-fixture"})
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
        "contract": contract,
        "probe_results": probe_results,
    }
    agent_quality = {
        "schema_version": AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
        "finding_ids": [],
        "probe_cases_are_code_defined": True,
        "assessment": fixture_paper_assessment(),
    }
    report = {
        "schema_version": AUDIT_REPORT_SCHEMA_VERSION,
        "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
        "audit_id": AUDIT_ID,
        "configuration": {"review_lane": "dual"},
        "findings": [
            {
                "finding_id": FINDING_A,
                "status": "OPEN",
                "title": "SOLUTION_ENTRYPOINT_MISSING",
                "severity": "HIGH",
            },
            {
                "finding_id": FINDING_B,
                "status": "OPEN",
                "title": "SOLUTION_HELPER_MISSING",
                "severity": "HIGH",
            },
        ],
        "deterministic_core": deterministic_core,
        "agent_quality": agent_quality,
        "deterministic_contract": contract,
        "materials_qualification": fixture_paper_assessment()[
            "materials_qualification"
        ],
        "evidence_contract": {"fail_closed": True, "gaps": []},
        "hard_gates": [],
        "summary": {
            "final_verdict": "CONDITIONAL",
            "disposition": "REPAIR_QUEUE",
            "total_score": 70,
            "hard_gate_triggered": False,
            "scoring_version": SCORING_SCHEMA_VERSION,
            "dimensions_v11": {
                "C01": {"normalized": 100.0},
                "C02": {"normalized": 40.0},
                "C03": {"normalized": 100.0},
                "C04": {"normalized": 60.0},
                "C05": {"normalized": 100.0},
                "C06": {"normalized": 100.0},
                "C07": {"normalized": 100.0},
            },
        },
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
    return package, runner


def finding_entry(
    finding_id: str,
    op_id: str,
    file: str,
    quote: str,
    *,
    repair_class: str = "AUTO_FIX",
    bad_evidence: bool = False,
) -> dict[str, Any]:
    is_entrypoint = Path(file).as_posix() == "solution/solve.sh"
    finding_code = (
        "SOLUTION_ORACLE_MISSING"
        if is_entrypoint
        else "SOLUTION_ROLE_MISSING"
    )
    if repair_class == "AUTO_FIX" and not is_entrypoint:
        repair_class = "ASSISTED_FIX"
    content = (
        "#!/bin/sh\nexec python3 solution/producer.py\n"
        if is_entrypoint
        else "#!/bin/sh\nexit 0\n"
    )
    source = (
        "not-a-real-source.md"
        if bad_evidence
        else f"benchmark_audit:{finding_id}"
        if is_entrypoint
        else "instruction.md"
    )
    evidence_item: dict[str, Any] = {
        "id": f"ev-{op_id}",
        "source": source,
        "quote": quote if is_entrypoint else "Compute the evidence-backed quantity.",
    }
    if not is_entrypoint and not bad_evidence:
        evidence_item["quote"] = (
            "The package declares solution/producer.py as the existing "
            "implementation and restores solution/helper.sh with replacement "
            "#!/bin/sh\nexit 0\n"
        )
        evidence_item.update(
            {
                "exact_quote": evidence_item["quote"],
                "source_kind": "PACKAGE_DIRECT_SOURCE",
                "kind": "harbor_path",
                "precision": {
                    "kind": "harbor_path",
                    "official_contract": (
                        "solution/producer.py"
                    ),
                    "existing_path_code": "solution/producer.py",
                    "replacement": content,
                },
                "applicability": "The fixture instruction defines the repair target.",
                "derivation": "The operation restores the declared helper role.",
                "core_science_change": False,
            }
        )
    return {
        "finding_id": finding_id,
        "deterministic_check": "D5",
        "finding_code": finding_code,
        "repair_class": repair_class,
        "justification": f"Restore {file}.",
        "core_science_change": False,
        "evidence": [evidence_item],
        "operations": [
            {
                "id": op_id,
                "type": "write_file",
                "file": file,
                "content": content,
                "executable": True,
                "evidence_ids": [f"ev-{op_id}"],
            }
        ],
        "regression_tests": [
            {
                "id": f"rt-{op_id}",
                "finding_id": finding_id,
                "causal_operation_ids": [op_id],
                "type": "text_contains",
                "file": file,
                "expected": content,
            }
        ],
    }


def bind_batch_plan(package: Path, plan: dict[str, Any]) -> None:
    module = repair_module()
    audit = external_audit_dir(package)
    manifest = json.loads(
        (audit / "audit_manifest.json").read_text(encoding="utf-8")
    )
    report = json.loads((audit / "audit_report.json").read_text(encoding="utf-8"))
    source_findings = [
        {
            "finding_id": finding["finding_id"],
            "title": finding.get("finding_code", "SOLUTION_ORACLE_MISSING"),
            "status": "OPEN",
            "repairable": True,
            "affected_files": sorted(
                {
                    operation.get("file")
                    for operation in finding.get("operations", [])
                    if isinstance(operation, dict)
                    and isinstance(operation.get("file"), str)
                }
            ),
            "evidence": {
                "quote": next(
                    (
                        item.get("quote")
                        for item in finding.get("evidence", [])
                        if isinstance(item, dict)
                        and isinstance(item.get("quote"), str)
                    ),
                    "",
                )
            },
        }
        for finding in plan["findings"]
    ]
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
        findings=source_findings,
    )
    report["findings"] = source_findings
    report["deterministic_contract"] = contract
    report["deterministic_core"]["contract"] = contract
    write_json(audit / "audit_report.json", report)
    write_json(audit / "deterministic_core/report.json", report["deterministic_core"])
    module.refresh_audit_manifest_hashes(audit)
    manifest = json.loads((audit / "audit_manifest.json").read_text(encoding="utf-8"))
    report_hash = sha256_file(audit / "audit_report.json")
    digest = module.core_contract_digest(package)
    plan["core_contract_digest"] = digest
    binding = {
        "schema_version": contract["schema_version"],
        "registry_version": contract["registry_version"],
        "contract_digest": contract["contract_digest"],
        "audit_id": plan["audit_id"],
        "required_finding_ids": contract["repair_summary"][
            "required_finding_ids"
        ],
    }
    plan["deterministic_contract"] = binding
    plan["source_audit"] = {
        "audit_id": plan["audit_id"],
        "input_hashes": manifest["input_hashes"],
        "review_implementation": manifest.get("review_implementation", {}),
        "review_lane": "dual",
        "core_contract_digest": digest,
        "assessment_hashes": {},
        "deterministic_contract": binding,
    }
    for finding in plan["findings"]:
        finding.setdefault("lane", "deterministic_core")
        finding.setdefault(
            "repair_scope",
            "DETERMINISTIC_WIRING"
            if finding.get("repair_class") == "AUTO_FIX"
            else "INSTRUCTION_CONTRACT",
        )
        for operation in finding.get("operations", []):
            if isinstance(operation, dict):
                operation.setdefault("publication_class", "REAUDIT_REQUIRED")
        for item in finding.get("evidence", []):
            source = item.get("source", "")
            if source.startswith("benchmark_audit:"):
                item["source_hash"] = report_hash
            else:
                local = package / source
                if local.is_file():
                    item["source_hash"] = sha256_file(local)
    plan["schema_version"] = REPAIR_PLAN_SCHEMA_VERSION
    assessment_path = package.parent / "agent_repair_assessment.json"
    assessment = build_agent_repair_assessment_for_plan(package, plan)
    write_json(assessment_path, assessment)
    plan["agent_repair_assessment"] = {
        "schema_version": AGENT_REPAIR_ASSESSMENT_SCHEMA_VERSION,
        "path": str(assessment_path),
        "assessment_hash": sha256_file(assessment_path),
    }
    write_audit_attestation(package)


def batch_plan(findings: list[dict[str, Any]]) -> dict[str, Any]:
    for finding in findings:
        finding.setdefault("lane", "deterministic_core")
        for operation in finding.get("operations", []):
            if isinstance(operation, dict):
                operation.setdefault("publication_class", "REAUDIT_REQUIRED")
    return {
        "schema_version": REPAIR_PLAN_SCHEMA_VERSION,
        "audit_id": AUDIT_ID,
        "core_science_change": False,
        "findings": sorted(findings, key=lambda item: item["finding_id"]),
        "deterministic_contract": {},
    }


def write_resumed_reaudit(
    module: Any,
    candidate: Path,
    output: Path,
    machine: dict[str, Any],
    assessment: dict[str, Any],
    *,
    not_proven: bool = False,
) -> dict[str, Any]:
    """Write an authenticated Review-shaped final bundle for the resume seam."""
    audit = output / "benchmark_audit"
    audit.mkdir(parents=True, exist_ok=True)
    effective = agent_contract_wiring.derive_effective_contract(
        machine, assessment
    )
    probe_results = {
        "schema_version": DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
        "probe_origin": "SCHEMA_DERIVED_DETERMINISTIC",
        "cases": [],
        "status": "ASSESSED",
    }
    deterministic_core = {
        "schema_version": DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
        "contract": machine,
        "effective_contract": effective,
        "agent_contract_assessment": assessment,
        "probe_results": probe_results,
    }
    agent_quality = {
        "schema_version": AGENT_QUALITY_ARTIFACT_SCHEMA_VERSION,
        "finding_ids": [],
        "probe_cases_are_code_defined": True,
    }
    route = "EVIDENCE_PENDING" if not_proven else "PUBLISH_CANDIDATE"
    verdict = "CONDITIONAL" if not_proven else "PASS"
    dimensions = {
        key: {"normalized": 100.0}
        for key in ("C01", "C02", "C03", "C04", "C05", "C06", "C07")
    }
    report = {
        "schema_version": AUDIT_REPORT_SCHEMA_VERSION,
        "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
        "audit_id": "audit-resumed-contract",
        "configuration": {"review_lane": "dual"},
        "findings": [],
        "deterministic_core": deterministic_core,
        "agent_quality": agent_quality,
        "deterministic_contract": machine,
        "effective_deterministic_contract": effective,
        "agent_contract_assessment": assessment,
        "summary": {
            "final_verdict": verdict,
            "publication_route": route,
            "publishability": route,
            "total_score": 90,
            "hard_gate_triggered": False,
            "scoring_version": SCORING_SCHEMA_VERSION,
            "dimensions_v11": dimensions,
        },
        "publishability": route,
        "evidence_contract": {"fail_closed": True, "gaps": []},
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
    }
    write_json(audit / "audit_report.json", report)
    write_json(
        audit / "disposition.json",
        {
            "schema_version": DISPOSITION_SCHEMA_VERSION,
            "audit_id": report["audit_id"],
            "route": route,
            "verdict": verdict,
        },
    )
    write_json(audit / "deterministic_core/report.json", deterministic_core)
    write_json(audit / "deterministic_core/probe_results.json", probe_results)
    write_json(audit / "agent_quality/assessment.json", agent_quality)
    for relative in (
        "corpus_index_entry.json",
        "checker_tests.json",
        "resource_checks.json",
    ):
        write_json(audit / relative, {})
    output_hashes = {
        relative: sha256_file(audit / relative)
        for relative in (
            "audit_report.json",
            "disposition.json",
            "deterministic_core/report.json",
            "deterministic_core/probe_results.json",
            "agent_quality/assessment.json",
            "corpus_index_entry.json",
            "checker_tests.json",
            "resource_checks.json",
        )
    }
    write_json(
        audit / "audit_manifest.json",
        {
            "schema_version": AUDIT_MANIFEST_SCHEMA_VERSION,
            "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
            "audit_id": report["audit_id"],
            "benchmark_root": str(candidate),
            "input_hashes": module.package_hashes(candidate),
            "review_implementation": module.collect_review_implementation_hashes(),
            "core_contract_digest": module.core_contract_digest(candidate),
            "assessment_hashes": {},
            "output_hashes": output_hashes,
        },
    )
    return report


def pending_review_seam(module: Any, calls: dict[str, int]):
    """Prepare the same Review request shape used by the pending path."""

    def pending_review(
        candidate: Path,
        _report: dict[str, Any],
        _manifest: dict[str, Any],
        _plan: dict[str, Any],
        *,
        original_root: Path | None = None,
        **_kwargs: Any,
    ) -> dict[str, Any]:
        del original_root
        calls["count"] += 1
        output = module.reaudit_output_root(candidate)
        context = prepare_workspace(candidate, output)
        temp_dir = Path(context["audit_temp_dir"])
        machine = deterministic_contract.evaluate_deterministic_contract(
            normalized_instruction_contract={},
            grading_contract={},
            checker_analysis={"d6_core_output_scoring": {"status": "UNKNOWN"}},
            package_roles={
                "instruction.md": "ok",
                "tests/grading_spec.json": "ok",
                "tests/checker.py": "ok",
                "tests/test.sh": "ok",
                "oracle_entrypoint": "ok",
            },
            findings=[],
        )
        write_json(
            temp_dir / "deterministic_core/report.json",
            {
                "schema_version": DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
                "lane": "deterministic_core",
                "contract": machine,
            },
        )
        write_json(
            temp_dir / "deterministic_core/probe_results.json",
            {
                "schema_version": DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
                "probe_origin": "SCHEMA_DERIVED_DETERMINISTIC",
                "cases": [],
                "status": "ASSESSED",
            },
        )
        write_json(temp_dir / "evidence/static_checks/audit_static.json", {})
        write_json(temp_dir / "checker_tests.json", {})
        write_json(temp_dir / "resource_checks.json", {})
        write_json(
            temp_dir / "agent_quality/assessment.json",
            {"assessment": {"evidence_path": "instruction.md"}},
        )
        write_agent_contract_request(candidate, temp_dir, machine)
        return {
            "status": "AGENT_CONTRACT_PENDING",
            "audit_output_dir": str(output),
        }

    return pending_review


def run_repair(
    package: Path, plan_path: Path, runner: Path
) -> subprocess.CompletedProcess[str]:
    run = package.parent / ".review_records" / "fixture" / "theme" / package.name / "runs" / "repair-test"
    if run.exists():
        shutil.rmtree(run)
    (run / "agent_contract").mkdir(parents=True)
    (run / "regressions").mkdir()
    (run / "roots").mkdir()
    (run / "repair").mkdir(parents=True)
    write_json(run / "agent_contract/assessment.json", {})
    run_context.write_json_atomic(run / "context.json", {
        "schema_version": run_context.RUN_CONTEXT_SCHEMA, "run_id": "repair-test",
        "package_id": f"fixture/theme/{package.name}", "package_path": str(package.resolve()),
        "corpus_root": str(package.parent.resolve()), "review_contract_version": run_context.REVIEW_CONTRACT_VERSION,
        "created_at": run_context.now(),
    })
    run_context.write_json_atomic(run / "status.json", {
        "schema_version": run_context.STATUS_SCHEMA, "state": "ASSIGNED", "updated_at": run_context.now()
    })
    run_context.snapshot_package(package, run)
    shutil.copytree(external_audit_dir(package), run / "audit" / "benchmark_audit")
    shutil.copy2(package.parent / "audit-attestation.json", run / "audit_attestation.json")
    shutil.copy2(plan_path, run / "plan.json")
    run_context.write_content_root(run, "A0")
    materialize_run_assessment(run, package)
    run_context.transition(run, "REVIEWING")
    run_context.transition(run, "REVIEWED")
    return subprocess.run(
        [
            sys.executable,
            str(runner),
            "--run-dir",
            str(run),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


class MaterialsBatchRepairTests(unittest.TestCase):
    def test_agent_contract_pending_persists_resume_state_and_rejects_stale_assessment(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, _runner = batch_context(workspace)
            module = repair_module()
            source_audit = external_audit_dir(package)
            source_manifest = json.loads(
                (source_audit / "audit_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            source_manifest["review_implementation"] = (
                module.collect_review_implementation_hashes()
            )
            write_json(source_audit / "audit_manifest.json", source_manifest)
            write_audit_attestation(package)

            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-pending",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    )
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "pending-plan.json"
            write_json(plan_path, plan)
            package_before = module.package_hashes(package)
            review_calls = {"count": 0}

            def pending_review(
                candidate: Path,
                _report: dict[str, Any],
                _manifest: dict[str, Any],
                _plan: dict[str, Any],
                *,
                original_root: Path | None = None,
                **_kwargs: Any,
            ) -> dict[str, Any]:
                del original_root
                review_calls["count"] += 1
                output = module.reaudit_output_root(candidate)
                context = prepare_workspace(candidate, output)
                temp_dir = Path(context["audit_temp_dir"])
                machine = deterministic_contract.evaluate_deterministic_contract(
                    normalized_instruction_contract={},
                    grading_contract={},
                    checker_analysis={
                        "d6_core_output_scoring": {"status": "UNKNOWN"}
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
                write_json(
                    temp_dir / "deterministic_core/report.json",
                    {
                        "schema_version": DETERMINISTIC_CORE_ARTIFACT_SCHEMA_VERSION,
                        "lane": "deterministic_core",
                        "contract": machine,
                    },
                )
                write_json(
                    temp_dir / "deterministic_core/probe_results.json",
                    {
                        "schema_version": DETERMINISTIC_PROBE_RESULTS_SCHEMA_VERSION,
                        "probe_origin": "SCHEMA_DERIVED_DETERMINISTIC",
                        "cases": [],
                        "status": "ASSESSED",
                    },
                )
                write_json(
                    temp_dir / "evidence/static_checks/audit_static.json",
                    {},
                )
                write_json(temp_dir / "checker_tests.json", {})
                write_json(temp_dir / "resource_checks.json", {})
                write_json(
                    temp_dir / "agent_quality/assessment.json",
                    {"assessment": {"evidence_path": "instruction.md"}},
                )
                write_agent_contract_request(candidate, temp_dir, machine)
                return {
                    "status": "AGENT_CONTRACT_PENDING",
                    "audit_output_dir": str(output),
                }

            with patch.object(
                module, "run_equal_depth_review", side_effect=pending_review
            ):
                pending = module.repair(
                    package,
                    plan_path,
                    workspace / "audit-attestation.json",
                    audit_dir=source_audit,
                    repair_output_dir=external_repair_dir(package),
                )

            self.assertEqual(pending["status"], "AGENT_CONTRACT_PENDING")
            self.assertFalse(pending["publishable"])
            self.assertFalse(pending["attempt_consumed"])
            self.assertFalse(pending["package_mutated"])
            self.assertEqual(pending["attempt_number"], 0)
            self.assertEqual(module.package_hashes(package), package_before)
            history = Path(pending["history_dir"])
            self.assertTrue((history / "snapshot").is_dir())
            self.assertTrue((history / "candidate").is_dir())
            self.assertTrue((history / "reaudit_workspace").is_dir())
            self.assertTrue(
                (history / "reaudit_workspace/agent_contract/request.json").is_file()
            )
            self.assertTrue((history / "repair_context.json").is_file())
            self.assertTrue((history / "pending_state.json").is_file())
            self.assertTrue(
                (workspace / ".benchmark_repair_tmp").is_dir()
            )

            request = json.loads(
                (
                    history
                    / "reaudit_workspace/agent_contract/request.json"
                ).read_text(encoding="utf-8")
            )
            temp_dir = Path(request["audit_temp_dir"])
            quality_path = temp_dir / "agent_quality/assessment.json"
            self.assertTrue(quality_path.is_file())
            self.assertEqual(
                request["quality_assessment_hash"],
                sha256_file(quality_path),
            )
            machine = json.loads(
                (temp_dir / "deterministic_core/report.json").read_text(
                    encoding="utf-8"
                )
            )["contract"]
            checks = {
                check_id: {
                    "status": "PASS" if check_id == "D6" else "NOT_PROVEN",
                    "rationale": f"{check_id} contract wiring",
                    "evidence": (
                        [
                            {
                                "source_kind": "DETERMINISTIC_PROBE_ARTIFACT",
                                "path": "deterministic_core/probe_results.json",
                                "scope": "CONTRACT_WIRING",
                                "artifact_digest": request["probe_hash"],
                            }
                        ]
                        if check_id == "D6"
                        else []
                    ),
                }
                for check_id in ("D1", "D2", "D3", "D4", "D5", "D6")
            }
            assessment = agent_contract_wiring.make_agent_contract_assessment(
                machine, checks
            )
            assessment["assessment_digest"] = "sha256:stale"
            assessment_path = workspace / "stale-assessment.json"
            write_json(assessment_path, assessment)
            with self.assertRaisesRegex(ValueError, "assessment digest"):
                module.repair(
                    package,
                    plan_path,
                    workspace / "audit-attestation.json",
                    audit_dir=source_audit,
                    repair_output_dir=external_repair_dir(package),
                    resume_repair_id=pending["repair_id"],
                    agent_contract_assessment_path=assessment_path,
                )
            self.assertEqual(review_calls["count"], 1)
            prepared_probe_hash = sha256_file(
                temp_dir / "deterministic_core/probe_results.json"
            )
            valid_assessment = agent_contract_wiring.make_agent_contract_assessment(
                machine,
                {
                    check_id: {
                        "status": "PASS",
                        "rationale": f"{check_id} contract wiring",
                        "evidence": [
                            {
                                "source_kind": "DETERMINISTIC_PROBE_ARTIFACT",
                                "path": "deterministic_core/probe_results.json",
                                "scope": "CONTRACT_WIRING",
                                "artifact_digest": request["probe_hash"],
                            }
                        ],
                    }
                    for check_id in ("D1", "D2", "D3", "D4", "D5", "D6")
                },
            )
            write_json(workspace / "valid-assessment.json", valid_assessment)

            def final_review(
                candidate: Path,
                _report: dict[str, Any],
                _manifest: dict[str, Any],
                _plan: dict[str, Any],
                *,
                audit_output_dir: Path,
                **_kwargs: Any,
            ) -> dict[str, Any]:
                review_calls["count"] += 1
                return write_resumed_reaudit(
                    module,
                    candidate,
                    audit_output_dir,
                    machine,
                    valid_assessment,
                )

            with patch.object(
                module, "run_equal_depth_review", side_effect=final_review
            ):
                resumed = module.repair(
                    package,
                    plan_path,
                    workspace / "audit-attestation.json",
                    audit_dir=source_audit,
                    repair_output_dir=external_repair_dir(package),
                    resume_repair_id=pending["repair_id"],
                    agent_contract_assessment_path=(
                        workspace / "valid-assessment.json"
                    ),
                )

            self.assertEqual(resumed["status"], "REPAIRED")
            self.assertTrue(resumed["attempt_consumed"])
            self.assertTrue(resumed["package_mutated"])
            self.assertEqual(resumed["attempt_number"], 1)
            self.assertEqual(review_calls["count"], 2)
            self.assertTrue((package / "solution/solve.sh").is_file())
            retained_probe = Path(resumed["reaudit_bundle_dir"]) / (
                "benchmark_audit/deterministic_core/probe_results.json"
            )
            self.assertEqual(sha256_file(retained_probe), prepared_probe_hash)
            completed_state = json.loads(
                (history / "pending_state.json").read_text(encoding="utf-8")
            )
            self.assertEqual(completed_state["status"], "COMPLETED")
            self.assertTrue(completed_state["attempt_consumed"])
            self.assertTrue(completed_state["package_mutated"])
            attempt_manifest = json.loads(
                (history / "attempt_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertTrue(attempt_manifest["package_mutated"])
            with self.assertRaisesRegex(ValueError, "not resumable"):
                module.repair(
                    package,
                    plan_path,
                    workspace / "audit-attestation.json",
                    audit_dir=source_audit,
                    repair_output_dir=external_repair_dir(package),
                    resume_repair_id=pending["repair_id"],
                    agent_contract_assessment_path=(
                        workspace / "valid-assessment.json"
                    ),
                )
            self.assertEqual(review_calls["count"], 2)

    def test_agent_contract_not_proven_is_terminal_and_retains_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, _runner = batch_context(workspace)
            module = repair_module()
            source_audit = external_audit_dir(package)
            source_manifest = json.loads(
                (source_audit / "audit_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            source_manifest["review_implementation"] = (
                module.collect_review_implementation_hashes()
            )
            write_json(source_audit / "audit_manifest.json", source_manifest)
            write_audit_attestation(package)
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-not-proven",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    )
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "not-proven-plan.json"
            write_json(plan_path, plan)
            package_before = module.package_hashes(package)
            calls = {"count": 0}

            with patch.object(
                module,
                "run_equal_depth_review",
                side_effect=pending_review_seam(module, calls),
            ):
                pending = module.repair(
                    package,
                    plan_path,
                    workspace / "audit-attestation.json",
                    audit_dir=source_audit,
                    repair_output_dir=external_repair_dir(package),
                )

            history = Path(pending["history_dir"])
            request = json.loads(
                (
                    history / "reaudit_workspace/agent_contract/request.json"
                ).read_text(encoding="utf-8")
            )
            machine = json.loads(
                (
                    Path(request["audit_temp_dir"])
                    / "deterministic_core/report.json"
                ).read_text(encoding="utf-8")
            )["contract"]
            assessment = agent_contract_wiring.make_agent_contract_assessment(
                machine,
                {
                    check_id: {
                        "status": "NOT_PROVEN",
                        "rationale": f"{check_id} remains unproven",
                        "evidence": (
                            [
                                {
                                    "source_kind": "DETERMINISTIC_PROBE_ARTIFACT",
                                    "path": "deterministic_core/probe_results.json",
                                    "scope": "CONTRACT_WIRING",
                                    "artifact_digest": request["probe_hash"],
                                }
                            ]
                            if check_id == "D6"
                            else []
                        ),
                    }
                    for check_id in ("D1", "D2", "D3", "D4", "D5", "D6")
                },
            )
            assessment_path = workspace / "not-proven-assessment.json"
            write_json(assessment_path, assessment)

            def final_review(
                candidate: Path,
                _report: dict[str, Any],
                _manifest: dict[str, Any],
                _plan: dict[str, Any],
                *,
                audit_output_dir: Path,
                **_kwargs: Any,
            ) -> dict[str, Any]:
                calls["count"] += 1
                return write_resumed_reaudit(
                    module,
                    candidate,
                    audit_output_dir,
                    machine,
                    assessment,
                    not_proven=True,
                )

            with patch.object(
                module, "run_equal_depth_review", side_effect=final_review
            ):
                result = module.repair(
                    package,
                    plan_path,
                    workspace / "audit-attestation.json",
                    audit_dir=source_audit,
                    repair_output_dir=external_repair_dir(package),
                    resume_repair_id=pending["repair_id"],
                    agent_contract_assessment_path=assessment_path,
                )

            self.assertEqual(result["status"], "NOT_ASSESSABLE")
            self.assertEqual(result["publishability"], "EVIDENCE_PENDING")
            self.assertFalse(result["publishable"])
            self.assertFalse(result["package_mutated"])
            self.assertTrue(result["attempt_consumed"])
            self.assertEqual(result["attempt_number"], 1)
            self.assertEqual(result["agent_contract_status"], "NOT_PROVEN")
            self.assertEqual(calls["count"], 2)
            self.assertEqual(module.package_hashes(package), package_before)
            retained = Path(result["reaudit_bundle_dir"]) / "benchmark_audit"
            self.assertTrue((retained / "audit_report.json").is_file())
            self.assertTrue((retained / "audit_manifest.json").is_file())
            self.assertTrue(
                (retained / "deterministic_core/probe_results.json").is_file()
            )
            state = json.loads(
                (history / "pending_state.json").read_text(encoding="utf-8")
            )
            self.assertEqual(state["status"], "COMPLETED")
            self.assertEqual(state["terminal_status"], "NOT_ASSESSABLE")
            self.assertTrue(state["attempt_consumed"])

    def test_pending_relocation_preserves_quality_and_refreshes_request_hashes(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            module = repair_module()
            old_candidate = workspace / "old-candidate"
            new_candidate = workspace / "new-candidate"
            output = workspace / "prepared-output"
            old_candidate.mkdir()
            new_candidate.mkdir()
            temp_dir = output / ".benchmark_audit_tmp"
            (temp_dir / "evidence/static_checks").mkdir(parents=True)
            (temp_dir / "agent_quality").mkdir(parents=True)
            (temp_dir / "deterministic_core").mkdir(parents=True)
            write_json(
                temp_dir / "evidence/static_checks/audit_static.json",
                {"candidate": str(old_candidate)},
            )
            write_json(
                temp_dir / "checker_tests.json",
                {"output": str(output)},
            )
            write_json(
                temp_dir / "resource_checks.json",
                {"candidate": str(old_candidate)},
            )
            write_json(
                temp_dir / "deterministic_core/probe_results.json",
                {"candidate": str(old_candidate)},
            )
            opaque_path = (
                temp_dir
                / "deterministic_core/probe_cases/checker_tests/"
                "malformed_outputs/app/outputs/metrics.json"
            )
            opaque_path.parent.mkdir(parents=True)
            opaque_bytes = b'{"metrics": [}'
            opaque_path.write_bytes(opaque_bytes)
            quality_path = temp_dir / "agent_quality/assessment.json"
            quality_path.write_text(
                '{"assessment":{"evidence_path":"instruction.md"}}\n',
                encoding="utf-8",
            )
            request_path = output / "agent_contract/request.json"
            request_path.parent.mkdir(parents=True)
            write_json(
                request_path,
                {
                    "benchmark_root": str(old_candidate.resolve()),
                    "quality_assessment_hash": sha256_file(quality_path),
                    "request_digest": "stale-before-relocation",
                },
            )
            original_quality = quality_path.read_bytes()

            with patch.object(
                module,
                "validate_agent_contract_request",
                return_value={},
            ):
                request = module._rewrite_pending_review_workspace(
                    output,
                    old_candidate=old_candidate,
                    new_candidate=new_candidate,
                    old_output=output,
                    new_output=workspace / "relocated-output",
                )

            self.assertEqual(quality_path.read_bytes(), original_quality)
            self.assertEqual(opaque_path.read_bytes(), opaque_bytes)
            self.assertEqual(
                request["quality_assessment_hash"],
                sha256_file(quality_path),
            )
            self.assertEqual(
                request["static_hashes"],
                module.preparation_artifact_hashes(temp_dir)["static"],
            )
            self.assertEqual(
                request["probe_hashes"],
                module.preparation_artifact_hashes(temp_dir)["probes"],
            )
            self.assertEqual(
                request["request_digest"],
                module.canonical_mapping_hash(
                    {
                        key: value
                        for key, value in request.items()
                        if key != "request_digest"
                    }
                ),
            )
            quality_path.write_bytes(original_quality + b"tampered")
            with self.assertRaisesRegex(ValueError, "quality assessment"):
                module._rewrite_pending_review_workspace(
                    output,
                    old_candidate=old_candidate,
                    new_candidate=new_candidate,
                    old_output=output,
                    new_output=workspace / "relocated-output",
                )

    def test_shared_proof_operation_requires_explicit_owner_and_identity(self) -> None:
        module = repair_module()
        owner_fplan = {
            "finding_id": "d3-root",
            "repair_class": "AUTO_FIX",
            "deterministic_check": "D3",
        }
        consequence_fplan = {
            "finding_id": "d6-consequence",
            "repair_class": "AUTO_FIX",
            "deterministic_check": "D6",
        }
        operation = {
            "id": "append-return",
            "type": "replace_text",
            "file": "tests/checker.py",
            "old": "before",
            "new": "after",
            "primary_finding_id": "d3-root",
            "evidence_ids": ["root-evidence"],
        }
        self.assertTrue(
            module.shared_operation_is_safe(
                owner_fplan,
                operation,
                consequence_fplan,
                dict(operation),
            )
        )
        changed = dict(operation, new="different")
        self.assertFalse(
            module.shared_operation_is_safe(
                owner_fplan, operation, consequence_fplan, changed
            )
        )
        unowned = dict(operation)
        unowned.pop("primary_finding_id")
        self.assertFalse(
            module.shared_operation_is_safe(
                owner_fplan, operation, consequence_fplan, unowned
            )
        )



    def test_batch_multi_finding_repaired_and_published(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(workspace)
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    ),
                    finding_entry(
                        FINDING_B,
                        "op-b",
                        "solution/helper.sh",
                        "SOLUTION_HELPER_MISSING",
                    ),
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "batch-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "REPAIRED")
            self.assertEqual(result["repair_state"], "REPAIRED")
            self.assertEqual(result["disposition"], "PASS")
            self.assertTrue(result["publishable"])
            self.assertTrue(result["package_mutated"])
            self.assertEqual(
                sorted(result["resolved_findings"]), [FINDING_B, FINDING_A]
            )
            self.assertTrue((package / "solution/solve.sh").is_file())
            self.assertTrue((package / "solution/helper.sh").is_file())
            self.assertEqual(result["repair_delta"]["C02"]["before_normalized"], 40.0)
            self.assertEqual(result["repair_delta"]["C02"]["after_normalized"], 100.0)
            self.assertEqual(result["repair_delta"]["C02"]["delta_pp"], 60.0)
            repair_module().validate_fixed_bundle(
                external_repair_dir(package) / "benchmark_repair"
            )
            history = Path(result["history_dir"])
            repair_module().validate_fixed_bundle(history)
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

    def test_batch_partial_fix_not_published_preserves_original(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(workspace)
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    ),
                    {
                        "finding_id": FINDING_B,
                        "deterministic_check": "D5",
                        "finding_code": "SOLUTION_ROLE_MISSING",
                        "repair_class": "ABANDON",
                        "justification": "Needs a core science change; abandon.",
                        "evidence": [],
                        "operations": [],
                        "regression_tests": [],
                    },
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "partial-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "PARTIALLY_REPAIRED")
            self.assertEqual(result["repair_state"], "PARTIALLY_REPAIRED")
            self.assertEqual(result["disposition"], "CONDITIONAL")
            self.assertFalse(result["publishable"])
            self.assertFalse(result["package_mutated"])
            # The authoritative package is preserved unchanged: no publish.
            self.assertFalse((package / "solution/solve.sh").is_file())
            self.assertFalse((package / "benchmark_repair").exists())
            unresolved_ids = {item.get("finding_id") for item in result["unresolved"]}
            self.assertIn(FINDING_B, unresolved_ids)
            repair_module().validate_fixed_bundle(Path(result["history_dir"]))
            attempt = json.loads(
                (
                    Path(result["history_dir"]) / "attempt_manifest.json"
                ).read_text(encoding="utf-8")
            )
            self.assertFalse(attempt["package_mutated"])

    def test_batch_reaudit_bundle_is_retained_with_verified_references(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            module = repair_module()
            package, runner = batch_context(
                workspace,
                marker=True,
                malformed_probe_payload=True,
            )
            before = repair_module().package_hashes(package)
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    )
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "retention-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "PARTIALLY_REPAIRED")
            self.assertFalse(result["publishable"])
            self.assertEqual(repair_module().package_hashes(package), before)

            history = Path(result["history_dir"])
            archived = history / "repair_reaudit/benchmark_audit"
            canonical = external_reaudit_dir(package)
            self.assertTrue(archived.is_dir())
            self.assertTrue(canonical.is_dir())
            opaque_relative = (
                "deterministic_core/probe_cases/checker_tests/"
                "malformed_outputs/app/outputs/metrics.json"
            )
            opaque_bytes = b'{"metrics": [}'
            self.assertEqual(
                (archived / opaque_relative).read_bytes(),
                opaque_bytes,
            )
            self.assertEqual(
                (canonical / opaque_relative).read_bytes(),
                opaque_bytes,
            )
            archived_report = json.loads(
                (archived / "audit_report.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                archived_report["workspace_path"],
                str(package.resolve()),
            )
            self.assertIn(
                str(package.resolve()),
                (archived / "audit_report.md").read_text(encoding="utf-8"),
            )
            self.assertNotIn(
                ".benchmark_repair_tmp",
                (archived / "audit_report.md").read_text(encoding="utf-8"),
            )
            self.assertFalse((workspace / ".benchmark_repair_tmp").exists())
            self.assertFalse(
                any(
                    path.name == "audit_report.json"
                    for path in (workspace / ".benchmark_repair_tmp").rglob("*")
                )
                if (workspace / ".benchmark_repair_tmp").exists()
                else False
            )

            manifest = json.loads(
                (archived / "audit_manifest.json").read_text(encoding="utf-8")
            )
            for relative, expected in manifest["output_hashes"].items():
                self.assertEqual(
                    repair_module().sha256_file(archived / relative), expected
                )
            self.assertEqual(
                manifest["output_hashes"][opaque_relative],
                sha256_file(archived / opaque_relative),
            )
            self.assertEqual(
                manifest["bundle_hash"],
                module.canonical_json_hash(manifest["output_hashes"]),
            )
            # Archived legacy bundles are provenance only. Active run
            # integrity is enforced by the A0/R0/A1 ContentRoots instead of a
            # second report/manifest hash gate.
            (archived / opaque_relative).write_bytes(b"tampered")
            (archived / opaque_relative).write_bytes(opaque_bytes)
            references = json.loads(
                (history / "attempt_manifest.json").read_text(encoding="utf-8")
            )["reaudit_bundle"]
            self.assertEqual(references["bundle_dir"], str(archived.parent))
            self.assertEqual(references["audit_dir"], str(archived))
            self.assertEqual(references["audit_id"], manifest["audit_id"])
            self.assertEqual(
                references["report_hash"],
                repair_module().sha256_file(archived / "audit_report.json"),
            )
            self.assertEqual(
                references["manifest_hash"],
                repair_module().sha256_file(archived / "audit_manifest.json"),
            )
            self.assertEqual(
                references["bundle_hash"], repair_module().sha256_path(archived)
            )
            history_refs = json.loads(
                (history / "repair_manifest.json").read_text(encoding="utf-8")
            )["reaudit_bundle"]
            self.assertEqual(history_refs, references)
            self.assertNotIn(
                "oracle",
                (history / "evidence" / "records.json").read_text(encoding="utf-8").lower(),
            )
            repair_module().validate_fixed_bundle(history)

    def test_rebase_fails_closed_on_malformed_authoritative_json(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            module = repair_module()
            candidate = workspace / "candidate"
            final_root = workspace / "paper-final"
            output = workspace / "repair_reaudit"
            audit = output / "benchmark_audit"
            candidate.mkdir()
            final_root.mkdir()
            audit.mkdir(parents=True)
            malformed = audit / "audit_report.json"
            malformed.write_bytes(b'{"audit_id": [}')
            manifest = audit / "audit_manifest.json"
            write_json(
                manifest,
                {
                    "benchmark_root": str(candidate),
                    "output_hashes": {
                        "audit_report.json": sha256_file(malformed)
                    },
                },
            )
            manifest_before = manifest.read_bytes()
            with self.assertRaises(json.JSONDecodeError):
                module.rebase_audit_paths(
                    candidate,
                    final_root,
                    {},
                    audit_output_dir=output,
                )
            self.assertEqual(malformed.read_bytes(), b'{"audit_id": [}')
            self.assertEqual(manifest.read_bytes(), manifest_before)

    def test_batch_publish_only_on_full_reaudit_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(workspace, marker=True)
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    ),
                    finding_entry(
                        FINDING_B,
                        "op-b",
                        "solution/helper.sh",
                        "SOLUTION_HELPER_MISSING",
                    ),
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "invariant-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            # All findings applied cleanly, but the re-audit is not PASS.
            self.assertEqual(result["status"], "PARTIALLY_REPAIRED")
            self.assertFalse(result["publishable"])
            self.assertFalse((package / "solution/solve.sh").is_file())

    def test_batch_retains_nonblocking_agent_quality_high_residual(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(
                workspace, agent_quality_residual=True
            )
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    )
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "agent-quality-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "PARTIALLY_REPAIRED")
            residual = next(
                item
                for item in result["unresolved"]
                if item.get("finding_id") == "agent-quality-high"
            )
            self.assertEqual(residual["severity"], "HIGH")
            self.assertFalse(residual["blocking"])
            self.assertEqual(residual["lane"], "agent_quality")
            self.assertTrue(residual["finding_fingerprint"].startswith("sha256:"))
            self.assertNotIn("oracle", json.dumps(result).lower())
            repair_module().validate_fixed_bundle(Path(result["history_dir"]))

    def test_batch_per_op_block_does_not_block_sibling(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(workspace)
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    ),
                    finding_entry(
                        FINDING_B,
                        "op-b",
                        "solution/helper.sh",
                        "SOLUTION_HELPER_MISSING",
                        bad_evidence=True,
                    ),
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "sibling-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "PARTIALLY_REPAIRED")
            unresolved_ids = {item.get("finding_id") for item in result["unresolved"]}
            self.assertIn(FINDING_B, unresolved_ids)
            self.assertFalse((package / "solution/solve.sh").is_file())



    def test_batch_publishes_reading_publication_route_not_verdict(self) -> None:
        # Regression for Bug 1: the re-audit stub emits the real v11 layout
        # where summary.disposition holds the VERDICT ("PASS") and the publish
        # route lives in publication_route / disposition.json route.  Reading
        # summary.disposition as the route (the bug) would leave this batch at
        # PARTIALLY_REPAIRED and never publish.
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(workspace)
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    ),
                    finding_entry(
                        FINDING_B,
                        "op-b",
                        "solution/helper.sh",
                        "SOLUTION_HELPER_MISSING",
                    ),
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "route-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(
                completed.returncode,
                0,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "REPAIRED")
            self.assertTrue(result["publishable"])
            self.assertTrue((package / "solution/solve.sh").is_file())
            # Confirm the published re-audit really used the v11 layout: the
            # verdict lives in disposition, and the route is elsewhere.
            repair_manifest = json.loads(
                (
                    external_repair_dir(package)
                    / "benchmark_repair/repair_report.json"
                ).read_text(encoding="utf-8")
            )
            comparison = repair_manifest["re_audit_comparison"]
            self.assertEqual(comparison["reaudit_verdict"], "PASS")
            self.assertEqual(
                comparison["publication_route"], "PUBLISH_CANDIDATE"
            )

    def test_batch_residual_target_finding_blocks_publish(self) -> None:
        # Regression for Bug 2: the re-audit routes PASS/PUBLISH_CANDIDATE but
        # still lists a targeted finding code.  The batch must NOT publish; it
        # stays PARTIALLY_REPAIRED and the original package is preserved.
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(workspace, residual_target=True)
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    ),
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "residual-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "PARTIALLY_REPAIRED")
            self.assertFalse(result["publishable"])
            self.assertFalse((package / "solution/solve.sh").is_file())
            self.assertFalse((package / "benchmark_repair").exists())
            residual = next(
                item
                for item in result["unresolved"]
                if item.get("source_finding_id") == FINDING_A
            )
            self.assertEqual(residual["finding_id"], "reaudit-residual")
            self.assertEqual(
                residual["finding_code"], "SOLUTION_ORACLE_MISSING"
            )
            self.assertTrue(
                residual["finding_fingerprint"].startswith("sha256:")
            )
            repair_module().validate_fixed_bundle(Path(result["history_dir"]))

    def test_batch_rollback_before_regressions_preserves_package(self) -> None:
        # Item 3 regression: force a failure during the "before" regression run
        # (i.e. BEFORE regression_results is assigned) and assert the rollback
        # archival does not raise UnboundLocalError, surfaces the original
        # error, and preserves the authoritative package.
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(workspace, precreate_solve=True)
            original_solve = (package / "solution/solve.sh").read_text(
                encoding="utf-8"
            )
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    ),
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "rollback-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            # returncode 3 = controlled non-publish outcome; 2 would mean an
            # uncaught exception (e.g. UnboundLocalError) escaped repair_batch.
            self.assertEqual(
                completed.returncode,
                3,
                msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
            )
            self.assertNotIn("UnboundLocalError", completed.stderr)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "ROLLED_BACK")
            self.assertFalse(result["publishable"])
            # The original (pre-regression) error is surfaced, not shadowed.
            self.assertIn("regression test before result", result["reason"])
            # Authoritative package preserved unchanged; no publish.
            self.assertTrue((package / "solution/solve.sh").is_file())
            self.assertEqual(
                (package / "solution/solve.sh").read_text(encoding="utf-8"),
                original_solve,
            )
            self.assertFalse((package / "benchmark_repair").exists())
            first_history = Path(result["history_dir"])
            first_attempt = json.loads(
                (first_history / "attempt_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertNotIn("reaudit_bundle", first_attempt)
            self.assertFalse(
                (first_history / "repair_reaudit").exists()
            )

            # A new user-created run does not inherit another run's control
            # breaker history.
            completed_again = run_repair(package, plan_path, runner)
            self.assertEqual(completed_again.returncode, 3)
            second = json.loads(completed_again.stdout)
            self.assertEqual(second["status"], "ROLLED_BACK")
            self.assertEqual(second["attempt_number"], 1)
            self.assertEqual(second["attempt_kind"], "CONTROL_FAILURE")
            self.assertFalse(second["attempt_consumed"])
            self.assertTrue(second["retryable"])
            self.assertFalse(second["package_mutated"])
            self.assertEqual(second["control_failure_same_fingerprint"], 1)

            # A third fresh run is likewise isolated from earlier control
            # failures.
            completed_third = run_repair(package, plan_path, runner)
            self.assertEqual(completed_third.returncode, 3)
            third = json.loads(completed_third.stdout)
            self.assertEqual(third["status"], "ROLLED_BACK")
            self.assertNotEqual(third["history_dir"], second["history_dir"])

    def test_batch_attempt_limit_second_failure_is_abandoned(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(workspace, marker=True)

            def one_pass() -> dict[str, Any]:
                plan = batch_plan(
                    [
                        finding_entry(
                            FINDING_A,
                            "op-a",
                            "solution/solve.sh",
                            "SOLUTION_ENTRYPOINT_MISSING",
                        )
                    ]
                )
                bind_batch_plan(package, plan)
                plan_path = workspace / "attempt-plan.json"
                write_json(plan_path, plan)
                completed = run_repair(package, plan_path, runner)
                self.assertEqual(completed.returncode, 3)
                return json.loads(completed.stdout)

            first = one_pass()
            self.assertEqual(first["status"], "PARTIALLY_REPAIRED")
            second = one_pass()
            self.assertEqual(second["status"], "PARTIALLY_REPAIRED")
            self.assertEqual(second["repair_state"], "PARTIALLY_REPAIRED")
            self.assertEqual(second["disposition"], "CONDITIONAL")
            self.assertFalse(second["publishable"])
            self.assertFalse(second["package_mutated"])
            second_history = Path(second["history_dir"])
            self.assertTrue(
                (second_history / "repair_reaudit/benchmark_audit").is_dir()
            )
            second_attempt = json.loads(
                (second_history / "attempt_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertIn("reaudit_bundle", second_attempt)
            self.assertFalse(second_attempt["package_mutated"])
            repair_module().validate_fixed_bundle(second_history)

    def test_reaudit_score_below_60_abandons_without_publication(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            package, runner = batch_context(workspace, low_score=True)
            plan = batch_plan(
                [
                    finding_entry(
                        FINDING_A,
                        "op-a",
                        "solution/solve.sh",
                        "SOLUTION_ENTRYPOINT_MISSING",
                    )
                ]
            )
            bind_batch_plan(package, plan)
            plan_path = workspace / "low-score-plan.json"
            write_json(plan_path, plan)

            completed = run_repair(package, plan_path, runner)

            self.assertEqual(completed.returncode, 3)
            result = json.loads(completed.stdout)
            self.assertEqual(result["status"], "ABANDONED")
            self.assertFalse(result["publishable"])
            self.assertFalse((package / "solution/solve.sh").exists())
            history = Path(result["history_dir"])
            self.assertTrue(
                (history / "repair_reaudit/benchmark_audit").is_dir()
            )
            repair_module().validate_fixed_bundle(history)


    def test_atomic_publication_failure_restores_false_mutation_attestation(
        self,
    ) -> None:
        module = repair_module()
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root = workspace / "paper-root"
            candidate = workspace / "candidate"
            history = workspace / "history"
            root.mkdir()
            candidate.mkdir()
            history.mkdir()
            (root / "state.txt").write_text("original", encoding="utf-8")
            (candidate / "state.txt").write_text("candidate", encoding="utf-8")
            attempt_manifest = history / "attempt_manifest.json"
            write_json(
                attempt_manifest,
                {"status": "REPAIRED", "package_mutated": False},
            )
            original_writer = module.write_attempt_manifest

            def fail_final_attestation(
                path: Path,
                manifest: dict[str, Any],
                *,
                package_mutated: bool,
            ) -> None:
                if package_mutated:
                    raise OSError("simulated attestation write failure")
                original_writer(
                    path, manifest, package_mutated=package_mutated
                )

            with patch.object(
                module,
                "write_attempt_manifest",
                side_effect=fail_final_attestation,
            ):
                with self.assertRaisesRegex(
                    OSError, "attestation write failure"
                ):
                    module.atomic_publish_candidate(
                        root=root,
                        candidate=candidate,
                        history=history,
                        generated_outputs={},
                        attempt_manifest_path=attempt_manifest,
                    )

            self.assertEqual(
                (root / "state.txt").read_text(encoding="utf-8"),
                "original",
            )
            self.assertEqual(
                (candidate / "state.txt").read_text(encoding="utf-8"),
                "candidate",
            )
            self.assertFalse(
                json.loads(attempt_manifest.read_text(encoding="utf-8"))[
                    "package_mutated"
                ]
            )


if __name__ == "__main__":
    unittest.main()
