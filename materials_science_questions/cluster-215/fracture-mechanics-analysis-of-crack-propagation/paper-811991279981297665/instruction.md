# Spring-back ratio and critical loading factor in V-die bending

## Problem background
In V-die bending, sheet metal is formed by a punch and die. After unloading, elastic recovery causes spring-back — the bent part changes shape, reducing geometric accuracy. A common method to reduce spring-back is to apply a coining force during the bottoming stage, counteracting the elastic unloading. An analytical model was developed that relates the residual spring-back to material and process parameters, quantifying the effect of the coining force. The model defines a dimensionless spring-back ratio SR that measures the remaining spring-back; when SR reaches zero, spring-back is eliminated. A critical loading factor α_c is the coining force (relative to material strength) needed to achieve complete elimination. Additionally, a geometric lower limit exists for the thickness‑to‑punch‑radius ratio t/2ρ, derived from the requirement that the coining contact length remain positive. This task reproduces the analytic expressions and computes SR, α_c, and the lower limit for a range of process and material parameters.

## Approach
The model considers a V‑die bending process under plane‑strain conditions. During bottoming, the pure‑bending moment in the region under the punch nose is neutralized by moments from normal and shear components of the coining force. Using elementary bending theory for the elastic unloading and Hill's anisotropic plasticity (with normal anisotropy R and power‑law hardening exponent n), one obtains closed‑form expressions for the spring‑back ratio SR, the critical loading factor α_c, and the lower geometric limit.

Spring‑back ratio SR (a dimensionless measure):
`SR = (t/(2ρ))^(-2) * { (1/(1+n)) * [ ((1+R)/√(1+2R)) * (t/(2ρ)) ]^(1+n) - α (n/e)^n [ (w/t)*(1/cosθ) - ( (t/(2ρ))^(-1) + 1 ) tanθ ] * [ tanθ * (t/(2ρ)) + (tanθ+2μ) * (1 - cosθ + μ sinθ (t/(2ρ))) / (cosθ + μ sinθ) ] }`
where:
- ρ = punch radius + t/2 (punch nose radius plus half sheet thickness)
- α = loading factor (coining force normalized by material tensile strength and contact length)
- w/t = die‑width‑to‑thickness ratio
- t/2ρ = thickness‑to‑diameter ratio (geometric parameter)
- μ = Coulomb friction coefficient
- θ = half bent angle (in the die)
- e = Euler's number (base of natural logarithm).

Critical loading factor α_c is the value of α that makes SR = 0:
`α_c = [ ((1+R)/√(1+2R)) * (t/(2ρ)) ]^(1+n) / (1+n) * (n/e)^(-n) * [ (w/t)/cosθ - ( (t/(2ρ))^(-1) + 1 ) tanθ ]^(-1) * [ (tanθ+2μ)*(1 - cosθ + μ sinθ (t/(2ρ))) / (cosθ + μ sinθ) + tanθ * (t/(2ρ)) ]^(-1)`.

Lower limit of t/2ρ: from the condition that the contact length l₀ > 0, one obtains
`t/(2ρ) > sinθ / (w/t - sinθ)`.
The minimum allowed t/2ρ (the lower limit) is the right‑hand side; it depends on w/t and θ.

These formulas are implemented in Python and evaluated over prescribed parameter grids to generate the three scored CSV artifacts.

## Reproduction target
Compute the following quantities and write them as CSV files:

1. **sr_data.csv** — Spring‑back ratio SR as a function of loading factor α for all parameter combinations. Parameter grids:
   - w/t in [8, 14] step 2
   - t/2ρ in [0.05, 0.15] step 0.025
   - n in [0.1, 0.5] step 0.1
   - μ in [0.0, 0.2] step 0.1
   - R in [0.5, 2.0] step 0.5
   - θ in [30°, 60°] step 10°
   - α from 0 to 0.2 step 0.01.

