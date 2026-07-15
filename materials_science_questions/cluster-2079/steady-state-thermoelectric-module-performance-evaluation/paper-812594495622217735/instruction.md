# Thermal simulation of a Peltier current lead with cryogenic mixed-refrigerant cycle

## Problem background
Current leads that feed electrical power from room-temperature terminals into a cryogenic superconducting device constitute one of the dominant heat loads on the cryogenic system. The heat originates from ohmic (Joule) heating and thermal conduction; design efforts aim to minimize the cold-end heat load. A promising concept augments a DC current lead with Peltier thermoelectric elements at the warm end and uses a cryogenic mixed-refrigerant Joule‑Thomson cycle (CMRC) to cool the middle section. Your task is to model the thermal behaviour of a 10 kA current lead built with such a combination and to quantify the cold‑end heat load at nominal current and in the zero‑current (heat‑leak) case.

## Approach
The lead is divided into three serially connected segments: (1) a short Peltier segment made of Bi₂Te₃ at the warm end, (2) an upper copper segment (CuI) that is cooled by the low‑pressure stream of a mixed‑refrigerant counter‑flow heat exchanger, and (3) a lower copper segment (CuII) that is anchored to a 78 K cryocooler. Heat conduction and Joule heating in each segment are described by one‑dimensional steady‑state heat equations. The Peltier segment is driven by the same transport current and contributes additional thermoelectric cooling. The heat exchanger model uses a multi‑tube‑in‑tube geometry with the high‑pressure mixed‑refrigerant stream being throttled to produce additional cooling. The mixed refrigerant is a four‑component hydrocarbon/nitrogen mixture (mass fractions 35.9 % N₂, 31.9 % CH₄, 18.2 % C₂H₆, 14 % C₃H₈); its thermophysical properties are obtained from the Peng–Robinson equation of state via an open‑source library. The material properties of Bi₂Te₃ (thermal conductivity, temperature‑dependent electrical resistivity and Seebeck coefficient) and oxygen‑free copper (RRR = 50) must be supplied from public reference data. Boundary conditions are a fixed warm‑end temperature of 300 K and a fixed cold‑end temperature of 78 K, with energy conservation at the interfaces. The coupled system of ordinary differential equations is solved numerically to yield the temperature profile along the full length of the lead and the associated heat flows. The simulation is then repeated with zero transport current to obtain the passive heat leak.

## Reproduction target
For the design current of 10 kA, produce the temperature profile from the warm end to the cold end as a CSV file and a JSON summary of the heat loads (warm‑end heat load, Peltier cooling power, heat flow at the Peltier‑copper interface, Joule heating in CuI, heat intercepted by the LP stream, Joule heating in CuII, and cold‑end heat load). For the zero‑current case, produce only the cold‑end heat load as a JSON file. The exact output formats, column names, and keys are specified in the workflow steps below.

## Assets

- CoolProp thermophysical properties library: https://github.com/CoolProp/CoolProp
- Public copper thermal and electrical conductivity data (RRR=50)
- Standard heat transfer and pressure drop correlations
- Python scientific stack (numpy, scipy, matplotlib): numpy, scipy, matplotlib

## Workflow steps

### Step 1: Generate fluid thermophysical properties
- Role: process
- Action: Implement a fluid property function using the Peng-Robinson equation of state (via CoolProp) for the mixed refrigerant N2/CH4/C2H6/C3H8 (mass fractions 35.9% / 31.9% / 18.2% / 14%) over the temperature range 78–300 K and pressure range 3–19 bar. Provide callable functions that return enthalpy, density, viscosity, and thermal conductivity as functions of temperature and pressure.
- Evidence: `/app/outputs/fluid_property_spot_checks.json`

### Step 2: Simulate temperature profile of 10 kA current lead
- Role: scored (load-bearing)
- Action: Solve the coupled one-dimensional heat conduction equations for the Peltier (PE), upper copper (CuI), and lower copper (CuII) segments, coupled with the counter-flow heat exchanger (CFHX) model, using the given geometry (L_PE=7 mm, d_PE=45 mm, L_CuI=0.58 m, A_CuI=2.0e-3 m², L_CuII=0.4 m, A_CuII=3.0e-3 m², L_CFHX=5.5 m, n=10 parallel elements), material properties (Bi₂Te₃ properties as specified, copper RRR=50), boundary conditions (T_warm=300 K, T_cold=78 K), and operating parameters (I=10 kA, LP mass flow=3 g/s). Obtain the temperature profile along the entire current lead from warm end to cold end.
- Output file: `/app/outputs/temperature_profile.csv`
- Format: csv
- Contract: Columns: length_m (float, position along lead from warm end), temperature_K (float, computed temperature).
- Scoring: scored by hidden verifier

