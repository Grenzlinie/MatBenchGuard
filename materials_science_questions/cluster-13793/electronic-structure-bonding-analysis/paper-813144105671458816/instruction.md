# First-Principles Band Gaps and Optical Properties of MgYZ2 Chalcopyrites

## Problem background
MgYZ₂ (Y=Si, Ge; Z=N, P) chalcopyrite semiconductors are of interest for optoelectronic and photovoltaic technologies. A thorough understanding of their electronic band structure and optical response is needed for device design. This task reproduces a first-principles investigation of the electronic and optical properties of four MgYZ₂ compounds. Specifically, you will compute the direct band gaps at the Γ point using two exchange-correlation functionals, and extract the static (zero-frequency) refractive index, reflectivity, and the onset of optical conductivity for each compound.

## Approach
The method is based on density-functional theory using the full-potential linearized augmented plane-wave plus local orbitals (FP-LAPW+lo) framework, implemented in an open-source code (e.g., exciting, Elk, ABINIT). You will construct the crystal structures from the experimental chalcopyrite lattice parameters (a, c, internal parameter u) and muffin-tin radii. Self-consistent field (SCF) calculations are run with two exchange-correlation functionals: the conventional generalized-gradient approximation (GGA) and the Engel–Vosko variant (EV-GGA). From the converged band structures, you extract the direct band gap at Γ. Using the EV-GGA ground state, you compute the complex dielectric function and derive the frequency-dependent refractive index (parallel and perpendicular components), reflectivity, and optical conductivity. From these spectra, the zero-frequency (static) refractive index and reflectivity are recorded, and the critical point (absorption onset) of the optical conductivity is identified.

## Reproduction target
Your task is to produce three CSV files in `/app/outputs`:

1. `band_gaps_GGA.csv` – Header: `Compound, Eg_GGA (eV)`. Rows: MgSiN2, MgGeN2, MgSiP2, MgGeP2.
2. `band_gaps_EV.csv` – Header: `Compound, Eg_EV (eV)`. Same row order.
3. `optical_static.csv` – Header: `Compound, n_par_0, n_perp_0, R_par_0 (%), R_perp_0 (%), critical_point (eV)`. Same row order. The units are: refractive indices dimensionless, reflectivity in percent, critical point in eV.

The values must be extracted from the DFT calculations as described in the workflow steps; reporting pre-existing numbers will not satisfy the scoring criteria.

## Assets

- All-electron DFT code capable of band structure and optical calculations (e.g., exciting, Elk, ABINIT): http://exciting-code.org

## Workflow steps

### Step 1: Crystal structure setup
- Role: process
- Action: Construct input crystal structures for MgSiN2, MgGeN2, MgSiP2, and MgGeP2 in the chalcopyrite phase using experimental lattice constants (a, c), internal parameter u, and muffin-tin radii R_MT. Create input files for the chosen DFT code.
- Evidence: `/app/outputs/step_01_structures.log`

### Step 2: SCF calculation with GGA
- Role: process
- Action: Perform self-consistent field (SCF) calculations for each compound using the conventional generalized-gradient approximation (GGA) exchange-correlation functional. Use the computational parameters: R_MT·K_max = 7, l_max = 10, a k-mesh of 99 k-points in the irreducible Brillouin zone, and a charge-convergence threshold of 0.001 Ry.
- Evidence: `/app/outputs/step_02_GGA_scf.log`

### Step 3: GGA direct band gaps
- Role: scored (load-bearing)
- Action: From the GGA SCF band structure, extract the direct band gap value at the Γ point for each compound and write the results to band_gaps_GGA.csv.
- Output file: `/app/outputs/band_gaps_GGA.csv`
- Format: csv
- Contract: Header: Compound, Eg_GGA (eV). Rows: MgSiN2, MgGeN2, MgSiP2, MgGeP2 (that order).
- Scoring: scored by hidden verifier

### Step 4: SCF calculation with EV-GGA
- Role: process
- Action: Repeat the SCF calculation for all compounds using the Engel–Vosko variant of GGA (EV-GGA), keeping the same numerical parameters.
- Evidence: `/app/outputs/step_04_EV_scf.log`

### Step 5: EV-GGA direct band gaps
- Role: scored (load-bearing)
- Action: From the EV-GGA SCF band structure, extract the direct band gap at Γ for each compound and write band_gaps_EV.csv.
- Output file: `/app/outputs/band_gaps_EV.csv`
- Format: csv
- Contract: Header: Compound, Eg_EV (eV). Rows: MgSiN2, MgGeN2, MgSiP2, MgGeP2 (same order as band_gaps_GGA.csv).
- Scoring: scored by hidden verifier

