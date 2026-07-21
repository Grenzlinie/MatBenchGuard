# Piezoelectric damage from microvoids via unit-cell FEM

## Problem background
Piezoelectric ceramics are widely used in sensors and actuators, but the presence of inherent microvoids degrades their mechanical and electrical performance. Continuum damage mechanics models require quantitative relationships between microvoid morphology (volume fraction and aspect ratio) and the anisotropic damage tensors that describe property degradation. This task focuses on computing these relationships for the piezoelectric ceramic PZT-7A. Using finite-element unit-cell simulations, you will determine the mechanical damage components D11^M and D33^M (damage in the isotropic plane and along the poling direction, respectively) and the electrical damage components D11^E and D33^E as functions of void volume fraction and void aspect ratio. Additionally, you will extract the effective piezoelectric coefficients e31, e33, e15 to examine the validity of the transversely isotropic damage hypothesis. The target challenge is to produce the damage-vs-parameters curves and piezoelectric coefficient curves through a parametric computational study.

## Approach
You will model a periodic array of insulating microvoids in PZT-7A by a quarter-symmetric three-dimensional unit cell. An open-source multiphysics finite-element solver (e.g., Elmer) with 8‑node piezoelectric brick elements is used. For each unit‑cell geometry (defined by volume fraction f and aspect ratio S), you apply a series of load cases:
- Prescribed displacements on one face to extract effective elastic constants c₁₁ and c₃₃.
- Applied voltage differences between opposite faces to extract dielectric constants λ₁₁ and λ₃₃.
- Electric fields with constrained strains to extract piezoelectric coefficients e₃₁, e₃₃, e₁₅.
From the reaction forces, electric flux densities, and applied voltages/displacements, compute the effective constants via averaging relations analogous to those derived from the unit-cell method. Then, using the known undamaged bulk constants of PZT-7A (provided below), compute mechanical damage components D₁₁^M = 1 – c₁₁^eff / c₁₁^bulk, D₃₃^M = 1 – c₃₃^eff / c₃₃^bulk, and electrical damage components D₁₁^E = 1 – λ₁₁^eff / λ₁₁^bulk, D₃₃^E = 1 – λ₃₃^eff / λ₃₃^bulk.

Undamaged PZT-7A bulk constants (transversely isotropic, poling axis x₃):

| Property        | Value      |
|-----------------|------------|
| c₁₁ (GPa)      | 148.0      |
| c₁₂ (GPa)      | 76.2       |
| c₁₃ (GPa)      | 74.2       |
| c₃₃ (GPa)      | 131.0      |
| c₄₄ (GPa)      | 25.3       |
| c₆₆ (GPa)      | 35.9       |
| e₃₁ (C/m²)     | −2.1       |
| e₃₃ (C/m²)     | 9.5        |
| e₁₅ (C/m²)     | 9.2        |
| λ₁₁ (10⁻⁹ F/m) | 4.07       |
| λ₃₃ (10⁻⁹ F/m) | 2.08       |

Perform two parametric sweeps:
1. Spherical voids (S=1.0) with volume fraction f = [0.001, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.321].
2. Fixed volume fraction f=0.0654 with void aspect ratio S = [0.3, 0.5, 0.8, 1.0, 1.5, 2.0].
Save the raw effective constants and extracted piezoelectric coefficients for each case in an intermediate file (effective_constants.json) before computing the damage components.

## Reproduction target
From the finite-element parametric sweeps described above, produce two CSV files under `/app/outputs`:

1. `damage_vs_parameters.csv` – contains one row per (f, S) combination with columns: f (volume fraction), S (aspect ratio), D11_M, D33_M, D11_E, D33_E.
2. `piezo_coefficients.csv` – contains one row per (f, S) combination with columns: f, S, e31, e33, e15.

For the spherical‑void sweep (S=1.0), use the ten volume fractions: 0.001, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.321. For the aspect‑ratio sweep (f=0.0654), use the six aspect ratios: 0.3, 0.5, 0.8, 1.0, 1.5, 2.0. The resulting CSVs should capture the variation of damage and piezoelectric coefficients over these parameter ranges.

## Assets

- Open-source finite-element multiphysics solver (e.g., Elmer FEM): https://www.csc.fi/web/elmer
- PZT-7A material properties

## Workflow steps

### Step 1: Run finite-element simulations for parametric sweep of void parameters
- Role: process
- Action: Set up quarter-symmetric 3-D unit-cell models of voided PZT-7A with varying void volume fraction f (spherical voids, S=1) and varying void aspect ratio S (fixed f=6.54%) using an open-source piezoelectric solver. For each geometry, apply the required load cases to extract effective elastic constants (c11, c33), dielectric constants (λ11, λ33), and piezoelectric coefficients (e31, e33, e15) via the averaging formulas derived from the paper’s extraction method. Save the raw effective constants and piezoelectric coefficients for each (f,S) in an intermediate structured JSON file for use in later steps.
- Evidence: `/app/outputs/effective_constants.json`

