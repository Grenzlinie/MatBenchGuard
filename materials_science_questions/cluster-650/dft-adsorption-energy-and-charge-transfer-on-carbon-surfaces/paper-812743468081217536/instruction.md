# MD simulation of ds-DNA adsorption orientation and interaction energy on MoS2

## Problem background
Two-dimensional molybdenum disulfide (MoS2) has emerged as a promising material for biosensors and DNA sequencing devices due to its unique electronic properties and direct band gap. Understanding the interfacial interaction between double-stranded DNA (ds-DNA) and MoS2 is essential for developing such applications. Molecular dynamics (MD) simulations can provide atomic-level insight into the adsorption orientation, driving forces, and the influence of DNA sequence and length on the interaction. This task reproduces key MD simulation results investigating how ds-DNA adsorbs on a MoS2 surface.

## Approach
The workflow constructs a 12-bp ds-DNA model and a single-layer MoS2 sheet using the CHARMM27 force field. Two initial configurations are prepared: DNA perpendicular (⊥) and parallel (∥) to the MoS2 surface. Both systems are solvated in TIP3P water with counterions and subjected to energy minimization followed by 200 ns NVT MD simulations at 300 K. Trajectory analysis yields the time evolution of the angle between DNA axis and surface, the distance profile of base pairs from the surface, and the van der Waals and electrostatic interaction energies for residues within 4 Å. In addition, control simulations with an altered DNA sequence and with shorter ds-DNA lengths (8 bp, 6 bp) are run starting from a perpendicular orientation to assess the effect of sequence and length on the adsorption orientation.

## Reproduction target
Perform MD simulations as described and compute the following quantitative results: (1) The adsorption orientation angle between the ds-DNA main axis and the MoS2 plane over the full 200 ns trajectory for both the perpendicular and parallel starting configurations. (2) The average distance from the center of mass of each of the 12 base pairs to the MoS2 surface during the last 15 ns of each main simulation. (3) The van der Waals and electrostatic interaction energies between DNA residues within 4 Å of the surface and the MoS2 sheet, averaged over the last 15 ns. (4) For all five systems (DNA⊥MoS2, DNA∥MoS2, altered sequence, 8 bp, 6 bp), the average adsorption angle during the last 15 ns of each simulation. Output the results as the specified CSV files.

## Assets

- GROMACS: https://www.gromacs.org/
- CHARMM27 force field: http://mackerell.umaryland.edu/charmm_ff.shtml
- MoS₂ Lennard-Jones parameters: 10.1063/1.4944401

## Workflow steps

### Step 1: Build ds-DNA model
- Role: process
- Action: Construct a 12-bp ds-DNA with sequence 5'-ATCGATCGATCG-3' and its complement using the CHARMM27 force field. Produce GROMACS structure and topology files.
- Evidence: `/app/outputs/dna.pdb`

### Step 2: Build MoS₂ sheet
- Role: process
- Action: Build a single-layer MoS₂ sheet of dimensions 8.1 nm × 8.4 nm with Mo atoms (charge +0.76 e) and S atoms (−0.38 e), using Lennard-Jones parameters from Luan and Zhou (2016). Export GROMACS coordinate and topology files.
- Evidence: `/app/outputs/mos2.pdb`

### Step 3: Solvate system and add counterions
- Role: process
- Action: Combine DNA and MoS₂, solvate in a TIP3P water box of size 8.3 nm × 9.6 nm × 8.6 nm, and add K⁺ counterions to neutralise the DNA charge. Use periodic boundary conditions.
- Evidence: `/app/outputs/solvated.gro`

### Step 4: Prepare initial perpendicular and parallel orientations
- Role: process
- Action: Create two starting configurations: DNA main axis perpendicular to MoS₂ surface (DNA⊥MoS₂) and parallel (DNA∥MoS₂), with the minimum vertical distance between DNA and MoS₂ ~15 Å.
- Evidence: none

### Step 5: Energy minimization
- Role: process
- Action: Perform 50 000 steps of energy minimization on each configuration using GROMACS.
- Evidence: none

### Step 6: Main NVT MD simulation
- Role: process
- Action: Run 200 ns NVT MD simulations at 300 K using the Berendsen thermostat, a 2 fs time step, PME electrostatics, 10 Å cutoff for non-bonded interactions, and LINCS constraints. Perform one simulation for the perpendicular configuration and one for the parallel configuration.
- Evidence: none

### Step 7: Analyze adsorption orientation angle over time
- Role: scored
- Action: From the main trajectories, compute the angle between the ds-DNA main axis and the MoS₂ plane as a function of time. Output the time series.
- Output file: `/app/outputs/step_01_angle_vs_time.csv`
- Format: csv
- Contract: CSV with columns: time(ns), angle_perp(deg), angle_par(deg). Rows covering the full 200 ns trajectory.
- Scoring: scored by hidden verifier

### Step 8: Analyze base-pair distance to surface
- Role: scored
- Action: During the last 15 ns of each main trajectory, compute the average distance from the center of mass of each base pair to the MoS₂ surface. Output one row per base pair.
- Output file: `/app/outputs/step_02_basepair_distance.csv`
- Format: csv
- Contract: CSV with columns: base_pair (integer, 1-12), distance_perp(nm), distance_par(nm).
- Scoring: scored by hidden verifier

