# Thermoelastic Parameter Fitting for Na-majorite Garnet

## Problem background
Na-majorite (Na₂MgSi₅O₁₂) is a garnet mineral present in the Earth’s deep mantle. Its thermoelastic properties—isothermal bulk modulus, its pressure derivative, temperature derivative, thermal expansion coefficients, and Grüneisen parameter—are critical for interpreting mineral assemblages formed at high pressures and temperatures. This task uses a set of pressure-volume-temperature measurements on synthetic Na-majorite to extract these parameters by fitting well-established equations of state.

## Approach
The extraction is performed via nonlinear least-squares fitting of pressure-volume-temperature data to three standard equations of state. First, the room-temperature third-order Birch-Murnaghan equation is fitted to data at 300 K to obtain the ambient unit-cell volume, isothermal bulk modulus, and its pressure derivative. Second, the high-temperature Birch-Murnaghan formalism is applied to the full dataset, assuming a linear temperature dependence for the bulk modulus and a quadratic form for the volumetric thermal expansion coefficient α = a + bT. In this step, the ambient volume is fixed to a known value. Finally, the Mie-Grüneisen-Debye model is used to determine the Grüneisen parameter by fitting the thermal pressure. In that fitting, the Debye temperature and the exponent q are fixed, along with the bulk modulus and its pressure derivative. All fits are implemented with open-source scientific Python tools (NumPy, SciPy).

## Reproduction target
Given the tabulated P-V-T data (provided as a bundled CSV file), produce three output files: (1) `room_temp_BM_params.json` containing V0, K0_300, K_prime_0_300 and their uncertainties; (2) `HTBM_params.json` containing K0_300, K_prime_0_300, dK/dT, a, b and their uncertainties, with V0 fixed to 1475.9 Å³; (3) `MGD_params.json` containing the Grüneisen parameter γ0 and its uncertainty, with θ0 fixed at 890 K and q = 1. The target is to compute these parameters as accurately as the fitting and data allow.

## Assets

- Na-majorite P-V-T data (Table 1)
- NumPy: https://pypi.tuna.tsinghua.edu.cn/simple numpy
- SciPy: https://pypi.tuna.tsinghua.edu.cn/simple scipy

## Workflow steps

### Step 1: Room-temperature Birch-Murnaghan EoS fitting
- Role: scored
- Action: From the provided P-V-T data (bundled CSV), select the subset at 300 K. Fit the third-order Birch-Murnaghan equation of state to obtain the ambient unit-cell volume V0, isothermal bulk modulus K0_300, and its pressure derivative K_prime_0_300. Write the fitted parameters and their 1-sigma uncertainties to the output file.
- Output file: `/app/outputs/room_temp_BM_params.json`
- Format: json
- Contract: {"V0": float (Å³), "K0_300": float (GPa), "K_prime_0_300": float, "V0_err": float, "K0_300_err": float, "K_prime_0_300_err": float}
- Scoring: scored by hidden verifier

### Step 2: High-temperature Birch-Murnaghan EoS fitting
- Role: scored
- Action: Fix the ambient volume to V0 = 1475.9 Å³. Fit the entire P-V-T data to the high-temperature Birch-Murnaghan equations (temperature-dependent bulk modulus and thermal expansion) using nonlinear least squares. Extract the bulk modulus K0_300, its pressure derivative K_prime_0_300, temperature derivative of bulk modulus dK_dT, and thermal expansion parameters a and b (where α = a + bT). Write the fitted parameters and their uncertainties to the output file.
- Output file: `/app/outputs/HTBM_params.json`
- Format: json
- Contract: {"V0": 1475.9 (fixed), "K0_300": float (GPa), "K_prime_0_300": float, "dK_dT": float (GPa/K), "a": float (K⁻¹), "b": float (K⁻²), "K0_300_err": float, "K_prime_0_300_err": float, "dK_dT_err": float, "a_err": float, "b_err": float}
- Scoring: scored by hidden verifier

### Step 3: Mie-Grüneisen-Debye EoS fitting
- Role: scored
- Action: Using the Mie-Grüneisen-Debye equation of state, fix V0 = 1475.9 Å³, K0_300 = 184 GPa, K_prime_0_300 = 3.8, Debye temperature θ0 = 890 K, and q = 1. Fit the thermal pressure from the P-V-T data to obtain the Grüneisen parameter γ0. Write γ0 and its uncertainty to the output file.
- Output file: `/app/outputs/MGD_params.json`
- Format: json
- Contract: {"gamma0": float (dimensionless), "gamma0_err": float, "theta0": 890 (K), "q": 1}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/room_temp_BM_params.json`
- `/app/outputs/HTBM_params.json`
- `/app/outputs/MGD_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### room_temp_BM_params.json
- path: `/app/outputs/room_temp_BM_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted parameters from the room-temperature Birch-Murnaghan EoS. Unit cell volume V0, isothermal bulk modulus K0_300, its pressure derivative K_prime_0_300, and their one-sigma uncertainties.
- schema:
  - `type`: object
  - `required`: `V0`, `K0_300`, `K_prime_0_300`, `V0_err`, `K0_300_err`, `K_prime_0_300_err`
  - `properties`:
    - `V0`:
      - `type`: number
      - `unit`: Å³
    - `K0_300`:
      - `type`: number
      - `unit`: GPa
    - `K_prime_0_300`:
      - `type`: number
    - `V0_err`:
      - `type`: number
      - `unit`: Å³
    - `K0_300_err`:
      - `type`: number
      - `unit`: GPa
    - `K_prime_0_300_err`:
      - `type`: number

### HTBM_params.json
- path: `/app/outputs/HTBM_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermoelastic parameters from the high-temperature Birch-Murnaghan EoS. Ambient volume V0 fixed to 1475.9 Å³.
- schema:
  - `type`: object
  - `required`: `V0`, `K0_300`, `K_prime_0_300`, `dK_dT`, `a`, `b`, `K0_300_err`, `K_prime_0_300_err`, `dK_dT_err`, `a_err`, `b_err`
  - `properties`:
    - `V0`:
      - `type`: number
      - `unit`: Å³
      - `const`: 1475.9
    - `K0_300`:
      - `type`: number
      - `unit`: GPa
    - `K_prime_0_300`:
      - `type`: number
    - `dK_dT`:
      - `type`: number
      - `unit`: GPa/K
    - `a`:
      - `type`: number
      - `unit`: K⁻¹
    - `b`:
      - `type`: number
      - `unit`: K⁻²
    - `K0_300_err`:
      - `type`: number
      - `unit`: GPa
    - `K_prime_0_300_err`:
      - `type`: number
    - `dK_dT_err`:
      - `type`: number
      - `unit`: GPa/K
    - `a_err`:
      - `type`: number
      - `unit`: K⁻¹
    - `b_err`:
      - `type`: number
      - `unit`: K⁻²

