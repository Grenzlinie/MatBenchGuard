from __future__ import annotations

import importlib.util
import json
import csv
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
sys.path.insert(0, str(REVIEW_SCRIPTS))
import run_context  # noqa: E402


def load_finalizer():
    spec = importlib.util.spec_from_file_location(
        "finalize_materials_review_batch",
        REPO_ROOT / "tools/finalize_materials_review_batch.py",
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_batch_creator():
    spec = importlib.util.spec_from_file_location(
        "create_materials_review_batch",
        REPO_ROOT / "tools/create_materials_review_batch.py",
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MaterialsBatchCoordinationTests(unittest.TestCase):
    def package(self, root: Path) -> Path:
        package = root / "corpus/cluster-1/theme/paper-1"
        (package / "tests").mkdir(parents=True)
        (package / "instruction.md").write_text("task\n", encoding="utf-8")
        return package

    def tracking(self, root: Path) -> Path:
        path = root / "corpus/corpus_review_tracking.json"
        path.write_text(json.dumps({"records": [{"package_id": "cluster-1/theme/paper-1"}]}), encoding="utf-8")
        return path

    def test_finalizer_requires_terminal_batch_and_updates_tracking(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.package(root)
            tracking = self.tracking(root)
            run = run_context.create_run(root / "corpus", "cluster-1/theme/paper-1", "run-1")
            finalizer = load_finalizer()
            with self.assertRaisesRegex(run_context.RunContextError, "not terminal"):
                finalizer.tracking_update([run], tracking)
            run_context.transition(run, "REVIEWING")
            run_context.transition(run, "REVIEWED", review_result={"review_verdict": "PASS", "audit_id": "a0"})
            run_context.complete(run, outcome="NOT_REQUIRED", repair_status="NOT_REQUIRED")
            result = finalizer.tracking_update([run], tracking)
            self.assertEqual(result["updated"][0]["outcome"], "NOT_REQUIRED")
            record = json.loads(tracking.read_text())["records"][0]
            self.assertEqual(record["review_verdict"], "PASS")
            self.assertEqual(record["repair_status"], "NOT_REQUIRED")

    def test_main_agent_updates_only_matching_assignment_row(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.package(root)
            run = run_context.create_run(root / "corpus", "cluster-1/theme/paper-1", "run-1")
            run_context.transition(run, "REVIEWING")
            run_context.transition(run, "REVIEWED", review_result={"review_verdict": "REJECT"})
            run_context.complete(run, outcome="ABANDONED", repair_status="ABANDONED")
            ledger = root / "assignments.csv"
            fields = ["package_id", "run_id", "status", "completed_at", "review_verdict", "repair_status"]
            with ledger.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"package_id": "cluster-1/theme/paper-1", "run_id": "run-1", "status": "ASSIGNED", "completed_at": "", "review_verdict": "", "repair_status": ""})
            finalizer = load_finalizer()
            finalizer.update_assignment_ledger([run], ledger)
            with ledger.open(encoding="utf-8", newline="") as handle:
                row = next(csv.DictReader(handle))
            self.assertEqual(row["status"], "COMPLETED")
            self.assertEqual(row["repair_status"], "ABANDONED")

    def test_batch_creator_validates_all_packages_and_parallelism(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.package(root)
            second = root / "corpus/cluster-2/theme/paper-2"
            (second / "tests").mkdir(parents=True)
            (second / "instruction.md").write_text("task\n", encoding="utf-8")
            creator = load_batch_creator()
            runs = creator.create_batch(
                root / "corpus",
                ["cluster-1/theme/paper-1", "cluster-2/theme/paper-2"],
                "main-agent",
                3,
            )
            self.assertEqual(len(runs), 2)
            with self.assertRaisesRegex(run_context.RunContextError, "between 1 and 3"):
                creator.create_batch(root / "corpus", ["cluster-1/theme/paper-1"], "main-agent", 4)
