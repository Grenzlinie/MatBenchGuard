# CG Simulation of J-integral in CNT/PMMA Composites

## Problem background
Carbon nanotube (CNT)-reinforced polymer composites are promising materials, but their fracture behavior at the nanoscale is difficult to characterize. The J-integral quantifies the energy release rate during crack growth; however, conventional methods require precise knowledge of the crack tip position and the surrounding continuum fields – information that is extremely hard to obtain in amorphous polymers. This work proposes a coarse-grained (CG) simulation approach that calculates the mode‑I J-integral of a double‑edge‑notched specimen directly from a single global load‑displacement curve, without needing any crack‑tip information. The influence of CNT weight fraction, covalent cross‑links between CNTs and the polymer matrix, notch length, and representative volume element (RVE) size on the J-integral is investigated.

## Approach
The core idea is to represent the polymer and CNTs at a coarse-grained level: each methyl methacrylate monomer is mapped to a single bead (P bead) and each five‑atom ring of a (5,5) CNT is mapped to a single bead (C bead). Interactions are described by bonded (bond, angle, dihedral) and non‑bonded (Lennard–Jones) potentials with parameters derived from atomistic simulations. Covalent cross‑links (2CH₂ between CNT and polymer, and EGDMA between polymer chains) are added as additional bond potentials. A thin, double‑edge‑notched RVE is constructed and equilibrated. To simulate quasi‑static loading, a small tensile strain is repeatedly applied perpendicular to the cracks; after each increment the potential energy is re‑minimised while lateral pressures are kept at atmospheric. This yields the potential‑energy versus displacement curve, from which the load is obtained as the derivative. The J-integral is computed by decomposing the response into an elastic contribution – evaluated via the analytical stress intensity factor of a double‑edge‑notched panel – and a plastic work contribution derived from the load‑displacement curve. The method does not require tracking the crack tip.

## Reproduction target
Construct and simulate three material systems, all within a 60×60×5 nm³ RVE containing in‑plane randomly distributed 10‑nm long (5,5) CNTs:

1. Pure PMMA (0 wt% CNT).
2. PMMA with 5 wt% CNT, no cross‑links.
3. PMMA with 10 wt% CNT and 2% mole fraction of 2CH₂ cross‑links between CNTs and the polymer matrix.

For each system, introduce two 15‑nm edge notches (a/W = 0.5), perform static tensile deformation, and compute the J-integral (J/m²) as described. Additionally, submit the full potential‑energy versus displacement curve for the 5 wt% CNT case as a separate scored artifact. The objective is to obtain J-integral values that are consistent with the CG model predictions; the verifier will compare them against reference results.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/download.html

## Workflow steps

### Step 1: CG System Construction and Equilibration
- Role: process
- Action: Build coarse-grained PMMA/CNT composite RVEs (60×60×5 nm³) for three conditions: pure PMMA, CNT 5 wt% no cross-links, CNT 10 wt% with 2% mole fraction 2CH₂ cross-links. Use CG force field parameters for bond, angle, dihedral, and vdW interactions as given in the paper. For each system: energy minimization (conjugate-gradient), NPT heating to 298 K at 101 kPa, 5 ns NPT equilibration, final energy minimization to remove internal stresses. Then introduce two center edge notches (a=15 nm, a/W=0.5) by deleting beads/bonds, followed by energy minimization and 3 ns NPT relaxation. The result is a set of relaxed cracked configurations ready for deformation.
- Evidence: `/app/outputs/log.txt`

### Step 2: Static Deformation and Load-Displacement Curve (Baseline)
- Role: scored (load-bearing)
- Action: For the baseline condition (CNT 5 wt%, no cross-links), apply constant-strain tensile deformation (incremental strain, direction perpendicular to notches) by minimizing the potential energy at each strain step while maintaining lateral atmospheric pressure. Record the potential energy U as a function of displacement Δ. Output the curve as a CSV file.
- Output file: `/app/outputs/load_displacement_baseline.csv`
- Format: csv
- Contract: columns: displacement_Angstrom (float, Angstrom), potential_energy_kcal_mol (float, kcal/mol)
- Scoring: scored by hidden verifier (structural audit: required columns and monotonicity; J-integral is not recomputed from this file)

