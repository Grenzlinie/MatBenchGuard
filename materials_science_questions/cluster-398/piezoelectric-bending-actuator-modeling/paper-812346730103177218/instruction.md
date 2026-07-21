# Nonlinear Piezoelectric Bending Actuator

## Problem background
Piezoelectric bending actuators are essential components in precision positioning, smart structures, and acoustic transducers. They consist of thin piezoelectric plates bonded together (bimorph) or bonded to an elastic substrate (unimorph) so that an applied electric field generates a large bending displacement. Under strong electric fields, the tip deflection and blocking force of these actuators deviate significantly from the predictions of linear piezoelectric theory because of field‑dependent nonlinear effects: electroelastic softening (change in elastic compliance with field) and electrostrictive strain (strain quadratic in field). Understanding and correctly modeling these nonlinearities is critical for actuator design. This work develops a nonlinear analytical model that captures the observed behavior, allowing the tip deflection and blocking force to be computed as functions of the applied electric field.

## Approach
The model treats the actuator as a laminated slender beam under the Kirchhoff hypothesis. A nonlinear constitutive relation that includes the piezoelectric coefficient d31, an electroelastic coefficient d311, and an electrostrictive coefficient m31 is used. The effective stiffness of the piezoelectric layer becomes field‑dependent: Q11 = Ep/(1 + d311 Ep Ez). An effective electrostrictive constant m31' = m31 - 2 Ep d31 d311 absorbs the electroelastic coupling. Force and moment resultants are derived, and the governing differential equations are solved with cantilever boundary conditions to obtain closed‑form expressions for the static tip deflection and blocking force. For a symmetric bimorph (two identical PZT plates, no substrate) the expressions simplify further. For a unimorph (one PZT plate on a stainless‑steel substrate) the stiffnesses of both layers and the thickness ratio enter. The task is to implement these closed‑form expressions, together with the specified material constants and geometric parameters, to compute the nonlinear response curves of both actuator types.

## Key formulas

### Bimorph actuator (symmetric, no substrate)

The tip deflection δ (m) and blocking force Fbl (N) for a bimorph with two identical PZT plates are given by:

δ = (3 * L² / (2 * t)) * (1 + d311 * Ez * Ep) * d31 * Ez

Fbl = (3 * b * t² * Ep / (8 * L)) * (1 + d311 * Ez * Ep) * d31 * Ez

where:
- L = 40 mm = 0.04 m (actuator length)
- b = 7 mm = 0.007 m (width)
- tp = 0.5 mm = 0.0005 m (single plate thickness), total thickness t = 2 * tp = 0.001 m
- Ep = 60.6e9 Pa
- d31 = -274e-12 C/N (or m/V)
- d311 = 2.85e-17 m³/(N·V)

### Unimorph actuator (PZT on stainless steel)

Use the following nonlinear expressions from the paper (Eqs. 40‑41):

Given:
L = 40 mm = 0.04 m, b = 7 mm = 0.007 m
tp = 0.68 mm = 0.00068 m (PZT thickness)
ts = 0.38 mm = 0.00038 m (steel thickness)
t = tp + ts = 0.00106 m
Ep = 60.6e9 Pa, Em = 210e9 Pa
d31 = -274e-12 C/N
d311 = 2.85e-17 m³/(N·V)
m31' = -3.70e-16 m²/V²

Define:
A = Em / Ep
B = ts / tp

