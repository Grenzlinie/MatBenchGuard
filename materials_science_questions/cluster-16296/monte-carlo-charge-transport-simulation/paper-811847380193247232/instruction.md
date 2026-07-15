# Compute Position-Dependent Scattering Rates in an AlGaAs/GaAs HEMT via a Poisson-Schrödinger Pipeline

## Problem background
In a high electron mobility transistor (HEMT), the quantum confinement of carriers can change along the channel from source to drain due to the varying gate-to-channel potential. This may influence carrier scattering rates, which in turn affect device transport properties such as mobility. The task is to compute position-dependent two-dimensional scattering rates for polar optical phonons, acoustic phonons, and ionized impurity scattering in an Al0.5Ga0.5As/GaAs HEMT operating in the sub-ohmic regime. The goal is to determine whether the scattering rates differ measurably between channel positions and to quantify any such differences.

## Approach
The computational workflow proceeds in three stages. First, using the device layer structure (three layers: GaAs substrate, AlGaAs spacer, AlGaAs doped) and bias conditions (gate-to-source and drain-to-source voltages of 0.6 V in the gradual channel approximation), a one-dimensional Poisson solver computes the conduction band edge profiles E_C(z) at three gate-to-channel voltages V_GC = 0.0, 0.3, and 0.6 V. Second, for each profile the time-independent effective-mass Schrödinger equation (m* = 0.065 m0) is solved with the Numerov method to obtain the first five subband eigenenergies and envelope wavefunctions. Third, using the subband data and provided material constants (dielectric constants, polar optical phonon energy, sound velocity, deformation potential, density), two-dimensional scattering rates are evaluated via Fermi's Golden Rule. The considered mechanisms are: polar optical phonon (POP) intrasubband 1→1 and intersubband 1→2, both absorption and emission; acoustic phonon via deformation potential (AP) intrasubband 1→1 absorption and emission; and ionized impurity (II) intrasubband 1→1 and 2→2. All rates are computed as functions of incident electron energy from 0.0 to 0.5 eV in steps of at most 0.01 eV at each of the three channel positions.

## Reproduction target
Produce a CSV file `/app/outputs/scattering_rates.csv` containing the energy-resolved scattering rates (in s⁻¹) for eight scattering mechanisms at each of the three gate-to-channel voltages: V_GC = 0.0, 0.3, and 0.6 V. The incident electron energy must cover the range 0.0–0.5 eV with a step size no larger than 0.01 eV. The CSV must have exactly four columns: mechanism (one of 'POP_1to1_abs', 'POP_1to1_emi', 'POP_1to2_abs', 'POP_1to2_emi', 'AP_1to1_abs', 'AP_1to1_emi', 'II_1to1', 'II_2to2'), position_V (float, 0.0, 0.3, or 0.6), energy_eV (float), rate_s_1 (float).

## Assets

- HEMT device structure parameters
- Material parameters for scattering calculations
- 1D Poisson solver

## Workflow steps

### Step 1: Solve 1D Poisson equation for conduction band profiles
- Role: process
- Action: Compute one-dimensional conduction band edge profiles E_C(z) for three channel positions (gate-to-channel voltages V_GC = 0.0, 0.3, 0.6 V) using a 1D Poisson solver with the provided device structure and bias conditions (V_GS=0.6 V, V_DS=0.6 V, gradual channel approximation).
- Evidence: `/app/outputs/poisson_profiles.npy`

### Step 2: Solve Schrödinger equation for subband energies and wavefunctions
- Role: process
- Action: For each E_C(z) profile, solve the time-independent 1D Schrödinger equation with effective mass m*=0.065 m0 using the Numerov method to obtain the first five subband eigenenergies and envelope wavefunctions.
- Evidence: `/app/outputs/subband_data.npz`

### Step 3: Compute position- and energy-resolved scattering rates
- Role: scored (load-bearing)
- Action: Using the subband data and material parameters, compute two-dimensional scattering rates for polar optical phonons (POP 1→1 absorption/emission, 1→2 absorption/emission), acoustic phonons via deformation potential (AP 1→1 absorption/emission), and ionized impurity scattering (II 1→1, 2→2) as a function of incident electron energy (0 to 0.5 eV in steps ≤0.01 eV) at each channel position. Evaluate the rates using Fermi's Golden Rule with the appropriate matrix elements and screening.
- Output file: `/app/outputs/scattering_rates.csv`
- Format: csv
- Contract: Columns: mechanism (string, e.g., 'POP_1to1_abs', 'POP_1to1_emi', 'POP_1to2_abs', 'POP_1to2_emi', 'AP_1to1_abs', 'AP_1to1_emi', 'II_1to1', 'II_2to2'), position_V (float: 0.0, 0.3, 0.6), energy_eV (float), rate_s_1 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scattering_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scattering_rates.csv
- path: `/app/outputs/scattering_rates.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Energy-resolved scattering rates for POP, AP, and II mechanisms at three channel positions.
- schema:
  - `type`: table
  - `required_columns`: `mechanism`, `position_V`, `energy_eV`, `rate_s_1`
  - `units`:
    - `position_V`: V
    - `energy_eV`: eV
    - `rate_s_1`: s^{-1}

Notes: The rates are compared to hidden gold values digitized from the source paper; the checker computes mean absolute percentage error (MAPE) for each mechanism/position and scores based on tolerance and structural trends (e.g., source rates higher than drain rates).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scattering_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "mechanism",
          "position_V",
          "energy_eV",
          "rate_s_1"
        ],
        "units": {
          "position_V": "V",
          "energy_eV": "eV",
          "rate_s_1": "s^{-1}"
        }
      },
      "description": "Energy-resolved scattering rates for POP, AP, and II mechanisms at three channel positions."
    }
  ],
  "notes": "The rates are compared to hidden gold values digitized from the source paper; the checker computes mean absolute percentage error (MAPE) for each mechanism/position and scores based on tolerance and structural trends (e.g., source rates higher than drain rates)."
}
```

## How you are scored
A hidden verifier reads the submitted `scattering_rates.csv` and independently scores the result. The verifier compares the computed rates to reference values and also checks structural properties such as relative ordering between positions. The total reward is a weighted combination of these checks, and the score decreases as the computed rates deviate from the expected values. Simply reporting numbers without executing the full Poisson-Schrödinger-scattering pipeline is unlikely to yield a high score.
