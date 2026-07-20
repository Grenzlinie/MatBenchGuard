from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
)
REPAIR_SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
)
sys.path.insert(0, str(REVIEW_SCRIPTS))
sys.path.insert(0, str(REPAIR_SCRIPTS))

import d6_core_output_scoring as d6  # noqa: E402
import deterministic_contract  # noqa: E402
import run_repair  # noqa: E402


def static_inputs(
    *,
    checker_reads: str = "STATIC_GENERIC_LOADER_CANDIDATE",
    semantic_validation: str = "STATIC_CONTENT_READ_CANDIDATE",
    scorer_bound: bool = True,
    binding_status: str = "STATIC_SOURCE_BOUND",
    weight: float = 1.0,
) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    output = {
        "file": "result.json",
        "checker_reads": checker_reads,
        "semantic_validation": semantic_validation,
        "checker_scoring": {
            "step_id": "result",
            "declared_weight": weight,
            "scorer_bound": scorer_bound,
            "scorer_binding_status": binding_status,
        },
    }
    contract_map = {"core_outputs": ["result.json"]}
    checker_analysis = {
        "outputs": [output],
        "scorer_bindings": {"result": "score_result"}
        if scorer_bound
        else {},
        "scorer_status": {
            "result": {
                "status": "STATIC_RETURN_CANDIDATE",
                "return_status": "STATIC_RETURN_CANDIDATE",
            }
        },
    }
    grading = {
        "steps": [
            {"id": "result", "output_file": "result.json", "weight": weight}
        ]
    }
    return contract_map, checker_analysis, grading