### MGD_params.json
- path: `/app/outputs/MGD_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Grüneisen parameter γ0 from the Mie-Grüneisen-Debye EoS, with Debye temperature fixed at 890 K and q = 1.
- schema:
  - `type`: object
  - `required`: `gamma0`, `gamma0_err`
  - `properties`:
    - `gamma0`:
      - `type`: number
    - `gamma0_err`:
      - `type`: number
    - `theta0`:
      - `type`: number
      - `unit`: K
      - `const`: 890
    - `q`:
      - `type`: number
      - `const`: 1

Notes: All fitting results are scored by comparison with the paper's reported values. The agent must use the provided data file and standard open-source tools (NumPy, SciPy).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "room_temp_BM_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "V0",
          "K0_300",
          "K_prime_0_300",
          "V0_err",
          "K0_300_err",
          "K_prime_0_300_err"
        ],
        "properties": {
          "V0": {
            "type": "number",
            "unit": "Å³"
          },
          "K0_300": {
            "type": "number",
            "unit": "GPa"
          },
          "K_prime_0_300": {
            "type": "number"
          },
          "V0_err": {
            "type": "number",
            "unit": "Å³"
          },
          "K0_300_err": {
            "type": "number",
            "unit": "GPa"
          },
          "K_prime_0_300_err": {
            "type": "number"
          }
        }
      },
      "description": "Fitted parameters from the room-temperature Birch-Murnaghan EoS. Unit cell volume V0, isothermal bulk modulus K0_300, its pressure derivative K_prime_0_300, and their one-sigma uncertainties."
    },
    {
      "file": "HTBM_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "V0",
          "K0_300",
          "K_prime_0_300",
          "dK_dT",
          "a",
          "b",
          "K0_300_err",
          "K_prime_0_300_err",
          "dK_dT_err",
          "a_err",
          "b_err"
        ],
        "properties": {
          "V0": {
            "type": "number",
            "unit": "Å³",
            "const": 1475.9
          },
          "K0_300": {
            "type": "number",
            "unit": "GPa"
          },
          "K_prime_0_300": {
            "type": "number"
          },
          "dK_dT": {
            "type": "number",
            "unit": "GPa/K"
          },
          "a": {
            "type": "number",
            "unit": "K⁻¹"
          },
          "b": {
            "type": "number",
            "unit": "K⁻²"
          },
          "K0_300_err": {
            "type": "number",
            "unit": "GPa"
          },
          "K_prime_0_300_err": {
            "type": "number"
          },
          "dK_dT_err": {
            "type": "number",
            "unit": "GPa/K"
          },
          "a_err": {
            "type": "number",
            "unit": "K⁻¹"
          },
          "b_err": {
            "type": "number",
            "unit": "K⁻²"
          }
        }
      },
      "description": "Thermoelastic parameters from the high-temperature Birch-Murnaghan EoS. Ambient volume V0 fixed to 1475.9 Å³."
    },
    {
      "file": "MGD_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "gamma0",
          "gamma0_err"
        ],
        "properties": {
          "gamma0": {
            "type": "number"
          },
          "gamma0_err": {
            "type": "number"
          },
          "theta0": {
            "type": "number",
            "unit": "K",
            "const": 890
          },
          "q": {
            "type": "number",
            "const": 1
          }
        }
      },
      "description": "Grüneisen parameter γ0 from the Mie-Grüneisen-Debye EoS, with Debye temperature fixed at 890 K and q = 1."
    }
  ],
  "notes": "All fitting results are scored by comparison with the paper's reported values. The agent must use the provided data file and standard open-source tools (NumPy, SciPy)."
}
```

## How you are scored
A hidden verifier compares the parameters you report in each output file against established reference values (derived from the original study) using appropriate tolerances. Each parameter is scored individually; the total reward is the weighted sum across all output files. The verifier does not consider how you obtained the numbers—only the submitted JSON files matter. It is thus essential that your fitting procedure is sound and the reported values are consistent with the data.
