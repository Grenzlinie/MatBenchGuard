# Prediction of Ground-State PDOS from Core-Loss Spectra: Noise Robustness and Extrapolation

## Problem background
Core‑loss spectroscopy (ELNES/XANES) measures the unoccupied electronic states near the absorption edge, but many molecular properties – such as chemical bonding and mechanical behaviour – are governed by the ground‑state occupied orbitals, which cannot be directly extracted from such spectra. This work investigates whether a machine learning model can predict the full ground‑state carbon s‑ and p‑orbital partial density of states (PDOS) from C K‑edge core‑loss spectra. The model uses a public database of simulated spectra and PDOS for thousands of organic molecules. The task examines the prediction accuracy, the effect of training‑set composition on extrapolation to larger molecules, and the robustness of the predictions to Poisson noise, a common noise source in experimental spectra.

## Approach
**Model:** A feedforward neural network (FNN) with two hidden layers (160 and 120 units, ReLU activation, dropout 0.27) maps an input spectrum discretized into 160 energy bins (‑1 to 15 eV) to the ground‑state s‑ and p‑orbital PDOS discretized into 300 bins (‑15 to 15 eV). Training uses mean squared error loss, the Adam optimizer, and early stopping on validation loss (patience 500 epochs). The database is randomly split 90% training / 10% test.

**Prediction quality:** The trained model is evaluated on the test set. Mean squared error (MSE) is computed per molecule over the full energy range, over occupied states (E < 0 eV), and over unoccupied states (E > 0 eV).

**Extrapolation analysis:** To understand how training‑set composition affects prediction on larger molecules, three series of training subsets are constructed, all using molecules with up to 20 atoms:
- *Model‑blue:* for each atom count n from 12 to 20, select exactly n‑atom molecules, fixing the subset size to 1000.
- *Model‑green:* for each n, include all molecules with 1 to n atoms.
- *Model‑brown:* for each n, include all molecules with n to 20 atoms.
Additionally, two specific models are compared: model A (trained on all molecules with up to 20 atoms) and model B (trained on molecules with 18–20 atoms). All models are evaluated on the test molecules with 21–26 atoms, and the average MSE is recorded for every (model_type, n) combination.

**Noise robustness:** Poisson noise with count‑rate λ is added to the training spectra (λ = 10, 50, 100, 500, 1000), and separate FNN models are trained at each λ. Test spectra are generated with the same λ values, each prepared in three versions: unsmoothed, and Savitzky–Golay smoothed with widths 0.3 eV and 0.5 eV. For every pairing of training noise level and test noise level, the MSE is computed to determine which training condition yields the lowest error and how smoothing shifts the optimum.

**Augmentation comparison:** Naive noise augmentation (multiple Poisson realizations added to clean training spectra) is also applied for each λ. The resulting augmented models are compared to the matched‑noise models on unsmoothed noisy test spectra to assess whether augmentation provides comparable benefit.

## Reproduction target
Using the public simulated C K‑edge spectral database (Shibata et al. 2022), implement the full pipeline described above and produce the following four CSV files under `/app/outputs`:

1. `main_mse.csv` – per‑molecule MSEs (full, occupied, unoccupied) for the baseline model trained on all molecules with up to 20 atoms.
2. `extrapolation_mse.csv` – average MSE on test molecules of 21–26 atoms for each (model_type: blue, green, brown; n = 12…20) and for models A and B.
3. `noise_matching_mse.csv` – MSE for every combination of training λ and test λ, for each smoothing condition (none, 0.3, 0.5 eV).
4. `augmentation_mse.csv` – MSE for matched‑noise training vs. augmentation training at each λ.

The hidden verifier will examine whether certain quantitative relationships hold among these tables. No prior knowledge of the paper’s specific numerical values is needed; the results must be consistent with a faithful reproduction of the described protocol.

## Assets

- Simulated C K‑edge spectral database of organic molecules: 10.1038/s41597-022-01312-3
- Python machine learning stack: torch, numpy, scipy, scikit-learn

## Workflow steps

### Step 1: Load and preprocess dataset
- Role: process
- Action: Download the public C K-edge spectral database (Shibata et al. 2022). Remove the four unreasonable structures. Split data into 90% train and 10% test. Discretize spectra to 160 energy bins (−1 to 15 eV, 0.1 eV step) and PDOS to 300 bins (−15 to 15 eV). Normalize each spectrum and PDOS by its integrated intensity (area normalization).
- Evidence: `/app/outputs/preprocessing.log`

