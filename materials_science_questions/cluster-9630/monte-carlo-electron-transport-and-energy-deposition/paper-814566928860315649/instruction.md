# Optimization of position-sensitive silicon detector strip pitches via Monte Carlo simulation

## Problem background
Low-energy electrons and protons (0.1–1.0 MeV) in the space radiation environment affect spacecraft charging, yet detectors to monitor them in this energy range are rare. One conceptual design uses a permanent magnet to deflect incident particles and two one-dimensional position-sensitive silicon micro-strip detectors (PSSMSDs) to measure their energy: protons are collected on a detector D1 placed near the entrance aperture, while electrons are deflected 180° and collected on a second detector D2. The hit position on each detector is related to the incident particle energy. The strip pitch of the detectors – the width of the readout strips – determines how finely the hit position can be resolved and therefore affects the precision of the energy measurement. This task aims to find the strip pitch that gives the best energy measurement performance for both the electron and proton channels.

## Approach
The detector is modelled as a simple geometry in Geant4: an entrance aperture of 2.0 mm gap, a uniform magnetic field of 0.1 T directed along negative X, D1 placed along the Z axis at a 5 mm offset, and D2 placed along the Y axis. Both detectors are silicon with an active thickness of 0.5 mm and lengths of 15 cm (for simplified simulation). A low-energy electromagnetic physics list is used, and primary particles are generated uniformly in kinetic energy between 0.1 and 1.0 MeV.

Two separate Monte‑Carlo runs are performed – one with 100,000 electrons and one with 100,000 protons. For each event the incident kinetic energy, the hit position (distance from the centre line on the corresponding detector) and the total energy deposited in the detector are recorded. The hit positions are then binned into strips of various widths: for D2 (electrons) the pitches tested are 0.5, 1.0, 1.5, 2.0, 2.5, 3.0 mm; for D1 (protons) the pitches are 5, 10, 15, 20 mm. For each pitch, a measured energy is derived from the hit position using a linear calibration (the relationship between hit position and true energy is linear). The root-mean-square (RMS) error between measured and true incident energy is computed, together with the energy resolution (RMS divided by mean deposited energy, expressed as a percentage). The optimal pitch for each detector is the one that minimises the RMS energy error.

## Reproduction target
Produce two CSV files and one text file that together capture the outcome of the simulation study:

- `electron_analysis.csv`: for each D2 strip pitch (0.5–3.0 mm) give the RMS energy error (MeV) and energy resolution (%).
- `proton_analysis.csv`: for each D1 strip pitch (5–20 mm) give the RMS energy error (MeV) and energy resolution (%).
- `optimal_pitches.txt`: two lines reporting the strip pitch (in mm) that minimises the RMS error for D2 (electrons) and D1 (protons), formatted as:
  `D2_optimal_pitch_mm=<float>`
  `D1_optimal_pitch_mm=<float>`

All files must be placed in `/app/outputs` exactly as specified in the workflow steps and the output contract.

## Assets

- Geant4 Monte Carlo toolkit: https://geant4.web.cern.ch/
- Python 3: python3
- NumPy: numpy

## Workflow steps

### Step 1: Detector Geant4 model setup
- Role: process
- Action: Set up the Geant4 model of the detector: aperture gap 2.0 mm, uniform magnetic field 0.1 T along negative X, D1 placed along Z at 5 mm offset, D2 placed along Y; silicon detector active thickness 0.5 mm, lengths as described (D1 15 cm, D2 15 cm). Configure a suitable low-energy electromagnetic physics list and a primary particle generator for electrons and protons.
- Evidence: none

### Step 2: Electron Monte Carlo simulation
- Role: process
- Action: Run Geant4 simulation of 100,000 electrons with kinetic energies uniformly distributed between 0.1 and 1.0 MeV entering through the aperture. For each event, record incident kinetic energy, hit position on D2 (distance from center line), and total energy deposited in D2. Save the raw data.
- Evidence: `/app/outputs/electron_raw_hits.csv`

### Step 3: Electron energy resolution analysis
- Role: scored
- Action: Load the electron simulation data. For each strip pitch value in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0] mm, bin hit positions into strips of that width, derive a measured energy from the position using a linear calibration (fit or known linear relationship), and compute the root mean square (RMS) error between measured and true incident energy, and the energy resolution (RMS divided by mean deposited energy, as percentage). Output the results.
- Output file: `/app/outputs/electron_analysis.csv`
- Format: csv
- Contract: CSV with header: strip_pitch_mm, rms_energy_MeV, energy_resolution_pct. One row per pitch value.
- Scoring: scored by hidden verifier

