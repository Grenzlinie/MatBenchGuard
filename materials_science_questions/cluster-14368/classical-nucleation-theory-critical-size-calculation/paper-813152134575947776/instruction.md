# Molecular Dynamics Reproduction of Vapor Bubble Nucleation by Rubbing Surfaces

## Problem background
When two solid surfaces rub together immersed in a liquid, vapor bubbles can sometimes nucleate, a phenomenon relevant to lubrication, bearing systems, and cavitation damage. A proposed microscopic mechanism is that fluid molecules squeezed between the solids are suddenly released with high kinetic energy into the bulk liquid, potentially triggering bubble nucleation. Molecular dynamics (MD) simulations of a Lennard-Jones fluid can be used to investigate this mechanism. The goal is to quantify the relationship between the kinetic energy of a burst of released molecules and the number of molecules released, and to determine the conditions under which a proto-bubble grows to a macroscopic size.

## Approach
The approach uses classical MD to simulate a Lennard-Jones liquid confined between two solid plates with a small movable block representing an asperity. The system is first equilibrated at a temperature and pressure corresponding to the liquid’s saturation conditions, then depressurized to create a superheated metastable state while the block descends, trapping some fluid molecules underneath. Rubbing is simulated by applying a normal pressure to the block and moving it tangentially. From the trajectories we identify “burst” events where a cluster of trapped molecules is suddenly released; for each burst we compute the total kinetic energy and the number of molecules involved. Separately, a simulation of a flat liquid-vapor interface at the same temperature yields the surface tension, from which we compute the critical bubble radius for the superheat using the two-dimensional Young-Laplace relation (R_c = surface_tension / (saturation pressure – ambient pressure)). Finally, for each rubbing run we track the proto-bubble radius and decide whether nucleation occurred by comparing the maximum radius to the critical radius. A linear model passing through the origin is fitted to the burst data to obtain the per-molecule kinetic energy constant.

## Reproduction target
Run rubbing MD simulations for at least two distinct squeezing pressures at a fixed rubbing velocity of 1 m/s, with multiple independent realizations per condition. From the combined trajectories, extract all burst events (release of many squeezed molecules within ~10 ps) and compile a CSV file with the total kinetic energy and molecule count for each burst. Fit those data points to a straight line through the origin to obtain the proportionality constant (per-molecule kinetic energy). Compute the surface tension from a separate flat-interface simulation and use it to calculate the critical bubble radius for the imposed superheat. For each rubbing condition, record whether nucleation occurred. The required output files are: `burst_energy_vs_molecules.csv`, `fitted_slope.json`, `critical_radius.json`, and `nucleation_outcomes.csv`.

## Assets

- LAMMPS: https://lammps.sandia.gov

## Workflow steps

### Step 1: System preparation: equilibration and block descent
- Role: process
- Action: Set up the simulation box for the Lennard-Jones fluid between solid plates with a movable block. Equilibrate the fluid at T=372 K and p_sat=5.33 MPa for ~1400 ps, then descend the block while reducing system pressure to p_inf=2.47 MPa to obtain a superheated metastable liquid with molecules squeezed under the block. Save the configuration for subsequent rubbing simulations.
- Evidence: `/app/outputs/system_restart.data`

### Step 2: Flat liquid-vapor interface MD simulation for surface tension
- Role: process
- Action: Set up a separate simulation with a flat liquid-vapor interface of the same Lennard-Jones fluid at T=372 K. Equilibrate and compute the surface tension from the difference of normal and tangential pressure components. Output the computed surface tension value.
- Evidence: `/app/outputs/surface_tension.log`

### Step 3: Compute critical bubble radius
- Role: scored (load-bearing)
- Action: From the surface tension value obtained in the previous step and the superheat pressure difference (p_sat - p_inf), compute the two-dimensional critical bubble radius using the formula: R_c = surface_tension / (p_sat - p_inf). Output the critical radius in nm.
- Output file: `/app/outputs/critical_radius.json`
- Format: json
- Contract: JSON object with key: R_c_nm (float, critical radius in nm).
- Scoring: scored by hidden verifier

### Step 4: Run rubbing MD simulations
- Role: process
- Action: Starting from the configuration produced in step 1, run LAMMPS simulations where the block is pressed with a downward pressure p and moved tangentially with velocity V=1 m/s. Conduct multiple independent runs for at least two pressure conditions (e.g., p=6.3 GPa and p=1.6 GPa), with at least 2 runs per condition. For each run, record the proto-bubble radius time series and the number of squeezed molecules under the block, continuing until all squeezed molecules are released.
- Evidence: `/app/outputs/rubbing_runs_complete.txt`

