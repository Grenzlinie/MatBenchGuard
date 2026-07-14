---
name: BioMaster-benchmark-review
description: audit biology, biomedical, and bioinformatics benchmark packages for genuine biological relevance, resource reachability, task answerability, execution feasibility, checker validity, anti-gaming robustness, reproducibility, leakage, safety, and optional paper fidelity. use when reviewing a benchmark directory or zip containing instructions, resources, workflows, grading specifications, checkers, gold or reference files, environments, and optional papers. supports no-paper and paper-grounded modes, execution levels e0-e4, and writes a fixed audit bundle into the benchmark root.
---

# BioMaster-benchmark-review

Audit a candidate biology, biomedical, or bioinformatics benchmark before admission into a benchmark suite.

A valid benchmark must be answerable from its public instructions, declared resources, and permitted environment. Its checker must reward the scientific work the task claims to test, distinguish different answer qualities, and resist trivial or adversarial submissions.

Never inspect or rely on `solution/`, `solve.sh`, hidden answers, or reference solution code when deciding whether the task is valid.

## Inputs

Accept a benchmark directory or ZIP archive. Locate functional equivalents of:

- instruction or task description;
- task, manifest, or configuration files;
- steps or workflow definitions;
- resource declarations;
- grading specification and checker;
- gold, reference, fixture, or test files;
- environment, requirements, lock files, or containers;
- optional paper and supplementary materials.

Do not reject a package solely because names or layout differ. First create a file-role mapping.

## Configure the audit

Choose two independent settings.

### Paper mode

- `no_paper`: audit whether the package independently defines a valid benchmark. Do not claim paper fidelity. Mark paper-dependent dimensions `NOT_ASSESSED`.
- `paper_grounded`: complete all no-paper checks, then verify the task against the paper, figures, methods, supplements, code, models, and data provenance.

### Execution level

- `E0 STATIC`: structure, code, semantics, security, and declarations.
- `E1 CHECKER_DYNAMIC`: generic and task-specific checker attacks.
- `E2 SMOKE_RUN`: minimal input proves the workflow starts and emits valid outputs.
- `E3 REDUCED_REPRODUCTION`: run the complete workflow on reduced data.
- `E4 FULL_REPRODUCTION`: run the full task in the declared environment.

Default to at least `E1`. Only claim that the scientific workflow was executed when `E2-E4` was actually completed. Only claim reproduction when `E3` or `E4` supports it.

## Prepare the fixed output workspace

Before auditing, run:

```bash
python scripts/prepare_audit_output.py <benchmark-directory-or-zip> \
  --paper-mode no_paper \
  --execution-level E1
```

Read the emitted JSON. Use its `benchmark_root` and `audit_temp_dir` paths.

The script:

- safely extracts ZIP input when necessary;
- locates the benchmark root;
- archives any prior `benchmark_audit/` under `benchmark_audit_history/<audit_id>/`;
- creates `<benchmark_root>/.benchmark_audit_tmp/` with the required report skeleton;
- never writes inside `tests/`, `solution/`, `paper/`, or the submission output directory.

All audit evidence and reports must be written into the temporary audit directory. Do not leave the final result only in chat.

## Audit workflow

Use cheap deterministic gates before expensive model or execution checks. Stop expensive phases after a fatal gate, but still write a complete audit report that records skipped phases and reasons.

### Phase 0 — Package structure and security

Run:

```bash
python scripts/audit_package.py <benchmark-root> \
  --output <audit-temp-dir>/evidence/static_checks/audit_static.json
```

Check:

- required roles exist and files parse;
- paths, outputs, schemas, weights, and resource declarations agree across files;
- the instruction clearly defines inputs, outputs, units, identifiers, reference versions, tolerances, missing values, sorting, and duplication rules;
- checker inputs are declared and load-bearing outputs are actually read;
- archive paths, symlinks, deserialization, subprocesses, XML/YAML parsing, filesystem access, network access, and resource limits are safe;
- public files do not leak hidden tests, gold values, checker thresholds, or solution paths.

Read `references/security_audit.md` for mandatory security checks.

Fatal examples:

- no usable instruction or scoring logic;
- the requested submission cannot be determined;
- exploitable arbitrary code execution or hidden-answer access;
- core configuration is unparseable and not locally repairable.

### Phase 1 — Biological admissibility and capability alignment

Read `references/biology_gate.md`.

Classify the task as:

- `BIO_CORE`
- `BIO_METHOD`
- `BIO_WRAPPER`
- `NON_BIO`
- `AMBIGUOUS`

