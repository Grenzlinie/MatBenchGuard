## Agent skills

### Issue tracker

Issues and PRDs are tracked in `Grenzlinie/qa-review` GitHub Issues. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five canonical triage roles with their default label names. See `docs/agents/triage-labels.md`.

### Domain docs

This repository uses a single-context domain model. See `docs/agents/domain.md`.

### Review/Repair coordination

Review/Repair work is coordinated by human prompts. Track corpus status in
`materials_science_questions/corpus_review_tracking.json`, regenerated or merged
with `python tools/init_corpus_review_tracking.py` (use `--merge` to preserve
human-updated fields while resyncing packages).

Audit, repair, candidate, and evidence artifacts must stay outside Harbor
packages. Use the Agent-primary Review and Repair skills; there is no lifecycle,
lock, digest, pending/resume, or deterministic-contract dispatcher.
