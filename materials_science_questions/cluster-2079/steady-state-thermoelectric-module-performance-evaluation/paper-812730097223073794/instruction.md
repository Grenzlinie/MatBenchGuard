# Steady-State Thermoelectric Generator Output Simulation

## Problem background
Thermoelectric generators (TEGs) convert heat directly into electricity via the Seebeck effect. This task focuses on a flexible thin-film μ-TEG built from 15 pairs of Bi₂Te₃ (n-type) and Sb₂Te₃ (p-type) legs on a Kapton substrate, without metal contacts at the p–n junctions. The device performance is evaluated numerically by solving the steady-state coupled heat and electrical conduction equations. The simulation predicts the open-circuit voltage and maximum output power as a function of the temperature difference applied across the device, using the material properties and geometry reported in the original study. Reproducing these numerical predictions helps understand the role of direct p–n junctions in TEG performance.

## Approach
The thermoelectric device is modelled as a planar 15-pair p–n TEG. The coupled partial differential equations for temperature and electric potential are solved under steady-state conditions using the material properties listed in the task. The device is subject to a fixed cold-side temperature of 30 °C, while the hot-side temperature is set to 30 °C + ΔT for each ΔT ∈ {11, 17, 22, 35} K. One silver pad is electrically grounded, and all outer surfaces are thermally and electrically insulated. The simulation is carried out for each ΔT separately, producing an internal current-voltage (I-V) curve. From the I-V curve, the open-circuit voltage V0 and the maximum output power Pmax are extracted. The internal resistance R_int can be obtained from the slope of the I-V curve or taken as the value reported in the reference study. Any open-source finite element or PDE solver (e.g., FEniCS, scipy) can be used to implement the model.

## Reproduction target
Compute, for each temperature difference ΔT ∈ {11, 17, 22, 35} K, the open‑circuit voltage V0 (in mV) and the maximum output power Pmax (in nW) of the 15‑pair p‑n TEG. Also report the device internal resistance R_int (in Ω). Output a CSV file with one row per ΔT and columns: Delta_T_K, V0_mV, Pmax_nW, R_int_Ohm. The file must be placed at `/app/outputs/step_01_device_performance.csv`.

## Assets

- Device geometry and material properties
- Open-source finite element / PDE solver: fenics-dolfinx, scipy, or equivalent open-source library

## Workflow steps

### Step 1: Thermoelectric device simulation
- Role: process
- Action: Implement a steady-state thermoelectric model for a 15-pair planar p-n TEG. Use the device geometry (legs 8 mm × 1 mm × 400 nm on Kapton substrate), material properties (n-type Bi2Te3: Seebeck -220 µV/K, σ=5.60e4 S/m, κ=2 W/(m·K); p-type Sb2Te3: Seebeck +167 µV/K, σ=2.72e4 S/m, κ=1.65 W/(m·K); Al contacts: σ=3.77e7 S/m, κ=238 W/(m·K)), and contact resistances described in the task. Set boundary conditions: cold side at 30 °C, hot side at 30 °C + ΔT for ΔT ∈ {11, 17, 22, 35} K; electrical ground at one silver pad; all outer surfaces thermally and electrically insulated. Solve the coupled heat and electrical conduction equations for each ΔT to obtain internal current-voltage characteristics. Extract the open-circuit voltage (V0), maximum output power (Pmax), and device internal resistance (R_int).
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Output device performance summary
- Role: scored (load-bearing)
- Action: Collect the computed open-circuit voltage (V0) in mV, maximum output power (Pmax) in nW, and internal resistance (R_int) in Ohms for each temperature difference. Write a CSV file with one row per ΔT (11, 17, 22, 35 K). The file must contain the columns: Delta_T_K, V0_mV, Pmax_nW, R_int_Ohm.
- Output file: `/app/outputs/step_01_device_performance.csv`
- Format: csv
- Contract: CSV with header: Delta_T_K, V0_mV, Pmax_nW, R_int_Ohm. There is exactly one row for each ΔT ∈ {11, 17, 22, 35}. All columns contain numeric values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_device_performance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_device_performance.csv
- path: `/app/outputs/step_01_device_performance.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The agent's simulated open-circuit voltage, maximum output power, and internal resistance for the p-n TEG at ΔT = 11, 17, 22, 35 K. Each value is compared against a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `Delta_T_K`, `V0_mV`, `Pmax_nW`, `R_int_Ohm`
  - `units`:
    - `Delta_T_K`: K
    - `V0_mV`: mV
    - `Pmax_nW`: nW
    - `R_int_Ohm`: Ohm

Notes: The hidden reference values are the paper's reported COMSOL simulation results for the same device and conditions. Only the columns V0_mV and Pmax_nW are scored; R_int_Ohm is required for completeness but carries negligible weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_device_performance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Delta_T_K",
          "V0_mV",
          "Pmax_nW",
          "R_int_Ohm"
        ],
        "units": {
          "Delta_T_K": "K",
          "V0_mV": "mV",
          "Pmax_nW": "nW",
          "R_int_Ohm": "Ohm"
        }
      },
      "description": "The agent's simulated open-circuit voltage, maximum output power, and internal resistance for the p-n TEG at ΔT = 11, 17, 22, 35 K. Each value is compared against a hidden reference."
    }
  ],
  "notes": "The hidden reference values are the paper's reported COMSOL simulation results for the same device and conditions. Only the columns V0_mV and Pmax_nW are scored; R_int_Ohm is required for completeness but carries negligible weight."
}
```

## How you are scored
A hidden verifier checks the submitted CSV file. It compares the V0_mV and Pmax_nW values against reference results obtained from the original numerical simulation. The comparison uses appropriate tolerances to account for differences in solver implementation and discretization. The R_int_Ohm column is also verified but contributes less to the final score. The reward is a number between 0 and 1, reflecting how closely your simulated performance matches the reference across all ΔT. The verifier’s exact criteria are not disclosed to ensure an honest reproduction attempt.
