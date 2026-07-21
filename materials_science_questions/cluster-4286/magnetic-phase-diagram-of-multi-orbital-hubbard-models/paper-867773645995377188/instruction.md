# Compute ground-state energy, gap, and magnetization for the half-filled 1D Hubbard chain with open and twisted boundary conditions

## Problem background
The one-dimensional Hubbard model describes strongly correlated electrons on a chain with on-site Coulomb repulsion U and nearest-neighbor hopping t0. For finite-size systems the choice of boundary conditions—open, periodic, or twisted—affects the symmetries (translation, particle-hole, inversion) and therefore influences how rapidly ground-state properties converge to the infinite-lattice limit. At half-filling the Hamiltonian is particle-hole symmetric, and twisted boundary conditions with a special torsion can preserve both translational and particle-hole symmetry, while open boundary conditions break translation but retain particle-hole symmetry. Understanding the effect of boundary conditions on the ground-state energy, the energy gap, and the magnetization density is crucial for nanoscale applications and for extrapolating finite-size numerical calculations to the thermodynamic limit. This task requires numerically computing these quantities for a finite Hubbard chain under open and twisted boundary conditions.

## Approach
Implement the half-filled one-dimensional Hubbard Hamiltonian on a chain of L sites with real nearest-neighbor hopping t0 and on-site Coulomb repulsion U. Employ two boundary conditions: open (τ = 0) and twisted with the special torsion Θ = πL/2 (τ = t0 exp(iΘ)). Exploit conservation laws to work in sectors with fixed particle number and spin. For odd L, the half-filled ground state lies in the sector with N = L electrons and total spin z‑component Sz = 1/2. Construct the many-body Hamiltonian matrix in that sector and diagonalize it numerically to obtain eigenvalues and the ground‑state eigenvector. To compute the energy gap, also diagonalize the Hamiltonian in the sector with N = L − 1 electrons. The ground‑state energy per site is obtained by dividing the lowest eigenvalue by L. The energy gap is the difference between the lowest eigenvalue of the N = L − 1 sector and the ground‑state energy of the N = L sector. For the magnetization density, use the ground‑state eigenvector for L = 3 under OBC to evaluate the expectation value of the local spin operator ⟨n_{ℓ↑} − n_{ℓ↓}⟩ at each site. Perform the calculations for a sequence of U/t0 values and record the results in CSV files. The computed energies, gaps, and magnetizations will be compared against a hidden reference by the verifier.

## Reproduction target
Compute the ground‑state energy per site and the energy gap for the half-filled 1D Hubbard chain of lengths L = 3, 5, 7 under open boundary conditions (OBC) and twisted boundary conditions (TBC) with torsion Θ = πL/2. Use a range of U/t0 values (e.g., U/t0 = 0, 2, 4, 8, 16, 32, 64, 128). Compute the site‑resolved magnetization density for L = 3 under OBC at the same U/t0 values. Write the results to the following CSV files with the specified columns:

- `/app/outputs/ground_state_energy.csv`: L (int), BC (str: OBC or TBC), U (float), E_per_site (float)
- `/app/outputs/energy_gap.csv`: L (int), BC (str: OBC or TBC), U (float), gap (float)
- `/app/outputs/magnetization_L3_OBC.csv`: U (float), site (int: 1,2,3), magnetization (float)

The verifier will compare these artifacts to reference data and assign a score.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Construct and diagonalize the finite-size Hubbard Hamiltonian
- Role: process
- Action: Implement the half-filled Hubbard Hamiltonian on a 1D chain of L sites with open (OBC) and twisted (TBC, Θ = πL/2) boundary conditions. For each L in {3, 5, 7}, each BC, and each U/t0 in the sequence 0, 2, 4, 8, 16, 32, 64, 128, construct the many-body Hamiltonian matrix in the appropriate symmetry sector (N=L, Sz=1/2) and diagonalize it to obtain eigenvalues and eigenvectors. For the gap computation, also diagonalize the N=L−1 sectors. For magnetization, compute the ground-state expectation values of the spin density operator.
- Evidence: `/app/outputs/diagonalization_log.txt`

