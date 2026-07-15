# Slow Dislocation Solute Atmosphere Force Factor Calculation

## Problem background
Dislocations in crystals interact with solute atoms through long-range stress fields. Around a stationary edge dislocation, solute atoms form a symmetric Maxwell–Boltzmann atmosphere. When the dislocation moves at a finite speed, the atmosphere becomes asymmetric, generating a net force on the dislocation that opposes its motion. This viscous drag depends on the dislocation speed and the solute diffusion kinetics. The key physical quantity is the dimensionless perturbation force factor, which normalises the drag force and characterises the effect. Computing this factor for a slow dislocation reveals the strength of the solute pinning and the conditions for unstable breakaway.

## Approach
The problem is treated in a coordinate frame moving with a positive edge dislocation. The steady-state concentration of solute atoms satisfies a convective-diffusion equation that includes drift from the dislocation stress field, Fickian diffusion, and the imposed dislocation speed. This equation is transformed into a separable form by introducing a pseudo‑equilibrium function and a reduced function ψ. Separation of variables leads to an angular Mathieu equation and a radial hyperbolic Mathieu equation. For a slow dislocation (small speed parameter q), only the first angular modes (ce₁, se₁) and the corresponding radial functions (Fek₁*, Gek₁*) are needed in the series solution for ψ. The concentration field c(r,θ) is then reconstructed from ψ and the pseudo‑equilibrium factor. Finally, the dimensionless perturbation force factor is obtained by numerically integrating the force density over a grid of polar coordinates (ρ from 0.1 to 10, θ from 0 to 2π) according to the perturbation force integral.

## Reproduction target
For a slowly moving positive edge dislocation with speed parameter q = 0.04, implement the approximate concentration solution using Mathieu functions as described. Define a polar grid with radial coordinate ρ ranging from 0.1 to 10 and angular coordinate θ from 0 to 2π. Numerically evaluate the perturbation force integral over this grid to obtain the dimensionless force factor F/(A μ c₀), where A is the interaction strength parameter, μ the atomic density, and c₀ the average solute concentration. Report the computed factor together with the q value in a JSON file named `force_factor.json` under `/app/outputs`.

## Assets

- SciPy library: scipy

## Workflow steps

### Step 1: Set up dimensionless grid
- Role: process
- Action: Set the speed parameter q = 0.04 directly. Define a polar grid for integration: radial coordinate ρ from 0.1 to 10 (use, for example, 50 logarithmically spaced points to capture the peak of the integrand). Angular coordinate θ from 0 to 2π (e.g., 24 points at 15° increments, mirroring the paper's evaluation increments). Store the grid arrays for later use.
- Evidence: none

### Step 2: Compute Mathieu functions
- Role: process
- Action: Evaluate the angular Mathieu functions for the first mode using scipy.special. For each grid point (ρ,θ), compute:
  (a) ω = θ - π/4.
  (b) ce₁(ω) = scipy.special.mathieu_cem(1, q, ω)[0] (the function value).
  (c) se₁(ω) = scipy.special.mathieu_sem(1, q, ω)[0].
  For the radial hyperbolic Mathieu functions of the second kind that vanish as ρ→∞, use scipy.special.mathieu_modcem2 and mathieu_modsem2 with argument z = ln(ρ) for ρ ≥ 1. The raw even/odd functions need to be normalized to the convention where the leading behavior at small q is Fek₁*(ρ) ≈ 2 I₁(√q / ρ) and Gek₁*(ρ) ≈ 2 I₁(√q / ρ). Determine the scaling factor C by evaluating the raw even function and the Bessel function I₁ at a small reference ρ (e.g., ρ=0.1): C = 2 * scipy.special.iv(1, √q / ρ_ref) / raw_even(ρ_ref). Then set Fek₁*(ρ) = C * scipy.special.mathieu_modcem2(1, q, ln ρ)[0] and Gek₁*(ρ) = C * scipy.special.mathieu_modsem2(1, q, ln ρ)[0]. For ρ < 1 use the symmetry Fek₁*(ρ) = Gek₁*(1/ρ) (the functions are interchanged under ρ→1/ρ).
- Evidence: none

### Step 3: Compute concentration field
- Role: process
- Action: For each grid point (ρ,θ) evaluate:
  E = exp( (√q / ρ) sinθ + √q ρ cosθ )
  ψ = E - √2 * ce₁(ω) * Fek₁*(ρ) + ( -√2 ) * se₁(ω) * Gek₁*(ρ)    (coefficients A₁^c=√2, A₁^s=-√2)
  Then the relative concentration is c/c₀ = ψ * exp( -(√q / ρ) sinθ - √q ρ cosθ ).
  Compute the perturbation Q defined by c/c₀ = (1+Q) * exp(-V/kT) where V/kT = (2√q / ρ) sinθ. Therefore Q = (c/c₀) * exp( (2√q / ρ) sinθ ) - 1.
- Evidence: none

### Step 4: Integration of perturbation force
- Role: scored (load-bearing)
- Action: Numerically integrate the perturbation force integral over rho and theta to obtain the dimensionless force factor F/(A mu c0). Save the result in force_factor.json.
- Output file: `/app/outputs/force_factor.json`
- Format: json
- Contract: {"q": float, "factor": float, "description": string}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/force_factor.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### force_factor.json
- path: `/app/outputs/force_factor.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dimensionless perturbation force factor F/(A mu c0) computed at q=0.04. The checker compares the factor to a hidden gold value with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `q`: float
    - `factor`: float
    - `description`: string
  - `items`: object
  - `required_columns`:
  - `units`:
    - `q`: dimensionless
    - `factor`: dimensionless

Notes: The dimensionless force factor for q=0.04 computed from the approximate solution. The checker compares the factor to a hidden gold value with tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "force_factor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "q": "float",
          "factor": "float",
          "description": "string"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "q": "dimensionless",
          "factor": "dimensionless"
        }
      },
      "description": "Dimensionless perturbation force factor F/(A mu c0) computed at q=0.04. The checker compares the factor to a hidden gold value with tolerance."
    }
  ],
  "notes": "The dimensionless force factor for q=0.04 computed from the approximate solution. The checker compares the factor to a hidden gold value with tolerance."
}
```

## How you are scored
A hidden verifier will independently read your `force_factor.json` and check that it contains the required fields. The verifier will then compare your reported dimensionless force factor against a hidden reference value, derived from the physical model, using a tolerance that accounts for numerical integration and implementation differences. The reward is 1.0 if your factor falls within the tolerance window; it decreases linearly to zero for larger deviations. Your factor must be positive and physically plausible to be considered valid. Note: you do not need to match the reference exactly; the tolerance is set to accept correct independent calculations.
