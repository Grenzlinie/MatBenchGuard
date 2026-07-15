# Dipole moments of self-assembled monolayers of benzoic acid disulfides

## Problem background
Self-assembled monolayers (SAMs) of organic molecules on semiconductors or ferroelectrics can modify the surface electronic properties, enabling applications in molecular electronics and sensors. This task examines SAMs of symmetric disulfides of benzoic acid with functional elements X = H, F, Br. The key questions are: how do the functional elements and the intermolecular spacing affect the net dipole moment per molecule of the SAM, and how do the dipole moment and the HOMO-LUMO gap respond to an external electric field applied perpendicular to the monolayer? The goal is to compute these quantities and uncover the underlying trends using first-principles electronic structure calculations.

## Approach
The problem is approached via plane-wave density functional theory (DFT) calculations. For each combination of functional element (H, F, Br) and two intermolecular periodicities (7.81 Å and 11.7 Å), you will construct a periodic slab model of the SAM from the molecular structure of the symmetric disulfide. After relaxing the atomic positions (keeping the cell vectors fixed), static DFT calculations without an external field yield the total dipole moment along the direction perpendicular to the slab; dividing by the number of molecules gives the dipole moment per molecule. For the field-dependent study, additional DFT calculations are performed with a uniform external electric field applied along this direction at strengths of 0.0, 0.1, 0.2, and 0.3 V/Å, from which both the net dipole per molecule and the HOMO‑LUMO gap are extracted. An open-source DFT code such as Quantum ESPRESSO can be used for all calculations.

## Reproduction target
Produce the following two scored CSV artifacts under `/app/outputs`:

1. **Zero-field dipole moments** (`step_1_dipole_moments_zero_field.csv`): six rows covering X = H, F, Br for both intermolecular spacings (7.81 Å and 11.7 Å). Each row reports the dipole moment per molecule in Debye (positive means pointing in the +z direction).

2. **Field-dependent dipole moments and energy gaps** (`step_2_field_dependence.csv`): rows for X = H and F at both spacings, for every field strength (0.0, 0.1, 0.2, 0.3 V/Å). For each condition, record the dipole moment per molecule (Debye) and, where computed, the HOMO‑LUMO gap (eV).

The objective is to investigate, from these computed results, the relative ordering of dipole moments among the different functional elements, the influence of intermolecular spacing, and the response of the dipole moment and energy gap to the applied electric field.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- ASE (Atomic Simulation Environment): https://gitlab.com/ase/ase
- Molecular structure generator (RDKit / Open Babel): rdkit, openbabel

## Workflow steps

### Step 1: Geometry optimization of SAM structures
- Role: process
- Action: For each combination of functional element X (H, F, Br) and intermolecular separation a=7.81 Å and 11.7 Å, construct a periodic slab model of the SAM using an initial molecular geometry for the symmetric disulfide of benzoic acid. Perform DFT geometry relaxation (relax atomic positions only, keeping cell vectors fixed) to obtain optimized coordinates. Save the relaxation log.
- Evidence: `/app/outputs/relax.log`

### Step 2: Zero-field dipole moments
- Role: scored (load-bearing)
- Action: Using the relaxed SAM structures from the previous step, run DFT static calculations (no external electric field) to compute the total dipole moment along the z-axis for each structure. Extract the dipole moment per molecule in Debye (positive means pointing in +z direction). Write the results to step_1_dipole_moments_zero_field.csv with columns X, separation_angstrom, dipole_D for all six conditions.
- Output file: `/app/outputs/step_1_dipole_moments_zero_field.csv`
- Format: csv
- Contract: Columns: X (string: H, F, Br), separation_angstrom (float: 7.81 or 11.7), dipole_D (float, in Debye, positive means +z direction). Exactly six rows.
- Scoring: scored by hidden verifier

