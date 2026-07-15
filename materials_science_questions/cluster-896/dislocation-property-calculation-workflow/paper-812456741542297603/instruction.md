# Steady Oscillating Dislocation Shape Calculation

## Problem background
Koehler's model describes edge-type dislocations pinned by impurities in a metal single crystal under oscillatory shear stress. The dimensionless displacement φ(z,τ) satisfies a damped wave equation with parameters ε (inertia) and δ (damping). The steady oscillatory motion is of interest for understanding dislocation behavior across a range of material parameters. This task reproduces the exact analytic steady-state solution for the spatial profiles U(z), V(z) and the total amplitude, and explores how the maximum centre amplitude depends on ε and δ.

## Approach
The particular steady-state oscillating solution is obtained by seeking a solution of the dimensionless partial differential equation in the form φ(z,τ)=U(z)cos(τ)+V(z)sin(τ). Substitution leads to a pair of ordinary differential equations that combine into a single complex equation for W(z)=U(z)+iV(z): W''+(iδ+ε)W = -1, with boundary conditions W(0)=W(1)=0. This is solved analytically to give W(z) = C₁ e^{α z} + C₂ e^{-α z} - 1/(iδ+ε), where α = ½[√(√(ε²+δ²)+δ)(1+i) - √(√(ε²+δ²)-δ)(1-i)] and the constants C₁, C₂ are determined from the boundary conditions. The transient (homogeneous) solution decays rapidly and is not needed; the complete spatial information is obtained by evaluating U(z)=Re(W(z)), V(z)=Im(W(z)), and the total amplitude A(z)=√(U²+V²).

## Reproduction target
Recompute the steady-state oscillating solution for given dimensionless parameters ε and δ. Produce three CSV files: (1) spatial profiles U(z), V(z), and total amplitude over z∈[0,1] at nominal parameters ε=10⁻⁶, δ=0.2; (2) maximum amplitude at the centre z=0.5 as a function of δ (with ε=10⁻⁶); (3) maximum amplitude at the centre as a function of ε (with δ=0.2).

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute shape at nominal parameters
- Role: scored (load-bearing)
- Action: Evaluate the exact steady oscillating solution for the Koehler dislocation model with dimensionless parameters ε=1e-6, δ=0.2 over a uniform grid of z from 0 to 1 (≥1000 points). Compute U(z)=Re(W(z)), V(z)=Im(W(z)), and total amplitude sqrt(U²+V²) from the complex function W(z) of the analytical solution.
- Output file: `/app/outputs/shape_nominal.csv`
- Format: csv
- Contract: CSV with columns: z (float), U (float), V (float), amplitude (float). 1000 rows for z in [0,1].
- Scoring: scored by hidden verifier

### Step 2: Maximum amplitude vs δ
- Role: scored
- Action: For each δ in the set {0.1, 0.5, 1, 2, 5, 10, 20, 50, 100}, compute the total amplitude at z=0.5 with ε=1e-6 using the same analytical solution. Record δ and the resulting amplitude.
- Output file: `/app/outputs/max_amplitude_vs_delta.csv`
- Format: csv
- Contract: CSV with columns: delta (float), max_amplitude (float). One row per δ value.
- Scoring: scored by hidden verifier

### Step 3: Maximum amplitude vs ε
- Role: scored
- Action: For each ε in the set {0.1, 1, 5, 10, 20, 50, 100}, compute the total amplitude at z=0.5 with δ=0.2 using the same analytical solution. Record ε and the resulting amplitude.
- Output file: `/app/outputs/max_amplitude_vs_epsilon.csv`
- Format: csv
- Contract: CSV with columns: epsilon (float), max_amplitude (float). One row per ε value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/shape_nominal.csv`
- `/app/outputs/max_amplitude_vs_delta.csv`
- `/app/outputs/max_amplitude_vs_epsilon.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### shape_nominal.csv
- path: `/app/outputs/shape_nominal.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Spatial profiles of U, V, and total amplitude for ε=1e-6, δ=0.2.
- schema:
  - `type`: table
  - `required_columns`: `z`, `U`, `V`, `amplitude`
  - `units`: object

### max_amplitude_vs_delta.csv
- path: `/app/outputs/max_amplitude_vs_delta.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Maximum amplitude at z=0.5 as a function of δ, for ε=1e-6.
- schema:
  - `type`: table
  - `required_columns`: `delta`, `max_amplitude`
  - `units`: object

### max_amplitude_vs_epsilon.csv
- path: `/app/outputs/max_amplitude_vs_epsilon.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Maximum amplitude at z=0.5 as a function of ε, for δ=0.2.
- schema:
  - `type`: table
  - `required_columns`: `epsilon`, `max_amplitude`
  - `units`: object

Notes: All outputs are deterministic numeric values from the exact analytic steady oscillating solution. The checker recomputes the same formulas and compares element-wise with a tight tolerance appropriate for double precision.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "shape_nominal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "U",
          "V",
          "amplitude"
        ],
        "units": {}
      },
      "description": "Spatial profiles of U, V, and total amplitude for ε=1e-6, δ=0.2."
    },
    {
      "file": "max_amplitude_vs_delta.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta",
          "max_amplitude"
        ],
        "units": {}
      },
      "description": "Maximum amplitude at z=0.5 as a function of δ, for ε=1e-6."
    },
    {
      "file": "max_amplitude_vs_epsilon.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "epsilon",
          "max_amplitude"
        ],
        "units": {}
      },
      "description": "Maximum amplitude at z=0.5 as a function of ε, for δ=0.2."
    }
  ],
  "notes": "All outputs are deterministic numeric values from the exact analytic steady oscillating solution. The checker recomputes the same formulas and compares element-wise with a tight tolerance appropriate for double precision."
}
```

## How you are scored
A hidden verifier independently recomputes each scored artifact using the same analytic formulas and compares your numeric values to the correct reference. Scores from each artifact are combined into a single reward that reflects the accuracy of all three outputs. Reporting the paper’s numbers without correct computation will result in low or zero reward.
