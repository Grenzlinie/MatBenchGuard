# Analytical Modeling of Circular Diaphragm Piezoactuator with Gas Compression

## Problem background
A circular diaphragm-type piezoelectric actuator consists of one or more piezoelectric (PZT) layers bonded to a passive layer. When clamped at its edge and driven by a voltage, the actuator bends, changing the volume of an underlying sealed chamber filled with gas. The coupled deflection and gas compression determine the static pressure rise achievable in a gas micropump. An analytical model that predicts the actuator's transverse displacement and the resulting gas pressure as functions of geometry, material properties, and applied voltage is needed to design and optimise such pumps. This task reproduces the analytical framework that captures the electro-fluid-structural coupling and applies it to a specific bimorph actuator configuration.

## Approach
The model is built on the principle of minimum total potential energy. The total potential includes: the elastic strain energy of the passive, bonding, and piezoelectric layers (described by Kirchhoff thin plate theory and linear piezoelectric constitutive relations); the electric potential energy due to the applied voltage; and the work done on the gas, treated as an ideal gas undergoing isothermal compression. A trial function for the transverse displacement w(r) is chosen that automatically satisfies the clamped‑edge boundary conditions (zero displacement and zero slope at the clamped radius). The trial function is a polynomial in (1 – r²/r₁²) multiplied by an envelope that guarantees these conditions. The unknown coefficients are obtained by solving the linear system that results from setting the derivatives of the total potential with respect to each coefficient to zero (Rayleigh–Ritz method). Once the coefficients are known, the displacement at any radius and the resulting chamber pressure can be evaluated. The model is applied to a bimorph actuator (two symmetric PZT layers, two thin bonding layers, and a central brass passive layer) using the specific geometry and material constants provided in the task; all required parameters are given in the problem statement.

## Reproduction target
1. Using the geometry and material parameters for the bimorph (provided in the task assets), implement the Rayleigh–Ritz model **without gas compression** (gas work term turned off). Evaluate the transverse deflection w(r) at 20 equally spaced radial positions from r = 0 to the clamped edge radius r₁ = 15 mm, for an applied voltage V = 100 V. Save this profile as `deflection_profile.csv` with columns `r_mm` and `w_um`. Also record the center displacement (the value at r = 0) for later inclusion in the results file.

2. Enable the gas compression term (chamber depth Hc = 100 μm, initial pressure P₀ = 101.3 kPa). Keeping the default bimorph dimensions as a baseline, search over a physically reasonable range of the PZT radius to passive radius ratio (r₂/r₁) and the PZT thickness to passive thickness ratio (t_{pzt}/t_p) to find the combination that **maximises the static pressure rise**. Report the optimal r₂/r₁ and t_{pzt}/t_p, and the pressure rise (in kPa) computed at V = 120 V under those optimal ratios, together with the center displacement from step 1, in a JSON file `results.json` with keys `center_displacement_um`, `pressure_rise_kPa`, `optimal_r2_r1`, and `optimal_tpzt_tp`. Use the same energy‑minimisation framework throughout; do not attempt to guess or short‑circuit the optimisation.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement Rayleigh-Ritz analytical model
- Role: process
- Action: Implement the total potential energy functional L = U_p + U_b + U_{pzt} - U_E + U_{gas} for the bimorph actuator using the geometry and material parameters from the paper. Derive the elastic energies of passive, bonding, and PZT layers, the electric potential energy, and the gas compression work (with chamber depth Hc and initial pressure P0). Apply the trial function w(r) = (1 - r²/r₁²)² Σ_{i=1}^{4} C_i (1 - r²/r₁²)^{i-1} satisfying clamped-edge conditions, set up the linear system ∂L/∂C_i = 0, and solve for coefficients C_i. This step produces the callable model that will be used in downstream steps.
- Evidence: none

### Step 2: Compute deflection profile of bimorph at 100V
- Role: scored
- Action: Using the implemented model with no gas compression (U_gas = 0), compute the transverse deflection w(r) for the bimorph actuator at applied voltage V = 100 V. Evaluate w(r) at 20 equally spaced radial positions from r = 0 to r = r₁ (outer radius = 15 mm). Output the profile as a CSV file with columns r_mm (radius in mm) and w_um (deflection in μm).
- Output file: `/app/outputs/deflection_profile.csv`
- Format: csv
- Contract: columns: r_mm (float), w_um (float); 20 rows.
- Scoring: scored by hidden verifier

