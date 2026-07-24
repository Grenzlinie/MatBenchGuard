---
name: materials-benchmark-orchestration
description: Drain a whole corpus of Harbor materials-science question packages through the review + repair pipeline in parallel — one package per subagent — using a lock-based self-claim queue that guarantees no two agents touch the same package. Use when given a NEW collection/folder of packages to QA at scale. Provides the queue (fcntl.flock), a per-package PLAYBOOK, the orchestration loop (spawn/top-up/release/quarantine), and clean-package publish + Harbor-format verification. Works across Codex, Claude Code, and Cursor multi-agent modes.
---

# Materials Benchmark Parallel Orchestration

Run `materials-benchmark-review` (+ `materials-benchmark-repair`) over an entire
corpus of Harbor packages concurrently. Each worker is a subagent that claims
ONE package at a time from a shared, lock-protected queue, processes it end to
end per the PLAYBOOK, marks it done, and claims the next. The orchestrator keeps
a pool of workers full until the queue drains, then assembles the clean,
publishable packages.

This skill is the "how to run it at scale" layer. The scientific adjudication
rules live in `materials-benchmark-review` and `materials-benchmark-repair`;
read those too — every worker must follow them.

## When to use
- A new folder/collection of Harbor question packages needs QA (review + repair).
- You want many agents (Codex / Claude Code / Cursor subagents, or several
  separate sessions) working the same corpus without colliding or duplicating.

## Files
- `scripts/queue.py`        atomic claim/done/release/status/reap (flock).
- `scripts/init_corpus.py`  scan a source root -> `corpus_manifest.json` + state.
- `scripts/publish.py`      assemble clean packages into `_publish/`.
- `scripts/verify_harbor.py` verify `_publish/` matches the Harbor file tree.
- `assets/PLAYBOOK.md`      the per-package procedure handed to every worker.

## Paths (two roots, set once via env)
- `QA_SRC`  = read-only source corpus root (the Harbor packages). NEVER mutated.
- `QA_ROOT` = writable work/output root (default `/personal/qa_review`). Holds
  `corpus_manifest.json`, `state/`, per-package `<pkg>/` outputs, and `_publish/`.

Package ids are paths relative to `QA_SRC` (e.g. `cluster-x/theme/paper-y`), so
they map 1:1 to both `QA_SRC/<pkg>` and `QA_ROOT/<pkg>`.

## Concurrency & the lock (why it is safe)
`queue.py` serializes every state mutation with `fcntl.flock(LOCK_EX)` on
`QA_ROOT/state/queue.lock`. `claim` picks the first unclaimed, not-done package,
records `{agent, ts}` in `assigned.json`, and releases the lock — so two workers
(even in different sessions / tools) can never receive the same package. `done`
records it in `done.json` and drops the assignment. Stale claims (unfinished,
older than `QA_STALE_SEC`, default 2h) are auto-reaped on the next `claim`, so a
crashed worker never strands a package. A `.done` marker in `QA_ROOT/<pkg>/` is
also treated as done, making the queue idempotent across reruns and new corpora.

## Procedure

### 1. Initialize the queue (once per corpus)
```
export QA_SRC=/abs/path/to/source_corpus
export QA_ROOT=/personal/qa_review          # or any writable root
uv run --python 3.12 python <this>/scripts/init_corpus.py
uv run --python 3.12 python <this>/scripts/queue.py status   # {total, done, remaining}
```
Re-running init on an existing QA_ROOT is safe (keeps state; a new/expanded
corpus just adds unclaimed packages).

### 2. Spawn a worker pool
Launch N subagents (start ~8–16; scale up freely — the lock handles any count).
Give EACH a globally-unique AGENT_ID. Each worker's prompt = "read
`assets/PLAYBOOK.md` in full, then run the self-claim loop", with `QA_SRC`,
`QA_ROOT`, and the review/repair skill paths exported. Multiple humans/tools can
add their own workers to the same queue concurrently — instruct them to use
distinct AGENT_IDs and to claim ONLY via `queue.py claim` (never hand-pick).

Worker prompt skeleton:
> You are a QA review+repair worker; AGENT_ID `qa-<uniq>`. Read
> `<this>/assets/PLAYBOOK.md` IN FULL and follow it. Self-claim loop:
> `queue.py claim qa-<uniq> 1`; if a pkg prints, process it EXACTLY per the
> PLAYBOOK (evidence + probes + validated `agent_final_decision.json`; if not
> PASS run the repair flow + validated `repair_report.json`; `touch OUT/.done`;
> `queue.py done <pkg>`); if empty, STOP. Up to 8 packages, then report & exit;
> always finish the package you started; if blocked, `queue.py release <pkg>`.

### 3. Keep the pool full (orchestrator loop)
- Each worker processes up to 8 packages then exits (bounds context). On each
  completion notification, launch a fresh worker with a new AGENT_ID until
  `queue.py status` shows `remaining == 0` and `assigned_open == 0`.
- Poll progress any time with `queue.py status`.
- On worker **failure/stall** (API error, or a completion whose last step was
  mid-package): release its orphaned claim so another worker retakes it —
  `queue.py release <pkg>` (identify via `assigned.json`); optionally wipe a
  partial `QA_ROOT/<pkg>/` first. Do NOT kill a worker merely for being slow —
  a repair with fail-before/pass-after + equal-depth re-audit can take 20+ min.
- **Quarantine** a package that repeatedly crashes workers for reasons unrelated
  to QA (e.g. content-filter false-positives on the same package twice): add it
  to `done.json` + `state/quarantine.txt` + a `QUARANTINE.txt` note so the pool
  stops re-serving it, and flag it for manual handling (do NOT count as PASS).

### 4. Assemble publishable packages
When the queue is drained:
```
uv run --python 3.12 python <this>/scripts/publish.py         # -> QA_ROOT/_publish
uv run --python 3.12 python <this>/scripts/verify_harbor.py   # must print RESULT: PASS
```
`_publish/<pkg>/` holds the clean deliverable — PASS packages copied unchanged
from source, REPAIRED packages copied from `QA_ROOT/<pkg>/candidate` — with NO
audit files and `__pycache__` stripped. `verify_harbor.py` fails on any missing
core file or leaked audit artifact; extra `solution/*.py` helpers and
repair-bundled input/gold data files are allowed (legitimate package content).

## Multi-tool notes (Codex / Claude Code / Cursor)
- The queue is just a file + flock, tool-agnostic: any mix of Codex, Claude
  Code, and Cursor agents (and multiple sessions per tool) can share one
  `QA_ROOT`. Coordination is entirely through `queue.py`.
- Only requirement: every concurrently-claiming worker uses `queue.py claim`
  with a unique AGENT_ID and writes outputs under `QA_ROOT/<pkg>/`.
- If a separate session is running its own pool on the same queue, its NEW
  claims read the current skills/PLAYBOOK; stop a session only to change the
  rules mid-run.

## Gotchas learned in practice
- Stalled != dead: check whether the worker's last action was "writing repair
  report / marking done" before releasing — releasing + wiping loses finished work.
- `run_checker_probes` leaves `tests/__pycache__` in the tree; `publish.py`
  strips it — do not commit it.
- Repairs may legitimately ADD indispensable input/gold files that were declared
  but missing (CSV/JSON). These belong in the package; keep them.
- `queue.py status` counts `.done` markers, so it is accurate even if state
  files are edited by other sessions.
