# Homogenization-Based Elastic Property Prediction for Macroporous Scaffolds

## Problem background
Designing porous scaffolds for bone regeneration requires control of mechanical properties. The elastic modulus, Poisson ratio, and shear modulus of a scaffold depend strongly on its macroporosity geometry and volume fraction. This task uses computational homogenization to predict the effective elastic constants of periodic hydroxyapatite cement scaffolds with an orthogonal array of 1 mm cylindrical pores. By analyzing cubic representative volume elements (RVEs) with varying pore size/spacing (aspect ratio), one can map the relationship between pore geometry and mechanical performance – a relationship that can be compared with experimental measurements.

## Approach
The workflow applies a displacement-based linear elastic finite‑element homogenisation procedure. For each RVE, a cubic unit cell with a central cylindrical pore is discretised into hexahedral voxel elements. The solid phase is modelled as isotropic with known Young's modulus (13.5 GPa) and Poisson ratio (0.14). Periodic boundary conditions are imposed, and the six canonical homogenisation load cases are solved to obtain the effective fourth‑order elasticity tensor. Because the RVE geometry exhibits cubic symmetry, three independent constants fully characterise the effective behaviour: the Young modulus along a principal axis, the Poisson ratio, and the shear modulus. These are extracted from the effective elasticity tensor and written to a CSV file for seven prescribed aspect ratios covering volume fractions from near‑zero to near‑unity. The computed values can then be contrasted with the paper's homogenisation predictions.

## Reproduction target
Produce a CSV file `homogenization_results.csv` containing the three effective elastic constants for each of the seven RVEs defined by the aspect ratios 0.05, 0.133, 0.33, 0.5, 0.66, 0.8, 1.0 (corresponding volume fractions 0.007, 0.036, 0.206, 0.403, 0.623, 0.779, 0.943). Each row must list: aspect_ratio, volume_fraction, the effective Young's modulus (GPa), Poisson's ratio (dimensionless), and shear modulus (GPa). The hidden verifier will compare these values to the reference homogenization curve.

## Assets

- Mesh generation tool (e.g., Gmsh): gmsh
- Finite-element solver with homogenization capabilities (e.g., FEniCS): fenics

## Workflow steps

### Step 1: RVE Mesh Generation
- Role: process
- Action: Generate finite-element meshes for the seven RVEs with aspect ratios 0.05, 0.133, 0.33, 0.5, 0.66, 0.8, 1.0, corresponding to volume fractions 0.007, 0.036, 0.206, 0.403, 0.623, 0.779, 0.943. Each RVE is a cubic unit cell containing a central cylindrical pore of diameter defined by aspect ratio (diameter/spacing). Use voxel-based meshing with hexahedral elements.
- Evidence: `/app/outputs/mesh_generation.log`

### Step 2: Homogenization Simulation
- Role: scored (load-bearing)
- Action: Using the generated RVE meshes, assign isotropic linear elastic properties (Young's modulus E=13.5 GPa, Poisson's ratio ν=0.14) to the solid phase. Solve the six canonical homogenization problems with periodic boundary conditions to obtain the effective elastic tensor for each RVE. Compute and extract the three independent elastic constants: effective Young's modulus along principal axes, effective Poisson's ratio, and effective shear modulus. Write a CSV file with columns: aspect_ratio, volume_fraction, Youngs_modulus_GPa, Poissons_ratio, Shear_modulus_GPa.
- Output file: `/app/outputs/homogenization_results.csv`
- Format: csv
- Contract: CSV with columns: aspect_ratio (float), volume_fraction (float), Youngs_modulus_GPa (float), Poissons_ratio (float), Shear_modulus_GPa (float). One row per RVE.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/homogenization_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### homogenization_results.csv
- path: `/app/outputs/homogenization_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Homogenized elastic constants for seven RVE aspect ratios (volume fractions). The checker compares each row’s values against the paper’s homogenization curve (Fig. 7) using relative error for moduli and absolute error for Poisson’s ratio.
- schema:
  - `type`: table
  - `required_columns`: `aspect_ratio`, `volume_fraction`, `Youngs_modulus_GPa`, `Poissons_ratio`, `Shear_modulus_GPa`
  - `units`:
    - `Youngs_modulus_GPa`: GPa
    - `Shear_modulus_GPa`: GPa
    - `Poissons_ratio`: dimensionless

Notes: Only the computational homogenization result is scored; experimental mechanical testing and comparison are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "homogenization_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "aspect_ratio",
          "volume_fraction",
          "Youngs_modulus_GPa",
          "Poissons_ratio",
          "Shear_modulus_GPa"
        ],
        "units": {
          "Youngs_modulus_GPa": "GPa",
          "Shear_modulus_GPa": "GPa",
          "Poissons_ratio": "dimensionless"
        }
      },
      "description": "Homogenized elastic constants for seven RVE aspect ratios (volume fractions). The checker compares each row’s values against the paper’s homogenization curve (Fig. 7) using relative error for moduli and absolute error for Poisson’s ratio."
    }
  ],
  "notes": "Only the computational homogenization result is scored; experimental mechanical testing and comparison are excluded."
}
```

## How you are scored
A hidden verifier reads your `homogenization_results.csv` and independently compares each row's three elastic constants to the paper's expected reference values. The comparison uses per‑quantity tolerances that account for legitimate differences arising from mesh, solver, and implementation details. Your overall score is the fraction of rows that meet the required tolerances across all three constants, and the reward is proportional to that fraction. Reporting numbers without actually running the homogenization pipeline will not match the hidden reference and will receive low reward.
