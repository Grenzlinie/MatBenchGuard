# Micromechanical Modeling of CNT-Reinforced Polymer Composites using Mori–Tanaka with Effective Volume Fraction

## Problem background
Carbon nanotube (CNT) reinforced polypropylene composites show improved stiffness at low filler loadings, but imperfect interfacial bonding reduces load transfer. A Mori–Tanaka micromechanical model with an effective volume fraction factor α can capture the observed Young's modulus behaviour. This task implements the model for the low-concentration regime (0.05 and 0.1 wt% CNT) with and without maleic anhydride compatibiliser, using given α values.

## Approach
Use the Mori–Tanaka effective stiffness formulation for a composite containing randomly oriented, transversely isotropic fibres. The matrix and fibre elastic constants are fixed: matrix Young's modulus = 1.017 GPa, Poisson ratio = 0.3; fibre longitudinal modulus = 600 GPa, transverse modulus = 6 GPa, longitudinal Poisson ratio = 0.125, transverse Poisson ratio = 0.3, shear modulus = 2.5 GPa. Convert the CNT weight fractions (0.05 wt%, 0.1 wt%) to nominal volume fractions using the 2:1 rule‑of‑thumb (weight‑to‑volume). Then apply the effective volume fraction factor: α = 0.26 for formulations without maleic anhydride (MA) and α = 0.21 for formulations with MA. For each condition, compute the Eshelby tensor for a fibrous inclusion in an isotropic matrix, assemble the composite stiffness, and extract the overall Young's modulus.

## Reproduction target
Compute the Young's modulus predictions for iPP/MWCNT composites at 0.05 wt% and 0.1 wt% CNT, without and with MA (four conditions), using the Mori–Tanaka model and the prescribed material constants and α factors. Write the four predicted values to /app/outputs/predictions.csv with columns: wt% (float), MA_wt% (int), predicted_E_GPa (float). The predictions will be compared to experimental reference values by a hidden verifier.

## Assets

- NumPy: https://numpy.org
- SciPy: https://scipy.org

## Workflow steps

### Step 1: Convert weight fractions to effective volume fractions
- Role: process
- Action: Convert CNT weight fractions (0.05 wt%, 0.1 wt%) to effective volume fractions using the rule-of-thumb factor 2:1 (weight‑to‑volume) and then apply the α factor (α = 0.26 for formulations without MA, α = 0.21 for formulations with MA) to obtain the effective fiber volume fraction c_f,eff used in the Mori–Tanaka model.
- Evidence: `/app/outputs/conversion.txt`

### Step 2: Compute Mori–Tanaka Young's modulus predictions
- Role: scored (load-bearing)
- Action: Implement the Mori–Tanaka effective stiffness tensor for a composite containing randomly oriented transversely isotropic fibers. Use the following input material constants: matrix Young's modulus = 1.017 GPa, matrix Poisson ratio = 0.3; fiber longitudinal Young's modulus = 600 GPa, transverse modulus = 6 GPa, longitudinal Poisson ratio = 0.125, transverse Poisson ratio = 0.3, shear modulus = 2.5 GPa. Compute the Eshelby tensor for a fibrous inclusion in an isotropic matrix. For each condition (0.05 wt% and 0.1 wt% CNT, with and without MA), use the effective volume fraction obtained in the previous step to calculate the overall composite Young's modulus. Write the four predictions to /app/outputs/predictions.csv with columns: wt% (float), MA_wt% (int), predicted_E_GPa (float).
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: Columns: wt% (float, e.g., 0.05, 0.1), MA_wt% (int, 0 or 5), predicted_E_GPa (float). Four rows: (0.05,0), (0.1,0), (0.05,5), (0.1,5).
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
- target_policy: reference_match
- description: Predicted Young's modulus for the four conditions (0.05 and 0.1 wt% CNT, without and with MA). The values are compared to hidden experimental reference values.
- schema:
  - `type`: table
  - `required_columns`: `wt%`, `MA_wt%`, `predicted_E_GPa`
  - `units`:
    - `wt%`: wt%
    - `MA_wt%`: wt%
    - `predicted_E_GPa`: GPa

Notes: The predicted values are compared to hidden experimental reference data for the same conditions. The comparison uses an absolute tolerance.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wt%",
          "MA_wt%",
          "predicted_E_GPa"
        ],
        "units": {
          "wt%": "wt%",
          "MA_wt%": "wt%",
          "predicted_E_GPa": "GPa"
        }
      },
      "description": "Predicted Young's modulus for the four conditions (0.05 and 0.1 wt% CNT, without and with MA). The values are compared to hidden experimental reference values."
    }
  ],
  "notes": "The predicted values are compared to hidden experimental reference data for the same conditions. The comparison uses an absolute tolerance."
}
```

## How you are scored
A hidden verifier evaluates each workflow stage’s output independently. For the scored predictions.csv, it compares each predicted Young's modulus to the corresponding experimentally measured value using an absolute tolerance. The fraction of predictions within tolerance (up to 1) is the main score. The verifier may also check the presence and correctness of the process-step evidence (conversion.txt). The overall reward is a weighted sum of the individual stage scores.
