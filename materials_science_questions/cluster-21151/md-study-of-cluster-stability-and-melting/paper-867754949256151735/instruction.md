# Melting transitions in small sodium clusters from orbital-free Car-Parrinello molecular dynamics

## Problem background
Small sodium clusters undergo solid-like to liquid-like transitions that differ from bulk melting and may occur over broad temperature ranges with possible stepwise behavior. This task reproduces an orbital-free Car-Parrinello molecular dynamics study of melting in Na₈ and Na₂₀. The goal is to compute two caloric indicators — the relative root-mean-square bond length fluctuation δ and the specific heat C — as functions of cluster temperature, and to use the δ(T) curves to locate the temperatures at which melting-like transitions set in and complete.

## Approach
The method uses an orbital-free density functional theory (OF-DFT) energy functional that avoids Kohn-Sham orbitals by treating the valence electron density as the dynamic variable. The electronic kinetic energy is approximated by the gradient expansion through second order: Thomas-Fermi plus one-ninth Weizsäcker. Exchange and correlation are treated within the local density approximation (Perdew-Zunger parametrization), and the electron-ion interaction uses the local pseudopotential of Fiolhais et al. for sodium. The ground-state structures of Na₈ and Na₂₀ are first determined by dynamical simulated annealing (heat to 600 K then slow cool). A series of constant-energy molecular dynamics simulations is then performed for each cluster, spanning internal energies that correspond to low temperatures (below 50 K) up to high temperatures (above 300 K). From the ionic coordinates and velocities saved during each production run, the internal temperature T is computed from the average ionic kinetic energy, the relative RMS bond-length fluctuation δ from the variance of interatomic distances, and the specific heat C from fluctuations in the ionic kinetic energy. The resulting T, δ, and C values across all runs yield the caloric and fluctuation curves from which the melting transition temperatures are extracted.

## Reproduction target
Produce two CSV files — na8_caloric.csv and na20_caloric.csv — each containing columns temperature_K (float), delta (float), and specific_heat (float), with one row per simulated temperature. Use at least 8 distinct temperature points per cluster, spanning the full range from well below to well above the melting transitions. From the δ vs. temperature data, identify the approximate temperatures at which melting transitions begin, any intermediate steps, and where the liquid-like phase is fully established.

## Assets

- Orbital-free DFT package (e.g., GPAW): https://wiki.fysik.dtu.dk/gpaw/
- Fiolhais local pseudopotential parameters for sodium: 10.1103/PhysRevB.51.14001

## Workflow steps

### Step 1: Determine ground-state structures for Na8 and Na20
- Role: process
- Action: Using an orbital-free Car-Parrinello MD code (configured with gradient-expansion kinetic energy (Thomas-Fermi + 1/9 Weizsäcker), LDA exchange-correlation (Perdew-Zunger), and the local Fiolhais pseudopotential for sodium), perform dynamical simulated annealing (heat to 600 K then slow cool) to determine the ground-state atomic configurations of Na8 and Na20.
- Evidence: `/app/outputs/ground_state_structures.xyz`

### Step 2: Run constant-energy MD production runs for Na8
- Role: process
- Action: Starting from the Na8 ground-state geometry, perform a sequence of constant-energy orbital-free MD simulations at multiple internal energies covering low temperature (<50 K) to high temperature (>300 K). For each run, discard the first 2 ps for equilibration and save the ionic coordinates and velocities during the production phase.
- Evidence: `/app/outputs/na8_trajectories.log`

### Step 3: Compute Na8 melting indicators and write na8_caloric.csv
- Role: scored (load-bearing)
- Action: From the saved Na8 trajectories, compute for each production run the internal temperature T (from ionic kinetic energy average), the relative RMS bond length fluctuation δ, and the specific heat C (from fluctuations in ionic kinetic energy). Write the results to na8_caloric.csv.
- Output file: `/app/outputs/na8_caloric.csv`
- Format: csv
- Contract: Columns: temperature_K (float), delta (float), specific_heat (float). One row per simulated temperature.
- Scoring: scored by hidden verifier

### Step 4: Run constant-energy MD production runs for Na20
- Role: process
- Action: Starting from the Na20 ground-state geometry, perform a sequence of constant-energy orbital-free MD simulations at multiple internal energies covering low temperature (<50 K) to high temperature (>300 K). For each run, discard the first 2 ps for equilibration and save the ionic coordinates and velocities during the production phase.
- Evidence: `/app/outputs/na20_trajectories.log`

### Step 5: Compute Na20 melting indicators and write na20_caloric.csv
- Role: scored (load-bearing)
- Action: From the saved Na20 trajectories, compute for each production run the internal temperature T, relative RMS bond length fluctuation δ, and specific heat C. Write the results to na20_caloric.csv.
- Output file: `/app/outputs/na20_caloric.csv`
- Format: csv
- Contract: Columns: temperature_K (float), delta (float), specific_heat (float). One row per simulated temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/na8_caloric.csv`
- `/app/outputs/na20_caloric.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### na8_caloric.csv
- path: `/app/outputs/na8_caloric.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed temperature, bond length fluctuation and specific heat for Na8. The checker will extract transition temperatures from δ(T) and compare against hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `delta`, `specific_heat`
  - `units`:
    - `temperature_K`: Kelvin
    - `delta`: dimensionless
    - `specific_heat`: dimensionless

### na20_caloric.csv
- path: `/app/outputs/na20_caloric.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed temperature, bond length fluctuation and specific heat for Na20. The checker will extract transition temperatures from δ(T) and compare against hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `delta`, `specific_heat`
  - `units`:
    - `temperature_K`: Kelvin
    - `delta`: dimensionless
    - `specific_heat`: dimensionless

Notes: The checker identifies melting transition temperatures from the δ vs T data and compares them to reference values within tolerance. No paper-specific details are provided in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "na8_caloric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "delta",
          "specific_heat"
        ],
        "units": {
          "temperature_K": "Kelvin",
          "delta": "dimensionless",
          "specific_heat": "dimensionless"
        }
      },
      "description": "Computed temperature, bond length fluctuation and specific heat for Na8. The checker will extract transition temperatures from δ(T) and compare against hidden reference values."
    },
    {
      "file": "na20_caloric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "delta",
          "specific_heat"
        ],
        "units": {
          "temperature_K": "Kelvin",
          "delta": "dimensionless",
          "specific_heat": "dimensionless"
        }
      },
      "description": "Computed temperature, bond length fluctuation and specific heat for Na20. The checker will extract transition temperatures from δ(T) and compare against hidden reference values."
    }
  ],
  "notes": "The checker identifies melting transition temperatures from the δ vs T data and compares them to reference values within tolerance. No paper-specific details are provided in the public contract."
}
```

## How you are scored
A hidden verifier reads your CSV files and scores them per cluster. It computes the numerical derivative of δ with respect to temperature, locates the temperature(s) where δ shows a sharp stepwise increase, and matches those candidate transition temperatures against expected values known to the verifier. It also verifies that the specific heat C exhibits peaks in the corresponding transition regions. The final reward is proportional to how many of the expected transition temperatures are correctly identified and that the δ values lie in a physically reasonable range (0.0–0.5). Simply reporting numbers without running the required simulations is insufficient; the verifier checks internal consistency between δ, C, and temperature.
