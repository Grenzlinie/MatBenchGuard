# Effect of Hard-Constraint Degree on PINN Accuracy for Navier-Stokes Flows

## Problem background
Physics-informed neural networks (PINNs) solve partial differential equations by embedding physical laws (such as the Navier‑Stokes equations) into the loss function. For fluid flow problems, enforcing boundary conditions accurately is critical. A promising approach is to use *hard constraints*: instead of adding penalty terms for boundary residuals, the network output is multiplied by a smooth function that vanishes at the boundaries, guaranteeing that the boundary conditions are exactly satisfied. The smooth function typically contains a free parameter, the algebraic *degree* `k`, which controls how sharply the function approaches zero at the walls. Higher `k` produces a smoother transition, while `k=1` makes the function linear. This study investigates how the choice of the degree `k` influences the prediction accuracy of hard‑constraint PINNs for two incompressible laminar flows that have analytic solutions: Couette flow and plate shear flow. The goal is to quantify the relative errors of the PINN‑predicted velocity field for three values of `k` (1.0, 2.0, 3.0) across a range of Reynolds numbers, providing insight into the necessary smoothness of the boundary multiplier.

## Approach
We consider two classic fluid flow problems for which analytic velocity profiles are known.
1. **Couette flow**: pressure‑driven laminar flow between two parallel stationary plates. The analytic streamwise velocity follows a parabolic profile with maximum at the centerline.
2. **Plate shear flow**: flow driven by a moving upper plate (lower plate fixed) with zero pressure gradient; the analytic profile is linear.
For each flow we build a physics‑informed neural network that predicts the velocity components and pressure as functions of spatial coordinates. The boundary conditions are embedded as hard constraints: the network's raw output is multiplied by a smooth function `D(y) = a * ((d/2)^k − |y|^k)` (with plate half‑distance `d` and scaling factor `a` fixed to 1.0). This function vanishes at the solid walls `y = ±d/2`, forcing the predicted velocity to zero there. The degree `k` is the variable of interest; we examine three values: `k = 1.0, 2.0, 3.0`.
The loss function comprises the residual of the steady incompressible Navier‑Stokes equations (continuity and momentum). We do not add any boundary‑loss penalty terms because the hard constraint already guarantees the wall conditions.
For each flow and for each of five Reynolds numbers (Couette: 139, 313, 553, 1250, 2000; PlateShear: 60, 120, 240, 480, 960) we train a separate PINN for each `k` value, using a standard fully‑connected architecture (2 hidden layers, Swish activation). Reynolds number is varied by adjusting the viscosity (Couette) or the plate speed (PlateShear) while keeping the geometry fixed.
After training, we evaluate the predicted axial velocity field and compare it with the known analytic solution. For Couette flow the error metric is the relative error of the maximum axial velocity: `(u_pred_max − u_anal_max) / u_anal_max × 100%`. For plate shear flow we use the relative L2‑norm error over the grid points: `sqrt(Σ(u_pred_i − u_anal_i)²) / sqrt(Σ(u_anal_i)²) × 100%`. The output is a CSV file collecting all error percentages.

## Reproduction target
For Couette flow and plate shear flow, implement the hard‑constraint PINN method described above. Train models for the three degree values `k = 1.0, 2.0, 3.0` at the Reynolds numbers:
- Couette flow: 139, 313, 553, 1250, 2000
- Plate shear flow: 60, 120, 240, 480, 960
For every configuration compute the appropriate error metric: maximum axial velocity relative error (in percent) for Couette flow, and relative L2‑norm error of axial velocity (in percent) for plate shear flow. Produce a CSV file `/app/outputs/errors_summary.csv` with one row per (flow, Reynolds, k) and columns: `flow`, `Reynolds`, `k`, `error_percent`. All error percentages should be reported as floating‑point numbers.

## Assets

