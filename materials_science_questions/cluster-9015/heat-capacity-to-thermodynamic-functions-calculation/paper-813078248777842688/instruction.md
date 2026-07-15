# Derive Thermodynamic Functions and Formation Enthalpy of EuB6 from EMF and Enthalpy Increment Data

## Problem background
Europium boride (EuB6) is a candidate control-rod material for nuclear reactors because of its high neutron absorption cross-sections and ability to accommodate helium. Designing reactor components requires reliable data on its thermodynamic stability. This work addresses the experimental determination of the standard Gibbs energy of formation of EuB6, its heat capacity, entropy, and Gibbs energy functions, and the standard enthalpy of formation at 298 K. The target quantities are derived from two independent sets of measurements: (i) electromotive force (EMF) measurements on two galvanic cells that employ a YSZ solid electrolyte, and (ii) enthalpy increment measurements on EuB6 obtained by drop calorimetry. The resulting thermodynamic functions provide essential input for nuclear-material databases and for evaluating EuB6 as an absorber material.

## Approach
The experiment uses two EMF cells of the type: test electrode (EuB6 + Eu2O3 + B) || YSZ || reference electrode (Ni/NiO for cell I, Fe/FeO for cell II). Measured EMF versus temperature is fitted to a linear expression. The cell reaction involves transfer of 6 electrons; applying the Nernst equation converts the EMF to the standard reaction Gibbs energy. Combining this with the known standard Gibbs energies of formation of NiO (or FeO) and Eu2O3 yields the standard Gibbs energy of formation of EuB6 as a linear function of temperature. The enthalpy increments of EuB6 measured by drop calorimetry are fitted to a polynomial of the form (H_T – H_298) = a·T + b·T² + c/T + d, constrained so that the function is zero at 298 K and its temperature derivative at 298 K equals the known heat capacity at 298 K. From the fitted polynomial, the heat capacity Cp(T) is obtained by differentiation, entropy S(T) by integration of Cp/T, and the Gibbs energy function (fef) as S(T) – (H_T – H_298)/T. A third-law analysis is performed by computing the pointwise ΔfG°(EuB6) from each EMF datum, interpolating the fef of EuB6 (derived from calorimetry) and the fefs of Eu(s) and B(s) from auxiliary data, and solving ΔfH°298 = ΔfG° – T·Δfef for every measurement point to obtain mean values and standard deviations for each cell.

## Reproduction target
Given the data files emf_cellI.csv, emf_cellII.csv (EMF vs temperature for cells I and II), enthalpy_increments.csv (measured H_T – H_298 vs T), and auxiliary_constants.csv (containing the Faraday constant, Cp at 298 K, S at 298 K, the linear ΔfG° expressions for NiO, FeO, and Eu2O3, and the Gibbs energy functions for Eu(s) and B(s)), perform the following:

- Fit linear EMF expressions for both cells and derive the corresponding linear ΔfG°(EuB6) expressions.
- Fit the enthalpy increment data to the constrained polynomial described in the Approach.
- From the enthalpy fit, compute and tabulate Cp, S, and the Gibbs energy function (GEF) at temperatures from 300 K to 1600 K in 100 K steps.
- Carry out the third-law analysis to obtain the mean ΔfH°298(EuB6) for each cell.

The computed results are written to the specified output files (/app/outputs/step_01_... through step_05_...). The task is purely computational; no wet-lab measurements are required.

## Assets

- EMF measurements for cell I: ./data/emf_cellI.csv
- EMF measurements for cell II: ./data/emf_cellII.csv
- Enthalpy increment measurements: ./data/enthalpy_increments.csv
- Auxiliary thermodynamic data: ./data/auxiliary_constants.csv

## Workflow steps

### Step 1: Fit EMF and derive Gibbs energies for cell I
- Role: scored
- Action: Load emf_cellI.csv, perform linear least-squares regression of EMF (mV) vs Temperature (K) to obtain intercept and slope. Convert EMF expression to standard reaction Gibbs energy change ΔrG°(4) using ΔrG° = -6·F·(EMF/1000). Combine with auxiliary ΔfG° of NiO and Eu2O3 to obtain linear expression for ΔfG° of EuB6. Write all coefficients to a JSON file.
- Output file: `/app/outputs/step_01_cellI_results.json`
- Format: json
- Contract: JSON object with numeric fields: emf_intercept (mV), emf_slope (mV/K), drG_intercept (kJ/mol), drG_slope (kJ/K·mol), dfG_intercept (kJ/mol), dfG_slope (kJ/K·mol).
- Scoring: scored by hidden verifier

