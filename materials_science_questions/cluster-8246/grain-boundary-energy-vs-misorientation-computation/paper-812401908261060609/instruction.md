# MD simulation of grain boundary order parameter vs temperature and time in an aluminum bicrystal

## Problem background
Grain boundaries can undergo structural transitions at temperatures below the bulk melting point, but the atomistic details of these transformations are challenging to observe. Molecular dynamics (MD) simulations offer a way to probe the thermal stability of grain boundaries by tracking an order parameter that measures the local crystalline order parallel to the boundary plane. This task investigates the structural behavior of a Σ=5 symmetrical tilt bicrystal of aluminum at elevated temperatures using a Morse interatomic potential. The objective is to compute the order parameter ρ_j(K) for the boundary core region as a function of reduced temperature T/T_m and to follow its time evolution at selected temperatures, quantifying how thermal disorder influences the grain boundary structure.

## Approach
Construct an atomistic model of a Σ=5 (001) symmetrical tilt bicrystal containing 900 Al atoms with periodic boundaries in the plane of the boundary and fixed borders perpendicular to it. Use the Cotterill-Doyama Morse potential for aluminum. Relax the bicrystal at zero temperature to find a minimum-energy configuration (M1) via rigid-body translations and MD annealing. Separately, build a single-crystal model with the same potential and run constant-pressure MD to locate the bulk melting temperature T_m. Divide the bicrystal simulation cell into 12 equal regions along the z-axis. For a set of temperatures covering a wide range of T/T_m, run short MD simulations (3000 time steps after equilibration) and compute the time-averaged order parameter ρ_j(K) for each region using the probe vector K = (0, 2π/a, 0). For three selected reduced temperatures, perform much longer MD runs (at least 160,000 time steps) and record the instantaneous or time-binned regional order parameters as a function of simulation time. The results allow the comparison of structural order in the boundary core with that of the surrounding crystal and the propagation of disorder over time.

## Reproduction target
Produce two scored CSV artifacts under `/app/outputs`:

1. **Order parameter vs. temperature** (`rho_vs_T.csv`): Columns `T_div_Tm` (float, reduced temperature) and `rho_6` (float, order parameter for region 6, unitless). One row per temperature from the short MD runs. This file captures the temperature dependence of structural order in the grain boundary core.

2. **Time evolution of order parameter** (`rho_time_evolution.csv`): Columns `T_div_Tm` (float), `time_step` (int, arbitrary unit), `region` (int, 1–12), and `rho` (float). One row per (temperature, time snapshot, region) from the long MD runs at T/T_m = 0.43, 0.54, and 0.65. This file records the spatial and temporal propagation of disorder.

## Assets

- Cotterill-Doyama Morse potential parameters for aluminum
- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov

## Workflow steps

### Step 1: Zero-temperature bicrystal relaxation
- Role: process
- Action: Construct the Σ=5 (001) symmetrical tilt bicrystal of 900 Al atoms with periodic boundaries in x and y and fixed borders in z. Use the Cotterill-Doyama Morse potential. Perform energy minimization by sampling rigid-body translations and MD annealing to find the M1 minimum-energy structure with translation (Δx = -0.158a, Δy = 0, Δz = 0).
- Evidence: `/app/outputs/relaxed_structure.dat`

### Step 2: Single-crystal melting point determination
- Role: process
- Action: Build a single-crystal model of Al with the same Morse potential and run constant-pressure MD simulations. Compute internal energy vs temperature to locate the melting transition and determine the reference melting temperature Tm (around 940 K).
- Evidence: `/app/outputs/melting_point_log.txt`

### Step 3: Short simulation order parameter vs temperature
- Role: scored (load-bearing)
- Action: Divide the bicrystal simulation cell into 12 equal regions along z. For a set of temperatures spanning T/Tm from about 0.2 to 0.8, run short MD simulations (3000 time steps after equilibration). Compute the time-averaged order parameter ρ_j(K) for each region using probe vector K=(0, 2π/a, 0). Output only the values for region 6 (the boundary core) as a function of reduced temperature.
- Output file: `/app/outputs/rho_vs_T.csv`
- Format: csv
- Contract: Two columns: T_div_Tm (float, reduced temperature), rho_6 (float, order parameter, unitless). One row per temperature.
- Scoring: scored by hidden verifier

### Step 4: Long simulation time evolution of order parameter
- Role: scored (load-bearing)
- Action: Run long MD trajectories (at least 160,000 time steps) at T/Tm = 0.43, 0.54, 0.65. For each temperature, record the instantaneous or time-binned regional order parameters ρ_j(K) for all 12 regions as a function of simulation time.
- Output file: `/app/outputs/rho_time_evolution.csv`
- Format: csv
- Contract: Columns: T_div_Tm (float), time_step (int, arbitrary unit), region (int, 1-12), rho (float). One row per (temperature, time snapshot, region).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rho_vs_T.csv`
- `/app/outputs/rho_time_evolution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rho_vs_T.csv
- path: `/app/outputs/rho_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Order parameter vs reduced temperature for grain boundary core region from short MD runs.
- schema:
  - `type`: table
  - `required_columns`: `T_div_Tm`, `rho_6`
  - `units`:
    - `T_div_Tm`: dimensionless
    - `rho_6`: dimensionless

### rho_time_evolution.csv
- path: `/app/outputs/rho_time_evolution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time evolution of order parameter for all 12 regions at three reduced temperatures from long MD runs.
- schema:
  - `type`: table
  - `required_columns`: `T_div_Tm`, `time_step`, `region`, `rho`
  - `units`:
    - `time_step`: arbitrary
    - `rho`: dimensionless

Notes: Scoring uses hidden digitized reference for the temperature curve and structural trend checks for the time evolution. The agent must execute all MD stages to produce genuine load-bearing artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rho_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_div_Tm",
          "rho_6"
        ],
        "units": {
          "T_div_Tm": "dimensionless",
          "rho_6": "dimensionless"
        }
      },
      "description": "Order parameter vs reduced temperature for grain boundary core region from short MD runs."
    },
    {
      "file": "rho_time_evolution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_div_Tm",
          "time_step",
          "region",
          "rho"
        ],
        "units": {
          "time_step": "arbitrary",
          "rho": "dimensionless"
        }
      },
      "description": "Time evolution of order parameter for all 12 regions at three reduced temperatures from long MD runs."
    }
  ],
  "notes": "Scoring uses hidden digitized reference for the temperature curve and structural trend checks for the time evolution. The agent must execute all MD stages to produce genuine load-bearing artifacts."
}
```

## How you are scored
Your submission will be evaluated by a hidden automatic verifier that assigns a total score between 0 and 1. The verifier independently scores each of the two main artifacts and combines them with weights that reflect their importance.

- For `rho_vs_T.csv`, the verifier compares the rho_6 values against a hidden reference curve (digitized from the original study) using a tolerance that accounts for simulation-to-simulation variation. A result that closely follows the reference trend earns full credit for this part.

- For `rho_time_evolution.csv`, the verifier audits the time traces for expected qualitative behaviors—such as stability at low temperature, progressive disorder at intermediate temperature, and widespread loss of order at higher temperature—and checks that the reported values are self-consistent and physically plausible. Structural trend checks contribute to the score, and fabricated or nonsensical traces are penalized.

Simply reporting numbers that match a known result is not sufficient; the artifacts must emerge from genuine MD simulations. The verifier may also examine the supporting evidence (`relaxed_structure.dat`, `melting_point_log.txt`) to ensure the workflow was properly executed.
