# Stress Distribution Across a Crack in Graded Non-local Elastic Material

## Problem background
Classical elasticity predicts that stresses diverge to infinity at crack tips, which is physically unrealistic and prevents the direct use of a stress-based fracture criterion. Non-local elasticity theory incorporates a characteristic material length scale by averaging stresses over a finite neighbourhood, thereby yielding finite crack‑tip stresses. The present study investigates a mode‑I crack in an exponentially graded material (shear modulus μ₀e^{γx}) using a non‑local formulation with a Gaussian influence function. The goal is to compute the normalised normal stress distribution along the crack line and determine whether the non‑local model eliminates the singularity, producing a finite stress field that could support a maximum‑stress fracture criterion.

## Approach
The problem is formulated using two‑dimensional non‑local elasticity where the shear modulus varies exponentially along the crack direction. Fourier transforms are applied to the governing partial differential equations, leading to two pairs of dual integral equations for the jumps of the displacement components across the crack faces. These dual integral equations are solved by expanding the displacement jumps in series of Jacobi polynomials and applying the Schmidt orthogonalisation method, yielding the series coefficients. The non‑local stresses along the crack line are then obtained by numerically evaluating the Fourier inversion integrals that arise from the constitutive relations, using the previously computed coefficients. The entire solution procedure is implemented in Python with NumPy and SciPy, and the computed stress values are written to a CSV file for subsequent scoring.

## Reproduction target
For a mode‑I crack of half‑length l = 1.0 in an exponentially graded material with γl = 0.4 and non‑local parameter a/(βl) = 0.001, under uniform tension p₀ and plane‑strain conditions (Poisson’s ratio ν = 0.28), compute the normalised normal stress τ_yy / τ₀ (τ₀ = p₀) along the crack line y = 0. Produce a CSV file (stress_curve.csv) that contains the normalised stress at evenly spaced values of x/l covering the range [-2.0, 2.0] (at least 200 points). From this distribution, extract three key numbers: the stress at the crack tip (x/l = 1.0), and the location and value of the maximum normalised stress. The primary objective is to generate the complete stress curve from which these quantities can be obtained; the correctness of the extracted numbers will be judged by a hidden verifier.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve displacement jump coefficients
- Role: process
- Action: Implement the non-local elasticity formulation for the mode-I crack problem in an exponentially graded material. Transform the governing PDEs via Fourier transforms, derive the dual integral equations for displacement jumps across the crack faces, and solve them using the Schmidt method with Jacobi polynomial expansion for the given parameters: gamma*l=0.4, a/(beta*l)=0.001, l=1.0, Poisson's ratio nu=0.28, and uniform loading p0 (constant). Compute the series coefficients a_n and b_n up to a sufficient truncation order (e.g., first 10 terms).
- Evidence: `/app/outputs/coefficients.json`

### Step 2: Evaluate stress along crack line
- Role: scored (load-bearing)
- Action: Using the displacement jump coefficients from the previous step, evaluate the non-local normal stress tau_yy(x,0) along the crack line y=0 by numerically integrating the Fourier inversion formula. Generate data for x/l in the range [-2.0, 2.0] with at least 200 uniformly spaced points, normalize the stress by the applied tension tau_0 = p0, and write the results to stress_curve.csv.
- Output file: `/app/outputs/stress_curve.csv`
- Format: csv
- Contract: CSV with columns: x_over_l (float), stress_normalized (float). At least 200 rows covering x/l from -2.0 to 2.0, sorted by x_over_l.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_curve.csv
- path: `/app/outputs/stress_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized normal stress distribution tau_yy/tau_0 along the crack line (y=0). The checker extracts stress at x/l=1.0 (crack tip) and the location and value of the maximum stress, and compares them against hidden gold values digitised from the paper with an absolute tolerance. The CSV must have >=200 rows and cover x/l from -2.0 to 2.0.
- schema:
  - `type`: table
  - `required_columns`: `x_over_l`, `stress_normalized`
  - `units`:
    - `x_over_l`: dimensionless
    - `stress_normalized`: dimensionless

Notes: The hidden gold values are approximate digitizations from the paper's figure, used as reference. The tolerance is set to absorb legitimate implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_over_l",
          "stress_normalized"
        ],
        "units": {
          "x_over_l": "dimensionless",
          "stress_normalized": "dimensionless"
        }
      },
      "description": "Normalized normal stress distribution tau_yy/tau_0 along the crack line (y=0). The checker extracts stress at x/l=1.0 (crack tip) and the location and value of the maximum stress, and compares them against hidden gold values digitised from the paper with an absolute tolerance. The CSV must have >=200 rows and cover x/l from -2.0 to 2.0."
    }
  ],
  "notes": "The hidden gold values are approximate digitizations from the paper's figure, used as reference. The tolerance is set to absorb legitimate implementation differences."
}
```

## How you are scored
The hidden verifier reads stress_curve.csv and first checks that the file has at least 200 rows and covers the required x/l range. It then extracts the normalised stress at x/l = 1.0 and scans the data to locate the maximum stress value and its corresponding x/l coordinate. These three extracted numbers are compared against reference values derived from the paper's reported results, using a tolerance that accounts for legitimate differences in numerical implementation (truncation order, integration grid, etc.). The final reward is based solely on how well these comparisons match; the format and coverage checks contribute a minor weight. The solve_coefficients step is required to produce coefficients.json as evidence that the solver was invoked, but that file is not directly scored.