### Step 5: Post-process trajectories: burst identification and properties
- Role: scored (load-bearing)
- Action: For each rubbing run, analyze the trajectory to identify burst release events where more than several tens of molecules are released within ~10 ps and the instantaneous kinetic energy peaks. For each identified burst, compute the total kinetic energy E_burst (sum over burst duration) and the number of released molecules ΔN_burst. Collect all (E_burst, ΔN_burst) pairs from all runs.
- Output file: `/app/outputs/burst_energy_vs_molecules.csv`
- Format: csv
- Contract: CSV with columns: burst_total_energy_kJ_per_mol (float), burst_molecules_count (int). One row per burst event observed across all runs.
- Scoring: scored by hidden verifier

### Step 6: Fit linear model E_burst vs ΔN_burst
- Role: scored (load-bearing)
- Action: Read the burst_energy_vs_molecules.csv data. Fit a linear model E_burst = E_mol0 * ΔN_burst passing through the origin using least squares. Output the fitted slope E_mol0 in kJ/mol.
- Output file: `/app/outputs/fitted_slope.json`
- Format: json
- Contract: JSON object with key: E_mol0_kJ_per_mol (float).
- Scoring: scored by hidden verifier

### Step 7: Determine nucleation outcomes
- Role: scored (load-bearing)
- Action: For each rubbing run, track the proto-bubble equivalent radius R (computed from vapor region area using a subcell density classification). Use the critical radius R_c from step 3. Classify a run as nucleating if R exceeds R_c at any time and the bubble subsequently grows. Record the nucleation outcome for each run along with the pressure and velocity conditions, and summarize per condition (pressure, velocity, whether nucleation occurred in majority of runs, and total number of runs).
- Output file: `/app/outputs/nucleation_outcomes.csv`
- Format: csv
- Contract: CSV with columns: pressure_GPa (float), velocity_m_per_s (float), nucleation_occurred (boolean), number_of_runs (int). One row per condition tested (at least two pressure conditions).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_radius.json`
- `/app/outputs/burst_energy_vs_molecules.csv`
- `/app/outputs/fitted_slope.json`
- `/app/outputs/nucleation_outcomes.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_radius.json
- path: `/app/outputs/critical_radius.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed 2D critical bubble radius from surface tension and pressure difference.
- schema:
  - `type`: object
  - `required`:
    - `R_c_nm`: number

### burst_energy_vs_molecules.csv
- path: `/app/outputs/burst_energy_vs_molecules.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total burst kinetic energy and number of molecules released per burst event across all rubbing runs.
- schema:
  - `type`: table
  - `required_columns`: `burst_total_energy_kJ_per_mol`, `burst_molecules_count`

### fitted_slope.json
- path: `/app/outputs/fitted_slope.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted per-molecule kinetic energy constant from burst data.
- schema:
  - `type`: object
  - `required`:
    - `E_mol0_kJ_per_mol`: number

### nucleation_outcomes.csv
- path: `/app/outputs/nucleation_outcomes.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nucleation outcome per pressure/velocity condition.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `velocity_m_per_s`, `nucleation_occurred`, `number_of_runs`

Notes: All scored outputs are compared against hidden reference values derived from the paper, using appropriate tolerances. The burst energy CSV is used by the checker to recompute the fitted slope, while the other outputs are directly compared to the paper's reported numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_radius.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "R_c_nm": "number"
        }
      },
      "description": "Computed 2D critical bubble radius from surface tension and pressure difference."
    },
    {
      "file": "burst_energy_vs_molecules.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "burst_total_energy_kJ_per_mol",
          "burst_molecules_count"
        ]
      },
      "description": "Total burst kinetic energy and number of molecules released per burst event across all rubbing runs."
    },
    {
      "file": "fitted_slope.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "E_mol0_kJ_per_mol": "number"
        }
      },
      "description": "Fitted per-molecule kinetic energy constant from burst data."
    },
    {
      "file": "nucleation_outcomes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "velocity_m_per_s",
          "nucleation_occurred",
          "number_of_runs"
        ]
      },
      "description": "Nucleation outcome per pressure/velocity condition."
    }
  ],
  "notes": "All scored outputs are compared against hidden reference values derived from the paper, using appropriate tolerances. The burst energy CSV is used by the checker to recompute the fitted slope, while the other outputs are directly compared to the paper's reported numbers."
}
```

## How you are scored
A hidden verifier will independently evaluate each output artifact against reference values derived from the original study, using appropriate tolerances. The verifier compares your reported fitted slope and critical radius to the expected values, re-fits a line through the origin on your submitted burst data and compares the resulting slope, and checks your nucleation classifications against the expected outcomes. The total reward is a weighted combination of scores from these checks; simply printing the paper’s published numbers is insufficient because the verifier recomputes metrics from your raw data where possible.
