# ANOVA, NSGA-II Optimization, and Machine Learning Modeling of Laser Cladding Process Parameters for Coating Properties

## Problem background
Laser cladding of lightweight refractory high-entropy alloy coatings is used to produce wear-resistant surfaces, but the resulting porosity, dilution, and microhardness are highly sensitive to the processing parameters: laser power (LP), scanning speed (SS), and powder feeding speed (PF). The central challenge is to understand and control these relationships to produce coatings with minimal porosity, a target dilution around 25%, and maximized microhardness. This task uses a 25-sample orthogonal experimental dataset to quantitatively assess how LP, SS, and PF contribute to each property, to identify optimal parameter settings via multi-objective optimization, and to build predictive machine-learning models that capture the nonlinear input–output mapping.

## Approach
The workflow consists of three main stages:

1. **Analysis of variance (ANOVA)** – From the raw experimental data, the contribution percentage and p‑value of each process variable (LP, SS, PF) to the variability of porosity (P), dilution (D), and microhardness (MH) are computed. This provides a quantitative ranking of parameter importance.

2. **Multi‑objective optimization with NSGA‑II** – Quadratic polynomial surrogate models are first fitted to the data for each target (P, D, MH) as functions of the three inputs (including linear, quadratic, and interaction terms). These surrogates serve as objective functions. The NSGA‑II algorithm then searches for Pareto‑optimal (LP, SS, PF) combinations that simultaneously minimize porosity, minimize the absolute deviation of dilution from 25%, and maximize microhardness. A single best‑compromise solution is selected from the Pareto front.

3. **Machine‑learning predictive modeling** – Using the z‑score normalized dataset, three regression models are trained and compared: Random Forest (RF), Gradient Boosting Decision Tree (GBDT), and a Genetic Algorithm‑optimized GBDT (GA‑GBDT). For GA‑GBDT, a genetic algorithm tunes the GBDT hyperparameters. All models are evaluated with 5‑fold cross‑validation on the 20 training samples, and the average R², MAE, and RMSE are reported for each model‑target pair (P, D, MH).

## Reproduction target
Use the provided 25‑sample orthogonal experimental dataset (columns: LP, SS, PF, P, D, MH) to produce three scored artifacts:

- **step_01_anova_contributions.csv** – A table of contribution percentages and p‑values for each factor–response combination.
- **step_02_nsga2_optimal.csv** – The optimal LP, SS, PF obtained by NSGA‑II together with the predicted P, D, and MH at that point.
- **step_03_ml_metrics.csv** – Cross‑validated R², MAE, and RMSE for RF, GBDT, and GA‑GBDT on each target.

All outputs must be derived solely from the given experimental data using the workflow described in the steps.

## Assets

- Orthogonal experimental data (25 samples) with LP, SS, PF and P, D, MH

## Workflow steps

### Step 1: Z-score normalization of experimental data
- Role: process
- Action: Load the experimental dataset (25 samples). Compute mean and standard deviation for each variable (LP, SS, PF, P, D, MH). Apply z-score normalization to all variables to obtain a normalized dataset. Save the normalized data as normalized_data.csv.
- Evidence: `/app/outputs/normalized_data.csv`

### Step 2: Analysis of variance (ANOVA) of process effects on coating properties
- Role: scored (load-bearing)
- Action: Perform ANOVA on the raw experimental data to compute the contribution percentage and p-value of each process variable (LP, SS, PF) to the variance in porosity (P), dilution (D), and microhardness (MH).
- Output file: `/app/outputs/step_01_anova_contributions.csv`
- Format: csv
- Contract: response, factor, contribution_%, p_value
- Scoring: scored by hidden verifier

### Step 3: Fit polynomial surrogate models for objective functions
- Role: process
- Action: Using the raw experimental data, fit quadratic polynomial regression models for each of the three targets (P, D, MH) as functions of the three input variables LP, SS, PF (including linear, quadratic, and interaction terms). Save the model coefficients in a JSON file.
- Evidence: `/app/outputs/surrogate_models.json`

