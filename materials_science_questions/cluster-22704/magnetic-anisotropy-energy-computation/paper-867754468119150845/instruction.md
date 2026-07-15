# Strain-Tuned Magnetic Anisotropy Energy of LaCrO3

## Problem background
LaCrO3 (LCO) is a perovskite orthochromite exhibiting a canted G-type antiferromagnetic (AFM) order with weak ferromagnetism. The magnetic anisotropy energy (MAE) determines the orientation of the easy magnetization axis relative to the crystal lattice. This work investigates, via density functional theory (DFT), how epitaxial strain alters the MAE landscape and thus the magnetic easy axis. Understanding the strain dependence of MAE is crucial for designing magnetoelectric and spintronic devices based on orthochromite films.

## Approach
The approach uses first-principles density functional theory (DFT) with Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation, a Hubbard U correction (GGA+U) for Cr 3d electrons, and non-collinear spin-orbit coupling (SOC). Calculations are performed on the orthorhombic 20-atom unit cell (space group Pbnm) of LaCrO3. Three strain states are considered: fully relaxed, 1% in-plane tensile strain, and 1% in-plane compressive strain. For the strained cases, the in-plane lattice parameters are constrained to ±1% of the relaxed values while the out-of-plane lattice parameter and all internal coordinates are allowed to relax. For each strain state, the total energy is computed as the local Cr spin orientation is rotated from the in-plane [100] direction to the out-of-plane [001] direction in discrete angular steps. The magnetic anisotropy energy (MAE) is then derived from the energy variation with spin angle, quantifying the energetic cost of aligning the magnetization away from the easy axis.

## Reproduction target
Compute the magnetic anisotropy energy (MAE) as a function of spin orientation angle θ (between in-plane [100] and out-of-plane [001]) for orthorhombic LaCrO3 in three strain states: relaxed, 1% in-plane tensile strain, and 1% in-plane compressive strain. Output the MAE versus angle for all strain states as a CSV file.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency Pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Structural relaxation and strained cell generation
- Role: process
- Action: Perform DFT+U structural relaxation for bulk orthorhombic LaCrO3 (a=5.513 Å, b=5.476 Å, c=7.759 Å, space group Pbnm) with G-type AFM initial magnetic order using PBE+U (U=3.7 eV on Cr 3d). The procedure must then generate cells under 1% in-plane tensile and 1% in-plane compressive strain by constraining in-plane lattice parameters relative to the relaxed values and relaxing out-of-plane lattice parameter and internal coordinates. Produce the relaxed, tensile and compressive geometries as input files for the next step.
- Evidence: `/app/outputs/relax_summary.txt`

### Step 2: MAE vs spin angle for all strain states
- Role: scored (load-bearing)
- Action: For each strain state (relaxed, 1% tensile, 1% compressive), run a series of non-collinear DFT+SOC calculations with spin orientations θ varying from 0° (in-plane [100]) to 90° (out-of-plane [001]) in steps of 15°. Extract total energy for each angle and compute MAE (in meV/f.u.) as (E(θ) - E_min) × 1000 / 4, where E_min is the lowest total energy in that strain state and the factor 4 converts from the 20-atom cell to per formula unit.
- Output file: `/app/outputs/step_01_MAE_vs_angle.csv`
- Format: csv
- Contract: CSV with columns: strain_state (string: relaxed, tensile_1pct, compressive_1pct), spin_angle_deg (float, 0,15,…,90), total_energy_eV (float), MAE_meV_per_fu (float). One row per (strain_state, angle) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_MAE_vs_angle.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_MAE_vs_angle.csv
- path: `/app/outputs/step_01_MAE_vs_angle.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetic anisotropy energy (MAE) as a function of spin orientation angle for relaxed, 1% tensile and 1% compressive in-plane strain. The checker compares the reported MAE values to hidden reference values from the paper and verifies that the overall MAE versus angle trends are physically consistent.
- schema:
  - `type`: table
  - `required_columns`: `strain_state`, `spin_angle_deg`, `total_energy_eV`, `MAE_meV_per_fu`
  - `units`:
    - `spin_angle_deg`: degrees
    - `total_energy_eV`: eV
    - `MAE_meV_per_fu`: meV per formula unit

Notes: The output file is scored. The agent must compute MAE from total energy differences; the hidden checker will compare the reported MAE values at specific angles against the paper's reference MAE and check physical consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_MAE_vs_angle.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_state",
          "spin_angle_deg",
          "total_energy_eV",
          "MAE_meV_per_fu"
        ],
        "units": {
          "spin_angle_deg": "degrees",
          "total_energy_eV": "eV",
          "MAE_meV_per_fu": "meV per formula unit"
        }
      },
      "description": "Magnetic anisotropy energy (MAE) as a function of spin orientation angle for relaxed, 1% tensile and 1% compressive in-plane strain. The checker compares the reported MAE values to hidden reference values from the paper and verifies that the overall MAE versus angle trends are physically consistent."
    }
  ],
  "notes": "The output file is scored. The agent must compute MAE from total energy differences; the hidden checker will compare the reported MAE values at specific angles against the paper's reference MAE and check physical consistency."
}
```

## How you are scored
A hidden verifier will independently score your submission by reading the output file `/app/outputs/step_01_MAE_vs_angle.csv`. The verifier compares the reported magnetic anisotropy energy (MAE) values to reference values derived from the paper and checks that the overall MAE versus angle trends across the three strain states are physically consistent with the expected behavior. The scoring uses tolerances appropriate for DFT calculations and does not require an exact match to a specific set of numbers. The reward is computed from the agreement of your submitted CSV with the hidden reference, combined with consistency checks. Reporting the paper's numbers without actually performing the DFT workflow will not pass the scoring. The process step evidence (relax_summary.txt) is not directly scored but is expected to be produced as part of the workflow.
