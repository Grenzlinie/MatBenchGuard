# Compute thermodynamic functions from heat capacity data using numerical integration

## Problem background
Thermophysical characterization of metal alkanoates provides fundamental thermodynamic data for understanding phase transitions and structural disorder. The heat capacity of potassium 2‑methylpropanoate has been measured by adiabatic calorimetry from 8 to 350 K. From these experimental heat capacities, the standard molar thermodynamic functions — heat capacity, entropy, enthalpy increment, and Gibbs free energy function — can be derived. The goal is to compute these functions at a set of prescribed temperatures by numerically integrating the provided experimental data.

## Approach
The raw experimental heat capacities (given as Cp/R vs. temperature) are first smoothed into a continuous curve. For temperatures below the lowest measured point (8 K), the heat capacity is extrapolated to 0 K using a T³ law, appropriate for lattice vibrations at very low temperatures. Numerical integration by the trapezoidal rule is then performed from 0 K to each target temperature to obtain the enthalpy increment H(T)–H(0) and the entropy S(T)–S(0). The Gibbs free energy function –[G(T)–H(0)]/(RT) is derived from the entropy and enthalpy values via the thermodynamic identity. The integration uses a fine temperature grid generated from the smoothed Cp curve.

## Reproduction target
Compute the smoothed Cp/R, S(T)–S(0)/R, {H(T)–H(0)}/R (in K), and –{G(T)–H(0)}/(RT) at the following temperatures: 0, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 298.15, 300, 320, 350 K. Output the results as a TSV file with columns T, Cp_over_R, S_over_R, H_over_RK, G_over_RT. All values are dimensionless except H_over_RK which is in kelvin.

## Assets

- Experimental molar heat capacity data (Table 1)
- NumPy: numpy
- SciPy: scipy
- pandas: pandas

## Workflow steps

### Step 1: Parse raw heat capacity data
- Role: process
- Action: Extract the raw molar heat capacity data (temperature in K, Cp/R dimensionless) from the provided table (Table 1 in the instruction) and write to a CSV file named 'raw_cp.csv'. Include columns T_K and Cp_over_R. Use all data points from the three series.
- Evidence: `/app/outputs/raw_cp.csv`

### Step 2: Compute thermodynamic functions
- Role: scored (load-bearing)
- Action: Smooth the raw heat capacity data, extrapolate to 0 K with a T³ law using the lowest temperature points, perform numerical integration (trapezoidal rule) to obtain the enthalpy increment H(T)–H(0) and entropy S(T)–S(0), and derive the Gibbs free energy function –[G(T)–H(0)]/(RT). Output a TSV file with columns T, Cp_over_R (smoothed), S_over_R, H_over_RK, G_over_RT at every temperature from the list: 0, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 298.15, 300, 320, 350. Cp, S, G are dimensionless; H is in K.
- Output file: `/app/outputs/thermodynamic_functions.tsv`
- Format: tsv
- Contract: TSV file with header: T, Cp_over_R, S_over_R, H_over_RK, G_over_RT. T is in K (float), Cp_over_R and S_over_R and G_over_RT are dimensionless (float), H_over_RK is in K (float). One row per temperature from the specified list.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.tsv
- path: `/app/outputs/thermodynamic_functions.tsv`
- format: tsv
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic functions computed from raw heat capacity data. Checker compares values row by row against hidden reference data (paper's Table 2) using relative tolerance 1 % for values ≥1.0 and absolute tolerance 0.01 for values <1.0.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp_over_R`, `S_over_R`, `H_over_RK`, `G_over_RT`
  - `units`:
    - `T`: K
    - `Cp_over_R`: dimensionless
    - `S_over_R`: dimensionless
    - `H_over_RK`: K
    - `G_over_RT`: dimensionless

Notes: The agent must compute these functions by smoothing and numerical integration of the provided raw heat capacity data. Temperatures in the output must exactly match the required list (including 0 K and 298.15 K). Values should be given to at least 3 decimal places for Cp, S, G; 1 decimal for H.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Cp_over_R",
          "S_over_R",
          "H_over_RK",
          "G_over_RT"
        ],
        "units": {
          "T": "K",
          "Cp_over_R": "dimensionless",
          "S_over_R": "dimensionless",
          "H_over_RK": "K",
          "G_over_RT": "dimensionless"
        }
      },
      "description": "Thermodynamic functions computed from raw heat capacity data. Checker compares values row by row against hidden reference data (paper's Table 2) using relative tolerance 1 % for values ≥1.0 and absolute tolerance 0.01 for values <1.0."
    }
  ],
  "notes": "The agent must compute these functions by smoothing and numerical integration of the provided raw heat capacity data. Temperatures in the output must exactly match the required list (including 0 K and 298.15 K). Values should be given to at least 3 decimal places for Cp, S, G; 1 decimal for H."
}
```

## How you are scored
A hidden verifier will read your 'thermodynamic_functions.tsv' and compare each computed column (Cp_over_R, S_over_R, H_over_RK, G_over_RT) against reference values at the same temperatures. The comparison uses tolerances that allow for legitimate differences due to smoothing and numerical integration. The final reward is the fraction of the required temperatures for which all four functions fall within the allowed tolerances. To earn full credit, you must correctly implement the smoothing, extrapolation, and integration described above; simply reporting values from the literature will not pass the hidden comparison.
