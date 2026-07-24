from __future__ import annotations

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


collector = load("mechanical_collector", ROOT / ".cursor/skills/materials-benchmark-review/scripts/collect_package_evidence.py")
runner = load("probe_runner", ROOT / ".cursor/skills/materials-benchmark-review/scripts/run_checker_probes.py")


def make_package(root: Path) -> Path:
    package = root / "paper-1"; tests = package / "tests"; tests.mkdir(parents=True)
    (package / "instruction.md").write_text(
        "# Task\nWrite `/app/outputs/result.json` with value in eV.\n"
        "Required dataset: https://example.invalid/data.json\n",
        encoding="utf-8",
    )
    (tests / "grading_spec.json").write_text(json.dumps({
        "pass_threshold": 0.8,
        "output_contract": {"outputs": [{"file": "result.json", "format": "json", "purpose": "scored", "schema": {"required": ["value"]}}]},
        "steps": [{"id": "score_value", "output_file": "result.json", "kind": "numeric", "weight": 1.0}],
    }), encoding="utf-8")
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
    (tests / "test.sh").write_text("#!/usr/bin/env bash\nset -euo pipefail\npython /tests/checker.py\n", encoding="utf-8")
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
            self.assertEqual(result["grading_contract_facts"]["outputs"][0]["file"], "result.json")
            self.assertEqual(result["grading_contract_facts"]["weights"][0]["weight"], 1.0)
            self.assertTrue(result["checker_ast_facts"]["scorer_registry"])
            chain = result["checker_ast_facts"]["scoring_chain_candidates"][0]
            self.assertEqual(chain["output_file"], "result.json")
            self.assertTrue(chain["all_step_ids_have_registered_scorer_candidate"])
            self.assertTrue(chain["final_reward_write_candidate_present"])
            self.assertIn("result.json", {x["file"] for x in result["instruction_contract_candidates"]["output_mentions"]})

    def test_unknown_grading_shape_is_limitation_not_schema_finding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            (package / "tests/grading_spec.json").write_text(json.dumps({"custom_contract": {"artifact": "result.json"}}), encoding="utf-8")
            result = collector.collect(package)
            grading = result["grading_contract_facts"]
            self.assertEqual(grading["status"], "PARSED")
            self.assertTrue(grading["limitations"])
            self.assertNotIn("findings", result)

    def test_url_probe_blocks_private_network(self) -> None:
        observed = collector.probe_url("http://127.0.0.1/private", 1)
        self.assertEqual(observed["status"], "BLOCKED")

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
            root = Path(temporary); package = make_package(root); positive = root / "positive"; positive.mkdir()
            (positive / "result.json").write_text('{"value": 1.0}\n', encoding="utf-8")
            result = runner.run(package, {"valid_positive": positive}, timeout=10)
            observed = next(x for x in result["observations"] if x["case_id"] == "valid_positive")
            self.assertEqual(observed["status"], "OBSERVED")
            self.assertEqual(observed["reward"], 1.0)

    def test_probe_execution_can_only_be_skipped_explicitly(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = make_package(Path(temporary))
            result = runner.run(package, {}, timeout=10, execute=False)
            self.assertTrue(all(x["status"] == "NOT_ASSESSED" for x in result["observations"]))


if __name__ == "__main__":
    unittest.main()
