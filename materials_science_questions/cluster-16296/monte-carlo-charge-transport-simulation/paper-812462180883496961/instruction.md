# Quantum Monte Carlo Simulation of Drift-Velocity Overshoot in Silicon

## Problem background
Charge transport quantum effects in semiconductors become important at small scales. This task investigates the influence of the intracollisional field effect on the transient drift‑velocity overshoot in silicon. Using a homogeneous electron gas model with a single spherical parabolic band and optical phonon scattering, the goal is to quantify the difference between a fully quantum description of transport and the standard semiclassical picture under pulsed electric fields at cryogenic and room temperature.

## Approach
The core of the reproduction is a quantum Monte Carlo (QMC) simulation based on the time evolution of the electronic density matrix. The approach works in the basis of accelerated plane waves (interaction picture with respect to the electric field) and uses a transformed density matrix that absorbs a damping factor γ into a dressed propagator. An iterative perturbative expansion, analogous to the Chambers formulation of semiclassical transport, is sampled with Monte Carlo techniques. This automatically accounts for quantum out‑scattering and reproduces the intracollisional field effect without requiring a full solution of the Liouville–von Neumann equation. The QMC simulation is complemented by a standard semiclassical ensemble Monte Carlo simulation of the Boltzmann equation for the identical physical model. Both simulations are run for the same system parameters and initial conditions. The model consists of a single spherical parabolic band (effective mass 0.295 m₀) and a single optical phonon mode (equivalent temperature 450 K, deformation‑potential coupling constant 8 × 10⁸ eV cm⁻¹, crystal density 2.329 g cm⁻³). A constant damping factor γ (chosen reasonably, e.g. on the order of the scattering rate) is used for the QMC. Ensemble‑averaged drift velocity and mean kinetic energy are recorded as functions of time from 0 to 1 ps, providing a clear comparison between quantum and semiclassical dynamics.

## Reproduction target
Produce four CSV files, one for each of the following electric field / temperature combinations: (20 kV cm⁻¹, 10 K), (40 kV cm⁻¹, 10 K), (60 kV cm⁻¹, 10 K), and (60 kV cm⁻¹, 300 K). Every file must contain columns: `time_ps`, `quantum_drift_velocity_cm_per_s`, `semiclassical_drift_velocity_cm_per_s`, `quantum_mean_kinetic_energy_eV`, `semiclassical_mean_kinetic_energy_eV`. The time axis should span 0–1 ps with sufficient resolution to capture the overshoot dynamics. The values must be self‑consistent: both the semiclassical and quantum columns must originate from the same model and simulation setup for that condition.

## Assets

- Python scientific computing environment

## Workflow steps

### Step 1: Initialize semiconductor model
- Role: process
- Action: Define the simplified silicon model parameters: a single spherical parabolic band with effective mass m*=0.295 m0, a single optical phonon mode with equivalent temperature 450 K, deformation-potential coupling constant 8e8 eV/cm, and crystal density 2.329 g/cm³. Set up the initial equilibrium electron distribution (Maxwell-Boltzmann or Fermi-Dirac appropriate to the chosen temperature). Store the model configuration so downstream steps can load it.
- Evidence: `/app/outputs/model_init.json`

### Step 2: Run semiclassical Monte Carlo simulation
- Role: process
- Action: For each condition (E=20, 40, 60 kV/cm at T=10 K, and E=60 kV/cm at T=300 K), perform a standard semiclassical ensemble Monte Carlo simulation of the Boltzmann equation using the model from step 1. Record the ensemble-averaged drift velocity (cm/s) and mean kinetic energy (eV) as a function of time from 0 to 1 ps with sufficient temporal resolution. Save the raw time series for later assembly.
- Evidence: `/app/outputs/semiclassical_traces.json`

### Step 3: Run quantum Monte Carlo simulation
- Role: process
- Action: Implement the quantum Monte Carlo algorithm based on the transformed density matrix and the Chambers-like iterative expansion with a constant damping factor γ (choose a reasonable value, e.g., on the order of the scattering rate). For the same four conditions, simulate carrier transport and record the ensemble-averaged quantum drift velocity (cm/s) and mean kinetic energy (eV) time series, using enough trajectories to obtain stable averages.
- Evidence: `/app/outputs/qmc_traces.json`

