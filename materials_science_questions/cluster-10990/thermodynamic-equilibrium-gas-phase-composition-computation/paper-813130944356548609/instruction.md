# Equilibrium composition of diatomite plasma processing system

## Problem background
This task investigates the plasma-assisted production of nanodisperse silica (SiO₂) powder from natural diatomite, a high-silica raw material. The plasma process operates at a total pressure of 0.1 MPa, using a mixture of 10 wt% raw material and 90 wt% air, over the wide temperature range 300–5000 K. Thermodynamic equilibrium modeling is employed to predict which condensed and gaseous species form under these conditions, with the practical goal of identifying a temperature window where SiO₂ sublimates into the gas phase while Al₂O₃ remains condensed, thereby ensuring a high-purity SiO₂ nanopowder product.

## Approach
The core computational approach is a Gibbs free energy minimization at constant pressure. The input mixture is derived from the diatomite oxide composition (mass percentages provided in the workflow) combined with air (molar composition N₂:O₂ = 79:21) to achieve the specified overall mass fraction of raw material. Using an open-source equilibrium solver (such as Cantera), the equilibrium mass fractions of all species are computed as a function of temperature from 300 K to 5000 K with a step no larger than 50 K. The key condensed phases tracked are SiO₂, Al₂O₃, Fe₂O₃, and Fe₃O₄, while the gaseous species include SiO₂ and AlO. The resulting mass-fraction grid is the basis for extracting phase‑transition temperatures and species‑presence criteria downstream.

## Reproduction target
Produce a CSV file (`equilibrium_composition.csv`) that contains the equilibrium mass fractions of the required species at every sampled temperature between 300 K and 5000 K. The file must include columns for temperature_K and for the mass fractions of condensed SiO₂(s), Al₂O₃(s), Fe₂O₃(s), Fe₃O₄(s), and gaseous SiO₂(g), AlO(g). Additional species may be included but are not required. The hidden verifier will read this CSV, extract several key quantities using a deterministic procedure — specifically, the temperature at which condensed SiO₂ disappears, the temperature at which condensed Al₂O₃ disappears, the dominant iron‑containing condensed phase above 2000 K, and whether gaseous SiO₂ and AlO are present above 3000 K — and compare them to reference criteria. The CSV itself must be the output of a genuine equilibrium simulation; an incomplete or fabricated grid will not pass verification.

## Assets

- Cantera chemical thermodynamics package: cantera
- Burcat thermodynamic database: https://burcat.technion.ac.il/

## Workflow steps

### Step 1: Prepare feed composition and conditions
- Role: process
- Action: Convert the diatomite weight percentages (SiO2 80.40, Al2O3 7.27, Fe2O3 4.41, CaO 1.27, MgO 1.64, K2O 1.21, Na2O 0.32 wt%; ignition loss 3.48% may be omitted) into elemental mole or mass amounts. Combine with air (79% N2, 21% O2 by mole) to form an overall mixture of 10 wt% raw material and 90 wt% air. Set total pressure to 0.1 MPa and define a temperature sweep from 300 to 5000 K with a maximum step of 50 K.
- Evidence: `/app/outputs/input_summary.json`

### Step 2: Run Gibbs energy minimization simulation
- Role: process
- Action: Using Cantera (or an equivalent open-source equilibrium solver), compute the equilibrium chemical composition (mass fractions) of all species (condensed and gaseous) for the mixture at constant pressure 0.1 MPa, scanning temperature from 300 K to 5000 K with a step of no more than 50 K. Include at least the condensed species SiO2(s), Al2O3(s), Fe2O3(s), Fe3O4(s) and gaseous species SiO2(g), AlO(g), together with other relevant phases.
- Evidence: `/app/outputs/raw_equilibrium_data.npy`

