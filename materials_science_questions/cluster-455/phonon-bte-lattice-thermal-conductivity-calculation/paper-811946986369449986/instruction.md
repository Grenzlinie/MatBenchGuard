# Numerical Solver for Spectral Phonon BTE in Axisymmetric Cylindrical Geometry

## Problem background
At the nanoscale, phonon mean free paths can exceed the dimensions of semiconductor structures, causing heat conduction to deviate from Fourier's law. In silicon nanofilms and nanowires, the spectral phonon Boltzmann transport equation (BTE) under the relaxation time approximation provides a framework to describe these deviations. This task revolves around a numerical solver for the spectral phonon BTE in an axisymmetric cylindrical geometry, which accounts for frequency-dependent scattering and acoustic phonon dispersion. The solver computes steady‑state thermal conductance/conductivity and transient temperature evolution, revealing the transition between ballistic and diffusive heat transport. The goal is to implement such a solver and produce physically consistent predictions of thermal conductance, conductivity, and transient mid‑point temperature evolution for silicon nanostructures under prescribed conditions.

## Approach
The core is a time‑dependent solver for the phonon BTE in the relaxation time approximation, cast in axisymmetric cylindrical coordinates. Angular integration is performed with a discrete ordinate method; spatial discretisation uses a rectangular mesh. The temperature field is updated implicitly via the energy balance relation summed over all phonon modes.

Phonon interactions are modelled by frequency‑dependent relaxation times: Rayleigh‑like impurity scattering ∝ ω⁴, normal anharmonic scattering ∝ ω² T³, and umklapp scattering ∝ ω² / sinh(ħω / kB T). The inverse relaxation times are combined with Matthiessen’s rule. Only acoustic branches are considered, using the acoustic phonon dispersion and group velocities from Pop et al. 2004. Bulk thermal conductivity of silicon over 50–400 K serves as the calibration target for the relaxation‑time coefficients.

Two boundary‑condition modes are used: specular lateral reflection (equivalent to a film) and diffuse lateral reflection (equivalent to a nanowire). In steady‑state simulations, thermal conductance of films and thermal conductivity of nanowires are computed for a range of thicknesses and temperatures respectively. In transient simulations, the temperature at the midpoint of a film or nanowire is recorded after a boundary temperature step, probing the characteristic ballistic and diffusive transport signatures.

## Reproduction target
Implement the numerical solver described above, calibrate the relaxation‑time coefficients to reproduce bulk silicon thermal conductivity over 50–400 K, and then produce the following three data files:

1. **Steady‑state thermal conductance of silicon nanofilms:** run the solver in film mode (specular lateral boundaries) at 300 K for multiple film thicknesses, and save conductance vs. thickness in `steady_state_films_conductance.csv` (columns: thickness_nm, conductance_W_per_K).
2. **Steady‑state thermal conductivity of silicon nanowires:** run the solver in wire mode (diffuse lateral boundaries) for diameters 37 nm, 56 nm, and 115 nm at temperatures 50, 100, 150, 200, 250, 300, 350, 400 K, and save conductivity vs. temperature in `steady_state_nanowires_conductivity.csv` (columns: diameter_nm, temperature_K, thermal_conductivity_W_per_mK).
3. **Transient midpoint temperature evolution:** for a 1 µm thick film (specular boundaries) and a 1 µm long, 37 nm diameter nanowire (diffuse boundaries), both initially at approximately 10 K, impose a boundary temperature step and record the temperature at the midpoint at several time instants; save the time series in `transient_temperature_profiles.csv` (columns: system, time_ns, position, temperature_K).

All output files must follow the schemas given in the Output contract section. The solver’s outputs will be compared to hidden reference data; correctness of the calibration and implementation is judged through the agreement of these outputs with the references, not by inspecting calibration parameters directly.

## Assets

- Silicon acoustic phonon dispersion and group velocity parameters (Pop et al. 2004): 10.1063/1.1805123
- Bulk silicon thermal conductivity reference data

## Workflow steps

### Step 1: Calibrate phonon relaxation time parameters to bulk silicon thermal conductivity
- Role: process
- Action: Calibrate the coefficients for impurity (Rayleigh-like ∝ ω⁴), normal (∝ ω² T³), and umklapp (∝ ω² / sinh(ħω/kbT)) scattering, combined via Matthiessen's rule, so that the BTE solver reproduces known bulk silicon thermal conductivity over the temperature range 50–400 K. Use acoustic phonon dispersion from Pop et al. 2004.
- Evidence: none

### Step 2: Compute steady-state thermal conductance of silicon nanofilms
- Role: scored (load-bearing)
- Action: Run the BTE solver in steady state with specular lateral boundaries (film mode) for a range of film thicknesses at 300 K. Compute thermal conductance for each thickness and store results in a CSV file.
- Output file: `/app/outputs/steady_state_films_conductance.csv`
- Format: csv
- Contract: CSV with columns: thickness_nm (numeric), conductance_W_per_K (numeric). At least 10 data points.
- Scoring: scored by hidden verifier

