from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CERTIFIER = (
    REPO_ROOT
    / "review_artifacts"
    / "materials_fast_e1_100"
    / "certify_final_100.py"
)
REVIEW_SKILL_ROOT = (
    REPO_ROOT / ".cursor/skills/materials-benchmark-review"
)
REVIEW_IMPLEMENTATION_FILES = (
    "scripts/prepare_audit_output.py",
    "scripts/audit_package.py",
    "scripts/dynamic_checker_probe.py",
    "scripts/finalize_audit_output.py",
    "scripts/run_review.py",
    "scripts/run_fast_e1_batch.py",
)


def canonical_hash(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def review_implementation() -> dict[str, Any]:
    files = {
        relative: file_hash(REVIEW_SKILL_ROOT / relative)
        for relative in REVIEW_IMPLEMENTATION_FILES
    }
    return {
        "schema_version": "materials-review-implementation/1.0",
        "root": ".cursor/skills/materials-benchmark-review",
        "files": files,
        "aggregate_hash": canonical_hash(files),
    }


def write_legacy_pass_batch(batch: Path) -> None:
    package_id = "cluster-1/theme/paper-1"
    audit = batch / "cli_reports" / package_id
    audit.mkdir(parents=True)
    dimensions = [
        {
            "dimension": name,
            "max_points": maximum,
            "points_earned": maximum,
            "status": "PASS",
            "evidence": [],
        }
        for name, maximum in (
            ("scientific_validity", 35),
            ("instruction_answerability", 20),
            ("checker_gold_alignment", 25),
            ("robustness_discrimination", 15),
            ("solution_completeness", 5),
        )
    ]
    gates = [
        {"code": code, "status": "PASS", "evidence": [{"fact": "legacy"}]}
        for code in (
            "NON_MATERIALS_TASK",
            "SCIENTIFIC_TARGET_INVALID",
            "CHECKER_CORE_TASK_UNASSESSED",
            "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
        )
    ]
    report = {
        "audit_id": "audit-legacy",
        "summary": {
            "scoring_version": "materials-review-scoring/1.0",
            "final_verdict": "PASS",
            "total_score": 100,
            "hard_gate_triggered": False,
        },
        "configuration": {"paper_mode": "no_paper"},
        "materials_qualification": {
            "authoritative": False,
            "classification": "MAT_CORE",
            "evidence": [],
        },
        "dimension_scores": dimensions,
        "hard_gates": gates,
        "scope": {"solution_content_inspected": False},
    }
    report_path = audit / "audit_report.json"
    report_path.write_text(json.dumps(report), encoding="utf-8")
    checker_path = audit / "checker_tests.json"
    checker_path.write_text(
        json.dumps(
            {
                "solution_content_inspected": False,
                "solution_oracle": {"scientific_evidence": False},
            }
        ),
        encoding="utf-8",
    )
    manifest = {
        "audit_id": "audit-legacy",
        "input_hashes": {"instruction.md": "sha256:source"},
        "output_hashes": {"audit_report.json": file_hash(report_path)},
    }
    manifest_path = audit / "audit_manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    scoring = {
        "scoring_version": "materials-review-scoring/1.0",
        "final_verdict": "PASS",
        "total_score": 100,
        "hard_gate_triggered": False,
        "dimension_scores": dimensions,
        "hard_gates": gates,
    }
    scoring["snapshot_hash"] = canonical_hash(scoring)
    record = {
        "package_id": package_id,
        "source_relative_path": package_id,
        "evidence": {
            "cli_scoring": scoring,
            "source_binding": {
                "package_id": package_id,
                "source_relative_path": package_id,
                "source_role_hashes": manifest["input_hashes"],
                "cli_audit_identity": {
                    "status": "VALIDATED",
                    "package_id": package_id,
                    "source_relative_path": package_id,
                    "audit_id": "audit-legacy",
                    "scoring_snapshot_hash": scoring["snapshot_hash"],
                    "report_path": report_path.relative_to(batch).as_posix(),
                    "manifest_path": manifest_path.relative_to(batch).as_posix(),
                },
            },
        },
    }
    (batch / "index.json").write_text(
        json.dumps({"records": [record]}), encoding="utf-8"
    )


