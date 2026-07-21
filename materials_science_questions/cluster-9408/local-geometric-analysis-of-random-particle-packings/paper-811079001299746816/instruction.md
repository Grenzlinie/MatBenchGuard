# Macroscopic stress response of ordered bubble packings

## Problem background
Soft jammed materials like foams and emulsions are elastic solids above the jamming transition. Stress is transmitted through contacts between deformed particles. Conventional models assume pairwise additive two-body interaction forces, but real bubbles or droplets conserve volume — when a particle is squeezed at one contact, it expands elsewhere. This introduces a many-body coupling among all contacts of a given particle, modifying the force-displacement relation at each contact in a way that depends on the entire set of contact forces. The aim is to compute the macroscopic mechanical response of a face-centered cubic (fcc) monodisperse bubble packing, using an analytical many-body interaction model, and to quantify its predictions for three distinct loading modes.

## Approach
Implement the many-body interaction law derived from the theory of Morse and Witten for weakly deformed particles. The model expresses the radial surface displacement at a contact as the sum of a local logarithmic term (function of the force at that contact) and a non-local geometric coupling term that depends on all other contact forces on the same particle through a Green's function of the angular separation between contacts. To solve for the forces given a macroscopic deformation, use the iterative linearization algorithm: start from an initial force estimate, linearize the logarithmic term, solve the resulting linear system for new forces, and repeat until convergence. From the converged forces, compute the macroscopic stress tensor via the Irwin–Kirkwood relation. Apply this procedure to a periodic fcc unit cell at a packing fraction of 0.8, for three independent deformation modes:
- Isotropic compression (varying packing fraction φ).
- Isochoric uniaxial strain (extension along x₃, lateral contraction along x₁ and x₂).
- Simple shear (shear component along x₃).
For each mode, produce the corresponding stress component as a function of the deformation parameter (confinement pressure, normal stress difference, shear stress). The results will be compared against reference data from high-fidelity simulations.

## Reproduction target
Produce three CSV files that contain the macroscopic stress response of the fcc bubble packing, computed with the many-body interaction model and the iterative force solver:

1. `isotropic_pressure.csv`: First column `phi` (packing fraction, dimensionless), second column `pressure` (dimensionless confinement pressure Π·R₀/γ). Include at least rows at φ = 0.79, 0.81, 0.83, 0.85.
2. `uniaxial_stress.csv`: First column `extension_ratio_minus_one` (dimensionless λ−1), second column `normal_stress_difference` (σ₃₃−σ₁₁ in units of γ/R₀). Cover λ−1 from 0 to 0.15 with at least points at λ−1 = 0.02, 0.05, 0.08, 0.10, 0.12.
3. `shear_stress.csv`: First column `shear_strain` (dimensionless), second column `shear_stress` (σ₁₃ in units of γ/R₀). Cover shear strain from 0 to 0.2 with at least points at 0.05, 0.10, 0.15, 0.20.

The computed curves will be evaluated against hidden reference values obtained from independent high-fidelity simulations.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Implement many-body force solver
- Role: process
- Action: Implement the many-body interaction law (Eq. 6) and the iterative linearization algorithm to solve for contact forces in a face-centered cubic (fcc) monodisperse bubble packing at packing fraction 0.8, given a macroscopic deformation (isotropic compression, uniaxial strain, simple shear).
- Evidence: none

### Step 2: Isotropic compression pressure
- Role: scored (load-bearing)
- Action: Using the many-body force solver, compute the confinement pressure Π for isotropic compression of the fcc packing at packing fractions φ between 0.79 and 0.85. Output a CSV with columns: phi (dimensionless packing fraction) and pressure (dimensionless confinement pressure Π * R_o / γ).
- Output file: `/app/outputs/isotropic_pressure.csv`
- Format: csv
- Contract: columns: phi (float), pressure (float). Must include rows at φ=0.79,0.81,0.83,0.85 at minimum.
- Scoring: scored by hidden verifier

### Step 3: Uniaxial normal stress difference
- Role: scored
- Action: Using the many-body force solver, compute the normal stress difference σ_{33}-σ_{11} for isochoric uniaxial strain with extension ratio λ-1 ranging from 0 to 0.15. Output a CSV with columns: extension_ratio_minus_one (λ-1, dimensionless) and normal_stress_difference (σ_{33}-σ_{11} in units of γ/R_o).
- Output file: `/app/outputs/uniaxial_stress.csv`
- Format: csv
- Contract: columns: extension_ratio_minus_one (float), normal_stress_difference (float). Must cover λ-1 in [0, 0.15] with sufficient points including λ-1=0.02,0.05,0.08,0.10,0.12.
- Scoring: scored by hidden verifier