### Step 2: Compute mechanical and electrical damage components and export CSV
- Role: scored (load-bearing)
- Action: From the effective elastic and dielectric constants obtained in the previous step, compute the mechanical and electrical damage components using the undamaged PZT-7A constants. Specifically, compute D11_M = 1 - c11_eff/c11_undamaged, D33_M = 1 - c33_eff/c33_undamaged, D11_E = 1 - λ11_eff/λ11_undamaged, D33_E = 1 - λ33_eff/λ33_undamaged. Write a CSV file containing a row for each (f,S) case with columns: f, S, D11_M, D33_M, D11_E, D33_E.
- Output file: `/app/outputs/damage_vs_parameters.csv`
- Format: csv
- Contract: CSV with header: f, S, D11_M, D33_M, D11_E, D33_E. All columns are floating-point numbers. f is volume fraction (0 < f ≤ 0.321), S is aspect ratio (>0).
- Scoring: scored by hidden verifier

### Step 3: Export effective piezoelectric coefficients to CSV
- Role: scored
- Action: From the same finite-element runs, retrieve the directly extracted effective piezoelectric coefficients e31, e33, e15 for each (f,S) case. Write a CSV file with columns: f, S, e31, e33, e15.
- Output file: `/app/outputs/piezo_coefficients.csv`
- Format: csv
- Contract: CSV with header: f, S, e31, e33, e15. All columns are floating-point numbers. e31, e33, e15 are in C/m².
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/damage_vs_parameters.csv`
- `/app/outputs/piezo_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### damage_vs_parameters.csv
- path: `/app/outputs/damage_vs_parameters.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Mechanical and electrical damage components as functions of void volume fraction f and aspect ratio S. Each row corresponds to one simulation case. For spherical void scan, S=1.0; for aspect ratio scan, f=0.0654.
- schema:
  - `type`: table
  - `required_columns`: `f`, `S`, `D11_M`, `D33_M`, `D11_E`, `D33_E`
  - `units`:
    - `f`: 1 (volume fraction)
    - `S`: 1 (aspect ratio)
    - `D11_M`: 1 (damage)
    - `D33_M`: 1 (damage)
    - `D11_E`: 1 (damage)
    - `D33_E`: 1 (damage)

### piezo_coefficients.csv
- path: `/app/outputs/piezo_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Directly extracted effective piezoelectric coefficients e31, e33, e15 for the same (f,S) parameter grid as the damage CSV. Used to verify transversely isotropic damage hypothesis and trends.
- schema:
  - `type`: table
  - `required_columns`: `f`, `S`, `e31`, `e33`, `e15`
  - `units`:
    - `f`: 1 (volume fraction)
    - `S`: 1 (aspect ratio)
    - `e31`: C/m²
    - `e33`: C/m²
    - `e15`: C/m²

Notes: Verification is structural (T3): monotonicity of D11_M, D33_M with f; decrease of D33_M with increasing S; near-constancy of D11_E, D33_E with S; decreasing trends in e31, e33, e15 with f. Additional loose tolerance (±30%) against digitized reference curves ensures approximate quantitative agreement.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "damage_vs_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "S",
          "D11_M",
          "D33_M",
          "D11_E",
          "D33_E"
        ],
        "units": {
          "f": "1 (volume fraction)",
          "S": "1 (aspect ratio)",
          "D11_M": "1 (damage)",
          "D33_M": "1 (damage)",
          "D11_E": "1 (damage)",
          "D33_E": "1 (damage)"
        }
      },
      "description": "Mechanical and electrical damage components as functions of void volume fraction f and aspect ratio S. Each row corresponds to one simulation case. For spherical void scan, S=1.0; for aspect ratio scan, f=0.0654."
    },
    {
      "file": "piezo_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "S",
          "e31",
          "e33",
          "e15"
        ],
        "units": {
          "f": "1 (volume fraction)",
          "S": "1 (aspect ratio)",
          "e31": "C/m²",
          "e33": "C/m²",
          "e15": "C/m²"
        }
      },
      "description": "Directly extracted effective piezoelectric coefficients e31, e33, e15 for the same (f,S) parameter grid as the damage CSV. Used to verify transversely isotropic damage hypothesis and trends."
    }
  ],
  "notes": "Verification is structural (T3): monotonicity of D11_M, D33_M with f; decrease of D33_M with increasing S; near-constancy of D11_E, D33_E with S; decreasing trends in e31, e33, e15 with f. Additional loose tolerance (±30%) against digitized reference curves ensures approximate quantitative agreement."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that checks both the structure and the physical consistency of the output CSV files. The verifier will:
- Confirm the files exist and contain the required columns.
- Verify monotonic trends: D11_M and D33_M must increase with volume fraction f for spherical voids; for varying aspect ratio S, D33_M must decrease while D11_M increases slowly; D11_E and D33_E must be approximately constant with S.
- Check that the effective piezoelectric coefficients follow reasonable decreasing trends with f and exhibit consistent behavior with respect to S.
- Compare the numerical values to expected reference curves within a generous tolerance to accommodate differences in solver implementation and mesh density.
A weighted score combining trend compliance and numerical agreement will be assigned. The emphasis is on correct physical trends and approximate quantitative agreement; no single exact value is required.
