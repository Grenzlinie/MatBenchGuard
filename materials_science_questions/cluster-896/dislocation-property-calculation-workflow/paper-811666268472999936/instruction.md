# Dislocation Pileup Hall-Petch Slope Scaling Computation

## Problem background
The Hall–Petch relation relates the yield stress \(\sigma\) to the average grain size \(d\) via \(\sigma = \sigma^* + k d^{-1/2}\). A classical model derives this relation from the stress concentration at the head of a dislocation pile-up against a grain boundary. In this work we extend the model to two situations where the nature of the barrier differs from the simple locked dislocation of the same Burgers vector:

1. The barrier is a locked dislocation whose Burgers vector component in the slip plane is \(m\) times that of the free dislocations (\(m > 0\)).
2. The barrier is a second-phase particle; screw dislocations in the matrix pile up against a straight interface across which the shear modulus changes, characterised by the modulus ratio \(K = (G_2-G_1)/(G_2+G_1)\).

For each case the Hall–Petch slope \(k\) depends on the barrier parameter. The present task is to compute how the slope changes when \(m\) varies from 1 to 2 in the first case, and when \(K\) changes from 0 to 0.5 in the second case. The quantitative slope ratios are the central target of the reproduction.

## Approach
The equilibrium positions of discrete dislocations are determined by force-balance equations that include the pairwise interaction forces, the applied stress, and, in the two-phase case, image forces from the interface. The approach is to solve these equations numerically for small dislocation numbers \(n\) (from 2 up to about 50) under a specific yield criterion, then collect the applied stress \(\sigma\) and the pile-up length \(L\). Finally, a linear regression of \(\sigma\) versus \(L^{-1/2}\) yields the Hall–Petch slope for each barrier parameter value.

**Case II – locked dislocation.**
The dislocations are edge type. Let \(n-1\) free dislocations of Burgers vector \(b\) be positioned at \(x_j\) (scaled by \(A/(2\sigma)\) with \(A = Gb/[2\pi(1-\nu)]\) for isotropic elasticity, \(\nu\) is Poisson’s ratio). The locked dislocation of effective Burgers vector \(m b\) lies at \(x=0\). The equilibrium condition for each free dislocation is
\[
\frac{m}{x_j} + \sum_{\substack{i=1\\ i\neq j}}^{n-1} \frac{1}{x_j - x_i} - \frac{1}{2} = 0, \qquad j=1,\dots,n-1.
\]
The yield condition is taken as a critical spacing \(x_1 = 10\,b\) between the locked dislocation and the nearest free dislocation. For each \(n\) we find the applied stress \(\sigma\) (normalised by \(G\)) that satisfies this spacing, and record the corresponding dimensionless pile-up length \(L/b\).

**Case I – two‑phase screw pile‑up.**
Here screw dislocations are considered. With the interface at \(x=0\), image dislocations of strength \(K b\) appear symmetrically. The equilibrium of the \(n\) real dislocations at positions \(x_j\) reads
\[
\sum_{\substack{i=1\\ i\neq j}}^{n} \frac{A}{x_j - x_i} + K \sum_{i=1}^{n} \frac{A}{x_j + x_i} = \sigma, \qquad j=1,\dots,n,
\]
with \(A = G_1 b/(2\pi)\) and \(G_1\) the matrix shear modulus. The yield condition is a critical force on the interface, \(F_{\text{cr}} = G_2 b/30\), which determines the applied stress for each \(n\). The corresponding pile‑up length \(L\) (in units of \(b\)) and normalised stress \(\sigma/G_1\) are recorded.

**Hall–Petch fit.**
For each parameter set (\(m=1,2\); \(K=0,0.5\)) the collected (\(L/b\), \(\sigma/G\) or \(\sigma/G_1\)) points are used to perform a linear least‑squares fit of \(\sigma/G\) (or \(\sigma/G_1\)) against \((L/b)^{-1/2}\). The slope of this line is the Hall–Petch slope for that condition. The ratio of the slopes for the higher‑parameter value to the lower one (\(m=2\) vs \(m=1\); \(K=0.5\) vs \(K=0\)) is the primary quantity to report.

## Reproduction target
Numerically reproduce the Hall–Petch slope scaling for the two barrier variants:

1. **Locked dislocation case (Case II)** – for \(m = 1\) and \(m = 2\), compute the raw pile‑up data (\(n\), \(L/b\), \(\sigma/G\)) for \(n\) from 2 up to roughly 50, fit the Hall–Petch slope from those data, and determine the ratio of the fitted slope for \(m=2\) to that for \(m=1\).
2. **Two‑phase screw pile‑up case (Case I)** – for \(K = 0\) and \(K = 0.5\) (i.e. inclusion/matrix modulus ratio 0 and 0.5), compute the raw pile‑up data (\(n\), \(L/b\), \(\sigma/G_1\)) for \(n\) from 2 to roughly 50, fit the Hall–Petch slope for each \(K\), and determine the ratio of the slope for \(K=0.5\) to that for \(K=0\).

All data and fitted results must be written to the output CSV files exactly as specified in the workflow steps. The target is the pair of slope ratios; a hidden verifier will compare them to a benchmark derived from the original study.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement and validate dislocation pileup solvers
- Role: process
- Action: Implement numerical solvers for the discrete dislocation pileup equilibrium equations: (a) locked dislocation case with force-balance equations including a Burgers vector ratio m, and (b) two-phase screw pileup case with image forces from a straight inclusion interface. Validate each solver by computing positions for small n (e.g., n=2) and verifying that the residual forces are below a tight tolerance. Write a brief solver validation log.
- Evidence: `/app/outputs/solver_validation.txt`

