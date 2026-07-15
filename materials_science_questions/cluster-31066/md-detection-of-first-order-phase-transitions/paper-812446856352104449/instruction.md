# Mean-Field Phase Diagram of a Two-Sublattice Liquid-Liquid Transition Model

## Problem background
Certain liquids are hypothesised to possess local crystal-like order that can be described by a tangent lattice. A phenomenological model was proposed in which two independent tensor sublattices can rotate relative to one another; a change in their mutual orientation can drive a liquid-liquid phase transition. In a simplified version, each sublattice is treated as a four-state Potts variable, and the system is analysed in the mean-field approximation. The mean-field self-consistent equations predict a phase diagram in the dimensionless parameter plane spanned by \(\alpha/(n\mu)\) and \(\beta n\mu\), featuring a first-order coexistence line and a critical point. The goal is to reproduce this mean-field phase diagram numerically.

## Approach
The model comprises two coupled sublattices, each with four discrete orientations, interacting through parameters \(I\), \(\gamma\), and a coordination number \(n\). An additional term proportional to \(\mu\) penalises changes in the relative orientation order parameter \(p\). In the mean-field approximation, the self-consistent equations for the sublattice order parameters and for \(\langle p \rangle\) are derived by minimising a thermodynamic potential. Two phases appear: a p-phase where the average orientations are the same and an o-phase where they differ. The first-order phase boundary is located by scanning the parameters \(\alpha/(n\mu)\) and \(\beta n\mu\), solving the self-consistent equations at each point, and identifying where the free energies of the two phases become equal. The critical point is found as the condition where the two solutions merge.

## Reproduction target
Produce two CSV files under `/app/outputs`:

  * `phase_boundary.csv` — a sequence of points on the first-order liquid-liquid coexistence line, ordered by increasing \(\alpha/(n\mu)\).
  * `critical_point.csv` — the coordinates \((\alpha/(n\mu), \beta n\mu)\) of the critical point terminating the first-order line.

Both files must be computed from the mean-field self-consistent equations. The phase boundary is obtained by mapping the locus of equal free energies, and the critical point is the point where the distinct high- and low-temperature solutions merge.

## Assets

- Python scientific computing environment

## Workflow steps

### Step 1: Solve mean-field equations and locate phase boundary
- Role: process
- Action: Implement the mean-field approximation for the two-sublattice Potts model with four orientations per sublattice. Derive the self-consistent equations for the order parameters and the thermodynamic potential. Perform a parameter sweep over α/(nμ) and βnμ to identify the first-order phase coexistence line where free energies of the two phases are equal, and determine the critical point where the solutions merge.
- Evidence: none

### Step 2: Output phase boundary points
- Role: scored (load-bearing)
- Action: Write the sequence of points (α/(nμ), βnμ) on the first-order coexistence line to phase_boundary.csv. Points should be ordered by increasing α/(nμ).
- Output file: `/app/outputs/phase_boundary.csv`
- Format: csv
- Contract: CSV with header: alpha_over_nmu,beta_nmu. Rows: floating‑point values sorted by ascending alpha_over_nmu.
- Scoring: scored by hidden verifier

### Step 3: Output critical point
- Role: scored
- Action: Write the coordinates (α/(nμ), βnμ) of the critical point to critical_point.csv.
- Output file: `/app/outputs/critical_point.csv`
- Format: csv
- Contract: CSV with header: alpha_over_nmu,beta_nmu. Single row of floating‑point values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundary.csv`
- `/app/outputs/critical_point.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundary.csv
- path: `/app/outputs/phase_boundary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Points on the first-order liquid-liquid phase transition line. The checker compares the reported βnmu values against a theoretical reference curve.
- schema:
  - `type`: table
  - `required_columns`: `alpha_over_nmu`, `beta_nmu`
  - `units`:
    - `alpha_over_nmu`: dimensionless
    - `beta_nmu`: dimensionless

### critical_point.csv
- path: `/app/outputs/critical_point.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The coordinates of the critical point terminating the first-order line. The checker compares these values to the expected critical point coordinates.
- schema:
  - `type`: table
  - `required_columns`: `alpha_over_nmu`, `beta_nmu`
  - `units`:
    - `alpha_over_nmu`: dimensionless
    - `beta_nmu`: dimensionless

Notes: Both outputs are evaluated by comparison to the correct theoretical values, allowing small deviations due to implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha_over_nmu",
          "beta_nmu"
        ],
        "units": {
          "alpha_over_nmu": "dimensionless",
          "beta_nmu": "dimensionless"
        }
      },
      "description": "Points on the first-order liquid-liquid phase transition line. The checker compares the reported βnmu values against a theoretical reference curve."
    },
    {
      "file": "critical_point.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha_over_nmu",
          "beta_nmu"
        ],
        "units": {
          "alpha_over_nmu": "dimensionless",
          "beta_nmu": "dimensionless"
        }
      },
      "description": "The coordinates of the critical point terminating the first-order line. The checker compares these values to the expected critical point coordinates."
    }
  ],
  "notes": "Both outputs are evaluated by comparison to the correct theoretical values, allowing small deviations due to implementation differences."
}
```

## How you are scored
A hidden verifier will evaluate each output file independently. For `phase_boundary.csv`, the checker will compare your reported \(\beta n\mu\) values against a reference curve (the analytic mean-field transition line). For `critical_point.csv`, it will compare your coordinates against the known critical-point coordinates. Credit is awarded according to how closely your results match the reference within prescribed tolerances; both artifacts must be present to receive a full score. The evaluation is fully automatic, and no partial information about the tolerances or gold values is provided.
