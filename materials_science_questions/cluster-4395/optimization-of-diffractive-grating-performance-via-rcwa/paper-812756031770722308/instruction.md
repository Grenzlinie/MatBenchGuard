# Reflection Phase Independence of Thick Metal Gratings via RCWA

## Problem background
Thick infinite gratings of parallel conducting cylinders can exhibit a remarkable electromagnetic property when the incident electric field is parallel to the conductors (E‑polarised plane‑wave illumination): for a special choice of the conductor cross‑section and grating periodicity, the phase of the reflection coefficient can become nearly independent of both frequency and incidence angle. Understanding and reproducing this behaviour requires rigorous numerical simulation of the reflection coefficient phase as a function of normalised period and angle. This task focuses on determining, through computation, the optimal grating geometry that yields such phase independence and on verifying the property by computing phase sweeps over a wide range of parameters.

## Approach
The electromagnetic scattering from a periodic array of perfectly conducting circular cylinders is solved using a rigorous coupled‑wave analysis (RCWA) or an equivalent open‑source grating‑diffraction solver. The reflection coefficient phase is extracted as a function of the normalised period p/λ (ratio of grating period to free‑space wavelength) and the incidence angle. By first sweeping the cylinder‑width‑to‑period ratio w/p at a low p/λ and normal incidence, one can identify the geometry that makes the reflection phase nearly stationary with respect to frequency (the phase‑stability condition). With that optimal w/p fixed, the reflection phase is then computed over a range of p/λ at normal incidence and over a range of incidence angles at a chosen p/λ. The resulting sweeps reveal whether the phase remains approximately constant for the optimal grating, confirming the frequency‑ and angle‑independence phenomenon.

## Reproduction target
Produce two CSV files containing the computed reflection coefficient phase (in degrees) for a grating of perfectly conducting circular cylinders under E‑polarised illumination, after numerically determining the optimal width‑to‑period ratio.  
- `frequency_sweep.csv`: reflection phase at normal incidence for p/λ = 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40.  
- `angular_sweep.csv`: reflection phase at fixed p/λ = 0.2 for incidence angles 0°, 10°, 20°, 30°, 40°, 50°, 60°, 70°, 80°.  
The optimal grating should exhibit very small phase variation across both sweeps, confirming the frequency‑ and angle‑independence property.

## Assets

- RCWA solver (e.g., S4, RETICOLO, or custom open-source implementation): https://github.com/vdrobinin/s4
- Python with numpy, scipy: numpy scipy

## Workflow steps

### Step 1: Determine optimal circular-cylinder geometry
- Role: process
- Action: Use an RCWA solver to sweep w/p from 0.2 to 0.4 at a low p/λ (e.g., 0.1) and normal incidence. Identify the w/p that yields a reflection phase closest to 180°. Use this optimal w/p in subsequent steps.
- Evidence: `/app/outputs/optimal_wp.txt`

### Step 2: Frequency sweep of reflection phase for optimal grating
- Role: scored (load-bearing)
- Action: For the optimal circular-cylinder grating found in step 1, compute the reflection coefficient phase at normal incidence for p/λ values 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40. Save the results to /app/outputs/frequency_sweep.csv.
- Output file: `/app/outputs/frequency_sweep.csv`
- Format: csv
- Contract: columns: p_lambda (float), reflection_phase_deg (float). One row per p/λ value.
- Scoring: scored by hidden verifier

### Step 3: Angular sweep of reflection phase for optimal grating
- Role: scored
- Action: For the same optimal grating, compute the reflection coefficient phase at fixed p/λ = 0.2 for incidence angles 0°, 10°, 20°, 30°, 40°, 50°, 60°, 70°, 80°. Save the results to /app/outputs/angular_sweep.csv.
- Output file: `/app/outputs/angular_sweep.csv`
- Format: csv
- Contract: columns: incidence_angle_deg (float), reflection_phase_deg (float). One row per angle.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequency_sweep.csv`
- `/app/outputs/angular_sweep.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequency_sweep.csv
- path: `/app/outputs/frequency_sweep.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed reflection coefficient phase for the optimal grating at normal incidence over a range of normalized periods p/λ.
- schema:
  - `type`: table
  - `required_columns`: `p_lambda`, `reflection_phase_deg`
  - `units`:
    - `p_lambda`: dimensionless
    - `reflection_phase_deg`: degrees

### angular_sweep.csv
- path: `/app/outputs/angular_sweep.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed reflection coefficient phase for the optimal grating at fixed p/λ=0.2 for various incidence angles.
- schema:
  - `type`: table
  - `required_columns`: `incidence_angle_deg`, `reflection_phase_deg`
  - `units`:
    - `incidence_angle_deg`: degrees
    - `reflection_phase_deg`: degrees

Notes: The checker will recompute the reflection phase for the optimal geometry using an independent RCWA solver and compare the submitted values. It will also verify that the phase variation across the frequency sweep (p/λ ≤ 0.2) is less than 5° and across the angular sweep is less than 5°, confirming the independence property. Tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequency_sweep.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_lambda",
          "reflection_phase_deg"
        ],
        "units": {
          "p_lambda": "dimensionless",
          "reflection_phase_deg": "degrees"
        }
      },
      "description": "Computed reflection coefficient phase for the optimal grating at normal incidence over a range of normalized periods p/λ."
    },
    {
      "file": "angular_sweep.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "incidence_angle_deg",
          "reflection_phase_deg"
        ],
        "units": {
          "incidence_angle_deg": "degrees",
          "reflection_phase_deg": "degrees"
        }
      },
      "description": "Computed reflection coefficient phase for the optimal grating at fixed p/λ=0.2 for various incidence angles."
    }
  ],
  "notes": "The checker will recompute the reflection phase for the optimal geometry using an independent RCWA solver and compare the submitted values. It will also verify that the phase variation across the frequency sweep (p/λ ≤ 0.2) is less than 5° and across the angular sweep is less than 5°, confirming the independence property. Tolerances are hidden."
}
```

## How you are scored
A hidden verifier independently recomputes the reflection phase for the same optimal circular‑cylinder grating at the specified p/λ and incidence‑angle points using a reference RCWA solver. For each of `frequency_sweep.csv` and `angular_sweep.csv`, your submitted phase values are compared against these reference values, and the phase variation across each sweep is assessed. The final reward (a float between 0 and 1) is a weighted combination of the scores from the two artifacts. Simply quoting a literature value or fabricating numbers will be detected by the hidden recomputation; the task must be solved by actually performing the electromagnetic simulations described in the workflow.