def write_evidence_pass_batch(batch: Path) -> None:
    write_legacy_pass_batch(batch)
    index_path = batch / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    record = index["records"][0]
    identity = record["evidence"]["source_binding"]["cli_audit_identity"]
    report_path = batch / identity["report_path"]
    manifest_path = batch / identity["manifest_path"]
    checker_path = report_path.with_name("checker_tests.json")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["evidence_contract"] = {
        "version": "materials-evidence-contract/1.0",
        "fail_closed": True,
        "gaps": [],
    }
    report["materials_qualification"] = {
        "authoritative": True,
        "classification": "MAT_CORE",
        "rationale": "Instruction/tests evidence establishes the material task.",
        "evidence": [
            {
                "axis": "object",
                "package_file": "instruction.md",
                "package_quote": "crystal",
            }
        ],
    }
    report["findings"] = []
    report["scope"] = {
        "solution_content_inspected": False,
        "solution_oracle_executed": True,
    }
    report["contract_map"] = {
        "requirements": [
            {
                "requirement_index": 1,
                "step": "Compute result",
                "agent_work": "Compute result",
                "role": "scored (load-bearing)",
            }
        ],
        "requirement_chains": [
            {
                "requirement_index": 1,
                "declaration_index": 1,
                "core_output": "result.json",
                "checker_read": "STATIC_EXPLICIT_READ_CANDIDATE",
            }
        ],
        "instruction_outputs": ["result.json"],
        "process_evidence": [],
        "scored_outputs": ["result.json"],
        "load_bearing_outputs": ["result.json"],
        "core_outputs": ["result.json"],
        "checker_analysis": {
            "outputs": [
                {
                    "file": "result.json",
                    "checker_reads": "STATIC_EXPLICIT_READ_CANDIDATE",
                }
            ],
            "dynamic_checks_required": [
                {
                    "check": "component_isolation",
                    "status": "NOT_RUN",
                    "reason": "no independent fixture",
                    "provenance": {
                        "source_kind": "NONE",
                        "oracle_used": False,
                        "source_bindings_verified": False,
                        "runtime_bindings_verified": False,
                        "cases_planned": 0,
                        "cases_executed": 0,
                    },
                },
            ],
        },
    }
    report["gold_provenance"] = {
        "status": "ASSESSED",
        "mode": "no_paper",
        "reason": "Independent public evidence supports the Gold contract.",
        "outputs": ["result.json"],
        "oracle_used": False,
        "provenance": {
            "source_kind": "INDEPENDENT_PUBLIC_FIXTURE",
            "independent": True,
        },
    }
    report["paper_trigger_adjudication"] = [
        {
            "trigger": trigger,
            "status": "NOT_TRIGGERED",
            "rationale": "Instruction/tests do not trigger paper review.",
            "evidence": [
                {
                    "package_file": "instruction.md",
                    "package_quote": "crystal",
                }
            ],
        }
        for trigger in (
            "SCIENTIFIC_CONFLICT",
            "NECESSARY_INFORMATION_MISSING",
            "GOLD_PROVENANCE_UNCERTAIN",
            "EXPLICIT_REPRODUCTION_CLAIM",
        )
    ]
    for dimension in report["dimension_scores"]:
        dimension["evidence"] = [
            {
                "evidence_type": "public_contract",
                "observed_fact": "Instruction/tests and dynamic probes support this dimension.",
            }
        ]
        if dimension["dimension"] == "robustness_discrimination":
            dimension["points_earned"] = 12
            dimension["status"] = "PASS"
    report["summary"]["total_score"] = 97
    report_path.write_text(json.dumps(report), encoding="utf-8")
    checker = {
        "solution_content_inspected": False,
        "solution_oracle": {
            "used": True,
            "status": "PASS",
            "positive_mock_available": True,
            "attempted": True,
            "setup_attempted": True,
            "setup_prepared": True,
            "producer_started": True,
            "executed": True,
            "scientific_evidence": False,
        },
        "tests": [
            {
                "probe_class": "positive",
                "observed_status": "COMPLETED",
            },
            {
                "probe_class": "negative",
                "observed_status": "COMPLETED",
            },
        ],
        "usable_reward_count": 2,
        "probe_coverage": {
            "positive": {
                "status": "ASSESSED",
                "provenance": {
                    "source_kinds": ["ORACLE_POSITIVE_MOCK"],
                    "oracle_scientific_evidence": False,
                },
            },
            "negative": {
                "status": "ASSESSED",
                "provenance": {
                    "source_kind": "SCHEMA_SHAPED_SYNTHETIC_ATTACKS",
                    "oracle_used": False,
                },
            },
            "discrimination": {
                "status": "NOT_ASSESSABLE",
                "provenance": {
                    "source_kind": "NONE",
                    "fixture_hashes": {},
                    "oracle_used": False,
                },
            },
            "equivalence": {
                "status": "NOT_ASSESSABLE",
                "provenance": {
                    "source_kind": "NONE",
                    "fixture_hashes": {},
                    "oracle_used": False,
                },
            },
            "component_isolation": {
                "status": "NOT_RUN",
                "reason": "no independent fixture",
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                    "source_bindings_verified": False,
                    "runtime_bindings_verified": False,
                    "cases_planned": 0,
                    "cases_executed": 0,
                },
            },
            "task_family_attacks": {
                attack: {
                    "status": "NOT_APPLICABLE",
                    "reason": "attack is not applicable to this fixture",
                    "provenance": {
                        "source_kind": "NONE",
                        "oracle_used": False,
                        "cases": [],
                        "modes": [],
                    },
                }
                for attack in (
                    "constant_or_all_zero",
                    "all_positive_or_negative",
                    "conflicting_or_irrelevant_records",
                    "threshold_boundary",
                    "unit_error",
                    "element_or_phase_error",
                    "coordinate_or_lattice_error",
                    "duplicate_structure",
                    "wrong_objective_or_endpoint",
                    "missing_core_model",
                )
            },
        },
    }
    checker_path.write_text(json.dumps(checker), encoding="utf-8")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["output_hashes"]["audit_report.json"] = file_hash(report_path)
    manifest["output_hashes"]["checker_tests.json"] = file_hash(checker_path)
    manifest["review_implementation"] = review_implementation()
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    scoring = {
        "scoring_version": report["summary"]["scoring_version"],
        "final_verdict": report["summary"]["final_verdict"],
        "total_score": report["summary"]["total_score"],
        "hard_gate_triggered": report["summary"]["hard_gate_triggered"],
        "dimension_scores": report["dimension_scores"],
        "hard_gates": report["hard_gates"],
    }
    scoring["snapshot_hash"] = canonical_hash(scoring)
    record["evidence"]["cli_scoring"] = scoring
    identity["scoring_snapshot_hash"] = scoring["snapshot_hash"]
    cli_evidence = {
        "contract_version": report["evidence_contract"]["version"],
        "audit_id": report["audit_id"],
        "fail_closed": True,
        "gaps": [],
        "materials_qualification": report["materials_qualification"],
        "paper_trigger_adjudication": report["paper_trigger_adjudication"],
        "probe_coverage": checker["probe_coverage"],
        "review_implementation": manifest["review_implementation"],
        "solution_oracle": checker["solution_oracle"],
        "report_path": identity["report_path"],
        "manifest_path": identity["manifest_path"],
        "checker_tests_path": checker_path.relative_to(batch).as_posix(),
        "report_hash": file_hash(report_path),
        "manifest_hash": file_hash(manifest_path),
        "checker_tests_hash": file_hash(checker_path),
    }
    cli_evidence["snapshot_hash"] = canonical_hash(cli_evidence)
    record["evidence"]["cli_evidence"] = cli_evidence
    index_path.write_text(json.dumps(index), encoding="utf-8")