### Step 4: Shear stress
- Role: scored
- Action: Using the many-body force solver, compute the shear stress σ_{13} for simple shear deformation with shear strain ranging from 0 to 0.2. Output a CSV with columns: shear_strain (dimensionless) and shear_stress (σ_{13} in units of γ/R_o).
- Output file: `/app/outputs/shear_stress.csv`
- Format: csv
- Contract: columns: shear_strain (float), shear_stress (float). Must cover shear strain in [0, 0.2] with sufficient points including shear_strain=0.05,0.10,0.15,0.20.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/isotropic_pressure.csv`
- `/app/outputs/uniaxial_stress.csv`
- `/app/outputs/shear_stress.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### isotropic_pressure.csv
- path: `/app/outputs/isotropic_pressure.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Confinement pressure vs packing fraction for isotropic compression of fcc bubble packing, computed using the many-body model.
- schema:
  - `type`: table
  - `required_columns`: `phi`, `pressure`
  - `units`:
    - `phi`: dimensionless
    - `pressure`: Π * R_o / γ

### uniaxial_stress.csv
- path: `/app/outputs/uniaxial_stress.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normal stress difference vs extension ratio for isochoric uniaxial strain of fcc bubble packing, computed using the many-body model.
- schema:
  - `type`: table
  - `required_columns`: `extension_ratio_minus_one`, `normal_stress_difference`
  - `units`:
    - `extension_ratio_minus_one`: dimensionless
    - `normal_stress_difference`: γ/R_o

### shear_stress.csv
- path: `/app/outputs/shear_stress.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Shear stress vs shear strain for simple shear deformation of fcc bubble packing, computed using the many-body model.
- schema:
  - `type`: table
  - `required_columns`: `shear_strain`, `shear_stress`
  - `units`:
    - `shear_strain`: dimensionless
    - `shear_stress`: γ/R_o

Notes: The agent computes the many-body interaction model predictions for the fcc packing under isotropic compression, uniaxial strain, and simple shear. The hidden checker compares the computed stress curves to Surface Evolver simulation data from the literature, using relative and absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "isotropic_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi",
          "pressure"
        ],
        "units": {
          "phi": "dimensionless",
          "pressure": "Π * R_o / γ"
        }
      },
      "description": "Confinement pressure vs packing fraction for isotropic compression of fcc bubble packing, computed using the many-body model."
    },
    {
      "file": "uniaxial_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "extension_ratio_minus_one",
          "normal_stress_difference"
        ],
        "units": {
          "extension_ratio_minus_one": "dimensionless",
          "normal_stress_difference": "γ/R_o"
        }
      },
      "description": "Normal stress difference vs extension ratio for isochoric uniaxial strain of fcc bubble packing, computed using the many-body model."
    },
    {
      "file": "shear_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "shear_strain",
          "shear_stress"
        ],
        "units": {
          "shear_strain": "dimensionless",
          "shear_stress": "γ/R_o"
        }
      },
      "description": "Shear stress vs shear strain for simple shear deformation of fcc bubble packing, computed using the many-body model."
    }
  ],
  "notes": "The agent computes the many-body interaction model predictions for the fcc packing under isotropic compression, uniaxial strain, and simple shear. The hidden checker compares the computed stress curves to Surface Evolver simulation data from the literature, using relative and absolute tolerances."
}
```

## How you are scored
Each scored artifact (`isotropic_pressure.csv`, `uniaxial_stress.csv`, `shear_stress.csv`) is evaluated independently by a hidden verifier. The verifier reads your output files and compares the reported stress values at specific points to hidden reference data using error metrics (relative error for pressure, absolute error for stress differences). It also checks internal consistency: the sum of forces on each particle must be zero (within machine precision) and the computed stress tensor must be symmetric (off-diagonal differences within a small threshold). The per‑artifact scores are combined into a final reward. Reporting a number that matches the external reference without actually running the many-body solver and computing the forces will not satisfy the consistency checks; all steps contribute to the final outcome.
