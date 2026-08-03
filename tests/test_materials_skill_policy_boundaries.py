from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / ".cursor/skills/materials-benchmark-review"
REPAIR = ROOT / ".cursor/skills/materials-benchmark-repair"


class MaterialsSkillPolicyBoundariesTest(unittest.TestCase):
    def read(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def test_instruction_is_public_contract_not_paper_reading(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        contract = self.read(REVIEW / "references/harbor-package-contract.md")
        self.assertIn("唯一 solver-visible", review)
        self.assertIn("拿走论文测试", review)
        self.assertIn("题面不是文献阅读任务", contract)
        self.assertIn("不得写“查看 Fig./Table/Section/paper.md”", review)

    def test_q0_keeps_two_rejection_classes_and_experiment_boundaries(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        for mode in ("PURE_INFORMATION_EXTRACTION", "PURE_ALGEBRAIC_COMPUTATION", "EXPERIMENTAL_OPERATION_REQUIRED", "TRIVIAL_EXPERIMENTAL_DATA_REDUCTION"):
            self.assertIn(mode, review)
        self.assertIn("计算机复现", review)

    def test_four_parameter_classes_and_policies_are_explicit(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        for value in ("PAPER_FIXED", "SOLVER_SEARCHABLE", "TARGET_DEFINING", "INDISPENSABLE_ASSET", "MESH_SEARCH", "CONVERGENCE", "OPTIMIZATION", "SOLVER_JUSTIFIED", "RESOURCE"):
            self.assertIn(value, review)
        for field in ("paper_reports_unique_value", "instruction_requires_unique_value", "checker_requires_unique_value"):
            self.assertIn(field, review)

    def test_paper_content_restored_and_searchable_value_not_invented(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        repair = self.read(REPAIR / "SKILL.md")
        self.assertIn("必须保留或补齐", review)
        self.assertIn("不得因论文没有唯一值而失败", review)
        self.assertIn("不补值", repair)
        self.assertIn("REMOVE_GUESSED_EXECUTION_PARAMETER", repair)

    def test_parameter_conflicts_and_workflow_continuity_are_required(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        repair = self.read(REPAIR / "SKILL.md")
        self.assertIn("parameter_conflicts", review)
        self.assertIn("workflow_continuity", review)
        self.assertIn("FIX_PARAMETER_CONFLICT", repair)
        self.assertIn("RESTORE_WORKFLOW_DEPENDENCY", repair)

    def test_baseline_and_enhancement_are_separate(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        repair = self.read(REPAIR / "SKILL.md")
        checkpoints = self.read(REVIEW / "references/hidden-checkpoints.md")
        self.assertIn("高级 hacking 风险不影响", review)
        self.assertIn("没有附加 checkpoint 仍可 PASS", review)
        self.assertIn("Gold 占 60--80%", checkpoints)
        self.assertIn("Stage A", repair)
        self.assertIn("Stage B", repair)
        self.assertIn("回退", repair)

    def test_multiple_groups_keep_distinct_gold(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        scoring = self.read(REPAIR / "references/scientific-scoring-and-tolerance-design.md")
        self.assertIn("不能缩成“任选一组”", review)
        self.assertIn("不同参数组分别使用不同 Gold", scoring)
        self.assertIn("A 组 Gold 检查 B 组结果", scoring)

    def test_unavailable_indispensable_assets_fail_closed(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        contract = self.read(REVIEW / "references/harbor-package-contract.md")
        self.assertIn("无交付、链接、运行时供给或合法替代时失败", review)
        self.assertIn("没有任何上述取得方式，题包拒绝", contract)

    def test_missing_cif_is_not_automatically_an_indispensable_asset(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        repair = self.read(REPAIR / "SKILL.md")
        gates = self.read(REVIEW / "references/correctness-gates.md")
        self.assertIn("没有 CIF/POSCAR/结构文件本身不构成失败", review)
        self.assertIn("缺少 CIF 不触发 Q6", gates)
        self.assertIn("不得虚构 CIF", repair)
        self.assertIn("无法从论文描述合理重建", review)

    def test_checker_cost_and_full_trajectory_bans(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        repair = self.read(REPAIR / "SKILL.md")
        self.assertIn("32 CPU", review)
        self.assertIn("H100", review)
        self.assertIn("600", review)
        self.assertIn("大体积 MD", review)
        self.assertIn("不重跑 SCF", review)
        self.assertIn("不要求 Harbor+Codex", repair)

    def test_solution_exclusion_and_only_new_schema(self) -> None:
        review = self.read(REVIEW / "SKILL.md")
        repair = self.read(REPAIR / "SKILL.md")
        self.assertIn("`solution/` 完全排除", review)
        self.assertIn("`solution/` 完全排除", repair)
        self.assertIn("core_review_template.json", review)
        self.assertIn("core_repair_template.json", repair)
        for obsolete in ("agent_final_decision", "repair_report_template", "lifecycle dispatcher"):
            self.assertNotIn(obsolete, review)
            self.assertNotIn(obsolete, repair)


if __name__ == "__main__":
    unittest.main()
