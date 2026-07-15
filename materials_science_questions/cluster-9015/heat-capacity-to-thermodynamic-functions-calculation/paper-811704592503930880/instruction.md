# Phonon model fitting and thermodynamic functions from heat capacity data

## Problem background
Ternary bismuth tantalum oxides are constituents of systems important for non‑volatile memory and microwave dielectrics. Accurate thermodynamic data—especially molar heat capacity and standard molar entropy—are needed for phase‑diagram calculations and material design. This task computes those thermodynamic functions from experimental heat capacity measurements using a phonon model analysis and numerical integration.

## Approach
Low‑temperature isobaric heat capacity data (relaxation calorimetry and DSC) are modelled with an additive Debye–Einstein phonon spectrum that includes anharmonic corrections. One triply degenerate Debye acoustic branch and several grouped Einstein optical branches (with fixed degeneracies per compound) are fitted to the experimental $C_{pm}$ vs $T$ data by non‑linear least squares.

From the fitted model, thermodynamic functions at 298.15 K are obtained by numerical integration: relative enthalpy $H_m(T)-H_m(0)$ from $\int_0^T C_{pm}\,\mathrm{d}T$ and standard molar entropy $S_m^\circ(T)$ from $\int_0^T \frac{C_{pm}}{T}\,\mathrm{d}T$ (the low‑$T$ limit $C_{pm}/T\to0$ is used).

High‑temperature $C_{pm}$ is represented by the polynomial $C_{pm}=A+BT-C/T^2$, with coefficients determined by weighted least squares using DSC and enthalpy‑increment data and constrained to match the low‑temperature model at 298.15 K. The workflow is implemented with open‑source Python libraries (non‑linear optimisation, numerical integration).

## Reproduction target
Using the provided low‑temperature heat capacity (relaxation calorimetry and DSC) and high‑temperature enthalpy increment data for the three oxides $\text{Bi}_4\text{Ta}_2\text{O}_{11}$, $\text{Bi}_7\text{Ta}_3\text{O}_{18}$, and $\text{Bi}_3\text{TaO}_7$, perform the following for **every** compound:

1. Fit the additive Debye+Einstein phonon model with anharmonic corrections to the low‑$T$ $C_{pm}$ data; report the Debye and Einstein characteristic temperatures, anharmonic coefficients, and degeneracies.
2. Numerically integrate the fitted model to obtain $S_m^\circ(298.15\,\text{K})$, $H_m(298.15\,\text{K})-H_m(0)$, and $C_{pm}(298.15\,\text{K})$.
3. Fit the polynomial $C_{pm}=A+BT-C/T^2$ to the combined DSC and enthalpy increment data by weighted least squares, enforcing the constraint that $C_{pm}(298.15\,\text{K})$ equals the value from the low‑temperature model.

Write the results to the structured output files listed below. The outputs must strictly follow the declared formats and schemas.

## Assets

- Supplementary Tables S1-S3 (low-temperature Cpm, DSC, and enthalpy increment data): 10.1016/j.jssc.2010.11.020
- Python scientific computing stack (numpy, scipy, lmfit): numpy scipy lmfit

## Workflow steps

### Step 1: Low-temperature linear analysis (C_pm/T vs T^2)
- Role: process
- Action: For each oxide (Bi4Ta2O11, Bi7Ta3O18, Bi3TaO7), using the low-temperature C_pm data for T < 8 K, fit C_pm/T vs T^2 to a linear function to estimate the coefficient β (proportional to the Debye temperature) and any Sommerfeld-like term, and compute an initial Debye temperature ΘD from β.
- Evidence: `/app/outputs/low_T_linear_fit.json`

