## Problem background

Accurate prediction of standard enthalpies of formation (Δ_f H°) is a central task in quantum chemistry.  While high-level composite methods can reach chemical accuracy, they become prohibitively expensive for larger molecules.  Density functional theory (DFT) at the B3LYP/6-31G(d,p) level is computationally efficient but exhibits systematic errors that grow with molecular size, especially for compounds containing sulphur or halogens.  A promising strategy is to build a statistical calibration model that learns a correction to the raw DFT enthalpy based on molecular descriptors.  This task reproduces such a calibration pipeline for a diverse set of 771 organic compounds.

## Approach

1. **Raw enthalpies.** For each of 771 organic compounds (neutrals and radicals containing C, H, O, N, S, F, Cl, Br), perform geometry optimisation and harmonic frequency analysis at the B3LYP/6-31G(d,p) level using an open-source quantum chemistry package.  Calculate the standard enthalpy of formation via the atomisation energy scheme, using experimental gas-phase atomic enthalpies from the NIST‑JANAF tables (C: 171.3, H: 52.1, O: 59.6, N: 113.0, S: 66.2, F: 19.0, Cl: 29.0, Br: 26.7 kcal/mol).  Zero‑point energies (ZPE) are retained.

2. **Molecular descriptors.** From the optimised geometries and ZPE, compute 47 descriptors that encode molecular structure: atom counts (C, H, O, N, S, F, Cl, Br), bond‑type counts (C=C, N−H, O−H, C−O, C=N, N=N, S=O, NO₂), ring descriptors (number of 3‑ and 4‑membered rings, rings with size >4, aromatic rings), lone‑pair counts on N and S, unpaired electrons, radical‑environment indicators (H atoms on radical, heavy atoms on radical, radical on a double/triple bond), and the molecule’s zero‑point energy.

3. **Descriptor reduction.** Remove any pair of descriptors whose absolute Pearson correlation coefficient exceeds 0.90.  This leaves a reduced set of approximately 39 descriptors.

4. **Feature selection.** Using Metropolis Monte Carlo simulated annealing with leave‑one‑out cross‑validated squared correlation coefficient q² as the fitness function, select an optimal subset of 17 descriptors from the reduced set.

5. **Calibration model.** Fit the linear equation
   Δ_f H_ls⁰ = Δ_f H_DFT⁰ + A + ∑ᵢ cᵢ xᵢ
   by ordinary least‑squares regression on the full dataset, where xᵢ are the values of the 17 selected descriptors and A is a constant term.  Obtain the regression coefficients and the constant.

6. **Evaluation.** Apply the calibration model to all 771 compounds.  Report the mean absolute error (MAE) of the raw B3LYP enthalpies versus experiment, the MAE of the calibrated predictions, the squared correlation coefficient r² between calibrated and experimental values, and the leave‑one‑out cross‑validated q².

## Reproduction target

Your goal is to implement the full pipeline described above and produce three scored artifacts:
- The list of 17 descriptors selected by the feature selection procedure.
- The fitted regression coefficients and constant term of the calibration model.
- The key performance metrics (MAE before calibration, MAE after calibration, r², q²).

The hidden verifier will compare your outputs against expected structural properties and performance thresholds; the exact paper‑reported numbers are used only as hidden references.

## Assets

- **Dataset:** The 771‑compound list with experimental enthalpies of formation and structural information (names/SMILES) is available in the Supporting Information (Table S1) of the original publication at https://onlinelibrary.wiley.com/doi/suppl/10.1002/jcc.21550 .
- **Atomic enthalpies:** Use the NIST‑JANAF values provided in the Approach above (C: 171.3, H: 52.1, O: 59.6, N: 113.0, S: 66.2, F: 19.0, Cl: 29.0, Br: 26.7 kcal/mol).
- **Quantum chemistry package:** An open‑source program capable of B3LYP/6‑31G(d,p) geometry optimisation, harmonic frequency calculation, and single‑point energy (e.g., Psi4, ORCA, PySCF).
- **Cheminformatics library:** A tool to generate 3D geometries from structures and to compute bond/ring descriptors (e.g., RDKit).
- **Python packages:** numpy, scipy, pandas, scikit‑learn for descriptor computation, correlation analysis, simulated annealing, and linear regression.

## Workflow steps

### Step 1: Assemble the 771‑compound dataset
- Role: process
- Action: Extract the list of 771 organic compounds and their experimental enthalpies of formation from the Supporting Information (Table S1). Generate initial 3D molecular geometries from the provided structures (names, SMILES) using a cheminformatics tool.
- Evidence: `/app/outputs/dataset_summary.txt`

### Step 2: B3LYP/6‑31G(d,p) DFT calculations
- Role: process
- Action: For every compound, perform geometry optimisation, harmonic vibrational frequency analysis, and single‑point energy calculation at the B3LYP/6‑31G(d,p) level with an open‑source quantum chemistry package. Convert the results to raw standard enthalpies of formation via the atomisation energy scheme using the NIST‑JANAF atomic enthalpies (given above). Retain the computed zero‑point energies (ZPE).
- Evidence: `/app/outputs/raw_dft_energies.csv`

### Step 3: Compute molecular descriptors
- Role: process
- Action: From the optimised geometries and ZPEs, calculate the 47 descriptors described in the Approach: atom counts, bond‑type counts, ring descriptors, lone‑pair/unpaired‑electron counts, radical‑environment descriptors, and ZPE.
- Evidence: `/app/outputs/descriptors_matrix.csv`

### Step 4: Correlation‑based descriptor reduction
- Role: process
- Action: Compute the Pearson correlation matrix for the 47 descriptors. Remove any descriptor pair whose absolute correlation exceeds 0.90, keeping one descriptor from each such pair. Retain the remaining set of descriptors.
- Evidence: `/app/outputs/reduced_descriptors.csv`

