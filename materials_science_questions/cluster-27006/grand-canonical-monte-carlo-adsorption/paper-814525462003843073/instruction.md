# Grand Canonical Monte Carlo Simulation of CO₂ Adsorption in Hybrid Ultramicroporous Materials with Interpenetrated pcu Networks

## Problem background
Hybrid ultramicroporous materials (HUMs) with interpenetrated pcu networks are being developed for selective CO₂ capture and separation. The adsorption performance of these materials is often evaluated by the isosteric heat of adsorption (Qst) and by simulated CO₂ adsorption isotherms. Understanding the molecular-level binding sites and thermodynamic properties through Grand Canonical Monte Carlo (GCMC) simulations is essential for validating the computational methodology used to assess these materials and for guiding future design.

## Approach
The computational approach follows a standard GCMC workflow for rigid frameworks. First, the crystal structures of DICRO-3-Ni-i and DICRO-3-Cu-i are obtained, and force-field parameters are assigned: the framework atoms use the Universal Force Field (UFF) Lennard‑Jones parameters, and CO₂ guest molecules are described by the TraPPE model. Partial charges for the framework atoms are assigned consistently (e.g., via DDEC or QEq methods). Then, GCMC simulations of CO₂ adsorption are carried out at 273 K, 283 K, and 293 K over a fugacity range of approximately 0–1 bar for each material. The simulation output provides the absolute CO₂ loading (mmol/g) as a function of fugacity at each temperature. From these three-temperature adsorption isotherms, the zero-loading isosteric heat of adsorption (Qst) is derived by fitting a virial equation to the low-loading region and applying the Clausius-Clapeyron relation. This computational pipeline yields the CO₂ adsorption isotherms and the zero-loading Qst for both materials, which are the target quantities for this task.

## Reproduction target
Compute the CO₂ adsorption isotherms at 273 K, 283 K, and 293 K for DICRO-3-Ni-i and DICRO-3-Cu-i from GCMC simulations, and derive the zero‑loading isosteric heat of adsorption (Qst) for each material. The results must be provided as two CSV files containing the isotherm data (Temperature_K, Fugacity_bar, Loading_mmol_g) and one JSON file reporting the derived zero-loading Qst values for DICRO-3-Ni-i and DICRO-3-Cu-i.

## Assets

- Crystal structure of DICRO-3-Ni-i (CCDC 1448216): 1448216
- Crystal structure of DICRO-3-Cu-i (CCDC 1448217): 1448217
- RASPA GCMC simulation package or equivalent: https://github.com/Wagmore-Group/RASPA
- Force field parameters (UFF for framework, TraPPE for CO₂): RASPA

## Workflow steps

### Step 1: Prepare simulation-ready structures
- Role: process
- Action: Obtain the crystal structures of DICRO-3-Ni-i and DICRO-3-Cu-i from the CSD (deposition numbers 1448216 and 1448217). Assign Lennard-Jones parameters (UFF) and partial charges to all framework atoms consistently (e.g., DDEC or QEq). Use TraPPE parameters for CO₂. Create the input files needed by a GCMC code for CO₂ adsorption simulations of both materials at 273 K, 283 K, and 293 K over 0–1 bar.
- Evidence: none

### Step 2: Run GCMC simulations for DICRO-3-Ni-i
- Role: process
- Action: Perform Grand Canonical Monte Carlo simulations of CO₂ adsorption in DICRO-3-Ni-i at 273 K, 283 K, and 293 K over a range of fugacities approximately 0–1 bar. Collect the per-state-point absolute CO₂ loading (mmol/g) and potential energy data from the raw simulation outputs.
- Evidence: none

### Step 3: Run GCMC simulations for DICRO-3-Cu-i
- Role: process
- Action: Perform Grand Canonical Monte Carlo simulations of CO₂ adsorption in DICRO-3-Cu-i at 273 K, 283 K, and 293 K over a range of fugacities approximately 0–1 bar. Collect the per-state-point absolute CO₂ loading (mmol/g) and potential energy data from the raw simulation outputs.
- Evidence: none

### Step 4: Generate DICRO-3-Ni-i isotherm file
- Role: scored (load-bearing)
- Action: Extract CO₂ loading (mmol/g) as a function of fugacity (bar) from the raw GCMC output for DICRO-3-Ni-i at each temperature (273, 283, 293 K). Write a CSV file with one row per state point and columns Temperature_K, Fugacity_bar, Loading_mmol_g. Cover enough points to define the isotherm shape over 0–1 bar.
- Output file: `/app/outputs/step_01_isotherms_Ni.csv`
- Format: csv
- Contract: CSV with header row and columns: Temperature_K (float, 273 / 283 / 293), Fugacity_bar (float, 0 to ~1), Loading_mmol_g (float, non-negative). One row per (temperature, fugacity) state point.
- Scoring: scored by hidden verifier

### Step 5: Generate DICRO-3-Cu-i isotherm file
- Role: scored (load-bearing)
- Action: Extract CO₂ loading (mmol/g) as a function of fugacity (bar) from the raw GCMC output for DICRO-3-Cu-i at each temperature (273, 283, 293 K). Write a CSV file with one row per state point and columns Temperature_K, Fugacity_bar, Loading_mmol_g. Cover enough points to define the isotherm shape over 0–1 bar.
- Output file: `/app/outputs/step_02_isotherms_Cu.csv`
- Format: csv
- Contract: CSV with header row and columns: Temperature_K (float, 273 / 283 / 293), Fugacity_bar (float, 0 to ~1), Loading_mmol_g (float, non-negative). One row per (temperature, fugacity) state point.
- Scoring: scored by hidden verifier

