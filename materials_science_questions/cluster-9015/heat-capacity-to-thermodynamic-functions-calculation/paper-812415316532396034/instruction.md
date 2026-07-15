# Derive thermodynamic functions from high-temperature calorimetric enthalpy data

## Problem background
Plutonium carbides are candidate advanced nuclear fuels, and reliable high-temperature thermodynamic data are essential for reactor design and safety analyses. Experimental molar enthalpy data for the monocarbide (PuC0.82) and sesquicarbide (Pu2C2.98) have been measured by drop calorimetry up to 1500 K. The goal is to derive a complete set of thermodynamic functions — molar heat capacity, enthalpy increment, entropy, and Gibbs free energy — from these measurements. This task involves fitting the measured enthalpy increments to a constrained analytical expression and then integrating to produce tables of thermodynamic properties.

## Approach
The experimental molar enthalpy data for each compound, provided as a CSV, are fitted to a polynomial of the form:
  H°(T) − H°(298) = a + bT + cT^{2} + dT^{3} + e/T .
The fit minimizes the sum of squared percent errors while enforcing three boundary conditions at T = 298.15 K:
  - H°(298) − H°(298) = 0 ;
  - Cp(298) equals the known low-temperature value;
  - dCp/dT(298) equals the known low-temperature value.
These low-temperature boundary constants, taken from Hall et al., are:
  For PuC0.82: Cp(298) = 46.060 J K^{−1} mol^{−1}, dCp/dT(298) = 0.0426 J K^{−2} mol^{−1}.
  For Pu2C2.98: Cp(298) = 114.0 J K^{−1} mol^{−1}, dCp/dT(298) = 0.1268 J K^{−2} mol^{−1}.
Once the fitted coefficients are obtained, the heat capacity polynomial is derived by differentiation:
  Cp(T) = b + 2cT + 3dT^{2} − e/T^{2} .
Using the fitted enthalpy and heat capacity polynomials together with the standard entropy at 298.15 K (provided for each compound), the thermodynamic functions are computed at 100 K intervals from 300 to 1500 K:
  - Cp(T) directly from the Cp polynomial;
  - H°(T) − H°(298) from the enthalpy polynomial;
  - S°(T) = S°(298) + ∫_{298}^{T} (Cp/τ) dτ ;
  - −[G°(T) − H°(298)]/T = S°(T) − [H°(T) − H°(298)]/T .
The integration for entropy can be performed analytically or numerically. The results are saved as two CSV files, one per compound, with columns for temperature, Cp, enthalpy increment, entropy, and the Gibbs free energy function.

## Reproduction target
Given the experimental molar enthalpy data for plutonium monocarbide (PuC0.82, 12 points) and plutonium sesquicarbide (Pu2C2.98, 13 points) in the bundled CSV, and the boundary condition values stated above, perform the constrained fit for each compound, derive the respective heat capacity polynomials, and compute thermodynamic functions at T = 300, 400, 500, …, 1500 K. Produce two CSV files:
  - thermo_PuC082.csv: columns T(K), Cp(J/K/mol), H_H298(J/mol), S(J/K/mol), G_H298_div_T(J/K/mol);
  - thermo_Pu2C298.csv: same columns.
The csv files must follow the output contract’s column order and units.

## Assets

- Experimental enthalpy data for PuC0.82 and Pu2C2.98

## Workflow steps

### Step 1: Fit enthalpy polynomials and derive heat capacity functions
- Role: process
- Action: Load the experimental enthalpy data from the provided CSV. For each compound, perform a constrained least-squares fit to the model H°(T)-H°(298) = a + bT + cT^2 + dT^3 + e/T, minimizing the sum of squared percent errors, subject to boundary conditions at 298.15 K (zero enthalpy, Cp(298) and dCp/dT(298) from literature). Derive the heat capacity polynomial Cp(T) by differentiation. Save the fitted coefficients for later use.
- Evidence: `/app/outputs/fit_coefficients.json`

### Step 2: Compute PuC0.82 thermodynamic functions table
- Role: scored (load-bearing)
- Action: Using the fitted enthalpy and heat capacity polynomials for PuC0.82 and the given standard entropy S°(298) = 69.590 J/K/mol, compute Cp, enthalpy increment H°(T)-H°(298), entropy S°(T) (via integration of Cp/T from 298 K), and the Gibbs free energy function -(G°(T)-H°(298))/T at temperatures 300, 400, 500, …, 1500 K. Output the results as a CSV file.
- Output file: `/app/outputs/thermo_PuC082.csv`
- Format: csv
- Contract: Columns: T(K), Cp(J/K/mol), H_H298(J/mol), S(J/K/mol), G_H298_div_T(J/K/mol). Rows for T=300,400,...,1500 K.
- Scoring: scored by hidden verifier

