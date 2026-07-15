# High-Entropy Alloy Phase Classification via Learned Energetic Mismatch Criterion

## Problem background
High-entropy alloys (HEAs) are multi-principal-element alloys with promising mechanical and thermal properties. A key open question in HEA design is predicting whether a given alloy composition will form a single solid-solution phase or segregate into multiple phases or even an amorphous structure. Traditional empirical criteria rely on atomic size mismatch, enthalpy of mixing, and valence electron concentration, but their predictive power is limited. This work develops a data-driven energetic mismatch criterion that uses learned atomic embeddings to assess the compatibility of elements in an HEA. Your task is to reproduce the classification pipeline that separates single-phase from multiphase/amorphous HEAs using the criterion derived from the embedding.

## Approach
The core idea is to represent each element by two vectors: a host vector and a substituent vector. The energy per atom of a composition is modelled as a sum over substituents of their inner product with an environment vector that is a weighted average of the host vectors of all elements present. This dual-vector scheme is first trained on single-element and binary formation energies from the Materials Project database, minimizing mean squared error between the model-predicted energy per atom and the DFT-calculated energy per atom. The trained embedding yields an energetic similarity matrix for any composition (rows indexed by host, columns by substituent). For each HEA, this similarity matrix is row-normalized, binarized using an optimized cutoff, weighted by atomic proportions, and summed to produce a single mismatch value. Alloys with mismatch below an optimized borderline threshold are classified as single-phase; all others are classified as multiphase/amorphous. The key hyperparameter choices are a 3-dimensional embedding, small random initialization, and training on singlet+binary data only (ternary data are used only as a perturbation refinement, which is omitted here). The cutoff and borderline are tuned on the 90 experimental HEA compositions to best separate the two phase categories.

## Reproduction target
Your goal is to implement the complete pipeline: (1) Download and filter DFT energies from the Materials Project for the 45 elements listed in the supplementary information, keeping only the lowest energy per chemical formula. (2) Train the 3-dimensional dual-vector embedding on the resulting singlet and binary compositions. (3) For the 90 experimental HEA compositions from the public literature, construct the energetic mismatch criterion, optimize its cutoff and borderline using the same 90 alloys, and output predicted phase labels (0 = multiphase/amorphous, 1 = single-phase) to `/app/outputs/predictions.csv`. The classification correctness (fraction of alloys correctly labeled) will be used as the primary performance metric.

## Assets

- Materials Project database: https://materialsproject.org/
- Experimental HEA dataset (90 alloys with phase labels)

## Workflow steps

### Step 1: Curate Materials Project data
- Role: process
- Action: Download DFT energies for single-element and binary materials from the Materials Project for the 45 elements specified in the paper. Filter to keep only the lowest energy per chemical formula, yielding a training set of singlet and binary compositions with energy per atom.
- Evidence: `/app/outputs/filtered_data.csv`

### Step 2: Train initial embedding (singlet+binary)
- Role: process
- Action: Initialize host and substituent embedding vectors (Dim=3) for the 45 elements with small random values. Using only singlet and binary compositions from the curated dataset, minimize the mean squared error between the model-predicted energy per atom and the DFT energy per atom. Save the optimized embedding vectors.
- Evidence: `/app/outputs/embedding_vectors.json`

### Step 3: Classify 90 HEAs with mismatch criterion
- Role: scored (load-bearing)
- Action: For each of the 90 experimental HEA compositions, compute the similarity matrix (host-substituent inner products) using the trained embedding. Apply row-wise normalization, binarize with an optimized cutoff (determined by scanning over the 90 alloys to best separate single-phase from others), weight by atomic proportions, sum to obtain mismatch values, and classify as single-phase (1) if mismatch < borderline, else multiphase/amorphous (0). Write the predicted labels to predictions.csv.
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: Columns: alloy_name (str), predicted_phase (int, 0=multiphase/amorphous, 1=single-phase)
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
- description: Phase classification predictions for the 90 experimental high-entropy alloys. The correctness score is recomputed by comparing these labels against hidden ground-truth labels from the public literature dataset.
- schema:
  - `type`: table
  - `required_columns`: `alloy_name`, `predicted_phase`

Notes: Only the binary-trained embedding pipeline is used; the ternary perturbation refinement is omitted as per the minimal reproduction scope. Classification correctness is the sole scored metric.

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
          "alloy_name",
          "predicted_phase"
        ]
      },
      "description": "Phase classification predictions for the 90 experimental high-entropy alloys. The correctness score is recomputed by comparing these labels against hidden ground-truth labels from the public literature dataset."
    }
  ],
  "notes": "Only the binary-trained embedding pipeline is used; the ternary perturbation refinement is omitted as per the minimal reproduction scope. Classification correctness is the sole scored metric."
}
```

## How you are scored
A hidden verifier will evaluate your submission. The main scored artifact is `predictions.csv`; the verifier will compare your predicted labels against hidden ground-truth labels for the 90 alloys and compute classification correctness. Your reward on this stage is based on that correctness according to a monotonic policy (higher correctness yields higher reward). In addition, the verifier will examine the existence and structure of the supporting files (`filtered_data.csv` and `embedding_vectors.json`) and may award a small amount of credit for their presence as evidence that the required process steps were executed. The final overall score is a weighted combination of these individual stage rewards. Note that simply writing a pre‑computed number is not sufficient; the verifier directly scores the correctness derived from your predictions.