### Step 3: J-Integral Calculation and Reporting
- Role: scored
- Action: Obtain the load-displacement curve for the other two conditions (pure PMMA and CNT 10 wt% with 2% 2CH₂ cross-links) by repeating the static deformation simulation; reuse the baseline curve from step2. For each curve: compute the load P as the derivative of potential energy with respect to displacement (dU/dΔ), decompose the total displacement into elastic and plastic parts, then compute the mode-I J-integral using the analytical expression that separates an elastic contribution via the stress intensity factor for a double-edge-notched panel and a plastic work term derived from the P–Δ curve. Report the three J-integral values (J/m²) in a single CSV file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: columns: condition (string, one of 'pure_PMMA','CNT5wt%','CNT10wt%_2pct_crosslink'), J_integral (float, J/m^2)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/load_displacement_baseline.csv`
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### load_displacement_baseline.csv
- path: `/app/outputs/load_displacement_baseline.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw potential energy vs. displacement data for baseline CNT 5 wt% without cross-links. The verifier performs a structural audit (required columns, monotonicity) to ensure the file is a valid load-displacement curve; it does not recompute the J-integral from this file.
- schema:
  - `type`: table
  - `required_columns`: `displacement_Angstrom`, `potential_energy_kcal_mol`
  - `units`:
    - `displacement_Angstrom`: Angstrom
    - `potential_energy_kcal_mol`: kcal/mol
  - `structure_checks`: `columns_present`, `monotonic_increasing_displacement`

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Agent-reported J-integral values for three conditions. The checker compares these to hidden paper-reported reference values; meeting or beating the reference earns full credit.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `J_integral`
  - `condition_values`: `pure_PMMA`, `CNT5wt%`, `CNT10wt%_2pct_crosslink`
  - `units`:
    - `J_integral`: J/m^2

Notes: The baseline load-displacement curve is verified by structural audit; the results.csv J-integral values are compared to gold references under a threshold_or_better policy. There is no cross-validation between the two files.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "load_displacement_baseline.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "displacement_Angstrom",
          "potential_energy_kcal_mol"
        ],
        "units": {
          "displacement_Angstrom": "Angstrom",
          "potential_energy_kcal_mol": "kcal/mol"
        },
        "structure_checks": [
          "columns_present",
          "monotonic_increasing_displacement"
        ]
      },
      "description": "Raw potential energy vs. displacement data for baseline CNT 5 wt% without cross-links. The verifier performs a structural audit (required columns, monotonicity) to ensure the file is a valid load-displacement curve; it does not recompute the J-integral from this file."
    },
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "J_integral"
        ],
        "condition_values": [
          "pure_PMMA",
          "CNT5wt%",
          "CNT10wt%_2pct_crosslink"
        ],
        "units": {
          "J_integral": "J/m^2"
        }
      },
      "description": "Agent-reported J-integral values for three conditions. The checker compares these to hidden paper-reported reference values; meeting or beating the reference earns full credit."
    }
  ],
  "notes": "The baseline load-displacement curve is verified by structural audit; the results.csv J-integral values are compared to gold references under a threshold_or_better policy. There is no cross-validation between the two files."
}
```

## How you are scored
A hidden verifier independently evaluates the two scored artifacts. For the baseline load‑displacement curve (`load_displacement_baseline.csv`), the verifier performs a structural audit (checking required columns and monotonicity) to verify the file is a valid load‑displacement curve; the J-integral is not recomputed from this file. For the three J-integral values in `results.csv`, the verifier compares them to reference values. The main reward comes from the J-integral results; the baseline curve must pass the structural check to be considered valid. The verifier never reveals the reference values or tolerances during evaluation.
