# Equilibrium H2O and CO2 contents in rhyolitic melt from D-Compress

## Problem background
Understanding how volatile species (H₂O, CO₂, S, etc.) partition between a silicate melt and a coexisting gas phase under magmatic conditions is critical for interpreting volcanic degassing and melt inclusion data. The D-Compress software provides a thermodynamic model to compute the equilibrium composition of both phases for volatile-dominated systems, including the C–O–H system. The model combines gas-phase equilibria, fugacity coefficients for real gases, and empirical power-law solubility relations calibrated for common melt compositions such as rhyolite. This task asks you to use D-Compress to determine the amounts of H₂O and CO₂ that would be dissolved in a rhyolitic melt at a specific combination of pressure, temperature, and redox state.

## Approach
Obtain the D-Compress software (or write a faithful re-implementation of its chemical model) for the C–O–H system. The software contains all necessary equilibrium constants, fugacity models, and solubility parameters for rhyolitic melt. Configure the calculation for a single-point (isobaric) equilibrium: set the chemical system to C–O–H, the melt type to rhyolite, the pressure to 2000 bar, the temperature to 850 °C, and the redox state to NNO+1. Run the calculation and extract the resulting melt weight fractions of H₂O and CO₂. No fitting of solubility coefficients is required – they are built into the software.

## Reproduction target
Compute the equilibrium weight fractions (wt%) of H₂O and CO₂ dissolved in a rhyolitic silicate melt at 850 °C, 2000 bar total pressure, and redox state NNO+1, using the D-Compress model for the C–O–H system. Report the two values in a JSON file with the keys H2O_melt_wt% and CO2_melt_wt% (both floating-point numbers).

## Assets

- D-Compress software (compiled executable and source code): http://dx.doi.org/10.1016/j.cageo.2015.03.002

## Workflow steps

### Step 1: Compute equilibrium H2O and CO2 melt contents for rhyolitic melt at 850°C, 2000 bar, NNO+1
- Role: scored
- Action: Obtain and run D-Compress (or implement its chemical model) for the C-O-H system with rhyolitic melt at 850°C, 2000 bar, and redox state NNO+1. Output the computed H2O and CO2 melt weight fractions (wt%).
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: {"H2O_melt_wt%": float, "CO2_melt_wt%": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Equilibrium weight fractions of H2O and CO2 in a rhyolitic melt at 850°C, 2000 bar, NNO+1, computed by D-Compress or a faithful re-implementation.
- schema:
  - `type`: object
  - `required`:
    - `H2O_melt_wt%`: number
    - `CO2_melt_wt%`: number

Notes: The hidden checker computes relative errors against reference values and scores based on whether errors fall within a defined threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "H2O_melt_wt%": "number",
          "CO2_melt_wt%": "number"
        }
      },
      "description": "Equilibrium weight fractions of H2O and CO2 in a rhyolitic melt at 850°C, 2000 bar, NNO+1, computed by D-Compress or a faithful re-implementation."
    }
  ],
  "notes": "The hidden checker computes relative errors against reference values and scores based on whether errors fall within a defined threshold."
}
```

## How you are scored
A hidden verifier reads your output file and independently compares the H₂O and CO₂ values to reference values derived from the paper’s reported results. The comparison uses an appropriate tolerance and awards credit based on how close your computed results are to the expected results. The reward is a weighted combination of the scores from each scored workflow stage; reporting the paper’s numbers verbatim is not enough – you must compute them yourself.
