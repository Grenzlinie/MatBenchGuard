# Ionic Liquid Property Prediction and Screening with Mol2vec Embeddings

## Problem background
Ionic liquids (ILs)—molten salts composed of organic cations and inorganic/organic anions—exhibit exceptional tunability, making them attractive solvents for applications such as biomass processing, CO2 capture, and battery electrolytes. Experimentally evaluating millions of possible cation–anion combinations is impractical, so there is a need for data-driven models that can predict key physicochemical properties directly from molecular structure. This task addresses the challenge by developing and applying machine learning methods to predict seven critical IL properties and using those predictions to screen large combinatorial libraries for task-specific candidates.

## Approach
The work uses natural language processing (NLP) to represent ILs. Each IL is converted to a SMILES string, and a pre-trained Mol2vec model (an unsupervised embedding analogous to Word2vec over molecular substructures) generates a 300‑dimensional feature vector that captures both local and global chemical environments. These embeddings, together with experimental temperature and pressure, serve as input to separate gradient‑boosted tree models (CATBoost) trained to predict individual properties: viscosity, density, ionic conductivity, surface tension, melting temperature, toxicity, and water activity. For comparison, the same models are also trained with alternative featurizations—Morgan fingerprints, atom‑count descriptors, and quantum‑chemistry‑derived sigma profiles. Training uses a stratified (iSIM‑based) split (70 % training, 10 % validation, 20 % test) with hyperparameters optimised by Bayesian search. After evaluating on the held‑out test sets, the trained Mol2vec‑based models are used to predict properties for a large set of novel ILs generated combinatorially from diverse cations and anions using RDKit. The predicted properties are then filtered through multi‑property criteria to identify candidates for CO2‑capture solvents and lithium/sodium battery electrolytes.

## Reproduction target
Train separate CATBoost regression models using Mol2vec embeddings for seven IL properties (viscosity, density, ionic conductivity, surface tension, toxicity, water activity, and melting temperature; plus a classification model for melting temperature liquid/solid). Evaluate each model on its held‑out test set and report the coefficient of determination (R²) and root‑mean‑squared error (RMSE). Then, using RDKit, generate at least 1000 cations and 200 anions and combine them to create a library of at least 10 000 unique novel ILs. Compute Mol2vec embeddings for these new ILs, predict all seven properties with the trained models, and also compute synthesizability scores. Apply the combined screening thresholds for CO2 capture (log‑viscosity < 4.5 mPa s, surface tension < 45 mN m⁻¹, ionic conductivity 0.1–0.5 S m⁻¹, hydrophilic, synthesizability < 6, liquid at ambient) and for battery electrolyte (ionic conductivity > 1.5 S m⁻¹, log‑viscosity < 5 mPa s, log toxicity > 2.0, synthesizability < 6, liquid at ambient). Output the number of ILs that satisfy all criteria for each application, and list the top 5 candidates per application with their full predicted property profiles.

## Assets

- NIST ILThermo v2.0: https://ilthermo.boulder.nist.gov/
- Paper's GitHub repository (datasets and code): https://github.com/MohanMood/NLP_Ionic-Liquid_Properties
- Mol2vec pre-trained model: https://github.com/samoturk/mol2vec
- CATBoost: catboost
- RDKit: rdkit
- Zenodo deposit (generated ILs, optional reference): 10.5281/zenodo.15580854
- scikit-learn: scikit-learn
- Optuna: optuna

## Workflow steps

### Step 1: Data preparation and splitting
- Role: process
- Action: Obtain the seven IL property datasets from the paper's GitHub repository (and NIST ILThermo if needed). Clean SMILES, correct charge imbalances, and split each property dataset into train/validation/test sets using iSIM-based stratified sampling (70/10/20%).
- Evidence: none

### Step 2: Mol2vec featurization
- Role: process
- Action: Generate 300-dimensional Mol2vec embeddings for all ILs in the training, validation, and test sets using the pre-trained Mol2vec model (radii 0 and 1). Include experimental temperature and pressure as additional features.
- Evidence: none

### Step 3: CATBoost model training
- Role: process
- Action: Train separate CATBoost regression models for surface tension, viscosity, ionic conductivity, density, toxicity, water activity, and melting temperature (regression). Also train a classification model for melting temperature (liquid/solid). Use Bayesian hyperparameter optimization with Optuna and virtual ensemble for uncertainty. Save the trained models for later prediction.
- Evidence: `/app/outputs/step_03_training_log.txt`

### Step 4: Test-set evaluation metrics
- Role: scored
- Action: Evaluate the trained CATBoost models on the held-out test sets. Compute and report the coefficient of determination (R²) and root-mean-squared error (RMSE) for each property's regression model. For Tm classification, report accuracy. Store results in a JSON file.
- Output file: `/app/outputs/step_04_test_set_metrics.json`
- Format: json
- Contract: Object with keys: surface_tension, viscosity, ionic_conductivity, density, melting_temperature, toxicity, water_activity. Each value is an object with 'test_R2' (float) and 'test_RMSE' (float). For melting temperature classification, include 'test_accuracy' (float).
- Scoring: scored by hidden verifier

### Step 5: Generation of novel IL candidates
- Role: process
- Action: Use RDKit to systematically generate a diverse set of chemically valid cations (≥1000) and anions (≥200) with varying alkyl chains and functional groups, then combine them to produce at least 10,000 unique IL SMILES strings. Save the generated SMILES for downstream use.
- Evidence: `/app/outputs/generated_ils.csv`

