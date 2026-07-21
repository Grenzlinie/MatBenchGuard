from __future__ import annotations

import csv
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = (
    REPO_ROOT
    / ".cursor/skills/materials-benchmark-review/scripts"
)
FIXTURES = REPO_ROOT / "tests/fixtures/probe_packages"
sys.path.insert(0, str(SCRIPTS))

import dynamic_checker_probe as probe  # noqa: E402


def _local_grade_json_numeric(outputs: Path) -> float:
    data = json.loads((outputs / "metrics.json").read_text(encoding="utf-8"))
    target = {"R2": 0.9, "RMSE": 0.1, "MAE": 0.05}
    scores = []
    for key, expected in target.items():
        value = float(data[key])
        if key == "R2":
            scores.append(max(0.0, 1.0 - abs(value - expected) / 0.5))
        else:
            scores.append(
                max(0.0, 1.0 - abs(value - expected) / max(expected, 1e-6))
            )
    return sum(scores) / len(scores)


def _local_grade_categorical(outputs: Path) -> float:
    data = json.loads((outputs / "labels.json").read_text(encoding="utf-8"))
    target = {"phase": "metal", "stability": "stable"}
    scores = [1.0 if data.get(key) == value else 0.0 for key, value in target.items()]
    return sum(scores) / len(scores)


