# Thermodynamic functions of CaF₂ from heat capacity equations

## Problem background
Electroslag remelting (ESR) is used to produce high-quality steels, and mathematical models of the process require accurate thermal property data for the slag layers.  Calcium fluoride, CaF₂, is a major constituent of many ESR slags.  An important input to these models is the thermodynamic behaviour of the slag as a function of temperature: the specific heat capacity, the enthalpy increment (H_T − H_298), and the entropy increment (S_T − S_298).  This task focuses on computing these three thermodynamic functions for pure CaF₂ over the temperature range 298–1900 K, using established piecewise heat capacity equations and known enthalpies of the solid–solid transition and fusion.

## Approach
The heat capacity of CaF₂ is described by three polynomial/constant expressions, each valid over a specific temperature interval.  The solid‑solid transition occurs at 1424 K with an enthalpy of 13.2 kJ kg⁻¹; the melting (fusion) transition occurs at 1695 K with an enthalpy of 393 kJ kg⁻¹.  The three intervals and the corresponding cₚ equations (in kJ K⁻¹ kg⁻¹) are:

- **Low‑temperature solid (298–1424 K):**  
  cₚ(T) = 1.025 − 0.247×10⁻³ T + 0.395×10⁻⁶ T² − 11 550 T⁻²  

- **High‑temperature solid (1424–1695 K):**  
  cₚ(T) = 1.689  

- **Liquid (1695–1900 K):**  
  cₚ(T) = 1.187  

From these equations you compute, for each temperature of interest, the specific heat capacity cₚ directly, the enthalpy increment by numerically integrating cₚ with respect to temperature and adding the full transition or fusion enthalpy at the appropriate discontinuity, and the entropy increment by numerically integrating cₚ/T with respect to temperature (again accounting for the discontinuities).  The result is a table of values at the exact temperatures specified in the reproduction target.

## Reproduction target
Produce a single CSV file `/app/outputs/thermodynamic_functions_caf2.csv` with the following columns and units:

- `T` (K) – temperature
- `cp` (kJ kg⁻¹ K⁻¹) – specific heat capacity
- `enthalpy_increment` (kJ kg⁻¹) – enthalpy relative to 298 K
- `entropy_increment` (kJ K⁻¹ kg⁻¹) – entropy relative to 298 K

The file must contain exactly 21 data rows (plus a header), with one row for each of the following temperatures in this order: 298, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1424 (solid state just before the transition), 1424 (solid state just after the transition), 1500, 1600, 1695 (solid just before fusion), 1695 (liquid just after fusion), 1700, 1800, 1900 K.  Use the cp equations and transition/fusion enthalpies given in the Approach.

## Assets

- Python 3
- NumPy and SciPy: numpy scipy

## Workflow steps

### Step 1: Compute thermodynamic functions for CaF₂
- Role: scored (load-bearing)
- Action: Implement the piecewise heat capacity equations for solid and liquid CaF₂, then compute the specific heat capacity (cp), enthalpy increment (H_T−H_298), and entropy increment (S_T−S_298) by numerical integration over the temperature range 298–1900 K. Apply the solid-state transition enthalpy (13.2 kJ kg⁻¹) at 1424 K and the fusion enthalpy (393 kJ kg⁻¹) at 1695 K. Write the results to a CSV file.
- Output file: `/app/outputs/thermodynamic_functions_caf2.csv`
- Format: csv
- Contract: CSV with header: T,cp,enthalpy_increment,entropy_increment. Each row gives the computed value for that temperature. 21 data rows plus header, in the order listed.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions_caf2.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions_caf2.csv
- path: `/app/outputs/thermodynamic_functions_caf2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic functions (heat capacity, enthalpy increment, entropy increment) for CaF₂ at the temperatures specified in the task. The checker recomputes the reference values using the same piecewise heat capacity equations and numerical integration, and compares the agent's output with proportional tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `cp`, `enthalpy_increment`, `entropy_increment`
  - `units`:
    - `T`: K
    - `cp`: kJ kg⁻¹ K⁻¹
    - `enthalpy_increment`: kJ kg⁻¹
    - `entropy_increment`: kJ K⁻¹ kg⁻¹

Notes: The transition and fusion enthalpies are 13.2 kJ kg⁻¹ and 393 kJ kg⁻¹, respectively. The checker implements the same cₚ(T) functions and trapezoidal integration with a fine step, then compares enthalpy_increment and entropy_increment within 1% and 0.5% relative error, respectively.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions_caf2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "cp",
          "enthalpy_increment",
          "entropy_increment"
        ],
        "units": {
          "T": "K",
          "cp": "kJ kg⁻¹ K⁻¹",
          "enthalpy_increment": "kJ kg⁻¹",
          "entropy_increment": "kJ K⁻¹ kg⁻¹"
        }
      },
      "description": "Thermodynamic functions (heat capacity, enthalpy increment, entropy increment) for CaF₂ at the temperatures specified in the task. The checker recomputes the reference values using the same piecewise heat capacity equations and numerical integration, and compares the agent's output with proportional tolerances."
    }
  ],
  "notes": "The transition and fusion enthalpies are 13.2 kJ kg⁻¹ and 393 kJ kg⁻¹, respectively. The checker implements the same cₚ(T) functions and trapezoidal integration with a fine step, then compares enthalpy_increment and entropy_increment within 1% and 0.5% relative error, respectively."
}
```

## How you are scored
A hidden verifier will independently recompute the enthalpy and entropy increments from the same piecewise heat capacity equations using fine‑step numerical integration.  It will then compare your reported values for `enthalpy_increment` and `entropy_increment` row‑by‑row against its own recomputed reference.  The comparison uses proportional tolerances; the exact tolerances are hidden from you.  Your submission is scored solely on the CSV file; reporting the correct numerical values with high accuracy is essential.
