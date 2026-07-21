# Off-lattice Potts Model Monte Carlo Phase Transition Simulation

## Problem background
The off-lattice Potts model is a statistical-mechanical model of interacting agents whose manifest opinions and internal beliefs can differ. Agents move freely in a periodic square box and interact via short-range coupling when closer than a cutoff distance. The model undergoes a first-order phase transition that separates a low-energy clustered phase from a high-energy dispersed phase, with intermediate metastable states that are inaccessible in the canonical ensemble. Studying the caloric curves and the dynamics of this model reveals how multistability and negative heat capacity can appear even in systems with short-range interactions. In this task, you will implement the model and perform Monte Carlo simulations to explore its thermodynamic behavior and the phenomenon of multiple metastable states near the phase transition.

## Approach
The core idea is to simulate the off-lattice Q=2 Potts model in both the canonical and microcanonical ensembles using the Metropolis Monte Carlo method. The system consists of N=100 agents, each with a manifest spin S_i ∈ {0,1} and a fixed internal belief B_i ∈ {0,1}. The potential energy Φ is given by

Φ = -0.5 (J/C) Σ_i Σ_{j≠i} δ(S_i,S_j) Θ(R_c – r_{ij}) - 2 Σ_i δ(S_i,B_i)

with C=1, J/C=0.6, cutoff R_c=6.708, and a square simulation box of side L=111.8 under periodic boundary conditions.

Monte Carlo moves are chosen as follows: with probability p_s=0.1, a randomly selected agent flips its spin; otherwise, a randomly selected agent attempts a small random displacement. In the canonical ensemble, trial moves are accepted with probability min(1, exp(-β ΔΦ)), where β = 1/T. In the microcanonical ensemble, trial moves are accepted with probability min(1, [(E – Φ′)/(E – Φ)]^{N–1}) at fixed total energy E. The microcanonical temperature at a given energy is estimated as T(E) = ⟨ N/(E – Φ) ⟩_E.

You will run three simulation stages:
1. Canonical scans over a range of temperatures that cover the phase transition. At each temperature compute the average potential energy ⟨Φ⟩.
2. Microcanonical scans over a range of total energies that include the transition region. At each energy compute the microcanonical temperature.
3. A long microcanonical trace at a fixed total energy E = 3.006125, recording the instantaneous potential energy at every Monte Carlo step to capture the switching dynamics between metastable states.

The results from these three stages form the scored artifacts; no pre-computed data or external training is required.

## Reproduction target
The reproduction target is a quantitative exploration of the first-order phase transition and metastability of the off-lattice Potts model, as captured by three raw data files:

- `canonical_caloric.csv`: The canonical caloric curve, containing the average potential energy ⟨Φ⟩ as a function of temperature. The curve should exhibit a steep change in energy over a narrow temperature interval, characteristic of a first-order phase transition.
- `microcanonical_caloric.csv`: The microcanonical caloric curve, containing the estimated temperature T(E) as a function of total energy E. This curve should contain a region where the temperature decreases with increasing energy (negative heat capacity), indicating the presence of metastable states that are forbidden in the canonical ensemble.
- `trace_E_3_006125.csv`: A time series of the potential energy Φ at a fixed total energy E = 3.006125, recorded at each Monte Carlo step for at least 1,000,000 steps. The distribution of Φ over this trace should be bimodal, demonstrating that the system switches between two distinct metastable energy levels.

The specific temperatures, energies, and exact values are not provided; the hidden verifier will check that your submitted files contain the correct qualitative and quantitative features with reference to the expected physical behavior of the model. Your task is to produce these files by faithfully implementing the model and running the simulations — simply reporting numbers will not suffice.

## Assets

- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Implement off-lattice Potts model and MC methods
- Role: process
- Action: Write and test Python code that implements the off-lattice Potts model. The code must define: (1) the Hamiltonian potential energy Φ = -0.5*(J/C) Σ_i Σ_{j≠i} δ(S_i,S_j) Θ(Rc – r_ij) – 2 Σ_i δ(S_i, B_i), with C=1, J/C=0.6, Q=2, N=100, square box L=111.8, cutoff Rc=6.708, periodic boundary conditions; (2) trial moves: with probability p_s=0.1 pick a random agent and flip its spin, otherwise pick a random agent and attempt a small random displacement; (3) canonical Metropolis acceptance prob = min(1, exp(-β ΔΦ)); (4) microcanonical acceptance prob = min(1, [(E–Φ′)/(E–Φ)]^(N–1)). The implementation should be reusable for the subsequent simulation steps.
- Evidence: `/app/outputs/model_code.py`

