# Steepest descent velocity decay exponent in 2D harmonic spheres

## Problem background
Glass-forming liquids exhibit complex relaxation dynamics when quenched to low energy states. The steepest descent (overdamped) dynamics from equilibrium configurations probes the geometry of the potential energy landscape. A central observable is the root-mean-squared velocity, which often follows a power-law decay with an exponent β that can depend on initial temperature and spatial dimension. Understanding this exponent in finite-dimensional systems is important for characterizing the nature of energy landscapes and the role of localized defects in structural glasses. This task requires computing the steepest descent velocity decay exponent β for a two-dimensional polydisperse harmonic sphere model at two contrasting initial conditions.

## Approach
The approach uses a two-dimensional polydisperse harmonic sphere model. For the high-temperature limit, a random non-overlapping configuration is generated as the initial state. For the low-temperature regime, an equilibrium configuration is prepared using swap Monte Carlo at a low target temperature. For each configuration, the overdamped equations of motion are integrated to simulate steepest descent dynamics. The root-mean-squared velocity of all particles is recorded at logarithmically spaced time points. The long-time portion of the velocity decay is then fit to a power-law model to extract the exponent β, which quantifies how rapidly the system relaxes toward a local energy minimum.

## Reproduction target
For a 2D polydisperse harmonic sphere system with N=64000 particles, continuous size distribution f(d) ∝ d⁻³, polydispersity δ=0.23, nonadditivity ε=0.2, and volume fraction φ=1.2, produce the following:

- A random, non-overlapping initial configuration (high-temperature limit) and an equilibrium configuration prepared by swap Monte Carlo at T=0.035 (low-temperature).
- Simulate steepest descent dynamics from each configuration, recording the root-mean-squared velocity as a function of time in CSV files (velocity_highT.csv, velocity_lowT.csv).
- For each velocity time series, select the long-time window beyond initial transients and before finite-size cutoff, fit a power-law decay ⟨|v(t)|⟩ ∝ t⁻ᵝ, and extract the exponents β_highT and β_lowT.
- Write the fitted exponents to beta_results.json.

## Assets

- LAMMPS: https://www.lammps.org/
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Prepare equilibrium configurations
- Role: process
- Action: Generate initial equilibrium configurations for a 2D polydisperse harmonic sphere model with N=64000 particles, size distribution f(d) ∝ d^{-3}, polydispersity δ=0.23, nonadditivity ε=0.2, volume fraction φ=1.2. For the high‑temperature limit (T→∞) create a random non‑overlapping configuration. For the low‑temperature condition (T=0.035) equilibrate using swap Monte Carlo (swap probability 0.2, similar‑diameter restriction |d_i-d_j|<0.2). Save the configurations as files to be used by the dynamics step.
- Evidence: `/app/outputs/init_highT.data, init_lowT.data`

### Step 2: Run steepest descent dynamics (high temperature)
- Role: scored (load-bearing)
- Action: Starting from the high‑temperature configuration, integrate the overdamped equations of motion ζ dr_i/dt = -∂E/∂r_i using LAMMPS or equivalent. Record the root‑mean‑squared velocity ⟨|v(t)|⟩ = sqrt( (1/N)∑_i |dr_i/dt|^2 ) at logarithmically spaced time points covering the power‑law decay regime. Save the time series as a CSV file with columns 'time' (simulation time units) and 'velocity' (RMS velocity).
- Output file: `/app/outputs/velocity_highT.csv`
- Format: csv
- Contract: Columns: time (float, simulation time units), velocity (float, RMS velocity). At least 100 time points covering the power‑law decay regime.
- Scoring: scored by hidden verifier

### Step 3: Run steepest descent dynamics (low temperature)
- Role: scored (load-bearing)
- Action: Starting from the low‑temperature configuration, integrate the overdamped equations of motion and record ⟨|v(t)|⟩ as described for the high‑temperature case. Save the time series as velocity_lowT.csv with the same schema.
- Output file: `/app/outputs/velocity_lowT.csv`
- Format: csv
- Contract: Columns: time (float), velocity (float).
- Scoring: scored by hidden verifier

