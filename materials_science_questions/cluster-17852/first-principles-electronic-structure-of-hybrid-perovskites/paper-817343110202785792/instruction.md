# Comparative Optical Performance of Lead-Free Iron Perovskite via First-Principles

## Problem background
Perovskite solar cells have achieved high efficiencies but rely on lead-based absorbers, which pose serious environmental and health hazards. Replacing lead with a non-toxic, earth-abundant metal is a critical challenge. This work computationally investigates whether the iron perovskite CH3NH3FeI3 can serve as an alternative to the widely used lead perovskite CH3NH3PbI3. The study focuses on the optical performance of the two materials: how well their absorption coefficients align with the solar irradiance spectrum, and how Brewster-angle effects at the device interfaces (TiO2/perovskite and perovskite/spiro-OMeTAD) influence light harvesting. The task is to compute the wavelength-dependent absorption coefficients and refractive indices from first principles and submit them for a hidden comparative analysis.

## Approach
The reproduction employs density functional theory (DFT) within the generalized gradient approximation using the PBE functional. Starting from the experimentally known tetragonal crystal structure of MAPbI3 (space group I4cm), an initial structure for MAFeI3 is built by replacing Pb with Fe, preserving the same lattice symmetry. Both structures are then fully relaxed: unit cell volume, c/a ratio, and atomic positions are optimized. For each optimized structure, the frequency-dependent complex dielectric function ε(ω) is computed for the three Cartesian directions (xx, yy, zz). From these dielectric functions, the absorption coefficient α(λ) and the refractive index n(λ) are derived as a function of wavelength. The spectra are then used to assess optical performance via two indicators: (a) an optical correlation coefficient that integrates the absorption coefficient with a solar irradiance spectrum, and (b) a Brewster-angle factor that involves the refractive indices of the perovskite together with literature values for TiO2 and spiro-OMeTAD. The agent produces only the raw spectral data; the check of the correlation and Brewster-angle comparisons is performed by the hidden verifier.

## Reproduction target
Perform the described DFT calculations and submit two CSV files: `absorption_coefficients.csv` and `refractive_indices.csv`. The first file must contain wavelength (nm) and the absorption coefficients (cm⁻¹) for both perovskites along each Cartesian direction. The second file must contain wavelength (nm) and the corresponding refractive indices. The hidden verifier will use these spectra to compute the relative optical performance of MAFeI3 with respect to MAPbI3—specifically, the ratio of their optical correlation coefficients and a Brewster-angle performance factor. Your raw data must faithfully represent the calculated optical properties; the verifier will independently derive the comparison metrics.

## Assets

- Crystal structure of MAPbI3 (tetragonal, I4cm) from Dang et al. 2015: 10.5517/cc149n2d
- DFT code (e.g., Quantum ESPRESSO or Elk): https://www.quantum-espresso.org/
- Pseudopotentials for H, C, N, I, Fe, Pb: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Prepare initial crystal structures
- Role: process
- Action: Obtain the tetragonal crystal structure of MAPbI3 from CCDC deposition 1048128 (Dang et al., CrystEngComm 2015). Build the initial MAFeI3 structure by replacing Pb with Fe, keeping the same unit cell symmetry and approximate atomic positions.
- Evidence: `/app/outputs/initial_structures.txt`

### Step 2: Optimize unit cell and atomic positions
- Role: process
- Action: Using a DFT code with the PBE functional, optimize the unit cell volume and c/a ratio, then relax atomic positions until forces are converged, for both MAPbI3 and MAFeI3.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 3: Calculate dielectric function
- Role: process
- Action: For the optimized structures of both perovskites, compute the frequency-dependent complex dielectric function for each Cartesian direction (xx, yy, zz) using the PBE functional.
- Evidence: `/app/outputs/dielectric_calculation.log`

### Step 4: Derive absorption coefficient spectra
- Role: scored (load-bearing)
- Action: From the dielectric function components, compute the absorption coefficient α(λ) for each direction using the standard formula linking dielectric function to absorption. Output a CSV file with wavelength (nm) and the absorption coefficients for both perovskites.
- Output file: `/app/outputs/absorption_coefficients.csv`
- Format: csv
- Contract: wavelength_nm, alpha_Fe_xx_cm1, alpha_Fe_yy_cm1, alpha_Fe_zz_cm1, alpha_Pb_xx_cm1, alpha_Pb_yy_cm1, alpha_Pb_zz_cm1
- Scoring: scored by hidden verifier

