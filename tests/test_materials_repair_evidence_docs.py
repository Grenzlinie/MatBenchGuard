from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REVIEW_SKILL = (
    REPO_ROOT / ".cursor/skills/materials-benchmark-review/SKILL.md"
)
REPAIR_SKILL = (
    REPO_ROOT / ".cursor/skills/materials-benchmark-repair/SKILL.md"
)
EVIDENCE_NOTE = REPO_ROOT / "docs/plans/materials-checker-repair-evidence.md"


class MaterialsRepairEvidenceDocsTests(unittest.TestCase):
    def test_skills_state_the_narrow_auto_fix_boundary(self) -> None:
        for path in (REVIEW_SKILL, REPAIR_SKILL):
            with self.subTest(path=path):
                text = path.read_text(encoding="utf-8")
                normalized = " ".join(text.split())
                self.assertIn("D1", text)
                self.assertIn("AUTO_FIX", text)
                self.assertIn("contract/scoring wiring", text)
                self.assertIn("Gold", text)
                self.assertIn("threshold", text)
                self.assertIn("formula", text)
                self.assertIn("science semantics", normalized)

    def test_evidence_note_has_casebook_and_oracle_safe_boundary(self) -> None:
        text = EVIDENCE_NOTE.read_text(encoding="utf-8")
        for ticket in ("#21", "#28", "#29", "#30", "#31", "#32"):
            self.assertIn(ticket, text)
        self.assertIn("D1–D6 boundary by check", text)
        self.assertIn("no Oracle values", text)
        self.assertIn("non-Oracle fixture", text)
        self.assertNotIn('"reward":', text)
        self.assertNotIn('"breakdown":', text)


if __name__ == "__main__":
    unittest.main()