### Step 6: Compute zero-loading isosteric heat of adsorption
- Role: scored
- Action: From the three-temperature isotherm data in the previous two steps, fit a virial equation to the low-loading region of each material's isotherms and apply the Clausius-Clapeyron relation to derive the zero-loading isosteric heat of adsorption (Qst, kJ/mol) for DICRO-3-Ni-i and DICRO-3-Cu-i. Output a JSON file containing the two values.
- Output file: `/app/outputs/step_03_Qst_results.json`
- Format: json
- Contract: JSON object with numeric fields: "DICRO-3-Ni-i_zero_loading_Qst_kJmol" (float, positive), and "DICRO-3-Cu-i_zero_loading_Qst_kJmol" (float, positive).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_isotherms_Ni.csv`
- `/app/outputs/step_02_isotherms_Cu.csv`
- `/app/outputs/step_03_Qst_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_isotherms_Ni.csv
- path: `/app/outputs/step_01_isotherms_Ni.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CO₂ adsorption isotherm from GCMC simulation for DICRO-3-Ni-i at 273, 283, and 293 K. The checker reads this file to verify physical plausibility (monotonicity with pressure, correct temperature ordering) and to independently recompute the zero-loading isosteric heat of adsorption via virial fitting and the Clausius-Clapeyron relation.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Fugacity_bar`, `Loading_mmol_g`
  - `units`:
    - `Temperature_K`: K
    - `Fugacity_bar`: bar
    - `Loading_mmol_g`: mmol/g

### step_02_isotherms_Cu.csv
- path: `/app/outputs/step_02_isotherms_Cu.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CO₂ adsorption isotherm from GCMC simulation for DICRO-3-Cu-i at 273, 283, and 293 K. The checker reads this file to verify physical plausibility and to independently recompute the zero-loading isosteric heat of adsorption.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Fugacity_bar`, `Loading_mmol_g`
  - `units`:
    - `Temperature_K`: K
    - `Fugacity_bar`: bar
    - `Loading_mmol_g`: mmol/g

### step_03_Qst_results.json
- path: `/app/outputs/step_03_Qst_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Agent-derived zero-loading isosteric heat of adsorption for both materials. The checker independently recomputes Qst from the submitted isotherm CSVs and compares both the agent's reported values and the checker's recomputed values to the hidden paper-reported simulated Qst.
- schema:
  - `type`: object
  - `required`:
    - `DICRO-3-Ni-i_zero_loading_Qst_kJmol`: number (float, kJ/mol)
    - `DICRO-3-Cu-i_zero_loading_Qst_kJmol`: number (float, kJ/mol)

Notes: The primary scored artifacts are the isotherm CSVs, from which the checker recomputes Qst. The Qst JSON provides the agent's own derived values for cross-validation. Isotherm physical plausibility (monotonic increase with pressure, higher uptake at lower temperature) is also verified. All fields needed by the checker are declared in the schema; no hidden columns or keys exist.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_isotherms_Ni.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Fugacity_bar",
          "Loading_mmol_g"
        ],
        "units": {
          "Temperature_K": "K",
          "Fugacity_bar": "bar",
          "Loading_mmol_g": "mmol/g"
        }
      },
      "description": "CO₂ adsorption isotherm from GCMC simulation for DICRO-3-Ni-i at 273, 283, and 293 K. The checker reads this file to verify physical plausibility (monotonicity with pressure, correct temperature ordering) and to independently recompute the zero-loading isosteric heat of adsorption via virial fitting and the Clausius-Clapeyron relation."
    },
    {
      "file": "step_02_isotherms_Cu.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Fugacity_bar",
          "Loading_mmol_g"
        ],
        "units": {
          "Temperature_K": "K",
          "Fugacity_bar": "bar",
          "Loading_mmol_g": "mmol/g"
        }
      },
      "description": "CO₂ adsorption isotherm from GCMC simulation for DICRO-3-Cu-i at 273, 283, and 293 K. The checker reads this file to verify physical plausibility and to independently recompute the zero-loading isosteric heat of adsorption."
    },
    {
      "file": "step_03_Qst_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "DICRO-3-Ni-i_zero_loading_Qst_kJmol": "number (float, kJ/mol)",
          "DICRO-3-Cu-i_zero_loading_Qst_kJmol": "number (float, kJ/mol)"
        }
      },
      "description": "Agent-derived zero-loading isosteric heat of adsorption for both materials. The checker independently recomputes Qst from the submitted isotherm CSVs and compares both the agent's reported values and the checker's recomputed values to the hidden paper-reported simulated Qst."
    }
  ],
  "notes": "The primary scored artifacts are the isotherm CSVs, from which the checker recomputes Qst. The Qst JSON provides the agent's own derived values for cross-validation. Isotherm physical plausibility (monotonic increase with pressure, higher uptake at lower temperature) is also verified. All fields needed by the checker are declared in the schema; no hidden columns or keys exist."
}
```

## How you are scored
A hidden verifier checks your submitted artifacts. For each isotherm CSV, it verifies physical plausibility (loading should increase monotonically with fugacity and decrease with increasing temperature). The verifier then independently fits a virial equation to your three‑temperature isotherm data and recomputes the zero‑loading isosteric heat of adsorption for each material. These recomputed Qst values are compared to hidden reference values. Your own reported Qst values in the JSON file are also cross‑checked against the verifier’s recomputed values. The total reward combines the weight of each check. Only performing the full simulation pipeline and providing real simulation output will satisfy these checks; simple reporting of a known numeric answer is not sufficient.
