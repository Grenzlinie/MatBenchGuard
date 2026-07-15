# Ge Vacancy Formation Energy vs Rhombohedral Distortion in GeTe

## Problem background
Rhombohedral GeTe is a promising thermoelectric material whose p-type electrical conduction is dominated by native Ge vacancies. Understanding what controls the concentration of these vacancies is essential for optimizing its performance. This task investigates how the formation energy of intrinsic point defects—particularly Ge vacancies—changes with the degree of rhombohedral distortion. The material's lattice can be described by an interaxial angle α; as α increases, the structure approaches the more symmetric cubic phase. The central aim is to compute the Ge-vacancy formation energy at the valence band maximum for a series of interaxial angles and to determine whether a systematic relationship exists between the lattice distortion and the ease of vacancy formation.

## Approach
Density functional theory (DFT) will be used to calculate total energies of rhombohedral GeTe in various configurations. Primitive cells corresponding to five interaxial angles (57.802°, 58°, 58.5°, 59°, 59.5°) will be constructed and then expanded to 2×2×2 supercells. For each angle, total energies will be obtained for the pristine supercell, elemental Ge and Te references, and supercells containing single intrinsic defects: Ge vacancy, Te vacancy, Te-on-Ge antisite, and Ge-on-Te antisite. All calculations will be performed with Quantum ESPRESSO using standard pseudopotentials from the SSSP library. From the collected total energies, defect formation energies will be derived as a function of the Fermi level under both Ge-rich and Te-rich chemical potential conditions. The formation energy at the valence band maximum (Fermi energy = 0) will be extracted for each defect, condition, and angle combination. The investigation focuses on the trend of the Ge vacancy formation energy with α under Ge-rich conditions.

## Reproduction target
Produce a CSV file named `formation_energy_summary.csv` containing the computed defect formation energies at the valence band maximum for all defect types, chemical conditions, and interaxial angles. The file must include, at a minimum, rows for the Ge vacancy under Ge-rich conditions at angles 57.802°, 58°, 58.5°, 59°, and 59.5°. The value in each row should be the result of a first-principles DFT calculation as described, not a manually adjusted or externally sourced number.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBS pseudopotentials (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- Rhombohedral GeTe crystal structure parameters

## Workflow steps

### Step 1: Structure generation and DFT total energy calculations
- Role: process
- Action: Build rhombohedral GeTe primitive cells at interaxial angles 57.802°, 58°, 58.5°, 59°, 59.5°, construct 2×2×2 supercells for pristine GeTe, elemental Ge, elemental Te, and supercells with intrinsic defects (Ge vacancy, Te vacancy, Te_Ge antisite, Ge_Te antisite). Perform DFT total energy calculations using Quantum ESPRESSO, including ionic relaxation as needed. Save all total energies to a JSON file for later analysis.
- Evidence: `/app/outputs/dft_energies.json`

### Step 2: Defect formation energy analysis and output
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute the formation energy of each defect as a function of Fermi energy under both Ge-rich and Te-rich chemical potential conditions. For each defect, condition, and angle, extract the formation energy at the valence band maximum (Fermi energy = 0). Write a summary CSV containing all combinations.
- Output file: `/app/outputs/formation_energy_summary.csv`
- Format: csv
- Contract: Columns: angle (float, degrees), condition (string, one of 'Ge-rich' or 'Te-rich'), defect (string, one of 'Vac_Ge', 'Vac_Te', 'Te_Ge', 'Ge_Te'), formation_energy_at_VBM (float, eV). Must include rows for Vac_Ge under Ge-rich for all five angles.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energy_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energy_summary.csv
- path: `/app/outputs/formation_energy_summary.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed defect formation energies at the valence band maximum for intrinsic defects in rhombohedral GeTe at five interaxial angles. The checker will verify the structural properties of Ge vacancy formation energy under Ge-rich conditions: monotonic decrease with increasing angle, negative values for angles >= 59°, and consistency with hidden reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `angle`, `condition`, `defect`, `formation_energy_at_VBM`
  - `units`:
    - `formation_energy_at_VBM`: eV
    - `angle`: degree

Notes: Only the Ge vacancy (Vac_Ge) row under Ge-rich condition for each angle is scored; other rows are provided for completeness.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energy_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle",
          "condition",
          "defect",
          "formation_energy_at_VBM"
        ],
        "units": {
          "formation_energy_at_VBM": "eV",
          "angle": "degree"
        }
      },
      "description": "Computed defect formation energies at the valence band maximum for intrinsic defects in rhombohedral GeTe at five interaxial angles. The checker will verify the structural properties of Ge vacancy formation energy under Ge-rich conditions: monotonic decrease with increasing angle, negative values for angles >= 59°, and consistency with hidden reference values within tolerance."
    }
  ],
  "notes": "Only the Ge vacancy (Vac_Ge) row under Ge-rich condition for each angle is scored; other rows are provided for completeness."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that examines the `formation_energy_summary.csv` file. The verifier will check that the Ge vacancy formation energies satisfy the expected physical trends and fall within an acceptable tolerance of a reference dataset. Reporting plausible numbers without genuinely running the required DFT calculations will not suffice, as the verifier's checks are designed to detect inconsistencies. Precise scoring criteria and tolerance values are kept hidden to preserve the integrity of the reproduction task.
