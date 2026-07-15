# AE Energy Rate Analysis for Failure Prediction Using Voight Law

## Problem background
Quasi-brittle materials such as granite and bone fail under constant load through microcrack coalescence, accompanied by accelerating acoustic emission (AE). This task investigates whether the AE energy rate during the final cascade before failure conforms to Voight's rate-dependent material failure law and, if so, whether the inverse rate can be used to predict the time to failure. The analysis is applied to six granite beam experiments (ranging in duration from 35 seconds to 50 hours) and two skull fracture experiments on human cadaver heads under surgical pinning loads.

## Approach
The analysis treats the normalized cumulative AE energy as the observable. For each experiment, event energies (amplitude × duration) are accumulated and normalized by the median event energy, yielding a dimensionless cumulative energy curve. The AE energy rate and acceleration are then obtained via a finite-difference scheme with down-sampling to suppress noise. Compliance with Voight's law is examined by a linear regression of log(acceleration/rate) versus log(rate) over the final failure cascade, from which the exponent α and coefficient η are extracted. To predict the failure time, the inverse rate is extrapolated to zero using a moving‑window linear regression; the x‑intercept gives the predicted failure time. The actual failure time is taken as the time of the last AE event.

## Reproduction target
For every experiment (six granite beams and two skull fracture tests), compute the Voight law exponent α, the coefficient η, the actual failure time, and the predicted failure time. Write the results to `/app/outputs/results_summary.csv` with the columns: experiment, material, actual_failure_time_seconds, predicted_failure_time_seconds, alpha, eta.

## Assets

- Granite beam AE event data (Winner et al. 2018): http://d-scholarship.pitt.edu/id/eprint/48634
- Skull fracture AE event data (Bunger et al. 2024): http://d-scholarship.pitt.edu/id/eprint/46998
- Python packages: numpy, scipy, pandas, matplotlib: numpy scipy pandas matplotlib

## Workflow steps

### Step 1: Load AE event data
- Role: process
- Action: Download the granite beam and skull fracture AE event datasets from the public repositories. Parse each dataset into tables containing event time, amplitude, and duration for all 8 experiments (6 granite beams, 2 skull fracture locations).
- Evidence: `/app/outputs/ae_data_load.log`

### Step 2: Compute normalized cumulative AE energy Ω(t)
- Role: process
- Action: For each experiment, compute event energy as amplitude × duration, cumulative energy over time, then normalize by the median event energy to obtain the dimensionless response Ω(t).
- Evidence: `/app/outputs/omega_curves.npy`

### Step 3: Compute AE energy rate and acceleration
- Role: process
- Action: Apply a finite-difference scheme with down-sampling to Ω(t) to compute the rate dΩ/dt and acceleration d²Ω/dt². Use down-sampling factors f_d = 500 for five longer granite beam tests, f_d = 50 for the 35‑second granite test, and f_d = 20 for both skull fracture tests.
- Evidence: `/app/outputs/rate_accel.npy`

### Step 4: Fit Voight law, predict failure time, and write results
- Role: scored (load-bearing)
- Action: For each experiment: (1) determine the onset of the final failure cascade as the period after the initial rate decline where dΩ/dt begins to increase monotonically; (2) perform linear regression on log(d²Ω/dt² / (dΩ/dt)) vs log(dΩ/dt) over that cascade to extract α = slope + 1 and η = exp(intercept); (3) compute the inverse rate 1/(dΩ/dt) and apply a moving‑window linear regression (window sizes: c_win = 100 for five longer rock tests, c_win = 50 for the 35‑second rock test, c_win = 5 for both skull tests) to predict failure time t_c as the x‑intercept; (4) determine the actual failure time as the time of the last AE event; (5) write results_summary.csv with columns: experiment, material, actual_failure_time_seconds, predicted_failure_time_seconds, alpha, eta.
- Output file: `/app/outputs/results_summary.csv`
- Format: csv
- Contract: columns: experiment (string), material (string), actual_failure_time_seconds (float), predicted_failure_time_seconds (float), alpha (float), eta (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_summary.csv
- path: `/app/outputs/results_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: For each of the 8 experiments, the fitted Voight law exponent α, coefficient η, actual failure time, and predicted failure time. The checker compares each value against hidden reference values derived from the paper's analysis.
- schema:
  - `type`: table
  - `required_columns`: `experiment`, `material`, `actual_failure_time_seconds`, `predicted_failure_time_seconds`, `alpha`, `eta`
  - `items`: object
  - `units`:
    - `actual_failure_time_seconds`: seconds
    - `predicted_failure_time_seconds`: seconds
    - `alpha`: dimensionless
    - `eta`: dimensionless

Notes: The checker uses a hidden gold extracted from the paper's reported results (α and failure times) and applies tolerances appropriate for the analysis method. The agent's reported actual_failure_time_seconds is also verified against known experiment durations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "experiment",
          "material",
          "actual_failure_time_seconds",
          "predicted_failure_time_seconds",
          "alpha",
          "eta"
        ],
        "items": {},
        "units": {
          "actual_failure_time_seconds": "seconds",
          "predicted_failure_time_seconds": "seconds",
          "alpha": "dimensionless",
          "eta": "dimensionless"
        }
      },
      "description": "For each of the 8 experiments, the fitted Voight law exponent α, coefficient η, actual failure time, and predicted failure time. The checker compares each value against hidden reference values derived from the paper's analysis."
    }
  ],
  "notes": "The checker uses a hidden gold extracted from the paper's reported results (α and failure times) and applies tolerances appropriate for the analysis method. The agent's reported actual_failure_time_seconds is also verified against known experiment durations."
}
```

## How you are scored
A hidden verifier automatically scores your output. It compares your reported values (α and predicted failure time for each experiment) to hidden reference values derived from the original analysis, using tolerances appropriate for the method. The reward reflects how closely your computed values match the reference; simply reporting a known number without running the analysis does NOT yield a high score. The verifier reads only your `results_summary.csv` and any required intermediate evidence files, then computes a combined score across all experiments.
