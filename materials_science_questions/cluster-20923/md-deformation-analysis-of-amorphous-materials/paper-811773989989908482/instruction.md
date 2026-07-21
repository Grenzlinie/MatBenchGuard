# Analytic nominal yield strength estimate for notched metallic glass specimen

## Problem background
This work investigates the plasticity improvement in Zr-based metallic glass by introducing artificial macroscopic notches. The critical analytic component estimates the nominal yield strength of the two-symmetric-notch specimen using an approximate stress-field integration. Understanding this estimate explains the observed reduction in yield strength relative to unnotched samples and supports the design strategy of using notches to control shear-band propagation.

## Approach
The approximate analytic method treats the notched specimen as a strip with two symmetrical semi-circular notches under compression. The stress component σ_y along the loading axis across the notched section is given by the polynomial (Glinka & Newport, 1987):

σ_y(x) = K_t σ_nt [1.00 − 2.330 (x/ρ) + 2.590 (x/ρ)^1.5 − 0.907 (x/ρ)^2 + 0.037 (x/ρ)^3],

where K_t = 1.90 is the stress concentration factor, ρ = 0.5 mm is the notch radius, and σ_nt is the nominal stress on the notched section (σ_nt = P/(2d h), with d = 1.0 mm the half‑spacing between notch tips and h the out‑of‑plane thickness). The nominal stress on the full (N) section is σ_n = P/(2(d+ρ) h). Numerically integrate σ_y along the notched section from the notch tip (x = 0) to the specimen centerline (x = d), then double for symmetry to obtain the total stress sum Ω = 2 ∫_0^d σ_y(x) dx. Express Ω as a multiple of σ_n by eliminating P and h. Compute the average stress on the notched section σ_a = Ω/(2d). Then compute the global average stress as the simple mean of the notched‑section average and the full‑section nominal stress: σ_aver = (σ_a + σ_n)/2. By equating this global average to the known material yield stress σ_s = 1.80 GPa, solve for the nominal yield strength σ_n. Finally, calculate the dimensionless global averaging factor σ_aver/σ_n as a consistency check.

## Reproduction target
Implement the analytic derivation described in the approach for the two-symmetric-notch specimen (specimen C) with the following fixed parameters: stress concentration factor K_t = 1.90, notch radius ρ = 0.5 mm, half-spacing between notch tips d = 1.0 mm, and material yield stress σ_s = 1.80 GPa. Output the estimated nominal yield strength σ_n (in GPa) and the computed global averaging factor σ_aver/σ_n to the scored artifact.

## Assets

- Python scientific stack (NumPy, SciPy)

## Workflow steps

### Step 1: Analytic nominal yield strength estimate for specimen C
- Role: scored (load-bearing)
- Action: Implement the σ_y polynomial: σ_y = K_t σ_nt [1.00 − 2.330 (x/ρ) + 2.590 (x/ρ)^1.5 − 0.907 (x/ρ)^2 + 0.037 (x/ρ)^3], with K_t=1.90, ρ=0.5 mm. Use the geometric relations σ_nt = P/(2d h) and σ_n = P/(2(d+ρ) h), where d=1.0 mm. Numerically integrate σ_y from x=0 to x=d (1.0 mm), then double for symmetry to obtain Ω = 2 ∫_0^d σ_y dx. Express Ω as a multiple of σ_n. Compute the notched-section average σ_a = Ω/(2d) and the global average stress σ_aver = (σ_a + σ_n)/2. Equate σ_aver to the material yield stress σ_s = 1.80 GPa to solve for σ_n. Also compute the global averaging factor σ_aver/σ_n. Write both results to the output JSON.
- Output file: `/app/outputs/yield_strength_estimate.json`
- Format: json
- Contract: {"nominal_yield_strength_GPa": float, "computed_average_stress_factor": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/yield_strength_estimate.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### yield_strength_estimate.json
- path: `/app/outputs/yield_strength_estimate.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The estimated nominal yield strength σn in GPa and the computed global averaging factor σaver/σn for the two‑symmetric‑notch specimen.
- schema:
  - `type`: object
  - `required`:
    - `nominal_yield_strength_GPa`: float
    - `computed_average_stress_factor`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `nominal_yield_strength_GPa`: GPa
    - `computed_average_stress_factor`: dimensionless

Notes: All parameters required for the analytic estimate are explicitly stated in the task; the agent re‑implements the integration and averaging procedure. The checker recomputes the same quantities independently and compares the submitted values within a hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "yield_strength_estimate.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "nominal_yield_strength_GPa": "float",
          "computed_average_stress_factor": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "nominal_yield_strength_GPa": "GPa",
          "computed_average_stress_factor": "dimensionless"
        }
      },
      "description": "The estimated nominal yield strength σn in GPa and the computed global averaging factor σaver/σn for the two‑symmetric‑notch specimen."
    }
  ],
  "notes": "All parameters required for the analytic estimate are explicitly stated in the task; the agent re‑implements the integration and averaging procedure. The checker recomputes the same quantities independently and compares the submitted values within a hidden tolerance."
}
```

## How you are scored
A hidden verifier will independently recompute the same analytic estimate using the given parameters and compare your submitted 'nominal_yield_strength_GPa' and 'computed_average_stress_factor' to the verifier's own computed values. Your score for this step reflects the agreement between your results and the expected quantities. The overall reward is determined solely by the verifier's assessment of your scored output files.
