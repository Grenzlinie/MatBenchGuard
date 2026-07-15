# Monte Carlo simulation of electron energy deposition in a GaN PIN device structure

## Problem background
Betavoltaic (BV) micro-batteries harness high-energy electrons from radioisotope sources to generate electron–hole pairs in semiconductor devices. GaN PIN diodes are attractive for BV applications because of their wide bandgap and radiation hardness. To optimize device designs, it is important to understand how incident electron energy is distributed among the material layers as a function of the beam accelerating voltage. Monte Carlo simulations of electron transport and energy deposition provide a direct way to compute the percentage of beam energy that is absorbed in the active semiconductor region and to estimate the resulting maximum power output.

## Approach
Use the open-source CASINO2 Monte Carlo simulation software to model electron trajectories and energy loss in a multilayer GaN PIN device. The device structure is: 80 nm p-GaN, 500 nm i-GaN (intrinsic), 3.6 µm n-GaN, all on an AlN buffer layer and a sapphire substrate. For each beam accelerating voltage—62, 80, 100, 120, 140, 160, 180, and 200 kV—run 1×10⁶ simulated electrons with a depth resolution of approximately 10 nm. The active region is defined as the depth from the top surface through the p-GaN and the full i-GaN (0–580 nm). From the depth-dependent energy deposition profiles, compute two quantities: (1) the percentage of the total energy deposited in the active region relative to the entire stack; (2) a simulated maximum power produced (MPP) trend, obtained by scaling against the known experimental MPP at 62 kV (97.8 nW). That is, for each voltage, simulated MPP = (energy_absorbed_pct / energy_absorbed_pct at 62 kV) × 97.8 nW.

## Reproduction target
Produce two CSV files under /app/outputs. (1) step_01_energy_absorption.csv: columns beam_voltage_kV (integer) and energy_absorbed_pct (float), rows for the eight beam voltages (62, 80, 100, 120, 140, 160, 180, 200 kV). energy_absorbed_pct is the percentage of the total incident beam energy that is deposited within the active region (0–580 nm depth). (2) step_02_simulated_mpp_trend.csv: columns beam_voltage_kV (integer) and simulated_mpp_nW (float), rows for the same eight voltages. simulated_mpp_nW is computed from the absorption percentages using the formula (energy_absorbed_pct / energy_absorbed_pct at 62 kV) × 97.8 nW. The values must originate from the actual Monte Carlo simulation runs.

## Assets

- CASINO2 Monte Carlo simulation software: http://www.gel.usherbrooke.ca/casino/index.html

## Workflow steps

### Step 1: Run CASINO2 electron energy deposition simulations
- Role: process
- Action: Run the CASINO2 Monte Carlo simulation program for each beam accelerating voltage (62, 80, 100, 120, 140, 160, 180, 200 kV) using the specified device layer structure (80 nm p-GaN / 500 nm i-GaN / 3.6 μm n-GaN on AlN buffer and sapphire substrate) and simulation parameters (1e6 electrons per run, depth resolution ~10 nm). Capture the raw depth-dependent energy deposition output for each energy.
- Evidence: none

### Step 2: Extract percentage energy absorbed in active region
- Role: scored
- Action: From the raw simulation outputs, compute for each beam voltage the total energy deposited in the active region (depth 0-580 nm from surface, i.e., p-GaN (80 nm) and full i-GaN (500 nm)) and the total energy deposited in the entire multi-layer structure. Calculate the percentage: (active_energy / total_energy) × 100. Write the results to step_01_energy_absorption.csv.
- Output file: `/app/outputs/step_01_energy_absorption.csv`
- Format: csv
- Contract: Columns: beam_voltage_kV (int), energy_absorbed_pct (float). Rows for voltages: 62,80,100,120,140,160,180,200.
- Scoring: scored by hidden verifier

### Step 3: Compute simulated MPP trend
- Role: scored
- Action: Using the energy absorption percentages from step_01_energy_absorption.csv, compute the simulated maximum power produced (MPP) for each beam voltage as: (energy_absorbed_pct / energy_absorbed_pct at 62 kV) × 97.8 nW. Write the results to step_02_simulated_mpp_trend.csv.
- Output file: `/app/outputs/step_02_simulated_mpp_trend.csv`
- Format: csv
- Contract: Columns: beam_voltage_kV (int), simulated_mpp_nW (float). Rows for voltages: 62,80,100,120,140,160,180,200.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energy_absorption.csv`
- `/app/outputs/step_02_simulated_mpp_trend.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energy_absorption.csv
- path: `/app/outputs/step_01_energy_absorption.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Percentage of total incident beam energy absorbed in the active region (0–580 nm depth) for each beam accelerating voltage.
- schema:
  - `type`: table
  - `required_columns`: `beam_voltage_kV`, `energy_absorbed_pct`
  - `units`:
    - `beam_voltage_kV`: kV
    - `energy_absorbed_pct`: percentage

### step_02_simulated_mpp_trend.csv
- path: `/app/outputs/step_02_simulated_mpp_trend.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Simulated maximum power produced (nW) derived from the energy absorption percentages and the experimental MPP baseline at 62 kV.
- schema:
  - `type`: table
  - `required_columns`: `beam_voltage_kV`, `simulated_mpp_nW`
  - `units`:
    - `beam_voltage_kV`: kV
    - `simulated_mpp_nW`: nW

Notes: The output values must be traceable to the CASINO2 Monte Carlo simulations. The checker will compare the submitted percentages and simulated MPP values against independently known reference values with appropriate tolerances, and will also verify that the simulated MPP trend is monotonically decreasing (except possibly a slight increase at high voltages).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energy_absorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "beam_voltage_kV",
          "energy_absorbed_pct"
        ],
        "units": {
          "beam_voltage_kV": "kV",
          "energy_absorbed_pct": "percentage"
        }
      },
      "description": "Percentage of total incident beam energy absorbed in the active region (0–580 nm depth) for each beam accelerating voltage."
    },
    {
      "file": "step_02_simulated_mpp_trend.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "beam_voltage_kV",
          "simulated_mpp_nW"
        ],
        "units": {
          "beam_voltage_kV": "kV",
          "simulated_mpp_nW": "nW"
        }
      },
      "description": "Simulated maximum power produced (nW) derived from the energy absorption percentages and the experimental MPP baseline at 62 kV."
    }
  ],
  "notes": "The output values must be traceable to the CASINO2 Monte Carlo simulations. The checker will compare the submitted percentages and simulated MPP values against independently known reference values with appropriate tolerances, and will also verify that the simulated MPP trend is monotonically decreasing (except possibly a slight increase at high voltages)."
}
```

## How you are scored
A hidden verifier evaluates each output file independently. The verifier checks that the energy_absorbed_pct values follow the expected physical trend (generally decreasing with higher beam voltage, possibly with a slight upturn at the highest voltages). It also compares your submitted absorption percentages and simulated MPP values to independently generated reference values that correspond to a correct execution of the Monte Carlo simulation. Scoring is based on how well your computed numbers agree with the reference, using appropriate tolerances. The final reward is a weighted combination of the scores from both artifacts; simply copying the paper's published numbers without running the simulation will not earn a passing score.
