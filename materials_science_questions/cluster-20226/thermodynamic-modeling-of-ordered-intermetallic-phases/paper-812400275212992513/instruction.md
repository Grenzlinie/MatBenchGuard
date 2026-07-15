# Compute Coherent Equilibrium in a Simple Two-Phase Model

## Problem background
In coherent phase equilibrium between two solid phases, the elastic energy due to coherency (matching atomic planes across the interface) adds an extra term to the free energy that depends on the volume fractions and compositions of the phases. This invalidates the common tangent construction used for fluid or incoherent phase diagrams. A simple model with two quadratic free energy curves and an elastic term proportional to $A z(1-z)$ illustrates how coherency changes equilibrium: phase compositions become dependent on the overall alloy composition, the two-phase field narrows, and a special point (the Williams point) can terminate two-phase coexistence. Your task is to compute the equilibrium phase compositions, volume fractions, and field boundaries for this model.

## Approach
Consider a binary system that can form two coherent phases $\alpha$ and $\beta$. The dimensionless free energy per mole is

$$
\phi = z(1-x)^2 + (1-z)(1+y)^2 + A \, z(1-z),
$$

where $x$ and $y$ are reduced compositions of $\alpha$ and $\beta$, $z$ is the mole fraction of $\alpha$, and $A$ is a dimensionless coherency parameter (fixed for a given temperature). The mass conservation constraint is

$$
w = z x + (1-z) y,
$$
with $w$ the overall reduced composition. The equilibrium state for a given $(A,w)$ minimizes $\phi$ subject to $0 \le z \le 1$.

You may solve this minimization by any reliable method (e.g., Lagrange multipliers, direct numerical optimization). When the two-phase solution yields the global minimum, it gives the equilibrium compositions $x$, $y$, phase fraction $z$, and reduced free energy $\phi$. By sweeping $A$ and comparing the two-phase free energy with the single-phase free energies ($z=0$ or $z=1$), you can determine the composition range $[w_{\text{lower}}, w_{\text{upper}}]$ over which coherent two-phase coexistence is the equilibrium state.

## Reproduction target
You are to produce two CSV files:

1. **equilibrium_data.csv**: For each $(A,w)$ pair provided in the instruction (a grid of the coherency parameter $A$ and overall composition $w$), compute the equilibrium values of $x$, $y$, $z$, and $\phi$ that minimize the dimensionless free energy subject to the mass conservation constraint. The CSV must have columns `A,w,x,y,z,phi`.

2. **field_boundaries.csv**: For each $A$ value provided, determine the lower and upper composition limits $w_{\text{lower}}$ and $w_{\text{upper}}$ that enclose the two-phase coherent field, i.e., the $w$ interval where the two-phase solution has a lower free energy than both single-phase minima. If no two-phase region exists for a given $A$, indicate this appropriately (e.g., the boundaries collapse to a single value or no coexistence). The CSV must have columns `A,w_lower,w_upper`.

All outputs must be computed from the model and the given inputs; the numbers should not be manually inserted from the literature.

## Inputs

The agent must compute using the following deterministic input points. Create a JSON file `/solution/input_spec.json` with the structure `{"equilibrium_pairs": [[A, w], ...], "field_A_values": [...]}` containing:
- `equilibrium_pairs`: all combinations of A ∈ {0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0} and w ∈ { -2.0, -1.8, -1.6, ..., 2.0 } (i.e., from -2.0 to 2.0 in steps of 0.2). Total 231 pairs.
- `field_A_values`: [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

## Assets

- Python with NumPy and SciPy: numpy scipy

## Workflow steps

### Step 0: Prepare input specification file
- Role: process
- Action: Create the JSON file `/solution/input_spec.json` containing the equilibrium pairs and field A values as specified in the Inputs section. The file must have the structure `{"equilibrium_pairs": [[A,w], ...], "field_A_values": [...]}`.
- Evidence: `/solution/input_spec.json`

### Step 1: Compute equilibrium phase compositions and free energy
- Role: scored (load-bearing)
- Action: Implement the dimensionless free energy model φ = z(1-x)² + (1-z)(1+y)² + A z(1-z) with mass conservation w = z x + (1-z) y. For each provided (A, w) pair, find the equilibrium (x, y, z) that minimizes φ, and compute the corresponding reduced free energy φ. Output the results as a CSV table with columns A, w, x, y, z, phi.
- Output file: `/app/outputs/equilibrium_data.csv`
- Format: csv
- Contract: CSV with header: A (float), w (float), x (float), y (float), z (float), phi (float). Each row corresponds to one (A,w) pair.
- Scoring: scored by hidden verifier

### Step 2: Determine field boundaries of two-phase coexistence
- Role: scored
- Action: For each provided A value, determine the composition interval [w_lower, w_upper] within which the two-phase solution (coexistence of α and β) has lower free energy than any single-phase solution (z=0 or z=1). If no two-phase region exists, indicate this appropriately. Output the boundaries as a CSV with columns A, w_lower, w_upper.
- Output file: `/app/outputs/field_boundaries.csv`
- Format: csv
- Contract: CSV with header: A (float), w_lower (float), w_upper (float). Each row corresponds to one A value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_data.csv`
- `/app/outputs/field_boundaries.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_data.csv
- path: `/app/outputs/equilibrium_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium phase compositions x, y, phase fraction z, and reduced free energy φ for a grid of (A, w) points.
- schema:
  - `header`: A,w,x,y,z,phi
  - `column_types`: `float`, `float`, `float`, `float`, `float`, `float`

### field_boundaries.csv
- path: `/app/outputs/field_boundaries.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Lower and upper composition limits of the two-phase coherent field for a set of A values.
- schema:
  - `header`: A,w_lower,w_upper
  - `column_types`: `float`, `float`, `float`

Notes: Both outputs are scored by numeric recompute with tolerances. The input specification file is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "/app/outputs/equilibrium_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "header": "A,w,x,y,z,phi",
        "column_types": [
          "float",
          "float",
          "float",
          "float",
          "float",
          "float"
        ]
      },
      "description": "Equilibrium phase compositions x, y, phase fraction z, and reduced free energy φ for a grid of (A, w) points."
    },
    {
      "file": "/app/outputs/field_boundaries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "header": "A,w_lower,w_upper",
        "column_types": [
          "float",
          "float",
          "float"
        ]
      },
      "description": "Lower and upper composition limits of the two-phase coherent field for a set of A values."
    }
  ],
  "notes": "Both outputs are scored by numeric recompute with tolerances. The input specification file is not scored."
}
```

## How you are scored
A hidden verifier will independently check each of your two output files. For **equilibrium_data.csv**, the verifier will recompute the expected equilibrium $x$, $y$, $z$, and $\phi$ for each $(A,w)$ pair using the correct analytical solution and compare your submitted values. For **field_boundaries.csv**, it will similarly recompute the true field boundaries for each $A$ and compare your $w_{\text{lower}}$ and $w_{\text{upper}}$. Both stages are scored quantitatively, and the final reward is a weighted combination of the scores from the two artifacts. Reporting numbers alone is not enough; your computed values must match the expected results (within hidden tolerances). The verifier does not read the paper; it knows the correct answers from direct computation.