### Step 4: Fit velocity decay exponents
- Role: scored
- Action: Read velocity_highT.csv and velocity_lowT.csv. For each file, select the long‑time window where the decay is power‑law (after initial transients, before finite‑size cutoff). Fit a model ⟨|v(t)|⟩ = A·t^{-β} (e.g., linear regression on log-log data). Extract the exponents β_highT and β_lowT. Write the results as a JSON file containing "beta_highT" and "beta_lowT".
- Output file: `/app/outputs/beta_results.json`
- Format: json
- Contract: {"beta_highT": float, "beta_lowT": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/velocity_highT.csv`
- `/app/outputs/velocity_lowT.csv`
- `/app/outputs/beta_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### velocity_highT.csv
- path: `/app/outputs/velocity_highT.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: High‑temperature steepest descent velocity time series. The checker will refit the decay exponent β from these data.
- schema:
  - `type`: table
  - `required_columns`: `time`, `velocity`
  - `units`:
    - `time`: simulation time units
    - `velocity`: RMS velocity (same units as dr_i/dt)

### velocity_lowT.csv
- path: `/app/outputs/velocity_lowT.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Low‑temperature steepest descent velocity time series. The checker will refit the decay exponent β from these data.
- schema:
  - `type`: table
  - `required_columns`: `time`, `velocity`
  - `units`:
    - `time`: simulation time units
    - `velocity`: RMS velocity

### beta_results.json
- path: `/app/outputs/beta_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Self‑reported fitted exponents β for the two temperatures. The checker will recompute β from the raw velocity files, compare to hidden paper‑reported values, and cross‑verify the self‑reported numbers.
- schema:
  - `type`: object
  - `required`:
    - `beta_highT`: float (unitless)
    - `beta_lowT`: float (unitless)

Notes: The primary scoring is based on recomputing β from velocity_highT.csv and velocity_lowT.csv using a power‑law fit in the appropriate long‑time window. The beta_results.json file provides self‑consistency cross‑check but does not carry strong scoring weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "velocity_highT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "velocity"
        ],
        "units": {
          "time": "simulation time units",
          "velocity": "RMS velocity (same units as dr_i/dt)"
        }
      },
      "description": "High‑temperature steepest descent velocity time series. The checker will refit the decay exponent β from these data."
    },
    {
      "file": "velocity_lowT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "velocity"
        ],
        "units": {
          "time": "simulation time units",
          "velocity": "RMS velocity"
        }
      },
      "description": "Low‑temperature steepest descent velocity time series. The checker will refit the decay exponent β from these data."
    },
    {
      "file": "beta_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "beta_highT": "float (unitless)",
          "beta_lowT": "float (unitless)"
        }
      },
      "description": "Self‑reported fitted exponents β for the two temperatures. The checker will recompute β from the raw velocity files, compare to hidden paper‑reported values, and cross‑verify the self‑reported numbers."
    }
  ],
  "notes": "The primary scoring is based on recomputing β from velocity_highT.csv and velocity_lowT.csv using a power‑law fit in the appropriate long‑time window. The beta_results.json file provides self‑consistency cross‑check but does not carry strong scoring weight."
}
```

## How you are scored
A hidden verifier independently reads your velocity_highT.csv and velocity_lowT.csv. It performs its own power-law fit on the long-time domain and obtains recomputed β values. It then compares these recomputed exponents to reference values (not revealed to you) and cross-checks the self-reported β in beta_results.json for consistency. Each scored stage (the two velocity CSVs and the final beta_results.json) contributes to a weighted score. The overall reward reflects how accurately your computed exponents agree with the reference, measured with a permissive tolerance that absorbs legitimate implementation variability. Simply reporting a number is not sufficient; the raw velocity data must support a comparable fit.
