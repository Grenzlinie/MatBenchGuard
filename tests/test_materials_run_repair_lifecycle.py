from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
sys.path.insert(0, str(REVIEW_SCRIPTS))
import run_context  # noqa: E402


def repair_module():
    path = REPO_ROOT / ".cursor/skills/materials-benchmark-repair/scripts/run_repair.py"
    spec = importlib.util.spec_from_file_location("run_repair_lifecycle", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MaterialsRunRepairLifecycleTests(unittest.TestCase):
    def test_repair_can_run_once_and_second_attempt_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "corpus/cluster-1/theme/paper-1"
            (package / "tests").mkdir(parents=True)
            (package / "instruction.md").write_text("task\n", encoding="utf-8")
            run = run_context.create_run(root / "corpus", "cluster-1/theme/paper-1", "run-1")
            run_context.snapshot_package(package, run)
            (run / "audit").mkdir()
            (run / "audit/audit_report.json").write_text("{}", encoding="utf-8")
            (run / "plan.json").write_text(
                json.dumps({"schema_version": "materials-deterministic-repair-plan/1.0", "audit_id": "audit-1", "findings": [], "deterministic_contract": {}}),
                encoding="utf-8",
            )
            run_context.write_content_root(run, "A0")
            run_context.transition(run, "REVIEWING")
            run_context.transition(run, "REVIEWED")
            module = repair_module()

            def fake_repair(*_args: object, **_kwargs: object) -> dict[str, object]:
                candidate = run / "candidate"
                candidate.mkdir()
                (candidate / "instruction.md").write_text("candidate\n", encoding="utf-8")
                (run / "reaudit").mkdir()
                (run / "reaudit/audit.json").write_text("{}", encoding="utf-8")
                return {"status": "PARTIALLY_REPAIRED", "package_mutated": False}

            with patch.object(module, "_repair_locked", side_effect=fake_repair):
                result = module.repair_context(run)
            self.assertEqual(result["status"], "PARTIALLY_REPAIRED")
            self.assertEqual(run_context.status(run)["state"], "COMPLETED")
            self.assertTrue((run / "roots/R0.json").is_file())
            self.assertTrue((run / "roots/A1.json").is_file())
            with self.assertRaisesRegex(run_context.RunContextError, "REVIEWED"):
                module.repair_context(run)
