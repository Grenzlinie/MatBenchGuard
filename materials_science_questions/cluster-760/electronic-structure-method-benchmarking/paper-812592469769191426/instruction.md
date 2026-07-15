# Conformer Energy Method Benchmark

## Problem background
Accurate prediction of relative conformer energies is essential for many applications in computational chemistry, from property prediction to drug design. A wide variety of computational methods—force fields, semiempirical, density functional theory (DFT), ab initio, and machine learning—trade off cost and accuracy differently. To guide method selection, it is necessary to rigorously benchmark these approaches against a high-quality reference on a large, diverse set of drug-like molecules. This task measures how well each method reproduces DLPNO-CCSD(T)/cc-pVTZ atomization energies across ~700 molecules (up to 10 low-energy conformers each) by computing per-molecule error and correlation metrics.

## Approach
All calculations use optimized molecular geometries provided in the reference dataset; no geometry optimization is performed. Single-point atomization energies are computed with each method at the fixed geometry. The methods span several tiers:
- Classical force fields: MMFF94, UFF, GAFF.
- Semiempirical and density-functional tight-binding: PM7, GFN0, GFN1, GFN2.
- Low-cost DFT composite methods: B97-3c, PBEh-3c.
- Dispersion-corrected DFT with double- and triple-zeta basis sets: B3LYP-D3BJ and PBE-D3BJ with def2-SVP and def2-TZVP; ωB97X-D3/def2-TZVP.
- Ab initio RI-MP2/cc-pVTZ.
- Machine learning: pre-trained ANI-1x, ANI-1ccx, ANI-2x; bag-of-features (BOB, BAT, BATTY) trained per molecule on 5 conformers, with a variant BATTY/n normalized by atom count.
- Ablation: B3LYP/def2-TZVP and PBE/def2-TZVP without dispersion correction to test the effect of dispersion.

For each molecule and method, the mean absolute relative energy (MARE), Pearson R², and Spearman rank correlation ρ are computed against the provided DLPNO-CCSD(T) reference energies. These metrics separate absolute energy errors from systematic shifts and ranking quality.

## Reproduction target
Produce a CSV file, `per_molecule_metrics.csv`, that contains one row per (molecule, method) pair. Required columns: molecule (string), method (string), MARE (float, kcal/mol), R2 (float), Spearman_rho (float). The set of methods must include all those listed in the approach, including the dispersion-off variants and BATTY/n. The file will be used by the hidden checker to compute median metrics per method and evaluate agreement with published benchmarks.

## Assets

- conformer-benchmark GitHub repository: https://github.com/ghutchis/conformer-benchmark
- Open Babel 3.0: https://openbabel.org/
- OpenMOPAC: http://openmopac.net/
- xtb 6.2: https://github.com/grimme-lab/xtb
- ORCA 4.0.1: https://orcaforum.kofo.mpg.de/
- TorchANI: https://github.com/aiqm/torchani
- chemreps: https://github.com/ghutchis/chemreps
- scikit-learn: scikit-learn
- cclib 1.6.2: https://cclib.github.io/

## Workflow steps

### Step 1: Acquire benchmark geometries and reference energies
- Role: process
- Action: Clone/download the conformer-benchmark GitHub repository. Extract the optimized molecular geometries (XYZ files) and the DLPNO-CCSD(T)/cc-pVTZ atomization energy CSV for all conformers.
- Evidence: `/app/outputs/benchmark_data_inventory.txt`

### Step 2: Compute force field energies
- Role: process
- Action: For each provided conformer geometry, compute single-point energies using GAFF, MMFF94, and UFF force fields with Open Babel. Extract atomization energies.
- Evidence: `/app/outputs/force_field_energies.csv`

### Step 3: Compute semiempirical and GFN energies
- Role: process
- Action: For each conformer, run PM7 with OpenMOPAC and GFN0, GFN1, GFN2 with xtb. Extract atomization energies.
- Evidence: `/app/outputs/semiempirical_gfn_energies.csv`

