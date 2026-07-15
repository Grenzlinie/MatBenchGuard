# Hybrid kinetic–phase-field model for SMA elastocaloric cooling

## Problem background
Shape memory alloy (SMA) films exhibit the elastocaloric effect – a temperature change upon cyclic loading/unloading – making them candidates for solid-state micro‑cooling devices. The effect arises from a stress‑induced martensitic phase transformation that is highly localized in thin‑film geometries, where Lüders‑like strain bands nucleate and propagate. Understanding and predicting the coupled thermo‑mechanical response (macroscopic stress–strain characteristics, temperature evolution, and mesoscale band patterns) is critical for device design. This task reproduces the core simulation predictions of a model that captures these phenomena for a Ti‑Ni‑Cu‑Co film.

## Approach
The model combines the Müller–Achenbach–Seelecke (MAS) rate‑dependent kinetic law for martensite–austenite phase fractions with a diffuse‑interface phase‑field (PF) gradient energy term that penalises sharp interfaces. Together, these form a single evolution equation for the martensite fraction. The mechanical part uses 2D plane‑stress continuum mechanics with a transformation strain tensor that induces lateral contraction and produces inclined bands. Thermal coupling incorporates latent heat release/absorption, heat conduction (phase‑dependent conductivity) and convective surface cooling. Material inhomogeneity is introduced through a spatial lognormal distribution of the transformation stress barrier with a prescribed mean and standard deviation. The resulting coupled PDEs are solved via finite elements for a thin‑film sample under strain‑controlled cyclic loading at two different rates. From the computed spatiotemporal fields, the engineering stress–strain curve, the sample‑averaged temperature time series, and the dominant band tilt angle are extracted.

## Reproduction target
Produce three scored artifacts:
1. Engineering stress–strain curves (stress_strain_curves.csv) for strain rates 1×10⁻³ s⁻¹ and 1×10⁻² s⁻¹, covering full loading/unloading cycles to 2.1% strain.
2. Sample‑area‑averaged temperature evolution (temperature_evolution.csv) for the same two strain rates.
3. The dominant band tilt angle (in degrees) relative to the tensile direction, extracted from the martensite phase field at the moment of maximum strain for the 1×10⁻³ s⁻¹ run (band_angle.json).
A hidden verifier will compare these outputs to reference simulation data derived from the model implementation described in the source work.

## Assets

- Open-source finite element library (e.g., FEniCS, deal.II, or MOOSE): https://fenicsproject.org/

## Workflow steps

### Step 1: Run coupled thermo-mechanical MAS–PF simulation
- Role: process
- Action: Implement the 2D plane-stress finite element model for the SMA film (15 × 1.75 × 0.02 mm) using an open-source FEM library. Use the material parameters (Table 1 of the source): elastic moduli, transformation stresses, Clausius–Clapeyron coefficients, latent heat, conductivities, interface tension, kinetic coefficient, etc. Apply a lognormal distribution to the transformation stress barrier with mean 242 MPa and standard deviation 12 MPa. Apply strain-controlled cyclic loading to 2.1% strain at constant rates of 1×10⁻³ s⁻¹ and 1×10⁻² s⁻¹, each with a 10 s hold at maximum strain and after unloading. Solve the coupled PDEs for martensite fraction, mechanical equilibrium, and heat transfer with appropriate boundary conditions (clamped ends at ambient temperature, convective cooling on free boundaries). Save the complete spatiotemporal fields (martensite fraction, stress components, temperature) to a structured portable binary file (e.g., HDF5).
- Evidence: `/app/outputs/simulation_output.h5`

### Step 2: Extract engineering stress-strain curves
- Role: scored (load-bearing)
- Action: From simulation_output.h5, compute the engineering stress (area-averaged Tresca stress over the sample) and engineering strain (sample displacement divided by length) at each measurement point for both strain rates, covering the full loading/unloading cycles. Write the data to stress_strain_curves.csv.
- Output file: `/app/outputs/stress_strain_curves.csv`
- Format: csv
- Contract: strain_rate[float],strain[float],stress[float]
- Scoring: scored by hidden verifier

### Step 3: Extract sample-averaged temperature evolution
- Role: scored
- Action: From simulation_output.h5, compute the sample-area-averaged temperature at each time step for each strain rate. Write the data to temperature_evolution.csv.
- Output file: `/app/outputs/temperature_evolution.csv`
- Format: csv
- Contract: strain_rate[float],time[float],temperature[float]
- Scoring: scored by hidden verifier

