# Silica Polymerization Prediction for Cerro Prieto Brine

## Problem background
In geothermal brine handling, understanding silica polymerization is essential because rapid conversion of dissolved silica to colloidal amorphous silica can cause severe scaling and plugging. This task focuses on predicting both the molecular deposition rate (the chemical deposition of dissolved silica onto solid surfaces) and the time shift of homogeneous nucleation curves for a simplified brine system. The goal is to compute these two quantities for a given set of brine conditions, which serve as indicators of whether scale formation will be dominated by molecular deposition or by fast nucleation and aggregation. The work develops semi-empirical equations and tabulated type curves that account for temperature, pH, salinity, and silica concentration, and a worked example illustrates their application.

## Approach
The computation proceeds step by step as follows. All necessary constants, equations, and tabulated values are given here; you must reproduce the calculation exactly.

### 1. Activity coefficients and dissociation fraction
Use the Debye-Hückel equation (Eq. A-2):
```
log γ = - (A_DH * I^0.5) / (1 + a * B_DH * I^0.5) + b * I
```
With T = 373.15 K, m_NaCl = 0.3 mol/kg, ionic strength I = m_NaCl = 0.3.
From Table 2 (100°C row): A_DH = 0.596, B_DH = 0.341.
For Na⁺: a = 4, b = 0.075.
For H₃SiO₄⁻: a = 4, b = 0.0.
Calculate γ_Na⁺ and γ_sil.

Then, dissociation fraction α (Eq. A-3):
```
α = 1 / [1 + γ_sil * 10^(pK_sil - pH)]
```
At 100°C, pK_sil = 9.10.

### 2. Pure-water solubility and water activity
```
c_o (g/kg H₂O) = 10^(1.52 - 731/T)    (Eq. 4)
a_w = exp(-0.033 * m_NaCl)            (Eq. 6)
```

### 3. Sodium activity and nominal pH
```
[Na⁺] = γ_Na⁺ * m_NaCl               (Eq. A-4)
pH_nom = pH + log10([Na⁺] / 0.069)  (Eq. 10)
```

### 4. Saturation ratios
Undissociated silica concentration: c_i(1 - α) with c_i = 1.0 g/kg.
```
S_a = c_i(1 - α) / c_o               (Eq. 3)
S = S_a / a_w                        (Eq. 7)
```

### 5. Surface ionization factor F and integral I
```
F   = 0.45 f'(pH) + 0.55 f'(pH_nom)   (Eq. 9)
I   = 0.45 i(pH) + 0.55 i(pH_nom)     (Eq. 12 in the paper, where i is the integral of f over pH)
```
Values of f' and i are given in Tables 1 and 4 below. The tables provide f' and i at pH values spaced by 0.02. For intermediate pH values, use linear interpolation.

### 6. Surface tension
```
γ (erg·cm⁻²) = 63.68 - 0.049 * T - 0.2174 * T * I   (Eq. 11)
```

### 7. Reference curve and base rate
From Table 3, for c_i = 1.0 g/kg and T = 100°C:
  S_ref = 2.75
  F_ref = 2.41

The base molecular deposition rate at pH = 7.0 (F=1), T=100°C, and c_i(1-α) ≈ 0.981 g/kg is:
  R_md_base = 2.2 × 10⁻⁷ g·cm⁻²·min⁻¹.

### 8. Final rate and time shift
```
R_md = R_md_base * F

Δlog t = -1 - log10(F) + 1412 * (γ / T)^3 * (ln S)^(-2) - F_ref   (Eq. 13)
```
(where ln is natural log; the constant 1412 is an integer in the paper, sometimes written as 1.412×10³.)

Write R_md (g·cm⁻²·min⁻¹) and Δlog t (dimensionless) to results.json.

### Table 1: f'(pH) vs pH
(values for each pH from 5.0 to 8.4 at intervals of 0.02; columns: pH, 0.0, 0.02, 0.04, 0.06, 0.08)

