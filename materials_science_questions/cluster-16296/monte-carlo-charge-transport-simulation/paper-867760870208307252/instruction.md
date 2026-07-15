# FDTD Simulation of Broadside-Coupled SRR Metamaterial with Tunable Lateral Offset

## Problem background
Terahertz-frequency metamaterials can achieve nonlinear transmission responses by integrating semiconductor elements that interact with confined electric fields. A promising design is the broadside-coupled split-ring resonator (BC-SRR), where two stacked arrays of metallic SRRs control near-field coupling. The lateral positioning of the upper array relative to the lower array alters the mutual capacitance and inductance, which shifts resonance frequencies and changes the field confinement in the capacitive gaps. This task computationally investigates how the resonance behavior and local electric field enhancement in such a BC-SRR structure depend on the lateral offset between the two SRR layers.

## Approach
The approach uses finite-difference time-domain (FDTD) simulations, implemented with the open-source MEEP package. A three-dimensional unit cell is constructed with gold SRRs, a polyimide spacer, and a GaAs substrate containing an n-doped epilayer. A broadband terahertz plane wave is launched with the electric field polarized across the SRR capacitive gaps. For a set of lateral offsets L_shift, the complex transmission coefficient S21 is recorded as a function of frequency. Additionally, near the resonance condition, the time-domain electric field distribution in the plane of the lower SRR gap is captured. Post-processing yields the transmission magnitude |S21|, the resonance depth and frequency of the lowest-order BC-SRR mode, and the local-field enhancement factor (ratio of maximum gap field to incident field). These steps isolate the structural tuning mechanism studied in the original work.

## Reproduction target
The objective is to numerically reproduce the transmission spectra and resonance characteristics for the BC-SRR unit cell described above. Specifically, you must produce two scored CSV files under /app/outputs: transmission_spectra.csv (columns L_shift, frequency, transmission) for L_shift = 0, 12, 24, 36, 48 µm, and resonance_properties.csv (columns L_shift, resonance_frequency, resonance_depth, local_field_enhancement) for at least the extreme offsets 0 and 48 µm. The tasks are to run the FDTD simulations, extract the required quantities, and format the outputs according to the given schemas. No experimental measurements are required.

## Assets

- MEEP: https://github.com/NanoComp/meep

## Workflow steps

### Step 1: Run FDTD simulations for frequency-domain transmission and near-field
- Role: process
- Action: Set up the BC-SRR metamaterial unit cell in MEEP using the geometry: lower SRR L1=28 µm, w1=6 µm, g1=2 µm; upper SRR L2=48 µm, w2=6 µm, g2=2 µm; periodicity P=96 µm; 2 µm thick polyimide spacer between arrays; lower SRR on 1 µm n-GaAs epilayer (n=2e16 cm⁻³) above semi-insulating GaAs; gold modeled as a lossy metal. For each lateral offset L_shift in [0, 12, 24, 36, 48] µm, run a broadband simulation with THz excitation polarized perpendicular to the SRR capacitive gaps and record the complex transmission coefficient (S21) vs. frequency. For L_shift=0 and 48 µm, also store the time-domain electric field strength in the plane of the lower SRR gap to enable field enhancement calculation. Archive the raw data for subsequent post-processing.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Generate transmission_spectra.csv
- Role: scored (load-bearing)
- Action: From the FDTD results, compile the transmission magnitude (|S21|) versus frequency for each L_shift. Save as CSV with one row per frequency point.
- Output file: `/app/outputs/transmission_spectra.csv`
- Format: csv
- Contract: CSV with three columns: L_shift (float, µm), frequency (float, THz), transmission (float, unitless).
- Scoring: scored by hidden verifier

### Step 3: Generate resonance_properties.csv
- Role: scored (load-bearing)
- Action: Analyze the transmission spectra to determine, for each L_shift, the frequency and depth (minimum transmission) of resonance A. Using the near-field data for the two extreme offsets, compute the local electric field enhancement factor as max(|E| in lower SRR gap) divided by the incident field amplitude. Write the results to resonance_properties.csv.
- Output file: `/app/outputs/resonance_properties.csv`
- Format: csv
- Contract: CSV with four columns: L_shift (float, µm), resonance_frequency (float, THz), resonance_depth (float, unitless transmission minimum), local_field_enhancement (float, ratio; may be empty for intermediate L_shift values).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transmission_spectra.csv`
- `/app/outputs/resonance_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transmission_spectra.csv
- path: `/app/outputs/transmission_spectra.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Transmission magnitude |S21| vs frequency for each L_shift value. The checker will recompute the resonance depth (minimum transmission) and frequency for resonance A at L_shift=0 and 48 µm to verify the ~80% depth increase and frequency shift.
- schema:
  - `type`: table
  - `required_columns`: `L_shift`, `frequency`, `transmission`
  - `units`:
    - `L_shift`: µm
    - `frequency`: THz
    - `transmission`: unitless

### resonance_properties.csv
- path: `/app/outputs/resonance_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Extracted resonance A properties per offset: frequency, depth, and local field enhancement factor (for L_shift=0 and 48 µm). Checker verifies these match the paper's reference values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `L_shift`, `resonance_frequency`, `resonance_depth`, `local_field_enhancement`
  - `units`:
    - `L_shift`: µm
    - `resonance_frequency`: THz
    - `resonance_depth`: unitless transmission
    - `local_field_enhancement`: ratio

Notes: The task reproduces only the FDTD simulation pipeline that quantifies structural tuning of the metamaterial resonance and local field enhancement. The experimental THz-TDS measurements and fabrication steps are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transmission_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "L_shift",
          "frequency",
          "transmission"
        ],
        "units": {
          "L_shift": "µm",
          "frequency": "THz",
          "transmission": "unitless"
        }
      },
      "description": "Transmission magnitude |S21| vs frequency for each L_shift value. The checker will recompute the resonance depth (minimum transmission) and frequency for resonance A at L_shift=0 and 48 µm to verify the ~80% depth increase and frequency shift."
    },
    {
      "file": "resonance_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L_shift",
          "resonance_frequency",
          "resonance_depth",
          "local_field_enhancement"
        ],
        "units": {
          "L_shift": "µm",
          "resonance_frequency": "THz",
          "resonance_depth": "unitless transmission",
          "local_field_enhancement": "ratio"
        }
      },
      "description": "Extracted resonance A properties per offset: frequency, depth, and local field enhancement factor (for L_shift=0 and 48 µm). Checker verifies these match the paper's reference values within tolerances."
    }
  ],
  "notes": "The task reproduces only the FDTD simulation pipeline that quantifies structural tuning of the metamaterial resonance and local field enhancement. The experimental THz-TDS measurements and fabrication steps are excluded."
}
```

## How you are scored
A hidden verifier program will independently read your two CSV outputs after the task completes. It will verify that the files are present, contain the required columns, and have the expected shapes. For the transmission spectra, the verifier will recompute the resonance depth and frequency of the lowest-order mode at the extreme L_shift values and compare the relative changes against a set of hidden criteria derived from the original study. For the resonance properties, it will check that the reported resonance frequencies, depths, and field enhancement factors are self-consistent with the transmission data and that the relative trends match expectations. The final numeric reward is a weighted combination of these checks; higher scores are earned when your computed results faithfully capture the physics of the structural tuning observed in the literature.
