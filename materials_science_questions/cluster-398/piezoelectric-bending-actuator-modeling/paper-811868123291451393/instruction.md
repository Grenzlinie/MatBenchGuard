# End-effect decay rates for transversely isotropic piezoelectric strips

## Problem background
When a transversely isotropic piezoelectric semi‑infinite strip is loaded at its end, the induced stresses decay with distance away from the end. The strip is traction‑free on its surfaces, and the electrical boundary condition is either charge‑free or electric‑potential‑free. The rate of stress decay is captured by a dimensionless decay rate γ, from which a decay length can be derived. The objective is to compute the decay rates and decay lengths for four common piezoelectric materials (PZT‑5H, PZT‑5, PZT‑4, Ceramic‑B) for both symmetric and antisymmetric deformation modes. These quantities determine how far end effects penetrate into the strip.

## Approach
The Saint‑Venant end effect for a transversely isotropic piezoelectric semi‑infinite strip under plane deformation is governed by a system that decouples into symmetric and antisymmetric modes. The computation proceeds as follows.

### 1. Material constants conversion
The input material constants are the elastic compliances (s₁₁, s₁₂, s₁₃, s₃₃, s₄₄), piezoelectric strain constants (d₃₁, d₃₃, d₁₅), and dielectric permittivities at constant stress (ε₁₁, ε₃₃). From these, compute the stiffness matrix at constant electric field C by inverting the 5×5 compliance matrix:

S = [[s₁₁, s₁₂, s₁₃, 0, 0],
     [s₁₂, s₁₁, s₁₃, 0, 0],
     [s₁₃, s₁₃, s₃₃, 0, 0],
     [0, 0, 0, s₄₄, 0],
     [0, 0, 0, 0, s₆₆ ]]  with s₆₆ = 2(s₁₁ − s₁₂).

Compute C = S⁻¹. The piezoelectric stress constants e are obtained as eₖᵢ = dₖⱼ Cⱼᵢ (matrix multiply with appropriate index mapping). The clamped dielectric constants εⁱⱼ^S are εⁱⱼ^S = εⁱⱼ − dₖⱼ eₖⱼ.

Then define the coefficients that appear in the 6th‑order characteristic polynomial as:

a₁₁ = C₁₁,  a₁₂ = C₁₃,  a₂₂ = C₃₃,  a₃₃ = C₄₄,
b₂₁ = e₃₁,  b₂₂ = e₃₃,  b₁₃ = e₁₅,
δ₁₁ = εⁱ¹₁^S,  δ₂₂ = εⁱ³₃³^S.

### 2. Characteristic polynomial and root parameters
For each material, construct the 6th‑order polynomial:

a₁₁ δ₁₁ q⁶ + [a₁₁ δ₂₂ + (2a₁₂ + a₃₃) δ₁₁ + (b₂₁ + b₁₃)²] q⁴
+ [a₂₂ δ₁₁ + (2a₁₂ + a₃₃) δ₂₂ + 2 b₂₂ (b₂₁ + b₁₃)] q² + (a₂₂ δ₂₂ + b₂₂²) = 0.

Solve numerically for its six complex roots. Identify the three roots with positive imaginary parts; they occur in complex‑conjugate pairs. Label them as:

q₁ = i β₁,  q₂ = −i β₁  (purely imaginary),
q₃ = α₂ + i β₂,  q₄ = α₂ − i β₂,
q₅ = −α₂ + i β₂,  q₆ = −α₂ − i β₂.

The real parameters β₁, α₂, β₂ are extracted from these root patterns.

### 3. Auxiliary constants
From β₁, α₂, β₂ and the material constants compute the following auxiliary quantities.

First evaluate B₁…B₄ and A₁…A₅ (cf. Eq. A.16):

B₁ = δ₁₁ a₁₁,
B₂ = δ₁₁ (2a₁₂ + a₃₃) + (b₂₁ + b₁₃)²,
B₃ = δ₁₁ a₂₂ + b₂₂ (b₂₁ + b₁₃),
B₄ = δ₂₂ (b₂₁ + b₁₃) − δ₁₁ b₂₂.

A₁ = B₁ β₁⁴ − B₂ β₁² + B₃,
A₂ = B₁ (α₂⁴ − 6α₂² β₂² + β₂⁴) + B₂ (α₂² − β₂²) + B₃,
A₃ = 2α₂ β₂ [2B₁ (α₂² − β₂²) + B₂],
A₄ = B₁ (α₂⁴ − 10α₂² β₂² + 5β₂⁴) + B₂ (α₂² − 3β₂²) + B₃,
A₅ = B₁ (5α₂⁴ − 10α₂² β₂² + β₂⁴) + B₂ (3α₂² − β₂²) + B₃.

