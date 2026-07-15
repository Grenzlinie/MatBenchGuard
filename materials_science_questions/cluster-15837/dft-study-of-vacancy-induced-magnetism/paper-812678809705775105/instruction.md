# DFT study of vacancy-induced magnetism in In2S3: defect supercell calculations

## Problem background
Diluted magnetic semiconductors (DMS) with room-temperature ferromagnetism are promising for spintronic devices. This task investigates the microscopic origin of magnetism in Sm-doped In2S3 nanoparticles using first-principles density functional theory (DFT). The crystal structure of β-In2S3 contains intrinsic cation vacancies, and the introduction of rare-earth Sm3+ dopants may induce additional magnetic moments. The objective is to compute the total spin magnetic moment of several defect configurations to understand which structural features give rise to spin polarization.

## Approach
The study uses spin-polarized DFT with the generalized gradient approximation (GGA) and on-site Hubbard U corrections to treat strongly correlated electrons on In d and Sm f orbitals. Five supercell models of β-In2S3 are constructed: a perfect 16-formula-unit supercell, one with a sulfur vacancy (V_S), one with an indium vacancy (V_In), one where Sm substitutes for In (Sm_In), and a defect complex with both Sm_In and V_In. For each model, the atomic geometry is fully relaxed to minimize forces and stress, followed by a self-consistent field calculation from which the total magnetic moment is extracted. The calculations are performed using an open-source DFT code (e.g., Quantum ESPRESSO) with appropriate pseudopotentials and convergence settings. The key observable is the total magnetic moment of each defect configuration.

## Reproduction target
Compute and report the total magnetic moment (in μB) for each of the five defect supercell models of β-In2S3: pristine, V_S, V_In, Sm_In, and Sm_In+V_In. The results must be saved in a CSV file with columns 'model' and 'total_magnetic_moment_muB'.

## Assets

- Crystal structure of β-In2S3 (tetragonal, JCPDS 73-1366)
- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/
- GGA pseudopotentials (PBE PAW/ultrasoft from PSLibrary): https://pseudopotentials.quantum-espresso.org/
- Atomic Simulation Environment (ASE) or pymatgen: ase

## Workflow steps

### Step 1: Build defect supercell models
- Role: process
- Action: Construct a 16-formula-unit supercell of β-In2S3 (32 In, 48 S) from the public crystal structure. Create five models: pristine In32S48, one sulfur vacancy (V_S), one indium vacancy (V_In), one In substituted by Sm (Sm_In), and one Sm substitution plus one In vacancy (Sm_In+V_In). Save structures in standard format (e.g., QE input or CIF).
- Evidence: `/app/outputs/build_models.log`

### Step 2: Relax atomic geometries
- Role: process
- Action: For each of the five models, perform spin-polarized DFT geometry optimization using GGA+U with Hubbard U corrections for In d (5 eV) and Sm f (7.35 eV) orbitals. Use a plane-wave cutoff and k-point mesh consistent with the paper's method. Relax atomic positions until forces and total energy converge. Save final relaxed structures and total energies.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Compute total magnetic moments
- Role: scored (load-bearing)
- Action: Using the relaxed structures, run a spin-polarized self-consistent field (SCF) calculation with the same DFT settings to converge the electronic ground state. Extract the total magnetic moment (in μB) for each model. Report results in a CSV file named magnetic_moments.csv.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: CSV with header: model (string, one of pristine, V_S, V_In, Sm_In, Sm_In+V_In), total_magnetic_moment_muB (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total magnetic moment for each of the five defect supercell models: pristine, V_S, V_In, Sm_In, Sm_In+V_In.
- schema:
  - `type`: table
  - `required_columns`: `model`, `total_magnetic_moment_muB`
  - `units`:
    - `total_magnetic_moment_muB`: μB

Notes: Verification compares the reported total magnetic moments against known paper reference values using a tolerance; the scoring uses linear-decay closeness (reference_match style). Only the magnetic moments are scored; band structures and formation energies are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "total_magnetic_moment_muB"
        ],
        "units": {
          "total_magnetic_moment_muB": "μB"
        }
      },
      "description": "Total magnetic moment for each of the five defect supercell models: pristine, V_S, V_In, Sm_In, Sm_In+V_In."
    }
  ],
  "notes": "Verification compares the reported total magnetic moments against known paper reference values using a tolerance; the scoring uses linear-decay closeness (reference_match style). Only the magnetic moments are scored; band structures and formation energies are not required."
}
```

## How you are scored
A hidden verifier will compare your reported total magnetic moments against a reference set derived from the original study. The scoring rewards values that fall within a tolerance that accounts for differences in DFT implementations and pseudopotentials. The overall score is a weighted combination of these checks.