### Step 2: Fit EMF and derive Gibbs energies for cell II
- Role: scored
- Action: Load emf_cellII.csv, perform linear least-squares regression of EMF vs T. Convert to ΔrG°(9) via Nernst equation with n=6, then combine with auxiliary ΔfG° of FeO and Eu2O3 to obtain ΔfG° of EuB6. Write the coefficients to JSON.
- Output file: `/app/outputs/step_02_cellII_results.json`
- Format: json
- Contract: JSON object with numeric fields: emf_intercept (mV), emf_slope (mV/K), drG_intercept (kJ/mol), drG_slope (kJ/K·mol), dfG_intercept (kJ/mol), dfG_slope (kJ/K·mol).
- Scoring: scored by hidden verifier

### Step 3: Fit enthalpy increment polynomial
- Role: scored
- Action: Load enthalpy_increments.csv, perform least-squares fit to the functional form (H_T–H_298) = a·T + b·T^2 + c·T^{-1} + d, constrained such that H_T–H_298 = 0 at 298 K and dH/dT = Cp_298. Report the four coefficients.
- Output file: `/app/outputs/step_03_enthalpy_fit.json`
- Format: json
- Contract: JSON object with numeric fields: constant (J/mol), T_coefficient (J/K·mol), T2_coefficient (J/K^2·mol), T_inv_coefficient (J·K/mol).
- Scoring: scored by hidden verifier

### Step 4: Compute thermodynamic functions
- Role: scored (load-bearing)
- Action: Using the fitted enthalpy polynomial, differentiate to obtain Cp(T). Compute entropy S(T) by integration S_T = S_298 + ∫_{298}^T Cp/T dT and Gibbs energy functions (GEF) as -(G_T – H_298)/T = S_T – (H_T–H_298)/T. Output a CSV table at temperatures 300–1600 K in 100 K steps.
- Output file: `/app/outputs/step_04_thermo_functions.csv`
- Format: csv
- Contract: CSV table with columns: T(K), H_T_H298 (kJ/mol), Cp (J/K·mol), S (J/K·mol), GEF (J/K·mol). Rows for T = 300, 400, ..., 1600 K.
- Scoring: scored by hidden verifier

### Step 5: Third-law analysis for ΔfH°298
- Role: scored
- Action: For each experimental EMF point of cells I and II, compute pointwise ΔfG°(EuB6) via Nernst relation combined with auxiliary ΔfG° of reference oxides. Interpolate fefs of EuB6 from Step 4 and fefs of Eu(s) and B(s) from auxiliary constants. Compute ΔfH298 for each datum using ΔfH298 = ΔfG° – T·Δfef, and calculate the mean and standard deviation for each cell. Write the results to JSON.
- Output file: `/app/outputs/step_05_third_law_results.json`
- Format: json
- Contract: JSON object with fields: cell_I_mean_delta_f_H298 (kJ/mol), cell_II_mean_delta_f_H298 (kJ/mol), and optionally arrays cell_I_values, cell_II_values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_cellI_results.json`
- `/app/outputs/step_02_cellII_results.json`
- `/app/outputs/step_03_enthalpy_fit.json`
- `/app/outputs/step_04_thermo_functions.csv`
- `/app/outputs/step_05_third_law_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_cellI_results.json
- path: `/app/outputs/step_01_cellI_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Regression and derived Gibbs energy coefficients for cell I.
- schema:
  - `type`: object
  - `required`:
    - `emf_intercept`: number (mV)
    - `emf_slope`: number (mV/K)
    - `drG_intercept`: number (kJ/mol)
    - `drG_slope`: number (kJ/(K·mol))
    - `dfG_intercept`: number (kJ/mol)
    - `dfG_slope`: number (kJ/(K·mol))

### step_02_cellII_results.json
- path: `/app/outputs/step_02_cellII_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Regression and derived Gibbs energy coefficients for cell II.
- schema:
  - `type`: object
  - `required`:
    - `emf_intercept`: number (mV)
    - `emf_slope`: number (mV/K)
    - `drG_intercept`: number (kJ/mol)
    - `drG_slope`: number (kJ/(K·mol))
    - `dfG_intercept`: number (kJ/mol)
    - `dfG_slope`: number (kJ/(K·mol))

