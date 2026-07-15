# Two-Electron State Monte Carlo Transport Simulation

## Problem background
Monte Carlo simulation is a principal tool for studying hot electron transport in semiconductors, providing the drift velocity overshoot, electron temperature, and valley transfer dynamics directly from scattering rates. Accurately treating electron-electron (e-e) scattering is difficult because it couples pairs of carriers, and conventional serial Monte Carlo methods cannot conserve energy and momentum exactly during two-particle collisions. A recently proposed two-electron state Ensemble Monte Carlo (EMC) approach addresses this by simulating pairs of electrons together, thereby enforcing exact conservation laws in e-e events without introducing artificial extra scattering. This task implements that method for n-GaAs at a high electric field and compares the transient transport properties against a conventional single-electron EMC without e-e scattering, thereby evaluating the influence of e-e collisions on the carrier dynamics.

## Approach
The two-electron state EMC method groups electrons into pairs. For a pair of states (k1, k2), the total scattering rate is the sum of the individual electron scattering rates (acoustic deformation potential, polar optical phonon, piezoelectric, intervalley) plus the joint pair e-e scattering rate. The e-e rate for a pair is computed from the short-range Coulomb interaction with Debye screening, using the pair's relative wave vector and the screening length. Energy and momentum are conserved exactly during every e-e event. The baseline is a conventional single-electron EMC in which only the same single-electron scattering mechanisms are active, without any e-e scattering. Both simulations are run for 5000 electrons (or 5000 pairs) with an initial Maxwellian distribution at 300 K, a uniform electric field of 5 kV/cm applied at t=0, and a doping density of 1×10^18 cm⁻³. The time step is 0.01 ps and the total simulated time is at least 2 ps. At each time step, the ensemble-averaged drift velocity, electron temperature (mean kinetic energy per electron), and fractional populations in the Γ and L valleys are recorded. This generates three time-series datasets that allow a direct comparison of transport with and without e-e scattering.

## Reproduction target
Produce three CSV files, each containing a full 2 ps time series of a transport quantity for both simulation types (no e-e and with e-e):
- drift_velocity_vs_time.csv – drift velocity in cm·s⁻¹
- electron_temperature_vs_time.csv – electron temperature in K
- valley_population_vs_time.csv – fractional occupation of Γ and L valleys.
The required columns are specified in the Output contract. The objective is to faithfully compute these temporal profiles from the underlying EMC implementations, so that the hidden verifier can assess the self-consistency between the two simulation sets.

## Assets

- GaAs material parameters (Littlejohn et al. 1977): https://doi.org/10.1063/1.323553
- NumPy: https://pypi.org/project/numpy
- SciPy: https://pypi.org/project/scipy

## Workflow steps

### Step 1: Parameter and scattering rate configuration
- Role: process
- Action: Retrieve the GaAs material parameters from the paper by Littlejohn et al. (1977) (DOI 10.1063/1.323553). Define the scattering rate functions for all relevant mechanisms: acoustic deformation potential, polar optic phonon, piezoelectric, intervalley phonon, and the short‑range electron‑electron scattering rate with screening. Implement the total scattering rate for a two‑electron state as the sum of single‑electron rates plus the pair electron‑electron contribution.
- Evidence: none

### Step 2: Run the two EMC simulations
- Role: process
- Action: Implement and run two Ensemble Monte Carlo simulations for n‑GaAs at lattice temperature T=300 K, uniform electric field 5 kV/cm, doping concentration 1×10^18 cm⁻³.  
1. Two‑electron state EMC with electron‑electron scattering included (new method).  
2. Conventional single‑electron EMC without electron‑electron scattering.  
Use 5000 pairs (5000 electrons per simulation), initial Maxwellian distribution at zero field, time step 0.01 ps, total simulation time at least 2 ps. Track ensemble‑averaged drift velocity, electron temperature (mean kinetic energy per electron), and fractional populations in Γ and L valleys at each time step. Save the full time series to an intermediate file for later extraction (e.g., simulation_outputs.npz).
- Evidence: `/app/outputs/simulation_outputs.npz`

### Step 3: Produce drift velocity comparison
- Role: scored (load-bearing)
- Action: From the simulation outputs, extract the time‑dependent drift velocity for both simulation types and write them to drift_velocity_vs_time.csv with columns: time_ps (float), v_drift_no_ee_cm_s (float), v_drift_with_ee_cm_s (float). The file must cover the full simulation time from 0 to at least 2 ps.
- Output file: `/app/outputs/drift_velocity_vs_time.csv`
- Format: csv
- Contract: Columns: time_ps, v_drift_no_ee_cm_s, v_drift_with_ee_cm_s.
- Scoring: scored by hidden verifier

