# Group-theoretical vibrational mode decomposition with partial occupancy

## Problem background
Strontium barium niobate (SBN) crystals adopt a tetragonal tungsten bronze structure (space group P4bm) with a unit cell nominally containing 45 atoms. Some atomic sites exhibit fractional occupancy, meaning the number of atoms per site is not an integer. Earlier group-theoretical analyses of the vibrational modes assumed full occupancy, yielding incorrect total degrees of freedom (144 or 138) and incorrect irreducible representation decompositions. The goal is to compute the correct total irreducible representation for the real compound, accounting for the actual partial occupancies, which gives a true total of 135 vibrational degrees of freedom. The result demonstrates that partial occupancy leads to half‑integral coefficients for certain symmetry species, resolving earlier discrepancies.

## Approach
The total vibrational representation Γ_tot is obtained by summing the contributions of all atoms, where each atom contributes its site’s irreducible representation (irrep) weighted by its fractional occupancy. The crystallographic sites (Wyckoff positions) and their occupancies are known from Rietveld analysis; the irreps for atoms occupying the four distinct sites in P4bm are available in the literature (Xia et al., Phys. Rev. B 55, 14892).

Specifically:
- 2a site contributes A₁ + A₂ + 2E per atom,
- 2b site contributes A₁ + B₂ + 2E per atom,
- 4c site contributes 2A₁ + A₂ + B₁ + 2B₂ + 3E per atom,
- 8d site contributes 3A₁ + 3A₂ + 3B₁ + 3B₂ + 6E per atom.

The atomic positions and occupancies to use are:
- Ba(1) at 2a, occupancy 0.50,
- Sr/Ba(2) at 4c, occupancy 1.00,
- Nb(1) at 2b, occupancy 1.00,
- Nb(2) at 8d, occupancy 1.00,
- O(1) at 8d, occupancy 1.00,
- O(2) at 8d, occupancy 1.00,
- O(3) at 4c, occupancy 1.00,
- O(4) at 4c, occupancy 0.50,
- O(5) at 8d, occupancy 1.00.

For each atom, multiply the irep contributions of its Wyckoff position by its occupancy. Then sum these weighted contributions over all atoms to obtain the total coefficients for A₁, A₂, B₁, B₂, and E. The total number of degrees of freedom must equal 3×45 = 135. No experimental spectra or fitting is involved; this is a purely group-theoretical computation.

## Reproduction target
Compute the total irreducible representation decomposition for the SBN compound as described, accounting for fractional site occupancies. Produce a single JSON file containing the coefficients (as numbers, which may be integers, fractions, or decimals) for each symmetry species A₁, A₂, B₁, B₂, E and the total degrees of freedom (which must equal 135).

## Assets

- Irreducible representations for Wyckoff positions in space group P4bm: 10.1103/PhysRevB.55.14892

## Workflow steps

### Step 1: Compute total irreducible representation
- Role: scored (load-bearing)
- Action: Using the crystallographic site data (Wyckoff positions 2a, 2b, 4c, 8d) and occupancies from Table 1 (column 4) of the paper, multiply each site’s irreducible representation contributions from the public reference by its fractional occupancy, and sum over all atoms. Report the total coefficients for symmetry species A1, A2, B1, B2, E and the total degrees of freedom (3×45=135).
- Output file: `/app/outputs/step_01_total_irrep.json`
- Format: json
- Contract: {"a1": "<number>", "a2": "<number>", "b1": "<number>", "b2": "<number>", "e": "<number>", "total_df": 135}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_total_irrep.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_total_irrep.json
- path: `/app/outputs/step_01_total_irrep.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total irreducible representation decomposition for the actual (Sr/Ba)₅Nb₁₀O₃₀ compound with partial occupancies.
- schema:
  - `type`: object
  - `required`: `a1`, `a2`, `b1`, `b2`, `e`, `total_df`
  - `properties`:
    - `a1`:
      - `type`: number
      - `description`: Irreducible representation count for A1 (may be fractional)
    - `a2`:
      - `type`: number
      - `description`: Irreducible representation count for A2
    - `b1`:
      - `type`: number
      - `description`: Irreducible representation count for B1 (may be fractional)
    - `b2`:
      - `type`: number
      - `description`: Irreducible representation count for B2
    - `e`:
      - `type`: number
      - `description`: Irreducible representation count for E (may be fractional)
    - `total_df`:
      - `type`: integer
      - `description`: Total degrees of freedom, must equal 135

Notes: This artifact reproduces Eq. (6) of the paper. The checker will recompute the decomposition independently and compare all coefficients within a floating‑point tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_total_irrep.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a1",
          "a2",
          "b1",
          "b2",
          "e",
          "total_df"
        ],
        "properties": {
          "a1": {
            "type": "number",
            "description": "Irreducible representation count for A1 (may be fractional)"
          },
          "a2": {
            "type": "number",
            "description": "Irreducible representation count for A2"
          },
          "b1": {
            "type": "number",
            "description": "Irreducible representation count for B1 (may be fractional)"
          },
          "b2": {
            "type": "number",
            "description": "Irreducible representation count for B2"
          },
          "e": {
            "type": "number",
            "description": "Irreducible representation count for E (may be fractional)"
          },
          "total_df": {
            "type": "integer",
            "description": "Total degrees of freedom, must equal 135"
          }
        }
      },
      "description": "Total irreducible representation decomposition for the actual (Sr/Ba)₅Nb₁₀O₃₀ compound with partial occupancies."
    }
  ],
  "notes": "This artifact reproduces Eq. (6) of the paper. The checker will recompute the decomposition independently and compare all coefficients within a floating‑point tolerance."
}
```

## How you are scored
Your output will be evaluated by a hidden verifier that independently recomputes the total irreducible representation using the same site occupancies and group-theoretical data. The verifier compares the coefficients you report for a1, a2, b1, b2, and e against its own computed values, checking that they match within a narrow tolerance. The total_df must be exactly 135. Your final reward (between 0 and 1) is based on the agreement of all coefficients and the total degrees of freedom. Simply writing the paper’s numbers without performing the actual computation will not work, because the verifier recomputes from scratch.
