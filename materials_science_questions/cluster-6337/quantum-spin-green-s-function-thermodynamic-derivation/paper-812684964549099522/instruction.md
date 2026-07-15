# 2D XY model Monte Carlo simulation and magnetization moment analysis

## Problem background
The two-dimensional XY model is a classic system for studying finite-size effects near a continuous phase transition. In its low-temperature phase, the model exhibits critical correlations over a whole range of temperatures, leading to anomalously large finite-size corrections. Although the thermodynamic magnetization vanishes, finite systems still show a measurable scalar order parameter M (the instantaneous magnetization per spin), whose probability distribution is asymmetric and universal. Spin-wave theory provides exact analytical expressions for the mean magnetization and susceptibility in the thermodynamic limit, while Monte Carlo simulations reveal the distribution's shape. The asymmetry of the distribution originates from three-spin and higher correlations, and it cannot be captured by a simple Gaussian approximation.

## Approach
The core idea is to simulate the harmonic XY (HXY) model, which approximates the full XY Hamiltonian by expanding the cosine potential to quadratic order while respecting the periodic nature of the angles. A Metropolis Monte Carlo algorithm is used to sample equilibrium spin configurations on a 32×32 square lattice with periodic boundary conditions. From the time series of instantaneous magnetization M (per spin), we compute its lower moments: mean <M>, variance σ², and skewness γ₁. These are compared with the exact spin-wave predictions for the mean magnetization and the magnetic susceptibility χ. The analytical mean is obtained from a closed-form expression that depends only on the lattice size N, temperature T, and exchange coupling J. The susceptibility is computed via a lattice Green's function and approximated by a simple formula involving a known numerical constant. The comparison tests whether the simulated fluctuations reproduce the theoretically expected moments, and whether the skewness is significantly positive, confirming an asymmetric distribution.

## Reproduction target
Run a Metropolis simulation of the HXY model on an L=32 square lattice (N=1024 spins) at T/J = 0.5. Use at least 2000 sweeps for equilibration and collect at least 10,000 independent measurements of the instantaneous magnetization per spin M. From the collected samples, compute the thermal average <M>, variance σ², and skewness γ₁. Also compute the analytical spin-wave predictions for the mean magnetization and the susceptibility χ (using N=1024, T=0.5, J=1, and the lattice constant a₂D=258.6). Write the five quantities — mean, variance, skewness, analytical_mean, analytical_chi — to /app/outputs/magnetization_moments.json, and also output the binned probability distribution of the scaled magnetization y to /app/outputs/magnetization_distribution.json. The verifier will independently recompute the expected analytical values from the public parameters, compare your simulated moments to them, and check the consistency of the distribution.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Monte Carlo simulation of the HXY model
- Role: process
- Action: Implement a Metropolis Monte Carlo simulation of the 2D harmonic XY (HXY) model on an L=32 square lattice with periodic boundary conditions, using J=1, T=0.5. Define the instantaneous magnetization per spin as M = (1/N) sqrt((∑_i cos θ_i)^2 + (∑_i sin θ_i)^2) where N = L^2 = 1024. Equilibrate for at least 2000 sweeps, then collect at least 10,000 independent values of M, one per sweep. Store the raw magnetization time series for later analysis.
- Evidence: `/app/outputs/magnetization_samples.csv`

### Step 2: Magnetization moments and analytical spin‑wave predictions
- Role: scored (load-bearing)
- Action: From the magnetization samples collected in step_01, compute the thermal average <M>, variance σ², and skewness γ₁ = <(M−<M>)³>/σ³. Also compute the analytical spin‑wave predictions for the mean and susceptibility using the formulas from the paper (mean = (1/(2N))^{T/(8πJ)}, susceptibility = (1/(2·a_2D))·N·<M>²·T/J² with a_2D=258.6). Store all five quantities in magnetization_moments.json.
- Output file: `/app/outputs/magnetization_moments.json`
- Format: json
- Contract: {"mean": <float>, "variance": <float>, "skewness": <float>, "analytical_mean": <float>, "analytical_chi": <float>}
- Scoring: scored by hidden verifier

### Step 3: Magnetization probability distribution
- Role: scored
- Action: Using the magnetization samples from step_01, compute the binned probability distribution of the scaled magnetization variable y = (1/T) * L^{T/(4πJ)} * M, where L=32, T=0.5, J=1. First compute the mean <y> from the samples. Then define bins spanning at least -5σ to +5σ around the mean with at least 50 bins, where σ is the standard deviation of y. Count the number of samples falling into each bin. Store the bin edges and the corresponding counts in magnetization_distribution.json.
- Output file: `/app/outputs/magnetization_distribution.json`
- Format: json
- Contract: {"bin_edges": [float], "counts": [int], "num_samples": int}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_moments.json`
- `/app/outputs/magnetization_distribution.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_moments.json
- path: `/app/outputs/magnetization_moments.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Monte Carlo magnetization moments (mean, variance, skewness) and the theoretically expected spin‑wave values (analytical_mean, analytical_chi). The hidden checker recomputes the expected references and verifies mean and variance within tolerance and skewness ≥0.1.
- schema:
  - `type`: object
  - `required`: `mean`, `variance`, `skewness`, `analytical_mean`, `analytical_chi`
  - `properties`:
    - `mean`:
      - `type`: number
    - `variance`:
      - `type`: number
    - `skewness`:
      - `type`: number
    - `analytical_mean`:
      - `type`: number
    - `analytical_chi`:
      - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "mean",
          "variance",
          "skewness",
          "analytical_mean",
          "analytical_chi"
        ],
        "properties": {
          "mean": {
            "type": "number"
          },
          "variance": {
            "type": "number"
          },
          "skewness": {
            "type": "number"
          },
          "analytical_mean": {
            "type": "number"
          },
          "analytical_chi": {
            "type": "number"
          }
        }
      },
      "description": "Monte Carlo magnetization moments (mean, variance, skewness) and the theoretically expected spin‑wave values (analytical_mean, analytical_chi). The hidden checker recomputes the expected references and verifies mean and variance within tolerance and skewness ≥0.1."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your magnetization_moments.json. It independently computes the analytical spin-wave mean and susceptibility from the same public parameters (T, J, N, a₂D) and then compares your simulated mean and variance to those expected values, using an appropriate tolerance that accounts for run-to-run stochastic fluctuations. It also checks that the skewness meets a minimum threshold. Each of these three checks contributes equally to the final reward. Simply reporting the paper's known numbers without genuinely running the simulation will not pass, because the verifier performs its own recomputation and can detect inconsistencies.
