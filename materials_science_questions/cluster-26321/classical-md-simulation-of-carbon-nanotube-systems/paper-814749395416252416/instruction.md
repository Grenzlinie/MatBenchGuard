# Carbon Nanotube Hypervelocity Impact MD Simulations: Stress Distribution and Mass Loss

## Problem background
When carbon nanotubes collide with a solid target at hypervelocity (~6 km/s), the damage depends strongly on the impact angle: lateral impacts can lead to unzipping into graphene nanoribbons, while frontal impacts cause fragmentation. Understanding how stress dissipates and mass is lost during such collisions, and how these processes vary with impact angle, is important for mechanically processing nanotubes and for basic fracture physics. This task investigates the angle-dependent response of a double-walled carbon nanotube (inner (10,10), outer (15,15), length 10 nm) impacting a rigid target at 6.0 km/s using fully atomistic reactive molecular dynamics simulations.

## Approach
Fully atomistic reactive molecular dynamics (ReaxFF) simulations are used to model the impact process. A double-walled carbon nanotube is positioned relative to a rigid target and given an initial velocity of 6.0 km/s. Simulations are run at 300 K using a Nosé-Hoover thermostat and a 0.025 fs time step. Three impact angles are considered: 0° (lateral), 45° (diagonal), and 90° (frontal). After the impact, per-atom von Mises stress is computed from the stress tensor at each time step. Atoms with stress above the fracture threshold (~100 GPa) are classified as highly stressed. The analysis quantifies the fraction of highly stressed atoms near 200 fs after initial contact and the percentage of atoms that are ejected from the nanotube by the end of the simulation. These metrics are compared across the three angles to reveal the role of impact geometry.

## Reproduction target
For each impact angle (0°, 45°, 90°), compute the fraction of atoms with von Mises stress greater than 100 GPa at the time step closest to 200 fs after the nanotube first contacts the target, and the percentage of atoms that have left the nanotube (mass loss) at the end of the simulation. Report these results in a CSV file with columns: angle_deg, fraction_highly_stressed_200fs, mass_loss_percent, avg_stress_highly_stressed_GPa. Also export the final atomic coordinates from each simulation as an XYZ snapshot and concatenate the three frames into a single file.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov
- ReaxFF force field parameter file (CHO system): https://www.lammps.org/movies.html#reaxff (or use CHO.ff from LAMMPS examples)

## Workflow steps

### Step 1: System construction and simulation setup
- Role: process
- Action: Build atomic coordinates for a double-walled carbon nanotube (inner (10,10), outer (15,15), length 10 nm) and a rigid solid target. Set up LAMMPS input decks for three impact angles (0°, 45°, 90°) with the ReaxFF force field, NVT ensemble at 300 K controlled by a Nosé-Hoover thermostat, 0.025 fs time step, and shooting velocity of 6.0 km/s set by scaling atomic velocities. Generate initial configuration and input files.
- Evidence: `/app/outputs/system_setup.log`

### Step 2: Reactive MD simulations of CNT-target impacts
- Role: process
- Action: Run LAMMPS ReaxFF simulations for each impact angle using the generated input files. Each simulation should run for at least 0.5 ps and capture atomic trajectories (positions, velocities, forces, per-atom stress tensors) at intervals suitable for stress analysis (every 100 time‑steps). Save the required trajectory data for post-processing.
- Evidence: `/app/outputs/md_run.log`

### Step 3: Post‑simulation stress analysis and mass loss quantification
- Role: scored (load-bearing)
- Action: From MD trajectories, compute per‑atom von Mises stress every 100 time‑steps. Classify atoms as highly stressed when their von Mises stress exceeds 100 GPa. For each impact angle, identify the time step closest to 200 fs after initial contact and compute the fraction of atoms that are highly stressed and the average von Mises stress of those atoms. Also compute the percentage of atoms ejected (mass loss) at the end of the simulation. Output a CSV file with one row per angle containing angle_deg, fraction_highly_stressed_200fs, mass_loss_percent, avg_stress_highly_stressed_GPa.
- Output file: `/app/outputs/simulation_report.csv`
- Format: csv
- Contract: Columns: angle_deg (int, 0/45/90), fraction_highly_stressed_200fs (float, fraction of atoms with von Mises stress > 100 GPa), mass_loss_percent (float, % of atoms ejected), avg_stress_highly_stressed_GPa (float, average stress of highly stressed atoms in GPa). One row per angle.
- Scoring: scored by hidden verifier

