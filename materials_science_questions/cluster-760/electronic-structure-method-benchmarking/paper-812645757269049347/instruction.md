# Ab Initio and Bond‑Additivity‑Corrected Enthalpies of Formation for Chlorofluoromethanes

## Problem background
Accurate thermochemical data for chlorofluorocarbons (CFCs) are essential for the design of fire suppression agents and for kinetic modeling of atmospheric chemistry. However, experimental enthalpies of formation for many CFCs are either scarce or have large uncertainties. Quantum chemical composite methods offer a route to predict these enthalpies, but they may suffer from systematic errors that grow with the number of carbon‑halogen bonds. Bond additivity corrections (BACs) have been proposed to compensate for such systematic errors. This task investigates whether the G2, G2(MP2), CBS‑4, and CBS‑Q composite methods, combined with BACs, can yield accurate enthalpies of formation for the series of chlorofluoromethanes when compared to accepted experimental reference values.

## Approach
The core idea is to compute the enthalpies of formation at 298.15 K for 15 methane derivatives (fluoromethanes, chloromethanes, and chlorofluoromethanes) using four well‑established composite ab initio methods: G2, G2(MP2), CBS‑4, and CBS‑Q. These methods perform a series of lower‑level calculations (geometry optimizations, frequency analyses, single‑point energy evaluations) to obtain an accurate estimate of the ground‑state electronic energy. From the electronic energy, the standard enthalpy of formation can be derived via atomization energies and known atomic enthalpies of formation of the elements.

Because the direct ab initio enthalpies may contain systematic errors that depend on the number of C–F and C–Cl bonds, a bond additivity correction is applied. The corrected enthalpy is calculated as:
ΔfH°(BAC) = ΔfH°(uncorrected) – (n_CF × Δ_CF + n_CCl × Δ_CCl)
where n_CF and n_CCl are the numbers of C–F and C–Cl bonds in the molecule, and Δ_CF, Δ_CCl are method‑specific correction parameters provided in the task resources. (The C–H bond correction is set to zero.)
The corrected enthalpies are then compared to experimental enthalpies of formation supplied in the resources to evaluate the performance of each method.

## Reproduction target
The concrete objective is to produce two scored artifacts.

First, for each of the 15 molecules (CH4, CH3F, CH2F2, CHF3, CF4, CH3Cl, CH2Cl2, CHCl3, CCl4, CH2FCl, CHF2Cl, CF3Cl, CHFCl2, CF2Cl2, CFCl3) and for each of the four methods (G2, G2(MP2), CBS‑4, CBS‑Q), compute both the uncorrected and the BAC‑corrected enthalpy of formation (ΔfH°) at 298.15 K in kJ/mol. Also compute the deviation of each enthalpy from the corresponding experimental value (Δ(calc) – ΔfH°(expt)). Record the results as species, method, enthalpy_type (uncorrected/corrected), delta_H, and deviation_from_expt. Write this table to /app/outputs/step_03_enthalpies.csv.

Second, using only the corrected enthalpies, compute per‑method root‑mean‑square deviation (rms_deviation) and average deviation (avg_deviation) from experiment, and write the summary to /app/outputs/step_04_summary.csv with columns method, enthalpy_type (always ‘corrected’), rms_deviation, and avg_deviation.

## Provided Reference Data

The following experimental enthalpies of formation (ΔfH° at 298.15 K, kJ/mol) are to be used for deviation calculations.

| Species | ΔfH° (expt) |
|---------|-------------|
| CH4     | -74.9       |
| CH3F    | -232.6      |
| CH2F2   | -452.2      |
| CHF3    | -697.6      |
| CF4     | -933.0      |
| CH3Cl   | -83.7       |
| CH2Cl2  | -95.5       |
| CHCl3   | -103.2      |
| CCl4    | -96.0       |
| CH2FCl  | -261.9      |
| CHF2Cl  | -481.6      |
| CF3Cl   | -707.9      |
| CHFCl2  | -283.3      |
| CF2Cl2  | -491.6      |
| CFCl3   | -288.7      |

The BAC correction parameters (Δ_CF, Δ_CCl in kJ/bond) for each method are:

| Method    | Δ_CF  | Δ_CCl  |
|-----------|-------|--------|
| G2        | -6.51 | -2.80  |
| G2(MP2)   | -7.98 | -6.54  |
| CBS-4     | -1.28 | -10.62 |
| CBS-Q     | -3.51 | -8.50  |

Access to a quantum chemistry package (e.g., PySCF) is still required.

## Workflow steps

### Step 1: Compute electronic energies and uncorrected enthalpies
- Role: process
- Action: For each of the 15 molecules (CH4, CH3F, CH2F2, CHF3, CF4, CH3Cl, CH2Cl2, CHCl3, CCl4, CH2FCl, CHF2Cl, CF3Cl, CHFCl2, CF2Cl2, CFCl3), run the G2, G2(MP2), CBS‑4, and CBS‑Q composite methods to obtain ground‑state electronic energies. Convert the electronic energies to uncorrected standard enthalpies of formation at 298.15 K using the built‑in atomic reference data of each composite method. This step produces the uncorrected ΔfH° values that are used in the next step.
- Evidence: `/app/outputs/compute_energies.log`

