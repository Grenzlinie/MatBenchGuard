# Spherical Cavity Elasticity under Uniaxial Stress: Hollow vs Water-Filled Inclusions

## Problem background
Concrete contains many voids (pores) that may be filled with air/vapour (dry) or with water (saturated). It is well known that moisture content affects measured compressive strength, static modulus of elasticity, and tensile strength, but a unified mechanistic explanation is needed. This task implements an analytical elastic model that treats concrete pores as spherical cavities inside an infinite elastic matrix. Under remote uniaxial compressive or tensile load, the stress distributions around hollow (air-filled) and water-filled cavities are computed and compared to quantify how moisture influences mechanical behaviour.

## Approach
The model uses Goodier's classical solution for a spherical inclusion in an infinite elastic body. The concrete matrix has Poisson's ratio v = 0.2.

For a hollow cavity (inclusion shear modulus μ_i = 0), the elastic constants A, B, C are determined from boundary conditions; the hoop stress ww (the stress component on the equator in the loading direction) on the cavity surface is then evaluated at polar angles w = 0 (top/bottom) and w = π/2 (equator), expressed as a ratio of the applied remote uniaxial compressive stress p.

For a water-filled cavity, water is treated as incompressible. The cavity volume change computed from the hollow-cavity radial displacement is resisted by an internal pressure q. Using superposition, the solution is the sum of (a) the hollow cavity under uniaxial load and (b) the unloaded body with uniform internal pressure q. The pressure q is derived by equating the volume-change contribution of the radial displacement to that caused by the internal pressure. The resulting hoop stresses at w = 0 and w = π/2 are then computed.

To model the effect on static modulus, a cubic element containing a single spherical cavity is considered. The dry (hollow) and wet (water-filled) total displacements ΔL1 and ΔL2 are computed from the analytic formulas that depend on the ratio of cavity diameter to side length, D/L. Two representative values are evaluated: D/L = 0.5 and D/L = 0.667.

For uniaxial tension, the applied stress p is replaced by −p. Under tension the cavity volume increases, so water cannot pressurize; therefore the stress distributions for hollow and water-filled cavities are identical. Hoop stresses at w = 0 are computed for both cases to confirm this equivalence.

All quantities are dimensionless ratios (stresses normalised by |p|) and are collected into a single JSON file.

## Reproduction target
Implement the analytical elastic model for a spherical cavity under remote uniaxial stress. For a concrete matrix with Poisson's ratio v = 0.2, compute the following dimensionless quantities (all expressed as ratios of the applied load magnitude):
(1) Hoop stress ww on the cavity surface for a hollow (air-filled) cavity under uniaxial compression at angles w = 0 and w = π/2.
(2) Internal pressure q developed in a water-filled cavity under uniaxial compression, as a fraction of the applied load.
(3) Hoop stress ww on the cavity surface for a water-filled cavity under uniaxial compression at w = 0 and w = π/2.
(4) Displacement ratio ΔL1/ΔL2 for a cubic element containing a spherical cavity, for D/L = 0.5 and D/L = 0.667.
(5) Hoop stress ww at w = 0 for both hollow and water-filled cavities under uniaxial tension, confirming that the two values are equal.
All results must be written to /app/outputs/results.json as a JSON object with the keys specified in the output contract.

## Assets
This task requires only standard Python 3 with the built-in math library. No external datasets, models, or packages are needed.

## Workflow steps

### Step 1: Compute hollow cavity stresses
- Role: process
- Action: Implement Goodier's solution for a spherical cavity (mu_i = 0) in an infinite matrix with Poisson's ratio v = 0.2. Compute the constants A, B, C and evaluate the hoop stress ww (the component on the equator in the loading direction) on the cavity surface (r = a) at polar angles w = 0 (top/bottom) and w = pi/2 (equator). All stresses to be expressed as ratios of the applied uniaxial compressive stress p.
- Evidence: none

### Step 2: Derive internal pressure q for water-filled cavity
- Role: process
- Action: Obtain the radial displacement component that affects volume change for the hollow cavity. Equate this to the displacement caused by an internal pressure q in an unloaded elastic body to derive q as a function of p and v. Compute the numerical ratio q/p for v = 0.2.
- Evidence: none

### Step 3: Compute water-filled cavity stresses
- Role: process
- Action: Using superposition, combine the hollow cavity stress solution with the stress field from a uniform internal pressure of magnitude q (derived above) to obtain the hoop stress ww at the cavity surface for a water-filled cavity. Evaluate at w = 0 and w = pi/2, expressing results as ratios of p.
- Evidence: none

### Step 4: Compute displacement ratios for cubic element model
- Role: process
- Action: For a cubic element containing a spherical cavity, compute the dry-to-wet total displacement ratio ΔL1/ΔL2 using the analytic formulas that depend on the ratio D/L. Compute for two representative values: D/L = 0.5 and D/L = 0.667.
- Evidence: none

### Step 5: Compute tensile case equivalence
- Role: process
- Action: For uniaxial tension (p replaced by -p), compute the hollow cavity hoop stress ww at w = 0. Show that the water-filled cavity stress is identical (water cannot pressurize under tension) and evaluate at w = 0, expressing both as ratios of |p|.
- Evidence: none

