# Hafnium site-interchange enthalpy extraction in lithium niobate and lithium tantalate

## Problem background
Lithium niobate (LiNbO3) and lithium tantalate (LiTaO3) are isostructural ferroelectric materials with important technological applications. The properties of these crystals are strongly influenced by dopant atoms. Using perturbed-angular-correlation (PAC) spectroscopy with the 181Hf→181Ta probe, it was observed that Hf4+ dopants, which occupy lithium sites at low temperatures, dynamically redistribute at high temperatures by also occupying group-V (Nb or Ta) sites. The temperature-dependent site-occupancy ratio (A2/A1) can be interpreted as an equilibrium site-interchange process described by a defect-chemistry reaction. A thermodynamic model yields a linear relationship between ln(A2/A1) and reciprocal temperature, from which the standard-state enthalpy change (ΔH) of the interchange reaction can be extracted. The goal is to compute this enthalpy for both LiNbO3 and LiTaO3.

## Approach
The site-interchange process is modeled as a mass-action equilibrium: Hf ions initially on Li sites exchange with group-V ions on their regular sites. The equilibrium constant for this defect-exchange reaction leads to a linear relation between the logarithm of the occupancy ratio (A2/A1) and inverse temperature (1/T), where the slope is directly proportional to the standard-state enthalpy ΔH and the intercept includes entropy and stoichiometry contributions. Therefore, given a table of measured (temperature, A2/A1) pairs for each material, we implement a linear least-squares fit of ln(A2/A1) vs 1/T. From the fitted slope we compute ΔH in electron-volts using the Boltzmann constant (8.617333262145×10⁻⁵ eV/K). The two enthalpies are the sole output.

## Reproduction target
For the digitised PAC occupancy-ratio data provided below, perform a linear least-squares fit of ln(A2/A1) versus 1/T separately for LiNbO3 and LiTaO3. Convert each fitted slope to a standard-state enthalpy ΔH in electron-volts (eV). Store both values in the output file step_01_fitted_enthalpies.json as a JSON object with keys LiNbO3_enthalpy_eV and LiTaO3_enthalpy_eV.

## Assets

- digitised PAC occupancy ratios
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Fit site-interchange model and compute enthalpies
- Role: scored (load-bearing)
- Action: Use the provided digitised table of (temperature, A₂/A₁) for LiNbO₃ and LiTaO₃. For each material, compute ln(A₂/A₁) and perform a linear least-squares fit of ln(A₂/A₁) versus 1/T. Extract the slope and convert it to a standard-state enthalpy ΔH (in eV) using the Boltzmann constant (k_B = 8.617333262145×10⁻⁵ eV/K). Store the two enthalpies in the output JSON file.
- Output file: `/app/outputs/step_01_fitted_enthalpies.json`
- Format: json
- Contract: {"LiNbO3_enthalpy_eV": number, "LiTaO3_enthalpy_eV": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_fitted_enthalpies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_fitted_enthalpies.json
- path: `/app/outputs/step_01_fitted_enthalpies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON object containing the computed standard-state enthalpy changes for the Hf site-interchange reaction in LiNbO₃ and LiTaO₃.
- schema:
  - `type`: object
  - `required`:
    - `LiNbO3_enthalpy_eV`: number (eV)
    - `LiTaO3_enthalpy_eV`: number (eV)

Notes: The digitised occupancy ratio data table will be provided in instruction.md. The enthalpies are compared against hidden paper-reported values with a tolerance that accounts for fitting variability.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_fitted_enthalpies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "LiNbO3_enthalpy_eV": "number (eV)",
          "LiTaO3_enthalpy_eV": "number (eV)"
        }
      },
      "description": "JSON object containing the computed standard-state enthalpy changes for the Hf site-interchange reaction in LiNbO₃ and LiTaO₃."
    }
  ],
  "notes": "The digitised occupancy ratio data table will be provided in instruction.md. The enthalpies are compared against hidden paper-reported values with a tolerance that accounts for fitting variability."
}
```

## How you are scored
Your submitted step_01_fitted_enthalpies.json will be read by a hidden verifier. The verifier compares your reported ΔH values for LiNbO3 and LiTaO3 against the paper’s original reported enthalpies (which are hidden from you). A tolerance is applied that absorbs legitimate differences arising from alternative linear-fitting implementations and floating-point handling; your result is accepted if each enthalpy lies within that tolerance. The score is the fraction of the two enthalpies that pass (full credit when both are within tolerance, partial credit if only one passes).
