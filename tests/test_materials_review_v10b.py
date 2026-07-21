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
            },
        )
        self.assertIn(
            "task_family_attacks",
            result["probe_coverage"]["negative"]["subcoverage"],
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
- Role: core_output
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

        attacks = result["probe_coverage"]["negative"]["subcoverage"][
            "task_family_attacks"
        ]
        self.assertTrue(attacks)
        for attack in attacks.values():
            self.assertIn(
                attack["status"],
                {"ASSESSED", "NOT_ASSESSABLE", "NOT_APPLICABLE"},
            )
            self.assertIsInstance(attack["provenance"], dict)
            self.assertFalse(attack["provenance"].get("oracle_used", True))

    def test_process_only_step_does_not_change_task_attack_statuses(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "instruction.md").write_text(
                """
### Step 1: Report the scalar energy
- Role: scored_output
- Action: Compute the crystal energy.
- Output file: `/app/outputs/result.json`
""",
                encoding="utf-8",
            )
            specification_path = package / "tests/grading_spec.json"
            specification = json.loads(
                specification_path.read_text(encoding="utf-8")
            )
            specification["output_contract"]["outputs"][0]["description"] += (
                " The scored output includes a full crystal structure model."
            )
            specification_path.write_text(
                json.dumps(specification), encoding="utf-8"
            )
            without_process = dynamic_checker_probe.dynamic_checker_probe(
                package, Path(temporary) / "without-process.json"
            )
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + """

### Step 2: Save process diagnostics
- Role: process_evidence
- Action: Save the intermediate audit log.
- Evidence: `/app/outputs/process.log`
""",
                encoding="utf-8",
            )
            with_process = dynamic_checker_probe.dynamic_checker_probe(
                package, Path(temporary) / "with-process.json"
            )

        without_statuses = {
            name: value["status"]
            for name, value in without_process["probe_coverage"]["negative"][
                "subcoverage"
            ]["task_family_attacks"].items()
        }
        with_statuses = {
            name: value["status"]
            for name, value in with_process["probe_coverage"]["negative"][
                "subcoverage"
            ]["task_family_attacks"].items()
        }
        self.assertEqual(with_statuses, without_statuses)
        self.assertEqual(with_statuses["duplicate_structure"], "ASSESSED")
        self.assertEqual(with_statuses["missing_core_model"], "ASSESSED")

    def test_process_label_cannot_downgrade_load_bearing_core_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "instruction.md").write_text(
                """
### Step 1: Build the complete predictive model
- Role: process
- Action: Return the complete predictive model.
- Evidence: `/app/outputs/predictive_model.bin`

### Step 2: Return the full crystal structure
- Role: process_evidence
- Action: Return the full crystal structure.
- Evidence: `/app/outputs/crystal_structure.cif`

### Step 3: Save the audit log
- Role: process
- Action: Save an intermediate audit log.
- Evidence: `/app/outputs/process.log`
""",
                encoding="utf-8",
            )
            static = audit_package.static_audit(
                package, Path(temporary) / "static.json"
            )

        contract_map = static["contract_map"]
        self.assertEqual(
            contract_map["process_evidence"],
            ["process.log"],
        )
        self.assertEqual(
            contract_map["core_outputs"],
            ["crystal_structure.cif", "predictive_model.bin"],
        )
        self.assertEqual(
            [
                requirement["classification"]
                for requirement in contract_map["requirements"]
            ],
            ["UNCLASSIFIED", "UNCLASSIFIED", "PROCESS_ONLY"],
        )
        finding_codes = {item["code"] for item in static["issues"]}
        self.assertIn("CONTRADICTORY_OUTPUT_ROLE", finding_codes)
        severe = [
            item
            for item in static["issues"]
            if item["code"] == "CHECKER_CORE_TASK_UNASSESSED"
        ]
        self.assertTrue(all(item["severity"] == "FATAL" for item in severe))
        messages = " ".join(item["message"] for item in severe)
        self.assertIn("predictive_model.bin", messages)
        self.assertIn("crystal_structure.cif", messages)
        self.assertNotIn("process.log", messages)

    def test_missing_harbor_verifier_entrypoint_skips_direct_probes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "tests/test.sh").unlink()
            run_review.run_review(package, None)
            checker = json.loads(
                (package / "benchmark_audit/checker_tests.json").read_text(
                    encoding="utf-8"
                )
            )

        self.assertEqual(checker["tests"], [])
        self.assertEqual(
            checker["runtime_provenance"]["status"], "NOT_ASSESSABLE"
        )
        self.assertEqual(
            checker["runtime_provenance"]["reason"],
            "HARBOR_VERIFIER_ENTRYPOINT_MISSING",
        )

    def test_e2_cannot_be_published_by_authoritative_review(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            with self.assertRaisesRegex(ValueError, "fixed at E1"):
                run_review.run_review(package, None, execution_level="E2")

    def test_structured_roles_recognize_wording_variants_conservatively(self) -> None:
        variants = {
            "predictive_model.bin": "Build a full predictive model",
            "crystal.cif": "Return the full crystal structure",
            "trajectory.xyz": "Generate a complete trajectory",
            "field.vtk": "Generate a complete prediction field",
            "mesh.msh": "Generate a complete simulation mesh",
        }
        lines: list[str] = []
        for index, (filename, title) in enumerate(variants.items(), start=1):
            lines.extend(
                [
                    f"### Step {index}: {title}",
                    "- Role: core_output",
                    f"- Output file: `/app/outputs/{filename}`",
                    "",
                ]
            )
        lines.extend(
            [
                "### Step 9: Save an uncertain artifact",
                "- Role: auxiliary",
                "- Artifact: `/app/outputs/uncertain.dat`",
            ]
        )

        contract_map = audit_package.instruction_contract_map("\n".join(lines))

        self.assertEqual(
            set(contract_map["core_outputs"]), set(variants)
        )
        self.assertEqual(
            contract_map["unclassified_outputs"], ["uncertain.dat"]
        )
        for requirement in contract_map["requirements"]:
            self.assertIn(
                requirement["classification"],
                {"CORE_OUTPUT", "PROCESS_ONLY", "UNCLASSIFIED"},
            )

    def test_all_four_hard_gates_are_pre_paper_stops(self) -> None:
        codes = run_review.pre_paper_hard_gate_codes(
            {
                "issues": [
                    {"code": "UNRECOVERABLE_TASK_DEFINITION"},
                    {"code": "CHECKER_CORE_TASK_UNASSESSED"},
                ]
            },
            {
                "findings": [
                    {"code": "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"}
                ]
            },
            {"classification": "NON_MAT"},
        )

        self.assertEqual(
            codes,
            [
                "NON_MATERIALS_TASK",
                "UNRECOVERABLE_TASK_DEFINITION",
                "CHECKER_CORE_TASK_UNASSESSED",
                "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
            ],
        )

    def test_non_materials_gate_stops_before_paper_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            package = base / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "paper").mkdir(exist_ok=True)
            (package / "paper/paper.md").write_text(
                "This paper must remain outside fail-fast evidence.",
                encoding="utf-8",
            )
            (package / "paper/images_manifest.json").write_text(
                "[]\n", encoding="utf-8"
            )
            instruction = (package / "instruction.md").read_text(
                encoding="utf-8"
            )
            quote = next(
                line.strip() for line in instruction.splitlines() if line.strip()
            )
            assessment = base / "assessment.json"
            assessment.write_text(
                json.dumps(
                    {
                        "materials_qualification": {
                            "classification": "NON_MAT",
                            "rationale": "Authoritative adjudication rejects the task.",
                            "evidence": [
                                {
                                    "axis": axis,
                                    "package_file": "instruction.md",
                                    "package_quote": quote,
                                }
                                for axis in (
                                    "object",
                                    "operation",
                                    "endpoint",
                                    "domain_dependence",
                                )
                            ],
                        },
                        "dimensions": "must not be read before the gate",
                    }
                ),
                encoding="utf-8",
            )

            run_review.run_review(
                package,
                paper_mode="paper_grounded",
                agent_assessment_path=assessment,
            )
            report = json.loads(
                (package / "benchmark_audit/audit_report.json").read_text(
                    encoding="utf-8"
                )
            )
            manifest = json.loads(
                (package / "benchmark_audit/audit_manifest.json").read_text(
                    encoding="utf-8"
                )
            )

        self.assertEqual(report["summary"]["final_verdict"], "REJECT")
        self.assertIn(
            "NON_MATERIALS_TASK",
            [
                gate["code"]
                for gate in report["hard_gates"]
                if gate["status"] == "FAIL"
            ],
        )
        self.assertEqual(report["paper_consistency"]["status"], "NOT_ASSESSED")
        self.assertNotIn("paper/paper.md", manifest["input_hashes"])

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
