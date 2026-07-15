# Free vibration analysis of FG-CNTRC doubly curved shell panels

## Problem background
This work examines the free vibration of moderately thick doubly curved shell panels made of a polymer matrix reinforced with carbon nanotubes (CNTs). The CNTs are distributed either uniformly or in a functionally graded pattern across the thickness, following one of five distribution types. The panels can assume spherical, cylindrical, hyperbolic paraboloid, or flat plate geometries. The objective is to compute the fundamental (lowest) nondimensional natural frequency of these nanocomposite panels under various combinations of curvature, CNT distribution, CNT volume fraction, and edge support conditions. The computed frequencies quantify how the stiffness and mass distribution influence the dynamic response.

## Approach
The effective orthotropic material properties are obtained via the modified rule of mixtures, which expresses the through-thickness profiles of elastic moduli, shear modulus, Poisson's ratio, and density as functions of the CNT volume fraction and CNT efficiency parameters. Using the first-order shear deformation theory (FSDT) for moderately thick shells, the governing equations of motion are derived in terms of the mid-surface displacements and rotations. Integrating the effective properties through the thickness yields the stiffness coefficients (extensional, coupling, bending, and transverse shear) and the mass moments of inertia. A shear correction factor of 5/6 is applied.

Galerkin's method is employed to discretize the equations. The mid-surface displacements and rotations are expanded in trigonometric trial functions that satisfy the boundary conditions—simply supported (SSSS) or clamped (CCCC) on all edges. Substituting the expansions and integrating over the panel surface produces a generalized eigenvalue problem. Solving for the smallest eigenvalue yields the natural frequency, which is then nondimensionalized using the matrix material properties and panel dimensions. This procedure is repeated for every combination of geometry, boundary condition, CNT distribution, and CNT volume fraction to generate the required dataset.

## Reproduction target
Produce the nondimensional fundamental frequency for FG-CNTRC doubly curved panels over the following parameter grid:

- Geometries (defined by the curvature ratios a/Rx and b/Ry):
  - spherical       : a/Rx = 0.5, b/Ry = 0.5
  - hyperbolic paraboloid : a/Rx = 0.5, b/Ry = -0.5
  - cylindrical      : a/Rx = 0.5, b/Ry = 0
  - plate            : a/Rx = 0,   b/Ry = 0

- Boundary conditions: SSSS (all edges simply supported) and CCCC (all edges clamped).

- CNT distributions: UD (uniform), FG-A (linear decrease from top to bottom), FG-V (linear increase), FG-X (peak at mid-surface), FG-O (peak at surfaces).

- CNT volume fraction V* : 0.11, 0.14, 0.17.

The frequency is defined as Ω = ω a²/h √(ρᵐ/Eᵐ), where ω is the circular frequency, h the panel thickness, and ρᵐ, Eᵐ the matrix density and Young's modulus. The specific matrix and CNT properties (including CNT efficiency parameters) are provided in the material description.

Write the results to a CSV file with one row per combination (120 rows total). Columns: boundary_condition, geometry_type, CNT_distribution, V_star, frequency. The row order is not prescribed, but every combination must be present. Use sufficient Galerkin modes to ensure convergence; at least 18 modes in each direction is recommended.

## Material and geometric parameters

The composite consists of a PmPV polymer matrix and (10,10) single-walled carbon nanotubes as reinforcement. The matrix properties are:
- Young's modulus: E^m = 2.1 GPa
- Poisson's ratio: ν^m = 0.34
- Density: ρ^m = 1150 kg/m³

The CNT properties are:
- Longitudinal Young's modulus: E11^CNT = 5.6466 TPa
- Transverse Young's modulus: E22^CNT = 7.0800 TPa
- In-plane shear modulus: G12^CNT = 1.9445 TPa
- Poisson's ratios: ν12^CNT = ν21^CNT = 0.175
- Density: ρ^CNT = 1400 kg/m³

The CNT efficiency parameters η1, η2, η3 (with η3 = η2) depend on the CNT volume fraction V_CNT^*:
- V_CNT^* = 0.11: η1 = 0.149, η2 = 0.934
- V_CNT^* = 0.14: η1 = 0.150, η2 = 0.941
- V_CNT^* = 0.17: η1 = 0.149, η2 = 1.381

The panel aspect ratio is a/b = 1 and the thickness ratio is a/h = 20. The shear correction factor is K_s = 5/6.

The transverse shear moduli G13 and G23 are taken as equal to G12 (i.e., G13 = G12 and G23 = G12) because the CNT reinforcement does not alter the transverse shear properties appreciably in the modified rule of mixtures.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute effective material properties
- Role: process
- Action: Using the modified rule of mixtures and the given CNT/polymer properties, compute through-thickness profiles of E11(z), E22(z), G12(z), ν12(z), ρ(z) for each CNT distribution type and V_CNT^*.
- Evidence: `/app/outputs/effective_properties.npz`

### Step 2: Compute stiffness coefficients and mass moments
- Role: process
- Action: Integrate the effective material properties over the thickness to obtain stiffness coefficients A_i, B_i, C_i, D1, F1 and mass moments I0, I1, I2. Use a shear correction factor K_s = 5/6.
- Evidence: `/app/outputs/coefficients.json`

### Step 3: Solve for nondimensional frequencies
- Role: scored (load-bearing)
- Action: For each combination of geometry (a/R_x, b/R_y), boundary condition (SSSS or CCCC), CNT distribution type, and V_CNT^*, assemble the mass and stiffness matrices using Galerkin's method with appropriate trigonometric trial functions and solve the generalized eigenvalue problem. Extract the lowest eigenvalue to compute the nondimensional fundamental frequency Ω = ω a²/h sqrt(ρ^m/E^m). Output all results to a CSV file.
- Output file: `/app/outputs/frequencies_fg_cntrc.csv`
- Format: csv
- Contract: boundary_condition,geometry_type,CNT_distribution,V_star,frequency
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequencies_fg_cntrc.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequencies_fg_cntrc.csv
- path: `/app/outputs/frequencies_fg_cntrc.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Nondimensional fundamental frequency Ω for each combination. The verifier compares each frequency to the hidden reference values with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `boundary_condition`, `geometry_type`, `CNT_distribution`, `V_star`, `frequency`
  - `units`:
    - `frequency`: nondimensional

Notes: The agent must produce exactly 120 rows covering all 2×4×5×3 parameter combinations. The nondimensional frequency values are compared to hidden reference values from the original paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequencies_fg_cntrc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "boundary_condition",
          "geometry_type",
          "CNT_distribution",
          "V_star",
          "frequency"
        ],
        "units": {
          "frequency": "nondimensional"
        }
      },
      "description": "Nondimensional fundamental frequency Ω for each combination. The verifier compares each frequency to the hidden reference values with a tolerance."
    }
  ],
  "notes": "The agent must produce exactly 120 rows covering all 2×4×5×3 parameter combinations. The nondimensional frequency values are compared to hidden reference values from the original paper."
}
```

## How you are scored
A hidden verifier reads your final frequency CSV and compares each nondimensional frequency to the corresponding reference value derived from the original investigation. The score is the fraction of rows whose frequency lies within a prescribed relative tolerance. The intermediate evidence files (effective_properties.npz and coefficients.json) document your workflow but are not numerically scored; only the CSV determines the final reward. Full credit is awarded if all 120 frequencies are within tolerance; partial credit scales linearly with the number of matched rows.
