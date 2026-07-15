# Snow Crystal Growth Simulation using Lattice Boltzmann Volumetric Reactive Boundary

## Problem background
Understanding how ice crystals grow from supersaturated water vapor in clouds is a fundamental problem in atmospheric physics. Crystal morphology can range from compact, roughly circular shapes to intricate, branched dendritic structures, depending on environmental conditions such as temperature, supersaturation, and the relative rates of diffusion and surface deposition. Reproducing this morphological variation is challenging because it requires capturing the interplay between vapor‑phase diffusion, surface reaction kinetics, and the evolving crystal shape. This task addresses the problem by applying a lattice Boltzmann method with a volumetric reactive boundary condition to simulate two‑dimensional crystal growth. The goal is to compute how the geometry of the growing solid phase changes with the Damköhler number and supersaturation, and to validate the simulation against an analytical reaction‑diffusion benchmark.

## Approach
The simulation is built on a two‑dimensional, nine‑speed (D2Q9) lattice Boltzmann model. Vapor‑phase water concentration evolves according to a convection‑diffusion equation recovered from the lattice Boltzmann scheme. At the fluid‑solid interface, a first‑order kinetic reaction removes mass from the vapor according to the local supersaturation, and the accumulated solid mass advances the interface in discrete steps. The growth direction is randomized to avoid grid anisotropy. Physical parameters (saturation vapor density over ice, vapor diffusivity, and the kinetic deposition rate) are obtained from published thermophysical expressions and used to scale the lattice Boltzmann model parameters (D_m, k_m) via similarity analysis. The key control parameter is the Damköhler number, Da, which sets the relative strength of reactive deposition versus diffusion. First, the reactive transport scheme is tested by solving a steady‑state diffusion‑reaction problem on a rectangular domain and comparing the resulting concentration field with the analytical solution. Then, two crystal growth simulations are performed, each at a different Da value, from a small central seed in a supersaturated environment. The resulting solid‑phase patterns are analyzed to quantify their morphology.

## Reproduction target
Implement the lattice Boltzmann simulator and produce the following artifacts:
1. For the rectangular‑domain validation (Da = 1440, domain size 125×100 lattice units), a file containing the steady‑state solute concentration at every grid point.
2. Two growth simulations on a 100×100 lattice, both at T = –15 °C, S = 1.20, with random growth and 750 000 time steps, but at two different Da values (Da = 16 and Da = 400). The outputs are the final solid mass arrays.
3. From these mass arrays, compute the box‑counting fractal dimension of each crystal.
4. Compute the theoretical critical dendrite arm spacing λ_c using the surface‑vapor‑layer model, with the same physical parameters and conditions.
All results are to be written to the specified output files under /app/outputs.

## Assets

- D2Q9 lattice Boltzmann method description
- Physical parameters for water vapor and ice
- Python 3 with numpy, scipy: numpy scipy

## Workflow steps

### Step 1: Validation simulation (Da=1440)
- Role: scored
- Action: Set up a 2D D2Q9 LB model with volumetric reactive boundary for diffusion only. Use a rectangular domain of 125x100 lattice units with reaction at the upper boundary, constant concentration at x=0, no-flux elsewhere, parameters D_m=3.47e-3, k_m=0.05 (Da=1440), with constant concentration at x=0 C0=10.0 and equilibrium concentration Ceq=1.0 (the analytical solution uses these values). Run to steady state and output the concentration at every node.
- Output file: `/app/outputs/step_01_validation_contour.csv`
- Format: csv
- Contract: CSV with columns: x (integer, 0..124), y (integer, 0..99), concentration (float).
- Scoring: scored by hidden verifier

### Step 2: Scaling analysis and parameter setup
- Role: process
- Action: Using temperature T = -15°C, pressure p = 900 mbar, condensation coefficient χ = 0.1, compute physical parameters: saturation concentration over ice, diffusivity, kinetic rate constant, and the fundamental length scale λ_p. Then using scaling relations and the LB model constants (l_m=100, D_m=0.0104), compute the required k_m values that yield Da = 16 and Da = 400. Store all computed parameters.
- Evidence: `/app/outputs/scaling_parameters.json`

### Step 3: Random growth simulation Da=16
- Role: scored (load-bearing)
- Action: On a 100x100 lattice, initialize a small seed crystal at the centre. Set supersaturation S = 1.20 (C_far = S * C_sat) and LB parameters from previous step for Da=16. Use the volumetric reactive boundary scheme with random growth rule. Run simulation for 750,000 time steps. Output the final solid mass at every lattice node.
- Output file: `/app/outputs/step_02_growth_da16.csv`
- Format: csv
- Contract: CSV with columns: x (integer, 0..99), y (integer, 0..99), solid_mass (float).
- Scoring: scored by hidden verifier

### Step 4: Random growth simulation Da=400
- Role: scored (load-bearing)
- Action: Repeat the growth simulation for Da=400 using the parameters from previous step, all other conditions identical (100x100 lattice, S=1.20, T=-15°C, random growth, 750,000 time steps). Output the final solid mass array.
- Output file: `/app/outputs/step_03_growth_da400.csv`
- Format: csv
- Contract: CSV with columns: x (integer, 0..99), y (integer, 0..99), solid_mass (float).
- Scoring: scored by hidden verifier

### Step 5: Compute fractal dimensions
- Role: scored
- Action: From the two solid mass arrays, binarise by thresholding (solid node if mass >= 0.5). Compute the box-counting fractal dimension D_f for each crystal using square box sizes from 1 to the grid size. Output the two fractal dimensions.
- Output file: `/app/outputs/step_04_fractal_dimensions.json`
- Format: json
- Contract: JSON object with keys 'da16' (float) and 'da400' (float).
- Scoring: scored by hidden verifier

