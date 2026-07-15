# IAST Mixed-Gas Adsorption Predictions using pyIAST

## Problem background
Mixed-gas adsorption isotherms are essential for designing gas separation, storage, and catalysis processes, yet they are far more difficult to measure directly than pure-component isotherms. Ideal Adsorbed Solution Theory (IAST) provides a thermodynamic framework that predicts multi-component adsorption equilibria using only the pure-component adsorption isotherms of the individual gases. The open-source Python package pyIAST implements IAST for an arbitrary number of components, offering both analytical model fitting and numerical interpolation of pure-component data, and is capable of forward and reverse IAST calculations. This task evaluates the ability to reproduce IAST predictions for several benchmark systems using pyIAST.

## Approach
The core of the method is to characterise each pure-component adsorption isotherm \( n_i^0(P) \) from provided data and then solve the IAST nonlinear system of equations: for each component, Raoult's-law-like relation \( p_i = x_i p_i^0 \) holds, where \( p_i \) is the partial pressure and \( x_i \) the adsorbed mole fraction, and the spreading pressures of all components must be equal at the pure-component pressures \( p_i^0 \). The spreading pressure is obtained from the pure-component isotherm via integration. pyIAST supports two strategies: (1) fitting an analytical isotherm model (Langmuir, Henry, etc.) and using the resulting analytical expression for the spreading pressure; (2) linearly interpolating the given data points and using numerical quadrature to compute the spreading pressure, with an optional fill-value for extrapolation when the isotherm saturates.

The workflow encompasses four distinct IAST problems:
- A synthetic ternary mixture of fictitious gases A, B, and C, each following a Langmuir isotherm with the same saturation loading but different Langmuir constants (M=1, K_A=2, K_B=10, K_C=20). This serves as a controlled validation case, since an analytical competitive Langmuir expression for the mixture exists.
- Binary methane/ethane adsorption in metal-organic framework IRMOF-1 at 298 K and 65 bar total pressure. The pure-component isotherms are provided as discrete data points and will be characterised using the InterpolatorIsotherm method with the fill-value set to the maximum observed loading.
- Reverse IAST for the same binary system: given a desired adsorbed-phase ethane mole fraction, compute the required gas-phase composition and the resulting component loadings at 65 bar.
- Ternary CO₂/N₂/H₂O adsorption in activated carbon AX-21 at 40 °C, with partial pressures of 166 mbar CO₂, 679 mbar N₂, and 20 mbar H₂O. Pure-component data for CO₂ and N₂ are fitted to Langmuir and Henry models, respectively, while the H₂O isotherm is handled by interpolation.

## Reproduction target
For each system, produce a CSV file of predicted component loadings (all in mmol/g) placed under `/app/outputs`:
- `step_01_langmuir_predictions.csv`: ternary Langmuir mixture at 1 bar total pressure. The file must contain a grid of gas-phase compositions (mole fractions xA, xB, xC summing to 1, e.g., in steps of 0.1). Columns: xA, xB, xC, predicted_loading_A, predicted_loading_B, predicted_loading_C.
- `step_02_binary_predictions.csv`: binary methane/ethane in IRMOF-1 at 65 bar. Scan the gas-phase ethane mole fraction y_ethane from 0 to 1 in steps of 0.05. Columns: y_ethane, predicted_loading_CH4, predicted_loading_C2H6, total_loading.
- `step_03_reverse_predictions.csv`: reverse IAST binary methane/ethane at 65 bar. Scan desired adsorbed ethane mole fraction x_ethane from 0 to 1 in steps of 0.05. Columns: x_ethane, required_y_ethane, predicted_loading_CH4, predicted_loading_C2H6.
- `step_04_ternary_predictions.csv`: ternary CO₂/N₂/H₂O in AX-21, single row with columns: predicted_loading_CO2, predicted_loading_N2, predicted_loading_H2O.
All required pure-component isotherm data files are publicly available and are listed in the Assets section.

