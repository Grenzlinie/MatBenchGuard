# Kinetic Monte Carlo Surface Growth Simulation

## Problem background
In the sol-gel synthesis of silica colloids from partially hydrolysed tetraethoxysilane (TEOS), the water-to-TEOS molar ratio \(W\) controls the hydrolysis extent and, consequently, the morphology of the resulting clusters. Small-angle scattering experiments show a striking crossover from mass fractal to surface fractal structures as \(W\) increases. Understanding this structural transition is important for controlling ceramic precursors and other materials with tunable porosity and surface roughness.

This task investigates a modified Eden growth model that incorporates the chemical reality of incomplete monomer hydrolysis to reproduce the experimentally observed scattering behaviour and the crossover. In this model, monomers have a number of unhydrolysed ('poisoned') sites that cannot mediate polymerization, and the cluster grows by one-particle nucleation on a tetragonal lattice. The goal is to simulate cluster growth for several functionality distributions that correspond to different \(W\) regimes, compute the scattering structure factor \(S(k)\), extract the power-law exponent \(\alpha\), and derive an analytical relationship linking the mean monomer functionality \(\langle n \rangle\) to \(W\).

## Approach
The model uses a face-centred cubic lattice with a two-point basis, yielding coordination 4 and mimicking the local tetrahedral geometry of silicon. Growth proceeds by repeatedly selecting a monomer from a given functionality distribution (the proportions of tetra-, tri-, di-, and mono-functional sites) and attaching it to an available surface site. A geometric acceptance rule ensures that a site can accept a monomer only if it has at least as many vacant/growth adjacent sites as the monomer has poisoned sites; the poisoned sites are then placed randomly among those neighbours, and the remaining unfilled neighbours become new growth sites. This rule prevents unphysical double-occupancy and results in clusters with internal porosity that depends on the monomer distribution.

The computational pipeline consists of four stages. First, clusters containing \(5\times10^4\) monomers are grown for each of the specified functionality distributions, with 100 independent realizations per distribution. Second, the circularly averaged static structure factor \(S(k)\) is computed from the final cluster configurations. Third, a power-law fit \(S(k) \sim k^{-\alpha}\) is performed on the large-\(k\) tail to extract the scattering exponent \(\alpha\). Finally, a probabilistic model of hydrolysis is used to derive an algebraic relation between the mean functionality \(\langle n \rangle\) and the water ratio \(W\), with a hydrolysis capacity parameter \(\varepsilon\) calibrated to match the experimental slope at \(W=1\). The agent must compute \(\langle n \rangle\) for \(W=1,2,3,4\) using \(\varepsilon=5\).

## Reproduction target
Produce three scored artifacts: (i) `Sk_curves.csv` containing the circularly averaged \(S(k)\) for all distributions; (ii) `alpha_distributions.csv` reporting the fitted \(\alpha\) and its standard error for each distribution; and (iii) `analytical_relation.csv` giving \(\langle n \rangle\) for \(W=1..4\) obtained from the probabilistic model with \(\varepsilon=5\). The primary objective is to obtain \(\alpha\) values that are consistent with mass-fractal or surface-fractal signatures: distributions with low mean functionality should yield \(\alpha < 3\) (mass fractal), while those with high mean functionality should yield \(\alpha > 3\) (surface fractal). The analytical relation should yield physically sensible mean functionalities that increase with \(W\).

## Assets

- Python 3 with NumPy, SciPy: numpy scipy

## Workflow steps

### Step 1: Simulate cluster growth (modified Eden model)
- Role: process
- Action: Implement the modified Eden model on a tetragonal lattice (FCC with two-point basis, coordination 4, cubic cell L=64) with monomer-specific poisoning. For each specified functionality distribution — (1:0:0:0), (3:3:3:1), (0:1:1:0), (2:0:1:0) — grow clusters by repeatedly selecting monomers from the distribution and attaching them to available growth sites according to the geometric acceptance criterion until 5×10⁴ monomers have been added. Discard dead clusters and restart to obtain 100 independent realizations per distribution.

