## Problem background
Graph Neural Networks (GNNs) for atomistic simulations, such as SchNet, can produce unreliable predictions on out-of-domain data. Uncertainty quantification (UQ) is needed to detect such cases. This work integrates a lightweight UQ method, Direct Propagation of Shallow Ensembles (DPOSE), into SchNet by replacing its final layer with 64 independent output heads trained with Negative Log-Likelihood (NLL) loss. This enables the model to output both a predictive mean and a predictive variance (uncertainty). The goal is to test whether this uncertainty can distinguish in-domain from out-of-domain molecular and material configurations across different datasets.

## Approach
The core idea is to modify SchNet's architecture: sharing all weights up to the final layer, then splitting the final output into n=64 shallow ensemble heads. Each head predicts a scalar energy. The ensemble mean \(\bar{y}\) and variance \(\sigma^2\) are computed from the 64 head outputs. The model is trained using the NLL loss that jointly optimizes mean prediction and uncertainty calibration.

Three separate model instances are trained/fine-tuned on different datasets:

- QM9-SE: a SchNet ensemble trained from scratch on the full QM9 dataset of small organic molecules.
- OC20-SE: a SchNet ensemble fine-tuned on the intermetallic slab subset of the Open Catalyst 2020 (OC20) dataset, starting from a pretrained SchNet checkpoint (originally trained on the full OC20). During fine-tuning, all upstream weights are frozen and only the DPOSE heads are updated.
- AuMD-SE: a SchNet ensemble fine-tuned on the bulk gold configurations from a Gold Molecular Dynamics dataset, using the same pretrained OC20 checkpoint and freezing upstream weights.

For evaluation, the trained models are applied to both in-domain (seen during training/fine-tuning) and out-of-domain (unseen) inputs to compute predictive variance per sample. Additionally, the regression performance (R²) is measured on the respective in-domain test splits.

The out-of-domain test cases include:
- QM9: molecules containing elements not present in QM9 (Si, Cl), such as CCl₄, SiH₄, HCl, SiF₄, SiCl₄, and their in-domain counterparts (CF₄, CH₄, HF).
- OC20: non-metal slabs (out-of-domain) vs. intermetallic slabs (in-domain).
- Gold dataset: silver structures (Au replaced by Ag) vs. gold structures.

The comparison of predictive variance between in-domain and out-of-domain inputs is the core experiment.

## Reproduction target
Construct the DPOSE-modified SchNet architecture, train/fine-tune the three models as described, and evaluate them to produce an aggregated JSON file containing:
- Per-molecule predictive variance for the specified QM9 molecules.
- Median predictive variance over intermetallic and non-metal slab subsets from OC20.
- Mean predictive variance over gold and silver systems from the Gold dataset.
- R² scores on the QM9 test split and on the OC20 intermetallic test split.
The concrete objective is to compute these quantities from the trained models and report them. The hidden grader will verify the structural relationships (e.g., variance trends) and threshold compliance.

## Assets
The following public resources are needed:
1. QM9 dataset: a benchmark dataset of 130,831 small organic molecules with DFT energies. Access: https://figshare.com/articles/dataset/QM9/1004782
2. Open Catalyst 2020 (OC20) dataset: a large dataset of heterogeneous catalytic surfaces with molecular adsorbates. The intermetallic slab subset will be extracted. Access: https://github.com/Open-Catalyst-Project/ocp
3. Gold Molecular Dynamics dataset: gold systems (bulk, amorphous, clusters) from Boes et al. (2016). The bulk structures are used for fine-tuning; the same structures (with Ag substitution) are used for silver evaluation. Access: DOI 10.1002/qua.25115 (the agent obtains the dataset).
4. Pretrained SchNet checkpoint for OC20: a SchNet model pretrained on the full OC20 dataset. Access: available from the Open Catalyst Project releases at https://github.com/Open-Catalyst-Project/ocp/releases/
5. SchNet implementation: any open-source SchNet implementation (e.g., from torch_geometric or schnetpack via PyPI) can be used. The agent may install necessary packages.

## Workflow steps

### Step 1: Train QM9-SE model from scratch
- Role: process
- Action: Train a SchNet model with DPOSE (64 output heads, NLL loss) on the full QM9 dataset using an 80/20 train/test split. Obtain a trained QM9-SE model.
- Evidence: `/app/outputs/training_log_qm9.txt`

