# Calibration and adaptive modeling error reduction in atomic-to-continuum coupling of a harmonic lattice

## Problem background
This task addresses the adaptive control of modeling error in atomic-to-continuum coupling for two-dimensional particle lattices. The reference system is a 2D square lattice of particles interacting through harmonic pairwise potentials. Springs among nearest neighbors have constant k₁=10, diagonal nearest neighbors k₁d=5, and next-nearest neighbors k₂=2, with equilibrium lengths ℓ, √2ℓ, 2ℓ respectively (ℓ=1). A continuum model based on plane-stress linear elasticity is cheaper but introduces error. The procedure calibrates the continuum elastic constants from particle simulations, couples the two models using the Arlequin framework, and employs a goal-oriented adjoint-based error estimator to adaptively enlarge the particle domain around the applied load, aiming to reduce the modeling error in a user-chosen quantity of interest.

## Approach
Calibration: virtual representative volume element (RVE) experiments are performed on increasing n×n particle samples. Kinematic boundary conditions are applied to impose uniaxial tension, biaxial tension, and shear. From the particle strain energy and volume, the energy density is equated to that of a plane-stress linear elastic continuum. Young's modulus E, shear modulus G, and Poisson ratio ν are fitted by least-squares over several loading increments and sample sizes until convergence. Adaptive modeling: a boundary point-force problem is set up on a 51×51 lattice, bottom edge fixed, free elsewhere, with a vertical point load F=1 at particle P₁ applied in 10 increments of ΔF=0.1. An Arlequin coupled problem is constructed: a small particle domain surrounds the load, the continuum domain covers the entire lattice, and an overlap region with constant weighting (α_c=0.5) and H¹ coupling (β₀=0, β₁=1) is used. The continuum is discretized by bilinear quadrilateral finite elements with mesh size equal to the lattice spacing. After solving the forward problem, the quantity of interest Q = vertical displacement at P₁ is evaluated. To estimate the error, an adjoint problem is solved over an extended particle domain (one extra layer of particles). The residual-based error estimate is decomposed into element-wise contributions. The particle domain is then locally enlarged by switching continuum elements to the particle model wherever the element's residual contribution exceeds a fraction of the maximum contribution. This forward–adjoint–adapt cycle is repeated several times, recording the estimated relative error at each iteration.

## Reproduction target
Produce the following two artifacts:
(a) calibrated_constants.json – the converged plane-stress linear elastic constants (E, G, ν) for the given harmonic lattice, obtained from the RVE calibration procedure.
(b) error_sequence.csv – a CSV file with columns 'iteration' (integer) and 'relative_error' (float, percent), containing the estimated relative modeling error in the vertical displacement at the loaded particle. The first row corresponds to the initial surrogate (iteration 0) and subsequent rows to the estimates after each of six adaptive iterations (iterations 1 through 6). The sequence must be strictly decreasing.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Calibration of continuum elastic parameters via RVE virtual experiments
- Role: scored
- Action: For the square lattice with harmonic potentials (nearest and next-nearest neighbor interactions with specified spring constants and equilibrium lengths), perform RVE virtual experiments. For increasing RVE sizes, apply kinematic boundary conditions (uni-axial tension, bi-axial tension, shear), compute particle strain energy and macroscopic forces, assume energy density equivalence with plane-stress linear elasticity, and fit Young's modulus E, shear modulus G, Poisson ratio ν by least-squares until convergence. Write the converged values to calibrated_constants.json.
- Output file: `/app/outputs/calibrated_constants.json`
- Format: json
- Contract: {"E": <float>, "G": <float>, "ν": <float>}
- Scoring: scored by hidden verifier

### Step 2: Goal-oriented adaptive error reduction for boundary point load
- Role: scored (load-bearing)
- Action: Set up the boundary example: 51×51 particle lattice with the same harmonic potentials, bottom edge fixed, vertical point force applied at P1. Use the calibrated constants to define a continuum domain via plane-stress linear elasticity. Initialize an Arlequin coupled problem with a small particle domain, an overlapping continuum domain, and H¹ coupling. Compute the forward solution. Define the quantity of interest as the vertical displacement at P1. Extend the particle domain by one layer and solve an adjoint problem. Compute residual-based error estimate and its local contributions. Perform six adaptive iterations: locally switch continuum elements to particle model where the residual contribution exceeds a threshold, re-solve forward/adjoint, and re-estimate the error. Record the estimated relative error (percent) after the initial surrogate (iteration 0) and after each adaptation (iterations 1-6). Output the sequence to error_sequence.csv with columns iteration (int) and relative_error (float, percent).
- Output file: `/app/outputs/error_sequence.csv`
- Format: csv
- Contract: iteration (int), relative_error (float, percent)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calibrated_constants.json`
- `/app/outputs/error_sequence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calibrated_constants.json
- path: `/app/outputs/calibrated_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Calibrated Young's modulus E, shear modulus G, Poisson ratio ν for the harmonic square lattice. Compared to hidden reference values with a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `E`: float
    - `G`: float
    - `ν`: float

### error_sequence.csv
- path: `/app/outputs/error_sequence.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Estimated relative modeling error (percent) in the vertical displacement at the loaded particle after the initial surrogate (iteration 0) and after each of the six adaptive iterations. Lower error is better; scoring uses a threshold with a tolerance window.
- schema:
  - `type`: table
  - `required_columns`: `iteration`, `relative_error`
  - `units`:
    - `relative_error`: percent

Notes: No gold values are revealed. Scoring is based on comparing the calibrated constants to hidden reference values with a tolerance, and on comparing the error sequence entries to reference values (with tolerance) and checking monotonic decreasing trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calibrated_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E": "float",
          "G": "float",
          "ν": "float"
        }
      },
      "description": "Calibrated Young's modulus E, shear modulus G, Poisson ratio ν for the harmonic square lattice. Compared to hidden reference values with a tolerance."
    },
    {
      "file": "error_sequence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "iteration",
          "relative_error"
        ],
        "units": {
          "relative_error": "percent"
        }
      },
      "description": "Estimated relative modeling error (percent) in the vertical displacement at the loaded particle after the initial surrogate (iteration 0) and after each of the six adaptive iterations. Lower error is better; scoring uses a threshold with a tolerance window."
    }
  ],
  "notes": "No gold values are revealed. Scoring is based on comparing the calibrated constants to hidden reference values with a tolerance, and on comparing the error sequence entries to reference values (with tolerance) and checking monotonic decreasing trend."
}
```

## How you are scored
A hidden verifier independently reads your output files. For calibrated_constants.json, it compares your reported (E, G, ν) to reference values with an appropriate tolerance. For error_sequence.csv, it checks that the file contains exactly 7 rows (iterations 0–6), that the relative error sequence is strictly decreasing, and that each entry matches reference values within a tolerance. Each artifact contributes a weighted share to a final reward between 0 and 1. You are not given the reference values or tolerances; the task is to faithfully implement the calibration and adaptive coupling procedure and report your computed numbers.
