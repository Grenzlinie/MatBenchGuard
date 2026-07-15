# Element Orbital Basis Kohn-Sham Energy Calculation for BCC Sodium

## Problem background
Kohn-Sham density functional theory (KS-DFT) is the most widely used electronic structure method for condensed matter. A central challenge is the choice of basis functions: uniform bases such as plane waves give high accuracy at the cost of thousands of degrees of freedom per atom, while compact contracted bases (e.g., atomic orbitals) reduce cost but rely on a fitting procedure whose accuracy can degrade for systems far from the training set. This task implements a scheme that automatically contracts a uniform plane-wave basis into a small set of highly accurate, localized basis functions called element orbitals (EOs), aiming to combine the systematic accuracy of plane waves with the low cost of contracted bases. Your goal is to use this method to compute the total free energy per atom for a periodic sodium crystal.

## Approach
The method constructs element orbitals in two stages. First, the crystal supercell is partitioned into rectangular elements. For each element, a local Kohn-Sham problem is solved within an extended element (the element plus its neighbors) using a plane-wave basis and a norm-conserving pseudopotential. The lowest eigenfunctions are restricted to the original element and orthonormalized, yielding adaptive local basis functions (ALBs). Second, the global discontinuous Galerkin Hamiltonian is built in the ALB basis. For each element, the local submatrix is diagonalized to obtain low-energy candidate functions; a localization weight is then applied and a generalized eigenvalue problem is solved to select a few localized element orbitals per atom. These EOs form a compact basis. Self-consistent field (SCF) iterations are then performed in the EO basis to compute the total free energy. The procedure is repeated for several lattice constants to trace the energy curve of a BCC Na crystal.

## Reproduction target
Implement the element orbital method described above and compute the total free energy per atom of a body‑centered cubic (BCC) sodium crystal with 432 atoms at the lattice constants: 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9 a.u. Output the results as a CSV file with the name `/app/outputs/na_lattice_energies.csv` containing exactly two columns: `lattice_constant` (a.u.) and `total_free_energy_per_atom` (Hartree), one row for each lattice constant.

## Assets

- HGH norm-conserving pseudopotential for Na: https://www.abinit.org/psp-tables/Na
- Plane-wave DFT software: https://www.abinit.org/

## Workflow steps

### Step 1: Generate adaptive local basis functions (ALBs)
- Role: process
- Action: Partition the supercell into 6×6×6 rectangular elements (each element corresponds to a conventional BCC unit cell containing 2 Na atoms) and their extended elements. For each element, solve the local Kohn-Sham problem in the extended element using plane-wave DFT with the HGH pseudopotential, with the potential taken from the current electron density (or initial guess). Truncate to exactly 42 ALBs per atom and orthonormalize via Gram-Schmidt. This produces orthonormal adaptive local basis functions supported on each element, which serve as the primitive basis for EO construction.
- Evidence: `/app/outputs/alb_generation.log`

### Step 2: Construct element orbitals (EOs) from ALBs
- Role: process
- Action: Assemble the global discontinuous Galerkin Hamiltonian matrix in the ALB basis. For each element, extract the local Hamiltonian submatrix restricted to ALBs in its extended element, diagonalize to obtain low-energy candidate functions, then solve the localization generalized eigenvalue problem using a weight function with a localization radius of 6.0 a.u. to select exactly 4 localized EOs per atom. Build the global EO coefficient matrix.
- Evidence: `/app/outputs/eo_construction.log`

### Step 3: Compute total free energy per atom vs lattice constant
- Role: scored (load-bearing)
- Action: For each lattice constant in {7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9} a.u., set up the BCC Na supercell with 432 atoms accordingly, initialize electron density, and perform self-consistent field iterations in the EO basis until convergence. Record the converged total free energy per atom. Output all results to a CSV file.
- Output file: `/app/outputs/na_lattice_energies.csv`
- Format: csv
- Contract: Header: lattice_constant, total_free_energy_per_atom. Each row: lattice_constant (float, in atomic units), total_free_energy_per_atom (float, in Hartree).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/na_lattice_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### na_lattice_energies.csv
- path: `/app/outputs/na_lattice_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total free energy per atom of the 432-atom BCC Na supercell for lattice constants from 7.3 to 7.9 a.u. The checker will compare these energies against hidden reference values (the paper's EO-based results) and compute a mean absolute error (MAE). The reward is 1.0 if the MAE is below a hidden accuracy threshold, and decays linearly to 0 for larger errors. Lower MAE is always better.
- schema:
  - `type`: table
  - `required_columns`: `lattice_constant`, `total_free_energy_per_atom`
  - `units`:
    - `lattice_constant`: a.u.
    - `total_free_energy_per_atom`: Hartree

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "na_lattice_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice_constant",
          "total_free_energy_per_atom"
        ],
        "units": {
          "lattice_constant": "a.u.",
          "total_free_energy_per_atom": "Hartree"
        }
      },
      "description": "Total free energy per atom of the 432-atom BCC Na supercell for lattice constants from 7.3 to 7.9 a.u. The checker will compare these energies against hidden reference values (the paper's EO-based results) and compute a mean absolute error (MAE). The reward is 1.0 if the MAE is below a hidden accuracy threshold, and decays linearly to 0 for larger errors. Lower MAE is always better."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your CSV file. For each lattice constant, the verifier compares your `total_free_energy_per_atom` value to a hidden reference value by computing the absolute difference. It then calculates the mean absolute error (MAE) over all seven lattice constants. You receive full credit if the MAE is below a hidden accuracy threshold; the score decreases linearly as the MAE grows, reaching zero when the MAE exceeds an upper bound. The exact thresholds are hidden; aim to produce the most accurate energies your implementation can achieve. The verifier also checks that the CSV format and column headers match the specification exactly.
