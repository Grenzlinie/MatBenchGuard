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
