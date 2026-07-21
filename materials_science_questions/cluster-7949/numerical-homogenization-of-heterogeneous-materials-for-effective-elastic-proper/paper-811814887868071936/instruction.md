# Effective Thermoelastic Properties of Staggered Composites via Analytical Homogenization

## Problem background
Staggered composites, inspired by biological materials such as nacre, consist of parallel stiff platelets embedded in a softer matrix. Their effective coefficient of thermal expansion (CTE) and thermal mismatch stress are determined by the geometry and material contrast of the two phases. A continuum-mechanics homogenization model provides closed-form predictions for these quantities, which can be implemented and benchmarked. In this task, you will re-implement that analytical model to compute normalized CTEs and thermal mismatch stresses as functions of the platelet aspect ratio, using specified material constants.

## Approach
The analytical model proceeds in two stages. First, compute the baseline thermoelastic response of a sandwich composite (hard and soft layers in a simple laminate) under a temperature change ΔT by solving the coupled constitutive, equilibrium, and kinematic equations. This yields reference CTEs and phase stresses (tilde quantities). Second, extend the sandwich model to a staggered geometry: the hard platelets are separated by a longitudinal gap of length d. The kinematics in the loading direction are modified to account for gap elongation Δd, which introduces additional degrees of freedom. The system is closed by minimizing the total elastic energy, which includes normal strain energy in both phases and shear strain energy in the soft matrix, with an energy modification factor γ. Solving the energy minimization yields an expression for Δd, from which the effective CTEs (α_x, α_y) and the average thermal mismatch stresses in the hard and soft phases (σ_x^H, σ_y^H, σ_x^S, σ_y^S) are obtained. The sandwich baseline values serve as the starting point for the staggered calculations.

## Reproduction target
Produce a CSV file `staggered_thermal_results.csv` with the following columns: `aspect_ratio` (values 3.0, 10.0, 20.0, 35.0), `normalized_alpha_x`, `normalized_alpha_y`, `normalized_sigma_x_H`, `normalized_sigma_y_H`. All CTE quantities are normalized by the volume-averaged CTE c_H α_H + (1−c_H) α_S, and all stress quantities are normalized by (α_S−α_H) ΔT E_S. The required material constants are: E_H/E_S=100, ν_H=0.2, ν_S=0.3, α_S/α_H=10, h_S/h_H=1, d/h_H=1. Use a dimensionless temperature change (e.g., ΔT=1) for the calculations. The goal is to correctly compute these normalized properties at each aspect ratio using the analytical model.

## Assets

- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Sandwich composite baseline
- Role: process
- Action: Using the given material constants (E_H/E_S=100, ν_H=0.2, ν_S=0.3, α_S/α_H=10, h_S/h_H=1) and a dimensionless temperature change (e.g., ΔT=1), compute the effective CTE and stresses of a sandwich composite from the analytical model. These 'tilde' quantities serve as the reference baseline for the staggered composite model. Record the sandwich in-plane CTE (α_x) as a reference.
- Evidence: `/app/outputs/sandwich_baseline.json`

### Step 2: Staggered composite CTE and stress
- Role: scored (load-bearing)
- Action: For aspect ratios l/h_H = 3, 10, 20, 35 and d/h_H = 1, use the sandwich baseline and the full staggered analytical model to compute the effective longitudinal CTE (α_x), transverse CTE (α_y), and average thermal mismatch stresses in the hard phase (σ_x^H, σ_y^H). Normalize the CTE by the volume-averaged CTE c_H α_H + (1-c_H) α_S, and stresses by (α_S-α_H)ΔT E_S. Write the results to a CSV.
- Output file: `/app/outputs/staggered_thermal_results.csv`
- Format: csv
- Contract: columns: aspect_ratio (float, values [3.0,10.0,20.0,35.0]), normalized_alpha_x (float), normalized_alpha_y (float), normalized_sigma_x_H (float), normalized_sigma_y_H (float). All normalized values are dimensionless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/staggered_thermal_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### staggered_thermal_results.csv
- path: `/app/outputs/staggered_thermal_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermoelastic properties of staggered composites at four aspect ratios, normalized as specified.
- schema:
  - `type`: table
  - `required_columns`: `aspect_ratio`, `normalized_alpha_x`, `normalized_alpha_y`, `normalized_sigma_x_H`, `normalized_sigma_y_H`
  - `units`:
    - `aspect_ratio`: dimensionless
    - `normalized_alpha_x`: dimensionless
    - `normalized_alpha_y`: dimensionless
    - `normalized_sigma_x_H`: dimensionless
    - `normalized_sigma_y_H`: dimensionless

Notes: The hidden checker independently implements the same analytical model to compute reference values and compares row-wise with a relative tolerance. No FEM simulations or parameter studies beyond these four aspect ratios are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "staggered_thermal_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "aspect_ratio",
          "normalized_alpha_x",
          "normalized_alpha_y",
          "normalized_sigma_x_H",
          "normalized_sigma_y_H"
        ],
        "units": {
          "aspect_ratio": "dimensionless",
          "normalized_alpha_x": "dimensionless",
          "normalized_alpha_y": "dimensionless",
          "normalized_sigma_x_H": "dimensionless",
          "normalized_sigma_y_H": "dimensionless"
        }
      },
      "description": "Thermoelastic properties of staggered composites at four aspect ratios, normalized as specified."
    }
  ],
  "notes": "The hidden checker independently implements the same analytical model to compute reference values and compares row-wise with a relative tolerance. No FEM simulations or parameter studies beyond these four aspect ratios are required."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently implements the same analytical model with the same inputs to compute reference values for each aspect ratio. Your output CSV is compared row-wise against these references using a tight relative tolerance on each normalized quantity. The overall reward is 1.0 if all comparisons pass; otherwise, credit is proportional to the number of passing rows. The scoring ensures that only a correct implementation that properly chains the sandwich baseline and staggered model can achieve full credit.