### Step 4: Generate drift_velocity_E20_T10.csv
- Role: scored (load-bearing)
- Action: Combine the semiclassical and quantum time series for E=20 kV/cm, T=10 K into a CSV file with columns: time_ps, quantum_drift_velocity_cm_per_s, semiclassical_drift_velocity_cm_per_s, quantum_mean_kinetic_energy_eV, semiclassical_mean_kinetic_energy_eV. Write the file to /app/outputs/drift_velocity_E20_T10.csv.
- Output file: `/app/outputs/drift_velocity_E20_T10.csv`
- Format: csv
- Contract: CSV with columns: time_ps (float), quantum_drift_velocity_cm_per_s (float), semiclassical_drift_velocity_cm_per_s (float), quantum_mean_kinetic_energy_eV (float), semiclassical_mean_kinetic_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 5: Generate drift_velocity_E40_T10.csv
- Role: scored (load-bearing)
- Action: Combine the semiclassical and quantum time series for E=40 kV/cm, T=10 K into a CSV with the same schema. Write /app/outputs/drift_velocity_E40_T10.csv.
- Output file: `/app/outputs/drift_velocity_E40_T10.csv`
- Format: csv
- Contract: Same schema as step_4.
- Scoring: scored by hidden verifier

### Step 6: Generate drift_velocity_E60_T10.csv
- Role: scored (load-bearing)
- Action: Combine the semiclassical and quantum time series for E=60 kV/cm, T=10 K into a CSV with the same schema. Write /app/outputs/drift_velocity_E60_T10.csv.
- Output file: `/app/outputs/drift_velocity_E60_T10.csv`
- Format: csv
- Contract: Same schema as step_4.
- Scoring: scored by hidden verifier

### Step 7: Generate drift_velocity_E60_T300.csv
- Role: scored (load-bearing)
- Action: Combine the semiclassical and quantum time series for E=60 kV/cm, T=300 K into a CSV with the same schema. Write /app/outputs/drift_velocity_E60_T300.csv.
- Output file: `/app/outputs/drift_velocity_E60_T300.csv`
- Format: csv
- Contract: Same schema as step_4.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/drift_velocity_E20_T10.csv`
- `/app/outputs/drift_velocity_E40_T10.csv`
- `/app/outputs/drift_velocity_E60_T10.csv`
- `/app/outputs/drift_velocity_E60_T300.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### drift_velocity_E20_T10.csv
- path: `/app/outputs/drift_velocity_E20_T10.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Combined time series of drift velocity and mean kinetic energy for E=20 kV/cm, T=10 K.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `quantum_drift_velocity_cm_per_s`, `semiclassical_drift_velocity_cm_per_s`, `quantum_mean_kinetic_energy_eV`, `semiclassical_mean_kinetic_energy_eV`
  - `units`:
    - `time_ps`: ps
    - `quantum_drift_velocity_cm_per_s`: cm/s
    - `semiclassical_drift_velocity_cm_per_s`: cm/s
    - `quantum_mean_kinetic_energy_eV`: eV
    - `semiclassical_mean_kinetic_energy_eV`: eV

### drift_velocity_E40_T10.csv
- path: `/app/outputs/drift_velocity_E40_T10.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Combined time series of drift velocity and mean kinetic energy for E=40 kV/cm, T=10 K.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `quantum_drift_velocity_cm_per_s`, `semiclassical_drift_velocity_cm_per_s`, `quantum_mean_kinetic_energy_eV`, `semiclassical_mean_kinetic_energy_eV`
  - `units`:
    - `time_ps`: ps
    - `quantum_drift_velocity_cm_per_s`: cm/s
    - `semiclassical_drift_velocity_cm_per_s`: cm/s
    - `quantum_mean_kinetic_energy_eV`: eV
    - `semiclassical_mean_kinetic_energy_eV`: eV

### drift_velocity_E60_T10.csv
- path: `/app/outputs/drift_velocity_E60_T10.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Combined time series of drift velocity and mean kinetic energy for E=60 kV/cm, T=10 K.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `quantum_drift_velocity_cm_per_s`, `semiclassical_drift_velocity_cm_per_s`, `quantum_mean_kinetic_energy_eV`, `semiclassical_mean_kinetic_energy_eV`
  - `units`:
    - `time_ps`: ps
    - `quantum_drift_velocity_cm_per_s`: cm/s
    - `semiclassical_drift_velocity_cm_per_s`: cm/s
    - `quantum_mean_kinetic_energy_eV`: eV
    - `semiclassical_mean_kinetic_energy_eV`: eV

### drift_velocity_E60_T300.csv
- path: `/app/outputs/drift_velocity_E60_T300.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Combined time series of drift velocity and mean kinetic energy for E=60 kV/cm, T=300 K.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `quantum_drift_velocity_cm_per_s`, `semiclassical_drift_velocity_cm_per_s`, `quantum_mean_kinetic_energy_eV`, `semiclassical_mean_kinetic_energy_eV`
  - `units`:
    - `time_ps`: ps
    - `quantum_drift_velocity_cm_per_s`: cm/s
    - `semiclassical_drift_velocity_cm_per_s`: cm/s
    - `quantum_mean_kinetic_energy_eV`: eV
    - `semiclassical_mean_kinetic_energy_eV`: eV

