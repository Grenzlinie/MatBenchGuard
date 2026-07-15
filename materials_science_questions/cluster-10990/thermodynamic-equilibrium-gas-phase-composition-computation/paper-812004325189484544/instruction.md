# Equilibrium Speciation of Alkali Carbonate Additives in Hot Moist Air

## Problem background
This task investigates the thermochemical effect of dry chemical powders (potassium carbonate and sodium carbonate) on flame extinguishment. There is a debate whether heat extraction or chemical inhibition is the primary extinguishment mechanism. Chemical equilibrium calculations can reveal the speciation of the additive in hot combustion gases: whether it remains as a solid/oxide or converts to gaseous hydroxide species, and how that conversion affects the temperature reduction. In this task, you will compute equilibrium compositions of specified gas mixtures containing alkali carbonates to determine the distribution of alkali species and the fraction present as hydroxide, without assuming a particular decomposition path.

## Approach
Use a chemical equilibrium solver that performs Gibbs free energy minimization (e.g., Cantera or NASA CEA). Formulate the initial gas mixtures for the conditions given in the workflow steps: baseline moist air (N2 77.45%, O2 20.59%, H2O 2.00% by mole) plus a precise loading of K2CO3 or Na2CO3, and one case with a stoichiometric propane–air mixture plus K2CO3. Convert the additive masses (g per liter of cold gas) to mole fractions using the ideal gas law at 298 K and 1 atm. Then compute the equilibrium composition at the specified temperature (1700 K or 1900 K) and 1 atm total pressure. From the full equilibrium mole fractions, extract the mole fractions of the key alkali species (KOH, K, KO for potassium; NaOH, Na, NaO for sodium) and compute the molar percentage of the alkali metal that ends up as gaseous hydroxide. The workflow consists of three ordered steps: run the five equilibrium calculations, extract the 1900 K moist-air mole fractions, and compute the hydroxide percentages for all five conditions. The final outputs are two CSV files that record these quantities.

## Reproduction target
Produce two CSV files under /app/outputs that accurately capture the equilibrium speciation results for the five conditions described in the workflow steps:
1. moist_air_1900K_molefractions.csv: For the two 1900 K moist-air cases (K2CO3 and Na2CO3), list the mole percentage of each alkali species (KOH, K, KO; NaOH, Na, NaO) in the total equilibrium mixture.
2. hydroxide_percentages.csv: For all five conditions (moist air + K2CO3 at 1900 K and 1700 K, moist air + Na2CO3 at 1900 K and 1700 K, and stoichiometric propane–air + K2CO3 at 1900 K), report the molar percentage of the alkali metal present as gaseous hydroxide, computed as 100 × (mole fraction of hydroxide) / (sum of mole fractions of all alkali species for that metal).
The true target is to obtain these quantities from a faithful equilibrium calculation; the correctness of your outputs will be judged by a hidden verifier against reference values derived from the same calculations. There is no need to reproduce temperature–enthalpy curves or temperature reductions.

## Assets

- Chemical equilibrium solver (Cantera or NASA CEA): https://cantera.org

## Workflow steps

### Step 1: Run equilibrium calculations for all five conditions
- Role: process
- Action: Using a chemical equilibrium solver that performs Gibbs free energy minimization (Cantera or NASA CEA), compute the equilibrium gas-phase composition for the following five cases: (1) Moist air (77.45% N2, 20.59% O2, 2.00% H2O by mole) + 0.0305 g K2CO3 per liter of cold air, at T=1900 K, P=1 atm. (2) Same moist air + 0.04305 g Na2CO3 per liter, T=1900 K, P=1 atm. (3) Same moist air + 0.0305 g K2CO3 per liter, T=1700 K, P=1 atm. (4) Same moist air + 0.04305 g Na2CO3 per liter, T=1700 K, P=1 atm. (5) Stoichiometric propane-air mixture (C3H8 + 5 O2 + 18.80 N2) + 0.0305 g K2CO3 per liter of air volume, T=1900 K, P=1 atm. Convert the mass per liter of additive to moles using the ideal gas law at 298 K and 1 atm (1 liter of cold gas contains 0.04087 mol total gas) and the appropriate molar masses (K2CO3: 138.205 g/mol, Na2CO3: 105.988 g/mol). Save the full equilibrium mole fractions for all species (as percentages of the total mixture) in a structured file.
- Evidence: `/app/outputs/all_equilibrium_compositions.json`

### Step 2: Extract 1900 K moist-air mole fractions
- Role: scored
- Action: From the equilibrium results produced in step_0, extract the mole percentages for the alkali species in the two 1900 K moist-air cases: for the K2CO3 case, KOH, K, KO; for the Na2CO3 case, NaOH, Na, NaO. Write a CSV file with columns: Case (either 'K2CO3' or 'Na2CO3'), Species (species name, one of KOH, K, KO, NaOH, Na, NaO), MolePercent (float, the mole percentage of that species in the total equilibrium mixture).
- Output file: `/app/outputs/moist_air_1900K_molefractions.csv`
- Format: csv
- Contract: Case (string, one of 'K2CO3','Na2CO3'), Species (string, species name), MolePercent (float between 0 and 100).
- Scoring: scored by hidden verifier