### Step 6: Write compiled results
- Role: scored (load-bearing)
- Action: Collect all computed quantities and write them to /app/outputs/results.json as a JSON object with numeric keys. All values are dimensionless ratios (normalized by the applied stress magnitude p). The required keys are: 'hollow_ww_at_0', 'hollow_ww_at_pi2', 'water_ww_at_0', 'water_ww_at_pi2', 'internal_pressure_q', 'delta_L1_delta_L2_DL_0_5', 'delta_L1_delta_L2_DL_0_667', 'tension_hollow_ww_at_0', 'tension_water_ww_at_0'.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: object with numeric keys: hollow_ww_at_0, hollow_ww_at_pi2, water_ww_at_0, water_ww_at_pi2, internal_pressure_q, delta_L1_delta_L2_DL_0_5, delta_L1_delta_L2_DL_0_667, tension_hollow_ww_at_0, tension_water_ww_at_0
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
- description: Compiled dimensionless results from the elastic analysis of hollow and water-filled spherical cavities under uniaxial compression and tension.
- schema:
  - `type`: object
  - `required`: `hollow_ww_at_0`, `hollow_ww_at_pi2`, `water_ww_at_0`, `water_ww_at_pi2`, `internal_pressure_q`, `delta_L1_delta_L2_DL_0_5`, `delta_L1_delta_L2_DL_0_667`, `tension_hollow_ww_at_0`, `tension_water_ww_at_0`
  - `properties`:
    - `hollow_ww_at_0`:
      - `type`: number
      - `description`: hoop stress ww at cavity surface and angle 0 for hollow cavity, ratio of applied stress p
    - `hollow_ww_at_pi2`:
      - `type`: number
      - `description`: hoop stress ww at cavity surface and angle pi/2 for hollow cavity, ratio of p
    - `water_ww_at_0`:
      - `type`: number
      - `description`: hoop stress ww at cavity surface and angle 0 for water-filled cavity, ratio of p
    - `water_ww_at_pi2`:
      - `type`: number
      - `description`: hoop stress ww at cavity surface and angle pi/2 for water-filled cavity, ratio of p
    - `internal_pressure_q`:
      - `type`: number
      - `description`: internal cavity pressure q, ratio of p
    - `delta_L1_delta_L2_DL_0_5`:
      - `type`: number
      - `description`: displacement ratio ΔL1/ΔL2 for D/L = 0.5
    - `delta_L1_delta_L2_DL_0_667`:
      - `type`: number
      - `description`: displacement ratio ΔL1/ΔL2 for D/L = 0.667
    - `tension_hollow_ww_at_0`:
      - `type`: number
      - `description`: hoop stress ww at cavity surface and angle 0 for hollow cavity under uniaxial tension, ratio of |p|
    - `tension_water_ww_at_0`:
      - `type`: number
      - `description`: hoop stress ww at cavity surface and angle 0 for water-filled cavity under uniaxial tension, ratio of |p|

Notes: All stresses are reported as ratios of the applied remote uniaxial stress magnitude. The numerical values correspond to Poisson's ratio v = 0.2 for the concrete matrix. The displacement ratios follow the cubic element model and are based on the given analytic formulas for D/L = 0.5 and 0.667.

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
          "hollow_ww_at_0",
          "hollow_ww_at_pi2",
          "water_ww_at_0",
          "water_ww_at_pi2",
          "internal_pressure_q",
          "delta_L1_delta_L2_DL_0_5",
          "delta_L1_delta_L2_DL_0_667",
          "tension_hollow_ww_at_0",
          "tension_water_ww_at_0"
        ],
        "properties": {
          "hollow_ww_at_0": {
            "type": "number",
            "description": "hoop stress ww at cavity surface and angle 0 for hollow cavity, ratio of applied stress p"
          },
          "hollow_ww_at_pi2": {
            "type": "number",
            "description": "hoop stress ww at cavity surface and angle pi/2 for hollow cavity, ratio of p"
          },
          "water_ww_at_0": {
            "type": "number",
            "description": "hoop stress ww at cavity surface and angle 0 for water-filled cavity, ratio of p"
          },
          "water_ww_at_pi2": {
            "type": "number",
            "description": "hoop stress ww at cavity surface and angle pi/2 for water-filled cavity, ratio of p"
          },
          "internal_pressure_q": {
            "type": "number",
            "description": "internal cavity pressure q, ratio of p"
          },
          "delta_L1_delta_L2_DL_0_5": {
            "type": "number",
            "description": "displacement ratio ΔL1/ΔL2 for D/L = 0.5"
          },
          "delta_L1_delta_L2_DL_0_667": {
            "type": "number",
            "description": "displacement ratio ΔL1/ΔL2 for D/L = 0.667"
          },
          "tension_hollow_ww_at_0": {
            "type": "number",
            "description": "hoop stress ww at cavity surface and angle 0 for hollow cavity under uniaxial tension, ratio of |p|"
          },
          "tension_water_ww_at_0": {
            "type": "number",
            "description": "hoop stress ww at cavity surface and angle 0 for water-filled cavity under uniaxial tension, ratio of |p|"
          }
        }
      },
      "description": "Compiled dimensionless results from the elastic analysis of hollow and water-filled spherical cavities under uniaxial compression and tension."
    }
  ],
  "notes": "All stresses are reported as ratios of the applied remote uniaxial stress magnitude. The numerical values correspond to Poisson's ratio v = 0.2 for the concrete matrix. The displacement ratios follow the cubic element model and are based on the given analytic formulas for D/L = 0.5 and 0.667."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that reads /app/outputs/results.json. For each required key, the verifier compares your computed value to an independent reference (obtained from the same analytic formulas) and assigns credit based on closeness within a hidden tolerance. The verifier also checks structural relationships (for example, the ratio of two values and the equality of the two tension values). Partial credit is given for each correctly computed quantity; the final reward is the weighted sum of the component scores.
