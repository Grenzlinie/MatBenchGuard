# Perovskite Hydride Formation Ability via Goldschmidt Tolerance Factor

## Problem background
Perovskite-type hydrides (ABH₃) are promising hydrogen storage materials with high volumetric hydrogen density. The geometric stability of the perovskite structure is often assessed by the Goldschmidt tolerance factor t = (R_A + R_X) / (√2 (R_B + R_X)), which depends on the ionic radii of the A and B cations and the anion X. For hydrides, the anion is H⁻ with a commonly adopted radius of 0.140 nm. A synthesis screening could be guided by whether a candidate (R_A, R_B) pair falls within a predicted formation region — a quadrilateral in (R_A, R_B) space bounded by two t-isolines and octahedral stability limits on R_B. The task is to compute t for a set of reported stoichiometric perovskite hydrides using the Shannon effective ionic radii provided below and to determine, for each hydride, whether its ionic radii place it inside that quadrilateral region.

## Approach
The analysis uses the Goldschmidt tolerance factor t = (R_A + R_H) / (√2 (R_B + R_H)) with R_H = 0.140 nm. The Shannon effective ionic radii appropriate for the perovskite coordination (12-fold cubo-octahedral for the A site, 6-fold octahedral for the B site) are given for each hydride in the table below. For mixed-occupancy B-sites, the radius is already a weighted average. The quadrilateral formation region is defined by: 0.90 ≤ t ≤ 1.10 and 0.058 nm ≤ R_B ≤ 0.102 nm (the latter derived from Pauling's octahedral stability criterion 0.414 < R_B/R_H < 0.732). The workflow simply collects the provided radii, computes t and checks membership, and outputs the results for the 16 stoichiometric ABH₃ hydrides.

## Input: Shannon effective ionic radii to be used (R in nm)
| hydride_name              | R_A (nm) | R_B (nm) |
|---------------------------|----------|----------|
| SrLiH3                    | 0.144    | 0.076    |
| BaLiH3                    | 0.161    | 0.076    |
| EuLiH3                    | 0.153    | 0.076    |
| NaMgH3                    | 0.139    | 0.072    |
| KMgH3                     | 0.164    | 0.072    |
| RbMgH3                    | 0.172    | 0.072    |
| HT-CsMgH3                 | 0.188    | 0.072    |
| RbCaH3                    | 0.172    | 0.100    |
| CsCaH3                    | 0.188    | 0.100    |
| Na(Li0.5Al0.5)H3          | 0.139    | 0.06475  |
| β-Na(Na0.5Al0.5)H3        | 0.139    | 0.07775  |
| K(Li0.5Al0.5)H3           | 0.164    | 0.06475  |
| K(Na0.5Al0.5)H3           | 0.164    | 0.07775  |
| CaCoH3                    | 0.134    | 0.0745   |
| CaNiH3                    | 0.134    | 0.069    |
| EuPdH3                    | 0.128    | 0.086    |

These radii are taken from the standard Shannon effective ionic radii and are consistent with the values used in the literature analysis of perovskite hydride formation ability. Use these values directly; no further database look-up is needed.

## Reproduction target
For each hydride listed above, use the provided R_A and R_B to compute t = (R_A + 0.140) / (√2 × (R_B + 0.140)). Determine whether each hydride's (R_A, R_B) pair falls inside the quadrilateral region defined by 0.90 ≤ t ≤ 1.10 and 0.058 ≤ R_B ≤ 0.102 nm. Output a CSV file (tolerance_factor_results.csv) with columns: hydride_name, R_A_nm (in nm), R_B_nm (in nm), tolerance_factor_t, inside_quadrilateral (True/False).

## Workflow steps

### Step 1: Tolerance Factor Calculation and Quadrilateral Check
- Role: scored
- Action: For each hydride listed in the Input section, take the corresponding R_A and R_B from the provided table. Compute the Goldschmidt tolerance factor t = (R_A + 0.140) / (√2 × (R_B + 0.140)). Determine whether the (R_A, R_B) pair falls inside the quadrilateral formation region (0.90 ≤ t ≤ 1.10 and 0.058 ≤ R_B ≤ 0.102). Write results to a CSV file named tolerance_factor_results.csv.
- Output file: `/app/outputs/tolerance_factor_results.csv`
- Format: csv
- Contract: CSV with header: hydride_name(str), R_A_nm(float,nm), R_B_nm(float,nm), tolerance_factor_t(float), inside_quadrilateral(bool)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tolerance_factor_results.csv`

## Output contract
Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tolerance_factor_results.csv
- path: `/app/outputs/tolerance_factor_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Goldschmidt tolerance factors and quadrilateral membership for each stoichiometric perovskite-type hydride.
- schema:
  - `type`: table
  - `required_columns`: `hydride_name`, `R_A_nm`, `R_B_nm`, `tolerance_factor_t`, `inside_quadrilateral`
  - `units`:
    - `R_A_nm`: nm
    - `R_B_nm`: nm

Notes: The CSV must contain exactly the 16 hydrides listed in the Input table. Non-stoichiometric hydrides are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tolerance_factor_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "hydride_name",
          "R_A_nm",
          "R_B_nm",
          "tolerance_factor_t",
          "inside_quadrilateral"
        ],
        "units": {
          "R_A_nm": "nm",
          "R_B_nm": "nm"
        }
      },
      "description": "Computed Goldschmidt tolerance factors and quadrilateral membership for each stoichiometric perovskite-type hydride."
    }
  ],
  "notes": "The CSV must contain the 16 stoichiometric ABH3 hydrides listed in the task. Non-stoichiometric hydrides are not required."
}
```

## How you are scored
A hidden verifier will independently score the uploaded tolerance_factor_results.csv. The verifier will:
- Compare your reported R_A_nm and R_B_nm against the correct Shannon effective ionic radii (the same values as provided in this instruction). Any significant deviation will reduce the score.
- Recompute t from your submitted (R_A, R_B) and check that it matches your reported tolerance_factor_t within a small tolerance.
- Verify that the inside_quadrilateral flag is consistent with the definition (0.90 ≤ t ≤ 1.10 and 0.058 ≤ R_B ≤ 0.102).
The total reward is a weighted combination of these checks.