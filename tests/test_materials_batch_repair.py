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


REPO_ROOT = Path(__file__).resolve().parents[1]
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
parser.add_argument("--paper-mode", required=True)
parser.add_argument("--execution-level", required=True)
parser.add_argument("--agent-assessment")
parser.add_argument("--e2-smoke-plan")
args = parser.parse_args()
root = Path(args.root)
instruction_text = (root / "instruction.md").read_text()
broken = "STILL_BROKEN" in instruction_text
residual_target = "STILL_LISTS_TARGET" in instruction_text
low_score = "LOW_SCORE" in instruction_text
audit = root / "benchmark_audit"
if audit.exists():
    shutil.rmtree(audit)
audit.mkdir()
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
                 "title": "SOLUTION_ENTRYPOINT_MISSING", "severity": "LOW"}]
    dimensions = {k: {"normalized": 100.0} for k in
                  ("C01","C02","C03","C04","C05","C06","C07")}
else:
    verdict, route = "PASS", "PUBLISH_CANDIDATE"
    findings = []
    dimensions = {k: {"normalized": 100.0} for k in
                  ("C01","C02","C03","C04","C05","C06","C07")}
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
    "configuration": {"paper_mode": args.paper_mode,
                      "execution_level": args.execution_level},
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
    audit = package / "benchmark_audit"
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
    if precreate_solve:
        # Pre-seed the operation target with the exact content the plan writes
        # so the "before" regression already passes and run_regressions raises
        # BEFORE regression_results is assigned (exercises the sentinel branch).
        (package / "solution/solve.sh").write_text(
            "#!/bin/sh\nexit 0\n", encoding="utf-8"
        )
    instruction = "Compute the evidence-backed quantity.\n"
    if marker:
        instruction += "STILL_BROKEN\n"
    if residual_target:
        instruction += "STILL_LISTS_TARGET\n"
    if low_score:
        instruction += "LOW_SCORE\n"
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
    }
    report = {
        "schema_version": AUDIT_REPORT_SCHEMA_VERSION,
        "bundle_schema_version": AUDIT_BUNDLE_SCHEMA_VERSION,
        "audit_id": AUDIT_ID,
        "configuration": {"paper_mode": "paper_grounded", "execution_level": "E1"},
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
    write_json(package / "benchmark_audit/audit_report.json", report)
    write_json(
        package / "benchmark_audit/disposition.json",
        {
            "schema_version": DISPOSITION_SCHEMA_VERSION,
            "audit_id": AUDIT_ID,
            "route": "REPAIR_QUEUE",
            "verdict": "CONDITIONAL",
        },
    )
    write_json(
        package / "benchmark_audit/deterministic_core/report.json",
        deterministic_core,
    )
    write_json(
        package / "benchmark_audit/deterministic_core/probe_results.json",
        probe_results,
    )
    write_json(
        package / "benchmark_audit/agent_quality/assessment.json",
        agent_quality,
    )
    for relative in (
        "corpus_index_entry.json",
        "checker_tests.json",
        "resource_checks.json",
    ):
        write_json(package / f"benchmark_audit/{relative}", {})
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
        package / "benchmark_audit/audit_manifest.json",
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
                    package / "benchmark_audit/audit_report.json"
                ),
                "disposition.json": sha256_file(
                    package / "benchmark_audit/disposition.json"
                ),
                "corpus_index_entry.json": sha256_file(
                    package / "benchmark_audit/corpus_index_entry.json"
                ),
                "checker_tests.json": sha256_file(
                    package / "benchmark_audit/checker_tests.json"
                ),
                "resource_checks.json": sha256_file(
                    package / "benchmark_audit/resource_checks.json"
                ),
                "deterministic_core/report.json": sha256_file(
                    package / "benchmark_audit/deterministic_core/report.json"
                ),
                "deterministic_core/probe_results.json": sha256_file(
                    package
                    / "benchmark_audit/deterministic_core/probe_results.json"
                ),
                "agent_quality/assessment.json": sha256_file(
                    package / "benchmark_audit/agent_quality/assessment.json"
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
    return {
        "finding_id": finding_id,
        "repair_class": repair_class,
        "justification": f"Restore {file}.",
        "core_science_change": False,
        "evidence": [
            {
                "id": f"ev-{op_id}",
                "source": (
                    "not-a-real-source.md"
                    if bad_evidence
                    else f"benchmark_audit:{finding_id}"
                ),
                "quote": quote,
            }
        ],
        "operations": [
            {
                "id": op_id,
                "type": "write_file",
                "file": file,
                "content": "#!/bin/sh\nexit 0\n",
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
                "expected": "#!/bin/sh\nexit 0\n",
            }
        ],
    }


def bind_batch_plan(package: Path, plan: dict[str, Any]) -> None:
    module = repair_module()
    manifest = json.loads(
        (package / "benchmark_audit/audit_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    report_hash = sha256_file(package / "benchmark_audit/audit_report.json")
    digest = module.core_contract_digest(package)
    plan["core_contract_digest"] = digest
    plan["source_audit"] = {
        "audit_id": plan["audit_id"],
        "input_hashes": manifest["input_hashes"],
        "review_implementation": manifest.get("review_implementation", {}),
        "paper_mode": "paper_grounded",
        "execution_level": "E1",
        "core_contract_digest": digest,
        "assessment_hashes": {},
    }
    for finding in plan["findings"]:
        for item in finding.get("evidence", []):
            source = item.get("source", "")
            if source.startswith("benchmark_audit:"):
                item["source_hash"] = report_hash
            else:
                local = package / source
                if local.is_file():
                    item["source_hash"] = sha256_file(local)


def batch_plan(findings: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": "0.1",
        "audit_id": AUDIT_ID,
        "core_science_change": False,
        "findings": findings,
    }


def run_repair(
    package: Path, plan_path: Path, runner: Path
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(runner),
            str(package),
            "--plan",
            str(plan_path),
            "--audit-attestation",
            str(package.parent / "audit-attestation.json"),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )


class MaterialsBatchRepairTests(unittest.TestCase):
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
            self.assertEqual(
                sorted(result["resolved_findings"]), [FINDING_B, FINDING_A]
            )
            self.assertTrue((package / "solution/solve.sh").is_file())
            self.assertTrue((package / "solution/helper.sh").is_file())
            self.assertEqual(result["repair_delta"]["C02"]["before_normalized"], 40.0)
            self.assertEqual(result["repair_delta"]["C02"]["after_normalized"], 100.0)
            self.assertEqual(result["repair_delta"]["C02"]["delta_pp"], 60.0)
            repair_module().validate_fixed_bundle(package / "benchmark_repair")
            repair_module().validate_fixed_bundle(Path(result["history_dir"]))

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
            # The authoritative package is preserved unchanged: no publish.
            self.assertFalse((package / "solution/solve.sh").is_file())
            self.assertFalse((package / "benchmark_repair").exists())
            unresolved_ids = {item.get("finding_id") for item in result["unresolved"]}
            self.assertIn(FINDING_B, unresolved_ids)
            repair_module().validate_fixed_bundle(Path(result["history_dir"]))

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
            reaudit = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(reaudit["summary"]["disposition"], "PASS")
            self.assertEqual(
                reaudit["summary"]["publication_route"], "PUBLISH_CANDIDATE"
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
                residual["finding_code"], "SOLUTION_ENTRYPOINT_MISSING"
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

            # A control/regression-harness rollback is not an authoritative
            # semantic attempt. The repeated fingerprint trips the separate
            # control-plane circuit breaker without converging to ABANDONED.
            completed_again = run_repair(package, plan_path, runner)
            self.assertEqual(completed_again.returncode, 3)
            second = json.loads(completed_again.stdout)
            self.assertEqual(second["status"], "INFRASTRUCTURE_BLOCKED")
            self.assertEqual(second["attempt_number"], 1)
            self.assertEqual(second["attempt_kind"], "CONTROL_FAILURE")
            self.assertFalse(second["attempt_consumed"])
            self.assertFalse(second["retryable"])
            self.assertEqual(second["control_failure_same_fingerprint"], 2)

            # Once open, the breaker returns its existing terminal record and
            # does not create an unbounded stream of retry histories.
            completed_third = run_repair(package, plan_path, runner)
            self.assertEqual(completed_third.returncode, 3)
            third = json.loads(completed_third.stdout)
            self.assertEqual(third["status"], "INFRASTRUCTURE_BLOCKED")
            self.assertEqual(third["history_dir"], second["history_dir"])

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
            self.assertEqual(second["status"], "ABANDONED")
            self.assertEqual(second["repair_state"], "ABANDONED")
            self.assertEqual(second["disposition"], "REJECT")
            self.assertFalse(second["publishable"])

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


if __name__ == "__main__":
    unittest.main()
