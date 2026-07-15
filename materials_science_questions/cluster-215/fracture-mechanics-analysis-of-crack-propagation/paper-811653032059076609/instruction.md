# Residual strength prediction of unidirectional Gr_f/Al composites with circular holes

## Problem background
Unidirectional graphite fiber‑reinforced aluminum (Gr_f/Al) composites offer high specific stiffness and strength, but their tensile performance is sensitive to stress concentrations around holes and notches. Accurately predicting the residual strength of notched Gr_f/Al components is critical for safe design. Several analytical criteria originally developed for polymer matrix composites — the Point Stress Criterion (PSC), Average Stress Criterion (AVC), Damage Zone Criterion (DZC), and the Effective Crack Growth Model (ECGM) — have not been thoroughly evaluated for metal matrix composites. This task reproduces the computational evaluation of these four models, using known composite mechanical properties, characteristic distances, and the apparent fracture energy obtained from a notched three‑point bending test (provided below), to compute predicted residual tensile strengths for various hole diameters.

## Approach
The procedure is a computational comparison of four notched‑strength prediction methods. First, the orthotropic stress concentration factor (SCF) is computed for each hole diameter using Tan’s finite‑width correction formulas, requiring the composite’s elastic constants and the specimen width. Then:
- The Point Stress Criterion (PSC) uses the SCF and a characteristic distance to predict failure.
- The Average Stress Criterion (AVC) averages the stress over a critical distance.
- The Damage Zone Criterion (DZC) incorporates a critical damage length.
- The Effective Crack Growth Model (ECGM) iteratively simulates crack growth, driven by the apparent fracture energy and the SCF, with a fixed damage increment.
All models rely on the same SCFs and the unnotched tensile strength. The predicted strengths for five hole diameters are collected and will be compared against experimental measurements.

## Reproduction target
Build a self‑contained computational pipeline that, using the provided mechanical properties, characteristic distances, apparent fracture energy, specimen width, and hole diameters, computes the predicted residual tensile strength for each of five hole diameters (0.6, 1.1, 1.5, 2.2, 5.1 mm) under each of the four models (PSC, AVC, DZC, ECGM). The final deliverable is a CSV file with one row per hole diameter and columns for the predictions from each model (in MPa).

## Assets
No external datasets or pre‑trained models are needed; all material constants and model parameters are provided in this instruction. The agent may install standard Python packages for numerical computation, such as:
- numpy (PyPI package `numpy`)
- scipy (PyPI package `scipy`)

## Workflow steps

### Step 1: Compute stress concentration factors
- Role: process
- Action: Compute the stress concentration factor (SCF) for each hole diameter using the orthotropic stiffness matrix derived from the composite's elastic constants (E1=240.1 GPa, E2=40.2 GPa, ν12=0.28, G12=29.0 GPa), the specimen width W=30 mm, and Tan's finite‑width correction formulas. Produce SCF values for D = 0.6, 1.1, 1.5, 2.2, 5.1 mm.
- Evidence: none

### Step 2: Run ECGM residual strength simulation
- Role: process
- Action: Implement the Effective Crack Growth Model (ECGM) iteratively with a damage increment Δc=0.001. Use the computed SCFs, the apparent fracture energy Gc*=4.1 kJ/m², unnotched strength σ0=542.8 MPa, specimen geometry, and elastic constants to compute the predicted residual tensile strength for each hole diameter.
- Evidence: none

### Step 3: Apply PSC, AVC, and DZC predictions
- Role: process
- Action: Implement the Point Stress Criterion (PSC) with characteristic distance d0=0.20 mm, Average Stress Criterion (AVC) with a0=0.53 mm, and Damage Zone Criterion (DZC) with d1*=0.19 mm. Using the SCFs and the unnotched strength σ0=542.8 MPa, compute the predicted residual tensile strength for each hole diameter.
- Evidence: none

### Step 4: Write predicted residual strengths
- Role: scored (load-bearing)
- Action: Assemble all predicted strengths into a single CSV file 'predicted_strengths.csv'. Each row corresponds to a hole diameter (0.6, 1.1, 1.5, 2.2, 5.1 mm); columns: hole_diameter (mm), PSC_predicted (MPa), AVC_predicted (MPa), DZC_predicted (MPa), ECGM_predicted (MPa). All values are floats.
- Output file: `/app/outputs/predicted_strengths.csv`
- Format: csv
- Contract: Columns: hole_diameter (mm, float), PSC_predicted (MPa, float), AVC_predicted (MPa, float), DZC_predicted (MPa, float), ECGM_predicted (MPa, float). Five rows, one per hole diameter.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_strengths.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_strengths.csv
- path: `/app/outputs/predicted_strengths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted residual tensile strengths for five hole diameters and four analytical models. The checker compares these to the paper’s measured values and computes relative errors, scoring based on the mean absolute deviation of those errors.
- schema:
  - `type`: table
  - `required_columns`: `hole_diameter`, `PSC_predicted`, `AVC_predicted`, `DZC_predicted`, `ECGM_predicted`
  - `units`:
    - `hole_diameter`: mm
    - `PSC_predicted`: MPa
    - `AVC_predicted`: MPa
    - `DZC_predicted`: MPa
    - `ECGM_predicted`: MPa

Notes: All necessary material constants and model parameters are provided in the instruction; no external dataset download is required. The iterative ECGM simulation should use Δc=0.001 to match the paper’s reported predictions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_strengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "hole_diameter",
          "PSC_predicted",
          "AVC_predicted",
          "DZC_predicted",
          "ECGM_predicted"
        ],
        "units": {
          "hole_diameter": "mm",
          "PSC_predicted": "MPa",
          "AVC_predicted": "MPa",
          "DZC_predicted": "MPa",
          "ECGM_predicted": "MPa"
        }
      },
      "description": "Predicted residual tensile strengths for five hole diameters and four analytical models. The checker compares these to the paper’s measured values and computes relative errors, scoring based on the mean absolute deviation of those errors."
    }
  ],
  "notes": "All necessary material constants and model parameters are provided in the instruction; no external dataset download is required. The iterative ECGM simulation should use Δc=0.001 to match the paper’s reported predictions."
}
```

## How you are scored
Your predictions in `predicted_strengths.csv` are checked by a hidden verifier. The verifier computes relative errors between your predicted strengths and the experimental tensile strength values that were measured for each hole diameter (those measurements are not provided to you). It then compares those errors to the paper's reported fits. The reward is based on how closely your predictions reproduce the expected error levels across all model–diameter combinations. Reporting the paper's numbers without running the computation is not sufficient — a genuine implementation of the models is required.
