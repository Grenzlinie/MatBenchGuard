# Twist-Averaged Boundary Condition Convergence Benchmark in 2D Hubbard Model

## Problem background
The two-dimensional Hubbard model is a fundamental model of correlated electron systems. Twist-averaged boundary conditions (TABC) reduce finite-size effects in lattice calculations by averaging ground-state energies over a set of boundary-condition twist angles. The choice of twist angle sequence affects the convergence rate with respect to the number of twists Nθ. Low-discrepancy quasirandom sequences (e.g., Halton) have been proposed to combine fast convergence with the ability to incrementally add twists while avoiding degeneracies that plague uniform grids. This task benchmarks the convergence behavior of three twist-sampling methods: Halton quasirandom (QR), pseudorandom (PR), and a uniform grid, on small Hubbard model clusters.

## Approach
You will implement exact diagonalization (ED) for a 4×4 square-lattice Hubbard model. For the noninteracting case (U=0, half-filling) and interacting case (U=8, two spin-up and two spin-down electrons), you will compute the ground-state energy for each twist angle in a set of QR, PR, and grid sequences covering [0,2π) in both directions. From these energies, you will calculate: (1) the TABC-averaged energy for various Nθ and the absolute relative error with respect to the thermodynamic-limit value -16/π² for the noninteracting case; (2) error bars (standard deviation of block averages) as a function of Nθ for the interacting case, using a pre-generated set of 3600 twists per method. Finally, you will perform a linear regression of log10(errorbar) vs log10(Nθ) to obtain power-law convergence exponents (slopes) for each method.

## Reproduction target
Your task is to produce the following three scored output files:

- `fig1_convergence_data.csv`: method, N_theta, relative_error for the noninteracting convergence.
- `fig2a_errorbar_data.csv`: method, N_theta, errorbar for the interacting convergence.
- `fitted_slopes.json`: a JSON object with keys 'QR', 'PR', 'grid' and values being the fitted slopes from the interacting data.

The data must be computed by following the workflow steps; the numerical values will be independently verified.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Generate twist angle sets
- Role: process
- Action: Generate Halton quasirandom (QR), pseudorandom (PR) with a fixed seed, and uniform grid (θ_ij = (2π i/N_θx, 2π j/N_θy)) twist angle sequences covering [0,2π)×[0,2π) for a range of N_θ up to 3600. Store the three sets for later use.
- Evidence: `/app/outputs/twist_log.txt`

### Step 2: Noninteracting convergence data (U=0)
- Role: scored
- Action: Set up the noninteracting Hubbard Hamiltonian on a 4×4 lattice with twist phases. For each method (QR, PR, grid) and for a range of N_θ values (e.g., every 10 or 100 angles from 1 to 3600), compute the TABC average ground-state energy as the mean over the first N_θ twists. Compute the absolute relative error with respect to the exact infinite‑lattice value -16/π². Write the pairs (N_θ, relative_error) to a CSV file.
- Output file: `/app/outputs/fig1_convergence_data.csv`
- Format: csv
- Contract: method (string: QR, PR, grid), N_theta (int), relative_error (float, non‑negative)
- Scoring: scored by hidden verifier

### Step 3: Interacting convergence data (U=8, n=0.25)
- Role: scored (load-bearing)
- Action: Construct the full many‑body Hamiltonian for the 4×4 Hubbard model with U=8 and two spin‑up, two spin‑down electrons. For each twist angle in the pre‑generated QR, PR, and grid sets (up to 3600 twists), perform exact diagonalization to obtain the ground‑state energy. For each method, partition the 3600 twists into blocks of size N_θ, compute the standard deviation of the block‑average energies, and output method, N_theta, errorbar to a CSV file.
- Output file: `/app/outputs/fig2a_errorbar_data.csv`
- Format: csv
- Contract: method (string: QR, PR, grid), N_theta (int), errorbar (float, >0)
- Scoring: scored by hidden verifier

### Step 4: Fit convergence slopes
- Role: scored
- Action: Read fig2a_errorbar_data.csv and, for each method, perform a linear fit of log10(errorbar) vs log10(N_theta). Write the fitted slopes (without uncertainties) as a JSON object with keys QR, PR, grid.
- Output file: `/app/outputs/fitted_slopes.json`
- Format: json
- Contract: {"QR": float, "PR": float, "grid": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fig1_convergence_data.csv`
- `/app/outputs/fig2a_errorbar_data.csv`
- `/app/outputs/fitted_slopes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fig1_convergence_data.csv
- path: `/app/outputs/fig1_convergence_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw noninteracting convergence data; the checker recomputes slopes from this file.
- schema:
  - `type`: table
  - `required_columns`: `method`, `N_theta`, `relative_error`

### fig2a_errorbar_data.csv
- path: `/app/outputs/fig2a_errorbar_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw interacting error‑bar data; the checker recomputes convergence slopes from this file.
- schema:
  - `type`: table
  - `required_columns`: `method`, `N_theta`, `errorbar`

### fitted_slopes.json
- path: `/app/outputs/fitted_slopes.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent‑reported slope values; the checker cross‑validates them against slopes recomputed from the raw data.
- schema:
  - `type`: object
  - `required`:
    - `QR`: number
    - `PR`: number
    - `grid`: number

Notes: The checker recomputes the convergence slopes (log‑log fit) from the raw data CSVs and compares them against the paper‑reported gold with tolerances. The fitted_slopes.json is checked for self‑consistency (should match the recomputed slopes within a tight margin).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fig1_convergence_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "N_theta",
          "relative_error"
        ]
      },
      "description": "Raw noninteracting convergence data; the checker recomputes slopes from this file."
    },
    {
      "file": "fig2a_errorbar_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "N_theta",
          "errorbar"
        ]
      },
      "description": "Raw interacting error‑bar data; the checker recomputes convergence slopes from this file."
    },
    {
      "file": "fitted_slopes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "QR": "number",
          "PR": "number",
          "grid": "number"
        }
      },
      "description": "Agent‑reported slope values; the checker cross‑validates them against slopes recomputed from the raw data."
    }
  ],
  "notes": "The checker recomputes the convergence slopes (log‑log fit) from the raw data CSVs and compares them against the paper‑reported gold with tolerances. The fitted_slopes.json is checked for self‑consistency (should match the recomputed slopes within a tight margin)."
}
```

## How you are scored
A hidden verifier will read your output files and score them. For the noninteracting convergence data, the verifier will recompute an effective convergence rate and verify that the relative error decreases with increasing Nθ in a manner consistent with the expected asymptotic behavior. For the interacting error-bar data, the verifier will recompute the power-law slopes via a log-log linear fit and compare them against a hidden reference (the slopes must fall within a tolerance region that accounts for implementation variance). The reported slopes in `fitted_slopes.json` must be self-consistent with the recomputed values. The final reward is a weighted sum over all scored stages, with the interacting convergence data carrying the highest weight. Simply providing numbers without genuine computation will not meet the required accuracy.
