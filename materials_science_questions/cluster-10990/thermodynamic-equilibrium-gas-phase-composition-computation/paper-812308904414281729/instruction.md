# Thermodynamic Equilibrium Gas-Phase Composition Computation for Xe-F2 System

## Problem background
The chemical system of xenon and fluorine is central to understanding the stability and reactivity of xenon fluorides. In the gas phase, a mixture of elemental xenon and fluorine (F₂) can form multiple binary compounds: XeF₂, XeF₄, and XeF₆. The relative thermodynamic stability of these species, together with the dissociation products F and Xe, determines the equilibrium composition as a function of temperature, pressure, and initial stoichiometry. Computing these equilibrium gas-phase compositions by minimizing the total Gibbs free energy of the mixture provides quantitative insight into which species dominate under given conditions and is essential for interpreting reaction pathways, such as the tendency of XeF₂ to disproportionate into XeF₄ and xenon.

## Approach
Use standard thermodynamic data (Gibbs free energies of formation as a function of temperature) for the gas-phase species Xe, F₂, XeF₂, XeF₄, and XeF₆. Treat the mixture as an ideal gas, where the chemical potential of each species depends on its partial pressure. Implement a Gibbs free energy minimization solver (e.g., a direct minimization algorithm or a systematic approach using equilibrium constants derived from the free energies). For every condition, solve for the set of species amounts that minimizes the total Gibbs free energy while conserving the total number of xenon and fluorine atoms. Convert the resulting partial pressures to percentages of the total pressure. Apply the solver to the following 24 conditions: total pressures of 1 bar and 100 bar, temperatures of 500, 600, 700, and 800 K, and initial Xe:F₂ molar ratios of 1:1, 1:2, and 1:3. Output the equilibrium partial pressure (as a percentage) of each of the six species for every condition.

## Reproduction target
Compute the equilibrium partial pressures (as percentage of total pressure) for F₂, F, Xe, XeF₂, XeF₄, and XeF₆ at all 24 combinations of total pressure, temperature, and initial Xe:F₂ ratio listed above. Write the results to a CSV file `xe_f2_equilibrium_composition.csv` with one row per condition and columns: `total_pressure_bar`, `temperature_K`, `initial_ratio_Xe_F2`, `F2`, `F`, `Xe`, `XeF2`, `XeF4`, `XeF6`. The file must contain exactly 24 rows, each representing a distinct condition. The species percentages must follow from a correct thermodynamic equilibrium calculation using publicly available standard thermochemical data.

## Assets

- Standard thermochemical data for Xe, F₂, XeF₂, XeF₄, XeF₆: https://janaf.nist.gov

## Workflow steps

### Step 1: Equilibrium gas-phase composition computation
- Role: scored (load-bearing)
- Action: Compute equilibrium partial pressures (as percentage of total pressure) for the Xe-F₂ system at 24 conditions: total pressures of 1 bar and 100 bar, temperatures of 500, 600, 700, 800 K, and initial Xe:F₂ molar ratios of 1:1, 1:2, 1:3. Implement a thermodynamic equilibrium solver (e.g., Gibbs free energy minimization) using publicly available standard thermochemical data for species Xe, F₂, XeF₂, XeF₄, XeF₆. Write the results to the output CSV.
- Output file: `/app/outputs/xe_f2_equilibrium_composition.csv`
- Format: csv
- Contract: CSV with columns: total_pressure_bar (float), temperature_K (int), initial_ratio_Xe_F2 (string, e.g. '1:1'), F2 (float), F (float), Xe (float), XeF2 (float), XeF4 (float), XeF6 (float). 24 rows, one per condition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/xe_f2_equilibrium_composition.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### xe_f2_equilibrium_composition.csv
- path: `/app/outputs/xe_f2_equilibrium_composition.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium partial pressures as percentages of total pressure for the Xe-F₂ system under 24 conditions.
- schema:
  - `type`: table
  - `required_columns`: `total_pressure_bar`, `temperature_K`, `initial_ratio_Xe_F2`, `F2`, `F`, `Xe`, `XeF2`, `XeF4`, `XeF6`

Notes: The hidden checker compares each species percentage against the paper's reported values from Table 3, using appropriate tolerances for values ≥1% and <1%.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "xe_f2_equilibrium_composition.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "total_pressure_bar",
          "temperature_K",
          "initial_ratio_Xe_F2",
          "F2",
          "F",
          "Xe",
          "XeF2",
          "XeF4",
          "XeF6"
        ]
      },
      "description": "Equilibrium partial pressures as percentages of total pressure for the Xe-F₂ system under 24 conditions."
    }
  ],
  "notes": "The hidden checker compares each species percentage against the paper's reported values from Table 3, using appropriate tolerances for values ≥1% and <1%."
}
```

## How you are scored
A hidden verifier reads your `xe_f2_equilibrium_composition.csv` file and compares the partial pressure percentage of each species at every condition against the reference values that result from a correct thermodynamic equilibrium computation. The reward is based on the number of conditions whose species percentages fall within the verifier's tolerance ranges. Full credit is awarded only when all 24 rows satisfy the tolerance criteria for every species. The verifier also validates that the file contains the required columns and exactly 24 rows; a schema violation results in zero credit for this scored step.