2. **alpha_c_data.csv** — Critical loading factor α_c for each parameter combination (without α). Grids:
   - R in [0.5, 2.0] step 0.5
   - n in [0.1, 0.5] step 0.1
   - w/t in [8, 14] step 2
   - t/2ρ in [0.05, 0.15] step 0.025
   - μ in [0.0, 0.2] step 0.1
   - θ in [30°, 60°] step 10°.

3. **lower_limit_data.csv** — Lower limit of t/2ρ for given w/t and θ. Grids:
   - w/t in [8, 14] step 1
   - θ in [30°, 60°] step 5°.

The columns and units for each file are specified in the workflow steps and output contract. All outputs must be placed under /app/outputs.

## Assets

- Python with NumPy: python3, numpy

## Workflow steps

### Step 1: Implement analytic functions
- Role: process
- Action: Translate the closed-form expressions for spring‑back ratio SR, critical loading factor α_c, and the lower‑limit inequality (as derived in the paper) into Python functions. These will be used in the subsequent computation steps.
- Evidence: none

### Step 2: Compute spring‑back ratio SR vs loading factor α
- Role: scored (load-bearing)
- Action: For each combination of fixed parameters (w/t, t/2ρ, n, μ, R, θ) and for loading factor α from 0 to 0.2 in steps of 0.01, evaluate the SR function. Write the results to sr_data.csv.
- Output file: `/app/outputs/sr_data.csv`
- Format: csv
- Contract: columns: alpha (numeric), w_t (numeric), t_2rho (numeric), n (numeric), mu (numeric), R (numeric), theta (numeric), SR (numeric). The parameter grids are: w/t in [8, 14] step 2, t/2ρ in [0.05, 0.15] step 0.025, n in [0.1, 0.5] step 0.1, μ in [0.0, 0.2] step 0.1, R in [0.5, 2.0] step 0.5, θ in [30°, 60°] step 10°. Alpha ranges from 0 to 0.2 with step 0.01.
- Scoring: scored by hidden verifier

### Step 3: Compute critical loading factor α_c
- Role: scored (load-bearing)
- Action: For each combination of parameters (R, n, w/t, t/2ρ, μ, θ) from the specified grids, evaluate the α_c function that satisfies SR=0. Write the results to alpha_c_data.csv.
- Output file: `/app/outputs/alpha_c_data.csv`
- Format: csv
- Contract: columns: R (numeric), n (numeric), w_t (numeric), t_2rho (numeric), mu (numeric), theta (numeric), alpha_c (numeric). Parameter ranges: R in [0.5, 2.0] step 0.5, n in [0.1, 0.5] step 0.1, w/t in [8, 14] step 2, t/2ρ in [0.05, 0.15] step 0.025, μ in [0.0, 0.2] step 0.1, θ in [30°, 60°] step 10°.
- Scoring: scored by hidden verifier

### Step 4: Compute lower limit of t/2ρ
- Role: scored (load-bearing)
- Action: For each combination of w/t and θ, compute the minimum allowed t/2ρ from the inequality l0/t > 0. Write the results to lower_limit_data.csv.
- Output file: `/app/outputs/lower_limit_data.csv`
- Format: csv
- Contract: columns: w_t (numeric), theta (numeric), lower_limit (numeric). w/t in [8, 14] step 1, θ in [30°, 60°] step 5°.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sr_data.csv`
- `/app/outputs/alpha_c_data.csv`
- `/app/outputs/lower_limit_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sr_data.csv
- path: `/app/outputs/sr_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Spring‑back ratio SR as a function of loading factor α and other process/material parameters. The hidden checker will recompute the SR values using the same analytic formulas and parameter grids, comparing each cell within a relative tolerance (e.g., 1e-4).
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `w_t`, `t_2rho`, `n`, `mu`, `R`, `theta`, `SR`
  - `units`:
    - `alpha`: dimensionless
    - `w_t`: dimensionless
    - `t_2rho`: dimensionless
    - `n`: dimensionless
    - `mu`: dimensionless
    - `R`: dimensionless
    - `theta`: degrees
    - `SR`: dimensionless

### alpha_c_data.csv
- path: `/app/outputs/alpha_c_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Critical loading factor α_c for spring‑back elimination. The hidden checker will recompute α_c from the equation SR=0 and verify numeric agreement.
- schema:
  - `type`: table
  - `required_columns`: `R`, `n`, `w_t`, `t_2rho`, `mu`, `theta`, `alpha_c`
  - `units`:
    - `R`: dimensionless
    - `n`: dimensionless
    - `w_t`: dimensionless
    - `t_2rho`: dimensionless
    - `mu`: dimensionless
    - `theta`: degrees
    - `alpha_c`: dimensionless

