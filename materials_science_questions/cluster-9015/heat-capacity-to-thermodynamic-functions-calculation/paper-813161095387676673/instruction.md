# Heat capacity to enthalpy and entropy increments

## Problem background
Certain oxide compounds in the rare‑earth–copper–oxide family are of interest for understanding high‑temperature superconductivity. The compound Tm₂Cu₂O₅ is one of the least studied members. Reliable thermodynamic data, particularly the temperature dependence of the molar heat capacity and the derived enthalpy and entropy increments, are essential for phase stability calculations and for optimizing synthesis conditions. This task focuses on computing those derived thermodynamic functions from experimentally measured heat capacity data.

## Approach
The core idea is to start from a table of experimental molar heat capacity Cp values of Tm₂Cu₂O₅ measured at a series of temperatures. The enthalpy increment H_T⁰ − H_431⁰ and the entropy increment S_T⁰ − S_431⁰ are obtained by integrating the heat capacity with respect to temperature: H = ∫Cp dT and S = ∫(Cp/T) dT, with 431 K as the reference temperature. Two integration strategies are possible: (1) direct numerical integration using, for example, the trapezoidal rule on the provided discrete Cp data; (2) fitting the Maier–Kelley equation Cp = a + bT + cT⁻² to the data and integrating the resulting analytical expression. Both approaches yield comparable results and are acceptable. The required output is a table of temperatures, the corresponding Cp values, and the computed H and S increments at selected temperatures from 450 K to 1000 K.

## Reproduction target
From the provided input file `Cp_input.csv` (which lists temperature in K and molar heat capacity Cp in J mol⁻¹ K⁻¹ for Tm₂Cu₂O₅), compute the thermodynamic functions at the following target temperatures: 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, and 1000 K. For each temperature T, calculate:
- H: the enthalpy increment H_T⁰ − H_431⁰, expressed in kJ mol⁻¹,
- S: the entropy increment S_T⁰ − S_431⁰, expressed in J mol⁻¹ K⁻¹.
Output the results as a CSV file with the columns `T`, `Cp`, `H`, `S`. The `Cp` column should reproduce the measured values from the input file (the values may be taken directly from `Cp_input.csv`). The `H` and `S` columns must be obtained by numerical integration or by fitting and analytic integration as described in the Approach section. All numeric values must use a period as the decimal separator.

## Assets

- Cp_input.csv
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute thermodynamic functions
- Role: scored (load-bearing)
- Action: Read the provided Cp data from Cp_input.csv. For each temperature T in [450, 500, ..., 1000] K, compute the enthalpy increment H_T^0 - H_431^0 (kJ/mol) and entropy increment S_T^0 - S_431^0 (J/mol·K) by numerical integration of Cp (e.g., trapezoidal rule) from 431 K to T. Alternatively, fit the Maier–Kelley equation Cp = a + bT + cT^{-2} to the data and integrate analytically. Output the results as a CSV file with columns T (K), Cp (J/mol·K), H (kJ/mol), S (J/mol·K).
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: CSV with header row: T (K), Cp (J/mol·K), H (kJ/mol), S (J/mol·K). All columns are numeric; decimal separator is a period.
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
- target_policy: reference_match
- description: The table of thermodynamic properties: temperature, heat capacity, and the calculated enthalpy and entropy increments. The H and S columns are compared to hidden reference values from the original publication within specified tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp`, `H`, `S`
  - `units`:
    - `T`: K
    - `Cp`: J/(mol K)
    - `H`: kJ/mol
    - `S`: J/(mol K)

Notes: The agent may choose either direct numerical integration or a fitted Maier–Kelley equation; tolerances accommodate both. Only the H and S columns are scored.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Cp",
          "H",
          "S"
        ],
        "units": {
          "T": "K",
          "Cp": "J/(mol K)",
          "H": "kJ/mol",
          "S": "J/(mol K)"
        }
      },
      "description": "The table of thermodynamic properties: temperature, heat capacity, and the calculated enthalpy and entropy increments. The H and S columns are compared to hidden reference values from the original publication within specified tolerances."
    }
  ],
  "notes": "The agent may choose either direct numerical integration or a fitted Maier–Kelley equation; tolerances accommodate both. Only the H and S columns are scored."
}
```

## How you are scored
After you produce `thermodynamic_functions.csv`, a hidden verifier will read your file and evaluate it automatically. The verifier checks two aspects:
1. **Correct input usage:** For each temperature, your reported Cp value must agree with the corresponding value in the supplied `Cp_input.csv` (within a small tolerance) to confirm that the original experimental data were used.
2. **Physical result accuracy:** The verifier compares your computed H and S values at each target temperature to independently derived reference values. A point is awarded for each temperature where both H and S lie within the allowed error margins.
Your total reward is the fraction of the 12 temperature points that pass both checks. The verifier does not require any network access; it runs on the submitted file alone. No additional artefacts or textual explanations are scored.