### Step 2: Train baseline FNN model
- Role: process
- Action: Train a feedforward neural network (input 160, two hidden layers: 160 and 120 units, ReLU, dropout 0.27, output 300, MSE loss) on the training set containing all molecules with up to 20 atoms. Use early stopping with patience 500 epochs on validation loss. Save the trained model.
- Evidence: `/app/outputs/model_A.checkpoint`

### Step 3: Evaluate baseline PDOS prediction
- Role: scored
- Action: Use the trained baseline model to predict PDOS for the test set. For each test molecule, compute the mean squared error (MSE) over the full energy range, over occupied states (energies < 0 eV), and over unoccupied states (energies > 0 eV). Write a CSV file with one row per test molecule.
- Output file: `/app/outputs/main_mse.csv`
- Format: csv
- Contract: Columns: molecule_id (string), MSE_full (float), MSE_occupied (float), MSE_unoccupied (float).
- Scoring: scored by hidden verifier

### Step 4: Prepare size‑filtered training sets and train extrapolation models
- Role: process
- Action: Create the three series of training subsets: (1) model‑blue: for each n from 12 to 20 select exactly n‑atom molecules, fix subset size to 1000; (2) model‑green: for each n select molecules with 1–n atoms; (3) model‑brown: for each n select molecules with n–20 atoms. For every subset, independently train an FNN using the same architecture and training protocol. Additionally, train the two highlighted models: model A (1–20 atoms) and model B (18–20 atoms). Save all trained models.
- Evidence: `/app/outputs/extrapolation_models.json`

### Step 5: Evaluate extrapolation performance
- Role: scored
- Action: For each of the trained models (including models A and B), compute the mean MSE over the test set of molecules with 21–26 atoms. Aggregate results and write a CSV file with one row per (model_type, n) combination.
- Output file: `/app/outputs/extrapolation_mse.csv`
- Format: csv
- Contract: Columns: n (int), model_type (string: blue|green|brown), MSE (float).
- Scoring: scored by hidden verifier

### Step 6: Generate noisy spectra and train λ‑specific models
- Role: process
- Action: Add Poisson noise with count‑rate λ to the training spectra, using λ values: 10, 50, 100, 500, 1000. Area‑normalize the noisy spectra. For each λ, train a separate FNN model (same architecture and protocol). Also prepare test spectra with the same λ values, and for each λ generate three versions: unsmoothed, and Savitzky–Golay smoothed with widths 0.3 eV and 0.5 eV. Save all trained λ‑models and the noisy test spectra.
- Evidence: `/app/outputs/noise_models.json`

### Step 7: Evaluate noise matching and smoothing
- Role: scored (load-bearing)
- Action: For each test noise level λ (10,50,100,500,1000) and for each smoothing condition (none, 0.3, 0.5 eV), evaluate every λ‑trained model (including a noise‑free trained model) on the corresponding noisy test spectra. Compute the per‑molecule MSE and average across the test set. Write a CSV file with one row per (train_lambda, test_lambda, smoothing_width) combination.
- Output file: `/app/outputs/noise_matching_mse.csv`
- Format: csv
- Contract: Columns: train_lambda (float), test_lambda (float), smoothing_width (string: 'none' or '0.3' or '0.5'), MSE (float).
- Scoring: scored by hidden verifier

### Step 8: Train models with naive noise augmentation
- Role: process
- Action: For each target noise level λ (10,50,100,500,1000), create an augmented training set by adding multiple Poisson‑noise realizations to the noise‑free spectra. Train an FNN model (same architecture) on the augmented set. Save each augmentation‑trained model.
- Evidence: `/app/outputs/augmentation_models.json`

