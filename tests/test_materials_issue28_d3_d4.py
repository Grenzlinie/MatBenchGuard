from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = (
    "/Users/siyuliu/Desktop/qa_review/"
    ".cursor/skills/materials-benchmark-review/scripts"
)
if SCRIPTS not in sys.path:
    sys.path.insert(0, SCRIPTS)

from d3_d4_checker import (  # noqa: E402
    add_checker_health_issues,
    analyze_checker_health,
    analyze_weights,
    auto_fix_operation_error,
    expected_repair_class,
)
import audit_package  # noqa: E402


class MaterialsIssue28D3D4Tests(unittest.TestCase):
    def test_oversized_json_weight_is_reported_without_crashing(self) -> None:
        oversized = 10**400
        result = analyze_weights(
            {
                "steps": [
                    {
                        "id": "oversized",
                        "output_file": "result.json",
                        "weight": oversized,
                    }
                ]
            }
        )
        finding = next(
            item
            for item in result["findings"]
            if item["code"] == "NON_FINITE_WEIGHT"
        )
        self.assertEqual(
            finding["evidence"]["weights"][0]["value"], oversized
        )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "tests").mkdir()
            (root / "instruction.md").write_text(
                "### Step 1\n"
                "- Role: scored\n"
                "- Output file: /app/outputs/result.json\n",
                encoding="utf-8",
            )
            (root / "tests/checker.py").write_text(
                "def score_result(value):\n    return 1.0\n",
                encoding="utf-8",
            )
            (root / "tests/test.sh").write_text(
                "#!/bin/sh\n", encoding="utf-8"
            )
            (root / "tests/grading_spec.json").write_text(
                json.dumps(
                    {
                        "pass_threshold": 0.8,
                        "output_contract": {
                            "outputs": [{"file": "result.json"}]
                        },
                        "steps": [
                            {
                                "id": "oversized",
                                "output_file": "result.json",
                                "weight": oversized,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            static = audit_package.static_audit(
                root, root / "static-audit.json"
            )
        self.assertIn(
            "NON_FINITE_WEIGHT",
            {item["code"] for item in static["issues"]},
        )

    def test_d3_reports_proven_health_defects_and_unique_wiring(self) -> None:
        source = """
def score_partial(value):
    if value:
        return score

def score_zero(value):
    return 0

def score_one(value):
    return 1

def score_div(value):
    return value / 0

def score_signed_div(value):
    return value / -0.0

_SCORERS = {
    "partial": score_partial,
    "zero": score_zero,
    "one": score_one,
    "div": score_div,
    "signed_div": score_signed_div,
}
"""
        health = analyze_checker_health(
            source,
            {
                "partial": "score_partial",
                "zero": "score_zero",
                "one": "score_one",
                "div": "score_div",
                    "signed_div": "score_signed_div",
            },
            scorer_registry_present=True,
                scoring_step_ids=["partial", "zero", "one", "div", "signed_div"],
        )
        issues: list[dict[str, object]] = []
        add_checker_health_issues(
            issues,
            health,
            scorer_bindings={},
            scoring_step_ids=[],
        )
        self.assertEqual(
            {
                item["code"]
                for item in issues
            },
            {
                "SCORER_RETURN_NOT_TOTAL",
                "ALWAYS_ZERO_SCORER",
                "ALWAYS_PASS_SCORER",
                "DIVISION_BY_ZERO_LITERAL",
            },
        )
        proof = next(
            item for item in issues if item["code"] == "SCORER_RETURN_NOT_TOTAL"
        )["evidence"]
        self.assertTrue(proof["return_proof"]["partial"]["auto_fix_provable"])
        self.assertEqual(
            expected_repair_class(
                "D3", "SCORER_RETURN_NOT_TOTAL", proof
            ),
            "AUTO_FIX",
        )

        wiring_health = analyze_checker_health(
            "def score_a(value):\n    return 0.5\n_SCORERS = {}\n",
            {},
            scorer_registry_present=True,
            scoring_step_ids=["a"],
        )
        self.assertEqual(
            wiring_health["missing_wiring"][0]["candidate_function"],
            "score_a",
        )
        wiring_issues: list[dict[str, object]] = []
        add_checker_health_issues(
            wiring_issues,
            wiring_health,
            scorer_bindings={},
            scoring_step_ids=["a"],
        )
        self.assertEqual(wiring_issues[0]["code"], "SCORER_WIRING_MISSING")
        self.assertEqual(
            expected_repair_class(
                "D3", "SCORER_WIRING_MISSING", wiring_issues[0]["evidence"]
            ),
            "AUTO_FIX",
        )

    def test_missing_outer_return_proves_unique_nested_wrapper(self) -> None:
        source = """
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        return 1.0

_SCORERS = {"step": score_0}
"""
        health = analyze_checker_health(
            source,
            {"step": "score_0"},
            scorer_registry_present=True,
            scoring_step_ids=["step"],
        )
        status = health["scorer_status"]["step"]
        proof = status["return_proof"]

        self.assertEqual(status["return_status"], "MISSING_DIRECT_RETURN")
        self.assertEqual(proof["proof_status"], "PROVEN")
        self.assertTrue(proof["auto_fix_provable"])
        self.assertEqual(
            proof["source_hash"],
            "sha256:" + hashlib.sha256(source.encode("utf-8")).hexdigest(),
        )
        self.assertEqual(
            proof["return_expression"], "score(artifact, step, ctx)"
        )
        self.assertTrue(proof["call_derived"])
        self.assertEqual(
            proof["argument_mapping"],
            {"artifact": "artifact", "step": "step", "ctx": "ctx"},
        )
        for span_key in (
            "outer_function_span",
            "inner_function_span",
        ):
            self.assertIsInstance(proof[span_key], dict)
            self.assertLessEqual(
                proof[span_key]["start_line"], proof[span_key]["end_line"]
            )
        self.assertIsNone(proof["call_span"])

        issues: list[dict[str, object]] = []
        add_checker_health_issues(issues, health)
        finding = next(
            item for item in issues if item["code"] == "SCORER_MISSING_RETURN"
        )
        self.assertTrue(finding["evidence"]["auto_fix_provable"])
        self.assertEqual(
            expected_repair_class("D3", "SCORER_MISSING_RETURN", finding["evidence"]),
            "AUTO_FIX",
        )

    def test_correct_nested_wrapper_has_no_missing_return_finding(self) -> None:
        source = """
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        return 1.0
    return score(artifact, step, ctx)

_SCORERS = {"step": score_0}
"""
        health = analyze_checker_health(
            source,
            {"step": "score_0"},
            scorer_registry_present=True,
            scoring_step_ids=["step"],
        )
        issues: list[dict[str, object]] = []
        add_checker_health_issues(issues, health)

        self.assertEqual(health["missing_returns"], [])
        self.assertNotIn(
            "SCORER_MISSING_RETURN", {item["code"] for item in issues}
        )
        self.assertEqual(
            health["scorer_status"]["step"]["return_status"],
            "STATIC_RETURN_CANDIDATE",
        )

    def test_ambiguous_nested_wrappers_remain_assisted(self) -> None:
        sources = {
            "multiple nested functions": """
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        return 1.0
    def helper(artifact, step, ctx):
        return 0.5
    score(artifact, step, ctx)
""",
            "argument mismatch": """
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        return 1.0
    score(artifact, step)
""",
            "outer logic": """
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        return 1.0
    computed = score(artifact, step, ctx)
    computed
""",
            "closure capture": """
def score_0(artifact, step, ctx):
    multiplier = 2
    def score(artifact, step, ctx):
        return multiplier
    score(artifact, step, ctx)
""",
            "async inner scorer": """
def score_0(artifact, step, ctx):
    async def score(artifact, step, ctx):
        return 1.0
    score(artifact, step, ctx)
""",
        }
        for label, source in sources.items():
            with self.subTest(label=label):
                health = analyze_checker_health(
                    source,
                    {"step": "score_0"},
                    scorer_registry_present=True,
                    scoring_step_ids=["step"],
                )
                proof = health["scorer_status"]["step"]["return_proof"]
                self.assertEqual(proof["proof_status"], "AMBIGUOUS")
                self.assertFalse(proof["auto_fix_provable"])
                self.assertEqual(
                    expected_repair_class(
                        "D3",
                        "SCORER_MISSING_RETURN",
                        {"return_proof": {"step": proof}},
                    ),
                    "ASSISTED_FIX",
                )

    def test_mixed_missing_return_proofs_fail_closed(self) -> None:
        source = """
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        return 1.0

def score_1(artifact, step, ctx):
    pass

_SCORERS = {"proven": score_0, "ambiguous": score_1}
"""
        health = analyze_checker_health(
            source,
            {"proven": "score_0", "ambiguous": "score_1"},
            scorer_registry_present=True,
            scoring_step_ids=["proven", "ambiguous"],
        )
        issues: list[dict[str, object]] = []
        add_checker_health_issues(issues, health)
        finding = next(
            item for item in issues if item["code"] == "SCORER_MISSING_RETURN"
        )

        self.assertFalse(finding["evidence"]["auto_fix_provable"])
        self.assertEqual(
            expected_repair_class(
                "D3", "SCORER_MISSING_RETURN", finding["evidence"]
            ),
            "ASSISTED_FIX",
        )

    def test_d3_reports_syntax_failure_without_guessing_a_fix(self) -> None:
        health = analyze_checker_health("def broken(:\n    pass\n")
        issues: list[dict[str, object]] = []
        add_checker_health_issues(
            issues, health, scorer_bindings={}, scoring_step_ids=[]
        )
        self.assertEqual(issues[0]["code"], "CHECKER_STATIC_ANALYSIS_UNAVAILABLE")
        self.assertEqual(
            expected_repair_class(
                "D3",
                "CHECKER_STATIC_ANALYSIS_UNAVAILABLE",
                issues[0]["evidence"],
            ),
            "ASSISTED_FIX",
        )

    def test_d4_reports_invalid_nonfinite_zero_and_ineffective_weights(
        self,
    ) -> None:
        result = analyze_weights(
            {
                "steps": [
                    {"id": "text", "weight": "0.5"},
                    {"id": "nan", "weight": float("nan")},
                    {"id": "zero", "weight": 0.0},
                    {"id": "negative", "weight": -1.0},
                    {"id": "ineffective", "weight": 0.5},
                ]
            },
            checker_analysis={
                "outputs": [
                    {
                        "step_id": "ineffective",
                        "checker_scoring": {"scorer_bound": False},
                    }
                ]
            },
        )
        codes = {item["code"] for item in result["findings"]}
        self.assertEqual(
            codes,
            {
                "INVALID_WEIGHT",
                "NON_FINITE_WEIGHT",
                "ZERO_WEIGHT_SCORING_COMPONENT",
                "INEFFECTIVE_WEIGHT_SCORING_COMPONENT",
            },
        )

        normalized = analyze_weights(
            {"steps": [{"id": "a", "weight": 2.0}, {"id": "b", "weight": 1.0}]}
        )
        normalization = next(
            item
            for item in normalized["findings"]
            if item["code"] == "WEIGHTS_NOT_ONE"
        )
        self.assertTrue(
            normalization["evidence"]["ratio_preserving_normalization"]
        )
        self.assertEqual(
            expected_repair_class(
                "D4", "WEIGHTS_NOT_ONE", normalization["evidence"]
            ),
            "AUTO_FIX",
        )
        self.assertEqual(
            expected_repair_class(
                "D4",
                "ZERO_WEIGHT_SCORING_COMPONENT",
                {"weights": [{"component_id": "zero", "value": 0.0}]},
            ),
            "ASSISTED_FIX",
        )

    def test_d3_d4_auto_fix_operations_are_proof_bound(self) -> None:
        return_finding = {
            "deterministic_check": "D3",
            "title": "SCORER_RETURN_NOT_TOTAL",
            "evidence": {
                "return_proof": {
                    "partial": {
                        "auto_fix_provable": True,
                        "return_expression": "score",
                    }
                }
            },
        }
        self.assertIsNone(
            auto_fix_operation_error(
                return_finding,
                {
                    "file": "tests/checker.py",
                    "new": "if value:\n    return score\nreturn score\n",
                },
            )
        )
        self.assertIsNotNone(
            auto_fix_operation_error(
                {
                    "deterministic_check": "D3",
                    "title": "ALWAYS_ZERO_SCORER",
                    "evidence": {},
                },
                {"file": "tests/checker.py", "new": "return 0.5\n"},
            )
        )
        self.assertIsNotNone(
            auto_fix_operation_error(
                return_finding,
                {
                    "file": "tests/grading_spec.json",
                    "new": "return score\n",
                },
            )
        )
        self.assertIsNone(
            auto_fix_operation_error(
                {
                    "deterministic_check": "D4",
                    "title": "WEIGHTS_NOT_ONE",
                    "evidence": {
                        "weights": [
                            {"component_id": "a", "value": 2.0},
                            {"component_id": "b", "value": 1.0},
                        ],
                        "ratio_preserving_normalization": True,
                        "normalized_weights": [
                            {"component_id": "a", "value": 2 / 3},
                            {"component_id": "b", "value": 1 / 3},
                        ],
                    },
                },
                {
                    "type": "json_set",
                    "file": "tests/grading_spec.json",
                    "path": ["steps", 0, "weight"],
                    "value": 2 / 3,
                },
            )
        )
        self.assertIsNotNone(
            auto_fix_operation_error(
                {
                    "deterministic_check": "D4",
                    "title": "WEIGHTS_NOT_ONE",
                    "evidence": {
                        "weights": [
                            {"component_id": "a", "value": 2.0},
                            {"component_id": "b", "value": 1.0},
                        ],
                        "ratio_preserving_normalization": True,
                        "normalized_weights": [
                            {"component_id": "a", "value": 2 / 3},
                            {"component_id": "b", "value": 1 / 3},
                        ],
                    },
                },
                {
                    "type": "json_set",
                    "file": "tests/checker.py",
                    "path": ["steps", 0, "weight"],
                    "value": 2 / 3,
                },
            )
        )


if __name__ == "__main__":
    unittest.main()
