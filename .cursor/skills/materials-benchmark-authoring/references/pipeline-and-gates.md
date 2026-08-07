# Authoring pipeline and gates

## State flow

```text
PDF
 -> SOURCE_FROZEN
 -> PAPER_PARSED
 -> EVIDENCE_MAPPED
 -> CANDIDATES_GATED
 -> CANDIDATE_SELECTED
 -> PACKAGE_AUTHORED
 -> ORACLE_VALIDATED
 -> LOCAL_GATES_PASS
 -> INDEPENDENT_REVIEW
 -> REVIEW_PASSED | REVIEW_HANDOFF
```

Do not skip forward. A later success cannot repair a failed earlier scientific gate.

## Stage gates

### G0 Source integrity

- Record original filename and SHA-256.
- Store UniParser token and flags without credentials.
- Require readable text plus any load-bearing equations/tables/captions.
- Route missing load-bearing parse content to `BLOCKED_SOURCE_PARSE`.

### G1 Evidence completeness

- Every task-defining statement has a Markdown locator.
- Every candidate Gold has a policy, condition signature, units, and provenance.
- Every indispensable asset has an identity, role, and availability state.

### G2 Computational-science admission

Reject candidate cores classified as:

- `PURE_INFORMATION_EXTRACTION`;
- `PURE_ALGEBRAIC_COMPUTATION`;
- `EXPERIMENTAL_OPERATION_REQUIRED`;
- `TRIVIAL_EXPERIMENTAL_DATA_REDUCTION`.

Prefer model fitting, optimization, convergence, atomistic/continuum simulation, structure or trajectory analysis, non-trivial error analysis, candidate comparison, and mechanism inference.

### G3 Paper and parameter fidelity

- Preserve paper-reported method, formulas, fixed parameters, and necessary steps.
- Never turn an unreported execution choice into a fixed value.
- Never add a method only because it is easy to verify.
- Require producer/consumer continuity between workflow steps.

### G4 Gold applicability

- Bind every target to one or more complete condition groups.
- Use paper-direct absolute values only under the same system, method, and condition.
- Under changed/smoke conditions, use only paper-supported relations or independently derived references with explicit applicability.
- Block unauditable figure-derived values.

### G5 Resource closure

- `INDISPENSABLE_ASSET` must be bundled, public, runtime-provided, or replaceable by a declared generic equivalent.
- A bundled file must exist under candidate `resources/` during authoring.
- Missing assets produce `BLOCKED_RESOURCE`; they are not solver-searchable parameters.
- Structure files are not indispensable by default. If the paper supplies enough composition/symmetry/lattice/construction information for a solver-built or optimized realization, author the build rule and allow legitimate structural choices. Require a structure resource only for a fixed, non-reconstructible atomic realization on which the Gold depends.

### G6 Optional Enhanced value

Upgrade a Baseline candidate to Enhanced only when at least one result-layer check is:

- derived from required final output;
- supported by a paper equation, invariant, conservation law, ordering, residual, cross-file relation, or auditable offline reference;
- tied to a concrete fabrication or hacking risk;
- materially able to discriminate a wrong scientific result from a credible one;
- compliant with the checker budget.

Affordability alone does not make a checkpoint valuable. If any value condition is absent, keep the candidate as Baseline; do not reject it merely for lacking Enhancement.

### G7 Package and checker correctness

- Public contracts and hidden checks map one-to-one.
- All core outputs and all required condition groups are read.
- Correct output passes; malformed, non-finite, duplicate, and wrong-science outputs fail.
- For Enhanced, Gold remains 60--80% of reward and enhancement remains 20--40%; Baseline uses Gold-only scoring.
- Checker cost passes on real-scale input.
- `solution/solve.sh` is the only entry under `solution/`, is executable, uses inline Python as a `CHECKER_FULL_SCORE_FIXTURE`, and remains outside the environment image.
- Harbor Oracle reports reward `1.0` and full credit for every scoring component without running the primary scientific computation.
- Oracle evidence is stored outside the candidate package and is never reused as Gold provenance, solvability evidence, or proof of scientific execution.

### G8 Independent Review

Only an independent `materials-benchmark-review` can sign off scientific publication. Local validation cannot self-certify.

## Outcomes

| Outcome | Meaning | Publish |
|---|---|---:|
| `REVIEW_PASSED` | Independent Review confirms a publishable Baseline or Enhanced task | yes |
| `READY_FOR_REVIEW` | Local authoring gates pass | no |
| `BLOCKED_SOURCE_PARSE` | Load-bearing paper content was not parsed | no |
| `BLOCKED_RESOURCE` | Indispensable asset is unavailable | no |
| `BLOCKED_ORACLE_VALIDATION` | Oracle fixture, environment, paths, or verifier do not produce reward `1.0` with every component full | no |
| `REVIEW_HANDOFF` | Review produced a non-publishable verdict or operational failure; Authoring stops | no |

Do not revise the scientific task after the first Review. Preserve its artifact and hand the result to the existing Review/Repair routing. Oracle-specific failures remain in Authoring because `solution/` is outside Review/Repair scope.
