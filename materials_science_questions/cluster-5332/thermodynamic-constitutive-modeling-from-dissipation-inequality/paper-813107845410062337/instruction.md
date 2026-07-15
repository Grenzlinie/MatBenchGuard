# Thermo-magneto-mechanical coupling in magnetoactive elastomers: analytical boundary value solutions

## Problem background
Magneto-rheological elastomers (MREs) are composite materials whose mechanical properties can be altered by an external magnetic field. Because the polymer matrix is temperature-sensitive, thermal effects significantly influence the material response. Experiments are often non-isothermal, and temperature gradients can develop inside the material. This task addresses the coupled thermo-magneto-mechanical behaviour of MREs by computing the mechanical response of a thick-walled cylindrical tube subjected to combined mechanical (inflation, axial stretch, torsion), magnetic (azimuthal field), and thermal (radial temperature gradient) loads. The objective is to determine the internal pressure and normal force required to maintain given deformations, and the torque needed to twist the tube, using a thermodynamically consistent constitutive framework.

## Approach
The constitutive model is based on a total energy formulation where the free energy function depends on the deformation gradient, temperature, and magnetic field. Temperature effects are incorporated by linearly scaling the energy with temperature relative to a reference state Θ₀. The field-sensitive shear modulus is given by μ(I₄) = (μₑ/4)[1 + αₑ tanh(I₄/mₑ)], where I₄ = |H_Φ|² is the magnetic invariant. The material parameters are μₑ = 0.1 MPa, αₑ = 30, mₑ = 1 T², and the magneto-mechanical coupling constant is c₂ = 0.5 μ₀. The steady-state temperature profile in the radial direction is obtained from the heat equation, resulting in Θ(r) = k₁ + k₂ ln r, with k₁,k₂ determined from the prescribed inner and outer surface temperatures. The azimuthal magnetic field follows from Ampère’s law: h_φ = c / r, where c is a constant related to the applied current. For the extension/inflation problem, the internal pressure P and normal force N are expressed as integrals over the radius; for the torsion problem, the torque M is similarly expressed. The integrals involve terms with the hyperbolic tangent and require numerical quadrature (e.g., Gaussian quadrature). The task is to implement these expressions and compute the values for the provided input parameter grids.

## Reproduction target
Produce two CSV files containing the computed mechanical quantities for a set of input parameter combinations. For the extension/inflation problem (`step_01_extension_inflation.csv`): columns `lambda_i` (radial stretch), `lambda_z` (axial stretch), `zeta` (thickness ratio A_e/A_i), `c` (current constant), `Theta_e` (external temperature in K), `P` (pressure in MPa), `N` (normal force in MPa). For the torsion problem (`step_02_torsion.csv`): columns `tau` (twist angle per unit length, rad/mm), `lambda_z`, `zeta`, `c`, `Theta_e`, `M` (torque in N·m). The values must be computed using the constitutive model described above and numerical integration of the relevant integrals.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute steady-state temperature distribution and azimuthal magnetic field
- Role: process
- Action: Implement the analytical solution for the radial temperature profile Θ(r) = k₁ + k₂ ln r using the provided inner and outer surface temperatures at radii a_i and a_e. Compute the azimuthal magnetic field 𝕙_φ = c/r (where c is a constant related to the applied current) and the associated Maxwell stress components σ_rr^(max) = σ_zz^(max) = −σ_φφ^(max) = (1/2) μ₀ c²/r². These intermediate quantities are needed as inputs for the boundary value solutions.
- Evidence: none

### Step 2: Solve BVP1: Inflation and extension – pressure and normal force
- Role: scored (load-bearing)
- Action: For the first boundary value problem (radial inflation + axial extension), evaluate the integrals for the internal pressure P and normal force N using the thermo-magneto-mechanical constitutive model. Use the temperature-dependent energy function (derived from the total energy) with the field-sensitive hyperbolic shear modulus μ(I₄) = μ_e/4 [1 + α_e tanh(I₄/m_e)], and the material parameters μ_e = 0.1 MPa, α_e = 30, m_e = 1 T², c₂ = 0.5 μ₀. Numerical integration (e.g., Gauss quadrature or scipy.integrate.quad) must be employed for terms involving the hyperbolic function. Compute P and N for each combination of input parameters (λ_i, λ_z, ζ, c, Θ_e) and write the results to the CSV file.
- Output file: `/app/outputs/step_01_extension_inflation.csv`
- Format: csv
- Contract: CSV with columns: lambda_i (radial stretch, dimensionless), lambda_z (axial stretch, dimensionless), zeta (thickness ratio A_e/A_i, dimensionless), c (current constant, A or arbitrary), Theta_e (external temperature, K), P (pressure, MPa), N (normal force, MPa).
- Scoring: scored by hidden verifier

