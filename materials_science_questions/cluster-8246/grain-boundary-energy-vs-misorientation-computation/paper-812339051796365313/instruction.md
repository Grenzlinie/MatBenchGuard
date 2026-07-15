# Validation of Möbius periodic boundary conditions for atomistic simulations of silicon grain boundaries

## Problem background
Standard periodic boundary conditions (Born von Kármán, BVK) require two equivalent grain boundaries per simulation box, which can lead to artefacts at high temperature when grain boundaries migrate and interact. A new type of boundary condition, called Möbius or antiperiodic boundary conditions, allows only one grain boundary per box, potentially avoiding these artefacts. This task reproduces the numerical validation of Möbius periodic boundary conditions for silicon, by comparing equilibrium thermodynamic properties, atomic displacement profiles, and grain boundary energies against those from standard BVK simulations.

## Approach
Implement Möbius periodic boundary conditions in the y‑direction, using the transformation x' = -x, y' = y + L_y, z' = -z. Use the Stillinger‑Weber potential and set up a cubic box of 512 silicon atoms in the diamond structure. Perform molecular dynamics simulations at 1000 K in both NVE and Nosé NVT ensembles, with a timestep of 1.5 fs, for 10,000 steps, under both Möbius and standard BVK PBCs. For each run, compute the average energy per atom, temperature, pressure, and the whole‑box root‑mean‑square atomic displacement (RMSAD). Additionally, compute RMSAD values averaged over 5 Å thick slices perpendicular to the y‑direction, to check the spatial homogeneity of the displacements. For the grain boundary study, construct atomic configurations for the Σ=11(233)[011] tilt grain boundary (twist angle 50.48°) using coincidence site lattice methods; prepare a Möbius box containing one grain boundary and a double‑sized BVK box containing two equivalent boundaries. Then perform static energy minimisation for both the Σ11A and Σ11B variants. From the minimised energies, compute the interfacial energy γ (in mJ/m²) as (total energy – bulk reference energy) divided by (2 × interface area). Compare the minimised energy per atom between the Möbius and the double‑BVK boxes, and report the interfacial energies for the two structures.

## Reproduction target
Produce three CSV files (`bulk_properties.csv`, `rmsad_slices.csv`, and `gb_energies.csv`) with the columns specified in the workflow steps. The bulk properties file must contain thermodynamic averages and whole‑box RMSAD for each combination of ensemble and PBC type. The RMSAD slices file must provide per‑slice RMSAD values for both PBC types. The grain boundary energies file must list minimised energy per atom and interfacial energy for each structure and PBC type. Your submission will be scored on the internal consistency between Möbius and BVK results for bulk properties and RMSAD slices, on the equivalence of minimised energies per atom between the Möbius and double‑BVK boxes, on the absolute interfacial energies of Σ11A and Σ11B, and on the relative ordering of those two interfacial energies.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- Stillinger-Weber potential for silicon

## Workflow steps

### Step 1: Implement Möbius boundary conditions
- Role: process
- Action: Implement Möbius periodic boundary conditions in the y-direction for atomistic simulations. The transformation is: x' = -x, y' = y + Ly, z' = -z, where Ly is the box length in y. The implementation must also support standard BVK PBCs for comparison. The code should work with the Stillinger-Weber potential.
- Evidence: `/app/outputs/mobius_implementation_notes.txt`

### Step 2: Bulk MD thermodynamic and whole-box RMSAD comparison
- Role: scored
- Action: Create a cubic diamond-structure silicon box with 512 atoms. Run molecular dynamics with the Stillinger-Weber potential at 1000 K for 10,000 steps (timestep 1.5 fs) in both NVE and Nosé NVT ensembles, using both Möbius and standard BVK PBCs. For each run, compute the average energy per atom, average temperature, average pressure, and the root-mean-square atomic displacement (RMSAD) over the whole box. Write the results for all eight combinations.
- Output file: `/app/outputs/bulk_properties.csv`
- Format: csv
- Contract: simulation_id, pbc_type, ensemble, average_energy_eVperatom, average_temperature_K, average_pressure_bar, rmsad_Angstrom
- Scoring: scored by hidden verifier

### Step 3: RMSAD profiles across slices perpendicular to Möbius direction
- Role: scored
- Action: From the MD trajectories, compute the RMSAD averaged over 5 Å thick slices perpendicular to the y (Möbius) direction. For each slice position, record the RMSAD for the Möbius simulation and the corresponding BVK simulation. Use the same MD data as step_02.
- Output file: `/app/outputs/rmsad_slices.csv`
- Format: csv
- Contract: slice_position_Angstrom, mobius_rmsad_Angstrom, bvk_rmsad_Angstrom
- Scoring: scored by hidden verifier