### step_03_enthalpy_fit.json
- path: `/app/outputs/step_03_enthalpy_fit.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted polynomial coefficients for enthalpy increment.
- schema:
  - `type`: object
  - `required`:
    - `constant`: number (J/mol)
    - `T_coefficient`: number (J/(K·mol))
    - `T2_coefficient`: number (J/(K^2·mol))
    - `T_inv_coefficient`: number (J·K/mol)

### step_04_thermo_functions.csv
- path: `/app/outputs/step_04_thermo_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic functions derived from the enthalpy fit at 300-1600 K in 100 K steps.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `H_T_H298 (kJ/mol)`, `Cp (J/K·mol)`, `S (J/K·mol)`, `GEF (J/K·mol)`
  - `units`:
    - `T(K)`: K
    - `H_T_H298 (kJ/mol)`: kJ/mol
    - `Cp (J/K·mol)`: J/(K·mol)
    - `S (J/K·mol)`: J/(K·mol)
    - `GEF (J/K·mol)`: J/(K·mol)

### step_05_third_law_results.json
- path: `/app/outputs/step_05_third_law_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Third-law derived mean standard enthalpy of formation at 298 K from each cell.
- schema:
  - `type`: object
  - `required`:
    - `cell_I_mean_delta_f_H298`: number (kJ/mol)
    - `cell_II_mean_delta_f_H298`: number (kJ/mol)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_cellI_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "emf_intercept": "number (mV)",
          "emf_slope": "number (mV/K)",
          "drG_intercept": "number (kJ/mol)",
          "drG_slope": "number (kJ/(K·mol))",
          "dfG_intercept": "number (kJ/mol)",
          "dfG_slope": "number (kJ/(K·mol))"
        }
      },
      "description": "Regression and derived Gibbs energy coefficients for cell I."
    },
    {
      "file": "step_02_cellII_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "emf_intercept": "number (mV)",
          "emf_slope": "number (mV/K)",
          "drG_intercept": "number (kJ/mol)",
          "drG_slope": "number (kJ/(K·mol))",
          "dfG_intercept": "number (kJ/mol)",
          "dfG_slope": "number (kJ/(K·mol))"
        }
      },
      "description": "Regression and derived Gibbs energy coefficients for cell II."
    },
    {
      "file": "step_03_enthalpy_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "constant": "number (J/mol)",
          "T_coefficient": "number (J/(K·mol))",
          "T2_coefficient": "number (J/(K^2·mol))",
          "T_inv_coefficient": "number (J·K/mol)"
        }
      },
      "description": "Fitted polynomial coefficients for enthalpy increment."
    },
    {
      "file": "step_04_thermo_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "H_T_H298 (kJ/mol)",
          "Cp (J/K·mol)",
          "S (J/K·mol)",
          "GEF (J/K·mol)"
        ],
        "units": {
          "T(K)": "K",
          "H_T_H298 (kJ/mol)": "kJ/mol",
          "Cp (J/K·mol)": "J/(K·mol)",
          "S (J/K·mol)": "J/(K·mol)",
          "GEF (J/K·mol)": "J/(K·mol)"
        }
      },
      "description": "Thermodynamic functions derived from the enthalpy fit at 300-1600 K in 100 K steps."
    },
    {
      "file": "step_05_third_law_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "cell_I_mean_delta_f_H298": "number (kJ/mol)",
          "cell_II_mean_delta_f_H298": "number (kJ/mol)"
        }
      },
      "description": "Third-law derived mean standard enthalpy of formation at 298 K from each cell."
    }
  ],
  "notes": ""
}
```

## How you are scored
Each of the five steps produces a scored artifact. A hidden verifier compares your artifacts against reference values derived from the original measurements. The verifier does not award credit for simply stating the expected results; it evaluates the actual numerical outputs you compute. The scoring for each step uses appropriate tolerance margins that account for legitimate computational differences (e.g., due to linear regression or integration methods). The step scores are combined by weight to compute the final reward, with the main thermodynamic function table and the third-law enthalpy values carrying the largest weight. The quality of your work determines the score; the verifier is designed to reward accurate reproduction of the underlying thermodynamic quantities, not to penalize minor implementation differences that fall within the expected reproducibility window.
