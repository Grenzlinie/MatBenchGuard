from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


review = load("core_review_v33", ROOT / ".cursor/skills/materials-benchmark-review/scripts/validate_core_review.py")
repair = load("core_repair_v23", ROOT / ".cursor/skills/materials-benchmark-repair/scripts/validate_core_repair.py")
probe_runner = load("probe_runner_v21", ROOT / ".cursor/skills/materials-benchmark-review/scripts/run_checker_probes.py")


def ev(path: str = "instruction.md", result: str = "verified") -> list[dict[str, str]]:
    return [{"path": path, "locator": "section", "result": result}]


def gates(codes: set[str], status: str = "PASS", path: str = "instruction.md") -> list[dict]:
    return [{"code": code, "status": status, "rationale": "verified", "evidence": ev(path)} for code in sorted(codes)]


def baseline_review(*, enhanced: bool = False) -> dict:
    value = {
        "schema_version": review.SCHEMA,
        "package_id": "cluster/theme/paper-1",
        "source_package": "materials_science_questions/material_v3_question/cluster/theme/paper-1",
        "reviewed_scope": ["instruction.md", "paper/paper.md", "manifest.json", "steps.json", "task.toml", "environment/**", "resources.json", "tests/**"],
        "instruction_contract": {
            "solver_visible_file": "instruction.md", "output_root": "/app/outputs",
            "required_headings": ["# Title", "## Problem background", "## Approach", "## Reproduction target", "## Assets", "## Workflow steps", "## Output files", "## Output contract", "## How you are scored"],
            "derived_files_consistent": True, "assets_use_generic_roles": True,
            "paper_reading_language_absent": True,
            "public_outputs": [{"path": "/app/outputs/result.csv", "format": "csv", "purpose": "scored", "contract_complete": True}],
            "required_condition_groups": [{"condition_group_id": "g1", "condition_signature": "paper system and condition", "public_identifier": "/app/outputs/result.csv:condition_group_id=g1"}],
        },
        "scientific_task_admission": {"status": "PASS", "computer_reproducible": True, "requires_physical_experiment": False, "failure_modes": [], "rationale": "non-trivial computational science", "evidence": ev()},
        "instruction_analysis": {
            "paper_parameter_coverage": {"status": "PASS", "evidence": ev("paper/paper.md")},
            "parameter_records": [
                {"canonical_id": "temperature", "symbol": "T", "meaning": "paper temperature", "value_or_range": "300", "unit": "K", "scope": "g1", "parameter_class": "PAPER_FIXED", "selection_policy": "PAPER_VALUE", "paper_reports_unique_value": True, "instruction_requires_unique_value": True, "checker_requires_unique_value": True, "source_locator": "paper/paper.md Results", "introduced_at": "instruction.md target", "used_at": ["Step 1"]},
                {"canonical_id": "mesh", "symbol": "mesh", "meaning": "numerical resolution", "value_or_range": "solver-converged", "unit": "dimensionless", "scope": "g1", "parameter_class": "SOLVER_SEARCHABLE", "selection_policy": "CONVERGENCE", "paper_reports_unique_value": False, "instruction_requires_unique_value": False, "checker_requires_unique_value": False, "source_locator": "paper/paper.md does not report a unique mesh", "introduced_at": "instruction.md workflow", "used_at": ["Step 1"]},
            ],
            "parameter_conflicts": [],
            "formula_step_records": [{"locator": "instruction.md Step 1", "kind": "WORKFLOW_STEP", "role": "REQUIRED_WORKFLOW_DEPENDENCY", "paper_supported": True, "action": "KEEP", "dependency_effect": "produces result", "rationale": "paper method", "evidence": ev("paper/paper.md")}],
            "workflow_continuity": {"status": "PASS", "evidence": ev()},
        },
        "resource_records": [],
        "question_correctness": {"status": "PASS", "gates": gates(review.QUESTION_GATES)},
        "answer_correctness": {
            "status": "PASS", "gates": gates(review.ANSWER_GATES, path="tests/checker.py"),
            "condition_group_records": [{"condition_group_id": "g1", "condition_signature": "paper system and condition", "public_identifier": "/app/outputs/result.csv:condition_group_id=g1", "required_target_ids": ["result"], "coverage_status": "PASS", "provenance": ev("paper/paper.md")}],
            "gold_records": [{"target_id": "result", "condition_group_ids": ["g1"], "role": "CORE", "policy": "PAPER_DIRECT", "comparison_kind": "NUMERIC", "value_or_relation": "1.25", "applicability": "g1 only", "units": "eV", "provenance": ev("paper/paper.md"), "independent_check": "paper table checked"}],
            "tolerance_records": [{"target_id": "result", "status": "EVIDENCED", "blocker_code": None, "units": "eV", "metric": "absolute_error", "atol": 0.01, "rtol": 0.0, "basis": "reported_precision", "evidence": ev("paper/paper.md"), "boundary_policy": "inclusive", "public_result": "/app/outputs/result.csv:value"}],
            "result_check_assessment": ([{"result_id": "residual", "action": "KEEP_RESULT_CHECK", "scientific_basis": "paper equation residual", "rationale": "cheap result-level invariant", "evidence": ev("tests/checker.py")} ] if enhanced else []),
        },
        "correctness_assessment": {"question_correct": True, "answer_correct": True, "core_outputs_covered": True, "correct_answer_accepted": True, "obviously_wrong_rejected": True, "rationale": "question and answer are paper-grounded", "evidence": ev("evidence/baseline.json")},
        "enhancement_assessment": {"status": "PASS" if enhanced else "NOT_ASSESSED", "minimal_result_checks": enhanced, "quality_gradient": enhanced, "risk_based_probes": enhanced, "baseline_preserved": enhanced, "weights": {"gold": 0.7 if enhanced else 1.0, "result_checks": 0.3 if enhanced else 0.0}},
        "checker_cost_record": {"hardware_class": "CPU", "cpu_cores": 1, "gpu_count": 0, "gpu_type": None, "measured_wall_seconds": 0.2, "peak_memory_mb": 30, "input_bytes_read": 2048, "uses_full_trajectory": False, "performs_new_simulation": False, "real_scale_input": True, "cost_rationale": "measured on full expected result.csv", "status": "PASS"},
        "operational_status": "PASS", "pass_threshold": 0.6,
        "probes": [], "findings": [], "rejection": None, "verdict": "PASS",
        "quality_tier": "RESULT_ENHANCED" if enhanced else "BASELINE_CORRECT",
        "publishable": True, "limitations": [],
    }
    probe_rewards = {
        "valid_positive": 1.0, "tolerance_boundary": 1.0,
        "missing_or_malformed": 0.0, "non_finite_and_duplicate": 0.0,
        "wrong_science": 0.0,
    }
    if enhanced:
        probe_rewards.update({"minimal_fabrication": 0.0, "quality_gradient": 0.7, "cross_condition_group_mismatch": 0.0})
    value["probes"] = [{"case_id": cls, "class": cls, "status": "PASS", "reward": reward, "expectation": "observed", "evidence_path": "evidence/probes.json"} for cls, reward in probe_rewards.items()]
    return value