### Step 4: Proton Monte Carlo simulation
- Role: process
- Action: Run Geant4 simulation of 100,000 protons with kinetic energies uniformly distributed between 0.1 and 1.0 MeV entering through the aperture. For each event, record incident kinetic energy, hit position on D1 (distance from center line), and deposited energy in D1. Save the raw data.
- Evidence: `/app/outputs/proton_raw_hits.csv`

### Step 5: Proton energy resolution analysis
- Role: scored
- Action: Load the proton simulation data. For each D1 strip pitch value in [5, 10, 15, 20] mm, bin hit positions into strips of that width, derive a measured energy, and compute the RMS error and energy resolution (RMS divided by mean deposited energy). Output the results.
- Output file: `/app/outputs/proton_analysis.csv`
- Format: csv
- Contract: CSV with header: strip_pitch_mm, rms_energy_MeV, energy_resolution_pct. One row per pitch value.
- Scoring: scored by hidden verifier

### Step 6: Determine optimal strip pitches
- Role: scored (load-bearing)
- Action: From electron_analysis.csv and proton_analysis.csv, identify the strip pitch that minimizes the RMS energy error for D2 (electrons) and for D1 (protons). Write the optimal pitches to a text file.
- Output file: `/app/outputs/optimal_pitches.txt`
- Format: txt
- Contract: Plain text with two lines: D2_optimal_pitch_mm=<float> and D1_optimal_pitch_mm=<float>.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electron_analysis.csv`
- `/app/outputs/proton_analysis.csv`
- `/app/outputs/optimal_pitches.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electron_analysis.csv
- path: `/app/outputs/electron_analysis.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: RMS energy error and energy resolution for D2 strip pitches. The RMS should decrease then increase, showing a minimum.
- schema:
  - `type`: table
  - `required_columns`: `strip_pitch_mm`, `rms_energy_MeV`, `energy_resolution_pct`

### proton_analysis.csv
- path: `/app/outputs/proton_analysis.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: RMS energy error and energy resolution for D1 strip pitches. The RMS should decrease then increase, showing a minimum.
- schema:
  - `type`: table
  - `required_columns`: `strip_pitch_mm`, `rms_energy_MeV`, `energy_resolution_pct`

### optimal_pitches.txt
- path: `/app/outputs/optimal_pitches.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Optimal strip pitches that minimize RMS energy error for electrons (D2) and protons (D1).
- schema:
  - `type`: text
  - `description`: Two lines: D2_optimal_pitch_mm=<value> and D1_optimal_pitch_mm=<value>.

Notes: The electron and proton analysis CSVs are verified by structural audit (RMS curve shape). The optimal pitches are the primary scored artifact; they are compared to the paper's reported values with a tolerance hidden from the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electron_analysis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strip_pitch_mm",
          "rms_energy_MeV",
          "energy_resolution_pct"
        ]
      },
      "description": "RMS energy error and energy resolution for D2 strip pitches. The RMS should decrease then increase, showing a minimum."
    },
    {
      "file": "proton_analysis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strip_pitch_mm",
          "rms_energy_MeV",
          "energy_resolution_pct"
        ]
      },
      "description": "RMS energy error and energy resolution for D1 strip pitches. The RMS should decrease then increase, showing a minimum."
    },
    {
      "file": "optimal_pitches.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Two lines: D2_optimal_pitch_mm=<value> and D1_optimal_pitch_mm=<value>."
      },
      "description": "Optimal strip pitches that minimize RMS energy error for electrons (D2) and protons (D1)."
    }
  ],
  "notes": "The electron and proton analysis CSVs are verified by structural audit (RMS curve shape). The optimal pitches are the primary scored artifact; they are compared to the paper's reported values with a tolerance hidden from the agent."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier that runs after the workflow completes. The electron and proton analysis CSVs are first inspected for their shape: the RMS error and energy resolution should show a clear minimum – decreasing then increasing – as the strip pitch varies; this structural check carries a small fraction of the total score. The main portion of the reward comes from a direct comparison of the optimal pitch values you report in `optimal_pitches.txt` against hidden reference values. A tolerance is applied that accounts for reasonable differences arising from toolchain choices and statistical fluctuations, so a faithful simulation will pass. You do not need to hit exact numbers, only to fall within the allowed tolerance.
