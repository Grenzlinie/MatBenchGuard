# Optimal design and transient temperature analysis of a thermoelectric radiant panel

## Problem background
Thermoelectric radiant panels offer a solid-state, refrigerant-free alternative to conventional hydronic radiant heating and cooling. A panel consists of an aluminum plate bonded to an array of thermoelectric modules (TEMs) that actively pump heat between the plate and a heat sink. The key design challenge is choosing the plate thickness and the number of TEMs per square meter such that the inner surface temperature stays within comfort ranges (cooling: 17–20 °C, heating: 27–100 °C) while delivering the required sensible loads (approximately 90 W/m² cooling, 70 W/m² heating) and minimizing material and operating cost. A valid design must also avoid surface temperatures that cause dew-point condensation. To guide this choice, a coupled thermal-electrical model is developed that predicts both steady-state performance and transient temperature uniformity. This work uses that model to perform a parametric design optimization and to validate the predicted transient temperature distribution against experimental measurements.

## Approach
A one-dimensional transient heat conduction equation for the aluminum plate is coupled with algebraic energy‑balance relations for each TEM. The TEM equations include the Peltier effect, internal Joule heating (assumed split equally between hot and cold sides), and Fourier conduction, and link the cold (or hot) side temperature of the TEM to the plate temperature at the attachment point. The system is closed by a heat‑balance equation at the opposite side of the TEM that accounts for heat exchange with the outdoor environment through a thermal resistance.

The model is solved numerically with the finite‑volume method. Material properties of 6063 aluminum alloy and parameters for the commercial TEC1‑12706 TEM are used.

The design procedure sweeps over candidate plate thicknesses (2 mm to 6 mm) and extract‑unit lengths (which determine TEM spacing and density). For each pair the critical cooling and heating capacities are computed under the constraint that the surface temperature at the centre and corner of the unit stays within the prescribed comfort limits when the heat‑rejecting radiator has a fixed thermal resistance of 1 K/W. Feasible designs are those that can also meet the target area‑specific loads. From the feasible set, the optimal design is selected by balancing the coefficient of performance (COP) and the total number of TEMs (which drives initial cost).

With the optimal design fixed, the full transient model is then run under two specific experimental conditions (cooling and heating) to obtain the temperature evolution at three characteristic points on the panel: directly over the centre of the TEM, at the midpoint of the extract unit, and at the far edge.

## Reproduction target
Your objective is to determine the optimal panel design by performing the parametric analysis described above, and then to simulate the transient temperature distribution at three spatial positions on a single panel unit under the experimental validation conditions.

- **Optimal design**: Determine the plate thickness (mm) and the number of TEMs per square meter that satisfy the indoor surface temperature ranges (cooling: 17–20 °C, heating: 27–100 °C) and the target cooling/heating loads (~90 W/m² and ~70 W/m², respectively) while minimising cost. Write the result to `/app/outputs/optimal_design.json` with keys `thickness_mm` (number) and `TEM_per_sqm` (integer).
- **Cooling transient simulation**: Using the optimal design parameters and the cooling‑mode conditions (applied current I=1 A, outdoor air temperature 35 °C, indoor air temperature 26 °C, total heat‑transfer coefficient h=11 W/(m²·K), heater‑radiator thermal resistance Rₒ=0.01 K/W), solve the coupled PDE‑TEM system from a uniform initial temperature of 35 °C until steady state. Record the temperature in Kelvin at the left end (x=0, centre of the TEM), the midpoint (x=√2 L_l/2), and the right end (x=√2 L_l) at each time step. Output a CSV file `/app/outputs/cooling_transient.csv` with columns `time_s, T_left_K, T_middle_K, T_right_K` (time from 0 to steady state, roughly 2100 s, at regular intervals).
- **Heating transient simulation**: Repeat the transient simulation for heating mode: applied current I=3 A, outdoor air temperature 10 °C, indoor air temperature 22 °C, heat‑transfer coefficient h=6 W/(m²·K), Rₒ=0.01 K/W, starting from a uniform initial temperature of 10 °C. Record the same three temperatures and output `/app/outputs/heating_transient.csv` with the same column structure.

## Assets

- Material properties and TEM parameters: Public constants: aluminum 6063 (ρ=2680 kg/m³, κ=209 W/(m·K), C=900 J/(kg·K)); TEM TEC1-12706 (α=0.051 V/K, R=1.9558 Ω, K=0.5177 W/K).

## Workflow steps

### Step 1: Optimal panel design determination
- Role: scored (load-bearing)
- Action: Perform a parametric sweep over plate thickness (2,3,4,5,6 mm) and extract unit length (0.1 to 0.227 m) with radiator thermal resistance R_o=1 K/W. For each combination compute the critical cooling and heating capacities, required TEM current, and performance per square meter using the coupled thermal-electrical model (conduction PDE + TEM algebraic equations). Select the combination that satisfies indoor surface temperature ranges (cooling: 17-20°C, heating: 27-100°C) and load constraints (cooling ~90 W/m², heating ~70 W/m²) while minimizing cost (accounting for number of TEMs). Output the optimal thickness (mm) and number of TEMs per square meter.
- Output file: `/app/outputs/optimal_design.json`
- Format: json
- Contract: {"thickness_mm": number, "TEM_per_sqm": integer}
- Scoring: scored by hidden verifier

