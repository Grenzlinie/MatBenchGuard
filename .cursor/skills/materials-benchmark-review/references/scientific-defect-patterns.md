# Scientific defect patterns

Review every pattern below against the complete package and paper. Record each
one in `scientific_risk_patterns` as `PASS`, `FAIL`, `NOT_APPLICABLE`, or
`NOT_ASSESSABLE`. A mechanical candidate is not a finding until the Agent
adjudicates it. Every `FAIL` requires a matching confirmed finding.

Silence in the paper is not a defect by itself. A package may define a
scientifically valid extension or implementation choice that the paper did not
discuss. Fail only when the package contradicts its own contract or the paper,
misrepresents reproduction intent, omits a target-defining choice while
expecting a unique answer, or uses unsupported reference values.

## Required patterns

### `CROSS_STEP_PARAMETER_CONTRADICTION` → 2.2 / C02

Compare repeated values and definitions across `instruction.md`, `steps.json`,
`grading_spec.json`, resources, and checker. Check analysis windows, simulation
duration, temperature, pressure, load, timestep, cutoff, coordinate convention,
units, sampling interval, output rows, and thresholds.

Example: one step says to analyze the final 15 ns while a downstream scored step
says final 5 ns. Different production and analysis durations are not inherently
wrong; fail only when two statements govern the same quantity or output and
cannot both be satisfied.

### `METHOD_REFERENCE_MISMATCH` → 2.3 / C03

Fail when the package materially changes the paper's physical system, method,
conditions, or structure-generation protocol but still requires agreement with
the paper's absolute numerical values as if it were a faithful reproduction.

Method changes are allowed when the paper did not prescribe the choice, the task
is honestly classified as reimplementation/extension, and Gold is independently
generated and validated for the declared method. A paper value is not portable
across materially different atom counts, vacancies, codes, functionals,
potentials, ensembles, temperatures, trajectories, or preparation histories
without evidence.

A reduced or smoke-scale system can validly score a qualitative trend,
direction, ordering, sign, or invariant relationship instead of an absolute
paper value when all of the following hold:

1. the public task and grading contract explicitly declare that relational
   target rather than exact-value reproduction;
2. the paper or another authoritative source supports the relationship;
3. there is scientific justification that the relationship remains applicable
   to the declared reduced system and conditions, including relevant
   finite-size or timescale limitations;
4. the checker scores only the supported relation and accepts scientifically
   equivalent numerical realizations;
5. counterexamples, reversed trends, ties/boundaries, and component-isolation
   probes demonstrate discrimination.

For example, reducing a 500-atom calculation to 50 atoms is not itself a defect
when the benchmark evaluates a supported ordering rather than requiring the
50-atom output to equal the 500-atom paper values.

### `UNSUPPORTED_SYNTHETIC_GOLD` → 2.6 / C04

Trace every Gold value to a paper table/figure with matching conditions, an
authoritative public source, or a reproducible calculation using the declared
method and inputs. Fail when acceptance values are random, randomly perturbed,
linearly interpolated, curve-fitted, trend-shaped, or smoke/dummy/placeholder
outputs and then presented as truth.

Interpolation or fitting is allowed only when it is the scientifically declared
target, its source observations are valid, and the checker evaluates the
declared fitted quantity rather than treating a synthetic estimate as ground
truth.

A source-backed trend or ordering is not `UNSUPPORTED_SYNTHETIC_GOLD`. The
checker may encode a relation such as increasing/decreasing, A > B, sign,
rank order, or a bounded qualitative regime without storing exact paper values,
provided its provenance and applicability are documented. Distinguish:

- **valid relational reference**: the authoritative source supports the exact
  relation being scored for the relevant domain, and the checker tests that
  relation directly;
- **invalid trend-shaped pseudo-Gold**: code invents plausible numbers from a
  paper figure/trend and then scores their magnitudes as if computed truth.

The words `smoke`, `random`, `fit`, or `interpolate` in `tests/` are
mechanical candidates only. Dismiss the candidate when the code is test-data
generation, robustness probing, a declared analysis operation, or a smoke-scale
runner that does not define unsupported acceptance truth.

`solution/` is outside Review and Repair. Do not open or use it to establish
Gold provenance; judge only provenance recorded in in-scope package files and
authoritative sources.

### `MISSING_TARGET_DEFINING_INPUTS` → 2.3 / C03

Fail when multiple scientifically reasonable choices for an omitted parameter
would materially change the expected answer. Check structure, cell/density,
composition, defects, charge/spin, potential/pseudopotential/basis, cutoff,
k-points, thermostat/barostat, timestep, equilibration, seed policy, boundary
conditions, reference state, and target-defining analysis settings.

Do not fail parameters that the paper did not fix and that are genuinely
solver-selectable under the parameter policy.

### `CRYSTALLOGRAPHIC_SELF_CONTRADICTION` → 2.3 / C03

