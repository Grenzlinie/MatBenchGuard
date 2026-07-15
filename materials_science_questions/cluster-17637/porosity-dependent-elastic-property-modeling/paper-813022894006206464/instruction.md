# Porosity-Dependent Elastic Property Prediction via Modified Mori-Tanaka Schemes

## Problem background
Porous ceramics are widely used in engineering for their low density, high surface area, and thermal resistance. Their mechanical behavior depends strongly on porosity and pore microstructure. A common method to estimate effective elastic moduli is the Mori-Tanaka (MT) scheme, which treats the material as a matrix containing isolated pores. However, classical MT assumes dilute, non-overlapping pores and loses accuracy at high porosities (above ~30–40%), where pores merge into interconnected networks. Accurately predicting the effective Young's modulus of highly porous ceramics therefore requires modifying the MT scheme to account for pore merging and open-cell connectivity.

## Approach
Two modifications are applied to the MT scheme. First, merged pores are identified using geometrical probability theory: the number of overlapping spherical void pairs is estimated, and each merged pair is replaced by an equivalent ellipsoid of the same volume. Second, open-cell pores are treated as damaged material with reduced load-carrying capacity; the effective Young's modulus of a structure containing open pores is scaled by the fraction of non-open area. For reproducibility, the open porosity \(\phi_{open}\) is taken as equal to the total porosity \(\phi\) at each level. The method is implemented in a stepwise differential fashion: pores of increasing radius are added sequentially to the host material, with the instantaneous porosity and concentration parameter updated at each step. Three models are compared:
- **MT**: classical Mori-Tanaka for spherical isolated pores.
- **MMT**: merged-pore modification, replacing overlapped spheres with ellipsoids.
- **OMT**: both merged and open-cell modifications, applying the open-cell reduction to the MMT result.

The host material is stainless steel (Young's modulus 193 GPa, Poisson's ratio 0.27). The pore size distribution is approximated by a normal distribution with radii from 10 to 100 μm, five equal-width size classes, mean 55 μm, and standard deviation 31.8 μm. The porosity levels to be examined are 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, and 90%.

## Reproduction target
Implement the differential Mori-Tanaka scheme with merged and open-cell modifications as described above. Compute the effective Young's modulus (in GPa) predicted by the MT, MMT, and OMT models for each of the nine porosity levels using the given material properties and pore size distribution. Save the results to `/app/outputs/predicted_moduli.csv`, with a header row containing column names: porosity,E_MT,E_MMT,E_OMT. The columns are: porosity (integer percent), E_MT (float, GPa), E_MMT (float, GPa), E_OMT (float, GPa).

## Assets

- NumPy
- SciPy

## Workflow steps

### Step 1: Implement modified Mori-Tanaka schemes
- Role: process
- Action: Implement the stepwise differential Mori-Tanaka scheme for porous materials with merged and open-cell pore modifications, including Eshelby tensor computations for spherical and ellipsoidal inclusions.
- Evidence: `/app/outputs/model_implementation.py`

### Step 2: Compute predicted Young's moduli across porosities
- Role: scored (load-bearing)
- Action: For each porosity level in [10, 20, 30, 40, 50, 60, 70, 80, 90]%, compute E_MT, E_MMT, and E_OMT using the implemented models and save the results to /app/outputs/predicted_moduli.csv.
- Output file: `/app/outputs/predicted_moduli.csv`
- Format: csv
- Contract: Header row with column names: porosity,E_MT,E_MMT,E_OMT. Columns: porosity (integer percent, 10-90), E_MT (float, GPa), E_MMT (float, GPa), E_OMT (float, GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_moduli.csv
- path: `/app/outputs/predicted_moduli.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Effective Young's modulus (GPa) predicted by classical MT, merged-pore modified MT (MMT), and open-cell modified MT (OMT) models for the artificial stainless steel case at porosities 10%–90%. The first row is a header with column names porosity,E_MT,E_MMT,E_OMT. For OMT, open porosity φ_open is assumed equal to the total porosity φ. The checker compares these predictions to hidden FEM reference data, evaluating relative error and RMSE improvement of OMT over MT.
- schema:
  - `type`: table
  - `required_columns`: `porosity`, `E_MT`, `E_MMT`, `E_OMT`
  - `units`:
    - `porosity`: %
    - `E_MT`: GPa
    - `E_MMT`: GPa
    - `E_OMT`: GPa

Notes: The task uses the stepwise differential MT scheme with merged and open-cell modifications as described in the paper's sections 2.2.1–2.2.4. Material: stainless steel (E=193 GPa, ν=0.27); pore size distribution: normal distribution, radii 10–100 μm, five equal-width classes, μ=55 μm, σ=31.8 μm. The CSV must include a header row with column names porosity,E_MT,E_MMT,E_OMT; porosity values are integer percents 10,20,...,90. For OMT, open porosity φ_open is equal to total porosity φ.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "porosity",
          "E_MT",
          "E_MMT",
          "E_OMT"
        ],
        "units": {
          "porosity": "%",
          "E_MT": "GPa",
          "E_MMT": "GPa",
          "E_OMT": "GPa"
        }
      },
      "description": "Effective Young's modulus (GPa) predicted by classical MT, merged-pore modified MT (MMT), and open-cell modified MT (OMT) models for the artificial stainless steel case at porosities 10%–90%. The first row is a header with column names porosity,E_MT,E_MMT,E_OMT. For OMT, open porosity φ_open is assumed equal to the total porosity φ. The checker compares these predictions to hidden FEM reference data, evaluating relative error and RMSE improvement of OMT over MT."
    }
  ],
  "notes": "The task uses the stepwise differential MT scheme with merged and open-cell modifications as described in the paper's sections 2.2.1–2.2.4. Material: stainless steel (E=193 GPa, ν=0.27); pore size distribution: normal distribution, radii 10–100 μm, five equal-width classes, μ=55 μm, σ=31.8 μm. The CSV must include a header row with column names porosity,E_MT,E_MMT,E_OMT; porosity values are integer percents 10,20,...,90. For OMT, open porosity φ_open is equal to total porosity φ."
}
```

## How you are scored
A hidden verifier will compare your `predicted_moduli.csv` against reference effective Young's modulus data. The main evaluation will check the trend of OMT predictions relative to MT and MMT, assessing whether the OMT model yields improved accuracy (lower relative error) compared to the classical MT predictions. The verifier combines scores from all measured criteria; simply reporting numbers without correctly running the computational pipeline will not earn a high reward.
