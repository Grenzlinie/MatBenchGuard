# Pressure-Dependent Electron Concentration Linear Regression

## Problem background
In zero-gap semiconductors such as HgSe, doping with certain 3d transition metals can create resonant donor states that pin the Fermi energy. According to the Kane model, if the Fermi level is pinned, the conduction electron concentration n follows a signature relationship with hydrostatic pressure P: n^{2/3} depends linearly on P, and the slope is related to the band-gap pressure coefficient. In contrast, if no resonant level is present, n is expected to be nearly independent of pressure. This task provides experimental electron concentrations measured at different pressures for three doped HgSe samples (two iron-doped and one cobalt-doped). The goal is to determine, for each sample, whether n^{2/3} varies linearly with pressure or remains constant, by performing a quantitative linear regression analysis.

## Approach
The task is a purely computational re-analysis of the provided data. A CSV file (bundled as data.csv) contains the electron concentration n (in units of 10^18 cm^{-3}) at pressures P = 0, 3, and 5 kbar for three samples identified by a sample_id column. The approach is to:
- Convert n from the given units to cm^{-3}.
- Compute n^{2/3} in units of cm^{-2} for each measurement.
- For each sample separately, fit a straight line n^{2/3} = a + b * P using ordinary least-squares linear regression on the three data points.
- Record the fitted slope b, intercept a, and the coefficient of determination R².

The differences in slope and linearity across samples are the quantities of interest; they indicate whether the data follow the constant-Fermi-level linear relationship or a pressure-independent behaviour.

## Reproduction target
Given the bundled data.csv, compute for each sample the slope (cm^{-2}/kbar), intercept (cm^{-2}), and R² of the linear regression of n^{2/3} vs pressure P. Write these results to /app/outputs/linear_fits.csv with columns sample_id, slope, intercept, r_squared. The slope and intercept units derive from n in cm^{-3} and P in kbar.

## Assets

- Experimental electron concentration vs pressure (Table 1)
- Python scientific computing packages: https://pypi.tuna.tsinghua.edu.cn/simple

## Workflow steps

### Step 1: Linear regression of n^{2/3} vs pressure
- Role: scored (load-bearing)
- Action: Load the bundled data.csv. For each sample, convert electron concentration n from units of 10^18 cm^{-3} to cm^{-3}, compute n^{2/3} in cm^{-2}, then perform ordinary least-squares linear regression of n^{2/3} against pressure P (in kbar) using the three data points. Write one row per sample to linear_fits.csv with columns: sample_id, slope (cm^{-2}/kbar), intercept (cm^{-2}), r_squared.
- Output file: `/app/outputs/linear_fits.csv`
- Format: csv
- Contract: sample_id (string), slope (float, cm^{-2}/kbar), intercept (float, cm^{-2}), r_squared (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/linear_fits.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### linear_fits.csv
- path: `/app/outputs/linear_fits.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing linear regression results of n^{2/3} vs hydrostatic pressure for three samples (two HgSe(Fe) and one HgSe(Co)).
- schema:
  - `type`: table
  - `required_columns`: `sample_id`, `slope`, `intercept`, `r_squared`
  - `units`:
    - `slope`: cm^{-2}/kbar
    - `intercept`: cm^{-2}
    - `r_squared`: dimensionless

Notes: The regression is performed on the three-point (P=0,3,5 kbar) dataset provided as data.csv. The checker will recompute the gold slopes and intercepts from the same data and compare the agent's values with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "linear_fits.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample_id",
          "slope",
          "intercept",
          "r_squared"
        ],
        "units": {
          "slope": "cm^{-2}/kbar",
          "intercept": "cm^{-2}",
          "r_squared": "dimensionless"
        }
      },
      "description": "CSV containing linear regression results of n^{2/3} vs hydrostatic pressure for three samples (two HgSe(Fe) and one HgSe(Co))."
    }
  ],
  "notes": "The regression is performed on the three-point (P=0,3,5 kbar) dataset provided as data.csv. The checker will recompute the gold slopes and intercepts from the same data and compare the agent's values with tolerances."
}
```

## How you are scored
A hidden verifier independently recomputes the gold-standard linear regression results from the same three-point dataset for each sample. It compares your reported slopes and intercepts against these recomputed values using appropriate tolerances that account for legitimate numerical differences in linear regression implementations. For the sample expected to have a nearly constant n, an additional check on the magnitude of the slope is applied. R² values are also compared. The final reward (a float between 0 and 1) is a weighted combination of the per-sample accuracy scores; reporting a paper-copied number without genuine computation will not pass these checks because the hidden tolerances are set to require correct derivation from the provided data points.