### Step 6: Compute theoretical dendrite spacing limit
- Role: scored
- Action: Using the physical parameters (λ_p = D_p/k_p ≈ 1.5 µm, supersaturation S = 1.20), compute the critical dendrite spacing λ_c from the formula λ_c = 2π * λ_p * sqrt(S / (S-1)). Report λ_c in micrometers.
- Output file: `/app/outputs/step_05_theoretical_critical_spacing.json`
- Format: json
- Contract: JSON object with key 'lambda_c' (float, units µm).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_validation_contour.csv`
- `/app/outputs/step_02_growth_da16.csv`
- `/app/outputs/step_03_growth_da400.csv`
- `/app/outputs/step_04_fractal_dimensions.json`
- `/app/outputs/step_05_theoretical_critical_spacing.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_validation_contour.csv
- path: `/app/outputs/step_01_validation_contour.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Steady-state solute concentration field for the reactive boundary benchmark (Da=1440). Checker recomputes RMSE against the analytical solution.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `concentration`
  - `items`: object
  - `required`: object
  - `units`:
    - `concentration`: dimensionless concentration

### step_02_growth_da16.csv
- path: `/app/outputs/step_02_growth_da16.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Final solid mass array after crystal growth at Da=16. The checker audited shape and non‑trivial content; the actual fractal dimension is derived from this array.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `solid_mass`
  - `items`: object
  - `required`: object
  - `units`:
    - `solid_mass`: accumulated solid mass (lattice units)

### step_03_growth_da400.csv
- path: `/app/outputs/step_03_growth_da400.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Final solid mass array after crystal growth at Da=400. The checker audited shape and non‑trivial content; the actual fractal dimension is derived from this array.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `solid_mass`
  - `items`: object
  - `required`: object
  - `units`:
    - `solid_mass`: accumulated solid mass (lattice units)

### step_04_fractal_dimensions.json
- path: `/app/outputs/step_04_fractal_dimensions.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Box-counting fractal dimensions of the crystals at Da=16 and Da=400. The checker compares each to hidden threshold values (compact high, dendritic low) and also recomputes from the mass arrays for consistency.
- schema:
  - `type`: object
  - `required`: `da16`, `da400`
  - `items`: object
  - `units`:
    - `da16`: dimensionless
    - `da400`: dimensionless

### step_05_theoretical_critical_spacing.json
- path: `/app/outputs/step_05_theoretical_critical_spacing.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Theoretical dendrite spacing limit λ_c derived from the surface-vapor-layer model. Checked against the paper-calculated value within a tolerance.
- schema:
  - `type`: object
  - `required`: `lambda_c`
  - `items`: object
  - `units`:
    - `lambda_c`: micrometers

Notes: All output files are written under /app/outputs. The growth simulations are the core of the reproduction; the fractal dimensions are the primary scored headline with load-bearing property that requires the process and growth steps to have been executed. The theoretical spacing is a supporting scored output.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_validation_contour.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "concentration"
        ],
        "items": {},
        "required": {},
        "units": {
          "concentration": "dimensionless concentration"
        }
      },
      "description": "Steady-state solute concentration field for the reactive boundary benchmark (Da=1440). Checker recomputes RMSE against the analytical solution."
    },
    {
      "file": "step_02_growth_da16.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "solid_mass"
        ],
        "items": {},
        "required": {},
        "units": {
          "solid_mass": "accumulated solid mass (lattice units)"
        }
      },
      "description": "Final solid mass array after crystal growth at Da=16. The checker audited shape and non‑trivial content; the actual fractal dimension is derived from this array."
    },
    {
      "file": "step_03_growth_da400.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "solid_mass"
        ],
        "items": {},
        "required": {},
        "units": {
          "solid_mass": "accumulated solid mass (lattice units)"
        }
      },
      "description": "Final solid mass array after crystal growth at Da=400. The checker audited shape and non‑trivial content; the actual fractal dimension is derived from this array."
    },
    {
      "file": "step_04_fractal_dimensions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "da16",
          "da400"
        ],
        "items": {},
        "units": {
          "da16": "dimensionless",
          "da400": "dimensionless"
        }
      },
      "description": "Box-counting fractal dimensions of the crystals at Da=16 and Da=400. The checker compares each to hidden threshold values (compact high, dendritic low) and also recomputes from the mass arrays for consistency."
    },
    {
      "file": "step_05_theoretical_critical_spacing.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "lambda_c"
        ],
        "items": {},
        "units": {
          "lambda_c": "micrometers"
        }
      },
      "description": "Theoretical dendrite spacing limit λ_c derived from the surface-vapor-layer model. Checked against the paper-calculated value within a tolerance."
    }
  ],
  "notes": "All output files are written under /app/outputs. The growth simulations are the core of the reproduction; the fractal dimensions are the primary scored headline with load-bearing property that requires the process and growth steps to have been executed. The theoretical spacing is a supporting scored output."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently recomputes the key quantities from your output files. The process is:
- The validation concentration grid is compared against the analytical solution for the same boundary conditions. The reward reflects how closely your field matches the true solution.
- The growth mass arrays (Da=16 and Da=400) are read, binarized, and their fractal dimensions are recomputed by the verifier. These recomputed dimensions are compared against expected thresholds that characterize the compact‑to‑dendritic transition.
- The fractal dimensions you report in the JSON file are checked for consistency with the mass arrays; any discrepancy reduces the reward.
- The theoretical dendrite spacing λ_c is compared against a reference value derived from the simulation parameters.
Each scored stage carries a weight, and the final reward is the weighted sum across all stages. The main weight rests on the fractal dimensions and their consistency with the simulated crystals. Merely reporting numbers without genuinely running the simulation is detectable and will yield a low score.
