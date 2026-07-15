# Spectral Contact Solver Implementation and Validation

## Problem background
Nanoindentation experiments probe plasticity at the mesoscale, but interpreting the force-displacement response requires understanding the elastic contact and the stress fields that drive dislocation motion. Coupling discrete dislocation dynamics (DDD) with a contact mechanics solver has traditionally relied on expensive finite-element calculations. An efficient compute-driven alternative uses spectral methods: the contact problem is solved in reciprocal space via Fast Fourier Transforms, and the resulting volume stress field is obtained from a Fourier series representation of the elastic fields. Reproducing the elastic contact validation of this spectral solver — its force-depth curves, its stress fields, and its convergence with grid resolution — is essential to verify the solver’s correctness and the viability of the spectral approach for nanoindentation DDD.

## Approach
The core idea is to decouple the indentation contact problem into two efficient, FFT-based stages. First, the contact pressure between a rigid indenter and an isotropic elastic half-space is found by solving a Boussinesq-type convolution in reciprocal space. Using conjugate gradient iteration, the algorithm enforces the contact constraints (no interpenetration, zero pressure outside the contact) and outputs the normal pressure distribution on the surface. Second, with that pressure as a boundary condition, the full three-dimensional elastic stress field is computed through a Fourier series solution of the equilibrium equations for an isotropic half-space. The method requires only the elastic constants (Young's modulus, Poisson's ratio), the indenter geometry (a parabolic shape of given radius), and the dimensions of the periodic simulation cell. In this task you will implement this spectral solver from scratch using NumPy/SciPy and use it to generate three quantitative artifacts that verify the solver’s behavior under elastic contact.

## Reproduction target
Your goal is to produce three scored CSV artifacts that validate the spectral solver for an isotropic aluminium half-space (E=70 GPa, ν=0.3) under elastic contact with a rigid parabolic indenter:

1. **Force-displacement curves** — Compute the total contact force (nN) vs. indentation depth (nm) for indenter radii R=0.25 µm and R=1 µm, each with simulation box lengths L=5, 10, 25 µm, all using a fixed 64×64 surface grid. Provide depth points from 0 to 200 nm in steps ≤ 1 nm.
2. **Stress field on a vertical slice** — For the case R=1 µm, L=5 µm, indentation depth d=100 nm, compute the σzz stress component (Pa) along a vertical line at x=0, from z=–2 µm to z=0 with a step ≤ 0.01 µm.
3. **Convergence with grid resolution** — For the same vertical slice (R=1 µm, L=5 µm, d=100 nm), compute σzz for surface grid resolutions N=32, 64, 128, 256, 512 and report the normalized mean-square error (MSE) relative to a reference solution obtained at N=1024².

Each artifact must be a CSV file with the exact columns and units specified in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implementation of the spectral solver
- Role: process
- Action: Implement the FFT-based contact solver and the volume stress solver for an isotropic half-space in Python, using NumPy/SciPy. The code must accept elastic constants (E, ν), indenter geometry (radius), surface grid size (Nx, Ny), box dimensions, and indentation depth schedule, and produce contact pressure and the full stress field. Use the Boussinesq kernel in reciprocal space and conjugate gradient iteration for the contact problem.
- Evidence: `/app/outputs/code_commit.log`

### Step 2: Elastic force-displacement curves for parabolic indenter
- Role: scored
- Action: Using the completed solver, compute force vs. depth for a parabolic indenter of radius R=0.25 µm and R=1 µm on an isotropic aluminium half-space (E=70 GPa, ν=0.3) with box lengths L=5, 10, 25 µm and a fixed 64×64 surface grid. For each combination, output the total contact force (nN) at depth increments of at most 1 nm from 0 to 200 nm.
- Output file: `/app/outputs/force_depth_parabolic.csv`
- Format: csv
- Contract: Columns: R_um (float, indenter radius in µm), L_um (float, box length in µm), depth_nm (float, indentation depth in nm), force_nN (float, total contact force in nN). All rows for the required combinations must be present.
- Scoring: scored by hidden verifier