- PyTorch: https://pypi.org/project/torch/
- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Define flow problem configurations and analytic solutions
- Role: process
- Action: Prepare the domain coordinates, boundary conditions, and analytic velocity formulas for Couette flow and plate shear flow. For Couette flow, the analytic solution is u = (d^2/4 - y^2) * Δp/(2 ν ρ L) with d=0.1, L=1, ρ=1, Δp=0.1. For plate shear flow, the analytic velocity profile is u = u_u * (y + d/2)/d with d=0.1, u_u determined by Reynolds number (Re = u_u * d / ν), ν=1e-3. Determine the viscosity (Couette) or plate velocity (PlateShear) for each required Reynolds number (Couette: 139, 313, 553, 1250, 2000; PlateShear: 60, 120, 240, 480, 960). Set up the training grid points for each flow case.
- Evidence: `/app/outputs/config_log.txt`

### Step 2: Train hard-constraint PINN models
- Role: process
- Action: For each flow (Couette, PlateShear), each degree k in {1.0, 2.0, 3.0} and each Reynolds number listed above, construct and train a separate physics-informed neural network with hard constraints. Use the network architecture (2 hidden layers, 20 neurons per layer, Swish activation), training configuration (Adam optimizer, learning rate 1e-3, batch size = number of domain points, 50,000 epochs) and hard-constraint formulation (Equations 22 and 23 with scaling factor a=1.0) described in the paper. The loss is the residual of the steady Navier–Stokes equations. Save all trained model checkpoints for evaluation.
- Evidence: `/app/outputs/training_log.txt`

### Step 3: Evaluate models and compile error summary
- Role: scored (load-bearing)
- Action: For every trained model, evaluate the predicted axial velocity field against the analytic solution. For Couette flow, compute the maximum axial velocity relative error: (u_pred_max - u_anal_max)/u_anal_max * 100%. For plate shear flow, compute the relative L2‑norm error: sqrt(Σ(u_pred_i - u_anal_i)^2) / sqrt(Σ(u_anal_i)^2) * 100% over the grid points. Collect all error percentages and write them to /app/outputs/errors_summary.csv with one row per configuration.
- Output file: `/app/outputs/errors_summary.csv`
- Format: csv
- Contract: csv with columns: flow (one of 'Couette' or 'PlateShear'), Reynolds (int), k (float), error_percent (float, percentage)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/errors_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### errors_summary.csv
- path: `/app/outputs/errors_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Error percentages for Couette flow (maximum axial velocity relative error) and plate shear flow (relative L2‑norm error) for each Reynolds number and smooth‑function degree k. The checker compares these values to hidden paper‑reported references with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `flow`, `Reynolds`, `k`, `error_percent`
  - `units`:
    - `error_percent`: %

Notes: The hidden checker uses reference_match: it compares each error_percent against paper‑reported gold values with domain‑specific tolerances and structural conditions (e.g., k=1 errors must exceed 100%, k=2 errors must be below thresholds). The agent must provide all rows for the specified flows, Reynolds numbers, and k values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "errors_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "flow",
          "Reynolds",
          "k",
          "error_percent"
        ],
        "units": {
          "error_percent": "%"
        }
      },
      "description": "Error percentages for Couette flow (maximum axial velocity relative error) and plate shear flow (relative L2‑norm error) for each Reynolds number and smooth‑function degree k. The checker compares these values to hidden paper‑reported references with appropriate tolerances."
    }
  ],
  "notes": "The hidden checker uses reference_match: it compares each error_percent against paper‑reported gold values with domain‑specific tolerances and structural conditions (e.g., k=1 errors must exceed 100%, k=2 errors must be below thresholds). The agent must provide all rows for the specified flows, Reynolds numbers, and k values."
}
```

## How you are scored
A hidden verifier will read your `errors_summary.csv` and compare each reported error percentage against expected reference values using tolerance margins appropriate for reproduction of a stochastic training process. The comparison accounts for the fact that different hardware, random seeds, and implementation details can cause minor numerical differences. Additionally, the verifier may check that the relative magnitudes of the errors across the three `k` values are physically consistent: a correct implementation will produce a clearly distinguishable pattern that can be verified without reference to the exact numeric target values. The final score is a weighted combination of how many rows fall within tolerance and how well the structural pattern holds. Simply copying numbers from an unrelated source or reporting physically impossible values will result in a low score.
