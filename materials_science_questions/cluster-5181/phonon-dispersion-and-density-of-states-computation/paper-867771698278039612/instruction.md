# First-principles computation of phonon Hall conductivity in ionic crystals

## Problem background
The phonon Hall effect (PHE) is the thermal Hall conductivity carried by phonons in insulating crystals under an external magnetic field. This work develops a first-principles computational workflow combining density functional theory (DFT), anharmonic self-consistent phonon (SCPH) theory, and Berry-curvature topological analysis to compute the phonon Hall conductivity \(\kappa_{xy}\) for real materials. The main targets are benchmark values for sodium chloride (NaCl) and barium titanate (BaTiO₃), providing an assessment of the role of soft optical modes and spin-phonon coupling in the PHE.

## Approach
The technique uses three open-source computational packages: Quantum-Espresso for first-principles DFT calculations, and ALAMODE for anharmonic lattice dynamics. The workflow proceeds in two parallel pipelines — one for NaCl and one for BaTiO₃ — each consisting of: (i) DFT structure optimization and generation of finite-displacement force data for the chosen supercell, along with extraction of Born effective charge tensors; (ii) fitting of harmonic, third-order, and fourth-order interatomic force constants (IFCs) from the DFT forces; (iii) self-consistent phonon (SCPH) calculations to obtain temperature-dependent dynamical matrices that include nonanalytic LO-TO corrections; (iv) construction of the effective antisymmetric vector potential A matrix from the Born effective charges and an external magnetic field (the spin-phonon interaction); (v) solution of the generalized phonon eigenproblem to obtain eigenfrequencies and eigenvectors; (vi) computation of the phonon Berry curvature using a regularized sum-over-states formula with a small phenomenological broadening; and (vii) summation of weighted Berry curvatures over the Brillouin zone using the analytic Θ-function to obtain the phonon Hall conductivity \(\kappa_{xy}\). The computed \(\kappa_{xy}\) values are collected over specified magnetic field and temperature points, enabling a direct comparison of the two materials and an evaluation of the conductivity’s dependence on field and temperature.

## Reproduction target
Compute the phonon Hall conductivity \(\kappa_{xy}\) (in W/(m·K)) for NaCl and BaTiO₃ under the following conditions and save the results as CSV tables:

- For NaCl: \(\kappa_{xy}\) vs. magnetic field at fixed temperatures 50 K and 100 K (fields 0, 1 × 10⁴, 5 × 10⁴, 1 × 10⁵, 2 × 10⁵, 3 × 10⁵, 4 × 10⁵, 5 × 10⁵ T), and \(\kappa_{xy}\) vs. temperature at fixed fields 3 × 10⁵ T and 5 × 10⁵ T (temperatures 10, 20, 30, 50, 70, 100, 150, 200, 300 K). Save to `step_04_kappa_NaCl.csv`.
- For BaTiO₃: \(\kappa_{xy}\) vs. magnetic field at fixed temperature 60 K (fields 0, 2, 4, 8, 12, 16 T), and \(\kappa_{xy}\) vs. temperature at fixed field 16 T (temperatures 50, 70, 100, 150, 200, 250, 300 K). Save to `step_05_kappa_BTO.csv`.

Each CSV must have columns: `magnetic_field_T` (float), `temperature_K` (float), `kappa_xy_W_mK` (float). The target is to produce physically grounded, internally consistent conductivity values that follow the applied field and temperature variations.

## Assets

- Quantum-Espresso: https://www.quantum-espresso.org/
- ALAMODE: https://alamode.readthedocs.io/en/latest/
- PAW-PBE pseudopotentials for Na and Cl: https://www.materialscloud.org/discover/sssp/
- PAW-PBE pseudopotentials for Ba, Ti, and O: https://www.materialscloud.org/discover/sssp/
- Crystal structures of rocksalt NaCl and cubic BaTiO₃

## Workflow steps

### Step 1: DFT relaxation and force data for NaCl
- Role: process
- Action: Perform DFT structure optimization for NaCl using Quantum-Espresso with PAW-PBE pseudopotentials, then generate finite-displacement force data for a 2x2x3 supercell. Extract the Born effective charge tensors.
- Evidence: none

### Step 2: Extract interatomic force constants (IFCs) for NaCl
- Role: process
- Action: Use ALAMODE to fit harmonic, third-order, and fourth-order interatomic force constants from the DFT force/displacement data.
- Evidence: none

### Step 3: Self-consistent phonon calculation for NaCl
- Role: process
- Action: Run the SCPH method (ALAMODE) to obtain temperature-dependent dynamical matrices D_q(T) for NaCl. Include nonanalytic LO-TO corrections via the mixed-space approach.
- Evidence: none