def _local_grade_csv(outputs: Path) -> float:
    with (outputs / "predictions.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = ["true_value", "predicted_mean", "predicted_std"]
    if not rows or any(column not in rows[0] for column in required):
        return 0.0
    errors = []
    for row in rows:
        true = float(row["true_value"])
        pred = float(row["predicted_mean"])
        std = float(row["predicted_std"])
        errors.append(abs(true - pred) + abs(std - 0.1))
    return max(0.0, 1.0 - (sum(errors) / len(errors)))


def _local_grade_metrics_csv(outputs: Path) -> float:
    with (outputs / "predictions.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = ["true_oxidation_state", "predicted_mean", "predicted_std"]
    structural = 1.0 if rows and all(column in rows[0] for column in required) else 0.0
    metrics = json.loads((outputs / "metrics.json").read_text(encoding="utf-8"))
    r2 = float(metrics["R2"])
    rmse = float(metrics["RMSE"])
    metric_score = (
        max(0.0, 1.0 - abs(r2 - 0.85) / 0.5) * 0.5
        + max(0.0, 1.0 - abs(rmse - 0.24) / 0.5) * 0.5
    )
    return 0.2 * structural + 0.8 * metric_score


class ProbeFixtureMutationTests(unittest.TestCase):
    def _oracle_dir(self, fixture_name: str, temporary: Path) -> Path:
        fixture = FIXTURES / fixture_name
        oracle = temporary / "oracle"
        oracle.mkdir()
        # materialize oracle outputs by running the fixture solve logic locally
        if fixture_name == "json_numeric_multi":
            (oracle / "metrics.json").write_text(
                json.dumps({"R2": 0.9, "RMSE": 0.1, "MAE": 0.05}),
                encoding="utf-8",
            )
        elif fixture_name == "categorical_labels":
            (oracle / "labels.json").write_text(
                json.dumps({"phase": "metal", "stability": "stable"}),
                encoding="utf-8",
            )
        elif fixture_name == "csv_table":
            (oracle / "predictions.csv").write_text(
                "true_value,predicted_mean,predicted_std\n"
                "1.0,1.0,0.1\n"
                "2.0,2.0,0.1\n",
                encoding="utf-8",
            )
        elif fixture_name == "metrics_and_csv":
            (oracle / "predictions.csv").write_text(
                "true_oxidation_state,predicted_mean,predicted_std\n"
                "1.0,1.0,0.05\n"
                "2.0,2.0,0.05\n",
                encoding="utf-8",
            )
            (oracle / "metrics.json").write_text(
                json.dumps({"R2": 0.85, "RMSE": 0.24}),
                encoding="utf-8",
            )
        elif fixture_name == "nested_json":
            (oracle / "result.json").write_text(
                json.dumps(
                    {
                        "model": {"metrics": {"rmse": 0.1, "mae": 0.05}},
                        "validation": {"score": 0.95},
                    }
                ),
                encoding="utf-8",
            )
        elif fixture_name == "scalar_txt":
            (oracle / "score.txt").write_text("0.75\n", encoding="utf-8")
        else:
            raise AssertionError(fixture_name)
        return oracle

    def _score_cases(
        self,
        fixture_name: str,
        grade,
    ) -> tuple[float, float, float]:
        fixture = FIXTURES / fixture_name
        specification = json.loads(
            (fixture / "tests/grading_spec.json").read_text(encoding="utf-8")
        )
        with tempfile.TemporaryDirectory() as temporary_name:
            temporary = Path(temporary_name)
            oracle = self._oracle_dir(fixture_name, temporary)
            plan, reason = probe.schema_derived_probe_plan(specification, oracle)
            self.assertIsNone(reason)
            self.assertTrue(any(item["case"] == "all_wrong" for item in plan))

            full_dir = temporary / "full"
            full_dir.mkdir()
            for path in oracle.iterdir():
                shutil.copy2(path, full_dir / path.name)
            full_score = grade(full_dir)

            # Prefer a partial mutation that can change the local score.
            partial_candidates = [
                item for item in plan if item["mode"] == "partial"
            ]
            partial_score = full_score
            detail = None
            for partial_item in reversed(partial_candidates):
                partial_dir = temporary / f"partial_{partial_item['case']}"
                if partial_dir.exists():
                    shutil.rmtree(partial_dir)
                partial_dir.mkdir()
                for path in oracle.iterdir():
                    shutil.copy2(path, partial_dir / path.name)
                detail = probe.mutate_declared_component(
                    partial_dir,
                    partial_item["components"][0],
                    all_wrong=False,
                    specification=specification,
                )
                if detail.get("mutation") == "not_assessable":
                    continue
                candidate_score = grade(partial_dir)
                if candidate_score < full_score - 1e-12:
                    partial_score = candidate_score
                    break
            self.assertIsNotNone(detail)
            self.assertNotEqual(detail.get("mutation"), "not_assessable")
            self.assertLess(partial_score, full_score)

            all_wrong_dir = temporary / "all_wrong"
            all_wrong_dir.mkdir()
            for path in oracle.iterdir():
                shutil.copy2(path, all_wrong_dir / path.name)
            for component in next(
                item for item in plan if item["case"] == "all_wrong"
            )["components"]:
                detail = probe.mutate_declared_component(
                    all_wrong_dir,
                    component,
                    all_wrong=True,
                    specification=specification,
                )
                self.assertNotEqual(detail.get("mutation"), "not_assessable")
            all_wrong_score = grade(all_wrong_dir)

            malformed_dir = temporary / "malformed"
            malformed_dir.mkdir()
            probe.write_malformed_outputs(malformed_dir, specification)
            try:
                malformed_score = grade(malformed_dir)
            except Exception:
                malformed_score = 0.0
            self.assertLess(malformed_score, full_score)

            return full_score, partial_score, all_wrong_score

    def test_json_numeric_multi_field_ordering(self) -> None:
        full, partial, all_wrong = self._score_cases(
            "json_numeric_multi", _local_grade_json_numeric
        )
        self.assertGreater(full, partial)
        self.assertGreater(partial, all_wrong)

    def test_categorical_labels_ordering(self) -> None:
        full, partial, all_wrong = self._score_cases(
            "categorical_labels", _local_grade_categorical
        )
        self.assertGreater(full, partial)
        self.assertGreaterEqual(partial, all_wrong)

    def test_csv_table_ordering(self) -> None:
        full, partial, all_wrong = self._score_cases(
            "csv_table", _local_grade_csv
        )
        self.assertGreater(full, partial)
        self.assertGreaterEqual(partial, all_wrong)

    def test_metrics_and_csv_ordering(self) -> None:
        full, partial, all_wrong = self._score_cases(
            "metrics_and_csv", _local_grade_metrics_csv
        )
        self.assertGreater(full, partial)
        self.assertGreater(partial, all_wrong)

    def test_all_wrong_mutates_every_json_numeric_field(self) -> None:
        fixture = FIXTURES / "json_numeric_multi"
        specification = json.loads(
            (fixture / "tests/grading_spec.json").read_text(encoding="utf-8")
        )
        with tempfile.TemporaryDirectory() as temporary_name:
            temporary = Path(temporary_name)
            oracle = self._oracle_dir("json_numeric_multi", temporary)
            work = temporary / "work"
            work.mkdir()
            shutil.copy2(oracle / "metrics.json", work / "metrics.json")
            before = json.loads((work / "metrics.json").read_text(encoding="utf-8"))
            detail = probe.mutate_declared_component(
                work,
                {"component_id": "eval_metrics", "file": "metrics.json"},
                all_wrong=True,
                specification=specification,
            )
            after = json.loads((work / "metrics.json").read_text(encoding="utf-8"))
            self.assertEqual(detail["mutation"], "all_scored_json_leaves")
            self.assertEqual(set(before), set(after))
            self.assertTrue(all(before[key] != after[key] for key in before))

    def test_nested_json_preserves_component_identity_and_mutates_all_paths(self) -> None:
        fixture = FIXTURES / "nested_json"
        specification = json.loads(
            (fixture / "tests/grading_spec.json").read_text(encoding="utf-8")
        )
        components = probe.declared_scoring_components(specification)
        self.assertEqual(
            [item["component_id"] for item in components],
            ["model_errors", "validation_score"],
        )
        self.assertEqual([item["file"] for item in components], ["result.json"] * 2)
        with tempfile.TemporaryDirectory() as temporary_name:
            root = Path(temporary_name)
            oracle = self._oracle_dir("nested_json", root)
            before = json.loads((oracle / "result.json").read_text())
            for component in components:
                detail = probe.mutate_declared_component(
                    oracle,
                    component,
                    all_wrong=True,
                    specification=specification,
                )
                self.assertNotEqual(detail["mutation"], "not_assessable")
            after = json.loads((oracle / "result.json").read_text())
            self.assertEqual(before.keys(), after.keys())
            self.assertNotEqual(
                before["model"]["metrics"], after["model"]["metrics"]
            )
            self.assertNotEqual(
                before["validation"]["score"], after["validation"]["score"]
            )

    def test_scalar_text_mutations_remain_parseable(self) -> None:
        fixture = FIXTURES / "scalar_txt"
        specification = json.loads(
            (fixture / "tests/grading_spec.json").read_text(encoding="utf-8")
        )
        component = probe.declared_scoring_components(specification)[0]
        with tempfile.TemporaryDirectory() as temporary_name:
            root = Path(temporary_name)
            oracle = self._oracle_dir("scalar_txt", root)
            for all_wrong in (False, True):
                (oracle / "score.txt").write_text("0.75\n", encoding="utf-8")
                detail = probe.mutate_declared_component(
                    oracle,
                    component,
                    all_wrong=all_wrong,
                    specification=specification,
                )
                self.assertEqual(detail["mutation"], "parseable_numeric_text")
                self.assertNotEqual(float((oracle / "score.txt").read_text()), 0.75)


class CorpusTrackingTests(unittest.TestCase):
    def test_generator_discovers_current_corpus_count(self) -> None:
        sys.path.insert(0, str(REPO_ROOT / "tools"))
        import init_corpus_review_tracking as tracker  # noqa: E402

        payload = tracker.build_tracking(REPO_ROOT / "materials_science_questions")
        self.assertEqual(payload["schema_version"], tracker.SCHEMA_VERSION)
        self.assertEqual(payload["package_count"], len(payload["records"]))
        self.assertGreaterEqual(payload["package_count"], 1800)
        self.assertFalse(
            any("review_outputs" in item["package_id"] for item in payload["records"])
        )
        ranks = [item["discovery_rank"] for item in payload["records"]]
        self.assertEqual(ranks, list(range(1, len(ranks) + 1)))
        ids = [item["package_id"] for item in payload["records"]]
        self.assertEqual(ids, sorted(ids))


if __name__ == "__main__":
    unittest.main()
