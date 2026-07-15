# Power-law model for mean strain at UTS in polycrystalline struts

## Problem background
Coronary stent struts have dimensions (thickness and length) that are comparable to the metallic grain size of their constituent alloys. When a strut contains only a few grains across its cross‑section or along its length, its mechanical behaviour can deviate significantly from that of bulk material – a phenomenon known as statistical size effects (SSEs). This task investigates SSEs in thin polycrystalline struts made of 316L stainless steel under tensile and bending loading. The goal is to quantify how the mean strain at ultimate tensile strength (ε̄<sub>u</sub>) depends on the strut length‑to‑grain‑size ratio (l/d) and thickness‑to‑grain‑size ratio (t/d), and to examine whether surface strain at maximum moment in bending decreases with increasing l/d at fixed t/d.

## Approach
A two‑dimensional generalised plane‑strain finite element approach is used, with each grain explicitly modelled and assigned a random three‑dimensional face‑centred‑cubic (FCC) lattice orientation. The deformation of 316L is described by a rate‑dependent crystal plasticity constitutive law that includes {111}<110> slip systems, power‑law flow, and Taylor isotropic hardening with the hyperbolic‑tangent hardness evolution of Peirce et al. Material parameters for 316L are calibrated to match a reference bulk stress–strain curve (yield ~400 MPa, UTS ~713 MPa, ε<sub>u</sub> ~ 0.33). The model is implemented using an open‑source crystal plasticity solver (e.g., DAMASK).

A regular hexagonal grain geometry with a fixed grain diameter of 5.95 µm is used for all microstructures. For the tension study, simulations are performed for a grid of l/d and t/d ratios, with five independent random orientations per condition. For each simulation the engineering stress–strain curve is extracted and the strain at maximum load (ε<sub>u</sub>) is recorded; the mean across orientations gives ε̄<sub>u</sub> for that geometry. A single‑crystal baseline ε̄<sub>u,0</sub> is obtained from the limiting case l/d = 1, t/d = 1.

For the bending study, struts are subjected to pure bending, and the surface strain at the curvature corresponding to maximum moment is computed. All results are aggregated into CSV files.

## Reproduction target
Provide two CSV files under `/app/outputs`.

- **`step_01_aggregate_data.csv`** must contain, for each simulated (l/d, t/d) condition in the tension study, the columns `l_d`, `t_d`, `epsilon_u_bar` (the mean ε̄<sub>u</sub> across the five orientations), and `epsilon_u_0` (the single‑crystal baseline mean from l/d = 1, t/d = 1). The file must include at least 10 rows covering at least 3 distinct `l_d` values and at least 3 distinct `t_d` values.
- **`step_02_bending_trend.csv`** must contain, for struts subjected to pure bending, the columns `l_d`, `t_d`, `epsilon_s` (the surface strain at maximum moment). The data must include at least two rows with the same `t_d` but increasing `l_d`, and the `epsilon_s` values should exhibit a decreasing trend with increasing `l_d`.

## Assets

- DAMASK (crystal plasticity solver): https://github.com/eisenforschung/DAMASK
- damask (Python package): damask

## Workflow steps

### Step 1: Implement 316L crystal plasticity model
- Role: process
- Action: Implement an FCC crystal plasticity constitutive model for 316L with {111}<110> slip systems, a power-law rate-dependent flow rule, and Taylor isotropic hardening with hardness evolution g(γ)=g₀+(g∞-g₀)tanh|h₀γ/(g∞-g₀)|. Use the material parameters: elastic constants E=190 GPa, ν=0.28; reference strain rate 0.0106 s⁻¹, rate sensitivity exponent 50; initial slip resistance g₀=140 MPa, saturation slip resistance g∞=380 MPa, initial hardening modulus h₀=260 MPa. The bulk stress-strain curve should match a yield stress of ~400 MPa, UTS ~713 MPa, and ε_u ~0.33.
- Evidence: `/app/outputs/crystal_plasticity_model.py`

### Step 2: Generate 2D meshed strut microstructures
- Role: process
- Action: Create regular hexagonal grain geometries with grain diameter d=5.95 µm for single-crystal (l/d=1, t/d=1) and polycrystal strut configurations over a grid of l/d and t/d ratios: l/d ∈ {5, 10, 20, 40, 80}, t/d ∈ {1.5, 3, 5, 10} for tension, and a few bending configurations (e.g., l/d=40, t/d=1.5 and 5). Use 2D generalised plane-strain elements with approximately 96 elements per grain. Output mesh files compatible with the chosen crystal plasticity solver.
- Evidence: `/app/outputs/mesh_generation_log.txt`

### Step 3: Compute single-crystal baseline strain at UTS
- Role: process
- Action: Run uniaxial tensile simulations on the single-crystal configuration (l/d=1, t/d=1) with 5 different random FCC lattice orientations, using the implemented 316L model. Extract engineering stress-strain curves, find the strain at maximum load (ε_u) for each orientation, and compute the mean ε̄_u,0. Record this baseline value for use in the downstream aggregate output.
- Evidence: `/app/outputs/single_crystal_results.txt`

