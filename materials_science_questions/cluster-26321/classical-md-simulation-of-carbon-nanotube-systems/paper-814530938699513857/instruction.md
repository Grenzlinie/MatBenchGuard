# Classical Molecular Dynamics of a Triple-Walled Carbon Nanotube Motor

## Problem background
A nanomotor built from triple-walled carbon nanotubes (TWCNTs) can convert thermal energy into mechanical motion. The outer tube is split into two fixed stators; when some atoms at the stator ends are displaced inward (inward radial deviation, IRD), the symmetry breaking causes thermal vibrations to collide with the free mid-rotor, driving its rotation. The inner-rotor is then driven by intertube friction, and it may simultaneously exhibit large-amplitude axial oscillation. Understanding how the rotational frequency, the relative synchronization of the rotors, and the oscillation amplitude depend on the IRD layout and on temperature is essential for designing such nano-devices.

## Approach
We use classical molecular dynamics with the AIREBO potential to simulate the TWCNT motor. The motor consists of (15,15) outer stators, a (10,10) mid-rotor, and a (5,5) inner-rotor. Eight IRD schemes are applied to the stator ends, varying the number and symmetry of the radially deviated atoms: 1L, 2L, 3L, 4L (left stator only) and 1LR, 2LR, 3LR, 4LR (both stators). The radial deviation is 0.4 times the C–C bond length. For each scheme, constant-temperature (NVT) simulations are run at several temperatures (200 K, 300 K, 400 K, and optionally 250 K, 350 K) for a total of 8000 ps with a 0.001 ps time step. After energy minimization, the stator atoms are fixed, and the rotational frequencies of both rotors as well as the axial centre-of-mass position of the inner-rotor are recorded at every time step. The compiled time series makes it possible to analyse the rotational acceleration, the stable frequency, the temperature trend, and the amplitude of the inner-rotor oscillation across all IRD configurations.

## Reproduction target
Produce a single CSV file (`/app/outputs/simulation_results.csv`) that contains the time series of rotational dynamics for every simulated (scheme, temperature) condition. The columns are: `scheme` (text), `temperature` (K), `time` (ps), `mid_rotor_frequency` (GHz), `inner_rotor_frequency` (GHz), and `inner_rotor_z_position` (nm). The file must cover the full 0–8000 ps interval for each combination. From this file, the stable rotational frequency of the mid-rotor (average over the last 1000 ps) and the amplitude of the inner-rotor axial oscillation can be computed. The evaluation will focus on: the stable mid-rotor frequency as a function of temperature for the 1LR and 4LR schemes; the temperature dependence of the mid-rotor frequency for the 1LR scheme (e.g., determine whether the frequency increases with temperature); and the amplitude of the inner-rotor oscillation.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/
- AIREBO potential

## Workflow steps

### Step 1: Build TWCNT motor atomic models
- Role: process
- Action: Generate initial atomic coordinates for the triple-walled CNT motor with (15,15) stators, (10,10) mid-rotor, (5,5) inner-rotor. Apply inward radial deviation (IRD) to stator end atoms for all eight schemes (1L, 2L, 3L, 4L, 1LR, 2LR, 3LR, 4LR). Write each configuration as a LAMMPS data file.
- Evidence: none

### Step 2: Run MD production simulations
- Role: process
- Action: For each structure (scheme) and temperature (at least 200 K, 300 K, 400 K; optionally 250, 350 K), perform energy minimization and NVT simulation in LAMMPS using the AIREBO potential, a time step of 0.001 ps, and a duration of 8000 ps. Fix the stator atoms after minimization. Compute and output the rotational frequencies of the mid-rotor and inner-rotor and the z‑center‑of‑mass of the inner‑rotor at every timestep.
- Evidence: none

### Step 3: Compile rotational dynamics time series
- Role: scored (load-bearing)
- Action: Collect the mid-rotor and inner-rotor rotational frequencies and inner-rotor z-position from all simulation outputs and write a single CSV file containing the columns: scheme, temperature, time, mid_rotor_frequency, inner_rotor_frequency, inner_rotor_z_position.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: Columns: scheme (text), temperature (float, K), time (float, ps), mid_rotor_frequency (float, GHz), inner_rotor_frequency (float, GHz), inner_rotor_z_position (float, nm). One row per time step per condition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of rotational frequencies and inner-rotor z-position from the MD simulations. The checker recomputes stable rotational frequencies and oscillation trends.
- schema:
  - `type`: table
  - `required_columns`: `scheme`, `temperature`, `time`, `mid_rotor_frequency`, `inner_rotor_frequency`, `inner_rotor_z_position`
  - `units`:
    - `temperature`: K
    - `time`: ps
    - `mid_rotor_frequency`: GHz
    - `inner_rotor_frequency`: GHz
    - `inner_rotor_z_position`: nm

Notes: The time series must cover the full 8000 ps for each simulated condition. The checker will compute the stable rotational frequency of the mid-rotor from the last 1000 ps and verify the temperature dependence and the oscillation amplitude.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "scheme",
          "temperature",
          "time",
          "mid_rotor_frequency",
          "inner_rotor_frequency",
          "inner_rotor_z_position"
        ],
        "units": {
          "temperature": "K",
          "time": "ps",
          "mid_rotor_frequency": "GHz",
          "inner_rotor_frequency": "GHz",
          "inner_rotor_z_position": "nm"
        }
      },
      "description": "Time series of rotational frequencies and inner-rotor z-position from the MD simulations. The checker recomputes stable rotational frequencies and oscillation trends."
    }
  ],
  "notes": "The time series must cover the full 8000 ps for each simulated condition. The checker will compute the stable rotational frequency of the mid-rotor from the last 1000 ps and verify the temperature dependence and the oscillation amplitude."
}
```

## How you are scored
An automatic hidden verifier will read `simulation_results.csv`, recompute the stable rotational frequencies (from the last 1000 ps) and the oscillation amplitude for the relevant schemes and temperatures, and compare these quantities against expected reference values. It checks trends (e.g., the temperature dependence of the mid-rotor frequency for the 1LR scheme) and verifies that the magnitudes lie within realistic ranges. Each check is weighted and the final reward (0–1) reflects how well the time series reproduce the physical behaviour. Providing numbers that happen to match the paper's published values without a physically consistent time series will not yield a high score.
