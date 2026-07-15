# Compute Orowan bypass shear stress for nanoscale precipitates in cast austenitic alloys

## Problem background
Metal matrix composites — particularly cast austenitic stainless steels — can achieve high-temperature creep strength through nanoscale precipitates that pin dislocations. The Orowan bowing mechanism relates the bypass shear stress to precipitate size, inter-particle spacing, and shear modulus. Quantifying this stress for the Z-phase nitrides in the improved alloy CF8C-Plus, and comparing it with the predecessor CF8C, helps evaluate the contribution of fine precipitation to creep resistance. This task computes the Orowan shear stress at 750 °C for both alloys.

## Approach
Use the following precipitate statistics: CF8C‑Plus: d = 16 nm, N_V = 6.8×10^20 m⁻³; CF8C: d = 55 nm, N_V = 4.6×10^19 m⁻³. The temperature T = 750 °C, and the following material constants: Taylor factor M = 3.06, Burgers vector b = 2.53×10⁻¹⁰ m, Poisson’s ratio ν = 0.25, core radius r₀ = b. The elastic modulus E (GPa) obeys the linear relation E = 140 − 0.07·T (°C). Compute the shear modulus G = E/[2(1+ν)]. Then, for each alloy, calculate the mean planar inter-particle separation λ_S = 1/(2√(N_V·d)), the mean planar intersection diameter d_S = d·√(2/3), and the Orowan bypass shear stress τ = (0.81·M·G·b) / (2π√(1-ν)) · ln(d_S/r₀) / (λ_S − d_S). The result is a CSV containing the input parameters and all intermediate quantities for CF8C-Plus and CF8C.

## Reproduction target
Compute the Orowan bypass shear stress τ (in MPa) for the Z‑phase precipitates in CF8C-Plus and for the Nb(C,N) precipitates in CF8C at 750 °C using the given precipitate statistics and formulas. Produce a CSV file that includes, for each alloy, the input diameter and number density, the computed λ_S, d_S, G, and the final τ.

## Assets

- Python numerical libraries (numpy, pandas): numpy, pandas

## Workflow steps

### Step 1: Compute Orowan shear stress for CF8C-Plus and CF8C
- Role: scored
- Action: Using the given precipitate statistics (d, N_v) and temperature, compute the mean planar inter-particle separation (lambda_S) from equation lambda_S = 1/(2*sqrt(N_v*d)), the mean planar intersection diameter (d_S = d * sqrt(2/3)), the shear modulus G from the elastic modulus relation E(GPa)=140-0.07*T(°C) and Poisson's ratio 0.25 via G = E/(2*(1+ν)), and the Orowan bypass shear stress tau via the formula tau = (0.81 * M * G * b) / (2 * pi * sqrt(1-ν)) * ln(d_S/r0) / (lambda_S - d_S), with M=3.06, b=2.53e-10 m, r0=b. Compute for both alloys and write the intermediate and final results to step_02_orowan_contribution.csv.
- Output file: `/app/outputs/step_02_orowan_contribution.csv`
- Format: csv
- Contract: CSV with columns: alloy (string), d_nm (float), N_V_per_m3 (float), lambda_S_nm (float), d_S_nm (float), G_GPa (float), tau_MPa (float). Exactly two rows: CF8C-Plus and CF8C.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_orowan_contribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_orowan_contribution.csv
- path: `/app/outputs/step_02_orowan_contribution.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file containing intermediate computed quantities and the final Orowan shear stress (tau_MPa) for CF8C-Plus and CF8C. The checker recomputes tau_MPa from lambda_S_nm, d_S_nm, G_GPa using the Orowan formula and compares the recomputed values to hidden gold values with tolerance, and checks that CF8C-Plus tau > CF8C tau.
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `d_nm`, `N_V_per_m3`, `lambda_S_nm`, `d_S_nm`, `G_GPa`, `tau_MPa`
  - `units`:
    - `d_nm`: nm
    - `N_V_per_m3`: m^{-3}
    - `lambda_S_nm`: nm
    - `d_S_nm`: nm
    - `G_GPa`: GPa
    - `tau_MPa`: MPa

Notes: The public instruction provides the precipitate statistics (d, N_v) for both alloys, the temperature (750°C), the elastic modulus relation E(GPa)=140-0.07T, the material constants (M=3.06, b=2.53e-10 m, ν=0.25, r0=b), and the formulas for lambda_S, d_S, and tau. No hidden parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_orowan_contribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "d_nm",
          "N_V_per_m3",
          "lambda_S_nm",
          "d_S_nm",
          "G_GPa",
          "tau_MPa"
        ],
        "units": {
          "d_nm": "nm",
          "N_V_per_m3": "m^{-3}",
          "lambda_S_nm": "nm",
          "d_S_nm": "nm",
          "G_GPa": "GPa",
          "tau_MPa": "MPa"
        }
      },
      "description": "CSV file containing intermediate computed quantities and the final Orowan shear stress (tau_MPa) for CF8C-Plus and CF8C. The checker recomputes tau_MPa from lambda_S_nm, d_S_nm, G_GPa using the Orowan formula and compares the recomputed values to hidden gold values with tolerance, and checks that CF8C-Plus tau > CF8C tau."
    }
  ],
  "notes": "The public instruction provides the precipitate statistics (d, N_v) for both alloys, the temperature (750°C), the elastic modulus relation E(GPa)=140-0.07T, the material constants (M=3.06, b=2.53e-10 m, ν=0.25, r0=b), and the formulas for lambda_S, d_S, and tau. No hidden parameters."
}
```

## How you are scored
An automated hidden verifier will read your CSV and score the task in two ways. First, it will recompute the Orowan stress τ from your reported intermediate values (λ_S, d_S, G) using the same formula, and check that the recomputed τ agrees with your reported τ and with hidden reference values within an appropriate tolerance. Second, it will confirm that the τ value for CF8C-Plus strictly exceeds that for CF8C. The overall reward is a weighted combination of these consistency and comparison checks. Reporting numbers that merely match the paper without correctly intermediate calculations will not pass; your intermediate values must be internally consistent and correctly derived from the given parameters.