### Step 4: Tensile SSE simulations and aggregated data
- Role: scored (load-bearing)
- Action: For each (l/d, t/d) combination in the grid (l/d ∈ {5,10,20,40,80}, t/d ∈ {1.5,3,5,10}), run uniaxial tensile simulations with 5 random orientations each. From the engineering stress-strain curve of each simulation, extract the strain at maximum load (ε_u) and compute the mean ε̄_u across the 5 orientations. Output the aggregated results to step_01_aggregate_data.csv with columns: l_d, t_d, epsilon_u_bar (mean ε̄_u), epsilon_u_0 (the single-crystal baseline mean computed in step_02). Include at least 10 rows covering at least 3 distinct l/d and 3 distinct t/d values.
- Output file: `/app/outputs/step_01_aggregate_data.csv`
- Format: csv
- Contract: Columns: l_d (float), t_d (float), epsilon_u_bar (float), epsilon_u_0 (float). At least 10 rows with ≥3 distinct l_d and ≥3 distinct t_d.
- Scoring: scored by hidden verifier

### Step 5: Bending SSE trend data
- Role: scored
- Action: Run pure bending simulations for a few conditions (e.g., l/d=40, t/d=1.5 and l/d=80, t/d=1.5) using the same 316L model and mesh generation. Compute curvature at maximum moment κ_u and derive surface strain ε_s = κ_u * t / 2, averaged over orientations. Output to step_02_bending_trend.csv with columns: l_d, t_d, epsilon_s. The data must show a decreasing ε_s trend with increasing l_d at fixed t_d.
- Output file: `/app/outputs/step_02_bending_trend.csv`
- Format: csv
- Contract: Columns: l_d (float), t_d (float), epsilon_s (float). At least 2 rows with the same t_d and increasing l_d showing decreasing epsilon_s.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_aggregate_data.csv`
- `/app/outputs/step_02_bending_trend.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_aggregate_data.csv
- path: `/app/outputs/step_01_aggregate_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Aggregated mean strain at UTS for each l/d and t/d condition, used by the checker to recompute the power-law model parameter β and coefficient of determination R².
- schema:
  - `type`: table
  - `required_columns`: `l_d`, `t_d`, `epsilon_u_bar`, `epsilon_u_0`
  - `units`:
    - `l_d`: dimensionless
    - `t_d`: dimensionless
    - `epsilon_u_bar`: dimensionless
    - `epsilon_u_0`: dimensionless

### step_02_bending_trend.csv
- path: `/app/outputs/step_02_bending_trend.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Surface strain at maximum moment for bending, checked for decreasing ε_s trend with increasing l/d at fixed t/d.
- schema:
  - `type`: table
  - `required_columns`: `l_d`, `t_d`, `epsilon_s`
  - `units`:
    - `l_d`: dimensionless
    - `t_d`: dimensionless
    - `epsilon_s`: dimensionless

Notes: The checker will fit the power-law model from step_01_aggregate_data.csv and verify the bending trend from step_02_bending_trend.csv. All outputs are dimensionless; the agent must compute and report values from simulations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_aggregate_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "l_d",
          "t_d",
          "epsilon_u_bar",
          "epsilon_u_0"
        ],
        "units": {
          "l_d": "dimensionless",
          "t_d": "dimensionless",
          "epsilon_u_bar": "dimensionless",
          "epsilon_u_0": "dimensionless"
        }
      },
      "description": "Aggregated mean strain at UTS for each l/d and t/d condition, used by the checker to recompute the power-law model parameter β and coefficient of determination R²."
    },
    {
      "file": "step_02_bending_trend.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "l_d",
          "t_d",
          "epsilon_s"
        ],
        "units": {
          "l_d": "dimensionless",
          "t_d": "dimensionless",
          "epsilon_s": "dimensionless"
        }
      },
      "description": "Surface strain at maximum moment for bending, checked for decreasing ε_s trend with increasing l/d at fixed t/d."
    }
  ],
  "notes": "The checker will fit the power-law model from step_01_aggregate_data.csv and verify the bending trend from step_02_bending_trend.csv. All outputs are dimensionless; the agent must compute and report values from simulations."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the specified CSV files.

- For `step_01_aggregate_data.csv`, the verifier will use the data to fit the power‑law model described in the approach and compute the model parameter β and the coefficient of determination R²; it will then compare these to hidden reference values. It will also verify that, for fixed `t_d`, `epsilon_u_bar` is a decreasing function of `l_d` (a monotonic trend).
- For `step_02_bending_trend.csv`, the verifier will check that for fixed `t_d`, `epsilon_s` decreases with increasing `l_d`.

The combined score is a weighted sum of the performance on the tension and bending stages. The verifier does not receive the paper and does not expect exact numerical matches; it assesses whether your computed data support the intended trends and quantitative relationships. Reporting the paper’s numbers without genuine simulation will not pass.
