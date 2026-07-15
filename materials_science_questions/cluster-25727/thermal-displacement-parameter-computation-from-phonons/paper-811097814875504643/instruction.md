# Mean-square velocities in harmonic linear chains with free boundaries

## Problem background
The second-order Doppler shift in Mössbauer spectroscopy is proportional to the mean-square velocity of the emitting or absorbing atom. This work derives a general expression for the mean-square velocity of an atom in a harmonic crystal without periodic boundary conditions. Applying this to linear chains with free ends allows us to investigate how proximity to a surface affects the atomic velocity. The task is to compute the mean-square velocities for atoms in specific monatomic and diatomic harmonic chains and determine the relationship between the velocities of end atoms and interior atoms.

## Approach
The approach is based on harmonic lattice dynamics with free boundary conditions. For a diatomic linear chain with nearest-neighbor forces, the high-temperature correction term P2 can be obtained directly from the diagonal elements of the dynamical matrix. For a monatomic chain at zero temperature, the mean-square velocity can be computed from the normal modes of the chain or from an explicit closed-form expression derived from the eigenvectors. The agent implements these formulas for the specified chain parameters and outputs per-atom values. The results allow a comparison between end atoms and interior atoms of the same mass, both for the high-temperature correction and the zero-temperature limit.

## Reproduction target
For a diatomic linear chain with free ends, N=10 unit cells (20 atoms), masses m1=1 (odd indices) and m2=4 (even indices), force constant γ=1, compute the high-temperature correction term P2(r) for each atom r=1..20 (set ħ=1, kB=1, T=1). Write the result as a CSV file with columns atom_index (1-indexed) and P2_value.

For a monatomic linear chain with free ends, N=20 atoms, mass m=1, force constant γ=1, compute the zero-temperature mean-square velocity ⟨|u̇_r|²⟩ for each atom r=1..20 (set ħ=1). Write the result as a CSV file with columns atom_index (1-indexed) and mean_square_velocity.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute high-temperature P2 correction for diatomic chain
- Role: scored
- Action: For a diatomic linear chain with free ends, N=10 unit cells (20 atoms), masses m₁=1 (atoms at odd indices) and m₂=4 (atoms at even indices), force constant γ=1. The high-temperature correction P₂(r) for each atom r=1..20 follows from Eqs. (18) after omitting the common factor ħ²/(k_B T) which equals 1 here (ħ=1, k_B=1, T=1). Compute according to:
  - Define ω₁² = 2γ/m₁, ω₂² = 2γ/m₂.
  - For odd-indexed atoms r=1,3,...,19:
    * if r=1 (left end): P₂ = ħ² ω₁² / (24 m₁ k_B T) = ω₁² / (24 m₁)
    * otherwise (r=3,5,...,19): P₂ = ħ² ω₁² / (12 m₁ k_B T) = ω₁² / (12 m₁)
  - For even-indexed atoms r=2,4,...,20:
    * if r=20 (right end): P₂ = ħ² ω₂² / (24 m₂ k_B T) = ω₂² / (24 m₂)
    * otherwise (r=2,4,...,18): P₂ = ħ² ω₂² / (12 m₂ k_B T) = ω₂² / (12 m₂)
  Write a CSV file with columns 'atom_index' (1-indexed integer) and 'P2_value' (float).
- Output file: `/app/outputs/high_temp_P2.csv`
- Format: csv
- Contract: columns: atom_index (integer, 1-indexed), P2_value (float)
- Scoring: scored by hidden verifier

### Step 2: Compute zero-temperature mean-square velocity for monatomic chain
- Role: scored
- Action: For a monatomic linear chain with free ends, N=20 atoms, mass m=1, force constant γ=1, compute the mean-square velocity at absolute zero temperature ⟨|u̇_r|²⟩ for each atom r=1..20 using the closed-form result from Eq. (22). Set ħ=1. The explicit formula is:
  ω_L = √(4γ/m)
  ⟨|u̇_r|²⟩ = [ħ ω_L / (16 N m)] × {cot[(4r-1)π/(8N)] - cot[(4r-3)π/(8N)] + 2 cot(π/(8N))}
  where cot(x) = cos(x)/sin(x). Write a CSV file with columns 'atom_index' (1-indexed integer) and 'mean_square_velocity' (float).
- Output file: `/app/outputs/low_temp_msv.csv`
- Format: csv
- Contract: columns: atom_index (integer, 1-indexed), mean_square_velocity (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/high_temp_P2.csv`
- `/app/outputs/low_temp_msv.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### high_temp_P2.csv
- path: `/app/outputs/high_temp_P2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: High-temperature correction P2(r) for a diatomic linear chain with N=10 unit cells, m1=1, m2=4, γ=1.
- schema:
  - `type`: table
  - `required_columns`: `atom_index`, `P2_value`
  - `units`:
    - `atom_index`: dimensionless
    - `P2_value`: arbitrary (ħ=k_B=T=1)

### low_temp_msv.csv
- path: `/app/outputs/low_temp_msv.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zero-temperature mean-square velocity for a monatomic linear chain with N=20 atoms, m=1, γ=1.
- schema:
  - `type`: table
  - `required_columns`: `atom_index`, `mean_square_velocity`
  - `units`:
    - `atom_index`: dimensionless
    - `mean_square_velocity`: arbitrary (ħ=1)

Notes: The checker recomputes the expected per-atom values from the same formulas and parameters using standard floating-point arithmetic, then compares element-wise with a relative tolerance. Structural patterns (end vs. interior ratios for diatomic chain; monotonic decrease for monatomic chain) are evaluated separately.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "high_temp_P2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom_index",
          "P2_value"
        ],
        "units": {
          "atom_index": "dimensionless",
          "P2_value": "arbitrary (ħ=k_B=T=1)"
        }
      },
      "description": "High-temperature correction P2(r) for a diatomic linear chain with N=10 unit cells, m1=1, m2=4, γ=1."
    },
    {
      "file": "low_temp_msv.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom_index",
          "mean_square_velocity"
        ],
        "units": {
          "atom_index": "dimensionless",
          "mean_square_velocity": "arbitrary (ħ=1)"
        }
      },
      "description": "Zero-temperature mean-square velocity for a monatomic linear chain with N=20 atoms, m=1, γ=1."
    }
  ],
  "notes": "The checker recomputes the expected per-atom values from the same formulas and parameters using standard floating-point arithmetic, then compares element-wise with a relative tolerance. Structural patterns (end vs. interior ratios for diatomic chain; monotonic decrease for monatomic chain) are evaluated separately."
}
```

## How you are scored
A hidden verifier will independently recompute the expected per-atom values for each chain from the same physical model and parameters. It will compare your submitted CSV files element-wise, checking both numerical agreement and structural properties (e.g., the relative sizes of end vs. interior atoms). The two scored outputs are combined into a final reward between 0 (worst) and 1 (best). The reward reflects how closely your computed values match the expected results; simply reporting the paper's numbers without proper computation will not suffice.
