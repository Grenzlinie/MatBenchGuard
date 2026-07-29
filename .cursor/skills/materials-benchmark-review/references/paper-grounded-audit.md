# Paper-grounded audit and parameter policy

Always read the paper for scientific validity, data/method fidelity, and Gold.
Only an already-established `NON_MATERIALS_TASK` may skip the paper.

Classify intent as `EXACT_REPRODUCTION`, `METHOD_REIMPLEMENTATION` (default), or
`SCIENTIFIC_EXTENSION`.

## Fixed or source-required parameters

Supply or unambiguously derive any value that defines the target, physical
system, boundary condition, reference identity, units, comparison basis, Gold,
tolerance, or checker-accepted result. If the paper/instruction fixes it, the
package must match. The checker must not secretly require a value the prompt
allows the solver to choose.

Examples include composition, structure/phase, charge or spin state,
target-defining temperature/pressure, ensemble, boundary conditions, reference
state, unit convention, evaluation split, target label, and fixed paper
parameters essential to the claimed reproduction.

## Solver-selectable parameters

In method reimplementation or extension, equivalent software, compatible
versions, solver-selected convergence settings, meshes, cutoffs, seeds,
supercells, optimizers, and search settings may be chosen only when:

1. the paper/instruction does not fix them;
2. multiple choices validly implement the method;
3. the choice does not redefine the target or expose Gold;
4. the checker accepts scientifically equivalent results instead of one hidden
   implementation;
5. the answer records choices material to reproducibility.

These are not automatically free choices in exact reproduction or when results
materially depend on them.

## Paper fidelity checklist

Record exact paper and package evidence for:

- instruction/target fidelity;
- data, sample, structure, split, and condition fidelity;
- method and fixed-parameter fidelity;
- reproduction-intent honesty;
- Gold values or documented derivation;
- unit, direction, tolerance, and uncertainty consistency.

Paper-sourced Gold is by design. Open a defect only for a wrong/absent citation,
paper-to-package mismatch, grading-to-checker mismatch, fabricated tolerance,
or misdeclared reproduction intent.

## Method and Gold portability

Build a side-by-side table for the paper and package covering code/method,
physical system and atom count, composition/defects, structure preparation,
functional/potential, basis/pseudopotential, cutoff/k-points, ensemble,
temperature schedule, timestep, trajectory length, analysis window, and
observable definition.

If any material difference can change an absolute answer, paper values are not
portable to the package by default. Require either:

1. exact or scientifically evidenced equivalence; or
2. independently generated and validated Gold for the package's declared
   method and conditions.

Otherwise record `METHOD_REFERENCE_MISMATCH` when exact-value agreement is
required. Do not treat a more modern code, larger/smaller system, shorter smoke
calculation, or plausible-looking trend as evidence that absolute numerical
results remain comparable.

Absolute-value portability and relation portability are different claims. A
reduced system may be acceptable when the declared endpoint is a trend,
ordering, sign, or qualitative regime supported by the paper/authoritative
source. Record why that relationship should survive the system/method change,
including finite-size and timescale limits, and verify that the checker scores
only the supported relation. Do not require a 50-atom smoke result to equal a
500-atom paper value when exact reproduction is not the task.

For each Gold file/key record its source or generating command and inspect that
producer. Random generation, noise injection, interpolation, curve fitting,
manual trend shaping, or smoke/dummy/placeholder data in `tests/` triggers an
`UNSUPPORTED_SYNTHETIC_GOLD` candidate. The Agent must confirm or dismiss it
from primary evidence. A keyword hit in tests is not a defect: dismiss it when
it creates negative-test fixtures, performs the declared analysis, or runs a
reduced smoke calculation without defining unsupported acceptance truth.
`solution/` is out of scope and must not be opened to complete this trace.
