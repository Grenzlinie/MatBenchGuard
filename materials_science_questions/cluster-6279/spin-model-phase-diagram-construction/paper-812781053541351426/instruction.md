# Coupled Mean-Field Phase Diagram of a Driven Lattice Gas

## Problem background
A driven lattice gas on a square lattice, with nearest-neighbor attractive interactions and an oscillatory external field, evolves to nonequilibrium steady states (NESS) that exhibit temperature-driven order–disorder transitions. Depending on density and field amplitude, the system displays first- or second-order phase boundaries. The coupled mean-field (CMF) approach describes the local density dynamics and provides a computationally feasible route to map the phase diagram, revealing the dependence of the critical temperature on density and field, and the possible existence of a multicritical point where the critical temperature becomes independent of the field.

## Approach
The system is a lattice gas on a square lattice with nearest‑neighbor attraction: the Hamiltonian is H = -4J ∑_{⟨ij,i'j'⟩} n_{i,j}n_{i',j'}, where the sum runs over all nearest‑neighbour bonds. The driving oscillatory field E acts along the ±y‑direction with half‑period τ (time between sign changes); on the CMF level the field flips sign every τ time units. The reference CMF calculations use τ=1, so we adopt τ=1 here. The Metropolis jump rate for a particle hop is p = min[1, exp(-(ΔH - εE(τ))/k_B T)], where ε = -1, 0, 1 for a hop against, orthogonal to, or along the driving field, respectively. The CMF method writes a set of coupled ODEs (Eq. (2) of the reference) for the local occupation probabilities ρ_{i,j} on each site, using these rates and assuming no stochastic fluctuations. The ODEs are integrated numerically for a lattice of size 80×40 with periodic boundary conditions, starting from random initial conditions. For each fixed global density ρ0 and field amplitude E, we simulate over a range of temperatures, time-averaging after an initial transient. At each temperature we measure the longitudinal order parameter OP_x, defined as OP_x = (R L_x)^{-1} ∑_{i=1}^{L_x} |P(i) - ρ0|, where P(i) = (L_y)^{-1}∑_j n_{i,j} is the density profile along the x‑direction and the normalization constant R = 2ρ0(1-ρ0). The critical temperature Tc is then determined as the temperature where OP_x first exceeds a small threshold (e.g., 0.01) upon cooling. This process is repeated for densities from 0.05 to 0.50 and field amplitudes E=1 and E=10 to construct the phase diagram.

## Reproduction target
Run CMF simulations for the parameter grid: global densities ρ0 ∈ {0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50} and field amplitudes E ∈ {1, 10}. For each (ρ0, E) pair, extract the critical temperature Tc (in units of J/k_B) and write the results to `/app/outputs/phasediagram.csv` with columns `density`, `field`, `Tc`. Using the collected phase diagram, examine the dependence of Tc on field and density, and identify whether there exists a density for which Tc is the same for both field amplitudes.

## Assets

- Python with NumPy and SciPy: numpy, scipy

## Workflow steps

### Step 1: CMF model simulation
- Role: process
- Action: Implement the coupled mean-field (CMF) equations for the driven lattice gas model on a square lattice of size 80×40 with periodic boundary conditions. Use the Hamiltonian H = -4J ∑_{⟨ij,i'j'⟩} n_{i,j}n_{i',j'} and the Metropolis jump rate min[1, exp(-(ΔH - εE(τ))/k_B T)], where ε = -1,0,1 for a hop (against, orthogonal to, along) the oscillatory driving field and the field’s half‑period is τ=1. For each pair of global density ρ0 in {0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50} and field amplitude E in {1, 10}, integrate the ODEs from random initial conditions with integration time step Δt=0.25 up to t=25000, time-averaging for t≥20000. At each temperature T in a range that covers the expected transition (e.g., from 1.0 to 3.0 in steps of 0.1 or finer), compute the longitudinal order parameter OP_x = (R L_x)^{-1} ∑_{i=1}^{L_x} |P(i) - ρ0|, with P(i) = (L_y)^{-1}∑_j n_{i,j} and R = 2ρ0(1-ρ0). Store the raw OP_x(T) data for each (ρ0, E) pair in a structured file (e.g., JSON).
- Evidence: `/app/outputs/cmf_raw_results.json`

### Step 2: Phase diagram extraction
- Role: scored (load-bearing)
- Action: From the CMF simulation results, for each (ρ0, E) pair, determine the critical temperature Tc as the temperature where OP_x first exceeds a small threshold (e.g., 0.01) upon cooling. If no crossing, set Tc = 0. Write a CSV file 'phasediagram.csv' with columns density, field, Tc (units: J/k_B).
- Output file: `/app/outputs/phasediagram.csv`
- Format: csv
- Contract: density (float), field (float), Tc (float, J/k_B)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phasediagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phasediagram.csv
- path: `/app/outputs/phasediagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing the phase diagram: critical temperature Tc (in units of J/k_B) for each density and field amplitude.
- schema:
  - `type`: table
  - `required_columns`: `density`, `field`, `Tc`
  - `units`:
    - `density`: dimensionless
    - `field`: dimensionless (J)
    - `Tc`: J/k_B

Notes: The scored Tc values are compared against hidden gold values derived from the paper's CMF results. The checker verifies that for density ≈0.16 the Tc values for E=1 and E=10 are equal within tolerance (multicritical point evidence).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phasediagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "density",
          "field",
          "Tc"
        ],
        "units": {
          "density": "dimensionless",
          "field": "dimensionless (J)",
          "Tc": "J/k_B"
        }
      },
      "description": "CSV containing the phase diagram: critical temperature Tc (in units of J/k_B) for each density and field amplitude."
    }
  ],
  "notes": "The scored Tc values are compared against hidden gold values derived from the paper's CMF results. The checker verifies that for density ≈0.16 the Tc values for E=1 and E=10 are equal within tolerance (multicritical point evidence)."
}
```

## How you are scored
A hidden verifier loads your `phasediagram.csv` and validates its schema. It then compares each reported Tc against a set of expected values derived from the paper's CMF results. For each (density, field) point, your Tc is scored based on whether it lies within a specified tolerance of the expected value. Additionally, the verifier checks whether at a specific density your Tc values for E=1 and E=10 match within tolerance, which tests for a multicritical point. The final reward is the fraction of point comparisons that pass these checks.
