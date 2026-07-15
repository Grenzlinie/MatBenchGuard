# Effective Elasticity of a Medium with Many Parallel Fractures

## Problem background
This task addresses the effective long-wave elasticity of a composite medium formed by a host rock containing a set of thin, parallel, flat fractures filled with solidified material. In many seismic applications, the fractures are often modelled as infinitely weak and infinitesimally thin planes of displacement discontinuity (the linear-slip model). The goal is to evaluate whether relaxing these two assumptions — by allowing the fracture layer to have finite thickness and finite stiffness — leads to substantially different effective elastic properties, and under what conditions the classical linear-slip approximation remains accurate.

## Approach
We consider one set of parallel fractures normal to the x1-axis. The host rock is a VTI medium with a known stiffness matrix. The fractures are represented as another VTI layer whose stiffness matrix is a scaled version of the background (scaling factor k). The relative thickness of the fracture system is h_f. The effective stiffness of the combined medium is computed by two methods:

1. **Generalized approach** — the full Backus-averaging formulas (eqs. 6–8 of the source) that keep both k and h_f arbitrary, without assuming infinite weakness or zero thickness.
2. **Linear‑slip approximation** — the simplified expressions (eqs. 9–11) that assume k → 0 and h_f → 0, reducing the fracture influence to an excess compliance matrix Z.

The difference between the two is quantified by the relative error in the stiffness change from the background (the l2‑norm of the difference between the two Δ matrices divided by the norm of the linear-slip Δ, expressed as a percentage). We study this error as a function of k at fixed small h_f, as a function of h_f at fixed small k, and for three constant Z ratios (k/h_f = 10, 1, 0.5) while both parameters grow. Finally, for a representative case (k = h_f = 0.04) we compute the phase slowness surfaces in three principal planes to illustrate how the discrepancy translates into wave-speed differences.

## Reproduction target
Implement both the generalized and the linear‑slip effective‑stiffness formulas for a stack where the background medium has stiffness matrix C_b = [[10,4,2.5,0,0,0],[4,10,2.5,0,0,0],[2.5,2.5,6,0,0,0],[0,0,0,2,0,0],[0,0,0,0,2,0],[0,0,0,0,0,3]] and fracture stiffness is C_f = k * C_b. For an appropriate range of k and h_f values, compute the effective stiffness tensors from both approaches and then the relative error as defined above. Produce a CSV file (`step_01_err_data.csv`) containing the error (%) for five scenarios: (a) vary k while keeping h_f = 1e‑5, (b) vary h_f while keeping k = 1e‑5, and (c)–(e) cumulative scenarios where the ratio k/h_f is fixed at 10, 1, and 0.5 while k and h_f increase together. For the particular case k = h_f = 0.04, compute and save the phase slowness in s/km for the three wave types (qP, qS1, qS2) in the three principal planes (x3x1, x3x2, x1x2) as a second CSV file (`step_02_slowness_surfaces.csv`). The results must be self‑contained, obtained purely from the described formulas and parameter choices without referring to any external data.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute effective stiffness tensors for all scenarios
- Role: process
- Action: Implement the generalized Schoenberg–Douma formulas (with scaling factor k) and the linear-slip formulas for one set of parallel fractures normal to the x1-axis. Use the VTI background stiffness matrix: C_b = [[10,4,2.5,0,0,0],[4,10,2.5,0,0,0],[2.5,2.5,6,0,0,0],[0,0,0,2,0,0],[0,0,0,0,2,0],[0,0,0,0,0,3]]. Represent fracture stiffness as C_f = k * C_b. For all parameter combinations described in the next steps (ranges of k and h_f, and constant k/h_f ratios), compute the generalized effective stiffness C_eff and the linear-slip effective stiffness C_l_eff. Save all tensors as an archive for documentation.
- Evidence: `/app/outputs/effective_stiffness.npz`

