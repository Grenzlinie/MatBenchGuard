from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / ".cursor/skills/materials-benchmark-review"
REPAIR = ROOT / ".cursor/skills/materials-benchmark-repair"


class MaterialsSkillPolicyBoundariesTest(unittest.TestCase):
    def read(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def test_review_is_final_result_only(self) -> None:
        skill = self.read(REVIEW / "SKILL.md")
        dimensions = self.read(REVIEW / "references/audit-dimensions.md")
        checker = self.read(REVIEW / "references/checker-audit.md")
        self.assertIn("final core scientific outputs", skill)
        self.assertIn("public final-output requirement", dimensions)
        self.assertIn("the checker need not read or authenticate them", checker)
        self.assertIn("Failure to prove that a specified process", dimensions)

    def test_container_path_failures_are_automation_limitations(self) -> None:
        review = self.read(REVIEW / "references/checker-audit.md")
        repair = self.read(REPAIR / "references/checker-repair.md")
        self.assertIn("declared container layout", review)
        self.assertIn("`AUTOMATION_LIMITATION`", review)
        self.assertIn("declared Docker/container layout", repair)
        self.assertIn("`AUTOMATION_LIMITATION`", repair)

    def test_parser_defenses_are_auto_fix_not_abandonment(self) -> None:
        categories = self.read(REPAIR / "references/repair-categories.md")
        abandonment = self.read(REPAIR / "references/abandonment.md")
        self.assertIn("finite-number rejection", categories)
        self.assertIn("NaN/Inf", abandonment)
        self.assertIn("not\nindependent abandonment grounds", abandonment)

    def test_repair_requires_candidate_evidence_and_full_pass(self) -> None:
        skill = self.read(REPAIR / "SKILL.md")
        policy = self.read(REPAIR / "references/repair-policy.md")
        self.assertIn("fail-before/pass-after", skill)
        self.assertIn("equal-depth Review is\n    `PASS`", skill)
        self.assertIn("/personal/qa_review/<cluster>/<theme>/<paper>/candidate", policy)


if __name__ == "__main__":
    unittest.main()
