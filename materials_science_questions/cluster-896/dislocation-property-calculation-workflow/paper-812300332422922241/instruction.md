# Dislocation Domain Nucleation Computation

## Problem background
In ferroelectric perovskite crystals, dislocations interact with the surrounding domain structure. It is hypothesised that a dislocation can lower its strain energy by nucleating a suitable ferroelectric domain around it. This task computes, for a screw dislocation in a cubic perovskite, which type of domain (60°, 90°, or 180°) is favoured and determines the resulting domain width, using the continuum‑elasticity concept of a relieving displacement.

## Approach
The analysis models a screw dislocation along the axis of a cylindrical region of radius r1. The dislocation produces a shear stress field that varies as 1/r. A hypothetical relieving displacement rotation generates an opposing shear stress field varying linearly with r. By requiring that the torsional couples balance over the cylindrical shell (from core radius r0 to outer radius r1), the constant A characterising the relieving displacement is determined. The radial distance r' at which the two stress fields cancel in magnitude is then computed. Using the known crystallographic relations (the dislocation lies along <111> and domain walls form on planes at 45° to the radial direction), r' is converted to the domain half‑width R. Finally, the deformation of the pseudocubic (001) plane under the relieving displacement is compared with the deformation required by the spontaneous strain of a ferroelectric domain; this deformation‑compatibility analysis determines which type of domain (60°, 90°, or 180°) is favoured. In orthorhombic KNbO₃, the pseudocubic a_m axis is elongated relative to c_m; a 60° domain has its polar axis along a_m, a 90° domain along c_m, and a 180° domain involves no length change.

## Reproduction target
Given the material parameters μ = 1.0×10^10 Pa, b = 4.0×10^-10 m, r0 = 1.0×10^-9 m, r1 = 5.0×10^-6 m, implement the derivation and output a JSON file containing the relieving displacement constant A (in m^-2), the stress‑cancellation distance r' (in m), the domain half‑width R (in m), and the favoured domain type (as a string).

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Derive and Compute Dislocation Domain Properties
- Role: scored (load-bearing)
- Action: Given the input parameters (shear modulus μ = 1.0×10^10 Pa, Burgers vector b = 4.0×10^-10 m, core radius r0 = 1.0×10^-9 m, outer cylinder radius r1 = 5.0×10^-6 m), implement the analytical derivation: compute the screw dislocation stress field σ_{3θ} = μb/(2πr), the relieving displacement stress field σ'_{3θ} = -μAr, determine constant A by equating the torsional couples over the cylindrical shell (r0 to r1), find the radial distance r' where |σ_{3θ}| = |σ'_{3θ}|, convert r' to domain half-width R = r'/cos45°, and determine the favoured domain type by analyzing deformation compatibility with spontaneous strain. Write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: 'A_constant' (number), 'r_prime' (number), 'domain_half_width_R' (number), 'favored_domain_type' (string).
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
- target_policy: reference_match
- description: Computed dislocation domain properties: relieving displacement constant A, stress cancellation distance r', domain half-width R, and favoured domain type.
- schema:
  - `type`: object
  - `required`:
    - `A_constant`: number (float, m^-2)
    - `r_prime`: number (float, m)
    - `domain_half_width_R`: number (float, m)
    - `favored_domain_type`: string

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "A_constant": "number (float, m^-2)",
          "r_prime": "number (float, m)",
          "domain_half_width_R": "number (float, m)",
          "favored_domain_type": "string"
        }
      },
      "description": "Computed dislocation domain properties: relieving displacement constant A, stress cancellation distance r', domain half-width R, and favoured domain type."
    }
  ],
  "notes": ""
}
```

## How you are scored
After you submit, a hidden verifier will independently recompute the expected values of A, r', and R from the same input parameters and compare them to your submitted numbers. Your computed favoured domain type will be compared by exact string match. The final score is a weighted combination of these comparisons; merely stating the paper's numbers without correct computation will not achieve a high score.