The reduced parameters Ā_i are Ā_i = A_i / B₄  (i = 1,…,5).

The constants gᵢ (Eq. A.14) are:

g₁ = β₁,  g₂ = α₂,  g₃ = β₂,
g₄ = K₁,  g₅ = K₂,  g₆ = K₃,
g₇ = K₄,  g₈ = K₅,  g₉ = K₆,
g₁₀ = Ā₁,  g₁₁ = Ā₂,  g₁₂ = Ā₃,
g₁₃ = K₇,  g₁₄ = K₈,  g₁₅ = K₉,

where K₁…K₉ (Eq. A.15) are:

K₁ = b₂₁ Ā₁ + (−a₁₁ β₁² + a₁₂),
K₂ = b₂₁ Ā₂ + a₁₁ (α₂² − β₂²) + a₁₂,
K₃ = b₂₁ Ā₃ + 2 a₁₁ α₂ β₂,
K₄ = [(b₁₃+b₂₁) Ā₁ + (−a₁₁ β₁² + a₁₂+a₃₃)] β₁,
K₅ = [(b₁₃+b₂₁) Ā₄ + a₁₁ (α₂² − 3β₂² + a₁₂+a₃₃)] α₂,
K₆ = [(b₁₃+b₂₁) Ā₅ + a₁₁ (3α₂² − β₂² + a₁₂+a₃₃)] β₂,
K₇ = (δ₁₁ Ā₁ − b₁₃) β₁,
K₈ = (δ₁₁ Ā₄ − b₁₃) α₂,
K₉ = (δ₁₁ Ā₅ − b₁₃) β₂.

(For K₅ and K₆ the forms above correct a typographical error present in some printed versions; the verifier uses these corrected expressions.)

Finally, compute the parameters that appear in the characteristic equations:

For Case A:  ᵱ̄₁ = α₂ (Ā₁ − Ā₂) − β₂ Ā₃,   ᵱ̄₂ = β₂ (Ā₁ − Ā₂) + α₂ Ā₃.
For Case B:  ᵱ̄₃ = K₇ α₂ − K₈ β₁,   ᵱ̄₄ = −K₇ β₂ + K₉ β₁,   ᵱ̄₅ = K₉ α₂ − K₈ β₂.

### 4. Characteristic equations for the decay rate γ
For each combination (material, boundary case, symmetry mode) the dimensionless decay rate γ is the smallest positive real root of the corresponding equation:

Case A (traction‑free, charge‑free):
Symmetric (F_AS):
β₁ Ā₃ sin(β₁ γ)[cos(2β₂ γ) + cosh(2α₂ γ)] + cos(β₁ γ)[ᵱ̄₁ sin(2β₂ γ) + ᵱ̄₂ sinh(2α₂ γ)] = 0.   (6)

Antisymmetric (F_AA):
β₁ Ā₃ cos(β₁ γ)[cos(2β₂ γ) − cosh(2α₂ γ)] + sin(β₁ γ)[−ᵱ̄₁ sin(2β₂ γ) + ᵱ̄₂ sinh(2α₂ γ)] = 0.  (7)

Case B (traction‑free, electric‑potential‑free):
Symmetric (F_BS):
ᵱ̄₅ cos(β₁ γ)[cos(2β₂ γ) − cosh(2α₂ γ)] + sin(β₁ γ)[ᵱ̄₃ sin(2β₂ γ) − ᵱ̄₄ sinh(2α₂ γ)] = 0.   (8)

Antisymmetric (F_BA):
ᵱ̄₅ sin(β₁ γ)[cos(2β₂ γ) + cosh(2α₂ γ)] − cos(β₁ γ)[ᵱ̄₃ sin(2β₂ γ) + ᵱ̄₄ sinh(2α₂ γ)] = 0.  (9)

### 5. Numerical root‑finding and decay length
For each of the 16 combinations, find the smallest positive real root γ of the appropriate transcendental equation using a robust root‑finding algorithm. The dimensionless decay length is then L/(2c) = ln(100)/(2γ). Report the values rounded to at least six significant digits.

## Reproduction target
For all 16 combinations (4 materials × 2 boundary cases × 2 symmetry modes), numerically solve the corresponding characteristic equation to find the smallest positive real root γ. Compute the associated decay length L/(2c) = ln(100) / (2γ). Record the results in a JSON file (`decay_results.json`) with the following keys for each entry: `material` (string), `boundary_case` (string, either `"A"` or `"B"`), `symmetry_mode` (string, either `"symmetric"` or `"antisymmetric"`), `decay_rate_real` (float), `decay_length_over_2c` (float).

## Assets

- Material constants for PZT-5H, PZT-5, PZT-4, Ceramic-B: 10.1016/S0020-7683(99)00034-7

