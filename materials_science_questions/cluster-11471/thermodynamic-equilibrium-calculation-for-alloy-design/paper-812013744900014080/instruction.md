# Calculation of carbon activity coefficient in austenitic Fe-Cr-Ni-C alloys via Wagner analysis

## Problem background
Austenitic stainless steels are susceptible to intergranular corrosion after sensitization heat-treatment because chromium carbides (Cr23C6) precipitate at grain boundaries, depleting the adjacent matrix of chromium. A thermodynamic model can predict the equilibrium chromium content at the grain boundary if the activity coefficient of carbon in the alloy is known. This task reproduces the computation of the carbon activity coefficient γ_C in austenitic Fe-Cr-Ni-C alloys using the Wagner analysis, which provides a dilute-solution approximation for the activity coefficient as a function of composition and temperature.

## Approach
The Wagner analysis expresses the logarithm of the carbon activity coefficient as a linear combination of the mole fractions of the solute elements (C, Ni, Cr) multiplied by interaction parameters (∂ln γ_C/∂X_i), plus a Henry's law constant γ°_C for carbon in iron. The interaction parameters are obtained from published binary data (Heckler & Winchell, 1963, and Chipman & Brush, 1968) and are provided in the resource `interaction_parameters.csv`. The temperature dependence is introduced by assuming a regular-solution behavior: ln γ_C = H^M/(RT), where H^M is the partial molar enthalpy of mixing, which is considered temperature-independent over the range of interest. The alloy composition is converted from weight percent to mole fraction, and carbon is treated as a dilute solute (X_C ≈ 0). The calculation yields γ_C as a function of chromium, nickel, and temperature.

## Reproduction target
The goal is to compute the carbon activity coefficient γ_C for two composition-temperature grids: (a) Cr varying from 0 to 24 wt% in steps of 2 wt%, with Ni fixed at 10 wt%, at temperatures 500, 600, 700, and 800 °C; (b) Ni varying from 0 to 20 wt% in steps of 2 wt%, with Cr fixed at 5, 10, and 18 wt%, at 600 °C. The results must be written to a CSV file `gamma_C_data.csv` with columns `T_C` (Celsius), `Cr_wt` (weight percent Cr), `Ni_wt` (weight percent Ni), and `gamma_C` (dimensionless).

## Assets

- Wagner interaction parameters for carbon in austenite
- Free energy of formation of Cr23C6

## Workflow steps

### Step 1: Compute carbon activity coefficient γ_C
- Role: scored (load-bearing)
- Action: Implement the Wagner analysis for the carbon activity coefficient in austenitic Fe-Cr-Ni-C alloys. Obtain the Wagner interaction parameters ∂lnγ_C/∂X_Cr, ∂lnγ_C/∂X_Ni, ∂lnγ_C/∂X_C, and the Henry's law constant γ°_C from the provided resource 'interaction_parameters.csv'. Apply the regular‑solution temperature correction ln γ_C = H^M/(RT) to extend the interaction parameters to 500–800 °C. For carbon, assume X_C ≈ 0 (the alloy is dilute). Compute γ_C on the following grids: (a) Cr from 0 to 24 wt% in steps of 2 wt%, Ni fixed at 10 wt%, at temperatures 500, 600, 700, 800 °C; (b) Ni from 0 to 20 wt% in steps of 2 wt%, Cr fixed at 5, 10, 18 wt%, at 600 °C. Write the results to a CSV file with columns T_C (Celsius), Cr_wt (weight percent Cr), Ni_wt (weight percent Ni), gamma_C (dimensionless).
- Output file: `/app/outputs/gamma_C_data.csv`
- Format: csv
- Contract: Header: T_C,Cr_wt,Ni_wt,gamma_C. Each row corresponds to one composition‑temperature point of the specified grids. T_C is a float in Celsius (500, 600, 700, 800). Cr_wt is a float, weight percent chromium (0, 2, 4, ..., 24). Ni_wt is a float, weight percent nickel (0, 2, ..., 20). gamma_C is a dimensionless float, the activity coefficient of carbon.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gamma_C_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gamma_C_data.csv
- path: `/app/outputs/gamma_C_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed carbon activity coefficient γ_C on the specified composition‑temperature grid. The checker compares each row to hidden reference values digitized from the paper's Figures 1 and 2, using a combined relative/absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T_C`, `Cr_wt`, `Ni_wt`, `gamma_C`
  - `units`:
    - `T_C`: Celsius
    - `Cr_wt`: weight percent
    - `Ni_wt`: weight percent
    - `gamma_C`: dimensionless

Notes: No gold values or tolerances are disclosed here. The agent must compute γ_C from the Wagner equation using the provided interaction parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gamma_C_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_C",
          "Cr_wt",
          "Ni_wt",
          "gamma_C"
        ],
        "units": {
          "T_C": "Celsius",
          "Cr_wt": "weight percent",
          "Ni_wt": "weight percent",
          "gamma_C": "dimensionless"
        }
      },
      "description": "Computed carbon activity coefficient γ_C on the specified composition‑temperature grid. The checker compares each row to hidden reference values digitized from the paper's Figures 1 and 2, using a combined relative/absolute tolerance."
    }
  ],
  "notes": "No gold values or tolerances are disclosed here. The agent must compute γ_C from the Wagner equation using the provided interaction parameters."
}
```

## How you are scored
A hidden verifier will evaluate your submitted `gamma_C_data.csv`. It contains secret reference values for γ_C derived from the same Wagner equation and interaction parameters. For each composition-temperature point, the verifier checks whether your computed γ_C is within a combined relative and absolute tolerance. Points that fall within the tolerance earn full credit; larger errors receive proportionally reduced credit up to a maximum allowed deviation. The overall reward is the average score over all points. You must compute γ_C from the provided interaction parameters and the Wagner analysis; simply copying the paper's reported values will not pass.