### Step 2: Compute circularly averaged structure factor S(k)
- Role: scored (load-bearing)
- Action: For each distribution and each realization, compute the static structure factor \(S(k)\) from the final cluster configuration.
  
  **Definition of the structure factor**
  For a single realization, define the density field \(v(\mathbf{r})\) on the cubic lattice (\(L=64\) grid points) as:
  
  \[
  v(\mathbf{r}) = \begin{cases}
  1 & \text{if the lattice vertex } \mathbf{r} \text{ is occupied by a monomer}, \\
  0 & \text{otherwise}.
  \end{cases}
  \]
  
  The structure factor is given by Equation (1) of the reference study:
  
  \[
  S(\mathbf{k}) = \frac{1}{N} \sum_{\mathbf{r}} \sum_{\mathbf{r'}} \bigl[ v(\mathbf{r}+\mathbf{r'}) v(\mathbf{r'}) - \langle v\rangle^2 \bigr] e^{\mathrm{i}\,\mathbf{k}\cdot\mathbf{r}},
  \]
  
  where \(N = L^3 = 64^3\), \(\langle v\rangle = \frac{1}{N}\sum_{\mathbf{r}} v(\mathbf{r})\) is the mean density, and the sums run over all lattice vertices with periodic boundary conditions.
  
  **Circular averaging**
  Compute \(S(\mathbf{k})\) on a grid of reciprocal‑space vectors. Because the aggregates are isotropic, average over all directions of \(\mathbf{k}\) with the same magnitude \(k = |\mathbf{k}|\) to obtain \(S(k)\) as a function of the scalar wavenumber.
  
  **Ensemble averaging**
  Repeat this calculation for each of the 100 independent realizations and average the resulting \(S(k)\) curves together. The final ensemble‑averaged curves should be written to `Sk_curves.csv`.
  
  To adequately resolve the high‑\(k\) (large‑\(k\)) power‑law tail, evaluate \(S(k)\) at a set of logarithmically spaced \(k\) values, for example 60 points between \(k = 0.05\) and \(k = 1.0\).

- Output file: `/app/outputs/Sk_curves.csv`
- Format: csv
- Contract: Columns: distribution (str), k (float), S (float). One row per (distribution, k) point. Data should cover a sufficient range of k to include the large‑k power‑law regime.
- Scoring: scored by hidden verifier

### Step 3: Extract scattering exponent α
- Role: scored
- Action: Fit a power law \(S(k) \sim k^{-\alpha}\) to the large‑k portion of each averaged \(S(k)\) curve. Following the procedure described in the reference study, take the highest‑\(k\) region (e.g., the last 20% of the \(k\)‑points) and perform a linear least‑squares fit to \(\log S(k)\) versus \(\log k\). The scattering exponent is \(\alpha = -\,\text{slope}\) of the fitted line. Report the fitted \(\alpha\) and its standard error (the standard error of the slope) in `alpha_distributions.csv`.
- Output file: `/app/outputs/alpha_distributions.csv`
- Format: csv
- Contract: Columns: distribution (str), alpha (float), alpha_error (float). One row per specified functionality distribution.
- Scoring: scored by hidden verifier

### Step 4: Derive analytical mean functionality relation
- Role: scored
- Action: Derive the mean monomer functionality \(\langle n \rangle\) as a function of the water ratio \(W\) from a probabilistic model of incomplete hydrolysis. Consider that a site on a silica monomer is hydrolysed with a probability proportional to \(W\), and remains unhydrolysed (poisoned) with a probability proportional to \(1/\varepsilon\), where \(\varepsilon=5\) is a hydrolysis capacity constant. After normalization for sites actually found in the aggregate, obtain an expression linking \(\langle n \rangle\), \(W\), and \(\varepsilon\). Compute \(\langle n \rangle\) for \(W = 1, 2, 3, 4\) using \(\varepsilon=5\).
- Output file: `/app/outputs/analytical_relation.csv`
- Format: csv
- Contract: Columns: W (int, 1..4), mean_n (float). One row per W.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Sk_curves.csv`
- `/app/outputs/alpha_distributions.csv`
- `/app/outputs/analytical_relation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Sk_curves.csv
- path: `/app/outputs/Sk_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Circularly averaged structure factor S(k) for each functionality distribution. The checker will recompute the power-law exponent α from this file and score against hidden gold.
- schema:
  - `type`: table
  - `required_columns`: `distribution`, `k`, `S`
  - `units`:
    - `k`: arbitrary
    - `S`: arbitrary intensity

### alpha_distributions.csv
- path: `/app/outputs/alpha_distributions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Agent-reported scattering exponent α and its standard error for each distribution. The checker will compare these to hidden gold values from the reference study.
- schema:
  - `type`: table
  - `required_columns`: `distribution`, `alpha`, `alpha_error`
  - `units`:
    - `alpha`: dimensionless
    - `alpha_error`: dimensionless

### analytical_relation.csv
- path: `/app/outputs/analytical_relation.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mean functionality ⟨n⟩ computed from the analytical formula for W=1,2,3,4 using ε=5. Values are exact and will be checked against precomputed gold.
- schema:
  - `type`: table
  - `required_columns`: `W`, `mean_n`
  - `units`:
    - `W`: molar ratio
    - `mean_n`: dimensionless

Notes: The Sk_curves.csv file is the primary recomputed artifact driving the main scoring; the checker will independently fit α from this raw data. The alpha_distributions.csv file provides a self-consistency check between the agent's own fit and the recomputed α.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Sk_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "distribution",
          "k",
          "S"
        ],
        "units": {
          "k": "arbitrary",
          "S": "arbitrary intensity"
        }
      },
      "description": "Circularly averaged structure factor S(k) for each functionality distribution. The checker will recompute the power-law exponent α from this file and score against hidden gold."
    },
    {
      "file": "alpha_distributions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "distribution",
          "alpha",
          "alpha_error"
        ],
        "units": {
          "alpha": "dimensionless",
          "alpha_error": "dimensionless"
        }
      },
      "description": "Agent-reported scattering exponent α and its standard error for each distribution. The checker will compare these to hidden gold values from the reference study."
    },
    {
      "file": "analytical_relation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "W",
          "mean_n"
        ],
        "units": {
          "W": "molar ratio",
          "mean_n": "dimensionless"
        }
      },
      "description": "Mean functionality ⟨n⟩ computed from the analytical formula for W=1,2,3,4 using ε=5. Values are exact and will be checked against precomputed gold."
    }
  ],
  "notes": "The Sk_curves.csv file is the primary recomputed artifact driving the main scoring; the checker will independently fit α from this raw data. The alpha_distributions.csv file provides a self-consistency check between the agent's own fit and the recomputed α."
}
```

## How you are scored
Each artifact will be checked by an automated verifier. The raw \(S(k)\) curves are the load-bearing artifact: the verifier will independently extract the power-law exponent \(\alpha\) from your submitted `Sk_curves.csv` and compare these recomputed values to hidden reference values from the reference study. This recompute‑based check determines the majority of the score. Your reported \(\alpha\) values in `alpha_distributions.csv` will be cross-checked for self-consistency (they must be close to the recomputed \(\alpha\)). The `analytical_relation.csv` will be scored by exact match against precomputed gold values. A successful reproduction must demonstrate that the correct scattering behaviour and the analytical relationship can be obtained from the described procedure.