# Lattice Energy Calculation for Diquinoline Host Inclusion Compounds

## Problem background
Diquinoline host 6 and its inclusion compounds with various small organic guests exhibit different crystal packings depending on the guest. To understand the relative stabilities of these supramolecular assemblies, lattice energy calculations are performed on the crystal structures. The problem is to compute the normalized packing energies (kcal per 1000 Å³) for the apohost and six representative inclusion compounds, and to determine which crystal is the most favourable (lowest normalized energy) and which is the least favourable (highest normalized energy).

## Approach
Compute the total lattice energy of each crystal structure as the sum of van der Waals and Coulombic contributions. Van der Waals interactions are described by a Lennard‑Jones potential with atom‑type‑specific parameters taken from the literature. Coulombic energies are evaluated after performing a charge equilibration (QEq) to assign partial charges, with the electrostatic energy computed by Ewald summation. The total energy per unit cell is normalised by the unit cell volume to obtain a per‑volume packing energy that permits comparison across crystals with different cell sizes.

## Reproduction target
Using the crystal structures of apohost 6 and its inclusion compounds with carbon disulfide, dichloromethane, acetone, chloroform, benzene, and toluene, compute the total lattice energy, unit cell volume, and normalized packing energy (total energy divided by (cell volume / 1000)) for each compound. Report the results in the specified CSV file. From these energies, determine the stability ranking of the seven crystals: which compound gives the highest (least negative) normalized packing energy, and which gives the lowest (most negative).

## Assets

- CIF files for host 6 inclusion compounds: https://www.ccdc.cam.ac.uk/structures/
- Molecular simulation package (e.g., LAMMPS, GULP, OpenMM): lammps

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Retrieve the CIF files for the seven target crystal structures from the Cambridge Crystallographic Data Centre (CCDC) using the deposition numbers given in the resources. Convert each CIF into an input structure file suitable for the chosen simulation package (e.g., LAMMPS data file or GULP input), preserving the unit cell, space group, atomic coordinates, and atom types.
- Evidence: `/app/outputs/cif_preparation.log`

### Step 2: Compute lattice energies
- Role: scored (load-bearing)
- Action: For each of the seven target crystal structures (apohost 6 and its inclusion compounds with carbon disulfide, dichloromethane, acetone, chloroform, benzene, and toluene), compute the lattice energy using a classical force field. Use the Lennard-Jones parameters published in the paper: Br ε=0.370 kcal/mol, σ=1.98 Å; C ε=0.095, σ=1.95; Cl ε=0.283, σ=1.98; H ε=0.015, σ=1.60; N ε=0.077, σ=1.83; O ε=0.096, σ=1.70; S ε=0.344, σ=2.02. Apply a cutoff of 12 Å for van der Waals interactions. For Coulombic interactions, perform QEq charge equilibration and evaluate the electrostatic energy using Ewald summation. Compute the total energy (kcal/mol per unit cell), the unit cell volume (Å³), and the normalized relative packing energy defined as total energy divided by (unit cell volume / 1000). Write the results to /app/outputs/lattice_energies.csv.
- Output file: `/app/outputs/lattice_energies.csv`
- Format: csv
- Contract: compound (string), total_energy_kcal_per_cell (float), cell_volume_A3 (float), normalized_energy_kcal_per_1000A3 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_energies.csv
- path: `/app/outputs/lattice_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lattice energies for apohost 6 and its inclusion compounds; compared to paper-reported reference values.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `total_energy_kcal_per_cell`, `cell_volume_A3`, `normalized_energy_kcal_per_1000A3`
  - `units`:
    - `total_energy_kcal_per_cell`: kcal/mol
    - `cell_volume_A3`: Å³
    - `normalized_energy_kcal_per_1000A3`: kcal per 1000 Å³

Notes: The quinolinium salt (11)·(acetophenone) is excluded from the scored target because its energy is not reported in the paper's Table 2. The checker compares each entry's normalized energy to the corresponding hidden paper value within a tolerance and also evaluates the ranking (apohost should have the highest normalized energy, chloroform compound the lowest).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "total_energy_kcal_per_cell",
          "cell_volume_A3",
          "normalized_energy_kcal_per_1000A3"
        ],
        "units": {
          "total_energy_kcal_per_cell": "kcal/mol",
          "cell_volume_A3": "Å³",
          "normalized_energy_kcal_per_1000A3": "kcal per 1000 Å³"
        }
      },
      "description": "Lattice energies for apohost 6 and its inclusion compounds; compared to paper-reported reference values."
    }
  ],
  "notes": "The quinolinium salt (11)·(acetophenone) is excluded from the scored target because its energy is not reported in the paper's Table 2. The checker compares each entry's normalized energy to the corresponding hidden paper value within a tolerance and also evaluates the ranking (apohost should have the highest normalized energy, chloroform compound the lowest)."
}
```

## How you are scored
A hidden verifier reads your `lattice_energies.csv` file. It compares each reported normalized energy to a reference value with an appropriate tolerance and also checks whether the ordering of the compounds (from highest to lowest normalized energy) matches the expected ranking. The verifier combines these comparisons into a weighted score between 0 and 1. Simply writing the paper's published numbers is not sufficient; you must actually perform the energy calculation and report the outcomes you obtain.
