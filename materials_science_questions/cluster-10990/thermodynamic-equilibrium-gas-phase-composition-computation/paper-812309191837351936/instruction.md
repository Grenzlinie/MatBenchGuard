# Equilibrium Partial Pressures in the Tungsten-Water Vapor System

## Problem background
In incandescent lamps, tungsten filaments degrade over time due to chemical reactions with trace water vapor present in the inert gas fill. Understanding the gas-phase composition near the hot filament as a function of temperature and water vapor concentration is essential to predict tungsten transport and lamp lifetime. This task reproduces the thermodynamic equilibrium calculation that determines the partial pressures of all major tungsten-containing and light gas species for the W(s)/H2O/H2/N2 system over a wide temperature range.

## Approach
The equilibrium composition is obtained by solving the combined system of reaction equilibria and element mass balances. Standard Gibbs free energies of formation for all species are taken from the NIST-JANAF thermochemical tables. These are used to compute temperature-dependent equilibrium constants for the 11 reactions listed below. The mass-balance constraints fix the total amounts of oxygen and hydrogen atoms according to the input water vapor concentration. The resulting nonlinear algebraic equations are solved simultaneously to yield the equilibrium partial pressures of the 14 gas-phase species at each temperature. The solution can employ standard numerical techniques such as Newton's method, or any suitable chemical equilibrium solver.

## Reactions

The following 11 gas-phase and heterogeneous reactions form the chemical system:

1. 2 H2O(g) ⇌ 2 H2(g) + O2(g)
2. H2(g) ⇌ 2 H(g)
3. O2(g) ⇌ 2 O(g)
4. O2(g) + H2(g) ⇌ 2 OH(g)
5. W(s) + H2O(g) ⇌ WO(g) + H2(g)
6. W(s) + 2 H2O(g) ⇌ WO2(g) + 2 H2(g)
7. W(s) + 3 H2O(g) ⇌ WO3(g) + 3 H2(g)
8. 2 W(s) + 6 H2O(g) ⇌ W2O6(g) + 6 H2(g)
9. 3 W(s) + 9 H2O(g) ⇌ W3O9(g) + 9 H2(g)
10. 4 W(s) + 12 H2O(g) ⇌ W4O12(g) + 12 H2(g)
11. W(s) + 4 H2O(g) ⇌ WO2(OH)2(g) + 3 H2(g)

Equilibrium constants for these reactions are computed from the standard Gibbs free energy change using the JANAF data.

## Reproduction target
Compute the equilibrium partial pressures (in atm) for the condition: the gas phase initially contains 20 parts per million (ppm) of H2O in an inert carrier gas (N2), no added H2, total pressure = 1 atmosphere. Carry out the calculation at the following temperatures: 1800 K, 2000 K, 2200 K, 2400 K, 2600 K, 2800 K, 3000 K, 3200 K, 3400 K, and 3600 K. Report the partial pressures of the 14 species — H2O, H2, H, O2, O, OH, W, WO, WO2, WO3, W2O6, W3O9, W4O12, and WO2(OH)2 — in a CSV file named table2_reproduced.csv with columns for Temperature and each species. Use scientific notation (e.g., 7.6E-6).

## Assets

- NIST-JANAF Thermochemical Tables: https://janaf.nist.gov/

## Workflow steps

### Step 1: Retrieve thermochemical data
- Role: process
- Action: Obtain standard thermochemical data (ΔH°_f, S°, heat capacity coefficients or free-energy functions) for all 14 gas-phase species and solid tungsten from the NIST-JANAF tables. Use this data to compute temperature-dependent equilibrium constants for the 11 reactions listed in the Reactions section above.
- Evidence: `/app/outputs/janaf_data_retrieved.log`

### Step 2: Compute equilibrium partial pressures
- Role: scored (load-bearing)
- Action: Using the equilibrium constants from step 1, solve the coupled system of 11 reaction equilibria and three elemental mass-balance constraints (for ΣP_O, ΣP_H, and ΣP_W) for the condition: 20 ppm H2O in inert gas, no added H2, total pressure = 1 atm. The mass balances are: ΣP_O = 2e-5 atm, ΣP_H = 4e-5 atm, and ΣP_W determined from the solution. Compute the equilibrium partial pressures (atm) of all 14 gas-phase species at each temperature from 1800 K to 3600 K in 200 K increments. Write the results to table2_reproduced.csv.
- Output file: `/app/outputs/table2_reproduced.csv`
- Format: csv
- Contract: CSV with columns: Temperature, H2O, H2, H, O2, O, OH, W, WO, WO2, WO3, W2O6, W3O9, W4O12, WO2(OH)2. 10 rows (temperatures 1800,2000,...,3600 K). Pressure values in atm, using scientific notation.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table2_reproduced.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table2_reproduced.csv
- path: `/app/outputs/table2_reproduced.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium partial pressures for the given conditions (20 ppm H2O, 1 atm total pressure). The checker compares each value to a reference dataset using tolerances appropriate for numerical and thermochemical data spread.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `H2O`, `H2`, `H`, `O2`, `O`, `OH`, `W`, `WO`, `WO2`, `WO3`, `W2O6`, `W3O9`, `W4O12`, `WO2(OH)2`
  - `units`:
    - `Temperature`: K
    - `H2O`: atm
    - `H2`: atm
    - `H`: atm
    - `O2`: atm
    - `O`: atm
    - `OH`: atm
    - `W`: atm
    - `WO`: atm
    - `WO2`: atm
    - `WO3`: atm
    - `W2O6`: atm
    - `W3O9`: atm
    - `W4O12`: atm
    - `WO2(OH)2`: atm

Notes: The checker validates the partial pressure values against a reference dataset derived from established thermodynamic standard data. Each value is compared within appropriate tolerances to account for numerical and data-source differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table2_reproduced.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "H2O",
          "H2",
          "H",
          "O2",
          "O",
          "OH",
          "W",
          "WO",
          "WO2",
          "WO3",
          "W2O6",
          "W3O9",
          "W4O12",
          "WO2(OH)2"
        ],
        "units": {
          "Temperature": "K",
          "H2O": "atm",
          "H2": "atm",
          "H": "atm",
          "O2": "atm",
          "O": "atm",
          "OH": "atm",
          "W": "atm",
          "WO": "atm",
          "WO2": "atm",
          "WO3": "atm",
          "W2O6": "atm",
          "W3O9": "atm",
          "W4O12": "atm",
          "WO2(OH)2": "atm"
        }
      },
      "description": "Equilibrium partial pressures for the given conditions (20 ppm H2O, 1 atm total pressure). The checker compares each value to a reference dataset using tolerances appropriate for numerical and thermochemical data spread."
    }
  ],
  "notes": "The checker validates the partial pressure values against a reference dataset derived from established thermodynamic standard data. Each value is compared within appropriate tolerances to account for numerical and data-source differences."
}
```

## How you are scored
Your solution is evaluated by a hidden verifier that compares every pressure value in your submitted CSV to a reference dataset derived from established thermodynamic data. Each entry is checked within appropriate numerical tolerances that account for differences in numerical solvers and minor variations in thermochemical data sources. The final score is the fraction of the 140 entries (10 temperatures × 14 species) that fall within the accepted tolerance. Additionally, the verifier confirms that the output file follows the required format and column specifications. There is no need to match the exact reference value digit-for-digit; a correct physical solution computed with sound methods will pass.
