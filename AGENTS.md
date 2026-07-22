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

Audit and repair artifacts must stay outside Harbor packages.

The active workflow uses one private lifecycle per explicitly assigned package:
`.review_records/<cluster>/<theme>/<paper>/runs/<run-id>/`.
The main Agent creates it with `tools/create_materials_review_run.py`, writes
the assignment ledger and updates `corpus_review_tracking.json` only after all
runs reach a terminal state. Workers receive only `--run-dir`; they never
select packages, write the ledger/tracking, or combine audit/plan paths from
another run. Operational records are local and ignored by Git.
