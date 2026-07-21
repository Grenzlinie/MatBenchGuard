# Computing tricritical points and critical w parameter in anisotropic Heisenberg model with random fields

## Problem background
The spin‑1/2 anisotropic quantum Heisenberg model on three dimensional lattices (simple cubic and body‑centered cubic) is considered in a spatially random longitudinal magnetic field. The field at each site is drawn from a trimodal distribution controlled by a weight parameter w that interpolates between a symmetric bimodal case (w=0) and a pure zero‑field system (w=1). Within an effective‑field‑theory two‑spin cluster approximation (EFT‑2), the magnetization can be expanded in odd powers whose coefficients determine the second‑order transition boundary (C1=1, C3<0) and the tricritical point where the transition changes character (C1=1, C3=0). The aim is to compute how exchange anisotropy and the distribution parameter w alter the phase diagrams, the location of tricritical points, and the existence of reentrant behaviour.

## Approach
We employ the EFT‑2 formulation, which treats the selected pair of spin‑1/2 particles exactly while replacing the perimeter spins by Ising variables (axial approximation) and using a decoupling approximation to handle the many‑spin correlations. After applying a differential operator technique, the magnetization per spin is cast as a sum over binomial expansions involving the lattice coordination numbers (z0 and z1) and the exchange couplings Jx, Jy, Jz. By integrating over the trimodal field distribution, we obtain odd‑order coefficients Ck that depend on the scaled exchange parameters rx, ry (with rz=1), the temperature T, the random‑field amplitude H0, and the weight w. The second‑order critical curve is the solution of C1=1 with C3<0; the tricritical point satisfies C1=1 and C3=0 simultaneously. Numerical root‑finding scans along these conditions yield the tricritical coordinates. For the trimodal case, the critical weight w* is defined as the largest w in [0,1] for which the phase boundary still reaches zero temperature (i.e., there exists some H0/J where Tc=0). This is found by sweeping w and detecting the threshold where the zero‑temperature intersection disappears. The required output tables are compiled directly from these computations.

## Reproduction target
1. For the bimodal distribution (w=0) on the simple cubic lattice (z0=5, z1=0) and on the body‑centered cubic lattice (z0=7, z1=0), with fixed exchange anisotropy rx=1.0 and three values of ry (1.0, 1.5, 2.0), compute the tricritical point coordinates (H0/J, kB Tc/J). Report each (lattice, ry) combination as a row in `tricritical_points_bimodal.csv`.
2. For the trimodal distribution on the simple cubic lattice with rx=1.0, ry=1.0, determine the critical weight w* — the maximum w in [0,1] such that the phase boundary touches the H0/J axis (i.e., there exists at least one H0/J for which Tc=0). Report the single value in `w_star_trimodal.csv`.

## Assets

- Python 3 with NumPy and SciPy: numpy, scipy

## Workflow steps

### Step 1: Implement EFT-2 solver
- Role: process
- Action: Implement the effective-field-theory two-spin cluster (EFT-2) equations for the spin-1/2 anisotropic quantum Heisenberg model with trimodal random field distribution. The solver must evaluate the odd-order coefficients C_k from the binomial expansion and random field averaging given Hamiltonian parameters (J_x,J_y,J_z with r_n=J_n/J, r_z=1), lattice geometry (z0,z1), random field distribution parameters (w,H0), and temperature T. It must be capable of locating second-order critical lines (C1=1, C3<0) and tricritical points (C1=1, C3=0).
- Evidence: none

### Step 2: Compute tricritical points for bimodal distribution
- Role: scored (load-bearing)
- Action: Using the EFT-2 solver, compute the tricritical point coordinates (H0/J, k_B T_c/J) for the bimodal random field distribution (w=0) on the simple cubic (z0=5, z1=0) and body-centered cubic (z0=7, z1=0) lattices. Set exchange anisotropy r_x=1.0 and r_y=1.0, 1.5, 2.0 (with r_z=1.0). For each (lattice, r_y) combination, determine the unique point satisfying C1=1 and C3=0. Write one row per combination to the output CSV.
- Output file: `/app/outputs/tricritical_points_bimodal.csv`
- Format: csv
- Contract: CSV with columns: lattice (string: 'SC' or 'BCC'), r_y (float), H0_over_J (float), kBTc_over_J (float).
- Scoring: scored by hidden verifier

### Step 3: Compute w* for trimodal distribution
- Role: scored
- Action: Using the EFT-2 solver, determine the critical trimodal parameter w* for the simple cubic lattice (z0=5, z1=0) with exchange anisotropy r_x=1.0, r_y=1.0. The parameter w* is defined as the maximum value of w in [0,1] for which there exists at least one field H0/J such that the critical temperature Tc is zero (i.e., the phase boundary touches the H0/J axis). Sweep w and locate the threshold. Output a single row with the found w*.
- Output file: `/app/outputs/w_star_trimodal.csv`
- Format: csv
- Contract: CSV with columns: lattice (string), r_x (float), r_y (float), w_star (float). One row: 'SC', 1.0, 1.0, <w_star>.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tricritical_points_bimodal.csv`
- `/app/outputs/w_star_trimodal.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tricritical_points_bimodal.csv
- path: `/app/outputs/tricritical_points_bimodal.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tricritical point coordinates (H0/J, kBTc/J) for bimodal random field distribution on SC and BCC lattices for r_y=1.0,1.5,2.0.
- schema:
  - `type`: table
  - `required_columns`: `lattice`, `r_y`, `H0_over_J`, `kBTc_over_J`
  - `units`:
    - `H0_over_J`: dimensionless
    - `kBTc_over_J`: dimensionless

### w_star_trimodal.csv
- path: `/app/outputs/w_star_trimodal.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical trimodal parameter w* on SC lattice at r_x=1.0, r_y=1.0.
- schema:
  - `type`: table
  - `required_columns`: `lattice`, `r_x`, `r_y`, `w_star`
  - `units`:
    - `w_star`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tricritical_points_bimodal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice",
          "r_y",
          "H0_over_J",
          "kBTc_over_J"
        ],
        "units": {
          "H0_over_J": "dimensionless",
          "kBTc_over_J": "dimensionless"
        }
      },
      "description": "Tricritical point coordinates (H0/J, kBTc/J) for bimodal random field distribution on SC and BCC lattices for r_y=1.0,1.5,2.0."
    },
    {
      "file": "w_star_trimodal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice",
          "r_x",
          "r_y",
          "w_star"
        ],
        "units": {
          "w_star": "dimensionless"
        }
      },
      "description": "Critical trimodal parameter w* on SC lattice at r_x=1.0, r_y=1.0."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier evaluates the two output CSV files independently. It compares your reported tricritical coordinates to hidden reference values derived from the published study, using relative tolerances that absorb legitimate implementation differences. It additionally checks two mandatory trends: (i) for each lattice, both H0/J and kB Tc/J must decrease monotonically as ry increases; (ii) for each ry, the BCC coordinates must be larger than the corresponding SC coordinates. The tricritical‑point stage (including the trend checks) accounts for 70% of the total reward. The reported w* is compared to the hidden reference with an absolute tolerance and contributes the remaining 30%. The reward is computed as a weighted combination; merely reporting numbers without a faithful EFT‑2 solver will not satisfy the trend verification.
