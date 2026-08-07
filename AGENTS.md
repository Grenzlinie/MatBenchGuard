## Agent skills

### Issue tracker

Issues and PRDs are tracked in `Grenzlinie/MatBenchGuard` GitHub Issues. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five canonical triage roles with their default label names. See `docs/agents/triage-labels.md`.

### Domain docs

This repository uses a single-context domain model. See `docs/agents/domain.md`.

### Authoring/Review/Repair coordination

`materials_science_questions/` is a local, Git-ignored corpus containing
materials-science Harbor-format question packages and their review results. It
is available to agents in the workspace but must not be added to Git. Since the
directory is ignored, search it explicitly when needed (for example,
`rg --no-ignore --files materials_science_questions`).

Authoring/Review/Repair work is coordinated by human prompts. Track corpus status directly
in `materials_science_questions/corpus_review_tracking.json`; preserve existing
human-updated fields when adding or revising package records. There is no separate
tracking generator or dispatcher.

Authoring workspaces and audit, repair, candidate, and evidence artifacts must
stay outside Harbor packages. Use the Agent-primary Authoring, Review, and Repair
skills; there is no lifecycle, lock, digest, pending/resume, or deterministic-contract
dispatcher.

## 开发要求

1. 不保留向后兼容。过时的实现直接删除，不增加兼容层，不编写 migration，不保留 fallback。

2. 选择能够满足当前需求的最简单实现。不要预防性抽象，不增加多余的配置层。

3. 系统应分层演进。先跑通一个最小的端到端版本，再逐步增加能力；绝不为了尚未完成的复杂设计拆掉已经能运行的实现。

4. 组件保持模块化，关注点分离。

5. 优先使用成熟且持续维护的库。没有明确理由时，不自行重写已有能力。

6. 先检查项目现有依赖能够提供什么能力，再考虑增加新包或自行实现；不要预先假设现有库无法满足需求。

7. 架构决策应面向长期。不接受“先这样，以后再换”的临时方案。

8. 先研究成熟产品如何解决同类问题，采用经过验证的模式，不从零发明。