Notes: The hidden checker compares the agent's quantum drift velocity and mean kinetic energy values at pre-specified time points to reference values digitized from the paper, using tolerances that absorb implementation variability. It also performs a structural audit: for each condition the quantum drift velocity must exceed the semiclassical one in the overshoot region, and the ratio of quantum to semiclassical peak must increase with electric field at 10 K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "drift_velocity_E20_T10.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "quantum_drift_velocity_cm_per_s",
          "semiclassical_drift_velocity_cm_per_s",
          "quantum_mean_kinetic_energy_eV",
          "semiclassical_mean_kinetic_energy_eV"
        ],
        "units": {
          "time_ps": "ps",
          "quantum_drift_velocity_cm_per_s": "cm/s",
          "semiclassical_drift_velocity_cm_per_s": "cm/s",
          "quantum_mean_kinetic_energy_eV": "eV",
          "semiclassical_mean_kinetic_energy_eV": "eV"
        }
      },
      "description": "Combined time series of drift velocity and mean kinetic energy for E=20 kV/cm, T=10 K."
    },
    {
      "file": "drift_velocity_E40_T10.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "quantum_drift_velocity_cm_per_s",
          "semiclassical_drift_velocity_cm_per_s",
          "quantum_mean_kinetic_energy_eV",
          "semiclassical_mean_kinetic_energy_eV"
        ],
        "units": {
          "time_ps": "ps",
          "quantum_drift_velocity_cm_per_s": "cm/s",
          "semiclassical_drift_velocity_cm_per_s": "cm/s",
          "quantum_mean_kinetic_energy_eV": "eV",
          "semiclassical_mean_kinetic_energy_eV": "eV"
        }
      },
      "description": "Combined time series of drift velocity and mean kinetic energy for E=40 kV/cm, T=10 K."
    },
    {
      "file": "drift_velocity_E60_T10.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "quantum_drift_velocity_cm_per_s",
          "semiclassical_drift_velocity_cm_per_s",
          "quantum_mean_kinetic_energy_eV",
          "semiclassical_mean_kinetic_energy_eV"
        ],
        "units": {
          "time_ps": "ps",
          "quantum_drift_velocity_cm_per_s": "cm/s",
          "semiclassical_drift_velocity_cm_per_s": "cm/s",
          "quantum_mean_kinetic_energy_eV": "eV",
          "semiclassical_mean_kinetic_energy_eV": "eV"
        }
      },
      "description": "Combined time series of drift velocity and mean kinetic energy for E=60 kV/cm, T=10 K."
    },
    {
      "file": "drift_velocity_E60_T300.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "quantum_drift_velocity_cm_per_s",
          "semiclassical_drift_velocity_cm_per_s",
          "quantum_mean_kinetic_energy_eV",
          "semiclassical_mean_kinetic_energy_eV"
        ],
        "units": {
          "time_ps": "ps",
          "quantum_drift_velocity_cm_per_s": "cm/s",
          "semiclassical_drift_velocity_cm_per_s": "cm/s",
          "quantum_mean_kinetic_energy_eV": "eV",
          "semiclassical_mean_kinetic_energy_eV": "eV"
        }
      },
      "description": "Combined time series of drift velocity and mean kinetic energy for E=60 kV/cm, T=300 K."
    }
  ],
  "notes": "The hidden checker compares the agent's quantum drift velocity and mean kinetic energy values at pre-specified time points to reference values digitized from the paper, using tolerances that absorb implementation variability. It also performs a structural audit: for each condition the quantum drift velocity must exceed the semiclassical one in the overshoot region, and the ratio of quantum to semiclassical peak must increase with electric field at 10 K."
}
```

## How you are scored
A hidden verifier inspects each output CSV. It compares your quantum drift velocity and mean kinetic energy time series to reference values at multiple time points, using tolerances that accommodate legitimate differences between implementations. Additionally, the verifier checks structural relationships (for example, the sign of the quantum‑semiclassical difference in the overshoot interval and how the magnitude of the overshoot enhancement varies with electric field). Each scored file contributes a weighted portion to the final reward, which is normalized to the 0–1 range. Missing or ill‑formatted files receive zero for that part. The objective is a physically correct re‑implementation of the described quantum Monte Carlo method, not a naïvely guessed number.
