# Resolved Breakaway Shear Stress of Pinned Dislocations in Iron

## Problem background
The study investigates the breakaway of impurity-pinned dislocations in iron single crystals using amplitude-dependent internal friction measurements. When the applied oscillatory stress exceeds a critical level, dislocations unpin, causing a deviation in the internal friction versus strain amplitude curve. The critical resolved breakaway shear stress can be derived from the measured breakaway strain, the specimen's Young's modulus, and an orientation factor that accounts for the crystallographic geometry (slip system and crystal orientation). This task asks you to compute the resolved breakaway shear stress for five iron single crystal specimens from the provided input data.

## Approach
The resolved breakaway shear stress τ_r (in kg/mm²) is calculated in two steps: first, the breakaway stress σ_b = ε_b × E, where ε_b is the breakaway strain and E is Young's modulus (kg/mm²). Then, τ_r = σ_b / (cosθ sinθ cosη), where the orientation factor cosθ sinθ cosη is given for each specimen. The necessary input data for the five specimens (Nos. 1–4 and 6) are listed in the table below. You will use these values directly; no external data download is required.

| Specimen | Breakaway strain | Young's modulus (kg/mm²) | Orientation factor |
|----------|-------------------|---------------------------|---------------------|
| 1        | 1.6e-6            | 1.94e4                    | 0.498               |
| 2        | 2.0e-6            | 1.48e4                    | 0.474               |
| 3        | 2.0e-6            | 1.83e4                    | 0.498               |
| 4        | 2.0e-6            | 1.44e4                    | 0.476               |
| 6        | 5.0e-6            | 1.22e4                    | 0.463               |

## Reproduction target
From the input data provided above, compute the resolved breakaway shear stress (units: kg/mm²) for each of the five specimens and write the results to a CSV file at `/app/outputs/resolved_shear_stresses.csv`. The CSV must contain two columns: `specimen` (integer) and `resolved_shear_stress_kg_per_mm2` (float).

## Assets
No external resources are required. All necessary input data are provided inline in the Approach section.

## Workflow steps

### Step 1: Compute resolved breakaway shear stress
- Role: scored (load-bearing)
- Action: Using the provided breakaway strain, Young's modulus, and orientation factor for each of the five iron single crystal specimens, compute the resolved breakaway shear stress (kg/mm²) as (breakaway strain × Young's modulus) / orientation factor. Output the values in a CSV file.
- Output file: `/app/outputs/resolved_shear_stresses.csv`
- Format: csv
- Contract: specimen (int), resolved_shear_stress_kg_per_mm2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/resolved_shear_stresses.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### resolved_shear_stresses.csv
- path: `/app/outputs/resolved_shear_stresses.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Resolved breakaway shear stress for each of the five iron single crystal specimens.
- schema:
  - `type`: table
  - `required_columns`: `specimen`, `resolved_shear_stress_kg_per_mm2`
  - `units`:
    - `resolved_shear_stress_kg_per_mm2`: kg/mm^2

Notes: The input data (breakaway strain, Young's modulus, and orientation factor for specimens No. 1–4 and No. 6) are provided in the instruction. No external resources or downloads are required. The computation is a simple arithmetic operation on the given values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "resolved_shear_stresses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "specimen",
          "resolved_shear_stress_kg_per_mm2"
        ],
        "units": {
          "resolved_shear_stress_kg_per_mm2": "kg/mm^2"
        }
      },
      "description": "Resolved breakaway shear stress for each of the five iron single crystal specimens."
    }
  ],
  "notes": "The input data (breakaway strain, Young's modulus, and orientation factor for specimens No. 1–4 and No. 6) are provided in the instruction. No external resources or downloads are required. The computation is a simple arithmetic operation on the given values."
}
```

## How you are scored
A hidden verifier will evaluate your submitted CSV file. It recomputes the resolved breakaway shear stress for each specimen from the input data and compares your values to the recomputed values with a specified absolute tolerance. It may also check structural properties: the stress values for specimens 1–4 should be mutually consistent (indicating orientation independence), and the value for specimen 6 should be higher than those for specimens 1–4. Your final score is the weighted result of these checks; a score of 1.0 requires all checks to pass. Simply reporting numbers without computation will not satisfy the verifier.
