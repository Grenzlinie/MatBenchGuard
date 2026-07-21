# Regression Models for High-Temperature Strength Prediction from Composition and SNIR Parameters

## Problem background
High-temperature nickel-base superalloys contain many alloying elements, making it difficult to predict properties such as high-temperature strength (endurance τ_m) from composition. This work investigates whether two parameters derived from the System of Nonpolarized Ionic Radii (SNIR), designated A and Zy, can serve as compact descriptors to replace explicit elemental mass fractions in predictive models. The goal is to determine if regression models using these SNIR parameters achieve comparable predictive accuracy to models that directly use the mass fractions of the key alloying elements Nb, V, Hf, and Ta.

## Approach
Four regression models are constructed to predict the endurance τ_m: two linear models and two exponential models. One linear and one exponential model use as inputs the mass fractions of Nb, V, Hf, and Ta; the other two use the SNIR parameters A and −2Zy. Each model is fitted to the provided dataset of 16 alloy melts by minimizing the sum of squared errors between predicted and experimental endurance values. After fitting, the mean absolute deviation δ = (1/16) Σ |τ_exp − τ_pred| is computed for each model as a measure of predictive accuracy.

The exact mathematical forms of the four regression models are:

- **Linear concentration-based:** τ_m = a_0 + a_1*Nb + a_2*V + a_3*Hf + a_4*Ta
- **Linear SNIR-based:** τ_m = a_0 + a_1*A + a_2*(-2Zy)
- **Exponential concentration-based:** τ_m = a_0 + a_1*Nb + a_2*V + a_3*Hf + a_4*Ta + a_5*exp(-b_5*Nb) + a_6*exp(-b_6*V) + a_7*exp(-b_7*Hf) + a_8*exp(-b_8*Ta)
- **Exponential SNIR-based:** τ_m = a_0 + a_1*A + a_2*(-2Zy) + a_3*exp(b_3*2Zy) + a_4*exp(b_4*A)

## Reproduction target
Using the provided dataset of 16 alloy melts (compositions, SNIR parameters A and −2Zy, and experimental endurance τ_m), fit the four regression models, compute the predicted endurance for each melt from each model, and calculate the mean absolute deviation δ for each model. Output the per-melt predictions in predictions.csv and the four δ values in model_performance.json.

## Assets

- SciPy: scipy
- NumPy: numpy

## Input Data

The following table provides the composition data (mass % of Nb, V, Hf, Ta), SNIR parameters A and -2Zy, and experimental endurance τ_m (hours) for the 16 alloy melts. This data must be used to fit the regression models.

| Alloy | Nb   | V    | Hf   | Ta   | A        | -2Zy     | τ_m,exp (h) |
|-------|------|------|------|------|----------|----------|--------------|
| 1     | 1.54 | 0.77 | 0.49 | 0.46 | 0.353224 | 4.56092  | 15.0         |
| 2     | 1.60 | 0.16 | 0.45 | 2.25 | 0.353449 | 4.58148  | 10.8         |
| 3     | 2.38 | 0.75 | 0.45 | 0.44 | 0.353523 | 4.59598  | 19.2         |
| 4     | 1.38 | 0.75 | 0.51 | 2.35 | 0.353551 | 4.61287  | 11.3         |
| 5     | 2.41 | 0.82 | 0.46 | 2.29 | 0.353933 | 4.66029  | 20.0         |
| 6     | 1.80 | 0.17 | 1.33 | 0.50 | 0.353532 | 4.56330  | 35.6         |
| 7     | 2.55 | 0.18 | 1.41 | 0.42 | 0.353838 | 4.59773  | 63.1         |
| 8     | 1.65 | 0.72 | 1.39 | 0.46 | 0.353593 | 4.58672  | 45.3         |
| 9     | 1.39 | 0.23 | 1.51 | 2.33 | 0.353832 | 4.61135  | 69.4         |
| 10    | 2.41 | 0.18 | 1.42 | 2.20 | 0.354159 | 4.64842  | 70.4         |
| 11    | 2.59 | 0.82 | 1.37 | 2.47 | 0.354392 | 4.69986  | 36.0         |
| 12    | 1.80 | 0.18 | 0.89 | 1.23 | 0.353513 | 4.57484  | 30.3         |
| 13    | 2.08 | 0.47 | 0.93 | 1.31 | 0.353710 | 4.60771  | 40.0         |
| 14    | 1.88 | 0.88 | 0.93 | 1.31 | 0.353721 | 4.62174  | 42.2         |
| 15    | 1.90 | 0.49 | 0.52 | 1.39 | 0.353507 | 4.59169  | 27.0         |
| 16    | 2.19 | 0.51 | 0.96 | 0.47 | 0.353604 | 4.58906  | 40.7         |

