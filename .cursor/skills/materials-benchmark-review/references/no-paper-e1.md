# E1 deterministic and dynamic evidence

This layer gathers the package-first (D-layer + dynamic) evidence that does not
itself require the paper. It is **not** a separate "no-paper mode": the normal
review path is always paper-grounded E1 (see `paper-grounded-audit.md`). The
only time the paper is skipped is a Stage 0 `NON_MAT` Hard Gate fail-fast.

Ask whether instruction and tests define a scientifically valid, answerable,
machine-checkable materials task.

## Static evidence

- substantive materials object, operation, and endpoint in instruction;
- necessary task definitions versus legitimate modeling/convergence freedom;
- output and score contract consistency between instruction and tests;
- Gold target, units, normalization, tolerances, and multiple-answer policy;
- checker implementation defects and leakage risks;
- solution Oracle presence or repairable absence.

Do not derive evidence from metadata, resources, steps, task configuration, or
environment declarations.

## Dynamic evidence

Run the real checker in isolation and classify every case:

- `positive`: isolated Oracle mock only;
- `negative`: malformed, empty, missing, random, sparse, duplicate, non-finite,
  and gaming outputs;
- `discrimination`: an independently justified public fixture and meaningfully
  worse outputs cannot score better;
- `equivalence`: scientifically equivalent representations preserve reward
  relative to the same independent public fixture.
- `component isolation`: a single source-bound component cannot pass alone.

These are the only top-level classes. Task-family materials attacks are named
cases and subcoverage within negative/discrimination, with explicit status and
provenance.

Task-family applicability is the stable union of core scientific requirements,
classified core output names, and grading-spec scored outputs. Filter
process-only requirement text; never use it to suppress grading-spec outputs.

An Oracle pass proves only that a positive checker path exists. It does not
prove scientific correctness or Gold provenance.

Process artifacts are recorded only in the contract map. They are never
checker targets, dynamic probes, deductions, gates, or anti-hacking traces.
Complete/full models, structures, trajectories, prediction fields, and meshes
remain core outputs when mislabeled process. Escalate the contradictory role
as `UNCLASSIFIED` without removing core checker analysis. Only non-load-bearing
logs and intermediate audit artifacts are process-only. An ignored core output
is a severe checker-core finding.

## Fixed paper rule (no trigger switch)

There is no paper trigger switch. `A2` (necessary definitions), `A4` (paper
fidelity and reproducibility), and `A5` (Gold credibility) **always read
`paper/`**; `A1` and `A3` are package-first and may extend to the paper when
needed. Every review therefore enters paper-grounded E1 unless Stage 0
fail-fasts on the `NON_MAT` Hard Gate. If the paper is temporarily unavailable,
use `NOT_ASSESSABLE`; do not invent a scientific failure.
