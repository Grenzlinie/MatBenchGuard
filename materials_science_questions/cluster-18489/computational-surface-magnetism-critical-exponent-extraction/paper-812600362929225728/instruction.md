# Finite-size scaling of specific heat and magnetization in a Heisenberg multilayer model

## Problem background
Magnetic multilayers made of alternating transition-metal (A) and rare-earth (B) layers with antiferromagnetic interface coupling exhibit complex thermal behavior. Monte Carlo simulations of a classical Heisenberg model can probe finite-size effects on the specific heat and magnetization of such a multilayer. The specific heat may show two peaks; finite-size scaling of these peaks with the in-plane size L can distinguish true thermodynamic phase transitions from short-range order fluctuations. In addition, the magnetization may display a compensation point where the net magnetization vanishes, provided the system is large enough. This task aims to reproduce these finite-size trends by simulating the model and analyzing the resulting specific heat C(T) and magnetization m(T) for different L and boundary conditions.

## Approach
Model the multilayer as a stack of P alternating A and B ferromagnetic layers, each consisting of four atomic planes of L×L classical Heisenberg spins on a simple cubic lattice. The exchange interactions are J_AA=780 K (A–A), J_BB=18 K (B–B), and J_AB=-200 K (A–B at interfaces). Use the Metropolis Monte Carlo algorithm with a standard importance-sampling protocol: equilibrate for 2 000 Monte Carlo steps (MCS) per temperature, then collect data over 78 000 production MCS. Compute the specific heat per atom from energy fluctuations, C = (⟨E²⟩ − ⟨E⟩²)/(N k_B T²), and the magnetization per atom from the root-mean-square of the total magnetic moment vector, averaging over MCS. To reduce statistical noise, average each quantity over three independent runs with different random seeds. Perform simulations for three configurations: (1) L = 6, P = 4, free boundary conditions along the stacking direction; (2) L = 24, P = 4, free boundary conditions; (3) L = 24, P = 2, periodic boundary conditions. Sweep temperature from 100 K to 1100 K with steps no larger than 10 K. Output the raw C(T) and m(T) data for all configurations into a single CSV file.

## Reproduction target
Produce the file simulation_results.csv containing the Monte Carlo simulation results for the Heisenberg multilayer model with the given exchange parameters (J_AA=780 K, J_BB=18 K, J_AB=-200 K). The CSV must include data for the three conditions: (L=6, P=4, free BC), (L=24, P=4, free BC), and (L=24, P=2, periodic BC). Each row provides temperature T (K), specific heat per atom C (in units of k_B), and magnetization per atom m (in μ_B). The data should be of sufficient accuracy and temperature resolution to resolve two distinct specific-heat peaks—one at lower temperature (associated with B layers) and one at higher temperature (associated with A layers)—and to allow analysis of finite-size scaling: the high-temperature peak should become higher and narrower as L increases from 6 to 24, while the low-temperature peak should remain nearly unchanged. Additionally, for L=24 the magnetization should exhibit a compensation point whose temperature depends on the boundary conditions. The hidden verifier will analyze this CSV to verify those trends and to assess whether the extracted peak positions and compensation temperatures match the expected values.

## Assets

- Python 3: https://www.python.org/
- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Monte Carlo simulation of Heisenberg multilayer
- Role: scored (load-bearing)
- Action: Implement a classical Heisenberg spin model with exchange parameters J_AA=780 K, J_BB=18 K, J_AB=-200 K on a simple cubic lattice. The stack consists of alternating A and B layers; each layer has four atomic planes of L×L spins. Use the Metropolis Monte Carlo algorithm with 2000 equilibration MCS and 78000 production MCS per temperature. Compute specific heat per atom from energy fluctuations: C = (⟨E²⟩ − ⟨E⟩²) / (N k_B T²). Compute magnetization per atom as m = (1/N) sqrt(⟨|∑ m_x|⟩² + ⟨|∑ m_y|⟩² + ⟨|∑ m_z|⟩²). Average over 3 independent runs with different random seeds. Perform simulations for three configurations: (L=6, P=4, free BC), (L=24, P=4, free BC), (L=24, P=2, periodic BC). Sweep temperature from 100 K to 1100 K with steps of at most 10 K. Write the results to simulation_results.csv.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: Columns: L (int), P (int), boundary (string, 'free' or 'periodic'), T (float, K), C (float, specific heat per atom in units of k_B), m (float, magnetization per atom in μ_B). Each row is one temperature point for one configuration.
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
- target_policy: metric_recompute
- description: Raw Monte Carlo simulation output: specific heat C(T) and magnetization m(T) for three configurations (L=6 free, L=24 free, L=24 periodic). The checker recomputes specific-heat peak locations, heights, widths, and compensation temperatures from this data to assess finite-size scaling and compensation behavior.
- schema:
  - `type`: table
  - `required_columns`: `L`, `P`, `boundary`, `T`, `C`, `m`
  - `units`:
    - `T`: K
    - `C`:  (units of k_B)
    - `m`: μ_B

Notes: The agent must produce a CSV with at least the three required configurations, covering the temperature range 100–1100 K with increments ≤10 K. The checker will read this file, detect peaks, and compare extracted quantities to the paper's expected trends and values.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "P",
          "boundary",
          "T",
          "C",
          "m"
        ],
        "units": {
          "T": "K",
          "C": " (units of k_B)",
          "m": "μ_B"
        }
      },
      "description": "Raw Monte Carlo simulation output: specific heat C(T) and magnetization m(T) for three configurations (L=6 free, L=24 free, L=24 periodic). The checker recomputes specific-heat peak locations, heights, widths, and compensation temperatures from this data to assess finite-size scaling and compensation behavior."
    }
  ],
  "notes": "The agent must produce a CSV with at least the three required configurations, covering the temperature range 100–1100 K with increments ≤10 K. The checker will read this file, detect peaks, and compare extracted quantities to the paper's expected trends and values."
}
```

## How you are scored
A hidden verifier reads your simulation_results.csv after the task finishes. It independently detects the two specific-heat peaks (low-temperature and high-temperature) for each configuration and computes their location, peak height, and peak width. It then checks the finite-size trends: whether the high-temperature peak height increases and its width decreases when going from L=6 to L=24 (free BC), while the low-temperature peak height and location differ by less than a specified tolerance. It also finds any compensation point in the magnetization (temperature of minimum total magnetization) for the L=24 configurations and compares its value to hidden reference temperatures. The verifier scores your data based on how well these extracted quantities and trends agree with the expected ones, using tolerance-based thresholds. Better agreement yields a higher reward. The score is a weighted combination of the checks for all configurations. Reporting pre‑computed numbers without running a genuine simulation will fail these checks.
