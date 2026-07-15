# Classical Nucleation Rate Computation for Lithium Disilicate Glass

## Problem background
Classical nucleation theory (CNT) provides a framework for predicting the rate of homogeneous crystal nucleation from a supercooled melt. This task implements the Turnbull–Fisher form of CNT to compute the absolute homogeneous nucleation rate I (cm⁻³ s⁻¹) of Li₂O·2SiO₂ crystals as a function of temperature, using physically motivated material parameters. The computed rates are central to assessing the theory’s predictions for this glass-forming system.

## Approach
The nucleation rate I is computed using the Turnbull–Fisher expression I = K_v exp(-ΔG_A/kT) exp(-ΔG*/kT), where the thermodynamic barrier ΔG* depends on the interfacial free energy σ and the bulk free-energy difference ΔG_v. The pre-factor K_v is constructed from molecular parameters. The calculation uses an accurate polynomial expression for ΔG_v(T) derived from calorimetric data, a fixed interfacial energy σ, and an activation energy ΔG_A for molecular transport across the nucleus–matrix interface. All required constants are provided in the workflow steps. The computation first sets up all physical constants and the list of 20 temperatures (in °C). Then, for each temperature converted to Kelvin, it computes ΔG_v, the critical radius r*, the pre-factor K_v, and finally the nucleation rate I. The results are written into a CSV file.

## Reproduction target
Compute the homogeneous crystal nucleation rate I (cm⁻³ s⁻¹) at each of the following temperatures (in °C): 575.7, 562.6, 549.6, 536.7, 523.5, 510.4, 497.3, 484.3, 471.2, 458.2, 445.1, 432.0, 419.0, 405.9, 392.9, 379.8, 366.7, 353.7, 340.6, 327.6, using the Turnbull–Fisher equation with the parameters and formulas given in the workflow steps. Write the output to /app/outputs/nucleation_rates.csv, with columns Temperature_C and I (cm⁻³ s⁻¹), one row per temperature in the order listed.

## Assets

- Python 3 with NumPy

## Workflow steps

### Step 1: Define parameters and temperature list
- Role: process
- Action: Set all physical constants and parameters: σ = 201 erg cm⁻², ΔG_A/k = 5.25e4 K, N = 1.0e22 cm⁻³, ρ_c = 2.45 g cm⁻³, M = 150 g mol⁻¹, Avogadro's number A = 6.02214076e23 mol⁻¹, Boltzmann constant k = 1.380649e-16 erg K⁻¹, Planck constant h = 6.62607015e-27 erg s. Define the list of 20 temperatures in Celsius from 575.7 down to 327.6 (as given in Table 1 of the paper). Convert each to Kelvin: T_K = T_C + 273.15.
- Evidence: none

### Step 2: Compute IT1 nucleation rate and output CSV
- Role: scored (load-bearing)
- Action: For each temperature T (in Kelvin): (1) compute bulk free energy ΔG_v = (8790 - 6.53 * T) * 1e6 erg cm⁻³; (2) compute critical radius r* = -2σ / ΔG_v; (3) compute pre‑factor K_v = (8 N / (3 h)) * (k T σ)^(1/2) * (4 π ρ_c A / M)^(1/3) * r*^2; (4) compute nucleation rate I = K_v * exp(-ΔG_A/(k T)) * exp(-16π σ^3 / (3 ΔG_v^2 k T)). Write a CSV file with columns Temperature_C and I (cm⁻³ s⁻¹), one row per temperature in the same order as the input list.
- Output file: `/app/outputs/nucleation_rates.csv`
- Format: csv
- Contract: Columns: Temperature_C (float, Celsius), I (float, nucleation rate in cm⁻³ s⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleation_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleation_rates.csv
- path: `/app/outputs/nucleation_rates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nucleation rates computed with the IT1 model (absolute values, not log10). One row per temperature in the order 575.7 °C down to 327.6 °C.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_C`, `I`
  - `units`:
    - `Temperature_C`: °C
    - `I`: cm^{-3} s^{-1}

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleation_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_C",
          "I"
        ],
        "units": {
          "Temperature_C": "°C",
          "I": "cm^{-3} s^{-1}"
        }
      },
      "description": "Nucleation rates computed with the IT1 model (absolute values, not log10). One row per temperature in the order 575.7 °C down to 327.6 °C."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your /app/outputs/nucleation_rates.csv and compares each reported I value against reference values at the same temperatures. The final score is the fraction of temperatures for which the computed rate matches the reference within a pre‑defined tolerance. The verifier does not inspect your code or intermediate artifacts; only the final CSV is scored.