### Step 4: Produce electron temperature comparison
- Role: scored
- Action: From the simulation outputs, extract the time‑dependent electron temperature for both simulation types and write them to electron_temperature_vs_time.csv with columns: time_ps (float), Te_no_ee_K (float), Te_with_ee_K (float). The file must cover the full simulation time.
- Output file: `/app/outputs/electron_temperature_vs_time.csv`
- Format: csv
- Contract: Columns: time_ps, Te_no_ee_K, Te_with_ee_K.
- Scoring: scored by hidden verifier

### Step 5: Produce valley occupation comparison
- Role: scored
- Action: From the simulation outputs, extract the time‑dependent fractional valley populations (Γ and L) for both simulation types and write them to valley_population_vs_time.csv with columns: time_ps (float), Gamma_no_ee (float), L_no_ee (float), Gamma_with_ee (float), L_with_ee (float). The file must cover the full simulation time.
- Output file: `/app/outputs/valley_population_vs_time.csv`
- Format: csv
- Contract: Columns: time_ps, Gamma_no_ee, L_no_ee, Gamma_with_ee, L_with_ee.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/drift_velocity_vs_time.csv`
- `/app/outputs/electron_temperature_vs_time.csv`
- `/app/outputs/valley_population_vs_time.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### drift_velocity_vs_time.csv
- path: `/app/outputs/drift_velocity_vs_time.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Time evolution of drift velocity for the two simulation types. The checker will compare the two curves and the steady‑state value.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `v_drift_no_ee_cm_s`, `v_drift_with_ee_cm_s`
  - `units`:
    - `time_ps`: ps
    - `v_drift_no_ee_cm_s`: cm/s
    - `v_drift_with_ee_cm_s`: cm/s

### electron_temperature_vs_time.csv
- path: `/app/outputs/electron_temperature_vs_time.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Time evolution of electron temperature for the two simulation types. The checker will compare the two curves.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `Te_no_ee_K`, `Te_with_ee_K`
  - `units`:
    - `time_ps`: ps
    - `Te_no_ee_K`: K
    - `Te_with_ee_K`: K

### valley_population_vs_time.csv
- path: `/app/outputs/valley_population_vs_time.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Time evolution of Γ and L valley fractional populations for the two simulation types. The checker will compare the two sets of curves.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `Gamma_no_ee`, `L_no_ee`, `Gamma_with_ee`, `L_with_ee`
  - `units`:
    - `time_ps`: ps
    - `Gamma_no_ee`: fraction
    - `L_no_ee`: fraction
    - `Gamma_with_ee`: fraction
    - `L_with_ee`: fraction

Notes: The three CSV files contain time-series data produced by the Monte Carlo simulations. They are scored by recomputing the maximum relative difference between the with‑ee and no‑ee curves and by checking the absolute steady‑state drift velocity against a hidden reference. No gold values are visible in this contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "drift_velocity_vs_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "v_drift_no_ee_cm_s",
          "v_drift_with_ee_cm_s"
        ],
        "units": {
          "time_ps": "ps",
          "v_drift_no_ee_cm_s": "cm/s",
          "v_drift_with_ee_cm_s": "cm/s"
        }
      },
      "description": "Time evolution of drift velocity for the two simulation types. The checker will compare the two curves and the steady‑state value."
    },
    {
      "file": "electron_temperature_vs_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "Te_no_ee_K",
          "Te_with_ee_K"
        ],
        "units": {
          "time_ps": "ps",
          "Te_no_ee_K": "K",
          "Te_with_ee_K": "K"
        }
      },
      "description": "Time evolution of electron temperature for the two simulation types. The checker will compare the two curves."
    },
    {
      "file": "valley_population_vs_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "Gamma_no_ee",
          "L_no_ee",
          "Gamma_with_ee",
          "L_with_ee"
        ],
        "units": {
          "time_ps": "ps",
          "Gamma_no_ee": "fraction",
          "L_no_ee": "fraction",
          "Gamma_with_ee": "fraction",
          "L_with_ee": "fraction"
        }
      },
      "description": "Time evolution of Γ and L valley fractional populations for the two simulation types. The checker will compare the two sets of curves."
    }
  ],
  "notes": "The three CSV files contain time-series data produced by the Monte Carlo simulations. They are scored by recomputing the maximum relative difference between the with‑ee and no‑ee curves and by checking the absolute steady‑state drift velocity against a hidden reference. No gold values are visible in this contract."
}
```

## How you are scored
Each scored workflow stage produces one output file. A hidden verifier reads these files, recomputes derived quantities where applicable, and compares them against reference criteria. The three time‑series files carry the bulk of the reward weight. The verifier aggregates the stage scores into a single reward between 0 and 1, with higher scores indicating better agreement with the expected target. Simply reporting the paper’s published numbers without a genuine simulation will not satisfy the checks. The exact reference values and tolerances are hidden; the agent should focus on correctly implementing the described EMC methods and producing the required time‑series data.