### Step 5: Simulated annealing feature selection
- Role: scored
- Action: Implement a Metropolis Monte Carlo simulated annealing algorithm that searches subsets of the reduced descriptor set, using the leave‑one‑out cross‑validated squared correlation coefficient q² as the fitness function. Select an optimal subset of exactly 17 descriptors. Write the abbreviations of the selected descriptors, one per line, to the output file.
- Output file: `/app/outputs/descriptor_selection.txt`
- Format: txt
- Contract: A plain text file with exactly 17 lines; each line contains one descriptor abbreviation as defined in the descriptor computation step (e.g., `N_C`, `N_OH`, `ZPE`).
- Scoring: scored by hidden verifier

### Step 6: Ordinary least‑squares model fitting
- Role: scored
- Action: Using the 17 selected descriptors and the raw DFT enthalpies, fit the calibration equation Δ_f H_ls⁰ = Δ_f H_DFT⁰ + A + ∑ cᵢ xᵢ to the full dataset via ordinary least‑squares regression. Write the constant term A and the dictionary of descriptor coefficients to the output file.
- Output file: `/app/outputs/model_coefficients.json`
- Format: json
- Contract: A JSON object with two keys: `"constant_A"` (a number, in kcal mol⁻¹) and `"coefficients"` (an object mapping each of the 17 descriptor abbreviations to its regression coefficient; the coefficient for ZPE is dimensionless, all others are in kcal mol⁻¹).
- Scoring: scored by hidden verifier

### Step 7: Model performance evaluation
- Role: scored (load‑bearing)
- Action: Apply the fitted calibration model to all 771 compounds. Compute (a) the MAE of the raw B3LYP enthalpies versus experimental values, (b) the MAE of the calibrated enthalpies, (c) the squared correlation coefficient r² between calibrated and experimental values, and (d) the leave‑one‑out cross‑validated q². Write these four numbers to the output file.
- Output file: `/app/outputs/performance_metrics.json`
- Format: json
- Contract: A JSON object with numeric fields: `"mae_before_calibration"` (kcal mol⁻¹), `"mae_after_calibration"` (kcal mol⁻¹), `"r_squared"` (dimensionless), `"q_squared"` (dimensionless).
- Scoring: scored by hidden verifier

## Output files

All artifacts must be written under `/app/outputs/`:

- `dataset_summary.txt` (evidence)
- `raw_dft_energies.csv` (evidence)
- `descriptors_matrix.csv` (evidence)
- `reduced_descriptors.csv` (evidence)
- `descriptor_selection.txt` (scored)
- `model_coefficients.json` (scored)
- `performance_metrics.json` (scored, load‑bearing)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### descriptor_selection.txt
- path: `/app/outputs/descriptor_selection.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: The set of 17 descriptor abbreviations selected by the feature selection procedure. Order-insensitive comparison against the expected set.
- schema:
  - `type`: text
  - `required_lines`: 17
  - `unit`: None

### model_coefficients.json
- path: `/app/outputs/model_coefficients.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Regression coefficients for the 17 selected descriptors and the constant term. Checked for structural completeness; coefficient values are not scored against exact paper numbers due to potential DFT code differences.
- schema:
  - `type`: object
  - `required`:
    - `constant_A`: number
    - `coefficients`: object
  - `coefficients_keys_count`: 17

### performance_metrics.json
- path: `/app/outputs/performance_metrics.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Reported MAE before and after calibration, r², and q². The verifier compares these values against hidden thresholds; full credit is awarded for meeting or exceeding the required level of accuracy.
- schema:
  - `type`: object
  - `required`:
    - `mae_before_calibration`: number (kcal/mol)
    - `mae_after_calibration`: number (kcal/mol)
    - `r_squared`: number (dimensionless)
    - `q_squared`: number (dimensionless)

Notes: The descriptor_selection.txt file must contain exactly 17 lines; the model_coefficients.json must contain exactly 17 coefficient entries plus constant_A.  The performance_metrics are only accepted under the contract that the metric conventions (r², q²) follow the definitions in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "descriptor_selection.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required_lines": 17,
        "unit": null
      },
      "description": "The set of 17 descriptor abbreviations selected by the feature selection procedure. Order-insensitive comparison against the expected set."
    },
    {
      "file": "model_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "constant_A": "number",
          "coefficients": "object"
        },
        "coefficients_keys_count": 17
      },
      "description": "Regression coefficients for the 17 selected descriptors and the constant term. Checked for structural completeness; coefficient values are not scored against exact paper numbers due to potential DFT code differences."
    },
    {
      "file": "performance_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "mae_before_calibration": "number (kcal/mol)",
          "mae_after_calibration": "number (kcal/mol)",
          "r_squared": "number (dimensionless)",
          "q_squared": "number (dimensionless)"
        }
      },
      "description": "Reported MAE before and after calibration, r², and q². The verifier compares these values against hidden thresholds; full credit is awarded for meeting or exceeding the required level of accuracy."
    }
  ],
  "notes": "The descriptor_selection.txt file must contain exactly 17 lines; the model_coefficients.json must contain exactly 17 coefficient entries plus constant_A.  The performance_metrics are only accepted under the contract that the metric conventions (r², q²) follow the definitions in the instruction."
}
```

## How you are scored

A hidden verifier independently evaluates your submission.  It checks the structural properties of the descriptor list and coefficient file, and compares your reported performance metrics against preset thresholds.  Rewards are awarded on a per‑artifact basis and combined to form the final score.  Simply reporting paper‑published numbers without carrying out the pipeline will not pass because the verifier uses cross‑validation and consistency checks that require genuine computation.