### Step 5: Derive refractive index spectra
- Role: scored (load-bearing)
- Action: From the dielectric function, compute the refractive index n(λ) for each direction and output a CSV file with wavelength (nm) and the refractive indices for both perovskites.
- Output file: `/app/outputs/refractive_indices.csv`
- Format: csv
- Contract: wavelength_nm, n_Fe_xx, n_Fe_yy, n_Fe_zz, n_Pb_xx, n_Pb_yy, n_Pb_zz
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/absorption_coefficients.csv`
- `/app/outputs/refractive_indices.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### absorption_coefficients.csv
- path: `/app/outputs/absorption_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Absorption coefficient spectra for MAFeI3 and MAPbI3. The checker recomputes the optical correlation coefficient ratio R_Fe/Pb from these data, using a hidden solar irradiance spectrum (310-830 nm), and scores whether the ratio meets a preset threshold derived from the literature.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `alpha_Fe_xx_cm1`, `alpha_Fe_yy_cm1`, `alpha_Fe_zz_cm1`, `alpha_Pb_xx_cm1`, `alpha_Pb_yy_cm1`, `alpha_Pb_zz_cm1`
  - `units`:
    - `wavelength_nm`: nm
    - `alpha_Fe_xx_cm1`: cm^-1
    - `alpha_Fe_yy_cm1`: cm^-1
    - `alpha_Fe_zz_cm1`: cm^-1
    - `alpha_Pb_xx_cm1`: cm^-1
    - `alpha_Pb_yy_cm1`: cm^-1
    - `alpha_Pb_zz_cm1`: cm^-1

### refractive_indices.csv
- path: `/app/outputs/refractive_indices.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Refractive index spectra for MAFeI3 and MAPbI3. The checker recomputes the Brewster angle performance factor R_B at a specified wavelength using hidden refractive indices of TiO2 and spiro-OMeTAD, and scores whether R_B meets a preset threshold derived from the literature.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `n_Fe_xx`, `n_Fe_yy`, `n_Fe_zz`, `n_Pb_xx`, `n_Pb_yy`, `n_Pb_zz`
  - `units`:
    - `wavelength_nm`: nm
    - `n_Fe_xx`: dimensionless
    - `n_Fe_yy`: dimensionless
    - `n_Fe_zz`: dimensionless
    - `n_Pb_xx`: dimensionless
    - `n_Pb_yy`: dimensionless
    - `n_Pb_zz`: dimensionless

Notes: The solving agent does not need to compute the optical correlation coefficient or Brewster angles; those are computed by the checker from the submitted data. All non-public data (solar irradiance, interface refractive indices) are bundled with the checker and not required by the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "absorption_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "alpha_Fe_xx_cm1",
          "alpha_Fe_yy_cm1",
          "alpha_Fe_zz_cm1",
          "alpha_Pb_xx_cm1",
          "alpha_Pb_yy_cm1",
          "alpha_Pb_zz_cm1"
        ],
        "units": {
          "wavelength_nm": "nm",
          "alpha_Fe_xx_cm1": "cm^-1",
          "alpha_Fe_yy_cm1": "cm^-1",
          "alpha_Fe_zz_cm1": "cm^-1",
          "alpha_Pb_xx_cm1": "cm^-1",
          "alpha_Pb_yy_cm1": "cm^-1",
          "alpha_Pb_zz_cm1": "cm^-1"
        }
      },
      "description": "Absorption coefficient spectra for MAFeI3 and MAPbI3. The checker recomputes the optical correlation coefficient ratio R_Fe/Pb from these data, using a hidden solar irradiance spectrum (310-830 nm), and scores whether the ratio meets a preset threshold derived from the literature."
    },
    {
      "file": "refractive_indices.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "n_Fe_xx",
          "n_Fe_yy",
          "n_Fe_zz",
          "n_Pb_xx",
          "n_Pb_yy",
          "n_Pb_zz"
        ],
        "units": {
          "wavelength_nm": "nm",
          "n_Fe_xx": "dimensionless",
          "n_Fe_yy": "dimensionless",
          "n_Fe_zz": "dimensionless",
          "n_Pb_xx": "dimensionless",
          "n_Pb_yy": "dimensionless",
          "n_Pb_zz": "dimensionless"
        }
      },
      "description": "Refractive index spectra for MAFeI3 and MAPbI3. The checker recomputes the Brewster angle performance factor R_B at a specified wavelength using hidden refractive indices of TiO2 and spiro-OMeTAD, and scores whether R_B meets a preset threshold derived from the literature."
    }
  ],
  "notes": "The solving agent does not need to compute the optical correlation coefficient or Brewster angles; those are computed by the checker from the submitted data. All non-public data (solar irradiance, interface refractive indices) are bundled with the checker and not required by the agent."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your two CSV files. The verifier computes: (1) an optical correlation coefficient for each perovskite by integrating your absorption coefficients with a hidden solar irradiance spectrum, and (2) Brewster-angle-related factors using your refractive indices together with hidden literature values for TiO2 and spiro-OMeTAD. Each metric is compared against a hidden reference threshold that reflects the expected physical performance relationship between the two materials. You receive a reward between 0.0 and 1.0 proportional to how closely your raw spectra reproduce the intended comparative outcome. The final reward is a weighted combination of these per-file sub-scores. Simply reporting a numerical value known from the literature, without providing the corresponding correct spectral data, will not earn the reward.
