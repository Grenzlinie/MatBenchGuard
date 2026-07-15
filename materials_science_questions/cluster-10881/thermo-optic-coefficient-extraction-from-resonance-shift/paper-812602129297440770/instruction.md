# Computation of Reflectance-Modulation Thermometry Calibration Constant

## Problem background
In high‑power laser diodes, the temperature of the mirror facet is a critical parameter that influences device reliability and catastrophic optical damage. Reflectance‑modulation thermometry is an optical technique that measures the local temperature rise by detecting the change in the reflected intensity of a probe beam. The temperature change is related to the measured relative reflectance change via a calibration constant C that must be determined from the optical properties of the semiconductor material. This task targets the computation of that calibration constant for the specific material, probe wavelength, and incidence angle used in a representative study.

## Approach
The calibration constant C is defined through the linear relation ΔT = C × (ΔR/R). The steady reflectance R depends on the refractive index n of the material and the incidence angle, following the standard p‑polarized Fresnel reflectance formula for oblique incidence. By differentiating R with respect to n, either analytically or numerically, one obtains dR/dn. The calibration constant is then given by C = R × (dR/dn)⁻¹ × (δn/δT)⁻¹, where δn/δT is the thermo‑optic coefficient. The agent will retrieve the refractive index n and its temperature derivative δn/δT for the target composition and wavelength from the publicly available reference (Aspnes et al. 1986), apply the reflectance formula at an incidence angle of 45°, evaluate the derivative, and compute C.

## Reproduction target
Compute the calibration constant C (in Kelvin) for the specified material (Al₀.₆₅Ga₀.₃₅As, probe wavelength 632.8 nm, incidence angle 45°) using the p‑polarized Fresnel reflectance formula. Obtain the necessary refractive index n and its temperature derivative δn/δT from the literature (Aspnes et al., J. Appl. Phys. 60, 754, 1986). Record the computed value in the output file `/app/outputs/calibration_constant.json` under the key "C".

## Assets

- Refractive index and thermo-optic coefficient of Al0.65Ga0.35As at 632.8 nm (Aspnes et al., J. Appl. Phys. 60, 754 (1986)): https://doi.org/10.1063/1.337057

## Workflow steps

### Step 1: Compute calibration constant C
- Role: scored (load-bearing)
- Action: Obtain the refractive index n and its temperature derivative δn/δT for Al0.65Ga0.35As at a probe wavelength of 632.8 nm from the literature (Aspnes et al. 1986). Using the p-polarized Fresnel reflectance formula for oblique incidence (incidence angle i = π/4), compute the steady reflectance R(n). Evaluate dR/dn analytically or numerically. Then calculate the calibration constant C = R × (dR/dn)⁻¹ × (δn/δT)⁻¹. Write the computed value in Kelvin to a JSON file.
- Output file: `/app/outputs/calibration_constant.json`
- Format: json
- Contract: {"type":"object","properties":{"C":{"type":"number","unit":"K"}},"required":["C"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calibration_constant.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calibration_constant.json
- path: `/app/outputs/calibration_constant.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The calibration constant C in Kelvin derived from the p-polarized Fresnel reflectance formula for Al0.65Ga0.35As at probe wavelength 632.8 nm and incidence angle 45°, using published refractive index and thermo-optic coefficient.
- schema:
  - `type`: object
  - `required`:
    - `C`: number
  - `units`:
    - `C`: K

Notes: The constant is computed from first principles using publicly available material parameters; the exact value is compared to the paper's reported constant under a hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calibration_constant.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C": "number"
        },
        "units": {
          "C": "K"
        }
      },
      "description": "The calibration constant C in Kelvin derived from the p-polarized Fresnel reflectance formula for Al0.65Ga0.35As at probe wavelength 632.8 nm and incidence angle 45°, using published refractive index and thermo-optic coefficient."
    }
  ],
  "notes": "The constant is computed from first principles using publicly available material parameters; the exact value is compared to the paper's reported constant under a hidden tolerance."
}
```

## How you are scored
A hidden verifier will read the computed calibration constant from your output file and compare it against an independently established reference value. The reward for this task is the overall score returned by the verifier after evaluating the scored artifact. Each workflow step that is marked as scored contributes to the reward; the only scored step here is the calibration constant computation. The checks are performed automatically — simply producing a number that looks plausible is not sufficient; the verifier assesses whether the result matches the expected reference within a predetermined tolerance.
