# Hot-Spot Temperature Reduction by Orthotropic Heat Spreader

## Problem background
On-chip hot spots in high-performance microprocessors are a critical thermal management challenge. One promising passive cooling strategy is to attach an orthotropic heat spreader with high in-plane thermal conductivity to the back of the silicon chip. Such a spreader laterally conducts heat away from a localised hot spot to cooler regions, thereby reducing the peak temperature. An analytical model has been developed to predict the hot‑spot temperature reduction achievable with an orthotropic spreader as a function of its in‑plane conductivity, thickness, and the system thermal parameters. In this task, you will implement that model and compute the key performance metrics for a representative chip/spreader configuration.

## Approach
The system is modelled as a two‑layer structure: a square silicon chip with a central square heat‑flux spot, and a square orthotropic spreader bonded on top. The back of the spreader is cooled by convection (uniform heat‑transfer coefficient). The analytical solution is obtained via separation of variables, yielding the excess temperature field on the active chip side as a Fourier‑series sum. Orthotropic conductivity in the spreader is handled through an equivalent isotropic transformation, which maps the anisotropic layer to an effective isotropic layer with transformed thickness and conductivity. The model provides the peak hot‑spot temperature, the spreading resistance, and the total thermal resistance (one‑dimensional conduction plus spreading). You will numerically evaluate the series solution for a fixed set of geometry and material properties (except for the in‑plane spreader conductivity, which you will vary) to compute the peak excess temperature at the hot‑spot centre. You will also compute the total thermal resistance as a function of spreader thickness for a specific in‑plane conductivity and determine the thickness that minimises this resistance.

## Reproduction target
Use the analytical model with the following fixed parameters: square chip side length 1 cm, thickness 250 µm, isotropic thermal conductivity 163 W m⁻¹ K⁻¹; square spreader thickness 500 µm, thru‑plane conductivity k_z = 5 W m⁻¹ K⁻¹; square hot spot side length 500 µm, heat flux 1.4 kW cm⁻²; convection coefficient on the back of the spreader 10 000 W m⁻² K⁻¹, ambient temperature 25 °C. Perform the following computations and write all results to a single JSON file named hot_spot_results.json:

1. Peak excess temperature at the hot‑spot centre (active chip side, z = 0) for three values of the spreader in‑plane conductivity:
   - k_xy = 5 W m⁻¹ K⁻¹
   - k_xy = 350 W m⁻¹ K⁻¹
   - k_xy = 1800 W m⁻¹ K⁻¹

2. For k_xy = 350 W m⁻¹ K⁻¹, compute the total thermal resistance (sum of one‑dimensional resistance and spreading resistance) as a function of spreader thickness, scan thicknesses to locate the minimum, and record:
   - the thickness (in µm) at which the minimum occurs, and
   - the minimum total thermal resistance (in K W⁻¹).

The JSON file must contain the five fields: kxy5_excess_temp, kxy350_excess_temp, kxy1800_excess_temp, kxy350_opt_thickness, and kxy350_total_thermal_resistance. All temperatures are in °C, the thickness in µm, and the thermal resistance in K W⁻¹.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute orthotropic spreader hot-spot cooling and optimum thickness
- Role: scored (load-bearing)
- Action: Implement the analytical temperature solution for a two-layer chip/spreader system using the separation of variables method. Use the exact geometry and material parameters: square chip side length 1 cm, thickness 250 µm, isotropic thermal conductivity 163 W/mK; square spreader thickness 500 µm, thru-plane conductivity k_z=5 W/mK, variable in-plane conductivity k_xy; square hot spot side length 500 µm, heat flux 1.4 kW/cm²; convective boundary on back of spreader with heat-transfer coefficient 10,000 W/m²K and ambient temperature 25°C. Account for orthotropic conductivity via the equivalent isotropic transformation. Compute the peak excess temperature at the hot-spot center on the active chip side (z=0) for k_xy = 5, 350, and 1800 W/mK. Calculate the total thermal resistance (sum of one-dimensional and spreading resistances) as a function of spreader thickness for k_xy=350 W/mK, and determine the thickness that minimizes this resistance. Write all results to hot_spot_results.json.
- Output file: `/app/outputs/hot_spot_results.json`
- Format: json
- Contract: {"kxy5_excess_temp": "float (peak excess temperature at hot-spot center in °C when k_xy=5 W/mK)", "kxy350_excess_temp": "float (peak excess temperature at hot-spot center in °C when k_xy=350 W/mK)", "kxy1800_excess_temp": "float (peak excess temperature at hot-spot center in °C when k_xy=1800 W/mK)", "kxy350_opt_thickness": "float (spreader thickness in µm that minimizes total thermal resistance for k_xy=350 W/mK)", "kxy350_total_thermal_resistance": "float (minimum total thermal resistance in K/W at optimum thickness for k_xy=350 W/mK)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hot_spot_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hot_spot_results.json
- path: `/app/outputs/hot_spot_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Peak hot-spot excess temperatures for three in-plane conductivities, the optimum spreader thickness for k_xy=350 W/mK, and the corresponding minimum total thermal resistance.
- schema:
  - `type`: object
  - `required`:
    - `kxy5_excess_temp`: number (float)
    - `kxy350_excess_temp`: number (float)
    - `kxy1800_excess_temp`: number (float)
    - `kxy350_opt_thickness`: number (float)
    - `kxy350_total_thermal_resistance`: number (float)
  - `units`:
    - `kxy5_excess_temp`: °C
    - `kxy350_excess_temp`: °C
    - `kxy1800_excess_temp`: °C
    - `kxy350_opt_thickness`: µm
    - `kxy350_total_thermal_resistance`: K/W

Notes: All parameters are as specified in the action. The analytical solution requires truncation of infinite Fourier-Bessel series; convergence should be ensured. The optimum thickness can be found via sweep or minimizer. The computed values are compared against paper-reported values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hot_spot_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "kxy5_excess_temp": "number (float)",
          "kxy350_excess_temp": "number (float)",
          "kxy1800_excess_temp": "number (float)",
          "kxy350_opt_thickness": "number (float)",
          "kxy350_total_thermal_resistance": "number (float)"
        },
        "units": {
          "kxy5_excess_temp": "°C",
          "kxy350_excess_temp": "°C",
          "kxy1800_excess_temp": "°C",
          "kxy350_opt_thickness": "µm",
          "kxy350_total_thermal_resistance": "K/W"
        }
      },
      "description": "Peak hot-spot excess temperatures for three in-plane conductivities, the optimum spreader thickness for k_xy=350 W/mK, and the corresponding minimum total thermal resistance."
    }
  ],
  "notes": "All parameters are as specified in the action. The analytical solution requires truncation of infinite Fourier-Bessel series; convergence should be ensured. The optimum thickness can be found via sweep or minimizer. The computed values are compared against paper-reported values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your hot_spot_results.json, extracts the five reported numbers, and compares them against independently determined reference values (derived from the paper) using appropriate tolerances. It also checks that the excess temperature monotonically decreases with increasing in‑plane conductivity (kxy350_excess_temp < kxy5_excess_temp and kxy1800_excess_temp < kxy5_excess_temp). The final score is an average of per‑check rewards based on how closely your numbers match the references within tolerance, and whether the trend is satisfied. Honest computation of the analytical model is required; you are not scored on matches to the paper’s formatting or artefacts.