### Step 4: Multi-objective optimization using NSGA-II
- Role: scored (load-bearing)
- Action: Implement the NSGA-II algorithm to find Pareto-optimal processing parameters (LP, SS, PF) that simultaneously minimize porosity P, minimize absolute deviation of dilution D from 25%, and maximize microhardness MH. Use the polynomial surrogate models from step3 as the objective functions. From the obtained Pareto front, select a single optimal set of parameters and report the optimized LP, SS, PF and the corresponding predicted P, D, MH.
- Output file: `/app/outputs/step_02_nsga2_optimal.csv`
- Format: csv
- Contract: LP_opt, SS_opt, PF_opt, P_pred, D_pred, MH_pred
- Scoring: scored by hidden verifier

### Step 5: Machine learning model training and cross-validation
- Role: scored
- Action: Using the z-score normalized dataset (step1), train and evaluate three regression models (Random Forest, Gradient Boosting Decision Tree, and a GA-optimized GBDT) to predict each of the three targets (P, D, MH) from the inputs LP, SS, PF. For GA-GBDT, implement a genetic algorithm to optimize GBDT hyperparameters. Use 5-fold cross-validation on the 20 training samples and compute the average R², MAE, and RMSE across folds for each model-target pair. Output the results.
- Output file: `/app/outputs/step_03_ml_metrics.csv`
- Format: csv
- Contract: model, target, R2, MAE, RMSE
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_anova_contributions.csv`
- `/app/outputs/step_02_nsga2_optimal.csv`
- `/app/outputs/step_03_ml_metrics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_anova_contributions.csv
- path: `/app/outputs/step_01_anova_contributions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: ANOVA fractional contributions and p-values for each factor on each response (porosity, dilution, microhardness).
- schema:
  - `type`: table
  - `required_columns`: `response`, `factor`, `contribution_%`, `p_value`

### step_02_nsga2_optimal.csv
- path: `/app/outputs/step_02_nsga2_optimal.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimal processing parameters and predicted coating properties obtained from NSGA-II.
- schema:
  - `type`: table
  - `required_columns`: `LP_opt`, `SS_opt`, `PF_opt`, `P_pred`, `D_pred`, `MH_pred`

### step_03_ml_metrics.csv
- path: `/app/outputs/step_03_ml_metrics.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Cross-validation performance metrics (R², MAE, RMSE) for RF, GBDT, and GA-GBDT on porosity, dilution, and microhardness.
- schema:
  - `type`: table
  - `required_columns`: `model`, `target`, `R2`, `MAE`, `RMSE`

Notes: All scored artifacts are compared against paper-reported reference values with appropriate tolerances; ML metrics use directional thresholds to reward equal or better performance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_anova_contributions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "response",
          "factor",
          "contribution_%",
          "p_value"
        ]
      },
      "description": "ANOVA fractional contributions and p-values for each factor on each response (porosity, dilution, microhardness)."
    },
    {
      "file": "step_02_nsga2_optimal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "LP_opt",
          "SS_opt",
          "PF_opt",
          "P_pred",
          "D_pred",
          "MH_pred"
        ]
      },
      "description": "Optimal processing parameters and predicted coating properties obtained from NSGA-II."
    },
    {
      "file": "step_03_ml_metrics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "target",
          "R2",
          "MAE",
          "RMSE"
        ]
      },
      "description": "Cross-validation performance metrics (R², MAE, RMSE) for RF, GBDT, and GA-GBDT on porosity, dilution, and microhardness."
    }
  ],
  "notes": "All scored artifacts are compared against paper-reported reference values with appropriate tolerances; ML metrics use directional thresholds to reward equal or better performance."
}
```

## How you are scored
A hidden verifier scores each output artifact independently against reference values extracted from the original study. The checks use appropriate tolerances and directional thresholds (e.g., lower error is always better; higher R² is rewarded). The verifier does not require exact replication of the reference numbers – improvements over the reported performance are accepted and earn full credit. The final reward is a weighted sum of the three stage scores. No single number needs to be matched exactly; what matters is that the computational pipeline produces results that are plausible, consistent, and close to the physical targets.
