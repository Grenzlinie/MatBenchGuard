# materials_bench_whitelist_100

来自材料科学 Harbor 题包审查全集：v9 evidence-bound E1 审查覆盖确定性全局排序的第 1–395 名，共得到 105 道可用 `PASS`；本包按 global rank 升序选取前 **100 道唯一 PASS 题包**。

## 目录结构

```text
materials/
  cluster-XXX/
    <family-name>/
      paper-YYYY/
        task.toml           # 任务元数据
        instruction.md      # agent 唯一可见的题面
        tests/
          grading_spec.json # 评分规范
          checker.py        # 评分器
          test.sh           # 验证入口
        solution/
          solve.sh          # 参考解入口
          *.py              # 可选的参考解辅助脚本
        paper/
          paper.md          # 论文原文
          images_manifest.json
        environment/
          Dockerfile        # 容器镜像
        manifest.json
        resources.json
        steps.json
manifest.json               # 100 道题的认证结论列表
README.md
```

## 分类

- pass: 100 道
- 原始题包: 99 道
- 修复后重新审查通过的题包: 1 道

## 复审方法

- 模型：`GPT-5.6 Luna xhigh`
- 执行等级：E1（静态审查 + 动态攻击评分器）
- 结论标准：总分至少 80、无未解决的可修复 HIGH、四项 Hard Gate 全部通过
- 证据边界：核心科学契约来自 `instruction.md`、`tests/` 与受限 Oracle；`paper/` 仅在触发条件成立时用于消歧和溯源
- 选择规则：在第 1–395 名的审查全集中，按 global rank 升序选择前 100 个唯一 `PASS`
- 截止位置：global rank 384
- 权威认证来源：`final_100_pass_v9_evidence_bound_20260716`

## 使用

每个 `paper-YYYY/` 目录都是独立的 Harbor 题包。进入目标目录后，可先运行题包自带的验证入口：

```bash
cd materials/cluster-XXX/<family-name>/paper-YYYY
bash tests/test.sh
```

在 Harbor 中实跑时，以该 `paper-YYYY/` 目录作为题包根目录。`solution/` 和 `tests/` 属于受限评测资产，不应暴露给解题 Agent。
