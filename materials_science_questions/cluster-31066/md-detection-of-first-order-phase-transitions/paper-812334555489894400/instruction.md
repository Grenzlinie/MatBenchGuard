# Equation of State and Phase Transition of Parallel Hard Squares

## Problem background
Hard-square systems are fundamental models for understanding the phase behavior of purely repulsive particles. Parallel hard squares cannot overlap and are constrained to remain mutually parallel. At high densities the system is expected to crystallize into a solid-like state, while at low densities it behaves as a fluid. The free-volume theory provides an exact expression for the pressure in the high-density limit, whereas the equation of state at low densities can be approximated by a Padé approximant to the virial expansion. By combining these theoretical descriptions, one can investigate the possibility of a solid-fluid phase transition and determine its location and properties.

## Approach
The reproduction approach consists of three parts:

1. **Analytical phase transition calculation**: Using the free-volume free energy of the solid phase and the fluid free energy obtained by numerically integrating the (3,3) Padé approximant for the pressure, compute the excess chemical potential difference as a function of the solid reduced volume. Find the transition pressure and the coexisting solid and fluid volumes where this difference vanishes.

2. **Event-driven molecular dynamics simulation**: Simulate a system of N=400 parallel hard squares under periodic boundary conditions at 16 reduced volumes. For each volume, start from a square lattice configuration, discard an initial equilibration segment, and record the instantaneous pressure over four consecutive sampling blocks.

3. **Equation-of-state analysis**: From the raw MD pressure blocks, compute the mean pressure and its standard deviation at each volume. Also compute the corresponding free-volume pressure and the (3,3) Padé approximant pressure. Collect all results into a single table.

## Reproduction target
Produce two scored artifacts under `/app/outputs`:

- **`md_pressure_table.csv`**: For each of the 16 simulated reduced volumes, provide the mean MD pressure (`pv_md`), its standard deviation (`pv_md_std`), the free-volume pressure (`pv_free_volume`), and the (3,3) Padé approximant pressure (`pv_pade`). The analytic pressure columns must be computed directly from the reduced volume using the known formulas.
- **`transition_results.json`**: A JSON object containing the computed transition pressure (`transition_pressure`) and the coexisting solid and fluid reduced volumes (`tau_solid`, `tau_fluid`).

## Assets

