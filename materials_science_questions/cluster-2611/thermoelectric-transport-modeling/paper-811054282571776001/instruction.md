# Predict Zintl Phase Structure Type from Electronegativity Ratio

## Problem background
Zintl phases with the formula A5M2Pn6, where A is an alkaline-earth or rare-earth metal, M is a triel (group 13), and Pn is a pnictogen (group 15), crystallize in two distinct structure types. In the Ca5Ga2As6 type, adjacent one-dimensional MPn4 tetrahedral chains are connected by Pn–Pn dimer bridges. In the Sr5Sn2P6 type, the chains remain separate with no Pn–Pn bonding. Understanding what drives the formation of bridging bonds is essential for predicting and tuning properties. A proposed rule links the bonding preference to the electronegativity of the anionic elements: the ratio of the Pauling electronegativity of the pnictogen to that of the triel (Pn/M) may determine which structure is adopted. This task asks you to investigate that rule by implementing a simple electronegativity-ratio classifier and evaluating its accuracy on a given list of compounds.

## Approach
The structural type can be predicted by a simple rule based on the electronegativity ratio of the pnictogen to the triel. Specifically, if the ratio Pn/M exceeds 1.125, the compound is expected to adopt the bridged (Ca5Ga2As6) type with Pn–Pn bonds; otherwise, it adopts the unbridged (Sr5Sn2P6) type. To implement the rule, you need the Pauling electronegativity values for each element (these are widely available constants), compute the ratio for each compound, and make a binary prediction. No model training or complex simulation is required; the task tests the predictive power of this heuristic rule.

## Reproduction target
For the provided list of seven A5M2Pn6 compounds (Ca5Sn2As6, Sr5Sn2As6, Sr5Sn2P6, Ca5Ga2Sb6, Ca5In2Sb6, Ca5Ga2As6, Ca5Al2Sb6), use the electronegativity-ratio rule to predict whether each compound adopts the bridged or unbridged structure type. Write your predictions to a CSV file with columns 'compound' and 'prediction'. The predictions will be evaluated against the true structure types (sourced from the crystallographic literature) using classification accuracy.

## Assets
No external datasets, files, or packages are required. The Pauling electronegativity values for all the elements involved (Ca, Sr, Sn, P, As, Ga, Sb, In, Al) are publicly available constants and can be hardcoded directly into your script or looked up from any standard chemistry reference. A standard Python environment is sufficient.

## Workflow steps

### Step 1: Predict structure type
- Role: scored
- Action: For each compound in the provided list (Ca5Sn2As6, Sr5Sn2As6, Sr5Sn2P6, Ca5Ga2Sb6, Ca5In2Sb6, Ca5Ga2As6, Ca5Al2Sb6), compute the ratio of the Pauling electronegativity of the pnictogen (Pn) to that of the triel (M). If the ratio is greater than 1.125, predict 'bridged'; otherwise predict 'unbridged'. Write the results to predictions.csv with columns compound and prediction.
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: CSV with columns: compound (string), prediction (string, one of 'bridged' or 'unbridged')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted structure type for each compound. The prediction must be either 'bridged' or 'unbridged'.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `prediction`
  - `units`: object

Notes: The hidden checker holds the ground-truth structure types for a set of A5M2Pn6 compounds and computes accuracy. The passing threshold is accuracy >= 0.90, with linear scaling down to 0 at 0.0 accuracy.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "prediction"
        ],
        "units": {}
      },
      "description": "Predicted structure type for each compound. The prediction must be either 'bridged' or 'unbridged'."
    }
  ],
  "notes": "The hidden checker holds the ground-truth structure types for a set of A5M2Pn6 compounds and computes accuracy. The passing threshold is accuracy >= 0.90, with linear scaling down to 0 at 0.0 accuracy."
}
```

## How you are scored
Your predictions.csv file will be compared against hidden ground-truth labels by an automated verifier. The verifier computes the accuracy (the fraction of compounds correctly classified) and translates it into a reward score. Perfect or near-perfect classification earns full credit; lower accuracies receive lower credit. The exact scoring function and acceptance threshold are not disclosed, so aim to classify every compound correctly.