### Step 6: Optical property calculation
- Role: process
- Action: Using the EV-GGA SCF eigenvalues and momentum matrix elements, calculate the complex dielectric function, then derive the refractive index (parallel and perpendicular components), reflectivity, and optical conductivity spectra for each compound.
- Evidence: `/app/outputs/step_06_optical_calc.log`

### Step 7: Static optical constants and critical point
- Role: scored (load-bearing)
- Action: From the computed optical spectra, extract the zero-frequency (static) values of the refractive index components n‖(0) and n⊥(0), the static reflectivity R‖(0) and R⊥(0) (in %), and the critical point (onset energy) of the optical conductivity. Write these quantities to optical_static.csv.
- Output file: `/app/outputs/optical_static.csv`
- Format: csv
- Contract: Header: Compound, n_par_0, n_perp_0, R_par_0 (%), R_perp_0 (%), critical_point (eV). Rows: MgSiN2, MgGeN2, MgSiP2, MgGeP2 (same order).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps_GGA.csv`
- `/app/outputs/band_gaps_EV.csv`
- `/app/outputs/optical_static.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps_GGA.csv
- path: `/app/outputs/band_gaps_GGA.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: GGA direct band gaps at Γ point for MgSiN2, MgGeN2, MgSiP2, MgGeP2.
- schema:
  - `type`: table
  - `required_columns`: `Compound`, `Eg_GGA (eV)`
  - `units`:
    - `Eg_GGA (eV)`: eV

### band_gaps_EV.csv
- path: `/app/outputs/band_gaps_EV.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: EV-GGA direct band gaps at Γ point for the four compounds.
- schema:
  - `type`: table
  - `required_columns`: `Compound`, `Eg_EV (eV)`
  - `units`:
    - `Eg_EV (eV)`: eV

### optical_static.csv
- path: `/app/outputs/optical_static.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Static (zero-frequency) refractive index, reflectivity, and optical conductivity critical point for the four compounds.
- schema:
  - `type`: table
  - `required_columns`: `Compound`, `n_par_0`, `n_perp_0`, `R_par_0 (%)`, `R_perp_0 (%)`, `critical_point (eV)`
  - `units`:
    - `n_par_0`: dimensionless
    - `n_perp_0`: dimensionless
    - `R_par_0 (%)`: %
    - `R_perp_0 (%)`: %
    - `critical_point (eV)`: eV

Notes: All output CSV files follow the same compound order: MgSiN2, MgGeN2, MgSiP2, MgGeP2. The static optical constants are extracted from the EV-GGA spectra.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps_GGA.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Compound",
          "Eg_GGA (eV)"
        ],
        "units": {
          "Eg_GGA (eV)": "eV"
        }
      },
      "description": "GGA direct band gaps at Γ point for MgSiN2, MgGeN2, MgSiP2, MgGeP2."
    },
    {
      "file": "band_gaps_EV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Compound",
          "Eg_EV (eV)"
        ],
        "units": {
          "Eg_EV (eV)": "eV"
        }
      },
      "description": "EV-GGA direct band gaps at Γ point for the four compounds."
    },
    {
      "file": "optical_static.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Compound",
          "n_par_0",
          "n_perp_0",
          "R_par_0 (%)",
          "R_perp_0 (%)",
          "critical_point (eV)"
        ],
        "units": {
          "n_par_0": "dimensionless",
          "n_perp_0": "dimensionless",
          "R_par_0 (%)": "%",
          "R_perp_0 (%)": "%",
          "critical_point (eV)": "eV"
        }
      },
      "description": "Static (zero-frequency) refractive index, reflectivity, and optical conductivity critical point for the four compounds."
    }
  ],
  "notes": "All output CSV files follow the same compound order: MgSiN2, MgGeN2, MgSiP2, MgGeP2. The static optical constants are extracted from the EV-GGA spectra."
}
```

## How you are scored
A hidden verifier reads each CSV file and compares every numeric field to a hidden reference. Scoring uses a threshold-or-better policy: a result that meets or exceeds the reference in the favorable direction earns full credit for that field; credit decreases monotonically as the result gets worse. The final reward is a weighted combination of the scores from all three files. Your CSV files must follow exactly the format, column names, and row ordering specified; any deviation will prevent the verifier from reading the data.
