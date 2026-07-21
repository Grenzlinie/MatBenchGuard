# BaTiO3 electro‑optic coefficients and birefringence values

## Problem background
The electro‑optic (Pockels) effect in ferroelectric perovskites such as BaTiO3 underlies many photonic applications. In the tetragonal phase, the refractive index changes can be described through a microscopic model that accounts for two contributions: the piezoelectric effect (lattice deformation) and the spontaneous Kerr effect (non‑linear polarizabilities). A theoretical study in the literature has derived the following eight quantities of interest.

## Quantities to report
Based on that model, the numerical values for BaTiO3 are:

- **r33_piezo** – linear electro‑optic coefficient *r*₃₃ arising from the piezoelectric contribution (m V⁻¹)
- **r33_Kerr_clamp** – clamped *r*₃₃ from the Kerr contribution (m V⁻¹)
- **r33_Kerr_free** – free *r*₃₃ from the Kerr contribution (m V⁻¹)
- **r33_free** – total free *r*₃₃ = r33_piezo + r33_Kerr_free (m V⁻¹)
- **r13_Kerr_clamp** – clamped *r*₁₃ from the Kerr contribution (m V⁻¹)
- **delta_n_piezo** – birefringence from the piezoelectric contribution (dimensionless)
- **delta_n_Kerr** – birefringence from the Kerr contribution (dimensionless)
- **delta_n_total** – total birefringence = delta_n_piezo + delta_n_Kerr (dimensionless)

The exact numerical results (taken directly from the study) are:

| Quantity                | Value (SI)        |
|-------------------------|-------------------|
| r33_piezo               | 1.9261 × 10⁻¹¹    |
| r33_Kerr_clamp          | 4.1903 × 10⁻¹¹    |
| r33_Kerr_free           | 6.4583 × 10⁻¹¹    |
| r33_free                | 8.3843 × 10⁻¹¹    |
| r13_Kerr_clamp          | 1.5181 × 10⁻¹¹    |
| delta_n_piezo           | −0.0339            |
| delta_n_Kerr            | −0.0566            |
| delta_n_total           | −0.0905            |

No further computation is required; the values above are the final results of the model.

## Task
Write these eight quantities into a single JSON file named **`electro_optic_results.json`** and place it in the output directory (`/app/outputs`). The JSON object must have exactly the following keys with the corresponding numeric values as shown:

```json
{
  "r33_piezo": 1.9261e-11,
  "r33_Kerr_clamp": 4.1903e-11,
  "r33_Kerr_free": 6.4583e-11,
  "r33_free": 8.3843e-11,
  "r13_Kerr_clamp": 1.5181e-11,
  "delta_n_piezo": -0.0339,
  "delta_n_Kerr": -0.0566,
  "delta_n_total": -0.0905
}
```

Use exactly the numeric representations given; do not round or reformat them. The file path must be `/app/outputs/electro_optic_results.json`.