### Step 3: Heat load summary for 10 kA case
- Role: scored
- Action: From the same simulation, compute the following heat loads in watts: warm-end heat load, Peltier cooling power, heat flow at PE-CuI interface, Joule heating in CuI, heat intercepted by the LP stream, Joule heating in CuII, and cold-end heat load. Save as JSON.
- Output file: `/app/outputs/heat_load_summary.json`
- Format: json
- Contract: JSON object with keys: current_kA (10), warm_end_heat_load_W (float), peltier_cooling_power_W (float), pe_cui_interface_heat_W (float), joule_cui_W (float), intercepted_by_lp_W (float), joule_cuii_W (float), cold_end_heat_load_W (float).
- Scoring: scored by hidden verifier

### Step 4: Simulate zero-current cold-end heat load
- Role: scored
- Action: Repeat the coupled simulation with the same geometry, mixture, and boundary conditions but with I=0 A. Compute the resulting cold-end heat load.
- Output file: `/app/outputs/zero_current_cold_end_heat_load.json`
- Format: json
- Contract: JSON object with key: cold_end_heat_load_W (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_profile.csv`
- `/app/outputs/heat_load_summary.json`
- `/app/outputs/zero_current_cold_end_heat_load.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_profile.csv
- path: `/app/outputs/temperature_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature profile along the current lead from warm end to cold end. Shape and values are audited for consistency (monotonic decrease, approximate endpoint temperatures).
- schema:
  - `type`: table
  - `required_columns`: `length_m`, `temperature_K`
  - `units`:
    - `length_m`: m
    - `temperature_K`: K

### heat_load_summary.json
- path: `/app/outputs/heat_load_summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Heat loads extracted from the 10 kA simulation. The primary scored quantity is cold_end_heat_load_W; lower is better, with threshold_or_better scoring.
- schema:
  - `type`: object
  - `required`:
    - `current_kA`: 10
    - `warm_end_heat_load_W`: float
    - `peltier_cooling_power_W`: float
    - `pe_cui_interface_heat_W`: float
    - `joule_cui_W`: float
    - `intercepted_by_lp_W`: float
    - `joule_cuii_W`: float
    - `cold_end_heat_load_W`: float

### zero_current_cold_end_heat_load.json
- path: `/app/outputs/zero_current_cold_end_heat_load.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Cold-end heat load when no transport current flows (I=0 A). Lower is better, scored with threshold_or_better.
- schema:
  - `type`: object
  - `required`:
    - `cold_end_heat_load_W`: float

Notes: The agent must implement the full coupled simulation from the described equations; the checker will compare the reported cold-end heat loads to the paper's values. The temperature profile is audited for structural plausibility.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "length_m",
          "temperature_K"
        ],
        "units": {
          "length_m": "m",
          "temperature_K": "K"
        }
      },
      "description": "Temperature profile along the current lead from warm end to cold end. Shape and values are audited for consistency (monotonic decrease, approximate endpoint temperatures)."
    },
    {
      "file": "heat_load_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "current_kA": 10,
          "warm_end_heat_load_W": "float",
          "peltier_cooling_power_W": "float",
          "pe_cui_interface_heat_W": "float",
          "joule_cui_W": "float",
          "intercepted_by_lp_W": "float",
          "joule_cuii_W": "float",
          "cold_end_heat_load_W": "float"
        }
      },
      "description": "Heat loads extracted from the 10 kA simulation. The primary scored quantity is cold_end_heat_load_W; lower is better, with threshold_or_better scoring."
    },
    {
      "file": "zero_current_cold_end_heat_load.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "cold_end_heat_load_W": "float"
        }
      },
      "description": "Cold-end heat load when no transport current flows (I=0 A). Lower is better, scored with threshold_or_better."
    }
  ],
  "notes": "The agent must implement the full coupled simulation from the described equations; the checker will compare the reported cold-end heat loads to the paper's values. The temperature profile is audited for structural plausibility."
}
```

## How you are scored
An automated verifier will examine each of the three output files. The temperature profile will be checked for structural consistency (monotonic decrease, approximate warm‑end and cold‑end temperatures). The heat‑load summaries will be compared against design targets that are derived from the publicly known system parameters; the cold‑end heat load at 10 kA and at zero current are the primary scored quantities. Your total reward is a weighted combination of these checks. The verifier expects results that are physically consistent with the described model and the specified geometry and operating conditions. Submitting values that cannot arise from a correct execution of the full coupled simulation will be penalized.
