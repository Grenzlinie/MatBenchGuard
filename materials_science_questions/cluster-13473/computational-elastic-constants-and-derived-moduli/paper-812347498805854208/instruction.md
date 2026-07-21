# Poisson Ratio of Hard Cyclic Multimers in Close‑Packed Limit

## Problem background
Hard cyclic multimers are two‑dimensional model particles. Each multimer is composed of \(m = 3k\) (with a positive integer \(k\)) hard discs of diameter \(\sigma\). The disc centres form a rigid regular \(m\)-gon whose side length is \(l\). The molecular geometry is characterised by the roughness parameter  

\[
\alpha = \frac{l}{2\sigma}.
\]

At close packing, the multimer centres arrange on a triangular lattice, which makes the system elastically isotropic. The elastic response of such a zero‑temperature packing can be described by the Poisson ratio \(\nu_P\). In the limit of infinitely many discs per multimer (\(m \to \infty\)) the Poisson ratio depends only on \(\alpha\) and is given by the analytic expression

\[
\nu_P(\alpha) = \frac{1 - 2\alpha^2}{3 - 2\alpha^2}.
\]

This result follows from an exact analysis of the close‑packed structure in the zero‑temperature limit.

## Task
Compute the Poisson ratio \(\nu_P\) for a set of roughness parameter values \(\alpha\) in the interval \([0, 1]\) (inclusive). Use **at least 10 \(\alpha\) points** covering this interval. Write the results to the CSV file `/app/outputs/poisson_ratio.csv` with columns `alpha` and `nu_P`.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute the Poisson ratio
- Role: process
- Action: For each chosen value of \(\alpha\) evaluate the formula  
  \(\nu_P = \dfrac{1 - 2\alpha^2}{3 - 2\alpha^2}\).
- Evidence: none

### Step 2: Output Poisson ratio CSV
- Role: scored (load‑bearing)
- Action: Generate at least 10 \(\alpha\) points in \([0, 1]\), compute \(\nu_P\) for each, and write the results to the output file.
- Output file: `/app/outputs/poisson_ratio.csv`
- Format: csv
- Contract: `alpha`: float, dimensionless, values in \([0,1]\); `nu_P`: float, dimensionless; at least 10 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/poisson_ratio.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### poisson_ratio.csv
- path: `/app/outputs/poisson_ratio.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file with columns `alpha` and `nu_P` giving the Poisson ratio as a function of the roughness parameter \(\alpha\).
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `nu_P`
  - `units`:
    - `alpha`: dimensionless
    - `nu_P`: dimensionless

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does **not** judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "poisson_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "nu_P"
        ],
        "units": {
          "alpha": "dimensionless",
          "nu_P": "dimensionless"
        }
      },
      "description": "CSV file with columns 'alpha' and 'nu_P' giving the Poisson ratio as a function of the roughness parameter α."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `poisson_ratio.csv`, validates its format and contents, and for each row computes the reference Poisson ratio using the analytic formula \(\nu_P = (1-2\alpha^2)/(3-2\alpha^2)\). It compares your computed \(\nu_P\) to the reference value with an appropriate tolerance. The final reward is the fraction of \(\alpha\) points whose \(\nu_P\) lies within tolerance. The verifier does **not** merely check for file existence; it performs an independent numerical evaluation.

**You do not need to derive the formula from first principles – the explicit expression is provided above.**