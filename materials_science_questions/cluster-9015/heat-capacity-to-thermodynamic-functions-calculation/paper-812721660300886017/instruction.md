# Compute thermodynamic functions (H, S, G) of BAs from heat-capacity polynomial

## Problem background
Boron arsenide (BAs) has attracted significant interest for its ultrahigh thermal conductivity, making it a candidate for thermal management in electronics. Reliable thermodynamic data—enthalpy (H), entropy (S), and Gibbs free energy (G)—are critical for understanding the material’s stability and for optimizing synthesis processes. This task reproduces the computation of these thermodynamic functions from an experimentally measured heat capacity polynomial and accepted reference values at 298 K. The results describe the temperature-dependent behavior of BAs and identify the temperature at which its formation becomes endothermic.

## Approach
The core of the reproduction is a straightforward thermodynamic integration. The isobaric heat capacity Cp(T) is represented by a polynomial with known coefficients. Using standard integral relations, the enthalpy H(T) is computed as H_f(298) + ∫_{298}^{T} Cp dT, the entropy S(T) as S_f(298) + ∫_{298}^{T} (Cp/T) dT, and the Gibbs free energy as G(T) = H(T) - T·S(T). The integration can be performed analytically or numerically. The task then evaluates these functions over the temperature range 298–1150 K at 50 K increments, exports the results in a table, and locates the temperature where the enthalpy crosses zero.

## Reproduction target
Given the heat capacity polynomial coefficients and reference values (provided in Step 1), compute H(T), S(T), and G(T) for BAs across 298–1150 K in 50 K steps. Produce a CSV table of T(K), Cp(J/mol/K), S(J/mol/K), G(kJ/mol), H(kJ/mol). Determine the temperature (to the nearest integer) at which H(T) changes sign from negative to positive (the zero-enthalpy crossing).

## Assets
Python packages: numpy, scipy, pandas (standard scientific Python stack). No external datasets or models are required; all necessary coefficients and reference values are given in the workflow steps.

## Workflow steps

### Step 1: Compute enthalpy, entropy, and Gibbs free energy from Cp polynomial
- Role: process
- Action: Define the heat-capacity polynomial Cp(T)=aT^2 + bT + cT^{-0.5} + d with coefficients a=2.65e-5 J mol^{-1} K^{-3}, b=-7.24e-2 J mol^{-1} K^{-2}, c=-1.59e3 J mol^{-1} K^{-0.5}, d=1.43e2 J mol^{-1} K^{-1}. Compute H(T)=H_f(298) + ∫_{298}^{T} Cp dT, S(T)=S_f(298) + ∫_{298}^{T} (Cp/T) dT, G(T)=H(T)-T·S(T) for temperatures 298–1150 K. Use reference values H_f(298 K) = -30 kJ/mol, S_f(298 K) = 40 J mol^{-1} K^{-1}. Ensure proper unit conversions (Cp, S in J mol^{-1} K^{-1}; H, G in kJ mol^{-1}).
- Evidence: `/app/outputs/integration_output.npy`

### Step 2: Export thermodynamic functions table as CSV
- Role: scored
- Action: Write a CSV file with columns T(K), Cp(J/mol/K), S(J/mol/K), G(kJ/mol), H(kJ/mol) for temperatures from 298 K to 1150 K in 50 K increments (or finer). Include the computed values from the integration step.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: Columns: T(K), Cp(J/mol/K), S(J/mol/K), G(kJ/mol), H(kJ/mol). One row per temperature.
- Scoring: scored by hidden verifier

### Step 3: Determine zero enthalpy crossing temperature
- Role: scored (load-bearing)
- Action: Using the computed H(T) values, locate the temperature at which H(T) crosses zero (changes sign from negative to positive) by linear interpolation between the two bounding temperatures. Output the temperature rounded to the nearest integer (K).
- Output file: `/app/outputs/zero_crossing.txt`
- Format: txt
- Contract: A single integer representing temperature in Kelvin.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions.csv`
- `/app/outputs/zero_crossing.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file of Cp, S, G, H vs. temperature (298–1150 K in 50 K increments) computed from the Cp polynomial.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `Cp(J/mol/K)`, `S(J/mol/K)`, `G(kJ/mol)`, `H(kJ/mol)`
  - `units`:
    - `T(K)`: K
    - `Cp(J/mol/K)`: J mol^{-1} K^{-1}
    - `S(J/mol/K)`: J mol^{-1} K^{-1}
    - `G(kJ/mol)`: kJ mol^{-1}
    - `H(kJ/mol)`: kJ mol^{-1}

### zero_crossing.txt
- path: `/app/outputs/zero_crossing.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Temperature (K) where the computed enthalpy H(T) crosses zero, rounded to the nearest integer.
- schema:
  - `type`: text
  - `content`: integer
  - `unit`: K

Notes: The checker recomputes the thermodynamic functions from the supplied Cp polynomial and reference values; it compares the CSV pointwise within tolerances and verifies the zero-crossing temperature against the paper-reported value of 984 K within ±2 K. The integration step is mandatory because the zero-crossing depends on the computed H(T) values.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "Cp(J/mol/K)",
          "S(J/mol/K)",
          "G(kJ/mol)",
          "H(kJ/mol)"
        ],
        "units": {
          "T(K)": "K",
          "Cp(J/mol/K)": "J mol^{-1} K^{-1}",
          "S(J/mol/K)": "J mol^{-1} K^{-1}",
          "G(kJ/mol)": "kJ mol^{-1}",
          "H(kJ/mol)": "kJ mol^{-1}"
        }
      },
      "description": "CSV file of Cp, S, G, H vs. temperature (298–1150 K in 50 K increments) computed from the Cp polynomial."
    },
    {
      "file": "zero_crossing.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "integer",
        "unit": "K"
      },
      "description": "Temperature (K) where the computed enthalpy H(T) crosses zero, rounded to the nearest integer."
    }
  ],
  "notes": "The checker recomputes the thermodynamic functions from the supplied Cp polynomial and reference values; it compares the CSV pointwise within tolerances and verifies the zero-crossing temperature against the paper-reported value of 984 K within ±2 K. The integration step is mandatory because the zero-crossing depends on the computed H(T) values."
}
```

## How you are scored
A hidden verifier independently integrates the same Cp polynomial and reference values to obtain gold-standard thermodynamic functions. The verifier compares your CSV values for H, S, and G at specific temperatures using pre-defined tolerances (relative for H and G, absolute for S). The zero-crossing temperature is compared to a hidden reference within an absolute tolerance. The final score combines these two artifacts with appropriate weights. Simply reporting paper-lookup numbers is not sufficient; the verifier recomputes from the supplied coefficients.