### Step 9: Evaluate augmentation strategy
- Role: scored
- Action: For each noise level λ, evaluate the corresponding augmentation‑trained model and the λ‑matched model (from step_06) on the unsmoothed noisy test spectra of the same λ. Compute the mean MSE and save the results.
- Output file: `/app/outputs/augmentation_mse.csv`
- Format: csv
- Contract: Columns: lambda (float), method (string: matched|augmentation), MSE (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/main_mse.csv`
- `/app/outputs/extrapolation_mse.csv`
- `/app/outputs/noise_matching_mse.csv`
- `/app/outputs/augmentation_mse.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### main_mse.csv
- path: `/app/outputs/main_mse.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Per‑molecule prediction errors for the baseline FNN trained on all molecules up to 20 atoms; used to verify that median MSE_occupied > MSE_unoccupied.
- schema:
  - `type`: table
  - `required_columns`: `molecule_id`, `MSE_full`, `MSE_occupied`, `MSE_unoccupied`
  - `units`:
    - `MSE_full`: arb. units (squared intensity)
    - `MSE_occupied`: arb. units
    - `MSE_unoccupied`: arb. units

### extrapolation_mse.csv
- path: `/app/outputs/extrapolation_mse.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Average MSE for extrapolation to larger molecules (21‑26 atoms) as a function of training set atom count n and model type (blue/green/brown); used to check that for n=20, brown MSE < blue MSE.
- schema:
  - `type`: table
  - `required_columns`: `n`, `model_type`, `MSE`
  - `units`:
    - `MSE`: arb. units

### noise_matching_mse.csv
- path: `/app/outputs/noise_matching_mse.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: MSE matrix for noise‑robustness: each row gives the MSE when a model trained with noise level train_lambda is evaluated on test spectra with noise level test_lambda, with or without Savitzky–Golay smoothing; used to verify optimal training λ matches test λ and smoothing shifts optimum to higher λ.
- schema:
  - `type`: table
  - `required_columns`: `train_lambda`, `test_lambda`, `smoothing_width`, `MSE`
  - `units`:
    - `MSE`: arb. units

### augmentation_mse.csv
- path: `/app/outputs/augmentation_mse.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Comparison of MSE for augmentation‑trained vs. λ‑matched training at each noise level; used to verify that matched training yields strictly lower MSE than augmentation.
- schema:
  - `type`: table
  - `required_columns`: `lambda`, `method`, `MSE`
  - `units`:
    - `MSE`: arb. units

Notes: All MSE values are in the same scale (intensity squared after area normalization). The checker will verify qualitative trends across these files without requiring exact numerical agreement with the paper. No gold values or tolerances are supplied to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "main_mse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule_id",
          "MSE_full",
          "MSE_occupied",
          "MSE_unoccupied"
        ],
        "units": {
          "MSE_full": "arb. units (squared intensity)",
          "MSE_occupied": "arb. units",
          "MSE_unoccupied": "arb. units"
        }
      },
      "description": "Per‑molecule prediction errors for the baseline FNN trained on all molecules up to 20 atoms; used to verify that median MSE_occupied > MSE_unoccupied."
    },
    {
      "file": "extrapolation_mse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "model_type",
          "MSE"
        ],
        "units": {
          "MSE": "arb. units"
        }
      },
      "description": "Average MSE for extrapolation to larger molecules (21‑26 atoms) as a function of training set atom count n and model type (blue/green/brown); used to check that for n=20, brown MSE < blue MSE."
    },
    {
      "file": "noise_matching_mse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "train_lambda",
          "test_lambda",
          "smoothing_width",
          "MSE"
        ],
        "units": {
          "MSE": "arb. units"
        }
      },
      "description": "MSE matrix for noise‑robustness: each row gives the MSE when a model trained with noise level train_lambda is evaluated on test spectra with noise level test_lambda, with or without Savitzky–Golay smoothing; used to verify optimal training λ matches test λ and smoothing shifts optimum to higher λ."
    },
    {
      "file": "augmentation_mse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda",
          "method",
          "MSE"
        ],
        "units": {
          "MSE": "arb. units"
        }
      },
      "description": "Comparison of MSE for augmentation‑trained vs. λ‑matched training at each noise level; used to verify that matched training yields strictly lower MSE than augmentation."
    }
  ],
  "notes": "All MSE values are in the same scale (intensity squared after area normalization). The checker will verify qualitative trends across these files without requiring exact numerical agreement with the paper. No gold values or tolerances are supplied to the agent."
}
```

## How you are scored
Your submission is scored by a hidden verifier that loads the four CSV files and checks a set of required trends and orderings among the reported MSEs. For example, the verifier will:
- Compare the median occupied and unoccupied MSEs from `main_mse.csv`.
- Check, from `extrapolation_mse.csv`, whether model‑brown at n=20 yields a lower MSE than model‑blue at n=20.
- For each test λ in `noise_matching_mse.csv`, determine the training λ that minimizes the MSE and verify that it matches the test λ or is nearby; additionally, check whether smoothing shifts the optimal training λ to a slightly higher value.
- Confirm from `augmentation_mse.csv` that for every λ, the MSE obtained with matched training is strictly lower than that obtained with augmentation.

Scoring is weighted across all stages; the main check is whether your computed results exhibit the expected structural relations, not whether they exactly match specific numbers from any publication.
