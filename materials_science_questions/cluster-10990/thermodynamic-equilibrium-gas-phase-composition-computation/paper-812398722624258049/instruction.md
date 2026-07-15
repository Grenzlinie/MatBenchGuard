# High-Temperature Equilibrium Speciation of Cs and I in Steam/Hydrogen Mixtures

## Problem background
In a pressurized water reactor (PWR) during a loss-of-coolant accident, the fission products cesium and iodine can escape from the fuel and enter a steam/hydrogen atmosphere formed by the Zircaloy-water reaction. The chemical form of iodine strongly influences its potential release: volatile elemental iodine (I) and hydrogen iodide (HI) may bypass containment systems, while cesium iodide (CsI) is much less mobile. Understanding the equilibrium speciation — the ratios of I, HI, CsOH, and atomic Cs relative to CsI — at high temperatures and pressures is therefore important for radiological source term assessments. This task requires computing these ratios for a range of conditions representative of accident scenarios, using thermodynamic equilibrium calculations.

## Approach
For a closed gaseous system at given temperature, pressure and initial amounts, the equilibrium composition is the state that minimizes the total Gibbs free energy. This equilibrium can be computed with a Gibbs free energy minimizer using standard thermodynamic data (Gibbs free energies or NASA polynomial coefficients) for the relevant species: Cs, I, CsI, HI, CsOH, and the H₂/H₂O mixture. Set up a system containing initial amounts of Cs (0.7 mol), I (0.04 mol), and the prescribed H₂ and H₂O moles at the specified temperature and pressure; run the equilibrium calculation, then derive the four ratios I/CsI, HI/CsI, CsOH/CsI, and Cs/CsI from the equilibrium concentrations. The ratios are expected to show systematic trends with temperature and pressure that provide internal consistency checks.

## Reproduction target
Produce a CSV file `ratios.csv` containing the equilibrium ratios for 12 conditions: temperatures of 1750, 2000, and 2250 K; total pressures of 3 atm and 70 atm; initial Cs = 0.7 mol, I = 0.04 mol; H₂ and H₂O initial amounts (in mol) as follows: for 3 atm, (H₂=140, H₂O=10) and (H₂=100, H₂O=50); for 70 atm, (H₂=800, H₂O=200) and (H₂=500, H₂O=500). Each row must contain the temperature (K), pressure (atm), the H₂ and H₂O mol values, and the four computed ratios: I_CsI, HI_CsI, CsOH_CsI, and Cs_CsI. These ratios must be derived directly from the equilibrium mole fractions or partial pressures of the gaseous species. The agent must use a Gibbs free energy minimizer and publicly available thermochemical data; the expected output format is a plain CSV with one row per condition and exactly the eight columns.

## Assets

- Thermochemical data for gas-phase species Cs, I, CsI, HI, CsOH, H2, H2O: https://janaf.nist.gov/
- Gibbs free energy minimization tool (e.g., Cantera): https://cantera.org/

## Workflow steps

### Step 1: Compute CsI dissociation ratios for the specified conditions
- Role: scored (load-bearing)
- Action: Using a Gibbs free energy minimizer and thermodynamic data for gaseous species Cs, I, CsI, HI, CsOH, H2, H2O, compute the equilibrium composition at each of the following 12 sets of conditions: temperatures of 1750 K, 2000 K, and 2250 K; total pressures of 3 atm and 70 atm; initial amounts Cs = 0.7 mol, I = 0.04 mol; H2 and H2O initial amounts (mol): (140,10) and (100,50) for 3 atm, and (800,200) and (500,500) for 70 atm. For each condition, derive the ratios I/CsI, HI/CsI, CsOH/CsI, and Cs/CsI from the equilibrium concentrations. Save the results as a CSV.
- Output file: `/app/outputs/ratios.csv`
- Format: csv
- Contract: Columns: temperature_K (int), pressure_atm (int), H2_mol (float), H2O_mol (float), I_CsI (float), HI_CsI (float), CsOH_CsI (float), Cs_CsI (float). One row per condition (12 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ratios.csv
- path: `/app/outputs/ratios.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with the equilibrium ratios for the CsI dissociation in steam/hydrogen mixtures under the 12 prescribed temperature/pressure/composition conditions.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `pressure_atm`, `H2_mol`, `H2O_mol`, `I_CsI`, `HI_CsI`, `CsOH_CsI`, `Cs_CsI`
  - `description`: Each row contains the input conditions and the computed equilibrium ratios for one of the 12 specified runs.

Notes: The hidden checker compares ratios to reference values using tolerances and verifies expected monotonic trends in I/CsI with temperature and pressure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "pressure_atm",
          "H2_mol",
          "H2O_mol",
          "I_CsI",
          "HI_CsI",
          "CsOH_CsI",
          "Cs_CsI"
        ],
        "description": "Each row contains the input conditions and the computed equilibrium ratios for one of the 12 specified runs."
      },
      "description": "CSV file with the equilibrium ratios for the CsI dissociation in steam/hydrogen mixtures under the 12 prescribed temperature/pressure/composition conditions."
    }
  ],
  "notes": "The hidden checker compares ratios to reference values using tolerances and verifies expected monotonic trends in I/CsI with temperature and pressure."
}
```

## How you are scored
A hidden verifier reads `ratios.csv`. For each row and each ratio, your computed value is compared to a hidden reference using tolerances appropriate to the magnitude of the ratio (larger ratios are compared with a relative tolerance, very small ratios with an absolute tolerance). The verifier also checks that the ratios obey physically expected monotonic trends with respect to temperature and pressure (for example, certain ratios should change in a predictable direction when temperature increases or when total pressure is changed, as can be inferred from Le Chatelier’s principle). The final score is the fraction of the 12 rows that satisfy both the value tolerances and the trend checks, with higher weight placed on the larger, more discriminating ratios. Simply reporting the correct external numbers is not sufficient; the submitted CSV must result from a genuine equilibrium calculation.
