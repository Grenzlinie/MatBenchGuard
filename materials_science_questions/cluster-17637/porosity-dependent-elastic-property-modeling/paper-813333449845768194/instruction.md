# Porosity-Dependent Elastic Property Modeling in Porous Silicon Superlattices

## Problem background
Porous silicon superlattices (SLs) are multilayered films formed by periodically alternating two porous silicon layers with different porosities. Their effective elastic constants depend on the porosity and layer structure, making them candidates for tunable mechanical applications. Brillouin light scattering (BLS) experiments have measured the elastic properties of single-layer porous silicon films and of SLs. The Grimsditch-Nizzoli (GN) effective medium model provides a theoretical prediction of the superlattice elastic constants based on the properties of the constituent layers. This task focuses on the computational side: using experimentally determined single-layer elastic constants, you will compute the GN model predictions for the elastic constants of the SLs, and fit an empirical porosity-dependence law to the single-layer data.

## Approach
The GN model treats a superlattice of cubic-symmetry layers as a tetragonal effective medium. For two alternating layers with elastic constants c11^[ζ], c12^[ζ], c44^[ζ] (ζ=1,2) and thickness fractions f^[1], f^[2] (f^[1]+f^[2]=1), the effective constants c11, c13, c33, c44 are given by the following algebraic expressions:

\[
\begin{aligned}
c_{13} &= \frac{\frac{c_{12}^{[1]} c_{11}^{[2]} f^{[1]}}{c_{11}^{[1]}} + c_{12}^{[2]} f^{[2]}}{\frac{c_{11}^{[2]} f^{[1]}}{c_{11}^{[1]}} + f^{[2]}},\\[4pt]
c_{33} &= \frac{c_{11}^{[2]} f^{[1]} + c_{11}^{[2]} f^{[2]}}{\frac{c_{11}^{[2]} f^{[1]}}{c_{11}^{[1]}} + f^{[2]}},\\[4pt]
c_{44} &= \frac{c_{44}^{[2]} f^{[1]} + c_{44}^{[2]} f^{[2]}}{\frac{c_{44}^{[2]} f^{[1]}}{c_{44}^{[1]}} + f^{[2]}},\\[4pt]
c_{11} &= \frac{f^{[1]} \left(c_{12}^{[1]} + c_{11}^{[1]}\frac{c_{12}^{[2]}-c_{12}^{[1]}}{c_{11}^{[1]}} + c_{11}^{[2]} f^{[2]}\right)}{f^{[1]}+f^{[2]}} - \frac{f^{[1]} \frac{c_{12}^{[2]}-c_{12}^{[1]}}{c_{11}^{[1]}} \left(c_{11}^{[2]} f^{[1]} + c_{11}^{[2]} f^{[2]}\right)}{\left(f^{[1]}+f^{[2]}\right)\left(\frac{c_{11}^{[2]} f^{[1]}}{c_{11}^{[1]}} + f^{[2]}\right)}.
\end{aligned}
\]

All elastic constants are in GPa. You will evaluate these for each of the seven superlattice samples using the input data provided below.

The porosity dependence of the single-layer elastic constants is empirically described by a power-law: \(c_{ij} = c_{ij}^{c-Si} (1 - \xi)^{\gamma_{ij}}\), where \(c_{ij}^{c-Si}\) is the elastic constant of crystalline silicon (\(c_{11}^{c-Si}=166\) GPa, \(c_{44}^{c-Si}=79\) GPa) and \(\xi\) is the porosity fraction. By performing a least-squares fit to the single-layer \(c_{11}\) and \(c_{44}\) data, you will determine the best-fit exponents \(\gamma_{11}\) and \(\gamma_{44}\).

## Reproduction target
You are provided with the following experimentally determined single-layer elastic constants (in GPa) for eight porosity levels:

| ξ (%) | c11 | c12 | c44 |
|-------|-----|-----|-----|
| 33    | 46  | 16  | 17  |
| 44    | 36  | 14  | 14  |
| 48    | 25  | 13  | 12  |
| 52    | 17  | 12  | 10  |
| 54    | 13  | 9   | 8   |
| 59    | 13  | 9   | 8   |
| 70    | 6.7 | 5   | 4.8 |
| 72    | 5.5 | 3.4 | 3.5 |

The superlattice samples consist of a 59%‑porosity layer (layer 1) with thickness \(d^{[1]}=10\) nm and a second layer (layer 2) whose porosity, thickness, and elastic constants are taken from the table above according to the following list (the sample identifier indicates the porosity of the two layers, e.g., “59‑33%” means layer 1 is 59% and layer 2 is 33%):

| Sample   | d[2] (nm) |
|----------|-----------|
| 59‑33%   | 15.6      |
| 59‑44%   | 20        |
| 59‑48%   | 10        |
| 59‑52%   | 10        |
| 59‑54%   | 10        |
| 59‑70%   | 10        |
| 59‑72%   | 10        |

