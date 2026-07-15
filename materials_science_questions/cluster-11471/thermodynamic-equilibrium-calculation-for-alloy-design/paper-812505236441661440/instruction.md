# Phase Evolution Simulation in Laser Surface Engineering of Nodular Cast Iron

## Problem background
Laser surface engineering (LSE) uses a moving laser beam to locally heat and rapidly cool the surface of nodular cast iron, creating a modified layer with enhanced wear resistance. The process induces complex phase transformations that depend on the initial microstructure, alloy composition, laser power, and scanning velocity. Accurately predicting the resulting phase distribution (graphite, ferrite, pearlite, austenite, ledeburite, martensite) as a function of depth is essential for designing treatment parameters. This task reproduces a computational thermo‑metallurgical model that simulates an LSE treatment on a ferritic nodular cast iron and computes the final phase volume fractions at given depths.

## Approach
The approach couples a macroscopic thermal simulation with a point‑wise metallurgical model. The thermal model solves the transient heat conduction equation on a 3D geometry using the finite‑element method. A moving rectangular laser beam with known spatial energy distribution, power, and scanning velocity provides the heat input, and convective‑radiative conditions are applied on external boundaries. The temperature history at each material point is then fed into a metallurgical model that integrates ordinary differential equations describing the sequence of phase transformations: reverse eutectoid transformation (ferrite/pearlite → austenite + graphite), carbon homogenisation in austenite, melting, solidification (liquid → ledeburite), eutectoid transformation during cooling, and martensitic transformations. The initial as‑cast microstructure (graphite nodule count, volume fractions of graphite and ferrite) and the alloy chemical composition are required inputs.

## Reproduction target
Reproduce the final phase volume fractions and the ledeburite‑martensite layer thickness for a specific LSE treatment scenario (referred to as case V2). The material is a ferritic nodular cast iron with composition 3.63 C‑2.7 Si‑0.25 Mn‑0.049 Cr‑Fe (wt %), initial graphite volume fraction 0.1165, graphite nodule count 1.0635 × 10¹³ m⁻³, and fully ferritic matrix (ferrite fraction 0.8835). The laser beam is rectangular (23 mm × 2 mm) with a uniform spatial energy distribution. The incident power varies linearly from 2500 W to 3500 W along the scanning path, and the scanning velocity is 1000 mm/min. The local absorptivity is computed with a bilinear model using coefficients k₁ = −2.268 × 10⁻⁴ /W, k₂ = −9.0967 × 10⁻⁵ min/mm, k₃ = 7.3033 × 10⁻⁸ min/(W·mm), k₄ = 1.227. After the simulation has returned the entire domain to room temperature, extract the volume fractions of graphite, ferrite, pearlite, austenite, ledeburite, and martensite at the centreline for depths 0, 100, 200, 300, and 400 µm below the irradiated surface. Also, determine the depth where the ledeburite volume fraction reaches or exceeds 0.9 and report this as the ledeburite‑martensite layer thickness.

## Assets

- Temperature‑dependent thermal properties of nodular cast iron: 10.1007/s11663-015-0508-6, 10.1007/s11663-012-9725-1
- FEniCS finite element solver: fenics
- SciPy numerical integration library: scipy

## Workflow steps

### Step 1: Model setup and input preparation
- Role: process
- Action: Prepare the simulation inputs for case V2: define the 3D half‑symmetry geometry (domain dimensions 100 mm × 32 mm × 2.5 mm) and a finite‑element mesh with refinement near the irradiated surface. Set up temperature‑dependent material thermal properties (density, thermal conductivity, specific heat) from the published literature. Initialize the as‑cast microstructure: graphite volume fraction 0.1165, ferrite fraction 0.8835, pearlite fraction 0.0, graphite nodule count 1.0635e13 m⁻³. Set the laser parameters: rectangular beam 23 mm × 2 mm with uniform spatial energy distribution, incident laser power linearly varying from 2500 W to 3500 W along the scanning path, scanning velocity 1000 mm/min. Compute the local laser absorptivity using the bilinear model with the published coefficients k₁ = −2.268×10⁻⁴ /W, k₂ = −9.0967×10⁻⁵ min/mm, k₃ = 7.3033×10⁻⁸ min/(W·mm), k₄ = 1.227. Record the prepared parameters in a log file.
- Evidence: `/app/outputs/setup_report.txt`

