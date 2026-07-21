# Atomistic simulations of grain boundary sliding and migration in aluminum

## Problem background
Atomistic simulations provide a crucial tool for understanding the mechanics of grain boundary sliding and migration, which are primary mechanisms for superplastic deformation. In aluminum, symmetric tilt grain boundaries with high-angle misorientation exhibit complex atomic-scale behavior under mechanical loads. This work investigates the energy landscape of pure grain boundary sliding, the coupling between sliding and migration under applied forces, and how the grain boundary energy influences mobility. By performing molecular statics and molecular dynamics simulations with embedded-atom method potentials, we aim to quantify these processes and compute property relationships that shed light on the fundamental deformation mechanisms.

## Approach
Two bicrystal simulation cells are constructed for aluminum symmetric tilt grain boundaries: Σ3(1-11) and Σ9(2-21). Both cells use the coincident-site lattice (CSL) model with a [001] tilt axis and the equilibrium lattice constant of 4.05 Å. Periodic boundary conditions are applied in the interface plane (x–z), while free surfaces are used normal to the boundary (y). The atomic interactions are described by the Oh–Johnson embedded-atom method (EAM) potential.

After energy minimization at 0 K using molecular statics, two types of mechanical tests are performed:

- Displacement-controlled 'pure' grain boundary sliding: incremental shear displacements (fractions of the CSL lattice parameter a_CSL) are applied to the top grain, and after each increment the structure is relaxed by molecular statics. The grain boundary energy per unit area is recorded as a function of displacement.

- Force-controlled molecular dynamics: a constant force is applied to all atoms in the top grain along the x‑direction to drive coupled sliding and migration. One simulation is run at a force of 0.02 eV/Å on the Σ3 boundary; another simulation is performed on both the Σ3 and Σ9 boundaries with an applied force per unit volume of 1.17×10⁻³ eV/Å⁴. Trajectories are saved and post‑processed to extract the sliding displacement (average x displacement of the top grain relative to the bottom grain) and the migration distance (shift of the grain boundary plane in the y‑direction) as functions of time.

## Reproduction target
You must produce four comma‑separated value (CSV) artifacts in the /app/outputs directory:

1. energy_vs_displacement.csv: columns displacement_fraction (float, fraction of a_CSL) and gb_energy (float, eV/Å²). This file contains the grain boundary energy profile for the Σ3(1‑11) boundary under displacement‑controlled pure sliding, obtained from incremental shearing followed by molecular‑statics relaxation.

2. sliding_vs_time.csv: columns time_ps (float, ps) and sliding_A (float, Å). This file contains the sliding displacement of the Σ3(1‑11) boundary as a function of time during molecular dynamics with a constant force of 0.02 eV/Å applied to the top grain.

3. migration_vs_time.csv: columns time_ps (float, ps) and migration_A (float, Å). This file contains the migration distance of the same Σ3(1‑11) boundary during the same simulation.

4. gb_energy_effect.csv: columns boundary_label (string) and sliding_at_5ps (float, Å). This file records the sliding displacement at 5 ps for both the Σ3(1‑11) and Σ9(2‑21) boundaries, each simulated with an applied force per unit volume of 1.17×10⁻³ eV/Å⁴ (the total force on the top grain must be scaled accordingly).

## Assets

- LAMMPS molecular dynamics package: https://lammps.sandia.gov/
- EAM potential for Aluminum (Oh-Johnson): https://github.com/lammps/lammps/raw/master/potentials/Al_Oh_Johnson.eam

## Workflow steps

### Step 1: Construct bicrystal simulation cells for Σ3 and Σ9 STGB
- Role: process
- Action: Construct initial atomic coordinates for Σ3(1-11) and Σ9(2-21) symmetric tilt grain boundaries of aluminum (FCC, a=4.05 Å) using the CSL model with [001] tilt axis. Set periodic boundary conditions in the interface plane and free surfaces normal to it. Output LAMMPS data files.
- Evidence: none

### Step 2: Molecular statics energy minimization of STGB cells
- Role: process
- Action: Perform energy minimization at 0 K using LAMMPS with the Oh-Johnson EAM potential on the constructed bicrystal cells to obtain equilibrium grain boundary structures. Save relaxed coordinates.
- Evidence: none

### Step 3: Displacement-controlled pure GBS of Σ3(1-11)
- Role: scored (load-bearing)
- Action: For the relaxed Σ3(1-11) bicrystal, apply incremental shear displacements to the top grain (e.g., 1% of a_CSL per step), relax the structure by molecular statics after each increment, and compute the grain boundary energy per unit area. Save the energy versus displacement.
- Output file: `/app/outputs/energy_vs_displacement.csv`
- Format: csv
- Contract: columns: displacement_fraction (float, fraction of a_CSL), gb_energy (float, eV/Å²)
- Scoring: scored by hidden verifier

### Step 4: Force-controlled MD simulation for Σ3 at 0.02 eV/Å
- Role: process
- Action: Run molecular dynamics in LAMMPS at constant volume on the relaxed Σ3(1-11) bicrystal, applying a force of 0.02 eV/Å on all atoms in the top grain along the x-direction, for at least 5 ps. Save atomic trajectories.
- Evidence: none

### Step 5: Extract sliding displacement vs time for Σ3
- Role: scored (load-bearing)
- Action: From the MD trajectory of step 4, compute the average x-displacement of the top grain relative to the bottom grain as a function of time (sliding displacement). Output sliding_vs_time.csv.
- Output file: `/app/outputs/sliding_vs_time.csv`
- Format: csv
- Contract: columns: time_ps (float), sliding_A (float)
- Scoring: scored by hidden verifier