### Step 2: Transient temperature simulation (cooling mode)
- Role: scored
- Action: Using the optimal design parameters (thickness and TEM density) and the cooling mode conditions: applied current I=1 A, outdoor temperature 35°C, indoor air temperature 26°C, heat transfer coefficient h=11 W/(m²·K), thermal resistance of water radiator R_o=0.01 K/W (conductance 100 W/K). Solve the coupled 1D transient heat conduction equation and TEM algebraic equations starting from uniform initial temperature 35°C until steady state. Record the temperature in Kelvin at three spatial points: the left end (x=0, centre of TEM), the midpoint (x=√2 L_l /2), and the right end (x=√2 L_l). Output the full transient data.
- Output file: `/app/outputs/cooling_transient.csv`
- Format: csv
- Contract: CSV with columns: time_s (float), T_left_K (float), T_middle_K (float), T_right_K (float). Time from 0 to steady state (~2100 s) at regular intervals (e.g., every 10 s).
- Scoring: scored by hidden verifier

### Step 3: Transient temperature simulation (heating mode)
- Role: scored
- Action: Using the optimal design parameters and the heating mode conditions: applied current I=3 A, outdoor temperature 10°C, indoor air temperature 22°C, heat transfer coefficient h=6 W/(m²·K), R_o=0.01 K/W. Solve the coupled system starting from uniform initial temperature 10°C until steady state. Record the same three temperatures in Kelvin and output the full transient data.
- Output file: `/app/outputs/heating_transient.csv`
- Format: csv
- Contract: CSV with columns: time_s (float), T_left_K (float), T_middle_K (float), T_right_K (float). Time from 0 to steady state at regular intervals.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimal_design.json`
- `/app/outputs/cooling_transient.csv`
- `/app/outputs/heating_transient.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimal_design.json
- path: `/app/outputs/optimal_design.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimal panel thickness (mm) and number of TEMs per square meter.
- schema:
  - `type`: object
  - `required`:
    - `thickness_mm`: number
    - `TEM_per_sqm`: integer
  - `items`: object
  - `required_columns`:
  - `units`: object

### cooling_transient.csv
- path: `/app/outputs/cooling_transient.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Transient temperatures in cooling mode at left, middle and right points.
- schema:
  - `type`: table
  - `required_columns`: `time_s`, `T_left_K`, `T_middle_K`, `T_right_K`
  - `units`:
    - `time_s`: second
    - `T_left_K`: Kelvin
    - `T_middle_K`: Kelvin
    - `T_right_K`: Kelvin

### heating_transient.csv
- path: `/app/outputs/heating_transient.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Transient temperatures in heating mode at left, middle and right points.
- schema:
  - `type`: table
  - `required_columns`: `time_s`, `T_left_K`, `T_middle_K`, `T_right_K`
  - `units`:
    - `time_s`: second
    - `T_left_K`: Kelvin
    - `T_middle_K`: Kelvin
    - `T_right_K`: Kelvin

Notes: The checker recomputes the final steady-state temperatures from the CSVs and compares them to hidden gold values (paper-reported experimental results) with appropriate tolerances, and verifies monotonic convergence to steady state.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimal_design.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "thickness_mm": "number",
          "TEM_per_sqm": "integer"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Optimal panel thickness (mm) and number of TEMs per square meter."
    },
    {
      "file": "cooling_transient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_s",
          "T_left_K",
          "T_middle_K",
          "T_right_K"
        ],
        "units": {
          "time_s": "second",
          "T_left_K": "Kelvin",
          "T_middle_K": "Kelvin",
          "T_right_K": "Kelvin"
        }
      },
      "description": "Transient temperatures in cooling mode at left, middle and right points."
    },
    {
      "file": "heating_transient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_s",
          "T_left_K",
          "T_middle_K",
          "T_right_K"
        ],
        "units": {
          "time_s": "second",
          "T_left_K": "Kelvin",
          "T_middle_K": "Kelvin",
          "T_right_K": "Kelvin"
        }
      },
      "description": "Transient temperatures in heating mode at left, middle and right points."
    }
  ],
  "notes": "The checker recomputes the final steady-state temperatures from the CSVs and compares them to hidden gold values (paper-reported experimental results) with appropriate tolerances, and verifies monotonic convergence to steady state."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three output files and combines the stage scores (weighted) into a single reward between 0 and 1.

- **`optimal_design.json`**: The checker compares the reported `thickness_mm` and `TEM_per_sqm` to the correct optimal design using an exact‑match criterion.
- **`cooling_transient.csv` and `heating_transient.csv`**: The checker extracts the final steady‑state temperature values (the last row of each CSV) and compares them to hidden reference measurements with a prescribed absolute tolerance. It also audits the transient curves for monotonic convergence to steady state; non‑monotonic or unphysical behaviour is penalised.

All scoring thresholds are derived from the original experimental data and are not disclosed. Simply copying published numbers is not sufficient; you must produce the artifacts by executing the prescribed computational workflow.
