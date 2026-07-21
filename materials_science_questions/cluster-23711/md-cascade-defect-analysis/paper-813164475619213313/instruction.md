# Energy Equipartition and Disordered Volume Scaling in UO₂ Cascades via Molecular Dynamics

## Problem background
Uranium dioxide (UO₂) is the most widely used nuclear fuel. Under irradiation, atomic collisions create displacement cascades that generate defects and alter the material's microstructure. The thermal evolution of these cascades is often approximated by thermal spike models, but their physical relevance is debated. This work uses classical molecular dynamics to simulate displacement cascades and dedicated thermal spikes in UO₂. The primary open questions are (i) whether the kinetic energy injected by a primary knock-on atom partitions equally between kinetic and potential forms (energy equipartition) in cascades, and whether thermal spike simulations exhibit the same behavior, and (ii) how the maximum volume of material brought above the melting temperature scales with the cascade energy, and whether it follows the prediction of a simple heat‑equation model.

## Approach
The experiment uses the CP2K program with the Morelon empirical potential for UO₂ and the ZBL universal potential for short‑range collisions. Two types of simulations are run in an NVE ensemble on an initially equilibrated single crystal at 700 K: (a) full displacement cascades, where a uranium PKA is accelerated with energies ranging from 0.2 to 20 keV, and (b) spherical thermal spikes, where the same total kinetic energy is injected by rescaling atom velocities within a sphere (no PKA). In both cases, the total kinetic energy and total potential energy of the simulation cell are recorded as functions of time, normalized by the total injected kinetic energy. A local temperature is defined from the mean kinetic energy per atom in small cubes, and the volume where this local temperature exceeds the melting temperature of UO₂ (3120 K) is tracked. This disordered volume is computed for each cascade energy; its maximum value as a function of energy is compared to the prediction of a continuous heat‑equation solution, which suggests that the maximum melted volume scales linearly with the cascade energy, with a coefficient determined by the material's density, the melting temperature, and the initial equilibrium temperature.

## Reproduction target
Run the two sets of MD simulations and extract three key datasets: (1) the average normalized kinetic and potential energy time series for 20 keV cascades at 700 K, from which the occurrence (or not) of energy equipartition can be assessed; (2) the analogous time series for a 20 keV thermal spike, to measure whether the energy remains predominantly kinetic; (3) the maximum disordered volume as a function of cascade energy (0.2–20 keV) at 700 K, to test whether the volume scales linearly with energy and whether its slope is consistent with the theoretical expression derived from the heat equation model.

## Assets

- CP2K: https://www.cp2k.org/
- Morelon empirical potential for UO₂: 10.1080/1478643031000115858
- Ziegler-Biersack-Littmark (ZBL) universal potential: 10.1016/B978-0-08-021607-2.50011-3
- UO₂ fluorite crystal structure
- UO₂ material properties (density, melting temperature, thermal diffusivity): 10.1016/S0022-3115(99)00273-1

## Workflow steps

### Step 1: Run displacement cascade MD simulations
- Role: process
- Action: Set up a UO₂ single crystal (fluorite structure) with the Morelon potential for lattice interactions and ZBL for short‑range collisions, using CP2K. Equilibrate the cell at 700 K. For cascade energies 0.2, 1, 5, 10, and 20 keV, accelerate a uranium primary knock-on atom (PKA) with a random direction and run NVE dynamics. At each logged timestep, record the total kinetic energy and total potential energy of the simulation cell, as well as atomic trajectories. Perform at least three independent cascade runs per energy (different PKA directions/positions).
- Evidence: `/app/outputs/cascade_simulation_summary.txt`

### Step 2: Run thermal spike MD simulations
- Role: process
- Action: Using the same equilibrated UO₂ cell at 700 K, create a spherical thermal spike by rescaling velocities of atoms inside a sphere so that the total injected kinetic energy equals 20 keV. Ensure no atom gains more than 20 eV. Use velocity directions either from the equilibrated cell or randomized (the result is insensitive to this choice). Run NVE dynamics with a weak thermostat on the outermost atomic layers to dissipate heat. Record total kinetic and potential energies and atomic trajectories.
- Evidence: `/app/outputs/thermal_spike_simulation_summary.txt`

### Step 3: Extract cascade energy equipartition data
- Role: scored (load-bearing)
- Action: From the MD runs of 20 keV cascades at 700 K (at least three independent runs), compute the average total kinetic energy and average total potential energy at each logged time step, normalized by the initial PKA kinetic energy E₀. Write a CSV file with columns time_ps, kinetic_norm, potential_norm.
- Output file: `/app/outputs/step_01_cascade_energies.csv`
- Format: csv
- Contract: Columns: time_ps (float), kinetic_norm (float), potential_norm (float).
- Scoring: scored by hidden verifier

### Step 4: Extract thermal spike energy time series
- Role: scored
- Action: From the MD runs of a 20 keV thermal spike at 700 K, compute the average total kinetic and potential energies, normalized by the total injected kinetic energy E₀. Write a CSV file with columns time_ps, kinetic_norm, potential_norm.
- Output file: `/app/outputs/step_02_thermal_spike_energies.csv`
- Format: csv
- Contract: Columns: time_ps (float), kinetic_norm (float), potential_norm (float).
- Scoring: scored by hidden verifier

