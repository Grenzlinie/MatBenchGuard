# Phase Diagram Calculation for a Two-Temperature Colloidal Mixture

## Problem background
Mixtures of colloidal particles maintained at different temperatures can phase separate even when the only interactions are purely repulsive (excluded volume). Thermodynamic theories derived in the dilute limit predict effective Flory‑Huggins‑like free energies that capture this behaviour. The goal of this task is to compute the phase diagram – the spinodal stability limit, the binodal coexistence curve, and the critical point – for a well‑defined parameter set, thereby demonstrating the predictions of the theory.

## Approach
We work within an effective equilibrium thermodynamics derived for two species (A, B) immersed in different heat baths. In the dilute, second‑virial approximation the dimensionless free energy and the corresponding chemical potentials (μ_A, μ_B) and pressure (p) are functions of the volume fractions φ_A and φ_B. The spinodal line is obtained by solving the stability limit: the determinant of the inverse compressibility matrix must be zero. The critical point is the point on the spinodal where the two coexisting phases become identical, which additionally requires the gradient of the spinodal condition to align with the eigenvector associated with the vanishing eigenvalue. The binodal (coexistence) curve then follows from numerically solving the three equilibrium conditions – equal μ_A, equal μ_B, and equal p – between two distinct phases. We restrict the computation to the low‑density approximation as in the original derivation.

## Reproduction target
Compute the spinodal line, the critical point, and the binodal coexistence curve for a mixture of equal‑sized hard spheres (volume ratio = 1, friction ratio = 1) with a temperature ratio T_A / T_B = 20. The dimensionless virial coefficients are ε_A = 8, ε_B = 8, and the cross‑species coefficient β_B = 8. Report at least 20 points on each curve: (φ_A, φ_B) for the spinodal in spinodal.csv; the critical composition (φ_A*, φ_B*) and the solvent fraction φ_s* in critical_point.json; and for the binodal, pairs of coexisting phases with six columns (φ_A, φ_B, φ_s for each phase) in binodal.csv.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement thermodynamic model
- Role: process
- Action: Implement the dimensionless effective free energy, chemical potentials (μ_A, μ_B), pressure (p), and the spinodal condition (determinant of the inverse compressibility matrix) for a two-species hard-sphere mixture with the given parameter set: temperature ratio α_T = 20, volume ratio α_v = 1, friction ratio α_ζ = 1, dimensionless virial coefficients ε_A = 8, ε_B = 8, and cross-species β_B = 8. Provide callable functions that will be used in subsequent computations.
- Evidence: none

### Step 2: Compute spinodal line
- Role: scored
- Action: Numerically solve the spinodal condition (stability limit) for the mixture, defined by the determinant of the inverse compressibility matrix equal to zero, over the physically allowed composition triangle φ_A + φ_B ≤ 1. Sample at least 20 points on the spinodal curve. Output the (φ_A, φ_B) points.
- Output file: `/app/outputs/spinodal.csv`
- Format: csv
- Contract: CSV with header: phi_A, phi_B. Each row is a point on the spinodal curve.
- Scoring: scored by hidden verifier

### Step 3: Determine critical point
- Role: scored
- Action: Find the critical composition (φ_A*, φ_B*) that satisfies both the spinodal condition and the condition that the gradient of the spinodal condition is aligned with the eigenvector of the inverse compressibility matrix corresponding to the vanishing eigenvalue. Write the critical point to critical_point.json.
- Output file: `/app/outputs/critical_point.json`
- Format: json
- Contract: JSON object with keys: phi_A_star, phi_B_star, phi_s_star (solvent volume fraction).
- Scoring: scored by hidden verifier

### Step 4: Compute binodal coexistence curve
- Role: scored (load-bearing)
- Action: Numerically solve the three phase-equilibrium conditions (equality of chemical potentials μ_A, μ_B and pressure p between two coexisting phases) to obtain the binodal line. Use the critical point as a starting point. Output at least 20 coexisting pairs (φ_A, φ_B, φ_s) for each phase. Write the results to binodal.csv.
- Output file: `/app/outputs/binodal.csv`
- Format: csv
- Contract: CSV with six columns: phi_A_a, phi_B_a, phi_s_a, phi_A_b, phi_B_b, phi_s_b. Each row is a coexisting pair; phi_A_a is volume fraction of species A in phase a, etc.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spinodal.csv`
- `/app/outputs/critical_point.json`
- `/app/outputs/binodal.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spinodal.csv
- path: `/app/outputs/spinodal.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Points on the spinodal curve. The verifying checker will recompute the spinodal condition at each point and check that it meets a threshold (i.e., the condition is satisfied within tolerance).
- schema:
  - `type`: table
  - `required_columns`: `phi_A`, `phi_B`

### critical_point.json
- path: `/app/outputs/critical_point.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Critical point composition. The checker will recompute the spinodal condition and the gradient-alignment equation to verify correctness.
- schema:
  - `type`: object
  - `required`:
    - `phi_A_star`: number
    - `phi_B_star`: number
    - `phi_s_star`: number

### binodal.csv
- path: `/app/outputs/binodal.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Coexisting phase compositions on the binodal line. The checker will recompute the chemical potentials and pressure for each pair and verify that the equilibrium conditions hold within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `phi_A_a`, `phi_B_a`, `phi_s_a`, `phi_A_b`, `phi_B_b`, `phi_s_b`

Notes: All calculations assume low densities (second virial approximation) as in the original derivation. The demixing boundary mapping (Fig. 3a/b of the paper) — which requires an additional parameter scan over (α_T, α_v) space solving the spinodal condition for each grid point — is excluded from this minimal reproduction task per the original approved scope; the task focuses on the spinodal, binodal, and critical point for the specified parameter set (T_A/T_B=20, equal sizes).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spinodal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_A",
          "phi_B"
        ]
      },
      "description": "Points on the spinodal curve. The verifying checker will recompute the spinodal condition at each point and check that it meets a threshold (i.e., the condition is satisfied within tolerance)."
    },
    {
      "file": "critical_point.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "phi_A_star": "number",
          "phi_B_star": "number",
          "phi_s_star": "number"
        }
      },
      "description": "Critical point composition. The checker will recompute the spinodal condition and the gradient-alignment equation to verify correctness."
    },
    {
      "file": "binodal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_A_a",
          "phi_B_a",
          "phi_s_a",
          "phi_A_b",
          "phi_B_b",
          "phi_s_b"
        ]
      },
      "description": "Coexisting phase compositions on the binodal line. The checker will recompute the chemical potentials and pressure for each pair and verify that the equilibrium conditions hold within tolerance."
    }
  ],
  "notes": "All calculations assume low densities (second virial approximation) as in the original derivation. The demixing boundary mapping (Fig. 3a/b of the paper) — which requires an additional parameter scan over (α_T, α_v) space solving the spinodal condition for each grid point — is excluded from this minimal reproduction task per the original approved scope; the task focuses on the spinodal, binodal, and critical point for the specified parameter set (T_A/T_B=20, equal sizes)."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage and combine the stage scores into a single final reward. For the spinodal, the verifier recomputes the spinodal condition at your submitted points and checks that it meets the required threshold. For the critical point, your composition is compared to a hidden reference derived from the same equations. For the binodal, the verifier recomputes the chemical potentials and pressure for each submitted coexisting pair and verifies that they are equal within tolerance. Simply claiming the paper’s numbers is not enough – every score is derived from re‑evaluation of your raw output.
