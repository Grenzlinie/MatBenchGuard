# Compute standard isobaric potentials for metal/oxide reactions with HCl and HF

## Problem background
During sintering of alloy steels in the presence of ammonium halide additions, the atmosphere contains HCl and HF. Metal and oxide species in the steel may react with these gases to form volatile halides, potentially affecting the final properties of the sintered material. To understand the thermodynamic feasibility of such reactions, the standard isobaric potentials (ΔZ⁰) of a set of 11 reactions between Cr, Fe, Ni, Si, Al (and their oxides) and HCl were computed as functions of temperature, along with the analogous set of reactions with HF. Additionally, for one reaction the isobaric potential under non‑standard conditions representative of real sintering atmospheres (alloy activity, varying HCl concentration) was estimated. This task requires you to compute these thermodynamic quantities using publicly available thermochemical data.

## Approach
The standard isobaric potential ΔZ⁰ for each reaction is obtained by the indirect combination method. You will obtain standard thermochemical data (enthalpies of formation, entropies, and temperature‑dependent heat capacities) for all species involved from a public database such as NIST‑JANAF. For each species, compute its Gibbs free energy of formation at the required temperatures by integrating the heat capacity (Kirchhoff integration). Combine these formation energies according to the stoichiometry of the reaction, including corrections for any phase transitions (melting, sublimation, boiling) using phase‑transition temperatures from standard handbooks. This yields ΔZ⁰ for the reaction. For non‑standard conditions, the isobaric potential ΔZ is computed from ΔZ⁰ plus a correction term that accounts for the activities of the components (derived from the gas‑phase composition, the activity of chromium in the alloy, and the equilibrium constant of the reaction). Reproduce the calculations for HCl reactions, the analogous HF reactions, and the selected non‑standard case as described in the workflow steps.

## Reproduction target
Compute the standard isobaric potential ΔZ⁰ (kJ/mol) for each of the 11 reactions with HCl and the 11 analogous reactions with HF at the temperatures 1000 K, 1200 K, and 1400 K. Write the results to /app/outputs/dZ_HCl.csv and /app/outputs/dZ_HF.csv respectively. Then, for reaction (1) under non‑standard conditions (chromium activity a_Cr = 0.17, HCl concentrations 5 %, 20 %, 50 %), compute ΔZ (kJ/mol) at 815 °C, 1300 °C, and 1500 °C and write the results to /app/outputs/dZ_nonstandard.csv. All computations must be performed using publicly available thermochemical data, and the outputs must follow the exact CSV schemas specified below.

## Assets

- NIST-JANAF Thermochemical Tables: https://janaf.nist.gov/
- Standard reference data for melting, sublimation, and boiling points of inorganic compounds

## Workflow steps

### Step 1: Compute standard isobaric potentials for HCl reactions
- Role: scored
- Action: For each of the 11 reactions with HCl listed in the paper, obtain necessary thermochemical data (standard enthalpies, entropies, heat capacity coefficients) for all species from NIST‑JANAF or equivalent public database. Compute ΔG_f°(T) for each species using Kirchhoff integration of temperature‑dependent heat capacities. Combine according to the reaction stoichiometries, including corrections for phase changes (melting, sublimation, boiling) using the compiled phase‑transition temperatures. Output the standard isobaric potential ΔZ^0 (kJ/mol) at 1000 K, 1200 K, and 1400 K.
- Output file: `/app/outputs/dZ_HCl.csv`
- Format: csv
- Contract: CSV with columns: reaction_id (integer 1‑11), T_K (float: 1000.0, 1200.0, 1400.0), dZ_kJ_per_mol (float, kJ/mol).
- Scoring: scored by hidden verifier

### Step 2: Compute standard isobaric potentials for HF reactions
- Role: scored
- Action: Analogous to step_01 but for the 11 reactions with HF (fluorides). Use available thermochemical data; for fluorides apply approximate phase‑transition temperatures (melting/boiling in the range 1000–1100 °C) as indicated in the paper. Output ΔZ^0 (kJ/mol) at the same three temperatures.
- Output file: `/app/outputs/dZ_HF.csv`
- Format: csv
- Contract: CSV with columns: reaction_id (integer 1‑11), T_K (float: 1000.0, 1200.0, 1400.0), dZ_kJ_per_mol (float, kJ/mol).
- Scoring: scored by hidden verifier

