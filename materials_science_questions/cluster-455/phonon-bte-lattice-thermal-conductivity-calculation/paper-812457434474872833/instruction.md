# Composition-based machine learning prediction of thermal conductivity for candidate oxide compositions

## Problem background
Discovering new oxide materials with low thermal conductivity requires exploring vast quaternary phase fields, where most possible compositions have unknown structures and properties. When structures are not known, structure-based property models cannot be applied. In such settings, composition-only machine learning models that predict lattice thermal conductivity (κ) solely from composition offer a way to rank candidate compositional regions and guide synthetic effort. This task involves building and evaluating such models on publicly available thermal-conductivity datasets, then applying them to a set of hypothetical probe-structure compositions in the Y–Sr–Ti–O and Y–Ba–Ti–O phase fields to predict their κ and assess the relative promise of different compositional regions.

## Approach
The approach uses Matminer to convert each composition into a vector of 121 composition-derived features. Two regression model types—a neural network and a random forest—are trained on a combined dataset of experimental and computational thermal-conductivity values from Gaultois et al. (2013) and TEDesignLab (2016). An 80/20 random split is used to create a validation set, and the model that achieves R² > 0.65 and MSE < 19 W² m⁻² K⁻² (or the best of the two if both meet) is selected. The trained model is then applied to the full list of probe-structure compositions. Each composition is assigned a phase field (Y–Sr–Ti–O or Y–Ba–Ti–O based on the presence of Sr or Ba) and a triangle membership label: “white” if it lies inside the triangle defined by Ba₀.₆₆₇Y₀.₁₆₇Ti₀.₁₆₇O₁.₂₅, Ba₀.₅Y₀.₃₃₃Ti₀.₁₆₇O₁.₃₃₃, and Ba₀.₅Y₀.₂₅Ti₀.₂₅O₁.₃₇₅; “grey” if inside the triangle defined by Ba₀.₁₆₇Y₀.₃₃₃Ti₀.₅O₁.₆₆₇, Ba₀.₁₆₇Y₀.₁₆₇Ti₀.₆₆₇O₁.₇₅, and Ba₆Y₂Ti₄O₁₇; otherwise “none”. The per‑composition predictions are saved to a CSV file for downstream analysis.

## Reproduction target
Build and train composition-only regression models on the combined Gaultois/TEDesignLab thermal-conductivity dataset. The selected model must meet validation‑set thresholds of R² > 0.65 and MSE < 19 W² m⁻² K⁻². Apply the model to the probe‑structure composition list and produce a CSV file (predictions.csv) with columns composition, predicted_kappa, phase_field, and triangle. Also record the chosen model’s type, validation R², validation MSE, and training‑data source in a JSON file (model_performance.json). The outputs allow an independent verifier to recompute the average predicted κ for the white and grey triangle regions and to compare the Y–Ba–Ti–O and Y–Sr–Ti–O phase fields.

## Assets

- Thermal conductivity training data: http://datacat.liverpool.ac.uk/id/eprint/1047
- Probe structure composition list: http://datacat.liverpool.ac.uk/id/eprint/1047
- Matminer: matminer
- scikit-learn: scikit-learn
- Neural network framework (TensorFlow or PyTorch): tensorflow # or torch as preferred by the solver
- numpy, pandas: numpy,pandas

## Workflow steps

### Step 1: Prepare training data
- Role: process
- Action: Load the thermal conductivity training dataset from the paper's data repository (or original sources). Featurize each composition using the Matminer composition featurizer (121 features). Split the data into training and validation sets (e.g., 80/20 random split).
- Evidence: `/app/outputs/training_data_shape.txt`

### Step 2: Train models and record performance
- Role: scored
- Action: Train a neural network regression model and a random forest regression model on the training set. Evaluate both models on the validation set, computing R² and MSE. Select the model that achieves R² > 0.65 and MSE < 19 W² m⁻² K⁻² (or the best performing if both meet). Write the selected model's performance and metadata to /app/outputs/model_performance.json.
- Output file: `/app/outputs/model_performance.json`
- Format: json
- Contract: JSON object with keys: "model_type" (string, one of "neural_network" or "random_forest"), "R2" (float), "MSE" (float, units W² m⁻² K⁻²), "training_data_source" (string).
- Scoring: scored by hidden verifier