### Step 3: Stress field on a vertical slice
- Role: scored
- Action: Using the solver, compute the σzz stress component (Pa) on a vertical line at x=0 for the case R=1 µm, L=5 µm, indentation depth d=100 nm. Sample z from –2 µm to 0 with a step of at most 0.01 µm.
- Output file: `/app/outputs/stress_slice_parabolic.csv`
- Format: csv
- Contract: Columns: z_um (float, coordinate in µm), sigma_zz_Pa (float, stress component in Pa). One row per z point, ordered.
- Scoring: scored by hidden verifier

### Step 4: Convergence of spectral solver with grid resolution
- Role: scored (load-bearing)
- Action: Compute the σzz stress field on the same vertical slice (R=1 µm, L=5 µm, d=100 nm) for surface grid resolutions N=32, 64, 128, 256, 512. For each resolution, calculate the normalized Mean Square Error (MSE) relative to a reference solution obtained with N=1024 (run the solver at 1024² to generate the reference). Output the grid size and corresponding MSE.
- Output file: `/app/outputs/convergence_mse.csv`
- Format: csv
- Contract: Columns: grid_size (int, pixels per side), MSE (float, dimensionless). One row per resolution.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/force_depth_parabolic.csv`
- `/app/outputs/stress_slice_parabolic.csv`
- `/app/outputs/convergence_mse.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### force_depth_parabolic.csv
- path: `/app/outputs/force_depth_parabolic.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Force vs. depth curves; checker verifies Hertzian scaling (slope and R²) and structural consistency.
- schema:
  - `type`: table
  - `required_columns`: `R_um`, `L_um`, `depth_nm`, `force_nN`
  - `units`:
    - `R_um`: µm
    - `L_um`: µm
    - `depth_nm`: nm
    - `force_nN`: nN

### stress_slice_parabolic.csv
- path: `/app/outputs/stress_slice_parabolic.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: σzz stress on a vertical line; checker verifies compressive (negative) and monotonic profile.
- schema:
  - `type`: table
  - `required_columns`: `z_um`, `sigma_zz_Pa`
  - `units`:
    - `z_um`: µm
    - `sigma_zz_Pa`: Pa

### convergence_mse.csv
- path: `/app/outputs/convergence_mse.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: MSE vs. grid resolution; checker verifies strictly decreasing trend and plausible range.
- schema:
  - `type`: table
  - `required_columns`: `grid_size`, `MSE`
  - `units`: object

Notes: All scoring is structural (T3). No hidden numerical references are required; the verifier checks physically-required trends and shape properties of the submitted CSV artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "force_depth_parabolic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "R_um",
          "L_um",
          "depth_nm",
          "force_nN"
        ],
        "units": {
          "R_um": "µm",
          "L_um": "µm",
          "depth_nm": "nm",
          "force_nN": "nN"
        }
      },
      "description": "Force vs. depth curves; checker verifies Hertzian scaling (slope and R²) and structural consistency."
    },
    {
      "file": "stress_slice_parabolic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z_um",
          "sigma_zz_Pa"
        ],
        "units": {
          "z_um": "µm",
          "sigma_zz_Pa": "Pa"
        }
      },
      "description": "σzz stress on a vertical line; checker verifies compressive (negative) and monotonic profile."
    },
    {
      "file": "convergence_mse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "grid_size",
          "MSE"
        ],
        "units": {}
      },
      "description": "MSE vs. grid resolution; checker verifies strictly decreasing trend and plausible range."
    }
  ],
  "notes": "All scoring is structural (T3). No hidden numerical references are required; the verifier checks physically-required trends and shape properties of the submitted CSV artifacts."
}
```

## How you are scored
A hidden verifier inspects each output file independently. It first checks that every file conforms to its required columns and format. For the force-depth curves it recomputes selected force values from your CSV and compares them against reference expectations, also verifying the Hertzian scaling relation. For the stress slice it computes the L2 error of your σzz values relative to a hidden reference solution, normalized by the reference maximum. For the convergence artifact it enforces that the reported MSE strictly decreases as the grid size increases. The verifier combines the scores from these checks into a single final reward in [0,1]; reporting numbers without proper computation will not satisfy the checks.
