# Optimal Reflector Angles for a Fixed-Tilt Solar Collector

## Problem background
In a flat-plate solar thermal collector, adding flat reflective surfaces above and below the collector can concentrate additional sunlight without active tracking. For a fixed collector orientation, the optimal tilt angles of these reflectors depend on the sun's seasonal position. The goal is to determine, for a south-facing collector tilted at 16° at a latitude of 16°14'N, the bottom and top reflector angles that maximize the total incident solar radiation at solar noon during the summer and winter solstices.

## Approach
The method uses standard solar geometry to compute the solar altitude at solar noon from the latitude, collector tilt, and solar declination (determined by day of year). The total incident radiation on the collector is modeled as the sum of direct radiation on the collector, diffuse sky radiation, ground-reflected radiation, and radiation reflected from the bottom and top reflectors. The reflector contributions depend on the reflector angles, the solar altitude, the collector tilt, and the reflectance of the aluminum reflectors (0.8) and the ground (0.2). The absolute magnitudes of the beam and diffuse irradiances are proportional constants; therefore the optimal angles can be found by maximizing only the geometric factors. Using numerical optimization (e.g., grid search or a derivative-free optimizer), one can determine the tilt angles of the bottom reflector (α₁) and top reflector (α₂) that maximize the total radiation. This is repeated for the summer solstice (21 June, declination 23.45°) and winter solstice (22 December, declination –23.45°).

## Reproduction target
Implement the solar geometry and radiation model to numerically optimize the bottom and top reflector tilt angles for the given location and collector tilt. Produce the optimal angles for the summer solstice (21 June) and winter solstice (22 December) and save them to /app/outputs/optimal_angles.csv with columns: date (YYYY-MM-DD), alpha1_deg (bottom reflector angle in degrees), alpha2_deg (top reflector angle in degrees). At minimum, the file must contain one row for each solstice.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute solar altitude at solar noon
- Role: process
- Action: For the site latitude φ=16°14'N (16.2333°) and collector tilt β=16°, compute the solar altitude angle α at solar noon (hour angle ω=0) for the summer solstice (21 June, δ=23.45°) and winter solstice (22 December, δ=-23.45°). Use standard solar geometry formulas: solar declination from day of year and the altitude equation (sin α = cos φ cos δ cos ω + sin φ sin δ).
- Evidence: `/app/outputs/none`

### Step 2: Optimise reflector angles and write CSV
- Role: scored (load-bearing)
- Action: For each solstice date, use numerical optimisation to find the bottom reflector tilt α₁ and top reflector tilt α₂ that maximise the total incident radiation as defined by the analytical radiation model. The model decomposes total radiation into direct, diffuse, ground-reflected, and two reflector components. The objective depends on solar altitude α, collector tilt β=16°, aluminium reflectance ρ_al=0.8, and ground reflectance ρ_g=0.2; absolute irradiance magnitudes act as constant multipliers and do not affect the optimum. Output the optimal angles in degrees to /app/outputs/optimal_angles.csv.
- Output file: `/app/outputs/optimal_angles.csv`
- Format: csv
- Contract: CSV with columns: date (YYYY-MM-DD format, you must use year 2023: 2023-06-21 for summer solstice, 2023-12-22 for winter solstice), alpha1_deg (float, bottom reflector optimal angle in degrees), alpha2_deg (float, top reflector optimal angle in degrees). At least two rows: one for summer solstice and one for winter solstice.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimal_angles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimal_angles.csv
- path: `/app/outputs/optimal_angles.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed optimal tilt angles for the bottom (α₁) and top (α₂) reflectors at the summer and winter solstices.
- schema:
  - `type`: table
  - `required_columns`: `date`, `alpha1_deg`, `alpha2_deg`
  - `units`:
    - `alpha1_deg`: degrees
    - `alpha2_deg`: degrees

Notes: The verifier compares the computed angles to the paper-reported values with a tolerance and checks the seasonal trend (alpha1 larger in summer, alpha2 smaller in summer).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimal_angles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "date",
          "alpha1_deg",
          "alpha2_deg"
        ],
        "units": {
          "alpha1_deg": "degrees",
          "alpha2_deg": "degrees"
        }
      },
      "description": "Computed optimal tilt angles for the bottom (α₁) and top (α₂) reflectors at the summer and winter solstices."
    }
  ],
  "notes": "The verifier compares the computed angles to the paper-reported values with a tolerance and checks the seasonal trend (alpha1 larger in summer, alpha2 smaller in summer)."
}
```

## How you are scored
A hidden verifier reads your optimal_angles.csv and checks whether the computed α₁ and α₂ for each solstice match expected values within a tolerance, and whether they satisfy a seasonal consistency check (the angles must change monotonically between solstices). The final reward is a weighted combination of per‑angle and trend checks. You must produce the CSV exactly as specified; simply reporting expected numbers without running the correct optimization will not satisfy all checks.