### Step 4: Export final structural snapshots
- Role: scored
- Action: Export the final atomic configuration from each simulation run in XYZ format. Concatenate the three frames (one per angle) into a single XYZ file. Each frame: header line with the number of atoms and a comment line, followed by atom_id element x y z per atom.
- Output file: `/app/outputs/final_snapshots.xyz`
- Format: other
- Contract: Standard XYZ format: header line with number of atoms and a comment line, then per‑atom lines: atom_id, element, x, y, z. Frames for 0°, 45°, 90° concatenated.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_report.csv`
- `/app/outputs/final_snapshots.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_report.csv
- path: `/app/outputs/simulation_report.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Quantitative metrics of stress response and mass loss for the three impact angles. The checker compares the reported values against hidden paper‑reported approximate values with tolerances and verifies the trend ordering (fraction: 0° > 45° > 90°; mass loss: 90° > 45° > 0°).
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `fraction_highly_stressed_200fs`, `mass_loss_percent`, `avg_stress_highly_stressed_GPa`
  - `units`:
    - `fraction_highly_stressed_200fs`: fraction (0‑1)
    - `mass_loss_percent`: percentage
    - `avg_stress_highly_stressed_GPa`: GPa

### final_snapshots.xyz
- path: `/app/outputs/final_snapshots.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: XYZ snapshots of the final state after impact for each angle; audited for structural plausibility (atom count, evidence of unzipping) as low‑weight auxiliary check.
- schema:
  - `type`: other
  - `description`: Concatenated XYZ trajectory snapshots. Each frame: header line with number of atoms and comment, then per‑atom lines: atom_id element x y z. Frames for 0°, 45°, 90° concatenated.

Notes: The primary scoring weight is on simulation_report.csv; the snapshots serve as a low‑weight structural sanity check. The agent may use GPU or parallel execution to reduce runtime, but runtime is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_report.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "fraction_highly_stressed_200fs",
          "mass_loss_percent",
          "avg_stress_highly_stressed_GPa"
        ],
        "units": {
          "fraction_highly_stressed_200fs": "fraction (0‑1)",
          "mass_loss_percent": "percentage",
          "avg_stress_highly_stressed_GPa": "GPa"
        }
      },
      "description": "Quantitative metrics of stress response and mass loss for the three impact angles. The checker compares the reported values against hidden paper‑reported approximate values with tolerances and verifies the trend ordering (fraction: 0° > 45° > 90°; mass loss: 90° > 45° > 0°)."
    },
    {
      "file": "final_snapshots.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "description": "Concatenated XYZ trajectory snapshots. Each frame: header line with number of atoms and comment, then per‑atom lines: atom_id element x y z. Frames for 0°, 45°, 90° concatenated."
      },
      "description": "XYZ snapshots of the final state after impact for each angle; audited for structural plausibility (atom count, evidence of unzipping) as low‑weight auxiliary check."
    }
  ],
  "notes": "The primary scoring weight is on simulation_report.csv; the snapshots serve as a low‑weight structural sanity check. The agent may use GPU or parallel execution to reduce runtime, but runtime is not scored."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently inspects each output artifact. The scored artifacts are: (1) simulation_report.csv – the verifier checks the reported fraction of highly stressed atoms and mass loss against hidden reference values derived from the published study, and also verifies that the results across the three angles satisfy expected monotonic trends. (2) final_snapshots.xyz – the verifier audits the snapshots for structural plausibility (e.g., atom count, evidence of unzipping). Each artifact carries a weight; the final score is a weighted combination. The verifier only evaluates what you write; runtime or intermediate logs are not scored.
