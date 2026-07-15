# Heat capacity to thermodynamic functions calculation

## Problem background
Nanoscale cobaltite–cuprate–manganite (LaSrCoCuMnO6) and nickelite–cuprate–manganite (LaSrNiCuMnO6) compounds were synthesized and their isobaric specific heat (Cp) was measured by dynamic calorimetry over the temperature range 298.15–673 K. From these experimental Cp data, the temperature dependences of entropy, enthalpy increment, and reduced Gibbs free energy can be derived through numerical integration. Your task is to compute these thermodynamic functions for both compounds.

## Approach
Load the experimental specific heat data (Cp values at multiple temperatures for both compounds) from the provided file `specific_heat_data.csv`. Use the standard entropy at 298.15 K as the integration constant: 262 J/(mol·K) for LaSrCoCuMnO6 and 253 J/(mol·K) for LaSrNiCuMnO6.

For each target temperature T (298.15, 300, 350, 400, 450, 500, 550, 600, 650, 675 K), compute:
- Entropy: S°(T) = S°(298.15) + ∫_{298.15}^{T} (Cp / T) dT
- Enthalpy increment: ΔH(T) = H°(T) – H°(298.15) = ∫_{298.15}^{T} Cp dT
- Reduced Gibbs potential: Φxx(T) = S°(T) – ΔH(T) / T

Perform the numerical integration over the discrete temperature grid using any suitable method (e.g., trapezoidal rule). The computed quantities should be reported in the units indicated in the output contract.

## Reproduction target
Given the specific heat data in `specific_heat_data.csv` and the standard entropy values above, compute S°(T) (in J/(mol·K)), H°(T)–H°(298.15 K) (in J/mol), and Φxx(T) (in J/(mol·K)) for LaSrCoCuMnO6 and LaSrNiCuMnO6 at T = 298.15, 300, 350, 400, 450, 500, 550, 600, 650, 675 K. Write the results to `thermodynamic_functions.csv` with columns: compound (LaSrCoCuMnO6 or LaSrNiCuMnO6), T (K), Cp (J/(mol·K)), S (J/(mol·K)), H_minus_H0 (J/mol), Phi (J/(mol·K)). One row per temperature per compound, ordered by compound then ascending T.

## Assets

- specific_heat_data.csv

## Workflow steps

### Step 1: Load specific heat data and standard entropy
- Role: process
- Action: Load the specific heat data from the provided CSV file (temperature and Cp values for both compounds) and store the standard entropy at 298.15 K: 262 J/(mol K) for LaSrCoCuMnO6, 253 J/(mol K) for LaSrNiCuMnO6.
- Evidence: none

### Step 2: Compute thermodynamic functions
- Role: scored (load-bearing)
- Action: From the loaded specific heat data and standard entropy, compute for each compound at T = 298.15, 300, 350, 400, 450, 500, 550, 600, 650, 675 K: (1) entropy S(T) by numerical integration of Cp/T, (2) enthalpy increment H(T)-H(298.15) by numerical integration of Cp, (3) reduced Gibbs potential Phi(T) = S(T) - [H(T)-H(298.15)]/T. Output the results to thermodynamic_functions.csv.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: CSV with columns: compound (LaSrCoCuMnO6 or LaSrNiCuMnO6), T (K), Cp (J/(mol K)), S (J/(mol K)), H_minus_H0 (J/mol), Phi (J/(mol K)). One row per temperature per compound, ordered by compound then ascending T.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of thermodynamic functions computed from specific heat data.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `T`, `Cp`, `S`, `H_minus_H0`, `Phi`
  - `units`:
    - `T`: K
    - `Cp`: J/(mol K)
    - `S`: J/(mol K)
    - `H_minus_H0`: J/mol
    - `Phi`: J/(mol K)

Notes: The agent must compute thermodynamic functions by numerical integration of the provided specific heat data and given standard entropy. The hidden checker compares computed S, H_minus_H0, and Phi values against the paper's reference with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "T",
          "Cp",
          "S",
          "H_minus_H0",
          "Phi"
        ],
        "units": {
          "T": "K",
          "Cp": "J/(mol K)",
          "S": "J/(mol K)",
          "H_minus_H0": "J/mol",
          "Phi": "J/(mol K)"
        }
      },
      "description": "Table of thermodynamic functions computed from specific heat data."
    }
  ],
  "notes": "The agent must compute thermodynamic functions by numerical integration of the provided specific heat data and given standard entropy. The hidden checker compares computed S, H_minus_H0, and Phi values against the paper's reference with tolerances."
}
```

## How you are scored
A hidden verifier will read your `thermodynamic_functions.csv` and extract the S, H_minus_H0, and Phi values for each compound and temperature. It will compare them to hidden reference values using a relative tolerance for each quantity. Your reward is proportional to the fraction of values that fall within the tolerance. You must compute the thermodynamic functions from the provided specific heat data; reporting numbers without genuine integration will not pass.