## Workflow steps

### Step 1: Fit regression models and generate predictions
- Role: scored
- Action: Load the provided alloy composition data (16 melts with Nb, V, Hf, Ta mass fractions, SNIR parameters A and -2Zy, and experimental endurance τ_m). Fit four regression models as specified: linear concentration-based, linear SNIR-based, exponential concentration-based, exponential SNIR-based, using a least-squares solver. Compute predicted endurance for each alloy and save to predictions.csv.
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: CSV with header: melt_id, tau_exp, linear_conc_pred, linear_snir_pred, exp_conc_pred, exp_snir_pred. Each row corresponds to one alloy melt. All prediction columns are floats.
- Scoring: scored by hidden verifier

### Step 2: Compute mean absolute deviation δ and output final metrics
- Role: scored (load-bearing)
- Action: Read predictions.csv. Compute the mean absolute deviation δ = (1/16) * Σ|tau_exp - tau_pred| for each of the four models (linear concentration, linear SNIR, exponential concentration, exponential SNIR). Write the four δ values to model_performance.json.
- Output file: `/app/outputs/model_performance.json`
- Format: json
- Contract: JSON object with fields: linear_concentration_delta, linear_snir_delta, exponential_concentration_delta, exponential_snir_delta. All values are positive floats (hours).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.csv`
- `/app/outputs/model_performance.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Per-alloy predicted endurance values used by the checker to recompute δ. Existence and schema are verified.
- schema:
  - `type`: table
  - `required_columns`: `melt_id`, `tau_exp`, `linear_conc_pred`, `linear_snir_pred`, `exp_conc_pred`, `exp_snir_pred`

### model_performance.json
- path: `/app/outputs/model_performance.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The computed δ values. The checker compares them to the paper's reported values (lower is better) and verifies relative trends (exponential δ < linear δ; SNIR δ within 2.0 of concentration δ).
- schema:
  - `type`: object
  - `required`:
    - `linear_concentration_delta`: float
    - `linear_snir_delta`: float
    - `exponential_concentration_delta`: float
    - `exponential_snir_delta`: float

Notes: The alloy composition data and SNIR parameters are provided inline in the Input Data section of the instruction (16 melts). The agent must fit the models and output the predictions and δ values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "melt_id",
          "tau_exp",
          "linear_conc_pred",
          "linear_snir_pred",
          "exp_conc_pred",
          "exp_snir_pred"
        ]
      },
      "description": "Per-alloy predicted endurance values used by the checker to recompute δ. Existence and schema are verified."
    },
    {
      "file": "model_performance.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "linear_concentration_delta": "float",
          "linear_snir_delta": "float",
          "exponential_concentration_delta": "float",
          "exponential_snir_delta": "float"
        }
      },
      "description": "The computed δ values. The checker compares them to the paper's reported values (lower is better) and verifies relative trends (exponential δ < linear δ; SNIR δ within 2.0 of concentration δ)."
    }
  ],
  "notes": "The alloy composition data and SNIR parameters are provided inline in the Input Data section of the instruction (16 melts). The agent must fit the models and output the predictions and δ values."
}
```

## How you are scored
A hidden verifier reads your output files and independently recomputes the δ values from predictions.csv to cross-check them. It then compares your δ values and the structure of the predictions to expected criteria derived from the paper's experimental data and modeling results. The verifier assigns a weighted score across the two workflow stages; the final reward is a float between 0 and 1. Simply hard-coding the paper's reported numbers without performing the required regression fitting will not pass, because the verifier checks for internal consistency and correct relationships between the predictions and the experimental data.
