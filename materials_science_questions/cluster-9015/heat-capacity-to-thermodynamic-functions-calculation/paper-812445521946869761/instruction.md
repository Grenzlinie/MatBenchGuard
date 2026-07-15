# Heat capacity and entropy from piecewise polynomial fits

## Problem background
The Bi₂O₃–CaO system contains several ternary bismuth calcium oxides that appear in the phase relations relevant to the Bi–Sr–Ca–Cu–O high-temperature superconductors. Accurate standard molar heat capacities and standard molar entropies at room temperature are essential for constructing thermodynamic databases and for understanding phase stability. This task concerns the computation of the standard molar heat capacity Cpm(298.15 K) and standard molar entropy Sm(298.15 K) for three stoichiometric compounds — Bi₂Ca₂O₅, Bi₂CaO₄, and Bi₆Ca₄O₁₃ — from experimentally derived piecewise polynomial representations of their molar heat capacity as a function of temperature.

## Approach
The low- and high-temperature heat capacity data for each compound have been parameterised as piecewise polynomial functions of temperature, with continuity and smoothness enforced at the boundary temperatures. Up to 298.15 K three segments are used:

- From 0 K to 40 K: Cpm,1(T) = A₁ T + B₁ T³ (the lowest temperature form that captures the limiting behaviour).
- From 40 K up to an intermediate boundary Tₓ (120 K for Bi₂Ca₂O₅, 110 K for Bi₂CaO₄ and Bi₆Ca₄O₁₃): Cpm,2(T) = A₂ + B₂ T + C₂ T² + D₂/T².
- From Tₓ to 298.15 K: Cpm,3(T) = A₃ + B₃ T + C₃ T² + D₃/T².

Above 298.15 K a fourth segment is defined, but only the value at 298.15 K is needed here:

- From 298.15 K upwards: Cpm,4(T) = A₄ + B₄ T + C₄/T².

The molar heat capacity at 298.15 K is obtained by evaluating Cpm,4(298.15 K) with the given coefficients. The standard molar entropy at 298.15 K is obtained by piecewise analytical integration of Cpm/T from 0 K to 298.15 K:

Sm(298.15) = ∫₀⁴⁰ (Cpm,1/T) dT + ∫₄₀ᵀˣ (Cpm,2/T) dT + ∫ₜₓ²⁹⁸·¹⁵ (Cpm,3/T) dT.

Each integrand reduces to elementary forms (constant, linear, 1/T, 1/T³), so the integrals can be evaluated analytically using the provided coefficients and boundary temperatures. The coefficients and the boundary temperatures for each compound are given in the problem statement (below); no external data are required.

## Reproduction target
You are given the piecewise polynomial coefficients and the boundary temperatures for Bi₂Ca₂O₅, Bi₂CaO₄, and Bi₆Ca₄O₁₃. Compute, for each compound:

1. The standard molar heat capacity at 298.15 K, Cpm(298.15 K), in J K⁻¹ mol⁻¹, by evaluating the high-temperature polynomial Cpm,4 at T = 298.15 K.
2. The standard molar entropy at 298.15 K, Sm(298.15 K), in J K⁻¹ mol⁻¹, by evaluating the three low-temperature integrals as described in the Approach and summing them.

Write the results as a JSON array of three objects, each with keys "compound", "Cpm_298", and "Sm_298". The array must contain exactly the three compounds listed above. The output file must be written to `/app/outputs/step_01_thermodynamic_functions.json`.

## Assets

- Python 3 with standard library: python3

## Workflow steps

### Step 1: Compute thermodynamic functions at 298.15 K
- Role: scored (load-bearing)
- Action: Compute the molar heat capacity at 298.15 K by evaluating the high-temperature heat capacity polynomial (Cpm,4) using the provided parameters for each ternary oxide. Compute the standard molar entropy at 298.15 K by piecewise analytical integration of Cpm/T from 0 K to 298.15 K across the given temperature intervals using the low-temperature polynomials (Cpm,1, Cpm,2, and Cpm,3). Write a JSON array containing the compound name, Cpm(298.15) in J K⁻¹ mol⁻¹, and Sm(298.15) in J K⁻¹ mol⁻¹ for all three compounds.
- Output file: `/app/outputs/step_01_thermodynamic_functions.json`
- Format: json
- Contract: A JSON array of three objects, each with keys: 'compound' (string, exactly 'Bi2Ca2O5', 'Bi2CaO4', or 'Bi6Ca4O13'), 'Cpm_298' (float, in J K⁻¹ mol⁻¹), 'Sm_298' (float, in J K⁻¹ mol⁻¹). Example: [{"compound":"Bi2Ca2O5", "Cpm_298":..., "Sm_298":...}, ...]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermodynamic_functions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermodynamic_functions.json
- path: `/app/outputs/step_01_thermodynamic_functions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed molar heat capacity and standard molar entropy at 298.15 K for the three ternary oxides.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `Cpm_298`, `Sm_298`
    - `properties`:
      - `compound`:
        - `type`: string
        - `enum`: `Bi2Ca2O5`, `Bi2CaO4`, `Bi6Ca4O13`
      - `Cpm_298`:
        - `type`: number
        - `unit`: J K^-1 mol^-1
      - `Sm_298`:
        - `type`: number
        - `unit`: J K^-1 mol^-1

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermodynamic_functions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "Cpm_298",
            "Sm_298"
          ],
          "properties": {
            "compound": {
              "type": "string",
              "enum": [
                "Bi2Ca2O5",
                "Bi2CaO4",
                "Bi6Ca4O13"
              ]
            },
            "Cpm_298": {
              "type": "number",
              "unit": "J K^-1 mol^-1"
            },
            "Sm_298": {
              "type": "number",
              "unit": "J K^-1 mol^-1"
            }
          }
        }
      },
      "description": "Computed molar heat capacity and standard molar entropy at 298.15 K for the three ternary oxides."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier computes the same thermodynamic quantities for each compound using the identical polynomial coefficients and boundary temperatures (which are kept hidden from you). The verifier reads your submitted JSON file and compares each value (Cpm_298 and Sm_298) against its own recomputed reference. Credit is awarded proportionally for each compound and each quantity based on the agreement with the reference. The verifier then combines the partial scores into a single overall reward for this step, which is the only scored artifact in the task. You are not required to reproduce intermediate values or submit computational code; only the final JSON file matters for scoring.
