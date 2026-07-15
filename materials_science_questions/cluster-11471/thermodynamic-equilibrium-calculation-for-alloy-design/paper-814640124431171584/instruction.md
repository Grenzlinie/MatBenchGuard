# Tensile Property Prediction for Medium-Mn Steel Using Isostrain Composite Model

## Problem background
Medium-Mn transformation-induced plasticity (TRIP) steels achieve attractive strength–ductility combinations through strain-induced austenite-to-martensite transformation. A simple isostrain composite model, combined with power‑law flow descriptions for each constituent phase and the Olson–Cohen transformation‑kinetics law, can predict the tensile behaviour—ultimate tensile strength (UTS), uniform elongation, and engineering stress–strain curves—of a Fe‑7.09Mn‑0.099C‑0.13Si (wt%) steel intercritically annealed at 600 °C, 625 °C, and 650 °C. This task requires implementing that model and producing the predicted mechanical properties for these three conditions.

## Approach
The composite model treats each phase (ferrite, austenite, martensite) as a load‑bearing constituent whose flow behaviour follows a Hollomon power law, σ = K ε^n. During deformation, austenite transforms to martensite according to the Olson–Cohen kinetic equation, which depends on three parameters (α, β, m) that describe shear‑band formation and nucleation probability. At each strain increment the phase fractions are updated, and the composite true stress is computed by volume‑fraction‑weighted averaging of the constituent stresses (the rule of mixtures). True stress–strain curves are converted to engineering stress–strain curves, and the plastic instability point (UTS and uniform elongation) is identified by the Considère criterion, dσ/dε = σ. The simulation is performed for three annealing temperatures (600 °C, 625 °C, 650 °C). Each temperature has a specific starting phase distribution and a specific set of Olson–Cohen parameters, all listed below. All required numeric values (initial phase fractions, Hollomon strength coefficients and strain‑hardening exponents, Olson‑Cohen parameters) are provided in these instructions; no external data retrieval is needed.

## Reproduction target
Produce two scored artifacts:
1. A CSV file, `predicted_properties.csv`, containing for each annealing temperature the predicted ultimate tensile strength (MPa) and the predicted uniform elongation (engineering strain, unitless).
2. A CSV file, `stress_strain_curves.csv`, containing the engineering stress–strain curves sampled at strain intervals no larger than 0.001, up to the instability point, for each annealing temperature.

These artifacts are the measurable target; they are generated from the composite‑model simulation described in the workflow steps. The hidden verifier compares them against reference results.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy (optimize): scipy

## Workflow steps

### Step 1: Run Composite Model Simulation
- Role: process
- Action: For each of the three annealing temperatures (600°C, 625°C, 650°C), set the initial phase fractions (austenite, ferrite, martensite) from provided values; assign each constituent a Hollomon flow law σ = K ε^n using provided strength coefficients and hardening exponents; update phase fractions during deformation with the Olson–Cohen equation f_α' = 1 – exp[–β (1 – exp(–α ε))^m] using provided α, β, m; compute composite true stress by the rule of mixtures; convert to engineering stress–strain; apply the Considère instability condition to find the tearing point; save the full trajectory (true strain, true stress, phase fractions, engineering stress, engineering strain) for each temperature.
- Evidence: `/app/outputs/simulation_intermediate.csv`

### Step 2: Extract Predicted Tensile Properties
- Role: scored
- Action: From the simulation output, determine the ultimate tensile strength (maximum engineering stress) and uniform elongation (engineering strain at that maximum) for each annealing temperature, and write to predicted_properties.csv.
- Output file: `/app/outputs/predicted_properties.csv`
- Format: csv
- Contract: CSV with header: annealing_temperature_C, predicted_UTS_MPa, predicted_uniform_elongation. Each row corresponds to one temperature (600, 625, 650).
- Scoring: scored by hidden verifier

### Step 3: Extract Engineering Stress–Strain Curves
- Role: scored (load-bearing)
- Action: From the simulation output, sample the engineering stress–strain curves at a strain resolution of at least 0.001 up to the instability point for each annealing temperature, and write to stress_strain_curves.csv.
- Output file: `/app/outputs/stress_strain_curves.csv`
- Format: csv
- Contract: CSV with header: annealing_temperature_C, engineering_strain, engineering_stress_MPa. Each row is a sampled point on one of the three curves. Strain increment ≤ 0.001, data up to the instability strain.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_properties.csv`
- `/app/outputs/stress_strain_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_properties.csv
- path: `/app/outputs/predicted_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Predicted ultimate tensile strength and uniform elongation for the three annealing conditions, to be compared against the paper's hidden reference by the checker.
- schema:
  - `type`: table
  - `required_columns`: `annealing_temperature_C`, `predicted_UTS_MPa`, `predicted_uniform_elongation`
  - `units`:
    - `predicted_UTS_MPa`: MPa
    - `predicted_uniform_elongation`: strain (unitless)
    - `annealing_temperature_C`: °C

### stress_strain_curves.csv
- path: `/app/outputs/stress_strain_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Engineering stress–strain curves up to the instability point for each annealing condition; the checker recomputes the instability point (max stress) and uniform elongation from these data.
- schema:
  - `type`: table
  - `required_columns`: `annealing_temperature_C`, `engineering_strain`, `engineering_stress_MPa`
  - `units`:
    - `engineering_stress_MPa`: MPa
    - `engineering_strain`: strain (unitless)
    - `annealing_temperature_C`: °C

Notes: Both scored artifacts are derived from the same simulation. The checker will verify that the instability point extracted from stress_strain_curves.csv matches the hidden gold UTS and uniform elongation within tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "annealing_temperature_C",
          "predicted_UTS_MPa",
          "predicted_uniform_elongation"
        ],
        "units": {
          "predicted_UTS_MPa": "MPa",
          "predicted_uniform_elongation": "strain (unitless)",
          "annealing_temperature_C": "°C"
        }
      },
      "description": "Predicted ultimate tensile strength and uniform elongation for the three annealing conditions, to be compared against the paper's hidden reference by the checker."
    },
    {
      "file": "stress_strain_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "annealing_temperature_C",
          "engineering_strain",
          "engineering_stress_MPa"
        ],
        "units": {
          "engineering_stress_MPa": "MPa",
          "engineering_strain": "strain (unitless)",
          "annealing_temperature_C": "°C"
        }
      },
      "description": "Engineering stress–strain curves up to the instability point for each annealing condition; the checker recomputes the instability point (max stress) and uniform elongation from these data."
    }
  ],
  "notes": "Both scored artifacts are derived from the same simulation. The checker will verify that the instability point extracted from stress_strain_curves.csv matches the hidden gold UTS and uniform elongation within tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your output files and compares them against reference values. For `predicted_properties.csv`, the verifier checks the predicted UTS and uniform elongation for each annealing temperature against pre‑set tolerance windows. For `stress_strain_curves.csv`, the verifier recomputes the instability point (maximum engineering stress and the corresponding strain) from your submitted curves and verifies consistency with the predicted properties. Both artifacts contribute to a combined reward score between 0 and 1; the exact tolerances and weighting are not disclosed. Focus on correctly implementing the physics‑based model and the numerical procedures described in the instructions.