### Step 3: Compute steady-state thermal conductivity of silicon nanowires
- Role: scored (load-bearing)
- Action: Run the BTE solver in steady state with diffuse lateral boundaries (wire mode) for diameters 37, 56, and 115 nm at temperatures 50, 100, 150, 200, 250, 300, 350, 400 K. Compute thermal conductivity for each condition and store results.
- Output file: `/app/outputs/steady_state_nanowires_conductivity.csv`
- Format: csv
- Contract: CSV with columns: diameter_nm (numeric), temperature_K (numeric), thermal_conductivity_W_per_mK (numeric). At least 24 rows (3 diameters × 8 temperatures).
- Scoring: scored by hidden verifier

### Step 4: Simulate transient temperature evolution in a nanofilm and a nanowire
- Role: scored
- Action: Run the time-dependent BTE solver for a 1 µm thick film (specular boundaries) and a 1 µm long, 37 nm diameter nanowire (diffuse boundaries) with initial temperature around 10 K. Impose a temperature step at one end, and record the temperature at the midpoint at several time instants. Store the time series.
- Output file: `/app/outputs/transient_temperature_profiles.csv`
- Format: csv
- Contract: CSV with columns: system (string: 'film' or 'nanowire'), time_ns (numeric), position (string: 'midpoint'), temperature_K (numeric). Provide data for both systems covering the time range where the transient occurs.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/steady_state_films_conductance.csv`
- `/app/outputs/steady_state_nanowires_conductivity.csv`
- `/app/outputs/transient_temperature_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### steady_state_films_conductance.csv
- path: `/app/outputs/steady_state_films_conductance.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductance of silicon nanofilms as a function of thickness at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `thickness_nm`, `conductance_W_per_K`
  - `units`:
    - `thickness_nm`: nm
    - `conductance_W_per_K`: W/K

### steady_state_nanowires_conductivity.csv
- path: `/app/outputs/steady_state_nanowires_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity of silicon nanowires for three diameters over temperatures 50–400 K.
- schema:
  - `type`: table
  - `required_columns`: `diameter_nm`, `temperature_K`, `thermal_conductivity_W_per_mK`
  - `units`:
    - `diameter_nm`: nm
    - `temperature_K`: K
    - `thermal_conductivity_W_per_mK`: W/(m·K)

### transient_temperature_profiles.csv
- path: `/app/outputs/transient_temperature_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Transient midpoint temperature evolution in a 1 µm film and a 37 nm nanowire following a boundary temperature step.
- schema:
  - `type`: table
  - `required_columns`: `system`, `time_ns`, `position`, `temperature_K`
  - `units`:
    - `time_ns`: ns
    - `temperature_K`: K

Notes: All outputs are produced by the agent's BTE solver. The solver must be implemented from scratch based on the method description; no pre-existing code is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "steady_state_films_conductance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_nm",
          "conductance_W_per_K"
        ],
        "units": {
          "thickness_nm": "nm",
          "conductance_W_per_K": "W/K"
        }
      },
      "description": "Thermal conductance of silicon nanofilms as a function of thickness at 300 K."
    },
    {
      "file": "steady_state_nanowires_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "diameter_nm",
          "temperature_K",
          "thermal_conductivity_W_per_mK"
        ],
        "units": {
          "diameter_nm": "nm",
          "temperature_K": "K",
          "thermal_conductivity_W_per_mK": "W/(m·K)"
        }
      },
      "description": "Thermal conductivity of silicon nanowires for three diameters over temperatures 50–400 K."
    },
    {
      "file": "transient_temperature_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "time_ns",
          "position",
          "temperature_K"
        ],
        "units": {
          "time_ns": "ns",
          "temperature_K": "K"
        }
      },
      "description": "Transient midpoint temperature evolution in a 1 µm film and a 37 nm nanowire following a boundary temperature step."
    }
  ],
  "notes": "All outputs are produced by the agent's BTE solver. The solver must be implemented from scratch based on the method description; no pre-existing code is provided."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage’s output. For the steady‑state film conductance CSV, it compares the conductance values against reference data for a set of thicknesses. For the steady‑state nanowire conductivity CSV, it checks that the conductivity values and their dependence on diameter and temperature match reference data. For the transient temperature profiles CSV, the verifier assesses the midpoint temperature evolution, including whether the film exhibits distinct ballistic steps and the nanowire shows a smooth diffusive rise, as well as approximate agreement with reference time points. The stage‑level scores are combined by weight into an overall reward in [0, 1]; precise tolerances and reference values are hidden. Your task is to produce physically correct outputs from a correct implementation – the verifier decides how close they are to the expected results.
