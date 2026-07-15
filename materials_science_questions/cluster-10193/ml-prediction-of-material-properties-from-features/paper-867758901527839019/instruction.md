# Transformer-based Oxidation State Prediction from Chemical Composition

## Problem background
Oxidation states (OS) are fundamental to understanding chemical bonding, reaction mechanisms, and material stability.  Assigning OS from chemical composition alone is challenging because many elements can adopt multiple oxidation states depending on their local environment.  While heuristic rules exist, they are limited and often fail for complex compounds.  Machine learning models have recently been applied to predict OS, but most rely on structural information, which is unavailable in high‑throughput screening of hypothetical compositions.  This task focuses on a composition‑based approach: predicting the oxidation states of every atom in an inorganic compound using only its formula.

## Approach
The core idea is to formulate oxidation state prediction as a token classification problem in natural language processing.  A chemical formula is expanded into a sequence of element tokens (ordered by electronegativity), and a BERT transformer language model is trained to predict the oxidation state of each token.  The model consists of a Bidirectional Encoder Representations from Transformers (BERT) network to learn contextual representations of each token, followed by a shared feedforward classification head that maps each token representation to an oxidation state integer.  The model is trained in a supervised manner on datasets derived from the Inorganic Crystal Structure Database (ICSD).  The training data provides element sequences and the true oxidation state of each atom.  The workflow uses provided pre‑defined training/validation/test splits for two datasets: a general set (OS‑ICSD) and a subset restricted to oxides (OS‑ICSD‑oxide).  The task requires implementing the BERT token classification architecture, training on each training set, and evaluating on the corresponding test set.

## Reproduction target
Train two BERTOS models: one on the OS‑ICSD training set and one on the OS‑ICSD‑oxide training set.  For each model, generate per‑atom oxidation state predictions on the respective test set and output a CSV file with columns: composition, element, true_oxidation_state, predicted_oxidation_state.  Then compute the following evaluation metrics from those predictions:
- overall site‑level accuracy (percentage of atom sites with correct oxidation state),
- compound‑level accuracy (percentage of compounds for which all atoms are correctly predicted),
- per‑element site‑level accuracy (a dictionary mapping each element to its accuracy).
Store these metrics in a JSON file.  The process must be executed for both datasets, producing four output files.

## Assets

- BERTOS code and datasets: http://www.github.com/usccolumbia/BERTOS
- PyTorch: torch
- Hugging Face Transformers: transformers
- NumPy: numpy
- scikit-learn: scikit-learn
- pandas: pandas

## Workflow steps

### Step 1: Train BERTOS on OS-ICSD training set
- Role: process
- Action: Train a BERTOS model (BERT-based transformer token classification) on the OS-ICSD training set using the provided data splits and the training configuration from the BERTOS repository.
- Evidence: `/app/outputs/bertos_os_icsd_model.pt`

### Step 2: Generate OS-ICSD test set oxidation state predictions
- Role: scored (load-bearing)
- Action: Load the trained OS-ICSD BERTOS model, run inference on the OS-ICSD test set, and output per-atom predicted oxidation states alongside true labels.
- Output file: `/app/outputs/os_icsd_predictions.csv`
- Format: csv
- Contract: Columns: composition (string), element (string), true_oxidation_state (int), predicted_oxidation_state (int). One row per atom site in the test set.
- Scoring: scored by hidden verifier

### Step 3: Compute OS-ICSD evaluation metrics
- Role: scored
- Action: Using the generated predictions, compute overall site-level accuracy, compound-level accuracy, and per-element site-level accuracies, and write the results to a JSON file.
- Output file: `/app/outputs/os_icsd_metrics.json`
- Format: json
- Contract: JSON object with keys: overall_site_accuracy (float, percent), compound_level_accuracy (float, percent), per_element_site_accuracy (object mapping element symbol to float percent).
- Scoring: scored by hidden verifier

### Step 4: Train BERTOS on OS-ICSD-oxide training set
- Role: process
- Action: Train a BERTOS model (same architecture) on the OS-ICSD-oxide training set using the provided oxide-specific data splits.
- Evidence: `/app/outputs/bertos_os_icsd_oxide_model.pt`

### Step 5: Generate OS-ICSD-oxide test set oxidation state predictions
- Role: scored (load-bearing)
- Action: Load the trained OS-ICSD-oxide BERTOS model, run inference on the OS-ICSD-oxide test set, and output per-atom predicted oxidation states alongside true labels.
- Output file: `/app/outputs/os_icsd_oxide_predictions.csv`
- Format: csv
- Contract: Columns: composition (string), element (string), true_oxidation_state (int), predicted_oxidation_state (int). One row per atom site in the oxide test set.
- Scoring: scored by hidden verifier