### Step 4: Extract dominant band tilt angle
- Role: scored
- Action: From simulation_output.h5, load the martensite phase field at the time of maximum applied strain for the 1×10⁻³ s⁻¹ run. Identify the dominant orientation of the A-M interfaces (e.g., via gradient analysis) and report the angle in degrees relative to the tensile direction in band_angle.json.
- Output file: `/app/outputs/band_angle.json`
- Format: json
- Contract: {"angle": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain_curves.csv`
- `/app/outputs/temperature_evolution.csv`
- `/app/outputs/band_angle.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain_curves.csv
- path: `/app/outputs/stress_strain_curves.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Engineering stress–strain curves for strain-controlled tensile loading/unloading at 1×10⁻³ s⁻¹ and 1×10⁻² s⁻¹. The checker computes the mean absolute percentage error (MAPE) of the stress values against digitized reference curves from the paper; MAPE < 5% for both rates is required.
- schema:
  - `type`: table
  - `required_columns`: `strain_rate`, `strain`, `stress`
  - `units`:
    - `strain_rate`: s⁻¹
    - `strain`: 1
    - `stress`: MPa

### temperature_evolution.csv
- path: `/app/outputs/temperature_evolution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sample-area-averaged temperature versus time for the two strain rates. The checker extracts the maximum temperature rise (T_max − T0) and minimum temperature drop (T0 − T_min) and compares them to paper‑reported simulation values; both must be within ±0.5 K.
- schema:
  - `type`: table
  - `required_columns`: `strain_rate`, `time`, `temperature`
  - `units`:
    - `strain_rate`: s⁻¹
    - `time`: s
    - `temperature`: K

### band_angle.json
- path: `/app/outputs/band_angle.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dominant band tilt angle (in degrees) measured from the martensite phase field at the peak strain of the 1×10⁻³ s⁻¹ run. The checker verifies that the reported angle lies within 53°–57°.
- schema:
  - `type`: object
  - `required`:
    - `angle`: float
  - `units`:
    - `angle`: degrees

Notes: The simulation evidence file (simulation_output.h5) is not scored but must be produced by the process step. The verifier reads only the three scored artifacts; it does not re‑run the FEM simulation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_rate",
          "strain",
          "stress"
        ],
        "units": {
          "strain_rate": "s⁻¹",
          "strain": "1",
          "stress": "MPa"
        }
      },
      "description": "Engineering stress–strain curves for strain-controlled tensile loading/unloading at 1×10⁻³ s⁻¹ and 1×10⁻² s⁻¹. The checker computes the mean absolute percentage error (MAPE) of the stress values against digitized reference curves from the paper; MAPE < 5% for both rates is required."
    },
    {
      "file": "temperature_evolution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_rate",
          "time",
          "temperature"
        ],
        "units": {
          "strain_rate": "s⁻¹",
          "time": "s",
          "temperature": "K"
        }
      },
      "description": "Sample-area-averaged temperature versus time for the two strain rates. The checker extracts the maximum temperature rise (T_max − T0) and minimum temperature drop (T0 − T_min) and compares them to paper‑reported simulation values; both must be within ±0.5 K."
    },
    {
      "file": "band_angle.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "angle": "float"
        },
        "units": {
          "angle": "degrees"
        }
      },
      "description": "Dominant band tilt angle (in degrees) measured from the martensite phase field at the peak strain of the 1×10⁻³ s⁻¹ run. The checker verifies that the reported angle lies within 53°–57°."
    }
  ],
  "notes": "The simulation evidence file (simulation_output.h5) is not scored but must be produced by the process step. The verifier reads only the three scored artifacts; it does not re‑run the FEM simulation."
}
```

## How you are scored
A hidden verifier script reads each of the three output files, compares the data to hidden reference results, and computes per‑artifact scores. For instance, the stress‑strain curves are compared to a reference curve, the temperature evolution is checked for agreement of key features, and the band angle is verified to lie within an expected range. The per‑artifact scores are then combined using predetermined weights to produce a final reward between 0 and 1. You must generate all three files in the exact format specified; the verifier does not re‑run the simulation.