### Step 4: Construct Σ11 tilt grain boundary structures
- Role: process
- Action: Construct atomic configurations for the Σ=11(233)[011] tilt grain boundary (twist angle 50.48°) in silicon using coincidence site lattice methods. Prepare a Möbius box containing one grain boundary, and a double-sized standard BVK box containing two equivalent grain boundaries. Use the diamond structure and the Stillinger-Weber potential.
- Evidence: `/app/outputs/gb_construction_log.txt`

### Step 5: Static energy minimisation of Σ11 grain boundaries
- Role: scored (load-bearing)
- Action: Perform static energy minimisation (e.g., conjugate gradient or quasi-molecular dynamics) on the constructed Σ11A and Σ11B grain boundary structures using both the Möbius box and the double-sized BVK box. Record the minimised energy per atom for each case. For the Möbius simulations, compute the interfacial energy γ (in mJ/m²) as (total energy minus bulk reference energy) divided by (2 × interface area).
- Output file: `/app/outputs/gb_energies.csv`
- Format: csv
- Contract: structure, pbc_type, minimized_energy_eVperatom, interfacial_energy_mJperm2
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.csv`
- `/app/outputs/rmsad_slices.csv`
- `/app/outputs/gb_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.csv
- path: `/app/outputs/bulk_properties.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Verifies that for each ensemble the thermodynamic averages and whole‑box RMSAD agree between Möbius and BVK PBCs within a tight relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `simulation_id`, `pbc_type`, `ensemble`, `average_energy_eVperatom`, `average_temperature_K`, `average_pressure_bar`, `rmsad_Angstrom`

### rmsad_slices.csv
- path: `/app/outputs/rmsad_slices.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Verifies that for every 5 Å slice the RMSAD values from Möbius and BVK simulations agree within 1% relative difference.
- schema:
  - `type`: table
  - `required_columns`: `slice_position_Angstrom`, `mobius_rmsad_Angstrom`, `bvk_rmsad_Angstrom`

### gb_energies.csv
- path: `/app/outputs/gb_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Compares the minimised energies and interfacial energies to the paper's reported values within tolerances, and checks that Σ11A has lower interfacial energy than Σ11B.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `pbc_type`, `minimized_energy_eVperatom`, `interfacial_energy_mJperm2`

Notes: Only the Stillinger-Weber potential is used. The Tersoff potential and high‑temperature MD observations are not part of the scored reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "simulation_id",
          "pbc_type",
          "ensemble",
          "average_energy_eVperatom",
          "average_temperature_K",
          "average_pressure_bar",
          "rmsad_Angstrom"
        ]
      },
      "description": "Verifies that for each ensemble the thermodynamic averages and whole‑box RMSAD agree between Möbius and BVK PBCs within a tight relative tolerance."
    },
    {
      "file": "rmsad_slices.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "slice_position_Angstrom",
          "mobius_rmsad_Angstrom",
          "bvk_rmsad_Angstrom"
        ]
      },
      "description": "Verifies that for every 5 Å slice the RMSAD values from Möbius and BVK simulations agree within 1% relative difference."
    },
    {
      "file": "gb_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "pbc_type",
          "minimized_energy_eVperatom",
          "interfacial_energy_mJperm2"
        ]
      },
      "description": "Compares the minimised energies and interfacial energies to the paper's reported values within tolerances, and checks that Σ11A has lower interfacial energy than Σ11B."
    }
  ],
  "notes": "Only the Stillinger-Weber potential is used. The Tersoff potential and high‑temperature MD observations are not part of the scored reproduction."
}
```

## How you are scored
The scoring is performed by a hidden verifier that reads your three CSV files under `/app/outputs`. The verifier applies a weighted composition of checks:

- For `bulk_properties.csv`, it checks that the Möbius results agree with the BVK results (average energy, temperature, pressure, RMSAD) within a tight relative tolerance.
- For `rmsad_slices.csv`, it checks that the per‑slice RMSAD values from Möbius and BVK simulations agree within a small relative difference.
- For `gb_energies.csv`, it verifies that the minimised energy per atom from the Möbius box matches that of the double BVK box within a tiny tolerance, that the interfacial energies match hidden reference values within an appropriate tolerance, and that the energy ordering of the Σ11A and Σ11B structures is correct.

Each of these checks contributes a portion of the total reward (0–1). Reporting numbers that happen to match the paper is not sufficient; the verifier independently evaluates your artifacts against its hidden gold standard. The final score is the sum of the stage scores, reflecting both the accuracy of individual quantities and the consistency of the overall reproduction.
