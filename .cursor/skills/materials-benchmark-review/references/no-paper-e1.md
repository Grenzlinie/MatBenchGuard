# E1 review without paper

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

- `positive`: Oracle mock or independently justified public output;
- `negative`: malformed, empty, missing, random, sparse, duplicate, non-finite,
  and gaming outputs;
- `discrimination`: meaningfully worse outputs cannot score better;
- `equivalence`: scientifically equivalent representations preserve reward;
- `component isolation`: a single source-bound component cannot pass alone.

These are the only top-level classes. Task-family materials attacks are named
cases and subcoverage within negative/discrimination, with explicit status and
provenance.

An Oracle pass proves only that a positive checker path exists. It does not
prove scientific correctness or Gold provenance.

Process artifacts are recorded only in the contract map. They are never
checker targets, dynamic probes, deductions, gates, or anti-hacking traces.
Explicitly core/scored/final complete models, structures, trajectories,
prediction fields, and meshes are core outputs; uncertain roles stay
`UNCLASSIFIED`, while explicit process-only roles cannot activate attacks or
findings. An ignored core output is a severe checker-core finding.

## Escalate to paper

Stop no-paper inference and trigger paper review for a scientific conflict,
possibly missing necessary definition, uncertain Gold provenance, or explicit
paper-reproduction claim. If paper is temporarily unavailable, use
`NOT_ASSESSABLE`; do not invent a scientific failure.
