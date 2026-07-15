# LCAO Interpolation and Recursion Method for Transition Metal Compounds

## Problem background
Transition-metal intermetallic compounds have complex electronic structures, and accurate band-structure calculations are usually performed with expensive first-principles methods (e.g., APW or KKR). For many practical purposes, such as interpreting X-ray spectra or estimating charge transfer, a simplified tight-binding model restricted to d-orbitals yields sufficient accuracy at drastically reduced computational cost. Moreover, the recursion method allows the calculation of local densities of states (LDOS) at individual atomic sites without explicitly computing wave functions or requiring translational symmetry. This task focuses on the d-band LCAO interpolation scheme and the recursion method applied to the CsCl-type intermetallic compound TiRu.

## Approach
The LCAO interpolation scheme is based on the Slater–Koster two-center tight-binding formalism, using only d-orbitals. The Hamiltonian includes on-site energies, crystal-field splittings (Δ¹, Δ²), and two-center hopping integrals (ddσ, ddπ, ddδ) between nearest and second-nearest neighbours. The parameters for TiRu (all energies in Rydberg) are:

| Parameter       | Value    |
|-----------------|----------|
| d₀¹             | 0.71573  |
| Δ¹               | 0.02100  |
| (ddσ)₂¹¹        | -0.03905 |
| (ddπ)₂¹¹        |  0.02331 |
| (ddδ)₂¹¹        |  0.00294 |
| d₀²             | 0.53866  |
| Δ²               | 0.01060  |
| (ddσ)₂²²        | -0.04001 |
| (ddπ)₂²²        |  0.02153 |
| (ddδ)₂²²        | -0.00067 |
| (ddσ)₁¹²        | -0.06530 |
| (ddπ)₁¹²        |  0.03713 |
| (ddδ)₁¹²        | -0.00410 |

These parameters describe the intrasite (first index 2) and intersite (index 1) hopping for Ti (superscript 1) and Ru (superscript 2) in the CsCl lattice.

**Total DOS via LCAO:** Construct the 10×10 tight-binding Hamiltonian for the two-atom unit cell using the parameters above, diagonalize it on a dense k-point mesh, and integrate the density of states with the tetrahedron method to obtain the total DOS per unit cell.

**Local DOS via recursion method:** Build a cluster of approximately 15 000 atoms with the CsCl structure. Starting from the five d-orbitals at either the Ti or Ru site, perform a Lanczos tridiagonalization to generate 16 pairs of recursion coefficients (aᵢ, bᵢ). Evaluate the continued fraction with constant-coefficient continuation and a small imaginary part (typically a few mRyd) to obtain the local DOS at that site. This procedure reproduces the local partial densities of states without diagonalizing the Hamiltonian.

## Reproduction target
Implement the workflows described above to produce the following three CSV files on a uniform energy grid spanning at least 0.3 to 0.9 Ryd:
- `total_dos.csv` – total density of states (states per Ryd per unit cell)
- `ldos_ti.csv` – local density of states at the Ti site (states per Ryd per atom)
- `ldos_ru.csv` – local density of states at the Ru site (states per Ryd per atom)

The hidden verifier will integrate each DOS curve over the energy grid to obtain the total number of d-electrons per unit cell and per atom, and will check that the results satisfy physical sum rules (for example, the integrated total DOS should be consistent with the expected number of d-electrons in the unit cell, and the sum of the site-projected LDOS should reconcile with the total DOS). It will also verify that all DOS values are non-negative and that the energy range covers the required interval.

## Assets

- Python scientific computing stack: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Compute LCAO total density of states
- Role: scored
- Action: Construct the d-orbital tight-binding Hamiltonian for TiRu (CsCl structure, lattice constant a=5.802 a.u.) using the Slater–Koster parameters provided in the instruction (on-site energies, crystal-field splittings, and two-center hopping integrals up to second-nearest neighbours). Diagonalize on a dense k-point mesh and apply the tetrahedron method to obtain the total density of states on a uniform energy grid spanning [0.3, 0.9] Ryd.
- Output file: `/app/outputs/total_dos.csv`
- Format: csv
- Contract: Columns: energy (Ryd), total_DOS (states per Ryd per unit cell)
- Scoring: scored by hidden verifier