### Step 6: Property prediction for generated ILs
- Role: process
- Action: Compute Mol2vec embeddings for the generated ILs. Use the trained CATBoost models from step 03 to predict: viscosity (ln(eta)), surface tension (sigma), ionic conductivity (kappa), density (rho), toxicity (log10 EC50), water activity coefficient (gamma_IL^w), melting temperature (or liquid/solid class). Also compute synthesizability (SA) scores using Ertl's method.
- Evidence: `/app/outputs/predicted_properties.csv`

### Step 7: Screening candidate counts
- Role: scored
- Action: Apply the stated screening criteria for CO2 capture (ln(eta) < 4.5, sigma < 45 mN/m, kappa 0.1-0.5 S/m, hydrophilic, SA score < 6, liquid at ambient) and for battery electrolytes (kappa > 1.5 S/m, ln(eta) < 5, log10 EC50 > 2.0, SA score < 6, liquid at ambient) to the predicted properties. Count how many of the generated ILs satisfy all criteria for each application. Save the counts in a JSON file.
- Output file: `/app/outputs/step_07_candidate_counts.json`
- Format: json
- Contract: Object with keys 'co2_capture' and 'battery_electrolyte', each mapping to an integer count.
- Scoring: scored by hidden verifier

### Step 8: Top candidate ILs and predictions
- Role: scored (load-bearing)
- Action: From the ILs that passed each screening, select the top 5 candidates (based on predicted properties as described in the paper). For each, output the SMILES, predicted property values, synthesizability score, and whether it passed each screening criterion. Save as a CSV file.
- Output file: `/app/outputs/step_07_top_candidates.csv`
- Format: csv
- Contract: Columns: application (co2 or battery), SMILES, predicted_ln_eta, predicted_sigma, predicted_kappa, predicted_logEC50, predicted_gamma_w, predicted_SA, predicted_Tm (or liquid/solid class), passed (True/False).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_test_set_metrics.json`
- `/app/outputs/step_07_candidate_counts.json`
- `/app/outputs/step_07_top_candidates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_test_set_metrics.json
- path: `/app/outputs/step_04_test_set_metrics.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Test-set performance metrics (R² and RMSE) for each IL property model.
- schema:
  - `type`: object
  - `required`:
    - `surface_tension`: object with test_R2 and test_RMSE
    - `viscosity`: object with test_R2 and test_RMSE
    - `ionic_conductivity`: object with test_R2 and test_RMSE
    - `density`: object with test_R2 and test_RMSE
    - `melting_temperature`: object with test_R2 and test_RMSE; optionally test_accuracy
    - `toxicity`: object with test_R2 and test_RMSE
    - `water_activity`: object with test_R2 and test_RMSE

### step_07_candidate_counts.json
- path: `/app/outputs/step_07_candidate_counts.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Number of generated ILs that pass all screening criteria for CO₂ capture and battery electrolyte, respectively.
- schema:
  - `type`: object
  - `required`:
    - `co2_capture`: integer
    - `battery_electrolyte`: integer

### step_07_top_candidates.csv
- path: `/app/outputs/step_07_top_candidates.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Top 5 ILs per application with their predicted properties and whether they satisfy the screening criteria.
- schema:
  - `type`: table
  - `required_columns`: `application`, `SMILES`, `predicted_ln_eta`, `predicted_sigma`, `predicted_kappa`, `predicted_logEC50`, `predicted_gamma_w`, `predicted_SA`, `predicted_Tm`, `passed`

Notes: Biomass pretreatment screening is omitted because it requires proprietary COSMO-RS calculations. The task uses a subset of at least 10,000 novel ILs instead of the full 10.6 million; screening counts are scored against a proportionally scaled reference. Top candidates are verified for structural correctness and compliance with stated thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_test_set_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "surface_tension": "object with test_R2 and test_RMSE",
          "viscosity": "object with test_R2 and test_RMSE",
          "ionic_conductivity": "object with test_R2 and test_RMSE",
          "density": "object with test_R2 and test_RMSE",
          "melting_temperature": "object with test_R2 and test_RMSE; optionally test_accuracy",
          "toxicity": "object with test_R2 and test_RMSE",
          "water_activity": "object with test_R2 and test_RMSE"
        }
      },
      "description": "Test-set performance metrics (R² and RMSE) for each IL property model."
    },
    {
      "file": "step_07_candidate_counts.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "co2_capture": "integer",
          "battery_electrolyte": "integer"
        }
      },
      "description": "Number of generated ILs that pass all screening criteria for CO₂ capture and battery electrolyte, respectively."
    },
    {
      "file": "step_07_top_candidates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "application",
          "SMILES",
          "predicted_ln_eta",
          "predicted_sigma",
          "predicted_kappa",
          "predicted_logEC50",
          "predicted_gamma_w",
          "predicted_SA",
          "predicted_Tm",
          "passed"
        ]
      },
      "description": "Top 5 ILs per application with their predicted properties and whether they satisfy the screening criteria."
    }
  ],
  "notes": "Biomass pretreatment screening is omitted because it requires proprietary COSMO-RS calculations. The task uses a subset of at least 10,000 novel ILs instead of the full 10.6 million; screening counts are scored against a proportionally scaled reference. Top candidates are verified for structural correctness and compliance with stated thresholds."
}
```

## How you are scored
The three scored artifacts (`step_04_test_set_metrics.json`, `step_07_candidate_counts.json`, `step_07_top_candidates.csv`) are each evaluated by a hidden verifier that compares the computed values against expected references (with appropriate tolerances) and checks the structural correctness of the candidate list. The overall reward is a weighted combination of these independent evaluations. Submitting plausible numbers without executing the full pipeline will not satisfy the verifier because the scoring accounts for the proper relationships between the trained models, the generated IL set, and the screening logic.
