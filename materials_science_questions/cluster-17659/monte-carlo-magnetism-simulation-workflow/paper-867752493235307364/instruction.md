# Phase Diagrams and Magnetization Jumps for the p-Spin Model with Inhomogeneous Transverse Field

## Problem background
Quantum annealing (QA) is a metaheuristic for combinatorial optimization that uses quantum fluctuations to explore the energy landscape of an Ising problem. In the adiabatic limit, the annealing time is controlled by the minimum energy gap along the evolution path, which tends to close exponentially at first-order quantum phase transitions. The ferromagnetic p-spin model (p ≥ 3) is a classic mean-field benchmark that exhibits such a transition under a conventional uniform transverse field. This work investigates whether a spatiotemporal inhomogeneous transverse field — applied as a zipper-like schedule that turns off the field site by site — can avoid or weaken the first-order transition, and how non-ideal conditions (finite temperature, incomplete turn-off) affect the outcome. The target quantities are the magnetization phase diagrams and the magnitude of the magnetization jump at first-order transitions.

## Approach
The system is treated in the thermodynamic limit using the Suzuki-Trotter decomposition combined with the static approximation. This leads to a mean-field free-energy functional and a self-consistent equation for the scalar magnetization m. The transverse field profile Γ(x) is taken as a step function: Γ(x) = 1 for 0 ≤ x ≤ 1−τ and Γ(x) = 0 for 1−τ < x ≤ 1, where τ ∈ [0,1] controls the fraction of spins with zero field. For the quantum model at inverse temperature β, the free energy per spin and the self-consistent equation are:

  f(m) = s(p−1)m^p − (1/β)∫_0^1 ln[2 cosh(β √((s p m^{p−1})^2 + Γ(x)^2))] dx,
  m = ∫_0^1 [s p m^{p−1} / √((s p m^{p−1})^2 + Γ(x)^2)] tanh(β √((s p m^{p−1})^2 + Γ(x)^2)) dx.

In the zero-temperature limit (β → ∞) these reduce to:

  f(m) = s(p−1)m^p − ∫_0^1 √((s p m^{p−1})^2 + Γ(x)^2) dx,
  m = ∫_0^1 s p m^{p−1} / √((s p m^{p−1})^2 + Γ(x)^2) dx.

For the spin-vector Monte Carlo (SVMC) model, the free energy becomes

  f(m) = s(p−1)m^p − (1/β)∫_0^1 ln[2π I_0(β √((s p m^{p−1})^2 + Γ(x)^2))] dx,

where I_0 is the modified Bessel function. For classical simulated annealing with inhomogeneous temperature, a fraction τ of spins is at a finite inverse temperature β_0 while the remaining spins have β_i = 0 (infinite temperature). The free energy per spin reduces to

  f(m) = (p−1)m^p − τ ln(2 cosh(β_0 p m^{p−1})) + const.

For each model, m is determined by minimizing the free energy or solving the extremization condition at each point in the (s,τ) plane.

## Reproduction target
Implement the above models for p = 3 and produce the following outputs:

1. For the zero-temperature quantum model: compute m on a grid s ∈ [0,1] (step 0.01) and τ ∈ [0,1] (step 0.01) and save to 'idealized_magnetization.csv'.
2. For the finite-temperature quantum model at β = 100 (T = 0.01): compute m on the same grid and save to 'finiteT_magnetization.csv'.
3. From the finite-temperature m(s,τ) data, locate first-order transition points (discontinuities in m vs s) for each τ. For every τ where a discontinuity is found, compute the jump Δm (the difference between the two stable m values) and save as (τ, Δm) pairs in 'jump_magnetization.csv'.
4. For the SVMC model at β = 100 (T = 0.01), compute m on the same grid and save to 'SVMC_magnetization.csv'.
5. For the classical simulated annealing model with β_0 = 2 (no random field), compute m on the same grid and save to 'SA_magnetization.csv'.

All CSV files must follow the column schemas described in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Ideal zero‑temperature quantum model magnetization
- Role: scored
- Action: Solve the zero‑temperature self‑consistent magnetization equation of the quantum model for the step‑function inhomogeneous transverse field, with p=3. Compute magnetization m on a grid s ∈ [0,1] (step 0.01), τ ∈ [0,1] (step 0.01). Save the (s, τ, m) triplets to a CSV file.
- Output file: `/app/outputs/idealized_magnetization.csv`
- Format: csv
- Contract: CSV with columns: s (float, dimensionless annealing parameter), tau (float, fraction of spins with zero transverse field), m (float, magnetization order parameter).
- Scoring: scored by hidden verifier

### Step 2: Finite‑temperature quantum model magnetization
- Role: scored
- Action: Solve the finite‑temperature self‑consistent magnetization equation of the quantum model for the same step‑function field, p=3, at T=0.01 (β=100). Compute m on the same (s,τ) grid and save to CSV.
- Output file: `/app/outputs/finiteT_magnetization.csv`
- Format: csv
- Contract: CSV with columns: s (float), tau (float), m (float).
- Scoring: scored by hidden verifier

### Step 3: Magnetization jump at first‑order transitions
- Role: scored (load-bearing)
- Action: From the finite‑temperature model solved in step_02, locate first‑order transition points by scanning for discontinuities in m(s) for each τ. For each τ where a first‑order transition exists, compute the jump Δm (difference between the two stable m values). Output a CSV of (τ, Δm) pairs.
- Output file: `/app/outputs/jump_magnetization.csv`
- Format: csv
- Contract: CSV with columns: tau (float), delta_m (float).
- Scoring: scored by hidden verifier

