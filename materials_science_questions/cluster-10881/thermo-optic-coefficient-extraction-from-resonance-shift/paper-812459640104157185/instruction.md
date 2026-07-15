# Threshold Current Density and Mode Spacing Computation for Deformed Microlasers

## Problem background
Quadrupolar-shaped GaAs-AlGaAs microdisk lasers emitting at ~10 µm exhibit a threshold current density that depends on resonator size and deformation. A simple model relating total losses to threshold current density has been proposed, where mirror losses vary with cavity geometry. This task requires computing the threshold current density for a set of geometries using that model, with the given material and fitting parameters, and comparing the predicted trends to experimental measurements.

## Approach
The threshold current density is expressed as J_th = (α_W + α_M) / (g Γ). The waveguide loss α_W, gain coefficient g, and confinement factor Γ are known material constants. The mirror loss α_M is modelled by a phenomenological formula: α_M = -ln(P1) / [2 (√(A π) (1 - P2))], where A is the cavity area and P1, P2 are fitting parameters. Two separate parameter sets are used for circular (ε=0) and ε=0.10 deformed resonators. The area A = π R² / (1+2ε). The task is to determine P1, P2 for each regime by fitting the model to experimental threshold current density data (provided below), and then use the fitted model to compute J_th for the same geometries. Separately, the bow-tie mode spacing is estimated from a ray-tracing path length.

## Reproduction target
Produce two artifacts. First, a CSV file containing the predicted threshold current densities for the resonator geometries listed in the experimental data table, computed using the mirror-loss model with parameters fitted by you from that data. Second, a text file with the computed bow-tie mode spacing (cm⁻¹) for one specific resonator (R=70 µm, ε=0.16) using the ray-tracing path-length estimate at contact angle Φ=50° with n_eff=3.15. A hidden verifier will compare your predicted J_th values against the hidden reference experimental data and your mode spacing to a hidden reference, awarding credit based on accuracy (with tolerances).

## Assets

- NumPy: numpy
- Experimental threshold current density data (used for fitting the mirror-loss model):

| R (µm) | ε   | J_th_measured (kA/cm²) |
|--------|-----|------------------------|
| 22     | 0.0  | 9.27                   |
| 22     | 0.10 | 13.00                  |
| 50     | 0.0  | 8.02                   |
| 50     | 0.10 | 9.66                   |
| 60     | 0.0  | 7.86                   |
| 60     | 0.10 | 9.22                   |
| 70     | 0.0  | 7.74                   |
| 70     | 0.10 | 8.91                   |

## Workflow steps

### Step 1: Fit mirror-loss model parameters (process)
- Role: process
- Action: Using the experimental J_th data provided in the Assets table, implement the mirror-loss model (J_th = (α_W + α_M) / (g Γ) with α_M = -ln(P1) / [2 (√(A π) (1 - P2))], area A = π R² / (1+2ε)). Fit the parameters P1, P2 separately for the ε=0 and ε=0.10 regimes by minimizing the squared error between the model and the measured J_th values. Use the material constants: α_W = 19 cm⁻¹, Γ = 0.27, g = 10 cm⁻¹/(kA/cm²). You may perform the fit using non-linear least squares (e.g., scipy.optimize.curve_fit) or an equivalent method. Keep the fitted parameters for the next step.
- Evidence: none (this step is not directly scored; its output is used in Step 2)

### Step 2: Compute threshold current densities (scored, load-bearing)
- Role: scored (load-bearing)
- Action: Using the P1, P2 values you obtained for ε=0 and ε=0.10, compute the model-predicted threshold current density J_th for each of the eight (R, ε) combinations in the experimental data table. Use the same mirror-loss formula and material constants. Save the results to CSV.
- Output file: `/app/outputs/threshold_current_densities.csv`
- Format: csv
- Contract: Columns: R (float, µm), epsilon (float), computed_Jth (float, kA/cm²). One row per (R, epsilon) combination (the same eight rows as the input table).
- Scoring: scored by hidden verifier, which compares your computed_Jth values against the hidden reference experimental data (mean absolute error, threshold_or_better).

### Step 3: Compute mode spacing (scored)
- Role: scored
- Action: For a resonator with R = 70 µm and ε = 0.16, calculate the bow-tie mode spacing Δν = 1 / (L n_eff) using n_eff = 3.15 and the contact angle Φ = 50°. The path length L = 4 r(Φ) + 4 r(Φ) cos(Φ), where r(Φ) = R / sqrt(1+2ε) * sqrt(1+2ε cos(2Φ)). Save the result as a single number (in cm⁻¹) to a text file.
- Output file: `/app/outputs/mode_spacing.txt`
- Format: txt
- Contract: A single numeric value representing the mode spacing in cm⁻¹. No additional text.
- Scoring: scored by hidden verifier, which compares your number to a hidden reference value (absolute tolerance).

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/threshold_current_densities.csv`
- `/app/outputs/mode_spacing.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### threshold_current_densities.csv
- path: `/app/outputs/threshold_current_densities.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed threshold current densities for various resonator geometries.
- schema:
  - `type`: table
  - `required_columns`: `R`, `epsilon`, `computed_Jth`
  - `units`:
    - `R`: µm
    - `epsilon`: dimensionless
    - `computed_Jth`: kA/cm²

### mode_spacing.txt
- path: `/app/outputs/mode_spacing.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Computed mode spacing for the bow-tie mode in the specified resonator.
- schema:
  - `type`: text
  - `description`: Single numeric value representing the mode spacing in cm⁻¹.

Notes: The checker will recompute the MAE between the submitted threshold densities and hidden experimental data (using a tolerance-based threshold policy), and compare the submitted mode spacing to a hidden reference value with an absolute tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "threshold_current_densities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "epsilon",
          "computed_Jth"
        ],
        "units": {
          "R": "µm",
          "epsilon": "dimensionless",
          "computed_Jth": "kA/cm²"
        }
      },
      "description": "Computed threshold current densities for various resonator geometries."
    },
    {
      "file": "mode_spacing.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single numeric value representing the mode spacing in cm⁻¹."
      },
      "description": "Computed mode spacing for the bow-tie mode in the specified resonator."
    }
  ],
  "notes": "The checker will recompute the MAE between the submitted threshold densities and hidden experimental data (using a tolerance-based threshold policy), and compare the submitted mode spacing to a hidden reference value with an absolute tolerance."
}
```

## How you are scored
A hidden verifier inspects your submitted artifacts independently. For the threshold densities, it reads the computed values from the CSV, calculates the mean absolute error against hidden experimental reference data, and awards full credit when the error is below a tolerance, with score decreasing as error grows. For the mode spacing, it compares your submitted number to a hidden reference value and awards credit based on absolute difference within a tolerance. The two stages are combined with weighting to produce the final reward. Simply reporting the reference paper's numbers is not enough; your computed artifacts are scored.
