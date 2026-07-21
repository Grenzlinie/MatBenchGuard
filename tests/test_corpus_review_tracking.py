from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import init_corpus_review_tracking as tracker  # noqa: E402


class CorpusReviewTrackingTests(unittest.TestCase):
    @staticmethod
    def _make_package(path: Path) -> None:
        path.mkdir(parents=True)
        (path / "instruction.md").write_text("x\n", encoding="utf-8")
        (path / "tests").mkdir()

    def test_merge_preserves_human_fields(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_name:
            temporary = Path(temporary_name)
            corpus = temporary / "materials_science_questions"
            package = (
                corpus
                / "cluster-1"
                / "theme-a"
                / "paper-123"
            )
            package.mkdir(parents=True)
            (package / "instruction.md").write_text("x\n", encoding="utf-8")
            (package / "tests").mkdir()
            (package / "tests/checker.py").write_text("pass\n", encoding="utf-8")
            # management dirs must be ignored
            management = corpus / "cluster-1" / "theme-a" / "review_outputs" / "123"
            management.mkdir(parents=True)
            (management / "instruction.md").write_text("ignore\n", encoding="utf-8")
            (management / "tests").mkdir()

            first = tracker.build_tracking(corpus)
            self.assertEqual(first["package_count"], 1)
            first["records"][0]["review_status"] = "reviewed"
            first["records"][0]["review_verdict"] = "PASS"
            first["records"][0]["notes"] = "human note"

            # add a second package and merge
            package2 = corpus / "cluster-1" / "theme-a" / "paper-456"
            package2.mkdir(parents=True)
            (package2 / "instruction.md").write_text("y\n", encoding="utf-8")
            (package2 / "tests").mkdir()

            merged = tracker.build_tracking(corpus, previous=first)
            self.assertEqual(merged["package_count"], 2)
            by_id = {item["package_id"]: item for item in merged["records"]}
            self.assertEqual(by_id["cluster-1/theme-a/paper-123"]["review_status"], "reviewed")
            self.assertEqual(by_id["cluster-1/theme-a/paper-123"]["notes"], "human note")
            self.assertEqual(by_id["cluster-1/theme-a/paper-456"]["review_status"], "pending")

    def test_checked_in_tracking_matches_generator(self) -> None:
        checked = json.loads(
            (
                REPO_ROOT
                / "materials_science_questions/corpus_review_tracking.json"
            ).read_text(encoding="utf-8")
        )
        fresh = tracker.build_tracking(REPO_ROOT / "materials_science_questions")
        self.assertEqual(checked["package_count"], fresh["package_count"])
        self.assertEqual(
            [item["package_id"] for item in checked["records"]],
            [item["package_id"] for item in fresh["records"]],
        )

    def test_scanner_excludes_management_nested_and_symlink_identities(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_name:
            corpus = Path(temporary_name) / "materials_science_questions"
            valid = corpus / "cluster-1/theme-a/paper-1"
            self._make_package(valid)
            (corpus / "corpus_review_tracking.json").write_text("{}", encoding="utf-8")

            for name in (
                "review_outputs",
                "review_records",
                ".benchmark_repair_history",
            ):
                self._make_package(corpus / f"cluster-1/theme-a/{name}/paper-fake")
            self._make_package(valid / "nested/paper-fake")

            external = Path(temporary_name) / "external-paper"
            self._make_package(external)
            symlink = corpus / "cluster-1/theme-a/paper-link"
            symlink.symlink_to(external, target_is_directory=True)

            packages = tracker.discover_packages(corpus)
            self.assertEqual(packages, [valid.resolve()])


if __name__ == "__main__":
    unittest.main()
