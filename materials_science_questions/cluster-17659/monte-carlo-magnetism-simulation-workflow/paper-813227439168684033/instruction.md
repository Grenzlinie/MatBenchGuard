# Monte Carlo simulation of short-time magnetization relaxation in dipolar Ising spin systems

## Problem background
Low-temperature magnetization relaxation in magnetic molecular solids, such as Fe8, is highly non-exponential. Experiments often observe a square-root-in-time behavior at short times, but explaining this requires accounting for long-range dipole-dipole interactions between molecular spins. These interactions couple the spins and make a simple independent‑spin picture invalid. Monte Carlo simulations of Ising spins with dipolar couplings and a tunneling‑based flip rule provide a means to study the magnetization decay from first principles and to test whether the short‑time behavior follows a sqrt(t) law and with what coefficient.

## Approach
The simulation models the molecular solid as a spherical sample of N Ising spins on a cubic lattice. Spins interact via dipole‑dipole couplings of the form K_ij = 2 E_dm a^3 (1 - 3 z_ij^2/r_ij^2) / r_ij^3, where a is the near‑neighbor distance and the easy axis points along z. The system is initialized with all spins up (saturated magnetization). Time is discretised into small steps dt. At each step the bias energy E_i on every site (sum_j K_ij sigma_j) is computed. A spin flips if |E_i| ≤ W, with probability Γ_0 dt; otherwise it does not flip. The parameters are: Δ_2 = 2.0, E_dm = 50 Δ_2, W = 2.5 Δ_2, Γ_0 = Δ_2^2/(4W), and dt = 0.01 E_dm/Δ_2^2. The simulation is run for at least 10 independent realizations (different random seeds) up to about 5 τ, where τ = E_dm/Δ_2^2. The average magnetization m(t) is recorded at every time step; the final averaged curve is sampled at six normalized times. From this averaged m(t) the form m(t) = 1 - sqrt(G t) is fitted to the short‑time region (t/τ ≤ 5), and the fitted coefficient G is reported. The quality of the fit and the extracted G characterize the short‑time relaxation and can be compared with theoretical expectations.

## Reproduction target
Produce two artifacts:
1. magnetization_curve.csv – a CSV file with columns 'time, magnetization', containing the averaged magnetization m(t) at the normalized times t/τ = 0.1, 0.3, 0.5, 1.0, 3.0, 5.0.
2. sqrt_coefficient.txt – a text file containing the fitted coefficient G obtained by fitting m(t) = 1 - sqrt(G t) over the short‑time range (t/τ ≤ 5).
The simulation must be executed for a spherical sample of N=9171 spins (diameter 27, a=1) using exactly the protocol and parameters described above.

## Assets

- Python 3 with NumPy, SciPy: python

## Workflow steps

### Step 1: Build sample and dipole-coupling lookup table
- Role: process
- Action: Construct a spherical sample of N=9171 spins on a simple cubic lattice (diameter 27a, a=1). Compute and store all pairwise dipole couplings K_ij = 2 * E_dm * a^3 / r_ij^3 * (1 - 3*z_ij^2/r_ij^2) using E_dm = 50 * Delta_2 and Delta_2 = 2.0.
- Evidence: `/app/outputs/coupling_table.pkl`

### Step 2: Monte Carlo simulation of magnetization decay curve
- Role: scored (load-bearing)
- Action: Initialize all spins up. Evolve using the modified flip protocol: at each time step dt = 0.01 * E_dm / Delta_2^2, compute bias E_i at every site, then flip spin i with probability Gamma_0 * dt if |E_i| <= W, where Gamma_0 = Delta_2^2/(4W) and W = 2.5 * Delta_2. Record magnetization m(t) at every time step. Repeat for at least 10 independent runs and average. Save the averaged magnetization at the normalized times t/tau = [0.1, 0.3, 0.5, 1.0, 3.0, 5.0] (tau = E_dm/Delta_2^2).
- Output file: `/app/outputs/magnetization_curve.csv`
- Format: csv
- Contract: CSV with header: time, magnetization. Rows correspond to the six normalized times listed.
- Scoring: scored by hidden verifier

### Step 3: Fit sqrt(t) law and report coefficient
- Role: scored
- Action: Using the full magnetization time series obtained from the simulation, fit the short-time magnetization for t/tau <= 5 to the form 1 - sqrt(G * t) and report the best-fit G.
- Output file: `/app/outputs/sqrt_coefficient.txt`
- Format: txt
- Contract: Single line containing the numerical value of G (unitless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_curve.csv`
- `/app/outputs/sqrt_coefficient.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_curve.csv
- path: `/app/outputs/magnetization_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Averaged magnetization m(t) at six normalized times; the checker recomputes the mean absolute error against hidden paper‑reported values for these same conditions and scores monotonically (lower error yields higher reward).
- schema:
  - `type`: table
  - `required_columns`: `time`, `magnetization`

### sqrt_coefficient.txt
- path: `/app/outputs/sqrt_coefficient.txt`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Fitted coefficient G from the short‑time sqrt(t) law; the checker computes the relative error with respect to the paper‑derived theoretical coefficient and scores monotonically (smaller relative error yields higher reward).
- schema:
  - `type`: text
  - `required`: object

Notes: The agent must implement the Monte Carlo simulation from scratch using the public protocol and parameters. No gold values are given; the checker compares against hidden reference values derived from the paper's own simulation and theoretical expression.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "magnetization"
        ]
      },
      "description": "Averaged magnetization m(t) at six normalized times; the checker recomputes the mean absolute error against hidden paper‑reported values for these same conditions and scores monotonically (lower error yields higher reward)."
    },
    {
      "file": "sqrt_coefficient.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "required": {}
      },
      "description": "Fitted coefficient G from the short‑time sqrt(t) law; the checker computes the relative error with respect to the paper‑derived theoretical coefficient and scores monotonically (smaller relative error yields higher reward)."
    }
  ],
  "notes": "The agent must implement the Monte Carlo simulation from scratch using the public protocol and parameters. No gold values are given; the checker compares against hidden reference values derived from the paper's own simulation and theoretical expression."
}
```

## How you are scored
A hidden verifier independently evaluates each artifact. For magnetization_curve.csv the verifier computes the mean absolute error (MAE) between your reported magnetization values at the six times and a hidden reference curve obtained from a high‑fidelity simulation of the same system under identical conditions. For sqrt_coefficient.txt the verifier computes the relative error between your reported G and a hidden theoretical reference value. The final reward is a weighted combination: lower MAE and smaller relative error yield higher reward, with reward decreasing monotonically as errors increase. Executing the Monte Carlo simulation accurately (proper averaging over runs, correct bias computation) is essential; simply reporting a number without running the simulation will be penalised through the reward function.
