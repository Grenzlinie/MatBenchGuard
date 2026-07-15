# Calorimetric Phase Transition Enthalpy/Entropy Determination

## Problem background
The low-temperature phase transitions in the alkali metal hydroxides KOH and KOD involve antiferroelectric ordering driven by tunneling of the hydroxide/deuteroxide ions. Understanding these transitions requires accurate thermodynamic parameters: the transition temperature, the enthalpy change, and the entropy change associated with the transformation. This task provides high-precision heat capacity data for both KOH and KOD, measured by adiabatic calorimetry, and asks you to determine those parameters from the experimental Cp vs. T curves.

## Approach
For each compound, the transition temperature is identified as the temperature where the heat capacity reaches a maximum. A baseline heat capacity, representing the Cp the material would have had in the absence of the transition, is constructed by linearly extrapolating the experimental Cp from a temperature 30 K below the transition to the transition temperature, and from a temperature 15 K above the transition back to the transition temperature. Using this baseline, the excess heat capacity (Cp_experimental − Cp_baseline) is integrated over the transition region to obtain the transition enthalpy, and (Cp_experimental − Cp_baseline)/T is integrated to obtain the transition entropy. The molar gas constant R = 8.314 J/(mol·K) converts the integrated quantities into standard units.

## Reproduction target
Compute the transition temperature T_tr (in K), the transition enthalpy ΔH_tr (in J/mol), and the transition entropy ΔS_tr (in units of R) for both KOH and KOD from the provided Cp data files using the baseline and integration procedure described above. Report the results in a JSON file at /app/outputs/results.json with the exact schema specified in the output contract.

## Assets

- KOH_Cp_data.csv
- KOD_Cp_data.csv

## Workflow steps

### Step 1: Determine transition temperature and baseline heat capacity
- Role: process
- Action: For each compound (KOH and KOD), read the provided Cp data, identify the transition temperature T_tr as the temperature of maximum Cp, and construct a baseline Cp by taking the experimental Cp from a temperature 30 K below T_tr extrapolated forward to T_tr, and from 15 K above T_tr extrapolated back to T_tr. Save the constructed baseline(s) for use in integration.
- Evidence: `/app/outputs/baseline_diagnostics.json`

### Step 2: Integrate excess heat capacity to obtain ΔH_tr and ΔS_tr
- Role: scored (load-bearing)
- Action: Using the baseline and the experimental Cp data, for each compound compute the transition enthalpy ΔH_tr (in J/mol) by integrating (Cp · R – Cp_baseline · R) across the transition region, and the transition entropy ΔS_tr (in units of R) by integrating (Cp – Cp_baseline)/T across the transition region. The gas constant R = 8.314 J/(mol·K). Convert ΔH_tr from R to J/mol. Output the results as a JSON file with keys 'KOH' and 'KOD', each containing 'T_tr' (K), 'ΔH_tr' (J/mol), 'ΔS_tr' (dimensionless, in R).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with keys 'KOH' and 'KOD'. Each key maps to an object: {'T_tr': number (K), 'ΔH_tr': number (J/mol), 'ΔS_tr': number (in units of R)}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The transition temperature, enthalpy, and entropy for KOH and KOD low‑temperature phase transitions. All values are scalars. T_tr in K, ΔH_tr in J/mol, ΔS_tr in units of the molar gas constant R.
- schema:
  - `type`: object
  - `required`:
    - `KOH`:
      - `type`: object
      - `required`:
        - `T_tr`: number (unit: K)
        - `ΔH_tr`: number (unit: J/mol)
        - `ΔS_tr`: number (unit: R, dimensionless)
    - `KOD`:
      - `type`: object
      - `required`:
        - `T_tr`: number (unit: K)
        - `ΔH_tr`: number (unit: J/mol)
        - `ΔS_tr`: number (unit: R, dimensionless)

Notes: The checker compares the submitted numeric values to hidden paper‑reported values (Table III) with appropriate absolute tolerances. Full credit is awarded when all values fall within the tolerances; partial credit may be given based on the number of correct values. The choice of baseline (extrapolation from fixed offsets below/above T_tr) is fully specified in the workflow steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "KOH": {
            "type": "object",
            "required": {
              "T_tr": "number (unit: K)",
              "ΔH_tr": "number (unit: J/mol)",
              "ΔS_tr": "number (unit: R, dimensionless)"
            }
          },
          "KOD": {
            "type": "object",
            "required": {
              "T_tr": "number (unit: K)",
              "ΔH_tr": "number (unit: J/mol)",
              "ΔS_tr": "number (unit: R, dimensionless)"
            }
          }
        }
      },
      "description": "The transition temperature, enthalpy, and entropy for KOH and KOD low‑temperature phase transitions. All values are scalars. T_tr in K, ΔH_tr in J/mol, ΔS_tr in units of the molar gas constant R."
    }
  ],
  "notes": "The checker compares the submitted numeric values to hidden paper‑reported values (Table III) with appropriate absolute tolerances. Full credit is awarded when all values fall within the tolerances; partial credit may be given based on the number of correct values. The choice of baseline (extrapolation from fixed offsets below/above T_tr) is fully specified in the workflow steps."
}
```

## How you are scored
A hidden verifier will read your results.json and compare each reported value (T_tr, ΔH_tr, ΔS_tr) for both KOH and KOD against independently determined reference values using appropriate tolerances. The final reward is computed from the number of values that fall within the tolerance bands. Submitting numbers without performing the full baseline construction and integration as described will not earn credit; the verifier checks agreement with the expected thermodynamic parameters derived from the same experimental data.
