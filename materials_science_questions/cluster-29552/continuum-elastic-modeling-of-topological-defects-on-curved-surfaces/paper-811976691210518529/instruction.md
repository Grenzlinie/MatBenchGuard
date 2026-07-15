# Curvature Energy Calculation of Smectic Focal Domains

## Problem background
Smectic liquid crystals exhibit focal conic defects, where layers fold around an ellipse and hyperbola (or parabolae) while maintaining constant thickness, forming surfaces known as Dupin cyclides. The elastic energy of these curved layers is dominated by curvature energy, which can be expressed in terms of the mean curvature. This task focuses on computing and comparing the curvature energy of two types of focal domains: normal focal domains (built on an ellipse and a hyperbola) and parabolic focal domains (built on two intersecting parabolae). The main quantity of interest is the total curvature energy integrated over the layer region, which depends on geometric parameters such as the semi-major axis a and eccentricity e for the normal domain, and the focal length f and confining cylinder radius R for the parabolic domain. The aim is to compute these energies and determine which configuration is energetically favored under a given set of sizes.

## Approach
The method is based on the analytical theory of surfaces. For a Dupin cyclide, the principal curvatures σ₁, σ₂ and the metric coefficients A, B are derived from the geometry of the conics. The curvature energy per unit area and per unit length along the layer normal is (1/2) K₁ (σ₁+σ₂)², where K₁ is the splay elastic constant (set to 1 as a scaling factor). The total energy W is obtained by integrating this density over the volume of the domain: W = (1/2) K₁ ∫ (σ₁+σ₂)² A B du dv dr. For the normal focal domain, the leading-order large-size limit yields the analytic formula W_n = 4π K₁ a (1-e²) K(e²) ln(a/r_c). For the parabolic domain, the analogous limit gives W_p = (π/8) K₁ f (R/f)⁴ ln(R²/(4 f r_c)). These formulas are evaluated directly with the specified parameters; the computed energies (W_n and W_p) are then compared.

## Reproduction target
For the given parameters — normal domain: semi-major axis a = 1, eccentricity e = 0.5, core radius r_c = 0.01; parabolic domain: focal length f = 1, cylinder radius R = 2, core radius r_c = 0.01, with K₁ = 1 — compute the curvature energies W_n (normal focal domain) and W_p (parabolic focal domain of the first species). Produce a JSON file containing these two energy values (in units of K₁·length) and a boolean parabolic_favored that is true if W_p < W_n, else false.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute focal domain curvature energies
- Role: scored (load-bearing)
- Action: Compute the curvature energies using the paper's leading-order large-size analytic formulas. For the normal focal domain of the first species, use: W_n = 4π K1 a (1-e²) K(e²) ln(a/r_c), where K(e²) is the complete elliptic integral of the first kind. For the parabolic focal domain of the first species, use: W_p = (π/8) K1 f (R/f)⁴ ln(R²/(4 f r_c)). Set K1 = 1. Evaluate these expressions with the parameters: normal domain: a=1, e=0.5, r_c=0.01; parabolic domain: f=1, R=2, r_c=0.01. Determine whether the parabolic domain is energetically favoured (W_p < W_n). Write the computed numeric values of W_n, W_p and the boolean parabolic_favored to focal_domain_energies.json.
- Output file: `/app/outputs/focal_domain_energies.json`
- Format: json
- Contract: type=object; required=['W_n', 'W_p', 'parabolic_favored']; fields={'W_n': {'type': 'number', 'units': 'K1·length (K1=1)'}, 'W_p': {'type': 'number', 'units': 'K1·length (K1=1)'}, 'parabolic_favored': {'type': 'boolean'}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/focal_domain_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### focal_domain_energies.json
- path: `/app/outputs/focal_domain_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed curvature energies for normal and parabolic focal domains of the first species, with energy scaled by K1=1. The boolean indicates if the parabolic domain is energetically favoured (W_p < W_n). Tolerance: relative 0.01 for energies, exact for boolean.
- schema:
  - `type`: object
  - `required`: `W_n`, `W_p`, `parabolic_favored`
  - `fields`:
    - `W_n`:
      - `type`: number
      - `units`: K1·length (K1=1)
    - `W_p`:
      - `type`: number
      - `units`: K1·length (K1=1)
    - `parabolic_favored`:
      - `type`: boolean

Notes: Energy values are in units of K1·length. The elastic constant K1 is set to 1 as scaling factor. The hidden checker compares the submitted values to reference values derived from the paper’s analytic approximations with a relative tolerance of 0.01 for energies and exact match for the boolean.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "focal_domain_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "W_n",
          "W_p",
          "parabolic_favored"
        ],
        "fields": {
          "W_n": {
            "type": "number",
            "units": "K1·length (K1=1)"
          },
          "W_p": {
            "type": "number",
            "units": "K1·length (K1=1)"
          },
          "parabolic_favored": {
            "type": "boolean"
          }
        }
      },
      "description": "Computed curvature energies for normal and parabolic focal domains of the first species, with energy scaled by K1=1. The boolean indicates if the parabolic domain is energetically favoured (W_p < W_n). Tolerance: relative 0.01 for energies, exact for boolean."
    }
  ],
  "notes": "Energy values are in units of K1·length. The elastic constant K1 is set to 1 as scaling factor. The hidden checker compares the submitted values to reference values derived from the paper’s analytic approximations with a relative tolerance of 0.01 for energies and exact match for the boolean."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. The verifier independently computes reference values for W_n and W_p using the same geometric formulas and compares your submitted numbers to these references. The energy values must be within a specified relative tolerance. The boolean flag is checked for strict correctness. The final reward is a score between 0 and 1 reflecting the accuracy of your computed energies and the flag. Note: reporting the paper's numbers without genuine computation will not pass because the hidden verifier uses its own derived values based on the same public formulas.