### Step 9: Analyze interaction energy decomposition
- Role: scored
- Action: For residues within 4 Å of the MoS₂ surface, calculate the van der Waals and electrostatic interaction energies between DNA and MoS₂, averaged over the last 15 ns of each main simulation. Output the per-component energies.
- Output file: `/app/outputs/step_03_interaction_energy.csv`
- Format: csv
- Contract: CSV with columns: system (str: perp or par), distance_cutoff(A), energy_type (str: vdW|Ele|Total), value(kJ/mol).
- Scoring: scored by hidden verifier

### Step 10: Build control DNA models
- Role: process
- Action: Build ds-DNA models with an altered sequence (5'-GCTAGCTAGCTA-3' and complement) and with shorter lengths (8 bp and 6 bp) using the CHARMM27 force field.
- Evidence: none

### Step 11: Run control MD simulations
- Role: process
- Action: For each control DNA model, set up a system with the DNA initially perpendicular to the MoS₂ surface, solvate, minimize, and run a 200 ns NVT simulation under the same conditions as the main simulations.
- Evidence: none

### Step 12: Compute final adsorption angles for all systems
- Role: scored (load-bearing)
- Action: For each system (DNA⊥MoS₂, DNA∥MoS₂, altered sequence, 8 bp, 6 bp), average the angle between the DNA axis and the MoS₂ plane over the last 15 ns of the respective simulation and report the result.
- Output file: `/app/outputs/step_04_final_angles.csv`
- Format: csv
- Contract: CSV with columns: system (str: perp, par, seq_changed, 8bp, 6bp), final_angle(deg).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_angle_vs_time.csv`
- `/app/outputs/step_02_basepair_distance.csv`
- `/app/outputs/step_03_interaction_energy.csv`
- `/app/outputs/step_04_final_angles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_angle_vs_time.csv
- path: `/app/outputs/step_01_angle_vs_time.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time evolution of the angle between the ds-DNA main axis and the MoS₂ surface for the two main orientations.
- schema:
  - `type`: table
  - `required_columns`: `time(ns)`, `angle_perp(deg)`, `angle_par(deg)`
  - `units`:
    - `time(ns)`: ns
    - `angle_perp(deg)`: deg
    - `angle_par(deg)`: deg

### step_02_basepair_distance.csv
- path: `/app/outputs/step_02_basepair_distance.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average distance from the centre of mass of each base pair to the MoS₂ surface during the last 15 ns of the main simulations.
- schema:
  - `type`: table
  - `required_columns`: `base_pair`, `distance_perp(nm)`, `distance_par(nm)`
  - `units`:
    - `distance_perp(nm)`: nm
    - `distance_par(nm)`: nm

### step_03_interaction_energy.csv
- path: `/app/outputs/step_03_interaction_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Van der Waals and electrostatic interaction energies between DNA and MoS₂ for residues within 4 Å of the surface.
- schema:
  - `type`: table
  - `required_columns`: `system`, `distance_cutoff(A)`, `energy_type`, `value(kJ/mol)`
  - `units`:
    - `distance_cutoff(A)`: Å
    - `value(kJ/mol)`: kJ/mol

### step_04_final_angles.csv
- path: `/app/outputs/step_04_final_angles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Final equilibrium adsorption angles for all five systems (two main orientations, altered sequence, 8 bp, 6 bp).
- schema:
  - `type`: table
  - `required_columns`: `system`, `final_angle(deg)`
  - `units`:
    - `final_angle(deg)`: deg

Notes: All outputs are scored by comparing computed quantities to hidden reference values with per-artifact tolerances. Angles, distances, energies, and stability metrics must match the paper's reported trends and approximate values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_angle_vs_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time(ns)",
          "angle_perp(deg)",
          "angle_par(deg)"
        ],
        "units": {
          "time(ns)": "ns",
          "angle_perp(deg)": "deg",
          "angle_par(deg)": "deg"
        }
      },
      "description": "Time evolution of the angle between the ds-DNA main axis and the MoS₂ surface for the two main orientations."
    },
    {
      "file": "step_02_basepair_distance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "base_pair",
          "distance_perp(nm)",
          "distance_par(nm)"
        ],
        "units": {
          "distance_perp(nm)": "nm",
          "distance_par(nm)": "nm"
        }
      },
      "description": "Average distance from the centre of mass of each base pair to the MoS₂ surface during the last 15 ns of the main simulations."
    },
    {
      "file": "step_03_interaction_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "distance_cutoff(A)",
          "energy_type",
          "value(kJ/mol)"
        ],
        "units": {
          "distance_cutoff(A)": "Å",
          "value(kJ/mol)": "kJ/mol"
        }
      },
      "description": "Van der Waals and electrostatic interaction energies between DNA and MoS₂ for residues within 4 Å of the surface."
    },
    {
      "file": "step_04_final_angles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "final_angle(deg)"
        ],
        "units": {
          "final_angle(deg)": "deg"
        }
      },
      "description": "Final equilibrium adsorption angles for all five systems (two main orientations, altered sequence, 8 bp, 6 bp)."
    }
  ],
  "notes": "All outputs are scored by comparing computed quantities to hidden reference values with per-artifact tolerances. Angles, distances, energies, and stability metrics must match the paper's reported trends and approximate values."
}
```

## How you are scored
A hidden verifier will read your CSV output files and compare the reported quantities to reference values derived from the original study. Each scored artifact is checked independently; the degree of agreement (within prescribed tolerances) determines the score for that artifact. The final reward is a weighted average of these per-artifact scores. Simply reporting expected values without actually running the simulations may not satisfy the verifier, as it may check consistency across artifacts or within the expected physical behavior.
