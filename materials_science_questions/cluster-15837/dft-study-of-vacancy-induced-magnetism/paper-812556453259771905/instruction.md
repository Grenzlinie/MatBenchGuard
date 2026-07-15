# Magnetic moments of doped penta-graphene bilayers from DFT

## Problem background
Penta-graphene (PG) is a two-dimensional carbon allotrope with a pentagonal lattice composed of both sp² and sp³ hybridized carbon layers. In bilayer stacks, this structure provides multiple distinct atomic sites for substitutional doping, making PG a flexible platform for tuning electronic and magnetic properties. This task investigates how replacing a single carbon atom in the top layer of a PG bilayer with boron (B), nitrogen (N), or oxygen (O) at different crystallographic positions (sp²-in, sp³, sp²-out) affects the system's total spin magnetic moment, computed from first-principles density functional theory (DFT).

## Approach
Build the atomic models of a pristine penta-graphene bilayer and nine substitutionally doped configurations (B, N, O at the sp²-in, sp³, and sp²-out sites of the upper layer). For each system, perform a spin-polarized DFT geometry relaxation to obtain the ground-state structure, using the SIESTA code with a double-ζ plus polarization (DZP) basis set, the GGA/PBE functional with van der Waals corrections, and Troullier–Martins pseudopotentials. After convergence, extract the total spin magnetic moment |m| for each configuration. The sequence of structures (pristine and nine doped systems) covers the doping combinations whose magnetic response the task aims to reproduce.

## Reproduction target
Compute the total spin magnetic moment |m| (in Bohr magnetons, µ_B) per unit cell for each of the ten bilayer configurations: pristine, B-sp2-in, B-sp3, B-sp2-out, O-sp2-in, O-sp3, O-sp2-out, N-sp2-in, N-sp3, and N-sp2-out. Write the results to a CSV file (`magnetic_moments.csv`) with exactly ten rows and two columns: 'configuration' and 'magnetic_moment'.

## Assets

- SIESTA (open-source DFT code): https://departments.icmab.es/leem/siesta/
- Troullier-Martins pseudopotentials for C, B, N, O: https://departments.icmab.es/leem/siesta/Databases/Pseudopotentials/PseudoPotentialData/

## Workflow steps

### Step 1: Construct initial atomic models
- Role: process
- Action: Build the pristine penta-graphene bilayer supercell and generate initial atom coordinates for the nine substitutionally doped bilayers (B, N, O at sp2-in, sp3, sp2-out sites) from the known PG structure and doping positions described in the paper.
- Evidence: none

### Step 2: Spin-polarized DFT geometry optimization
- Role: process
- Action: For each of the 10 configurations, run SIESTA with spin-polarized DFT using the DZP basis, GGA/PBE+vDW functional, Troullier-Martins pseudopotentials, a 15×15×1 Monkhorst-Pack k-point grid, mesh cutoff of 200 Ry, and force convergence criterion of 0.001 eV/Å. Allow the atomic positions to relax to the ground state.
- Evidence: `/app/outputs/siesta_outputs.tar.gz`

### Step 3: Extract magnetic moments
- Role: scored (load-bearing)
- Action: From each SIESTA output, extract the total spin magnetic moment (|m|, in Bohr magnetons per unit cell). Write a CSV file with columns 'configuration' and 'magnetic_moment' containing one row per configuration.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: Columns: configuration (string), magnetic_moment (float, Bohr magnetons). Exactly 10 rows.
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
- target_policy: exact_match
- description: The computed magnetic moments for each doping configuration.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `magnetic_moment`
  - `units`:
    - `magnetic_moment`: µ_B

Notes: The hidden checker compares the reported magnetic moments to reference values with an appropriate tolerance. No formation energies, band structures, or PDOS are required; only the magnetic moments are scored.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "magnetic_moment"
        ],
        "units": {
          "magnetic_moment": "µ_B"
        }
      },
      "description": "The computed magnetic moments for each doping configuration."
    }
  ],
  "notes": "The hidden checker compares the reported magnetic moments to reference values with an appropriate tolerance. No formation energies, band structures, or PDOS are required; only the magnetic moments are scored."
}
```

## How you are scored
A hidden verifier reads the submitted `magnetic_moments.csv` and compares the reported magnetic moments to reference values for the same configurations. The reward is a single float in [0,1] that reflects how close the computed moments are to the expected results. No other artifacts contribute to the score. Only the `magnetic_moments.csv` file is checked.