### Step 2: Fine-tune OC20-SE model on intermetallic slabs
- Role: process
- Action: Load the pretrained SchNet checkpoint, modify the final layer to DPOSE (64 heads), and fine-tune on the intermetallic slab subset of OC20, freezing all upstream weights. Obtain the OC20-SE model.
- Evidence: `/app/outputs/training_log_oc20.txt`

### Step 3: Fine-tune AuMD-SE model on bulk gold
- Role: process
- Action: Using the same pretrained SchNet checkpoint, add DPOSE heads and fine-tune on the bulk gold configurations from the Gold dataset, freezing upstream weights. Obtain the AuMD-SE model.
- Evidence: `/app/outputs/training_log_gold.txt`

### Step 4: Evaluate all models and produce summary (load-bearing)
- Role: scored (load-bearing)
- Action: For each trained model, perform the following computations and write the results to a single JSON file:
  * QM9-SE: Compute predictive variance (σ²) for the molecules CF₄, CH₄, HF (in-domain) and CCl₄, SiH₄, HCl, SiF₄, SiCl₄ (out-of-domain). Also compute the R² score on the QM9 test split.
  * OC20-SE: Compute the median predictive variance over the intermetallic slab test subset and over a non-metal slab subset. Compute the R² score on the intermetallic test set.
  * AuMD-SE: Compute the mean predictive variance over a set of gold structures (bulk) and over corresponding silver structures (generated by replacing Au atoms with Ag in the same geometries).
- Output file: `/app/outputs/evaluation_summary.json`
- Format: json
- Contract: a JSON object with keys `qm9_in_domain_variance` (array of 3 floats), `qm9_out_of_domain_variance` (array of 5 floats), `oc20_intermetallic_variance_median` (float), `oc20_nonmetal_variance_median` (float), `gold_variance_au_mean` (float), `gold_variance_ag_mean` (float), `qm9_test_R2` (float), `oc20_intermetallic_test_R2` (float).
- Scoring: scored by hidden verifier

## Output files
All output files must be placed under `/app/outputs/`.
- training_log_qm9.txt (evidence)
- training_log_oc20.txt (evidence)
- training_log_gold.txt (evidence)
- evaluation_summary.json (scored)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### evaluation_summary.json
- path: `/app/outputs/evaluation_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Aggregated variance and R² results from QM9, OC20, and Gold evaluations. Variances are in units of energy squared (eV² or eV²/atom² as appropriate). The checker will verify structural relationships (trends, thresholds) among the reported quantities.
- schema:
  - `type`: object
  - `required`:
    - `qm9_in_domain_variance`: array of float (length 3)
    - `qm9_out_of_domain_variance`: array of float (length 5)
    - `oc20_intermetallic_variance_median`: float
    - `oc20_nonmetal_variance_median`: float
    - `gold_variance_au_mean`: float
    - `gold_variance_ag_mean`: float
    - `qm9_test_R2`: float
    - `oc20_intermetallic_test_R2`: float

Notes: The graded artifact is evaluation_summary.json. Process‑step logs are not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "evaluation_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "qm9_in_domain_variance": "array of float (length 3)",
          "qm9_out_of_domain_variance": "array of float (length 5)",
          "oc20_intermetallic_variance_median": "float",
          "oc20_nonmetal_variance_median": "float",
          "gold_variance_au_mean": "float",
          "gold_variance_ag_mean": "float",
          "qm9_test_R2": "float",
          "oc20_intermetallic_test_R2": "float"
        }
      },
      "description": "Aggregated variance and R² results from QM9, OC20, and Gold evaluations. Variances are in units of energy squared (eV² or eV²/atom² as appropriate). The checker will verify structural relationships (trends, thresholds) among the reported quantities."
    }
  ],
  "notes": "The graded artifact is evaluation_summary.json. Process‑step logs are not scored."
}
```

## How you are scored
A hidden verifier will read your `evaluation_summary.json` and check the structural relationships between the reported quantities (e.g., whether out-of-domain variances are substantially higher than in-domain ones, whether the R² thresholds are met). Simply reporting numbers that satisfy generic guesses will not pass; the values must be derived from the actual trained models. A weighted combination of the checks produces a final reward in [0,1].