### Step 6: Compute OS-ICSD-oxide evaluation metrics
- Role: scored
- Action: Using the generated oxide predictions, compute overall site-level accuracy, compound-level accuracy, and per-element site-level accuracies, and write the results to a JSON file.
- Output file: `/app/outputs/os_icsd_oxide_metrics.json`
- Format: json
- Contract: JSON object with keys: overall_site_accuracy (float, percent), compound_level_accuracy (float, percent), per_element_site_accuracy (object mapping element symbol to float percent).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/os_icsd_predictions.csv`
- `/app/outputs/os_icsd_metrics.json`
- `/app/outputs/os_icsd_oxide_predictions.csv`
- `/app/outputs/os_icsd_oxide_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### os_icsd_predictions.csv
- path: `/app/outputs/os_icsd_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per‑atom site predictions used to recompute overall site accuracy, compound-level accuracy, and per-element accuracies for the OS-ICSD test set.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `element`, `true_oxidation_state`, `predicted_oxidation_state`
  - `description`: Each row is an atom site from the OS-ICSD test set. composition is the material formula, element is the element symbol, true_oxidation_state is the ICSD-provided oxidation state, predicted_oxidation_state is the model output.

### os_icsd_metrics.json
- path: `/app/outputs/os_icsd_metrics.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent‑computed summary metrics for the OS-ICSD evaluation. Checked for structural completeness and plausible ranges.
- schema:
  - `type`: object
  - `required`: `overall_site_accuracy`, `compound_level_accuracy`, `per_element_site_accuracy`
  - `units`:
    - `overall_site_accuracy`: percent
    - `compound_level_accuracy`: percent

### os_icsd_oxide_predictions.csv
- path: `/app/outputs/os_icsd_oxide_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per‑atom site predictions used to recompute overall site accuracy, compound-level accuracy, and per-element accuracies for the oxide test set.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `element`, `true_oxidation_state`, `predicted_oxidation_state`
  - `description`: Each row is an atom site from the OS-ICSD-oxide test set.

### os_icsd_oxide_metrics.json
- path: `/app/outputs/os_icsd_oxide_metrics.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent‑computed summary metrics for the oxide evaluation. Checked for structural completeness and plausible ranges.
- schema:
  - `type`: object
  - `required`: `overall_site_accuracy`, `compound_level_accuracy`, `per_element_site_accuracy`
  - `units`:
    - `overall_site_accuracy`: percent
    - `compound_level_accuracy`: percent

Notes: The checker recomputes site‑level, compound‑level, and per‑element accuracies directly from the prediction CSV files. The metrics JSON files are expected but serve as a structural sanity check; primary scoring relies on the recomputed values from the raw predictions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "os_icsd_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "element",
          "true_oxidation_state",
          "predicted_oxidation_state"
        ],
        "description": "Each row is an atom site from the OS-ICSD test set. composition is the material formula, element is the element symbol, true_oxidation_state is the ICSD-provided oxidation state, predicted_oxidation_state is the model output."
      },
      "description": "Per‑atom site predictions used to recompute overall site accuracy, compound-level accuracy, and per-element accuracies for the OS-ICSD test set."
    },
    {
      "file": "os_icsd_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "overall_site_accuracy",
          "compound_level_accuracy",
          "per_element_site_accuracy"
        ],
        "units": {
          "overall_site_accuracy": "percent",
          "compound_level_accuracy": "percent"
        }
      },
      "description": "Agent‑computed summary metrics for the OS-ICSD evaluation. Checked for structural completeness and plausible ranges."
    },
    {
      "file": "os_icsd_oxide_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "element",
          "true_oxidation_state",
          "predicted_oxidation_state"
        ],
        "description": "Each row is an atom site from the OS-ICSD-oxide test set."
      },
      "description": "Per‑atom site predictions used to recompute overall site accuracy, compound-level accuracy, and per-element accuracies for the oxide test set."
    },
    {
      "file": "os_icsd_oxide_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "overall_site_accuracy",
          "compound_level_accuracy",
          "per_element_site_accuracy"
        ],
        "units": {
          "overall_site_accuracy": "percent",
          "compound_level_accuracy": "percent"
        }
      },
      "description": "Agent‑computed summary metrics for the oxide evaluation. Checked for structural completeness and plausible ranges."
    }
  ],
  "notes": "The checker recomputes site‑level, compound‑level, and per‑element accuracies directly from the prediction CSV files. The metrics JSON files are expected but serve as a structural sanity check; primary scoring relies on the recomputed values from the raw predictions."
}
```

## How you are scored
The hidden verifier will independently process your submitted outputs.  For each prediction CSV file, it will recompute the overall site accuracy, compound‑level accuracy, and per‑element accuracies from the predictions and compare them to reference values (with appropriate tolerances).  The metrics JSON files will be checked for correct structure and internal consistency with the predictions (e.g., recomputed metrics should match the JSON).  Your final reward is a weighted combination of these evaluations, with the recomputed accuracy metrics from the prediction CSVs carrying the highest weight.  Simply reporting numbers that do not match the verifier's recomputation will result in a low score, even if they appear plausible.
