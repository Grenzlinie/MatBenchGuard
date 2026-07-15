# Dielectric Properties and Dipole Moments of Liquid HFC-143a

## Problem background
The relative permittivity (dielectric constant) of liquid 1,1,1-trifluoroethane (HFC-143a), a hydrofluorocarbon refrigerant, provides insight into molecular interactions and is essential for evaluating compressor oil compatibility and thermodynamic properties. In this task you will use a published experimental dataset of relative permittivity and density as a function of temperature and pressure, together with the refractive index of the liquid, to compute two distinct estimates of the dipole moment in the liquid phase (from the Kirkwood and from the Kirkwood-Frölich theories) and to derive the isobaric thermal expansion coefficient and the isothermal compressibility at each measured state point. The quantity you compute from the data is an open target; the correctness of your fitted models, derived moments, and thermodynamic coefficients will be judged against hidden reference values.

## Approach
The overall workflow consists of loading the experimental dataset, fitting two dielectric equations of state, then using the fitted coefficients and the data to compute the dipole moments and thermodynamic properties.

For the dipole moments, you will first compute per-isotherm average values of the Kirkwood function (which depends on relative permittivity, density, and molar mass) and of the Kirkwood-Frölich function (which additionally depends on the refractive index). You then perform linear regression of these function values against the reciprocal temperature. The slopes of the regressions yield the apparent dipole moment μ_K* (Kirkwood) and the effective dipole moment μ_KF* (Kirkwood-Frölich). These are compared to the known gas-phase dipole moment (μ = 2.340 D, given) to obtain the Kirkwood correlation parameters g_K and g_KF.

For the thermodynamic coefficients, you derive analytic expressions for the partial derivatives of the relative permittivity with respect to temperature, pressure, and density from the fitted dielectric equations. These derivatives are then combined with density to compute the isobaric thermal expansion coefficient α_P and the isothermal compressibility κ_T at every (T_n, P) point in the dataset.

All calculations use standard scientific Python libraries (numpy, scipy). The refractive index must be obtained from the literature (Pitschmann & Straub, 2002). The digitized experimental dataset (Table 2) is provided as a CSV file with columns T, P, rho, epsilon_r.

## Reproduction target
Using the provided CSV dataset (columns T, P, rho, epsilon_r for nine isotherms from ~218 K to ~294 K and pressures up to 15 MPa) and the liquid refractive index of HFC-143a, produce the following four artifacts:

1. Fitted coefficients and standard errors of the two dielectric equations of state: one equation in terms of temperature and density, the other in terms of temperature and pressure.
2. Per-isotherm Kirkwood function values, the slope and intercept of the linear regression against 1/T, and the derived apparent dipole moment μ_K* and correlation factor g_K.
3. Per-isotherm Kirkwood-Frölich function values, the slope and intercept of the linear regression against 1/T, and the derived effective dipole moment μ_KF* and correlation factor g_KF.
4. A table of isobaric thermal expansion coefficients α_P and isothermal compressibilities κ_T at each (T_n, P) state point.

Each output must follow the schema and file format described in the workflow steps and the output contract. The task is to reproduce these quantities from the data; the hidden verifier will compare your results to reference values that are not disclosed in these instructions.

## Assets

- Digitized Table 2: relative permittivity and density of HFC-143a
- Refractive index of HFC-143a: https://doi.org/10.1007/s10765-002-0056-5
- Gas-phase dipole moment of HFC-143a (μ = 2.340 D)
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Data preparation
- Role: process
- Action: Load the provided experimental dataset (CSV with columns T, P, rho, epsilon_r) and the refractive index n for liquid HFC-143a from the literature source.
- Evidence: none

### Step 2: Fit dielectric equations of state
- Role: scored
- Action: Using the full (T, P, rho, epsilon_r) dataset, perform nonlinear least-squares fitting of the dielectric equations epsilon_r = a1/T + a2*rho + a3*rho/T and epsilon_r = b0 + b1/T + b2*P + b3*P/T. Output fitted coefficients and their estimated standard errors.
- Output file: `/app/outputs/dielectric_eqn_coefficients.json`
- Format: json
- Contract: {"type": "object", "required_keys": ["a1", "a1_err", "a2", "a2_err", "a3", "a3_err", "b0", "b0_err", "b1", "b1_err", "b2", "b2_err", "b3", "b3_err"]}
- Scoring: scored by hidden verifier

### Step 3: Kirkwood dipole moment calculation
- Role: scored
- Action: For each (T, P, rho, epsilon_r) data point compute the Kirkwood function K1 = (epsilon_r - 1)*(2*epsilon_r + 1)*M/(9*epsilon_r*rho) with M the molar mass. For each isotherm obtain a representative K1 value. Perform linear regression of these per-isotherm K1 values against 1/T_n. From the slope derive the apparent dipole moment μ_K^* and the correlation factor g_K = (μ_K^*/μ)^2 using the known gas-phase dipole μ = 2.340 D.
- Output file: `/app/outputs/kirkwood_results.json`
- Format: json
- Contract: {"type": "object", "required_keys": ["kirkwood_function", "slope", "intercept", "mu_K_star", "g_K"], "kirkwood_function": {"type": "array", "items": {"T_n": "number", "K1": "number"}}}
- Scoring: scored by hidden verifier

