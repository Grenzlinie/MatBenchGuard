# Mori chain parameters for a Debye isotropic solid: displacement damping coefficients and Laplace transforms

## Problem background
Subsystem relaxation in condensed phases is often modeled by coupling to a macroscopic phonon heatbath. Mori’s projection-operator formalism provides a systematic way to replace the true many-body reservoir with an equivalent few-degree-of-freedom mechanical system. This task applies that formalism to a Debye isotropic solid, focusing on the atomic displacement operator. The aim is to compute the Mori‑chain coupling constants and terminal damping coefficients that characterize the equivalent reduced heatbath, as well as certain zero‑frequency Laplace transforms of correlation functions, thereby probing whether the few‑body chain captures the same damping as the full phonon reservoir.

## Approach
The approach follows Mori theory. Starting from the displacement operator, one builds a chain of orthogonalized variables using projection operators. This yields a set of frequency parameters Δ₁², Δ₂², Δ₃², Δ₄² and damping coefficients γ₁, γ₂, γ₃, γ₄. The parameters are determined entirely by the Debye phonon spectral density D(ω) = 3ω²/ω_D³ for 0 ≤ ω ≤ ω_D. One computes the adiabatic frequency ω_a² = ω_D²/3 and the even moments ⟨ω²⟩, ⟨ω⁴⟩, ⟨ω⁶⟩, then uses the recurrences Δ₁² = ω_a², Δ₂² = ⟨ω²⟩ − ω_a², Δ₃² = (⟨ω⁴⟩ − ⟨ω²⟩²)/Δ₂², and Δ₄² from a continued‑fraction expression.

The displacement autocorrelation function is Φ₀(t) = sin(ω_D t) / (ω_D t); its Laplace transform at zero yields Φ̂₀(0). The damping coefficients follow via γ₁ = Δ₁²·Φ̂₀(0), γ₂ = Δ₂²/γ₁, γ₃ = Δ₃²/γ₂, γ₄ = Δ₄²/γ₃. For the velocity operator the same chain is built starting from the velocity variable; the velocity autocorrelation function for the Debye model is Φ_vel(t) = 3[ sin(ω_D t)/(ω_D t) + 2 cos(ω_D t)/(ω_D² t²) − 2 sin(ω_D t)/(ω_D³ t²) ], whose zero‑frequency Laplace transform is also evaluated. All computations are analytic and can be implemented with elementary functions in Python using NumPy; no external data are required.

## Reproduction target
Produce two JSON files:
1) step_01_mori_chain_params.json – containing the dimensionless ratios Δ₁²/ω_D², Δ₂²/ω_D², Δ₃²/ω_D², Δ₄²/ω_D² and γ₁/ω_D, γ₂/ω_D, γ₃/ω_D, γ₄/ω_D for the atomic displacement operator of a Debye isotropic solid.
2) step_02_correlation_laplace.json – containing the dimensionless zero‑frequency Laplace transforms of the displacement autocorrelation function (Φ̂₀(0)/ω_D) and the velocity autocorrelation function (Φ̂_vel(0)/ω_D).

## Assets

- Python with NumPy: numpy

## Workflow steps

### Step 1: Compute Debye spectral moments
- Role: process
- Action: Using the Debye phonon spectral density D(ω)=3ω²/ω_D³ (0 ≤ ω ≤ ω_D), compute the adiabatic frequency ω_a² = ω_D²/3 and the even spectral moments ⟨ω²⟩, ⟨ω⁴⟩, ⟨ω⁶⟩ as rational multiples of ω_D². These intermediates are needed for the Mori chain parameters.
- Evidence: `/app/outputs/debye_moments.json`

