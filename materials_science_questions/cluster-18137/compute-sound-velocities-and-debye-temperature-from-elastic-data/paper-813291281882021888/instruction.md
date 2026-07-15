# Kieffer Model Heat Capacity and Polynomial Fit for Mg2SiO4 Ringwoodite

## Problem background
Mg2SiO4 ringwoodite is an abundant mineral in the Earth's mantle transition zone. Its high-temperature isobaric heat capacity (Cp) is needed for thermodynamic modelling but previous experimental measurements contain systematic errors. The current work provides a redetermined Cp from calorimetry and extrapolation by a lattice vibrational (Kieffer) model. The computational part of the work models the vibrational density of states (VDoS) of ringwoodite using a Kieffer model with acoustic branches and two optic continua, converts the computed isochoric heat capacity Cv to Cp using thermodynamic relations, and fits a polynomial to Cp over a wide temperature range. The outcome demonstrates how the model reproduces experimental data and supplies reliable Cp for geophysical calculations.

## Approach
The Kieffer lattice vibrational model represents the phonon density of states of a solid as a continuous distribution made of several continua. For Mg2SiO4 ringwoodite the VDoS is partitioned into three acoustic branches (TA1, TA2, LA) each spanning from zero to a distinct cutoff wavenumber, and two optic continua (OC1 and OC2) that cover higher wavenumber regions with assigned mode counts. The model computes isochoric heat capacity Cv(T) by integrating/summing the contribution of each branch over frequency. The result is then converted to isobaric heat capacity Cp using the thermodynamic relation Cp = Cv + (γth·Cv)²·T/(K0T·V), where K0T is the temperature-dependent isothermal bulk modulus and V is the constant zero-pressure volume. The lower cutoff frequency of the first optic continuum (OC1) is not taken directly from the literature; it is calibrated so that the model reproduces published low-temperature Cp measurements (Step 1). All other physical parameters (VDoS cutoffs except that calibrated limit, mode fractions, formula weight, reference volume, bulk modulus and its temperature derivative, thermal Grüneisen parameter) are fixed. The computed Cp is evaluated at a series of fixed temperatures. Finally, a least‑squares polynomial fit of the form Cp = k0 + k1·T + k2·T⁻¹ + k3·T⁻² + k4·T⁻³ is performed on the Cp values from 250 K to 2500 K to obtain the coefficients.

## Reproduction target
Compute the isobaric heat capacity Cp of Mg2SiO4 ringwoodite from the Kieffer model at the following temperatures (Kelvin): 50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2500. Save the results to `cp_values.csv`. Then, using the Cp values for the temperature range 250–2500 K, fit the polynomial Cp = k0 + k1·T + k2·T⁻¹ + k3·T⁻² + k4·T⁻³ and write the fitted coefficients to `polynomial_coefficients.json`. Both files must follow the output contracts below.

## Assets
No external data files are required. All physical parameters (VDoS cutoffs and fractions, formula weight, volume, bulk modulus, temperature derivative, Grüneisen parameter) are given in the instruction. The implementation only needs standard scientific Python packages such as `numpy`, `scipy`, `pandas`, and `matplotlib` (optional). These can be installed from the Tsinghua PyPI mirror.

## Workflow steps

### Step 1: Calibrate lower cutoff of the first optic continuum
- Role: process
- Action: Obtain the low-temperature isobaric heat capacity data for Mg2SiO4 ringwoodite from the literature (Akaogi et al., 2007). The reported values are: 3.43 J/(mol·K) at 50 K, 25.25 at 100 K, 53.61 at 150 K, 79.51 at 200 K, and 114.65 at 300 K. Implement the Kieffer lattice vibrational model for Mg2SiO4 ringwoodite using the vibrational density of states: acoustic branches TA1 (0–146 cm⁻¹, fraction 0.0238), TA2 (0–155 cm⁻¹, fraction 0.0238), LA (0–255 cm⁻¹, fraction 0.0238); two optic continua with the second (OC2) fixed at 790–840 cm⁻¹ (fraction 0.1905, 8 modes). The first optic continuum (OC1) contains 31 modes, fraction 0.7381, and its upper cutoff is fixed at 600 cm⁻¹, but its lower cutoff frequency (call it ω_low) is treated as an adjustable parameter. Other physical parameters are: formula weight 140.69 g mol⁻¹, volume 131.14 Å³ per reduced cell (Z=2), isothermal bulk modulus at 298 K 182 GPa, temperature derivative of bulk modulus –0.025 GPa K⁻¹, thermal Grüneisen parameter 1.10. Compute isochoric heat capacity Cv(T) from the Kieffer model and convert to isobaric heat capacity using Cp = Cv + (γth·Cv)²·T / (K0T·V) with K0T = K0,298 + (dK0/dT)_P·(T–298) and constant V = V298. Optimise ω_low (e.g., by scanning or root‑finding) so that the model Cp agrees with the reference low‑temperature data at the five specified temperatures (e.g., minimise root‑mean‑square deviation). Save the final optimised ω_low (in cm⁻¹) to `/app/outputs/calibrated_cutoff.json`.
- Evidence: `/app/outputs/calibrated_cutoff.json`
- Format: json

