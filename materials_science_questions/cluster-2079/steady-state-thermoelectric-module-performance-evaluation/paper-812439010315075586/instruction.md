# Steady-state thermoelectric module performance evaluation

## Problem background
Conventional thermoelectric modules rely on heat conduction to establish temperature differences, which couples heat and electricity transport and limits performance. This task addresses a proposed design: a porous thermoelectric module combined with a reciprocating air flow that reduces effective thermal conductivity and continuously preheats cold junctions. The aim is to numerically predict the temperature distribution, parametric dependencies, and coefficient of performance (COP) for such a heating device. Specifically, you will compute the steady-periodic temperature profiles, explore how heating-region and outlet temperatures vary with battery voltage, flow velocity, and porosity, and determine the heating COP as a function of temperature difference. The predicted trends and structural properties of these curves are the main target.

## Approach
The device consists of two porous thermoelectric (TE) modules separated by a plain porous center medium, all placed in an insulated channel. Air flows through the channel, and the flow direction reverses at a fixed half-cycle interval. Heat exchange between the fluid and solid phases is described by a one‑dimensional transient model that couples gas and solid energy equations, including convection, conduction, Joule heating, and Peltier heating/cooling at the hot and cold junctions. The key idea is that the reciprocating flow makes the effective thermal conductivity negligible and preheats cold junctions, potentially enabling higher hot‑junction temperatures. To evaluate the design, you will build a numerical solver that integrates these equations until a periodic steady state is reached. Baseline simulations are run for specified geometry, porosity, flow velocity, and battery voltage. Then, parametric sweeps systematically vary the battery voltage, flow velocity, and porous material porosity to obtain time-averaged heating-region and outlet air temperatures. Finally, you will compute the heating COP for different temperature differences between the heating region and the ambient by adjusting the heat absorption rate. The solver must be implemented from the physical description; standard thermoelectric material properties (e.g., for Bi2Te3) are publicly available and should be used.

