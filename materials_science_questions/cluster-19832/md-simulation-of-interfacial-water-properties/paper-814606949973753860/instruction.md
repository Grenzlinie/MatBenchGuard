# Water Dynamics in a Model Transbilayer Pore: MD Simulation and Analysis

## Problem background
Water-filled pores in membrane proteins play crucial roles in ion and solute transport. Understanding the dynamic properties of water molecules confined within such pores is essential for modeling transport mechanisms and electrostatics. This task investigates the simplest model system: a hydrophobic cylindrical pore and a periodic bulk water box, using molecular dynamics simulations to quantify translational and rotational mobility of water molecules in these two environments.

## Approach
Molecular dynamics (MD) simulations will be performed using the open-source GROMACS engine with the CHARMM27 force field and the TIP3P water model. Two simulation systems are prepared: (1) a cubic box of bulk TIP3P water with periodic boundary conditions (~19.042 Å per side), and (2) a hydrophobic cylindrical cavity of length 60 Å and radius 3 Å solvated with TIP3P water. For each system, a 100 ps MD simulation is run comprising 6 ps of heating, 9 ps of equilibration, and 85 ps of production in the NVE ensemble. The atomic trajectories are then analyzed to compute the self-diffusion coefficient D (Å²/ps), rotational reorientation rates τ₁⁻¹ (ps⁻¹) and τ₂⁻¹ (ps⁻¹), and the average z-projection of the water dipole moment μ_z (Debye) for bulk water and for water inside the cylinder (central region along the pore axis). The computed properties are compared between the two environments.

## Reproduction target
Produce a CSV file, water_dynamics.csv, containing the computed D, τ₁⁻¹, τ₂⁻¹, and μ_z for the bulk water model and the cylindrical pore model. Use the column names: model, D, tau1_inv, tau2_inv, mu_z. The goal is to obtain accurate values for these dynamic properties and to demonstrate whether and how water mobility differs between the unconfined and confined environments.

## Assets

- GROMACS: https://www.gromacs.org/
- CHARMM27 force field with TIP3P water model: gromacs

## Workflow steps

### Step 1: Prepare simulation systems
- Role: process
- Action: Build a bulk TIP3P water box of size approximately (19.042)^3 Å^3 with periodic boundary conditions. Build a hydrophobic cylindrical cavity of length 60 Å and radius 3 Å, oriented along the z-axis, and solvate it with TIP3P water molecules. Use the CHARMM27 force field and the TIP3P water model.
- Evidence: none

### Step 2: Run molecular dynamics simulations
- Role: process
- Action: For both the bulk water box and the solvated cylinder, run a 100 ps MD simulation using GROMACS: 6 ps heating, 9 ps equilibration, 85 ps production in the NVE ensemble. Save the atomic trajectories.
- Evidence: none

### Step 3: Compute water dynamic properties
- Role: scored (load-bearing)
- Action: From the trajectories, compute for bulk water and for water molecules inside the cylinder (defining 'inside' as the central region along the pore axis) the self-diffusion coefficient D (Å²/ps), the rotational reorientation rates τ₁⁻¹ (ps⁻¹) and τ₂⁻¹ (ps⁻¹), and the average z-projection of the water dipole moment μ_z (Debye). Write the results to water_dynamics.csv.
- Output file: `/app/outputs/water_dynamics.csv`
- Format: csv
- Contract: model (string: 'bulk' or 'cylinder'), D (float, Å²/ps), tau1_inv (float, ps⁻¹), tau2_inv (float, ps⁻¹), mu_z (float, Debye). Two rows, one for each model.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/water_dynamics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### water_dynamics.csv
- path: `/app/outputs/water_dynamics.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed dynamic properties for bulk water and for water inside a cylindrical hydrophobic pore. The checker compares these to hidden reference values with tolerances and verifies that intra-pore mobility is reduced relative to bulk water (D_bulk > D_cylinder, τ₁⁻¹_bulk > τ₁⁻¹_cylinder, τ₂⁻¹_bulk > τ₂⁻¹_cylinder).
- schema:
  - `type`: table
  - `required_columns`: `model`, `D`, `tau1_inv`, `tau2_inv`, `mu_z`
  - `units`:
    - `D`: Å²/ps
    - `tau1_inv`: ps⁻¹
    - `tau2_inv`: ps⁻¹
    - `mu_z`: Debye

Notes: The checker will compare the reported values to the paper's Table 1 reference values for bulk and cylinder models using absolute tolerances, and will additionally enforce the structural trend that mobility inside the pore is lower than in bulk.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "water_dynamics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "D",
          "tau1_inv",
          "tau2_inv",
          "mu_z"
        ],
        "units": {
          "D": "Å²/ps",
          "tau1_inv": "ps⁻¹",
          "tau2_inv": "ps⁻¹",
          "mu_z": "Debye"
        }
      },
      "description": "Computed dynamic properties for bulk water and for water inside a cylindrical hydrophobic pore. The checker compares these to hidden reference values with tolerances and verifies that intra-pore mobility is reduced relative to bulk water (D_bulk > D_cylinder, τ₁⁻¹_bulk > τ₁⁻¹_cylinder, τ₂⁻¹_bulk > τ₂⁻¹_cylinder)."
    }
  ],
  "notes": "The checker will compare the reported values to the paper's Table 1 reference values for bulk and cylinder models using absolute tolerances, and will additionally enforce the structural trend that mobility inside the pore is lower than in bulk."
}
```

## How you are scored
After you submit water_dynamics.csv, a hidden verifier will read your file and evaluate it against a stored reference. The verifier compares each reported property value (D, τ₁⁻¹, τ₂⁻¹, μ_z) to hidden reference values using allowed tolerances. It may also verify that your results satisfy certain structural relationships expected from the underlying physics. Your final reward is proportional to the number of conditions satisfied: both the absolute value comparisons and any required trends. Simply reporting numbers without performing the simulation is not sufficient to meet all criteria.