### Step 5: Compute maximum disordered volume vs. cascade energy
- Role: scored
- Action: For each cascade energy (0.2, 1, 5, 10, 20 keV) at 700 K, use the atomic trajectories to compute a local temperature from the mean kinetic energy per atom in cubes of side 1.5a (a = UO₂ unit‑cell dimension). Identify the volume V(t) where the local temperature exceeds the melting temperature 3120 K. Record the maximum Vmax reached during the simulation for each cascade run, then average over the at least three runs per energy. Write a CSV with columns energy_keV, max_volume_nm3.
- Output file: `/app/outputs/step_03_max_volume_vs_energy.csv`
- Format: csv
- Contract: Columns: energy_keV (float), max_volume_nm3 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_cascade_energies.csv`
- `/app/outputs/step_02_thermal_spike_energies.csv`
- `/app/outputs/step_03_max_volume_vs_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_cascade_energies.csv
- path: `/app/outputs/step_01_cascade_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Energy equipartition curves for 20 keV cascades at 700 K: kinetic_norm should drop from ~1.0 to ~0.5 and potential_norm should rise correspondingly within approximately 0.35 ps.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `kinetic_norm`, `potential_norm`
  - `units`:
    - `time_ps`: ps
    - `kinetic_norm`: dimensionless (E/E0)
    - `potential_norm`: dimensionless (ΔE/E0)

### step_02_thermal_spike_energies.csv
- path: `/app/outputs/step_02_thermal_spike_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Energy curves for a 20 keV thermal spike at 700 K: kinetic_norm should stay near 1.0 and potential_norm should show little variation, indicating no equipartition.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `kinetic_norm`, `potential_norm`
  - `units`:
    - `time_ps`: ps
    - `kinetic_norm`: dimensionless (E/E0)
    - `potential_norm`: dimensionless (ΔE/E0)

### step_03_max_volume_vs_energy.csv
- path: `/app/outputs/step_03_max_volume_vs_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum disordered volume as a function of cascade energy. The checker will perform a linear fit and compare the slope to the theoretical value derived from Eq. 3 (using UO₂ density at 700 K, melting temperature, and E₀/2).
- schema:
  - `type`: table
  - `required_columns`: `energy_keV`, `max_volume_nm3`
  - `units`:
    - `energy_keV`: keV
    - `max_volume_nm3`: nm³

Notes: The structural checks on step_01 and step_02 verify the direction and magnitude of the energy transfer; the reference_match on step_03 tests agreement with the analytical model slope within a tolerance that absorbs tool‑chain variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_cascade_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "kinetic_norm",
          "potential_norm"
        ],
        "units": {
          "time_ps": "ps",
          "kinetic_norm": "dimensionless (E/E0)",
          "potential_norm": "dimensionless (ΔE/E0)"
        }
      },
      "description": "Energy equipartition curves for 20 keV cascades at 700 K: kinetic_norm should drop from ~1.0 to ~0.5 and potential_norm should rise correspondingly within approximately 0.35 ps."
    },
    {
      "file": "step_02_thermal_spike_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "kinetic_norm",
          "potential_norm"
        ],
        "units": {
          "time_ps": "ps",
          "kinetic_norm": "dimensionless (E/E0)",
          "potential_norm": "dimensionless (ΔE/E0)"
        }
      },
      "description": "Energy curves for a 20 keV thermal spike at 700 K: kinetic_norm should stay near 1.0 and potential_norm should show little variation, indicating no equipartition."
    },
    {
      "file": "step_03_max_volume_vs_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_keV",
          "max_volume_nm3"
        ],
        "units": {
          "energy_keV": "keV",
          "max_volume_nm3": "nm³"
        }
      },
      "description": "Maximum disordered volume as a function of cascade energy. The checker will perform a linear fit and compare the slope to the theoretical value derived from Eq. 3 (using UO₂ density at 700 K, melting temperature, and E₀/2)."
    }
  ],
  "notes": "The structural checks on step_01 and step_02 verify the direction and magnitude of the energy transfer; the reference_match on step_03 tests agreement with the analytical model slope within a tolerance that absorbs tool‑chain variation."
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier that examines each output file independently. For step 3 (the cascade energy curves), it checks that the kinetic energy drops and the potential energy rises within the expected time window, consistent with equipartition. For step 4 (the thermal spike curves), it verifies that the potential energy does not grow significantly and the kinetic energy remains dominant. For step 5 (the maximum volume versus energy), it fits a straight line to the submitted data points and compares the fitted slope to a theoretical value computed from the material properties (UO₂ density, melting temperature, and equilibrium temperature) using the heat‑equation model. The final score is a weighted combination of these three checks; reporting a result that merely matches the paper's numbers is not sufficient — the verifier requires the shape and trend extracted from your actual MD simulations.
