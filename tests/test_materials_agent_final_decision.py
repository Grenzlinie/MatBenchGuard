from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".cursor/skills/materials-benchmark-review/scripts/validate_agent_decision.py"
SPEC = importlib.util.spec_from_file_location("validate_agent_decision", SCRIPT)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def evidence(result: str = "verified") -> list[dict[str, str]]:
    return [{"source_kind": "TEST", "path": "fixture", "locator": "line 1", "quote_or_result": result}]


def decision() -> dict:
    criteria = {
        key: {"name": name, "status": "PASS", "rationale": "Verified from primary evidence.", "evidence": evidence()}
        for key, name in module.CRITERIA.items()
    }
    dimensions = [
        {"dimension": dim, "weight": weight, "normalized": 100, "evidence": evidence()}
        for dim, weight in module.DIMENSIONS.items()
    ]
    gates = [
        {
            "code": code,
            "status": "PASS",
            "disposition": "NONE",
            "failure_modes": [],
            "rationale": "No gate defect.",
            "evidence": evidence(),
        }
        for code in sorted(module.HARD_GATES)
    ]
    probes = {
        name: {"status": "PASS", "rationale": "Probe behaved as required.", "evidence": evidence(name)}
        for name in module.PROBES
    }
    resource = {
        "resource_id": "embedded", "role": "required input", "identity_version": "v1",
        "locator": "data/input.json", "access_result": "readable",
        "sufficiency": "complete", "allowed_alternative": "none required",
    }
    readiness = {
        name: {"status": "READY", "rationale": "Required resources are ready.", "evidence": evidence(name), "resources": [resource]}
        for name in module.READINESS
    }
    parameters = {
        name: {"status": "PASS", "rationale": "Policy boundary verified.", "evidence": evidence(name), "items": []}
        for name in ("fixed_or_source_required", "solver_selectable")
    }
    return {
        "schema_version": module.SCHEMA, "package_id": "cluster/theme/paper-1",
        "mode": "REVIEW", "reproduction_intent": "METHOD_REIMPLEMENTATION",
        "reviewed_scope": ["instruction.md", "resources.json", "paper/**", "tests/**"],
        "verdict": "PASS", "weighted_score": 100.0, "criteria": criteria,
        "dimensions": dimensions, "hard_gates": gates, "checker_probes": probes,
        "readiness": readiness, "parameter_assessment": parameters,
        "diagnostic_adjudications": [], "open_confirmed_findings": [], "limitations": [],
    }


def reasoning_absent_decision(*modes: str) -> dict:
    value = decision()
    value["criteria"]["2.3"]["status"] = "FAIL"
    gate = next(item for item in value["hard_gates"] if item["code"] == "SCIENTIFIC_REASONING_ABSENT")
    gate.update({"status": "FAIL", "disposition": "ABANDON", "failure_modes": list(modes)})
    value["open_confirmed_findings"] = [{
        "finding_id": "F-SCI-REASONING-ABSENT",
        "title": "Final task lacks substantive scientific reasoning.",
        "severity": "FATAL",
        "dimension": "C03",
        "repairable": False,
        "hard_gate": True,
        "hard_gate_code": "SCIENTIFIC_REASONING_ABSENT",
        "disposition": "ABANDON",
        "failure_modes": list(modes),
        "evidence": evidence("instruction leaves only mechanical work"),
    }]
    value["verdict"] = "REJECT"
    return value


