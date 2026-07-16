from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_materials_benchmark_review_e1 import (
    SOURCE_PACKAGE,
    copy_source_package,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
)
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import audit_package  # noqa: E402
import dynamic_checker_probe  # noqa: E402
import finalize_audit_output  # noqa: E402
import run_review  # noqa: E402


class MaterialsReviewV10BTests(unittest.TestCase):
    def test_process_artifacts_are_contract_map_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            baseline = audit_package.static_audit(
                package, Path(temporary) / "baseline-static.json"
            )
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + "\n\n### Step 2: Record process trace\n"
                + "- Role: process\n"
                + "- Action: Record the convergence trace.\n"
                + "- Evidence: `/app/outputs/process_trace.json`\n",
                encoding="utf-8",
            )
            result = dynamic_checker_probe.dynamic_checker_probe(
                package,
                Path(temporary) / "checker.json",
            )
            with_process = audit_package.static_audit(
                package, Path(temporary) / "process-static.json"
            )

        self.assertEqual(
            baseline["static_verdict"], with_process["static_verdict"]
        )
        self.assertEqual(
            [item["code"] for item in baseline["issues"]],
            [item["code"] for item in with_process["issues"]],
        )
        self.assertEqual(
            set(result["probe_coverage"]),
            {
                "positive",
                "negative",
                "discrimination",
                "equivalence",
                "component_isolation",
                "task_family_attacks",
            },
        )
        self.assertNotIn(
            "PROCESS_EVIDENCE_NOT_VERIFIED",
            {item["code"] for item in result["findings"]},
        )

    def test_ignored_load_bearing_output_is_a_severe_core_finding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "instruction.md").write_text(
                """
### Step 1: Build the complete crystal structure model
- Role: process
- Action: Generate the complete load-bearing crystal structure.
- Output file: `/app/outputs/structure.cif`
""",
                encoding="utf-8",
            )
            static = audit_package.static_audit(
                package, Path(temporary) / "static.json"
            )

        finding = next(
            item
            for item in static["issues"]
            if item["code"] == "CHECKER_CORE_TASK_UNASSESSED"
        )
        self.assertIn("structure.cif", finding["message"])
        self.assertEqual(finding["severity"], "FATAL")

    def test_existence_only_core_output_is_a_severe_finding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "instruction.md").write_text(
                """
### Step 1: Build the complete crystal structure model
- Role: scored
- Action: Generate the complete load-bearing crystal structure.
- Output file: `/app/outputs/structure.cif`
""",
                encoding="utf-8",
            )
            (package / "tests/checker.py").write_text(
                """
from pathlib import Path

reward = 1.0 if Path("/app/outputs/structure.cif").exists() else 0.0
""",
                encoding="utf-8",
            )
            static = audit_package.static_audit(
                package, Path(temporary) / "static.json"
            )

        finding = next(
            item
            for item in static["issues"]
            if item["code"] == "CHECKER_CORE_TASK_UNASSESSED"
        )
        self.assertEqual(finding["severity"], "FATAL")
        self.assertEqual(
            finding["evidence"]["semantic_validation"], "EXISTENCE_ONLY"
        )

    def test_gold_provenance_is_present_in_no_paper_report(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            run_review.run_review(package, None)
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )

        self.assertIn("gold_provenance", report)
        self.assertIn(
            report["gold_provenance"]["status"],
            {"ASSESSED", "NOT_ASSESSABLE"},
        )
        self.assertNotEqual(report["summary"]["final_verdict"], "PASS")
        self.assertEqual(
            report["summary"]["route"], "PAPER_GROUNDED_E1"
        )
        self.assertIsNotNone(
            report["audit_binding"]["implementation_hash"]
        )
        self.assertTrue(report["audit_binding"]["source_hashes"])

    def test_paper_binding_records_previous_audit_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            run_review.run_review(package, None)
            previous = json.loads(
                (
                    package / "benchmark_audit/audit_manifest.json"
                ).read_text(encoding="utf-8")
            )
            context = run_review.prepare_workspace(
                package, "paper_grounded", "E1"
            )
            manifest = json.loads(
                (Path(context["audit_temp_dir"]) / "audit_manifest.json").read_text(
                    encoding="utf-8"
                )
            )

        self.assertEqual(manifest["parent_audit_id"], previous["audit_id"])
        self.assertTrue(manifest["input_hashes"])
        self.assertIsNotNone(
            manifest["review_implementation"]["aggregate_hash"]
        )

    def test_task_family_attacks_have_explicit_status_and_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            result = dynamic_checker_probe.dynamic_checker_probe(
                package,
                Path(temporary) / "checker.json",
            )

        attacks = result["probe_coverage"]["task_family_attacks"]
        self.assertTrue(attacks)
        for attack in attacks.values():
            self.assertIn(
                attack["status"],
                {"ASSESSED", "NOT_ASSESSABLE", "NOT_APPLICABLE"},
            )
            self.assertIsInstance(attack["provenance"], dict)
            self.assertFalse(attack["provenance"].get("oracle_used", True))

    def test_report_keeps_route_distinct_from_four_level_verdict(self) -> None:
        self.assertEqual(
            finalize_audit_output.ROUTES["PASS"],
            "PUBLISH_CANDIDATE",
        )
        self.assertNotIn(
            finalize_audit_output.ROUTES["PASS"],
            finalize_audit_output.VERDICTS,
        )


if __name__ == "__main__":
    unittest.main()
