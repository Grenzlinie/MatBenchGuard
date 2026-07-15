# Magnetic Anisotropy Energy Computation for Fe and Co Thin Films using FLAPW

## Problem background
Ferromagnetic thin films exhibit magnetic anisotropy that determines whether the magnetization prefers to lie in the film plane or point perpendicular to it. This easy-axis orientation has critical implications for magnetic device applications. First-principles calculations can predict the magnetic anisotropy energy (MAE) and the resulting easy axis by evaluating total-energy differences between in-plane and out-of-plane magnetization directions. The goal is to compute the MAE and determine the easy axis for several Fe and Co monolayer systems.

## Approach
This task uses the full-potential linearized augmented plane wave (FLAPW) method with spin-orbit coupling (SOC). The workflow consists of two main computational stages for each slab system:

1. **Semirelativistic self-consistent field (SCF) calculation**: A conventional FLAPW calculation without spin-orbit coupling is performed to obtain the self-consistent charge density and wave functions. This step also yields magnetic moments.

2. **Fully relativistic total-energy evaluation**: Starting from the converged semirelativistic density and wave functions, separate relativistic diagonalizations are carried out for two magnetization orientations: in-plane (e.g., along [100]) and out-of-plane (along [001]). The total energies are extracted from these calculations.

The magnetic anisotropy energy is defined as

MAE = E_out-of-plane − E_in-plane

A positive MAE indicates an out-of-plane easy axis; a negative MAE indicates an in-plane easy axis. This protocol is applied to five slab systems: free-standing Fe(001) and Co(001) monolayers, and Fe monolayers on Au(001), Ag(001), and Pd(001) substrates.

## Reproduction target
Perform the full FLAPW+SOC workflow for each of the following systems:

- Free-standing Fe(001) monolayer
- Free-standing Co(001) monolayer
- Fe monolayer on Au(001) substrate (1Fe/1Au slab)
- Fe monolayer on Ag(001) substrate (1Fe/1Ag slab)
- Fe monolayer on Pd(001) substrate (1Fe/1Pd slab)

For every system, compute the total energy with magnetization in-plane and out-of-plane, derive the MAE, and determine the easy-axis orientation. Write the results to a CSV file named `results.csv` with the columns: `system`, `E_perp_au_eV`, `E_inplane_au_eV`, `MAE_eV`, `easy_axis`. The energies must be reported in eV with at least four decimal places. The `easy_axis` column must contain either the string `'out-of-plane'` or `'in-plane'` based solely on the sign of the MAE.

## Assets

- FLEUR: https://github.com/JuDFTteam/fleur
- ASE (Atomic Simulation Environment): ase

## Workflow steps

### Step 1: Construct slab models
- Role: process
- Action: Generate atomic structures for free-standing Fe(001) monolayer, Co(001) monolayer, Fe/Au(001), Fe/Ag(001), and Fe/Pd(001) using experimental lattice constants and appropriate vacuum spacing. Create FLEUR input files with default computational parameters.
- Evidence: none

### Step 2: Semirelativistic FLAPW SCF calculations
- Role: process
- Action: For each slab system, perform semirelativistic (no spin-orbit) FLAPW self-consistent calculations to obtain charge density, wave functions, and magnetic moments of Fe or Co atoms. Optionally record magnetic moments in magnetic_moments.csv as evidence.
- Evidence: `/app/outputs/magnetic_moments.csv`

### Step 3: Spin-orbit coupling total energy calculations
- Role: process
- Action: Starting from the semirelativistic charge density and wave functions, perform fully relativistic diagonalizations for each system with magnetization oriented in-plane (e.g., [100]) and out-of-plane ([001]), recording the total energy for each orientation.
- Evidence: none

### Step 4: Magnetic anisotropy energy results
- Role: scored (load-bearing)
- Action: For each system, compute MAE = E_out-of-plane - E_in-plane (in eV) and determine easy-axis orientation: 'out-of-plane' if MAE > 0, else 'in-plane'. Write results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: system (string), E_perp_au_eV (float), E_inplane_au_eV (float), MAE_eV (float), easy_axis (string, 'in-plane' or 'out-of-plane')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The single scored output containing computed MAE and easy-axis orientation for each of the five slab systems.
- schema:
  - `type`: table
  - `required_columns`: `system`, `E_perp_au_eV`, `E_inplane_au_eV`, `MAE_eV`, `easy_axis`
  - `description`: Each row corresponds to one slab system. The checker recomputes easy_axis from MAE sign and compares to hidden expected orientations; correct sign for all five systems earns full credit.

Notes: Only the sign of MAE (easy-axis orientation) is scored. Absolute MAE values are not evaluated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "E_perp_au_eV",
          "E_inplane_au_eV",
          "MAE_eV",
          "easy_axis"
        ],
        "description": "Each row corresponds to one slab system. The checker recomputes easy_axis from MAE sign and compares to hidden expected orientations; correct sign for all five systems earns full credit."
      },
      "description": "The single scored output containing computed MAE and easy-axis orientation for each of the five slab systems."
    }
  ],
  "notes": "Only the sign of MAE (easy-axis orientation) is scored. Absolute MAE values are not evaluated."
}
```

## How you are scored
A hidden verifier will inspect your `results.csv`. For each of the five systems, it will check whether the reported easy-axis orientation matches the correct answer determined by the physics of the problem. The total reward is the fraction of systems for which the easy axis is correct (so all five correct gives a score of 1.0). The verifier may also verify that the `easy_axis` string is consistent with the sign of the MAE field. Simply submitting numbers without actually running the required FLAPW calculations will not pass this audit, because the correct orientations are not trivially guessable.
