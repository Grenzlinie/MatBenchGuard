from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CERTIFIER = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
    / "certify_final_100.py"
)
REVIEW_SKILL_ROOT = (
    REPO_ROOT / ".cursor/skills/materials-benchmark-review"
)
def canonical_hash(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def run_certifier(
    batch: Path, output: Path, *, expected_count: int = 1
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(CERTIFIER),
            "--batch",
            str(batch),
            "--output",
            str(output),
            "--expected-count",
            str(expected_count),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def review_implementation() -> dict[str, Any]:
    implementation_manifest = json.loads(
        (
            REVIEW_SKILL_ROOT
            / "references/review-implementation-files.json"
        ).read_text(encoding="utf-8")
    )
    files = {
        relative: file_hash(REVIEW_SKILL_ROOT / relative)
        for relative in implementation_manifest["files"]
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
        "role_conflicts": [],
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
            "process_evidence_policy": {
                "status": "NOT_APPLICABLE",
                "reason": (
                    "process evidence is not a dynamic fixture or "
                    "checker-probe target"
                ),
                "files": {},
                "instrumentation": "NONE",
                "provenance": {
                    "source_kind": "NONE",
                    "oracle_used": False,
                },
            },
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
        "runtime_provenance": {
            "status": "ASSESSED",
            "entrypoint": "tests/test.sh",
            "execution_mode": "ISOLATED_REBASED_HARBOR_VERIFIER",
            "cases_executed": 2,
        },
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
                "subcoverage": {
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
            },
            "discrimination": {
                "status": "NOT_ASSESSABLE",
                "reason": "no independent public fixture",
                "provenance": {
                    "source_kind": "NONE",
                    "fixture_hashes": {},
                    "oracle_used": False,
                },
            },
            "equivalence": {
                "status": "NOT_ASSESSABLE",
                "reason": "no independent public fixture",
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
    upgrade_synthetic_certification_fixture(batch)


def upgrade_synthetic_certification_fixture(batch: Path) -> None:
    """Create all certifier inputs inside the test-owned temp directory."""
    index_path = batch / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    record = index["records"][0]
    identity = record["evidence"]["source_binding"]["cli_audit_identity"]
    report_path = batch / identity["report_path"]
    manifest_path = batch / identity["manifest_path"]
    checker_path = report_path.with_name("checker_tests.json")
    disposition_path = report_path.with_name("disposition.json")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    canonical = {
        "review_verdict": "PASS",
        "publishability": "PUBLISH_CANDIDATE",
        "repair_decision": "NOT_REQUIRED",
        "repair_status": "NOT_APPLICABLE",
    }
    report.update(canonical)
    report["configuration"] = {
        "paper_mode": "no_paper",
        "execution_level": "E1",
    }
    report["summary"].update(canonical)
    report["summary"].update(
        {
            "final_verdict": "PASS",
            "disposition": "PUBLISH_CANDIDATE",
            "scoring_version": "materials-review-scoring/1.0",
            "total_score": 97,
            "hard_gate_triggered": False,
        }
    )
    report["evidence_contract"] = {
        "version": "materials-evidence-contract/1.0",
        "fail_closed": True,
        "gaps": [],
    }
    report["scope"] = {
        "solution_content_inspected": False,
        "solution_oracle_executed": True,
    }
    report["audit_binding"] = {
        "parent_audit_id": None,
        "source_hashes": {},
        "implementation_hash": None,
    }
    report["source_bindings"] = {
        "fixture_hashes": {},
        "assessment_hashes": {},
        "core_contract_digest": "sha256:" + "1" * 64,
    }
    report["gold_provenance"] = {
        "status": "ASSESSED",
        "mode": "no_paper",
        "oracle_used": False,
        "provenance": {"source_kind": "INDEPENDENT_PUBLIC_FIXTURE"},
    }
    report["qa_axes"] = {
        axis: {
            "status": "PASS",
            "evidence": [
                {
                    "source": "instruction.md",
                    "fact": f"{axis} assessed",
                    "semantic": "supports_pass",
                }
            ],
            "locations": [
                {
                    "file": "instruction.md",
                    "line": 1,
                    "quote": "crystal",
                }
            ],
            "limitations": [],
        }
        for axis in (
            "factual_accuracy",
            "answer_leakage",
            "instruction_completeness",
            "checker_instruction_consistency",
        )
    }
    report["dimension_scores"] = [
        {
            "dimension": name,
            "max_points": maximum,
            "points_earned": (
                12 if name == "robustness_discrimination" else maximum
            ),
            "normalized_score": round(
                (12 if name == "robustness_discrimination" else maximum)
                / maximum,
                6,
            ),
            "status": "PASS",
            "evidence": [{"fact": f"{name} assessed"}],
        }
        for name, maximum in (
            ("scientific_validity", 35),
            ("instruction_answerability", 20),
            ("checker_gold_alignment", 25),
            ("robustness_discrimination", 15),
            ("solution_completeness", 5),
        )
    ]
    report["hard_gates"] = [
        {
            "code": code,
            "status": "PASS",
            "evidence": [{"fact": "gate assessed"}],
            "affected_locations": [
                {"file": "instruction.md", "line": 1, "quote": "crystal"}
            ],
        }
        for code in (
            "NON_MATERIALS_TASK",
            "SCIENTIFIC_TARGET_INVALID",
            "CHECKER_CORE_TASK_UNASSESSED",
            "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
        )
    ]
    report["paper_trigger_adjudication"] = [
        {
            "trigger": trigger,
            "status": "NOT_TRIGGERED",
            "evidence": [{"package_file": "instruction.md", "package_quote": "crystal"}],
        }
        for trigger in (
            "SCIENTIFIC_CONFLICT",
            "NECESSARY_INFORMATION_MISSING",
            "GOLD_PROVENANCE_UNCERTAIN",
            "EXPLICIT_REPRODUCTION_CLAIM",
        )
    ]
    checker["solution_content_inspected"] = False
    checker["solution_oracle"].update(
        {
            "used": True,
            "status": "PASS",
            "positive_mock_available": True,
            "attempted": True,
            "setup_attempted": True,
            "setup_prepared": True,
            "producer_started": True,
            "executed": True,
            "scientific_evidence": False,
        }
    )
    checker["probe_coverage"]["positive"]["provenance"].update(
        {"oracle_used": True}
    )
    checker["probe_coverage"]["negative"]["provenance"]["oracle_used"] = False
    checker["probe_coverage"]["discrimination"]["provenance"]["oracle_used"] = False
    checker["probe_coverage"]["equivalence"]["provenance"]["oracle_used"] = False
    checker["probe_coverage"]["component_isolation"]["provenance"][
        "oracle_used"
    ] = False
    source = batch.parent / "source" / record["source_relative_path"]
    (source / "tests").mkdir(parents=True, exist_ok=True)
    (source / "instruction.md").write_text(
        "Compute the crystal result.\n", encoding="utf-8"
    )
    (source / "tests/checker.py").write_text(
        "print('checker')\n", encoding="utf-8"
    )
    (source / "tests/grading_spec.json").write_text(
        "{}\n", encoding="utf-8"
    )
    (source / "tests/test.sh").write_text(
        "exit 0\n", encoding="utf-8"
    )
    source_hashes = {
        relative: file_hash(source / relative)
        for relative in (
            "instruction.md",
            "tests/checker.py",
            "tests/grading_spec.json",
            "tests/test.sh",
        )
    }
    manifest.update(
        {
            **canonical,
            "execution_level": "E1",
            "parent_audit_id": None,
            "input_hashes": source_hashes,
            "review_implementation": review_implementation(),
            "output_hashes": {},
        }
    )
    report["audit_binding"] = {
        "parent_audit_id": None,
        "source_hashes": source_hashes,
        "implementation_hash": manifest["review_implementation"][
            "aggregate_hash"
        ],
    }
    report["source_bindings"]["core_contract_digest"] = "sha256:" + "1" * 64
    report_path.write_text(json.dumps(report), encoding="utf-8")
    checker_path.write_text(json.dumps(checker), encoding="utf-8")
    disposition_path.write_text(
        json.dumps(
            {
                **canonical,
                "audit_id": report["audit_id"],
                "route": "PUBLISH_CANDIDATE",
                "verdict": "PASS",
            }
        ),
        encoding="utf-8",
    )
    manifest["output_hashes"] = {
        "audit_report.json": file_hash(report_path),
        "checker_tests.json": file_hash(checker_path),
        "disposition.json": file_hash(disposition_path),
    }
    manifest["bundle_hash"] = canonical_hash(manifest["output_hashes"])
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    record.update(canonical)
    record["selection_rank"] = 0
    record["global_rank"] = 1
    record["evidence"]["source_binding"]["source_path"] = str(source)
    record["evidence"]["source_binding"]["source_role_hashes"] = source_hashes
    record["evidence"]["cli_evidence"].update(
        {
            "stage_binding": {
                "status": "NO_PAPER_ONLY",
                "no_paper_audit_id": None,
                "paper_grounded_audit_id": None,
            },
            "review_implementation": manifest["review_implementation"],
            "audit_bundle_hash": manifest["bundle_hash"],
            "report_hash": file_hash(report_path),
            "manifest_hash": file_hash(manifest_path),
            "checker_tests_hash": file_hash(checker_path),
        }
    )
    record["evidence"]["cli_evidence"]["snapshot_hash"] = canonical_hash(
        {
            key: value
            for key, value in record["evidence"]["cli_evidence"].items()
            if key != "snapshot_hash"
        }
    )
    index.update(
        {
            "schema_version": "materials-final-100-index/1.0",
            "selection_policy": {
                "ordering": "deterministic_selected_prefix",
                "universe_path": "ordered_universe.json",
            },
        }
    )
    universe = {
        "schema_version": "materials-final-100-universe/1.0",
        "records": [
            {
                "global_rank": 1,
                "package_id": record["package_id"],
                "eligible": True,
                "review_verdict": "PASS",
            }
        ],
    }
    universe_path = batch / "ordered_universe.json"
    universe_path.write_text(json.dumps(universe), encoding="utf-8")
    index["selection_policy"]["universe_hash"] = file_hash(universe_path)
    index["records"] = [record]
    index_path.write_text(json.dumps(index), encoding="utf-8")
    refresh_evidence_bindings(batch)


def upgrade_synthetic_repaired_fixture(batch: Path) -> None:
    upgrade_synthetic_certification_fixture(batch)
    index_path = batch / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    record = index["records"][0]
    identity = record["evidence"]["source_binding"]["cli_audit_identity"]
    report_path = batch / identity["report_path"]
    manifest_path = batch / identity["manifest_path"]
    disposition_path = report_path.with_name("disposition.json")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    disposition = json.loads(disposition_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    canonical = {
        "review_verdict": "PASS",
        "publishability": "PUBLISH_CANDIDATE",
        "repair_decision": "AUTO_FIX",
        "repair_status": "PUBLISHED",
    }
    report.update(canonical)
    report["summary"].update(canonical)
    disposition.update(canonical)
    report_path.write_text(json.dumps(report), encoding="utf-8")
    disposition_path.write_text(json.dumps(disposition), encoding="utf-8")
    manifest["output_hashes"]["audit_report.json"] = file_hash(report_path)
    manifest["output_hashes"]["disposition.json"] = file_hash(disposition_path)
    manifest["bundle_hash"] = canonical_hash(manifest["output_hashes"])
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    repair_dir = batch / "repair-bundle"
    repair_dir.mkdir()
    changes = [
        {
            "operation_id": "op-1",
            "file": "instruction.md",
            "operation": "replace_text",
            "before_hash": "sha256:" + "1" * 64,
            "after_hash": "sha256:" + "2" * 64,
            "evidence_ids": ["evidence-1"],
        }
    ]
    json_files = {
        "repair_plan.json": {
            **canonical,
            "schema_version": "0.1",
            "audit_id": identity["audit_id"],
            "finding_id": "FINDING-001",
            "justification": "Synthetic evidence-backed repair.",
            "repair_class": "AUTO_FIX",
            "operations": [{"id": "op-1", "type": "replace_text"}],
            "regression_tests": [{"id": "regression-1", "type": "command"}],
        },
        "changes.json": changes,
        "unresolved.json": [],
        "regression_results.json": [
            {
                "specification": {
                    "id": "regression-1",
                    "type": "command",
                },
                "before_passed": False,
                "after_passed": True,
            }
        ],
        "re_audit_comparison.json": {
            "target_resolved": True,
            "reaudit_audit_id": report["audit_id"],
            "source_finding": {
                "finding_id": "FINDING-001",
                "status": "OPEN",
            },
            "source_configuration": {
                "paper_mode": "no_paper",
                "execution_level": "E1",
            },
            "reaudit_configuration": {
                "paper_mode": "no_paper",
                "execution_level": "E1",
            },
        },
        "patch.json": {
            "schema_version": "0.1",
            "files": changes,
            "atomic_publish": True,
        },
        "evidence.json": [
            {
                "evidence_id": "evidence-1",
                "source": "synthetic-independent-evidence",
            }
        ],
    }
    for name, value in json_files.items():
        (repair_dir / name).write_text(json.dumps(value), encoding="utf-8")
    (repair_dir / "repair.log").write_text(
        "INFO decision=AUTO_FIX status=PUBLISHED\n", encoding="utf-8"
    )
    bundle_hashes = {
        name: file_hash(repair_dir / name)
        for name in (
            "repair_plan.json",
            "changes.json",
            "unresolved.json",
            "regression_results.json",
            "re_audit_comparison.json",
            "patch.json",
            "evidence.json",
            "repair.log",
        )
    }
    history = {
        **canonical,
        "root_cause": "synthetic-root-cause",
        "attempt_number": 1,
        "status": "PUBLISHED",
        "decision": "AUTO_FIX",
        "bundle_complete": True,
        "bundle_files": [
            "repair_plan.json",
            "changes.json",
            "unresolved.json",
            "regression_results.json",
            "re_audit_comparison.json",
            "patch.json",
            "evidence.json",
            "repair.log",
            "history.json",
        ],
        "bundle_hashes": bundle_hashes,
        "bundle_digest": canonical_hash(bundle_hashes),
    }
    (repair_dir / "history.json").write_text(
        json.dumps(history), encoding="utf-8"
    )
    repair_manifest = {
        **canonical,
        "schema_version": "0.1",
        "source_audit_id": identity["audit_id"],
        "repair_id": "synthetic-repair",
    }
    repair_manifest_path = batch / "repair-manifest.json"
    repair_manifest_path.write_text(
        json.dumps(repair_manifest), encoding="utf-8"
    )
    record.update(canonical)
    record["evidence"]["repair_binding"] = {
        "repair_manifest_path": repair_manifest_path.relative_to(batch).as_posix(),
        "bundle_path": repair_dir.relative_to(batch).as_posix(),
        "reaudit_report_path": report_path.relative_to(batch).as_posix(),
    }
    record["evidence"]["cli_evidence"].update(
        {
            "audit_bundle_hash": manifest["bundle_hash"],
            "report_hash": file_hash(report_path),
            "manifest_hash": file_hash(manifest_path),
        }
    )
    record["evidence"]["cli_evidence"]["snapshot_hash"] = canonical_hash(
        {
            key: value
            for key, value in record["evidence"]["cli_evidence"].items()
            if key != "snapshot_hash"
        }
    )
    index["records"] = [record]
    index_path.write_text(json.dumps(index), encoding="utf-8")


def refresh_evidence_bindings(batch: Path) -> None:
    index_path = batch / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    record = index["records"][0]
    identity = record["evidence"]["source_binding"]["cli_audit_identity"]
    report_path = batch / identity["report_path"]
    manifest_path = batch / identity["manifest_path"]
    checker_path = report_path.with_name("checker_tests.json")
    disposition_path = report_path.with_name("disposition.json")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    checker = json.loads(checker_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["output_hashes"]["audit_report.json"] = file_hash(report_path)
    manifest["output_hashes"]["checker_tests.json"] = file_hash(checker_path)
    manifest["output_hashes"]["disposition.json"] = file_hash(disposition_path)
    manifest["bundle_hash"] = canonical_hash(manifest["output_hashes"])
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    scoring = {
        "scoring_version": report["summary"]["scoring_version"],
        "final_verdict": report["summary"]["final_verdict"],
        "hard_gate_triggered": report["summary"]["hard_gate_triggered"],
        "dimension_scores": report["dimension_scores"],
        "hard_gates": report["hard_gates"],
    }
    if "total_score" in report["summary"]:
        scoring["total_score"] = report["summary"]["total_score"]
    scoring["snapshot_hash"] = canonical_hash(scoring)
    record["evidence"]["cli_scoring"] = scoring
    identity["scoring_snapshot_hash"] = scoring["snapshot_hash"]
    cli_evidence = record["evidence"]["cli_evidence"]
    cli_evidence["probe_coverage"] = checker.get("probe_coverage", {})
    cli_evidence["review_implementation"] = manifest.get(
        "review_implementation"
    )
    cli_evidence["report_hash"] = file_hash(report_path)
    cli_evidence["manifest_hash"] = file_hash(manifest_path)
    cli_evidence["checker_tests_hash"] = file_hash(checker_path)
    cli_evidence["audit_bundle_hash"] = manifest["bundle_hash"]
    cli_evidence["snapshot_hash"] = canonical_hash(
        {
            key: value
            for key, value in cli_evidence.items()
            if key != "snapshot_hash"
        }
    )
    index_path.write_text(json.dumps(index), encoding="utf-8")


def fixture_paths(batch: Path) -> tuple[Path, Path, Path, Path]:
    index = json.loads((batch / "index.json").read_text(encoding="utf-8"))
    identity = index["records"][0]["evidence"]["source_binding"][
        "cli_audit_identity"
    ]
    report = batch / identity["report_path"]
    manifest = batch / identity["manifest_path"]
    return (
        report,
        manifest,
        report.with_name("checker_tests.json"),
        report.with_name("disposition.json"),
    )


def rewrite_repair_hashes(batch: Path) -> None:
    repair_dir = batch / "repair-bundle"
    history_path = repair_dir / "history.json"
    history = json.loads(history_path.read_text(encoding="utf-8"))
    history["bundle_hashes"] = {
        name: file_hash(repair_dir / name)
        for name in history["bundle_files"]
        if name != "history.json"
    }
    history["bundle_digest"] = canonical_hash(history["bundle_hashes"])
    history_path.write_text(json.dumps(history), encoding="utf-8")


def upgrade_synthetic_paper_fixture(batch: Path) -> None:
    report_path, manifest_path, _, _ = fixture_paths(batch)
    index_path = batch / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    record = index["records"][0]
    report = json.loads(report_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    parent_id = "audit-parent-no-paper"
    parent_dir = batch / "cli_reports" / "parent-no-paper"
    shutil.copytree(report_path.parent, parent_dir)
    parent_report_path = parent_dir / "audit_report.json"
    parent_manifest_path = parent_dir / "audit_manifest.json"
    parent_report = json.loads(
        parent_report_path.read_text(encoding="utf-8")
    )
    parent_manifest = json.loads(
        parent_manifest_path.read_text(encoding="utf-8")
    )
    parent_report["audit_id"] = parent_id
    parent_report["configuration"] = {
        "paper_mode": "no_paper",
        "execution_level": "E1",
    }
    parent_report["audit_binding"]["parent_audit_id"] = None
    parent_manifest["audit_id"] = parent_id
    parent_manifest["parent_audit_id"] = None
    parent_report_path.write_text(json.dumps(parent_report), encoding="utf-8")
    parent_disposition_path = parent_dir / "disposition.json"
    parent_disposition = json.loads(
        parent_disposition_path.read_text(encoding="utf-8")
    )
    parent_disposition["audit_id"] = parent_id
    parent_disposition_path.write_text(
        json.dumps(parent_disposition), encoding="utf-8"
    )
    parent_manifest["output_hashes"] = {
        name: file_hash(parent_dir / name)
        for name in parent_manifest["output_hashes"]
    }
    parent_manifest["bundle_hash"] = canonical_hash(
        parent_manifest["output_hashes"]
    )
    parent_report_path.write_text(json.dumps(parent_report), encoding="utf-8")
    parent_manifest_path.write_text(
        json.dumps(parent_manifest), encoding="utf-8"
    )
    report["configuration"]["paper_mode"] = "paper_grounded"
    report["audit_binding"]["parent_audit_id"] = parent_id
    manifest["parent_audit_id"] = parent_id
    report_path.write_text(json.dumps(report), encoding="utf-8")
    manifest["output_hashes"]["audit_report.json"] = file_hash(report_path)
    manifest["bundle_hash"] = canonical_hash(manifest["output_hashes"])
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    stage = {
        "status": "PAPER_GROUNDED_BOUND_TO_NO_PAPER",
        "no_paper_audit_id": parent_id,
        "paper_grounded_audit_id": report["audit_id"],
        "no_paper_package_id": record["package_id"],
        "no_paper_report_path": parent_report_path.relative_to(batch).as_posix(),
        "no_paper_report_hash": file_hash(parent_report_path),
        "no_paper_manifest_path": parent_manifest_path.relative_to(
            batch
        ).as_posix(),
        "no_paper_manifest_hash": file_hash(parent_manifest_path),
        "source_role_hashes": manifest["input_hashes"],
        "review_implementation_hash": manifest["review_implementation"][
            "aggregate_hash"
        ],
    }
    record["evidence"]["cli_evidence"]["stage_binding"] = stage
    record["evidence"]["cli_evidence"]["audit_bundle_hash"] = manifest[
        "bundle_hash"
    ]
    record["evidence"]["cli_evidence"]["report_hash"] = file_hash(report_path)
    record["evidence"]["cli_evidence"]["manifest_hash"] = file_hash(
        manifest_path
    )
    record["evidence"]["cli_evidence"]["snapshot_hash"] = canonical_hash(
        {
            key: value
            for key, value in record["evidence"]["cli_evidence"].items()
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
                certified["schema_version"], "materials-final-100-index/1.0"
            )
            self.assertEqual(
                certified["selection_policy"],
                {
                    "ordering": "deterministic_selected_prefix",
                    "selected_prefix": 1,
                    "first_n_deterministic": True,
                },
            )
            self.assertEqual(
                {
                    key: certified["packages"][0][key]
                    for key in (
                        "review_verdict",
                        "publishability",
                        "repair_decision",
                        "repair_status",
                    )
                },
                {
                    "review_verdict": "PASS",
                    "publishability": "PUBLISH_CANDIDATE",
                    "repair_decision": "NOT_REQUIRED",
                    "repair_status": "NOT_APPLICABLE",
                },
            )
            self.assertEqual(
                certified["packages"][0]["review_implementation_hash"],
                review_implementation()["aggregate_hash"],
            )
            self.assertEqual(
                certified["legacy_v8_role"],
                "IDENTITY_ORDER_SOURCE_BINDING_BASELINE_ONLY",
            )

    def test_certifier_accepts_repaired_pass_with_bound_history(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            batch = base / "batch"
            output = base / "certified"
            write_evidence_pass_batch(batch)
            upgrade_synthetic_repaired_fixture(batch)

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
            self.assertEqual(
                certified["packages"][0]["repair_decision"], "AUTO_FIX"
            )
            self.assertEqual(
                certified["packages"][0]["repair_status"], "PUBLISHED"
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

    def test_certifier_rejects_missing_pass_score(self) -> None:
        mutations = {
            "missing": lambda summary: summary.pop("total_score"),
            "non_numeric": lambda summary: summary.update(
                {"total_score": "97"}
            ),
            "out_of_bounds": lambda summary: summary.update(
                {"total_score": 101}
            ),
            "below_pass_threshold": lambda summary: summary.update(
                {"total_score": 79}
            ),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as temporary:
                batch = Path(temporary) / "batch"
                output = Path(temporary) / "certified"
                write_evidence_pass_batch(batch)
                report_path, _, _, _ = fixture_paths(batch)
                report = json.loads(report_path.read_text(encoding="utf-8"))
                mutate(report["summary"])
                report_path.write_text(json.dumps(report), encoding="utf-8")
                refresh_evidence_bindings(batch)

                completed = run_certifier(batch, output)

                self.assertNotEqual(completed.returncode, 0)
                self.assertIn("score", completed.stderr.lower())
                self.assertFalse(output.exists())

    def test_certifier_rejects_failed_hard_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary) / "batch"
            output = Path(temporary) / "certified"
            write_evidence_pass_batch(batch)
            report_path, _, _, _ = fixture_paths(batch)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["hard_gates"][0]["status"] = "FAIL"
            report_path.write_text(json.dumps(report), encoding="utf-8")
            refresh_evidence_bindings(batch)

            completed = run_certifier(batch, output)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("hard gate", completed.stderr.lower())

    def test_certifier_rejects_malformed_qa_probe_and_oracle(self) -> None:
        mutations = {
            "qa": lambda report, checker: report["qa_axes"][
                "factual_accuracy"
            ].pop("locations"),
            "probe": lambda report, checker: checker["probe_coverage"][
                "negative"
            ].update({"status": "UNKNOWN"}),
            "oracle": lambda report, checker: checker["solution_oracle"].update(
                {"raw_scientific_value": "SECRET-ORACLE-VALUE"}
            ),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as temporary:
                batch = Path(temporary) / "batch"
                output = Path(temporary) / "certified"
                write_evidence_pass_batch(batch)
                report_path, _, checker_path, _ = fixture_paths(batch)
                report = json.loads(report_path.read_text(encoding="utf-8"))
                checker = json.loads(checker_path.read_text(encoding="utf-8"))
                mutate(report, checker)
                report_path.write_text(json.dumps(report), encoding="utf-8")
                checker_path.write_text(json.dumps(checker), encoding="utf-8")
                refresh_evidence_bindings(batch)

                completed = run_certifier(batch, output)

                self.assertNotEqual(completed.returncode, 0)
                self.assertFalse(output.exists())

    def test_certifier_rejects_fabricated_paper_parent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary) / "batch"
            output = Path(temporary) / "certified"
            write_evidence_pass_batch(batch)
            upgrade_synthetic_paper_fixture(batch)
            index_path = batch / "index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            stage = index["records"][0]["evidence"]["cli_evidence"][
                "stage_binding"
            ]
            parent_report_path = batch / stage["no_paper_report_path"]
            parent_manifest_path = batch / stage["no_paper_manifest_path"]
            parent_manifest = json.loads(
                parent_manifest_path.read_text(encoding="utf-8")
            )
            parent_report_path.write_text(
                json.dumps(
                    {
                        "audit_id": stage["no_paper_audit_id"],
                        "configuration": {
                            "paper_mode": "no_paper",
                            "execution_level": "E1",
                        },
                        "audit_binding": {
                            "parent_audit_id": None,
                            "source_hashes": stage["source_role_hashes"],
                            "implementation_hash": stage[
                                "review_implementation_hash"
                            ],
                        },
                    }
                ),
                encoding="utf-8",
            )
            parent_manifest_path.write_text(
                json.dumps(
                    {
                        "audit_id": stage["no_paper_audit_id"],
                        "parent_audit_id": None,
                        "input_hashes": stage["source_role_hashes"],
                        "review_implementation": parent_manifest[
                            "review_implementation"
                        ],
                        "execution_level": "E1",
                    }
                ),
                encoding="utf-8",
            )
            stage["no_paper_report_hash"] = file_hash(parent_report_path)
            stage["no_paper_manifest_hash"] = file_hash(parent_manifest_path)
            cli_evidence = index["records"][0]["evidence"]["cli_evidence"]
            cli_evidence["snapshot_hash"] = canonical_hash(
                {
                    key: value
                    for key, value in cli_evidence.items()
                    if key != "snapshot_hash"
                }
            )
            index_path.write_text(json.dumps(index), encoding="utf-8")

            completed = run_certifier(batch, output)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("parent", completed.stderr.lower())

    def test_certifier_accepts_real_paper_parent_binding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary) / "batch"
            output = Path(temporary) / "certified"
            write_evidence_pass_batch(batch)
            upgrade_synthetic_paper_fixture(batch)

            completed = run_certifier(batch, output)

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)

    def test_certifier_rejects_null_publishability(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary) / "batch"
            output = Path(temporary) / "certified"
            write_evidence_pass_batch(batch)
            index_path = batch / "index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["records"][0]["publishability"] = None
            index_path.write_text(json.dumps(index), encoding="utf-8")
            report_path, manifest_path, _, disposition_path = fixture_paths(batch)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            disposition = json.loads(disposition_path.read_text(encoding="utf-8"))
            report["publishability"] = None
            disposition["publishability"] = None
            report_path.write_text(json.dumps(report), encoding="utf-8")
            disposition_path.write_text(
                json.dumps(disposition), encoding="utf-8"
            )
            refresh_evidence_bindings(batch)

            completed = run_certifier(batch, output)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("canonical", completed.stderr.lower())

    def test_certifier_rejects_duplicate_global_rank_and_audit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary) / "batch"
            output = Path(temporary) / "certified"
            write_evidence_pass_batch(batch)
            index_path = batch / "index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            duplicate = json.loads(json.dumps(index["records"][0]))
            duplicate["package_id"] = "cluster-2/theme/paper-2"
            duplicate["source_relative_path"] = duplicate["package_id"]
            duplicate["selection_rank"] = 1
            index["records"].append(duplicate)
            universe_path = batch / index["selection_policy"]["universe_path"]
            universe = json.loads(universe_path.read_text(encoding="utf-8"))
            universe["records"].append(
                {
                    "global_rank": 1,
                    "package_id": duplicate["package_id"],
                    "eligible": True,
                    "review_verdict": "PASS",
                }
            )
            universe_path.write_text(json.dumps(universe), encoding="utf-8")
            index["selection_policy"]["universe_hash"] = file_hash(universe_path)
            index_path.write_text(json.dumps(index), encoding="utf-8")

            completed = run_certifier(batch, output, expected_count=2)

            self.assertNotEqual(completed.returncode, 0)
            self.assertRegex(completed.stderr.lower(), "rank|audit")

    def test_certifier_rejects_duplicate_audit_across_packages(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary) / "batch"
            output = Path(temporary) / "certified"
            write_evidence_pass_batch(batch)
            index_path = batch / "index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            duplicate = json.loads(json.dumps(index["records"][0]))
            duplicate["package_id"] = "cluster-2/theme/paper-2"
            duplicate["source_relative_path"] = duplicate["package_id"]
            duplicate["selection_rank"] = 1
            duplicate["global_rank"] = 2
            index["records"].append(duplicate)
            universe_path = batch / index["selection_policy"]["universe_path"]
            universe = json.loads(universe_path.read_text(encoding="utf-8"))
            universe["records"].append(
                {
                    "global_rank": 2,
                    "package_id": duplicate["package_id"],
                    "eligible": True,
                    "review_verdict": "PASS",
                }
            )
            universe_path.write_text(json.dumps(universe), encoding="utf-8")
            index["selection_policy"]["universe_hash"] = file_hash(universe_path)
            index_path.write_text(json.dumps(index), encoding="utf-8")

            completed = run_certifier(batch, output, expected_count=2)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("audit", completed.stderr.lower())

    def test_certifier_rejects_later_replacement_for_earlier_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary) / "batch"
            output = Path(temporary) / "certified"
            write_evidence_pass_batch(batch)
            index_path = batch / "index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["records"][0]["global_rank"] = 2
            universe_path = batch / index["selection_policy"]["universe_path"]
            universe = {
                "schema_version": "materials-final-100-universe/1.0",
                "records": [
                    {
                        "global_rank": 1,
                        "package_id": "cluster-0/theme/paper-0",
                        "eligible": True,
                        "review_verdict": "PASS",
                    },
                    {
                        "global_rank": 2,
                        "package_id": index["records"][0]["package_id"],
                        "eligible": True,
                        "review_verdict": "PASS",
                    },
                ],
            }
            universe_path.write_text(json.dumps(universe), encoding="utf-8")
            index["selection_policy"]["universe_hash"] = file_hash(universe_path)
            index_path.write_text(json.dumps(index), encoding="utf-8")

            completed = run_certifier(batch, output)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("first", completed.stderr.lower())

    def test_certifier_rejects_empty_repair_plan_with_recomputed_hashes(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary) / "batch"
            output = Path(temporary) / "certified"
            write_evidence_pass_batch(batch)
            upgrade_synthetic_repaired_fixture(batch)
            (batch / "repair-bundle/repair_plan.json").write_text(
                "{}", encoding="utf-8"
            )
            rewrite_repair_hashes(batch)

            completed = run_certifier(batch, output)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("repair_plan", completed.stderr.lower())

    def test_certifier_rejects_symlink_source_file_or_parent(self) -> None:
        for label, parent_link in (("file", False), ("parent", True)):
            with self.subTest(label=label), tempfile.TemporaryDirectory() as temporary:
                base = Path(temporary)
                batch = base / "batch"
                output = base / "certified"
                write_evidence_pass_batch(batch)
                index_path = batch / "index.json"
                index = json.loads(index_path.read_text(encoding="utf-8"))
                binding = index["records"][0]["evidence"]["source_binding"]
                source = Path(binding["source_path"])
                if parent_link:
                    alias_parent = base / "source-parent-link"
                    os.symlink(source.parent, alias_parent)
                    binding["source_path"] = str(alias_parent / source.name)
                else:
                    alias = base / "source-link"
                    os.symlink(source, alias)
                    binding["source_path"] = str(alias)
                index_path.write_text(json.dumps(index), encoding="utf-8")

                completed = run_certifier(batch, output)

                self.assertNotEqual(completed.returncode, 0)
                self.assertIn("symlink", completed.stderr.lower())

    def test_fast_batch_docs_have_no_deleted_artifact_dependency(self) -> None:
        documentation = (
            REVIEW_SKILL_ROOT / "references/fast-e1-batch.md"
        ).read_text(encoding="utf-8")
        self.assertNotIn(
            "review_artifacts/materials_fast_e1_100", documentation
        )
        self.assertIn("scripts/certify_final_100.py", documentation)


if __name__ == "__main__":
    unittest.main()
