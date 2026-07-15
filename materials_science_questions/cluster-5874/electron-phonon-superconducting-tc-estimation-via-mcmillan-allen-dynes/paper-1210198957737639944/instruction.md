# Superconducting Parameters from Input Critical Fields and Specific Heat Coefficients

## Problem background
Niobium-rich alloys with early transition metals are type‑II superconductors with potentially high critical fields and current densities. Their superconducting performance is characterized by derived parameters such as the Ginzburg–Landau coherence length, penetration depth, GL parameter, thermodynamic critical field, Debye temperature, and electron–phonon coupling constant. These quantities are not measured directly but are computed from experimentally measured values (critical fields, transition temperature, and specific heat coefficients) using standard superconductivity relations. The task is to compute these derived parameters for three representative alloys to quantitatively assess their superconducting properties.

## Approach
Compute the six derived superconducting parameters from the provided measured input values using a set of well‑established relations. From the zero‑temperature upper critical field, obtain the GL coherence length via flux quantization. Then, numerically solve the transcendental equation linking the lower critical field, coherence length, and penetration depth to determine the penetration depth. The GL parameter is the ratio of the two length scales. The thermodynamic critical field is obtained from the two critical fields and the GL parameter under the GL framework. The Debye temperature is derived from the phononic heat‑capacity coefficient using the Debye model, assuming a fixed number of atoms per formula unit. Finally, the electron–phonon coupling constant is calculated with McMillan’s formula, using the transition temperature, Debye temperature, and a standard Coulomb pseudopotential. All required input values are taken from the magnetization and specific-heat measurements reported in the paper. The values for each alloy are:

| Alloy | Tc (K) | Hc1(0) (mT) | Hc2(0) (T) | γ_n (mJ mol⁻¹ K⁻²) | β (mJ mol⁻¹ K⁻⁴) |
|-------|--------|-------------|------------|----------------------|-------------------|
| Nb₆Ti | 9.65   | 39.4        | 5.57       | 51.17                | 0.63              |
| Nb₆Zr | 11.05  | 107.4       | 9.51       | 61.45                | 0.79              |
| Nb₆Hf | 9.67   | 46.5        | 5.81       | 51.93                | 0.99              |

## Reproduction target
For each of the three alloy compositions Nb6Ti, Nb6Zr, and Nb6Hf, compute the following six parameters from the inputs provided in the task instruction:
- GL coherence length ξ_GL(0) (Å)
- penetration depth λ_GL(0) (Å)
- GL parameter k_GL (dimensionless)
- thermodynamic critical field H_c(0) (mT)
- Debye temperature θ_D (K)
- electron–phonon coupling constant λ_e-ph (dimensionless)
Write the results to a single CSV file at /app/outputs/computed_params.csv with the specified columns. The output must include exactly one row per alloy.

## Assets

- Python 3 with numpy and scipy: numpy, scipy

## Workflow steps

### Step 1: Compute derived superconducting parameters
- Role: scored (load-bearing)
- Action: Implement the formulas: compute GL coherence length xi_GL from Hc2(0) via xi_GL = sqrt(Phi0/(2*pi*Hc2(0))) with Phi0=2.07e-15 T m^2, numerically solve the transcendental equation Hc1(0) = (Phi0/(4*pi*lambda_GL^2))*(ln(lambda_GL/xi_GL)+0.12) for lambda_GL using the given Hc1(0) and the computed xi_GL, compute the GL parameter k_GL = lambda_GL/xi_GL, compute the thermodynamic critical field Hc(0) from Hc1(0)*Hc2(0) = Hc(0)^2 * ln(k_GL), compute the Debye temperature theta_D from the phonon coefficient beta using theta_D = (12*pi^4 * R * N / (5*beta))^(1/3) with N=7 (atoms per formula unit for Nb6X) and R=8.314 J/(mol K), and compute the electron-phonon coupling constant lambda_e-ph via McMillan's formula using theta_D, Tc and mu*=0.13. Use the input values (Tc, Hc1(0), Hc2(0), gamma_n, beta) provided in the instruction for each of the three alloys: Nb6Ti, Nb6Zr, Nb6Hf. Write the results for each alloy.
- Output file: `/app/outputs/computed_params.csv`
- Format: csv
- Contract: columns: alloy (string), xi_GL_A (float, angstrom), lambda_GL_A (float, angstrom), k_GL (float), H_c_mT (float, mT), theta_D_K (float, K), lambda_e_ph (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_params.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_params.csv
- path: `/app/outputs/computed_params.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed superconducting parameters for the three alloys.
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `xi_GL_A`, `lambda_GL_A`, `k_GL`, `H_c_mT`, `theta_D_K`, `lambda_e_ph`
  - `units`:
    - `xi_GL_A`: angstrom
    - `lambda_GL_A`: angstrom
    - `k_GL`: dimensionless
    - `H_c_mT`: millitesla
    - `theta_D_K`: kelvin
    - `lambda_e_ph`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "xi_GL_A",
          "lambda_GL_A",
          "k_GL",
          "H_c_mT",
          "theta_D_K",
          "lambda_e_ph"
        ],
        "units": {
          "xi_GL_A": "angstrom",
          "lambda_GL_A": "angstrom",
          "k_GL": "dimensionless",
          "H_c_mT": "millitesla",
          "theta_D_K": "kelvin",
          "lambda_e_ph": "dimensionless"
        }
      },
      "description": "Computed superconducting parameters for the three alloys."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently recompute the same six parameters for each alloy using the identical input values and the same set of formulas. It will compare your submitted values in computed_params.csv against its own computed reference values. The score is the fraction of individual alloy–parameter comparisons (18 in total) that fall within the verifier’s tolerance. No partial credit is given for approximate matches outside the tolerance. A correct submission in which all computed values agree with the verifier’s reference yields a maximum score of 1.0.
