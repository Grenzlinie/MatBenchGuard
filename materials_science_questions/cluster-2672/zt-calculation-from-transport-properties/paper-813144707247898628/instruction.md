# Thermodynamic Evaluation of Oxide Impurity Reduction Explaining Lattice Parameter Shifts in RuIn₃

## Problem background
The intermetallic compound RuIn₃ is a narrow-gap semiconductor with promising thermoelectric properties. Chemical substitution of the Ru site with transition metals such as Re, Rh, or Ir can tune the charge carrier concentration. During high-temperature synthesis using commercial elemental powders, oxide impurities—particularly RuO₂—may participate in redox reactions with the liquid metal flux, consuming indium or zinc and forming secondary oxide phases. The RuIn₃ phase also exhibits a homogeneity range, leading to systematic variations in the c lattice parameter. Understanding the thermodynamic driving force of these reduction reactions is essential for interpreting the resulting lattice parameters and compositions.

## Approach
**Thermodynamic analysis.** Compute the standard free reaction enthalpy ΔG(T) for eight redox reactions involving RuO₂, Rh₂O₃, IrO₂, and ReO₂ with metallic In, Zn, Rh, Ir, and Re. Use the provided thermochemical data (ΔH⁰_f(298), S⁰(298), and Cp(T) coefficients) and integrate heat capacities to evaluate ΔH(T) and ΔS(T), yielding ΔG(T) = ΔH(T) – T·ΔS(T) at temperatures from 300 to 1000 K. Normalize all ΔG values to one mole of the oxidizing agent. The resulting Ellingham-style table allows comparison of the relative stability of oxides. **Redox–lattice linkage.** Apply the thermodynamic results to predict, for four specific sample compositions, which reduction is most favored and whether indium or zinc is consumed, leading to an indium-poor or indium-rich matrix. Use the provided experimental c lattice parameters and the homogeneity-range endpoints to determine the experimentally observed side of the homogeneity range. Compare predictions and observations per sample.

## Reproduction target
Using the bundled thermochemical data file and the experimental lattice parameter/composition file, perform the following:
1. Compute ΔG for the eight reactions listed in workflow step 1 at 300, 400, 500, 600, 700, 800, 900, and 1000 K, and write them to `reaction_free_enthalpies.csv` with columns Reaction, Temperature_K, DeltaG_kJ_per_mol_R.
2. For each of the four samples (nominal compositions Ru₀.₉₅Re₀.₀₅In₃, Ru₀.₉₅Rh₀.₀₅In₃, Ru₀.₉₅Ir₀.₀₅In₃, and Ru₀.₉₅Ir₀.₀₅In₂.₉₅Zn₀.₀₅), use the computed ΔG ordering to predict the favored reduction, predicted secondary phase, and whether the matrix should be indium-poor or indium-rich. Compare the predicted side with the experimental c lattice parameter side (derived from the homogeneity-range endpoints provided in the experimental data file) and record the prediction, experimental measurement, and a consistency flag in `redox_analysis.json`.

## Assets

- Thermochemical data for oxides and elements
- Experimental lattice parameters and compositions

## Workflow steps

### Step 1: Compute free reaction enthalpies (Ellingham diagram)
- Role: scored (load-bearing)
- Action: Compute the standard free reaction enthalpy ΔG(T) for the eight redox reactions listed in the task (RuO₂ with In, Zn, Rh, Ir, Re; Rh₂O₃ with In; IrO₂ with In; ReO₂ with In) at temperatures 300, 400, 500, 600, 700, 800, 900, and 1000 K. Use thermodynamic integration of the provided heat‑capacity data from 298 K and normalize all values to one mole of the oxidizing agent. Output the results as a CSV table.
- Output file: `/app/outputs/reaction_free_enthalpies.csv`
- Format: csv
- Contract: Columns: Reaction (string), Temperature_K (int), DeltaG_kJ_per_mol_R (float). One row per reaction per temperature.
- Scoring: scored by hidden verifier