### Step 4: Compute DFT and ab initio energies
- Role: process
- Action: Using a suitable quantum chemistry package (e.g., ORCA), perform single-point energy calculations for all conformers with the following methods and basis sets: B97-3c, PBEh-3c, B3LYP-D3BJ/def2-SVP, B3LYP-D3BJ/def2-TZVP, PBE-D3BJ/def2-SVP, PBE-D3BJ/def2-TZVP, ωB97X-D3/def2-TZVP, RI-MP2/cc-pVTZ. Additionally, run B3LYP/def2-TZVP without dispersion correction and PBE/def2-TZVP without dispersion. Extract atomization energies (e.g., with cclib).
- Evidence: `/app/outputs/dft_ab_initio_energies.csv`

### Step 5: Compute ANI machine learning energies
- Role: process
- Action: Use TorchANI with the official pre-trained models ANI-1x, ANI-1ccx, and ANI-2x to predict atomization energies for each conformer.
- Evidence: `/app/outputs/ani_energies.csv`

### Step 6: Train and predict bag-of-features models
- Role: process
- Action: Generate BOB, BAT, and BATTY descriptors for all conformers using chemreps. For each molecule, randomly select 5 conformers for training and the rest for testing. Train kernel ridge regression models to predict DLPNO-CCSD(T) atomization energy from descriptors. Predict energies for the test set. For the BATTY descriptor, also create a variant normalized by the number of atoms (BATTY/n).
- Evidence: `/app/outputs/bag_of_features_predictions.csv`

### Step 7: Compute per-molecule metrics and output results
- Role: scored (load-bearing)
- Action: For each molecule and each method (including all ablated variants), compute the mean absolute relative energy (MARE), Pearson R², and Spearman ρ rank correlation against the DLPNO-CCSD(T) reference energies. Output a CSV file.
- Output file: `/app/outputs/per_molecule_metrics.csv`
- Format: csv
- Contract: Columns: molecule (string), method (string), MARE (float, kcal/mol), R2 (float), Spearman_rho (float). One row per molecule per method.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/per_molecule_metrics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### per_molecule_metrics.csv
- path: `/app/outputs/per_molecule_metrics.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Per-molecule MARE, R², and Spearman ρ for all benchmarked methods compared to DLPNO-CCSD(T)/cc-pVTZ reference energies. Median metrics across molecules will be compared to paper golds using or-better scoring.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `method`, `MARE`, `R2`, `Spearman_rho`
  - `units`:
    - `MARE`: kcal/mol
    - `R2`: dimensionless
    - `Spearman_rho`: dimensionless

Notes: The hidden checker will group by method and compute median MARE, R², Spearman ρ; for MARE lower is better, for R² and Spearman ρ higher is better. Meeting or beating the paper's medians earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "per_molecule_metrics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "method",
          "MARE",
          "R2",
          "Spearman_rho"
        ],
        "units": {
          "MARE": "kcal/mol",
          "R2": "dimensionless",
          "Spearman_rho": "dimensionless"
        }
      },
      "description": "Per-molecule MARE, R², and Spearman ρ for all benchmarked methods compared to DLPNO-CCSD(T)/cc-pVTZ reference energies. Median metrics across molecules will be compared to paper golds using or-better scoring."
    }
  ],
  "notes": "The hidden checker will group by method and compute median MARE, R², Spearman ρ; for MARE lower is better, for R² and Spearman ρ higher is better. Meeting or beating the paper's medians earns full credit."
}
```

## How you are scored
A hidden verifier reads your `per_molecule_metrics.csv`, groups by method, and computes the median MARE, R², and Spearman ρ for each method. For each metric, median values are compared to the paper's reported values using a threshold-or-better policy: for MARE (lower is better), meeting or beating the reference earns full credit; for R² and Spearman ρ (higher is better), meeting or exceeding the reference earns full credit. Worse results receive partial credit based on deviation. Additionally, the verifier checks that expected structural trends hold (e.g., dispersion-corrected methods outperform their uncorrected counterparts, and BATTY/n is the best-performing bag-of-features variant). The weighted combination of these scores determines your final reward. Reporting the right numbers without executing the workflow is insufficient—the verifier re-derives the aggregates from your output.