## Reproduction target
Produce three CSV artifacts under `/app/outputs`: (1) `temperature_distribution.csv` – the gas and solid temperature profiles along the entire device at the end of a half‑cycle for the baseline condition (porosity ε=0.5, flow velocity u=0.35 m/s, half‑cycle τ=10 s, ambient T0=300 K, module thickness x_e=2.5 cm, center thickness x_p=5 cm, battery voltage chosen to give the model's baseline power condition). (2) `parametric_sweep.csv` – for sweeps over battery voltage V_Bat, flow velocity u, and porosity ε, record the time‑averaged heating‑region temperature T_heating and time‑averaged exhaust temperature T_outlet. (3) `cop_curves.csv` – for u=0.35 m/s, ε=0.5, τ=10 s and varying heat absorption rate, compute the temperature difference ΔT₀ = T_heating_avg – T0, the corresponding current density, heat release rate, input power, and COP. The hidden verifier will assess whether these outputs are physically consistent with the paper's reported behaviour.

## Assets

- Standard thermoelectric material properties for Bi2Te3
- numpy: numpy
- scipy: scipy
- matplotlib: matplotlib

## Workflow steps

### Step 1: Implement the 1D transient reciprocating flow TE heater solver
- Role: process
- Action: Develop a numerical solver for the 1D transient heat transfer model of a porous thermoelectric heater with reciprocating flow. The solver must integrate the coupled gas and solid energy equations including convection, conduction, Joule heating, and Peltier terms, with flow direction reversal every half cycle, and reach a periodic steady state.
- Evidence: none

### Step 2: Compute baseline temperature distribution
- Role: scored (load-bearing)
- Action: Run the solver for the baseline parameters: porosity ε=0.5, flow velocity u=0.35 m/s, half cycle τ=10 s, ambient air temperature T0=300 K, module thickness x_e=2.5 cm, center porous material thickness x_p=5 cm, and battery voltage V_Bat set such that the current density yields the model's baseline power condition. Record the gas temperature T_gas and solid temperature T_solid at all spatial grid points at the end of a half cycle (just before flow reversal).
- Output file: `/app/outputs/temperature_distribution.csv`
- Format: csv
- Contract: Columns: x (cm, numeric), T_gas (K, numeric), T_solid (K, numeric).
- Scoring: scored by hidden verifier

### Step 3: Parametric sweeps of heating region and outlet temperatures
- Role: scored
- Action: Run the solver for multiple conditions: (a) different battery voltages V_Bat while keeping ε=0.5 and u=0.35 m/s; (b) different flow velocities u while keeping ε=0.5 and V_Bat fixed at one of the previous values; (c) different porosities ε while keeping u=0.35 m/s and V_Bat fixed. For each run, after reaching periodic steady state, compute the time-averaged air temperature in the center porous medium (T_heating) and the time-averaged exhaust air temperature (T_outlet). Compile all results into a single CSV.
- Output file: `/app/outputs/parametric_sweep.csv`
- Format: csv
- Contract: Columns: current_density (A/m²), V_Bat (V), u (m/s), epsilon, T_heating (K), T_outlet (K).
- Scoring: scored by hidden verifier

### Step 4: Compute heating coefficient of performance (COP) curves
- Role: scored
- Action: Run the solver for u=0.35 m/s, ε=0.5, τ=10 s, with heat sinks located at both ends of the center porous medium. For each simulation, adjust the heat absorption rate to obtain a different steady-state temperature difference ΔT0 = T_heating_avg - T0. Record the corresponding current density j, the heat release rate q_h, the input power P, and the COP ψ = q_h/P. Output a CSV for a range of ΔT0 values.
- Output file: `/app/outputs/cop_curves.csv`
- Format: csv
- Contract: Columns: delta_T0 (K), current_density (A/m²), heat_release (W/m²), input_power (W/m²), COP (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_distribution.csv`
- `/app/outputs/parametric_sweep.csv`
- `/app/outputs/cop_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_distribution.csv
- path: `/app/outputs/temperature_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature distribution along the device at the end of a half-cycle for the baseline case. The checker verifies consistency with the paper's reported behaviour.
- schema:
  - `type`: table
  - `required_columns`: `x`, `T_gas`, `T_solid`
  - `units`:
    - `x`: cm
    - `T_gas`: K
    - `T_solid`: K

### parametric_sweep.csv
- path: `/app/outputs/parametric_sweep.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Parametric sweep results. The checker verifies consistency with the paper's reported behaviour.
- schema:
  - `type`: table
  - `required_columns`: `current_density`, `V_Bat`, `u`, `epsilon`, `T_heating`, `T_outlet`
  - `units`:
    - `current_density`: A/m^2
    - `V_Bat`: V
    - `u`: m/s
    - `epsilon`: dimensionless
    - `T_heating`: K
    - `T_outlet`: K

### cop_curves.csv
- path: `/app/outputs/cop_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: COP as a function of ΔT0. The checker verifies consistency with the paper's reported behaviour.
- schema:
  - `type`: table
  - `required_columns`: `delta_T0`, `current_density`, `heat_release`, `input_power`, `COP`
  - `units`:
    - `delta_T0`: K
    - `current_density`: A/m^2
    - `heat_release`: W/m^2
    - `input_power`: W/m^2
    - `COP`: dimensionless

Notes: All outputs are scored for consistency with the paper's physical results, not by exact numeric match, because exact material properties are not fully standardized and different solver implementations may yield slightly different values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "T_gas",
          "T_solid"
        ],
        "units": {
          "x": "cm",
          "T_gas": "K",
          "T_solid": "K"
        }
      },
      "description": "Temperature distribution along the device at the end of a half-cycle for the baseline case. The checker verifies consistency with the paper's reported behaviour."
    },
    {
      "file": "parametric_sweep.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "current_density",
          "V_Bat",
          "u",
          "epsilon",
          "T_heating",
          "T_outlet"
        ],
        "units": {
          "current_density": "A/m^2",
          "V_Bat": "V",
          "u": "m/s",
          "epsilon": "dimensionless",
          "T_heating": "K",
          "T_outlet": "K"
        }
      },
      "description": "Parametric sweep results. The checker verifies consistency with the paper's reported behaviour."
    },
    {
      "file": "cop_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta_T0",
          "current_density",
          "heat_release",
          "input_power",
          "COP"
        ],
        "units": {
          "delta_T0": "K",
          "current_density": "A/m^2",
          "heat_release": "W/m^2",
          "input_power": "W/m^2",
          "COP": "dimensionless"
        }
      },
      "description": "COP as a function of ΔT0. The checker verifies consistency with the paper's reported behaviour."
    }
  ],
  "notes": "All outputs are scored for consistency with the paper's physical results, not by exact numeric match, because exact material properties are not fully standardized and different solver implementations may yield slightly different values."
}
```

## How you are scored
A hidden checker independently examines each of the three output files to verify that they are consistent with the physical behaviour reported in the paper. No exact numeric match is required, as different solver implementations may yield slightly different values, but the essential physical trends must be present. The checker uses tolerance bands to exclude trivial fabricated answers while accepting legitimate numerical spread. Each artifact's contribution is weighted, with the main result carrying the largest weight. You must genuinely run the workflow – fabricating numbers will not satisfy the checks.