### Step 4: Compute Berry curvature and phonon Hall conductivity for NaCl
- Role: scored (load-bearing)
- Action: For NaCl: construct the effective antisymmetric A matrix from Born effective charges and the magnetic field vector; solve the generalized phonon eigenproblem to obtain eigenfrequencies and eigenvectors; compute the phonon Berry curvature using a regularized sum-over-states formula with a small phenomenological broadening; sum weighted Berry curvatures over the Brillouin zone using the analytic Θ-function to obtain the phonon Hall conductivity κ_xy at each required (B,T) point. Write results to step_04_kappa_NaCl.csv.
- Output file: `/app/outputs/step_04_kappa_NaCl.csv`
- Format: csv
- Contract: Columns: magnetic_field_T (float), temperature_K (float), kappa_xy_W_mK (float). Rows cover: magnetic fields 0, 1e4, 5e4, 1e5, 2e5, 3e5, 4e5, 5e5 T at T=50 K and T=100 K; and temperatures 10, 20, 30, 50, 70, 100, 150, 200, 300 K at B=3e5 T and B=5e5 T.
- Scoring: scored by hidden verifier

### Step 5: DFT relaxation and force data for BaTiO₃
- Role: process
- Action: Perform DFT structure optimization for cubic BaTiO₃ using Quantum-Espresso with PAW-PBE pseudopotentials, then generate finite-displacement force data for a 2x2x3 supercell. Extract the Born effective charge tensors.
- Evidence: none

### Step 6: Extract IFCs for BaTiO₃
- Role: process
- Action: Use ALAMODE to fit harmonic, third-order, and fourth-order IFCs from the BTO DFT force/displacement data.
- Evidence: none

### Step 7: Self-consistent phonon calculation for BaTiO₃
- Role: process
- Action: Run the SCPH method to obtain temperature-dependent dynamical matrices D_q(T) for BTO, including LO-TO splitting.
- Evidence: none

### Step 8: Compute Berry curvature and phonon Hall conductivity for BaTiO₃
- Role: scored
- Action: For BTO: construct the A matrix, solve the generalized eigenproblem, compute Berry curvatures (same regularized sum-over-states approach), and sum with the Θ-function to obtain κ_xy at each required (B,T) point. Write results to step_05_kappa_BTO.csv.
- Output file: `/app/outputs/step_05_kappa_BTO.csv`
- Format: csv
- Contract: Columns: magnetic_field_T (float), temperature_K (float), kappa_xy_W_mK (float). Rows cover: magnetic fields 0, 2, 4, 8, 12, 16 T at T=60 K; and temperatures 50, 70, 100, 150, 200, 250, 300 K at B=16 T.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_kappa_NaCl.csv`
- `/app/outputs/step_05_kappa_BTO.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_kappa_NaCl.csv
- path: `/app/outputs/step_04_kappa_NaCl.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed phonon Hall conductivity of NaCl under specified (B,T) conditions, compared against hidden gold values from the reference paper.
- schema:
  - `type`: table
  - `required_columns`: `magnetic_field_T`, `temperature_K`, `kappa_xy_W_mK`
  - `units`:
    - `magnetic_field_T`: T
    - `temperature_K`: K
    - `kappa_xy_W_mK`: W/(m·K)

### step_05_kappa_BTO.csv
- path: `/app/outputs/step_05_kappa_BTO.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed phonon Hall conductivity of BaTiO₃ under specified (B,T) conditions, compared against hidden gold values from the reference paper.
- schema:
  - `type`: table
  - `required_columns`: `magnetic_field_T`, `temperature_K`, `kappa_xy_W_mK`
  - `units`:
    - `magnetic_field_T`: T
    - `temperature_K`: K
    - `kappa_xy_W_mK`: W/(m·K)

Notes: Both CSVs must be present; the checker compares agent-reported κ_xy values to hidden gold (digitized from the reference paper) using a relative tolerance and sign agreement per (B,T) point. Missing rows or sign errors reduce the score proportionally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_kappa_NaCl.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "magnetic_field_T",
          "temperature_K",
          "kappa_xy_W_mK"
        ],
        "units": {
          "magnetic_field_T": "T",
          "temperature_K": "K",
          "kappa_xy_W_mK": "W/(m·K)"
        }
      },
      "description": "Computed phonon Hall conductivity of NaCl under specified (B,T) conditions, compared against hidden gold values from the reference paper."
    },
    {
      "file": "step_05_kappa_BTO.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "magnetic_field_T",
          "temperature_K",
          "kappa_xy_W_mK"
        ],
        "units": {
          "magnetic_field_T": "T",
          "temperature_K": "K",
          "kappa_xy_W_mK": "W/(m·K)"
        }
      },
      "description": "Computed phonon Hall conductivity of BaTiO₃ under specified (B,T) conditions, compared against hidden gold values from the reference paper."
    }
  ],
  "notes": "Both CSVs must be present; the checker compares agent-reported κ_xy values to hidden gold (digitized from the reference paper) using a relative tolerance and sign agreement per (B,T) point. Missing rows or sign errors reduce the score proportionally."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact and combines them by weight into a final reward in [0,1]. For each scored CSV, the verifier compares your reported \(\kappa_{xy}\) values against hidden reference results at the same field‑temperature points. Points are awarded based on agreement within a prescribed relative tolerance and on correct sign (positive/negative) of the conductivity. Missing data points or sign errors reduce the score proportionally. Both NaCl and BTO outputs must be present; absence of one output table reduces the maximum possible score. The verifier does not credit merely stating expected numbers — it checks consistency of the full CSV against the underlying reference dataset.