### Step 2: Redox‑driven lattice parameter consistency analysis
- Role: scored
- Action: Using the computed free enthalpies from step_01_enthalpies and the provided experimental data, predict which oxide reduction is most favored for each sample and whether indium (or zinc) is consumed, leading to an In‑poor or In‑rich matrix. For the four samples (Ru₀.₉₅Re₀.₀₅In₃, Ru₀.₉₅Rh₀.₀₅In₃, Ru₀.₉₅Ir₀.₀₅In₃, Ru₀.₉₅Ir₀.₀₅In₂.₉₅Zn₀.₀₅) assign the expected side of the homogeneity range, compare with the experimental c lattice parameter side derived from the provided homogeneity‑range endpoints, and output a JSON file recording the predictions, experimental readings, and consistency flags.
- Output file: `/app/outputs/redox_analysis.json`
- Format: json
- Contract: A JSON array of objects. Each object contains: sample (string), predicted_reduction (string), predicted_secondary_phase (string), expected_c_side (string, 'In‑poor' or 'In‑rich'), experimental_c_A (float), experimental_side (string, 'In‑poor' or 'In‑rich'), consistency (boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reaction_free_enthalpies.csv`
- `/app/outputs/redox_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reaction_free_enthalpies.csv
- path: `/app/outputs/reaction_free_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed free reaction enthalpy ΔG for each reaction and temperature, to be compared against a hidden reference derived from the same thermochemical data and the paper's reported Ellingham diagram.
- schema:
  - `type`: table
  - `required_columns`: `Reaction`, `Temperature_K`, `DeltaG_kJ_per_mol_R`
  - `units`:
    - `Temperature_K`: K
    - `DeltaG_kJ_per_mol_R`: kJ per mol of R

### redox_analysis.json
- path: `/app/outputs/redox_analysis.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: For each sample: the thermodynamically predicted reduction, secondary phase, expected homogeneity‑range side, the measured c parameter and its experimentally determined side, and a consistency flag. The hidden checker confirms the expected_c_side, experimental_side, and consistency flag exactly match the paper's conclusions.
- schema:
  - `type`: array
  - `items`:
    - `sample`: string
    - `predicted_reduction`: string
    - `predicted_secondary_phase`: string
    - `expected_c_side`: string
    - `experimental_c_A`: number
    - `experimental_side`: string
    - `consistency`: boolean

Notes: The output contract declares the exact schemas required for scoring. Step 1 is load‑bearing because the redox analysis depends on the computed ΔG values; without it the second step's predictions cannot be correctly derived. Step 2 is scored by exact match of categorical assignments and consistency flags, which are deterministic given the thermodynamic ordering and provided homogeneity‑range data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reaction_free_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Reaction",
          "Temperature_K",
          "DeltaG_kJ_per_mol_R"
        ],
        "units": {
          "Temperature_K": "K",
          "DeltaG_kJ_per_mol_R": "kJ per mol of R"
        }
      },
      "description": "Computed free reaction enthalpy ΔG for each reaction and temperature, to be compared against a hidden reference derived from the same thermochemical data and the paper's reported Ellingham diagram."
    },
    {
      "file": "redox_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "sample": "string",
          "predicted_reduction": "string",
          "predicted_secondary_phase": "string",
          "expected_c_side": "string",
          "experimental_c_A": "number",
          "experimental_side": "string",
          "consistency": "boolean"
        }
      },
      "description": "For each sample: the thermodynamically predicted reduction, secondary phase, expected homogeneity‑range side, the measured c parameter and its experimentally determined side, and a consistency flag. The hidden checker confirms the expected_c_side, experimental_side, and consistency flag exactly match the paper's conclusions."
    }
  ],
  "notes": "The output contract declares the exact schemas required for scoring. Step 1 is load‑bearing because the redox analysis depends on the computed ΔG values; without it the second step's predictions cannot be correctly derived. Step 2 is scored by exact match of categorical assignments and consistency flags, which are deterministic given the thermodynamic ordering and provided homogeneity‑range data."
}
```

## How you are scored
Your submitted artifacts are evaluated by an independent hidden verifier. For `reaction_free_enthalpies.csv`: the verifier recomputes the free reaction enthalpies from the same thermochemical data using a reference implementation and checks that your values are within an acceptable tolerance and that the relative ordering of reactions is correct. For `redox_analysis.json`: the verifier compares your predicted expected_c_side, experimental_side, and consistency flag against hidden gold assignments determined from the same experimental data and thermodynamic reasoning. The two stages are weighted and combined into a final reward. The scoring is monotonic: reporting a result that is more accurate or more consistent than the reference does not reduce your score. There is no single “correct” number beyond the tolerance, and you are not penalized for matching the target; your output is evaluated solely on whether the underlying computation and analysis are correctly performed.
