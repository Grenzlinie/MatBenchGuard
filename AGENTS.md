## Agent skills

### Issue tracker

Issues and PRDs are tracked in `Grenzlinie/qa-review` GitHub Issues. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five canonical triage roles with their default label names. See `docs/agents/triage-labels.md`.

### Domain docs

This repository uses a single-context domain model. See `docs/agents/domain.md`.

### Batch Review/Repair assignment lock

Batch Review/Repair dispatch is mandatory through
`assign_review_tasks/README.md` and `python assign_review_tasks/assign.py`. The parent agent must
write active claims before launching subagents, pass one claimed package to each
subagent, never dispatch an unclaimed, foreign-claimed, or completed package,
serialize registry writes through the CLI, and settle every claim after workers
stop. Workers must not edit the registry.