### Step 2: Evaluate relative error and save to CSV
- Role: scored (load-bearing)
- Action: Compute the relative error err (%) between the generalized and linear-slip effective stiffness changes relative to background: err = 100 * ||(C_b - C_l_eff) - (C_b - C_eff)||_2 / ||C_b - C_l_eff||_2. Compute this for five scenarios: (a) vary_k: h_f=1e-5, k from 1e-6 to 1; (b) vary_hf: k=1e-5, h_f from 1e-6 to 1; (c) cumul_Z10: k/h_f=10, k from 1e-6 to 1 (or h_f accordingly); (d) cumul_Z1: k/h_f=1, k from 1e-6 to 1; (e) cumul_Z05: k/h_f=0.5, k from 1e-6 to 1. Use at least 20 logarithmically spaced points per scenario. Save results to step_01_err_data.csv with one row per (scenario, parameter_value, err_percent).
- Output file: `/app/outputs/step_01_err_data.csv`
- Format: csv
- Contract: CSV with columns: `scenario` (string: vary_k, vary_hf, cumul_Z10, cumul_Z1, cumul_Z05), `parameter_value` (float, the varied k or h_f), `err_percent` (float, percentage).
- Scoring: scored by hidden verifier

### Step 3: Generate slowness surfaces and save to CSV
- Role: scored
- Action: Using the generalized effective stiffness tensor computed for k = h_f = 0.04, compute the phase slowness for quasi-P, qS1 and qS2 waves in the three principal planes: x3x1, x3x2, and x1x2. Solve the Christoffel equation for propagation direction angles from 0° to 90° in steps of 1°. Report slowness in s/km. Save results to step_02_slowness_surfaces.csv with columns: plane, wave_type, angle_degrees, slowness_s_per_km.
- Output file: `/app/outputs/step_02_slowness_surfaces.csv`
- Format: csv
- Contract: CSV with columns: `plane` (string: x3x1, x3x2, x1x2), `wave_type` (string: qP, qS1, qS2), `angle_degrees` (float, 0–90), `slowness_s_per_km` (float, s/km).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_err_data.csv`
- `/app/outputs/step_02_slowness_surfaces.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_err_data.csv
- path: `/app/outputs/step_01_err_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative error between generalized and linear-slip effective stiffness changes, for parameter variations and fixed Z-ratio scenarios.
- schema:
  - `type`: table
  - `required_columns`: `scenario`, `parameter_value`, `err_percent`
  - `units`:
    - `err_percent`: percent

### step_02_slowness_surfaces.csv
- path: `/app/outputs/step_02_slowness_surfaces.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase slowness surfaces in three principal planes for the generalized approach with k=h_f=0.04.
- schema:
  - `type`: table
  - `required_columns`: `plane`, `wave_type`, `angle_degrees`, `slowness_s_per_km`
  - `units`:
    - `angle_degrees`: degrees
    - `slowness_s_per_km`: s/km

Notes: The checker will recompute the relative error and slowness values using the same formulas and parameters defined in the task, and compare against the agent's outputs within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_err_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "scenario",
          "parameter_value",
          "err_percent"
        ],
        "units": {
          "err_percent": "percent"
        }
      },
      "description": "Relative error between generalized and linear-slip effective stiffness changes, for parameter variations and fixed Z-ratio scenarios."
    },
    {
      "file": "step_02_slowness_surfaces.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "plane",
          "wave_type",
          "angle_degrees",
          "slowness_s_per_km"
        ],
        "units": {
          "angle_degrees": "degrees",
          "slowness_s_per_km": "s/km"
        }
      },
      "description": "Phase slowness surfaces in three principal planes for the generalized approach with k=h_f=0.04."
    }
  ],
  "notes": "The checker will recompute the relative error and slowness values using the same formulas and parameters defined in the task, and compare against the agent's outputs within appropriate tolerances."
}
```

## How you are scored
A hidden verifier will independently recompute the relative‑error curve for selected test points and the slowness values at specific angles using the same formulas and parameters that are specified in this instruction. Your submitted CSV files will be read and compared to the verifier’s own recomputed values within appropriate numerical tolerances. Each scored stage contributes a non‑negligible weight to the final reward; merely reporting numbers that look plausible without correct computation will not pass. No paper‑specific reference tables are required — the verifier derives its references from the physics and parameters defined here.