def set_gate(value: dict, section: str, code: str, status: str) -> None:
    for item in value[section]["gates"]:
        if item["code"] == code:
            item["status"] = status
    value[section]["status"] = review.aggregate(value[section]["gates"])


class ReviewV33Tests(unittest.TestCase):
    def test_mesh_searchable_missing_unique_value_allows_baseline(self) -> None:
        value = baseline_review()
        self.assertEqual(review.validate(value)["quality_tier"], "BASELINE_CORRECT")

    def test_checker_cannot_secretly_fix_searchable_parameter(self) -> None:
        value = baseline_review()
        value["instruction_analysis"]["parameter_records"][1]["checker_requires_unique_value"] = True
        with self.assertRaisesRegex(ValueError, "must not secretly fix"):
            review.validate(value)

    def test_indispensable_asset_cannot_masquerade_as_searchable(self) -> None:
        value = baseline_review()
        value["instruction_analysis"]["parameter_records"][1].update({"parameter_class": "INDISPENSABLE_ASSET", "selection_policy": "CONVERGENCE"})
        with self.assertRaisesRegex(ValueError, "INDISPENSABLE_ASSET requires RESOURCE"):
            review.validate(value)

    def test_paper_defined_structure_can_be_built_without_a_cif_asset(self) -> None:
        value = baseline_review()
        value["instruction_analysis"]["parameter_records"].extend([
            {"canonical_id": "structure-definition", "symbol": "composition/space-group", "meaning": "paper-defined composition and crystal system", "value_or_range": "paper composition and space group", "unit": "not applicable", "scope": "g1", "parameter_class": "TARGET_DEFINING", "selection_policy": "PAPER_VALUE", "paper_reports_unique_value": True, "instruction_requires_unique_value": True, "checker_requires_unique_value": False, "source_locator": "paper/paper.md structure description", "introduced_at": "instruction.md structure definition", "used_at": ["Step 1"]},
            {"canonical_id": "atomic-realization", "symbol": "initial coordinates", "meaning": "solver-built atomic realization consistent with the paper description", "value_or_range": "solver justified and relaxed", "unit": "angstrom", "scope": "g1", "parameter_class": "SOLVER_SEARCHABLE", "selection_policy": "SOLVER_JUSTIFIED", "paper_reports_unique_value": False, "instruction_requires_unique_value": False, "checker_requires_unique_value": False, "source_locator": "paper/paper.md gives no unique CIF", "introduced_at": "instruction.md structure construction", "used_at": ["Step 1"]},
        ])
        self.assertEqual(value["resource_records"], [])
        self.assertEqual(review.validate(value)["verdict"], "PASS")

    def test_unavailable_indispensable_dataset_is_rejected(self) -> None:
        value = baseline_review()
        value["resource_records"] = [{"resource_id": "dataset", "kind": "DATASET", "indispensable": True, "delivery": "NONE", "locator": None, "equivalent_allowed": False, "availability": "UNAVAILABLE", "evidence": ev()}]
        set_gate(value, "question_correctness", "Q6_RESOURCE_SUFFICIENCY", "FAIL")
        value["answer_correctness"] = {"status": "NOT_ASSESSED", "gates": [], "condition_group_records": [], "gold_records": [], "tolerance_records": [], "result_check_assessment": []}
        value["correctness_assessment"].update({"question_correct": False, "answer_correct": False, "core_outputs_covered": False, "correct_answer_accepted": False, "obviously_wrong_rejected": False})
        value["probes"] = []
        value["findings"] = [{"finding_id": "F-ASSET", "layer": "QUESTION", "gate_codes": ["Q6_RESOURCE_SUFFICIENCY"], "severity": "FATAL", "route": "REJECT", "title": "dataset unavailable", "rationale": "no delivery or substitute", "evidence": ev()}]
        value["rejection"] = {"failure_modes": ["INDISPENSABLE_DATASET_UNAVAILABLE"], "reauthor_eligible": False, "rationale": "asset missing", "evidence": ev()}
        value.update({"verdict": "REJECTED", "quality_tier": None, "publishable": False})
        self.assertEqual(review.validate(value)["verdict"], "REJECTED")

    def test_baseline_does_not_require_checkpoint_or_enhancement_probes(self) -> None:
        value = baseline_review()
        self.assertEqual(value["answer_correctness"]["result_check_assessment"], [])
        self.assertTrue(review.validate(value)["publishable"])

    def test_lightweight_enhancement_passes(self) -> None:
        value = baseline_review(enhanced=True)
        self.assertEqual(review.validate(value)["quality_tier"], "RESULT_ENHANCED")

    def test_expensive_checker_preserves_scientific_pass_but_blocks_publish(self) -> None:
        value = baseline_review()
        value["checker_cost_record"].update({"measured_wall_seconds": 601, "status": "FAIL"})
        value.update({"operational_status": "FAIL", "publishable": False})
        value["findings"] = [{"finding_id": "F-COST", "layer": "OPERATIONAL", "gate_codes": [], "severity": "HIGH", "route": "REPAIR_CHECKER_COST", "title": "checker exceeds budget", "rationale": "601 seconds", "evidence": ev("evidence/cost.json")}]
        result = review.validate(value)
        self.assertEqual(result["verdict"], "PASS")
        self.assertFalse(result["publishable"])

    def test_full_trajectory_or_new_simulation_blocks_publish(self) -> None:
        for field in ("uses_full_trajectory", "performs_new_simulation"):
            with self.subTest(field=field):
                value = baseline_review()
                value["checker_cost_record"].update({field: True, "status": "FAIL"})
                value.update({"operational_status": "FAIL", "publishable": False})
                value["findings"] = [{"finding_id": "F-COST", "layer": "OPERATIONAL", "gate_codes": [], "severity": "HIGH", "route": "REPAIR_CHECKER_COST", "title": "forbidden checker work", "rationale": field, "evidence": ev("evidence/cost.json")}]
                self.assertFalse(review.validate(value)["publishable"])

    def test_real_scale_measurement_is_required(self) -> None:
        value = baseline_review()
        value["checker_cost_record"]["real_scale_input"] = False
        with self.assertRaisesRegex(ValueError, "status is inconsistent"):
            review.validate(value)

    def test_gpu_budget_accepts_one_recorded_gpu_and_rejects_multiple(self) -> None:
        value = baseline_review()
        value["checker_cost_record"].update({"hardware_class": "SINGLE_GPU", "gpu_count": 1, "gpu_type": "A100"})
        self.assertTrue(review.validate(value)["publishable"])
        value["checker_cost_record"]["gpu_count"] = 2
        value["checker_cost_record"]["status"] = "FAIL"
        with self.assertRaisesRegex(ValueError, "exactly one GPU"):
            review.validate(value)

    def test_probe_runner_declares_baseline_and_optional_classes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary)
            (package / "tests").mkdir()
            observed = probe_runner.run(package, {}, 1.0, execute=False)
        self.assertEqual(observed["schema_version"], "materials-checker-probe-observations/2.1")
        self.assertEqual(set(observed["probe_policy"]["baseline_required"]), review.BASELINE_PROBES)
        self.assertEqual(set(observed["probe_policy"]["enhancement_optional"]), review.ENHANCEMENT_PROBES)

    def test_package_aware_validation_rejects_weight_or_tolerance_drift(self) -> None:
        value = baseline_review(enhanced=True)
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary)
            (package / "tests").mkdir()
            spec = {"quality_tier": "RESULT_ENHANCED", "weights": {"gold": 0.6, "result_checks": 0.4}, "tolerance_contract": {"result": 0.01}}
            (package / "tests/grading_spec.json").write_text(json.dumps(spec), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "weights disagree"):
                review.validate_package_facts(value, package)
            spec["weights"] = {"gold": 0.7, "result_checks": 0.3}
            spec["tolerance_contract"]["result"] = 0.02
            (package / "tests/grading_spec.json").write_text(json.dumps(spec), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "tolerance records disagree"):
                review.validate_package_facts(value, package)


