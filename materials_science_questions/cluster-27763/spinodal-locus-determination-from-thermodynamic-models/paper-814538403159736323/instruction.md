# Short-Time Dynamics Monte Carlo Determination of Spinodals and Critical Point for Lennard-Jones Fluid

## Problem background
The gas-liquid phase transition in fluids is accompanied by a region of metastability where a phase can persist beyond the coexistence curve. The boundary beyond which the metastable phase becomes mechanically unstable is the thermodynamic spinodal. Determining the spinodal is challenging because equilibrium measurements in the deeply metastable region are difficult. Short-time dynamics (STD) provides a way to locate spinodals by studying the early-time relaxation of density fluctuations after a quench, without needing to reach equilibrium. In this task, you will apply the STD Monte Carlo method to a model Lennard-Jones fluid to compute its gas and liquid spinodal temperatures at several reduced pressures and to locate the critical point.

## Approach
The method studies the time evolution of the second moment of the global density, ρ^(2)(t), after the system is quenched to a final temperature at fixed pressure. Two types of initial conditions are used: a compressed liquid (ordered initial condition, OIC) to probe the liquid spinodal, and a hot gas at an estimated spinodal density (disordered initial condition, DIC) to probe the gas spinodal. The spinodal temperature for each phase and pressure is the temperature at which ρ^(2)(t) decays as a power law over at least one decade in time. To prepare the disordered initial condition, you first perform hysteresis loops to obtain rough estimates of the gas spinodal density. For each pressure, Monte Carlo simulations in the NpT ensemble (N=1728 particles, truncated Lennard-Jones potential with cutoff rc=2.5σ) are run for many independent trajectories (~2000) at several final temperatures around the expected spinodal. From the ρ^(2)(t) data, the liquid and gas spinodal temperatures are extracted. The critical point is then estimated by fitting the spinodal temperatures as a function of pressure and finding the intersection of the gas and liquid branches.

## Reproduction target
Compute the following quantities using the described STD Monte Carlo protocol and write them to `/app/outputs/spinodal_results.json` in the specified JSON format:

- Gas spinodal reduced temperatures at fixed reduced pressures p*=0.04, 0.10, and 0.1105.
- Liquid spinodal reduced temperatures at the same pressures.
- Critical reduced pressure p_c* and critical reduced temperature T_c* from the intersection of the spinodal curves.

## Assets
No external datasets or pre-built models are required. You are expected to implement the truncated Lennard-Jones potential and the Monte Carlo simulation from scratch. Standard numerical libraries (e.g., NumPy, SciPy) are available for data analysis.

## Workflow steps

### Step 1: Hysteresis loop simulation (gas density estimation)
- Role: process
- Action: Run isobaric NpT Monte Carlo simulations of the truncated Lennard-Jones fluid (rc=2.5σ) to produce hysteresis loops at reduced pressures p*=0.04 and 0.10 (and optionally p*=0.1105) by sweeping temperature. Use these loops to obtain rough estimates of the gas spinodal density ρ0* needed to initialise the disordered state for STD simulations.
- Evidence: `/app/outputs/hysteresis_densities.txt`

### Step 2: Short-time dynamics from ordered initial condition (liquid)
- Role: process
- Action: For each final pressure p_f*=0.04, 0.10, 0.1105, prepare a compressed liquid initial configuration (N=1728, ρ0*=0.82, T0*=∞) and perform NpT Monte Carlo simulations at several final temperatures T_f* around the expected liquid spinodal. For each (p_f*, T_f*) combination, run approximately 2000 independent trajectories and record the time series of the second moment of the global density ρ^(2)(t).
- Evidence: `/app/outputs/oic_rho2_data.zip`

### Step 3: Short-time dynamics from disordered initial condition (gas)
- Role: process
- Action: For each final pressure p_f*=0.04, 0.10, 0.1105, prepare a disordered gas initial configuration (N=1728, the estimated gas spinodal density ρ0* from the hysteresis step, T0*=∞) and perform NpT Monte Carlo simulations at several final temperatures T_f* around the expected gas spinodal. For each (p_f*, T_f*) combination, run approximately 2000 independent trajectories and record the time series of the second moment of the global density ρ^(2)(t).
- Evidence: `/app/outputs/dic_rho2_data.zip`

