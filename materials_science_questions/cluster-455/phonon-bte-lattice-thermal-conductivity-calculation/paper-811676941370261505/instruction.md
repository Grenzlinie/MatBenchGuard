# Disorder-induced transport regime transition in a Sierpinski triangle lattice

## Problem background
Lattice dynamics in fractal geometries such as the Sierpinski triangle exhibit unusual vibrational modes known as fractons, which can lead to anomalous transport properties. When structural disorder is introduced, the nature of phonon transport changes, potentially transitioning from fracton-dominated regimes to extended phonon states and possibly to localized states. This task investigates how the level of bond-rewiring disorder affects phonon transmission and the spectral properties of a finite Sierpinski triangle lattice, using the atomistic Green's function formalism to compute transport quantities and characterize the transition through correlation dimensions and transmission sums.

## Approach
Construct a Sierpinski triangle lattice at self-similarity level 6. For each disorder probability p (0.0, 0.1, 0.2, 0.4, 0.6), apply Watts–Strogatz bond rewiring with probability p, avoiding self-connections and duplicates. Build the harmonic dynamical matrix with normalized spring-to-mass ratio k/m = 1. Using the atomistic Green’s function method, attach a monatomic linear chain phonon source and drain to 4 randomly chosen source points and compute the retarded Green’s function, the phonon transmission per point, and the average local density of states (ALDoS) over a chosen frequency grid. Average the transmission and ALDoS over the 4 source points to obtain the mean transmission function T(ω²) and mean ALDoS for each p. From these averaged arrays, compute the correlation dimension v of the ALDoS via the correlation sum C₂(ε) — the probability that the difference between ALDoS values at two frequencies is less than ε — and the total transmission sum by summing T(ω²) over all sampled frequency bins. The results for different disorder levels are saved and analyzed to reveal how transport properties change with disorder.

## Reproduction target
For a Sierpinski triangle lattice at self-similarity level 6, compute the correlation dimension v of the average local density of states and the total transmission sum for disorder levels p ∈ {0.0, 0.1, 0.2, 0.4, 0.6}. Save these values in two CSV files:
- `/app/outputs/correlation_dimension_level6.csv` with columns `p` (disorder probability) and `v` (correlation dimension).
- `/app/outputs/transmission_sum_level6.csv` with columns `p` and `transmission_sum` (summed T(ω²) over frequency).
The results must be computed from the averaged ALDoS and transmission curves obtained from an atomistic Green's function simulation. The relative trends across the disorder levels will be evaluated; no absolute tolerances are prescribed.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Simulate phonon transport for Sierpinski lattice at level 6
- Role: process
- Action: Construct a Sierpinski triangle lattice at self-similarity level 6. For each disorder probability p in {0.0, 0.1, 0.2, 0.4, 0.6}, apply Watts-Strogatz bond rewiring with probability p (avoid self-connections and duplicates). Build the harmonic dynamical matrix with normalized spring-to-mass ratio of 1. Use the atomistic Green's function formalism with monatomic linear chain surface self-energy to compute the retarded Green's function, the phonon transmission per point, and the average local density of states (ALDoS) over a chosen frequency grid. Average the transmission and ALDoS over 4 random source points to obtain the mean transmission function and mean ALDoS for each p. Save these averaged arrays for each disorder level to a single NumPy archive file simulation_data.npz.
- Evidence: `/app/outputs/simulation_data.npz`

### Step 2: Compute correlation dimension of ADOS
- Role: scored (load-bearing)
- Action: For each disorder level p, load the averaged ALDoS arrays from simulation_data.npz. Compute the correlation sum C₂(ε) as the probability that the difference between transmission values (or ALDoS) at two frequencies is less than ε. Estimate the correlation dimension v from the scaling region of log C₂(ε) vs log ε via linear fit. Output a CSV file with two columns: p and v.
- Output file: `/app/outputs/correlation_dimension_level6.csv`
- Format: csv
- Contract: Two columns: p (float, disorder probability) and v (float, correlation dimension). Rows for p = 0.0, 0.1, 0.2, 0.4, 0.6.
- Scoring: scored by hidden verifier

### Step 3: Compute total transmission sum
- Role: scored (load-bearing)
- Action: For each disorder level p, load the averaged transmission function T(ω²) from simulation_data.npz. Sum T(ω²) over all sampled frequency bins to obtain the transmission sum. Output a CSV file with two columns: p and transmission_sum.
- Output file: `/app/outputs/transmission_sum_level6.csv`
- Format: csv
- Contract: Two columns: p (float) and transmission_sum (float). Rows for p = 0.0, 0.1, 0.2, 0.4, 0.6.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/correlation_dimension_level6.csv`
- `/app/outputs/transmission_sum_level6.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### correlation_dimension_level6.csv
- path: `/app/outputs/correlation_dimension_level6.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Correlation dimension of the average density of states for each disorder level. The trend v(p=0.1) > v(p=0.2) > v(p=0.4) indicates the formation of extended phonon bands at low disorder and a statistical fractal regime at higher disorder.
- schema:
  - `type`: table
  - `required_columns`: `p`, `v`
  - `units`:
    - `p`: probability
    - `v`: dimensionless

### transmission_sum_level6.csv
- path: `/app/outputs/transmission_sum_level6.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total transmission sum over all sampled frequency bins for each disorder level. The transmission sum should be higher for p≤0.2 than for p>0.2, showing the transition from broad-band to low-frequency concentrated transport.
- schema:
  - `type`: table
  - `required_columns`: `p`, `transmission_sum`
  - `units`:
    - `p`: probability
    - `transmission_sum`: arbitrary units

Notes: The agent may choose the frequency grid, lead natural frequency ω₀, and other numerical settings. The scored trend does not depend on absolute values. No absolute tolerances are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "correlation_dimension_level6.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "v"
        ],
        "units": {
          "p": "probability",
          "v": "dimensionless"
        }
      },
      "description": "Correlation dimension of the average density of states for each disorder level. The trend v(p=0.1) > v(p=0.2) > v(p=0.4) indicates the formation of extended phonon bands at low disorder and a statistical fractal regime at higher disorder."
    },
    {
      "file": "transmission_sum_level6.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "transmission_sum"
        ],
        "units": {
          "p": "probability",
          "transmission_sum": "arbitrary units"
        }
      },
      "description": "Total transmission sum over all sampled frequency bins for each disorder level. The transmission sum should be higher for p≤0.2 than for p>0.2, showing the transition from broad-band to low-frequency concentrated transport."
    }
  ],
  "notes": "The agent may choose the frequency grid, lead natural frequency ω₀, and other numerical settings. The scored trend does not depend on absolute values. No absolute tolerances are required."
}
```

## How you are scored
A hidden verifier reads the two output CSV files and checks that they follow the specified format and that the values satisfy certain structural relationships (relative orderings among the disorder levels) consistent with the expected physical behavior. Each output file contributes a weighted portion to the final reward (e.g., 0.5 each), producing a float between 0.0 and 1.0. The verifier may also perform sanity checks on any supporting evidence. Simply writing numbers from the paper or arbitrary values will not pass; the submitted data must be the result of a genuine simulation following the described approach.