### Step 2: Produce ground-state energy per site
- Role: scored (load-bearing)
- Action: Extract the lowest eigenvalue from the N=L diagonalizations and normalize by L. Write the results to ground_state_energy.csv.
- Output file: `/app/outputs/ground_state_energy.csv`
- Format: csv
- Contract: Columns: L (int), BC (str: OBC or TBC), U (float, U/t0), E_per_site (float)
- Scoring: scored by hidden verifier

### Step 3: Produce energy gap
- Role: scored
- Action: For each L, BC, U, compute the energy gap as the lowest eigenvalue of the N=L−1 sector minus the ground-state energy of the N=L sector. Write the results to energy_gap.csv.
- Output file: `/app/outputs/energy_gap.csv`
- Format: csv
- Contract: Columns: L (int), BC (str: OBC or TBC), U (float, U/t0), gap (float)
- Scoring: scored by hidden verifier

### Step 4: Produce magnetization density for L=3 OBC
- Role: scored
- Action: From the ground-state eigenvector for L=3 under OBC at each U, compute the site-resolved magnetization m_ℓ = ⟨n_ℓ↑ − n_ℓ↓⟩. Write the results to magnetization_L3_OBC.csv.
- Output file: `/app/outputs/magnetization_L3_OBC.csv`
- Format: csv
- Contract: Columns: U (float, U/t0), site (int: 1,2,3), magnetization (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ground_state_energy.csv`
- `/app/outputs/energy_gap.csv`
- `/app/outputs/magnetization_L3_OBC.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ground_state_energy.csv
- path: `/app/outputs/ground_state_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per‑site ground‑state energies for L=3,5,7 under OBC and TBC (Θ=πL/2) at multiple U/t0 values.
- schema:
  - `type`: table
  - `required_columns`: `L`, `BC`, `U`, `E_per_site`
  - `units`:
    - `U`: U/t0
    - `E_per_site`: t0

### energy_gap.csv
- path: `/app/outputs/energy_gap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energy gaps (E(N=L-1) - E(N=L)) for L=3,5,7 under OBC and TBC at multiple U/t0.
- schema:
  - `type`: table
  - `required_columns`: `L`, `BC`, `U`, `gap`
  - `units`:
    - `U`: U/t0
    - `gap`: t0

### magnetization_L3_OBC.csv
- path: `/app/outputs/magnetization_L3_OBC.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Site‑resolved magnetization density for the half‑filled L=3 Hubbard model under OBC at multiple U/t0.
- schema:
  - `type`: table
  - `required_columns`: `U`, `site`, `magnetization`
  - `units`:
    - `U`: U/t0

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ground_state_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "BC",
          "U",
          "E_per_site"
        ],
        "units": {
          "U": "U/t0",
          "E_per_site": "t0"
        }
      },
      "description": "Per‑site ground‑state energies for L=3,5,7 under OBC and TBC (Θ=πL/2) at multiple U/t0 values."
    },
    {
      "file": "energy_gap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "BC",
          "U",
          "gap"
        ],
        "units": {
          "U": "U/t0",
          "gap": "t0"
        }
      },
      "description": "Energy gaps (E(N=L-1) - E(N=L)) for L=3,5,7 under OBC and TBC at multiple U/t0."
    },
    {
      "file": "magnetization_L3_OBC.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "site",
          "magnetization"
        ],
        "units": {
          "U": "U/t0"
        }
      },
      "description": "Site‑resolved magnetization density for the half‑filled L=3 Hubbard model under OBC at multiple U/t0."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently inspects your three CSV artifacts and scores each one against a hidden reference. The ground-state energy per site, energy gap, and magnetization density are each checked for consistency within prescribed tolerances. The final reward is a weighted sum: `ground_state_energy.csv` contributes 0.4, `energy_gap.csv` contributes 0.4, and `magnetization_L3_OBC.csv` contributes 0.2. You must genuinely perform the exact diagonalization and compute the quantities; reporting arbitrary numbers will result in a low score because the verifier will detect discrepancies.
