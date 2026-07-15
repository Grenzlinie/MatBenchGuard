# Spin Correlation of Gutzwiller Wave Function in 1D Atomic Limit

## Problem background
Strongly correlated electron systems are described by Hubbard-type models where the Coulomb repulsion competes with electron hopping. The Gutzwiller wave function is a variational ansatz that globally reduces double occupancy and captures many essential correlations. Evaluating spin correlation functions for this wave function provides direct insight into the nature of magnetic order and the antiferromagnetic tendencies of the system. In one dimension, an analytic closed-form expression for the spin correlation function can be derived. In the atomic limit (correlation parameter \(g = 0\)) at half-filling (\(n = 1\)), the real-space spin correlation function \(C_j^{SS}\) simplifies to a compact form involving the sine integral. The present task is to compute this quantity for small lattice separations.

## Approach
Use the analytic formula for the spin correlation function in the atomic limit:  
\[C_j^{SS} = (-1)^j \frac{\mathrm{Si}(\pi j)}{\pi j},\]  
where \(\mathrm{Si}\) is the sine integral. This expression is valid for half-filling (\(n = 1\)) and \(g = 0\). Implement it in Python using standard scientific computing libraries (NumPy for numerical operations and SciPy for the special function \(\mathrm{Si}\)). Evaluate \(C_j^{SS}\) at integer separations \(j = 1, 2, \ldots, 8\) and write the results to a CSV file.

## Reproduction target
Compute the spin correlation function \(C_j^{SS}\) for the Gutzwiller wave function in one dimension at the atomic limit (\(g = 0\)) and half-filling (\(n = 1\)), for lattice separations \(j = 1, 2, \dots, 8\). Output the computed values to a CSV file with columns 'j' and 'C_j_SS', with rows in ascending order of \(j\).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute spin correlation function in atomic limit
- Role: scored (load-bearing)
- Action: Using the sine integral function from SciPy, implement the spin correlation function C_j^SS = (-1)^j * Si(πj) / (πj) for the atomic limit (correlation parameter g=0, half-filling n=1). Evaluate for integer separation j = 1, 2, ..., 8. Output the results to a CSV file with columns 'j' and 'C_j_SS'.
- Output file: `/app/outputs/spin_correlations.csv`
- Format: csv
- Contract: Two columns: 'j' (integer, 1 to 8) and 'C_j_SS' (float, computed value). Row order ascending j.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spin_correlations.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spin_correlations.csv
- path: `/app/outputs/spin_correlations.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed spin correlation values for the Gutzwiller wave function in the atomic limit.
- schema:
  - `type`: table
  - `required_columns`: `j`, `C_j_SS`
  - `units`:
    - `C_j_SS`: dimensionless

Notes: The paper reports multiple independent correlation functions (density, double occupancy, hole, superconducting) and ground-state energy minimization. This reproduction package focuses on the spin correlation function C_j^SS in the atomic limit (g=0,n=1) as the simplest closed-form instance demonstrating the method. The other correlation functions and energy minimization, while also reproducible with the same public formulas, require handling multiple momentum regimes, additional parameter dependencies, and variational optimization that would excessively expand the package beyond the single clean reproduction target. This scope is acceptable as a proof-of-concept reproduction of the paper's core analytic approach.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spin_correlations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "j",
          "C_j_SS"
        ],
        "units": {
          "C_j_SS": "dimensionless"
        }
      },
      "description": "Computed spin correlation values for the Gutzwiller wave function in the atomic limit."
    }
  ],
  "notes": "The paper reports multiple independent correlation functions (density, double occupancy, hole, superconducting) and ground-state energy minimization. This reproduction package focuses on the spin correlation function C_j^SS in the atomic limit (g=0,n=1) as the simplest closed-form instance demonstrating the method. The other correlation functions and energy minimization, while also reproducible with the same public formulas, require handling multiple momentum regimes, additional parameter dependencies, and variational optimization that would excessively expand the package beyond the single clean reproduction target. This scope is acceptable as a proof-of-concept reproduction of the paper's core analytic approach."
}
```

## How you are scored
A hidden verifier will read your output file and compare each computed \(C_j^{SS}\) value against a hidden reference for the corresponding \(j\). The reward is proportional to the number of \(j\) values that are within a hidden tolerance of the reference. Each workflow stage's artifact is scored independently, and the stage scores are combined (with the main artifact carrying the dominant weight) into a final reward. Reporting numbers from memory or from external sources will not satisfy the verifier; you must execute the computation as described in the workflow steps.