### Step 3: Compute non‑standard isobaric potential for CrCl₂ formation
- Role: scored
- Action: Using the standard ΔZ^0(T) for reaction (1) from step_01, compute the non‑standard isobaric potential ΔZ under the following conditions: chromium activity a_Cr = 0.17, hydrogen chloride activity a_HCl = 0.05, 0.20, 0.50, and hydrogen activity a_H₂ = 1 − a_HCl. Determine the activity of CrCl₂ from the equilibrium constant K_r (use ΔH° and ΔS° of reaction (1), neglecting the heat capacity of gaseous CrCl₂). Apply ΔZ = ΔZ^0 + RT ln( a_CrCl₂^{1/2} a_H₂^{1/2} / (a_Cr^{1/2} a_HCl) ) at three temperatures: 815 °C, 1300 °C, and 1500 °C. Use the same thermochemical data and phase corrections as in step_01. Output ΔZ (kJ/mol) for each combination of temperature and HCl fraction.
- Output file: `/app/outputs/dZ_nonstandard.csv`
- Format: csv
- Contract: CSV with columns: reaction_id (integer 1), T_C (float: 815.0, 1300.0, 1500.0), HCl_pct (float: 5.0, 20.0, 50.0), dZ_kJ_per_mol (float, kJ/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dZ_HCl.csv`
- `/app/outputs/dZ_HF.csv`
- `/app/outputs/dZ_nonstandard.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dZ_HCl.csv
- path: `/app/outputs/dZ_HCl.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Standard isobaric potentials ΔZ^0 for 11 HCl reactions at 1000, 1200, 1400 K. Units: kJ/mol.
- schema:
  - `type`: table
  - `required_columns`: `reaction_id`, `T_K`, `dZ_kJ_per_mol`
  - `column_types`:
    - `reaction_id`: int
    - `T_K`: float
    - `dZ_kJ_per_mol`: float

### dZ_HF.csv
- path: `/app/outputs/dZ_HF.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Standard isobaric potentials ΔZ^0 for the 11 analogous HF reactions at 1000, 1200, 1400 K. Units: kJ/mol.
- schema:
  - `type`: table
  - `required_columns`: `reaction_id`, `T_K`, `dZ_kJ_per_mol`
  - `column_types`:
    - `reaction_id`: int
    - `T_K`: float
    - `dZ_kJ_per_mol`: float

### dZ_nonstandard.csv
- path: `/app/outputs/dZ_nonstandard.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Non‑standard isobaric potential ΔZ for reaction (1) under the specified Cr activity and HCl concentrations. Temperatures in °C, HCl fraction in %, ΔZ in kJ/mol.
- schema:
  - `type`: table
  - `required_columns`: `reaction_id`, `T_C`, `HCl_pct`, `dZ_kJ_per_mol`
  - `column_types`:
    - `reaction_id`: int
    - `T_C`: float
    - `HCl_pct`: float
    - `dZ_kJ_per_mol`: float

Notes: All thermochemical data must be obtained from publicly available databases such as NIST‑JANAF. Phase transition temperatures (particularly for fluorides) are approximate and should be taken from standard handbooks; the paper notes a 1000–1100 °C range for fluoride melting/boiling points.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dZ_HCl.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_id",
          "T_K",
          "dZ_kJ_per_mol"
        ],
        "column_types": {
          "reaction_id": "int",
          "T_K": "float",
          "dZ_kJ_per_mol": "float"
        }
      },
      "description": "Standard isobaric potentials ΔZ^0 for 11 HCl reactions at 1000, 1200, 1400 K. Units: kJ/mol."
    },
    {
      "file": "dZ_HF.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_id",
          "T_K",
          "dZ_kJ_per_mol"
        ],
        "column_types": {
          "reaction_id": "int",
          "T_K": "float",
          "dZ_kJ_per_mol": "float"
        }
      },
      "description": "Standard isobaric potentials ΔZ^0 for the 11 analogous HF reactions at 1000, 1200, 1400 K. Units: kJ/mol."
    },
    {
      "file": "dZ_nonstandard.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_id",
          "T_C",
          "HCl_pct",
          "dZ_kJ_per_mol"
        ],
        "column_types": {
          "reaction_id": "int",
          "T_C": "float",
          "HCl_pct": "float",
          "dZ_kJ_per_mol": "float"
        }
      },
      "description": "Non‑standard isobaric potential ΔZ for reaction (1) under the specified Cr activity and HCl concentrations. Temperatures in °C, HCl fraction in %, ΔZ in kJ/mol."
    }
  ],
  "notes": "All thermochemical data must be obtained from publicly available databases such as NIST‑JANAF. Phase transition temperatures (particularly for fluorides) are approximate and should be taken from standard handbooks; the paper notes a 1000–1100 °C range for fluoride melting/boiling points."
}
```

## How you are scored
A hidden verifier will independently evaluate your three output files. For the standard potentials (dZ_HCl.csv and dZ_HF.csv), the verifier checks that your computed ΔZ⁰ values exhibit the thermodynamically expected temperature dependence and relative ordering among the reactions, and that their magnitudes fall within acceptable ranges derived from reference data. For dZ_nonstandard.csv, the verifier checks that your ΔZ values at each condition are consistent with the activity correction and fall within acceptable agreement with independently derived reference values. Your final score is a weighted combination of these checks (each stage carries a share of the total weight). Reporting a value is not sufficient; the calculation must be correctly performed.