class AgentFinalDecisionTests(unittest.TestCase):
    def test_full_quality_contract_passes(self) -> None:
        self.assertEqual(module.validate(decision())["verdict"], "PASS")

    def test_each_2_1_to_2_8_is_mandatory_for_pass(self) -> None:
        for key in module.CRITERIA:
            with self.subTest(key=key):
                value = decision()
                value["criteria"][key]["status"] = "FAIL"
                value["verdict"] = "CONDITIONAL"
                self.assertEqual(module.validate(value)["verdict"], "CONDITIONAL")
                value["verdict"] = "PASS"
                with self.assertRaisesRegex(ValueError, "expected CONDITIONAL"):
                    module.validate(value)

    def test_data_and_model_must_be_ready(self) -> None:
        for category in ("data", "model"):
            with self.subTest(category=category):
                value = decision()
                value["readiness"][category]["status"] = "NOT_READY"
                value["verdict"] = "CONDITIONAL"
                self.assertEqual(module.validate(value)["verdict"], "CONDITIONAL")

    def test_solver_generated_model_can_be_not_required(self) -> None:
        value = decision()
        value["readiness"]["model"] = {
            "status": "NOT_REQUIRED", "rationale": "The task trains the model as its output.",
            "evidence": evidence("instruction requires model training"), "resources": [],
        }
        self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_parameter_policy_failure_blocks_pass(self) -> None:
        value = decision()
        value["parameter_assessment"]["fixed_or_source_required"]["status"] = "FAIL"
        value["verdict"] = "CONDITIONAL"
        self.assertEqual(module.validate(value)["verdict"], "CONDITIONAL")

    def test_applicable_checker_probe_must_not_be_unassessed(self) -> None:
        value = decision()
        value["checker_probes"]["quality_gradient"]["status"] = "NOT_ASSESSABLE"
        value["verdict"] = "NOT_ASSESSABLE"
        self.assertEqual(module.validate(value)["verdict"], "NOT_ASSESSABLE")

    def test_false_positive_schema_diagnostic_does_not_block(self) -> None:
        value = decision()
        value["diagnostic_adjudications"] = [{
            "diagnostic": "INVALID_GRADING_SPEC_SCHEMA",
            "disposition": "DISMISSED_FALSE_POSITIVE",
            "reason": "Equivalent valid contract verified directly.",
            "evidence": evidence("source and runtime agree"),
        }]
        self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_score_below_80_is_conditional_even_when_criteria_pass(self) -> None:
        value = decision()
        value["dimensions"][0]["normalized"] = 0
        value["weighted_score"] = 90.0
        self.assertEqual(module.validate(value)["verdict"], "PASS")
        value["dimensions"][1]["normalized"] = 0
        value["weighted_score"] = 70.0
        value["verdict"] = "CONDITIONAL"
        self.assertEqual(module.validate(value)["verdict"], "CONDITIONAL")

    def test_hard_gate_forces_reject(self) -> None:
        value = decision()
        value["hard_gates"][0]["status"] = "FAIL"
        value["hard_gates"][0]["disposition"] = "REPAIR"
        value["verdict"] = "REJECT"
        self.assertEqual(module.validate(value)["verdict"], "REJECT")

    def test_pure_information_extraction_is_rejected_and_abandoned(self) -> None:
        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        self.assertEqual(module.validate(value)["verdict"], "REJECT")

    def test_pure_algebraic_computation_is_rejected_and_abandoned(self) -> None:
        value = reasoning_absent_decision("PURE_ALGEBRAIC_COMPUTATION")
        self.assertEqual(module.validate(value)["verdict"], "REJECT")

    def test_extraction_plus_algebra_records_both_modes_on_one_gate(self) -> None:
        value = reasoning_absent_decision(
            "PURE_INFORMATION_EXTRACTION", "PURE_ALGEBRAIC_COMPUTATION"
        )
        self.assertEqual(module.validate(value)["verdict"], "REJECT")

    def test_model_and_evidence_reasoning_examples_do_not_trigger_gate(self) -> None:
        for rationale in (
            "Task requires validating model applicability before computing a value.",
            "Task requires comparing conflicting evidence before producing a table.",
        ):
            with self.subTest(rationale=rationale):
                value = decision()
                gate = next(item for item in value["hard_gates"] if item["code"] == "SCIENTIFIC_REASONING_ABSENT")
                gate["rationale"] = rationale
                self.assertEqual(module.validate(value)["verdict"], "PASS")

    def test_reasoning_absence_rejects_inconsistent_dispositions(self) -> None:
        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        gate = next(item for item in value["hard_gates"] if item["code"] == "SCIENTIFIC_REASONING_ABSENT")
        gate["disposition"] = "REPAIR"
        with self.assertRaisesRegex(ValueError, "requires disposition ABANDON"):
            module.validate(value)

        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        value["open_confirmed_findings"][0]["repairable"] = True
        value["open_confirmed_findings"][0]["disposition"] = "REPAIR"
        with self.assertRaisesRegex(ValueError, "must be non-repairable ABANDON"):
            module.validate(value)

    def test_reasoning_absence_requires_reject_and_matching_c03_failure(self) -> None:
        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        value["criteria"]["2.3"]["status"] = "PASS"
        with self.assertRaisesRegex(ValueError, "criteria.2.3 FAIL"):
            module.validate(value)

        value = reasoning_absent_decision("PURE_INFORMATION_EXTRACTION")
        value["verdict"] = "CONDITIONAL"
        with self.assertRaisesRegex(ValueError, "expected REJECT"):
            module.validate(value)

    def test_version_2_0_is_rejected(self) -> None:
        value = decision()
        value["schema_version"] = "materials-agent-final-decision/2.0"
        with self.assertRaisesRegex(ValueError, "2.1"):
            module.validate(value)


if __name__ == "__main__":
    unittest.main()
