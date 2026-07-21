# Dislocation Glide Force Near Elliptical Inhomogeneity

## Problem background
An edge dislocation (a line defect in a crystal) moving in a material interacts elastically with nearby second-phase particles or fibers. When the particle is elliptical rather than circular, its shape strongly affects the force that pushes or pulls the dislocation. Understanding this interaction is important for designing fiber-reinforced composites and for predicting material strengthening.

The task is to compute the dimensionless glide force on an edge dislocation situated near an elliptical inhomogeneity embedded in an infinite elastic matrix. The glide force depends on the ellipse shape (ellipticity parameter m, defined from its semi-axes), the ratio of shear moduli Γ = G₂/G₁, the Poisson ratios of both phases, and the dislocation’s position and orientation. The Burgers vector is taken to lie along the x-direction (glide direction). The goal is to calculate the dimensionless glide force Fg for a variety of these parameters.

## Approach
The plane elasticity problem is solved using the complex variable method with conformal mapping. The elliptical inhomogeneity is mapped to a circle of radius √m via the transformation ω(ζ) = R(ζ + m/ζ), where R = (a+b)/2. The dislocation’s stress field in the matrix (the unperturbed solution) is described by two complex potentials whose Laurent expansion coefficients A_k and B_k (k ≥ 1) are known analytically.

The perturbative parts of the potentials that account for the inhomogeneity are then expressed as series whose unknown coefficients are determined by enforcing continuity of displacement and traction along the ellipse–matrix interface. For an elliptical shape, this leads to a set of linear recurrence relations (derived in a companion paper, Stagni, ZAMP 33, 315, 1982) that can be solved for the series coefficients.

Once the full potentials are known, the image force per unit length acting on the dislocation is obtained from the Peach–Koehler formula, which requires evaluating the perturbative potentials and their derivatives at the dislocation position. The glide component is the projection of this force onto the Burgers vector direction (x-axis), divided by the appropriate scaling factor to make it dimensionless. The procedure yields the dimensionless glide force Fg.

## Reproduction target
Implement the computational pipeline described above and compute the dimensionless glide force Fg for the test cases listed below. Each test case is defined by the parameters m (ellipticity), Γ (shear modulus ratio, use 0.0 for a hole and 1e10 for a rigid inclusion), ν₁ (matrix Poisson ratio), ν₂ (inclusion Poisson ratio), r₀/R (dimensionless dislocation distance from the center, >1), and φ₀ (angular position in degrees). The Burgers vector is always along the x-axis (B_y = 0).

Output a CSV file with exactly one row per test case and the columns: m, Gamma, nu1, nu2, r0_over_R, phi0_deg, Fg. The column order must match the header and all values must be floating-point numbers.

The test cases are:

| m | Gamma | nu1 | nu2 | r0_over_R | phi0_deg |
|---|---|---|---|---|---|
| 0.0 | 0.0 | 0.3 | 0.3 | 5.0 | 0.0 |
| 0.0 | 0.0 | 0.3 | 0.3 | 5.0 | 90.0 |
| 0.5 | 0.0 | 0.3 | 0.3 | 5.0 | 30.0 |
| 0.5 | 0.0 | 0.3 | 0.3 | 5.0 | 150.0 |
| -0.5 | 0.0 | 0.3 | 0.3 | 5.0 | 60.0 |
| -0.5 | 0.0 | 0.3 | 0.3 | 5.0 | 120.0 |
| 0.0 | 1e10 | 0.3 | 0.3 | 5.0 | 0.0 |
| 0.0 | 1e10 | 0.3 | 0.3 | 5.0 | 90.0 |
| 0.5 | 1e10 | 0.3 | 0.3 | 5.0 | 30.0 |
| -0.5 | 1e10 | 0.3 | 0.3 | 5.0 | 60.0 |
| 0.0 | 0.1 | 0.3 | 0.3 | 5.0 | 0.0 |
| 0.0 | 10.0 | 0.3 | 0.3 | 5.0 | 0.0 |
| 0.5 | 0.1 | 0.3 | 0.3 | 5.0 | 90.0 |
| -0.5 | 10.0 | 0.3 | 0.3 | 5.0 | 90.0 |
| 0.0 | 0.0 | 0.3 | 0.3 | 2.0 | 0.0 |
| 0.0 | 1e10 | 0.3 | 0.3 | 2.0 | 0.0 |
| 0.9 | 0.0 | 0.3 | 0.3 | 5.0 | 0.0 |
| -0.9 | 0.0 | 0.3 | 0.3 | 5.0 | 0.0 |

