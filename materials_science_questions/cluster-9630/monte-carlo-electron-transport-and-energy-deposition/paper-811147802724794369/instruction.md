# Monte Carlo electron transport and interior wall dose distribution

## Problem background
Low-energy electron beams can be used to sterilize the interior surfaces of containers by injecting electrons through the open mouth. Understanding the absorbed-dose distribution on the inner walls is critical for process validation and for avoiding excessive dose ratios that could damage container materials. Monte Carlo simulations can predict these dose distributions, aiding process optimization without extensive dosimetry.

## Approach
This task uses a Monte Carlo electron-transport simulation to compute the relative absorbed-dose profile along the inner walls of two container geometries (a 2 L blow-molded bottle and a 300 mL glass bottle) at an electron energy of 240 keV. The containers are approximated by simplified geometric models (cylinder-cone-cylinder). A spatial electron source with a Gaussian-like profile is placed at the container mouth. The simulation tracks at least 10⁶ electron histories and records energy deposited in a thin (10 μm) annular scoring layer divided into vertical and horizontal zones. The dose in each zone is normalized by the dose in the topmost zone (zone 1) to produce a relative dose profile that can be compared against reference data.

## Reproduction target
Simulate electron transport in the two containers using an open-source Monte Carlo code, compute the absorbed dose in predefined interior wall zones, normalize each zone's dose by the dose at zone 1, and output the resulting normalized dose profiles as CSV files. For the 2 L bottle, include only odd-numbered zones (1,3,5,…,25). For the 300 mL bottle, include all 15 zones (1 through 15).

## Assets

- Monte Carlo electron transport code: https://geant4.web.cern.ch/

## Workflow steps

### Step 1: Construct container geometry and discretize dosimetry zones
- Role: process
- Action: Build simplified geometric models for the two containers as described: (a) 2 L bottle: cylinder-cone-cylinder approximation with 35 mm diameter × 25 mm neck, conical section expanding to 110 mm, then a straight cylinder 160 mm long, flat bottom at 270 mm from mouth; (b) 300 mL bottle: 30 mm diameter × 15 mm cylindrical mouth, 60 mm diameter × 150 mm tall cylinder. Define a 10 μm thick inner-wall annulus and discretize it into zones: for the 2 L bottle, 27 vertical zones of 1 cm height (only odd-numbered zones 1,3,5,…,25 will be reported) and 36 horizontal subzones of 2 cm width (exploiting symmetry); for the 300 mL bottle, 15 vertical zones of 1 cm height.
- Evidence: none

### Step 2: Prepare electron source profile
- Role: process
- Action: Define the spatial electron source at 240 keV energy: a Gaussian-like profile with FWHM = 25 mm at the window (0 mm plane) and FWHM = 35 mm at 12 mm from the window. The source is located at the window foil plane. Position the container mouth 18 mm downstream from the foil (so the source enters the open mouth after passing through the foil and the 18 mm air gap).
- Evidence: none

### Step 3: Run Monte Carlo simulation
- Role: process
- Action: Execute a Monte Carlo electron transport simulation for both container geometries at 240 keV, using at least 10^6 source electrons. Record the energy deposited in each dosimetry zone (inner 10 μm wall annulus) during the simulation.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 4: Extract normalized dose for the 2 L bottle
- Role: scored (load-bearing)
- Action: From the simulation output, compute the average absorbed dose in each zone of the 2 L bottle. Normalize by the dose at zone 1 (topmost zone). Output only the odd-numbered vertical zones 1,3,5,…,25.
- Output file: `/app/outputs/dose_profile_2L.csv`
- Format: csv
- Contract: zone_number (int, 1-indexed odd numbers only), dose_norm (float, dose normalized to zone 1 dose)
- Scoring: scored by hidden verifier

### Step 5: Extract normalized dose for the 300 mL bottle
- Role: scored (load-bearing)
- Action: From the simulation output, compute the average absorbed dose in each zone of the 300 mL bottle. Normalize by the dose at zone 1. Output all 15 vertical zones (1 through 15).
- Output file: `/app/outputs/dose_profile_300ml.csv`
- Format: csv
- Contract: zone_number (int, 1-indexed, 1 to 15), dose_norm (float, dose normalized to zone 1 dose)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dose_profile_2L.csv`
- `/app/outputs/dose_profile_300ml.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dose_profile_2L.csv
- path: `/app/outputs/dose_profile_2L.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized absorbed dose along the interior wall for the 2 L container (odd zones 1,3,5,…,25). The checker compares this profile to a hidden reference profile derived from the paper's simulation values.
- schema:
  - `type`: table
  - `required_columns`: `zone_number`, `dose_norm`
  - `columns`:
    - `zone_number`: integer
    - `dose_norm`: float

### dose_profile_300ml.csv
- path: `/app/outputs/dose_profile_300ml.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized absorbed dose along the interior wall for the 300 mL container (zones 1–15). The checker compares this profile to a hidden reference profile derived from the paper's simulation values.
- schema:
  - `type`: table
  - `required_columns`: `zone_number`, `dose_norm`
  - `columns`:
    - `zone_number`: integer
    - `dose_norm`: float

Notes: The submitted normalized dose profiles will be scored by comparing them to hidden reference profiles using a quantitative error metric; full credit is awarded if the error is within an acceptable tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dose_profile_2L.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "zone_number",
          "dose_norm"
        ],
        "columns": {
          "zone_number": "integer",
          "dose_norm": "float"
        }
      },
      "description": "Normalized absorbed dose along the interior wall for the 2 L container (odd zones 1,3,5,…,25). The checker compares this profile to a hidden reference profile derived from the paper's simulation values."
    },
    {
      "file": "dose_profile_300ml.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "zone_number",
          "dose_norm"
        ],
        "columns": {
          "zone_number": "integer",
          "dose_norm": "float"
        }
      },
      "description": "Normalized absorbed dose along the interior wall for the 300 mL container (zones 1–15). The checker compares this profile to a hidden reference profile derived from the paper's simulation values."
    }
  ],
  "notes": "The submitted normalized dose profiles will be scored by comparing them to hidden reference profiles using a quantitative error metric; full credit is awarded if the error is within an acceptable tolerance."
}
```

## How you are scored
A hidden verifier reads your submitted CSV files and compares the normalized dose values for each zone against a hidden reference profile derived from the paper's reported simulation results. The verifier computes a quantitative error metric (root-mean-square error) between your profile and the reference. The final reward is a weighted combination of the scores for each container's profile; a low error yields a high score. Simply reporting the exact numbers from the paper is not sufficient—your simulation must produce consistent dose distributions that match the reference within the expected tolerance.
