# Dynamic Stress Intensity Factor in a Cracked Piezoelectric Strip under Impact

## Problem background
Piezoelectric ceramics are widely used as sensors and actuators because they couple mechanical and electrical fields. A central crack in such a material under impact loading creates a transient stress singularity at the crack tip, quantified by the dynamic stress intensity factor (SIF) K_I(t). The SIF governs crack propagation and structural integrity. The problem considered here is a plane-strain piezoelectric strip of width 2h containing a central crack of length 2c, loaded by a sudden normal step stress on the crack faces. The goal is to determine the time‑varying normalized SIF, K_I(t)/(σ₀√(πc)), as a function of material properties and the geometry ratio h/c, and to extract the peak SIF and its static limit.

## Approach
The analysis proceeds in the Laplace‑transform domain to convert the time‑dependent field equations into an equivalent static problem. Fourier transforms are applied along the crack direction, reducing the coupled electro‑elasticity equations to a system of ordinary differential equations. After satisfying the far‑field and symmetry conditions, the mixed boundary conditions on the crack plane yield a singular integral equation for the crack‑face displacement derivative. This integral equation contains semi‑infinite kernel integrals that depend on the material constants and the strip geometry. The equation is discretized using the Gauss‑Jacobi quadrature formula, together with a supplementary zero‑mean condition, producing a linear system for the unknown discretized crack‑face function. Extrapolation gives the crack‑tip value needed for the SIF. The Laplace‑domain SIF is then obtained, and the time‑domain SIF is recovered by the Papoulis numerical inverse Laplace transform. The entire procedure must be repeated for each combination of piezoelectric material (PZT‑4, PZT‑5H, P‑7, PZT‑6B) and geometry ratio h/c (∞, 3.0, 2.0, 1.7, 1.5). The material constants are fully specified in a reference table.

## Reproduction target
Implement the analytical‑numerical pipeline described above and compute the normalized dynamic stress intensity factor K_I(t)/(σ₀√(πc)) for every combination of the four piezoelectric materials (PZT‑4, PZT‑5H, P‑7, PZT‑6B) and five h/c ratios (inf, 3.0, 2.0, 1.7, 1.5). Write the time‑history results for a set of normalized times c₂t/c into the CSV file `sif_results.csv`. Additionally, extract the peak SIF (and its occurrence time) and the static‑limit SIF; include these as special rows with time_normalized set to -1 and -2 respectively. The CSV must contain columns: material, h_c_ratio, time_normalized, sif_normalized.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Load material constants and compute auxiliary functions
- Role: process
- Action: Load the piezoelectric material constants (elastic, piezoelectric, dielectric) for PZT-4, PZT-5H, P-7, PZT-6B from the published values (Table 1 of the paper). Implement functions to compute, for any given Laplace parameter p and wavenumber s, the characteristic parameters γ_j, γ'_j, a_j, a'_j, b_j, b'_j by solving the cubic characteristic equations, and derived quantities such as Q₀(s), Q₀^∞, C₃₃, and kernel ingredients needed for the singular integral equation.
- Evidence: none

### Step 2: Form and solve the singular integral equation in Laplace domain
- Role: process
- Action: For each material and h/c ratio (∞, 3.0, 2.0, 1.7, 1.5), choose a sufficient set of Laplace parameter p values. For each p, compute the semi-infinite integral kernels M₁ and M₂ numerically. Discretize the singular integral equation using Gauss-Jacobi quadrature, incorporate the supplementary zero-mean constraint, assemble and solve the (N+1)×(N+1) linear system to obtain the crack-face derivative values Ψ(u_m,κ). Extrapolate from the innermost nodes to get the crack-tip value Ψ(1,κ).
- Evidence: `/app/outputs/psi_values.csv`

