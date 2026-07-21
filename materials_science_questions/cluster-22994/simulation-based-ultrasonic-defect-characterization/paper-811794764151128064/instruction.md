# Generating DGS curves for ultrasonic phased array probes

## Problem background
Ultrasonic phased array testing is a non-destructive inspection technique where the active probe aperture can be varied electronically. Defect sizing often relies on Distance-Gain-Size (DGS) curves that give the echo amplitude from a flat circular reflector as a function of distance and reflector diameter. Such curves are readily available for standard circular probes but are not tabulated for phased array probes, whose active area is rectangular and depends on the number of active elements. Therefore, the objective is to implement a computational model that, given phased array probe parameters, generates the corresponding DGS curves. This task focuses on the zero‑degree beam case, where all elements are excited simultaneously to produce a normal beam.

## Approach
The model discretizes the active probe surface into rectangular elements (corresponding to the individual phased array elements or sub‑elements) and the circular reflector into radial and angular elements. For each probe‑reflector element pair, the distance ρ is computed. The ultrasonic field amplitude incident from a probe element on a reflector element is modeled as a spherical wave that decays with 1/ρ and incorporates a heuristic angular weighting factor (the cosine of the incident angle raised to a power). The total incident field on a reflector element is obtained by summing the contributions from all probe elements. Using the reciprocity principle, the back‑reflected signal from a reflector element is taken as the square of the incident field, and the overall received signal magnitude is the modulus of the sum of these squares over all reflector elements. The computed signal is normalized by its maximum value over the entire scan and expressed in decibels. The implementation must evaluate this model over a grid of distances and disk diameters for each probe configuration.

## Reproduction target
Produce DGS curves for three probe configurations by running the model over the following grid: distances from 5 mm to 600 mm in steps of 5 mm, and disk diameters from 0.5 mm to 20 mm in steps of 0.5 mm. For each (distance, diameter) pair, compute the normalized signal amplitude in dB and save the results as CSV files with columns `distance_mm`, `diameter_mm`, `signal_dB`.

The three configurations are:
1. Equivalent square probe: active area 18 mm × 18 mm, frequency 2 MHz, longitudinal wave speed c = 5920 m/s.
2. 32‑element phased array probe: element pitch 1.4 mm, active width 44.8 mm; frequency 2.25 MHz, c = 5920 m/s. Choose a reasonable element length (e.g. 10 mm).
3. 16‑element phased array probe: element pitch 1.4 mm, active width 22.4 mm; element length 10 mm; frequency 2.25 MHz, c = 5920 m/s.

The output files must be saved as `/app/outputs/dgs_curves_standard_equivalent.csv`, `/app/outputs/dgs_curves_32element.csv`, and `/app/outputs/dgs_curves_16element.csv` respectively.

## Assets

- NumPy: numpy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Generate DGS curves for equivalent square probe
- Role: scored (load-bearing)
- Action: Implement the ultrasonic echo model according to the described equations (discrete element field superposition with angular weighting and reciprocity). Compute the normalized echo amplitude signal_dB for an equivalent square probe with active area 18 mm × 18 mm, frequency 2 MHz, wave speed c = 5920 m/s. Vary reflector distance from 5 mm to 600 mm (step 5 mm) and disk diameter from 0.5 mm to 20 mm (step 0.5 mm). For each (distance, diameter) pair compute the signal magnitude S, normalize by the maximum over all computed points for this probe, convert to dB, and write to dgs_curves_standard_equivalent.csv.
- Output file: `/app/outputs/dgs_curves_standard_equivalent.csv`
- Format: csv
- Contract: distance_mm (float), diameter_mm (float), signal_dB (float)
- Scoring: scored by hidden verifier

### Step 2: Generate DGS curves for 32-element phased array probe
- Role: scored (load-bearing)
- Action: Using the same model, with parameters: number of elements = 32, element pitch = 1.4 mm, active width = 44.8 mm; choose a typical element length (e.g., 10 mm). Frequency = 2.25 MHz, c = 5920 m/s. Compute signal_dB over the same distance and diameter ranges as step 1. Write to dgs_curves_32element.csv.
- Output file: `/app/outputs/dgs_curves_32element.csv`
- Format: csv
- Contract: distance_mm (float), diameter_mm (float), signal_dB (float)
- Scoring: scored by hidden verifier

