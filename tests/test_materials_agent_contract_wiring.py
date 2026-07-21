from __future__ import annotations

from copy import deepcopy
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-review/scripts"
REPAIR_SCRIPTS = REPO_ROOT / ".cursor/skills/materials-benchmark-repair/scripts"
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(REPAIR_SCRIPTS))

import agent_contract_wiring  # noqa: E402
import deterministic_contract  # noqa: E402
import finalize_audit_output  # noqa: E402
import run_repair  # noqa: E402


def unavailable_d6_contract() -> dict[str, object]:
    return deterministic_contract.evaluate_deterministic_contract(
        normalized_instruction_contract={},
        grading_contract={},
        checker_analysis={
            "d6_core_output_scoring": {"status": "UNKNOWN"},
        },
        package_roles={},
        findings=[],
    )


def assessment_for(
    machine: dict[str, object],
    *,
    d6_status: str = "PASS",
    d6_evidence: list[dict[str, str]] | None = None,
) -> dict[str, object]:
    evidence = d6_evidence or [
        {
            "source_kind": "DETERMINISTIC_PROBE_ARTIFACT",
            "path": "deterministic_core/probe_results.json",
            "scope": "CONTRACT_WIRING",
            "artifact_digest": "sha256:probe",
        }
    ]
    checks = {
        check_id: {
            "status": d6_status if check_id == "D6" else "NOT_PROVEN",
            "rationale": f"{check_id} contract-wiring adjudication",
            "evidence": evidence if check_id == "D6" else [],
        }
        for check_id in deterministic_contract.CHECK_IDS
    }
    return agent_contract_wiring.make_agent_contract_assessment(
        machine,
        checks,
    )


def passing_dimensions() -> list[dict[str, object]]:
    return [
        {
            "dimension": dimension,
            "weight": weight,
            "points_earned": weight,
            "normalized": 100,
        }
        for dimension, weight in (
            ("C01", 10),
            ("C02", 20),
            ("C03", 20),
            ("C04", 20),
            ("C05", 10),
            ("C06", 10),
            ("C07", 10),
        )
    ]