| pH  | 0.0   | 0.02  | 0.04  | 0.06  | 0.08  |
|-----|-------|-------|-------|-------|-------|
| 5.0 | 0.0208| 0.0218| 0.0228| 0.0238| 0.0249|
| 5.1 | 0.0261| 0.0273| 0.0285| 0.0299| 0.0312|
| 5.2 | 0.0327| 0.0342| 0.0357| 0.0374| 0.0391|
| 5.3 | 0.0409| 0.0427| 0.0447| 0.0467| 0.0488|
| 5.4 | 0.0511| 0.0534| 0.0558| 0.0583| 0.0609|
| 5.5 | 0.0637| 0.0665| 0.0695| 0.0726| 0.0758|
| 5.6 | 0.0792| 0.0827| 0.0863| 0.0901| 0.0941|
| 5.7 | 0.0982| 0.1025| 0.1069| 0.1116| 0.1164|
| 5.8 | 0.1214| 0.1265| 0.1319| 0.1375| 0.1433|
| 5.9 | 0.1493| 0.1555| 0.1620| 0.1687| 0.1783|
| 6.0 | 0.185 | 0.193 | 0.201 | 0.209 | 0.217 |
| 6.1 | 0.225 | 0.234 | 0.243 | 0.253 | 0.262 |
| 6.2 | 0.273 | 0.283 | 0.294 | 0.305 | 0.316 |
| 6.3 | 0.328 | 0.340 | 0.353 | 0.366 | 0.379 |
| 6.4 | 0.392 | 0.407 | 0.421 | 0.436 | 0.451 |
| 6.5 | 0.467 | 0.483 | 0.500 | 0.517 | 0.534 |
| 6.6 | 0.552 | 0.570 | 0.589 | 0.608 | 0.627 |
| 6.7 | 0.648 | 0.668 | 0.689 | 0.710 | 0.732 |
| 6.8 | 0.754 | 0.777 | 0.800 | 0.824 | 0.848 |
| 6.9 | 0.872 | 0.897 | 0.922 | 0.948 | 0.974 |
| 7.0 | 1.000 | 1.027 | 1.054 | 1.082 | 1.109 |
| 7.1 | 1.138 | 1.166 | 1.195 | 1.225 | 1.254 |
| 7.2 | 1.284 | 1.315 | 1.345 | 1.376 | 1.408 |
| 7.3 | 1.439 | 1.471 | 1.503 | 1.535 | 1.568 |
| 7.4 | 1.601 | 1.634 | 1.668 | 1.701 | 1.735 |
| 7.5 | 1.769 | 1.804 | 1.839 | 1.873 | 1.909 |
| 7.6 | 1.94  | 1.98  | 2.02  | 2.05  | 2.09  |
| 7.7 | 2.12  | 2.16  | 2.20  | 2.24  | 2.27  |
| 7.8 | 2.31  | 2.35  | 2.39  | 2.42  | 2.46  |
| 7.9 | 2.50  | 2.54  | 2.58  | 2.62  | 2.66  |
| 8.0 | 2.70  | 2.74  | 2.78  | 2.82  | 2.86  |
| 8.1 | 2.90  | 2.94  | 2.98  | 3.02  | 3.06  |
| 8.2 | 3.10  | 3.14  | 3.18  | 3.22  | 3.27  |
| 8.3 | 3.31  | 3.35  | 3.39  | 3.43  | 3.47  |
| 8.4 | 3.52  | 3.56  | 3.60  | 3.64  | 3.68  |

### Table 4: i(pH) vs pH
(values for each pH from 5.0 to 8.4 at intervals of 0.02)

| pH  | 0.0   | 0.02  | 0.04  | 0.06  | 0.08  |
|-----|-------|-------|-------|-------|-------|
| 5.0 | 0.0011| 0.0011| 0.0012| 0.0012| 0.0013|
| 5.1 | 0.0014| 0.0014| 0.0015| 0.0016| 0.0016|
| 5.2 | 0.0017| 0.0018| 0.0019| 0.0020| 0.0020|
| 5.3 | 0.0021| 0.0022| 0.0023| 0.0025| 0.0026|
| 5.4 | 0.0027| 0.0028| 0.0029| 0.0031| 0.0032|
| 5.5 | 0.0034| 0.0035| 0.0037| 0.0039| 0.0040|
| 5.6 | 0.0042| 0.0044| 0.0046| 0.0048| 0.0050|
| 5.7 | 0.0053| 0.0055| 0.0058| 0.0060| 0.0063|
| 5.8 | 0.0066| 0.0069| 0.0072| 0.0075| 0.0078|
| 5.9 | 0.0082| 0.0085| 0.0089| 0.0093| 0.0097|
| 6.0 | 0.0102| 0.0106| 0.0111| 0.0116| 0.0121|
| 6.1 | 0.0126| 0.0132| 0.0138| 0.0144| 0.0150|
| 6.2 | 0.0156| 0.0163| 0.0170| 0.0177| 0.0184|
| 6.3 | 0.0192| 0.0200| 0.0208| 0.0217| 0.0225|
| 6.4 | 0.0235| 0.0244| 0.0254| 0.0264| 0.0274|
| 6.5 | 0.0285| 0.0296| 0.0308| 0.0320| 0.0332|
| 6.6 | 0.0345| 0.0358| 0.0372| 0.0386| 0.0400|
| 6.7 | 0.0415| 0.0431| 0.0447| 0.0463| 0.0480|
| 6.8 | 0.0497| 0.0515| 0.0534| 0.0553| 0.0572|
| 6.9 | 0.0592| 0.0613| 0.0634| 0.0656| 0.0679|
| 7.0 | 0.0702| 0.0725| 0.0750| 0.0775| 0.0801|
| 7.1 | 0.0827| 0.0854| 0.0882| 0.0911| 0.0940|
| 7.2 | 0.0970| 0.1001| 0.1032| 0.1064| 0.1098|
| 7.3 | 0.1131| 0.1166| 0.1202| 0.1238| 0.1275|
| 7.4 | 0.1313| 0.1352| 0.1391| 0.1432| 0.1473|
| 7.5 | 0.1516| 0.1559| 0.1603| 0.1648| 0.1694|
| 7.6 | 0.1741| 0.1789| 0.1837| 0.1887| 0.1937|
| 7.7 | 0.1989| 0.2041| 0.2095| 0.2149| 0.2204|
| 7.8 | 0.2261| 0.2318| 0.2376| 0.2435| 0.2495|
| 7.9 | 0.2556| 0.2618| 0.2681| 0.2745| 0.2809|
| 8.0 | 0.2875| 0.2942| 0.3009| 0.3078| 0.3147|
| 8.1 | 0.3217| 0.3288| 0.3360| 0.3433| 0.3507|
| 8.2 | 0.3582| 0.3657| 0.3733| 0.3810| 0.3888|
| 8.3 | 0.3966| 0.4045| 0.4125| 0.4206| 0.4288|
| 8.4 | 0.4370| 0.4452| 0.4535| 0.4619| 0.4704|