### Step 3: Predict thermal conductivity for probe structures
- Role: scored (load-bearing)
- Action: Load the list of probe-structure compositions from the paper's data repository. Featurize each using the same Matminer featurizer. Use the trained model from step 2 to predict lattice thermal conductivity for every composition. Determine the phase field (Y-Sr-Ti-O or Y-Ba-Ti-O) from the presence of Sr or Ba. Assign triangle labels: compositions within the white triangle (bounded by Ba0.667Y0.167Ti0.167O1.25, Ba0.5Y0.333Ti0.167O1.333, Ba0.5Y0.25Ti0.25O1.375) -> "white"; compositions within the grey triangle (Ba0.167Y0.333Ti0.5O1.667, Ba0.167Y0.167Ti0.667O1.75, Ba6Y2Ti4O17) -> "grey"; all others -> "none". Write the results to /app/outputs/predictions.csv with columns: composition, predicted_kappa, phase_field, triangle.
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: CSV with columns: composition (string), predicted_kappa (float, W m⁻¹ K⁻¹), phase_field (string, one of Y-Sr-Ti-O or Y-Ba-Ti-O), triangle (string, one of white, grey, none). One row per probe-structure composition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_performance.json`
- `/app/outputs/predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_performance.json
- path: `/app/outputs/model_performance.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Validation performance of the selected composition-only regression model. The solver must train and choose a model meeting R² > 0.65 and MSE < 19 W² m⁻² K⁻²; the checker verifies these thresholds.
- schema:
  - `type`: object
  - `required`:
    - `model_type`: string
    - `R2`: float
    - `MSE`: float
    - `training_data_source`: string
  - `units`:
    - `MSE`: W² m⁻² K⁻²

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw per-composition predictions of lattice thermal conductivity. The checker recomputes the average predicted κ for the white and grey triangle regions and compares them to hidden reference values, and also checks that the Ba-field average is lower than the Sr-field average.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `predicted_kappa`, `phase_field`, `triangle`
  - `units`:
    - `predicted_kappa`: W m⁻¹ K⁻¹

Notes: The DFT probe-structure energy calculations are excluded (taskability scope). The two required scored outputs are model performance (thresholds) and the raw prediction table (recomputed for triangle averages). The training and validation split is the solver's choice; the checker uses paper-reported thresholds for model quality and paper-reported triangle averages for the main prediction claim.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model_performance.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "model_type": "string",
          "R2": "float",
          "MSE": "float",
          "training_data_source": "string"
        },
        "units": {
          "MSE": "W² m⁻² K⁻²"
        }
      },
      "description": "Validation performance of the selected composition-only regression model. The solver must train and choose a model meeting R² > 0.65 and MSE < 19 W² m⁻² K⁻²; the checker verifies these thresholds."
    },
    {
      "file": "predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "predicted_kappa",
          "phase_field",
          "triangle"
        ],
        "units": {
          "predicted_kappa": "W m⁻¹ K⁻¹"
        }
      },
      "description": "Raw per-composition predictions of lattice thermal conductivity. The checker recomputes the average predicted κ for the white and grey triangle regions and compares them to hidden reference values, and also checks that the Ba-field average is lower than the Sr-field average."
    }
  ],
  "notes": "The DFT probe-structure energy calculations are excluded (taskability scope). The two required scored outputs are model performance (thresholds) and the raw prediction table (recomputed for triangle averages). The training and validation split is the solver's choice; the checker uses paper-reported thresholds for model quality and paper-reported triangle averages for the main prediction claim."
}
```

## How you are scored
A hidden verifier checks each required output artifact independently and combines the scores into a final reward.

- **model_performance.json** – the verifier reads the reported R² and MSE and confirms that R² > 0.65 and MSE < 19 W² m⁻² K⁻². Meeting these thresholds is required; exact values beyond that are not penalised.
- **predictions.csv** – the verifier loads the table and recomputes the average predicted κ for the compositions belonging to the white triangle and the grey triangle. These recomputed averages are compared to hidden reference values. The verifier also computes the overall average predicted κ for the Y–Ba–Ti–O and Y–Sr–Ti–O phase fields and checks that the relative ordering aligns with the paper’s findings.

Only the artifacts you write to `/app/outputs` are evaluated. The verifier does not access your code, training logs, or intermediate files. Simply achieving the magic numbers from the paper is not enough; your model must be trained on the required dataset and produce predictions that, when aggregated, satisfy the hidden checks.
