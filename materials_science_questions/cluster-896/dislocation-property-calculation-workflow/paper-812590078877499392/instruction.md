# Positron Annihilation at Defects in Aluminium: Thomas-Fermi Calculation of Electron Density and Annihilation Characteristics

## Problem background
Positron annihilation is a sensitive probe of electron density at lattice defects. This study computes the self-consistent electron charge distribution and annihilation characteristics for vacancies and edge dislocations in aluminium within the jellium model, using the Thomas-Fermi approximation and a mixed-density annihilation rate formula. The goal is to quantitatively reproduce the calculated positron lifetimes and angular correlation curves that explain experimental observations, including the anisotropy at dislocations.

## Approach
The approach uses the jellium model of metals, where the ions form a uniform positive background and defects are represented by local deviations in the ionic charge density. The electron density is obtained by solving the nonlinear Thomas-Fermi equation iteratively (using Green's functions) to enforce self-consistency. For vacancies, the ionic charge is absent inside a Wigner-Seitz sphere; for edge dislocations, a hollow-core model with an adjustable core radius R_b is used, with the ionic density outside given by linear elasticity theory.

A positron trapping potential is constructed as the sum of three terms: the electrostatic potential from the charge redistribution, an ionic pseudopotential that simulates the non-uniform ion background, and a correlation potential accounting for the density-dependent electron-positron correlation energy. The single-particle positron wavefunction is obtained by solving the Schrödinger equation (1D radial for the spherical vacancy, 2D variational with a parametrized trial function for the dislocation).

Annihilation characteristics are computed using two methods: the total annihilation rate (inverse lifetime) is evaluated from the local electron density at the positron using a Brandt-type enhancement factor; the momentum-dependent annihilation rate (angular correlation in slit geometry) is computed via a mixed-density formula that accounts for the non-uniform electron gas, integrating over the positron wavefunction and the local Fermi momentum.

For the dislocation, the core radius R_b is calibrated by requiring that the computed positron lifetime matches the known experimental value in deformed aluminium. The final quantities include electron densities at the defect centers relative to bulk, lifetimes, and angular correlation curves for all relevant momentum directions.

## Reproduction target
Produce the following deliverables:

1. For a spherical vacancy in aluminium: the electron density at the vacancy centre as a fraction of the bulk electron density, and the trapped positron lifetime in picoseconds.
2. The angular correlation curve I(p) for the vacancy (slit geometry) as a table of momentum p (in inverse ångströms) and normalized intensity.
3. For an edge dislocation: calibrate the hollow-core radius R_b (in ångströms) such that the computed positron lifetime reproduces the experimentally known lifetime in deformed aluminium. Then output: the calibrated R_b, the electron density at the dislocation core centre as a fraction of bulk, and the corresponding positron lifetime.
4. Angular correlation curves for the dislocation with momentum components along the dislocation line (z) and in the two perpendicular directions (x and y, in the glide plane), as separate tables.

All scalar results must be written in JSON format, angular correlation curves as two-column CSV files. The outputs must be saved to /app/outputs exactly as specified in the workflow steps.

## Assets

- Python with NumPy and SciPy: numpy scipy

## Workflow steps

### Step 1: Define vacancy ionic charge density
- Role: process
- Action: Set up aluminium material constants (Wigner-Seitz radius, Fermi wavevector, etc.) and construct the jellium ionic charge distribution ρ_i(r) for a spherical vacancy as described in Eq. (5.1).
- Evidence: `/app/outputs/vacancy_params.txt`

### Step 2: Solve Thomas-Fermi and compute vacancy electron density and positron lifetime
- Role: scored
- Action: Solve the nonlinear Thomas-Fermi equation iteratively (Green's function method) to obtain the self-consistent electron density ρ_e(r) and electrostatic potential φ(r) for the vacancy. Construct the total positron trapping potential V_t = eφ + V_i + V_corr, solve the one-dimensional positron Schrödinger equation, and compute the positron lifetime using the local annihilation rate formula (Eq. (4.1)). Record the electron density at the vacancy centre as a fraction of the bulk density.
- Output file: `/app/outputs/vacancy_results.json`
- Format: json
- Contract: {"electron_density_center_fraction_of_bulk": <float>, "positron_lifetime_ps": <float>}
- Scoring: scored by hidden verifier

### Step 3: Compute angular correlation curve for vacancy
- Role: scored
- Action: Using the positron wavefunction and electron density from the vacancy solution, evaluate the mixed-density annihilation rate formula (Eq. (4.18)) integrated over coordinates to obtain the angular correlation curve I(p) in slit geometry. Output a CSV with p (inverse angstrom) and I(p) (normalized arbitrary units).
- Output file: `/app/outputs/angular_correlation_vacancy.csv`
- Format: csv
- Contract: columns: p (float), I(p) (float)
- Scoring: scored by hidden verifier

### Step 4: Set up dislocation ionic density with hollow core
- Role: process
- Action: Define the edge dislocation geometry (Burgers vector, Poisson ratio) and the hollow-core ionic charge distribution parametrized by the core radius R_b, following the model of Eq. (6.3).
- Evidence: `/app/outputs/dislocation_setup.txt`

### Step 5: Calibrate dislocation core radius and compute electron density and lifetime
- Role: scored (load-bearing)
- Action: For a series of core radii R_b, solve the Thomas-Fermi equation in 2D cylindrical geometry, construct the total positron trapping potential, obtain the positron wavefunction via a variational method (trial function Eq. (6.6)), and compute the positron lifetime. Determine the R_b value that matches the experimentally known positron lifetime in deformed aluminium (Hautojärvi et al. 1970). Report the calibrated R_b, the electron density at the dislocation core centre relative to bulk, and the resulting positron lifetime.
- Output file: `/app/outputs/dislocation_results.json`
- Format: json
- Contract: {"hole_radius_angstrom": <float>, "electron_density_center_fraction_of_bulk": <float>, "positron_lifetime_ps": <float>}
- Scoring: scored by hidden verifier

### Step 6: Compute angular correlation curve for dislocation (z-direction)
- Role: scored
- Action: Using the final dislocation fields from the calibrated model, evaluate the mixed-density formula specialized to 2D translational invariance (Eq. (4.24)) to obtain the angular correlation curve I(p_z) for the momentum component parallel to the dislocation line. Output a CSV with p (angstrom^-1) and I_z(p).
- Output file: `/app/outputs/angular_correlation_dislocation_z.csv`
- Format: csv
- Contract: columns: p (float), I_z(p) (float)
- Scoring: scored by hidden verifier

### Step 7: Compute angular correlation curve for dislocation (x-direction)
- Role: scored
- Action: Same as step_06 but for I(p_x) (momentum component perpendicular to the dislocation line, along the x-axis). Output CSV with p and I_x(p).
- Output file: `/app/outputs/angular_correlation_dislocation_x.csv`
- Format: csv
- Contract: columns: p (float), I_x(p) (float)
- Scoring: scored by hidden verifier

### Step 8: Compute angular correlation curve for dislocation (y-direction)
- Role: scored
- Action: Same as step_06 but for I(p_y). Output CSV with p and I_y(p).
- Output file: `/app/outputs/angular_correlation_dislocation_y.csv`
- Format: csv
- Contract: columns: p (float), I_y(p) (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_results.json`
- `/app/outputs/dislocation_results.json`
- `/app/outputs/angular_correlation_vacancy.csv`
- `/app/outputs/angular_correlation_dislocation_z.csv`
- `/app/outputs/angular_correlation_dislocation_x.csv`
- `/app/outputs/angular_correlation_dislocation_y.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_results.json
- path: `/app/outputs/vacancy_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Vacancy electron density at centre (fraction of bulk) and trapped positron lifetime in picoseconds. Checker compares each scalar to the paper's reference value within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `electron_density_center_fraction_of_bulk`: float
    - `positron_lifetime_ps`: float

### dislocation_results.json
- path: `/app/outputs/dislocation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Calibrated hollow-core radius (angstrom), electron density at core centre (fraction of bulk), and positron lifetime (ps) for the dislocation. Checker compares each scalar to the paper's reference value within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `hole_radius_angstrom`: float
    - `electron_density_center_fraction_of_bulk`: float
    - `positron_lifetime_ps`: float

### angular_correlation_vacancy.csv
- path: `/app/outputs/angular_correlation_vacancy.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Angular correlation curve for a vacancy. Checker recomputes the full width at half maximum (FWHM) from this data and compares it to the paper's reference FWHM; also verifies the curve is non-negative and monotonic decreasing from p=0.
- schema:
  - `type`: table
  - `required_columns`: `p`, `I(p)`
  - `units`:
    - `p`: angstrom^-1
    - `I(p)`: normalized arbitrary units

### angular_correlation_dislocation_z.csv
- path: `/app/outputs/angular_correlation_dislocation_z.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Angular correlation curve for a dislocation, momentum component parallel to the line. Checker recomputes FWHM and compares to paper reference; checks shape constraints.
- schema:
  - `type`: table
  - `required_columns`: `p`, `I_z(p)`
  - `units`:
    - `p`: angstrom^-1
    - `I_z(p)`: normalized arbitrary units

### angular_correlation_dislocation_x.csv
- path: `/app/outputs/angular_correlation_dislocation_x.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Angular correlation curve for a dislocation, momentum component perpendicular to the line (x). Checker recomputes FWHM and compares to paper reference; checks shape constraints.
- schema:
  - `type`: table
  - `required_columns`: `p`, `I_x(p)`
  - `units`:
    - `p`: angstrom^-1
    - `I_x(p)`: normalized arbitrary units

### angular_correlation_dislocation_y.csv
- path: `/app/outputs/angular_correlation_dislocation_y.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Angular correlation curve for a dislocation, momentum component perpendicular to the line (y). Checker recomputes FWHM and compares to paper reference; checks shape constraints.
- schema:
  - `type`: table
  - `required_columns`: `p`, `I_y(p)`
  - `units`:
    - `p`: angstrom^-1
    - `I_y(p)`: normalized arbitrary units

Notes: The dislocation calibration step is load-bearing: the reported hole radius, electron density, and lifetime depend on a correct iterative fit to the known experimental lifetime. Angular correlation curves must exhibit the documented anisotropy (FWHM ratio between z and x/y components).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "electron_density_center_fraction_of_bulk": "float",
          "positron_lifetime_ps": "float"
        }
      },
      "description": "Vacancy electron density at centre (fraction of bulk) and trapped positron lifetime in picoseconds. Checker compares each scalar to the paper's reference value within a tolerance."
    },
    {
      "file": "dislocation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "hole_radius_angstrom": "float",
          "electron_density_center_fraction_of_bulk": "float",
          "positron_lifetime_ps": "float"
        }
      },
      "description": "Calibrated hollow-core radius (angstrom), electron density at core centre (fraction of bulk), and positron lifetime (ps) for the dislocation. Checker compares each scalar to the paper's reference value within a tolerance."
    },
    {
      "file": "angular_correlation_vacancy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "I(p)"
        ],
        "units": {
          "p": "angstrom^-1",
          "I(p)": "normalized arbitrary units"
        }
      },
      "description": "Angular correlation curve for a vacancy. Checker recomputes the full width at half maximum (FWHM) from this data and compares it to the paper's reference FWHM; also verifies the curve is non-negative and monotonic decreasing from p=0."
    },
    {
      "file": "angular_correlation_dislocation_z.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "I_z(p)"
        ],
        "units": {
          "p": "angstrom^-1",
          "I_z(p)": "normalized arbitrary units"
        }
      },
      "description": "Angular correlation curve for a dislocation, momentum component parallel to the line. Checker recomputes FWHM and compares to paper reference; checks shape constraints."
    },
    {
      "file": "angular_correlation_dislocation_x.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "I_x(p)"
        ],
        "units": {
          "p": "angstrom^-1",
          "I_x(p)": "normalized arbitrary units"
        }
      },
      "description": "Angular correlation curve for a dislocation, momentum component perpendicular to the line (x). Checker recomputes FWHM and compares to paper reference; checks shape constraints."
    },
    {
      "file": "angular_correlation_dislocation_y.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "I_y(p)"
        ],
        "units": {
          "p": "angstrom^-1",
          "I_y(p)": "normalized arbitrary units"
        }
      },
      "description": "Angular correlation curve for a dislocation, momentum component perpendicular to the line (y). Checker recomputes FWHM and compares to paper reference; checks shape constraints."
    }
  ],
  "notes": "The dislocation calibration step is load-bearing: the reported hole radius, electron density, and lifetime depend on a correct iterative fit to the known experimental lifetime. Angular correlation curves must exhibit the documented anisotropy (FWHM ratio between z and x/y components)."
}
```

## How you are scored
Each scored output file is independently evaluated by a hidden checker.

- For the scalar JSON files (vacancy and dislocation results), the checker compares your reported values to a hidden reference (the corresponding values from the paper) using appropriate tolerances that absorb numerical differences from re-implementations.
- For the angular correlation CSV files, the checker recomputes the full width at half maximum (FWHM) of each curve and compares it to the hidden reference FWHM. It also verifies that each curve is non‑negative and monotonically decreasing from p = 0. Additionally, the checker checks that the anisotropy between directions (the ratio of FWHM for z vs the perpendicular directions) matches expectations.
- Each stage carries a weighted share of the total reward, with the primary scalar results and FWHM comparisons receiving the largest weights. Reporting correct values alone is not sufficient; the checker validates the consistency and physical plausibility of the curves.
