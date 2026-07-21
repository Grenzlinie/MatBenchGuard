# Monte Carlo Simulation of Hysteresis in Dilute RFIM Order Parameter

## Problem background
The random-field Ising model (RFIM) describes dilute antiferromagnets such as FeₓZn₁₋ₓF₂ in an applied magnetic field. Experimental studies observe critical scaling consistent with a second-order phase transition, yet they also show striking hysteresis in the order parameter under field-cooled (FC) and zero-field-cooled (ZFC) protocols, as well as upon temperature reversals near the critical temperature. Monte Carlo (MC) simulations of the dilute Ising model are used to reproduce and characterize these non-equilibrium irreversibilities, testing whether the hysteresis is an intrinsic feature of the RFIM and how it depends on the cooling/heating history.

## Approach
The approach uses a Monte Carlo simulation of a dilute Ising model on a three-dimensional simple cubic lattice of size 2L×L×L with L=128 and periodic boundary conditions. Magnetic sites are randomly occupied with probability 0.85 (vacancies otherwise). The Hamiltonian consists of nearest-neighbor exchange interactions J₂ = 3.17 K between occupied sites and a uniform field h = 8.73 K acting on occupied sites. Dynamics are simulated via the Metropolis single-spin-flip algorithm. Temperature is varied in steps of ΔT = 0.01 K. At each temperature, magnetic sites are visited an average of N times, where N = 200 or N = 1000 depending on the protocol. The simulation tracks the magnitude of the staggered magnetization (order parameter) per spin. Several thermal protocols are executed: (a) zero-field-cooled (ZFC) and field-cooled (FC) runs with N=200, plus temperature reversals after ZFC at levels 0.8, 0.6, 0.4, and 0.2 K below the critical temperature; (b) ZFC and FC runs with N=1000, and a reversal at 0.6 K below the critical temperature followed by heating. The resulting data are used to examine hysteresis between the FC and ZFC curves and the behavior of the order parameter during the reversal branches.

## Reproduction target
Produce a single CSV file (`order_parameter_curves.csv`) containing the temperature-dependent staggered magnetization for all simulation protocols listed below. The file must have columns: `protocol` (string), `temperature` (float, in K), and `stag_mag` (float, dimensionless magnitude of staggered magnetization). The required protocol labels are: `'ZFC_N200'`, `'FC_N200'`, `'rev_N200_0.8'`, `'rev_N200_0.6'`, `'rev_N200_0.4'`, `'rev_N200_0.2'`, `'ZFC_N1000'`, `'FC_N1000'`, `'rev_N1000_0.6_cooling'`, `'rev_N1000_0.6_heating_lower'`, `'rev_N1000_0.6_heating_upper'`. The temperature range should cover the full cooling/heating sweep (approximately 30 K to 70 K) with a step of 0.01 K. There must be no missing values. The curves should exhibit distinct ZFC and FC branches (hysteresis) and the heating branches after reversal must reach distinct endpoint temperatures that reflect the dynamical history.

## Assets

- numpy: numpy
- matplotlib: matplotlib

## Workflow steps

### Step 1: Lattice and spin configuration initialization
- Role: process
- Action: Generate a 3D lattice of size 2L×L×L with L=128 and periodic boundary conditions. Assign site occupations ε_i = 1 with probability 0.85 (magnetic) and 0 (vacancy) otherwise, and assign random initial Ising spins S_i = ±2. Prepare the Hamiltonian parameters: exchange J2 = 3.17 K, uniform field h = 8.73 K.
- Evidence: none

### Step 2: Monte Carlo simulation and data collection
- Role: scored (load-bearing)
- Action: Implement Metropolis single-spin-flip Monte Carlo dynamics with temperature steps ΔT = 0.01 K. For each temperature, randomly visit magnetic sites an average of N times and attempt spin flips. Run the following protocols and continuously record the magnitude of the staggered magnetization (order parameter) per spin: (a) zero-field-cooled (ZFC) and field-cooled (FC) with N=200, plus temperature reversals after ZFC at 0.8, 0.6, 0.4, 0.2 K below the critical temperature; (b) ZFC and FC with N=1000, plus a reversal at 0.6 K below Tc followed by heating. Write all data to a single CSV file.
- Output file: `/app/outputs/order_parameter_curves.csv`
- Format: csv
- Contract: CSV with columns: protocol (string), temperature (float, in K), stag_mag (float, the magnitude of the staggered magnetization). Protocol labels must be: 'ZFC_N200', 'FC_N200', 'rev_N200_0.8', 'rev_N200_0.6', 'rev_N200_0.4', 'rev_N200_0.2', 'ZFC_N1000', 'FC_N1000', 'rev_N1000_0.6_cooling', 'rev_N1000_0.6_heating_lower', 'rev_N1000_0.6_heating_upper'. Temperature values should span the full cooling/heating range (e.g., ~30 K to ~70 K) with a step of 0.01 K. No missing values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/order_parameter_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### order_parameter_curves.csv
- path: `/app/outputs/order_parameter_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file containing staggered magnetization vs temperature for all simulated protocols. The checker will recompute the maximum temperature reached by the heating branches for the N=1000 reversal and validate that ZFC/FC curves are distinct; it will compare these recomputed endpoint temperatures to hidden gold values. The temperature range should cover from ~30 K to ~70 K with a step of 0.01 K.
- schema:
  - `type`: table
  - `required_columns`: `protocol`, `temperature`, `stag_mag`
  - `units`:
    - `temperature`: K
    - `stag_mag`: dimensionless magnitude of staggered magnetization per spin

Notes: The checker extracts structural properties (hysteresis distinctness) and endpoint temperatures from the raw CSV; no self-reported metrics are used. The solving agent must ensure the CSV covers all listed protocol labels and temperature steps continuously.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "order_parameter_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "protocol",
          "temperature",
          "stag_mag"
        ],
        "units": {
          "temperature": "K",
          "stag_mag": "dimensionless magnitude of staggered magnetization per spin"
        }
      },
      "description": "CSV file containing staggered magnetization vs temperature for all simulated protocols. The checker will recompute the maximum temperature reached by the heating branches for the N=1000 reversal and validate that ZFC/FC curves are distinct; it will compare these recomputed endpoint temperatures to hidden gold values. The temperature range should cover from ~30 K to ~70 K with a step of 0.01 K."
    }
  ],
  "notes": "The checker extracts structural properties (hysteresis distinctness) and endpoint temperatures from the raw CSV; no self-reported metrics are used. The solving agent must ensure the CSV covers all listed protocol labels and temperature steps continuously."
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier. The verifier loads the CSV, validates the required columns and protocol labels, and computes a series of structural and quantitative checks directly from your data. It verifies that the ZFC and FC curves are distinct (hysteresis) and that the heating branches after reversal reach endpoint temperatures consistent with a faithful reproduction of the simulation. Computed quantities are compared to hidden reference criteria with predefined tolerances. The final reward is a weighted combination of these checks; no self‑reported metric or single number in the CSV is used as the sole basis for scoring. The raw data must faithfully represent the full temperature sweep and demonstrably originate from a correct implementation of the Monte Carlo procedure.
