# Fracture Simulation of Square Punch Deep-Drawing with Uncoupled MMC Damage Model

## Problem background
Sheet metal forming of Advanced High Strength Steels (AHSS) is often limited by shear‑induced fracture that conventional Forming Limit Diagrams cannot predict. The Modified Mohr‑Coulomb (MMC) fracture criterion has been proposed to model crack initiation and propagation under complex loading by accounting for stress triaxiality and Lode angle. This task reproduces a deep‑drawing simulation using an uncoupled MMC damage model to compute fracture characteristics in a square punch test for TRIP690 steel. The simulation is scoped to the 0° sheet orientation (case 1) and the results are compared to experimental observations.

## Approach
The simulation uses an uncoupled MMC fracture model: a damage indicator D is accumulated as a function of equivalent plastic strain, stress triaxiality, and Lode angle parameter, integrated through five Simpson points across each shell element thickness. Elements are deleted only when all five integration points reach D=1. The material is TRIP690 represented with von Mises isotropic plasticity and power‑law hardening (A=1275.9 MPa, n=0.2655), together with the reported MMC fracture parameters (C1=0.12, C2=720 MPa, C3=1.095). The finite‑element model represents a 70 mm square punch with 10 mm punch radius, a die radius of 5 mm, and a 150 mm square blank of 1.6 mm thickness. The simulation uses shell elements (S4R‑type), a 1 mm mesh, blank‑holder force of 50 kN, punch velocity of 35 mm/s, a global friction coefficient of 0.17, and mass scaling factor 1000. From the output database you will extract a fracture summary (location, mode, punch travel at first fracture, peak force) and a load‑displacement curve.

## Reproduction target
Implement the MMC damage model in an open‑source finite‑element solver (e.g., CalculiX), set up the square punch deep‑drawing model for case 1 (0° orientation) with the specified geometry and parameters, and run the simulation. From the output, produce:

- `simulation_summary.json`: a JSON object containing the crack initiation location (die radius or punch radius), the fracture mode (flat or slant), the punch travel at first fracture (in mm), and the peak punch force (in N).
- `load_displacement.csv`: a CSV file with columns `punch_displacement_mm` and `punch_force_N` sampled throughout the forming process, including the fracture drop.

These outputs should be consistent with experimental measurements for square punch case 1 of TRIP690 steel.

## Assets

- CalculiX: https://www.calculix.de/

## Workflow steps

### Step 1: Implement MMC damage model in CalculiX
- Role: process
- Action: Implement the uncoupled Modified Mohr‑Coulomb (MMC) damage accumulation model in the open‑source FE solver CalculiX. The model must use von Mises isotropic plasticity with power‑law hardening (A=1275.9 MPa, n=0.2655) and the MMC fracture parameters (C1=0.12, C2=720 MPa, C3=1.095). It must evaluate the damage indicator D via Simpson integration at five through‑thickness points per shell element, and apply a 5‑point element deletion law (element deleted only when all five integration points reach D=1).
- Evidence: none

### Step 2: Run square punch Case 1 simulation
- Role: process
- Action: Build a finite element model of the square punch deep‑drawing test for TRIP690 sheet, case 1 (0° orientation). Use S4R shell elements with 1 mm mesh, rigid punch (70 mm square, radius 10 mm), die (radius 5 mm) and blank‑holder. Set blank‑holder force to 50 kN, punch velocity to 35 mm/s, friction coefficient to 0.17, and apply mass scaling factor 1000. Run the explicit dynamic simulation with the implemented MMC material model and save the complete output database (e.g., CalculiX .frd or .dat files).
- Evidence: none

### Step 3: Extract fracture summary and write simulation_summary.json
- Role: scored (load-bearing)
- Action: Post‑process the simulation output to determine: the location of first element deletion (die radius), the fracture mode (flat), the punch travel at first fracture (mm), and the peak punch force (N). Write these four values to simulation_summary.json.
- Output file: `/app/outputs/simulation_summary.json`
- Format: json
- Contract: {"crack_initiation_location": "string ('die_radius')", "fracture_mode": "string ('flat')", "punch_travel_at_first_fracture_mm": "float", "peak_force_N": "float"}
- Scoring: scored by hidden verifier

### Step 4: Extract load‑displacement curve and write load_displacement.csv
- Role: scored
- Action: From the simulation output, sample the punch reaction force versus punch displacement at regular intervals throughout the process (including the fracture drop) and write the data to load_displacement.csv.
- Output file: `/app/outputs/load_displacement.csv`
- Format: csv
- Contract: columns: punch_displacement_mm, punch_force_N; one row per sampled time step
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_summary.json`
- `/app/outputs/load_displacement.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_summary.json
- path: `/app/outputs/simulation_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Summary of predicted fracture characteristics: crack initiation location, fracture mode, punch travel at first fracture, and peak punch force.
- schema:
  - `type`: object
  - `required`:
    - `crack_initiation_location`: string
    - `fracture_mode`: string
    - `punch_travel_at_first_fracture_mm`: float (mm)
    - `peak_force_N`: float (N)

### load_displacement.csv
- path: `/app/outputs/load_displacement.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Load‑displacement curve sampled from the simulation, used to verify the qualitative shape (monotonic increase, sharp drop at fracture) and consistency with the summary peak force.
- schema:
  - `type`: table
  - `required_columns`: `punch_displacement_mm`, `punch_force_N`
  - `units`:
    - `punch_displacement_mm`: mm
    - `punch_force_N`: N

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "crack_initiation_location": "string",
          "fracture_mode": "string",
          "punch_travel_at_first_fracture_mm": "float (mm)",
          "peak_force_N": "float (N)"
        }
      },
      "description": "Summary of predicted fracture characteristics: crack initiation location, fracture mode, punch travel at first fracture, and peak punch force."
    },
    {
      "file": "load_displacement.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "punch_displacement_mm",
          "punch_force_N"
        ],
        "units": {
          "punch_displacement_mm": "mm",
          "punch_force_N": "N"
        }
      },
      "description": "Load‑displacement curve sampled from the simulation, used to verify the qualitative shape (monotonic increase, sharp drop at fracture) and consistency with the summary peak force."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently reads your `simulation_summary.json` and `load_displacement.csv`. It checks that `crack_initiation_location` and `fracture_mode` match expected values, that `punch_travel_at_first_fracture_mm` and `peak_force_N` fall within generous tolerances, and that the load‑displacement curve shows the correct qualitative shape (monotonic increase to a peak followed by a sharp drop). The reward is a weighted combination of these checks; the main weight is on the punch travel and peak force. Reporting the correct numbers is not enough – the verifier validates the structure and consistency of your outputs.