### Step 3: Generate DGS curves for 16-element phased array probe
- Role: scored (load-bearing)
- Action: Same model with parameters: number of elements = 16, element pitch = 1.4 mm, active width = 22.4 mm; element length = 10 mm. Frequency = 2.25 MHz, c = 5920 m/s. Compute over the same ranges and write to dgs_curves_16element.csv.
- Output file: `/app/outputs/dgs_curves_16element.csv`
- Format: csv
- Contract: distance_mm (float), diameter_mm (float), signal_dB (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dgs_curves_standard_equivalent.csv`
- `/app/outputs/dgs_curves_32element.csv`
- `/app/outputs/dgs_curves_16element.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dgs_curves_standard_equivalent.csv
- path: `/app/outputs/dgs_curves_standard_equivalent.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed DGS curve data for the equivalent square probe; each row is a (distance, diameter) point with normalized echo amplitude in dB.
- schema:
  - `type`: table
  - `required_columns`: `distance_mm`, `diameter_mm`, `signal_dB`
  - `units`:
    - `distance_mm`: mm
    - `diameter_mm`: mm
    - `signal_dB`: dB
  - `items`: None
  - `required`: None

### dgs_curves_32element.csv
- path: `/app/outputs/dgs_curves_32element.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed DGS curve data for the 32-element phased array probe; each row is a (distance, diameter) point with normalized echo amplitude in dB.
- schema:
  - `type`: table
  - `required_columns`: `distance_mm`, `diameter_mm`, `signal_dB`
  - `units`:
    - `distance_mm`: mm
    - `diameter_mm`: mm
    - `signal_dB`: dB
  - `items`: None
  - `required`: None

### dgs_curves_16element.csv
- path: `/app/outputs/dgs_curves_16element.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed DGS curve data for the 16-element phased array probe; each row is a (distance, diameter) point with normalized echo amplitude in dB.
- schema:
  - `type`: table
  - `required_columns`: `distance_mm`, `diameter_mm`, `signal_dB`
  - `units`:
    - `distance_mm`: mm
    - `diameter_mm`: mm
    - `signal_dB`: dB
  - `items`: None
  - `required`: None

Notes: Each CSV must cover the full grid of distances (5–600 mm, step 5 mm) and diameters (0.5–20 mm, step 0.5 mm) for the respective probe configuration. The scaling signal_dB is normalized to the maximum per probe and expressed in dB. The agent may adjust the elemental discretization and the element length for the phased array probes as long as the curves match the expected shape within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dgs_curves_standard_equivalent.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_mm",
          "diameter_mm",
          "signal_dB"
        ],
        "units": {
          "distance_mm": "mm",
          "diameter_mm": "mm",
          "signal_dB": "dB"
        },
        "items": null,
        "required": null
      },
      "description": "Computed DGS curve data for the equivalent square probe; each row is a (distance, diameter) point with normalized echo amplitude in dB."
    },
    {
      "file": "dgs_curves_32element.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_mm",
          "diameter_mm",
          "signal_dB"
        ],
        "units": {
          "distance_mm": "mm",
          "diameter_mm": "mm",
          "signal_dB": "dB"
        },
        "items": null,
        "required": null
      },
      "description": "Computed DGS curve data for the 32-element phased array probe; each row is a (distance, diameter) point with normalized echo amplitude in dB."
    },
    {
      "file": "dgs_curves_16element.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_mm",
          "diameter_mm",
          "signal_dB"
        ],
        "units": {
          "distance_mm": "mm",
          "diameter_mm": "mm",
          "signal_dB": "dB"
        },
        "items": null,
        "required": null
      },
      "description": "Computed DGS curve data for the 16-element phased array probe; each row is a (distance, diameter) point with normalized echo amplitude in dB."
    }
  ],
  "notes": "Each CSV must cover the full grid of distances (5–600 mm, step 5 mm) and diameters (0.5–20 mm, step 0.5 mm) for the respective probe configuration. The scaling signal_dB is normalized to the maximum per probe and expressed in dB. The agent may adjust the elemental discretization and the element length for the phased array probes as long as the curves match the expected shape within tolerance."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently samples a set of (distance, diameter) points from the covered grid and compares your reported `signal_dB` values against hidden reference values that represent the expected DGS behavior for each probe. The comparison uses a tolerance that absorbs legitimate implementation differences (e.g., discretization fineness, element length choice). Scoring follows a threshold‑or‑better policy: meeting or exceeding the reference quality (within tolerance) yields full credit for that point; credit degrades only as the result underperforms the reference. The final reward is a weighted combination of the scores across all three output files. Outputs that are not parseable or that omit required columns will receive zero credit for that step.
