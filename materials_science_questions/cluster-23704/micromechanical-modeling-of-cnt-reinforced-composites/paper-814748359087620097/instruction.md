# Micromechanical Modeling of CNT-Reinforced Composites

## Problem background
Carbon nanotube (CNT)-reinforced polymer nanocomposites exhibit significantly enhanced axial stiffness because of the exceptional elastic modulus of CNTs. Predicting the effective axial modulus of unidirectionally aligned CNT/polymer composites as a function of CNT loading is a key challenge in nanocomposite design. Several micromechanics theories have been proposed to estimate composite properties from the properties of the individual constituents and the filler geometry, but their relative accuracy for polymer nanocomposites remains an open question. This task addresses that question by implementing and evaluating three classical micromechanics models—Mori–Tanaka, self-consistent field, and Halpin–Tsai—for a set of eight CNT/polyimide systems with CNT weight fractions ranging from approximately 2% to 18%. The goal is to compute the axial modulus predictions of each model and compare them to reference atomistic simulation results.

## Approach
All three models treat the nanocomposite as a two-phase material consisting of a pristine polymer matrix and infinitely long, unidirectionally aligned CNTs. The Halpin–Tsai model provides a simple rule-of-mixtures estimate for the axial modulus: E_comp = E_CNT * v_CNT + E_matrix * v_matrix. The Mori–Tanaka and self-consistent field approaches are mean-field methods based on Eshelby's solution for an ellipsoidal inclusion. They compute the composite effective modulus as E_comp = E_matrix + v_CNT (E_CNT - E_matrix) * A_CNT, where A_CNT is the strain concentration tensor. The two methods differ in how A_CNT is evaluated. For Mori–Tanaka, the dilute concentration tensor (assuming a single inclusion in an infinite matrix) is corrected for finite volume fraction by assuming the inclusion is embedded in the pristine matrix. For the self-consistent scheme, the inclusion is placed in the unknown effective medium, leading to a coupled equation that must be solved iteratively. The Eshelby tensor for a cylindrical inclusion (appropriate for CNTs) depends on the inclusion aspect ratio and the matrix Poisson's ratio; the agent must compute this tensor as part of the implementation. The calculations require the pristine axial modulus of each system (provided as a bundled CSV file) and a literature value for the CNT axial elastic modulus (~1 TPa for a (10,10) SWCNT).

## Reproduction target
Produce a comma-separated value (CSV) file, axial_moduli_predictions.csv, containing the predicted axial modulus (in GPa) for each of the eight systems (Sys1 through Sys8) from the Mori–Tanaka, self-consistent field, and Halpin–Tsai models. Each row must correspond to one system and include the system name, the CNT weight fraction, and the three model predictions. The predictions will be compared against hidden atomistic simulation results to assess which model yields the best agreement. The file must follow the column structure: system, cnt_weight_fraction, mori_tanaka_E, self_consistent_E, halpin_tsai_E.

## Assets

- CNT axial elastic modulus
- System parameters (pristine moduli and CNT weight fractions)

## Workflow steps

### Step 1: Compute axial modulus predictions using micromechanics models
- Role: scored
- Action: Using the provided system parameter file (system, cnt_weight_fraction, pristine_C33) and a chosen CNT axial modulus, implement the Mori–Tanaka, self-consistent field, and Halpin–Tsai models. For each of the eight systems, compute the composite axial modulus. Write the results to axial_moduli_predictions.csv.
- Output file: `/app/outputs/axial_moduli_predictions.csv`
- Format: csv
- Contract: CSV with columns: system (string), cnt_weight_fraction (float, weight fraction), mori_tanaka_E (float, GPa), self_consistent_E (float, GPa), halpin_tsai_E (float, GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/axial_moduli_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### axial_moduli_predictions.csv
- path: `/app/outputs/axial_moduli_predictions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted axial moduli (GPa) for eight nanocomposite systems from Mori-Tanaka, self-consistent field, and Halpin-Tsai models.
- schema:
  - `type`: table
  - `required_columns`: `system`, `cnt_weight_fraction`, `mori_tanaka_E`, `self_consistent_E`, `halpin_tsai_E`
  - `units`:
    - `mori_tanaka_E`: GPa
    - `self_consistent_E`: GPa
    - `halpin_tsai_E`: GPa

Notes: The checker will compute the mean absolute percentage error (MAPE) for each model relative to hidden atomistic reference values and verify that the self-consistent field model yields the lowest MAPE.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "axial_moduli_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "cnt_weight_fraction",
          "mori_tanaka_E",
          "self_consistent_E",
          "halpin_tsai_E"
        ],
        "units": {
          "mori_tanaka_E": "GPa",
          "self_consistent_E": "GPa",
          "halpin_tsai_E": "GPa"
        }
      },
      "description": "Predicted axial moduli (GPa) for eight nanocomposite systems from Mori-Tanaka, self-consistent field, and Halpin-Tsai models."
    }
  ],
  "notes": "The checker will compute the mean absolute percentage error (MAPE) for each model relative to hidden atomistic reference values and verify that the self-consistent field model yields the lowest MAPE."
}
```

## How you are scored
A hidden verifier will read your axial_moduli_predictions.csv and compute, for each model, the mean absolute percentage error (MAPE) between your predictions and hidden reference values derived from atomistic simulations. The scoring rewards solutions where the model(s) that best match the reference achieve a low error; a penalty is applied if a model that should perform well according to the reference instead shows high error. The exact weighting is hidden but reflects the relative performance of the three models. A valid CSV file with the correct columns is required to receive any credit; incorrect formatting or missing columns will result in zero reward.
