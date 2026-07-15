# Coupled Electrochemical-Mechanical Li-Ion Battery Model with Pressure-Dependent Ionic Transport

## Problem background
Lithium-ion battery electrodes undergo intercalation-induced volume changes during charge and discharge, causing mechanical swelling and stress when the cell is constrained in a rigid casing or module frame. These mechanical effects alter the porous electrode structure and compress the separator, modifying ionic transport and potentially leading to heterogeneous lithiation and accelerated aging. A fully-coupled electrochemical-mechanical model that simultaneously accounts for solid-state Li diffusion, electrolyte transport, electrode swelling, porosity evolution, and pressure-dependent ionic conductivity is essential for predicting cell voltage, expansion, force, and internal concentration distributions under realistic mechanical constraints.

## Approach
The model combines a Newman-type porous electrode formulation with a macroscopic mechanical compression model. The electrochemical part includes spherical-particle solid-state diffusion, Butler-Volmer charge-transfer kinetics, and mass/charge transport in the electrolyte, using concentration- and pressure-dependent properties. The mechanical part introduces a swelling coefficient g = E / (E + E_case), where E is the local stiffness of the electrolyte-soaked porous component and E_case is the effective external constraint stiffness. This coefficient distributes the intercalation-induced volume change between macroscopic strain and pore compression. Pressure-dependent ionic transport factors f(p) and compressive stiffness curves E(p) for the anode, cathode, and separator are provided as experimentally digitized input files, along with open-circuit potentials and swelling functions versus state-of-charge. The coupled equations are solved numerically (e.g., finite differences) to simulate a 10 Ah NMC/graphite hard-case cell with a defined active area and initial mechanical preload. The simulation covers constant-current discharges at multiple C-rates under both stiff and soft jig configurations, and constant-current constant-voltage charges under several constant mechanical loads, producing full time histories of electrical and mechanical quantities that are then post-processed into the required output files.

## Reproduction target
Produce two scored CSV files by running the coupled electrochemical-mechanical simulation with the supplied digitized inputs and cell parameters. First, for constant-current discharges at C/5, C/2, 1C, and 2C, simulate the cell under both a stiff jig configuration (center stiffness 30 MPa, average 12.7 MPa) and a soft jig configuration (center 1.2 MPa, average 1.0 MPa), starting from an initial jig force of 3 kN at SOC 0%. Record cell voltage, swelling (thickness change relative to the initial state), and jig force as functions of time for all eight discharge cases. Second, for constant-current constant-voltage charges at 5.0 A to 4.2 V under constant mechanical loads of 0.4, 2.0, and 4.0 MPa, record the anode particle surface lithium concentration at both the separator interface and the current-collector interface as functions of time and state-of-charge. Output these results exactly as described in the workflow steps and output contract.

## Assets

- Separator ionic transport factor f(p)
- Anode ionic transport factor f(p)
- Cathode ionic transport factor f(p)
- Compression stiffness E(p) data
- Electrode swelling functions
- Electrode OCP functions
- Cell geometry and material parameters
- scipy: scipy
- numpy: numpy
- pandas: pandas
- matplotlib: matplotlib

## Workflow steps

### Step 1: Run the coupled electrochemical-mechanical simulation for all conditions
- Role: process
- Action: Implement the coupled 1D+1D electrochemical-mechanical model equations (solid diffusion in spherical particles, electrolyte mass and charge transport, Butler-Volmer kinetics, electrode swelling, porosity evolution, and mechanical coupling with case stiffness) using a numerical solver (e.g., finite differences). Load digitized input functions (OCP, swelling, ionic transport factor f(p), compression stiffness E(p)) and the cell geometry/material parameters from the provided resource files. Simulate the full 10 Ah cell (active area 0.3135 m²) starting from 3 kN jig force at SOC 0%. Run constant-current discharges at C/5, C/2, 1C, 2C in both stiff (center stiffness 30 MPa, average 12.7 MPa) and soft (center 1.2 MPa, average 1.0 MPa) jig configurations. Run constant-current constant-voltage charges at 5.0 A to 4.2 V under constant mechanical loads of 0.4, 2.0, and 4.0 MPa. Store the full time histories of cell voltage, current, thickness change, jig force, electrode potentials, concentrations, and anode particle surface concentrations at separator and current-collector interfaces.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Export validation discharge results (voltage, swelling, jig force)
- Role: scored (load-bearing)
- Action: From the simulation results, extract cell voltage, swelling (thickness change relative to the initial 3 kN jig force at SOC 0%), and jig force as functions of time for each of the eight discharge cases (2 jig configurations × 4 C‑rates). Format as a single CSV file.
- Output file: `/app/outputs/step_01_validation_results.csv`
- Format: csv
- Contract: columns: configuration (stiff/soft), c_rate (C_5/C_2/1C/2C), time_s (float, seconds), voltage_V (float), swelling_m (float, metres), jig_force_N (float)
- Scoring: scored by hidden verifier

