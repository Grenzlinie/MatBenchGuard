# Fitting Sellmeier Dispersion Equation to Fused Silica Refractive Index Data

## Problem background
Fused silica (amorphous SiO₂) is a key optical material used in lenses, windows, and fibers. Its refractive index depends on wavelength, and an accurate dispersion model is essential for designing optical systems and for material characterization. A common parametric model is the three‑term Sellmeier equation:

n² − 1 = Σ_{i=1}^{3} A_i λ² / (λ² − λ_i²),

where λ is the wavelength in microns and the six parameters (A₁, λ₁, A₂, λ₂, A₃, λ₃) characterize the dispersion. In this task you are given measured refractive‑index data for high‑purity fused silica across a wide spectral range. The challenge is to derive the Sellmeier parameters that best describe the measurements and to quantify the typical disagreement between the fitted model and the measured data.

## Approach
You will work with a bundled CSV dataset containing wavelengths (in microns) and the corresponding arithmetical‑mean refractive index at 20 °C, compiled from measurements on three optical‑quality fused silica specimens. Your task is to numerically fit the three‑term Sellmeier model to these data points using nonlinear least squares (e.g., via scipy.optimize.curve_fit). After fitting, compute the predicted refractive index at every wavelength from the fitted parameters, calculate the absolute residual |n_measured − n_predicted| for each wavelength, and then compute the overall average of those absolute residuals. The fitted parameters and the average absolute residual must be written to /app/outputs/sellmeier_results.json.

## Reproduction target
Using the provided refractive‑index dataset (60 wavelengths, bundled as a CSV file), perform the following:
- Fit the three‑term Sellmeier dispersion equation to the data.
- Report the six fitted parameters: A₁, λ₁, A₂, λ₂, A₃, λ₃.
- Report the overall average absolute residual between the measured refractive indices and the values predicted by the fitted equation, averaged over all 60 wavelengths.

The result must be saved as /app/outputs/sellmeier_results.json following the structure defined in the output contract.

## Assets

- Fused silica refractive index measurements (60 wavelengths)
- Python scientific stack

## Workflow steps

### Step 1: Load measured refractive index data
- Role: process
- Action: Read the bundled CSV file containing wavelength (microns) and the measured refractive index (arithmetical mean of three fused silica specimens at 20°C). Prepare the data for fitting.
- Evidence: none

### Step 2: Fit three‑term Sellmeier dispersion equation
- Role: scored (load-bearing)
- Action: Fit the model n² − 1 = Σ_{i=1}^{3} A_i λ²/(λ² − λ_i²) to the measured data using nonlinear least squares. Compute the predicted refractive indices, calculate the per‑wavelength absolute residuals, and derive the overall average absolute residual. Write the fitted parameters (A1, λ1, A2, λ2, A3, λ3) and the average residual to /app/outputs/sellmeier_results.json.
- Output file: `/app/outputs/sellmeier_results.json`
- Format: json
- Contract: { "fitted_parameters": { "A1": number, "lambda1": number, "A2": number, "lambda2": number, "A3": number, "lambda3": number }, "overall_average_absolute_residual": number }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sellmeier_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sellmeier_results.json
- path: `/app/outputs/sellmeier_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Fitted Sellmeier parameters and the overall average absolute residual. The checker recomputes the residual from the fitted parameters and the hidden measured data; the reported residual is not trusted.
- schema:
  - `type`: object
  - `required`: `fitted_parameters`, `overall_average_absolute_residual`
  - `properties`:
    - `fitted_parameters`:
      - `type`: object
      - `required`: `A1`, `lambda1`, `A2`, `lambda2`, `A3`, `lambda3`
      - `properties`:
        - `A1`:
          - `type`: number
        - `lambda1`:
          - `type`: number
        - `A2`:
          - `type`: number
        - `lambda2`:
          - `type`: number
        - `A3`:
          - `type`: number
        - `lambda3`:
          - `type`: number
    - `overall_average_absolute_residual`:
      - `type`: number

Notes: The checker recomputes the per‑wavelength average absolute residual from the agent's fitted parameters and the hidden reference refractive indices. The fitted parameters are also compared to the paper‑reported values within a tolerance. Both checks contribute to the final score.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sellmeier_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "fitted_parameters",
          "overall_average_absolute_residual"
        ],
        "properties": {
          "fitted_parameters": {
            "type": "object",
            "required": [
              "A1",
              "lambda1",
              "A2",
              "lambda2",
              "A3",
              "lambda3"
            ],
            "properties": {
              "A1": {
                "type": "number"
              },
              "lambda1": {
                "type": "number"
              },
              "A2": {
                "type": "number"
              },
              "lambda2": {
                "type": "number"
              },
              "A3": {
                "type": "number"
              },
              "lambda3": {
                "type": "number"
              }
            }
          },
          "overall_average_absolute_residual": {
            "type": "number"
          }
        }
      },
      "description": "Fitted Sellmeier parameters and the overall average absolute residual. The checker recomputes the residual from the fitted parameters and the hidden measured data; the reported residual is not trusted."
    }
  ],
  "notes": "The checker recomputes the per‑wavelength average absolute residual from the agent's fitted parameters and the hidden reference refractive indices. The fitted parameters are also compared to the paper‑reported values within a tolerance. Both checks contribute to the final score."
}
```

## How you are scored
A hidden verifier independently evaluates your sellmeier_results.json. It performs two checks:
1. **Residual recomputation**: The verifier recomputes the per‑wavelength absolute residuals from your reported parameters and the hidden reference refractive‑index values (the same 60 wavelengths you trained on). From those it calculates the overall average absolute residual and compares it to a reference threshold; a lower residual is better, and meeting or beating the threshold earns full credit.
2. **Parameter consistency**: The six fitted parameters are compared to hidden reference values within a tolerance to verify they are physically reasonable and consistent with the dispersion of high‑purity fused silica.

Both checks contribute to a total score between 0 and 1. There is no need to reproduce any specific number; the verifier judges the quality of your fit and the consistency of your parameters.
