"""Ticket 02: dual-lane repair queue with Agent-quality findings."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
sys.path.insert(0, str(REVIEW_SCRIPTS))

import artifact_schema  # noqa: E402
import deterministic_contract  # noqa: E402
import finalize_audit_output  # noqa: E402
import repair_findings as repair_queue  # noqa: E402
import run_review  # noqa: E402


def _sha256_text(text: str) -> str:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def _package(root: Path) -> Path:
    package = root / "paper-demo"
    (package / "tests").mkdir(parents=True)
    (package / "paper").mkdir(parents=True)
    instruction = (
        "Write outputs/bandgap.json with key bandgap_eV.\n"
        "Face-centred cubic copper (Cu) phonon endpoint.\n"
    )
    checker = (
        "def score(payload):\n"
        "    try:\n"
        "        return float(payload['bandgap_eV'])\n"
        "    except Exception:\n"
        "        return 1.0\n"
    )
    (package / "instruction.md").write_text(instruction, encoding="utf-8")
    (package / "tests/checker.py").write_text(checker, encoding="utf-8")
    (package / "tests/test.sh").write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
    (package / "tests/grading_spec.json").write_text(
        json.dumps({"pass_threshold": 0.8}), encoding="utf-8"
    )
    (package / "paper/paper.md").write_text(
        "The band gap is measured for Cu.\n", encoding="utf-8"
    )
    (package / "paper/images_manifest.json").write_text(
        json.dumps({"images": []}), encoding="utf-8"
    )
    return package


class AgentQualityRepairQueueTests(unittest.TestCase):
    def test_repair_scopes_include_required_taxonomy(self) -> None:
        required = {
            "DETERMINISTIC_WIRING",
            "CHECKER_ROBUSTNESS",
            "INSTRUCTION_CONTRACT",
            "SCORING_SEMANTICS",
            "DIRECT_INPUT_REFERENCE",
            "SCIENCE_SEMANTICS",
        }
        self.assertTrue(required.issubset(repair_queue.REPAIR_SCOPES))
        self.assertEqual(
            artifact_schema.REPAIR_FINDINGS_SCHEMA_VERSION,
            "materials-repair-findings/1.0",
        )

    def test_agent_finding_never_fabricates_deterministic_check(self) -> None:
        finding = {
            "finding_id": "FINDING-001",
            "title": "ADVERSARIAL_OUTPUT_PASSES",
            "severity": "HIGH",
            "status": "OPEN",
            "repairable": True,
            "lane": "quality_results",
            "evidence": {"fixture_source_kind": "SCHEMA_SHAPED"},
            "affected_files": ["tests/checker.py"],
        }
        annotated = repair_queue.annotate_repair_metadata([finding])[0]
        self.assertIsNone(annotated.get("deterministic_check"))
        self.assertEqual(annotated["repair_lane"], "agent_quality")
        self.assertEqual(annotated["repair_scope"], "CHECKER_ROBUSTNESS")
        self.assertEqual(annotated["dimension"], "C07")

    def test_validate_repair_findings_requires_exact_citation_and_hash(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = _package(Path(temporary))
            checker_text = (package / "tests/checker.py").read_text(
                encoding="utf-8"
            )
            quote = "except Exception:\n        return 1.0"
            entry = {
                "finding_id": "AQ-checker-nan-bypass-001",
                "lane": "agent_quality",
                "repair_lane": "agent_quality",
                "repair_scope": "CHECKER_ROBUSTNESS",
                "severity": "HIGH",
                "status": "OPEN",
                "repairable": True,
                "dimension": "C04",
                "title": "CHECKER_NONFINITE_BYPASS",
                "observed_fact": (
                    "Checker returns full credit on exception paths."
                ),
                "evidence": [
                    {
                        "package_file": "tests/checker.py",
                        "package_quote": quote,
                        "source_hash": _sha256_text(checker_text),
                    }
                ],
            }
            normalized = repair_queue.validate_repair_findings(
                package, [entry]
            )
            self.assertEqual(len(normalized), 1)
            self.assertEqual(
                normalized[0]["repair_scope"], "CHECKER_ROBUSTNESS"
            )

            bad_hash = json.loads(json.dumps(entry))
            bad_hash["evidence"][0]["source_hash"] = "sha256:" + ("0" * 64)
            with self.assertRaisesRegex(ValueError, "source_hash"):
                repair_queue.validate_repair_findings(package, [bad_hash])

            escaped = json.loads(json.dumps(entry))
            escaped["evidence"][0]["package_file"] = "../secret.txt"
            with self.assertRaisesRegex(ValueError, "package path"):
                repair_queue.validate_repair_findings(package, [escaped])

            bad_dim = json.loads(json.dumps(entry))
            bad_dim["dimension"] = "C99"
            with self.assertRaisesRegex(ValueError, "dimension"):
                repair_queue.validate_repair_findings(package, [bad_dim])

            fabricated_d = json.loads(json.dumps(entry))
            fabricated_d["deterministic_check"] = "D3"
            with self.assertRaisesRegex(ValueError, "deterministic_check"):
                repair_queue.validate_repair_findings(
                    package, [fabricated_d]
                )

    def test_open_repairable_agent_finding_routes_repair_queue_when_d_clean(
        self,
    ) -> None:
        findings = deterministic_contract.annotate_findings(
            repair_queue.annotate_repair_metadata(
                [
                    {
                        "finding_id": "FINDING-001",
                        "title": "ADVERSARIAL_OUTPUT_PASSES",
                        "severity": "HIGH",
                        "status": "OPEN",
                        "repairable": True,
                        "lane": "quality_results",
                        "evidence": {
                            "fixture_source_kind": "SCHEMA_SHAPED"
                        },
                        "affected_files": ["tests/checker.py"],
                        "affected_locations": [
                            {
                                "file": "tests/checker.py",
                                "line": 1,
                                "quote": "return 1.0",
                            }
                        ],
                        "observed_fact": "Adversarial output still passes.",
                        "impact": "Checker fairness defect.",
                        "minimal_repair": "Reject adversarial credit.",
                        "retest": "Re-run adversarial probe.",
                    }
                ]
            )
        )
        contract = deterministic_contract.evaluate_deterministic_contract(
            normalized_instruction_contract={},
            grading_contract={},
            checker_analysis={
                "d6_core_output_scoring": {"status": "PROVEN"}
            },
            package_roles={
                "instruction.md": "ok",
                "tests/grading_spec.json": "ok",
                "tests/checker.py": "ok",
                "tests/test.sh": "ok",
                "oracle_entrypoint": "ok",
            },
            findings=findings,
        )
        self.assertEqual(contract["repair_summary"]["state"], "CLEAN")
        self.assertEqual(
            contract["repair_summary"]["required_finding_ids"], []
        )

        agent_entries = repair_queue.build_agent_repair_findings(findings)
        self.assertEqual(len(agent_entries), 1)
        self.assertEqual(agent_entries[0]["lane"], "agent_quality")
        self.assertIsNone(agent_entries[0].get("deterministic_check"))

        complete = repair_queue.build_complete_open_repair_queue(
            contract, findings
        )
        self.assertEqual(
            [item["finding_id"] for item in complete["open_findings"]],
            ["FINDING-001"],
        )
        self.assertEqual(complete["open_findings"][0]["lane"], "agent_quality")

        verdict, reason = repair_queue.apply_agent_quality_repair_gate(
            verdict="PASS",
            score=92,
            hard_gate=False,
            evidence_gaps=[],
            findings=findings,
        )
        self.assertEqual(verdict, "CONDITIONAL")
        self.assertIn("Agent-quality", reason or "")
        self.assertEqual(
            finalize_audit_output.ROUTES[verdict], "REPAIR_QUEUE"
        )

    def test_hard_gate_and_evidence_gap_keep_non_repair_routes(self) -> None:
        findings = [
            {
                "finding_id": "FINDING-001",
                "title": "ADVERSARIAL_OUTPUT_PASSES",
                "severity": "HIGH",
                "status": "OPEN",
                "repairable": True,
                "lane": "agent_quality",
                "repair_lane": "agent_quality",
                "repair_scope": "CHECKER_ROBUSTNESS",
            }
        ]
        reject, _ = repair_queue.apply_agent_quality_repair_gate(
            verdict="REJECT",
            score=40,
            hard_gate=True,
            evidence_gaps=[],
            findings=findings,
        )
        self.assertEqual(reject, "REJECT")
        self.assertEqual(
            finalize_audit_output.ROUTES[reject], "QUARANTINE"
        )

        pending, _ = repair_queue.apply_agent_quality_repair_gate(
            verdict="NOT_ASSESSABLE",
            score=None,
            hard_gate=False,
            evidence_gaps=["C04"],
            findings=findings,
        )
        self.assertEqual(pending, "NOT_ASSESSABLE")
        self.assertEqual(
            finalize_audit_output.ROUTES[pending], "EVIDENCE_PENDING"
        )

    def test_agent_contract_pending_blocked_by_open_agent_finding(self) -> None:
        machine = {
            "repair_summary": {"state": "NOT_APPLICABLE"},
            "checks": [
                {
                    "check_id": "D1",
                    "status": "NOT_ASSESSABLE",
                    "proven_finding_ids": [],
                    "blocking_finding_ids": [],
                }
            ],
        }
        report = {
            "hard_gates": [{"code": "NON_MATERIALS_TASK", "status": "PASS"}],
            "findings": [
                {
                    "finding_id": "FINDING-001",
                    "lane": "agent_quality",
                    "status": "OPEN",
                    "repairable": True,
                    "severity": "HIGH",
                    "title": "CHECKER_NONFINITE_BYPASS",
                }
            ],
        }
        self.assertFalse(
            run_review.agent_contract_pending_eligible(machine, report)
        )

    def test_dual_lane_assessment_accepts_authored_repair_findings(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = _package(Path(temporary))
            checker_text = (package / "tests/checker.py").read_text(
                encoding="utf-8"
            )
            quote = "except Exception:\n        return 1.0"
            assessment_path = Path(temporary) / "agent_assessment.json"
            taxonomy = {
                "computation_task": ["声子与晶格动力学"],
                "research_domain": ["基础材料研究与材料发现"],
                "material_system": {
                    "primary": "金属与合金",
                    "secondary": [],
                },
            }
            # Minimal labels that match validate_taxonomy against the fixture
            # taxonomy file — use quotes present in instruction.md.
            instruction_quote = "Face-centred cubic copper (Cu) phonon endpoint."
            assessment = {
                "schema_version": "materials-agent-assessment/2.0",
                "materials_qualification": {
                    "classification": "MAT_CORE",
                    "rationale": "Materials phonon endpoint on Cu.",
                    "evidence": [
                        {
                            "axis": axis,
                            "package_file": "instruction.md",
                            "package_quote": instruction_quote,
                        }
                        for axis in (
                            "object",
                            "data",
                            "operation",
                            "endpoint",
                            "domain_dependence",
                        )
                    ],
                },
                "taxonomy": taxonomy,
                "taxonomy_evidence": [
                    {
                        "dimension": "computation_task",
                        "label": "声子与晶格动力学",
                        "package_file": "instruction.md",
                        "package_quote": instruction_quote,
                    },
                    {
                        "dimension": "research_domain",
                        "label": "基础材料研究与材料发现",
                        "package_file": "instruction.md",
                        "package_quote": instruction_quote,
                    },
                    {
                        "dimension": "material_system.primary",
                        "label": "金属与合金",
                        "package_file": "instruction.md",
                        "package_quote": instruction_quote,
                    },
                ],
                "reproduction_type": "METHOD_REIMPLEMENTATION",
                "dimensions": {
                    name: {
                        "status": "PASS",
                        "rationale": "Aligned with the paper band-gap claim.",
                        "evidence": [
                            {
                                "paper_quote": "The band gap is measured for Cu.",
                                "package_file": "instruction.md",
                                "package_quote": instruction_quote,
                            }
                        ],
                    }
                    for name in (
                        "instruction_fidelity",
                        "data_fidelity",
                        "method_fidelity",
                        "gold_provenance",
                        "checker_fidelity",
                    )
                },
                "repair_findings": [
                    {
                        "finding_id": "AQ-checker-nan-bypass-001",
                        "lane": "agent_quality",
                        "repair_lane": "agent_quality",
                        "repair_scope": "CHECKER_ROBUSTNESS",
                        "severity": "HIGH",
                        "status": "OPEN",
                        "repairable": True,
                        "dimension": "C04",
                        "title": "CHECKER_NONFINITE_BYPASS",
                        "observed_fact": (
                            "Checker returns full credit on exception paths."
                        ),
                        "evidence": [
                            {
                                "package_file": "tests/checker.py",
                                "package_quote": quote,
                                "source_hash": _sha256_text(checker_text),
                            }
                        ],
                    }
                ],
            }
            assessment_path.write_text(
                json.dumps(assessment), encoding="utf-8"
            )
            normalized = run_review.validate_agent_assessment(
                package, assessment_path
            )
            self.assertEqual(len(normalized["repair_findings"]), 1)
            self.assertEqual(
                normalized["repair_findings"][0]["finding_id"],
                "AQ-checker-nan-bypass-001",
            )
            self.assertFalse(
                any(
                    path.name.endswith(".json")
                    and "benchmark_audit" in str(path)
                    for path in package.rglob("*")
                )
            )

    def test_example_checker_fairness_queue_shape(self) -> None:
        """Document the REPAIR_QUEUE shape when D is CLEAN."""

        findings = repair_queue.annotate_repair_metadata(
            [
                {
                    "finding_id": "AQ-checker-nan-bypass-001",
                    "title": "CHECKER_NONFINITE_BYPASS",
                    "severity": "HIGH",
                    "status": "OPEN",
                    "repairable": True,
                    "lane": "agent_quality",
                    "affected_files": ["tests/checker.py"],
                    "affected_locations": [
                        {
                            "file": "tests/checker.py",
                            "line": 5,
                            "quote": "return 1.0",
                        }
                    ],
                    "observed_fact": (
                        "except Exception paths return 1.0 full credit."
                    ),
                    "evidence": {},
                }
            ]
        )
        contract = {
            "repair_summary": {
                "state": "CLEAN",
                "required_findings": [],
                "required_finding_ids": [],
            }
        }
        queue = repair_queue.build_complete_open_repair_queue(
            contract, findings
        )
        self.assertEqual(queue["deterministic_state"], "CLEAN")
        self.assertEqual(queue["deterministic_finding_ids"], [])
        entry = queue["open_findings"][0]
        self.assertEqual(entry["finding_id"], "AQ-checker-nan-bypass-001")
        self.assertEqual(entry["lane"], "agent_quality")
        self.assertEqual(entry["repair_scope"], "CHECKER_ROBUSTNESS")
        self.assertIsNone(entry["deterministic_check"])
        self.assertEqual(entry["publication_hint"], "REAUDIT_REQUIRED")
        verdict, _ = repair_queue.apply_agent_quality_repair_gate(
            verdict="PASS",
            score=90,
            hard_gate=False,
            evidence_gaps=[],
            findings=findings,
        )
        self.assertEqual(verdict, "CONDITIONAL")
        self.assertEqual(
            finalize_audit_output.ROUTES[verdict], "REPAIR_QUEUE"
        )
