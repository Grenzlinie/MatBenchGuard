# Process Sensitivity Analysis for Ion-Exchanged Planar Waveguides

## Problem background
Planar optical waveguides fabricated by silver-sodium ion exchange are key components in integrated optics. The effective refractive index of such waveguides is determined by the fabrication process, primarily the diffusion time in the molten salt bath and the melt temperature. Achieving high repeatability of the effective index is crucial for device performance, especially for passive components like directional couplers and resonant filters that require precise phase matching. This task investigates the sensitivity of the effective index to process parameter variations by analytically modelling the waveguide's index profile and mode propagation.

## Approach

The refractive index profile of the waveguide is approximated by a linear model:

n²(x) = n_s² - 2 n_s Δn_s (x / d₁)   (0 ≤ x ≤ d₁)

where the surface index n_s = 1.605, substrate index n₂ = 1.51625, so Δn_s = n_s − n₂ = 0.08875, and d₁ is the effective waveguide depth (in μm). The superstrate is air with n₀ = 1.0.

For the fundamental TE₀ mode, the WKB eigenvalue equation is

d₁ k_s³ / (3 k² n_s Δn_s) = π/4 + arctan(ξ k₀ / k_s),   with ξ = 1

where
k = 2π/λ,   λ = 0.6328 μm
k_s = k √(n_s² − n_e²)
k₀ = k √(n_e² − n₀²)

The effective depth d₁ depends on the diffusion time t (in minutes) and the melt temperature T (in Kelvin) via

d₁ = 8.243 × 10³ √t  exp(−1.02 × 10⁴ / (2 T))   [μm]

Differentiating the eigenvalue equation implicitly and using the chain rule yields the sensitivities of the effective index n_e to time and temperature:

α = k_s⁴ d₁ / [ 6 k⁴ n_s Δn_s ( (n_e/k₀) ξ [1 + (k₀/k_s)²] / [1 + (ξ k₀/k_s)²] + 3/k_s ) ]

δn_e/δt = α / t   [min⁻¹]

δn_e/δT = (1.02 × 10⁴ α) / T²   [K⁻¹]   (which equals per °C because a 1 °C change is a 1 K change).

To evaluate the curves, choose a representative grid of effective indices n_e ranging from just above the substrate index (1.51625) to near the surface index (1.605). For each n_e and for each of the three melt temperatures 217 °C, 250 °C, 310 °C (convert to Kelvin by adding 273.15), compute d₁, then k, k_s, k₀, α, δn_e/δt, and δn_e/δT. Write the results to a CSV file.

## Reproduction target
Compute the theoretical sensitivity of the effective index n_e to diffusion time (δn_e/δt, units 1/min) and to melt temperature (δn_e/δT, units 1/°C) for the fundamental TE0 mode as functions of n_e. Evaluate these sensitivities for a representative grid of n_e covering the single‑mode range (from just above the substrate index to near the surface index) at three melt temperatures: 217 °C, 250 °C, and 310 °C. Produce a CSV file at `/app/outputs/step_01_sensitivities.csv` with columns `ne`, `temperature_C`, `delta_ne_delta_t`, `delta_ne_delta_T`. The computation is purely analytical; no experimental data are required.

## Assets
No external datasets or pre‑trained models are needed. The computation uses only standard numerical packages. A Python environment with basic scientific computing libraries (e.g., numpy) is sufficient.

## Workflow steps

### Step 1: Compute sensitivity curves
- Role: scored (load-bearing)
- Action: Implement the analytic model: use the linear refractive index profile approximation, the eigenvalue equation for the TE0 mode, and the effective depth model to compute the sensitivity of effective index to diffusion time (δn_e/δt) and to melt temperature (δn_e/δT) as functions of effective index n_e. Evaluate for a representative range of n_e covering the single-mode region (from just above the substrate index to near the surface index) at three melt temperatures: 217 °C, 250 °C, and 310 °C. Write the computed values to a CSV file.
- Output file: `/app/outputs/step_01_sensitivities.csv`
- Format: csv
- Contract: Columns: ne (effective index, dimensionless), temperature_C (int: 217, 250, 310), delta_ne_delta_t (sensitivity to diffusion time, unit: 1/min), delta_ne_delta_T (sensitivity to temperature, unit: 1/°C). One row per effective index point per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_sensitivities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_sensitivities.csv
- path: `/app/outputs/step_01_sensitivities.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed theoretical sensitivity values for the TE0 mode at the specified melt temperatures over a range of effective indices covering the single-mode region.
- schema:
  - `type`: table
  - `required_columns`: `ne`, `temperature_C`, `delta_ne_delta_t`, `delta_ne_delta_T`
  - `units`:
    - `ne`: dimensionless
    - `temperature_C`: °C
    - `delta_ne_delta_t`: min⁻¹
    - `delta_ne_delta_T`: °C⁻¹

Notes: The agent must compute the sensitivity using the linear refractive index profile approximation and the eigenvalue equation for the TE0 mode described in the paper's methodology section. No external data are required; all necessary constants are provided in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_sensitivities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "ne",
          "temperature_C",
          "delta_ne_delta_t",
          "delta_ne_delta_T"
        ],
        "units": {
          "ne": "dimensionless",
          "temperature_C": "°C",
          "delta_ne_delta_t": "min⁻¹",
          "delta_ne_delta_T": "°C⁻¹"
        }
      },
      "description": "Computed theoretical sensitivity values for the TE0 mode at the specified melt temperatures over a range of effective indices covering the single-mode region."
    }
  ],
  "notes": "The agent must compute the sensitivity using the linear refractive index profile approximation and the eigenvalue equation for the TE0 mode described in the paper's methodology section. No external data are required; all necessary constants are provided in the paper."
}
```

## How you are scored
Your CSV output will be scored by a hidden verifier. The verifier will independently implement the same theoretical model to compute the correct ('gold') sensitivity values for the identical (ne, temperature_C) combinations. For each row in your submission, the verifier compares both `delta_ne_delta_t` and `delta_ne_delta_T` to the gold values. A row passes if both sensitivities are within the verifier's allowed tolerance. Your reward is the fraction of rows that pass. Because scoring relies on a recomputed reference, the accuracy of your implementation directly determines your score.