def repair_record(stage: str, candidate_review: dict, *, success: bool = True) -> dict:
    enhancement = stage == "RESULT_ENHANCEMENT"
    action = "ADD_MINIMAL_RESULT_CHECK" if enhancement else "MARK_SOLVER_SEARCHABLE"
    record = {
        "schema_version": repair.SCHEMA, "repair_stage": stage, "route": "REPAIR",
        "source_package": "source-package", "candidate_package": "candidate-package",
        "processing_root": "processing", "source_review": "source.json", "candidate_review": "candidate.json",
        "input_quality_tier": "BASELINE_CORRECT" if enhancement else None,
        "candidate_quality_tier": candidate_review.get("quality_tier"),
        "output_root": "/app/outputs", "source_unchanged": True,
        "scientific_target_preserved": True, "baseline_correctness_preserved": True,
        "reauthor_rationale": None, "derivation_order": repair.ORDER,
        "targets": [{"finding_id": "F-1", "action": action, "resolved": success, "rationale": "paper-backed staged repair"}],
        "changes": [{"finding_id": "F-1", "path": "tests/checker.py" if enhancement else "instruction.md", "before_sha256": "sha256:before", "after_sha256": "sha256:after", "evidence": "regression"}],
        "parameter_resolutions": [] if enhancement else [{"finding_id": "F-1", "canonical_id": "mesh", "before": "fixed", "after": "solver-converged", "paper_locator": "paper does not give unique mesh", "resolution": "remove guessed value", "parameter_class": "SOLVER_SEARCHABLE", "selection_policy": "CONVERGENCE", "introduced_external_value": False}],
        "guidance_changes": [], "resource_changes": [], "tolerance_changes": [], "condition_group_changes": [],
        "result_check_changes": ([{"finding_id": "F-1", "result_id": "residual", "action": "ADD_MINIMAL_RESULT_CHECK", "public_contract": "/app/outputs/result.csv:residual", "hidden_check": "cheap residual", "paper_or_invariant_basis": "paper equation", "cost_class": "CPU_LIGHT", "reads_full_trajectory": False, "reruns_primary_science": False}] if enhancement else []),
        "regressions": ([{"finding_id": "F-1", "case_id": "gold-only-quality", "mode": "QUALITY_GRADIENT", "specification": "Enhanced result checks reduce a Gold-only submission while preserving Baseline validity.", "baseline_reward": 1.0, "enhanced_reward": 0.7, "expected_relation": "enhanced_reward < baseline_reward", "evidence_path": "evidence/regression.json"}] if enhancement else [{"finding_id": "F-1", "case_id": "regression", "mode": "FAIL_BEFORE_PASS_AFTER", "specification": "fails before, passes after", "before_passed": False, "after_passed": True, "evidence_path": "evidence/regression.json"}]),
        "candidate_review_verdict": candidate_review["verdict"],
        "outcome": ("RESULT_ENHANCED" if enhancement else "BASELINE_REPAIRED") if success else "ROLLED_BACK",
        "publishable": True, "fallback_baseline_publishable": enhancement and not success,
        "published_candidate": "SOURCE_BASELINE" if enhancement and not success else "CANDIDATE",
        "limitations": [],
    }
    return record


