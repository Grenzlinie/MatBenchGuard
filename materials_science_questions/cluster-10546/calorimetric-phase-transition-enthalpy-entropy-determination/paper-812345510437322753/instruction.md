# Calorimetric phase transition enthalpy and entropy determination

## Problem background
Crystalline p-quaterphenyl undergoes a twist-related structural phase transition that manifests as a broad anomaly in its molar heat capacity curve. Accurately quantifying the transition enthalpy and entropy from calorimetric data is essential for understanding the thermodynamics of this order-disorder type process. This task processes the published heat-capacity data to isolate the transition signal, construct a baseline representing the non-transitional heat capacity, and compute the molar transition enthalpy and entropy. The twist transition manifests as a broad anomaly in the heat‑capacity curve; the agent must locate the anomaly and determine its temperature range from the data.

## Approach
The workflow separates the transition contribution from the normal heat capacity by a baseline-subtraction method. First, the heat capacity vs temperature data is loaded and the temperature region of the transition anomaly is identified. A smooth baseline heat capacity is then constructed by fitting a curve (e.g., a polynomial or spline) to the data points outside the anomaly interval. Subtracting this baseline from the measured heat capacity within the anomaly gives the excess heat capacity ΔCp(T). Finally, numerical integration of ΔCp over temperature yields the transition enthalpy ΔH, and integration of ΔCp/T yields the transition entropy ΔS. The results are saved together with the transition temperature.

## Reproduction target
Using the provided molar heat capacity data (Cp vs T) for p-quaterphenyl, compute the molar transition enthalpy ΔH (J/mol) and transition entropy ΔS (J/K/mol) associated with the twist phase transition. Produce a JSON file containing the transition temperature T_trs (K), the enthalpy, and the entropy.

## Assets

- Measured molar heat capacities of p-quaterphenyl (Table 1)

## Workflow steps

### Step 1: Load and preprocess heat capacity data
- Role: process
- Action: Read the provided CSV file containing temperature (K) and molar heat capacity (J/K/mol) data for p-quaterphenyl, clean if necessary, and sort by ascending temperature.
- Evidence: none

### Step 2: Locate the phase transition anomaly and determine temperature interval
- Role: process
- Action: Identify the region of anomalous heat capacity corresponding to the twist transition. Locate the temperature of maximum anomaly (T_trs) and determine the approximate temperature interval of the anomaly (roughly 180 K to 270 K).
- Evidence: none

### Step 3: Construct normal heat-capacity baseline
- Role: process
- Action: Select data points outside the anomaly interval (e.g., below 180 K and above 270 K) and fit a smooth interpolating curve (e.g., a low-order polynomial or spline) to represent the heat capacity in the absence of the transition. Extend this baseline across the anomaly interval.
- Evidence: none

### Step 4: Compute excess heat capacity
- Role: process
- Action: For each temperature in the anomaly interval, subtract the baseline heat capacity from the measured heat capacity to obtain the excess heat capacity ΔCp(T). Save the resulting table (columns: temperature K, excess_Cp J/K/mol) to 'excess_heat_capacity.csv'.
- Evidence: `/app/outputs/excess_heat_capacity.csv`

### Step 5: Integrate excess heat capacity to obtain transition enthalpy and entropy
- Role: scored (load-bearing)
- Action: Numerically integrate the excess heat capacity ΔCp(T) over the transition temperature interval to obtain the molar transition enthalpy ΔH = ∫ ΔCp dT. Integrate ΔCp(T)/T over the same interval to obtain the molar transition entropy ΔS = ∫ (ΔCp/T) dT. Write the results, together with the transition temperature T_trs (K), to 'transition_properties.json'.
- Output file: `/app/outputs/transition_properties.json`
- Format: json
- Contract: {"T_trs_K": <float>, "delta_H_J_per_mol": <float>, "delta_S_J_per_K_per_mol": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_properties.json
- path: `/app/outputs/transition_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the transition temperature (K), molar transition enthalpy (J/mol), and molar transition entropy (J/K/mol) computed from the excess heat capacity integration.
- schema:
  - `type`: object
  - `required`:
    - `T_trs_K`: number
    - `delta_H_J_per_mol`: number
    - `delta_S_J_per_K_per_mol`: number

Notes: The excess_heat_capacity.csv produced in the process step is used by the checker to independently recompute the integrals and compare against the paper's reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "T_trs_K": "number",
          "delta_H_J_per_mol": "number",
          "delta_S_J_per_K_per_mol": "number"
        }
      },
      "description": "Contains the transition temperature (K), molar transition enthalpy (J/mol), and molar transition entropy (J/K/mol) computed from the excess heat capacity integration."
    }
  ],
  "notes": "The excess_heat_capacity.csv produced in the process step is used by the checker to independently recompute the integrals and compare against the paper's reported values."
}
```

## How you are scored
A hidden verifier independently examines your `transition_properties.json` (and optionally `excess_heat_capacity.csv`) after the run. It recomputes the integrals from your excess heat capacity data, then compares the resulting enthalpy and entropy against a predefined hidden reference. Simply reporting numbers is not sufficient; the entire pipeline—from data loading through integration—must produce results that fall within acceptable tolerances. The final reward is the verifier's aggregate score based on these comparisons.
