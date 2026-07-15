# Ab Initio Calculation of Scattering Factors, Compton Profiles, and J(0) Surface for Benzene

## Problem background
Electron momentum-space properties such as Compton profiles and scattering factors provide complementary insight into molecular electronic structure. The directional Compton profile (DCP) measures the momentum density integrated over planes perpendicular to a chosen scattering vector, while molecular scattering factors represent the Fourier transform of the position‑space electron density. The J(0) surface—the set of directional Compton profiles evaluated at zero momentum transfer—is a compact visualisation tool that highlights the anisotropy of the momentum distribution in a molecule. This task reproduces an ab initio computation of directional Compton profiles, isotropic Compton profile, molecular scattering factors per electron, and the J(0) surface for benzene, a planar aromatic molecule that serves as a model system for studying directional effects.

## Approach
The reproduction is built around a restricted Hartree‑Fock calculation with a minimal STO‑3G basis set. Using the molecular geometry from the original work (C–C bond length 1.397 Å, C–H 1.084 Å, molecule lying in the xy plane with two C–C bonds parallel to the y‑axis), a molecular wavefunction (orbital coefficients) is obtained. From this wavefunction the electron momentum density is derived. Directional Compton profiles J(q e) are evaluated by integrating the momentum density over planes perpendicular to unit vector e at various momentum transfer magnitudes q. The isotropic Compton profile is computed as the spherical average of the directional profiles. Scattering factors per electron F(s)/N are obtained from the position‑space charge density via a Fourier transform along selected scattering vectors. The J(0) surface is constructed by evaluating the directional Compton profile at zero momentum transfer for a dense set of directions covering a hemisphere. The computed quantities are written as structured CSV files; no external datasets are needed—the calculation relies only on the wavefunction obtained in the first step.

## Reproduction target
You must produce three CSV files inside `/app/outputs` by faithfully executing the ordered workflow steps below:

1. **scattering_factors.csv** – a table of scattering factors per electron for scattering vectors along the molecular x, y, and z directions. The file must contain columns `s`, `F_x_N`, `F_y_N`, `F_z_N` (all dimensionless except s in atomic units) for the exact list of s values specified in Step 2.

2. **compton_profiles.csv** – a table of directional Compton profiles J(q eₓ), J(q e_y), J(q e_z) and the isotropic Compton profile J_iso(q) for a prescribed list of momentum transfer magnitudes q (atomic units). The required columns are `q`, `J_x`, `J_y`, `J_z`, `J_iso`, each in electrons per atomic unit.

3. **jzero_surface.csv** – a table of J(0) values, i.e. directional Compton profiles at |q|=0, for a hemisphere of scattering directions. Use a grid of polar angle θ (0° to 90°) and azimuthal angle φ (0° to 360°) with an angular step no larger than 5°. Columns: `theta_deg`, `phi_deg`, `J0` (electrons/a.u.).

All output files must adhere to the contract and schemas detailed in the workflow steps and the output contract section.

## Assets

- Open‑source quantum chemistry package supporting STO‑3G (e.g., PySCF): https://github.com/pyscf/pyscf

## Workflow steps

### Step 1: SCF‑LCAO‑MO wavefunction calculation for benzene
- Role: process
- Action: Perform a restricted Hartree‑Fock calculation with the STO‑3G basis on benzene using the molecular geometry: CC=1.397 Å, CH=1.084 Å, molecule in the xy plane with two CC bonds parallel to the y‑axis. Obtain the wavefunction (orbital coefficients) and total energy.
- Evidence: `/app/outputs/benzene_energy.txt`

### Step 2: Compute scattering factors
- Role: scored (load-bearing)
- Action: Using the wavefunction from step1, evaluate the molecular scattering factors per electron F(s)/N for scattering vectors along x, y, and z directions at the s values 0.000, 0.1330, 0.2660, 0.3990, 0.5320, 0.6650, 0.7980, 0.9310, 1.0640, 1.1970, 1.3299, 1.9949, 2.6599, 3.3249 a.u. Output a CSV with columns s, F_x_N, F_y_N, F_z_N.
- Output file: `/app/outputs/scattering_factors.csv`
- Format: csv
- Contract: s (float, a.u.), F_x_N (float, dimensionless), F_y_N (float, dimensionless), F_z_N (float, dimensionless)
- Scoring: scored by hidden verifier

### Step 3: Compute directional and isotropic Compton profiles
- Role: scored
- Action: Using the wavefunction from step1, compute the directional Compton profiles J(q e_x), J(q e_y), J(q e_z) and the isotropic Compton profile J_iso(q) at the q values 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3.0, 4.0, 5.0 a.u. Output a CSV with columns q, J_x, J_y, J_z, J_iso.
- Output file: `/app/outputs/compton_profiles.csv`
- Format: csv
- Contract: q (float, a.u.), J_x (float, electrons/a.u.), J_y (float, electrons/a.u.), J_z (float, electrons/a.u.), J_iso (float, electrons/a.u.)
- Scoring: scored by hidden verifier