### Step 4: Kirkwood-Frölich dipole moment calculation
- Role: scored
- Action: Convert refractive index n to ε_r,∞ = n². For each data point compute the Kirkwood-Frölich function KFF = (epsilon_r - n²)*(2*epsilon_r + n²)*M/(epsilon_r*(n²+2)²*rho). Average per isotherm to obtain representative values. Perform linear regression of KFF against 1/T_n. From the slope derive the effective dipole moment μ_KF^* and the correlation factor g_KF = (μ_KF^*/μ)^2.
- Output file: `/app/outputs/kf_results.json`
- Format: json
- Contract: {"type": "object", "required_keys": ["kf_function", "slope", "intercept", "mu_KF_star", "g_KF"], "kf_function": {"type": "array", "items": {"T_n": "number", "KFF": "number"}}}
- Scoring: scored by hidden verifier

### Step 5: Estimate thermodynamic coefficients
- Role: scored (load-bearing)
- Action: Using the fitted coefficients from the dielectric equations, derive the analytic partial derivatives of epsilon_r with respect to T, P, and ρ. For each (T, P) point in the dataset compute the isobaric thermal expansion coefficient α_P = –(∂ε_r/∂T)_P / (ρ (∂ε_r/∂ρ)_P) and the isothermal compressibility κ_T = (∂ε_r/∂P)_T / (ρ (∂ε_r/∂ρ)_T). Output a table with one row per (T_n, P) point.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: {"type": "table", "required_columns": ["T_n", "P", "alpha_P", "kappa_T"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dielectric_eqn_coefficients.json`
- `/app/outputs/kirkwood_results.json`
- `/app/outputs/kf_results.json`
- `/app/outputs/thermodynamic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dielectric_eqn_coefficients.json
- path: `/app/outputs/dielectric_eqn_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted coefficients of the two dielectric equations of state (Eqs. 2 and 3).
- schema:
  - `type`: object
  - `required_keys`: `a1`, `a1_err`, `a2`, `a2_err`, `a3`, `a3_err`, `b0`, `b0_err`, `b1`, `b1_err`, `b2`, `b2_err`, `b3`, `b3_err`

### kirkwood_results.json
- path: `/app/outputs/kirkwood_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Per-isotherm Kirkwood function values and derived apparent dipole moment.
- schema:
  - `type`: object
  - `required_keys`: `kirkwood_function`, `slope`, `intercept`, `mu_K_star`, `g_K`
  - `kirkwood_function`:
    - `type`: array
    - `items`:
      - `T_n`: number
      - `K1`: number

### kf_results.json
- path: `/app/outputs/kf_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Per-isotherm Kirkwood-Frölich function values and derived effective dipole moment.
- schema:
  - `type`: object
  - `required_keys`: `kf_function`, `slope`, `intercept`, `mu_KF_star`, `g_KF`
  - `kf_function`:
    - `type`: array
    - `items`:
      - `T_n`: number
      - `KFF`: number

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Isobaric thermal expansion coefficient and isothermal compressibility at each reported (T_n, P) state point.
- schema:
  - `type`: table
  - `required_columns`: `T_n`, `P`, `alpha_P`, `kappa_T`

Notes: The gas-phase dipole moment μ = 2.340 D is a known constant and is provided as a resource. The refractive index from Pitschmann & Straub (2002) must be used. The digitized Table 2 dataset is made available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dielectric_eqn_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "a1",
          "a1_err",
          "a2",
          "a2_err",
          "a3",
          "a3_err",
          "b0",
          "b0_err",
          "b1",
          "b1_err",
          "b2",
          "b2_err",
          "b3",
          "b3_err"
        ]
      },
      "description": "Fitted coefficients of the two dielectric equations of state (Eqs. 2 and 3)."
    },
    {
      "file": "kirkwood_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required_keys": [
          "kirkwood_function",
          "slope",
          "intercept",
          "mu_K_star",
          "g_K"
        ],
        "kirkwood_function": {
          "type": "array",
          "items": {
            "T_n": "number",
            "K1": "number"
          }
        }
      },
      "description": "Per-isotherm Kirkwood function values and derived apparent dipole moment."
    },
    {
      "file": "kf_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required_keys": [
          "kf_function",
          "slope",
          "intercept",
          "mu_KF_star",
          "g_KF"
        ],
        "kf_function": {
          "type": "array",
          "items": {
            "T_n": "number",
            "KFF": "number"
          }
        }
      },
      "description": "Per-isotherm Kirkwood-Frölich function values and derived effective dipole moment."
    },
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_n",
          "P",
          "alpha_P",
          "kappa_T"
        ]
      },
      "description": "Isobaric thermal expansion coefficient and isothermal compressibility at each reported (T_n, P) state point."
    }
  ],
  "notes": "The gas-phase dipole moment μ = 2.340 D is a known constant and is provided as a resource. The refractive index from Pitschmann & Straub (2002) must be used. The digitized Table 2 dataset is made available."
}
```

## How you are scored
Each of the four output files is scored independently by a hidden verifier. The verifier reads your submitted artifacts and compares the computed quantities (coefficients, dipole moments, and thermodynamic coefficients) to hidden reference values. The scores from the individual files are weighted and combined into a final reward between 0 and 1. Simply reporting numbers without performing the correct computation will not yield a high score; the verifier checks the internal consistency of derived results and, where applicable, recomputes intermediate relations to verify the correctness of your work. No further details about tolerances or reference values are provided in these instructions.
