# DFT Formation Energy Calculation of Sb3Sn4

## Problem background
Accurate thermodynamic data for intermetallic compounds are essential for materials design and phase diagram modeling. In the binary Sb–Sn system, a recently identified stable intermetallic phase, Sb₃Sn₄, lacks thermodynamic information. Density‑functional theory (DFT) calculations can directly supply the formation enthalpy and relaxed crystal structure of such a compound, providing a crucial parameter for subsequent thermodynamic assessment. This task requires you to compute the formation energy and optimized lattice constants of Sb₃Sn₄ by performing an ab‑initio DFT calculation according to the procedure described below.

## Approach
The calculation uses DFT within the generalized gradient approximation (GGA), implemented in the open‑source Siesta code, together with GGA pseudopotentials for Sb and Sn obtained from the Siesta website. The crystal structure of Sb₃Sn₄ belongs to space group R 3 m, with initial lattice parameters a = 4.33111 Å and c = 37.302 Å reported in crystallographic literature. Starting from these initial guesses, a full geometry optimization is performed, relaxing both atomic positions and unit‑cell parameters. Additionally, the total energies of the pure elements in their ground‑state structures—Sb in the rhombohedral A7 phase and Sn in the body‑centered tetragonal A5 phase—are computed using the same computational settings. From the relaxed total energies, the formation energy per Sb₃Sn₄ formula unit is obtained as

  E_formation = E(Sb₃Sn₄ cell) − 3 × E(Sb atom) − 4 × E(Sn atom),

where the atomic reference energies are derived by dividing the relaxed total energies of the pure element unit cells by the number of atoms in each cell. The only required inputs are the publicly available Siesta code and pseudopotentials; no experimental data need to be downloaded.

## Reproduction target
Produce a JSON file named `step_01_dft_results.json` inside `/app/outputs`. The file must contain three numeric quantities:

- `formation_energy_J_per_mol` — the formation energy of Sb₃Sn₄ in joules per mole of formula unit.
- `lattice_parameter_a_angstrom` — the relaxed lattice constant **a** of the Sb₃Sn₄ unit cell (in Å).
- `lattice_parameter_c_angstrom` — the relaxed lattice constant **c** of the Sb₃Sn₄ unit cell (in Å).

These values must be obtained by executing the DFT workflow described in the approach and in the workflow step below. No other output files are required for scoring.

## Assets

- Siesta DFT code: https://departments.icmab.es/leem/siesta/
- GGA pseudopotentials for Sb and Sn: https://departments.icmab.es/leem/siesta/

## Workflow steps

### Step 1: DFT geometry optimization and formation energy of Sb3Sn4
- Role: scored (load-bearing)
- Action: Prepare input structures for Sb3Sn4 (space group R-3m, initial lattice parameters a=4.33111 Å, c=37.302 Å) and for pure Sb (rhombohedral A7) and Sn (bct A5) in their ground-state crystal structures. Perform DFT calculations using Siesta with GGA pseudopotentials for Sb and Sn, running full geometry optimization for each structure. Compute the formation energy per formula unit of Sb3Sn4 as E_formation = E(Sb3Sn4_cell) - 3*E(Sb_atom) - 4*E(Sn_atom), where the atomic reference energies are obtained by dividing the relaxed total energies of the pure element unit cells by the number of atoms per cell. Record the formation energy (in J/mol) and the relaxed lattice parameters a and c (in Å) of the Sb3Sn4 unit cell in a JSON file.
- Output file: `/app/outputs/step_01_dft_results.json`
- Format: json
- Contract: json object with keys `formation_energy_J_per_mol` (number, unit J/mol), `lattice_parameter_a_angstrom` (number, unit Å), `lattice_parameter_c_angstrom` (number, unit Å)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_dft_results.json
- path: `/app/outputs/step_01_dft_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: DFT-computed formation energy and relaxed lattice constants of Sb3Sn4 intermetallic compound.
- schema:
  - `type`: object
  - `required`:
    - `formation_energy_J_per_mol`: float (units: J/mol of Sb3Sn4)
    - `lattice_parameter_a_angstrom`: float (units: Å)
    - `lattice_parameter_c_angstrom`: float (units: Å)
  - `units`:
    - `formation_energy_J_per_mol`: J/mol
    - `lattice_parameter_a_angstrom`: Å
    - `lattice_parameter_c_angstrom`: Å
  - `description`: Formation energy per mole of Sb3Sn4 (more negative is acceptable) and the relaxed lattice constants of the unit cell (compared to paper values within tolerance).

Notes: The CALPHAD optimization and phase diagram calculation stages are not included because they require proprietary Thermo-Calc/Pandat software and digitized experimental data that are not publicly bundled. The DFT stage is fully self-contained.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "formation_energy_J_per_mol": "float (units: J/mol of Sb3Sn4)",
          "lattice_parameter_a_angstrom": "float (units: Å)",
          "lattice_parameter_c_angstrom": "float (units: Å)"
        },
        "units": {
          "formation_energy_J_per_mol": "J/mol",
          "lattice_parameter_a_angstrom": "Å",
          "lattice_parameter_c_angstrom": "Å"
        },
        "description": "Formation energy per mole of Sb3Sn4 (more negative is acceptable) and the relaxed lattice constants of the unit cell (compared to paper values within tolerance)."
      },
      "description": "DFT-computed formation energy and relaxed lattice constants of Sb3Sn4 intermetallic compound."
    }
  ],
  "notes": "The CALPHAD optimization and phase diagram calculation stages are not included because they require proprietary Thermo-Calc/Pandat software and digitized experimental data that are not publicly bundled. The DFT stage is fully self-contained."
}
```

## How you are scored
An automated hidden verifier scores your submission by checking the output of each scored workflow stage and combining the scores by weight into a final reward between 0 and 1. For this task the single scored stage is **Step 1** (the DFT formation energy and lattice parameters). The verifier reads your `step_01_dft_results.json` and compares the reported formation energy and lattice parameters to reference values, applying tolerances that account for genuine numerical differences between DFT implementations. You must produce these numbers by actually performing the geometry optimizations and energy calculations; reporting arbitrary constants without a real DFT run will likely receive a low score because the tolerances are set to admit only results that arise from a correct execution of the workflow. The final reward reflects how well your computed values agree with the hidden reference.