### Step 6: Extract migration distance vs time for Σ3
- Role: scored
- Action: From the same MD trajectory, determine the change in y-position of the grain boundary plane (migration distance) as a function of time. Output migration_vs_time.csv.
- Output file: `/app/outputs/migration_vs_time.csv`
- Format: csv
- Contract: columns: time_ps (float), migration_A (float)
- Scoring: scored by hidden verifier

### Step 7: Force-controlled MD simulation for Σ3 and Σ9 at specified force per volume
- Role: process
- Action: Run molecular dynamics for the relaxed Σ3(1-11) and Σ9(2-21) bicrystals with an applied force per unit volume of 1.17e-3 eV/Å^4 (scale total force on top grain atoms accordingly). Run each for at least 5 ps and save trajectories.
- Evidence: none

### Step 8: GB energy effect on sliding displacement at 5 ps
- Role: scored
- Action: For both Σ3 and Σ9 MD runs from step 7, compute the sliding displacement at 5 ps and write a summary CSV.
- Output file: `/app/outputs/gb_energy_effect.csv`
- Format: csv
- Contract: columns: boundary_label (string), sliding_at_5ps (float, Å)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_vs_displacement.csv`
- `/app/outputs/sliding_vs_time.csv`
- `/app/outputs/migration_vs_time.csv`
- `/app/outputs/gb_energy_effect.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_vs_displacement.csv
- path: `/app/outputs/energy_vs_displacement.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Grain boundary energy profile for pure sliding of Σ3(1-11) boundary.
- schema:
  - `type`: table
  - `required_columns`: `displacement_fraction`, `gb_energy`
  - `units`:
    - `displacement_fraction`: fraction of a_CSL
    - `gb_energy`: eV/Å^2

### sliding_vs_time.csv
- path: `/app/outputs/sliding_vs_time.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sliding displacement vs. time for Σ3(1-11) under applied force 0.02 eV/Å.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `sliding_A`
  - `units`:
    - `time_ps`: ps
    - `sliding_A`: Å

### migration_vs_time.csv
- path: `/app/outputs/migration_vs_time.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Migration distance vs. time for Σ3(1-11) under applied force 0.02 eV/Å.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `migration_A`
  - `units`:
    - `time_ps`: ps
    - `migration_A`: Å

### gb_energy_effect.csv
- path: `/app/outputs/gb_energy_effect.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sliding displacement at 5 ps for Σ3 and Σ9 boundaries under three levels of applied force per unit volume (0.58e-3, 1.17e-3, 2.32e-3 eV/Å^4), demonstrating dependence on applied force and grain boundary energy.
- schema:
  - `type`: table
  - `required_columns`: `boundary_label`, `force_per_volume_eV_per_A4`, `sliding_at_5ps`
  - `units`:
    - `force_per_volume_eV_per_A4`: eV/Å^4
    - `sliding_at_5ps`: Å

Notes: All outputs placed under /app/outputs. The hidden checker verifies sliding values for each force-boundary combination, monotonic increase with force, and higher sliding for Σ9 than Σ3 at the same force.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_vs_displacement.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "displacement_fraction",
          "gb_energy"
        ],
        "units": {
          "displacement_fraction": "fraction of a_CSL",
          "gb_energy": "eV/Å^2"
        }
      },
      "description": "Grain boundary energy profile for pure sliding of Σ3(1-11) boundary."
    },
    {
      "file": "sliding_vs_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "sliding_A"
        ],
        "units": {
          "time_ps": "ps",
          "sliding_A": "Å"
        }
      },
      "description": "Sliding displacement vs. time for Σ3(1-11) under applied force 0.02 eV/Å."
    },
    {
      "file": "migration_vs_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "migration_A"
        ],
        "units": {
          "time_ps": "ps",
          "migration_A": "Å"
        }
      },
      "description": "Migration distance vs. time for Σ3(1-11) under applied force 0.02 eV/Å."
    },
    {
      "file": "gb_energy_effect.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "boundary_label",
          "force_per_volume_eV_per_A4",
          "sliding_at_5ps"
        ],
        "units": {
          "force_per_volume_eV_per_A4": "eV/Å^4",
          "sliding_at_5ps": "Å"
        }
      },
      "description": "Sliding displacement at 5 ps for Σ3 and Σ9 boundaries under three levels of applied force per unit volume (0.58e-3, 1.17e-3, 2.32e-3 eV/Å^4), demonstrating dependence on applied force and grain boundary energy."
    }
  ],
  "notes": "All outputs placed under /app/outputs. The hidden checker verifies sliding values for each force-boundary combination, monotonic increase with force, and higher sliding for Σ9 than Σ3 at the same force."
}
```

## How you are scored
The hidden verifier independently evaluates each of the four scored artifacts. It extracts key features from your CSV files — such as the locations and magnitudes of energy peaks and valleys in the displacement‑controlled sliding profile, the time‑dependent sliding and migration curves, and the relative sliding extent of the two grain boundaries under identical loading — and compares them against reference values. Each artifact carries a predetermined weight, and the final reward is a normalized combination of the per‑artifact scores. Reproducing the full computational pipeline (geometry construction, relaxation, shearing, and dynamics) is essential; simply reporting plausible numbers without genuine simulation will not yield results that survive the feature‑level comparisons.