For each sample, compute the thickness fractions \(f^{[1]} = d^{[1]}/(d^{[1]}+d^{[2]})\), \(f^{[2]} = d^{[2]}/(d^{[1]}+d^{[2]})\) and use the corresponding single‑layer elastic constants to evaluate the GN model formulas above. The result must be saved as a CSV file with columns: `sample`, `c11`, `c13`, `c33`, `c44` (all in GPa).

Separately, fit the empirical model \(c_{ij} = c_{ij}^{c-Si} (1 - \xi)^{\gamma_{ij}}\) to the single‑layer \(c_{11}\) and \(c_{44}\) data (ξ as a fraction, i.e., ξ=0.33, … ,0.72) using least‑squares regression. Report the fitted exponents \(\gamma_{11}\) and \(\gamma_{44}\) in a JSON file with keys `gamma_11` and `gamma_44`.

## Assets

- Python 3 interpreter
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Superlattice Elastic Constants via Grimsditch-Nizzoli Model
- Role: scored (load-bearing)
- Action: Using the provided single-layer elastic constants (c11, c12, c44) for each of eight porosity levels (33% to 72%), the crystalline silicon reference constants, and the layer thickness fractions for seven superlattice samples (as listed in the instruction), compute the effective elastic constants c11, c13, c33, c44 (all in GPa) for each superlattice. The computation follows the Grimsditch-Nizzoli effective medium model for layered composites of cubic symmetry, which relates the superlattice constants to the constituent single-layer constants and thickness fractions. Output the results as a CSV file.
- Output file: `/app/outputs/sl_elastic_constants.csv`
- Format: csv
- Contract: Columns: sample (str), c11 (float GPa), c13 (float GPa), c33 (float GPa), c44 (float GPa). Seven rows, one per superlattice sample.
- Scoring: scored by hidden verifier

### Step 2: Fit Porosity-Dependence Exponents for Single-Layer c11 and c44
- Role: scored
- Action: Using the provided single-layer c11 and c44 values for the eight porosity levels and the crystalline silicon reference values (c11_c-Si = 166 GPa, c44_c-Si = 79 GPa), perform a least-squares fit of the empirical model c_ij = c_ij^(c-Si) * (1 - ξ)^γ_ij to the c11 vs. porosity data and to the c44 vs. porosity data. Report the best-fit exponents γ11 and γ44 in a JSON object.
- Output file: `/app/outputs/porosity_fit_exponents.json`
- Format: json
- Contract: {'gamma_11': float, 'gamma_44': float}. Both are dimensionless exponents.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sl_elastic_constants.csv`
- `/app/outputs/porosity_fit_exponents.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sl_elastic_constants.csv
- path: `/app/outputs/sl_elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Superlattice effective elastic constants predicted by the GN model; the checker recomputes them from the same input data and compares within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `c11`, `c13`, `c33`, `c44`
  - `units`:
    - `c11`: GPa
    - `c13`: GPa
    - `c33`: GPa
    - `c44`: GPa

### porosity_fit_exponents.json
- path: `/app/outputs/porosity_fit_exponents.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Fitted porosity exponents γ11 and γ44; the checker independently refits the same empirical model and compares the values within a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `gamma_11`: number (dimensionless)
    - `gamma_44`: number (dimensionless)

Notes: The hidden checker recomputes both artifacts from the same single-layer elastic constants and superlattice parameters that are provided in the public instruction. Tolerances are hidden but designed to accommodate legitimate numerical differences from reimplementation while rejecting unconstrained guesses.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sl_elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "c11",
          "c13",
          "c33",
          "c44"
        ],
        "units": {
          "c11": "GPa",
          "c13": "GPa",
          "c33": "GPa",
          "c44": "GPa"
        }
      },
      "description": "Superlattice effective elastic constants predicted by the GN model; the checker recomputes them from the same input data and compares within a hidden tolerance."
    },
    {
      "file": "porosity_fit_exponents.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "gamma_11": "number (dimensionless)",
          "gamma_44": "number (dimensionless)"
        }
      },
      "description": "Fitted porosity exponents γ11 and γ44; the checker independently refits the same empirical model and compares the values within a hidden tolerance."
    }
  ],
  "notes": "The hidden checker recomputes both artifacts from the same single-layer elastic constants and superlattice parameters that are provided in the public instruction. Tolerances are hidden but designed to accommodate legitimate numerical differences from reimplementation while rejecting unconstrained guesses."
}
```

## How you are scored
A hidden verifier independently recomputes the expected superlattice elastic constants and the porosity‑dependence exponents using the same input data and the same formulas. Your `sl_elastic_constants.csv` is compared to the recomputed values; full credit requires agreement within the verifier’s tolerance. Your `porosity_fit_exponents.json` is compared to the recomputed exponents; the closer your values are to the hidden reference, the higher your score. The final reward is a weighted combination of the two artifact scores. No additional information from the source paper is needed.