Score and cite evidence for biological object, biological data, biological operation, biological endpoint, and domain dependence. Do not classify from keywords or title alone.

Extract:

```yaml
capability_target:
  primary: ...
  secondary: [...]
  excluded: [...]
```

Build the enforcement chain:

```text
claimed capability
→ required scientific operation
→ observable output
→ checker-enforced evidence
```

Determine the answer type:

- `DETERMINISTIC_EXACT`
- `TOLERANCE_BASED`
- `SET_VALUED`
- `RANKING_BASED`
- `EVIDENCE_BASED`
- `OPEN_ENDED`

Reject `NON_BIO`. Reject `BIO_WRAPPER` when the suite claims to measure biological research ability. Treat any benchmark that can pass without its claimed scientific operation as a fatal construct-validity failure.

### Phase 2 — Resource identity, reachability, and sufficiency

Run:

```bash
python scripts/ping_resources.py <benchmark-root-or-resources.json> \
  --output <audit-temp-dir>/resource_checks.json
```

Read `references/resource_reachability.md`.

For every resource, record its role:

- `CRITICAL`
- `REPLACEABLE`
- `OPTIONAL`

Record the highest verified level:

- `L0 DECLARED_ONLY`
- `L1 HOMEPAGE_REACHABLE`
- `L2 METADATA_RESOLVED`
- `L3 ARTIFACT_DISCOVERED`
- `L4 ARTIFACT_DOWNLOADABLE`
- `L5 IDENTITY_VERIFIED`
- `L6 ENVIRONMENT_VERIFIED`

A homepage returning HTTP 200 is not data access. Core data normally require at least `L4`; exact reproduction normally requires `L5` or `L6`.

Verify identifiers, versions, organisms, strains, samples, conditions, assay type, reference builds, file names, sizes, checksums, licenses, authentication, automation restrictions, mirrors, and runtime-environment access.

Also test sufficiency: reachable resources may still omit sample sheets, group labels, references, annotations, models, tokenizers, biomass definitions, reaction mappings, curation tables, splits, controls, or calibration assets.

Distinguish transient DNS, TLS, timeout, and rate-limit failures from persistent unavailability or identity mismatch.

Fatal examples:

- an irreplaceable core resource is unavailable or only named by a database homepage;
- required access needs unprovided login, approval, CAPTCHA, or private permission;
- data identity does not match the task;
- resources are accessible but insufficient to determine the requested result;
- use violates license, privacy, ethics, or consent requirements.

### Phase 3 — Task design, gold, feasibility, and checker static audit

Read:

- `references/checker_audit.md`
- `references/task_types_and_leakage.md`
- `references/audit_dimensions.md`

Audit:

- instruction completeness and distinction among `REQUIRED`, `RECOMMENDED`, `ALLOWED`, and `FORBIDDEN` choices;
- whether the data can answer the biological question;
- sample size, controls, biological unit, pseudoreplication, and split integrity;
- output contract and identifier semantics;
- checker coverage, score direction, tolerance, partial credit, missing values, and all-or-none behavior;
- whether one easy field can dominate the reward;
- whether the gold is experimental, curated, computational, or figure-digitized;
- gold independence, uncertainty, annotation disagreement, and tolerance basis;
- runtime, storage, memory, dependency, solver, and network feasibility;
- random seeds, versions, database drift, container pinning, and deterministic behavior;
- failure attribution among data, environment, execution, format, checker, and scientific mismatch.

Do not force a set-valued or open scientific task into one exact gold artifact without a defensible equivalence rule.

Fatal examples:

- the task is underdetermined from declared inputs;
- a load-bearing output is ignored;
- the checker compares only public hard-coded values while claiming to recompute science;
- biologically incorrect but syntactically valid output can score highly;
- severe train-test leakage invalidates the intended generalization claim;
- declared resources cannot physically complete the task.

### Phase 4 — Checker dynamic, gradient, and metamorphic testing

Run the generic probes:

```bash
python scripts/dynamic_checker_probe.py <benchmark-root> \
  --output <audit-temp-dir>/checker_tests.json
```

Then add domain-specific probes when required.

At minimum test:

- missing, empty, malformed, duplicate, irrelevant, and non-finite outputs;
- minimal gold-shaped output;
- omission of declared models, predictions, logs, or supporting evidence;
- random and constant baselines;
- threshold boundaries;
- scientifically correct fixtures when available;
- quality gradients such as 0%, 10%, 30%, 50%, 80%, and 100% correctness;
- semantic invariants such as row reordering, equivalent serialization, harmless metadata changes, synchronized matrix permutations, and object ordering.