### Step 4: Generate J(0) surface data
- Role: scored
- Action: For a hemisphere of scattering directions (polar angle theta 0° to 90°, azimuthal angle phi 0° to 360°, at a resolution of at most 5°), compute the directional Compton profile J(q) at |q|=0 using the wavefunction from step1. Output the raw J(0) values (without any constant subtraction) as a CSV with columns theta_deg, phi_deg, J0.
- Output file: `/app/outputs/jzero_surface.csv`
- Format: csv
- Contract: theta_deg (float, degrees), phi_deg (float, degrees), J0 (float, electrons/a.u.)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scattering_factors.csv`
- `/app/outputs/compton_profiles.csv`
- `/app/outputs/jzero_surface.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scattering_factors.csv
- path: `/app/outputs/scattering_factors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Directional scattering factors per electron for benzene. The hidden checker compares each value to the paper‑reported values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `s`, `F_x_N`, `F_y_N`, `F_z_N`
  - `units`:
    - `s`: a.u.
    - `F_x_N`: dimensionless
    - `F_y_N`: dimensionless
    - `F_z_N`: dimensionless

### compton_profiles.csv
- path: `/app/outputs/compton_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Directional and isotropic Compton profiles of benzene. Checked against paper‑reported values.
- schema:
  - `type`: table
  - `required_columns`: `q`, `J_x`, `J_y`, `J_z`, `J_iso`
  - `units`:
    - `q`: a.u.
    - `J_x`: electrons/a.u.
    - `J_y`: electrons/a.u.
    - `J_z`: electrons/a.u.
    - `J_iso`: electrons/a.u.

### jzero_surface.csv
- path: `/app/outputs/jzero_surface.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: J(0) surface data. Checked against paper values and structural features (flat region for theta<30°, sixfold star pattern for 30°<theta<90°, J0_z lower than J0_x and J0_y).
- schema:
  - `type`: table
  - `required_columns`: `theta_deg`, `phi_deg`, `J0`
  - `units`:
    - `theta_deg`: degrees
    - `phi_deg`: degrees
    - `J0`: electrons/a.u.

Notes: Result-level comparison (T0) against paper‑reported values with appropriate relative tolerances. The J(0) surface also undergoes structural pattern verification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scattering_factors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "s",
          "F_x_N",
          "F_y_N",
          "F_z_N"
        ],
        "units": {
          "s": "a.u.",
          "F_x_N": "dimensionless",
          "F_y_N": "dimensionless",
          "F_z_N": "dimensionless"
        }
      },
      "description": "Directional scattering factors per electron for benzene. The hidden checker compares each value to the paper‑reported values within tolerance."
    },
    {
      "file": "compton_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q",
          "J_x",
          "J_y",
          "J_z",
          "J_iso"
        ],
        "units": {
          "q": "a.u.",
          "J_x": "electrons/a.u.",
          "J_y": "electrons/a.u.",
          "J_z": "electrons/a.u.",
          "J_iso": "electrons/a.u."
        }
      },
      "description": "Directional and isotropic Compton profiles of benzene. Checked against paper‑reported values."
    },
    {
      "file": "jzero_surface.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta_deg",
          "phi_deg",
          "J0"
        ],
        "units": {
          "theta_deg": "degrees",
          "phi_deg": "degrees",
          "J0": "electrons/a.u."
        }
      },
      "description": "J(0) surface data. Checked against paper values and structural features (flat region for theta<30°, sixfold star pattern for 30°<theta<90°, J0_z lower than J0_x and J0_y)."
    }
  ],
  "notes": "Result-level comparison (T0) against paper‑reported values with appropriate relative tolerances. The J(0) surface also undergoes structural pattern verification."
}
```

## How you are scored
A hidden verifier will automatically score your submission after the task finishes. For each of the three scored output files the verifier reads your numeric values and compares them to a hidden reference derived from the original paper’s published results. The comparison uses appropriate relative tolerances that allow for small differences arising from the use of a different quantum chemistry package or minor implementation details, while still requiring a genuine ab initio recalculation. For the J(0) surface the verifier also checks that the surface exhibits the qualitatively expected symmetry and structural features (a flat region near the polar axis and a six‑fold pattern near the molecular plane). The final reward is a weighted sum of scores from the three output checks, with the scattering factor and Compton profile tables carrying the bulk of the weight. Merely reporting approximate numbers or copying a guessed value is not sufficient—the verifier requires a physically meaningful result obtained by running the SCF calculation and evaluating the properties as described.
