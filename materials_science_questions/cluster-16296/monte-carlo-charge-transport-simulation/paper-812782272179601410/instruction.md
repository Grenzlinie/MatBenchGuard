# Monte Carlo simulation of transient photocurrent and velocity overshoot in quantum well infrared photodetectors

## Problem background
Quantum well infrared photodetectors (QWIPs) operate via intersubband transitions in multiple-quantum-well structures. Under illumination by an ultrashort infrared pulse, photoexcited electrons are promoted into the Γ valley and experience a transient velocity overshoot before intervalley scattering transfers them into lower‑mobility satellite valleys. This overshoot produces a sharp photocurrent peak on sub‑picosecond timescales and can influence the frequency‑dependent responsivity of the device in the terahertz range. Capturing the nonequilibrium transport accurately requires an ensemble Monte Carlo particle simulation that tracks injection, capture, acceleration, intervalley scattering, and collection of electrons in the self‑consistent electric field.

## Approach
An ensemble Monte Carlo particle simulator is built for n‑type QWIPs made of two material systems: AlGaAs/GaAs and InP/InGaAs. The simulation includes electron injection from the emitter, capture into quantum wells, transport under the self‑consistent electric field, intervalley scattering among Γ, L, and X valleys, and escape to the collector. The steady‑state potential distribution before the pulse is obtained from the analytical model described by Ryzhii (1997) that accounts for the applied bias and steady illumination. Starting from this initial state, an ultrashort (δ‑like) infrared pulse photoexcites electrons from bound states into the Γ valley, and the resulting transient current is computed with sub‑picosecond resolution. From the transient current traces, the peak drift velocity is extracted as a function of average electric field, and the frequency‑dependent responsivity magnitude |R(ω)| is obtained via Fourier transform. The two material systems are compared under identical structural and operating conditions.

## Reproduction target
For both material systems (AlGaAs/GaAs and InP/InGaAs) with N=16 wells, period L=55 nm, average electric field E=50 kV/cm, temperature T=77 K, and a δ‑like infrared pulse (photon energy 0.1 eV), compute:
- The time‑dependent photocurrent (transient current vs time) for each system.
- The peak drift velocity v_peak as a function of average electric field across a range (e.g., 20–80 kV/cm) for both systems.
- The magnitude of the frequency‑dependent responsivity |R(ω)| vs frequency up to several THz for both systems, obtained from the transient current at the nominal field (E=50 kV/cm).

## Assets

- Material parameters for Al0.3Ga0.7As, GaAs, InP, In0.53Ga0.47As (band structure, scattering rates, effective masses): 10.1016/0010-4655(91)90109-X, 10.1002/9780470172780
- Analytical model for steady-state potential distribution in QWIPs from Ryzhii (1997): 10.1063/1.364518

## Workflow steps

### Step 1: Compute steady-state potential distribution
- Role: process
- Action: Implement the analytical model from the Ryzhii (1997) paper to calculate the self-consistent electrostatic potential profile along the multiple-quantum-well structure under the applied bias voltage V and steady infrared illumination I0, for the given device parameters (material system, doping, number of wells, period). This profile serves as the initial condition for the transient Monte Carlo simulation.
- Evidence: `/app/outputs/potential_profile.json`

### Step 2: Monte Carlo transient photocurrent – AlGaAs/GaAs
- Role: scored
- Action: Run the ensemble Monte Carlo particle simulator for an AlGaAs/GaAs QWIP with N=16 wells, period L=55 nm, average electric field E=50 kV/cm, temperature T=77 K, using the steady-state potential from s0. Apply a δ-like infrared pulse (photon energy 0.1 eV) that photoexcites electrons from bound states into the Γ valley. Simulate electron transport including injection, capture, intervalley scattering, and collection, and record the total transient current as a function of time with sub‑picosecond resolution.
- Output file: `/app/outputs/transient_current_AlGaAs.csv`
- Format: csv
- Contract: CSV with header: time, current
- Scoring: scored by hidden verifier

### Step 3: Monte Carlo transient photocurrent – InP/InGaAs
- Role: scored
- Action: Run the ensemble Monte Carlo particle simulator for an InP/InGaAs QWIP with identical structure (N=16, L=55 nm, E=50 kV/cm, T=77 K) and excitation conditions as in s1. Use the steady-state potential computed for the InP/InGaAs system. Record the transient current.
- Output file: `/app/outputs/transient_current_InP.csv`
- Format: csv
- Contract: CSV with header: time, current
- Scoring: scored by hidden verifier

### Step 4: Peak drift velocity vs electric field
- Role: scored
- Action: Run multiple Monte Carlo simulations for both material systems at a range of average electric fields (e.g., from 20 to 80 kV/cm). For each field, extract the peak electron drift velocity v_peak as the maximum of the ensemble-averaged velocity during the first 0.5 ps after the pulse. Compile a table of v_peak versus field for both systems.
- Output file: `/app/outputs/peak_velocity_vs_field.csv`
- Format: csv
- Contract: CSV with header: field, vpeak_AlGaAs, vpeak_InP
- Scoring: scored by hidden verifier

