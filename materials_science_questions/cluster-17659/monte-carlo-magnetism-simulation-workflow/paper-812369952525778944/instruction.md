# Monte Carlo Simulation of Adaptive-Threshold Buyer Cellular Automaton

## Problem background
In many buyer‑dominated markets, individual purchasing decisions and quality expectations co‑evolve through social influence. When a potential buyer sees many peers buying, they are more likely to buy themselves; after a purchase, their personal threshold for future purchases may rise, and after abstention it may fall. This task investigates a minimal threshold cellular automaton that captures such a feedback loop. Agents are placed on a 2D square lattice, each with a randomly assigned personal threshold. Whether an agent buys depends on how many of its four neighbours are currently buying, compared to the agent’s own threshold. The aggregate market state is measured by the magnetization – the difference between the fraction of buyers and non-buyers, ranging from −1 to +1. Starting from an initial state where all agents are buyers, the dynamics unfolds through random sequential updates. The goal is to implement the model and compute (i) the time evolution of magnetization for a fixed lattice size when agents can re‑evaluate immediately after each update, (ii) how the amplitude of magnetization fluctuations depends on the total number of agents, and (iii) the time course of the buyer fraction when purchases are irreversible (buy‑once). All model rules, initial conditions, and required lattice sizes are given; the agent must produce these quantities from the simulation.

## Approach
The market is modelled as a square lattice of N agents, each carrying a binary state (buying = +1, not buying = −1) and a personal threshold. The threshold is drawn initially from the set of odd integers {−5,−3,−1,1,3,5}. In each update, an agent is chosen at random and the sum of its four nearest‑neighbour states is computed. If this sum strictly exceeds the agent’s current threshold, the agent buys (state +1); otherwise it does not buy (state −1). The threshold is then adjusted by ±2: it increases by 2 after a purchase and decreases by 2 after a non‑purchase, and is clipped to the range −5 to 5 so that it never leaves the allowed set. One time step consists of N such updates on average. The magnetization M(t) = ⟨S_i⟩, i.e. the average over all agents of their current state, is recorded at each time step. Two extreme operating regimes are explored:  τ = 0 (no refractory period – agents can reconsider immediately) and the irreversible “buy‑once” case where a site that has ever bought is permanently frozen in the buying state.  For τ = 0 the simulation is run until a steady state is reached (or at least 1000 time steps for L=100), and the time series is saved. To study the scaling of fluctuations, the τ=0 simulation is repeated for several lattice linear sizes. After discarding an initial transient, the standard deviation of M(t) in the stationary regime is computed for each size and recorded in a table.  For the irreversible case, the fraction of buyers (which can only decrease) is recorded over time until saturation. All simulations use a standard numeric library (NumPy) for array operations and random number generation.

## Reproduction target
Produce the following three artifacts and place them under `/app/outputs`:  

1. `magnetization_time_series_tau0_2D.csv` – a time series of magnetization M(t) for a 100×100 lattice with τ=0, recorded at each time step for at least 1000 steps or until stationarity.  
2. `fluctuation_scaling.csv` – a table with columns L (linear size) and std_magnetization (standard deviation of M in the stationary regime) for the sizes L ∈ {20, 30, 50, 100, 200} at τ=0.  
3. `irreversible_fraction_tau_inf.csv` – a time series of the buyer fraction for the irreversible (buy‑once) dynamics on a 100×100 lattice, recorded until the market is saturated or for a large number of time steps.  

The hidden verifier will examine these files for structural compliance (correct columns and data types) and will analyse statistical properties of the data. For example, it may inspect the magnetization time series for oscillatory behaviour, fit a power‑law model to the fluctuation scaling data, and perform a log‑transformed linear fit on the irreversible buyer fraction to assess the decay trend. Your output will be scored on how well these properties match the expected dynamics of the model. You do not need to match any pre‑specified numbers; instead, faithfully implement the model and simulation as described.

## Assets

- NumPy: numpy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Simulate base dynamics for τ=0, L=100
- Role: scored
- Action: Implement the inhomogeneous adaptive-threshold cellular automaton on a 2D square lattice (nearest neighbours) with L=100 and τ=0. Initialise all spins to +1, assign each site a random threshold from {−5,−3,−1,1,3,5}, and run random sequential updates (one time step = N updates on average) for at least 1000 time steps or until steady state. Record the magnetization M(t) = ⟨S_i⟩ at each time step and save the time series.
- Output file: `/app/outputs/magnetization_time_series_tau0_2D.csv`
- Format: csv
- Contract: Columns: time (integer), magnetization (float between -1 and 1)
- Scoring: scored by hidden verifier