### lower_limit_data.csv
- path: `/app/outputs/lower_limit_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Lower limit of the geometrical ratio t/2ρ from the condition l0/t > 0. The hidden checker will recompute the limit and verify agreement.
- schema:
  - `type`: table
  - `required_columns`: `w_t`, `theta`, `lower_limit`
  - `units`:
    - `w_t`: dimensionless
    - `theta`: degrees
    - `lower_limit`: dimensionless

Notes: All output files are CSV tables with precisely the columns listed. The hidden checker will re‑implement the analytic expressions and compare values numerically. Trends (e.g., SR decreasing with α, α_c decreasing with w/t, lower limit decreasing with w/t) may be checked as additional structural evidence.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sr_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "w_t",
          "t_2rho",
          "n",
          "mu",
          "R",
          "theta",
          "SR"
        ],
        "units": {
          "alpha": "dimensionless",
          "w_t": "dimensionless",
          "t_2rho": "dimensionless",
          "n": "dimensionless",
          "mu": "dimensionless",
          "R": "dimensionless",
          "theta": "degrees",
          "SR": "dimensionless"
        }
      },
      "description": "Spring‑back ratio SR as a function of loading factor α and other process/material parameters. The hidden checker will recompute the SR values using the same analytic formulas and parameter grids, comparing each cell within a relative tolerance (e.g., 1e-4)."
    },
    {
      "file": "alpha_c_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "n",
          "w_t",
          "t_2rho",
          "mu",
          "theta",
          "alpha_c"
        ],
        "units": {
          "R": "dimensionless",
          "n": "dimensionless",
          "w_t": "dimensionless",
          "t_2rho": "dimensionless",
          "mu": "dimensionless",
          "theta": "degrees",
          "alpha_c": "dimensionless"
        }
      },
      "description": "Critical loading factor α_c for spring‑back elimination. The hidden checker will recompute α_c from the equation SR=0 and verify numeric agreement."
    },
    {
      "file": "lower_limit_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "w_t",
          "theta",
          "lower_limit"
        ],
        "units": {
          "w_t": "dimensionless",
          "theta": "degrees",
          "lower_limit": "dimensionless"
        }
      },
      "description": "Lower limit of the geometrical ratio t/2ρ from the condition l0/t > 0. The hidden checker will recompute the limit and verify agreement."
    }
  ],
  "notes": "All output files are CSV tables with precisely the columns listed. The hidden checker will re‑implement the analytic expressions and compare values numerically. Trends (e.g., SR decreasing with α, α_c decreasing with w/t, lower limit decreasing with w/t) may be checked as additional structural evidence."
}
```

## How you are scored
A hidden checker independently re‑implements the same analytic expressions and evaluates them on the identical parameter grids. It compares each cell of your CSV files against its own recomputed values (relative tolerance). Additionally, the checker verifies that the computed quantities follow physically expected monotonic relationships with respect to the input parameters (e.g., how SR changes with α, how α_c varies with w/t, and how the lower limit depends on w/t and θ). Each scored artifact (sr_data.csv, alpha_c_data.csv, lower_limit_data.csv) is compared and contributes a portion of the total reward. Reporting numbers without actually computing them from the formulas will not pass the structural and recomputation checks.