def refresh_evidence_bindings(batch: Path) -> None:
    index_path = batch / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    record = index["records"][0]
    identity = record["evidence"]["source_binding"]["cli_audit_identity"]
    report_path = batch / identity["report_path"]
    manifest_path = batch / identity["manifest_path"]
    checker_path = report_path.with_name("checker_tests.json")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["output_hashes"]["audit_report.json"] = file_hash(report_path)
    manifest["output_hashes"]["checker_tests.json"] = file_hash(checker_path)
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    cli_evidence = record["evidence"]["cli_evidence"]
    cli_evidence["probe_coverage"] = checker.get("probe_coverage", {})
    cli_evidence["review_implementation"] = manifest.get(
        "review_implementation"
    )
    cli_evidence["report_hash"] = file_hash(report_path)
    cli_evidence["manifest_hash"] = file_hash(manifest_path)
    cli_evidence["checker_tests_hash"] = file_hash(checker_path)
    cli_evidence["snapshot_hash"] = canonical_hash(
        {
            key: value
            for key, value in cli_evidence.items()
            if key != "snapshot_hash"
        }
    )
    index_path.write_text(json.dumps(index), encoding="utf-8")


class MaterialsFinal100CertificationTests(unittest.TestCase):
    def test_certifier_accepts_honest_partial_probe_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            batch = base / "batch"
            output = base / "certified"
            write_evidence_pass_batch(batch)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(CERTIFIER),
                    "--batch",
                    str(batch),
                    "--output",
                    str(output),
                    "--expected-count",
                    "1",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            certified = json.loads(
                (output / "final_100_pass_index.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(certified["certified_count"], 1)
            self.assertTrue(certified["all_evidence_contracts_valid"])
            self.assertEqual(
                certified["packages"][0]["review_implementation_hash"],
                review_implementation()["aggregate_hash"],
            )
            self.assertEqual(
                certified["legacy_v8_role"],
                "IDENTITY_ORDER_SOURCE_BINDING_BASELINE_ONLY",
            )

    def test_certifier_rejects_legacy_pass_without_evidence_contract(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            batch = base / "batch"
            output = base / "certified"
            write_legacy_pass_batch(batch)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(CERTIFIER),
                    "--batch",
                    str(batch),
                    "--output",
                    str(output),
                    "--expected-count",
                    "1",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("evidence contract", completed.stderr.lower())
            self.assertFalse(output.exists())

    def test_certifier_rejects_stale_review_implementation_hash(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            batch = base / "batch"
            output = base / "certified"
            write_evidence_pass_batch(batch)
            index = json.loads(
                (batch / "index.json").read_text(encoding="utf-8")
            )
            identity = index["records"][0]["evidence"]["source_binding"][
                "cli_audit_identity"
            ]
            manifest_path = batch / identity["manifest_path"]
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["review_implementation"]["files"][
                "scripts/run_review.py"
            ] = "sha256:stale"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            refresh_evidence_bindings(batch)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(CERTIFIER),
                    "--batch",
                    str(batch),
                    "--output",
                    str(output),
                    "--expected-count",
                    "1",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("stale review implementation", completed.stderr.lower())
            self.assertFalse(output.exists())

    def test_certifier_rejects_old_four_class_probe_report(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            batch = base / "batch"
            output = base / "certified"
            write_evidence_pass_batch(batch)
            index = json.loads(
                (batch / "index.json").read_text(encoding="utf-8")
            )
            identity = index["records"][0]["evidence"]["source_binding"][
                "cli_audit_identity"
            ]
            checker_path = (
                batch / identity["report_path"]
            ).with_name("checker_tests.json")
            checker = json.loads(checker_path.read_text(encoding="utf-8"))
            checker["probe_coverage"].pop("component_isolation")
            checker["probe_coverage"].pop("task_family_attacks")
            checker_path.write_text(json.dumps(checker), encoding="utf-8")
            refresh_evidence_bindings(batch)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(CERTIFIER),
                    "--batch",
                    str(batch),
                    "--output",
                    str(output),
                    "--expected-count",
                    "1",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("probe provenance is incomplete", completed.stderr.lower())
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
