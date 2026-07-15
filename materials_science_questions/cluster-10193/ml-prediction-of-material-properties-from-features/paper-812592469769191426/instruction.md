# Conformer Energy Accuracy Benchmark via MMFF94, GFN2, and ANI-1ccx

## Problem background
Ranking the relative energies of different conformers of a molecule is a fundamental task in computational chemistry. Conformer sampling often relies on fast classical force fields, but these may have poor correlation with accurate quantum mechanical methods. In contrast, high-level coupled-cluster calculations can provide accurate relative energies but are computationally expensive, making it impractical to use them for routine screening of many conformers of many molecules. A practical benchmark is therefore needed to understand where current methods—including force fields, semiempirical methods, density functional approximations, and modern machine-learning potentials—fall on the accuracy–speed tradeoff for this specific task.

## Approach
This work benchmarks a variety of computational methods for predicting single-point conformer energies using a publicly available dataset of approximately 681 drug-like molecules with multiple geometry-optimized conformers each (~6,500 conformers in total). For each method, single-point atomization energies are computed on every conformer geometry. The results are compared against high-level DLPNO-CCSD(T)/cc-pVTZ reference energies provided for the same geometries. Accuracy is quantified by three metrics computed per molecule: mean absolute relative error (MARE) of the energies, Pearson R² (coefficient of determination), and Spearman rank correlation ρ. The overall performance of a method is summarized by the median of each metric across all molecules. The present reproduction task focuses on three representative methods that span different cost and accuracy regimes: the classical MMFF94 force field, the semiempirical GFN2 tight-binding method, and the ANI-1ccx neural network potential.

## Reproduction target
Using the public conformer benchmark dataset (including B3LYP-D3BJ/def2-SVP optimized geometries and the corresponding DLPNO-CCSD(T)/cc-pVTZ reference atomization energies), compute single-point energies for every conformer with three methods: MMFF94 (via Open Babel), GFN2 (via xtb), and ANI-1ccx (via TorchANI). For each method, calculate per-molecule MARE (in kcal/mol), Pearson R², and Spearman ρ relative to the provided reference energies. Finally, compute the median of each metric across all molecules and write them to /app/outputs/evaluation_report.json as a JSON array of objects, one per method, with keys "method", "median_MARE", "median_R2", and "median_Spearman".

## Assets

- Conformer Benchmark Dataset and Scripts: https://github.com/ghutchis/conformer-benchmark
- Open Babel: openbabel
- xtb: xtb
- TorchANI: torchani

## Workflow steps

### Step 1: Load benchmark dataset
- Role: process
- Action: Download or clone the conformer-benchmark repository; load the conformer geometries (XYZ/SDF) and the DLPNO-CCSD(T)/cc-pVTZ reference atomization energies for all 681 molecules (approximately 6,500 conformers).
- Evidence: `/app/outputs/dataset_summary.json`

### Step 2: Compute single-point energies
- Role: process
- Action: For every conformer geometry, compute the atomization energy using (a) MMFF94 via Open Babel, (b) GFN2 via xtb, and (c) ANI-1ccx via TorchANI. Store the computed energies per conformer per method.
- Evidence: `/app/outputs/energy_calculations.json`

### Step 3: Evaluate accuracy metrics
- Role: scored (load-bearing)
- Action: For each of the three methods (MMFF94, GFN2, ANI-1ccx), compute per-molecule mean absolute relative error (MARE in kcal/mol), Pearson R², and Spearman ρ relative to the provided DLPNO-CCSD(T) reference energies. Then calculate the median of each metric across all 681 molecules. Write the results to evaluation_report.json.
- Output file: `/app/outputs/evaluation_report.json`
- Format: json
- Contract: A JSON array of objects, each with keys: method (string), median_MARE (float, in kcal/mol), median_R2 (float), median_Spearman (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/evaluation_report.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### evaluation_report.json
- path: `/app/outputs/evaluation_report.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Median accuracy metrics for MMFF94, GFN2, and ANI-1ccx against DLPNO-CCSD(T)/cc-pVTZ reference energies across 681 molecules.
- schema:
  - `type`: array
  - `items`:
    - `method`: string
    - `median_MARE`: float
    - `median_R2`: float
    - `median_Spearman`: float

Notes: The agent must report the three required methods. Additional methods are not scored. The hidden checker compares the reported median values against the paper's published reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "evaluation_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "method": "string",
          "median_MARE": "float",
          "median_R2": "float",
          "median_Spearman": "float"
        }
      },
      "description": "Median accuracy metrics for MMFF94, GFN2, and ANI-1ccx against DLPNO-CCSD(T)/cc-pVTZ reference energies across 681 molecules."
    }
  ],
  "notes": "The agent must report the three required methods. Additional methods are not scored. The hidden checker compares the reported median values against the paper's published reference values with appropriate tolerances."
}
```

## How you are scored
Your submission will be checked by a hidden verifier that reads /app/outputs/evaluation_report.json and compares each reported median value against a hidden gold standard (the published values for the same metrics from the original study). The verifier applies appropriate tolerances to account for minor differences in software versions, numerical implementations, and random fluctuations. The overall reward is calculated as the fraction of the three required methods for which all three metrics fall within the acceptable tolerance. Reporting numbers alone without genuinely running the computational pipeline is not sufficient to achieve a high reward, as the verifier may cross-check internal consistency and enforce plausible bounds derived from the dataset.