Compute tip deflection:
δ = (3 * L² / t) * (A * B * (1 + B)² * (1 + d311 * Ez * Ep)² * (d31 * Ez + 0.5 * m31' * Ez²)) / Δ

Compute blocking force:
Fbl = (3 * b * t² * Ep / (4 * L)) * (A * B * (1 + A² * B⁴ + 2 * A * (2 * B + 3 * B² + 2 * B³)) * (1 + d311 * Ez * Ep)² * (d31 * Ez + 0.5 * m31' * Ez²)) / ((1 + B) * (1 + A * B) * Δ)

where
Δ = 1 + A² * B⁴ + 2 * A * (2 * B + 3 * B² + 2 * B³) * (1 + d311 * Ez * Ep) + A² * B⁴ * d311 * Ez * Ep * (2 + d311 * Ez * Ep)

All quantities in SI units; Ez in V/m. Produce δ in meters, Fbl in Newtons.

## Reproduction target
Compute the tip deflection δ and blocking force Fbl of a symmetric bimorph actuator and a unimorph actuator over a range of applied electric field Ez from 0 to 1×10⁶ V/m in steps of 5×10⁴ V/m. Use the nonlinear expressions for each actuator type with the following fixed parameters.

Bimorph:
- Two identical PZT plates: length L = 40 mm, width b = 7 mm, each thickness tp = 0.5 mm (total thickness t = 2×tp = 1.0 mm).
- No substrate.

Unimorph:
- PZT plate: L = 40 mm, b = 7 mm, tp = 0.68 mm.
- Stainless‑steel substrate: L = 40 mm, b = 7 mm, ts = 0.38 mm; Young's modulus Em = 210 GPa.
- Total thickness t = tp + ts.

Piezoelectric material constants (soft PZT):
- Young's modulus Ep = 60.6 GPa,
- piezoelectric coefficient d31 = -274 × 10⁻¹² C/N,
- electroelastic coefficient d311 = 2.85 × 10⁻¹⁷ m³/(N·V),
- effective electrostrictive constant m31' = -3.70 × 10⁻¹⁶ m²/V².

Produce two JSON arrays under /app/outputs: step_01_bimorph_results.json and step_02_unimorph_results.json, each containing records with keys electric_field (V/m), tip_deflection (m), and blocking_force (N).

## Assets

- Python 3 with numpy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Bimorph nonlinear model computation
- Role: scored (load-bearing)
- Action: Using the closed‐form nonlinear expressions for tip deflection and blocking force of a symmetric bimorph (derived in the paper), compute the steady‐state response for a range of applied electric fields. For each field value (e.g., 0 to 1e6 V/m in steps of ~5e4 V/m), evaluate the tip deflection δ (m) and blocking force Fbl (N) with the material constants and actuator dimensions reported for the bimorph. Output the results as a JSON array.
- Output file: `/app/outputs/step_01_bimorph_results.json`
- Format: json
- Contract: JSON array of objects, each with numeric fields: electric_field (float, V/m), tip_deflection (float, m), blocking_force (float, N).
- Scoring: scored by hidden verifier

### Step 2: Unimorph nonlinear model computation
- Role: scored (load-bearing)
- Action: Using the closed‐form nonlinear expressions for tip deflection and blocking force of a unimorph with elastic substrate (derived in the paper), compute the same quantities over the same electric‐field range. Use the material constants and dimensions reported for the unimorph (PZT layer and substrate). Output the results as a JSON array.
- Output file: `/app/outputs/step_02_unimorph_results.json`
- Format: json
- Contract: JSON array of objects, each with numeric fields: electric_field (float, V/m), tip_deflection (float, m), blocking_force (float, N).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bimorph_results.json`
- `/app/outputs/step_02_unimorph_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bimorph_results.json
- path: `/app/outputs/step_01_bimorph_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Predicted bimorph tip deflection and blocking force as functions of electric field.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `electric_field`:
        - `type`: number
        - `unit`: V/m
      - `tip_deflection`:
        - `type`: number
        - `unit`: m
      - `blocking_force`:
        - `type`: number
        - `unit`: N
    - `required`: `electric_field`, `tip_deflection`, `blocking_force`

### step_02_unimorph_results.json
- path: `/app/outputs/step_02_unimorph_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Predicted unimorph tip deflection and blocking force as functions of electric field.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `electric_field`:
        - `type`: number
        - `unit`: V/m
      - `tip_deflection`:
        - `type`: number
        - `unit`: m
      - `blocking_force`:
        - `type`: number
        - `unit`: N
    - `required`: `electric_field`, `tip_deflection`, `blocking_force`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bimorph_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "electric_field": {
              "type": "number",
              "unit": "V/m"
            },
            "tip_deflection": {
              "type": "number",
              "unit": "m"
            },
            "blocking_force": {
              "type": "number",
              "unit": "N"
            }
          },
          "required": [
            "electric_field",
            "tip_deflection",
            "blocking_force"
          ]
        }
      },
      "description": "Predicted bimorph tip deflection and blocking force as functions of electric field."
    },
    {
      "file": "step_02_unimorph_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "electric_field": {
              "type": "number",
              "unit": "V/m"
            },
            "tip_deflection": {
              "type": "number",
              "unit": "m"
            },
            "blocking_force": {
              "type": "number",
              "unit": "N"
            }
          },
          "required": [
            "electric_field",
            "tip_deflection",
            "blocking_force"
          ]
        }
      },
      "description": "Predicted unimorph tip deflection and blocking force as functions of electric field."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently implements the same nonlinear model and recomputes the expected tip deflection and blocking force for each electric field value you provide. For each actuator type, the verifier compares your reported values to the recomputed ones point by point. A point is considered correct if both the deflection and the force lie within a small tolerance band. The reward for each actuator stage is proportional to the fraction of electric‑field points that pass this check. The final overall reward is the weighted sum of the two stage rewards. Reporting the paper’s numbers is not enough; you must produce the outputs by running your own implementation of the model.
