# TCIT Enthalpy of Formation Prediction Benchmark

## Problem background
Predicting gas-phase enthalpy of formation (ΔHf) is fundamental for evaluating reaction thermodynamics and molecular stability. Group increment theories decompose molecular ΔHf into additive contributions from chemically defined groups, enabling rapid predictions across large compound sets. Component increment theories refine this by increasing the chemical specificity of each additive unit, which can capture subtle steric and electronic effects. This task evaluates a self-consistent component increment theory (TCIT) that derives all component additivity values (CAVs) solely from quantum chemistry calculations on algorithmically generated model compounds, without empirical fitting to experimental data.

## Approach
TCIT decomposes gas-phase ΔHf of an acyclic molecule into the sum of CAVs, one for each non-terminal atom as defined by its local bonding graph out to two bonds. All CAVs are pre‑parameterized from Gaussian‑4 (G4) quantum chemistry results on small model compounds that are systematically generated from the target molecules. When all required CAVs are present in the database, predictions require no further computation beyond summing the component contributions. In this task, you will use a provided Python implementation of TCIT together with a pre‑computed CAV database to predict ΔHf for a set of 278 acyclic molecules from the PNK experimental benchmark that were not used as model compounds. You will then compare the predictions to the experimental reference values by computing the mean absolute error (MAE) and mean signed error (MSE).

## Reproduction target
Generate TCIT gas‑phase ΔHf predictions (kJ/mol) for the 278 non‑model acyclic compounds from the PNK benchmark dataset using the TCIT package and CAV database provided in the paper's Supporting Information. Then compute the mean absolute error (MAE) and mean signed error (MSE) between the predicted values and the experimental ΔHf values for the same compounds.

## Assets

- Supporting Information ZIP (TCIT Python implementation and CAV database): https://pubs.acs.org/doi/suppl/10.1021/acs.jcim.0c00092

## Workflow steps

### Step 1: Predict ΔHf for the 278 test compounds
- Role: scored
- Action: Use the TCIT implementation and CAV database from the Supporting Information to predict the gas-phase enthalpy of formation (ΔHf, kJ/mol) for each of the 278 non-model acyclic PNK benchmark compounds (SMILES list extracted from the SI). Write predictions.csv.
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: SMILES:string, predicted_delta_Hf_kJmol:float
- Scoring: scored by hidden verifier

### Step 2: Compute evaluation metrics
- Role: scored
- Action: Calculate the mean absolute error (MAE) and mean signed error (MSE) between the TCIT predictions (from predictions.csv) and the experimental ΔHf values (obtained from the PNK dataset). Write summary_metrics.json.
- Output file: `/app/outputs/summary_metrics.json`
- Format: json
- Contract: {"MAE_kJmol": float, "MSE_kJmol": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.csv`
- `/app/outputs/summary_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: TCIT-predicted gas-phase enthalpy of formation for each of the 278 non-model acyclic benchmark compounds.
- schema:
  - `type`: table
  - `required_columns`: `SMILES`, `predicted_delta_Hf_kJmol`
  - `units`:
    - `predicted_delta_Hf_kJmol`: kJ/mol

### summary_metrics.json
- path: `/app/outputs/summary_metrics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mean absolute error and mean signed error computed against experimental ΔHf values. The checker will verify these are consistent with its recomputed values.
- schema:
  - `type`: object
  - `required`:
    - `MAE_kJmol`: float (kJ/mol)
    - `MSE_kJmol`: float (kJ/mol)

Notes: The checker will recompute MAE and MSE from predictions.csv using hidden gold experimental ΔHf values and score using threshold_or_better (full reward if MAE ≤ 5.0 kJ/mol and |MSE| ≤ 1.0 kJ/mol, with reward decaying proportionally beyond). It will also check that summary_metrics.json values match the recomputed metrics within a small tolerance.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "SMILES",
          "predicted_delta_Hf_kJmol"
        ],
        "units": {
          "predicted_delta_Hf_kJmol": "kJ/mol"
        }
      },
      "description": "TCIT-predicted gas-phase enthalpy of formation for each of the 278 non-model acyclic benchmark compounds."
    },
    {
      "file": "summary_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "MAE_kJmol": "float (kJ/mol)",
          "MSE_kJmol": "float (kJ/mol)"
        }
      },
      "description": "Mean absolute error and mean signed error computed against experimental ΔHf values. The checker will verify these are consistent with its recomputed values."
    }
  ],
  "notes": "The checker will recompute MAE and MSE from predictions.csv using hidden gold experimental ΔHf values and score using threshold_or_better (full reward if MAE ≤ 5.0 kJ/mol and |MSE| ≤ 1.0 kJ/mol, with reward decaying proportionally beyond). It will also check that summary_metrics.json values match the recomputed metrics within a small tolerance."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage's artifact. For Step 1, the verifier will load your predictions.csv, pair each SMILES with the corresponding experimental ΔHf from a hidden reference dataset, and recompute the MAE and MSE. For Step 2, it will verify that the values in summary_metrics.json are consistent with these recomputed metrics. The final reward is a combination of the two assessments, weighted primarily by the MAE/MSE scores: the closer your predictions are to the experimental values (lower MAE and absolute MSE), the higher your reward. There is no reward for simply reproducing a specific numeric target; the evaluation is monotonic in predictive quality.
