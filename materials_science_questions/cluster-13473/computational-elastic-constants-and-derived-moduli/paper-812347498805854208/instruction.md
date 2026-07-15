# Poisson Ratio of Hard Cyclic Multimers in Close-Packed Limit

## Problem background
Hard cyclic multimers are model particles in two dimensions, each composed of m=3k (k a positive integer) hard discs of diameter σ whose centres form a rigid regular m-gon with side length l. The geometry is characterised by a roughness parameter α = l/(2σ). At close packing, the multimer centres arrange on a triangular lattice, which imposes elastic isotropy on the system. The elastic response of such a zero-temperature packing can be described by the bulk modulus, shear modulus, and Poisson ratio ν_P. The goal of this task is to determine, from first principles, how the Poisson ratio depends on the roughness parameter α.

## Approach
The hard potential is replaced by the limit of an n‑inverse power interaction (n→∞) between disc centres, and only the contacts between nearest‑neighbour discs belonging to different multimers are retained. For a given α, the total energy per unit area of the close‑packed reference state is expressed as a function of the applied strain. Small homogeneous deformations are introduced by varying the strain components, and the energy is differentiated with respect to those components at the reference state. The second derivatives yield the elastic constants λ_{ξηξη} and λ_{ξξηη}. From these, the bulk modulus B, shear modulus μ, and the Poisson ratio ν_P = (B – μ)/(B + μ) are computed. By changing α, the full functional dependence ν_P(α) is obtained.

## Reproduction target
Implement the model described above and compute ν_P for a series of α values in the interval [0, 1] (inclusive). Use at least 10 evenly spaced α points. For each α, apply the strain derivatives and extract the Poisson ratio. Write the results to a CSV file named poisson_ratio.csv under /app/outputs, with columns 'alpha' and 'nu_P'.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute elastic constants and Poisson ratio
- Role: process
- Action: Implement the geometric model of a cyclic multimer composed of m=3k hard discs (each of diameter σ) whose centres lie on a rigid regular m-gon of side length l. Define the roughness parameter α = l/(2σ). Establish the close-packed reference state as a triangular lattice of multimer centres. For a given α, evaluate the total interaction energy per unit area using the n‑inverse power potential in the limit n → ∞, restricted to nearest‑neighbour disc pairs between different multimers. Apply small homogeneous deformations and differentiate the energy with respect to the strain components to obtain the elastic constants λ_{ξηξη} and λ_{ξξηη}. From these, compute the bulk modulus B, the shear modulus μ, and the Poisson ratio ν_P = (B – μ)/(B + μ).
- Evidence: none

### Step 2: Output Poisson ratio CSV
- Role: scored (load-bearing)
- Action: For a series of α values from 0 to 1 inclusive (at least 10 evenly spaced points), compute ν_P using the procedure described in step 1 and write the results to a CSV file named 'poisson_ratio.csv'.
- Output file: `/app/outputs/poisson_ratio.csv`
- Format: csv
- Contract: alpha: float, dimensionless, values in [0,1] inclusive; nu_P: float, dimensionless, computed Poisson ratio; at least 10 rows.
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
- description: CSV file with columns 'alpha' and 'nu_P' giving the Poisson ratio as a function of the roughness parameter α.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `nu_P`
  - `units`:
    - `alpha`: dimensionless
    - `nu_P`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

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
A hidden verifier reads your poisson_ratio.csv, validates its format and contents, and for each row computes a reference Poisson ratio using the established analytical model. It compares your computed ν_P to the reference value with an appropriate tolerance. The final reward is the fraction of α points whose ν_P lies within tolerance. The verifier does not merely check for file existence; it performs an independent numerical evaluation of the elastic constants from the same input geometry. Your score depends only on the accuracy of the Poisson ratios you submit, not on matching any particular published number.
