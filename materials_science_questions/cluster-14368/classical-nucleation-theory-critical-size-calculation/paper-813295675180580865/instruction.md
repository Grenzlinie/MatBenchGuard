# Condensation Relaxation Simulation with Harmonic Pulsations

## Problem background
Consider a supersaturated vapor in a vapor–gas mixture that undergoes condensation relaxation through nucleation and droplet growth, characterized by a condensation‑relaxation time and a final droplet number density. When the thermodynamic parameters of the mixture (e.g., temperature) are subjected to small harmonic pulsations, the relaxation process may be altered. This work numerically explores how such pulsations, governed by their frequency, amplitude, and initial phase, affect the condensation‑relaxation time and droplet number density.

## Approach
The model is based on moment equations derived from the kinetic equation for the droplet‑size distribution, coupled with classical Zel’dovich–Frenkel’ nucleation theory for the nucleation rate and the free‑molecular growth law for the droplet growth rate. The working fluid is a cesium–argon mixture with a volume ratio of 1:7. The temperature pulsation is modeled as a small harmonic perturbation that modifies the supersaturation through the temperature‑dependent saturation vapor pressure.

First compute the baseline (no pulsation) condensation‑relaxation time and droplet number density for a set of initial supersaturations. Then introduce harmonic pulsations of different amplitudes and frequencies, recording the resulting relaxation time and number density over a wide frequency sweep. Finally, for each amplitude and supersaturation, perform a simulation at a sufficiently high frequency to capture the behavior in the regime where the outcome becomes independent of the pulsation details. All results are written to a CSV file.

## Reproduction target
Produce a single CSV file, `/app/outputs/simulation_results.csv`, containing the condensation‑relaxation time τ_c (in seconds) and droplet number density n_d (in m⁻³) for all required combinations of initial supersaturation s0, pulsation amplitude θ0, and frequency ν. The file must include baseline rows with θ0=0, ν=0, frequency‑sweep rows for s0=6, and plateau‑regime rows for all (s0, θ0>0) pairs. The hidden verifier will use this file to verify that the simulated system exhibits a minimum frequency plateau (i.e., ν_min) and to check how τ_c and n_d scale with s0 and θ0 in the high‑frequency regime.

## Assets

- Python interpreter: python>=3.8
- NumPy: numpy
- SciPy: scipy
- Classical nucleation theory formulas
- Cesium thermodynamic properties

## Workflow steps

### Step 1: Run condensation relaxation simulation
- Role: scored (load-bearing)
- Action: Implement the moment equations (3) for condensation relaxation of a cesium–argon mixture (volume ratio 1:7) using classical Zel'dovich–Frenkel' nucleation rate and free-molecular droplet growth. First compute the baseline condensation-relaxation time τ_c^0 and droplet number density n_d^0 without pulsations for initial supersaturations s0 = 3,4,5,6. Then introduce harmonic temperature pulsations of the form ϑ = ϑ0 sin(2π ν t) with initial phase zero. For s0 = 6 and pulsation amplitudes ϑ0 = 0.0005, 0.01, 0.05 (0.05%, 1%, 5%), sweep the frequency ν from 0.1 Hz to 10^4 Hz and compute τ_c and n_d. From these sweeps identify the minimum frequency ν_min above which τ_c and n_d plateau (relative change below ~10%). For each (s0, ϑ0>0) combination, simulate at a frequency in the plateau regime (e.g., ν > ν_min) to obtain representative τ_c and n_d. Write the results to simulation_results.csv.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: columns: s0 (float, initial supersaturation), theta0 (float, pulsation amplitude fraction), nu (float, frequency in Hz; set to 0 for baseline), tau_c (float, condensation-relaxation time in seconds), n_d (float, droplet number density in m^-3).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulation results containing τ_c and n_d for baseline (theta0=0, nu=0) and for pulsation cases across the required grid of saturation, amplitude, and frequency. The checker will extract plateau and baseline values to verify the existence of a minimum frequency plateau and the paper's scaling laws.
- schema:
  - `type`: table
  - `required_columns`: `s0`, `theta0`, `nu`, `tau_c`, `n_d`
  - `units`:
    - `nu`: Hz
    - `tau_c`: s
    - `n_d`: m^-3

Notes: The CSV must include all required (s0, theta0, nu) combinations as described in the step action. The frequency-sweep rows for s0=6 serve to identify ν_min and show the plateau; the plateau-regime rows provide the data for the scaling law verification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "s0",
          "theta0",
          "nu",
          "tau_c",
          "n_d"
        ],
        "units": {
          "nu": "Hz",
          "tau_c": "s",
          "n_d": "m^-3"
        }
      },
      "description": "Simulation results containing τ_c and n_d for baseline (theta0=0, nu=0) and for pulsation cases across the required grid of saturation, amplitude, and frequency. The checker will extract plateau and baseline values to verify the existence of a minimum frequency plateau and the paper's scaling laws."
    }
  ],
  "notes": "The CSV must include all required (s0, theta0, nu) combinations as described in the step action. The frequency-sweep rows for s0=6 serve to identify ν_min and show the plateau; the plateau-regime rows provide the data for the scaling law verification."
}
```

## How you are scored
The hidden verifier will read your `simulation_results.csv` and apply a set of checks: it will detect the plateau in the frequency sweep, compute the product ν_min·τ_c, and compare the baseline‑to‑plateau ratios of τ_c and n_d to reference scaling laws. Your reward is a weighted combination of these checks, producing a float between 0 and 1. Achieving a high score requires accurate simulation that reproduces the expected physical trends across the entire parameter grid. There is no partial credit for intermediate steps – only the final CSV file is evaluated.