### Step 3: Compute hydroxide percentages for all five conditions
- Role: scored (load-bearing)
- Action: Using the equilibrium compositions from step_0, compute the molar percentage of alkali present as gaseous hydroxide for each of the five conditions. For potassium cases: HydroxidePercent = 100 * KOH_mole_percent / (KOH_mole_percent + K_mole_percent + KO_mole_percent). For sodium cases: HydroxidePercent = 100 * NaOH_mole_percent / (NaOH_mole_percent + Na_mole_percent + NaO_mole_percent). Write a CSV file with columns: Case (a string identifier, e.g., 'MoistAir_K2CO3_1900K', 'MoistAir_Na2CO3_1900K', 'MoistAir_K2CO3_1700K', 'MoistAir_Na2CO3_1700K', 'PropaneAir_K2CO3_1900K'), Temperature_K (integer temperature in Kelvin), HydroxidePercent (float).
- Output file: `/app/outputs/hydroxide_percentages.csv`
- Format: csv
- Contract: Case (string identifier), Temperature_K (int), HydroxidePercent (float between 0 and 100).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/moist_air_1900K_molefractions.csv`
- `/app/outputs/hydroxide_percentages.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### moist_air_1900K_molefractions.csv
- path: `/app/outputs/moist_air_1900K_molefractions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mole fractions of alkali species (KOH, K, KO; NaOH, Na, NaO) for the two 1900 K moist-air equilibrium calculations. Compared to the paper's tabulated values within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Case`, `Species`, `MolePercent`
  - `units`:
    - `MolePercent`: percentage

### hydroxide_percentages.csv
- path: `/app/outputs/hydroxide_percentages.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Molar percentage of potassium or sodium present as gaseous hydroxide for all five conditions, plus the temperature reduction from the pure-air baseline at the enthalpy addition that raises pure moist air to approximately 1800 K (for the 1900 K K2CO3 and Na2CO3 cases). The baseline temperature is 1800 K; the reduction is the difference between that baseline temperature and the temperature of the additive mixture at the same enthalpy. Values for other cases are ignored. Compared to the paper's reported values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Case`, `Temperature_K`, `HydroxidePercent`, `BaselineTemperature_K`, `TemperatureReduction_K`
  - `units`:
    - `HydroxidePercent`: percentage
    - `BaselineTemperature_K`: kelvin
    - `TemperatureReduction_K`: kelvin

Notes: The task covers equilibrium speciation, derived hydroxide percentages, and the temperature reductions at the 1800 K baseline, all reproducible with the same chemical equilibrium solver. The enthalpy-temperature curves are generated as a process step; the reductions are scored within the hydroxide_percentages.csv file.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "moist_air_1900K_molefractions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Case",
          "Species",
          "MolePercent"
        ],
        "units": {
          "MolePercent": "percentage"
        }
      },
      "description": "Mole fractions of alkali species (KOH, K, KO; NaOH, Na, NaO) for the two 1900 K moist-air equilibrium calculations. Compared to the paper's tabulated values within a relative tolerance."
    },
    {
      "file": "hydroxide_percentages.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Case",
          "Temperature_K",
          "HydroxidePercent",
          "BaselineTemperature_K",
          "TemperatureReduction_K"
        ],
        "units": {
          "HydroxidePercent": "percentage",
          "BaselineTemperature_K": "kelvin",
          "TemperatureReduction_K": "kelvin"
        }
      },
      "description": "Molar percentage of potassium or sodium present as gaseous hydroxide for all five conditions, plus the temperature reduction from the pure-air baseline at the enthalpy addition that raises pure moist air to approximately 1800 K (for the 1900 K K2CO3 and Na2CO3 cases). The baseline temperature is 1800 K; the reduction is the difference between that baseline temperature and the temperature of the additive mixture at the same enthalpy. Values for other cases are ignored. Compared to the paper's reported values within tolerance."
    }
  ],
  "notes": "The task covers equilibrium speciation, derived hydroxide percentages, and the temperature reductions at the 1800 K baseline, all reproducible with the same chemical equilibrium solver. The enthalpy-temperature curves are generated as a process step; the reductions are scored within the hydroxide_percentages.csv file."
}
```

## How you are scored
A hidden verifier will independently evaluate your submitted CSV files against expected reference values. The verifier checks the mole fractions of alkali species in moist_air_1900K_molefractions.csv and the hydroxide percentages in hydroxide_percentages.csv. Each file contributes to a final reward score; the hydroxide percentage file carries the greater weight because it encapsulates the main speciation claim. The verifier uses appropriate tolerances to account for minor implementation differences between equilibrium solvers. Your task is to produce results that closely match the target equilibrium compositions; reporting arbitrary numbers or not following the specified workflow will result in a low score.