### Step 2: Recursion method local density of states (Ti)
- Role: scored (load-bearing)
- Action: Using the same tight-binding Hamiltonian, build a cluster of approximately 15000 atoms with the CsCl structure. Starting from Ti d-orbitals, run the recursion method (Lanczos tridiagonalization) to compute 16 pairs of recursion coefficients, then evaluate the continued fraction with constant-coefficient continuation and a small imaginary part to obtain the local density of states at Ti sites on the same energy grid as step 01.
- Output file: `/app/outputs/ldos_ti.csv`
- Format: csv
- Contract: Columns: energy (Ryd), ldos_Ti (states per Ryd per atom)
- Scoring: scored by hidden verifier

### Step 3: Recursion method local density of states (Ru)
- Role: scored
- Action: Same recursion procedure as step 02, but starting from Ru d-orbitals to produce the Ru-site local density of states on the same energy grid.
- Output file: `/app/outputs/ldos_ru.csv`
- Format: csv
- Contract: Columns: energy (Ryd), ldos_Ru (states per Ryd per atom)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_dos.csv`
- `/app/outputs/ldos_ti.csv`
- `/app/outputs/ldos_ru.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_dos.csv
- path: `/app/outputs/total_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total density of states computed by the LCAO interpolation scheme. The checker integrates this curve and checks physical sum rules and non-negativity.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_DOS`
  - `units`:
    - `energy`: Ryd
    - `total_DOS`: states per Ryd per unit cell

### ldos_ti.csv
- path: `/app/outputs/ldos_ti.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Local density of states at Ti sites from the recursion method. The checker integrates this curve and verifies charge neutrality and non-negativity.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `ldos_Ti`
  - `units`:
    - `energy`: Ryd
    - `ldos_Ti`: states per Ryd per atom

### ldos_ru.csv
- path: `/app/outputs/ldos_ru.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Local density of states at Ru sites from the recursion method. The checker integrates this curve and verifies charge neutrality and non-negativity.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `ldos_Ru`
  - `units`:
    - `energy`: Ryd
    - `ldos_Ru`: states per Ryd per atom

Notes: The verification is performed by structural audit: integrating the DOS curves over the energy grid with the trapezoidal rule and checking that (1) total integrated DOS of total_dos.csv is 10 ± 0.5 d-electrons per unit cell, (2) integrated LDOS for Ti is 5 ± 0.25, (3) integrated LDOS for Ru is 5 ± 0.25, (4) all DOS values are non-negative, and (5) the energy range covers at least [0.4, 0.8] Ryd. The paper-reported values are used as hidden gold thresholds but are not revealed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_DOS"
        ],
        "units": {
          "energy": "Ryd",
          "total_DOS": "states per Ryd per unit cell"
        }
      },
      "description": "Total density of states computed by the LCAO interpolation scheme. The checker integrates this curve and checks physical sum rules and non-negativity."
    },
    {
      "file": "ldos_ti.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "ldos_Ti"
        ],
        "units": {
          "energy": "Ryd",
          "ldos_Ti": "states per Ryd per atom"
        }
      },
      "description": "Local density of states at Ti sites from the recursion method. The checker integrates this curve and verifies charge neutrality and non-negativity."
    },
    {
      "file": "ldos_ru.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "ldos_Ru"
        ],
        "units": {
          "energy": "Ryd",
          "ldos_Ru": "states per Ryd per atom"
        }
      },
      "description": "Local density of states at Ru sites from the recursion method. The checker integrates this curve and verifies charge neutrality and non-negativity."
    }
  ],
  "notes": "The verification is performed by structural audit: integrating the DOS curves over the energy grid with the trapezoidal rule and checking that (1) total integrated DOS of total_dos.csv is 10 ± 0.5 d-electrons per unit cell, (2) integrated LDOS for Ti is 5 ± 0.25, (3) integrated LDOS for Ru is 5 ± 0.25, (4) all DOS values are non-negative, and (5) the energy range covers at least [0.4, 0.8] Ryd. The paper-reported values are used as hidden gold thresholds but are not revealed to the agent."
}
```

## How you are scored
Your submission is scored by an automated verifier that reads the three CSV files. For each file, the verifier computes integrated quantities (e.g., total number of electrons) and compares them against physical constraints derived from the system, without revealing the exact thresholds. It also checks structural properties such as non-negativity of the DOS values and coverage of the energy grid. The individual checks are combined into a final reward between 0 and 1 that reflects how well your computed results satisfy the expected sum rules and shape constraints. Simply reporting numbers from the literature is not sufficient; your outputs must result from a correct implementation of the computational steps.