### Step 2: Run lattice-size scans for τ=0
- Role: process
- Action: For linear sizes L ∈ {20, 30, 50, 200}, repeat the same model with τ=0, initial all spins up, random thresholds, and record the magnetization time series for each L until steady state (same number of time steps as L=100). These intermediate time series are required to compute fluctuation scaling in the next step but are not scored individually.
- Evidence: `/app/outputs/Intermediate time series files (e.g., magnetization_tau0_L20.csv, magnetization_tau0_L30.csv, magnetization_tau0_L50.csv, magnetization_tau0_L200.csv)`

### Step 3: Compute magnetization fluctuation scaling
- Role: scored (load-bearing)
- Action: From the time series for L ∈ {20, 30, 50, 100, 200} at τ=0 (using the L=100 series from step_01 and the others from step_02), discard a suitable initial transient (e.g., first 200 time steps) and compute the standard deviation of magnetization in the stationary regime for each L. Output a CSV table listing L and its corresponding σ(M).
- Output file: `/app/outputs/fluctuation_scaling.csv`
- Format: csv
- Contract: Columns: L (integer, linear size), std_magnetization (float, standard deviation of M)
- Scoring: scored by hidden verifier

### Step 4: Simulate irreversible (τ=∞) dynamics
- Role: scored
- Action: Implement the irreversible (buy-once) variant where once a site switches to +1 it never buys again. On a 2D square lattice with L=100, start all spins +1, random thresholds, and run the dynamics until the market is saturated (or for a large number of time steps). Record the fraction of buyers (magnetization) over time and save the time series.
- Output file: `/app/outputs/irreversible_fraction_tau_inf.csv`
- Format: csv
- Contract: Columns: time (integer), fraction_buyers (float between 0 and 1)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_time_series_tau0_2D.csv`
- `/app/outputs/fluctuation_scaling.csv`
- `/app/outputs/irreversible_fraction_tau_inf.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_time_series_tau0_2D.csv
- path: `/app/outputs/magnetization_time_series_tau0_2D.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetization time series for τ=0, L=100; checked for damped oscillation and steady-state mean.
- schema:
  - `type`: table
  - `required_columns`: `time`, `magnetization`

### fluctuation_scaling.csv
- path: `/app/outputs/fluctuation_scaling.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetization standard deviation vs. system size; checked for power-law scaling slope ≈ -1 and high R².
- schema:
  - `type`: table
  - `required_columns`: `L`, `std_magnetization`

### irreversible_fraction_tau_inf.csv
- path: `/app/outputs/irreversible_fraction_tau_inf.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Buyer fraction time series for τ=∞; checked for exponential decay after initial transient.
- schema:
  - `type`: table
  - `required_columns`: `time`, `fraction_buyers`

Notes: All outputs are CSV time series or summary tables. Scoring is structural: the verifier checks oscillations, steady-state mean, log-log scaling of fluctuations, and exponential decay. No gold numeric values are required in the task instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_time_series_tau0_2D.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "magnetization"
        ]
      },
      "description": "Magnetization time series for τ=0, L=100; checked for damped oscillation and steady-state mean."
    },
    {
      "file": "fluctuation_scaling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "std_magnetization"
        ]
      },
      "description": "Magnetization standard deviation vs. system size; checked for power-law scaling slope ≈ -1 and high R²."
    },
    {
      "file": "irreversible_fraction_tau_inf.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "fraction_buyers"
        ]
      },
      "description": "Buyer fraction time series for τ=∞; checked for exponential decay after initial transient."
    }
  ],
  "notes": "All outputs are CSV time series or summary tables. Scoring is structural: the verifier checks oscillations, steady-state mean, log-log scaling of fluctuations, and exponential decay. No gold numeric values are required in the task instruction."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that reads the artifact files from `/app/outputs` and performs a series of structural and statistical checks. For each scored artifact, the verifier first ensures the file conforms to the required format (columns, types). It then computes properties of the data that indicate whether the simulation reproduces the expected dynamical regime – for instance, testing for oscillatory patterns in the magnetization time series, fitting a log‑log power‑law model to the fluctuation scaling table, and analysing the decay trend of the buyer fraction after a logarithmic transformation. The checks are weighted, with greater weight placed on the most discriminative property. The final reward is a number between 0 and 1 (1 = best possible reproduction of the target dynamics). A score close to 1 means your simulation outputs exhibit the characteristic behaviour expected from the model’s rules; a score close to 0 means they do not. Simply printing a single reported number is not sufficient – the verifier examines the full data you provide. You do not need to look up the original paper; all required information is contained in this instruction.