### Step 2: Compute Heat Capacity from Kieffer Model
- Role: scored (load-bearing)
- Action: Implement the Kieffer lattice vibrational model for Mg2SiO4 ringwoodite using the vibrational density of states with the calibrated lower cutoff ω_low (from Step 1) for OC1: TA1 (0–146 cm⁻¹, fraction 0.0238), TA2 (0–155 cm⁻¹, fraction 0.0238), LA (0–255 cm⁻¹, fraction 0.0238), OC1 (ω_low–600 cm⁻¹, fraction 0.7381, 31 modes), OC2 (790–840 cm⁻¹, fraction 0.1905, 8 modes). Use physical parameters: formula weight 140.69 g mol⁻¹, volume 131.14 Å³ per reduced cell (Z=2), isothermal bulk modulus at 298 K 182 GPa, temperature derivative of bulk modulus –0.025 GPa K⁻¹, thermal Grüneisen parameter 1.10. Compute isochoric heat capacity Cv(T) from the Kieffer model and convert to isobaric heat capacity using Cp = Cv + (γth·Cv)²·T / (K0T·V) with K0T = K0,298 + (dK0/dT)_P·(T–298) and constant V = V298. Evaluate Cp at temperatures: 50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2500 K. Output the results to `/app/outputs/cp_values.csv`.
- Output file: `/app/outputs/cp_values.csv`
- Format: csv
- Contract: Two columns: Temperature_K (numeric, Kelvin), Cp_J_per_mol_K (numeric, J/(mol·K)). One row per temperature.
- Scoring: scored by hidden verifier

### Step 3: Fit Polynomial to Heat Capacity Data
- Role: scored (load-bearing)
- Action: Using the Cp values computed for temperatures from 250 K to 2500 K (inclusive), perform a least‑squares fit to the polynomial form Cp = k0 + k1·T + k2·T⁻¹ + k3·T⁻² + k4·T⁻³. Derive coefficients k0, k1, k2, k3, k4. Output the fitted coefficients to `/app/outputs/polynomial_coefficients.json`.
- Output file: `/app/outputs/polynomial_coefficients.json`
- Format: json
- Contract: JSON object with keys k0, k1, k2, k3, k4, each a numeric float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cp_values.csv`
- `/app/outputs/polynomial_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cp_values.csv
- path: `/app/outputs/cp_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Isobaric heat capacities of Mg2SiO4 ringwoodite computed from the Kieffer model at 18 specified temperatures.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Cp_J_per_mol_K`
  - `units`:
    - `Temperature_K`: Kelvin
    - `Cp_J_per_mol_K`: J/(mol·K)

### polynomial_coefficients.json
- path: `/app/outputs/polynomial_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Polynomial fit coefficients for Cp in the range 250–2500 K.
- schema:
  - `type`: object
  - `required`: `k0`, `k1`, `k2`, `k3`, `k4`
  - `items`:
    - `k0`: float
    - `k1`: float
    - `k2`: float
    - `k3`: float
    - `k4`: float
  - `units`: dimensionless coefficients; temperature in K

Notes: Both outputs are deterministic given the model parameters. The verifier compares the agent's submitted values to the paper's published references using hidden tolerances. No datasets or external models are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cp_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Cp_J_per_mol_K"
        ],
        "units": {
          "Temperature_K": "Kelvin",
          "Cp_J_per_mol_K": "J/(mol·K)"
        }
      },
      "description": "Isobaric heat capacities of Mg2SiO4 ringwoodite computed from the Kieffer model at 18 specified temperatures."
    },
    {
      "file": "polynomial_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "k0",
          "k1",
          "k2",
          "k3",
          "k4"
        ],
        "items": {
          "k0": "float",
          "k1": "float",
          "k2": "float",
          "k3": "float",
          "k4": "float"
        },
        "units": "dimensionless coefficients; temperature in K"
      },
      "description": "Polynomial fit coefficients for Cp in the range 250–2500 K."
    }
  ],
  "notes": "Both outputs are deterministic given the model parameters. The verifier compares the agent's submitted values to the paper's published references using hidden tolerances. No datasets or external models are required."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that scores each workflow stage independently and combines the scores by weight into a final reward. For `cp_values.csv`, the verifier compares your computed Cp values to reference values derived from the published model; for `polynomial_coefficients.json`, it compares your fitted coefficients to reference coefficients. Both checks use hidden tolerances appropriate for a numerical reproduction. Simply reporting a number that happens to match the paper's result is not sufficient—the verifier expects the outputs to be produced by faithful implementation of the described method.
