# Ising Model Monte Carlo Simulations: Equilibrium Domains in Dense and Sparse Networks

## Problem background
Non-equilibrium systems, where detailed balance is absent, are common across physics, biology, and finance. It has been conjectured that equilibrium-like domains can emerge spontaneously within such systems, yet quantitative examples are rare. This task investigates the conditions under which a subsystem of an out-of-equilibrium Ising-like spin system behaves as if it were in thermal equilibrium, described by the same macroscopic observables (magnetization, average energy) as the corresponding isolated equilibrium system. Two exemplar model topologies are studied: a densely connected bipartite network where one part acts as a non‑equilibrium 'environment' while the other may show equilibrium behavior; and a sparsely connected ferromagnetic random regular graph where a fraction of spins experience random time‑dependent external fields, breaking global equilibrium, while the unperturbed bulk might retain equilibrium‑like properties.

## Approach
Two complementary models are simulated using Monte Carlo methods. The dense model (N=1000 spins, two subsystems σ and τ) evolves with parallel synchronous updates at several noise levels (inverse temperature β). The time series of the two subsystem magnetizations is recorded. The sparse model is an Ising ferromagnet (N=1,000,000, degree 3) on a random regular graph. Asynchronous Glauber dynamics is run at several temperatures, both without external perturbations and with random binary (±1) fields applied to 5% of the sites. For the unperturbed nodes, equilibrium reference values for energy and magnetization are computed from the self‑consistent cavity equations. The comparison between simulated observables and equilibrium theory, especially near the critical temperature, forms the core analysis.

## Reproduction target
Produce two output files under `/app/outputs`:
1. `dense_model_magnetizations.csv` – time series from the dense model simulation; columns `beta`, `time_step`, `m_sigma`, `m_tau`.
2. `sparse_model_results.csv` – one row per temperature containing `temperature`, `energy_sim`, `magnet_sim`, `energy_eq`, `magnet_eq`, `energy_pert_sim`, `magnet_pert_sim`.
The hidden evaluator will assess the simulated magnetizations and compare the sparse-model observables to independently computed theoretical references.

## Assets

- NumPy: numpy
- SciPy: scipy
- NetworkX: networkx

## Workflow steps

### Step 1: Dense model simulation
- Role: scored (load-bearing)
- Action: Implement the densely connected Ising model with N=1000, N_sigma=N_tau=500, J_sigma=J_sigma_tau=1, J_tau and J_tau_sigma random ±1/√N, parallel synchronous updates. Simulate for t=0..99 at beta ∈ {0.8, 1.0, 1.2} with zero external fields. Compute m_sigma(t) and m_tau(t) at each step.
- Output file: `/app/outputs/dense_model_magnetizations.csv`
- Format: csv
- Contract: columns: beta (float), time_step (int), m_sigma (float), m_tau (float). One row per time step per beta value.
- Scoring: scored by hidden verifier

### Step 2: Build random regular graph and perturbation mask
- Role: process
- Action: Generate a random regular graph of degree k=3 with N=10^6 nodes using the configuration model. Assign ferromagnetic interaction J=1. Randomly select 5% of nodes as perturbation mask.
- Evidence: none

### Step 3: Sparse model analysis
- Role: scored (load-bearing)
- Action: For the generated graph, run asynchronous Glauber dynamics without perturbations for temperatures T ∈ {0.5, 1.0, 1.5, 2.0, 2.5, 3.0}: thermalize at least 1000 sweeps, then measure average energy per edge and magnetization per spin over at least 1000 sweeps. Repeat with random binary external fields (±1) on perturbed nodes and measure observables only on unperturbed nodes. Compute theoretical equilibrium values using cavity equations. Write CSV with all columns.
- Output file: `/app/outputs/sparse_model_results.csv`
- Format: csv
- Contract: columns: temperature (float), energy_sim (float), magnet_sim (float), energy_eq (float), magnet_eq (float), energy_pert_sim (float), magnet_pert_sim (float). One row per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dense_model_magnetizations.csv`
- `/app/outputs/sparse_model_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dense_model_magnetizations.csv
- path: `/app/outputs/dense_model_magnetizations.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of the two subsystem magnetizations.
- schema:
  - `type`: table
  - `required_columns`: `beta`, `time_step`, `m_sigma`, `m_tau`

### sparse_model_results.csv
- path: `/app/outputs/sparse_model_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated energy and magnetization for unperturbed nodes, reference equilibrium values, and perturbed-node results.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `energy_sim`, `magnet_sim`, `energy_eq`, `magnet_eq`, `energy_pert_sim`, `magnet_pert_sim`

Notes: Scoring is based on the raw time series and result table.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dense_model_magnetizations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "beta",
          "time_step",
          "m_sigma",
          "m_tau"
        ]
      },
      "description": "Time series of the two subsystem magnetizations."
    },
    {
      "file": "sparse_model_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "energy_sim",
          "magnet_sim",
          "energy_eq",
          "magnet_eq",
          "energy_pert_sim",
          "magnet_pert_sim"
        ]
      },
      "description": "Simulated energy and magnetization for unperturbed nodes, reference equilibrium values, and perturbed-node results."
    }
  ],
  "notes": "Scoring is based on the raw time series and result table."
}
```

## How you are scored
A hidden automated verifier reads the two CSV files from `/app/outputs` and compares the simulated quantities to independently computed reference values. Each scored artifact contributes a weight to the final reward in [0,1]; the verifier does not require a single aggregate metric – it operates directly on your produced tables.