- Scientific Python packages (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Compute phase transition coexistence
- Role: scored
- Action: Using the free-volume free energy per particle (F_s/NkT = -2 ln(√τ - 1) + C) with the additive constant C = -2 ln 2 - 0.260422, and the fluid free energy obtained by numerically integrating the (3,3) Padé approximant for PV/NkT: (1 + a1/τ + a2/τ^2 + a3/τ^3) / (1 + b1/τ + b2/τ^2 + b3/τ^3) with a1 = -0.98164, a2 = 0.32755, a3 = -0.0276113, b1 = -2.98164, b2 = 3.2908, b3 = -1.3310, determine the excess chemical potential difference ΔG as a function of the solid reduced volume τ₁. Find the transition pressure and the coexisting solid and fluid volumes where ΔG = 0.
- Output file: `/app/outputs/transition_results.json`
- Format: json
- Contract: JSON object with keys: transition_pressure (float), tau_solid (float), tau_fluid (float).
- Scoring: scored by hidden verifier

### Step 2: Molecular dynamics simulation of hard squares
- Role: process
- Action: Implement an event-driven molecular dynamics simulation for N=400 parallel hard squares of side σ in a periodic square box. For each reduced volume τ in the set {1.05, 1.1, 1.115, 1.125, 1.15, 1.175, 1.2, 1.285, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0}, start from a square lattice configuration, discard the first 10,000 collisions for equilibration, and record the instantaneous pressure for the next 40,000 collisions in four consecutive blocks of 10,000 collisions each. Save the raw block pressures for subsequent analysis.
- Evidence: `/app/outputs/raw_pressure_blocks.json`

### Step 3: Equation of state from MD data
- Role: scored (load-bearing)
- Action: For each τ, compute the mean and standard deviation of PV/NkT from the four post-equilibration blocks. Also compute the free-volume pressure using PV/NkT = τ^(1/2)/(τ^(1/2) - 1) and the (3,3) Padé approximant using the explicit coefficients: (1 + a1/τ + a2/τ^2 + a3/τ^3) / (1 + b1/τ + b2/τ^2 + b3/τ^3) with a1 = -0.98164, a2 = 0.32755, a3 = -0.0276113, b1 = -2.98164, b2 = 3.2908, b3 = -1.3310. Output a CSV file with columns: tau, pv_md (mean), pv_md_std, pv_free_volume, pv_pade.
- Output file: `/app/outputs/md_pressure_table.csv`
- Format: csv
- Contract: CSV with columns: tau (float), pv_md (float), pv_md_std (float), pv_free_volume (float), pv_pade (float). One row per τ value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_results.json`
- `/app/outputs/md_pressure_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_results.json
- path: `/app/outputs/transition_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed solid-fluid phase transition pressure and coexisting reduced volumes
- schema:
  - `type`: object
  - `required`: `transition_pressure`, `tau_solid`, `tau_fluid`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `transition_pressure`: PV_0/(NkT)
    - `tau_solid`: reduced volume (unitless)
    - `tau_fluid`: reduced volume (unitless)

### md_pressure_table.csv
- path: `/app/outputs/md_pressure_table.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equation of state from MD and analytic theories: reduced volume τ, mean MD pressure, standard deviation, free-volume pressure, and (3,3) Padé approximant pressure
- schema:
  - `type`: table
  - `required`: `tau`, `pv_md`, `pv_md_std`, `pv_free_volume`, `pv_pade`
  - `items`: object
  - `required_columns`: `tau`, `pv_md`, `pv_md_std`, `pv_free_volume`, `pv_pade`
  - `units`:
    - `tau`: reduced volume (unitless)
    - `pv_md`: PV/(NkT)
    - `pv_md_std`: PV/(NkT)
    - `pv_free_volume`: PV/(NkT)
    - `pv_pade`: PV/(NkT)

Notes: The MD simulation output (raw_pressure_blocks.json) is an intermediate evidence file and not directly scored. The analytic columns (pv_free_volume, pv_pade) must be computed from the agent's τ values using the exact formulas. The MD pressures are compared to hidden paper-reported values with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "transition_pressure",
          "tau_solid",
          "tau_fluid"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "transition_pressure": "PV_0/(NkT)",
          "tau_solid": "reduced volume (unitless)",
          "tau_fluid": "reduced volume (unitless)"
        }
      },
      "description": "Computed solid-fluid phase transition pressure and coexisting reduced volumes"
    },
    {
      "file": "md_pressure_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": [
          "tau",
          "pv_md",
          "pv_md_std",
          "pv_free_volume",
          "pv_pade"
        ],
        "items": {},
        "required_columns": [
          "tau",
          "pv_md",
          "pv_md_std",
          "pv_free_volume",
          "pv_pade"
        ],
        "units": {
          "tau": "reduced volume (unitless)",
          "pv_md": "PV/(NkT)",
          "pv_md_std": "PV/(NkT)",
          "pv_free_volume": "PV/(NkT)",
          "pv_pade": "PV/(NkT)"
        }
      },
      "description": "Equation of state from MD and analytic theories: reduced volume τ, mean MD pressure, standard deviation, free-volume pressure, and (3,3) Padé approximant pressure"
    }
  ],
  "notes": "The MD simulation output (raw_pressure_blocks.json) is an intermediate evidence file and not directly scored. The analytic columns (pv_free_volume, pv_pade) must be computed from the agent's τ values using the exact formulas. The MD pressures are compared to hidden paper-reported values with tolerances."
}
```

## How you are scored
Your submission is scored by a hidden automated verifier that evaluates each artifact independently and combines the scores by weight.

- **`md_pressure_table.csv`** (largest weight): The verifier recomputes the free-volume and Padé pressures from the reported tau values and checks for exact agreement. The MD pressures are compared to hidden reference values using tolerances that account for run-to-run variation; structural checks (e.g., monotonic decrease with increasing tau, consistency with free-volume theory at high densities) are also applied.
- **`transition_results.json`** (smaller weight): The transition pressure and coexisting volumes are compared to hidden reference values with appropriate tolerances.

Reporting numbers that happen to match the paper's published values is not sufficient — the verifier checks that your results are self-consistent and originate from the required simulation and analytical protocols. The final reward is a weighted combination of the scores for the two artifacts, with the equation-of-state table carrying the most weight.