### Step 4: Determine spinodal temperatures and critical point
- Role: scored (load-bearing)
- Action: From the ρ^(2)(t) time series obtained in the previous steps, identify the liquid and gas spinodal temperatures for each pressure by detecting the temperature at which ρ^(2)(t) follows a power-law over at least one decade. Use quadratic fits to the gas and liquid spinodal temperatures as functions of pressure to find their intersection, yielding the critical reduced temperature T_c* and pressure p_c*. Output the final values as a JSON file.
- Output file: `/app/outputs/spinodal_results.json`
- Format: json
- Contract: {"gas_spinodal_temperatures": {"p_0_04": number, "p_0_10": number, "p_0_1105": number}, "liquid_spinodal_temperatures": {"p_0_04": number, "p_0_10": number, "p_0_1105": number}, "critical_point": {"p_c": number, "T_c": number}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spinodal_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spinodal_results.json
- path: `/app/outputs/spinodal_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed gas and liquid spinodal temperatures at three reduced pressures, and the critical point estimated from their intersection, for the truncated Lennard-Jones fluid (rc=2.5σ).
- schema:
  - `type`: object
  - `required`: `gas_spinodal_temperatures`, `liquid_spinodal_temperatures`, `critical_point`
  - `properties`:
    - `gas_spinodal_temperatures`:
      - `type`: object
      - `required`: `p_0_04`, `p_0_10`, `p_0_1105`
      - `properties`:
        - `p_0_04`:
          - `type`: number
          - `description`: gas spinodal reduced temperature at p*=0.04
        - `p_0_10`:
          - `type`: number
          - `description`: gas spinodal reduced temperature at p*=0.10
        - `p_0_1105`:
          - `type`: number
          - `description`: gas spinodal reduced temperature at p*=0.1105
    - `liquid_spinodal_temperatures`:
      - `type`: object
      - `required`: `p_0_04`, `p_0_10`, `p_0_1105`
      - `properties`:
        - `p_0_04`:
          - `type`: number
          - `description`: liquid spinodal reduced temperature at p*=0.04
        - `p_0_10`:
          - `type`: number
          - `description`: liquid spinodal reduced temperature at p*=0.10
        - `p_0_1105`:
          - `type`: number
          - `description`: liquid spinodal reduced temperature at p*=0.1105
    - `critical_point`:
      - `type`: object
      - `required`: `p_c`, `T_c`
      - `properties`:
        - `p_c`:
          - `type`: number
          - `description`: critical reduced pressure
        - `T_c`:
          - `type`: number
          - `description`: critical reduced temperature

Notes: All temperatures and pressures are in reduced LJ units. The agent's reported values will be compared to the hidden reference values with tolerances based on the paper's stated error bars.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spinodal_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "gas_spinodal_temperatures",
          "liquid_spinodal_temperatures",
          "critical_point"
        ],
        "properties": {
          "gas_spinodal_temperatures": {
            "type": "object",
            "required": [
              "p_0_04",
              "p_0_10",
              "p_0_1105"
            ],
            "properties": {
              "p_0_04": {
                "type": "number",
                "description": "gas spinodal reduced temperature at p*=0.04"
              },
              "p_0_10": {
                "type": "number",
                "description": "gas spinodal reduced temperature at p*=0.10"
              },
              "p_0_1105": {
                "type": "number",
                "description": "gas spinodal reduced temperature at p*=0.1105"
              }
            }
          },
          "liquid_spinodal_temperatures": {
            "type": "object",
            "required": [
              "p_0_04",
              "p_0_10",
              "p_0_1105"
            ],
            "properties": {
              "p_0_04": {
                "type": "number",
                "description": "liquid spinodal reduced temperature at p*=0.04"
              },
              "p_0_10": {
                "type": "number",
                "description": "liquid spinodal reduced temperature at p*=0.10"
              },
              "p_0_1105": {
                "type": "number",
                "description": "liquid spinodal reduced temperature at p*=0.1105"
              }
            }
          },
          "critical_point": {
            "type": "object",
            "required": [
              "p_c",
              "T_c"
            ],
            "properties": {
              "p_c": {
                "type": "number",
                "description": "critical reduced pressure"
              },
              "T_c": {
                "type": "number",
                "description": "critical reduced temperature"
              }
            }
          }
        }
      },
      "description": "Computed gas and liquid spinodal temperatures at three reduced pressures, and the critical point estimated from their intersection, for the truncated Lennard-Jones fluid (rc=2.5σ)."
    }
  ],
  "notes": "All temperatures and pressures are in reduced LJ units. The agent's reported values will be compared to the hidden reference values with tolerances based on the paper's stated error bars."
}
```

## How you are scored
Your work will be scored by a hidden verifier. The verifier reads the final JSON file `spinodal_results.json` and compares each reported temperature and pressure to a set of reference values using appropriate tolerances. You must earn a good match for full credit. Intermediate evidence files (`hysteresis_densities.txt`, `oic_rho2_data.zip`, `dic_rho2_data.zip`) are required to demonstrate that you performed the necessary process steps; they carry no separate point value but their absence or evident fabrication may affect scoring of the final result. The verifier does NOT have access to your simulation code or raw data beyond the artifacts you output.