Evaluate:

- monotonicity;
- sensitivity;
- specificity;
- saturation;
- robustness;
- semantic rather than superficial scoring.

Load task-specific attacks for BED, VCF, count matrices, rankings, protein sequences or structures, metabolic models, images, and other specialized outputs.

Fatal examples:

- a minimal or random answer passes;
- core process artifacts can be omitted;
- score decreases as scientific quality improves;
- equivalent scientific outputs receive materially different scores because of ordering or serialization;
- a correct answer scores poorly.

### Phase 5 — Paper-grounded fidelity

Run only in `paper_grounded` mode. Read `references/paper_grounded_audit.md`.

First classify the benchmark as:

- `EXACT_REPRODUCTION`
- `METHOD_REIMPLEMENTATION`
- `SCIENTIFIC_EXTENSION`

Verify:

- methods, order, parameters, software, solver, database, and versions;
- accession, sample, organism, tissue, condition, controls, exclusions, and splits;
- figure and table values with visual PDF inspection where needed;
- supplementary models, code, initialization, curation, and hidden manual decisions;
- the complete gold provenance chain;
- whether current database drift changes the target;
- whether the checker rewards paper-faithful results.

A scientific extension must not be scored solely against exact paper values. A method reimplementation must define equivalence. Exact reproduction requires fixed historical inputs and versions.

Fatal examples:

- gold conflicts with the paper or has no supportable provenance;
- following the paper correctly leads to a low checker score;
- missing manual curation or supplementary assets makes the target indeterminate;
- historical versions are not fixed and exact results cannot be reproduced.

### Phase 6 — Synthesis and fixed output

Read `references/report_schema.md` and complete every required file under `<benchmark-root>/.benchmark_audit_tmp/`:

```text
benchmark_audit/
├── audit_report.md
├── audit_report.json
├── findings.jsonl
├── resource_checks.json
├── checker_tests.json
├── audit_manifest.json
├── evidence/
│   ├── static_checks/
│   ├── resource_checks/
│   ├── checker_tests/
│   └── paper_checks/
├── logs/
│   └── audit.log
└── patches/
    └── suggested.patch        # optional
```

Use `NOT_ASSESSED` for inapplicable or unexecuted sections. Never silently omit a required section because a prior gate failed.

Finalize atomically:

```bash
python scripts/finalize_audit_output.py <benchmark-root>
```

This validates the JSON and JSONL files, cross-checks core fields between Markdown and JSON, verifies evidence paths, writes SHA-256 hashes into `audit_manifest.json`, and renames `.benchmark_audit_tmp/` to `benchmark_audit/`.

The audit is incomplete until `<benchmark-root>/benchmark_audit/` exists and passes final validation.

## Verdicts

Hard gates override weighted scores.

- `PASS`: score at least 0.80, no fatal finding, no unresolved high finding, and every critical dimension at least 0.50.
- `CONDITIONAL`: score 0.60-0.79 or repairable high findings. State exactly which phases must be rerun.
- `REJECT`: score below 0.60, any fatal finding, or any critical dimension below 0.50.
- `NOT_ASSESSABLE`: essential evidence is unavailable and cannot be resolved from allowed inputs.

Critical dimensions are biological admissibility, capability alignment, resource reachability, task answerability, checker validity, and paper fidelity when applicable.

## Mandatory review principles

1. Hard gates override scores.
2. Determine whether the task is genuinely biological before expensive review.
3. Data existence, downloadability, identity, sufficiency, and legal usability are separate checks.
4. A package name is not a reproducible environment.
5. Statistical anomalies are evidence, not automatic proof of fabrication.
6. Rules must be species-, assay-, and file-type-aware.
7. Multiple scientifically valid outputs require equivalence-aware scoring.
8. Checker quality includes anti-gaming, monotonicity, sensitivity, specificity, and semantic invariance.
9. Distinguish data failure, environment failure, execution failure, output failure, checker failure, and scientific mismatch.
10. No-paper mode must not claim paper fidelity.
11. Separate exact reproduction, method reimplementation, and scientific extension.
12. Every fatal and high finding requires an evidence chain and a verification test after repair.
13. Separate facts, inferences, and recommendations.
14. Preserve the user's language in the human-readable report.
15. Always write the fixed audit bundle into the benchmark root; chat is only a summary channel.
