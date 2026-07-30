from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / ".cursor/skills/materials-benchmark-review"
REPAIR = ROOT / ".cursor/skills/materials-benchmark-repair"
ORCHESTRATION = ROOT / ".cursor/skills/materials-benchmark-orchestration"


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

    def test_responsibility_matrix_requires_hybrid_primary_file_review(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        matrix = self.read(REVIEW / "references/check-responsibility-matrix.md")
        repair = self.read(REPAIR / "SKILL.md")
        orchestration = self.read(ORCHESTRATION / "SKILL.md")
        playbook = self.read(ORCHESTRATION / "assets/PLAYBOOK.md")

        self.assertIn("check-responsibility-matrix.md", review)
        self.assertIn("`MECHANICAL`", matrix)
        self.assertIn("`HYBRID`", matrix)
        self.assertIn("`AGENT`", matrix)
        self.assertIn("机械候选为零不构成通过证据", repair)
        self.assertIn("check-responsibility-matrix.md", orchestration)
        self.assertIn("zero hits is never", playbook)
        self.assertIn("itself a verdict", playbook)
        self.assertIn("mandatory Phase 3 Hybrid check", playbook)

    def test_orchestration_and_repair_share_the_same_entry_gate(self) -> None:
        repair = self.read(REPAIR / "SKILL.md")
        report_schema = self.read(REPAIR / "references/report-schema.md")
        review = self.read(REVIEW / "SKILL.md")
        orchestration = self.read(ORCHESTRATION / "SKILL.md")
        playbook = self.read(ORCHESTRATION / "assets/PLAYBOOK.md")

        self.assertIn("Repair 准入 Gate", repair)
        self.assertIn("SCREENED_OUT", repair)
        self.assertIn("Do not create a repair report", report_schema)
        self.assertIn("该状态不是新的 Review verdict", review)
        self.assertIn("SCREENED_OUT/DONE", orchestration)
        self.assertIn("terminal state is `SCREENED_OUT`", playbook)
        self.assertIn("`NOT_ASSESSABLE` is never DONE", playbook)
        self.assertIn(
            "--probe-observations OUT/evidence/checker_observations.json",
            playbook,
        )
        self.assertIn("validate_lifecycle.py", orchestration)
        self.assertIn("不得手工创建 `.done`", orchestration)

    def test_playground_resource_deployment_is_outside_qa_scope(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        readiness = self.read(REVIEW / "references/resource-readiness.md")
        leakage = self.read(REVIEW / "references/task-types-and-leakage.md")
        repair = self.read(REPAIR / "SKILL.md")
        playbook = self.read(ORCHESTRATION / "assets/PLAYBOOK.md")

        self.assertIn("求解者直接收到的题面只有 `instruction.md`", review)
        self.assertIn("`assets`", review)
        self.assertIn("不审核平台部署或挂载结果", review)
        mechanical = self.read(REVIEW / "references/mechanical-evidence.md")
        self.assertIn("Add `--probe-urls` whenever", mechanical)
        self.assertIn("must not call Playground", readiness)
        self.assertIn("confirmed `404/410`", readiness)
        self.assertIn("not solver-facing", leakage)
        self.assertIn("不调用 Playground 拉取资源", repair)
        self.assertIn("Do not call Playground", playbook)
        self.assertIn("confirmed `404/410`", playbook)

    def test_simulation_parameter_closure_is_mandatory_and_not_repaired_by_guessing(
        self,
    ) -> None:
        review = self.read(REVIEW / "SKILL.md")
        patterns = self.read(REVIEW / "references/scientific-defect-patterns.md")
        parameter_policy = self.read(
            REVIEW / "references/paper-grounded-audit.md"
        )
        repair = self.read(REPAIR / "references/repair-policy.md")
        playbook = self.read(ORCHESTRATION / "assets/PLAYBOOK.md")

        self.assertIn("simulation_parameter_matrix.json", review)
        self.assertIn("机械候选为零不能免除", review)
        self.assertIn("SIMULATION_CONTRACT_UNDERDETERMINED", patterns)
        self.assertIn("SIMULATION_PARAMETER_DEPENDENCY_BROKEN", patterns)
        self.assertIn(
            "ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE", parameter_policy
        )
        self.assertIn("Software\ndefaults", repair)
        self.assertIn("non-repairable `ABANDON`", playbook)


if __name__ == "__main__":
    unittest.main()
