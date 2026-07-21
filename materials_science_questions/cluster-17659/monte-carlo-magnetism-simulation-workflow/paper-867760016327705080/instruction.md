# Monte Carlo Simulation of Random-Field Ising Model for Domain Growth Metrics

## Problem background
Sociophysics studies urban segregation using physics models. One approach is to model two groups of people (e.g., rich and poor) as spins in an Ising model on a square lattice. The random-field Ising model adds a local random field to each site, representing cheap or expensive residences that favor one spin orientation over the other. The central question is how domain sizes—large connected patches of one group—evolve over time under different temperatures and field strengths. In this context, low temperature favors alignment with neighbors, while high temperature introduces noise; a strong local field can lock spins to the local housing price, potentially preventing large domains.

## Approach
We implement the two-dimensional spin‑½ random-field Ising model with Glauber single-spin-flip kinetics on a 500×500 square lattice. Each site carries a random field ±h (equally likely), and spins interact ferromagnetically with their four nearest neighbors. Starting from a random configuration with zero net magnetization, the system evolves for many Monte Carlo sweeps per site. The energy of a spin flip determines its acceptance probability, which depends on the local field and the neighbor configuration. We investigate three parameter regimes: low temperature T=2.0 with weak field h=0.1; low temperature T=2.0 with strong field h=0.9; and high temperature T=99.0 with weak field h=0.1. At several intermediate times, we identify connected clusters of same-spin sites using 4-neighbor connectivity and compute the fraction of spins in the largest cluster and the total number of clusters. These metrics measure domain sizes and allow a comparison of how thermal noise and price differences affect segregation.

## Reproduction target
Produce a CSV file, `domain_metrics.csv`, containing the computed largest_cluster_fraction and number_of_clusters for each of the three simulation regimes (T=2.0, h=0.1; T=2.0, h=0.9; T=99.0, h=0.1) at the Monte Carlo sweep counts 40, 400, 4000, and 40000. The file must have exactly 12 rows with columns: temperature, field, time, largest_cluster_fraction, number_of_clusters. The simulation should be correctly implemented; the resulting metrics will reflect the physical dynamics of the random-field Ising model under each condition.

## Assets

- Python scientific computing environment: numpy, scipy

## Workflow steps

### Step 1: Monte Carlo simulation of 2D random-field Ising model and domain metric computation
- Role: scored (load-bearing)
- Action: Implement the 2D spin-1/2 random-field Ising model on a 500×500 square lattice with Glauber single-spin-flip kinetics. Run three simulation conditions: (a) T=2.0, h=±0.1; (b) T=2.0, h=±0.9; (c) T=99.0, h=±0.1, each for 40,000 Monte Carlo sweeps per site, starting from random zero-magnetization spin configurations with random site fields (±h). At sweeps 40, 400, 4,000, and 40,000, compute from the current spin configuration the fraction of spins belonging to the largest connected cluster (using 4-neighbor connectivity) and the total number of connected clusters. Write the collected metrics to domain_metrics.csv.
- Output file: `/app/outputs/domain_metrics.csv`
- Format: csv
- Contract: CSV with header: temperature (float), field (float), time (int), largest_cluster_fraction (float), number_of_clusters (int); one row per (condition, time) pair.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/domain_metrics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### domain_metrics.csv
- path: `/app/outputs/domain_metrics.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Domain growth metrics from Monte Carlo simulations of the random-field Ising model. The checker verifies that the largest_cluster_fraction trends match qualitative expectations without requiring exact numeric match.
- schema:
  - `type`: table
  - `required_columns`:
    - `name`: temperature
    - `type`: float
    - `description`: Reduced temperature kBT/J
    - `name`: field
    - `type`: float
    - `description`: Random field magnitude h
    - `name`: time
    - `type`: int
    - `description`: Monte Carlo sweeps per site
    - `name`: largest_cluster_fraction
    - `type`: float
    - `description`: Fraction of spins in the largest connected cluster (4-neighbor)
    - `name`: number_of_clusters
    - `type`: int
    - `description`: Total number of connected clusters
  - `description`: Exactly 12 rows covering three conditions (T=2.0,h=0.1; T=2.0,h=0.9; T=99.0,h=0.1) and four time points (40,400,4000,40000).

Notes: The high-temperature condition (T=99.0, h=0.1) is a supporting validation; the main claim is assessed via the low-temperature comparisons. No gold values or tolerances are disclosed; the hidden checker uses structural thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "domain_metrics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          {
            "name": "temperature",
            "type": "float",
            "description": "Reduced temperature kBT/J"
          },
          {
            "name": "field",
            "type": "float",
            "description": "Random field magnitude h"
          },
          {
            "name": "time",
            "type": "int",
            "description": "Monte Carlo sweeps per site"
          },
          {
            "name": "largest_cluster_fraction",
            "type": "float",
            "description": "Fraction of spins in the largest connected cluster (4-neighbor)"
          },
          {
            "name": "number_of_clusters",
            "type": "int",
            "description": "Total number of connected clusters"
          }
        ],
        "description": "Exactly 12 rows covering three conditions (T=2.0,h=0.1; T=2.0,h=0.9; T=99.0,h=0.1) and four time points (40,400,4000,40000)."
      },
      "description": "Domain growth metrics from Monte Carlo simulations of the random-field Ising model. The checker verifies that the largest_cluster_fraction trends match qualitative expectations without requiring exact numeric match."
    }
  ],
  "notes": "The high-temperature condition (T=99.0, h=0.1) is a supporting validation; the main claim is assessed via the low-temperature comparisons. No gold values or tolerances are disclosed; the hidden checker uses structural thresholds."
}
```

## How you are scored
A hidden verifier reads `domain_metrics.csv` and checks that the simulated domain-growth behavior under the three parameter regimes aligns with the expected physics. It uses internal thresholds on the largest_cluster_fraction and its trend over time; no exact numeric match is required. The verifier may also validate the file format and row count. Scoring is per‑regime, weighted equally, and combined into a final reward. The evaluation does not depend on matching any externally reported numbers — it only judges whether your simulation produces physically consistent results.
