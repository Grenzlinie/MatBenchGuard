# Computation of Ductile-to-Brittle Transition Strain Rate for Polycrystalline Ice

## Problem background
Polycrystalline ice exhibits a ductile-to-brittle transition under compression: at low strain rates it deforms plastically (ductile), while at higher rates it fails by brittle fracture. This transition is critical for engineering applications, limiting the forces exerted by moving ice against offshore structures. A micromechanical model proposes that the transition occurs when stress relaxation by crack-tip creep can no longer keep pace with crack propagation. This competition yields an analytic expression for the transition strain rate that depends on grain size, confinement, material creep properties, fracture toughness, and friction. The goal is to implement that expression and compute the transition strain rate over a range of grain sizes, confinement ratios, and material conditions.

## Approach
The model is based on the idea that cracks propagate when the crack-tip creep zone radius is smaller than a critical fraction of the crack length. The transition strain rate is given by an analytic expression involving the material's creep constant (B), fracture toughness (K_Ic), friction coefficient (μ), grain size (d), confinement ratio (R), and a geometric factor (f). You will implement this formula and evaluate it for three sets of parameters: (a) fresh-water ice at -10°C, (b) salt-water ice at -10°C, and (c) fresh-water ice at -40°C. The creep constant for -40°C must be obtained from the reference "Qi and Schulson (1998)". Then compute the transition strain rate (in s⁻¹) for a grid of grain sizes and confinement ratios covering the ranges specified in the workflow step, and write the results to a CSV file.

## Reproduction target
Compute the ductile-to-brittle transition strain rate for the specified material/temperature combinations at multiple grain sizes and confinement ratios. Write a single CSV file containing every combination of condition, grain size d (mm), confinement ratio R, material type ('fresh' or 'saline'), temperature (°C), and the computed transition strain rate. The hidden verifier will independently recompute the transition strain rate using the same analytic expression and parameter sources, compare your values, and verify that the set of computed rates exhibits the physically required trends with grain size, confinement, salinity, and temperature. You must compute and report the values; do not rely on pre-computed numbers.

## Assets

- Qi and Schulson (1998) paper

## Workflow steps

### Step 1: Compute ductile-to-brittle transition strain rates
- Role: scored (load-bearing)
- Action: Implement the formula ε̇_t = B K_Ic^3 / [ f d^{1.5} ( sqrt(1+μ^2) - μ - R (μ + sqrt(1+μ^2)) ) ]. Compute ε̇_t (in s^{-1}) for a grid of conditions covering varying grain sizes d (mm), confinement ratios R, and material/temperature combinations: (a) fresh-water ice at -10°C: B=4.3e-7 MPa^{-3}s^{-1}, K_Ic=0.1 MPa√m, μ=0.5, f=0.015; (b) salt-water ice at -10°C: B=5.1e-6 MPa^{-3}s^{-1}, K_Ic=0.1 MPa√m, μ=0.5, f=0.015; (c) fresh-water ice at -40°C: use B from Qi & Schulson (1998), μ=0.8, K_Ic=0.1 MPa√m, f=0.015. Write the results to a CSV file.
- Output file: `/app/outputs/transition_strain_rates.csv`
- Format: csv
- Contract: condition_id (string), d_mm (float), R (float), material (string, 'fresh' or 'saline'), temperature_C (float), epsilon_t_1_per_s (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_strain_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_strain_rates.csv
- path: `/app/outputs/transition_strain_rates.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file containing the ductile-to-brittle transition strain rate computed for all required combinations of grain size, confinement, material, and temperature.
- schema:
  - `columns`: `condition_id`, `d_mm`, `R`, `material`, `temperature_C`, `epsilon_t_1_per_s`
  - `types`:
    - `condition_id`: string
    - `d_mm`: float
    - `R`: float
    - `material`: string (fresh or saline)
    - `temperature_C`: float
    - `epsilon_t_1_per_s`: float

Notes: The verifier recomputes the formula with the same parameters, compares each row within relative tolerance, and checks monotonic trends across rows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_strain_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          "condition_id",
          "d_mm",
          "R",
          "material",
          "temperature_C",
          "epsilon_t_1_per_s"
        ],
        "types": {
          "condition_id": "string",
          "d_mm": "float",
          "R": "float",
          "material": "string (fresh or saline)",
          "temperature_C": "float",
          "epsilon_t_1_per_s": "float"
        }
      },
      "description": "CSV file containing the ductile-to-brittle transition strain rate computed for all required combinations of grain size, confinement, material, and temperature."
    }
  ],
  "notes": "The verifier recomputes the formula with the same parameters, compares each row within relative tolerance, and checks monotonic trends across rows."
}
```

## How you are scored
A hidden verifier will score your submitted CSV file. The verifier recomputes the transition strain rate using the same formula and reference parameter values for every condition you are required to evaluate. It compares your reported epsilon_t values to its own recomputed values within a relative tolerance (to account for floating-point precision). Additionally, the verifier checks that the computed values satisfy the physically required trends among the different conditions (trends that are expected from the underlying physics). The specific trends being verified are not disclosed; you must produce numerically correct results that naturally satisfy these physical relationships. The final reward combines numerical accuracy and trend checks; simply inserting the correct trend direction without computing the actual values will not pass.
