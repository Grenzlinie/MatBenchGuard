# Analytical Hot-Phonon Transport Model for Bulk GaN

## Problem background
Gallium nitride (GaN) is a highly polar semiconductor widely used in high‑power, high‑frequency field‑effect transistors. In such devices, the electron density in the channel can be very high, leading to copious emission of longitudinal‑optical (LO) phonons. When the phonon generation rate exceeds the rate at which these phonons thermalise with the lattice, the phonon population can deviate significantly from its equilibrium distribution. Whether and to what extent this ‘hot‑phonon’ effect limits the electron drift velocity and causes velocity saturation, and how this depends on the electron density, are central questions for understanding device performance.

## Approach
The approach combines a nonparabolic conduction‑band description (the standard k·p relation) with a rate‑equation treatment of LO‑phonon generation and decay. The key steps are:

1. **Power dissipation model:** Using the spontaneous emission rate of LO phonons and a phonon lifetime, the steady‑state phonon occupation is obtained, from which the power dissipated per electron is computed as a function of electron temperature.
2. **Mobility model:** The polar‑optical‑phonon‑limited mobility is calculated by averaging the momentum‑relaxation rate (Conwell–Vassell formula for a nonparabolic band) over a Maxwell–Boltzmann electron distribution, then combined with a temperature‑independent low‑field mobility to give the total electron mobility.
3. **Velocity–field relation:** The energy‑balance equation (electric power input equals power dissipation) is solved self‑consistently for the electric field, and the drift velocity is obtained from the product of mobility and field.

## Reproduction target
Compute and write two output files:

- `/app/outputs/power_dissipation.csv`: power dissipated per electron versus electron temperature over the range 300 K to 5000 K, at a fixed electron density.
- `/app/outputs/velocity_field.csv`: drift velocity versus electric field for five different electron densities, spanning the range 0.5 × 10¹⁸ cm⁻³ to 5 × 10¹⁸ cm⁻³.

All material constants and model parameters are taken from the literature; they are provided in the workflow steps.

## Assets

- Python 3 standard library: python3
- SciPy: scipy
- NumPy: numpy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Parameter definition
- Role: process
- Action: Define all GaN material constants and model parameters required by the hot-phonon transport model: electron effective mass, band gap, LO-phonon energy, phonon lifetime, static and high-frequency permittivities, lattice temperature, low-field mobility value, and the nonparabolic band relation.
- Evidence: none

### Step 2: Power dissipation computation
- Role: scored
- Action: Using the analytical hot-phonon model (nonparabolic band, LO-phonon generation and decay kinetics), compute the power dissipated per electron as a function of electron temperature over the range 300–5000 K at a representative electron density of 3×10^18 cm^{-3}. Write the result as a CSV.
- Output file: `/app/outputs/power_dissipation.csv`
- Format: csv
- Contract: electron_temperature_K (float), power_per_electron_W (float)
- Scoring: scored by hidden verifier

### Step 3: Mobility computation
- Role: process
- Action: Compute the total electron mobility as a function of electron temperature. Average the polar-optical-phonon momentum-relaxation rate (using the Conwell–Vassell expression for a nonparabolic band) over a Maxwell–Boltzmann distribution, and combine with a temperature-independent low-field mobility to obtain the total mobility function.
- Evidence: none

### Step 4: Velocity-field curves generation
- Role: scored (load-bearing)
- Action: For each electron density in {0.5, 1, 2, 3, 5}×10^18 cm^{-3}, compute the density-dependent power dissipation as in step_02, then solve the energy-balance equation e·μ(Te)·F^2 = P(Te) for the electric field F and obtain drift velocity v = μ(Te)·F. Write the (density, field, velocity) triples to the output CSV.
- Output file: `/app/outputs/velocity_field.csv`
- Format: csv
- Contract: density_cm3 (float), field_kV_cm (float), drift_velocity_cm_s (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/power_dissipation.csv`
- `/app/outputs/velocity_field.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### power_dissipation.csv
- path: `/app/outputs/power_dissipation.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Power dissipation per electron vs electron temperature. The checker will compare the values at selected probe temperatures against digitized reference data from a published figure, applying appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `electron_temperature_K`, `power_per_electron_W`

### velocity_field.csv
- path: `/app/outputs/velocity_field.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Drift velocity vs electric field for five electron densities. The checker will compare drift velocity at selected fields against digitized reference velocity-field curves, applying appropriate tolerances, and verify monotonic saturation trends.
- schema:
  - `type`: table
  - `required_columns`: `density_cm3`, `field_kV_cm`, `drift_velocity_cm_s`

Notes: The model uses an analytical hot-phonon framework with nonparabolic band and LO phonon kinetics. All material constants are taken from the public literature; no external datasets are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "power_dissipation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "electron_temperature_K",
          "power_per_electron_W"
        ]
      },
      "description": "Power dissipation per electron vs electron temperature. The checker will compare the values at selected probe temperatures against digitized reference data from a published figure, applying appropriate tolerances."
    },
    {
      "file": "velocity_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "density_cm3",
          "field_kV_cm",
          "drift_velocity_cm_s"
        ]
      },
      "description": "Drift velocity vs electric field for five electron densities. The checker will compare drift velocity at selected fields against digitized reference velocity-field curves, applying appropriate tolerances, and verify monotonic saturation trends."
    }
  ],
  "notes": "The model uses an analytical hot-phonon framework with nonparabolic band and LO phonon kinetics. All material constants are taken from the public literature; no external datasets are required."
}
```

## How you are scored
A hidden verifier inspects your two CSV files. It checks that each file has the correct columns and contains enough well‑formed data. It then extracts specific probe points (e.g., certain electron temperatures from the power dissipation file, certain electric fields from the velocity‑field file), compares your values against a reference, and also verifies physical trends such as velocity saturation and the dependence on electron density. The two scored artifacts are combined into a single reward, a float between 0 and 1. No part of the task requires the original paper; the verifier uses its own hidden reference.
