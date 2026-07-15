# Rigid-Plastic FEM Simulation of Deep Drawing with Ductile Fracture Criterion

## Problem background
Predicting the forming limit in sheet metal deep drawing is crucial for manufacturing special steel sheets with low ductility, where fracture can occur without any obvious necking. Traditional approaches based on tensile instability or bifurcation are often inadequate. This task evaluates whether a coupled rigid-plastic finite element simulation with a ductile fracture criterion can correctly predict the fracture initiation site and the critical punch stroke, thereby determining the formability under given tooling and blank configurations.

## Approach
The approach is to implement an axisymmetric rigid-plastic finite element method for the deep drawing process. The material is modeled as slightly compressible and anisotropic using a modified Hill yield criterion, taking into account the normal anisotropy. The true stress–strain relation follows a power law. The Oyane ductile fracture criterion is integrated into the simulation: for each element, at every deformation increment, the equivalent stress, hydrostatic stress, and incremental equivalent strain are computed, and the fracture integral is accumulated. The material constants for the fracture criterion are first calibrated using the uniaxial and plane-strain fracture strains of the sheet, derived from analytical stress–strain relations. The simulation is run for two drawing conditions with different punch profile radii and blank diameters. At each step the fracture integral is checked; the punch stroke at which the integral first reaches unity in any element is taken as the critical punch stroke. For one of the conditions, the through‑thickness‑averaged sheet thickness is also extracted at the critical stroke.

## Reproduction target
Reproduce the deep drawing simulation for material A (a Zn‑coated hard steel sheet) with a flow curve described by σ = 858 ε^0.03 (MPa) and normal anisotropy r = 0.87. Use the Oyane fracture constants obtained from the calibration step, a punch diameter of 40 mm, die diameter of 42.5 mm, die profile radius of 8 mm, and a friction coefficient of 0.1. Simulate two specific conditions: (i) punch profile radius 2 mm, blank diameter 80 mm; (ii) punch profile radius 8 mm, blank diameter 77 mm. For each condition, determine the critical punch stroke (in mm) at which the element‑wise fracture integral first reaches 1 and report both values in a JSON file. For condition (i) only, also extract the through‑thickness‑averaged sheet thickness at that critical stroke as a function of initial radial position and save it as a CSV file.

## Assets

- Python scientific computing packages: numpy scipy matplotlib

## Workflow steps

### Step 1: Calibrate Oyane fracture constants a and b
- Role: process
- Action: Using the uniaxial and plane‑strain fracture strains for material A (ε₁f = 0.303 and 0.130, respectively) and the normal anisotropy r = 0.87, apply the analytical stress‑strain ratios for uniaxial and plane‑strain tension to compute the Oyane ductile fracture material constants a and b. Save the computed constants.
- Evidence: `/app/outputs/oyane_constants.json`

### Step 2: Run rigid‑plastic FEM simulation and fracture integral accumulation
- Role: process
- Action: Implement the axisymmetric rigid‑plastic FEM formulation with slightly compressible material and the modified Hill yield criterion (a small positive constant g=0.001). Use flow curve σ = 858 ε^0.03 (MPa), anisotropy r=0.87, and the computed Oyane constants a,b. Simulate deep drawing for two conditions using: punch diameter 40 mm, die diameter 42.5 mm, die profile radius 8 mm, friction coefficient 0.1, through‑thickness solid elements. Condition (i): punch profile radius 2 mm, blank diameter 80 mm. Condition (ii): punch profile radius 8 mm, blank diameter 77 mm. At each deformation increment, evaluate elementwise equivalent stress, hydrostatic stress, and incremental equivalent strain, and accumulate the Oyane fracture integral I = (1/b)∫(σₘ/σ̄ + a) dε̄. Identify the first punch stroke where I reaches 1 in any element and save the deformed mesh and element thicknesses at that stroke.
- Evidence: `/app/outputs/simulation_results.pkl`

### Step 3: Extract critical punch strokes
- Role: scored (load-bearing)
- Action: From the simulation evidence, extract the critical punch stroke (mm) at which the fracture integral first reaches 1 for each of the two drawing conditions. Write a JSON object containing both values.
- Output file: `/app/outputs/critical_punch_strokes.json`
- Format: json
- Contract: JSON object with numeric keys 'condition_i' and 'condition_ii'.
- Scoring: scored by hidden verifier

### Step 4: Extract thickness distribution
- Role: scored (load-bearing)
- Action: For condition (i) only, extract the through‑thickness‑averaged sheet thickness at the critical stroke as a function of initial radial position. Write a CSV file with the positions and corresponding thicknesses.
- Output file: `/app/outputs/thickness_distribution.csv`
- Format: csv
- Contract: Columns: radial_position_mm (float), thickness_mm (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_punch_strokes.json`
- `/app/outputs/thickness_distribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_punch_strokes.json
- path: `/app/outputs/critical_punch_strokes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical punch strokes at fracture initiation for condition (i) (r_p=2 mm, d0=80 mm) and condition (ii) (r_p=8 mm, d0=77 mm). The hidden checker compares these reported values to the paper's gold values (6.3 mm and 11.0 mm) within a composite tolerance.
- schema:
  - `type`: object
  - `required`:
    - `condition_i`: number
    - `condition_ii`: number
  - `units`:
    - `condition_i`: mm
    - `condition_ii`: mm

### thickness_distribution.csv
- path: `/app/outputs/thickness_distribution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Through‑thickness‑averaged sheet thickness profile at the critical fracture stroke for condition (i). The hidden checker computes mean absolute error against a digitized reference profile from the paper.
- schema:
  - `type`: table
  - `required_columns`: `radial_position_mm`, `thickness_mm`
  - `units`:
    - `radial_position_mm`: mm
    - `thickness_mm`: mm

Notes: Only material A is considered. The two specific drawing conditions are as listed. The calibration and simulation steps are process steps that must be genuinely executed to produce the scored artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_punch_strokes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "condition_i": "number",
          "condition_ii": "number"
        },
        "units": {
          "condition_i": "mm",
          "condition_ii": "mm"
        }
      },
      "description": "Critical punch strokes at fracture initiation for condition (i) (r_p=2 mm, d0=80 mm) and condition (ii) (r_p=8 mm, d0=77 mm). The hidden checker compares these reported values to the paper's gold values (6.3 mm and 11.0 mm) within a composite tolerance."
    },
    {
      "file": "thickness_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radial_position_mm",
          "thickness_mm"
        ],
        "units": {
          "radial_position_mm": "mm",
          "thickness_mm": "mm"
        }
      },
      "description": "Through‑thickness‑averaged sheet thickness profile at the critical fracture stroke for condition (i). The hidden checker computes mean absolute error against a digitized reference profile from the paper."
    }
  ],
  "notes": "Only material A is considered. The two specific drawing conditions are as listed. The calibration and simulation steps are process steps that must be genuinely executed to produce the scored artifacts."
}
```

## How you are scored
Your submitted output files are evaluated by a hidden verifier. The two critical punch strokes are compared to reference values using a composite absolute/relative tolerance. The thickness distribution is compared to a reference profile using mean absolute error. Each scored artifact contributes to a weighted final reward between 0 and 1. The exact reference values, tolerances, and weights are hidden; your task is to genuinely run the described simulation and report its results — simply copying numbers from the paper will not satisfy the tolerance constraints and is not sufficient.