### Step 3: Solve BVP2: Extension and torsion – torque
- Role: scored
- Action: For the second boundary value problem (axial extension + torsion), evaluate the integral for the torque M using the same constitutive model and material parameters as in BVP1. Use numerical integration where closed‑form expressions are unavailable. Compute M for each combination of input parameters (τ, λ_z, ζ, c, Θ_e) and write the results to the CSV file.
- Output file: `/app/outputs/step_02_torsion.csv`
- Format: csv
- Contract: CSV with columns: tau (twist angle per unit length, rad/mm), lambda_z (axial stretch, dimensionless), zeta (thickness ratio A_e/A_i, dimensionless), c (current constant, A or arbitrary), Theta_e (external temperature, K), M (torque, N·m).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_extension_inflation.csv`
- `/app/outputs/step_02_torsion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_extension_inflation.csv
- path: `/app/outputs/step_01_extension_inflation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed internal pressure P and normal force N for the extension/inflation boundary value problem over a grid of input conditions.
- schema:
  - `type`: table
  - `required_columns`: `lambda_i`, `lambda_z`, `zeta`, `c`, `Theta_e`, `P`, `N`
  - `units`:
    - `lambda_i`: dimensionless
    - `lambda_z`: dimensionless
    - `zeta`: dimensionless
    - `c`: current constant (A or arbitrary)
    - `Theta_e`: K
    - `P`: MPa
    - `N`: MPa

### step_02_torsion.csv
- path: `/app/outputs/step_02_torsion.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed torque M for the extension/torsion boundary value problem over a grid of input conditions.
- schema:
  - `type`: table
  - `required_columns`: `tau`, `lambda_z`, `zeta`, `c`, `Theta_e`, `M`
  - `units`:
    - `tau`: rad/mm
    - `lambda_z`: dimensionless
    - `zeta`: dimensionless
    - `c`: current constant (A or arbitrary)
    - `Theta_e`: K
    - `M`: N·m

Notes: The hidden checker recomputes the expected P, N, M values for a hidden subset of parameter combinations using the same analytical formulas and numerical integration, then compares against the agent's submitted CSV values within a relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_extension_inflation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda_i",
          "lambda_z",
          "zeta",
          "c",
          "Theta_e",
          "P",
          "N"
        ],
        "units": {
          "lambda_i": "dimensionless",
          "lambda_z": "dimensionless",
          "zeta": "dimensionless",
          "c": "current constant (A or arbitrary)",
          "Theta_e": "K",
          "P": "MPa",
          "N": "MPa"
        }
      },
      "description": "Computed internal pressure P and normal force N for the extension/inflation boundary value problem over a grid of input conditions."
    },
    {
      "file": "step_02_torsion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "lambda_z",
          "zeta",
          "c",
          "Theta_e",
          "M"
        ],
        "units": {
          "tau": "rad/mm",
          "lambda_z": "dimensionless",
          "zeta": "dimensionless",
          "c": "current constant (A or arbitrary)",
          "Theta_e": "K",
          "M": "N·m"
        }
      },
      "description": "Computed torque M for the extension/torsion boundary value problem over a grid of input conditions."
    }
  ],
  "notes": "The hidden checker recomputes the expected P, N, M values for a hidden subset of parameter combinations using the same analytical formulas and numerical integration, then compares against the agent's submitted CSV values within a relative tolerance."
}
```

## How you are scored
A hidden verifier will independently recompute the expected pressure, normal force, and torque for a hidden subset of the input parameter combinations using the same analytical formulas and numerical integration. Your submitted CSV values will be compared to the recomputed gold values; a relative tolerance will be applied (with an absolute tolerance for near-zero quantities). The total score is a weighted sum of the scores for the two CSV files. Simply reporting the paper’s published numbers or any externally obtained values will not earn credit—only correctly computed results from your own implementation are accepted.