## Assets

- python3: python3
- numpy: numpy
- Stagni ZAMP 33, 315 (1982) perturbative solution paper: 10.1007/BF00945241

## Workflow steps

### Step 1: Compute Laurent expansion coefficients
- Role: process
- Action: For each test case, compute the Laurent expansion coefficients A_k and B_k (k>=1) from the dislocation position (zeta0), shape parameter m, and Burgers vector orientation. Truncate the series at a k_max sufficient for convergence (e.g., 30-50). Save the coefficients as evidence.
- Evidence: `/app/outputs/laurent_coefficients.json`

### Step 2: Compute perturbative potentials and image force
- Role: process
- Action: Implement the general perturbative solution for the elliptical inhomogeneity. Express the perturbative potentials as series and determine the unknown coefficients using interface continuity conditions or recurrence relations. Evaluate the image force components f_x, f_y at the dislocation position. Save the components as evidence.
- Evidence: `/app/outputs/image_force_components.json`

### Step 3: Compute dimensionless glide force for all test cases
- Role: scored (load-bearing)
- Action: For each test case, project the image force onto the Burgers vector direction (B along x-axis, so Fg = f_x / |gamma| with gamma = G1*(B_y - i B_x) / [pi R (kappa1+1)]). Write one row per test case with the input parameters and the computed dimensionless glide force Fg.
- Output file: `/app/outputs/glide_force_values.csv`
- Format: csv
- Contract: CSV header: m,Gamma,nu1,nu2,r0_over_R,phi0_deg,Fg. m: ellipticity parameter (float); Gamma: shear moduli ratio (float, 0 for hole, large e.g. 1e10 for rigid); nu1: matrix Poisson ratio (float); nu2: inclusion Poisson ratio (float); r0_over_R: dimensionless distance (float, >1); phi0_deg: angular position in degrees (float); Fg: dimensionless glide force (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/glide_force_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### glide_force_values.csv
- path: `/app/outputs/glide_force_values.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed dimensionless glide force for predefined test cases spanning shape, modulus ratios, and dislocation positions. The checker recomputes the correct Fg from each row's input parameters using a reference implementation and checks that the agent's reported Fg agrees within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `m`, `Gamma`, `nu1`, `nu2`, `r0_over_R`, `phi0_deg`, `Fg`

Notes: The hidden checker recomputes Fg from the input parameters in each row using a reference implementation of the full elasticity solution and applies a relative tolerance. Test cases are a public set that sample the parameter ranges shown in the paper's figures; the exercise verifies that the agent correctly implemented the complex potential method, perturbative series, and Peach-Koehler formula.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "glide_force_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "Gamma",
          "nu1",
          "nu2",
          "r0_over_R",
          "phi0_deg",
          "Fg"
        ]
      },
      "description": "Computed dimensionless glide force for predefined test cases spanning shape, modulus ratios, and dislocation positions. The checker recomputes the correct Fg from each row's input parameters using a reference implementation and checks that the agent's reported Fg agrees within a relative tolerance."
    }
  ],
  "notes": "The hidden checker recomputes Fg from the input parameters in each row using a reference implementation of the full elasticity solution and applies a relative tolerance. Test cases are a public set that sample the parameter ranges shown in the paper's figures; the exercise verifies that the agent correctly implemented the complex potential method, perturbative series, and Peach-Koehler formula."
}
```

## How you are scored
A hidden verifier program will read your output CSV, and for each row it will recompute the dimensionless glide force Fg from the input parameters (m, Gamma, nu1, nu2, r0_over_R, phi0_deg) using an independent reference implementation that correctly captures the full elasticity solution (including the conformal mapping, Laurent coefficients, perturbative series, and Peach–Koehler formula). The verifier compares your Fg to the reference Fg with a relative tolerance (the exact tolerance is not disclosed). Your score depends on how many test cases agree to within the tolerance. Simply reporting the paper's published numbers without actually solving the problem will not succeed. Additionally, a small number of hidden test cases (not listed in the public table) are checked to confirm general correctness. The final reward is a weighted sum of the per-case accuracies, with the listed public test cases carrying most of the weight.