### Table 2: Parameters for activity coefficients and pK_sil
(100°C row)

| Species       | a   | b     | Use to calculate  |
|---------------|-----|-------|-------------------|
| Na⁺           | 4   | 0.075 | γ_Na⁺, [Na⁺]     |
| H₃SiO₄⁻       | 4   | 0.0   | γ_sil, α          |
| Temperature (°C) | pK_sil | A_DH  | B_DH  |
| 100            | 9.10   | 0.596 | 0.341 |

### Table 3: Reference values S_ref and F_ref
For c_i = 1.0 g/kg at 100°C: S_ref = 2.75, F_ref = 2.41.
(Other rows omitted for brevity; only the 1.0 g/kg, 100°C row is needed.)

## Reproduction target
Implement the sequence of calculations to determine the molecular deposition rate R_md (g·cm⁻²·min⁻¹) and the nucleation time shift Δlog t (dimensionless) for brine with the following conditions: temperature = 373.15 K (100 °C), pH = 7.2, effective NaCl molality = 0.3 mol/kg, initial dissolved silica concentration = 1.0 g/kg. Write the computed R_md and Delta_log_t to the JSON file results.json under the prescribed keys.

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Compute R_md and Δlog t for Cerro Prieto brine
- Role: scored (load-bearing)
- Action: Implement the paper's calculation sequence for the Cerro Prieto example: from the given conditions (T=373.15 K, pH=7.2, m_NaCl=0.3 mol/kg, initial silica 1.0 g/kg) compute activity coefficients and dissociation fraction using the Debye‑Hückel formulas with the provided parameters; pure‑water solubility and water activity; sodium activity, undissociated silica concentration, and saturation ratios S_a and S; nominal pH; surface ionization factor F and integral I via the two‑term interpolation using tabulated function values; surface tension γ; select the appropriate reference curve from the tabulated reference values and obtain F_ref; obtain the base deposition rate at pH=7.0 for the current temperature and concentration; calculate the final R_md = base_rate × F; and compute Δlog t using the shift equation involving F, γ, T, S, and F_ref. Write the computed R_md (g·cm⁻²·min⁻¹) and Δlog t (dimensionless) to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with numeric keys 'R_md' (float, unit: g·cm⁻²·min⁻¹) and 'Delta_log_t' (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the two computed quantities: the molecular deposition rate and the nucleation time shift under the specified brine conditions.
- schema:
  - `type`: object
  - `required`:
    - `R_md`: number
    - `Delta_log_t`: number
  - `units`:
    - `R_md`: g·cm⁻²·min⁻¹
    - `Delta_log_t`: dimensionless

Notes: The checker compares these values against hidden reference numbers using a relative tolerance for R_md and an absolute tolerance for Delta_log_t. Better-than-reference values are not penalized.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "R_md": "number",
          "Delta_log_t": "number"
        },
        "units": {
          "R_md": "g·cm⁻²·min⁻¹",
          "Delta_log_t": "dimensionless"
        }
      },
      "description": "Contains the two computed quantities: the molecular deposition rate and the nucleation time shift under the specified brine conditions."
    }
  ],
  "notes": "The checker compares these values against hidden reference numbers using a relative tolerance for R_md and an absolute tolerance for Delta_log_t. Better-than-reference values are not penalized."
}
```

## How you are scored
A hidden verifier independently evaluates your output artifact. It reads results.json, extracts the two reported values, and compares them against reference numbers that correspond to the correct solution for the given conditions. The comparison uses appropriate tolerances that allow for minor numerical differences inherent in re‑implementation. Your final reward is based on how many of the two values meet the required accuracy. Simply writing numbers that look plausible is not sufficient; the values must result from faithfully executing the described computational steps.
