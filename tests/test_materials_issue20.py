from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tests.test_materials_benchmark_review_e1 import (
    SOURCE_PACKAGE,
    bind_public_fixture,
    copy_source_package,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER_SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-review"
    / "scripts"
)
if str(RUNNER_SCRIPTS) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(RUNNER_SCRIPTS))
REPAIR_SCRIPTS = (
    REPO_ROOT
    / ".cursor"
    / "skills"
    / "materials-benchmark-repair"
    / "scripts"
)
if str(REPAIR_SCRIPTS) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(REPAIR_SCRIPTS))

import dynamic_checker_probe  # noqa: E402
import finalize_audit_output  # noqa: E402
import probe_resources as resource_probe  # noqa: E402
import run_review  # noqa: E402
import run_fast_e1_batch as fast_batch  # noqa: E402
from run_repair import report_configuration, run_equal_depth_review  # noqa: E402


def usable_result(case: str) -> dict[str, object]:
    return {
        "case": case,
        "crashed": False,
        "reward": 1.0,
        "breakdown": {"score": 1.0, "_errors": {}},
    }


class MaterialsIssue20Tests(unittest.TestCase):
    def test_oracle_checker_values_never_persist(self) -> None:
        secret = "ORACLE-CHECKER-SECRET-987654321.12345"
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "solution/solve.sh").write_text(
                "#!/usr/bin/env bash\n"
                "mkdir -p \"${OUTPUT_DIR:-/app/outputs}\"\n"
                "printf 'direction,mode,k,frequency\\n"
                "100,L,0,987654321.12345\\n' "
                "> \"${OUTPUT_DIR:-/app/outputs}/dispersion_curves.csv\"\n",
                encoding="utf-8",
            )
            (package / "tests/checker.py").write_text(
                "import json\n"
                "from pathlib import Path\n"
                "logs = Path('/logs/verifier')\n"
                "logs.mkdir(parents=True, exist_ok=True)\n"
                "output = Path('/app/outputs/dispersion_curves.csv')\n"
                "present = output.is_file()\n"
                "oracle_case = present and '987654321.12345' in output.read_text()\n"
                "if oracle_case:\n"
                "    print(" + repr(secret) + ")\n"
                "(logs / 'reward.txt').write_text('1.0' if present else '0.0')\n"
                "(logs / 'breakdown.json').write_text(json.dumps({"
                "'_errors': {}, **({'secret': "
                + repr(secret)
                + "} if oracle_case else {})}))\n",
                encoding="utf-8",
            )

            run_review.run_review(package, known_valid_output=None)

            checker_path = package / "benchmark_audit/checker_tests.json"
            report_path = package / "benchmark_audit/audit_report.json"
            checker_text = checker_path.read_text(encoding="utf-8")
            report_text = report_path.read_text(encoding="utf-8")
            self.assertNotIn(secret, checker_text)
            self.assertNotIn(secret, report_text)
            checker = json.loads(checker_text)
            oracle = next(
                item
                for item in checker["tests"]
                if item["test_type"] == "positive_oracle"
            )
            self.assertIsNone(oracle["observed_score"])
            self.assertNotIn("breakdown", oracle["evidence"])
            self.assertNotIn("stdout", oracle["evidence"])
            self.assertNotIn("stderr", oracle["evidence"])
            self.assertNotIn("reward", oracle["evidence"])

    def test_authoritative_review_rejects_non_e1_execution(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)

            with self.assertRaisesRegex(ValueError, "E1-only"):
                run_review.run_review(
                    package,
                    known_valid_output=None,
                    execution_level="E2",
                )

    def test_authoritative_report_publishes_checker_runtime_provenance(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)

            run_review.run_review(package, known_valid_output=None)
            report = json.loads(
                (
                    package / "benchmark_audit/audit_report.json"
                ).read_text(encoding="utf-8")
            )

            self.assertEqual(
                report["checker_runtime"]["verifier_entrypoint"],
                "tests/test.sh",
            )
            self.assertEqual(
                report["checker_runtime"]["runtime_provenance"],
                "audit-host-copy",
            )
            self.assertFalse(
                report["checker_runtime"]["direct_checker_harness"]
            )
            self.assertFalse(
                report["execution_evidence"]["scientific_reproduction"]
            )

    def test_repair_reaudit_configuration_is_e1_only(self) -> None:
        with self.assertRaisesRegex(ValueError, "E1-only"):
            report_configuration(
                {
                    "configuration": {
                        "paper_mode": "no_paper",
                        "execution_level": "E2",
                    }
                }
            )

    def test_repair_reaudit_rejects_future_execution_plan(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot enter"):
            run_equal_depth_review(
                Path("."),
                {
                    "configuration": {
                        "paper_mode": "no_paper",
                        "execution_level": "E1",
                    }
                },
                {"e2_smoke_plan": "/tmp/future-plan.json"},
            )

    def test_public_fixture_is_not_the_positive_control(self) -> None:
        results = [
            usable_result("known_valid_public"),
            usable_result("quality_gradient_small_error"),
            usable_result("quality_gradient_large_error"),
            usable_result("metamorphic_equivalent_representation"),
        ]

        flags = dynamic_checker_probe.probe_assessment_flags(results)

        self.assertFalse(flags["positive"])
        self.assertTrue(flags["discrimination"])
        self.assertTrue(flags["equivalence"])

    def test_checker_cases_record_test_sh_audit_host_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            output = Path(temporary) / "checker.json"
            source_before = {
                path.relative_to(package): path.read_bytes()
                for path in package.rglob("*")
                if path.is_file()
            }

            result = dynamic_checker_probe.dynamic_checker_probe(
                package, output, known_valid_output=None
            )

            self.assertTrue(result["tests"])
            self.assertEqual(
                result["runtime"]["verifier_entrypoint"],
                "tests/test.sh",
            )
            self.assertEqual(
                result["runtime"]["runtime_provenance"],
                "audit-host-copy",
            )
            self.assertFalse(result["runtime"]["direct_checker_harness"])
            for case in result["tests"]:
                self.assertEqual(
                    case["evidence"]["verifier_entrypoint"],
                    "tests/test.sh",
                )
                self.assertEqual(
                    case["evidence"]["runtime_provenance"],
                    "audit-host-copy",
                )
            self.assertEqual(
                source_before,
                {
                    path.relative_to(package): path.read_bytes()
                    for path in package.rglob("*")
                    if path.is_file()
                },
            )

    def test_audit_host_missing_dependency_is_not_a_package_defect(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            checker = package / "tests/checker.py"
            checker.write_text(
                "import issue20_missing_audit_host_dependency\n"
                + checker.read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            dockerfile = package / "environment/Dockerfile"
            dockerfile.write_text(
                dockerfile.read_text(encoding="utf-8")
                + "\n# Harbor image supplies the checker dependency.\n",
                encoding="utf-8",
            )

            result = dynamic_checker_probe.dynamic_checker_probe(
                package,
                Path(temporary) / "checker.json",
                known_valid_output=None,
            )

            self.assertEqual(result["runtime"]["status"], "NOT_ASSESSABLE")
            self.assertEqual(
                result["runtime"]["runtime_provenance"], "not-assessable"
            )
            self.assertFalse(
                {"CHECKER_CRASH", "CHECKER_RESULT_UNUSABLE"}
                & {finding["code"] for finding in result["findings"]}
            )

    def test_verifier_dependency_install_failure_is_not_a_package_defect(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            (package / "tests/test.sh").write_text(
                "#!/usr/bin/env bash\n"
                "echo 'Could not find a version that satisfies the requirement' >&2\n"
                "exit 1\n",
                encoding="utf-8",
            )

            result = dynamic_checker_probe.dynamic_checker_probe(
                package,
                Path(temporary) / "checker.json",
                known_valid_output=None,
            )

            self.assertEqual(result["runtime"]["status"], "NOT_ASSESSABLE")
            self.assertFalse(
                {"CHECKER_CRASH", "CHECKER_RESULT_UNUSABLE"}
                & {finding["code"] for finding in result["findings"]}
            )

    def test_report_contains_unweighted_first_class_qa_axes(self) -> None:
        findings = [
            {
                "title": "INSTRUCTION_ONLY_OUTPUT",
                "severity": "MEDIUM",
                "observed_fact": "The final output is not contracted.",
                "affected_locations": [
                    {"file": "instruction.md", "line": 4, "quote": "result"}
                ],
            },
            {
                "title": "OUTPUT_NOT_CONTRACTED",
                "severity": "HIGH",
                "observed_fact": "The checker output is not contracted.",
                "affected_locations": [
                    {
                        "file": "tests/grading_spec.json",
                        "line": 8,
                        "quote": "outputs",
                    }
                ],
            },
        ]
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            findings,
            checker_result={
                "tests": [],
                "solution_content_inspected": False,
                "solution_oracle": {"executed": False},
            },
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(
            set(axes),
            {
                "factual_accuracy",
                "answer_leakage",
                "instruction_completeness",
                "checker_instruction_consistency",
            },
        )
        for axis in axes.values():
            self.assertEqual(
                set(axis),
                {"status", "evidence", "locations", "limitations"},
            )
            self.assertNotIn("points_earned", axis)
            self.assertIsInstance(axis["evidence"], list)
            self.assertIsInstance(axis["locations"], list)
            self.assertIsInstance(axis["limitations"], list)
        self.assertEqual(
            axes["instruction_completeness"]["status"], "FAIL"
        )
        self.assertEqual(
            axes["checker_instruction_consistency"]["status"], "FAIL"
        )
        self.assertEqual(
            axes["factual_accuracy"]["status"], "NOT_ASSESSABLE"
        )
        self.assertEqual(axes["answer_leakage"]["status"], "NOT_ASSESSABLE")

    def test_factual_uncertainty_has_its_own_qa_axis(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "SCIENTIFIC_TARGET_INVALID",
                    "observed_fact": "The scientific target is contradictory.",
                    "affected_locations": [
                        {"file": "instruction.md", "line": 3, "quote": "target"}
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(axes["factual_accuracy"]["status"], "FAIL")
        self.assertNotIn("points_earned", axes["factual_accuracy"])

    def test_external_accessibility_is_not_factual_inaccuracy(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
                    "observed_fact": "A fixed non-equivalent input is unavailable.",
                    "affected_locations": [
                        {"file": "instruction.md", "line": 7, "quote": "dataset"}
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(
            axes["factual_accuracy"]["status"], "NOT_ASSESSABLE"
        )

    def test_confirmed_direct_input_barriers_fail_availability_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "instruction.md").write_text(
                "Use the fixed indispensable input.", encoding="utf-8"
            )
            for status in (
                "REQUIRES_AUTH",
                "REQUIRES_LICENSE",
                "IDENTITY_MISMATCH",
            ):
                with self.subTest(status=status):
                    finding = finalize_audit_output.normalized_finding(
                        root,
                        {
                            "severity": "FATAL",
                            "code": "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
                            "message": "The solving Agent cannot access the input.",
                            "affected_files": ["instruction.md"],
                            "evidence": {"status": status},
                        },
                        "FINDING-001",
                        "RESOURCE",
                        "RESOURCE_USABILITY",
                    )
                    gates = finalize_audit_output.hard_gate_results(
                        root, [finding], []
                    )
                    direct = next(
                        gate
                        for gate in gates
                        if gate["code"]
                        == "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
                    )
                    self.assertEqual(direct["status"], "FAIL")

    def test_temporary_direct_input_gap_is_not_assessable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "instruction.md").write_text(
                "Use the fixed indispensable input.", encoding="utf-8"
            )
            finding = finalize_audit_output.normalized_finding(
                root,
                {
                    "severity": "HIGH",
                    "code": "INDISPENSABLE_DIRECT_INPUT_TRANSIENT_FAILURE",
                    "message": "The audit host had a temporary network failure.",
                    "affected_files": ["instruction.md"],
                    "evidence": {"status": "TRANSIENT_FAILURE"},
                },
                "FINDING-001",
                "RESOURCE",
                "RESOURCE_USABILITY",
            )

            gates = finalize_audit_output.hard_gate_results(
                root, [finding], []
            )
            direct = next(
                gate
                for gate in gates
                if gate["code"] == "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
            )
            self.assertEqual(direct["status"], "NOT_ASSESSABLE")

    def test_multiline_direct_input_declaration_is_parsed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "instruction.md").write_text(
                "### Inputs\n"
                "- Direct input declaration:\n"
                "  This dataset is fixed by the instruction.\n"
                "  It is indispensable for the requested answer.\n"
                "  Its identity must be preserved.\n"
                "  It must not be regenerated by the solver.\n"
                "  Additional validation notes apply.\n"
                "  No scientifically equivalent source is allowed.\n"
                "  Download URL:\n"
                "  https://example.invalid/fixed-data.csv\n",
                encoding="utf-8",
            )
            output = root / "resources.json"
            probe_report = {
                "resource_id": "direct",
                "verified_level": "L4",
                "required_level": "L4",
                "status": "AVAILABLE",
                "identity_match": True,
                "probe": {},
            }
            with mock.patch.object(
                resource_probe,
                "probe_item",
                return_value=(probe_report, []),
            ):
                result = resource_probe.probe_resources(
                    root, output, timeout=1
                )

            self.assertEqual(len(result["resources"]), 1)
            self.assertEqual(
                result["resources"][0]["declaration_source"],
                "instruction.md",
            )

    def test_separate_sibling_bullet_does_not_inherit_flags(self) -> None:
        instruction = (
            "### Direct inputs\n"
            "- The indispensable direct input has no equivalent source.\n"
            "- Locator: https://example.invalid/unrelated.csv\n"
        )

        self.assertEqual(
            resource_probe.instruction_direct_inputs(instruction), []
        )

    def test_heading_does_not_make_optional_sibling_required(self) -> None:
        instruction = (
            "### Indispensable direct inputs with no equivalent\n"
            "- Optional background: "
            "https://example.invalid/background.html\n"
            "- The required dataset is an indispensable direct input with "
            "no equivalent: "
            "[download](https://example.invalid/required.csv)\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(
            [item["access"]["url"] for item in resources],
            ["https://example.invalid/required.csv"],
        )

    def test_required_dataset_and_optional_docs_share_paragraph(self) -> None:
        instruction = (
            "### Direct inputs\n"
            "Dataset: indispensable, with no equivalent source, "
            "[download](https://example.invalid/data.csv); "
            "Docs: optional "
            "[guide](https://example.invalid/guide.html).\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(
            [item["access"]["url"] for item in resources],
            ["https://example.invalid/data.csv"],
        )

    def test_optional_docs_metadata_does_not_attach_to_dataset(self) -> None:
        docs_checksum = "b" * 64
        instruction = (
            "### Direct inputs\n"
            "Dataset: indispensable, no equivalent source, "
            "[download](https://example.invalid/data.csv); "
            "Docs: optional "
            "[guide](https://example.invalid/guide.html), "
            f"SHA-256: {docs_checksum}, and license authorization is not "
            "provided to the solving agent, Identity: docs-v2.\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(len(resources), 1)
        self.assertEqual(
            resources[0]["access"],
            {
                "method": "url",
                "url": "https://example.invalid/data.csv",
            },
        )

    def test_dataset_scoped_checksum_and_license_are_retained(self) -> None:
        dataset_checksum = "a" * 64
        instruction = (
            "### Resources\n"
            "- Dataset:\n"
            "  - Criticality: indispensable\n"
            "  - Equivalence: none\n"
            "  - Locator: https://example.invalid/licensed-data.csv\n"
            f"  - SHA-256: {dataset_checksum}\n"
            "  - Identity: dataset-v1\n"
            "  - License authorization is not provided to the solving "
            "agent.\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(len(resources), 1)
        self.assertEqual(
            resources[0]["access"],
            {
                "method": "license",
                "url": "https://example.invalid/licensed-data.csv",
                "checksum": f"sha256:{dataset_checksum}",
                "expected_identity": "dataset-v1",
                "license": "instruction-declared-license",
                "authorization_provided": False,
            },
        )

    def test_dataset_scoped_auth_metadata_is_retained(self) -> None:
        instruction = (
            "### Resources\n"
            "- Dataset:\n"
            "  - Criticality: indispensable\n"
            "  - Equivalence: none\n"
            "  - Locator: https://example.invalid/private-data.csv\n"
            "  - Auth: required\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)
        report, findings = resource_probe.probe_item(
            Path("."),
            resources[0],
            timeout=1,
            allow_private_network=False,
        )

        self.assertEqual(resources[0]["access"]["method"], "auth")
        self.assertEqual(report["status"], "REQUIRES_AUTH")
        self.assertIn(
            "RESOURCE_REQUIRES_AUTH",
            {item["code"] for item in findings},
        )

    def test_reversed_urls_keep_metadata_with_their_clause(self) -> None:
        dataset_checksum = "a" * 64
        docs_checksum = "b" * 64
        instruction = (
            "### Direct inputs\n"
            "Docs: optional https://example.invalid/guide.html, "
            f"SHA-256: {docs_checksum}, license authorization is not "
            "provided to the solving agent; "
            "Dataset: indispensable, no equivalent, "
            "https://example.invalid/data.csv, "
            f"SHA-256: {dataset_checksum}.\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(
            resources[0]["access"],
            {
                "method": "url",
                "url": "https://example.invalid/data.csv",
                "checksum": f"sha256:{dataset_checksum}",
            },
        )

    def test_optional_first_and_required_multi_link_clause(self) -> None:
        instruction = (
            "### Direct inputs\n"
            "Docs: optional [guide](https://example.invalid/guide.html) "
            "Dataset: indispensable, no equivalent source, "
            "[primary](https://example.invalid/primary.csv) and "
            "[mirror](https://example.invalid/mirror.csv).\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(
            [item["access"]["url"] for item in resources],
            [
                "https://example.invalid/primary.csv",
                "https://example.invalid/mirror.csv",
            ],
        )

    def test_ambiguous_mixed_url_clause_is_not_a_direct_input(self) -> None:
        instruction = (
            "### Direct inputs\n"
            "Dataset required with no equivalent and optional docs links: "
            "[first](https://example.invalid/ambiguous-a.csv) "
            "[second](https://example.invalid/ambiguous-b.html).\n"
        )

        self.assertEqual(
            resource_probe.instruction_direct_inputs(instruction), []
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "instruction.md").write_text(
                instruction, encoding="utf-8"
            )
            result = resource_probe.probe_resources(
                root, root / "resources.json", timeout=1
            )
            direct_gate = next(
                gate
                for gate in finalize_audit_output.hard_gate_results(
                    root, result["findings"], []
                )
                if gate["code"]
                == "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
            )
            self.assertNotEqual(direct_gate["status"], "FAIL")

    def test_nested_metadata_forms_one_direct_input_declaration(self) -> None:
        dataset_checksum = "a" * 64
        docs_checksum = "b" * 64
        instruction = (
            "### Resources\n"
            "- Dataset metadata:\n"
            "  - Criticality: indispensable and required\n"
            "  - Scientific equivalence: no equivalent source\n"
            "  - Locator: "
            "[download](https://example.invalid/nested-required.csv)\n"
            f"  - SHA-256: {dataset_checksum}\n"
            "  - Docs:\n"
            "    - Optional: true\n"
            "    - Locator: "
            "[open](https://example.invalid/nested-guide.html)\n"
            f"    - SHA-256: {docs_checksum}\n"
            "    - License authorization is not provided to the solving "
            "agent.\n"
            "  - Non-normative example:\n"
            "    ```text\n"
            "    https://example.invalid/example-only.csv\n"
            "    ```\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(
            [item["access"]["url"] for item in resources],
            ["https://example.invalid/nested-required.csv"],
        )
        self.assertEqual(
            resources[0]["access"]["checksum"],
            f"sha256:{dataset_checksum}",
        )
        self.assertEqual(resources[0]["access"]["method"], "url")

    def test_explicit_section_wide_declaration_applies_to_items(self) -> None:
        instruction = (
            "### Direct input resources\n"
            "All resources listed below are indispensable and have no "
            "equivalent source.\n\n"
            "- Dataset A: "
            "[download](https://example.invalid/required-a.csv)\n"
            "- Dataset B: https://example.invalid/required-b.csv\n"
            "- Docs: https://example.invalid/required-docs.html\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(
            [item["access"]["url"] for item in resources],
            [
                "https://example.invalid/required-a.csv",
                "https://example.invalid/required-b.csv",
                "https://example.invalid/required-docs.html",
            ],
        )

        heading_wide = (
            "### Every direct input in this section is indispensable and "
            "has no equivalent\n"
            "- Dataset C: https://example.invalid/required-c.csv\n"
        )
        self.assertEqual(
            [
                item["access"]["url"]
                for item in resource_probe.instruction_direct_inputs(
                    heading_wide
                )
            ],
            ["https://example.invalid/required-c.csv"],
        )

    def test_explicit_shared_metadata_applies_to_both_urls(self) -> None:
        shared_checksum = "c" * 64
        instruction = (
            "### Resources\n"
            "- Dataset mirrors: indispensable, no equivalent source. "
            "Both URLs share "
            f"SHA-256: {shared_checksum} and license authorization is not "
            "provided to the solving agent: "
            "https://example.invalid/mirror-a.csv "
            "https://example.invalid/mirror-b.csv\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(len(resources), 2)
        for resource in resources:
            self.assertEqual(resource["access"]["method"], "license")
            self.assertEqual(
                resource["access"]["checksum"],
                f"sha256:{shared_checksum}",
            )
            self.assertFalse(
                resource["access"]["authorization_provided"]
            )

    def test_ambiguous_shared_metadata_is_not_assigned(self) -> None:
        ambiguous_checksum = "d" * 64
        instruction = (
            "### Resources\n"
            "- Dataset mirrors are indispensable and have no equivalent: "
            "https://example.invalid/ambiguous-a.csv "
            "https://example.invalid/ambiguous-b.csv. "
            f"SHA-256: {ambiguous_checksum}. "
            "Identity: uncertain-artifact. "
            "License authorization is not provided to the solving agent.\n"
        )

        resources = resource_probe.instruction_direct_inputs(instruction)

        self.assertEqual(len(resources), 2)
        for resource in resources:
            access = resource["access"]
            self.assertEqual(access["method"], "url")
            self.assertEqual(
                access["metadata_status"], "NOT_ASSESSABLE"
            )
            self.assertNotIn("checksum", access)
            self.assertNotIn("expected_identity", access)
            self.assertNotIn("license", access)
        with mock.patch.object(
            resource_probe,
            "probe_url_access",
            return_value={
                "verified_level": 4,
                "status": "AVAILABLE",
                "identity_match": None,
                "probe": {},
            },
        ):
            probed = [
                resource_probe.probe_item(
                    Path("."),
                    resource,
                    timeout=1,
                    allow_private_network=False,
                )
                for resource in resources
            ]
        self.assertTrue(
            all(report["status"] == "AVAILABLE" for report, _ in probed)
        )
        self.assertFalse(
            any(
                finding["severity"] == "FATAL"
                for _, findings in probed
                for finding in findings
            )
        )

    def test_package_local_known_valid_fixture_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            fake = package / "tests/fake-public-fixture"
            fake.mkdir()
            (fake / "dispersion_curves.csv").write_text(
                "direction,mode,k,frequency\n100,L,0,0\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "external"):
                dynamic_checker_probe.dynamic_checker_probe(
                    package,
                    Path(temporary) / "checker.json",
                    known_valid_output=fake,
                )

    def test_external_fixture_requires_source_bound_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            fixture = Path(temporary) / "public-fixture"
            fixture.mkdir()
            (fixture / "dispersion_curves.csv").write_text(
                "direction,mode,k,frequency\n100,L,0,0\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "fixture manifest"):
                dynamic_checker_probe.dynamic_checker_probe(
                    package,
                    Path(temporary) / "checker.json",
                    known_valid_output=fixture,
                )

    def test_fixture_manifest_rejects_stale_source_binding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / SOURCE_PACKAGE.name
            copy_source_package(package)
            fixture = Path(temporary) / "public-fixture"
            fixture.mkdir()
            (fixture / "dispersion_curves.csv").write_text(
                "direction,mode,k,frequency\n100,L,0,0\n",
                encoding="utf-8",
            )
            bind_public_fixture(package, fixture)
            instruction = package / "instruction.md"
            instruction.write_text(
                instruction.read_text(encoding="utf-8")
                + "\nA source change invalidates the fixture assessment.\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "source-bound"):
                dynamic_checker_probe.dynamic_checker_probe(
                    package,
                    Path(temporary) / "checker.json",
                    known_valid_output=fixture,
                )

    def test_batch_snapshot_rejects_non_e1_report(self) -> None:
        template = json.loads(
            (
                REPO_ROOT
                / ".cursor/skills/materials-benchmark-review/assets"
                / "audit_report_template.json"
            ).read_text(encoding="utf-8")
        )
        template["configuration"]["execution_level"] = "E2"

        with self.assertRaisesRegex(ValueError, "E1"):
            fast_batch.authoritative_cli_scoring(template)

    def test_batch_excludes_failed_direct_input_gate(self) -> None:
        static = {
            "parse_status": {
                role: "ok" for role in fast_batch.QUALITY_EVIDENCE_ROLES
            },
            "materials_prescreen": {"classification": "MAT_CORE"},
            "issues": [],
        }
        checker = {
            "tests": [
                {
                    "observed_status": "COMPLETED",
                    "evidence": {
                        "runtime_package_contains_solution": False
                    },
                }
            ],
            "usable_reward_count": 1,
            "findings": [],
            "solution_content_inspected": False,
        }

        reasons = fast_batch.exclusion_reasons(
            static,
            checker,
            [],
            materials_class="MAT_CORE",
            hard_gates=[
                {
                    "code": "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE",
                    "status": "FAIL",
                }
            ],
        )

        self.assertIn(
            "HARD_GATE_INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE", reasons
        )
        with self.assertRaisesRegex(ValueError, "usable candidate"):
            fast_batch.validate_authoritative_candidate_state(
                {
                    "state": "E1_USABLE_CANDIDATE",
                    "exclusion_reasons": [],
                },
                {
                    "execution_level": "E1",
                    "hard_gates": [
                        {
                            "code": (
                                "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
                            ),
                            "status": "FAIL",
                        }
                    ],
                },
            )

    def test_semantically_empty_qa_axes_are_rejected(self) -> None:
        empty_axes = {
            name: {
                "status": "PASS",
                "evidence": [],
                "locations": [],
                "limitations": [],
            }
            for name in finalize_audit_output.QA_AXIS_NAMES
        }
        with self.assertRaisesRegex(ValueError, "evidence"):
            finalize_audit_output.validate_qa_axes(empty_axes)

        not_assessable = {
            name: {
                "status": "NOT_ASSESSABLE",
                "evidence": [
                    {
                        "finding_id": "FINDING-001",
                        "observed_fact": "fail",
                        "semantic": "supports_failure",
                    }
                ],
                "locations": [],
                "limitations": [],
            }
            for name in finalize_audit_output.QA_AXIS_NAMES
        }
        with self.assertRaisesRegex(ValueError, "NOT_ASSESSABLE"):
            finalize_audit_output.validate_qa_axes(not_assessable)

    def test_paper_not_assessable_keeps_factual_axis_unavailable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "instruction.md").write_text(
                "Compute a materials property.", encoding="utf-8"
            )

            axes = finalize_audit_output.derive_qa_axes(
                root,
                findings=[],
                checker_result={"tests": [], "solution_oracle": {}},
                contract_map={"requirements": []},
                paper_result={"status": "NOT_ASSESSABLE"},
                materials_assessment={},
            )

            factual = axes["factual_accuracy"]
            self.assertEqual(factual["status"], "NOT_ASSESSABLE")
            self.assertTrue(factual["limitations"])

    def test_pass_qa_axis_rejects_failure_finding_evidence(self) -> None:
        location = {
            "file": "instruction.md",
            "line": 1,
            "quote": "Compute a materials property.",
        }
        axes = {
            name: {
                "status": "PASS",
                "evidence": [
                    {
                        "source": "review",
                        "fact": "The axis passed.",
                        "semantic": "supports_pass",
                    }
                ],
                "locations": [location],
                "limitations": [],
            }
            for name in finalize_audit_output.QA_AXIS_NAMES
        }
        axes["factual_accuracy"]["evidence"] = [
            {
                "finding_id": "FINDING-FAIL-001",
                "observed_fact": "A factual contradiction was confirmed.",
                "semantic": "supports_failure",
            }
        ]

        with self.assertRaisesRegex(ValueError, "PASS.*failure"):
            finalize_audit_output.validate_qa_axes(axes)

    def test_answer_leakage_has_its_own_qa_axis(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "SOLUTION_BOUNDARY_VIOLATION",
                    "observed_fact": "Solution content entered checker runtime.",
                    "affected_locations": [
                        {"file": "solution/", "line": None, "quote": None}
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(axes["answer_leakage"]["status"], "FAIL")
        self.assertNotIn("points_earned", axes["answer_leakage"])

    def test_instruction_incompleteness_has_its_own_qa_axis(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "INSTRUCTION_ONLY_OUTPUT",
                    "observed_fact": "A required final output lacks a contract.",
                    "affected_locations": [
                        {"file": "instruction.md", "line": 4, "quote": "output"}
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(axes["instruction_completeness"]["status"], "FAIL")
        self.assertNotIn("points_earned", axes["instruction_completeness"])

    def test_checker_instruction_mismatch_has_its_own_qa_axis(self) -> None:
        axes = finalize_audit_output.derive_qa_axes(
            Path("."),
            [
                {
                    "title": "OUTPUT_NOT_CONTRACTED",
                    "observed_fact": "The checker reads an undeclared output.",
                    "affected_locations": [
                        {
                            "file": "tests/grading_spec.json",
                            "line": 8,
                            "quote": "output_file",
                        }
                    ],
                }
            ],
            checker_result={"tests": [], "solution_oracle": {}},
            contract_map={"requirements": []},
            paper_result={"status": "NOT_ASSESSED"},
            materials_assessment=None,
        )

        self.assertEqual(
            axes["checker_instruction_consistency"]["status"], "FAIL"
        )
        self.assertNotIn(
            "points_earned", axes["checker_instruction_consistency"]
        )


if __name__ == "__main__":
    unittest.main()