## Assets

- pyIAST source code (GitHub): https://github.com/CorySimon/pyIAST
- pyIAST package (PyPI): pyiast
- NumPy: numpy
- SciPy: scipy
- Pandas: pandas
- IRMOF-1 methane pure-component isotherm data: https://raw.githubusercontent.com/CorySimon/pyIAST/master/test/IRMOF-1_methane_isotherm_298K.csv
- IRMOF-1 ethane pure-component isotherm data: https://raw.githubusercontent.com/CorySimon/pyIAST/master/test/IRMOF-1_ethane_isotherm_298K.csv
- CO2 pure-component isotherm data (AX-21): https://raw.githubusercontent.com/CorySimon/pyIAST/master/test/CO2.csv
- N2 pure-component isotherm data (AX-21): https://raw.githubusercontent.com/CorySimon/pyIAST/master/test/N2.csv
- H2O pure-component isotherm data (AX-21): https://raw.githubusercontent.com/CorySimon/pyIAST/master/test/H2O.csv

## Workflow steps

### Step 1: Generate synthetic Langmuir isotherm data and fit models
- Role: process
- Action: Using the known Langmuir parameters (M=1, K_A=2, K_B=10, K_C=20), generate synthetic pure-component adsorption isotherm data for fictitious gases A, B, and C at a range of pressures. Then fit Langmuir models to each dataset using pyIAST's ModelIsotherm to obtain functional forms for the IAST calculation.
- Evidence: `/app/outputs/s01_langmuir_fit_params.json`

### Step 2: IAST predictions for ternary Langmuir mixture
- Role: scored (load-bearing)
- Action: Using the fitted Langmuir models for A, B, and C, run pyIAST.iast() for a grid of gas compositions (mole fractions of A, B, C that sum to 1, e.g., step 0.1) at total pressure 1 bar. Compute and record the predicted loadings of A, B, and C for each composition.
- Output file: `/app/outputs/step_01_langmuir_predictions.csv`
- Format: csv
- Contract: Columns: xA (float, mole fraction of A in gas), xB (float), xC (float), predicted_loading_A (float, mmol/g), predicted_loading_B (float), predicted_loading_C (float). The sum of xA+xB+xC = 1.
- Scoring: scored by hidden verifier

### Step 3: Characterize pure-component isotherms for methane and ethane (IRMOF-1)
- Role: process
- Action: Load the methane and ethane pure-component isotherm CSV files (IRMOF-1_methane_isotherm_298K.csv and IRMOF-1_ethane_isotherm_298K.csv). Create InterpolatorIsotherm objects for methane and ethane using linear interpolation with fill_value set to the maximum loading observed in each dataset.
- Evidence: `/app/outputs/s03_isotherm_models.pkl`

### Step 4: IAST binary methane/ethane predictions
- Role: scored (load-bearing)
- Action: Using the InterpolatorIsotherm objects for methane and ethane, run pyIAST.iast() for a range of gas-phase ethane mole fractions (y_ethane from 0 to 1, e.g., step 0.05) at total pressure 65 bar. Record the predicted loadings of methane and ethane and the total loading for each y_ethane.
- Output file: `/app/outputs/step_02_binary_predictions.csv`
- Format: csv
- Contract: Columns: y_ethane (float, 0-1), predicted_loading_CH4 (float, mmol/g), predicted_loading_C2H6 (float, mmol/g), total_loading (float, mmol/g). One row per y_ethane.
- Scoring: scored by hidden verifier

### Step 5: Reverse IAST for methane/ethane
- Role: scored (load-bearing)
- Action: Using the same InterpolatorIsotherm objects, run pyIAST.reverse_iast() for a range of desired adsorbed-phase ethane mole fractions (x_ethane from 0 to 1, e.g., step 0.05) at total pressure 65 bar. Record the required gas-phase ethane mole fraction and the resulting predicted loadings.
- Output file: `/app/outputs/step_03_reverse_predictions.csv`
- Format: csv
- Contract: Columns: x_ethane (float, 0-1), required_y_ethane (float, 0-1), predicted_loading_CH4 (float, mmol/g), predicted_loading_C2H6 (float, mmol/g). One row per x_ethane.
- Scoring: scored by hidden verifier

