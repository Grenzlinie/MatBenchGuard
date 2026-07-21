# Analytic Return-Loop Magnetization for 1D Random-Field Ising Model

## Problem background
Hysteresis in the one-dimensional random-field Ising model (RFIM) at zero temperature is a classic problem in statistical mechanics. The ferromagnetic RFIM, with coupling J=1 and a continuous distribution of quenched random fields, exhibits an exact analytic solution for the main hysteresis loop and for return (minor) loops when the applied field is reversed from an arbitrary point on the main loop. These closed-form expressions, obtained via probabilistic methods, provide precise benchmarks for avalanche dynamics and memory effects in disordered systems. This task reproduces the analytic magnetization on the lower main loop and on a first return loop using a Gaussian random-field distribution (mean 0, variance 1).

## Approach
The magnetization per spin can be expressed exactly in terms of single-spin flip probabilities and local-neighbourhood statistics. Define the probability that a spin with n up neighbours (n=0,1,2) flips up at applied field h:

  p_n(h) = Prob[ h_i ≥ 2(1-n)J - h ] = 1 − Φ( 2(1-n) − h )

where Φ is the cumulative distribution function of the Gaussian random field (mean=0, variance=1). Use `scipy.special.erf` to evaluate Φ.

The conditional probability that a neighbour flips up before the spin is

  P*(h) = p_0(h) / [ 1 − (p_1(h) − p_0(h)) ].

The probability that an arbitrary spin is up on the lower main loop is

  p(h) = [P*(h)]² p_2(h) + 2 P*(h)[1−P*(h)] p_1(h) + [1−P*(h)]² p_0(h),

and the magnetization is m(h) = 2 p(h) − 1.

When the field is reversed from a point h on the lower main loop down to h′ (with h−2J ≤ h′ ≤ h), up spins are classified by their local environments before reversal. The fractions that turn down are

  q_r² = [P*(h)]² [p_2(h) − p_2(h′)]

  q_r¹ = 2 P*(h) [q_a + q_b] [p_1(h) − p_1(h′)]

  q_r⁰ = [q_a + q_b]² [p_0(h) − p_0(h′)]

where

  f(h) = (1−p_2(h)) P*(h) + (1−p_1(h)) (1−P*(h))

  q_a = f(h) / [ 1 − (p_1(h) − p_1(h′)) ]

  q_b = [p_2(h) − p_2(h′)] P*(h) / [ 1 − (p_1(h) − p_1(h′)) ].

The fraction of up spins after reversal is p′(h′) = p(h) − q_r² − q_r¹ − q_r⁰, and the return-loop magnetization is m′(h′) = 2 p′(h′) − 1.

Note that the coupling is J=1 and the random-field distribution is Gaussian with mean 0 and variance 1 throughout.

## Reproduction target
Compute the lower main loop magnetization m(h) for applied field h from −5 to 5 (step 0.1) using the analytic formulas above. Write the results to `main_loop.csv`, sorted by increasing h, with columns `h` and `m`.

Then, taking the reversal point h=1 on the lower main loop, compute the return loop magnetization m′(h′) for the reversed field h′ from 1 down to −1 (step 0.05). Write the results to `return_loop.csv`, sorted by decreasing h′, with columns `h_prime` and `m_prime`.

Both output files must be placed under `/app/outputs`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute main loop magnetization
- Role: scored
- Action: Evaluate the closed-form expressions for the lower main loop magnetization m(h) for a Gaussian random-field distribution (mean=0, variance=1) and coupling J=1. Compute m(h) for applied field h from -5 to 5 with step 0.1. Write the results as a CSV file.
- Output file: `/app/outputs/main_loop.csv`
- Format: csv
- Contract: CSV with header 'h,m'. 'h' is float (applied field), 'm' is float (magnetization per spin). Rows sorted by increasing h.
- Scoring: scored by hidden verifier

### Step 2: Compute return loop magnetization
- Role: scored (load-bearing)
- Action: Evaluate the closed-form expressions for the return loop magnetization m'(h') when the field is reversed from h=1 on the lower main loop down to h'=-1 with step 0.05. Write the results as a CSV file.
- Output file: `/app/outputs/return_loop.csv`
- Format: csv
- Contract: CSV with header 'h_prime,m_prime'. 'h_prime' is float (reversed field), 'm_prime' is float (magnetization per spin). Rows sorted by decreasing h_prime.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/main_loop.csv`
- `/app/outputs/return_loop.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### main_loop.csv
- path: `/app/outputs/main_loop.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Lower main loop magnetization m(h) for applied field h from -5 to 5 (step 0.1).
- schema:
  - `type`: table
  - `required_columns`: `h`, `m`
  - `units`:
    - `h`: dimensionless (applied field relative to coupling units)
    - `m`: dimensionless (magnetization per spin)

### return_loop.csv
- path: `/app/outputs/return_loop.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: First return loop magnetization m'(h') for reversed field from h=1 down to -1 (step 0.05).
- schema:
  - `type`: table
  - `required_columns`: `h_prime`, `m_prime`
  - `units`:
    - `h_prime`: dimensionless (reversed field relative to coupling units)
    - `m_prime`: dimensionless (magnetization per spin)

Notes: Both CSV files are evaluated by recomputing the analytic magnetization values using the Gaussian CDF (scipy.special.erf) with the same distribution parameters and coupling. The checker compares each numeric value to its recomputed gold within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "main_loop.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "h",
          "m"
        ],
        "units": {
          "h": "dimensionless (applied field relative to coupling units)",
          "m": "dimensionless (magnetization per spin)"
        }
      },
      "description": "Lower main loop magnetization m(h) for applied field h from -5 to 5 (step 0.1)."
    },
    {
      "file": "return_loop.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "h_prime",
          "m_prime"
        ],
        "units": {
          "h_prime": "dimensionless (reversed field relative to coupling units)",
          "m_prime": "dimensionless (magnetization per spin)"
        }
      },
      "description": "First return loop magnetization m'(h') for reversed field from h=1 down to -1 (step 0.05)."
    }
  ],
  "notes": "Both CSV files are evaluated by recomputing the analytic magnetization values using the Gaussian CDF (scipy.special.erf) with the same distribution parameters and coupling. The checker compares each numeric value to its recomputed gold within appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently recomputes the magnetization values using the same analytic formulas and the same Gaussian distribution (mean=0, variance=1, J=1). It reads your CSV files and compares each numeric entry to its recomputed gold within appropriate relative and absolute tolerances. Both files must be present and correctly formatted. Your reward is proportional to the fraction of compared values that fall within tolerance, with full credit awarded when all values are sufficiently close. A partial score is given if only some values match.
