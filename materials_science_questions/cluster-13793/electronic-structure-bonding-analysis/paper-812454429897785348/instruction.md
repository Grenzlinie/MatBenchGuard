# Compute Mulliken Overlap Populations for Metal Sites in a Mixed Metal Phosphide via Extended Hückel Tight-Binding

## Problem background
The ternary phosphide Hf₅.₀₈Mo₀.₉₂P₃ crystallizes in a new structure type with six distinct metal sites, each having a different coordination environment of surrounding metal and phosphorus atoms. In the real compound, Mo atoms occupy only the M5 and M6 sites, while the other four sites are fully occupied by Hf. Understanding what drives this site preference requires quantifying the metal–metal and metal–phosphorus bonding strengths at every metal site. Extended Hückel tight-binding calculations provide a tool to compute Mulliken Overlap Populations (MOP) – a quantitative scale for bond strength – allowing the evaluation of relative bonding contributions across the six sites.

## Approach
Implement an extended Hückel tight-binding band structure calculation for a hypothetical "M₂P" compound that adopts the crystal structure of Hf₅.₀₈Mo₀.₉₂P₃ but has Hf atoms placed at all six metal sites. Using the provided lattice parameters, space group, fractional coordinates, and atomic parameters for Hf and P, construct the Hamiltonian and perform a band structure calculation over a suitable k‑point mesh. Carry out Mulliken population analysis on the resulting wavefunctions to obtain overlap populations for each metal site. Partition each site's total overlap population into its metal–metal (M–M) and metal–phosphorus (M–P) contributions.

## Reproduction target
Compute the total Mulliken overlap population (total_MOP), the metal–metal component (M_M_MOP), and the metal–phosphorus component (M_P_MOP) for each of the six metal sites M1, M2, M3, M4, M5, M6. Write the results to the file /app/outputs/mop_values.csv, with columns site, total_MOP, M_M_MOP, and M_P_MOP (one row per site, no index column).

## Assets

- Extended Hückel tight-binding calculator (YAeHMOP or equivalent open-source implementation): https://github.com/greglandrum/yaehmop

## Workflow steps

### Step 1: Construct crystal structure and prepare extended Hückel input
- Role: process
- Action: Construct the crystal structure of the hypothetical M₂P compound (Hf₅.₀₈Mo₀.₉₂P₃ structure type with all metal sites occupied by Hf) in space group Pnma (No. 62) using the provided lattice parameters and fractional coordinates. Set up the extended Hückel Hamiltonian using the specified atomic parameters for Hf and P. Prepare the full unit cell and a k-point mesh for Brillouin zone integration.
- Evidence: none

### Step 2: Compute Mulliken Overlap Populations
- Role: scored (load-bearing)
- Action: Perform the extended Hückel tight-binding band structure calculation on the constructed M₂P crystal structure. Compute Mulliken Overlap Populations from the resulting wavefunctions using population analysis. For each of the six metal sites M1–M6, partition the total overlap population into metal–metal (M–M) and metal–phosphorus (M–P) contributions and compute total_MOP, M_M_MOP, M_P_MOP. Write the results as a CSV file.
- Output file: `/app/outputs/mop_values.csv`
- Format: csv
- Contract: CSV with header row and exactly 6 data rows. Columns: site (string, values M1, M2, M3, M4, M5, M6), total_MOP (float), M_M_MOP (float), M_P_MOP (float). No index column.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mop_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mop_values.csv
- path: `/app/outputs/mop_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mulliken Overlap Populations per metal site for the hypothetical M2P structure. The checker compares each site's MOP values to reference values within a tolerance, and verifies that the total MOP ordering across sites is correct (checked against a hidden reference).
- schema:
  - `type`: table
  - `required_columns`: `site`, `total_MOP`, `M_M_MOP`, `M_P_MOP`

Notes: The scored output includes the total, M–M, and M–P MOPs for the six metal sites. The target policy is reference_match for numerical values; the ordering check is performed as a secondary structural audit within the grading tier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mop_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "total_MOP",
          "M_M_MOP",
          "M_P_MOP"
        ]
      },
      "description": "Mulliken Overlap Populations per metal site for the hypothetical M2P structure. The checker compares each site's MOP values to reference values within a tolerance, and verifies that the total MOP ordering across sites is correct (checked against a hidden reference)."
    }
  ],
  "notes": "The scored output includes the total, M–M, and M–P MOPs for the six metal sites. The target policy is reference_match for numerical values; the ordering check is performed as a secondary structural audit within the grading tier."
}
```

## How you are scored
A hidden verifier will read your mop_values.csv and compare the per-site total_MOP, M_M_MOP, and M_P_MOP values to reference values. The verifier will also check that the total MOP values across the six sites follow the expected ordering. The numerical comparison carries the primary reward weight; the ordering check carries a secondary weight. The verifier uses tolerances appropriate for the extended Hückel method. Your final reward is a weighted combination of these checks. Simply reporting a number without performing the calculation will not pass; the verifier independently scores your submitted artifact against its own hidden reference.
