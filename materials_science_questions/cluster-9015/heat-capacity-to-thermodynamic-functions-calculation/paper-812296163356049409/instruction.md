# Deriving Standard Thermodynamic Functions from Heat Capacity Data

## Problem background
The standard thermodynamic functions of a material—its entropy and enthalpy increment—can be obtained from low‑temperature heat capacity measurements by numerically integrating the heat capacity and its ratio with temperature. The present task concerns anhydrous dicalcium phosphate, CaHPO₄(c), whose heat capacity curve exhibits an anomalous broad hump beginning near 223 K and persisting through room temperature. Such a feature must be handled carefully when constructing a smoothed heat capacity curve and when integrating to obtain reliable standard entropy and enthalpy at 298.15 K. The goal is to derive these thermodynamic quantities from the observed low‑temperature heat capacity data, applying appropriate baseline treatment for the anomalous region.

## Approach
The workflow mirrors the standard calorimetric data‑reduction sequence. First, the heat capacity is extrapolated to 0 K using a linear fit of Cp/T against T² through the lowest available observed points—a common procedure for the low‑temperature limit where Cp ∝ T³. Second, the anomalous hump is treated by defining a “normal” heat capacity baseline through that temperature region. A polynomial, fitted by least squares to a chosen set of observed points on both sides of the hump, represents this baseline. Third, a continuous smoothed molar heat capacity table from 0 to 310 K is constructed by combining the extrapolated low‑T values, the observed data, and the polynomial baseline in the hump region, using appropriate interpolation and smoothing. Finally, the standard entropy S°(T) is obtained by numerically integrating Cp/T dT from 0 K to each temperature, and the enthalpy increment H°(T)−H°(0 K) by integrating Cp dT, both using the trapezoidal rule. The headline values at 298.15 K are extracted from these integrated functions.

## Reproduction target
Given the observed heat capacity data of CaHPO₄(c) as a CSV file (columns: temperature in K and heat capacity in cal/(K·mol)), construct the smoothed heat capacity curve from 0 to 310 K, compute the corresponding standard entropy S° and enthalpy increment H°−H°₀ over that range, and report the standard entropy at 298.15 K (cal/(K·mol)) and the enthalpy increment at 298.15 K (cal/mol). The result is the set of output files: a smoothed heat capacity table, a full thermodynamic properties table, and a JSON object with the two final values.

## Assets

- Observed heat capacity data for CaHPO4
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Extrapolate heat capacity to 0 K
- Role: process
- Action: Using the observed heat capacity data below about 12 K from the provided CSV, extrapolate Cp down to 0 K by a linear fit of Cp/T vs T^2 and compute the Cp contribution for the 0–10 K range.
- Evidence: `/app/outputs/extrapolation_result.csv`

### Step 2: Fit polynomial baseline for normal heat capacity in hump region
- Role: process
- Action: Fit a fourth-degree polynomial by least squares to the selected observed Cp data points: 8 points between 200 K and 223 K, and the point at 293.75 K. This polynomial describes the 'normal' Cp curve through the anomalous hump.
- Evidence: `/app/outputs/baseline_coefficients.json`

### Step 3: Construct smoothed heat capacity table
- Role: scored (load-bearing)
- Action: Combine the 0–10 K extrapolated Cp, the observed Cp data, and the polynomial baseline in the hump region to produce a continuous smoothed molar heat capacity table from 0 to 310 K. Use appropriate interpolation/smoothing. Write the table to smoothed_heat_capacity.csv.
- Output file: `/app/outputs/smoothed_heat_capacity.csv`
- Format: csv
- Contract: CSV with header: T_K, Cp_cal_per_K_mol.
- Scoring: scored by hidden verifier

### Step 4: Integrate to obtain thermodynamic functions
- Role: scored
- Action: Numerically integrate Cp/T dT from 0 K to each temperature using the trapezoidal rule to obtain standard entropy S°, and integrate Cp dT to obtain enthalpy increment H°−H₀°. Produce a table with columns T, Cp, S, H. Write to thermodynamic_properties.csv.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: CSV with header: T_K, Cp_cal_per_K_mol, S_cal_per_K_mol, H_minus_H0_cal_per_mol.
- Scoring: scored by hidden verifier

### Step 5: Extract final standard entropy and enthalpy at 298.15 K
- Role: scored
- Action: From the integration results, read the standard entropy at 298.15 K and the enthalpy increment at 298.15 K. Write these two numbers as a JSON object to final_values.json.
- Output file: `/app/outputs/final_values.json`
- Format: json
- Contract: JSON object with keys 'S_298_15_cal_per_K_mol' and 'H_298_15_minus_H0_cal_per_mol'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/smoothed_heat_capacity.csv`
- `/app/outputs/thermodynamic_properties.csv`
- `/app/outputs/final_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### smoothed_heat_capacity.csv
- path: `/app/outputs/smoothed_heat_capacity.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Smoothed molar heat capacity table from which thermodynamic functions are derived.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `Cp_cal_per_K_mol`
  - `units`:
    - `T_K`: K
    - `Cp_cal_per_K_mol`: cal/(K·mol)

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermodynamic functions table including entropy and enthalpy increment.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `Cp_cal_per_K_mol`, `S_cal_per_K_mol`, `H_minus_H0_cal_per_mol`
  - `units`:
    - `T_K`: K
    - `Cp_cal_per_K_mol`: cal/(K·mol)
    - `S_cal_per_K_mol`: cal/(K·mol)
    - `H_minus_H0_cal_per_mol`: cal/mol

### final_values.json
- path: `/app/outputs/final_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Standard entropy and enthalpy increment at 298.15 K.
- schema:
  - `type`: object
  - `required`:
    - `S_298_15_cal_per_K_mol`: float (cal/(K·mol))
    - `H_298_15_minus_H0_cal_per_mol`: float (cal/mol)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "smoothed_heat_capacity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "Cp_cal_per_K_mol"
        ],
        "units": {
          "T_K": "K",
          "Cp_cal_per_K_mol": "cal/(K·mol)"
        }
      },
      "description": "Smoothed molar heat capacity table from which thermodynamic functions are derived."
    },
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "Cp_cal_per_K_mol",
          "S_cal_per_K_mol",
          "H_minus_H0_cal_per_mol"
        ],
        "units": {
          "T_K": "K",
          "Cp_cal_per_K_mol": "cal/(K·mol)",
          "S_cal_per_K_mol": "cal/(K·mol)",
          "H_minus_H0_cal_per_mol": "cal/mol"
        }
      },
      "description": "Thermodynamic functions table including entropy and enthalpy increment."
    },
    {
      "file": "final_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "S_298_15_cal_per_K_mol": "float (cal/(K·mol))",
          "H_298_15_minus_H0_cal_per_mol": "float (cal/mol)"
        }
      },
      "description": "Standard entropy and enthalpy increment at 298.15 K."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier independently recomputes thermodynamic quantities from your smoothed_heat_capacity.csv and compares them to reference values derived from the original study. It also checks internal consistency of the smoothed Cp curve and cross‑checks the final_values.json against the recomputed numbers. Each scored artifact contributes a weighted share to the overall reward; merely reporting the paper’s numbers without a consistent smoothed curve and correct integration will receive a low or zero score.
