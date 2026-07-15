# Equilibrium Gas-phase Composition of Aspen Wood Gasification via Free Energy Minimization

## Problem background
Gasification of biomass at 600–800 °C can produce a clean gaseous fuel for combustion after removal of solid by-products, thereby avoiding the fouling and corrosion often caused by molten salts during direct combustion. The equilibrium gas composition determines the fuel quality and the fate of inorganic species, but it depends sensitively on feedstock elemental composition, temperature, pressure, and the amount of added water. For aspen wood, a representative low‑silica biomass, the main challenge is to predict the yields of the major gaseous species (H₂, CO, H₂O, CO₂, CH₄, N₂, H₂S) at three temperatures and three water‑to‑wood ratios, using a free‑energy minimization approach. Your task is to compute these equilibrium gas compositions, which are the basis for evaluating whether a molten salt phase can form at gasification conditions.

## Approach
The calculation performs multiphase Gibbs free energy minimization at constant temperature and pressure. The system is defined by the elemental composition of aspen wood (given below as weight percentages) and the water added according to the specified ratios. A feedstock mass of 100 g of wood is used. You will use the open‑source chemical equilibrium solver Cantera, coupled with a suitable thermodynamic database (the Burcat database is recommended) that includes gas‑phase and condensed species for all elements present. For each of the nine combinations of temperature (600, 700, 800 °C) and water/wood weight ratio (0.5/1, 0.75/1, 1/1) at a total pressure of 3 atm, you set up the elemental amounts, let the solver find the equilibrium state, and extract the total moles of gaseous products and the mole fractions of the seven listed species. The results are reported in a single CSV file. The elemental composition to use is (weight percent): C 51.57, H 6.27, N 0.47, O 39.52, P 0.0085, S 0.02504, K 0.0810, Ca 0.1524, Mg 0.0256, Al 0.001008, Fe 0.001872, B 0.00036, Mn 0.001008.

## Reproduction target
For 100 g of aspen wood with the given elemental composition, compute the equilibrium gas composition at 3 atm for all nine combinations of temperature (600 °C, 700 °C, 800 °C) and water/wood weight ratio (0.5/1, 0.75/1, 1/1). Report the total moles of gaseous products and the mole fractions of H₂, CO, H₂O, CO₂, CH₄, N₂, and H₂S. Output the results as a CSV file with columns: Temperature (integer, °C), WaterWoodRatio (string, e.g., '0.5/1'), TotalMoles (float), H2, CO, H2O, CO2, CH4, N2, H2S (all floats). One row per condition. The solver must account for the possible formation of solid and liquid phases, which sequester some elements and affect the gas composition.

## Assets

- Cantera chemical equilibrium toolkit: cantera
- Burcat thermodynamic database: https://github.com/Burcat/thermo

## Workflow steps

### Step 1: Define system inputs
- Role: process
- Action: Create a JSON file (inputs.json) containing the aspen wood elemental composition (exact mass fractions as given in the problem statement), the gasification conditions (temperatures 600, 700, 800 °C, total pressure 3 atm, water/wood weight ratios 0.5/1, 0.75/1, 1/1), and a feedstock mass of 100 g. This file serves as the structured input for the equilibrium computation.
- Evidence: `/app/outputs/inputs.json`

### Step 2: Compute equilibrium gas composition
- Role: scored (load-bearing)
- Action: Using an open-source chemical equilibrium solver (e.g., Cantera) with a suitable thermodynamic database that includes gas-phase and condensed species for all elements present, perform Gibbs free energy minimization for each of the nine condition combinations (temperature and water/wood ratio). Extract the total moles of gaseous product and the mole fractions of H2, CO, H2O, CO2, CH4, N2, and H2S. Write the results to gas_composition.csv.
- Output file: `/app/outputs/gas_composition.csv`
- Format: csv
- Contract: CSV with columns: Temperature (integer, °C), WaterWoodRatio (string, e.g., '0.5/1'), TotalMoles (float), H2 (float), CO (float), H2O (float), CO2 (float), CH4 (float), N2 (float), H2S (float). One row per condition.
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
- target_policy: threshold_or_better
- description: Equilibrium gas composition and liquid phase presence for aspen wood gasification at nine condition combinations. The checker compares the TotalMoles and species mole fractions against the paper's reported values using tolerances, and the LiquidPresent boolean against the paper's finding (no liquid at 600°C/700°C; presence at 800°C for the 0.75/1 ratio).
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `WaterWoodRatio`, `TotalMoles`, `H2`, `CO`, `H2O`, `CO2`, `CH4`, `N2`, `H2S`, `LiquidPresent`
  - `units`:
    - `Temperature`: °C
    - `TotalMoles`: moles per 100 g wood
    - `H2`: mole fraction
    - `CO`: mole fraction
    - `H2O`: mole fraction
    - `CO2`: mole fraction
    - `CH4`: mole fraction
    - `N2`: mole fraction
    - `H2S`: mole fraction
    - `LiquidPresent`: boolean

Notes: Liquid phase presence is merged into gas_composition.csv instead of a separate artifact, avoiding the need for an additional solve block.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "WaterWoodRatio",
          "TotalMoles",
          "H2",
          "CO",
          "H2O",
          "CO2",
          "CH4",
          "N2",
          "H2S",
          "LiquidPresent"
        ],
        "units": {
          "Temperature": "°C",
          "TotalMoles": "moles per 100 g wood",
          "H2": "mole fraction",
          "CO": "mole fraction",
          "H2O": "mole fraction",
          "CO2": "mole fraction",
          "CH4": "mole fraction",
          "N2": "mole fraction",
          "H2S": "mole fraction",
          "LiquidPresent": "boolean"
        }
      },
      "description": "Equilibrium gas composition and liquid phase presence for aspen wood gasification at nine condition combinations. The checker compares the TotalMoles and species mole fractions against the paper's reported values using tolerances, and the LiquidPresent boolean against the paper's finding (no liquid at 600°C/700°C; presence at 800°C for the 0.75/1 ratio)."
    }
  ],
  "notes": "Liquid phase presence is merged into gas_composition.csv instead of a separate artifact, avoiding the need for an additional solve block."
}
```

## How you are scored
A hidden verifier reads your gas_composition.csv and compares each reported value (total moles and mole fractions) against reference equilibrium gas composition results for the same conditions, computed using an independent implementation. Scoring uses per‑condition and per‑species tolerances that accommodate legitimate differences between equilibrium solvers and thermodynamic databases. For each quantity, meeting or exceeding a quality threshold (i.e., being as close or closer to the reference than a tolerance) earns full credit; larger deviations reduce the reward. The final reward combines the scores across all nine conditions and all reported species, with each carrying approximately equal weight. You must write the required CSV file to the specified path; the exact tolerances and reference values are hidden.
