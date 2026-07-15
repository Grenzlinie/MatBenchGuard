# Compute Linear Elastic Energy Release Rate Components for a Cracked Orthotropic Lamina

## Problem background
In fracture mechanics of composite materials, the energy release rate quantifies the energy available for crack growth. For an anisotropic centre‑cracked lamina under biaxial loading, the linear elastic energy release rate can be decomposed into three load‑directional components. This task computes those components for a specific graphite‑epoxy lamina using analytical formulas from linear elastic fracture mechanics, and explores how they vary with the fibre orientation and the biaxial load factor.

## Approach
The linear elastic energy release rate is computed from the orthotropic compliance coefficients of the lamina and the applied far‑field forces. Under the assumption that the crack lies along the fibre direction, the mixed‑mode stress intensity factors are expressed in terms of the far‑field stresses, the crack half‑length, and the fibre angle. These intensity factors are converted to energy release rate components G<sub>I</sub> and G<sub>II</sub>, whose sum is then re‑organised into three directional components G<sub>x</sub>, G<sub>y</sub>, and G<sub>xy</sub>. The total linear elastic energy release rate G is the sum of these three components. The computation uses the given material constants, specimen geometry, and applied forces to evaluate the required terms for a set of prescribed fibre‑orientation angles and biaxial load factors.

## Reproduction target
Compute the linear elastic energy release rate components G<sub>x</sub>, G<sub>y</sub>, G<sub>xy</sub> and the total linear release rate G for a centre‑cracked T300/5208 graphite‑epoxy lamina. Use material constants E1=181 GPa, E2=10.3 GPa, G12=7.17 GPa, ν12=0.28; geometry half‑width Lx=0.3 m, half‑length Ly=0.3 m, thickness B=0.0025 m, crack half‑length a=0.05 m; applied force Fy=0.331 MN, with Fx = k · Fy. Compute for fibre orientations β = 0°, 30°, 45°, 60°, 90° at biaxial factor k=0.5, and additionally for β=45° at k = –1, 0, 1. Convert all results to MJ/m² and write them to the CSV file with columns: beta (deg), k, G_x (MJ/m²), G_y (MJ/m²), G_xy (MJ/m²), G_total (MJ/m²).

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute linear energy release rate components
- Role: scored (load-bearing)
- Action: Implement the analytical formulas for a center-cracked orthotropic lamina under biaxial loading using linear elastic fracture mechanics. Use material constants: E1=181 GPa, E2=10.3 GPa, G12=7.17 GPa, ν12=0.28. Geometry: half-width Lx=0.3 m, half-length Ly=0.3 m, thickness B=0.0025 m, crack half-length a=0.05 m. Applied force Fy=0.331 MN; Fx = k * Fy. First compute the compliance coefficients: a11 = 1/E1, a22 = 1/E2, a12 = -ν12/E1, a66 = 1/G12. Then compute the factor ψ = [√(a22/a11) + (2 a12 + a66)/(2 a11)]^(1/2) * √(a11 a22 / 2). Next, compute the directional linear energy release rate components:

Gx = (π a ψ) / (4 B^2 L_y^2) * F_x^2 * cos^2(β) * (cos^2(β) + √(a11/a22) * sin^2(β))
Gy = (π a ψ) / (4 B^2 L_x^2) * F_y^2 * sin^2(β) * (sin^2(β) + √(a11/a22) * cos^2(β))
Gxy = (π a ψ) / (2 B^2 L_x L_y) * F_x F_y * sin^2(β) cos^2(β) * (1 - √(a11/a22))

and the total G_total = Gx + Gy + Gxy. Compute these for fiber orientations β in [0°, 30°, 45°, 60°, 90°] with biaxial factor k=0.5, and additionally for β=45° with k values [-1, 0, 1]. Convert all energy release rates to MJ/m^2. Write the results to the output CSV file with columns: beta, k, G_x (MJ/m^2), G_y (MJ/m^2), G_xy (MJ/m^2), G_total (MJ/m^2). Ensure consistent units (Pa, m, MN → N).
- Output file: `/app/outputs/linear_energy_release_rates.csv`
- Format: csv
- Contract: Columns: beta (float, degrees), k (float, unitless), G_x (float, MJ/m^2), G_y (float, MJ/m^2), G_xy (float, MJ/m^2), G_total (float, MJ/m^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/linear_energy_release_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### linear_energy_release_rates.csv
- path: `/app/outputs/linear_energy_release_rates.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Linear elastic energy release rate components (Gx, Gy, Gxy) and total G computed from the LEFM formulas for the specified (β, k) conditions.
- schema:
  - `type`: table
  - `required_columns`: `beta`, `k`, `G_x`, `G_y`, `G_xy`, `G_total`
  - `units`:
    - `beta`: deg
    - `k`: unitless
    - `G_x`: MJ/m^2
    - `G_y`: MJ/m^2
    - `G_xy`: MJ/m^2
    - `G_total`: MJ/m^2

Notes: The nonlinear correction coefficients (Figure 6) are omitted because they require experimental load-displacement data or fitted power-law parameters not numerically provided in the paper. The linear portion is fully self-contained and reproducible.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "linear_energy_release_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "beta",
          "k",
          "G_x",
          "G_y",
          "G_xy",
          "G_total"
        ],
        "units": {
          "beta": "deg",
          "k": "unitless",
          "G_x": "MJ/m^2",
          "G_y": "MJ/m^2",
          "G_xy": "MJ/m^2",
          "G_total": "MJ/m^2"
        }
      },
      "description": "Linear elastic energy release rate components (Gx, Gy, Gxy) and total G computed from the LEFM formulas for the specified (β, k) conditions."
    }
  ],
  "notes": "The nonlinear correction coefficients (Figure 6) are omitted because they require experimental load-displacement data or fitted power-law parameters not numerically provided in the paper. The linear portion is fully self-contained and reproducible."
}
```

## How you are scored
A hidden verifier independently recomputes the same linear energy release rate components from your submitted CSV for each specified (β, k) condition. It compares your values to the expected quantities using predefined tolerances. Each entry carries a weight, and your final score is the fraction of entries that match, so reporting the paper’s numbers without performing the computation is not sufficient. The verifier also validates the file format and required columns.