class MaterialsIssue31D6Tests(unittest.TestCase):
    def test_complete_chain_reports_all_runtime_states(self) -> None:
        contract_map, checker_analysis, grading = static_inputs()
        result = d6.analyze(
            contract_map=contract_map,
            checker_analysis=checker_analysis,
            grading_contract=grading,
            checker_source=(
                "def load_artifact(path):\n"
                "    with open(path) as handle:\n"
                "        return handle.read()\n"
                "def score_result(artifact, step, ctx):\n"
                "    return 1.0\n"
                "_SCORERS = {'result': score_result}\n"
            ),
            checker_result={
                "tests": [
                    {
                        "case": "known_valid_public",
                        "reward": 1.0,
                        "breakdown": {
                            "result": {"score": 1.0, "weight": 1.0},
                            "_errors": {},
                        },
                    },
                    {
                        "case": "random_baseline",
                        "reward": 0.0,
                        "breakdown": {
                            "result": {"score": 0.0, "weight": 1.0},
                            "_errors": {},
                        },
                    },
                ]
            },
        )

        self.assertEqual(result["status"], d6.PROVEN)
        chain = result["core_outputs"][0]
        self.assertEqual(
            {
                chain["content_read"],
                chain["scorer_binding"],
                chain["positive_effective_weight"],
                chain["finite_return"],
                chain["final_reward"],
            },
            {d6.PROVEN},
        )
        self.assertEqual(chain["states"]["final_reward"], d6.PROVEN)

    def test_filename_and_existence_checks_are_not_content_reads(self) -> None:
        contract_map, checker_analysis, grading = static_inputs(
            checker_reads="STATIC_FILENAME_REFERENCE_ONLY",
            semantic_validation="EXISTENCE_ONLY",
        )
        result = d6.analyze(
            contract_map=contract_map,
            checker_analysis=checker_analysis,
            grading_contract=grading,
            checker_source=(
                "from pathlib import Path\n"
                "if Path('/app/outputs/result.json').exists():\n"
                "    pass\n"
            ),
        )

        chain = result["core_outputs"][0]
        self.assertEqual(chain["content_read"], d6.FAILED)
        self.assertEqual(
            result["findings"][0]["code"],
            "CHECKER_CORE_TASK_UNASSESSED",
        )

    def test_unique_scorer_wiring_is_explicitly_auto_fixable(self) -> None:
        contract_map, checker_analysis, grading = static_inputs(
            scorer_bound=False,
            binding_status="STATIC_NOT_BOUND",
        )
        result = d6.analyze(
            contract_map=contract_map,
            checker_analysis=checker_analysis,
            grading_contract=grading,
            checker_source=(
                "def score_result(artifact, step, ctx):\n"
                "    return 1.0\n"
                "_SCORERS = {}\n"
            ),
        )

        chain = result["core_outputs"][0]
        binding = chain["evidence"]["scorer_binding"]
        self.assertEqual(binding["repair_class"], "AUTO_FIX")
        self.assertEqual(binding["repair_scope"], "UNIQUE_SCORING_WIRING")
        self.assertTrue(binding["unique_wiring"])
        self.assertEqual(
            deterministic_contract.annotate_findings(
                [
                    {
                        "finding_id": "FINDING-001",
                        "title": "SCORING_COMPONENT_NOT_BOUND",
                        "status": "OPEN",
                        "repairable": True,
                        "evidence": {
                            "repair_class": "AUTO_FIX",
                            "repair_scope": "UNIQUE_SCORING_WIRING",
                            "unique_wiring": True,
                            "source_bound_unique_proof": binding[
                                "source_bound_unique_proof"
                            ],
                        },
                    }
                ]
            )[0]["deterministic_repair_class"],
            "AUTO_FIX",
        )

    def test_unique_wiring_auto_fix_can_target_checker_without_semantic_evidence(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            checker = root / "tests/checker.py"
            checker.parent.mkdir()
            source = (
                "def score_result(artifact, step, ctx):\n"
                "    return 1.0\n"
                "_SCORERS = {}\n"
            )
            checker.write_text(source, encoding="utf-8")
            contract_map, checker_analysis, grading = static_inputs(
                scorer_bound=False,
                binding_status="STATIC_NOT_BOUND",
            )
            trace = d6.analyze(
                contract_map=contract_map,
                checker_analysis=checker_analysis,
                grading_contract=grading,
                checker_source=source,
            )
            proof = trace["core_outputs"][0]["evidence"]["scorer_binding"][
                "source_bound_unique_proof"
            ]
            quote = checker.read_text(encoding="utf-8")
            evidence = {
                "id": "wiring",
                "source": "tests/checker.py",
                "quote": quote,
                "source_hash": "sha256:"
                + hashlib.sha256(checker.read_bytes()).hexdigest(),
            }
            plan = {
                "core_science_change": False,
                "finding_id": "FINDING-001",
                "deterministic_check": "D6",
                "repair_scope": "UNIQUE_SCORING_WIRING",
                "repair_class": "AUTO_FIX",
                "operations": [
                    {
                        "id": "wire-result",
                        "type": "replace_text",
                        "file": "tests/checker.py",
                        "old": "_SCORERS = {}",
                        "new": "_SCORERS = {'result': score_result}",
                        "evidence_ids": ["wiring"],
                    }
                ],
                "evidence": [evidence],
            }
            report = {
                "findings": [
                    {
                        "finding_id": "FINDING-001",
                        "evidence": {
                            "repair_class": "AUTO_FIX",
                            "repair_scope": "UNIQUE_SCORING_WIRING",
                            "unique_wiring": True,
                            "source_bound_unique_proof": proof,
                        },
                    }
                ]
            }
            validated = run_repair.validate_policy(
                root,
                report,
                {},
                plan,
            )

        self.assertEqual(validated["wiring"]["source_category"], "checker_contract")

    def test_unique_wiring_auto_fix_rejects_arbitrary_checker_replacement(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            checker = root / "tests/checker.py"
            checker.parent.mkdir()
            source = (
                "def score_result(artifact, step, ctx):\n"
                "    return 1.0\n"
                "_SCORERS = {}\n"
            )
            checker.write_text(source, encoding="utf-8")
            contract_map, checker_analysis, grading = static_inputs(
                scorer_bound=False,
                binding_status="STATIC_NOT_BOUND",
            )
            trace = d6.analyze(
                contract_map=contract_map,
                checker_analysis=checker_analysis,
                grading_contract=grading,
                checker_source=source,
            )
            proof = trace["core_outputs"][0]["evidence"]["scorer_binding"][
                "source_bound_unique_proof"
            ]
            evidence = {
                "id": "wiring",
                "source": "tests/checker.py",
                "quote": source,
                "source_hash": "sha256:"
                + hashlib.sha256(checker.read_bytes()).hexdigest(),
            }
            plan = {
                "core_science_change": False,
                "finding_id": "FINDING-001",
                "deterministic_check": "D6",
                "repair_scope": "UNIQUE_SCORING_WIRING",
                "repair_class": "AUTO_FIX",
                "operations": [
                    {
                        "id": "rewrite-checker",
                        "type": "replace_text",
                        "file": "tests/checker.py",
                        "old": "_SCORERS = {}",
                        "new": "_SCORERS = {}\n# unrelated",
                        "evidence_ids": ["wiring"],
                    }
                ],
                "evidence": [evidence],
            }
            report = {
                "findings": [
                    {
                        "finding_id": "FINDING-001",
                        "evidence": {
                            "repair_class": "AUTO_FIX",
                            "repair_scope": "UNIQUE_SCORING_WIRING",
                            "unique_wiring": True,
                            "source_bound_unique_proof": proof,
                        },
                    }
                ]
            }
            with self.assertRaisesRegex(
                run_repair.PolicyStop, "exactly the proven"
            ):
                run_repair.validate_policy(root, report, {}, plan)

    def test_overwritten_output_alias_is_not_a_content_read(self) -> None:
        contract_map, checker_analysis, grading = static_inputs(
            checker_reads="STATIC_EXPLICIT_READ_CANDIDATE",
        )
        result = d6.analyze(
            contract_map=contract_map,
            checker_analysis=checker_analysis,
            grading_contract=grading,
            checker_source=(
                "def load():\n"
                "    path = '/app/outputs/result.json'\n"
                "    path = '/tmp/unrelated.json'\n"
                "    with open(path) as handle:\n"
                "        return handle.read()\n"
                "def score_result(artifact, step, ctx):\n"
                "    return 1.0\n"
                "_SCORERS = {'result': score_result}\n"
            ),
        )
        self.assertNotEqual(
            result["core_outputs"][0]["content_read"], d6.PROVEN
        )

    def test_breakdown_presence_does_not_prove_final_reward(self) -> None:
        contract_map, checker_analysis, grading = static_inputs()
        result = d6.analyze(
            contract_map=contract_map,
            checker_analysis=checker_analysis,
            grading_contract=grading,
            checker_source=(
                "def check():\n"
                "    breakdown = {'result': {'score': 0.5, 'weight': 1.0}}\n"
                "    reward = 1.0\n"
                "    return {'reward': reward, 'breakdown': breakdown}\n"
                "def score_result(artifact, step, ctx):\n"
                "    return 0.5\n"
                "_SCORERS = {'result': score_result}\n"
            ),
            checker_result={
                "tests": [
                    {
                        "case": "known_valid_public",
                        "reward": 1.0,
                        "breakdown": {
                            "result": {"score": 0.5, "weight": 1.0},
                            "_errors": {},
                        },
                    },
                    {
                        "case": "random_baseline",
                        "reward": 1.0,
                        "breakdown": {
                            "result": {"score": 0.0, "weight": 1.0},
                            "_errors": {},
                        },
                    },
                ]
            },
        )
        chain = result["core_outputs"][0]
        self.assertEqual(chain["final_reward"], d6.FAILED)
        self.assertEqual(result["status"], d6.FAILED)

    def test_scoring_semantics_requires_typed_contract_evidence(self) -> None:
        operation = {
            "type": "replace_text",
            "file": "tests/checker.py",
            "old": "return 0.0\n",
            "new": "return 1.0\n",
        }
        with self.assertRaises(run_repair.PolicyStop):
            run_repair.validate_precision_matrix(
                operation,
                [],
                "ASSISTED_FIX",
                "SCORING_SEMANTICS",
            )


if __name__ == "__main__":
    unittest.main()