class RepairV23Tests(unittest.TestCase):
    def validate_with_reviews(self, report: dict, source: dict, candidate: dict) -> dict:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "source.json").write_text(json.dumps(source), encoding="utf-8")
            (root / "candidate.json").write_text(json.dumps(candidate), encoding="utf-8")
            return repair.validate(report, report_path=root / "repair.json")

    def test_stage_b_requires_independently_reviewed_baseline(self) -> None:
        candidate = baseline_review(enhanced=True)
        report = repair_record("RESULT_ENHANCEMENT", candidate)
        source = baseline_review()
        self.assertEqual(self.validate_with_reviews(report, source, candidate)["outcome"], "RESULT_ENHANCED")

    def test_stage_b_cannot_read_full_trajectory(self) -> None:
        candidate = baseline_review(enhanced=True)
        report = repair_record("RESULT_ENHANCEMENT", candidate)
        report["result_check_changes"][0]["reads_full_trajectory"] = True
        with self.assertRaisesRegex(ValueError, "must not read full trajectories"):
            repair.validate(report)

    def test_failed_enhancement_publishes_source_baseline(self) -> None:
        source = baseline_review()
        candidate = copy.deepcopy(source)
        candidate["verdict"] = "REPAIR_REQUIRED"
        candidate["quality_tier"] = None
        candidate["correctness_assessment"]["answer_correct"] = False
        set_gate(candidate, "answer_correctness", "A5_CHECKER_ROBUSTNESS", "FAIL")
        candidate["findings"] = [{"finding_id": "F-ENH", "layer": "ANSWER", "gate_codes": ["A5_CHECKER_ROBUSTNESS"], "severity": "HIGH", "route": "REPAIR", "title": "enhancement regression", "rationale": "baseline was damaged", "evidence": ev("tests/checker.py")}]
        candidate["publishable"] = False
        report = repair_record("RESULT_ENHANCEMENT", candidate, success=False)
        result = self.validate_with_reviews(report, source, candidate)
        self.assertEqual(result["outcome"], "ROLLED_BACK")
        self.assertTrue(result["publishable"])
        self.assertEqual(result["published_candidate"], "SOURCE_BASELINE")


if __name__ == "__main__":
    unittest.main()
