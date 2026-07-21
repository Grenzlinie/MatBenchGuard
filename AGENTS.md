## Agent skills

### Issue tracker

Issues and PRDs are tracked in `Grenzlinie/qa-review` GitHub Issues. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five canonical triage roles with their default label names. See `docs/agents/triage-labels.md`.

### Domain docs

This repository uses a single-context domain model. See `docs/agents/domain.md`.

### Review/Repair coordination

Batch Review/Repair work is coordinated by human prompts. There is no
assignment-lock dispatcher. Track corpus review status in
`materials_science_questions/corpus_review_tracking.json`, regenerated or merged
with `python tools/init_corpus_review_tracking.py` (use `--merge` to preserve
human-updated fields while resyncing packages).

Audit and repair artifacts must stay outside Harbor packages. For
`<topic>/paper-<id>`, the default sibling management root is
`<topic>/review_outputs/<paper-id>/`.
