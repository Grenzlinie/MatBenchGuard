# Perovskite Hydride Formation Ability via Goldschmidt Tolerance Factor

## Problem background
Perovskite-type hydrides (ABH₃) are promising hydrogen storage materials with high volumetric hydrogen density. The geometric stability of the perovskite structure is often assessed by the Goldschmidt tolerance factor t = (R_A + R_X) / (√2 (R_B + R_X)), which depends on the ionic radii of the A and B cations and the anion X. For hydrides, the anion is H⁻ with a commonly adopted radius of 0.140 nm. A synthesis screening could be guided by whether a candidate (R_A, R_B) pair falls within a predicted formation region — a quadrilateral in (R_A, R_B) space bounded by two t-isolines and octahedral stability limits on R_B. The task is to compute t for a set of reported stoichiometric perovskite hydrides using public Shannon effective ionic radii and to determine, for each hydride, whether its ionic radii place it inside that quadrilateral region.

## Approach
The analysis uses the Goldschmidt tolerance factor t = (R_A + R_H) / (√2 (R_B + R_H)) with R_H = 0.140 nm. For each A and B cation, retrieve the Shannon effective ionic radius appropriate for the perovskite coordination: 12-fold cubo-octahedral for the A site and 6-fold octahedral for the B site. When a site is occupied by a mixture of cations (e.g., (Li₀.₅Al₀.₅)), compute a weighted-average radius based on the stoichiometric fractions. The quadrilateral formation region is defined by: 0.90 ≤ t ≤ 1.10 and 0.058 nm ≤ R_B ≤ 0.102 nm (the latter derived from Pauling's octahedral stability criterion 0.414 < R_B/R_H < 0.732). The computational workflow simply collects the radii, computes t and checks membership, and outputs the results for 16 stoichiometric ABH₃ hydrides.

## Reproduction target
For each of the following stoichiometric perovskite-type hydrides — SrLiH₃, BaLiH₃, EuLiH₃, NaMgH₃, KMgH₃, RbMgH₃, HT-CsMgH₃, RbCaH₃, CsCaH₃, Na(Li₀.₅Al₀.₅)H₃, β-Na(Na₀.₅Al₀.₅)H₃, K(Li₀.₅Al₀.₅)H₃, K(Na₀.₅Al₀.₅)H₃, CaCoH₃, CaNiH₃, EuPdH₃ — retrieve the appropriate Shannon effective ionic radii and compute t. Determine whether each hydride's (R_A, R_B) pair falls inside the quadrilateral region described above. Output a CSV file (tolerance_factor_results.csv) with columns: hydride_name, R_A_nm (in nm), R_B_nm (in nm), tolerance_factor_t, inside_quadrilateral (True/False). Additionally, from the computed results, report the minimum and maximum tolerance factor observed among these stoichiometric hydrides and the number of hydrides for which inside_quadrilateral is True.

## Assets

- Shannon Effective Ionic Radii database: 10.1107/S0567739476001551

## Workflow steps

### Step 1: Tolerance Factor Calculation and Quadrilateral Check
- Role: scored
- Action: Retrieve Shannon effective ionic radii for the A-site (12-coordinated) and B-site (6-coordinated) cations of each stoichiometric perovskite-type hydride listed in the task description. For mixed-occupancy sites, compute a weighted-average radius. Compute the Goldschmidt tolerance factor t = (R_A + 0.140) / (√2 × (R_B + 0.140)). Determine whether the (R_A, R_B) pair falls inside the quadrilateral formation region defined by 0.90 ≤ t ≤ 1.10 and 0.058 ≤ R_B ≤ 0.102 nm. Write results to a CSV file named tolerance_factor_results.csv.
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

Notes: The CSV must contain the 16 stoichiometric ABH3 hydrides listed in the task. Non-stoichiometric hydrides are not required.

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
A hidden verifier will independently score the uploaded tolerance_factor_results.csv. The verifier will read the CSV, recompute each tolerance factor from the agent-supplied R_A_nm and R_B_nm and check that it matches the reported tolerance_factor_t within a small tolerance. It will verify that the inside_quadrilateral flag is consistent with the computed t and the R_B_nm bounds. It will also compare your R_A_nm and R_B_nm values against a hidden reference table of Shannon radii to ensure the correct ionic radii were used. Finally, it will check that your reported minimum and maximum t and the count of inside_quadrilateral hydrides are correct. The total reward is a weighted combination of these checks.