### Step 2: Phonon model fitting
- Role: scored (load-bearing)
- Action: Fit an additive phonon model to the combined low-temperature molar heat capacity data (relaxation + DSC) for each oxide using nonlinear least-squares. The model consists of one triply degenerate Debye acoustic branch and five grouped Einstein optical branches, with anharmonic correction factors (1-αT)⁻¹.
Debye contribution: C_phD = (9R/(1-αD T)) (T/ΘD)³ ∫₀^{ΘD/T} x⁴ eˣ/(eˣ-1)² dx.
Einstein contribution for each group i: C_phEi = (R/(1-αEi T)) (ΘEi/T)² e^{ΘEi/T}/(e^{ΘEi/T}-1)².
Use the degeneracy groups specified in the paper for each oxide (Bi4Ta2O11: [6,8,10,10,14]; Bi7Ta3O18: [8,12,16,20,25]; Bi3TaO7: [4,6,6,8,6]). Fit simultaneously the Debye temperature ΘD, anharmonic coefficient αD, and for each Einstein group: ΘEi, αEi. Output the fitted parameters in JSON.
- Output file: `/app/outputs/phonon_parameters.json`
- Format: json
- Contract: JSON object with keys Bi4Ta2O11, Bi7Ta3O18, Bi3TaO7. Each value is an array of mode objects. Each object: {mode: string "D" or "Ei", Theta: number in K, alpha: number in K⁻¹, degeneracy: integer}. Order of entries within each array: D, E1, E2, E3, E4, E5.
- Scoring: scored by hidden verifier

### Step 3: Thermodynamic functions at 298.15 K
- Role: scored
- Action: From the fitted phonon model (obtained in the previous step), numerically integrate C_pm(T) from 0 to 298.15 K to obtain the relative enthalpy H_m(298.15 K) - H_m(0), and integrate C_pm(T)/T from 0 to 298.15 K (with the low-T limit C_pm/T → γ_el as T→0; γ_el is negligible) to obtain the standard molar entropy S_m(298.15 K). Also report C_pm(298.15 K). Save the results as CSV.
- Output file: `/app/outputs/thermodynamic_functions_298.csv`
- Format: csv
- Contract: CSV with header: compound, Cpm_298 (J K⁻¹ mol⁻¹), Hm_minus_H0 (J mol⁻¹), Sm_298 (J K⁻¹ mol⁻¹). Rows for Bi4Ta2O11, Bi7Ta3O18, Bi3TaO7.
- Scoring: scored by hidden verifier

### Step 4: High-temperature C_pm equation fitting
- Role: scored
- Action: Perform a weighted least-squares fit to obtain high-temperature heat capacity equations for each oxide. Use the DSC C_pm data (265-353 K) and drop calorimetry enthalpy increment data (622-1322 K) from the supplementary tables. Assign weights proportional to 1/σ² with relative uncertainties σ of 1% for DSC and 3% for drop data. Fit to the polynomial C_pm = A + B T - C/T², subject to the constraint that C_pm(298.15 K) matches the value obtained from the low-temperature phonon model fit. Report the coefficients A, B, C in CSV.
- Output file: `/app/outputs/high_t_cpm_coefficients.csv`
- Format: csv
- Contract: CSV with header: compound, A (J K⁻¹ mol⁻¹), B (J K⁻² mol⁻¹), C (J K mol⁻¹). Rows for Bi4Ta2O11, Bi7Ta3O18, Bi3TaO7.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_parameters.json`
- `/app/outputs/thermodynamic_functions_298.csv`
- `/app/outputs/high_t_cpm_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_parameters.json
- path: `/app/outputs/phonon_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted phonon model parameters: Debye and Einstein characteristic temperatures (K), anharmonic coefficients (K⁻¹), and degeneracies for each oxide. The array for each oxide must contain exactly 6 entries in order: D, E1, E2, E3, E4, E5.
- schema:
  - `type`: object
  - `required`: `Bi4Ta2O11`, `Bi7Ta3O18`, `Bi3TaO7`
  - `properties`:
    - `Bi4Ta2O11`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `mode`, `Theta`, `alpha`, `degeneracy`
        - `properties`:
          - `mode`:
            - `type`: string
          - `Theta`:
            - `type`: number
            - `units`: K
          - `alpha`:
            - `type`: number
            - `units`: K⁻¹
          - `degeneracy`:
            - `type`: integer
    - `Bi7Ta3O18`:
      - `$ref`: #/properties/Bi4Ta2O11
    - `Bi3TaO7`:
      - `$ref`: #/properties/Bi4Ta2O11

### thermodynamic_functions_298.csv
- path: `/app/outputs/thermodynamic_functions_298.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Standard molar heat capacity, relative enthalpy, and standard molar entropy at 298.15 K for Bi4Ta2O11, Bi7Ta3O18, Bi3TaO7.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `Cpm_298`, `Hm_minus_H0`, `Sm_298`
  - `columns`:
    - `compound`:
      - `type`: string
    - `Cpm_298`:
      - `type`: number
      - `units`: J K⁻¹ mol⁻¹
    - `Hm_minus_H0`:
      - `type`: number
      - `units`: J mol⁻¹
    - `Sm_298`:
      - `type`: number
      - `units`: J K⁻¹ mol⁻¹