### Step 3: Compute Pu2C2.98 thermodynamic functions table
- Role: scored (load-bearing)
- Action: Using the fitted enthalpy and heat capacity polynomials for Pu2C2.98 and the given standard entropy S°(298) = 150.0 J/K/mol, compute Cp, enthalpy increment H°(T)-H°(298), entropy S°(T), and the Gibbs free energy function -(G°(T)-H°(298))/T at temperatures 300, 400, 500, …, 1500 K. Output the results as a CSV file.
- Output file: `/app/outputs/thermo_Pu2C298.csv`
- Format: csv
- Contract: Columns: T(K), Cp(J/K/mol), H_H298(J/mol), S(J/K/mol), G_H298_div_T(J/K/mol). Rows for T=300,400,...,1500 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_PuC082.csv`
- `/app/outputs/thermo_Pu2C298.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_PuC082.csv
- path: `/app/outputs/thermo_PuC082.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Calculated thermodynamic functions for plutonium monocarbide PuC0.82 at 300–1500 K.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `Cp(J/K/mol)`, `H_H298(J/mol)`, `S(J/K/mol)`, `G_H298_div_T(J/K/mol)`
  - `units`:
    - `T(K)`: K
    - `Cp(J/K/mol)`: J/(K*mol)
    - `H_H298(J/mol)`: J/mol
    - `S(J/K/mol)`: J/(K*mol)
    - `G_H298_div_T(J/K/mol)`: J/(K*mol)

### thermo_Pu2C298.csv
- path: `/app/outputs/thermo_Pu2C298.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Calculated thermodynamic functions for plutonium sesquicarbide Pu2C2.98 at 300–1500 K.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `Cp(J/K/mol)`, `H_H298(J/mol)`, `S(J/K/mol)`, `G_H298_div_T(J/K/mol)`
  - `units`:
    - `T(K)`: K
    - `Cp(J/K/mol)`: J/(K*mol)
    - `H_H298(J/mol)`: J/mol
    - `S(J/K/mol)`: J/(K*mol)
    - `G_H298_div_T(J/K/mol)`: J/(K*mol)

Notes: The thermodynamic functions are computed from the fitted enthalpy polynomial and standard entropy at 298.15 K. The checker compares the values in these CSVs to the reference tables with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_PuC082.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "Cp(J/K/mol)",
          "H_H298(J/mol)",
          "S(J/K/mol)",
          "G_H298_div_T(J/K/mol)"
        ],
        "units": {
          "T(K)": "K",
          "Cp(J/K/mol)": "J/(K*mol)",
          "H_H298(J/mol)": "J/mol",
          "S(J/K/mol)": "J/(K*mol)",
          "G_H298_div_T(J/K/mol)": "J/(K*mol)"
        }
      },
      "description": "Calculated thermodynamic functions for plutonium monocarbide PuC0.82 at 300–1500 K."
    },
    {
      "file": "thermo_Pu2C298.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "Cp(J/K/mol)",
          "H_H298(J/mol)",
          "S(J/K/mol)",
          "G_H298_div_T(J/K/mol)"
        ],
        "units": {
          "T(K)": "K",
          "Cp(J/K/mol)": "J/(K*mol)",
          "H_H298(J/mol)": "J/mol",
          "S(J/K/mol)": "J/(K*mol)",
          "G_H298_div_T(J/K/mol)": "J/(K*mol)"
        }
      },
      "description": "Calculated thermodynamic functions for plutonium sesquicarbide Pu2C2.98 at 300–1500 K."
    }
  ],
  "notes": "The thermodynamic functions are computed from the fitted enthalpy polynomial and standard entropy at 298.15 K. The checker compares the values in these CSVs to the reference tables with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently scores each workflow step’s artifact. For the scored thermodynamic tables (Steps 2 and 3), the verifier loads your CSV files, compares the numerical values against the expected reference (derived from the same fitting procedure with the same inputs), and awards reward based on how many entries are within the required accuracy. Simply copying numbers from a published source is not sufficient — the verifier’s comparison uses tolerances appropriate for a correct re‑run of the described constrained fit and integration, so only a genuine computation will receive a high score. Reward from the two tables is combined to produce the final overall score.
