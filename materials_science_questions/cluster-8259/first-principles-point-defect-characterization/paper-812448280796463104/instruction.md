# DFT investigation of C_N–O_N defect complexes in wurtzite GaN

## Problem background
Undoped GaN epilayers grown by metalorganic vapor phase epitaxy often exhibit a broad yellow luminescence band (YB) centered around 2.27 eV. Photoluminescence measurements suggest that this band arises from transitions between inner electronic levels of a defect complex involving residual carbon and oxygen impurities. Density functional theory (DFT) calculations have been employed to investigate the electronic structure of C- and O-related defect complexes and to identify which complex is responsible for the YB.

## Approach
The calculations use a 72-atom wurtzite GaN supercell. First, the perfect crystal band structure is computed to establish the conduction band minimum (E_C). Then, defect complexes are introduced by substituting host atoms with C and O impurities. Two types of complexes are considered: C_N–O_N (C replacing N and O replacing a nearby N) and C_Ga–O_N (C replacing Ga and O replacing N). For each complex, the atomic positions are relaxed, and the total density of states (TDOS) is calculated. The energy of the defect-induced state closest to E_C is tracked as a function of the C–O separation. In addition, total energies are computed for selected complexes to compare their relative stability. The comparison allows inference about which complex formation is energetically favorable and how the defect state position shifts with impurity distance.

## Reproduction target
Compute the total density of states (TDOS) for wurtzite GaN supercells containing C_N–O_N complexes at two C–O distances, approximately 5.18 Å and 3.17 Å. From the TDOS, extract the energy of the defect level closest to the conduction band minimum (E_C) relative to the perfect-crystal E_C. Report these values in `defect_state_energies.csv`.

Separately, compute the total energy of the C_N–O_N complex at approximately 3.17 Å and of the C_Ga–O_N complex at approximately 1.97 Å. Report these in `total_energies.csv`.

## Assets

- Wurtzite GaN crystal structure
- DFT code
- Pseudopotentials for Ga, N, C, O

## Workflow steps

### Step 1: Pristine supercell band structure
- Role: process
- Action: Construct a 72-atom wurtzite GaN supercell using standard lattice parameters (a≈3.189 Å, c≈5.185 Å). Relax atomic positions (and cell if appropriate) and compute the band structure. Identify the conduction band minimum (E_C) and valence band maximum (E_V); retain the relaxation log as evidence.
- Evidence: `/app/outputs/pristine_relax.log`

### Step 2: Defect state energies from TDOS
- Role: scored (load-bearing)
- Action: Create C_N–O_N complexes by substituting one N with C and a nearby N with O at approximate distances of 5.18 Å and 3.17 Å. Relax atomic positions. Compute the total density of states (TDOS). For each complex, locate the defect-induced state closest to the conduction band and report its energy relative to the perfect-cell E_C from step s01, together with the actual C–O distance used. Output a CSV with columns: distance_Angstrom, defect_state_energy_relative_to_E_C_eV, perfect_E_C_eV. Provide exactly two rows.
- Output file: `/app/outputs/defect_state_energies.csv`
- Format: csv
- Contract: distance_Angstrom (float), defect_state_energy_relative_to_E_C_eV (float), perfect_E_C_eV (float)
- Scoring: scored by hidden verifier

### Step 3: Total energy comparison of complexes
- Role: scored (load-bearing)
- Action: Compute the total energy of the C_N–O_N complex at approximately 3.17 Å and of a C_Ga–O_N complex (C substituting Ga, O substituting N) at approximately 1.97 Å, using the same DFT method as step s02. Output a CSV with columns: complex_name, total_energy_eV. Include exactly two rows with names 'C_N-O_N' and 'C_Ga-O_N'.
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: complex_name (string), total_energy_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_state_energies.csv`
- `/app/outputs/total_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_state_energies.csv
- path: `/app/outputs/defect_state_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Two rows giving the defect-state energy relative to the conduction band for C_N–O_N complexes at ~5.18 Å and ~3.17 Å. The checker applies a hidden threshold to the defect-state energies (for example, comparing the two rows).
- schema:
  - `type`: table
  - `required_columns`: `distance_Angstrom`, `defect_state_energy_relative_to_E_C_eV`, `perfect_E_C_eV`
  - `units`:
    - `distance_Angstrom`: angstrom
    - `defect_state_energy_relative_to_E_C_eV`: eV
    - `perfect_E_C_eV`: eV

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Two rows with total energies for C_N-O_N (3.17 Å) and C_Ga-O_N (1.97 Å). The checker applies a hidden threshold to the total energies (for example, comparing the two rows).
- schema:
  - `type`: table
  - `required_columns`: `complex_name`, `total_energy_eV`
  - `units`:
    - `total_energy_eV`: eV

Notes: Scoring is result-level (T0) against hidden paper-derived thresholds. The exact threshold values are not disclosed. The agent must compute both artifacts using a consistent DFT method; toolchain variations are absorbed by the thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_state_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_Angstrom",
          "defect_state_energy_relative_to_E_C_eV",
          "perfect_E_C_eV"
        ],
        "units": {
          "distance_Angstrom": "angstrom",
          "defect_state_energy_relative_to_E_C_eV": "eV",
          "perfect_E_C_eV": "eV"
        }
      },
      "description": "Two rows giving the defect-state energy relative to the conduction band for C_N–O_N complexes at ~5.18 Å and ~3.17 Å. The checker applies a hidden threshold to the defect-state energies (for example, comparing the two rows)."
    },
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex_name",
          "total_energy_eV"
        ],
        "units": {
          "total_energy_eV": "eV"
        }
      },
      "description": "Two rows with total energies for C_N-O_N (3.17 Å) and C_Ga-O_N (1.97 Å). The checker applies a hidden threshold to the total energies (for example, comparing the two rows)."
    }
  ],
  "notes": "Scoring is result-level (T0) against hidden paper-derived thresholds. The exact threshold values are not disclosed. The agent must compute both artifacts using a consistent DFT method; toolchain variations are absorbed by the thresholds."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that reads only the files you write under `/app/outputs`. The verifier checks each scored artifact independently. For each artifact, the verifier applies a hidden condition to the data (for example, comparing the two rows) to determine whether the computation reproduces the paper's conclusion. Both CSV files must conform to the exact column schemas described in the workflow steps (two rows each, header included). The overall reward is a weighted combination of the stage scores; the verifier’s thresholds are designed to absorb normal toolchain variation (e.g., pseudopotential or functional choices) while still requiring a correct reproduction of the qualitative trends.

There is no need to match any specific absolute energy values from a reference; the check is based on relative differences between the rows.
