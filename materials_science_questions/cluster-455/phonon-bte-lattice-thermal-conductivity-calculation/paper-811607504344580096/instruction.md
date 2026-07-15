# NDTC in graphene nanoribbons via classical MD simulations

## Problem background
Graphene nanoribbons (GNRs) exhibit unique thermal transport properties. Under large temperature differences, nonlinear effects can emerge, where the heat current does not simply scale linearly with the applied temperature bias. One such effect is negative differential thermal conductance (NDTC), in which the heat current decreases as the temperature difference increases. Understanding and controlling NDTC is important for nanoscale thermal management and thermal signal processing. This task investigates thermal transport in armchair GNRs using classical molecular dynamics (MD) simulations. By applying different temperature bias protocols and varying the ribbon length and shape, we aim to determine whether NDTC occurs, and if so, under which conditions it appears or is suppressed.

## Approach
The approach employs non-equilibrium classical molecular dynamics (NEMD) with a reactive empirical bond-order (Brenner) potential to describe carbon-carbon interactions. Rectangular armchair GNRs of various lengths (~6 nm to 50 nm) and a triangular GNR are constructed. Nosé-Hoover thermostats are attached to the left and right ends of each ribbon to impose temperature differences. For each geometry, many simulations are run with different fixed thermostat temperatures, covering cases where the right thermostat is held at 300 K or 600 K while the left varies, as well as protocols where the average temperature is parameterized by α (with T₀ = 300 K). The steady-state heat current J (in nW) and the actual average temperature T_avg are recorded for each ΔT. The resulting J(ΔT) curves are then analyzed for structural trends: a non-monotonic behavior (a decrease of J over some range of ΔT) would indicate NDTC, while a monotonic increase would indicate its absence. The dependence of these trends on ribbon length, shape, and bias protocol is the subject of the study.

## Reproduction target
Produce a single CSV file, `simulation_data.csv`, containing the computed heat current J and average temperature T_avg for all required conditions: rectangular GNR of lengths 6, 12, 24, 50 nm (with T_R fixed at 300 K, plus the 6 nm case with T_R=600 K), triangular GNR (both bias directions), and three α-tuning protocols (α = -0.5, 0, 0.5). For each condition, a range of ΔT must be covered. The data in this file will be used to evaluate the presence or absence of NDTC in each case based on structural analysis of the J versus ΔT trend.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov/download.html
- Brenner potential for carbon (AIREBO/Brenner): LAMMPS

## Workflow steps

### Step 1: Build GNR atomic structures
- Role: process
- Action: Generate atomic coordinates for rectangular armchair graphene nanoribbons of width approximately 1.5 nm and lengths 6, 12, 24, and 50 nm, and for a triangular GNR as described in the paper. Write a summary of the generated structures (dimensions, atom counts) to an evidence file.
- Evidence: `/app/outputs/gnr_structure_info.txt`

### Step 2: Run non-equilibrium molecular dynamics simulations
- Role: process
- Action: For each atomic structure, run classical MD simulations with LAMMPS using the Brenner potential and Nosé-Hoover thermostats. For each simulation case: (a) rectangular 6 nm with T_R=300 K and T_L varied from 300 K to 30 K; (b) same with T_R=600 K; (c) rectangular 12, 24, 50 nm with T_R=300 K, T_L varied; (d) triangular GNR with narrow end fixed at 300 K and wide end varied, and vice versa; (e) alpha tuning with T_0=300 K, α = -0.5, 0, 0.5. Record the time-averaged heat current J (nW) and actual average temperature T_avg for each ΔT. Document that all simulations ran by writing a summary evidence file.
- Evidence: `/app/outputs/nemd_runs_summary.txt`

### Step 3: Compile simulation data
- Role: scored (load-bearing)
- Action: Compile all recorded J and T_avg values into a single CSV file `simulation_data.csv` with columns: case, delta_T (K), J (nW), T_avg (K). The case column must identify the simulation condition using the exact labels: rect_6nm_TR300, rect_6nm_TR600, rect_12nm_TR300, rect_24nm_TR300, rect_50nm_TR300, tri_narrow_fixed, tri_wide_fixed, alpha_neg05, alpha_0, alpha_05. Ensure all required conditions are covered and the file contains the raw data from which NDTC trends can be determined.
- Output file: `/app/outputs/simulation_data.csv`
- Format: csv
- Contract: Columns: case (string), delta_T (float, K), J (float, nW), T_avg (float, K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_data.csv
- path: `/app/outputs/simulation_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw simulation data from which NDTC trends are evaluated. The checker will verify the presence or absence of NDTC in each named case by analyzing the J vs delta_T trend.
- schema:
  - `type`: table
  - `required_columns`: `case`, `delta_T`, `J`, `T_avg`
  - `units`:
    - `delta_T`: K
    - `J`: nW
    - `T_avg`: K

Notes: The file must contain rows for every case listed in the workflow steps. Row order is arbitrary. NDTC assessment is based on structural trend analysis; no exact numeric match is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "delta_T",
          "J",
          "T_avg"
        ],
        "units": {
          "delta_T": "K",
          "J": "nW",
          "T_avg": "K"
        }
      },
      "description": "Raw simulation data from which NDTC trends are evaluated. The checker will verify the presence or absence of NDTC in each named case by analyzing the J vs delta_T trend."
    }
  ],
  "notes": "The file must contain rows for every case listed in the workflow steps. Row order is arbitrary. NDTC assessment is based on structural trend analysis; no exact numeric match is required."
}
```

## How you are scored
A hidden verifier will read your `simulation_data.csv` and independently analyze the J(ΔT) trend for each labeled case. For each condition, the verifier will check whether the heat current exhibits a specific structural pattern consistent with the paper's claims, for example, a non-monotonic decrease over a certain ΔT interval or a monotonic increase. The final score is a weighted combination of these per-case checks. The verifier's scoring rules are defined in advance and are not revealed. Your task is to faithfully run the simulations and compile the data; the verifier decides how well the observed patterns align with the expected behaviour.