## Workflow steps

### Step 1: Acquire material constants
- Role: process
- Action: Retrieve the elastic, piezoelectric, and dielectric constants for the four transversely isotropic piezoelectric materials PZT-5H, PZT-5, PZT-4, and Ceramic-B from Ruan et al. (2000).
- Evidence: `/app/outputs/constants_log.txt`

### Step 2: Compute root parameters and auxiliary constants
- Role: process
- Action: For each material, construct the 6th-order characteristic polynomial that arises from the plane-deformation Saint-Venant problem for a transversely isotropic piezoelectric strip. Solve for its complex roots and extract the real parameters β₁, α₂, β₂. Then compute the auxiliary constants gᵢ (i=1…15), Kᵢ (i=1…9), Āᵢ (i=1…5), and ᵱ̄ᵢ (i=1…5) using the definitions that express them in terms of the material constants and the root parameters.
- Evidence: `/app/outputs/derived_params.json`

### Step 3: Compute decay rates and decay lengths
- Role: scored (load-bearing)
- Action: For each of the 16 combinations (material, boundary case A/B, symmetry mode symmetric/antisymmetric), form the appropriate characteristic equation: for Case A (traction-free, charge-free) use the symmetric F_AS and antisymmetric F_AA; for Case B (traction-free, electric-potential-free) use the symmetric F_BS and antisymmetric F_BA. Numerically find the smallest positive real root γ of each equation. Compute the dimensionless decay length L/(2c) = ln(100) / (2γ). Record all results in a JSON file.
- Output file: `/app/outputs/decay_results.json`
- Format: json
- Contract: JSON array of objects with keys: material (string), boundary_case (string 'A' or 'B'), symmetry_mode (string 'symmetric' or 'antisymmetric'), decay_rate_real (float, dimensionless), decay_length_over_2c (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/decay_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### decay_results.json
- path: `/app/outputs/decay_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Decay rates and decay lengths for the 16 combinations; compared against predetermined gold values.
- schema:
  - `type`: array
  - `minItems`: 16
  - `maxItems`: 16
  - `items`:
    - `type`: object
    - `required`: `material`, `boundary_case`, `symmetry_mode`, `decay_rate_real`, `decay_length_over_2c`
    - `properties`:
      - `material`:
        - `type`: string
        - `enum`: `PZT-5H`, `PZT-5`, `PZT-4`, `Ceramic-B`
      - `boundary_case`:
        - `type`: string
        - `enum`: `A`, `B`
      - `symmetry_mode`:
        - `type`: string
        - `enum`: `symmetric`, `antisymmetric`
      - `decay_rate_real`:
        - `type`: number
        - `description`: dimensionless decay rate γ
      - `decay_length_over_2c`:
        - `type`: number
        - `description`: decay length in units of 2c

Notes: The checker compares the agent's reported decay_rate_real and decay_length_over_2c to fixed reference values (not recomputed). Tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "decay_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "minItems": 16,
        "maxItems": 16,
        "items": {
          "type": "object",
          "required": [
            "material",
            "boundary_case",
            "symmetry_mode",
            "decay_rate_real",
            "decay_length_over_2c"
          ],
          "properties": {
            "material": {
              "type": "string",
              "enum": [
                "PZT-5H",
                "PZT-5",
                "PZT-4",
                "Ceramic-B"
              ]
            },
            "boundary_case": {
              "type": "string",
              "enum": [
                "A",
                "B"
              ]
            },
            "symmetry_mode": {
              "type": "string",
              "enum": [
                "symmetric",
                "antisymmetric"
              ]
            },
            "decay_rate_real": {
              "type": "number",
              "description": "dimensionless decay rate γ"
            },
            "decay_length_over_2c": {
              "type": "number",
              "description": "decay length in units of 2c"
            }
          }
        }
      },
      "description": "Decay rates and decay lengths for the 16 combinations; compared against predetermined gold values."
    }
  ],
  "notes": "The checker compares the agent's reported decay_rate_real and decay_length_over_2c to fixed reference values (not recomputed). Tolerances are hidden."
}
```

## How you are scored
A hidden verifier, using the same material constants and characteristic equations, will independently recompute the decay rates and decay lengths. Your submitted values from `decay_results.json` will be compared against the verifier’s recomputed reference. For each combination, the score is based on how closely your reported decay rate and decay length match that reference; a solution that reproduces the values within an appropriate tolerance earns full credit, and the score decreases monotonically as the deviations grow. The verifier also checks that the output file is correctly structured (all required fields present, correct file format). In addition to the scored decay results, the verifier may inspect the intermediate evidence files to confirm that the computation pipeline was executed, but the primary scoring weight is on the final decay quantities.