### Step 3: Write equilibrium composition data as CSV
- Role: scored (load-bearing)
- Action: Save the computed equilibrium mass fractions to a CSV file. For every sampled temperature, output the temperature (K) and the mass fraction of each required species: condensed SiO2(s), Al2O3(s), Fe2O3(s), Fe3O4(s), and gaseous SiO2(g), AlO(g). Additional species may be included but are optional.
- Output file: `/app/outputs/equilibrium_composition.csv`
- Format: csv
- Contract: CSV with header row. Required columns (case-sensitive): temperature_K (float), SiO2(s) (float), Al2O3(s) (float), Fe2O3(s) (float), Fe3O4(s) (float), SiO2(g) (float), AlO(g) (float). Additional columns are allowed. Mass fractions should sum approximately to 1 at each row.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_composition.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_composition.csv
- path: `/app/outputs/equilibrium_composition.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium mass fraction grid vs. temperature. The verifier recomputes the paper's key phase transition temperatures (condensed SiO2 disappearance, Al2O3 disappearance), identifies the dominant iron condensed phase above 2000 K, and checks presence of gaseous SiO2 and AlO above 3000 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `SiO2(s)`, `Al2O3(s)`, `Fe2O3(s)`, `Fe3O4(s)`, `SiO2(g)`, `AlO(g)`
  - `units`:
    - `temperature_K`: K
    - `SiO2(s)`: mass fraction (dimensionless)
    - `Al2O3(s)`: mass fraction (dimensionless)
    - `Fe2O3(s)`: mass fraction (dimensionless)
    - `Fe3O4(s)`: mass fraction (dimensionless)
    - `SiO2(g)`: mass fraction (dimensionless)
    - `AlO(g)`: mass fraction (dimensionless)

Notes: Only the CSV file is scored. The process evidence files (input_summary.json, raw_equilibrium_data.npy) are not checked. Ignition loss (3.48%) may be excluded or interpreted by the agent; the scoring criteria are robust to that choice.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_composition.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "SiO2(s)",
          "Al2O3(s)",
          "Fe2O3(s)",
          "Fe3O4(s)",
          "SiO2(g)",
          "AlO(g)"
        ],
        "units": {
          "temperature_K": "K",
          "SiO2(s)": "mass fraction (dimensionless)",
          "Al2O3(s)": "mass fraction (dimensionless)",
          "Fe2O3(s)": "mass fraction (dimensionless)",
          "Fe3O4(s)": "mass fraction (dimensionless)",
          "SiO2(g)": "mass fraction (dimensionless)",
          "AlO(g)": "mass fraction (dimensionless)"
        }
      },
      "description": "Equilibrium mass fraction grid vs. temperature. The verifier recomputes the paper's key phase transition temperatures (condensed SiO2 disappearance, Al2O3 disappearance), identifies the dominant iron condensed phase above 2000 K, and checks presence of gaseous SiO2 and AlO above 3000 K."
    }
  ],
  "notes": "Only the CSV file is scored. The process evidence files (input_summary.json, raw_equilibrium_data.npy) are not checked. Ignition loss (3.48%) may be excluded or interpreted by the agent; the scoring criteria are robust to that choice."
}
```

## How you are scored
A hidden verifier reads your `equilibrium_composition.csv` and extracts the following quantities using a fixed, deterministic procedure: (a) the temperature at which the condensed SiO₂ mass fraction drops below a threshold relative to its maximum value, (b) the temperature at which condensed Al₂O₃ mass fraction drops below the same threshold, (c) the condensed iron phase with the largest mass fraction at temperatures above 2000 K, and (d) whether gaseous SiO₂ and AlO exhibit non‑zero mass fractions (above a small epsilon) at temperatures above 3000 K. These extracted values are compared against hidden reference criteria derived from the original study. The final reward is a weighted sum of the matches; each criterion that is satisfied contributes a fraction of the total reward. You must execute the full equilibrium simulation to produce a CSV that faithfully reflects the correct phase behavior; reporting the paper's stated numbers without the supporting grid will not yield a correct artifact and will fail verification.