### Step 2: Run thermo‑metallurgical simulation
- Role: process
- Action: Implement the coupled thermo‑metallurgical model. Solve the 3D transient heat conduction equation with the moving laser heat source and convection‑radiation boundary conditions on all external faces using the finite‑element method. Simultaneously, for each material point, integrate the system of ordinary differential equations describing the reverse eutectoid transformation (stable ferrite → austenite+graphite and metastable pearlite → austenite), carbon homogenisation in austenite, melting, eutectoid transformation during cooling, solidification into ledeburite, and martensitic transformations in the nodular cast iron and the ledeburite. The phase kinetics follow spherical‑domain diffusion‑controlled growth for the stable path and unidimensional‑domain diffusion for the pearlite path, with volume fractions updated from the domain radii or interface coordinates. Use the temperature history from the thermal solver as forcing. Run the simulation for case V2 until the whole domain returns to room temperature. Record a log of the simulation progress.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Extract phase fraction profiles
- Role: scored (load-bearing)
- Action: From the final simulation state at the centreline of the treated region, extract the volume fractions of graphite, ferrite, pearlite, austenite, ledeburite, and martensite at depths 0, 100, 200, 300, 400 µm below the irradiated surface. Write the results to /app/outputs/phase_fractions.csv as one row per depth.
- Output file: `/app/outputs/phase_fractions.csv`
- Format: csv
- Contract: Columns: depth_um (integer, micrometres), f_graphite (float, 0–1), f_ferrite (float, 0–1), f_pearlite (float, 0–1), f_austenite (float, 0–1), f_ledeburite (float, 0–1), f_martensite (float, 0–1). One row per depth point.
- Scoring: scored by hidden verifier

### Step 4: Compute ledeburite‑martensite layer thickness
- Role: scored
- Action: Using the ledeburite volume fraction field from the completed simulation, determine the depth (in micrometres) where the ledeburite fraction first reaches or exceeds 0.9. Report this value as the ledeburite‑martensite layer thickness. Write a JSON file /app/outputs/layer_thickness.json with the case identifier and the thickness.
- Output file: `/app/outputs/layer_thickness.json`
- Format: json
- Contract: JSON object with keys: 'case' (string, 'V2') and 'ledeburite_martensite_layer_thickness_um' (float, micrometres).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_fractions.csv`
- `/app/outputs/layer_thickness.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_fractions.csv
- path: `/app/outputs/phase_fractions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase volume fractions at the centreline for depths 0‑400 µm, comparing against paper‑reported values for case V2 within a fixed tolerance.
- schema:
  - `type`: table
  - `required_columns`: `depth_um`, `f_graphite`, `f_ferrite`, `f_pearlite`, `f_austenite`, `f_ledeburite`, `f_martensite`
  - `units`:
    - `depth_um`: micrometres

### layer_thickness.json
- path: `/app/outputs/layer_thickness.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Depth where ledeburite fraction ≥ 0.9, compared to the experimental reference for case V2.
- schema:
  - `type`: object
  - `required`:
    - `case`: string
    - `ledeburite_martensite_layer_thickness_um`: float

Notes: The hidden reference values were extracted from the paper’s simulated curves and measured layer thickness for case V2. The agent must implement the full coupled thermo‑metallurgical solver; using pre‑existing commercial software results is not accepted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_fractions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "depth_um",
          "f_graphite",
          "f_ferrite",
          "f_pearlite",
          "f_austenite",
          "f_ledeburite",
          "f_martensite"
        ],
        "units": {
          "depth_um": "micrometres"
        }
      },
      "description": "Phase volume fractions at the centreline for depths 0‑400 µm, comparing against paper‑reported values for case V2 within a fixed tolerance."
    },
    {
      "file": "layer_thickness.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "case": "string",
          "ledeburite_martensite_layer_thickness_um": "float"
        }
      },
      "description": "Depth where ledeburite fraction ≥ 0.9, compared to the experimental reference for case V2."
    }
  ],
  "notes": "The hidden reference values were extracted from the paper’s simulated curves and measured layer thickness for case V2. The agent must implement the full coupled thermo‑metallurgical solver; using pre‑existing commercial software results is not accepted."
}
```

## How you are scored
A hidden verifier independently scores each of the required output files. For `phase_fractions.csv` it compares your reported phase fractions (graphite, ferrite, pearlite, austenite, ledeburite, martensite) at each depth against reference values (extracted from the original study for case V2) using appropriate absolute tolerances. For `layer_thickness.json` it compares your reported ledeburite‑martensite layer thickness against the corresponding reference value. The two outputs carry different weights, and the final reward is a weighted combination of the scores. Simply reporting numbers from external sources without executing the full thermo‑metallurgical simulation is not sufficient; the verifier is designed to reward a genuine re‑implementation of the model.
