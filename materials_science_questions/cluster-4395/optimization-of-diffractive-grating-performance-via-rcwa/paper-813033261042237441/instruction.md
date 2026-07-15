# Grating-coupled SPR phase-interrogation optimization via RCWA

## Problem background
Surface plasmon resonance (SPR) biosensors in grating-coupling configuration offer advantages in miniaturization and lab-on-a-chip integration, but they often exhibit lower sensitivity compared to prism-coupled systems. In conical mounting, the reflected intensity depends on both the incident polarization and the azimuthal orientation of the grating. By performing a polarization scan and tracking the phase of the resulting sinusoidal reflectance curve, small refractive index changes (e.g., caused by analyte binding) can be detected. This approach, known as phase-interrogation, can be tuned by adjusting the polar and azimuthal angles and the grating line depth. This task focuses on the computational simulation part of such an optimization: using an open-source RCWA or Chandezon method solver to compute the phase response of a gold grating in water and to explore how the polar and azimuthal incidence angles affect the phase shift for a small refractive index change.

## Approach
The gold grating is simulated under conical mounting with a given period (400 nm), duty cycle (50%), and line depth (40 nm) at a wavelength of 633 nm. The reflectance as a function of incident polarization angle α is well described by R = f0 − f1 cos(2α + α0), where α0 is the phase parameter that shifts with the refractive index of the dielectric medium (water). The method consists of two stages: (1) For each chosen polar angle, the azimuthal angle that minimizes the reflectance (resonant azimuth) is first located by a coarse azimuth scan. (2) At the resonant azimuth, polarization spectra are computed for two nearby refractive indices (n=1.330 and n=1.332, corresponding to pure water and a 200 mM NaCl solution). Each spectrum is fitted to the harmonic form to extract α0, and the phase shift Δα0 = |α0(n=1.332) − α0(n=1.330)| is recorded. The same procedure is repeated for different polar angles, and later for a fixed polar angle while varying the azimuthal offset around resonance. All electromagnetic calculations can be performed with an open‑source RCWA or Chandezon method implementation; the solver must handle conical mounting and polarization-dependent reflectance.

## Reproduction target
Produce the two CSV tables described in the workflow steps below:

1. **Phase shift vs polar angle** – three data points (37°, 50°, 60°) at each polar angle's resonant azimuth.
2. **Phase shift vs azimuth offset** – nine data points (offsets from −4° to +4° in 1° steps) at a fixed polar angle of 60°.

Each table must contain the columns specified in its step contract. The outputs will be evaluated by a hidden verifier for physically meaningful structural properties (e.g., monotonicity, relative magnitude, peak position) rather than exact numerical agreement with any reference.

## Assets

- Gold optical constants at 633 nm: https://refractiveindex.info/?shelf=main&book=Au&page=Johnson
- Open-source RCWA or Chandezon method solver: https://github.com/photonica/rcwa

## Workflow steps

### Step 1: Simulate phase shift vs polar angle
- Role: scored
- Action: Implement an RCWA or Chandezon method solver for a gold grating (period=400 nm, duty cycle=50%, depth=40 nm) in water at 633 nm. For each polar angle (37, 50, 60 degrees) first find the resonant azimuth (minimum reflectance) by scanning azimuth. At each polar angle and its resonant azimuth, compute the polarization-dependent reflectance for refractive indices n=1.330 and n=1.332. Fit each reflectance curve to R = f0 - f1 cos(2α + α0) and extract the phase parameter α0. Compute the phase shift Δα0 = |α0(n=1.332) - α0(n=1.330)|. Output the three data points as a CSV.
- Output file: `/app/outputs/step_01_phase_vs_polar.csv`
- Format: csv
- Contract: columns: polar_angle (float, degrees), phase_shift (float, degrees)
- Scoring: scored by hidden verifier

### Step 2: Simulate phase shift vs azimuth offset at fixed polar angle
- Role: scored (load-bearing)
- Action: Fix polar angle at 60° and determine the resonant azimuth for water. Scan azimuth offsets from -4° to +4° in 1° steps (azimuth = resonant_azimuth + offset). For each offset, simulate polarization spectra at n=1.330 and n=1.332, fit to extract α0, and compute Δα0. Output a CSV with azimuth_offset and phase_shift.
- Output file: `/app/outputs/step_02_phase_vs_azimuth.csv`
- Format: csv
- Contract: columns: azimuth_offset (float, degrees), phase_shift (float, degrees)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phase_vs_polar.csv`
- `/app/outputs/step_02_phase_vs_azimuth.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phase_vs_polar.csv
- path: `/app/outputs/step_01_phase_vs_polar.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phase shift Δα0 between n=1.330 and n=1.332 at three polar angles (37, 50, 60 degrees) at their respective resonant azimuths. Checker verifies monotonic increase and ratio limits.
- schema:
  - `type`: table
  - `required_columns`: `polar_angle`, `phase_shift`
  - `units`:
    - `polar_angle`: degrees
    - `phase_shift`: degrees

### step_02_phase_vs_azimuth.csv
- path: `/app/outputs/step_02_phase_vs_azimuth.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phase shift Δα0 at 60° polar angle for azimuth offsets from -4 to +4 degrees around resonance. Checker verifies that the maximum phase shift occurs at a non-zero offset and the enhancement ratio is above a threshold.
- schema:
  - `type`: table
  - `required_columns`: `azimuth_offset`, `phase_shift`
  - `units`:
    - `azimuth_offset`: degrees
    - `phase_shift`: degrees

Notes: Both artifacts are scored by structural audit: monotonicity, ratio, and peak location rules absorb solver-specific numerical spread while confirming the paper's main trends. No tolerance windows are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phase_vs_polar.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "polar_angle",
          "phase_shift"
        ],
        "units": {
          "polar_angle": "degrees",
          "phase_shift": "degrees"
        }
      },
      "description": "Phase shift Δα0 between n=1.330 and n=1.332 at three polar angles (37, 50, 60 degrees) at their respective resonant azimuths. Checker verifies monotonic increase and ratio limits."
    },
    {
      "file": "step_02_phase_vs_azimuth.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "azimuth_offset",
          "phase_shift"
        ],
        "units": {
          "azimuth_offset": "degrees",
          "phase_shift": "degrees"
        }
      },
      "description": "Phase shift Δα0 at 60° polar angle for azimuth offsets from -4 to +4 degrees around resonance. Checker verifies that the maximum phase shift occurs at a non-zero offset and the enhancement ratio is above a threshold."
    }
  ],
  "notes": "Both artifacts are scored by structural audit: monotonicity, ratio, and peak location rules absorb solver-specific numerical spread while confirming the paper's main trends. No tolerance windows are exposed."
}
```

## How you are scored
After submission, a hidden verifier reads your CSV files from `/app/outputs` and inspects them against undisclosed criteria derived from the original simulation study. The scoring is based on structural properties such as the order of values, the location of maxima, and the ratios between selected data points—no exact match to a hidden number is expected. Each step contributes a portion of the total reward (the first step is scored; the second is both scored and load‑bearing), and the final score is a weighted sum in the range [0, 1]. Producing the tables by faithfully implementing the workflow as described, with correct physical modeling of the grating and the polarization spectrum, will naturally satisfy the verifier's requirements.
