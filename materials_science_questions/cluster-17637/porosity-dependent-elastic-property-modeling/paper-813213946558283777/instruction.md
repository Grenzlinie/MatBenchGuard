# Predict elastic modulus and proof stress of porous titanium using modified cellular solid model

## Problem background
Porous titanium produced by 3D printing and sintering can achieve a relative density (~0.6) that is twice the usual threshold for cellular solids (≤0.3). At such high relative densities, the standard cellular solid model often over‑predicts Young's modulus and under‑predicts the 0.2% proof stress. By incorporating pore geometry from micro‑CT image analysis, a modified cellular solid model can be used to compute predictions of elastic modulus and proof stress from morphological parameters (relative density, pore diameter, wall thickness) and known solid titanium properties. This task asks you to implement that modified model and compute its predictions for a set of sintering temperatures.

## Approach
The cellular solid model relates the porous material's modulus E* and yield stress σ* to the solid's properties and geometry factors. For modulus, E* = C1 (ρ*/ρs)^2 Es with Es = 110 GPa, where C1 is a geometry constant derived from the pore wall slenderness (t/l). The strut length l depends on the assumed pore cross‑sectional shape: for an octagonal cross‑section, l = d / 2.41; for a decagonal cross‑section, l = d / 3.08, where d is the average pore diameter. The geometry constant is then C1 = 1 / [(ρ*/ρs)^2 (t/l)^4].

For the 0.2% proof stress, the standard model uses σ* = 220 * 0.3 * (ρ*/ρs)^(3/2) MPa, while the modified model replaces the constant 0.3 with the relative density itself: σ* = 220 * (ρ*/ρs) * (ρ*/ρs)^(3/2) = 220 * (ρ*/ρs)^(5/2) MPa.

Using the morphological data provided for five final sintering temperatures, you will first compute C1 for both octagonal and decagonal shapes, then compute the corresponding elastic moduli, and finally compute both the standard and modified proof stress predictions.

## Reproduction target
Using the morphological data provided in the assets and the solid properties (Es = 110 GPa, σys = 220 MPa), compute the predicted Young's modulus for octagonal (E_oc*) and decagonal (E_dc*) pore cross‑sections, the standard 0.2% proof stress (sigma_standard), and the modified 0.2% proof stress (sigma_modified) for each of the five final sintering temperatures: 900, 1000, 1100, 1200, 1300 °C. Output the results as a CSV file named predicted_properties.csv under /app/outputs with columns: FST (integer, °C), E_oc_predicted (float, GPa), E_dc_predicted (float, GPa), sigma_standard_predicted (float, MPa), sigma_modified_predicted (float, MPa). There should be exactly five rows, one per FST.

## Assets
The morphological data required to compute the geometry constants and predictions is given in the table below. You do not need to download any external datasets.

| FST (°C) | Relative density ρ*/ρs | Pore diameter (μm) | Wall thickness (μm) |
|----------|------------------------|--------------------|--------------------|
| 900      | 0.61                   | 19.33              | 22.80              |
| 1000     | 0.62                   | 19.52              | 23.25              |
| 1100     | 0.60                   | 19.57              | 22.88              |
| 1200     | 0.62                   | 19.69              | 24.20              |
| 1300     | 0.64                   | 19.33              | 24.43              |

Solid titanium properties: Young's modulus Es = 110 GPa, 0.2% proof stress σys = 220 MPa.

## Workflow steps

### Step 1: Compute geometry constant C1 for octagonal and decagonal shapes
- Role: process
- Action: From the provided morphological data (relative density ρ*/ρ_s, pore diameter d, wall thickness t) for each sintering temperature, compute the strut length l for octagonal (l = d / 2.41) and decagonal (l = d / 3.08) pore cross-sections, then compute the geometry constant C1 = 1 / [(ρ*/ρ_s)^2 * (t/l)^4] for each shape.
- Evidence: none

### Step 2: Predict elastic modulus and 0.2% proof stress
- Role: scored (load-bearing)
- Action: Using the geometry constants C1 from the previous step, the morphological data, and solid titanium properties (Es = 110 GPa, σys = 220 MPa), compute: (1) the predicted Young's modulus for octagonal and decagonal shapes as E* = C1 * (ρ*/ρ_s)^2 * Es; (2) the standard baseline 0.2% proof stress as σ = 220 * 0.3 * (ρ*/ρ_s)^(3/2); and (3) the modified 0.2% proof stress as σ = 220 * (ρ*/ρ_s) * (ρ*/ρ_s)^(3/2). Write the results for the five sintering temperatures (900, 1000, 1100, 1200, 1300 °C) as a CSV file named predicted_properties.csv under /app/outputs.
- Output file: `/app/outputs/predicted_properties.csv`
- Format: csv
- Contract: Columns: FST (int, °C), E_oc_predicted (float, GPa), E_dc_predicted (float, GPa), sigma_standard_predicted (float, MPa), sigma_modified_predicted (float, MPa). One row per FST (5 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_properties.csv
- path: `/app/outputs/predicted_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Predicted elastic moduli and 0.2% proof stresses for five sintering temperatures, computed from the cellular solid model with octagonal and decagonal geometry constants. The values E_oc_predicted, E_dc_predicted and sigma_modified_predicted will be compared to the paper's reported results (Table 2) within tolerances; the standard yield model is computed for context and not scored.
- schema:
  - `type`: table
  - `required_columns`: `FST`, `E_oc_predicted`, `E_dc_predicted`, `sigma_standard_predicted`, `sigma_modified_predicted`
  - `units`:
    - `FST`: °C
    - `E_oc_predicted`: GPa
    - `E_dc_predicted`: GPa
    - `sigma_standard_predicted`: MPa
    - `sigma_modified_predicted`: MPa

Notes: The scored quantities are E_oc_predicted, E_dc_predicted, and sigma_modified_predicted. The standard yield model prediction is included for completeness but does not contribute to the reward.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "FST",
          "E_oc_predicted",
          "E_dc_predicted",
          "sigma_standard_predicted",
          "sigma_modified_predicted"
        ],
        "units": {
          "FST": "°C",
          "E_oc_predicted": "GPa",
          "E_dc_predicted": "GPa",
          "sigma_standard_predicted": "MPa",
          "sigma_modified_predicted": "MPa"
        }
      },
      "description": "Predicted elastic moduli and 0.2% proof stresses for five sintering temperatures, computed from the cellular solid model with octagonal and decagonal geometry constants. The values E_oc_predicted, E_dc_predicted and sigma_modified_predicted will be compared to the paper's reported results (Table 2) within tolerances; the standard yield model is computed for context and not scored."
    }
  ],
  "notes": "The scored quantities are E_oc_predicted, E_dc_predicted, and sigma_modified_predicted. The standard yield model prediction is included for completeness but does not contribute to the reward."
}
```

## How you are scored
Your predicted_properties.csv will be evaluated by a hidden verifier. The verifier will compare your reported E_oc_predicted, E_dc_predicted, and sigma_modified_predicted values to reference values using tolerance‑based checks. The sigma_standard_predicted column is computed for completeness but does not contribute to the score. Your final reward (0.0–1.0) is the fraction of the scored values that fall within the hidden tolerances.
