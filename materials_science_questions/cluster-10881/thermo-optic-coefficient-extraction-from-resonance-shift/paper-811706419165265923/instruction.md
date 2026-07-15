# Steady-State Temperature Field in an End-Pumped Cylindrical Laser Crystal with Convective End-Face Conditions

## Problem background
Diode-pumped solid-state lasers suffer from thermal effects because a fraction of the absorbed pump energy is converted to heat, causing a non-uniform temperature rise inside the laser crystal. Accurately modeling the steady-state temperature field is critical for predicting thermal lensing, distortion, and laser stability. This work addresses the case of an end-pumped cylindrical Nd:YAG crystal where, in addition to side-face cooling, the crystal ends exchange heat with the ambient air through convection. The task is to compute the temperature field for several heat-transfer strengths and to quantify how the temperature and the resulting thermal distortion at the pumped face depend on the end-face cooling condition.

## Approach
The temperature field is governed by a Poisson equation with a volumetric heat source that arises from the absorbed pump light (a Gaussian profile in radius, exponentially decaying along the crystal axis). The side face of the crystal is held at a constant temperature, and the two end faces satisfy mixed (convective) boundary conditions with a heat-transfer parameter σ. The solution is expressed as a series of zeroth-order Bessel functions in the radial direction; the axial dependence is obtained from a one-dimensional boundary-value problem that is solved analytically for each radial mode. The Bessel series is truncated after enough terms to guarantee convergence. Three values of σ are considered: zero (adiabatic ends), 0.6 (finite heat transfer), and a very large value that approximates the limit of infinite heat transfer (isothermal ends at the ambient air temperature).

## Reproduction target
Compute the steady-state temperature field u(r,z) inside an Nd:YAG crystal for three end-face heat-transfer conditions: σ = 0, σ = 0.6, and a large σ (e.g., 100) that approximates σ → ∞. Evaluate the field on a regular Cartesian grid covering r ∈ [0, 3] mm and z ∈ [0, 2] mm, using at least 100×100 points for each σ value. Use the crystal parameters: radius 3 mm, length 2 mm, thermal conductivity 13 W/(m·K), absorption coefficient 20.7 cm⁻¹, pump beam radius 0.32 mm, pump power 20 W, heat conversion factor η = 1 − (808 nm / 1064 nm), and ambient relative temperature 5 °C. Write the grid points to temperature_field.csv with columns sigma, r_mm, z_mm, u_degC. From this output the hidden verifier will extract the maximum temperature and its location, and will compute the maximum thermal distortion at the pumped end, checking how both quantities change with σ.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute temperature field on a grid
- Role: scored (load-bearing)
- Action: Implement the analytical eigenfunction expansion to compute the steady temperature field u(r,z) inside a cylindrical laser crystal for three values of the end-face heat-transfer parameter sigma (0, 0.6, and a large value approximating infinity) on a regular Cartesian grid covering r in [0,3] mm and z in [0,2] mm (minimum 100×100 points per sigma). Use the crystal parameters from the standard Nd:YAG specifications: radius 3 mm, length 2 mm, thermal conductivity 13 W/(m·K), absorption coefficient 20.7 cm⁻¹, pump beam radius 0.32 mm, pump power 20 W, heat conversion factor eta = 1 − (808 nm / 1064 nm), ambient relative temperature T = 5 °C. Write the computed grid points to temperature_field.csv.
- Output file: `/app/outputs/temperature_field.csv`
- Format: csv
- Contract: CSV with header: sigma (dimensionless), r_mm (float, radial position 0–3 mm), z_mm (float, axial position 0–2 mm), u_degC (float, computed relative temperature). One row per grid point for each sigma value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_field.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_field.csv
- path: `/app/outputs/temperature_field.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Gridded temperature field u(r,z) for three heat-transfer conditions. The checker will extract temperature maxima and compute thermal distortion l_z(r) = alpha * integral_0^L u(r,z) dz, compare the maxima to hidden gold, and verify the trend that both maxima decrease as sigma increases.
- schema:
  - `type`: table
  - `required_columns`: `sigma`, `r_mm`, `z_mm`, `u_degC`
  - `units`:
    - `r_mm`: mm
    - `z_mm`: mm
    - `u_degC`: °C

Notes: The checker recomputes derived quantities from the raw temperature field; no separate thermal distortion output is required from the agent. The hidden gold values are the paper's reported maximum temperatures and thermal distortions for each sigma value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "sigma",
          "r_mm",
          "z_mm",
          "u_degC"
        ],
        "units": {
          "r_mm": "mm",
          "z_mm": "mm",
          "u_degC": "°C"
        }
      },
      "description": "Gridded temperature field u(r,z) for three heat-transfer conditions. The checker will extract temperature maxima and compute thermal distortion l_z(r) = alpha * integral_0^L u(r,z) dz, compare the maxima to hidden gold, and verify the trend that both maxima decrease as sigma increases."
    }
  ],
  "notes": "The checker recomputes derived quantities from the raw temperature field; no separate thermal distortion output is required from the agent. The hidden gold values are the paper's reported maximum temperatures and thermal distortions for each sigma value."
}
```

## How you are scored
A hidden verifier reads your temperature_field.csv and groups the data by sigma. For each σ, it locates the maximum temperature and its (r,z) coordinates, and numerically integrates the temperature field along z for every radial point to obtain the thermal distortion profile l_z(r) = α ∫₀ᴸ u(r,z) dz, from which the maximum distortion at the pumped end (z = 0) is taken. These derived quantities are compared against hidden reference values using tolerances that account for numerical discretization and series truncation. The verifier also confirms that both the maximum temperature and the maximum thermal distortion decrease as σ increases. The stage score is the primary component of the final reward; a solution that implements the correct physics and yields results consistent with the reference within the allowed tolerances receives full credit, and a better-than-reference result is never penalized.