### Step 5: Frequency-dependent responsivity
- Role: scored (load-bearing)
- Action: From the transient photocurrent traces obtained for the nominal field (E=50 kV/cm) in s1 and s2, compute the frequency-dependent responsivity |R(ω)| via Fourier transform. For each material system, output the magnitude |R| as a function of frequency up to several THz. Combine into a single file.
- Output file: `/app/outputs/responsivity_vs_frequency.csv`
- Format: csv
- Contract: CSV with header: freq, R_AlGaAs, R_InP
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transient_current_AlGaAs.csv`
- `/app/outputs/transient_current_InP.csv`
- `/app/outputs/peak_velocity_vs_field.csv`
- `/app/outputs/responsivity_vs_frequency.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transient_current_AlGaAs.csv
- path: `/app/outputs/transient_current_AlGaAs.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated transient photocurrent for AlGaAs/GaAs QWIP. The hidden check compares the presence of a sharp peak within 0.5 ps, peak current amplitude, and decay shape against the paper's Fig. 5 with ±20% tolerance.
- schema:
  - `type`: table
  - `required_columns`: `time`, `current`
  - `units`:
    - `time`: ps
    - `current`: A

### transient_current_InP.csv
- path: `/app/outputs/transient_current_InP.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated transient photocurrent for InP/InGaAs QWIP. Checked similarly against Fig. 6.
- schema:
  - `type`: table
  - `required_columns`: `time`, `current`
  - `units`:
    - `time`: ps
    - `current`: A

### peak_velocity_vs_field.csv
- path: `/app/outputs/peak_velocity_vs_field.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Peak drift velocity vs electric field. The check verifies that vpeak_InP > vpeak_AlGaAs at each field and that the values fall within ±20% of the paper's gold values. Monotonic increase is also expected.
- schema:
  - `type`: table
  - `required_columns`: `field`, `vpeak_AlGaAs`, `vpeak_InP`
  - `units`:
    - `field`: kV/cm
    - `vpeak_AlGaAs`: cm/s
    - `vpeak_InP`: cm/s

### responsivity_vs_frequency.csv
- path: `/app/outputs/responsivity_vs_frequency.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Frequency-dependent responsivity. The check compares the magnitude at selected frequencies (e.g., 1 THz, 3 THz) against the paper's gold values within ±30% tolerance, and verifies that |R(ω)| decays with frequency and that R_InP > R_AlGaAs in the THz range.
- schema:
  - `type`: table
  - `required_columns`: `freq`, `R_AlGaAs`, `R_InP`
  - `units`:
    - `freq`: THz
    - `R_AlGaAs`: A/W
    - `R_InP`: A/W

Notes: All outputs are scored by direct comparison to the paper-reported values (T0 result-level compare). Tolerances are specified per artifact. The process step s0 is required but not scored; its evidence file is optional.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transient_current_AlGaAs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "current"
        ],
        "units": {
          "time": "ps",
          "current": "A"
        }
      },
      "description": "Simulated transient photocurrent for AlGaAs/GaAs QWIP. The hidden check compares the presence of a sharp peak within 0.5 ps, peak current amplitude, and decay shape against the paper's Fig. 5 with ±20% tolerance."
    },
    {
      "file": "transient_current_InP.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "current"
        ],
        "units": {
          "time": "ps",
          "current": "A"
        }
      },
      "description": "Simulated transient photocurrent for InP/InGaAs QWIP. Checked similarly against Fig. 6."
    },
    {
      "file": "peak_velocity_vs_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "field",
          "vpeak_AlGaAs",
          "vpeak_InP"
        ],
        "units": {
          "field": "kV/cm",
          "vpeak_AlGaAs": "cm/s",
          "vpeak_InP": "cm/s"
        }
      },
      "description": "Peak drift velocity vs electric field. The check verifies that vpeak_InP > vpeak_AlGaAs at each field and that the values fall within ±20% of the paper's gold values. Monotonic increase is also expected."
    },
    {
      "file": "responsivity_vs_frequency.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "freq",
          "R_AlGaAs",
          "R_InP"
        ],
        "units": {
          "freq": "THz",
          "R_AlGaAs": "A/W",
          "R_InP": "A/W"
        }
      },
      "description": "Frequency-dependent responsivity. The check compares the magnitude at selected frequencies (e.g., 1 THz, 3 THz) against the paper's gold values within ±30% tolerance, and verifies that |R(ω)| decays with frequency and that R_InP > R_AlGaAs in the THz range."
    }
  ],
  "notes": "All outputs are scored by direct comparison to the paper-reported values (T0 result-level compare). Tolerances are specified per artifact. The process step s0 is required but not scored; its evidence file is optional."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact. The verifier examines the transient current traces for the existence and timing of a sharp overshoot peak, evaluates the peak‑velocity‑vs‑field relationship and the relative comparison between the two material systems, and checks the responsivity magnitude and its trend with frequency. Each scored artifact contributes a weighted fraction to the final reward. Reporting the correct numbers is necessary but not sufficient; the verifier validates that the outputs are consistent with physically expected behavior and that the required trends are present.
