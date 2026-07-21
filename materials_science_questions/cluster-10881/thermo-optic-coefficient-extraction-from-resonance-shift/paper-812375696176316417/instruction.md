# Thermal Lens Focal Length from Analytic Temperature Distribution in a Laser Output Coupler

## Problem background
In high-power CO₂ lasers, the output coupler absorbs a fraction of the laser power, producing a non-uniform temperature distribution. This temperature gradient causes thermal expansion and refractive index changes, which together form a thermal lens that degrades output beam quality. Quantifying the resulting thermal lens focal length as a function of input laser power is critical for laser design.

## Approach
The temperature distribution in the coupler is obtained by solving the steady-state heat conduction equation assuming uniform volumetric heating and a linear edge temperature profile along the optical axis. The analytic solution uses Bessel functions and depends on a single eigenparameter λ determined from the center-to-edge temperature ratio. From the temperature field, the optical path difference between the center and edge is integrated, and a thin‑lens approximation is applied to compute the thermal lens focal length.

## Reproduction target
Compute the thermal lens focal length f_th (in cm) for a GaAs output coupler with the geometry and material properties specified below, evaluated for input laser powers P ranging from 0 W to 2000 W in steps of 100 W. Output the results as `thermal_focal_length.csv` with columns `P` (W) and `f_th` (cm).

## Given parameters (GaAs output coupler)

| Symbol | Value               | Units      | Description |
|--------|---------------------|------------|-------------|
| a      | 1.0                 | cm         | radius |
| d      | 0.5                 | cm         | thickness |
| k      | 0.037               | W/(cm·K)   | thermal conductivity |
| β      | 0.012               | cm⁻¹       | absorption coefficient |
| n0     | 3.30                | –          | refractive index at room temperature |
| γ      | 18.7 × 10⁻⁵         | K⁻¹        | thermo‑optic coefficient dn/dT |
| α      | 5.7 × 10⁻⁶          | K⁻¹        | thermal expansion coefficient |
| T0     | 298.0               | K          | temperature at r=a, z=0 (inside edge) |
| Tn     | 298.1               | K          | temperature at r=a, z=d (outside edge) |
| g      | 0.2                 | K/cm       | linear edge temperature gradient, g = (T_n − T_0)/d |

The centre temperature Tc (in K) depends on the input laser power P (in W) according to the experimentally determined relation:

  Tc = T0 + 2×10⁻⁴ · P

The intensity I (W/cm²) is uniform over the circular cross‑section:

  I = P / (π a²)

## Assets

- NumPy: numpy
- SciPy: scipy
- (Matplotlib is optional and not required for this task)

## Workflow steps

### Step 1: Determine eigenparameter λ for each power P
- Role: process
- Action: For each laser power P from 0 W to 2000 W in steps of 100 W, compute Tc as above, then solve the transcendental equation

  J₀(λ a) = T0 / Tc

  for the positive eigenvalue λ (in cm⁻¹). For P = 0 the ratio is 1 and λ = 0.
  Use a root‑finding method (e.g., bisection between 0 and the first zero of J₀, ≈ 2.4048).

### Step 2: Compute optical path difference ΔL for each power P
- Role: process
- Action: Using the coupler parameters (a, d, k, β, n0, α, γ, T0, g) and the λ value from Step 1, compute the optical path difference between the centre and the edge directly from the closed‑form expression (Eq. 20):

  ΔL = (α + γ) n0 · ( T0·d + ½·g·d² + (β·I)/(6·k)·d³ ) · ( 1 / J₀(λ a) − 1 )

  where I = P/(π a²).

### Step 3: Compute thermal lens focal length f_th
- Role: scored (load‑bearing)
- Action: For each P, compute the thin‑lens focal length

  f_th = a² / ( 2 · ΔL · (n0 − 1) )

  For P = 0, ΔL = 0 and f_th → ∞; in the output CSV you may represent this as “inf” or a numerically very large value (the verifier accepts “inf”).
  Write a CSV file `thermal_focal_length.csv` with columns `P` (W) and `f_th` (cm). The range must cover P = 0, 100, 200, …, 2000 W.
- Output file: `/app/outputs/thermal_focal_length.csv`
- Format: csv
- Contract: CSV with two columns: `P` (float, Watts) and `f_th` (float or “inf”, cm)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_focal_length.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_focal_length.csv
- path: `/app/outputs/thermal_focal_length.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The computed thermal lens focal length for each input laser power from 0 to 2000 W in steps of 100 W.
- schema:
  - `type`: table
  - `required_columns`: `P`, `f_th`
  - `units`:
    - `P`: W
    - `f_th`: cm

Notes: The beam quality analysis (stage 4) is omitted because the resonator parameters (R, L) are not available in the provided data and cannot be reliably reproduced.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_focal_length.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "P",
          "f_th"
        ],
        "units": {
          "P": "W",
          "f_th": "cm"
        }
      },
      "description": "The computed thermal lens focal length for each input laser power from 0 to 2000 W in steps of 100 W."
    }
  ],
  "notes": "The beam quality analysis (stage 4) is omitted because the resonator parameters (R, L) are not available in the provided data and cannot be reliably reproduced."
}
```

## How you are scored
A hidden verifier will recompute the thermal lens focal length from the same analytic expressions and the same coupler parameters, using the formulas given above. It will compare your reported f_th values against the recomputed values. All values must fall within an allowed relative margin. The reward is based on the accuracy of your computed results; simply guessing or hardcoding pre-determined numbers will not succeed.