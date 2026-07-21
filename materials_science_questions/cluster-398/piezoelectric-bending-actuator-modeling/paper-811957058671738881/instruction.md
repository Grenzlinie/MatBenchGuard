# Crack Intensity Factors in Functionally Graded Piezoelectric Materials

## Problem background
A Mode-I crack of length 2l is situated in an infinite transverse isotropic functionally graded piezoelectric material. The elastic, piezoelectric, and dielectric properties vary exponentially with the coordinate parallel to the crack (gradient parameter γ). The crack faces are modelled with a limited-permeable electric boundary condition, which accounts for the electric permittivity of the air inside the crack gap. This boundary condition couples the crack-opening displacement and the electric potential jump across the crack, making the electric field inside the gap non-trivial. The objective is to determine the near-tip singular fields, quantified by the stress intensity factor K_I and the electric displacement intensity factor K^D, for a specified combination of material gradient and electric permittivity ratio.

## Approach
The governing plane-strain/plane-stress equations for displacements and electric potential are derived using the exponential property gradation. The generalized Almansi's theorem is applied, and a Fourier transform with respect to the coordinate parallel to the crack is used to convert the system into a sixth-order ordinary differential equation in the transverse coordinate. The characteristic roots are obtained from the resulting cubic equation, and the general solution in the Fourier domain is expressed in terms of three unknown amplitude functions per half-plane. Imposing the crack-face boundary conditions yields two pairs of dual integral equations for the jumps of the displacements across the crack surfaces. The displacement jump f₂(x) is expanded in a series of Jacobi polynomials, and the dual integral equations are reduced to an infinite linear algebraic system via the Schmidt method. Truncating the series to N=10 terms gives a finite system that is solved for the expansion coefficients b_n. The stress and electric displacement intensity factors are then expressed as singular integrals involving these coefficients, from which K_I and K^D at the crack tips are computed. The material constants are given as c11=12.6×10¹⁰ N/m², c33=11.7×10¹⁰ N/m², c44=3.53×10¹⁰ N/m², c13=5.3×10¹⁰ N/m², e31=−6.5 C/m², e33=23.3 C/m², e15=17.0 C/m², ε11=151.0×10⁻¹⁰ C/Vm, ε33=130×10⁻¹⁰ C/Vm. The homogeneous limit (γ=0) recovers a closed-form solution that provides a built-in consistency check.

## Reproduction target
Compute the normalized stress intensity factor K_I/(τ₀√l) and normalized electric displacement intensity factor K^D/(τ₀√l) for a Mode-I limited-permeable crack under symmetric constant loading p₀. Two cases must be evaluated:

1. Graded material: γl = 0.4, electric permittivity ratio D₀/ε₀ = 4.0×10⁸, crack half-length l = 1.0.
2. Homogeneous material: γ = 0 (all other parameters unchanged).

The homogeneous case has a known closed-form analytical result that serves as an exact consistency check for the numerical implementation. Report the computed values in intensity_factors.json as described in the workflow steps.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement analytical kernel functions and asymptotic constants
- Role: process
- Action: Implement all derived analytical expressions from the paper in code: material coefficients (a, b, c, d, e, f, g, h, w1..w4), cofactors and α_i, the characteristic equation coefficients, the modal shape functions χ_i(s) and β_i(s), the kernel functions g1(s), g2(s), g3(s), g4(s), g5(s), and the asymptotic limits β1..β5. Produce a reusable Python module.
- Evidence: none

### Step 2: Solve dual integral equations via Schmidt method
- Role: process
- Action: For the graded case (γl=0.4, D₀/ε₀=4.0×10⁸, constant loading p₀) and for the homogeneous case (γ=0), construct the reduced equation, expand the displacement jump f₂(x) in Jacobi polynomials with 10 terms (N=10), and solve the resulting linear system using the Schmidt method to obtain the expansion coefficients b_n. Save the coefficients to expansion_coefficients.npz.
- Evidence: `/app/outputs/expansion_coefficients.npz`

### Step 3: Compute normalized intensity factors
- Role: scored (load-bearing)
- Action: Using the expansion coefficients from the previous step, compute the stress intensity factor K_I and electric displacement intensity factor K^D at the right crack tip using the formulas from the paper. Normalize by τ₀√l (τ₀ = p₀). Write the normalized values to /app/outputs/intensity_factors.json with the structure: { "homogeneous": {"K_I_normalized": <float>, "K_D_normalized": <float>}, "graded": {"gamma_l": 0.4, "D0_epsilon0": 4.0e8, "loading_type": "p0", "K_I_normalized": <float>, "K_D_normalized": <float>} }.
- Output file: `/app/outputs/intensity_factors.json`
- Format: json
- Contract: {
  "homogeneous": {
    "K_I_normalized": <float>,
    "K_D_normalized": <float>
  },
  "graded": {
    "gamma_l": 0.4,
    "D0_epsilon0": 4.0e8,
    "loading_type": "p0",
    "K_I_normalized": <float>,
    "K_D_normalized": <float>
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/intensity_factors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### intensity_factors.json
- path: `/app/outputs/intensity_factors.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Normalized stress intensity factor K_I/(τ₀√l) and electric displacement intensity factor K^D/(τ₀√l) for the homogeneous case (γ=0) and for the graded case (γl=0.4, D₀/ε₀=4.0×10⁸, symmetric constant loading p₀).
- schema:
  - `type`: object
  - `required`:
    - `homogeneous`:
      - `type`: object
      - `required`:
        - `K_I_normalized`: float
        - `K_D_normalized`: float
    - `graded`:
      - `type`: object
      - `required`:
        - `gamma_l`: 0.4
        - `D0_epsilon0`: 400000000.0
        - `loading_type`: p0
        - `K_I_normalized`: float
        - `K_D_normalized`: float

Notes: Checker independently recomputes the normalized intensity factors using a trusted reference implementation of the analytical-numerical method and compares the agent's reported values within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "intensity_factors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "homogeneous": {
            "type": "object",
            "required": {
              "K_I_normalized": "float",
              "K_D_normalized": "float"
            }
          },
          "graded": {
            "type": "object",
            "required": {
              "gamma_l": 0.4,
              "D0_epsilon0": 400000000.0,
              "loading_type": "p0",
              "K_I_normalized": "float",
              "K_D_normalized": "float"
            }
          }
        }
      },
      "description": "Normalized stress intensity factor K_I/(τ₀√l) and electric displacement intensity factor K^D/(τ₀√l) for the homogeneous case (γ=0) and for the graded case (γl=0.4, D₀/ε₀=4.0×10⁸, symmetric constant loading p₀)."
    }
  ],
  "notes": "Checker independently recomputes the normalized intensity factors using a trusted reference implementation of the analytical-numerical method and compares the agent's reported values within appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently recomputes the normalized intensity factors using a trusted reference implementation of the same analytical-numerical method. It compares your reported values to its recomputed numbers. For the homogeneous case, the verifier checks that your K_I_normalized satisfies the closed-form solution to within a tight absolute tolerance. For the graded case, your values are compared against the verifier's recomputed results within an appropriate relative tolerance. The verifier does not accept numbers reported without underlying computation; it evaluates your entire pipeline. The final intensity_factors.json carries the highest weight, but all workflow steps must be correctly executed to produce it.