### Step 2: Compute displacement Mori chain parameters and damping coefficients
- Role: scored (load-bearing)
- Action: Using the spectral moments and the displacement autocorrelation function, compute the dimensionless coupling coefficients Δ₁²/ω_D², Δ₂²/ω_D², Δ₃²/ω_D², Δ₄²/ω_D² and the dimensionless damping coefficients γ₁/ω_D, γ₂/ω_D, γ₃/ω_D, γ₄/ω_D for the atomic displacement operator of a Debye isotropic solid. Apply the Mori recurrence and the definition γ₁ = Δ₁²·Φ̂₀(0) with Φ̂₀(0) obtained from the Laplace transform of the displacement correlation function Φ₀(t).
- Output file: `/app/outputs/step_01_mori_chain_params.json`
- Format: json
- Contract: object with keys delta1_sq_over_wD2, delta2_sq_over_wD2, delta3_sq_over_wD2, delta4_sq_over_wD2 (all floats), gamma1_over_wD, gamma2_over_wD, gamma3_over_wD, gamma4_over_wD (all floats)
- Scoring: scored by hidden verifier

### Step 3: Compute zero-frequency Laplace transforms of correlation functions
- Role: scored
- Action: Compute the normalized displacement autocorrelation function Φ₀(t)=sin(ω_D t)/(ω_D t) and its Laplace transform at zero frequency. Also compute the velocity autocorrelation function for the Debye model and its zero-frequency Laplace transform. Report both Laplace transform values as dimensionless ratios relative to ω_D.
- Output file: `/app/outputs/step_02_correlation_laplace.json`
- Format: json
- Contract: object with keys Phi0_laplace_over_wD (float) and Phi0_vel_laplace_over_wD (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mori_chain_params.json`
- `/app/outputs/step_02_correlation_laplace.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mori_chain_params.json
- path: `/app/outputs/step_01_mori_chain_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dimensionless Mori chain coupling coefficients Δ_i²/ω_D² and damping coefficients γ_i/ω_D for the displacement operator.
- schema:
  - `type`: object
  - `required`:
    - `delta1_sq_over_wD2`: float
    - `delta2_sq_over_wD2`: float
    - `delta3_sq_over_wD2`: float
    - `delta4_sq_over_wD2`: float
    - `gamma1_over_wD`: float
    - `gamma2_over_wD`: float
    - `gamma3_over_wD`: float
    - `gamma4_over_wD`: float
  - `items`: object

### step_02_correlation_laplace.json
- path: `/app/outputs/step_02_correlation_laplace.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zero-frequency Laplace transforms of the displacement and velocity autocorrelation functions, expressed as dimensionless ratios relative to ω_D.
- schema:
  - `type`: object
  - `required`:
    - `Phi0_laplace_over_wD`: float
    - `Phi0_vel_laplace_over_wD`: float
  - `items`: object

Notes: All quantities are dimensionless ratios derived from the Debye model within the high-temperature classical limit. The values are uniquely determined by the public problem definition; exact analytic comparison is performed by the hidden checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mori_chain_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta1_sq_over_wD2": "float",
          "delta2_sq_over_wD2": "float",
          "delta3_sq_over_wD2": "float",
          "delta4_sq_over_wD2": "float",
          "gamma1_over_wD": "float",
          "gamma2_over_wD": "float",
          "gamma3_over_wD": "float",
          "gamma4_over_wD": "float"
        },
        "items": {}
      },
      "description": "Dimensionless Mori chain coupling coefficients Δ_i²/ω_D² and damping coefficients γ_i/ω_D for the displacement operator."
    },
    {
      "file": "step_02_correlation_laplace.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Phi0_laplace_over_wD": "float",
          "Phi0_vel_laplace_over_wD": "float"
        },
        "items": {}
      },
      "description": "Zero-frequency Laplace transforms of the displacement and velocity autocorrelation functions, expressed as dimensionless ratios relative to ω_D."
    }
  ],
  "notes": "All quantities are dimensionless ratios derived from the Debye model within the high-temperature classical limit. The values are uniquely determined by the public problem definition; exact analytic comparison is performed by the hidden checker."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently recomputes the expected analytic results from the same Debye model. For step_01 the verifier recomputes the exact Δ_i²/ω_D² and γ_i/ω_D from the spectral moments and Φ̂₀(0); for step_02 it recomputes the zero‑frequency Laplace transforms. Each artifact is compared to the recomputed reference with a numerical tolerance that accounts for floating‑point precision; the reported values must match to within that tolerance. The two scored artifacts are combined with weights (the main Mori‑chain artifact carries the largest weight) to produce the final reward in [0,1]. Reporting numbers that are not correctly derived from the model will not satisfy the comparison.
