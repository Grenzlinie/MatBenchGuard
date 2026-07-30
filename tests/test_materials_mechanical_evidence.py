from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


collector = load(
    "mechanical_collector",
    ROOT
    / ".cursor/skills/materials-benchmark-review/scripts/collect_package_evidence.py",
)
runner = load(
    "probe_runner",
    ROOT / ".cursor/skills/materials-benchmark-review/scripts/run_checker_probes.py",
)


def make_package(root: Path) -> Path:
    package = root / "paper-1"
    tests = package / "tests"
    tests.mkdir(parents=True)
    (package / "instruction.md").write_text(
        "# Task\nWrite `/app/outputs/result.json` with value in eV.\n"
        "Required dataset: https://example.invalid/data.json\n",
        encoding="utf-8",
    )
    (tests / "grading_spec.json").write_text(
        json.dumps(
            {
                "pass_threshold": 0.8,
                "output_contract": {
                    "outputs": [
                        {
                            "file": "result.json",
                            "format": "json",
                            "purpose": "scored",
                            "schema": {"required": ["value"]},
                        }
                    ]
                },
                "steps": [
                    {
                        "id": "score_value",
                        "output_file": "result.json",
                        "kind": "numeric",
                        "weight": 1.0,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (tests / "checker.py").write_text(
        "import json, os\n"
        "def score_value(data):\n    return float(data.get('value', 0.0)) if isinstance(data, dict) else 0.0\n"
        "_SCORERS = {'score_value': score_value}\n"
        "p='/app/outputs/result.json'\n"
        "try:\n    data=json.load(open(p))\n    score=max(0.0,min(1.0,score_value(data)))\nexcept Exception:\n    score=0.0\n"
        "os.makedirs('/logs/verifier',exist_ok=True)\n"
        "open('/logs/verifier/reward.txt','w').write(str(score))\n"
        "json.dump({'score_value':score},open('/logs/verifier/breakdown.json','w'))\n",
        encoding="utf-8",
    )
    (tests / "test.sh").write_text(
        "#!/usr/bin/env bash\nset -euo pipefail\npython /tests/checker.py\n",
        encoding="utf-8",
    )
    (tests / "test.sh").chmod(0o755)
    return package


class MechanicalEvidenceTests(unittest.TestCase):
    def test_static_collector_exports_facts_not_findings(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            result = collector.collect(package)
            self.assertEqual(result["authority"], "MECHANICAL_EVIDENCE_ONLY")
            self.assertFalse(result["may_decide_findings_or_verdict"])
            self.assertNotIn("findings", result)
            self.assertNotIn("verdict", result)
            self.assertEqual(result["package_structure"]["status"], "INCOMPLETE")
            self.assertEqual(
                result["package_structure"]["missing_required_files"],
                [
                    "manifest.json",
                    "task.toml",
                    "resources.json",
                    "steps.json",
                    "paper/paper.md",
                ],
            )
            self.assertEqual(
                result["package_structure"]["test_entrypoint"]["status"], "READY"
            )
            self.assertEqual(
                result["grading_contract_facts"]["outputs"][0]["file"], "result.json"
            )
            self.assertEqual(
                result["grading_contract_facts"]["weights"][0]["weight"], 1.0
            )
            self.assertTrue(result["checker_ast_facts"]["scorer_registry"])
            chain = result["checker_ast_facts"]["scoring_chain_candidates"][0]
            self.assertEqual(chain["output_file"], "result.json")
            self.assertTrue(chain["all_step_ids_have_registered_scorer_candidate"])
            self.assertTrue(chain["final_reward_write_candidate_present"])
            self.assertIn(
                "result.json",
                {
                    x["file"]
                    for x in result["instruction_contract_candidates"][
                        "output_mentions"
                    ]
                },
            )

    def test_missing_test_sh_is_a_required_structure_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            (package / "tests/test.sh").unlink()
            result = collector.collect(package)
            structure = result["package_structure"]
            self.assertEqual(structure["status"], "INCOMPLETE")
            self.assertIn("tests/test.sh", structure["missing_required_files"])
            self.assertEqual(structure["test_entrypoint"]["status"], "MISSING")

    def test_cross_step_analysis_window_conflict_is_collected_as_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            (package / "steps.json").write_text(
                json.dumps(
                    [
                        {
                            "id": "run_md",
                            "action": "Use the final 15 ns for analysis.",
                        },
                        {
                            "id": "score_energy",
                            "action": "From the final 5 ns calculate the energy.",
                        },
                    ]
                ),
                encoding="utf-8",
            )
            result = collector.collect(package)
            candidate = result["cross_step_parameter_candidates"]["analysis_window"]
            self.assertTrue(candidate["conflict_candidate"])
            self.assertEqual(len(candidate["mentions"]), 2)
            self.assertTrue(candidate["candidate_only"])

    def test_simulation_parameter_dependencies_are_collected_as_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            (package / "steps.json").write_text(
                json.dumps(
                    [
                        {
                            "id": "build",
                            "action": (
                                "Choose any reasonable mapping of the {111} plane "
                                "to a Cartesian axis."
                            ),
                        },
                        {
                            "id": "load",
                            "action": "Apply fixed strain epsilon_zz.",
                        },
                        {
                            "id": "score",
                            "action": "The target value must equal the paper value.",
                        },
                    ]
                ),
                encoding="utf-8",
            )
            result = collector.collect(package)
            candidate = result["cross_step_parameter_candidates"][
                "simulation_parameter"
            ]
            self.assertTrue(candidate["coordinate_dependency_candidate"]["present"])
            self.assertTrue(
                candidate["upstream_downstream_dependency_candidate"]["present"]
            )
            self.assertTrue(candidate["mentions"])
            self.assertIn("candidate_only", candidate["mentions"][0])

    def test_random_and_interpolated_gold_generation_are_risk_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            (package / "tests/make_gold.py").write_text(
                "gold = numpy.interp(x, xp, fp) + random.uniform(-0.1, 0.1)\n",
                encoding="utf-8",
            )
            result = collector.collect(package)
            patterns = {
                item["pattern_id"]
                for item in result["gold_provenance_risk_candidates"]
                if item["path"] == "tests/make_gold.py"
            }
            self.assertEqual(
                patterns,
                {
                    "RANDOM_OR_PERTURBED_REFERENCE",
                    "INTERPOLATED_OR_FITTED_REFERENCE",
                },
            )

    def test_solution_directory_is_completely_excluded(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            (package / "solution").mkdir()
            (package / "solution/run_smoke.sh").write_text(
                "#!/usr/bin/env bash\n# reduced smoke runner for trend validation\n",
                encoding="utf-8",
            )
            result = collector.collect(package)
            self.assertFalse(
                any(item["path"].startswith("solution/") for item in result["inventory"])
            )
            self.assertFalse(
                any(
                    item["path"].startswith("solution/")
                    for item in result["gold_provenance_risk_candidates"]
                )
            )
            self.assertNotIn("findings", result)
            self.assertFalse(result["may_decide_findings_or_verdict"])

    def test_unknown_grading_shape_is_limitation_not_schema_finding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            (package / "tests/grading_spec.json").write_text(
                json.dumps({"custom_contract": {"artifact": "result.json"}}),
                encoding="utf-8",
            )
            result = collector.collect(package)
            grading = result["grading_contract_facts"]
            self.assertEqual(grading["status"], "PARSED")
            self.assertTrue(grading["limitations"])
            self.assertNotIn("findings", result)

    def test_url_probe_blocks_private_network(self) -> None:
        observed = collector.probe_url("http://127.0.0.1/private", 1)
        self.assertEqual(observed["status"], "BLOCKED")

    def test_resources_json_urls_are_collected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            (package / "resources.json").write_text(
                json.dumps(
                    {
                        "resources": [
                            {
                                "id": "potential",
                                "url": "https://example.org/potential.eam",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            result = collector.collect(package)
            self.assertIn(
                {
                    "url": "https://example.org/potential.eam",
                    "path": "resources.json",
                    "locator": "$.resources[0].url",
                },
                result["url_candidates"],
            )

    def test_404_url_is_confirmed_missing_without_reading_body(self) -> None:
        error = collector.urllib.error.HTTPError(
            "https://example.org/missing", 404, "Not Found", None, None
        )
        address = [(None, None, None, None, ("93.184.216.34", 0))]
        with (
            mock.patch.object(collector.socket, "getaddrinfo", return_value=address),
            mock.patch.object(collector.urllib.request, "urlopen", side_effect=error),
        ):
            observed = collector.probe_url("https://example.org/missing", 1)
        self.assertEqual(observed["status"], "CONFIRMED_MISSING")
        self.assertEqual(observed["http_status"], 404)

    def test_skipped_url_probe_is_not_a_review_limitation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            (package / "instruction.md").write_text(
                "# Task\n\nAsset: https://play.bohrium.com/data/example\n",
                encoding="utf-8",
            )
            result = collector.collect(package)
            self.assertEqual(result["url_probes"], [])
            self.assertFalse(
                any(item.get("stage") == "url_probe" for item in result["limitations"])
            )

    def test_probe_runner_records_observations_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            result = runner.run(package, {}, timeout=10)
            self.assertEqual(result["authority"], "MECHANICAL_OBSERVATIONS_ONLY")
            self.assertFalse(result["may_decide_findings_or_verdict"])
            by_id = {item["case_id"]: item for item in result["observations"]}
            self.assertEqual(by_id["missing_output"]["status"], "OBSERVED")
            self.assertEqual(by_id["missing_output"]["reward"], 0.0)
            self.assertEqual(by_id["random_or_constant"]["status"], "OBSERVED")
            self.assertEqual(by_id["quality_gradient"]["status"], "NOT_ASSESSED")
            self.assertNotIn("verdict", result)

    def test_agent_supplied_positive_case_is_executed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = make_package(root)
            positive = root / "positive"
            positive.mkdir()
            (positive / "result.json").write_text('{"value": 1.0}\n', encoding="utf-8")
            result = runner.run(package, {"valid_positive": positive}, timeout=10)
            observed = next(
                x for x in result["observations"] if x["case_id"] == "valid_positive"
            )
            self.assertEqual(observed["status"], "OBSERVED")
            self.assertEqual(observed["probe_class"], "valid_positive")
            self.assertEqual(observed["reward"], 1.0)

    def test_task_specific_variant_is_retained_alongside_builtin_case(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = make_package(root)
            attack = root / "attack"
            attack.mkdir()
            (attack / "result.json").write_text('{"value": 0.9}\n', encoding="utf-8")
            supplied = runner.parse_cases(
                [f"minimal_exploit:wrong-coordinate={attack}"]
            )
            result = runner.run(package, supplied, timeout=10)
            by_id = {item["case_id"]: item for item in result["observations"]}
            self.assertIn("minimal_exploit", by_id)
            self.assertIn("minimal_exploit:wrong-coordinate", by_id)
            self.assertEqual(
                by_id["minimal_exploit:wrong-coordinate"]["probe_class"],
                "minimal_exploit",
            )
            self.assertEqual(by_id["minimal_exploit:wrong-coordinate"]["reward"], 0.9)

    def test_probe_execution_can_only_be_skipped_explicitly(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            result = runner.run(package, {}, timeout=10, execute=False)
            self.assertTrue(
                all(x["status"] == "NOT_ASSESSED" for x in result["observations"])
            )


if __name__ == "__main__":
    unittest.main()