### Step 6: Characterize pure-component isotherms for CO2, N2, H2O (AX-21)
- Role: process
- Action: Load the CO2.csv, N2.csv, and H2O.csv files. For CO2, fit a Langmuir model using pyIAST.ModelIsotherm. For N2, fit a Henry's law model. For H2O, create an InterpolatorIsotherm with fill_value equal to the maximum H2O loading. These models will be used for the ternary IAST calculation.
- Evidence: `/app/outputs/s06_ternary_models.pkl`

### Step 7: IAST ternary CO2/N2/H2O prediction
- Role: scored (load-bearing)
- Action: Using the isotherm models for CO2 (Langmuir), N2 (Henry), and H2O (InterpolatorIsotherm), run pyIAST.iast() with the partial pressures: CO2 = 0.166 bar, N2 = 0.679 bar, H2O = 0.020 bar. Record the predicted loadings of CO2, N2, and H2O.
- Output file: `/app/outputs/step_04_ternary_predictions.csv`
- Format: csv
- Contract: Columns: predicted_loading_CO2 (float, mmol/g), predicted_loading_N2 (float, mmol/g), predicted_loading_H2O (float, mmol/g). One row.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_langmuir_predictions.csv`
- `/app/outputs/step_02_binary_predictions.csv`
- `/app/outputs/step_03_reverse_predictions.csv`
- `/app/outputs/step_04_ternary_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_langmuir_predictions.csv
- path: `/app/outputs/step_01_langmuir_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Predicted adsorbed loadings for the synthetic ternary Langmuir mixture at 1 bar over a grid of gas compositions.
- schema:
  - `type`: table
  - `required_columns`: `xA`, `xB`, `xC`, `predicted_loading_A`, `predicted_loading_B`, `predicted_loading_C`
  - `units`:
    - `xA`: dimensionless
    - `xB`: dimensionless
    - `xC`: dimensionless
    - `predicted_loading_A`: mmol/g
    - `predicted_loading_B`: mmol/g
    - `predicted_loading_C`: mmol/g

### step_02_binary_predictions.csv
- path: `/app/outputs/step_02_binary_predictions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: IAST predictions for binary methane/ethane mixture in IRMOF-1 at 65 bar and varying gas-phase ethane mole fraction.
- schema:
  - `type`: table
  - `required_columns`: `y_ethane`, `predicted_loading_CH4`, `predicted_loading_C2H6`, `total_loading`
  - `units`:
    - `y_ethane`: dimensionless
    - `predicted_loading_CH4`: mmol/g
    - `predicted_loading_C2H6`: mmol/g
    - `total_loading`: mmol/g

### step_03_reverse_predictions.csv
- path: `/app/outputs/step_03_reverse_predictions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reverse IAST predictions for binary methane/ethane mixture in IRMOF-1 at 65 bar; required gas-phase composition to achieve desired adsorbed-phase ethane mole fraction.
- schema:
  - `type`: table
  - `required_columns`: `x_ethane`, `required_y_ethane`, `predicted_loading_CH4`, `predicted_loading_C2H6`
  - `units`:
    - `x_ethane`: dimensionless
    - `required_y_ethane`: dimensionless
    - `predicted_loading_CH4`: mmol/g
    - `predicted_loading_C2H6`: mmol/g

### step_04_ternary_predictions.csv
- path: `/app/outputs/step_04_ternary_predictions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: IAST ternary prediction for CO2/N2/H2O mixture in AX-21 at the specified partial pressures (166 mbar CO2, 679 mbar N2, 20 mbar H2O) at 40°C.
- schema:
  - `type`: table
  - `required_columns`: `predicted_loading_CO2`, `predicted_loading_N2`, `predicted_loading_H2O`
  - `units`:
    - `predicted_loading_CO2`: mmol/g
    - `predicted_loading_N2`: mmol/g
    - `predicted_loading_H2O`: mmol/g

