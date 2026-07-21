# Thermal Lensing On-Axis Temperature Computation

## Problem background
In thermal lensing, a focused laser beam heats an absorbing medium, creating a radial temperature distribution that changes the local refractive index. The steady-state heat equation with a Gaussian heat source yields an analytical expression for the temperature profile. Verifying the on-axis temperature rise for a given set of experimental parameters is a critical step in modeling the induced refractive index change and the resulting self-phase modulation effects.

## Approach
Compute the on-axis temperature change from the steady-state heat equation solution. For a Gaussian pump beam in a cylindrical sample, the solution leads to an expression involving the pump power, absorption coefficient, thermal conductivity, beam waist, sample half‑width, and the Euler–Mascheroni constant. Plug the provided numerical parameters into this expression, evaluate it using standard numerical primitives, and output the result.

## Reproduction target
Calculate the on-axis temperature rise using the analytical formula with the given parameters: pump power 0.3 W, absorption coefficient 130 m⁻¹, thermal conductivity 0.58 W/(m·K), beam waist 32 µm, and sample half‑width 0.5 cm. Output the computed temperature change in Kelvin as a single decimal number with at least 4 decimal places.

## Assets
This task requires no external datasets, models, or proprietary software. The computation can be performed using standard Python 3 math modules (e.g., `math`). No supplementary files need to be downloaded.

## Workflow steps

### Step 1: Compute on-axis temperature change
- Role: scored
- Action: Calculate the on-axis temperature change ΔT(0) using the analytical solution of the steady-state heat equation for a Gaussian pump beam in an absorbing medium. Use the formula ΔT(0) = (α·P/(4π·k))·(γ + ln(2·a²/w²)), where γ is the Euler–Mascheroni constant. Input parameters: α = 130 m⁻¹, P = 0.3 W, k = 0.58 W/(m·K), a = 0.005 m, w = 32e-6 m. Output the computed value as a plain-text decimal with at least 4 decimal places.
- Output file: `/app/outputs/delta_T_zero.txt`
- Format: txt
- Contract: A single decimal number with at least 4 decimal places.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_T_zero.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_T_zero.txt
- path: `/app/outputs/delta_T_zero.txt`
- format: txt
- purpose: scored
- target_policy: absolute_tolerance
- description: The computed on-axis temperature change ΔT(0) from the analytical heat equation model.
- schema:
  - `type`: text
  - `description`: A single decimal number representing the on-axis temperature change ΔT(0) in Kelvin, with at least 4 decimal places.

Notes: Only the on-axis temperature change is scored; the rest of the paper's workflow (refractive index profile, diffraction simulations, interferometric data processing) is omitted because the thermo-optic coefficient dn/dT is not provided in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_T_zero.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "absolute_tolerance",
      "schema": {
        "type": "text",
        "description": "A single decimal number representing the on-axis temperature change ΔT(0) in Kelvin, with at least 4 decimal places."
      },
      "description": "The computed on-axis temperature change ΔT(0) from the analytical heat equation model."
    }
  ],
  "notes": "Only the on-axis temperature change is scored; the rest of the paper's workflow (refractive index profile, diffraction simulations, interferometric data processing) is omitted because the thermo-optic coefficient dn/dT is not provided in the paper."
}
```

## How you are scored
A hidden verifier reads your output file and compares the computed value to a reference answer. The comparison uses a fixed tolerance that accounts for floating-point and numerical differences between implementations. Your score is based on whether the submitted number falls within the tolerance window; exact agreement is not required, but significant deviations will be penalized.