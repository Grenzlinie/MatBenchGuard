# Theoretical estimation of mechanical relaxation parameters in photoconducting CdS

## Problem background
A thin bar of CdS crystal vibrated longitudinally along the c‑axis exhibits internal friction that changes with light irradiation. The illumination alters the crystal’s photoconductivity, which interacts with the piezoelectric polarization, producing a mechanical relaxation peak and a corresponding dispersion of the sound velocity. This task computes the theoretical estimates of the maximum mechanical loss, the conductivity at which that maximum occurs, and the associated velocity change, using the analytical model derived from piezoelectric theory.

## Approach
The theory treats the dielectric constant of CdS as complex, with the photoconductivity entering through its imaginary part. For a longitudinal mode along the c‑axis under the stress‑free and open‑circuit boundary conditions of the composite‑bar method, the mechanical loss factor Q⁻¹ and the sound velocity v₃ become explicit functions of the conductivity σ₃. The loss reaches its maximum when σ₃ equals ε₃·ω (where ε₃ is the real part of the dielectric constant and ω the angular resonance frequency). From that condition, the maximum loss factor Q⁻¹_max and the fractional velocity change (dispersion rate) follow directly from the material constants. The reproduction therefore reduces to evaluating those three quantities numerically using the given constants.

## Reproduction target
Compute the following three theoretical estimates and write them to a JSON file:
- sigma_max = ε₃·ω  (Ω⁻¹·m⁻¹)
- Q⁻¹_max = (1/2)·s₃₃ᴱ·(e₃₃−Δ)² / ε₃  (dimensionless)
- dispersion_rate = 100 × Q⁻¹_max  (in %)

Use the provided constants: s₃₃ᴱ = 1.55×10⁻¹¹ m·s²/kg, ε₃ = 9·ε₀ (ε₀ = 8.85×10⁻¹² F/m), e₃₃−Δ = 0.4 C/m², ρ = 4.82×10³ kg/m³, ω = 2π·127×10³ rad/s. Store the results in a JSON file with keys "sigma_max", "Q⁻¹_max", and "dispersion_rate".

## Assets

- Python standard library: python3

## Workflow steps

### Step 1: Compute theoretical estimates
- Role: scored (load-bearing)
- Action: Using the provided material constants (s₃₃ᴱ, ε₃, e₃₃−Δ, ρ, ω) and the formulas for the mechanical loss factor Q⁻¹ and sound velocity v₃ under the condition of maximum loss (σ₃ = ε₃ω), compute sigma_max, Q⁻¹_max, and dispersion_rate, then write the results to a JSON file.
- Output file: `/app/outputs/step_01_theoretical_estimates.json`
- Format: json
- Contract: {"sigma_max": number (Ω⁻¹·m⁻¹), "Q⁻¹_max": number (dimensionless), "dispersion_rate": number (in %)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_theoretical_estimates.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_theoretical_estimates.json
- path: `/app/outputs/step_01_theoretical_estimates.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Theoretical estimates of maximum conductivity at mechanical loss peak, maximum mechanical loss factor, and dispersion rate.
- schema:
  - `type`: object
  - `required`:
    - `sigma_max`: number
    - `Q⁻¹_max`: number
    - `dispersion_rate`: number
  - `units`:
    - `sigma_max`: Ω⁻¹·m⁻¹
    - `Q⁻¹_max`: dimensionless
    - `dispersion_rate`: %

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_theoretical_estimates.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "sigma_max": "number",
          "Q⁻¹_max": "number",
          "dispersion_rate": "number"
        },
        "units": {
          "sigma_max": "Ω⁻¹·m⁻¹",
          "Q⁻¹_max": "dimensionless",
          "dispersion_rate": "%"
        }
      },
      "description": "Theoretical estimates of maximum conductivity at mechanical loss peak, maximum mechanical loss factor, and dispersion rate."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your output file `/app/outputs/step_01_theoretical_estimates.json` and compares your three numeric values to the expected theoretical results. Your score is based on how close your computed quantities are, within an appropriate tolerance that accounts for normal rounding differences. You must genuinely perform the calculation from the given constants and formulas; simply hardcoding numbers will not achieve full credit.