Notes: All loadings are in mmol/g. The synthetic Langmuir case uses dimensionless mole fractions xA, xB, xC summing to 1. The binary and reverse cases use y_ethane and x_ethane between 0 and 1. The ternary case is a single-condition prediction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_langmuir_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "xA",
          "xB",
          "xC",
          "predicted_loading_A",
          "predicted_loading_B",
          "predicted_loading_C"
        ],
        "units": {
          "xA": "dimensionless",
          "xB": "dimensionless",
          "xC": "dimensionless",
          "predicted_loading_A": "mmol/g",
          "predicted_loading_B": "mmol/g",
          "predicted_loading_C": "mmol/g"
        }
      },
      "description": "Predicted adsorbed loadings for the synthetic ternary Langmuir mixture at 1 bar over a grid of gas compositions."
    },
    {
      "file": "step_02_binary_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "y_ethane",
          "predicted_loading_CH4",
          "predicted_loading_C2H6",
          "total_loading"
        ],
        "units": {
          "y_ethane": "dimensionless",
          "predicted_loading_CH4": "mmol/g",
          "predicted_loading_C2H6": "mmol/g",
          "total_loading": "mmol/g"
        }
      },
      "description": "IAST predictions for binary methane/ethane mixture in IRMOF-1 at 65 bar and varying gas-phase ethane mole fraction."
    },
    {
      "file": "step_03_reverse_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_ethane",
          "required_y_ethane",
          "predicted_loading_CH4",
          "predicted_loading_C2H6"
        ],
        "units": {
          "x_ethane": "dimensionless",
          "required_y_ethane": "dimensionless",
          "predicted_loading_CH4": "mmol/g",
          "predicted_loading_C2H6": "mmol/g"
        }
      },
      "description": "Reverse IAST predictions for binary methane/ethane mixture in IRMOF-1 at 65 bar; required gas-phase composition to achieve desired adsorbed-phase ethane mole fraction."
    },
    {
      "file": "step_04_ternary_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "predicted_loading_CO2",
          "predicted_loading_N2",
          "predicted_loading_H2O"
        ],
        "units": {
          "predicted_loading_CO2": "mmol/g",
          "predicted_loading_N2": "mmol/g",
          "predicted_loading_H2O": "mmol/g"
        }
      },
      "description": "IAST ternary prediction for CO2/N2/H2O mixture in AX-21 at the specified partial pressures (166 mbar CO2, 679 mbar N2, 20 mbar H2O) at 40°C."
    }
  ],
  "notes": "All loadings are in mmol/g. The synthetic Langmuir case uses dimensionless mole fractions xA, xB, xC summing to 1. The binary and reverse cases use y_ethane and x_ethane between 0 and 1. The ternary case is a single-condition prediction."
}
```

## How you are scored
A hidden verifier reads each of the four CSV files and computes appropriate error metrics (e.g., root mean square deviation, mean absolute error) relative to hidden reference values. The four stages are weighted and combined into an overall reward in [0,1].
- For the synthetic ternary Langmuir mixture, the verifier uses the known analytical competitive Langmuir isotherm (derived from the given Langmuir parameters) as the reference.
- For the binary and reverse binary methane/ethane cases, reference component loadings are obtained from the paper's reported results.
- For the ternary AX-21 case, reference loadings are compared directly against the single prediction.
The scoring is monotonic: predictions that are closer to the reference (or better, when the metric is directional) earn higher credit; there is no penalty for outperforming the reference. The verifier uses tolerances that account for numerical solver differences and does not require exact reproduction of any specific figure. Reporting the paper's numbers without genuine computation is not sufficient to earn credit.
