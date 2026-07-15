# Crack-Inclusion Thermal Stress Intensity Factor Calculation

## Problem background
Reinforced composite materials often contain inclusions with different thermal expansion coefficients than the surrounding matrix. Under temperature changes, mismatched expansions generate thermal stresses that can initiate and drive cracks, potentially leading to failure. Predicting the stress intensity factors (SIFs) for cracks interacting with inclusions is essential for assessing the structural integrity of such materials. This task focuses on computing the normalized mode I and mode II SIFs for a single crack near a circular inclusion in a finite square plate subjected to a uniform temperature change.

## Approach
The numerical approach combines two techniques. First, Eshelby's equivalent inclusion method is applied to an infinite plate containing the inclusion, deriving the eigenstrains that represent the thermal mismatch. Solving the equivalence condition at the inclusion center yields the eigenstrains, from which the thermal stress field along the crack line is calculated. Second, the crack and the external boundary of the finite plate are modeled as continuous distributions of edge dislocations in an infinite medium. Traction-free conditions on the crack and boundary lead to a system of singular integral equations with Cauchy kernels. These equations are normalized and discretized using Gauss–Chebyshev quadrature, resulting in a linear algebraic system for dislocation density functions. Solving this system provides the densities at the crack tips, from which the mode I and mode II stress intensity factors are obtained. The entire computation is implemented in Python using NumPy and SciPy.

## Reproduction target
Implement the method for a specific configuration: a square plate with side length W = H = 10R, containing a single circular inclusion of radius R and a single horizontal crack of half-length a = R. The inclusion center is at the plate center; the crack is centered horizontally, with its center at a distance D = 3R from the inclusion center, and the line connecting the inclusion center to the crack center is horizontal (φ = 0). The matrix and inclusion have Poisson's ratio ν = 0.3, the shear modulus ratio μ₁/μ = 20, and the difference in thermal expansion coefficients is (α₁ − α). The plate is under a uniform temperature change ΔT and plane strain conditions. Compute the normalized stress intensity factors K / (μ·(α₁−α)·ΔT·√(πa)) for both mode I and mode II at the left crack tip (A) and the right crack tip (B). Output the four dimensionless values in a JSON file with the structure: {"tip_A": {"mode_I": number, "mode_II": number}, "tip_B": {"mode_I": number, "mode_II": number}}.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Thermal stress field via equivalent inclusion method
- Role: process
- Action: Using Eshelby's equivalent inclusion method, compute the thermal stress distribution on the crack lines for one circular inclusion in an infinite plate. Use the given geometry (inclusion radius R, crack half-length a = R, horizontal crack at distance D=3R from inclusion center), material properties (shear modulus ratio μ1/μ = 20, Poisson's ratio ν = 0.3, thermal expansion mismatch α1-α), and a uniform temperature change ΔT. Derive the eigenstrains by solving the linear system from the equivalence condition at the inclusion center, then compute the thermal stresses σ_y and σ_xy at collocation points along the crack line that will be used in the next step.
- Evidence: `/app/outputs/thermal_stress.npy`

### Step 2: Solve singular integral equations for dislocation densities
- Role: process
- Action: Model the crack and the square plate boundary (width W=height H=10R) as continuous distributions of edge dislocations. Formulate the singular integral equations with Cauchy kernels based on traction-free boundary conditions for the crack and the external boundary. Normalize the equations, apply Gauss-Chebyshev quadrature with sufficient points to achieve convergence, and solve the resulting linear algebraic system to obtain dislocation density functions along the crack and boundary.
- Evidence: `/app/outputs/dislocation_densities.npy`

### Step 3: Compute normalized stress intensity factors
- Role: scored (load-bearing)
- Action: From the dislocation density functions at the crack tips, compute mode I and mode II stress intensity factors using the standard relation K_I(±1) = ±√(πa) (2μ/(κ+1)) φ_y(±1) and K_II(±1) = ±√(πa) (2μ/(κ+1)) φ_x(±1). Normalize by μ · (α1-α) · ΔT · √(πa) to obtain the dimensionless factors. Output the normalized mode I and mode II SIFs for the left tip (A) and right tip (B) in JSON format.
- Output file: `/app/outputs/sif_results.json`
- Format: json
- Contract: {"tip_A": {"mode_I": "number", "mode_II": "number"}, "tip_B": {"mode_I": "number", "mode_II": "number"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sif_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sif_results.json
- path: `/app/outputs/sif_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The normalized mode I and II stress intensity factors for the two crack tips under the specified configuration.
- schema:
  - `type`: object
  - `required`: `tip_A`, `tip_B`
  - `properties`:
    - `tip_A`:
      - `type`: object
      - `required`: `mode_I`, `mode_II`
      - `properties`:
        - `mode_I`:
          - `type`: number
        - `mode_II`:
          - `type`: number
    - `tip_B`:
      - `type`: object
      - `required`: `mode_I`, `mode_II`
      - `properties`:
        - `mode_I`:
          - `type`: number
        - `mode_II`:
          - `type`: number

Notes: The checker reads the JSON and compares each of the four values to hidden gold values extracted from the paper's reported results for the same configuration (Fig. 12, μ1/μ = 20, a = R, D = 3R, φ = 0, W = H = 10R), using an absolute tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sif_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "tip_A",
          "tip_B"
        ],
        "properties": {
          "tip_A": {
            "type": "object",
            "required": [
              "mode_I",
              "mode_II"
            ],
            "properties": {
              "mode_I": {
                "type": "number"
              },
              "mode_II": {
                "type": "number"
              }
            }
          },
          "tip_B": {
            "type": "object",
            "required": [
              "mode_I",
              "mode_II"
            ],
            "properties": {
              "mode_I": {
                "type": "number"
              },
              "mode_II": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "The normalized mode I and II stress intensity factors for the two crack tips under the specified configuration."
    }
  ],
  "notes": "The checker reads the JSON and compares each of the four values to hidden gold values extracted from the paper's reported results for the same configuration (Fig. 12, μ1/μ = 20, a = R, D = 3R, φ = 0, W = H = 10R), using an absolute tolerance."
}
```

## How you are scored
A hidden verifier reads your sif_results.json and compares each of the four normalized SIF values (mode I and mode II for tips A and B) against hidden reference values. The comparison uses an absolute tolerance. If all four values fall within the tolerance, the reward is 1.0; otherwise it is 0.0. The intermediate process artifacts (thermal_stress.npy and dislocation_densities.npy) are recorded as evidence but not directly scored. Only the final sif_results.json carries the reward.