### Step 3: Compute optimal dimensions and pressure rise
- Role: scored (load-bearing)
- Action: Using the model including gas compression (chamber depth Hc=100 μm, initial pressure P0=101.3 kPa): (a) compute the center displacement at V=100 V without gas; (b) vary the radius ratio r₂/r₁ and thickness ratio t_{pzt}/t_p within physically reasonable bounds to locate the optimal values that maximize static pressure rise; (c) with the found optimal geometry, compute the pressure rise at V=120 V. Output all four numeric results in a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"center_displacement_um": <float>, "pressure_rise_kPa": <float>, "optimal_r2_r1": <float>, "optimal_tpzt_tp": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/deflection_profile.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deflection_profile.csv
- path: `/app/outputs/deflection_profile.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Deflection profile of the bimorph actuator at 100 V without gas compression, sampled at 20 equally spaced radii from 0 to 15 mm.
- schema:
  - `type`: table
  - `required_columns`: `r_mm`, `w_um`
  - `units`:
    - `r_mm`: mm
    - `w_um`: μm

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Key computed results: center displacement, optimal geometric ratios, and pressure rise under optimal conditions.
- schema:
  - `type`: object
  - `required`: `center_displacement_um`, `pressure_rise_kPa`, `optimal_r2_r1`, `optimal_tpzt_tp`
  - `properties`:
    - `center_displacement_um`:
      - `type`: number
      - `unit`: μm
    - `pressure_rise_kPa`:
      - `type`: number
      - `unit`: kPa
    - `optimal_r2_r1`:
      - `type`: number
    - `optimal_tpzt_tp`:
      - `type`: number

Notes: The hidden checker compares the reported deflection profile at a set of hidden radial points and the four numeric values in results.json against the paper's analytical solution, using tolerances appropriate for a re-implementation. The deflection profile is also checked for monotonic decrease from center to edge and near-zero displacement at the clamped boundary.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deflection_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_mm",
          "w_um"
        ],
        "units": {
          "r_mm": "mm",
          "w_um": "μm"
        }
      },
      "description": "Deflection profile of the bimorph actuator at 100 V without gas compression, sampled at 20 equally spaced radii from 0 to 15 mm."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "center_displacement_um",
          "pressure_rise_kPa",
          "optimal_r2_r1",
          "optimal_tpzt_tp"
        ],
        "properties": {
          "center_displacement_um": {
            "type": "number",
            "unit": "μm"
          },
          "pressure_rise_kPa": {
            "type": "number",
            "unit": "kPa"
          },
          "optimal_r2_r1": {
            "type": "number"
          },
          "optimal_tpzt_tp": {
            "type": "number"
          }
        }
      },
      "description": "Key computed results: center displacement, optimal geometric ratios, and pressure rise under optimal conditions."
    }
  ],
  "notes": "The hidden checker compares the reported deflection profile at a set of hidden radial points and the four numeric values in results.json against the paper's analytical solution, using tolerances appropriate for a re-implementation. The deflection profile is also checked for monotonic decrease from center to edge and near-zero displacement at the clamped boundary."
}
```

## How you are scored
An automated verifier compares your submitted artifacts to reference values derived from the paper's analytical solution (hidden from you). The verifier checks:

- **Deflection profile** (`deflection_profile.csv`): the shape is verified (monotonically decreasing from center to edge, near‑zero displacement at the clamped boundary), and the values at several hidden radial coordinates are compared against the expected analytical curve.
- **Key results** (`results.json`): the center displacement (μm) at 100 V without gas, the optimal r₂/r₁ and t_{pzt}/t_p ratios, and the pressure rise (kPa) at 120 V under optimal geometry are each compared to the analytical predictions with appropriate error tolerances.

The total reward is a weighted combination of per‑artifact scores. The verifier does **not** re‑run your model; it only reads your output files. Therefore, simply echoing expected numbers without correctly implementing the described energy‑minimisation solver will not yield a passing score, because the profile shape and the specific values require genuine computation. Implement the Rayleigh–Ritz procedure faithfully, and write the resulting quantities exactly as obtained from your solver.
