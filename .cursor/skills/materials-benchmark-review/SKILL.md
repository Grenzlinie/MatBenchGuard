---
name: materials-benchmark-review
description: Audit a materials-science Harbor 题包 for integrity, substantive materials relevance, paper fidelity, task-checker alignment, pinned taxonomy labels, and E1 checker robustness. Use when an Agent receives a paper2arm or Harbor 题包 directory and must produce a fixed no-paper or paper-grounded audit bundle without reading solution content.
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

## Choose the paper mode

- `no_paper` asks whether the public task independently defines a coherent,
  machine-checkable benchmark. It never claims paper fidelity.
- `paper_grounded` completes the no-paper checks, then compares the task,
  data, method, Gold, and checker with the bundled paper and applies pinned
  materials taxonomy labels.

Read [references/no-paper-e1.md](references/no-paper-e1.md) for no-paper.
For paper-grounded review, read
[references/paper-grounded-audit.md](references/paper-grounded-audit.md) and
[references/materials-taxonomy.json](references/materials-taxonomy.json).

## Run no-paper E1

Read the pinned taxonomy and write a taxonomy-only assessment outside the
题包 using the evidence shape in `paper-grounded-audit.md`. From this skill
directory, run:

```bash
python scripts/run_review.py <Harbor题包目录> \
  --paper-mode no_paper \
  --execution-level E1 \
  --agent-assessment <taxonomy-assessment.json>
```

The taxonomy assessment must not contain a reproduction type or paper
dimensions. Omitting it remains supported for low-level compatibility but
produces no labels.

When an independently justified public valid output is available, add:

```bash
--known-valid-output <output-directory>
```

The runner:

1. maps and parses Harbor file roles without traversing `solution/`;
2. records input hashes for public and privileged review files;
3. performs a materials relevance prescreen and cross-file static checks;
4. probes materials resources with bounded retries and a private-network deny
   boundary;
5. executes synthetic submissions against the real checker in isolation;
6. verifies every supplied taxonomy label and its exact package quote;
7. synthesizes an initial verdict and fixed report;
8. validates the candidate, preserves the prior bundle, and publishes
   `benchmark_audit/` with rollback on replacement failure.

## Run paper-grounded E1

Read the paper and every public/privileged package role except `solution/`.
Write the evidence-backed assessment defined in `paper-grounded-audit.md`
outside the 题包, then run:

```bash
python scripts/run_review.py <Harbor题包目录> \
  --paper-mode paper_grounded \
  --execution-level E1 \
  --agent-assessment <assessment.json>
```

The runner verifies every quote against the named file, rejects evidence from
`solution/`, validates labels against the pinned Feishu revision, hashes the
paper inputs, and merges paper findings and labels into the fixed bundle.
An unrecoverable E0 package Hard gate publishes a no-paper rejection and skips
the assessment and paper entirely; checker findings that can be repaired do
not suppress paper-grounded evidence.

## Review materials resources

Read
[references/materials-resource-policy.md](references/materials-resource-policy.md).
Every E1 review probes declared resources and records L0–L6, role, category,
identity, reachability, failure class, and whether E2 is recommended.

Use E2 only after reviewing the generated risk evidence. Write a smoke plan and
Python script outside the 题包, then run:

```bash
python scripts/run_review.py <Harbor题包目录> \
  --paper-mode no_paper \
  --execution-level E2 \
  --e2-smoke-plan <e2-smoke-plan.json>
```

The plan contains `schema_version`, the adjacent script filename,
`verifies_resources`, and `timeout_sec`. The runner executes it in Python
isolated mode on a solution-free package copy. The script must write
`e2_smoke_result.json` with the resource IDs it actually exercised. Audit-host
smoke evidence never claims L6 or scientific reproduction; a failed or
unsubstantiated smoke triggers an execution Hard gate.

Private, loopback, link-local, and credential-bearing resource URLs are blocked
by default. `--allow-private-network` exists only for controlled fixtures or
explicitly isolated test networks.

## Completion

This slice is complete only when:

- the command exits successfully;
- `benchmark_audit/` contains every required JSON, JSONL, Markdown, log, and
  manifest artifact;
- the report records the selected paper mode and execution level;
- no-paper consistency is `NOT_ASSESSED`; paper-grounded consistency records
  a reproduction type, all five dimensions, and evidence or
  `NOT_ASSESSABLE`;
- paper-grounded labels conform to the pinned taxonomy, include its source
  revision and exact package evidence in the report, and leave the original
  manifest unchanged;
- every checker probe records its observed reward and exit status, or the audit
  is `NOT_ASSESSABLE`;
- every declared resource records a role, material category, required and
  verified level, identity state, reachability status, and failure class;
- any resource below its required level produces a structured finding rather
  than only an E2 recommendation;
- critical permanent, authorization, license, or identity failures produce
  structured Hard-gate findings, while transient failures remain distinct;
- E2 records `SMOKE_RUN` and `scientific_reproduction: false`; audit-host smoke
  leaves `environment_verified: false`;
- a supplied known-valid public output executes; rejection produces
  `KNOWN_VALID_OUTPUT_REJECTED` and prevents `PASS`;
- any malformed or adversarial output at or above the threshold produces a
  FATAL finding and `REJECT`;
- the checker executes in a copied runtime that contains no `solution/`, and
  static and dynamic evidence both record that boundary.

Do not infer paper fidelity, scientific reproduction, Harbor-environment L6,
or task-family-specific robustness from this slice.
