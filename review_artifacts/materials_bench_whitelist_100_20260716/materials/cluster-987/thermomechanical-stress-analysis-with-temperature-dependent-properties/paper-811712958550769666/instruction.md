# Thermomechanical Stress Analysis with Temperature-Dependent Properties

## Problem background
Thermal shock treatment can introduce beneficial compressive residual stresses around a hole in a sheet metal, thereby improving its load-bearing capacity. This work addresses an axisymmetric thin disk with a concentric hole subjected to an annular thermal shock of finite duration. The aim is to determine the residual stress distribution induced by the shock and to quantify the resulting increase in the maximum tensile stress that the sheet can withstand before plastic yielding occurs.

## Approach
The problem is treated with quasi-static, uncoupled thermoelastoplasticity using incremental von Mises plasticity (elastic‑perfectly plastic material) under plane‑stress conditions. The temperature field is first obtained analytically by solving the transient heat conduction equation via the Hankel transform technique, yielding a series solution for the annular heat pulse. Next, the coupled integro‑differential equations for the mean stress σ(r,t) and the deviatoric difference s(r,t) are integrated numerically in time, with an iteration scheme for the plastic flow variables at each time step. The unknown shock intensity Q is determined by an inverse routine that drives the residual tangential stress at the hole rim to a prescribed target value after complete cooling. Finally, the resulting residual stress field is superimposed on the analytical elastic stress distribution for a uniaxially loaded infinite plate with a circular hole (Timoshenko formula), and the maximum applied tensile stress S that maintains the von Mises yield criterion everywhere is computed.

## Reproduction target
For the specific thermal shock applied over the annulus with inner normalized radius a₁/b = 0.25 and normalized width (b₁‑a₁)/b = 0.2375, duration 1.5×10⁻³ s, on an aluminum disk of given geometry and material properties (fully specified in the workflow), determine the shock intensity Q that yields the target residual tangential stress at the inner radius r = a (target given in the workflow). Then compute the complete residual stress distribution σ_r(r), σ_θ(r) after cooling and combine it with the elastic stress field for a uniaxial tensile load S on an infinite plate with a hole. Find the maximum S such that the von Mises yield criterion J₂ ≤ σ_ys² is satisfied everywhere. Report Q, the residual tangential stress at r = a, the maximum dimensionless tensile stress S/σ_ys, and the percentage improvement over the untreated case (S/σ_ys for a plain sheet with a hole but no residual stress).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve heat conduction problem
- Role: process
- Action: Numerically solve the axisymmetric transient heat conduction equation for a thin disk with given geometry and material properties, subjected to an annular square heat pulse of unknown intensity Q. Use the Hankel transform technique: compute eigenvalues from the transcendental equation, evaluate temperature as an infinite series for both heating (0 ≤ t ≤ t1) and cooling (t ≥ t1) phases. Produce the temperature field as a 2D array (radial grid × time steps).
- Evidence: `/app/outputs/temperature_field.npy`

### Step 2: Solve thermoelastoplastic stress evolution and determine thermal shock intensity Q
- Role: process
- Action: Starting from zero initial stresses, numerically integrate the coupled integro-differential equations for mean stress σ(r,t) and deviatoric difference s(r,t) under plane-stress, incremental von Mises plasticity (elastic‑perfectly plastic) with temperature‑independent yield strength. Use the temperature field from step_01. Implement an iteration scheme for the plastic flow variables g and μ at each time step, with a correction factor when the yield criterion is exceeded. At each time step, evaluate integrals involving temperature rate analytically and those involving μ by numerical quadrature. Iterate over the shock intensity Q to achieve the target residual tangential stress at r=a of -0.41 σ_ys. Record the complete residual stress distribution σ_r(r), σ_θ(r) after complete cooling (t→∞).
- Evidence: `/app/outputs/residual_stresses.csv`

### Step 3: Compute load-bearing capacity and final results
- Role: scored (load-bearing)
- Action: Load the residual stress distribution from step_02. Superimpose the analytical stress field for a uniaxial tensile stress S in an infinite plate with a hole (Timoshenko formula). Determine the maximum S such that the von Mises yield criterion J₂ ≤ σ_ys² is satisfied everywhere. Write the determined shock intensity Q, the residual tangential stress at r=a, the maximum dimensionless tensile stress S/σ_ys, and the percentage improvement over the untreated value 0.577 to a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: Q (float, units J/(hr·cm³)), residual_sigma_theta_at_a (float, units N/cm²), S_over_sigma_ys (float, dimensionless), improvement_percentage (float, in percent).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Final results containing the key quantities: Q, residual_sigma_theta_at_a, S_over_sigma_ys, improvement_percentage.
- schema:
  - `type`: object
  - `required`: `Q`, `residual_sigma_theta_at_a`, `S_over_sigma_ys`, `improvement_percentage`
  - `properties`:
    - `Q`:
      - `type`: number
      - `description`: Thermal shock intensity, J/(hr·cm³)
    - `residual_sigma_theta_at_a`:
      - `type`: number
      - `description`: Residual tangential stress at inner radius, N/cm²
    - `S_over_sigma_ys`:
      - `type`: number
      - `description`: Maximum dimensionless tensile stress
    - `improvement_percentage`:
      - `type`: number
      - `description`: Improvement over untreated value 0.577, percent

Notes: The task is scoped to the single optimal thermal shock case (a₁/b=0.25, (b₁‑a₁)/b=0.2375). The yield strength is treated as temperature‑independent. The shock intensity Q is determined by an inverse solution during step_02. The combined loading analysis uses the Timoshenko formula for stress distribution around a hole in an infinite plate.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Q",
          "residual_sigma_theta_at_a",
          "S_over_sigma_ys",
          "improvement_percentage"
        ],
        "properties": {
          "Q": {
            "type": "number",
            "description": "Thermal shock intensity, J/(hr·cm³)"
          },
          "residual_sigma_theta_at_a": {
            "type": "number",
            "description": "Residual tangential stress at inner radius, N/cm²"
          },
          "S_over_sigma_ys": {
            "type": "number",
            "description": "Maximum dimensionless tensile stress"
          },
          "improvement_percentage": {
            "type": "number",
            "description": "Improvement over untreated value 0.577, percent"
          }
        }
      },
      "description": "Final results containing the key quantities: Q, residual_sigma_theta_at_a, S_over_sigma_ys, improvement_percentage."
    }
  ],
  "notes": "The task is scoped to the single optimal thermal shock case (a₁/b=0.25, (b₁‑a₁)/b=0.2375). The yield strength is treated as temperature‑independent. The shock intensity Q is determined by an inverse solution during step_02. The combined loading analysis uses the Timoshenko formula for stress distribution around a hole in an infinite plate."
}
```

## How you are scored
A hidden verifier reads your `results.json` and independently compares each quantity (Q, residual_sigma_theta_at_a, S_over_sigma_ys, improvement_percentage) to reference values derived from the paper, applying tolerances that account for expected numerical differences due to discretisation, eigenvalue truncation, and solver choices. The reward is based on how close your computed results are to the reference; simply reporting a memorised number without executing the required computation will not yield a passing score.
