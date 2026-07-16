# Assessment of C–F Bond Additivity Correction for Fluoroethane Enthalpies

## Problem background
Ab initio composite methods (G2(MP2), G2, CBS-4, CBS-Q) systematically underestimate the standard enthalpies of formation of fluoroethanes. This task tests whether a single C–F bond additivity correction (BAC) derived from fluoromethanes can also compensate for the errors in the fluoroethane series. The key open question is the magnitude of the residual average error (AVE2) across the fluoroethanes after applying only the C–F BAC, which quantifies the remaining systematic bias.

## Approach
Given the provided electronic ground-state energies, scaled vibrational frequencies, and atomization enthalpies of elements (C, H, F), standard enthalpies of formation at 298 K are computed for ethane and nine fluoroethanes via an atomization-based thermochemical cycle that includes zero-point energy and thermal corrections. The raw enthalpies are then corrected by adding the bond additivity correction Δ_BAC = n_CF × Δ_C-F, where n_CF is the number of C–F bonds in the molecule and Δ_C-F is the method-specific correction parameter. The deviations of both the raw and the BAC-corrected enthalpies from the experimental reference values are evaluated. For each of the four methods, the average error (AVE2) over the fluoroethanes (molecules with at least one C–F bond) is then computed to assess the effectiveness of the single BAC.

## Reproduction target
Produce the CSV file `corrected_enthalpies_and_errors.csv` containing the raw and BAC-corrected enthalpies of formation and their deviations from experiment for all four methods and all ten molecules. From this file, for each method, compute the average error (AVE2) over the fluoroethanes (rows where n_CF > 0). The target is the four numerical AVE2 values, which will be compared by the verifier against the expected reference from the original study.

## Assets

- Ground-state electronic energies (E0)
- Scaled vibrational frequencies
- Experimental enthalpies of formation
- Atomization enthalpies of elements
- C–F bond additivity correction parameters
- Python scientific stack

## Workflow steps

### Step 1: Compute raw ab initio enthalpies of formation
- Role: process
- Action: Using the provided electronic energies, vibrational frequencies, and atomization enthalpies of elements, compute the standard enthalpies of formation (Δ_fH°) at 298 K for each molecule (ethane and nine fluoroethanes) and each method (G2(MP2), G2, CBS-4, CBS-Q) via an atomization-based thermochemical cycle. Incorporate zero-point energy and thermal corrections according to standard procedure.
- Evidence: `/app/outputs/raw_enthalpies.csv`

### Step 2: Apply C–F bond additivity correction and evaluate residual errors
- Role: scored (load-bearing)
- Action: Read the raw enthalpies, experimental enthalpies, and the provided Δ_C-F parameters. For each fluoroethane and ethane, compute the deviation of the raw enthalpy from experiment, then apply the C–F bond additivity correction (Δ_BAC = n_CF × Δ_C-F). Compute the BAC-corrected enthalpy and its deviation from experiment. Save all quantities to a CSV file.
- Output file: `/app/outputs/corrected_enthalpies_and_errors.csv`
- Format: csv
- Contract: CSV with columns: method (string), molecule (string), n_CF (int), calc_Hf_abinitio (numeric, kJ mol⁻¹), dev_abinitio (numeric, kJ mol⁻¹), calc_Hf_BAC (numeric, kJ mol⁻¹), dev_BAC (numeric, kJ mol⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/corrected_enthalpies_and_errors.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### corrected_enthalpies_and_errors.csv
- path: `/app/outputs/corrected_enthalpies_and_errors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Raw and C–F BAC‑corrected enthalpies of formation and deviations from experiment. The checker computes the per‑method mean of dev_BAC over fluoroethanes (n_CF > 0) and compares it against the paper‑reported average residual error (AVE2) within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `method`, `molecule`, `n_CF`, `calc_Hf_abinitio`, `dev_abinitio`, `calc_Hf_BAC`, `dev_BAC`
  - `units`:
    - `calc_Hf_abinitio`: kJ mol⁻¹
    - `dev_abinitio`: kJ mol⁻¹
    - `calc_Hf_BAC`: kJ mol⁻¹
    - `dev_BAC`: kJ mol⁻¹

Notes: The file must include rows for ethane (n_CF=0) as well. The scored quantity is the AVE2 derived from this file; it does not need to be reported separately.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "corrected_enthalpies_and_errors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "molecule",
          "n_CF",
          "calc_Hf_abinitio",
          "dev_abinitio",
          "calc_Hf_BAC",
          "dev_BAC"
        ],
        "units": {
          "calc_Hf_abinitio": "kJ mol⁻¹",
          "dev_abinitio": "kJ mol⁻¹",
          "calc_Hf_BAC": "kJ mol⁻¹",
          "dev_BAC": "kJ mol⁻¹"
        }
      },
      "description": "Raw and C–F BAC‑corrected enthalpies of formation and deviations from experiment. The checker computes the per‑method mean of dev_BAC over fluoroethanes (n_CF > 0) and compares it against the paper‑reported average residual error (AVE2) within a hidden tolerance."
    }
  ],
  "notes": "The file must include rows for ethane (n_CF=0) as well. The scored quantity is the AVE2 derived from this file; it does not need to be reported separately."
}
```

## How you are scored
The hidden verifier reads the submitted `corrected_enthalpies_and_errors.csv`, filters rows where `n_CF > 0`, and computes the per-method mean of the `dev_BAC` column. These four average errors (AVE2) are compared against the hidden reference values from the paper within a hidden tolerance. Full credit is awarded if all four averages are within the tolerance; if some methods fall outside, partial credit is given in proportion to the number of methods whose AVE2 meets the tolerance.