Check that axes lie in claimed planes when required, Miller indices and
coordinate conventions agree, interfaces can be constructed as described, and
the package matches the paper's orientation relationship. Fail geometrically
impossible or mutually inconsistent definitions.

### `UNSPECIFIED_MD_CONDITIONS` → 2.3 / C03

For MD-dependent targets, check target-defining temperature, timestep,
thermostat/barostat and damping, velocity initialization, equilibration,
production duration, sampling, and ensemble. Fail omissions that prevent a
unique or fairly scoreable result; mark irrelevant MD fields not applicable.

### `INCOMPLETE_CELL_BOUNDARY_DEFINITION` → 2.3 / C03

Check cell dimensions or construction rule, grain/slab thickness, periodic/free
boundaries, fixed layers, interface count and location, overlap deletion, and
surface treatment. Fail when these choices materially affect the scored result
and are neither fixed nor legitimately solver-selectable.

### `AMBIGUOUS_OBSERVABLE_DEFINITION` → 2.2 / C02

Check the complete mathematical definition of each scored observable: reference
energy, normalization, area multiplicity, sign, averaging, uncertainty,
neighbor definition, smoothing/binning/peak finding, and classification rules.
Fail when different reasonable definitions produce different scored answers.

### `AMBIGUOUS_LOAD_SEMANTICS` → 2.2 / C02

Check whether force/stress/load is per atom, total, per area, or per volume;
which atoms/region receive it; and how the effective area/volume is defined.
Fail when magnitudes can differ by system size under equally plausible readings.

### `OUTPUT_SCORING_CONTRACT_CONTRADICTION` → 2.2 / C02

Compare prose, output schema, grading spec, checker, and expected row/key counts.
Fail when the public contract cannot produce what the checker scores, such as
requesting one load in the body while requiring three loads or monotonicity
across them in grading.

### `UNVERIFIABLE_COMPUTATION_CLAIM` → 2.4 / C04

Do not fail merely because a checker reads final CSV rather than trajectories.
Fail when the package claims to assess execution of a scientific computation,
but the scored outputs are insufficient to distinguish that capability from
lookup, hardcoding, trend fitting, or a tiny fabricated result. In that case
either:

- define reproducibility artifacts as public final deliverables and score their
  scientifically relevant content; or
- narrow the capability claim to what the final results actually demonstrate.

Also consider `SCIENTIFIC_REASONING_ABSENT` and checker discrimination. Do not
add unverifiable process requirements solely to manufacture difficulty.

### `ANALYSIS_PROTOCOL_UNDERSPECIFIED` → 2.2 / C02

For analysis-derived Gold, check bin width, smoothing, peak search, fit range,
neighbor cutoff, Voronoi variant/radii, classification index sets, averaging
window, uncertainty estimator, and periodic-coordinate handling when they
materially affect the result. Fail only when the paper/package fixes the method
or the checker expects a unique value that depends on an omitted choice.

### `SIMULATION_CONTRACT_UNDERDETERMINED` → 2.3 / C03

For every simulation task, read the full paper and package and build the
simulation parameter matrix required by `paper-grounded-audit.md`. Fail when an
execution-required, target-defining, or scoring-sensitive parameter is absent
or unresolved and multiple scientifically reasonable choices can change the
simulation or accepted result.

This applies across MD, DFT, Monte Carlo, phase-field, finite-element, and other
simulation methods. Check system definition, reference frame, model,
initialization, boundary/load, evolution, thermodynamic control, run extent,
analysis, and derived parameters. Zero lexical candidates never establish
completeness.

When a task uses paper methods, conditions, or absolute Gold and an essential
parameter is neither stated nor uniquely derivable from the paper, supplement,
or declared authoritative source, fail
`ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE`. The finding is non-repairable
`ABANDON`. Do not import a software default, customary value, or value from a
different paper. A self-contained scientific extension with independently
validated Gold may define a value that the source paper did not use.

### `SIMULATION_PARAMETER_DEPENDENCY_BROKEN` → 2.3 / C03

Trace each parameter from the step that introduces it through every downstream
consumer and scored output. Fail when an upstream structure, orientation,
model, boundary, or computed value is free or incomplete but a later step uses
a fixed direction, number, formula, paper Gold, or checker branch valid only
for one upstream choice.

Coordinate labels are one example, not a special case. Mapping a physical
direction such as `{111}` to `x` rather than `z` is allowed when the complete
orientation mapping, load, boundary, analysis, output conversion, Gold, and
checker remain physically equivalent. Merely changing `z` to `x` without
updating the dependency chain is not a repair.

## Gold provenance evidence

For every scored absolute or relational reference record:

```text
Gold file/key or relation → target type (absolute/range/trend/order/sign)
→ source or generating command → physical system/conditions
→ applicability to the benchmark system → independent validation
→ tolerance/boundary rationale
```

The presence of a plausible number is not provenance. A passing author smoke
test proves packaging only and must never validate Gold.
