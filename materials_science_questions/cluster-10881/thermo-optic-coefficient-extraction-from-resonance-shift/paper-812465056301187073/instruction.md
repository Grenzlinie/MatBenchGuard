# Steady-State Thermo-Optic Wavelength Shift Prediction for Heated Fibre Bragg Grating

## Problem background
Tuneable fibre Bragg grating (FBG) filters are important components for optical measurement, sensing, and reconfigurable communication systems. Polymer optical fibre (POF) Bragg gratings offer high temperature sensitivity and the potential for wide wavelength tuning. This task centres on a POF FBG that is tuned via a thin-film resistive heater deposited on the fibre surface. The objective is to compute the steady-state wavelength shift per unit input electrical power predicted by a one-dimensional thermal model. This coefficient characterises the filter's tuning efficiency and is a key figure of merit for such devices.

## Approach
The heater-coated POF grating is modelled as a one-dimensional thermal system under the assumption of uniform heating along the grating length and negligible radial temperature gradients (the Biot number is small, ∼0.1). Under these conditions, the steady-state temperature rise of the fibre is proportional to the input electrical power, with the proportionality dictated by the fibre's thermal mass, its dissipation to the surroundings, and the fibre geometry. The induced steady-state temperature change alters the Bragg wavelength through two coupled effects: thermal expansion of the fibre and the thermo-optic change in refractive index. Both effects are linear in the temperature change, so the resulting Bragg wavelength shift Δλ_B is a linear function of the input power P_in. The task is to compute the slope d(Δλ_B)/dP_in, expressed in pm/mW, using the fibre parameters provided in the step description.

## Reproduction target
Using the material and geometric parameters listed in the step (density ρ=1190 kg/m³, specific heat c_p=1450 J/(kg·K), thermal conductivity K=0.17 W/(m·K), fibre radius R_fibre=120 µm, grating length L=1 cm, effective mode index n=1.478, thermal expansion coefficient α_e=70×10⁻⁶ K⁻¹, thermo‑optic coefficient β=−1.2×10⁻⁴ K⁻¹, grating period Λ=530.425 nm, and heat dissipation constant a=1.7 s⁻¹), compute the steady‑state Bragg wavelength shift per unit input power (slope in pm/mW) predicted by the one‑dimensional thermal model. Write the result as a single numeric value with no header to the file /app/outputs/predicted_slope.csv.

## Assets

- PMMA fibre and thermal parameters
- numpy: numpy

## Workflow steps

### Step 1: Compute thermo-optic wavelength shift slope
- Role: scored (load-bearing)
- Action: Using the provided fibre material properties (density, specific heat, thermal conductivity, thermal expansion coefficient, thermo-optic coefficient, fibre radius, grating length, effective mode index, grating period, and heat dissipation constant), compute the steady-state Bragg wavelength shift per unit input power from the one-dimensional heat diffusion model. The model assumes uniform heating along the grating and negligible radial thermal gradients (Biot number ~0.1), leading to a steady-state temperature rise proportional to input power. The Bragg wavelength shift is determined by the thermal expansion and thermo-optic effects. Compute the resulting slope in pm/mW and write it to predicted_slope.csv.
- Output file: `/app/outputs/predicted_slope.csv`
- Format: csv
- Contract: A CSV file containing a single numeric value (no header) representing the slope in units of pm/mW.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_slope.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_slope.csv
- path: `/app/outputs/predicted_slope.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Steady-state Bragg wavelength shift per unit input electrical power predicted by the 1D thermal model.
- schema:
  - `type`: other
  - `description`: single numeric value (no header), units pm/mW

Notes: The model uses the material and geometric parameters from the paper; the agent must implement the calculation. No additional outputs are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_slope.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "other",
        "description": "single numeric value (no header), units pm/mW"
      },
      "description": "Steady-state Bragg wavelength shift per unit input electrical power predicted by the 1D thermal model."
    }
  ],
  "notes": "The model uses the material and geometric parameters from the paper; the agent must implement the calculation. No additional outputs are required."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier that reads the value from predicted_slope.csv. The verifier compares your computed slope to a hidden gold value derived from the same model. The reward is based on how close your slope is to the gold; a result within a predetermined tolerance receives full credit, and the reward decreases for larger deviations. You must implement the calculation faithfully; simply reporting a constant value without performing the computation will not suffice.
