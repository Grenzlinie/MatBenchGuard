---
name: materials-benchmark-review
description: Audit a materials-science Harbor 题包 for integrity, substantive materials relevance, task-checker alignment, and E1 checker robustness. Use when an Agent receives a paper2arm or Harbor 题包 directory and must produce a fixed no-paper audit bundle without reading solution content.
---

# Materials Benchmark Review

Audit one Harbor 题包 at a time. The authoritative result is the fixed
`benchmark_audit/` bundle written inside that 题包.

## Inputs

Accept a `paper-{id}` directory containing the Harbor roles defined in
[references/harbor-contract.md](references/harbor-contract.md).

Treat `tests/` as privileged review evidence. Treat `solution/` as outside the
evidence boundary: confirm that the directory exists, but never list or read
its contents.

## Run the no-paper E1 slice

From this skill directory, run:

```bash
python scripts/run_review.py <Harbor题包目录> \
  --paper-mode no_paper \
  --execution-level E1
```

When an independently justified public valid output is available, add:

```bash
--known-valid-output <output-directory>
```

The runner:

1. maps and parses Harbor file roles without traversing `solution/`;
2. records input hashes for public and privileged review files;
3. performs a materials relevance prescreen and cross-file static checks;
4. executes synthetic submissions against the real checker in isolation;
5. synthesizes an initial verdict and fixed report;
6. validates the candidate, preserves the prior bundle, and publishes
   `benchmark_audit/` with rollback on replacement failure.

Read [references/no-paper-e1.md](references/no-paper-e1.md) before interpreting
the result.

## Completion

This slice is complete only when:

- the command exits successfully;
- `benchmark_audit/` contains every required JSON, JSONL, Markdown, log, and
  manifest artifact;
- the report says `paper_mode: no_paper` and `execution_level: E1`;
- paper consistency is `NOT_ASSESSED`;
- every checker probe records its observed reward and exit status, or the audit
  is `NOT_ASSESSABLE`;
- a supplied known-valid public output executes; rejection produces
  `KNOWN_VALID_OUTPUT_REJECTED` and prevents `PASS`;
- any malformed or adversarial output at or above the threshold produces a
  FATAL finding and `REJECT`;
- the checker executes in a copied runtime that contains no `solution/`, and
  static and dynamic evidence both record that boundary.

Do not infer paper fidelity, scientific reproduction, resource reachability, or
task-family-specific robustness from this E1 slice.