### high_t_cpm_coefficients.csv
- path: `/app/outputs/high_t_cpm_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: High-temperature C_pm polynomial coefficients A, B, C for each oxide.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `A`, `B`, `C`
  - `columns`:
    - `compound`:
      - `type`: string
    - `A`:
      - `type`: number
      - `units`: J K⁻¹ mol⁻¹
    - `B`:
      - `type`: number
      - `units`: J K⁻² mol⁻¹
    - `C`:
      - `type`: number
      - `units`: J K mol⁻¹

Notes: All values are compared to the paper-reported reference using appropriate relative tolerances. The low-temperature linear fit step is required as a preliminary analysis but its output is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Bi4Ta2O11",
          "Bi7Ta3O18",
          "Bi3TaO7"
        ],
        "properties": {
          "Bi4Ta2O11": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "mode",
                "Theta",
                "alpha",
                "degeneracy"
              ],
              "properties": {
                "mode": {
                  "type": "string"
                },
                "Theta": {
                  "type": "number",
                  "units": "K"
                },
                "alpha": {
                  "type": "number",
                  "units": "K⁻¹"
                },
                "degeneracy": {
                  "type": "integer"
                }
              }
            }
          },
          "Bi7Ta3O18": {
            "$ref": "#/properties/Bi4Ta2O11"
          },
          "Bi3TaO7": {
            "$ref": "#/properties/Bi4Ta2O11"
          }
        }
      },
      "description": "Fitted phonon model parameters: Debye and Einstein characteristic temperatures (K), anharmonic coefficients (K⁻¹), and degeneracies for each oxide. The array for each oxide must contain exactly 6 entries in order: D, E1, E2, E3, E4, E5."
    },
    {
      "file": "thermodynamic_functions_298.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "Cpm_298",
          "Hm_minus_H0",
          "Sm_298"
        ],
        "columns": {
          "compound": {
            "type": "string"
          },
          "Cpm_298": {
            "type": "number",
            "units": "J K⁻¹ mol⁻¹"
          },
          "Hm_minus_H0": {
            "type": "number",
            "units": "J mol⁻¹"
          },
          "Sm_298": {
            "type": "number",
            "units": "J K⁻¹ mol⁻¹"
          }
        }
      },
      "description": "Standard molar heat capacity, relative enthalpy, and standard molar entropy at 298.15 K for Bi4Ta2O11, Bi7Ta3O18, Bi3TaO7."
    },
    {
      "file": "high_t_cpm_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "A",
          "B",
          "C"
        ],
        "columns": {
          "compound": {
            "type": "string"
          },
          "A": {
            "type": "number",
            "units": "J K⁻¹ mol⁻¹"
          },
          "B": {
            "type": "number",
            "units": "J K⁻² mol⁻¹"
          },
          "C": {
            "type": "number",
            "units": "J K mol⁻¹"
          }
        }
      },
      "description": "High-temperature C_pm polynomial coefficients A, B, C for each oxide."
    }
  ],
  "notes": "All values are compared to the paper-reported reference using appropriate relative tolerances. The low-temperature linear fit step is required as a preliminary analysis but its output is not scored."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently evaluates each workflow stage’s artifact:

- Every numeric entry in `phonon_parameters.json`, `thermodynamic_functions_298.csv`, and `high_t_cpm_coefficients.csv` is compared against reference values derived from the published measurements, using appropriate tolerances.
- Self‑consistency checks are also applied (for example, the entropy obtained by integrating your submitted phonon model is compared with your reported $S_m^\circ(298.15)$).
- The final reward is a weighted sum of the individual artifact scores.

Simply copying numbers from the literature will not pass the verifier; only a genuine re‑execution of the computational pipeline (fitting, integration, constrained least squares) can produce artifacts that satisfy both the reference tolerances and the self‑consistency tests.
