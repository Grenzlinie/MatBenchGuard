# Refractive Index Interpolation at 193.39 nm from Measured DUV Data

## Problem background
Synthetic fused silica and calcium fluoride are critical optical materials for deep-ultraviolet (DUV) photolithography at 193.39 nm, the emission wavelength of ArF excimer lasers. Designing high-performance lens systems requires highly accurate refractive-index data in this wavelength region. While optical constants are well mapped in the visible and near UV, precise absolute refractive indices below 200 nm were scarce historically, with most published measurements stopping above 200 nm. This task provides measured refractive-index data for multiple fused silica and calcium fluoride samples at seven DUV wavelengths between 191 and 196 nm, and asks you to compute the refractive index and its dispersion at 193.39 nm by polynomial interpolation.

## Approach
Given per-sample measured refractive indices at several vacuum wavelengths in the DUV, a quadratic polynomial
n(λ) = a₀ + a₁ λ + a₂ λ²
is fit to the (wavelength, index) pairs using ordinary least squares. For each sample, the fitted polynomial is then evaluated at λ = 193.39 nm to yield the refractive index, and the dispersion is computed as
dn/dλ = a₁ + 2 a₂ × 193.39.
No additional physical model is required; the interpolation relies solely on the supplied measurement tables and a least-squares polynomial fit.

## Reproduction target
Produce two CSV files:
1. **fitted_indices.csv** – For every sample (8 fused silica and 3 calcium fluoride), report the interpolated refractive index at 193.39 nm and the dispersion dn/dλ.
2. **fitted_coefficients.csv** – For each sample, report the three quadratic polynomial coefficients a₀, a₁, a₂.
All values must be derived from the provided measured indices using the quadratic fitting procedure described above.

## Assets

- fused_silica_indices.csv
- calcium_fluoride_indices.csv
- duv_wavelengths.csv
- numpy: numpy

## Workflow steps

### Step 1: Load and prepare measurement data
- Role: process
- Action: Load the provided CSV files (fused_silica_indices.csv, calcium_fluoride_indices.csv, duv_wavelengths.csv). For each sample, remove any measurements marked as 'not obs.' or otherwise incomplete, keeping only complete (wavelength, index) pairs.
- Evidence: `/app/outputs/data_preprocessing.log`

### Step 2: Fit quadratic polynomials and compute n(193.39) and dn/dλ
- Role: scored (load-bearing)
- Action: For each sample (8 fused silica: A1, A2, A3, B1, B2, B3, C1, C2; 3 calcium fluoride: A1, A2, B) perform a least-squares fit of the model n(λ)=a0 + a1*λ + a2*λ^2 to its (wavelength, index) data. Evaluate the fitted polynomial at λ = 193.39 nm to obtain the refractive index, and compute the dispersion dn/dλ = a1 + 2*a2*193.39. Write the results to fitted_indices.csv.
- Output file: `/app/outputs/fitted_indices.csv`
- Format: csv
- Contract: CSV with columns: sample (string), material (either 'fused_silica' or 'calcium_fluoride'), n_193.39 (float), dn_dlambda (float)
- Scoring: scored by hidden verifier

### Step 3: Write fitted polynomial coefficients
- Role: scored
- Action: Extract the fitted coefficients a0, a1, a2 for each sample from the polynomials obtained in step 2, and write them to fitted_coefficients.csv.
- Output file: `/app/outputs/fitted_coefficients.csv`
- Format: csv
- Contract: CSV with columns: sample (string), material (string), a0 (float), a1 (float), a2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_indices.csv`
- `/app/outputs/fitted_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_indices.csv
- path: `/app/outputs/fitted_indices.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Refractive index and dispersion at 193.39 nm obtained by quadratic polynomial interpolation for all measured samples.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `material`, `n_193.39`, `dn_dlambda`
  - `units`:
    - `n_193.39`: dimensionless
    - `dn_dlambda`: nm^{-1}

### fitted_coefficients.csv
- path: `/app/outputs/fitted_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Quadratic polynomial coefficients n(λ)=a0 + a1*λ + a2*λ^2 that best fit the measured index data for each sample.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `material`, `a0`, `a1`, `a2`
  - `units`:
    - `a0`: dimensionless
    - `a1`: nm^{-1}
    - `a2`: nm^{-2}

Notes: The output files report the results of quadratic interpolation using the least-squares method on the provided measured indices. All reported values are expected at 20 °C and for the ArF laser wavelength 193.39 nm.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_indices.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "material",
          "n_193.39",
          "dn_dlambda"
        ],
        "units": {
          "n_193.39": "dimensionless",
          "dn_dlambda": "nm^{-1}"
        }
      },
      "description": "Refractive index and dispersion at 193.39 nm obtained by quadratic polynomial interpolation for all measured samples."
    },
    {
      "file": "fitted_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "material",
          "a0",
          "a1",
          "a2"
        ],
        "units": {
          "a0": "dimensionless",
          "a1": "nm^{-1}",
          "a2": "nm^{-2}"
        }
      },
      "description": "Quadratic polynomial coefficients n(λ)=a0 + a1*λ + a2*λ^2 that best fit the measured index data for each sample."
    }
  ],
  "notes": "The output files report the results of quadratic interpolation using the least-squares method on the provided measured indices. All reported values are expected at 20 °C and for the ArF laser wavelength 193.39 nm."
}
```

## How you are scored
Your submitted CSV files are examined by a hidden verifier. It compares each numeric field (refractive index, dispersion, and each coefficient) against reference results obtained by applying the same quadratic interpolation to the identical input data. The overall score is the proportion of individual comparisons that fall within pre‑set absolute tolerances. A higher proportion of matches yields a higher reward. Do not simply copy any external number; the verifier checks consistency with the polynomial fit.
