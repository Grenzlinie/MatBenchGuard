# Monte Carlo Simulation of Electron Storage and Secondary Production in a Magnetic Bottle

## Problem background
The KATRIN experiment uses a large MAC-E filter spectrometer to measure the neutrino mass. The spectrometer’s magnetic configuration forms a magnetic bottle that can trap charged particles. Nuclear decays occurring inside the spectrometer volume produce primary electrons with energies up to tens of keV, which may be stored for extended periods. During storage, these primary electrons lose energy through scattering on residual gas molecules, producing low-energy secondary electrons. These secondaries can reach the detector and constitute a background for the neutrino mass measurement. To estimate this background, it is essential to determine the correlation between the primary electron’s initial kinetic energy, the duration for which it remains trapped (storage time), and the number of secondary electrons it generates. This task requires computing these quantities via a Monte Carlo simulation under relevant conditions.

## Approach
A Monte Carlo particle-transport simulation tracks individual primary electrons in a magnetic field geometry representative of the KATRIN MAC-E filter. The magnetic bottle is defined by a low central field (Bmin ≈ 0.6 mT) and strong high-field regions at the ends (Bmax ≈ 4.2 T) with a mirror ratio around 7000. The vacuum is specified as ultra-high vacuum (10⁻¹¹ mbar) of residual hydrogen. The simulation must include physical processes that govern electron dynamics: synchrotron radiation energy losses, elastic and inelastic scattering on residual gas molecules (ionization and excitation), and non-adiabatic effects. For a given primary electron energy, the electron is tracked until it escapes the trap or its kinetic energy becomes negligible. The simulation records the total storage time and the total number of secondary electrons produced during the trajectory. This procedure is repeated for several primary energies to establish the energy dependence.

## Reproduction target
Run the Monte Carlo simulation for primary kinetic energies of 5 keV, 10 keV, and 20 keV. For each energy, output the storage time (in hours) and the number of secondary electrons. The result must be compiled into a CSV file `step_01_metrics.csv` with columns `energy_keV`, `storage_time_hours`, `secondary_count`, containing one row per energy. The reproduction target is to obtain values that are consistent with the underlying physics, and to demonstrate that both the storage time and the secondary multiplicity increase monotonically with primary energy.

## Assets

- Geant4 or equivalent open-source Monte Carlo particle transport toolkit: https://geant4.web.cern.ch

## Workflow steps

### Step 1: Monte Carlo electron transport simulation
- Role: process
- Action: Set up a Monte Carlo simulation of electron transport in a magnetic bottle representative of the KATRIN MAC-E filter. Define the magnetic field geometry (mirror ratio ~7000, Bmin ~0.6 mT, Bmax ~4.2 T) and ultra-high vacuum (10^-11 mbar H2). Implement or use a particle transport toolkit to track primary electrons with initial kinetic energies including 5, 10, and 20 keV. Include physics processes: synchrotron radiation, elastic and inelastic scattering on residual gas, and non-adiabatic effects. For each energy, record the storage time (time until the electron escapes the trap or its kinetic energy becomes negligible) and the total number of secondary electrons produced during storage. Optionally produce a log or trajectory file as evidence.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compile simulation results
- Role: scored (load-bearing)
- Action: Collect the simulation outputs and produce a CSV file with columns energy_keV, storage_time_hours, secondary_count. Include at least rows for the primary energies 5, 10, and 20 keV. All values must be directly derived from the simulation run.
- Output file: `/app/outputs/step_01_metrics.csv`
- Format: csv
- Contract: Columns: energy_keV (float), storage_time_hours (float), secondary_count (int). At minimum three rows for energies 5, 10, 20 keV are required.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_metrics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_metrics.csv
- path: `/app/outputs/step_01_metrics.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Quantitative results of the Monte Carlo electron transport simulation: storage time and secondary electron count for each simulated primary electron energy. The values must be non-decreasing with increasing primary energy.
- schema:
  - `type`: table
  - `required_columns`: `energy_keV`, `storage_time_hours`, `secondary_count`

Notes: The storage_time_hours and secondary_count are expected to be monotonic non-decreasing when energy_keV increases (5 < 10 < 20). The absolute values are compared to a hidden reference derived from the original paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_metrics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_keV",
          "storage_time_hours",
          "secondary_count"
        ]
      },
      "description": "Quantitative results of the Monte Carlo electron transport simulation: storage time and secondary electron count for each simulated primary electron energy. The values must be non-decreasing with increasing primary energy."
    }
  ],
  "notes": "The storage_time_hours and secondary_count are expected to be monotonic non-decreasing when energy_keV increases (5 < 10 < 20). The absolute values are compared to a hidden reference derived from the original paper."
}
```

## How you are scored
A hidden verifier reads your `step_01_metrics.csv` file. It compares the storage time and secondary count for the 10 keV primary against a hidden reference derived from the original study, awarding credit for values within a tolerance band. It also checks that `storage_time_hours` and `secondary_count` are non-decreasing when going from 5 keV to 10 keV to 20 keV. The 10 keV values account for 80% of the total score (40% each for storage time and secondary count), and the monotonicity check accounts for the remaining 20%. You must run a genuine simulation that respects the specified physics; reporting numbers without an underlying computation will not pass the verifier.
