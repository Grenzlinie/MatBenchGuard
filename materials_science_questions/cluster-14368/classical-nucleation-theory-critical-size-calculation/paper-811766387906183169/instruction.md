# Cloud Droplet Activation with Analytical Surfactant Partitioning Model

## Problem background
Surfactants dissolved in cloud droplets tend to partition to the droplet surface, reducing the surface tension. For micron-sized droplets, this partitioning can strongly deplete the surfactant in the bulk interior, which in turn alters the droplet's activation behaviour (the point at which it spontaneously grows into a cloud droplet). Solving the surfactant partitioning equilibrium numerically is computationally expensive, making it impractical for large-scale cloud models. This work derives simplified analytical equations that capture the partitioning effect, aiming to dramatically reduce computation time while preserving accuracy.

## Approach
You will implement two models for cloud droplet activation: (1) an **iterative numerical model** that solves the full Gibbs adsorption isotherm using root-finding, and (2) an **analytical model** based on a derived cubic equation for surfactant bulk concentration under the Szyskowski surface tension parameterisation. Both models use Köhler theory, with a constant dry particle size of 40 nm, temperature 298.15 K, and the surface tension parameters reported for SDS‑NaCl solutions (RTΓ∞ = 13.90×10⁻³ N/m, β = (9.273×10⁻⁶ M²)/(c_NaCl + 9.733×10⁻³ M), salt surface tension slope 1.61×10⁻³ N/m M⁻¹). For a range of surfactant mass fractions from 0 to 1, you will locate the maximum of the Köhler curve (the critical supersaturation) and record the corresponding critical droplet diameter and the bulk surfactant concentration. The analytical model's predictions will be compared against the iterative reference to quantify the maximum absolute difference in critical supersaturation.

## Reproduction target
Produce a CSV file (`critical_properties.csv`) containing for at least 15 surfactant mass fractions (covering 0 to 1) the critical supersaturation (%), critical droplet diameter (m), and surfactant bulk concentration (M) as computed by the analytical model. Also produce a JSON file (`error_analysis.json`) with the key `max_abs_diff_supersat_percent` holding the maximum absolute deviation in critical supersaturation between the iterative reference and the analytical model, using the same mass fraction grid.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute critical properties with iterative numerical model
- Role: process
- Action: Implement the Köhler equation together with the full numerical solution of the Gibbs adsorption isotherm for SDS-NaCl particles. Use the ternary Szyskowski surface tension parameters (RTΓ∞ = 13.90e-3 N/m, β = (9.273e-6 M²)/(c_NaCl + 9.733e-3 M)), salt surface tension slope 1.61e-3 N/m/M, dry particle diameter 40 nm, temperature 298.15 K. For at least 15 surfactant mass fractions covering [0,1], compute critical supersaturation, critical droplet diameter, and surfactant bulk concentration by locating the maximum of the Köhler curve. Write the results as a CSV file.
- Evidence: `/app/outputs/iterative_reference.csv`

### Step 2: Compute critical properties with analytical partitioning model
- Role: scored
- Action: Implement the analytical surfactant partitioning equations (cubic for common-ion case, with k₁ and k₂ constants) together with Köhler theory and the same Szyskowski parameters as in the iterative model. For the same mass fraction points, compute critical supersaturation (%), critical droplet diameter (m), and surfactant bulk concentration (M). Write the results to a CSV file.
- Output file: `/app/outputs/critical_properties.csv`
- Format: csv
- Contract: CSV with columns: mass_fraction_surfactant, critical_supersaturation, critical_diameter, surfactant_bulk_concentration
- Scoring: scored by hidden verifier

### Step 3: Compare analytical and iterative predictions
- Role: scored (load-bearing)
- Action: Load the iterative reference and analytical model outputs, align by mass fraction, and compute the absolute difference in critical supersaturation (in %). Record the maximum absolute difference as a JSON object.
- Output file: `/app/outputs/error_analysis.json`
- Format: json
- Contract: JSON object with key 'max_abs_diff_supersat_percent' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_properties.csv`
- `/app/outputs/error_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_properties.csv
- path: `/app/outputs/critical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Analytical model predictions of critical droplet properties for 40 nm SDS-NaCl particles as a function of surfactant mass fraction. Checked against hidden gold extracted from the paper's figures.
- schema:
  - `type`: table
  - `required_columns`: `mass_fraction_surfactant`, `critical_supersaturation`, `critical_diameter`, `surfactant_bulk_concentration`
  - `units`:
    - `mass_fraction_surfactant`: dimensionless (0-1)
    - `critical_supersaturation`: percent (%)
    - `critical_diameter`: meters (m)
    - `surfactant_bulk_concentration`: molarity (M)

### error_analysis.json
- path: `/app/outputs/error_analysis.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum absolute difference in critical supersaturation between analytical and iterative models, verifying the paper's claim of negligible numerical error.
- schema:
  - `type`: object
  - `required`:
    - `max_abs_diff_supersat_percent`: float
  - `units`: object

Notes: The iterative reference CSV is an internal intermediate, not scored. The analytical model output is the primary reproduction target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mass_fraction_surfactant",
          "critical_supersaturation",
          "critical_diameter",
          "surfactant_bulk_concentration"
        ],
        "units": {
          "mass_fraction_surfactant": "dimensionless (0-1)",
          "critical_supersaturation": "percent (%)",
          "critical_diameter": "meters (m)",
          "surfactant_bulk_concentration": "molarity (M)"
        }
      },
      "description": "Analytical model predictions of critical droplet properties for 40 nm SDS-NaCl particles as a function of surfactant mass fraction. Checked against hidden gold extracted from the paper's figures."
    },
    {
      "file": "error_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "max_abs_diff_supersat_percent": "float"
        },
        "units": {}
      },
      "description": "Maximum absolute difference in critical supersaturation between analytical and iterative models, verifying the paper's claim of negligible numerical error."
    }
  ],
  "notes": "The iterative reference CSV is an internal intermediate, not scored. The analytical model output is the primary reproduction target."
}
```

## How you are scored
A hidden verifier will independently inspect your submitted artifacts. For `critical_properties.csv`, it will compare your reported critical supersaturation values against a hidden reference derived from the original study. For `error_analysis.json`, it will check that the maximum absolute difference in critical supersaturation is below a predetermined threshold. The verifier weights these scores to compute a final reward. Reporting numbers that happen to match the paper's text is not sufficient; the verifier's checks are designed to confirm that the correct physical models were implemented and executed.
