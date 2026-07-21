# Critical Universal Ratio Extraction for 2D Random Ising Model Surface Correlation Length

## Problem background
At the critical point of the two-dimensional random Ising model, the surface correlation function is predicted to obey conformal covariance and to satisfy a universal relation between the correlation length along a strip and the width of the system. Verifying this relation for disordered systems requires a controlled numerical study that measures the surface correlation length for different strip widths and dilution strengths, and that analyses the finite‑size approach to the asymptotic limit. The key quantities are the typical correlation length and the average correlation length (obtained from the first moment of the correlation function), together with their dimensionless ratios with respect to the strip size.

## Approach
The measurement is carried out with the star‑triangle (ST) iterative method on a diagonal strip of the square lattice with free boundaries. Random ferromagnetic bonds take two values with equal probability at the self‑dual critical point. Applying an alternating sequence of star‑to‑triangle and triangle‑to‑star transformations iteratively decouples the surface spins from the bulk. Once the surface couplings have converged, the surface spin correlation function reduces to a one‑dimensional product form, from which the inverse correlation length is extracted for each disorder realization. Disorder‑averaging over many realizations yields the typical and the average correlation lengths, and finite‑size scaling analysis is performed by comparing results across odd strip widths L ≤ 21 and several dilution ratios ρ.

## Reproduction target
For strips of odd width L = 5, 7, 9, 11, 13, 15, 17, 19, 21 at dilution ratios ρ = 2 and 4 (optionally also ρ = 1 and 10), run the ST simulation with at least 10⁴ disorder realizations per (L, ρ) pair. Compute the disorder‑averaged typical correlation length ξ_L^typ and the average correlation length ξ_L^(1) (via the inverse‑of‑average prescription). Form the dimensionless ratios (π/2)·ξ_L^typ / l and (π/2)·ξ_L^(1) / l, where l = (L−1)/2. Assemble the results into a single CSV file with columns L, l, rho, xi_typ, xi_avg, ratio_typ, ratio_avg, covering all simulated (L, ρ). The hidden verifier will process this file to examine the L‑dependence of the ratios and to assess whether they converge to a universal value and exhibit distinct finite‑size correction patterns for the typical and the average cases.

## Assets

- Python scientific computing environment: https://www.python.org/

## Workflow steps

### Step 1: Star-triangle simulation and correlation length calculation
- Role: process
- Action: Implement the star-triangle iterative method for the 2D random Ising model on a diagonal strip of odd width L (L = 5, 7, 9, 11, 13, 15, 17, 19, 21) and length K ≥ 1024, with random ferromagnetic bonds (taking values J1, J2 with equal probability) at the self-dual critical point defined by tanh(J1/kBT) = exp(-2J2/kBT). For each (L, dilution ratio ρ = J1/J2 = 2, 4, optionally 1, 10), generate at least 10^4 independent disorder realizations. For each sample, apply successive ST transformations until convergence (approximately L² iterations) to obtain asymptotic surface couplings. Then compute the inverse surface correlation length 1/ξ_L using the product formula over a separation r = K/2 of neighbouring surface spins. Record per-sample ξ_L values so that disorder-averaged statistics can be computed later. Log progress to a file for evidence.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Export correlation length ratios for finite-size scaling
- Role: scored (load-bearing)
- Action: From the collected per-sample ξ_L values, compute the typical correlation length ξ_L^typ = disorder average of ξ_L, and the average correlation length ξ_L^(1) defined via the disorder average of the correlation function moment (using the first moment of the distribution of 1/ξ_L, i.e., the inverse of the average of 1/ξ_L, compatible with the cumulant expansion up to first order). Then compute the dimensionless ratios: ratio_typ = (π/2) * ξ_L^typ / l and ratio_avg = (π/2) * ξ_L^(1) / l, where l = (L-1)/2. Write a CSV file with columns L, l, rho, xi_typ, xi_avg, ratio_typ, ratio_avg for every combination of L and ρ that was simulated.
- Output file: `/app/outputs/step_01_results.csv`
- Format: csv
- Contract: Columns: L (int), l (int), rho (int), xi_typ (float), xi_avg (float), ratio_typ (float), ratio_avg (float). One row per (L,rho).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.csv
- path: `/app/outputs/step_01_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The agent's computed correlation length ratios for finite-size scaling. The checker will extrapolate ratio_typ vs 1/l and ratio_avg vs 1/ln l to assess convergence to a universal value, and will check structural trends (ratio_avg > ratio_typ, distinct correction patterns).
- schema:
  - `type`: table
  - `required_columns`: `L`, `l`, `rho`, `xi_typ`, `xi_avg`, `ratio_typ`, `ratio_avg`
  - `units`:
    - `xi_typ`: lattice units
    - `xi_avg`: lattice units
    - `ratio_typ`: dimensionless
    - `ratio_avg`: dimensionless

Notes: The agent must provide rows for at least L = 5,7,9,11,13,15,17,19,21 and rho = 2,4. Additional values (rho = 1,10) are optional. The checker will internally extrapolate and compare to the known universal value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "l",
          "rho",
          "xi_typ",
          "xi_avg",
          "ratio_typ",
          "ratio_avg"
        ],
        "units": {
          "xi_typ": "lattice units",
          "xi_avg": "lattice units",
          "ratio_typ": "dimensionless",
          "ratio_avg": "dimensionless"
        }
      },
      "description": "The agent's computed correlation length ratios for finite-size scaling. The checker will extrapolate ratio_typ vs 1/l and ratio_avg vs 1/ln l to assess convergence to a universal value, and will check structural trends (ratio_avg > ratio_typ, distinct correction patterns)."
    }
  ],
  "notes": "The agent must provide rows for at least L = 5,7,9,11,13,15,17,19,21 and rho = 2,4. Additional values (rho = 1,10) are optional. The checker will internally extrapolate and compare to the known universal value."
}
```

## How you are scored
A hidden verifier independently reads the submitted `step_01_results.csv`. For each dilution ratio it examines the trend of the typical and average ratios as functions of 1/l (or 1/ln l) and checks for structural relationships (e.g. whether the average ratio lies above the typical one, and whether the finite‑size corrections for the average are stronger than for the typical). The verifier then computes a weighted reward that summarises how well the data reproduce the expected universal behaviour. The reward depends on the number of (L, ρ) combinations supplied and on the agreement of the extrapolated behaviour with the known correct limit. Reporting numbers without actually running the simulation will not produce the required L‑dependence and will receive no credit.