### Step 3: Perform numerical Laplace inversion to obtain time-domain SIF
- Role: process
- Action: For each case, compute the Laplace-domain stress intensity factor K_I*(p) from Ψ(1,κ) and Q₀^∞. Apply the Papoulis numerical inverse Laplace transform to K_I*(p) to recover the time-domain dynamic stress intensity factor K_I(t) over a range of normalized times c₂t/c. Also evaluate the static limit K_I^∞ by taking p→0.
- Evidence: `/app/outputs/time_sif.csv`

### Step 4: Compile final normalized SIF results
- Role: scored (load-bearing)
- Action: For each material and h/c ratio, compute the normalized stress intensity factor K_I(t)/(σ₀√(πc)) at a set of discrete normalized times c₂t/c. Determine the maximum value K_I^Max and its time t^Max, and the static value K_I^∞. Write all data points into sif_results.csv with columns material, h_c_ratio, time_normalized, sif_normalized. Use time_normalized=-1 for the peak and -2 for the static limit.
- Output file: `/app/outputs/sif_results.csv`
- Format: csv
- Contract: CSV with columns: material (string: PZT-4, PZT-5H, P-7, PZT-6B), h_c_ratio (string: inf, 3.0, 2.0, 1.7, 1.5), time_normalized (float: c₂t/c for ordinary points; -1 for peak; -2 for static limit), sif_normalized (float: K_I/(σ₀√(πc))).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sif_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sif_results.csv
- path: `/app/outputs/sif_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized dynamic stress intensity factor values computed by the numerical pipeline. The hidden checker compares these values to the paper's reported reference using tolerances.
- schema:
  - `type`: table
  - `required_columns`: `material`, `h_c_ratio`, `time_normalized`, `sif_normalized`
  - `columns`:
    - `material`: string, one of PZT-4, PZT-5H, P-7, PZT-6B
    - `h_c_ratio`: string, one of inf, 3.0, 2.0, 1.7, 1.5
    - `time_normalized`: float, normalized time c₂t/c; -1 for peak value; -2 for static limit
    - `sif_normalized`: float, normalized SIF K_I/(σ₀√(πc))
  - `units`: object

Notes: The agent must implement the full numerical pipeline: characteristic cubics, semi-infinite integrals, Gauss-Jacobi quadrature, linear system solving, Papoulis inversion. The material constants are public (Table 1). The checker uses the paper's reported values (Table 2 and figures) as hidden gold and compares the agent's reported sif_normalized values with an appropriate tolerance (reference_match).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sif_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "h_c_ratio",
          "time_normalized",
          "sif_normalized"
        ],
        "columns": {
          "material": "string, one of PZT-4, PZT-5H, P-7, PZT-6B",
          "h_c_ratio": "string, one of inf, 3.0, 2.0, 1.7, 1.5",
          "time_normalized": "float, normalized time c₂t/c; -1 for peak value; -2 for static limit",
          "sif_normalized": "float, normalized SIF K_I/(σ₀√(πc))"
        },
        "units": {}
      },
      "description": "Normalized dynamic stress intensity factor values computed by the numerical pipeline. The hidden checker compares these values to the paper's reported reference using tolerances."
    }
  ],
  "notes": "The agent must implement the full numerical pipeline: characteristic cubics, semi-infinite integrals, Gauss-Jacobi quadrature, linear system solving, Papoulis inversion. The material constants are public (Table 1). The checker uses the paper's reported values (Table 2 and figures) as hidden gold and compares the agent's reported sif_normalized values with an appropriate tolerance (reference_match)."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier. The verifier reads `/app/outputs/sif_results.csv` and extracts the reported `sif_normalized` values for a set of hidden conditions (material, h_c_ratio, time_normalized). For each condition, it compares your value against a reference value using a tolerance. If your reported SIF is within tolerance, you earn full credit for that condition; if it is farther away, the credit decays linearly. The final reward is the weighted average across all checked conditions. Meeting or exceeding the reference is always treated as full credit – a slightly better agreement than the reference does not penalize you. Only the contents of `sif_results.csv` are scored; intermediate artifacts are not evaluated.
