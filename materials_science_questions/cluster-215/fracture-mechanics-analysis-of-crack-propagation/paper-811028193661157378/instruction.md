# Stress Singularity Orders for Anisotropic Bimaterial Interface Crack

## Problem background
For a crack in a gamma TiAl (face-centered tetragonal L1₀) / beta Ti-V (body-centered cubic) bicrystal where the crack tip touches the dissimilar-material interface, the near-tip stress field under Mode I loading consists of two independent singular terms. Each term has its own stress singularity order, denoted λ_A and λ_B, both lying in the interval (0, 1). These orders govern the asymptotic behavior of stresses and displacements at the crack tip. Analytical expressions for such anisotropic bimaterial interface cracks are unavailable, so the singularity orders must be determined numerically. This task computes the two admissible singularity exponents for the crack configuration described, using the elastic constants of the two phases.

## Approach
A sector-element finite element method (Yamada and Okumura) is employed. The angular region around the crack tip is discretized into quadratic sector elements whose shape captures the singular radial behavior through the mapping r = r₀ ((1+ξ)/2)^{1/λ}. Plane-strain material stiffness matrices for gamma TiAl (orthotropic) and beta Ti-V (cubic) are constructed from the following elastic constants (all in 10^11 N/m^2): gamma TiAl: C11=2.28, C12=1.02, C13=1.36, C33=2.78, C44=1.4, C66=0.776; beta Ti-V: C11=1.121, C12=0.771, C44=0.885. For each element, the principle of virtual work yields element matrices [kₐ], [kb], [kc], [k_sa], [k_sb] via numerical integration. These are assembled into global matrices [A], [B], [C]. The resulting quadratic eigenvalue problem (λ²[A] + λ[B] + [C]){U} = 0 is transformed into the standard eigenvalue problem [S]{V, U}^T = λ{V, U}^T. Solving this eigenproblem yields eigenvalues λ; the admissible ones are those in the open interval (0, 1). Two such values are found, corresponding to the two independent singular modes.

## Reproduction target
Implement the sector-element finite element method described above and numerically compute the two admissible stress singularity exponents for a crack tip exactly at the gamma TiAl / beta Ti-V interface. Report the computed exponents as a JSON file containing the fields `lambda_A` and `lambda_B` (both floats). The target is to produce these two numbers from the given material constants and the prescribed numerical procedure.

## Assets

- python3 with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compute singularity orders
- Role: scored (load-bearing)
- Action: Implement the sector-element finite element method for the near-tip region: (a) construct plane-strain material stiffness matrices for gamma TiAl (orthotropic) and beta Ti-V (cubic) using the given elastic constants; (b) discretize the angular domain around the crack tip into quadratic sector elements with the singular mapping; (c) numerically integrate over each element to obtain the element matrices; (d) assemble the global matrices [A], [B], [C]; (e) transform the quadratic eigenvalue problem (λ²[A] + λ[B] + [C]){U} = 0 into the standard eigenproblem [S]{V,U}^T = λ{V,U}^T; (f) solve the eigenvalue problem using scipy; (g) select eigenvalues λ satisfying 0 < λ < 1. Output the two admissible values as lambda_A and lambda_B in /app/outputs/singularity_orders.json.
- Output file: `/app/outputs/singularity_orders.json`
- Format: json
- Contract: A JSON object with keys lambda_A (float) and lambda_B (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/singularity_orders.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### singularity_orders.json
- path: `/app/outputs/singularity_orders.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Admissible stress singularity exponents for a crack touching the gamma/beta interface under Mode I remote loading.
- schema:
  - `type`: object
  - `properties`:
    - `lambda_A`:
      - `type`: number
      - `description`: Admissible singularity order, Mode A
    - `lambda_B`:
      - `type`: number
      - `description`: Admissible singularity order, Mode B
  - `required`: `lambda_A`, `lambda_B`

Notes: The checker compares the submitted lambda_A and lambda_B to the paper-reported values using a relative tolerance. Only the two eigenvalues in the open interval (0,1) are considered.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "singularity_orders.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "lambda_A": {
            "type": "number",
            "description": "Admissible singularity order, Mode A"
          },
          "lambda_B": {
            "type": "number",
            "description": "Admissible singularity order, Mode B"
          }
        },
        "required": [
          "lambda_A",
          "lambda_B"
        ]
      },
      "description": "Admissible stress singularity exponents for a crack touching the gamma/beta interface under Mode I remote loading."
    }
  ],
  "notes": "The checker compares the submitted lambda_A and lambda_B to the paper-reported values using a relative tolerance. Only the two eigenvalues in the open interval (0,1) are considered."
}
```

## How you are scored
A hidden verifier reads your `singularity_orders.json`, extracts the two exponents, and compares them to the expected reference values (the paper's reported results for the same setup). The evaluation uses a relative tolerance: both `lambda_A` and `lambda_B` must lie within the tolerance band around the hidden targets. If both are within tolerance, full credit is awarded; otherwise, credit is reduced based on the deviation. No other outputs are scored. Simply printing the expected numbers is not sufficient; you must run the finite element solver to obtain the values.
