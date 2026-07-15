# Compute Saturation Limits and Verify Thermodynamic Inequalities for Distortional Hardening Models

## Problem background
In metal plasticity, directional distortional hardening refers to the formation of a region of high curvature (sharpening) on the yield surface roughly in the loading direction and a region of low curvature (flattening) on the opposite side. This work introduces two thermodynamically consistent constitutive models for directional distortion: the α‑model (distortion coupled to the backstress) and the r‑model (distortion decoupled via a separate tensor-valued internal variable). A key part of the theory is the derivation of saturation (limit) values for the isotropic size, backstress, and distortional variables, and of constraints on the material constants that guarantee non‑negative plastic dissipation. For a set of publicly available constants for 304 stainless steel, the task is to compute those saturation limits and verify whether the derived thermodynamic inequalities hold.

## Approach
Both models are defined by a yield function and evolution (hardening) rules of the evanescent‑memory (Armstrong–Frederick) type. The saturation limits are obtained by setting the evolution rates to zero, which gives simple algebraic expressions in terms of the material constants κ₂, a₂, c₂, and ρ₂. For the α‑model the relevant quantities are the isotropic size limit k^l = 1/κ₂, the backstress norm limit |α^l| = 1/a₂, the distortional limit c^l = 1/(a₂ c₂), and the thermodynamic inequality c₂ a₂² ≥ 1. For the r‑model the additional limit is the distortional tensor norm |r^l| = 1/ρ₂, and the required thermodynamic condition is ρ₂ > 1. The task implements these formulas using the provided numerical constants and writes the results to a JSON file.

## Reproduction target
Compute the saturation limits of the internal variables and verify the thermodynamic inequalities for both the α‑model and the r‑model using the specified material constants for 304 stainless steel. Write the computed numeric values and boolean checks to `/app/outputs/limits.json` according to the output contract.

## Assets
No external assets are required. All material constants needed for the computation are listed in the workflow steps below.

## Workflow steps

### Step 1: Compute saturation limits and thermodynamic inequality checks
- Role: scored
- Action: Using the provided material constants for 304 stainless steel (κ₂=0.012 MPa⁻¹, a₂=0.012 MPa⁻¹ for α-model and a₂=0.01 MPa⁻¹ for r-model, c₂=10001 MPa², ρ₂=1.3), compute the isotropic size limit k^l = 1/κ₂, the backstress limit norm |α^l| = 1/a₂ (using the α-model a₂), the α-model distortional limit c^l = 1/(a₂ c₂) (using α-model a₂), and the r-model distortional limit norm |r^l| = 1/ρ₂. Evaluate the boolean conditions c₂ * a₂² >= 1 (using the α-model a₂) and ρ₂ > 1. Write the results to limits.json.
- Output file: `/app/outputs/limits.json`
- Format: json
- Contract: {"k_l": "<float: isotropic size limit 1/κ₂ (MPa)>", "alpha_l_norm": "<float: backstress limit norm 1/a₂ (α-model, MPa)>", "c_l": "<float: α-model distortional limit 1/(a₂ c₂) (MPa⁻¹)>", "r_l_norm": "<float: r-model distortional limit norm 1/ρ₂ (dimensionless)>", "c2_a2_sq_inequality": "<boolean: whether c₂ * a₂² >= 1 holds>", "rho2_greater_than_1": "<boolean: whether ρ₂ > 1 holds>"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/limits.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### limits.json
- path: `/app/outputs/limits.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed saturation limits and thermodynamic inequality checks for the directional distortional hardening models.
- schema:
  - `type`: object
  - `required`: `k_l`, `alpha_l_norm`, `c_l`, `r_l_norm`, `c2_a2_sq_inequality`, `rho2_greater_than_1`
  - `properties`:
    - `k_l`:
      - `type`: number
      - `description`: Isotropic size limit in MPa
    - `alpha_l_norm`:
      - `type`: number
      - `description`: Backstress limit norm in MPa (α‑model)
    - `c_l`:
      - `type`: number
      - `description`: α‑model distortional limit in MPa⁻¹
    - `r_l_norm`:
      - `type`: number
      - `description`: r‑model distortional limit norm (dimensionless)
    - `c2_a2_sq_inequality`:
      - `type`: boolean
      - `description`: Whether c₂ * a₂² ≥ 1 holds (α‑model)
    - `rho2_greater_than_1`:
      - `type`: boolean
      - `description`: Whether ρ₂ > 1 holds (r‑model)

Notes: The values are computed directly from the provided material constants using the analytic saturation formulas (1/κ₂, 1/a₂, 1/(a₂ c₂), 1/ρ₂). No external data or training is needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "limits.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "k_l",
          "alpha_l_norm",
          "c_l",
          "r_l_norm",
          "c2_a2_sq_inequality",
          "rho2_greater_than_1"
        ],
        "properties": {
          "k_l": {
            "type": "number",
            "description": "Isotropic size limit in MPa"
          },
          "alpha_l_norm": {
            "type": "number",
            "description": "Backstress limit norm in MPa (α‑model)"
          },
          "c_l": {
            "type": "number",
            "description": "α‑model distortional limit in MPa⁻¹"
          },
          "r_l_norm": {
            "type": "number",
            "description": "r‑model distortional limit norm (dimensionless)"
          },
          "c2_a2_sq_inequality": {
            "type": "boolean",
            "description": "Whether c₂ * a₂² ≥ 1 holds (α‑model)"
          },
          "rho2_greater_than_1": {
            "type": "boolean",
            "description": "Whether ρ₂ > 1 holds (r‑model)"
          }
        }
      },
      "description": "Computed saturation limits and thermodynamic inequality checks for the directional distortional hardening models."
    }
  ],
  "notes": "The values are computed directly from the provided material constants using the analytic saturation formulas (1/κ₂, 1/a₂, 1/(a₂ c₂), 1/ρ₂). No external data or training is needed."
}
```

## How you are scored
A hidden verifier independently recomputes each numeric limit from the same material constants using the analytic saturation formulas. Your values are compared to the reference within a small tolerance, and the boolean inequality checks must match the correct true/false. The final reward is a weighted combination of the per‑field correctness scores. Simply reporting numbers from the literature is insufficient; the verifier computes the answers in the same deterministic way and evaluates your output against them.
