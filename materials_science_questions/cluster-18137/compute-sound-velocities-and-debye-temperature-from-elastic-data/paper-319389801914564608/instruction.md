# Compute Invariant-Based Shear Modulus from Single-Crystal Elastic Constants

## Problem background
The polycrystalline average of a single-crystal physical property depends on the averaging method used. For elastic constants of cubic crystals, traditional methods (e.g., Voigt and Reuss) yield different results depending on whether the direct stiffness tensor or its inverse compliance tensor is averaged, and the discrepancy grows with increasing anisotropy. This task reproduces a method that computes a self-consistent polycrystalline shear modulus directly from the highest invariant of the fourth-rank stiffness tensor, avoiding numerical orientation integration. For cubic symmetry, the method gives a closed-form expression for the isotropic shear modulus in terms of the single-crystal elastic constants.

## Approach
For a cubic crystal, the single-crystal elastic constants are c11, c12, c44 (in units of 10^11 dyn/cm²). The bulk modulus has the well-known form K = (c11 + 2c12)/3. The anisotropy factor is defined as a = (c11 - c12) / (2 c44). Using the highest tensor invariant, the invariant-based polycrystalline shear modulus is G⁰ = c44 * a^(2/5). Compute these quantities for each crystal and write them to a CSV file.

## Reproduction target
Given the single-crystal elastic constants listed in the Assets section for the six cubic metals (Au, Ag, V, Nb, Ta, Pb), compute the bulk modulus K and the invariant-based shear modulus G0 for each metal. Write the results to '/app/outputs/computed_table.csv' with columns `crystal`, `G0` (units: 10^11 dyn/cm²), and `K` (units: 10^11 dyn/cm²). The computed values should be accurate to at least machine precision; no other artifacts are scored.

## Assets
The single-crystal elastic constants c11, c12, c44 (units: 10^11 dyn/cm²) for the six cubic crystals are:

| Crystal | c11   | c12   | c44   |
|---------|-------|-------|-------|
| Au      | 19.234| 16.314| 4.195 |
| Ag      | 12.399| 9.367 | 4.612 |
| V       | 22.8  | 11.9  | 4.26  |
| Nb      | 24.6  | 13.4  | 2.87  |
| Ta      | 26.7  | 16.1  | 8.25  |
| Pb      | 4.953 | 4.229 | 1.490 |

No other external assets are required.

## Workflow steps

### Step 1: Compute shear modulus G0 and bulk modulus K
- Role: scored (load-bearing)
- Action: For each of the six cubic crystals (Au, Ag, V, Nb, Ta, Pb), compute the anisotropy factor a = (c11 - c12) / (2 * c44), the bulk modulus K = (c11 + 2 * c12) / 3, and the invariant-based shear modulus G^0 = c44 * a^(2/5) using the single-crystal elastic constants (c11, c12, c44) provided in the instruction. Write a CSV file with columns 'crystal', 'G0', 'K' containing the computed values.
- Output file: `/app/outputs/computed_table.csv`
- Format: csv
- Contract: crystal (string), G0 (float, units: 10^11 dyn/cm^2), K (float, units: 10^11 dyn/cm^2), one row per crystal (Au, Ag, V, Nb, Ta, Pb).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_table.csv
- path: `/app/outputs/computed_table.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file with computed shear modulus G0 and bulk modulus K for six cubic crystals. The hidden checker recomputes G0 and K from the provided single-crystal elastic constants, compares the agent's values to paper-reported values, and performs structural consistency checks against Voigt, Reuss, and Hill averages.
- schema:
  - `type`: table
  - `required_columns`: `crystal`, `G0`, `K`
  - `units`:
    - `G0`: 10^11 dyn/cm^2
    - `K`: 10^11 dyn/cm^2

Notes: The single-crystal elastic constants are provided inline in the instruction. The agent must compute the required properties directly from those constants. No external dataset download is required. The task is purely arithmetic and requires only standard Python libraries.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "crystal",
          "G0",
          "K"
        ],
        "units": {
          "G0": "10^11 dyn/cm^2",
          "K": "10^11 dyn/cm^2"
        }
      },
      "description": "CSV file with computed shear modulus G0 and bulk modulus K for six cubic crystals. The hidden checker recomputes G0 and K from the provided single-crystal elastic constants, compares the agent's values to paper-reported values, and performs structural consistency checks against Voigt, Reuss, and Hill averages."
    }
  ],
  "notes": "The single-crystal elastic constants are provided inline in the instruction. The agent must compute the required properties directly from those constants. No external dataset download is required. The task is purely arithmetic and requires only standard Python libraries."
}
```

## How you are scored
After the workflow completes, a hidden verifier reads `/app/outputs/computed_table.csv`. It independently recomputes G0 and K from the same elastic constants. Your values must match the expected results within a relative tolerance (the exact tolerance is hidden). Additionally, the verifier will compute the Voigt shear modulus G_V = (c11 - c12 + 3c44)/5 and the Reuss shear modulus G_R = 5*c44*(c11 - c12) / (4*c44 + 3*(c11 - c12)) for each crystal and verify that your G0 equals (G_V + G_R)/2 within a tight tolerance, as a structural consistency check. Full credit requires all six crystals to satisfy both the value-matching and the consistency tests.