### Step 3: Field-dependent dipole moments and energy gaps
- Role: scored
- Action: For X=H and F at intermolecular separations a=7.81 Å and 11.7 Å, run DFT calculations with an external electric field applied perpendicular to the slab (along z) at field strengths 0.0, 0.1, 0.2, 0.3 V/Å. For each condition compute the net dipole moment per molecule (in Debye) and the HOMO-LUMO gap (in eV). For the a=11.7 Å case, computing the energy gap is optional. Write the results to step_2_field_dependence.csv with columns X, separation_angstrom, field_V_Ang, dipole_D, energy_gap_eV. Include all field combinations for X=H,F at both spacings; for a=11.7, leave energy_gap_eV empty if not computed.
- Output file: `/app/outputs/step_2_field_dependence.csv`
- Format: csv
- Contract: Columns: X (string: H or F), separation_angstrom (float: 7.81 or 11.7), field_V_Ang (float: 0.0, 0.1, 0.2, 0.3), dipole_D (float, Debye), energy_gap_eV (float, eV, may be empty for a=11.7). Rows: all field combinations for X=H,F at both spacings.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_1_dipole_moments_zero_field.csv`
- `/app/outputs/step_2_field_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_1_dipole_moments_zero_field.csv
- path: `/app/outputs/step_1_dipole_moments_zero_field.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zero-field molecular dipole moments for SAMs of symmetric disulfides of benzoic acid with functional elements H, F, Br at intermolecular spacings 7.81 Å and 11.7 Å. The checker compares these values to hidden reference results and assesses trends (sign ordering, spacing dependence).
- schema:
  - `type`: table
  - `required_columns`: `X`, `separation_angstrom`, `dipole_D`
  - `units`:
    - `dipole_D`: Debye
    - `separation_angstrom`: angstrom

### step_2_field_dependence.csv
- path: `/app/outputs/step_2_field_dependence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dipole moments and energy gaps under applied external electric fields. The checker compares values to hidden reference results and verifies the nonlinear response (monotonic decrease with field).
- schema:
  - `type`: table
  - `required_columns`: `X`, `separation_angstrom`, `field_V_Ang`, `dipole_D`, `energy_gap_eV`
  - `units`:
    - `dipole_D`: Debye
    - `energy_gap_eV`: eV
    - `field_V_Ang`: V/angstrom
    - `separation_angstrom`: angstrom

Notes: The checker will compare the agent's reported dipole moments and energy gaps to expected values within tolerance and check qualitative trends (sign of H dipole, ordering of F and Br magnitudes, decrease with spacing, and field dependence).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_1_dipole_moments_zero_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "X",
          "separation_angstrom",
          "dipole_D"
        ],
        "units": {
          "dipole_D": "Debye",
          "separation_angstrom": "angstrom"
        }
      },
      "description": "Zero-field molecular dipole moments for SAMs of symmetric disulfides of benzoic acid with functional elements H, F, Br at intermolecular spacings 7.81 Å and 11.7 Å. The checker compares these values to hidden reference results and assesses trends (sign ordering, spacing dependence)."
    },
    {
      "file": "step_2_field_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "X",
          "separation_angstrom",
          "field_V_Ang",
          "dipole_D",
          "energy_gap_eV"
        ],
        "units": {
          "dipole_D": "Debye",
          "energy_gap_eV": "eV",
          "field_V_Ang": "V/angstrom",
          "separation_angstrom": "angstrom"
        }
      },
      "description": "Dipole moments and energy gaps under applied external electric fields. The checker compares values to hidden reference results and verifies the nonlinear response (monotonic decrease with field)."
    }
  ],
  "notes": "The checker will compare the agent's reported dipole moments and energy gaps to expected values within tolerance and check qualitative trends (sign of H dipole, ordering of F and Br magnitudes, decrease with spacing, and field dependence)."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage’s artifact. For the zero-field dipole moment file, it checks the computed values against expected references and verifies the qualitative trends in sign ordering and spacing dependence. For the field-dependent file, it compares the reported dipole moments and energy gaps to expected references and validates the monotonic behavior with increasing field. The verifier combines these per-stage scores by weight into a single final reward in [0,1]. The scoring is based on the accuracy of the computed numbers and the presence of the required trends; the verifier’s reference values and tolerances are not disclosed. No manual inspection is involved.
