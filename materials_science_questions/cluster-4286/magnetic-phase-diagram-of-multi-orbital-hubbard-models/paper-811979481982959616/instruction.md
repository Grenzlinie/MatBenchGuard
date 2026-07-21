# Compute magnetization and energy in a two-band mean-field Hubbard model

## Problem background
Strongly correlated electron systems with multiple orbitals can exhibit complex magnetic order. The two-band Hubbard model with intra-site Coulomb repulsion U and Hund's rule coupling J describes electrons moving in two orbitals and interacting on the same site. Within a Hartree-Fock (mean-field) approximation at absolute zero, the occupation numbers of the four spin-orbital states satisfy a set of self-consistent equations. By solving these equations, one obtains the ground-state magnetization and energy per site as functions of U and J. This allows a quantitative investigation of how the competition between Coulomb repulsion and Hund's coupling affects the onset of ferromagnetism.

## Approach
The mean-field self-consistent equations for the occupation numbers n_{1,σ}, n_{2,σ} are derived from the two-band Hamiltonian assuming a free‑electron‑like density of states per orbital with constants A1 and A2. The equations couple the four occupation numbers; the chemical potential is fixed by the total electron concentration n = 2. For a given (U,J) pair, we seek two solutions: a paramagnetic (unmagnetized) solution with equal up- and down-spin occupations, and a magnetically ordered solution that may break spin symmetry. The self-consistent equations are solved numerically using a root-finding method. From the converged occupation numbers we then compute the relative magnetization M/(2μ_B) and the ground-state energy per site u for both solutions.

## Reproduction target
Produce a CSV file, self_consistent_results.csv, with the following columns: U, J, M_over_2muB, u_magnetized, u_unmagnetized. Perform two parameter sweeps at n = 2, A1 = 1.00, A2 = 1.01:
- Sweep 1: fix J = 0.1 and vary U = 0.2, 0.3, …, 0.8.
- Sweep 2: fix U = 0.3 and vary J = 0.0, 0.1, …, 0.5.
For each (U,J) point, report the magnetized and unmagnetized solutions. Units are in the arbitrary energy units of the model, with M/(2μ_B) dimensionless.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Solve Hartree-Fock self-consistent equations
- Role: process
- Action: Implement the two-band mean-field self-consistent equations for occupation numbers n_{1,σ}, n_{2,σ} derived from a Hartree-Fock approximation with a free-electron density of states. For each required combination of Hubbard U and Hund's coupling J, use a numerical root-finder to obtain magnetically ordered and paramagnetic solutions satisfying the total electron count n = 2. Save the converged occupation numbers as evidence.
- Evidence: `/app/outputs/occupation_numbers.npz`

### Step 2: Compute magnetization and ground-state energy
- Role: scored (load-bearing)
- Action: From the converged occupation numbers, compute the relative magnetization M/(2 μ_B) and the energy per site for both magnetized and unmagnetized states. Perform two parameter sweeps: (1) fix J = 0.1, vary U from 0.2 to 0.8 in steps of 0.1; (2) fix U = 0.3, vary J from 0.0 to 0.5 in steps of 0.1. Write a CSV with columns U, J, M_over_2muB, u_magnetized, u_unmagnetized.
- Output file: `/app/outputs/self_consistent_results.csv`
- Format: csv
- Contract: U (float), J (float), M_over_2muB (float), u_magnetized (float), u_unmagnetized (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/self_consistent_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### self_consistent_results.csv
- path: `/app/outputs/self_consistent_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the computed relative magnetization M/(2μ_B) and ground-state energies per site for magnetized and unmagnetized solutions at absolute zero, for two parameter sweeps: (1) fixed J=0.1, U=0.2,0.3,...,0.8; (2) fixed U=0.3, J=0.0,0.1,...,0.5. The checker recomputes the self-consistent Hartree-Fock equations to obtain reference values, compares M_over_2muB within a tolerance, checks energy ordering (u_magnetized < u_unmagnetized), and verifies non-decreasing magnetization with increasing U and J.
- schema:
  - `type`: table
  - `required_columns`: `U`, `J`, `M_over_2muB`, `u_magnetized`, `u_unmagnetized`
  - `units`:
    - `U`: energy (arbitrary units)
    - `J`: energy (arbitrary units)
    - `M_over_2muB`: dimensionless
    - `u_magnetized`: energy per site (arbitrary units)
    - `u_unmagnetized`: energy per site (arbitrary units)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "self_consistent_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "J",
          "M_over_2muB",
          "u_magnetized",
          "u_unmagnetized"
        ],
        "units": {
          "U": "energy (arbitrary units)",
          "J": "energy (arbitrary units)",
          "M_over_2muB": "dimensionless",
          "u_magnetized": "energy per site (arbitrary units)",
          "u_unmagnetized": "energy per site (arbitrary units)"
        }
      },
      "description": "CSV file containing the computed relative magnetization M/(2μ_B) and ground-state energies per site for magnetized and unmagnetized solutions at absolute zero, for two parameter sweeps: (1) fixed J=0.1, U=0.2,0.3,...,0.8; (2) fixed U=0.3, J=0.0,0.1,...,0.5. The checker recomputes the self-consistent Hartree-Fock equations to obtain reference values, compares M_over_2muB within a tolerance, checks energy ordering (u_magnetized < u_unmagnetized), and verifies non-decreasing magnetization with increasing U and J."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently re‑implements the same self-consistent equations and solves them for the identical (U,J) parameter sweeps using a standard numerical root‑finder. For each row the verifier:
- Compares your M_over_2muB to its own recomputed reference value, with a prescribed tolerance.
- Checks that the magnetized energy is lower than the unmagnetized energy (u_magnetized < u_unmagnetized).
- Verifies that M_over_2muB does not decrease when U increases at fixed J, and does not decrease when J increases at fixed U.
The final score (a float between 0 and 1) is a weighted combination of the fraction of rows that pass the tolerance check and the fraction that satisfy the trend conditions.