### Step 2: Canonical ensemble Monte Carlo simulation
- Role: scored (load-bearing)
- Action: Using the implemented model, run canonical Metropolis Monte Carlo simulations at a set of temperatures spanning the first-order transition (e.g., from ~5 to ~25, with fine resolution near the transition). At each temperature, after sufficient equilibration, compute the ensemble average of the potential energy Φ and write one row per temperature to canonical_caloric.csv.
- Output file: `/app/outputs/canonical_caloric.csv`
- Format: csv
- Contract: Two columns: 'temperature' (float) and 'avg_potential_energy' (float). Header required. One row per simulated temperature.
- Scoring: scored by hidden verifier

### Step 3: Microcanonical ensemble Monte Carlo simulation
- Role: scored (load-bearing)
- Action: Using the implemented model, run microcanonical Metropolis Monte Carlo simulations (Ray's version) at a set of total energies E spanning the expected metastable region (e.g., from about -60 to 40, with fine steps in the V-shaped region). At each energy, compute the microcanonical temperature estimator T(E) = ⟨ N/(E-Φ) ⟩_E and write one row per energy to microcanonical_caloric.csv.
- Output file: `/app/outputs/microcanonical_caloric.csv`
- Format: csv
- Contract: Two columns: 'total_energy' (float) and 'temperature' (float). Header required. One row per simulated total energy.
- Scoring: scored by hidden verifier

### Step 4: Microcanonical trace at fixed energy
- Role: scored (load-bearing)
- Action: Run a microcanonical Monte Carlo simulation at the single total energy E = 3.006125 for at least 1,000,000 Monte Carlo steps. At each step record the potential energy Φ (the instant value after the trial move) and write the complete time series to trace_E_3_006125.csv.
- Output file: `/app/outputs/trace_E_3_006125.csv`
- Format: csv
- Contract: Two columns: 'step' (int) and 'potential_energy' (float). Header required. At least 1,000,000 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/canonical_caloric.csv`
- `/app/outputs/microcanonical_caloric.csv`
- `/app/outputs/trace_E_3_006125.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### canonical_caloric.csv
- path: `/app/outputs/canonical_caloric.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Canonical caloric curve data. The checker will recompute derived quantities (e.g., temperature of steepest jump, low-temperature energy) and compare against hidden paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `avg_potential_energy`

### microcanonical_caloric.csv
- path: `/app/outputs/microcanonical_caloric.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Microcanonical caloric curve data. The checker will verify the existence and boundaries of a negative specific heat region (where dT/dE < 0).
- schema:
  - `type`: table
  - `required_columns`: `total_energy`, `temperature`

### trace_E_3_006125.csv
- path: `/app/outputs/trace_E_3_006125.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series at fixed energy. The checker will compute a histogram of potential energy and verify a bimodal distribution with two well-separated peaks.
- schema:
  - `type`: table
  - `required_columns`: `step`, `potential_energy`

Notes: All output files are CSV with a header row. The checker will recompute structural features from the raw data, not trust self-reported metrics. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "canonical_caloric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "avg_potential_energy"
        ]
      },
      "description": "Canonical caloric curve data. The checker will recompute derived quantities (e.g., temperature of steepest jump, low-temperature energy) and compare against hidden paper-reported values."
    },
    {
      "file": "microcanonical_caloric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "total_energy",
          "temperature"
        ]
      },
      "description": "Microcanonical caloric curve data. The checker will verify the existence and boundaries of a negative specific heat region (where dT/dE < 0)."
    },
    {
      "file": "trace_E_3_006125.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "step",
          "potential_energy"
        ]
      },
      "description": "Time series at fixed energy. The checker will compute a histogram of potential energy and verify a bimodal distribution with two well-separated peaks."
    }
  ],
  "notes": "All output files are CSV with a header row. The checker will recompute structural features from the raw data, not trust self-reported metrics. No gold values or tolerances are disclosed here."
}
```

## How you are scored
Each of the three required output files is scored independently by a hidden verifier. For `canonical_caloric.csv`, the verifier will automatically identify the temperature at which the average potential energy changes most rapidly and check it against a hidden reference interval; it will also verify that the low-temperature energy is in the expected range. For `microcanonical_caloric.csv`, the verifier will detect the presence of a negative-slope region in the T(E) curve and compare the energy boundaries of that region to hidden reference values. For `trace_E_3_006125.csv`, the verifier will compute the histogram of Φ and verify that it has at least two distinct peaks with sufficient separation and mass, consistent with bimodal switching.

The scores from these three checks are combined with predefined weights (the canonical and microcanonical curves each carry substantial weight, and the trace analysis carries the remainder) to produce a final reward between 0 and 1. The hidden thresholds and tolerances are derived from the published reference results; they are not disclosed in this instruction. To earn a high score you must actually run the full simulations — a simplistic or approximate solution, or one that reports plausible numbers without proper Monte Carlo sampling, will not pass the detailed structural checks.
