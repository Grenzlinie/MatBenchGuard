# Thermodynamic Equilibrium Gas-Phase Composition of the NbO2/TeCl4 System at 1 atm

## Problem background
In the Nb-O-Te-Cl system at high temperatures, chemical transport of niobium oxides occurs via gaseous species. Predicting which gaseous species dominate and carry oxygen is essential for understanding and controlling the transport process. This task addresses the equilibrium gas-phase composition over solid NbO2 at total pressure 1 atm and a Cl/Te balance ratio of 4. Using publicly available thermochemical data and phase-boundary oxygen pressures, the calculation determines the partial pressures of all relevant gaseous species as functions of temperature, revealing the dominant species and the main oxygen carrier.

## Approach
The gas-phase composition is obtained by solving a closed system of nonlinear equations derived from mass-action laws. First, standard enthalpy (ΔH_1000) and entropy (S_1000) values for all gaseous and solid species are compiled. From these, the reaction enthalpy and entropy for a set of ten independent gas-phase equilibria linking the species are computed, and temperature-dependent equilibrium constants are formed via the relation lg K = ΔS/(4.574) – ΔH/(4.574·T). The oxygen partial pressure pO2 is fixed by the coexisting solid oxide pair according to the given log pO2(T) formulas for the upper and lower NbO2 phase boundaries. Combined with the total pressure constraint (Σ p_i = 1 atm) and the chlorine/tellurium balance ratio (p_Cl*/p_Te* = 4), this defines a system of equations that is solved numerically at each temperature to yield the partial pressures of all 13 gaseous species: NbOCl3, NbCl4, NbCl5, TeOCl2, TeCl2, TeCl4, TeO2, TeO, Te2, Te, Cl2, Cl, O2.

## Reproduction target
Compute the equilibrium partial pressures of the 13 gaseous species listed above at temperatures spanning 1000 K to 1500 K (in steps of 50 K or 100 K) for both the upper phase boundary (NbO2.417/NbO2) and the lower phase boundary (NbO2/NbO). All calculations are performed at a total pressure of 1 atm and a Cl/Te balance ratio of 4. The final output must be a CSV file (`gas_composition.csv`) with columns T (integer K), species (string), p (float, atm), and boundary (`upper` or `lower`). The verification will check that the reported partial pressures agree with the values recomputed from the same thermochemical data and constraints within an acceptable tolerance, and that the dominant gaseous species are correctly identified across the temperature range.

## Assets

- Thermochemical data for all gaseous and solid species (ΔH_1000, S_1000)
- Oxygen coexistence pressure equations for NbOx boundaries
- Python numerical solver (scipy, numpy): scipy

## Workflow steps

### Step 1: Compile thermochemical data
- Role: process
- Action: Extract the enthalpy (ΔH_1000) and entropy (S_1000) values for the 14 gaseous species and 2 solid oxides (NbO2, NbO2.5) from Table 1 in the problem description. Store them in a structured format (e.g., JSON or Python dictionary) for later use.
- Evidence: `/app/outputs/thermochem_data.json`

### Step 2: Calculate equilibrium constants
- Role: process
- Action: Using the compiled thermochemical data, compute the reaction enthalpy ΔH_R and entropy ΔS_R for each of the 10 independent gas-phase reactions (1)–(10) at 1000 K. Then compute the equilibrium constant K(T) via the formula lg K = ΔS/(4.574) − ΔH/(4.574 T) for each temperature in the range of interest (1000–1500 K, e.g., every 50 or 100 K).
- Evidence: `/app/outputs/equilibrium_constants.csv`

### Step 3: Derive oxygen coexistence pressures
- Role: process
- Action: Compute the oxygen partial pressure pO2 as a function of temperature using the given equations: log pO2 = 11.5965 − 37452/T for the NbO2 upper phase boundary (NbO2.417/NbO2) and log pO2 = 10.1624 − 38951/T for the NbO2 lower phase boundary (NbO2/NbO). Produce a table of T and pO2 for the two boundaries.
- Evidence: `/app/outputs/pO2_values.csv`

### Step 4: Solve equilibrium gas-phase composition
- Role: scored (load-bearing)
- Action: For temperatures from 1000 K to 1500 K (e.g., every 50 or 100 K) and for each of the two phase boundaries, set up the system of 10 mass-action equations from the equilibrium constants, along with total pressure constraint Σ p_i = 1 atm, chlorine/tellurium balance ratio p_Cl*/p_Te* = 4, and the oxygen partial pressure from the previous step. Solve numerically for the 13 unknown partial pressures of the gaseous species: NbOCl3, NbCl4, NbCl5, TeOCl2, TeCl2, TeCl4, TeO2, TeO, Te2, Te, Cl2, Cl, O2. Output a CSV file with columns: T (K, integer), species (string), p (float, atm), boundary (string, either 'upper' or 'lower').
- Output file: `/app/outputs/gas_composition.csv`
- Format: csv
- Contract: CSV with header: T,species,p,boundary. T integer in K; species one of: NbOCl3,NbCl4,NbCl5,TeOCl2,TeCl2,TeCl4,TeO2,TeO,Te2,Te,Cl2,Cl,O2; p float in atm; boundary either 'upper' or 'lower'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gas_composition.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gas_composition.csv
- path: `/app/outputs/gas_composition.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium partial pressures of 13 gaseous species as a function of temperature for the upper and lower phase boundaries of NbO2 at total pressure 1 atm and Cl/Te balance ratio 4. The checker recomputes the expected pressures from the same public thermochemical data and constraints at hidden test temperatures, then compares them using relative errors.
- schema:
  - `type`: table
  - `required_columns`: `T`, `species`, `p`, `boundary`
  - `units`:
    - `T`: K
    - `p`: atm

Notes: The task requires solving a nonlinear system of mass-action equations with 10 reactions. The dominant species verification is part of the scoring. No hidden gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gas_composition.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "species",
          "p",
          "boundary"
        ],
        "units": {
          "T": "K",
          "p": "atm"
        }
      },
      "description": "Equilibrium partial pressures of 13 gaseous species as a function of temperature for the upper and lower phase boundaries of NbO2 at total pressure 1 atm and Cl/Te balance ratio 4. The checker recomputes the expected pressures from the same public thermochemical data and constraints at hidden test temperatures, then compares them using relative errors."
    }
  ],
  "notes": "The task requires solving a nonlinear system of mass-action equations with 10 reactions. The dominant species verification is part of the scoring. No hidden gold values or tolerances are disclosed here."
}
```

## How you are scored
An automated verifier runs after the task finishes. It recomputes the expected equilibrium partial pressures at a set of hidden validation temperatures (covering the same range and both boundaries) using the identical thermochemical data, oxygen coexistence equations, and mass-action constraints that you were provided. It compares your submitted pressures for each species using relative error metrics, and it checks that the species with the highest pressure matches the expected dominant species. The final reward is a weighted combination of these checks; producing the complete, correct `gas_composition.csv` artifact is required. The verifier accounts for numerical differences that naturally arise from different solver implementations by applying generous but physically motivated tolerances, so a correct computational reproduction earns full credit.
