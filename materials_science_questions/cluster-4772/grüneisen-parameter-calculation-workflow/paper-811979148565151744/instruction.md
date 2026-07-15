# Calculation of Acoustic Mode Grüneisen Parameters for an h.c.p. Lattice from Third-Order Elastic Constants

## Problem background
The low-temperature thermal expansion of uniaxial crystals is governed by the generalized Grüneisen parameters (GP's) of long-wave acoustic modes. These GP's can be calculated from the second- and third-order elastic constants of the crystal. This task applies the theory to a model hexagonal close-packed (h.c.p.) lattice with nearest-neighbour central interactions described by a (6,12) Lennard-Jones potential. The goal is to compute the acoustic wave velocities and the associated GP's (γ′ and γ″) for waves propagating in different directions relative to the crystal's unique axis, and to investigate how these parameters vary with propagation angle.

## Approach
We compute the second-order and third-order elastic constants for the ideal h.c.p. lattice from the lattice geometry and the derivatives of the Lennard-Jones potential. Using these constants, we construct the dynamic matrix D_jk for an unstrained crystal. For each chosen propagation direction (specified by the angle θ between the wave vector and the hexagonal axis), we solve the cubic characteristic equation to obtain the three acoustic wave velocity quantities X_i (in arbitrary units). From the dependence of the coefficients of this cubic on areal strain ε′ and longitudinal strain ζ, we derive closed-form expressions for the Grüneisen parameters γ′_i and γ″_i. The calculation is performed for nine angles between 5° and 85°, and the results for the three branches are ordered by decreasing X_i within each angle.

## Reproduction target
Produce a CSV file `gp_table.csv` with exactly 10 columns: `theta` (degrees), `X1`, `gamma1_prime`, `gamma1_doubleprime`, `X2`, `gamma2_prime`, `gamma2_doubleprime`, `X3`, `gamma3_prime`, `gamma3_doubleprime`. There must be one row for each of the angles θ = 5°, 15°, 25°, 35°, 45°, 55°, 65°, 75°, 85°. Within each angle, the three branches (1,2,3) correspond to the three eigenvalues X_i arranged from largest to smallest.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute second- and third-order elastic constants for the h.c.p. Lennard-Jones lattice
- Role: process
- Action: Derive and numerically compute the second-order elastic constants (C11, C12, C13, C33, C44) and third-order elastic constants (C111, C222, C333, C112, C113, C123, C133, C144, C155, C344) for an ideal h.c.p. lattice with nearest-neighbour central interaction of the (6,12) Lennard-Jones type, using the lattice geometry (nearest-neighbour distance D and ideal c/a ratio) and the potential derivatives (k2, k3) as described in the model derivation. No external data is required; the constants follow from the expressions given by the central-force model.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 2: Compute wave velocities and Grüneisen parameters table
- Role: scored (load-bearing)
- Action: For each propagation angle theta = 5°, 15°, 25°, 35°, 45°, 55°, 65°, 75°, 85°, use the computed elastic constants to construct the dynamic matrix D_jk in the unstrained state, solve the cubic characteristic equation to obtain the three acoustic wave velocities X_i (ordered from largest to smallest), and compute the generalized Grüneisen parameters gamma'_i and gamma''_i from the closed-form expressions relating them to derivatives of the characteristic polynomial coefficients. Write the results to a CSV file.
- Output file: `/app/outputs/gp_table.csv`
- Format: csv
- Contract: CSV with exactly 10 columns: theta (float, degrees), X1 (float), gamma1_prime (float), gamma1_doubleprime (float), X2 (float), gamma2_prime (float), gamma2_doubleprime (float), X3 (float), gamma3_prime (float), gamma3_doubleprime (float). Rows for theta = 5,15,25,35,45,55,65,75,85. Within each angle, branches are ordered by descending X_i (largest eigenvalue first).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gp_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gp_table.csv
- path: `/app/outputs/gp_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed acoustic wave velocities X_i and generalized Grüneisen parameters gamma'_i and gamma''_i for three branches at nine propagation angles.
- schema:
  - `type`: table
  - `required_columns`: `theta`, `X1`, `gamma1_prime`, `gamma1_doubleprime`, `X2`, `gamma2_prime`, `gamma2_doubleprime`, `X3`, `gamma3_prime`, `gamma3_doubleprime`
  - `units`:
    - `X1`: arbitrary units
    - `gamma1_prime`: dimensionless
    - `gamma1_doubleprime`: dimensionless
    - `X2`: arbitrary units
    - `gamma2_prime`: dimensionless
    - `gamma2_doubleprime`: dimensionless
    - `X3`: arbitrary units
    - `gamma3_prime`: dimensionless
    - `gamma3_doubleprime`: dimensionless

Notes: Scoring compares each numeric cell against the corresponding hidden reference value using predetermined absolute tolerances (0.5 for X_i values, 0.05 for the GP values). Branch ordering within each angle must be by descending X_i.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gp_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "X1",
          "gamma1_prime",
          "gamma1_doubleprime",
          "X2",
          "gamma2_prime",
          "gamma2_doubleprime",
          "X3",
          "gamma3_prime",
          "gamma3_doubleprime"
        ],
        "units": {
          "X1": "arbitrary units",
          "gamma1_prime": "dimensionless",
          "gamma1_doubleprime": "dimensionless",
          "X2": "arbitrary units",
          "gamma2_prime": "dimensionless",
          "gamma2_doubleprime": "dimensionless",
          "X3": "arbitrary units",
          "gamma3_prime": "dimensionless",
          "gamma3_doubleprime": "dimensionless"
        }
      },
      "description": "Computed acoustic wave velocities X_i and generalized Grüneisen parameters gamma'_i and gamma''_i for three branches at nine propagation angles."
    }
  ],
  "notes": "Scoring compares each numeric cell against the corresponding hidden reference value using predetermined absolute tolerances (0.5 for X_i values, 0.05 for the GP values). Branch ordering within each angle must be by descending X_i."
}
```

## How you are scored
A hidden verifier will compare every numeric cell in your submitted `gp_table.csv` against reference values (hidden gold) using predetermined absolute tolerances. The final score is a weighted combination of the deviations across all cells and the correct ordering of branches. The intermediate elastic constants evidence (`elastic_constants.json`) is not directly scored but its presence is required. Exact agreement with the paper's numbers is not necessary; however, you must compute the values sincerely by implementing the method described in the workflow steps.
