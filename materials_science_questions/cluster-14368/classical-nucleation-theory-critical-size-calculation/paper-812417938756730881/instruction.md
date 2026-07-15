# Critical Supersaturation in Nonuniform Vapor Nucleation

## Problem background
In classical nucleation theory, droplets form from a uniform supersaturated vapor. However, in many practical situations, such as diffusion cloud chambers, the vapor is nonuniform and clusters of molecules can diffuse away from the nucleation zone before they reach the critical size. This work extends the steady‑state cluster population balance by adding a volumetric diffusive‑loss term, leading to an equation that quantifies how diffusion increases the supersaturation needed to sustain a given nucleation rate. The task is to compute the resulting critical supersaturations for model compounds at various vapor pressures and to compare the nonuniform case (with diffusion loss) against the uniform case (no diffusion).

## Approach
The model adopts a planar‑slab geometry. The steady‑state cluster concentrations are described by a second‑order ordinary differential equation for the ratio f/N (actual concentration divided by the equilibrium distribution). The ODE contains terms for monomer addition/evaporation and a diffusion loss term characterized by a constant diffusion coefficient D. The equilibrium distribution N(n) follows the classical capillarity approximation. The ODE is discretized on a size grid using central finite differences, converting it into a tridiagonal linear system that is solved with Gaussian elimination (e.g., the Thomas algorithm). From the solution, the nucleation flux J at the critical nucleus size is evaluated. For a given saturation pressure P_e, an iterative root‑finding procedure (e.g., bisection) determines the supersaturation θ* for which J equals 1 cm⁻³ s⁻¹. The calculation is performed both with a non‑zero diffusion coefficient (D = 0.29 cm²/s) and with diffusion turned off (D = 0), allowing a direct assessment of the diffusion effect on the critical supersaturation.

## Reproduction target
You will implement the entire numerical pipeline and produce a table of critical supersaturations θ* for a set of saturation pressures P_e. The table must cover the following pressures (in torr): 1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6, all at a temperature of 293.15 K (20°C). For each P_e, compute θ* without diffusion (D = 0) and θ* with diffusion (D = 0.29 cm²/s). Write the results to a CSV file named `critical_supersaturation_table.csv` with the columns `P_e`, `theta_no_diff`, `theta_with_diff`. The hidden verifier will examine this table to assess how well your computed values reproduce the expected physical behavior.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Initialize model parameters and equilibrium distribution
- Role: process
- Action: Define all physical constants and model parameters (D, h, L, σ, v, T, m, k). For a given supersaturation θ and saturation pressure P_e, compute: monomer impingement rate β, cluster surface area S(n), equilibrium cluster concentration N(n) using the standard capillarity approximation, and the coefficient arrays g(n), h(n), d(n) for the ODE over a grid n=1 to 2n*.
- Evidence: none

### Step 2: Discretize ODE and solve for steady-state ratio
- Role: process
- Action: Discretize the linear ODE for u = f/N using central finite differences on the n-grid. Assemble the tridiagonal system with boundary conditions u(1)=1, u(2n*)=0 and solve it using Gaussian elimination (e.g., Thomas algorithm).
- Evidence: none

### Step 3: Compute nucleation rate at critical size
- Role: process
- Action: From the solved u(n), compute ∂u/∂n at the critical nucleus size n* (the size that maximizes the free-energy argument of N(n)). Evaluate the nucleation flux J* using the continuum flux expression.
- Evidence: none

### Step 4: Root-finding for critical supersaturation θ*
- Role: process
- Action: For a fixed saturation pressure P_e and all other parameters held constant, perform an iterative search over supersaturation θ (e.g., bisection or Brent's method) to find the value θ* such that J* = 1 cm⁻³ s⁻¹. Repeat the search for the uniform case (D=0) and the nonuniform case (D=0.29 cm²/s) at the same P_e.
- Evidence: none

### Step 5: Generate critical supersaturation comparison table
- Role: scored (load-bearing)
- Action: Run the θ* determination (stages s1-s4) for the set of saturation pressures P_e = 1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6 torr, all at T = 293.15 K. For each P_e, compute θ*_no_diff (D=0) and θ*_with_diff (D=0.29 cm²/s). Collect the results and write them as a CSV file.
- Output file: `/app/outputs/critical_supersaturation_table.csv`
- Format: csv
- Contract: CSV file with columns: P_e (torr), theta_no_diff (dimensionless), theta_with_diff (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_supersaturation_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_supersaturation_table.csv
- path: `/app/outputs/critical_supersaturation_table.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Table of critical supersaturations θ* for unit nucleation rate with and without diffusive loss, for seven saturation pressures at T=293.15 K. The checker recomputes the ratio of the two θ* values and verifies that it matches the paper's reported trend and threshold values.
- schema:
  - `type`: table
  - `required_columns`: `P_e`, `theta_no_diff`, `theta_with_diff`
  - `units`:
    - `P_e`: torr
    - `theta_no_diff`: dimensionless
    - `theta_with_diff`: dimensionless

Notes: The checker will compute the ratio theta_with_diff / theta_no_diff for each P_e and verify that it meets the paper's reported trend and thresholds. Gold values and tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_supersaturation_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "P_e",
          "theta_no_diff",
          "theta_with_diff"
        ],
        "units": {
          "P_e": "torr",
          "theta_no_diff": "dimensionless",
          "theta_with_diff": "dimensionless"
        }
      },
      "description": "Table of critical supersaturations θ* for unit nucleation rate with and without diffusive loss, for seven saturation pressures at T=293.15 K. The checker recomputes the ratio of the two θ* values and verifies that it matches the paper's reported trend and threshold values."
    }
  ],
  "notes": "The checker will compute the ratio theta_with_diff / theta_no_diff for each P_e and verify that it meets the paper's reported trend and thresholds. Gold values and tolerances are hidden."
}
```

## How you are scored
Your submission is scored by a hidden verifier program that reads your output table and independently checks the computed critical supersaturations. The verifier compares your values against reference criteria that reflect the underlying physical trends—such as how the ratio of the two θ* values changes with pressure, whether the supersaturation with diffusion is always larger than without, and whether certain threshold behaviors are present. The final reward is a number between 0 and 1, representing how well your results align with these expectations. Simply reporting a known number without a correct numerical implementation will not earn a high score. The verifier does not inspect your intermediate code or logs; the score is based solely on the CSV file.