class MaterialsAgentContractWiringTests(unittest.TestCase):
    def test_assessment_schema_and_machine_digest_binding(self) -> None:
        machine = unavailable_d6_contract()
        assessment = assessment_for(machine)
        validated = agent_contract_wiring.validate_agent_contract_assessment(
            assessment, machine
        )

        self.assertEqual(validated["checks"][-1]["status"], "PASS")
        self.assertEqual(
            validated["machine_contract_digest"], machine["contract_digest"]
        )
        self.assertEqual(
            validated["assessment_digest"],
            agent_contract_wiring.agent_contract_assessment_digest(assessment),
        )

        tampered = dict(assessment)
        tampered["machine_contract_digest"] = "sha256:stale"
        with self.assertRaisesRegex(ValueError, "machine contract digest"):
            agent_contract_wiring.validate_agent_contract_assessment(
                tampered, machine
            )

    def test_forbidden_evidence_surfaces_and_scopes_fail_closed(self) -> None:
        machine = unavailable_d6_contract()
        forbidden_cases = (
            {
                "source_kind": "PAPER",
                "path": "paper/paper.md",
                "scope": "CONTRACT_WIRING",
            },
            {
                "source_kind": "GRADING_SPEC",
                "path": "tests/checker.py",
                "scope": "CONTRACT_WIRING",
            },
            {
                "source_kind": "INSTRUCTION",
                "path": "solution/solve.sh",
                "scope": "CONTRACT_WIRING",
            },
            {
                "source_kind": "INSTRUCTION",
                "path": "instruction.md",
                "scope": "GOLD",
            },
            {
                "source_kind": "INSTRUCTION",
                "path": "instruction.md",
                "scope": "UNITS",
            },
        )
        for evidence in forbidden_cases:
            with self.subTest(evidence=evidence):
                with self.assertRaises(ValueError):
                    assessment_for(machine, d6_evidence=[evidence])

    def test_eligibility_rejects_blockers_gates_runtime_and_dependencies(self) -> None:
        machine_check = unavailable_d6_contract()["checks"][-1]
        eligible = agent_contract_wiring.check_eligibility(machine_check)
        self.assertTrue(eligible["eligible"])

        blocked = dict(machine_check, blocked_by=["D5"])
        self.assertIn(
            "DEPENDENCY_FAILURE",
            agent_contract_wiring.check_eligibility(blocked)["reason_codes"],
        )
        gated = agent_contract_wiring.check_eligibility(
            machine_check,
            hard_gates=[{"check_id": "D6", "status": "FAIL"}],
        )
        self.assertIn("HARD_GATE", gated["reason_codes"])
        contradicted = agent_contract_wiring.check_eligibility(
            machine_check,
            runtime_contradictions=[
                {"check_id": "D6", "usable_runtime_contradiction": True}
            ],
        )
        self.assertIn(
            "USABLE_RUNTIME_CONTRADICTION",
            contradicted["reason_codes"],
        )

    def test_merge_preserves_machine_findings_and_recomputes_clean_summary(self) -> None:
        machine = unavailable_d6_contract()
        assessment = assessment_for(machine)
        effective = agent_contract_wiring.derive_effective_contract(
            machine,
            assessment,
            agent_quality_findings=[
                {
                    "lane": "agent_quality",
                    "finding_id": "quality-1",
                }
            ],
        )

        self.assertEqual(effective["machine_status"]["checks"]["D6"], "NOT_ASSESSABLE")
        self.assertEqual(effective["checks"][-1]["status"], "PASS")
        self.assertEqual(effective["repair_summary"]["state"], "CLEAN")
        self.assertFalse(
            effective["adjudication"]["lane_isolation"][
                "agent_quality_findings_merged"
            ]
        )
        self.assertEqual(
            agent_contract_wiring.validate_effective_contract(effective),
            effective,
        )

    def test_partial_not_proven_does_not_create_effective_clean(self) -> None:
        machine = unavailable_d6_contract()
        assessment = assessment_for(machine, d6_status="NOT_PROVEN")
        effective = agent_contract_wiring.derive_effective_contract(
            machine, assessment
        )

        self.assertEqual(effective["checks"][-1]["status"], "NOT_ASSESSABLE")
        self.assertEqual(effective["repair_summary"]["state"], "NOT_APPLICABLE")
        self.assertFalse(effective["repair_summary"]["complete"])

    def test_machine_fail_and_blocker_cannot_be_suppressed(self) -> None:
        machine = deterministic_contract.evaluate_deterministic_contract(
            normalized_instruction_contract={},
            grading_contract={},
            checker_analysis={
                "d6_core_output_scoring": {"status": "UNKNOWN"},
            },
            package_roles={},
            findings=[
                {
                    "finding_id": "machine-f1",
                    "title": "ZERO_WEIGHT_SCORING_COMPONENT",
                    "status": "OPEN",
                    "repairable": True,
                    "evidence": {},
                }
            ],
        )
        assessment = assessment_for(machine)
        effective = agent_contract_wiring.derive_effective_contract(
            machine, assessment
        )

        d4 = effective["checks"][3]
        self.assertEqual(d4["machine_status"], "FAIL")
        self.assertEqual(d4["status"], "FAIL")
        self.assertEqual(d4["finding_ids"], ["machine-f1"])
        self.assertEqual(effective["repair_summary"]["state"], "REQUIRED")
        self.assertIn(
            "machine-f1",
            effective["repair_summary"]["required_finding_ids"],
        )

    def test_assessment_and_effective_digests_detect_tampering(self) -> None:
        machine = unavailable_d6_contract()
        assessment = assessment_for(machine)
        tampered_assessment = dict(assessment)
        tampered_checks = list(assessment["checks"])
        tampered_checks[-1] = dict(tampered_checks[-1], rationale="changed")
        tampered_assessment["checks"] = tampered_checks
        with self.assertRaisesRegex(ValueError, "assessment digest"):
            agent_contract_wiring.validate_agent_contract_assessment(
                tampered_assessment, machine
            )

        effective = agent_contract_wiring.derive_effective_contract(
            machine, assessment
        )
        tampered_effective = dict(effective)
        tampered_effective["effective_contract_digest"] = "sha256:stale"
        with self.assertRaisesRegex(ValueError, "effective contract digest"):
            agent_contract_wiring.validate_effective_contract(tampered_effective)

    def test_lane_isolation_rejects_quality_scope_and_keeps_quality_out(self) -> None:
        machine = unavailable_d6_contract()
        with self.assertRaisesRegex(ValueError, "outside contract wiring"):
            assessment_for(
                machine,
                d6_evidence=[
                    {
                        "source_kind": "INSTRUCTION",
                        "path": "instruction.md",
                        "scope": "SCIENCE_QUALITY",
                    }
                ],
            )

        assessment = assessment_for(machine)
        effective = agent_contract_wiring.derive_effective_contract(
            machine,
            assessment,
            agent_quality_findings=[
                {
                    "lane": "agent_quality",
                    "finding_id": "quality-only",
                    "status": "FAIL",
                }
            ],
        )
        self.assertNotIn("quality-only", str(effective))

    def test_effective_clean_is_accepted_at_the_publication_gate(self) -> None:
        machine = unavailable_d6_contract()
        assessment = assessment_for(machine)
        effective = agent_contract_wiring.derive_effective_contract(
            machine, assessment
        )

        verdict, reason = deterministic_contract.apply_deterministic_gate(
            verdict="PASS",
            score=90,
            hard_gate=False,
            evidence_gaps=[],
            contract=effective,
        )

        self.assertEqual(verdict, "PASS")
        self.assertIsNone(reason)
        self.assertEqual(effective["repair_summary"]["state"], "CLEAN")

        below_threshold, _ = deterministic_contract.apply_deterministic_gate(
            verdict="PASS",
            score=79,
            hard_gate=False,
            evidence_gaps=[],
            contract=effective,
        )
        self.assertEqual(below_threshold, "CONDITIONAL")

    def test_machine_not_applicable_without_adjudication_stays_unassessable(self) -> None:
        verdict, _ = deterministic_contract.apply_deterministic_gate(
            verdict="PASS",
            score=90,
            hard_gate=False,
            evidence_gaps=[],
            contract=unavailable_d6_contract(),
        )

        self.assertEqual(verdict, "NOT_ASSESSABLE")

    def test_tampered_effective_contract_is_rejected_for_publication(self) -> None:
        machine = unavailable_d6_contract()
        assessment = assessment_for(machine)
        effective = agent_contract_wiring.derive_effective_contract(
            machine, assessment
        )
        tampered = deepcopy(effective)
        tampered["effective_contract_digest"] = "sha256:tampered"

        with self.assertRaisesRegex(ValueError, "effective contract digest"):
            agent_contract_wiring.resolve_publication_contract(
                machine, tampered, assessment
            )

    def test_agent_quality_high_remains_conditional(self) -> None:
        verdict, score, hard_gate, _reason, gaps = (
            finalize_audit_output.scoring_verdict_v11(
                [
                    {
                        "status": "OPEN",
                        "severity": "HIGH",
                        "repairable": True,
                    }
                ],
                passing_dimensions(),
                [],
            )
        )

        self.assertEqual((verdict, score, hard_gate, gaps), ("CONDITIONAL", 100, False, []))

    def test_repair_authoritative_pass_accepts_effective_clean(self) -> None:
        machine = unavailable_d6_contract()
        assessment = assessment_for(machine)
        effective = agent_contract_wiring.derive_effective_contract(
            machine, assessment
        )
        gates = [
            {
                "code": code,
                "status": "PASS",
                "evidence": [{"fact": "gate assessed"}],
            }
            for code in run_repair.HARD_GATE_CODES
        ]
        report = {
            "summary": {
                "final_verdict": "PASS",
                "scoring_version": run_repair.CURRENT_SCORING_VERSION,
                "publication_route": "PUBLISH_CANDIDATE",
                "hard_gate_triggered": False,
                "total_score": 90,
            },
            "evidence_contract": {"fail_closed": True, "gaps": []},
            "hard_gates": gates,
            "deterministic_contract": machine,
            "effective_deterministic_contract": effective,
            "agent_contract_assessment": assessment,
            "findings": [],
        }

        result = run_repair.validate_authoritative_pass(report)

        self.assertTrue(result["authoritative_pass"])
        self.assertEqual(result["deterministic_state"], "CLEAN")


if __name__ == "__main__":
    unittest.main()
