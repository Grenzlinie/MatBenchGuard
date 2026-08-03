# Paper evidence and candidate selection

## Evidence map

Create records before drafting prose:

| Record | Required fields |
|---|---|
| system | material, structure/composition, physical state, boundary/ensemble |
| method | method name, equations, code/model if indispensable, paper locator |
| parameter | name, class, value or selection policy, units, scope, locator |
| condition group | stable ID, complete signature, target IDs, locator |
| Gold candidate | target ID, policy, value/relation, units, applicability, locator |
| resource | ID, role, indispensability, availability, filename/locator |
| workflow edge | producer step/output, consumer step/input |
| checkpoint candidate | output, relation/invariant, cost, attack addressed |

Use exact Markdown headings, table labels, equation labels, or distinctive text spans as locators. Do not use vague provenance such as "the paper".

## Parameter classification

- `PAPER_FIXED`: paper reports the task-relevant value; copy faithfully.
- `SOLVER_SEARCHABLE`: no unique paper value; expose search, convergence, optimization, or solver justification.
- `TARGET_DEFINING`: identifies system, state, or scientific condition; must be explicit.
- `INDISPENSABLE_ASSET`: data, a non-reconstructible fixed atomic realization/structure snapshot, potential, trained model, or specific code that must be obtainable.

A missing CIF is not an asset failure by itself. Record paper-given composition, crystal system/space group, lattice/Wyckoff data, and construction rules as `TARGET_DEFINING` or `PAPER_FIXED`. Record unspecified atomic placement, supercell realization, termination, defect site, initial perturbation, or pre-relaxation choice as `SOLVER_SEARCHABLE` when a solver can build and justify a compatible structure. Use an indispensable structure asset only when the Gold requires the same unreconstructible atomic realization and equivalent structures are not allowed.

For each parameter record, include:

```json
{
  "paper_reports_unique_value": false,
  "instruction_requires_unique_value": false,
  "checker_requires_unique_value": false
}
```

The three booleans expose hidden parameter fixation.

## Candidate enumeration

Aim for three to five candidates spanning different scientific operations. Examples:

- reproduce a multi-condition property curve and compare regimes;
- fit a physically constrained model and evaluate residual/invariant behavior;
- compute structure/trajectory summaries and infer a paper-supported mechanism;
- optimize or converge a numerical model and compare candidate materials;
- reimplement a paper method and evaluate multiple coupled outputs.

Do not create variants that differ only in filename or number of table rows.

## Candidate ranking

Rank lexicographically, not by a single averaged score:

1. Q0 passes.
2. Paper alignment and Gold provenance are complete.
3. Indispensable assets are closed.
4. Output contract can be self-contained.
5. At least one affordable enhanced checkpoint exists.
6. Compute fits the solver environment.
7. The task retains meaningful solver agency.

A lower-ranked but fully evidenced candidate beats a more impressive candidate with guessed parameters or missing inputs.

## Anti-patterns caught before authoring

- Asking the solver to read or reproduce a paper figure.
- Scoring a number already printed in the instruction.
- Adding a convenient method not used or supported by the paper.
- Changing conditions while keeping the original absolute Gold.
- Calling a missing potential or dataset a solver choice.
- Calling every missing CIF an indispensable asset even though the paper defines a buildable structure.
- Requiring a workflow artifact that no later step or checker consumes.
- Choosing a full trajectory as the only possible checkpoint.