### Step 2: Case II: Locked dislocation pileup Hall–Petch slope
- Role: scored
- Action: Using the validated locked-dislocation solver, for Burgers vector ratios m = 1 and m = 2, for each integer number of free dislocations n from 2 up to approximately 50, compute the equilibrium positions under the critical spacing criterion x1 = 10b. Determine the applied shear stress σ (normalized by G) that satisfies this criterion and the corresponding pileup length L (in units of b). For each m, fit the Hall–Petch relation (σ/G vs (L/b)^(-1/2)) using linear regression to obtain the slope. Compute the ratio of the fitted slope for m=2 to that for m=1. Write all raw (n, L/b, σ/G) points and the fitted slopes and ratio.
- Output file: `/app/outputs/caseII_results.csv`
- Format: csv
- Contract: Columns: n (int), m (int, 1 or 2), L_over_b (float), sigma_over_G (float), slope_fit (float), slope_ratio (float)
- Scoring: scored by hidden verifier

### Step 3: Case I: Two-phase screw pileup Hall–Petch slope
- Role: scored
- Action: Using the validated two-phase screw solver, for inclusion/matrix modulus ratios K = 0 and K = 0.5 (G2/G1 = 1 and 3), for each n from 2 to ~50, compute equilibrium positions under the critical force criterion F_cr = G2 b/30. Determine the applied stress σ (normalized by G1) and pileup length L (in units of b). Fit the Hall–Petch relation for each K to obtain the slope. Compute the ratio of the slope for K=0.5 to that for K=0. Write all raw (n, L/b, σ/G1) points and the fitted results.
- Output file: `/app/outputs/caseI_results.csv`
- Format: csv
- Contract: Columns: n (int), K (float, 0 or 0.5), L_over_b (float), sigma_over_G (float), slope_fit (float), slope_ratio (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/caseII_results.csv`
- `/app/outputs/caseI_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### caseII_results.csv
- path: `/app/outputs/caseII_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file containing for each n the computed pileup length and applied stress for m=1 and m=2, together with the fitted Hall-Petch slopes and the ratio of slopes.
- schema:
  - `type`: table
  - `required_columns`: `n`, `m`, `L_over_b`, `sigma_over_G`, `slope_fit`, `slope_ratio`
  - `units`:
    - `L_over_b`: dimensionless (length in units of b)
    - `sigma_over_G`: dimensionless (stress normalized by shear modulus G)

### caseI_results.csv
- path: `/app/outputs/caseI_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file containing for each n the computed pileup length and applied stress for K=0 and K=0.5, together with the fitted Hall-Petch slopes and the ratio of slopes.
- schema:
  - `type`: table
  - `required_columns`: `n`, `K`, `L_over_b`, `sigma_over_G`, `slope_fit`, `slope_ratio`
  - `units`:
    - `L_over_b`: dimensionless (length in units of b)
    - `sigma_over_G`: dimensionless (stress normalized by matrix shear modulus G1)

Notes: All material parameters (e.g., Poisson's ratio ν, asymptotic factors Q, critical spacing/force criteria) are specified in the problem context; the agent derives them from the force-balance equations and the specified yield criteria. The solver implementation details (root-finding method, tolerances) are left to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "caseII_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "m",
          "L_over_b",
          "sigma_over_G",
          "slope_fit",
          "slope_ratio"
        ],
        "units": {
          "L_over_b": "dimensionless (length in units of b)",
          "sigma_over_G": "dimensionless (stress normalized by shear modulus G)"
        }
      },
      "description": "CSV file containing for each n the computed pileup length and applied stress for m=1 and m=2, together with the fitted Hall-Petch slopes and the ratio of slopes."
    },
    {
      "file": "caseI_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "K",
          "L_over_b",
          "sigma_over_G",
          "slope_fit",
          "slope_ratio"
        ],
        "units": {
          "L_over_b": "dimensionless (length in units of b)",
          "sigma_over_G": "dimensionless (stress normalized by matrix shear modulus G1)"
        }
      },
      "description": "CSV file containing for each n the computed pileup length and applied stress for K=0 and K=0.5, together with the fitted Hall-Petch slopes and the ratio of slopes."
    }
  ],
  "notes": "All material parameters (e.g., Poisson's ratio ν, asymptotic factors Q, critical spacing/force criteria) are specified in the problem context; the agent derives them from the force-balance equations and the specified yield criteria. The solver implementation details (root-finding method, tolerances) are left to the agent."
}
```

## How you are scored
Your submission is scored by a deterministic hidden verifier that reads the two CSV files (`caseII_results.csv` and `caseI_results.csv`). For each condition (\(m=1,2\) and \(K=0,0.5\)) it takes the raw \(L/b\) and \(\sigma/G\) (or \(\sigma/G_1\)) columns, recomputes the Hall–Petch slope via linear regression, and computes the corresponding slope ratio. These recomputed ratios are compared against hidden reference values, and your reward is higher the closer your ratios are to those references. The verifier also checks that the linear fit of \(\sigma\) versus \((L/b)^{-1/2}\) has a sufficiently high R² and that the CSV files contain the required columns with correct data types. The final reward is a weighted combination of the slope‑ratio accuracy and the structural consistency checks. No network access or paper look‑up is needed by the verifier; it works solely with your output files and an internal benchmark.
