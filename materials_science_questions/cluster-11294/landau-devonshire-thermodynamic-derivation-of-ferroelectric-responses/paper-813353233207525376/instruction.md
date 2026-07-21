# Mean-Field Transverse Ising Model for Graded Ferroelectric Multilayers

## Problem background
Ferroelectric thin films with graded composition across layers can exhibit enhanced dielectric tunability. We consider a quasi‑2D layered ferroelectric modelled using the Transverse Ising Model (TIM) under the mean‑field approximation. The interlayer coupling is assumed to decay exponentially with the layer–layer distance, controlled by a grading parameter λ. The mean‑field self‑consistent equations yield a layer‑resolved polarization profile, from which macroscopic quantities—mean polarization, dielectric susceptibility, and percentage tunability—are derived as functions of the applied electric field, temperature, number of layers N, and grading strength λ. The central scientific question is whether exponential grading amplifies the tunability response and causes it to saturate at lower applied fields compared to a homogeneous system.

## Approach
We treat a stack of N ferroelectric layers. The interlayer coupling matrix is

K_{nm} = exp(-λ |n-m|),  n,m = 1,…,N,

where λ ≥ 0 is the grading parameter. Under the mean‑field approximation, the layer‑averaged pseudospin ⟨S_n^z⟩ satisfies the self‑consistency equation

⟨S_n^z⟩ = (h_n / |h_n|) tanh( |h_n| / k_B T ),

with the effective local field

h_n = Σ_{m=1}^N K_{nm} ⟨S_m^z⟩ + e^z,

and e^z is the applied longitudinal electric field. The temperature is expressed in reduced units k_B T/K (the reference interaction strength K = 1). These equations are solved by numerical iteration. From the converged layer profile we compute the mean polarization ⟨P^z⟩ = (1/N) Σ_n ⟨S_n^z⟩, the dielectric susceptibility χ as the numerical derivative of ⟨P^z⟩ with respect to e^z, and the relative tunability η = 100 × (χ(0) − χ(e^z)) / χ(0) %.

The target parameter space consists of four configurations:
- (N=5, λ=0)  – homogeneous small stack
- (N=5, λ=0.261) – graded small stack
- (N=50, λ=0) – homogeneous large stack
- (N=50, λ=0.01) – graded large stack

All calculations are performed at a reduced temperature k_B T/K = 1.0, and for applied fields e^z/K from 0.0 to 2.0 in steps of 0.1.

## Reproduction target
Produce a single CSV file that reports, for each of the four (N, λ) configurations at k_B T/K = 1.0 and for every e_z/K from 0.0 to 2.0 (step 0.1), the computed mean polarization (dimensionless), dielectric susceptibility (dimensionless), and percentage tunability (0–100%). From these data, determine whether the tunability is larger for graded systems (λ > 0) than for the corresponding homogeneous cases (λ = 0) at intermediate fields, and whether increasing the system size from N=5 to N=50 elevates the tunability for a given grading strength. The CSV must have the columns: N, lambda, kBT_K, e_z_over_K, mean_polarization, dielectric_susceptibility, tunability_percentage.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Solve self-consistent mean-field TIM for layered system
- Role: process
- Action: Implement the mean‑field model described in Approach. For each required (N, λ) combination and each applied field e_z/K, solve the self‑consistency equations ⟨S_n^z⟩ = (h_n/|h_n|) tanh(|h_n|/k_B T) with h_n = Σ_m K_{nm}⟨S_m^z⟩ + e^z, where K_{nm}=exp(−λ|n−m|), using fixed‑point iteration or root‑finding. Retain the converged layer‑resolved averages for subsequent steps.

### Step 2: Compute and output macroscopic dielectric and tunability responses
- Role: scored (load-bearing)
- Action: From the solved layer‑resolved pseudospin averages, calculate: (1) mean polarization ⟨P^z⟩ as the average over layers, (2) dielectric susceptibility χ from the numerical derivative of ⟨P^z⟩ with respect to e_z (using adjacent field points), and (3) tunability percentage η = (χ(0)−χ(E))/χ(0) × 100. Generate a single CSV file containing the results for parameter sets (N=5, λ=0.0), (N=5, λ=0.261), (N=50, λ=0.0), (N=50, λ=0.01) at reduced temperature kBT/K=1.0 and reduced field e_z/K from 0 to 2 in steps of 0.1.
- Output file: `/app/outputs/step_01_results.csv`
- Format: csv
- Contract: Header: N, lambda, kBT_K, e_z_over_K, mean_polarization, dielectric_susceptibility, tunability_percentage. Each row corresponds to one (N, lambda, e_z_over_K) combination at fixed kBT_K=1.0. All fields numeric.
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
- target_policy: trend_verification
- description: Macroscopic dielectric and tunability responses for four (N, λ) configurations at kBT/K=1.0, covering e_z/K from 0.0 to 2.0 in steps of 0.1. The hidden checker verifies that the output has the expected shape (columns, row count, parameter grid), that the reported tunability is internally consistent with the susceptibility values, that tunability is non‑decreasing with applied field and enhanced by grading and larger N, and that all values lie within physically plausible ranges.
- schema:
  - `type`: table
  - `required_columns`: `N`, `lambda`, `kBT_K`, `e_z_over_K`, `mean_polarization`, `dielectric_susceptibility`, `tunability_percentage`
  - `units`:
    - `mean_polarization`: dimensionless (reduced polarization)
    - `dielectric_susceptibility`: dimensionless
    - `tunability_percentage`: percent (0-100)

Notes: The file must contain exactly the expected parameter grid; no extra rows. All numeric columns must be finite and within physically plausible ranges. The hidden checker uses internal consistency checks and trend tests; higher tunability is better.

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
      "target_policy": "trend_verification",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "lambda",
          "kBT_K",
          "e_z_over_K",
          "mean_polarization",
          "dielectric_susceptibility",
          "tunability_percentage"
        ],
        "units": {
          "mean_polarization": "dimensionless (reduced polarization)",
          "dielectric_susceptibility": "dimensionless",
          "tunability_percentage": "percent (0-100)"
        }
      },
      "description": "Macroscopic dielectric and tunability responses for four (N, λ) configurations at kBT/K=1.0, covering e_z/K from 0.0 to 2.0 in steps of 0.1. The hidden checker verifies shape, internal consistency, trends, and plausibility."
    }
  ],
  "notes": "The file must contain exactly the expected parameter grid; no extra rows. All numeric columns must be finite and within physically plausible ranges. The hidden checker uses internal consistency checks and trend tests; higher tunability is better."
}
```

## How you are scored
A hidden verifier reads your output CSV and checks:
- **File shape**: required columns, exact row count (84), and completeness of the required (N, λ, e_z_over_K) parameter grid.
- **Tunability internal consistency**: for each (N, λ) configuration, the reported tunability must satisfy η = 100 × (χ(0) − χ(e_z)) / χ(0) within a small tolerance.
- **Monotonicity and enhancement**: tunability must be non‑decreasing with e_z for every configuration; at e_z/K = 1, graded systems must show higher tunability than the corresponding ungraded systems; and for λ = 0.01, the larger system (N=50) must exhibit higher tunability than the smaller one (N=5).
- **Plausibility**: mean_polarization ∈ [0, 1], dielectric_susceptibility ≥ 0, tunability_percentage ∈ [0, 100].

The verifier does not compare your numbers against any stored reference data; it solely evaluates the structural and trend properties listed above.