# Calibrated Mean-Field Homogenization for Thermal Conductivity of Lightweight Earth

## Problem background
Predicting the effective thermal conductivity of lightweight earth and raw earth blocks incorporating plant aggregates is challenging due to the high variability of raw materials and the complex microstructure of these composites. This task addresses that challenge by developing and calibrating a mean-field homogenization workflow that computes the effective thermal conductivity from the properties of the constituents, while considering realistic morphological features such as aggregate shape, cracking perpendicular to compaction, and coating of particles by the binder matrix.

## Approach
The workflow applies two analytical homogenization schemes: the Mori–Tanaka model and the double-inclusion model. For composites where the earth binder forms a continuous matrix with a low-to-moderate volume fraction of plant aggregates, the representative volume element (RVE) includes spheroidal air inclusions that represent post-drying cracking perpendicular to compaction (EB‑2 RVE). The effective thermal conductivity tensor is computed with the Mori–Tanaka scheme and its diagonal components are averaged to obtain a scalar prediction. For EB‑2 models, assume a random orientation of the plant aggregates in the plane perpendicular to compaction (2D orientation). For composites in which coated particles are immersed in an air matrix, a double-inclusion RVE (EB‑3) is used. In both cases, the model is calibrated by adjusting a free parameter — the cracking volume fraction for EB‑2 models or the coating fraction for the EB‑3 model — until the mean of the diagonal components of the effective thermal conductivity tensor matches the given experimental scalar conductivity. The provided inputs are the binder thermal conductivity, the aggregate thermal conductivity tensor components (or isotropic value), the volume fraction of the aggregate, and the particle aspect ratio.

## Input data

Table 1: Input parameters for each composite.

| Composite | Binder thermal conductivity (W·m⁻¹·K⁻¹) | Aggregate thermal conductivity (W·m⁻¹·K⁻¹) | Aggregate volume fraction | Aggregate aspect ratio | Experimental scalar thermal conductivity (W·m⁻¹·K⁻¹) |
|---|---|---|---|---|---|
| FH3-Laborel | 0.57 | λ_T = 0.044, λ_N = 0.066 | 0.22 | 3.3 | 0.30 |
| FH6-Laborel | 0.57 | λ_T = 0.044, λ_N = 0.066 | 0.37 | 3.3 | 0.20 |
| CSP-Belayachi | 0.27 | isotropic λ = 0.04 | 0.79 | 1.0 | 0.055 |
| CSB-Belayachi | 0.27 | λ_T = 0.045, λ_N = 0.068 | 0.39 | 3.4 | 0.158 |

Note: For CSP, use the isotropic aggregate thermal conductivity of 0.04 W·m⁻¹·K⁻¹ as selected in the reference study.

## Reproduction target
For each of the four composites (FH3‑Laborel, FH6‑Laborel, CSP‑Belayachi, CSB‑Belayachi), implement the appropriate homogenization model using the provided input data:
- FH3‑Laborel and FH6‑Laborel: EB‑2 (Mori–Tanaka with spheroidal air inclusions);
- CSB‑Belayachi: EB‑2;
- CSP‑Belayachi: EB‑3 (double‑inclusion with coated particles).
Calibrate the cracking volume fraction (EB‑2) or coating fraction (EB‑3) so that the arithmetic mean of the diagonal components of the effective thermal conductivity tensor reproduces the experimental scalar thermal conductivity given for that composite. Report the calibrated parameter as a percentage and the resulting predicted scalar conductivity (average of tensor components) in the output JSON file. The objective is to obtain predictions that follow from the physics of the homogenization models and the specified input values.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Calibrate homogenization models and predict thermal conductivity
- Role: scored (load-bearing)
- Action: Implement the Mori-Tanaka and double-inclusion mean-field homogenization models for thermal conductivity. For each of the four composites (FH3-Laborel, FH6-Laborel, CSP-Belayachi, CSB-Belayachi), use the provided input data (binder thermal conductivity, aggregate thermal conductivity tensor components, volume fractions, aspect ratios, and experimental scalar thermal conductivities). Build the appropriate RVE model: EB-2 (Mori-Tanaka with spheroidal air inclusions for cracking perpendicular to compaction) for FH3, FH6, CSB; EB-3 (double-inclusion with coated plant particles in an air matrix) for CSP. For each composite, calibrate the cracking volume fraction (EB-2) or coating fraction (EB-3) by adjusting it until the arithmetic mean of the diagonal components of the effective thermal conductivity tensor matches the given experimental scalar conductivity within a small tolerance. Write the calibrated parameter (percentage) and the resulting predicted scalar conductivity to a JSON file.
- Output file: `/app/outputs/calibration_results.json`
- Format: json
- Contract: JSON list of four objects, each with keys: composite (string), model_type (string, must be exactly 'EB-2-2D' for FH3, FH6, CSB; 'EB-3-3D' for CSP), calibrated_value (number, in %), predicted_lambda (number, in W·m⁻¹·K⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calibration_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calibration_results.json
- path: `/app/outputs/calibration_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: List of calibration results for four lightweight earth composites. Each entry reports the composite name, model type (must be 'EB-2-2D' for FH3, FH6, CSB; 'EB-3-3D' for CSP), the calibrated cracking or coating percentage, and the predicted scalar effective thermal conductivity.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `composite`, `model_type`, `calibrated_value`, `predicted_lambda`
    - `properties`:
      - `composite`:
        - `type`: string
      - `model_type`:
        - `type`: string
      - `calibrated_value`:
        - `type`: number
      - `predicted_lambda`:
        - `type`: number

Notes: The checker will compare the agent's reported predicted_lambda and calibrated_value to hidden reference values from the paper with appropriate tolerances. No additional output files are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calibration_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "composite",
            "model_type",
            "calibrated_value",
            "predicted_lambda"
          ],
          "properties": {
            "composite": {
              "type": "string"
            },
            "model_type": {
              "type": "string"
            },
            "calibrated_value": {
              "type": "number"
            },
            "predicted_lambda": {
              "type": "number"
            }
          }
        }
      },
      "description": "List of calibration results for four lightweight earth composites. Each entry reports the composite name, model type (must be 'EB-2-2D' for FH3, FH6, CSB; 'EB-3-3D' for CSP), the calibrated cracking or coating percentage, and the predicted scalar effective thermal conductivity."
    }
  ],
  "notes": "The checker will compare the agent's reported predicted_lambda and calibrated_value to hidden reference values from the paper with appropriate tolerances. No additional output files are required."
}
```

## How you are scored
A hidden verifier inspects the calibration_results.json file. For each composite it compares your reported predicted_lambda and calibrated_value to hidden reference values. Each composite contributes a partial score; the final reward is a weighted sum of those scores. The verifier allows small deviations that are typical of numerical methods, but large discrepancies will reduce the score. Merely writing down numbers without executing the homogenization and calibration procedure will not earn credit — the verifier expects the output to be the result of a genuine computational workflow.