### Step 2: Tabulate uncorrected and BAC‑corrected enthalpies of formation
- Role: scored (load-bearing)
- Action: From the uncorrected enthalpies of the previous step and the provided BAC parameters (Δ_CF, Δ_CCl per method), compute corrected enthalpies using the formula: ΔfH°(BAC) = ΔfH°(uncorrected) – (n_CF * Δ_CF + n_CCl * Δ_CCl). Collect all results — species, method (G2, G2(MP2), CBS‑4, CBS‑Q), enthalpy_type ('uncorrected' or 'corrected'), delta_H (kJ/mol), and deviation_from_expt (calculated minus experimental value, using the provided experimental enthalpies). Write the data to /app/outputs/step_03_enthalpies.csv.
- Output file: `/app/outputs/step_03_enthalpies.csv`
- Format: csv
- Contract: species (string), method (string, one of G2,G2(MP2),CBS‑4,CBS‑Q), enthalpy_type (string: 'uncorrected' or 'corrected'), delta_H (float, kJ/mol), deviation_from_expt (float, kJ/mol)
- Scoring: scored by hidden verifier

### Step 3: Compute RMS and mean deviations of corrected enthalpies
- Role: scored
- Action: Using the corrected delta_H values from step_03_enthalpies.csv and the provided experimental enthalpies, compute per‑method root‑mean‑square deviation (rms_deviation) and average deviation (avg_deviation) for the corrected results. Write the summary to /app/outputs/step_04_summary.csv.
- Output file: `/app/outputs/step_04_summary.csv`
- Format: csv
- Contract: method (string), enthalpy_type (string, 'corrected'), rms_deviation (float, kJ/mol), avg_deviation (float, kJ/mol)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_enthalpies.csv`
- `/app/outputs/step_04_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_enthalpies.csv
- path: `/app/outputs/step_03_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of uncorrected and BAC‑corrected enthalpies of formation (ΔfH° at 298.15 K) for each molecule and method, together with deviations from the provided experimental references.
- schema:
  - `type`: table
  - `required_columns`: `species`, `method`, `enthalpy_type`, `delta_H`, `deviation_from_expt`
  - `units`:
    - `delta_H`: kJ/mol
    - `deviation_from_expt`: kJ/mol

### step_04_summary.csv
- path: `/app/outputs/step_04_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per‑method RMS and average deviations of corrected enthalpies from experiment.
- schema:
  - `type`: table
  - `required_columns`: `method`, `enthalpy_type`, `rms_deviation`, `avg_deviation`
  - `units`:
    - `rms_deviation`: kJ/mol
    - `avg_deviation`: kJ/mol

Notes: The hidden checker reads step_03_enthalpies.csv, joins it with hidden experimental enthalpies, recomputes per‑method RMS and mean deviation for corrected values, and compares both the per‑entry corrected enthalpies and the recomputed RMS/mean to the paper‑reported gold with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "method",
          "enthalpy_type",
          "delta_H",
          "deviation_from_expt"
        ],
        "units": {
          "delta_H": "kJ/mol",
          "deviation_from_expt": "kJ/mol"
        }
      },
      "description": "Table of uncorrected and BAC‑corrected enthalpies of formation (ΔfH° at 298.15 K) for each molecule and method, together with deviations from the provided experimental references."
    },
    {
      "file": "step_04_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "enthalpy_type",
          "rms_deviation",
          "avg_deviation"
        ],
        "units": {
          "rms_deviation": "kJ/mol",
          "avg_deviation": "kJ/mol"
        }
      },
      "description": "Per‑method RMS and average deviations of corrected enthalpies from experiment."
    }
  ],
  "notes": "The hidden checker reads step_03_enthalpies.csv, joins it with hidden experimental enthalpies, recomputes per‑method RMS and mean deviation for corrected values, and compares both the per‑entry corrected enthalpies and the recomputed RMS/mean to the paper‑reported gold with tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares your produced numbers to a set of reference values (the paper’s reported results) using appropriate tolerances. The verifier examines each scored file independently.

- step_03_enthalpies.csv: both the uncorrected and corrected delta_H values and their deviations are compared. The primary check is on the corrected enthalpies; the uncorrected ones may carry lower weight. The verifier expects close agreement for all 15 molecules across the four methods.
- step_04_summary.csv: the per‑method RMS and average deviations are compared to the expected values.

The final reward is a weighted combination of the scores from the two files, with the enthalpies file carrying the dominant weight. A submission that merely reports numbers without running the actual quantum chemical calculations is unlikely to match the hidden reference within the required tolerances. The exact tolerances and weighting are not disclosed.
