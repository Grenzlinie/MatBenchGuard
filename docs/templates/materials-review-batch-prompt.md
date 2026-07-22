# Materials Review/Repair Batch Prompt

The human coordinator supplies an explicit list of package identifiers and may
set `max_parallelism` (default: 3). The main Agent creates each run before
delegating work; a failed package never cancels unrelated runs.

```text
packages:
  - cluster-123/topic-name/paper-456
  - cluster-789/other-topic/paper-012
max_parallelism: 3
```

Create the explicit batch before delegating work:

```sh
python tools/create_materials_review_batch.py \
  <package-id-1> <package-id-2> --agent <worker-id> --max-parallelism 3
```

Then the worker uses `run_review.py --run-dir <run-dir>`. Conditional findings
are planned in that run's `plan.json`, and the same worker or an independent
repair worker uses `run_repair.py --run-dir <run-dir>`. Only the main Agent
updates `corpus_review_tracking.json` after the batch has terminal results.