### Step 4: Spin‑vector Monte Carlo model magnetization
- Role: scored
- Action: Solve the SVMC free‑energy equation with the same step‑function field, p=3, T=0.01 (β=100). Compute m on the same (s,τ) grid and save to CSV.
- Output file: `/app/outputs/SVMC_magnetization.csv`
- Format: csv
- Contract: CSV with columns: s (float), tau (float), m (float).
- Scoring: scored by hidden verifier

### Step 5: Classical simulated annealing with inhomogeneous temperature magnetization
- Role: scored
- Action: Solve the classical SA free‑energy equation with site‑dependent inverse temperature following the step protocol: β_i = 0 for a fraction 1‑τ of spins and β_i = β0 for the remaining fraction, with β0=2 and no random field; p=3. Compute m on the same (s,τ) grid and save to CSV.
- Output file: `/app/outputs/SA_magnetization.csv`
- Format: csv
- Contract: CSV with columns: s (float), tau (float), m (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/idealized_magnetization.csv`
- `/app/outputs/finiteT_magnetization.csv`
- `/app/outputs/jump_magnetization.csv`
- `/app/outputs/SVMC_magnetization.csv`
- `/app/outputs/SA_magnetization.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### idealized_magnetization.csv
- path: `/app/outputs/idealized_magnetization.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ideal zero‑temperature quantum model magnetization grid.
- schema:
  - `type`: table
  - `required_columns`: `s`, `tau`, `m`
  - `units`:
    - `s`: dimensionless
    - `tau`: dimensionless
    - `m`: dimensionless

### finiteT_magnetization.csv
- path: `/app/outputs/finiteT_magnetization.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Finite‑temperature quantum model magnetization grid at T=0.01.
- schema:
  - `type`: table
  - `required_columns`: `s`, `tau`, `m`
  - `units`:
    - `s`: dimensionless
    - `tau`: dimensionless
    - `m`: dimensionless

### jump_magnetization.csv
- path: `/app/outputs/jump_magnetization.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetization jump Δm at first‑order transitions for the finite‑temperature quantum model.
- schema:
  - `type`: table
  - `required_columns`: `tau`, `delta_m`
  - `units`:
    - `tau`: dimensionless
    - `delta_m`: dimensionless

### SVMC_magnetization.csv
- path: `/app/outputs/SVMC_magnetization.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spin‑vector Monte Carlo model magnetization grid at T=0.01.
- schema:
  - `type`: table
  - `required_columns`: `s`, `tau`, `m`
  - `units`:
    - `s`: dimensionless
    - `tau`: dimensionless
    - `m`: dimensionless

### SA_magnetization.csv
- path: `/app/outputs/SA_magnetization.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Classical simulated‑annealing magnetization grid with β0=2.
- schema:
  - `type`: table
  - `required_columns`: `s`, `tau`, `m`
  - `units`:
    - `s`: dimensionless
    - `tau`: dimensionless
    - `m`: dimensionless

Notes: The checker implements the same self‑consistent equations to generate a hidden reference for each CSV, then compares the agent’s magnetization values pointwise with a tolerance of 1e-3 (for m) and computes the fraction of correct points. For the jump file, the checker computes its own Δm at the same τ values and compares the differences. The final score is a weighted average of these accuracies, with higher weight on the idealized and finite‑T quantum cases.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "idealized_magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "s",
          "tau",
          "m"
        ],
        "units": {
          "s": "dimensionless",
          "tau": "dimensionless",
          "m": "dimensionless"
        }
      },
      "description": "Ideal zero‑temperature quantum model magnetization grid."
    },
    {
      "file": "finiteT_magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "s",
          "tau",
          "m"
        ],
        "units": {
          "s": "dimensionless",
          "tau": "dimensionless",
          "m": "dimensionless"
        }
      },
      "description": "Finite‑temperature quantum model magnetization grid at T=0.01."
    },
    {
      "file": "jump_magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "delta_m"
        ],
        "units": {
          "tau": "dimensionless",
          "delta_m": "dimensionless"
        }
      },
      "description": "Magnetization jump Δm at first‑order transitions for the finite‑temperature quantum model."
    },
    {
      "file": "SVMC_magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "s",
          "tau",
          "m"
        ],
        "units": {
          "s": "dimensionless",
          "tau": "dimensionless",
          "m": "dimensionless"
        }
      },
      "description": "Spin‑vector Monte Carlo model magnetization grid at T=0.01."
    },
    {
      "file": "SA_magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "s",
          "tau",
          "m"
        ],
        "units": {
          "s": "dimensionless",
          "tau": "dimensionless",
          "m": "dimensionless"
        }
      },
      "description": "Classical simulated‑annealing magnetization grid with β0=2."
    }
  ],
  "notes": "The checker implements the same self‑consistent equations to generate a hidden reference for each CSV, then compares the agent’s magnetization values pointwise with a tolerance of 1e-3 (for m) and computes the fraction of correct points. For the jump file, the checker computes its own Δm at the same τ values and compares the differences. The final score is a weighted average of these accuracies, with higher weight on the idealized and finite‑T quantum cases."
}
```

## How you are scored
A hidden verifier independently implements the same mean-field equations to generate reference magnetization values for each grid point. For each CSV file, the verifier compares your m values to the reference values pointwise. A grid point is considered correct if the absolute difference between your m and the reference m is within a hidden tolerance. The score for each file is the fraction of correctly reproduced grid points. For the jump file, the verifier computes Δm from its own reference and compares the values at matching τ. The overall reward is a weighted average of the individual file scores, with higher weight assigned to the idealized and finite-temperature quantum magnetization files. Reporting a single aggregated number without the full grid data is insufficient to earn a high score, because the verifier needs the raw m(s,τ) results to perform the pointwise comparison.
