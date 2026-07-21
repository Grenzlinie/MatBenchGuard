# Monte Carlo Magnetization Fluctuations in the 2D XY Model

## Problem background
The two-dimensional XY model exhibits a low-temperature phase where correlations decay as a power law. In this regime, the thermodynamic magnetization is zero, but finite systems show measurable magnetization due to unusually large finite‑size corrections. Spin‑wave theory gives quantitative predictions for the mean magnetization and susceptibility as functions of the system size N and temperature T. Furthermore, the scaled probability distribution of the magnetization is expected to be universal—the standardized higher moments should be independent of N and T. The goal is to reproduce these features by performing Monte Carlo simulations of the harmonic XY model and reporting the mean magnetization, susceptibility, and standardized moments.

## Approach
Implement a Monte Carlo simulation of the harmonic XY model on a square lattice with periodic boundary conditions. The energy of a configuration is

E = -J ∑_{⟨i,j⟩} [1 − ½ (θ_i − θ_j − 2π n_ij)²]

where n_ij ∈ {0, ±1} is chosen so that (θ_i − θ_j − 2π n_ij) ∈ (-π, π], and the sum runs over all nearest-neighbour pairs. The scalar instantaneous magnetization is

M = (1/N) √[(∑_i cosθ_i)² + (∑_i sinθ_i)²].

Spin configurations are updated using standard Monte Carlo moves. After equilibration, record the time series of M. From this time series compute the mean magnetization ⟨M⟩, the susceptibility per spin χ = (N/T)(⟨M²⟩ − ⟨M⟩²), and the standardized moments ⟨z⁴⟩ and ⟨z⁶⟩ where z = (M − ⟨M⟩)/σ and σ = √(⟨M²⟩ − ⟨M⟩²). Run simulations for system sizes N = 100, 1024, 10000 (L = 10, 32, 100) at temperatures T/J = 0.5 and 1.0. The constancy of the standardized moments across these conditions tests the predicted universal distribution.

## Reproduction target
Implement a Monte Carlo simulation of the harmonic XY model and run it for N = 100, 1024, 10000 (L = 10, 32, 100) at T/J = 0.5 and 1.0. For each condition compute the mean magnetization ⟨M⟩, the susceptibility per spin χ, and the standardized moments ⟨z⁴⟩ and ⟨z⁶⟩. Output a single CSV file `/app/outputs/simulation_results.csv` with six rows (one per condition) and columns N, T_J, M_mean, chi, z4, z6. The goal is to obtain values that are consistent with spin‑wave theory and that show approximately constant standardized moments across all conditions, demonstrating universality.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Monte Carlo simulation and magnetization analysis
- Role: scored (load-bearing)
- Action: Implement a Monte Carlo simulation of the harmonic XY model on a square lattice of side L with periodic boundary conditions. For system sizes N = L² (L = 10, 32, 100) and temperatures T/J = 0.5 and 1.0, accumulate the scalar magnetization M after equilibration. From the resulting time series compute the mean magnetization ⟨M⟩, the susceptibility per spin χ = (N/T)(⟨M²⟩ − ⟨M⟩²), and the standardized moments ⟨z⁴⟩ and ⟨z⁶⟩ where z = (M − ⟨M⟩)/σ and σ = √(⟨M²⟩ − ⟨M⟩²). Save the six rows (one per condition) with columns N (integer), T_J (float), M_mean (float), chi (float), z4 (float), z6 (float).
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: CSV with columns: N (integer, system size), T_J (float, temperature in units of J), M_mean (float, mean magnetization), chi (float, susceptibility per spin), z4 (float, standardized 4th moment), z6 (float, standardized 6th moment). All numeric values are dimensionless or in units of the Hamiltonian; no physical units are attached. Each row corresponds to one (N, T_J) condition.
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
- description: The checker reads this CSV and compares the reported ⟨M⟩ and χ to the paper's analytical spin-wave predictions (hidden) with a relative tolerance. It additionally checks that the standardized moments ⟨z⁴⟩ and ⟨z⁶⟩ are approximately constant across all conditions (maximum deviation from the cross-condition mean is below a hidden threshold). Satisfying these checks demonstrates that the agent's simulation reproduces the spin-wave behavior and the universality of the scaled magnetization distribution.
- schema:
  - `type`: table
  - `required_columns`: `N`, `T_J`, `M_mean`, `chi`, `z4`, `z6`
  - `units`: object

Notes: The agent must simulate the harmonic XY model exactly as described; the checker uses the spin-wave formulas and the constancy of standardized moments as the hidden ground truth. No additional artifact is required.

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
          "N",
          "T_J",
          "M_mean",
          "chi",
          "z4",
          "z6"
        ],
        "units": {}
      },
      "description": "The checker reads this CSV and compares the reported ⟨M⟩ and χ to the paper's analytical spin-wave predictions (hidden) with a relative tolerance. It additionally checks that the standardized moments ⟨z⁴⟩ and ⟨z⁶⟩ are approximately constant across all conditions (maximum deviation from the cross-condition mean is below a hidden threshold). Satisfying these checks demonstrates that the agent's simulation reproduces the spin-wave behavior and the universality of the scaled magnetization distribution."
    }
  ],
  "notes": "The agent must simulate the harmonic XY model exactly as described; the checker uses the spin-wave formulas and the constancy of standardized moments as the hidden ground truth. No additional artifact is required."
}
```

## How you are scored
A hidden verifier reads your `simulation_results.csv` and scores the reported quantities. The main check compares your reported ⟨M⟩ and χ against the analytical spin‑wave predictions. Those predictions are not disclosed to you; the verifier computes them from your reported N and T using hidden formulas and allows a tolerance that accounts for normal statistical and implementation variation. A second check evaluates the constancy of the standardized moments ⟨z⁴⟩ and ⟨z⁶⟩ across all six conditions: they should be approximately independent of N and T. The two checks are combined into a single reward between 0 and 1. Partial credit is awarded for partially correct results. You must produce the CSV file exactly as specified; reporting a number without executing the genuine simulation will not satisfy the verifier.