### Step 3: Export lithiation results (anode surface concentrations)
- Role: scored
- Action: From the simulation of the 5 A CC‑CV charges under constant pressure, extract the anode particle surface lithium concentration at the separator interface and at the current collector interface as functions of time and state‑of‑charge (SOC). Format as a single CSV file.
- Output file: `/app/outputs/step_02_lithiation_results.csv`
- Format: csv
- Contract: columns: pressure_MPa (float, 0.4/2.0/4.0), time_s (float), soc (float, 0–1), anode_conc_sep_mol_m3 (float), anode_conc_cc_mol_m3 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_validation_results.csv`
- `/app/outputs/step_02_lithiation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_validation_results.csv
- path: `/app/outputs/step_01_validation_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Voltage, swelling, and jig force time series for all discharge configurations and C-rates. The hidden checker computes normalized RMSE against digitized experimental curves from the paper and accepts values within tolerance thresholds (voltage/swelling ≤5% RMSE, jig force ≤10% RMSE).
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `c_rate`, `time_s`, `voltage_V`, `swelling_m`, `jig_force_N`
  - `units`:
    - `time_s`: s
    - `voltage_V`: V
    - `swelling_m`: m
    - `jig_force_N`: N

### step_02_lithiation_results.csv
- path: `/app/outputs/step_02_lithiation_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Anode particle surface lithium concentration at separator and current-collector interfaces during CC-CV charges under constant pressures. The checker verifies that concentration increases monotonically with pressure and that values lie within ±15% of paper-derived reference curves.
- schema:
  - `type`: table
  - `required_columns`: `pressure_MPa`, `time_s`, `soc`, `anode_conc_sep_mol_m3`, `anode_conc_cc_mol_m3`
  - `units`:
    - `pressure_MPa`: MPa
    - `time_s`: s
    - `soc`: dimensionless
    - `anode_conc_sep_mol_m3`: mol/m^3
    - `anode_conc_cc_mol_m3`: mol/m^3

Notes: All public resources needed for the simulation (digitized f(p), E(p), swelling, OCP, and cell parameters) are bundled with this task. The scoring uses threshold_or_better on normalized RMSE and concentration trends; no gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_validation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "c_rate",
          "time_s",
          "voltage_V",
          "swelling_m",
          "jig_force_N"
        ],
        "units": {
          "time_s": "s",
          "voltage_V": "V",
          "swelling_m": "m",
          "jig_force_N": "N"
        }
      },
      "description": "Voltage, swelling, and jig force time series for all discharge configurations and C-rates. The hidden checker computes normalized RMSE against digitized experimental curves from the paper and accepts values within tolerance thresholds (voltage/swelling ≤5% RMSE, jig force ≤10% RMSE)."
    },
    {
      "file": "step_02_lithiation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_MPa",
          "time_s",
          "soc",
          "anode_conc_sep_mol_m3",
          "anode_conc_cc_mol_m3"
        ],
        "units": {
          "pressure_MPa": "MPa",
          "time_s": "s",
          "soc": "dimensionless",
          "anode_conc_sep_mol_m3": "mol/m^3",
          "anode_conc_cc_mol_m3": "mol/m^3"
        }
      },
      "description": "Anode particle surface lithium concentration at separator and current-collector interfaces during CC-CV charges under constant pressures. The checker verifies that concentration increases monotonically with pressure and that values lie within ±15% of paper-derived reference curves."
    }
  ],
  "notes": "All public resources needed for the simulation (digitized f(p), E(p), swelling, OCP, and cell parameters) are bundled with this task. The scoring uses threshold_or_better on normalized RMSE and concentration trends; no gold values are disclosed here."
}
```

## How you are scored
Each of the two required output files is scored independently by a hidden verifier that compares your submitted data against reference data derived from the original experiments. For the validation discharge file, the verifier computes normalized root-mean-square error (RMSE) between your voltage, swelling, and jig force curves and the reference curves for each configuration and C-rate; passing thresholds are hidden. For the lithiation file, the verifier checks that the anode surface concentration increases monotonically with applied pressure and falls within acceptable bounds relative to reference profiles. The total score is a weighted combination: the discharge validation results contribute 70% and the lithiation results contribute 30%. You must generate the full requested time-series data through simulation; reporting paper-derived numbers without running the model is insufficient to pass the verifier.
