# Finite Element Modelling of Electrochemical‑Poroelastic Response in Conducting Polymers

## Problem background
Conducting polymers such as polypyrrole undergo volume changes when ions are inserted or removed, making them attractive for soft actuators. These volume changes arise from two coupled phenomena: a passive poroelastic fluid flow driven by pressure gradients, and an active electrochemical insertion/de-insertion of ions under an applied electric current. Understanding the time evolution of internal fluid pressure, solid stress, and charge distribution is essential for designing polymer actuators, but requires solving coupled mechanical–electrochemical–transport equations. This task targets the computational reproduction of the transient poroelastic relaxation and the active cation‑insertion response of a polypyrrole membrane, producing the stress and pressure histories that characterise the actuator's behaviour. The membrane geometry (used for both passive and active cases) is a rectangular film with length along the ionic transport direction (x) = 0.0175 m, width (y) = 0.00585 m, and height (z) = 0.00585 m, yielding cross‑sectional area Sₓ = 34.2×10⁻⁶ m².

## Approach
The method extends Biot's poroelasticity with Onsager‑like relations to derive a coupled system of equations: a three‑dimensional stiffness equation for the solid, a Poisson equation for fluid pressure, an evolution equation for the volumetric strain rate, and a one‑dimensional ionic transport equation that governs the movement of cations. The resulting field equations are discretised by the finite element method. Eight‑node hexahedral elements are used for the 3D poroelastic domain, and line elements for the 1D ionic transport. The solver employs a weakly‑coupled sequential time‑stepping scheme: the ionic transport equation is solved first (it is uncoupled from the mechanical response), then the volumetric strain rate, the pressure, and the displacement fields are updated in sequence at each small time step.
For the passive poroelastic behaviour, an initial strain is applied to the membrane, and the transient solver tracks the relaxation of the average internal fluid pressure, the average solid stress, and the average total stress over time. For the active electrochemical‑poroelastic behaviour, a step‑wise electric current pattern is imposed across the membrane/electrolyte, and the solver computes the resulting pressure evolution at the membrane centre and the spatial distribution of electric charge density.

## Reproduction target
Produce three scored artifacts that characterise the polypyrrole membrane response:
1) The time histories of the average fluid pressure, average solid stress, and average total stress during passive poroelastic stress relaxation, using the membrane geometry and material parameters specified in the workflow.
2) The time evolution of the pressure at the membrane centre during active cation insertion (case 3, 6 s step current), using the same poroelastic parameters plus the additional electrochemical constants.
3) The spatial charge density profile across the membrane at the end of the current application (t = 6 s) for the same active insertion case.
All outputs must be written to CSV files with the exact schemas and units described in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Build Finite‑Element Solver
- Role: process
- Action: Implement a finite‑element solver for the coupled poroelastic‑electrochemical equations using the three‑dimensional stiffness equation for poroelastic solids, Poisson’s equation for pressure, the evolution equation of volumetric strain rate, and the one‑dimensional ionic transportation equation. Use eight‑node hexahedral elements for the 3D poroelastic domain and line elements for the 1D ionic transport, with a weakly‑coupled sequential time‑stepping scheme.
- Evidence: none

### Step 2: Simulate Passive Poroelastic Stress Relaxation
- Role: scored (load-bearing)
- Action: Use the membrane dimensions (length x = 0.0175 m, width y = 0.00585 m, height z = 0.00585 m). Apply an initial uniform strain e₀ = 0.00340909 in the z‑direction. Set boundary conditions: all external faces are traction‑free for the solid, and fluid pressure is fixed at zero (ambient) on all external faces. Run the transient poroelastic solver with passive material parameters (E=1290 MPa, ν=0.412, β=0.108, f=1.29×10²⁰ Ns/m⁴, time step Δt=0.005 s). Record the time evolution of the average internal fluid pressure, average solid stress, and average total stress.
- Output file: `/app/outputs/passive_time_histories.csv`
- Format: csv
- Contract: time (s), avg_pressure (Pa), solid_stress (Pa), total_stress (Pa)
- Scoring: scored by hidden verifier

### Step 3: Run Active Cation Insertion Simulation
- Role: process
- Action: Use the coupled solver with the same membrane geometry (length x = 0.0175 m, width y = 0.00585 m, height z = 0.00585 m). Apply the step‑wise current pattern of case 3: constant current i = 0.05 A from t = 0 to t = 6 s, with the membrane side negative and the electrolyte side positive; after t = 6 s the current is zero. Use active material parameters (η₁=1.18e-11 Ns/m², k=1.38e-23 Nm/K, T=293 K, e=1.6e-19 C, εₑ=2.8e-3 C²/Nm², Δt=5e-4 s, h=2×10⁻⁶ m, Sₓ=34.2e-6 m², Nₐ=6.02e23 /mol) together with the poroelastic parameters from the passive case. Write the full state time history to an intermediate HDF5 file.
- Evidence: `/app/outputs/simulation_case3_state.hdf5`

### Step 4: Extract Pressure at Membrane Center for Case 3
- Role: scored (load-bearing)
- Action: From the intermediate simulation output, extract the pressure at the membrane center as a function of time and write to a CSV file.
- Output file: `/app/outputs/active_pressure_case3.csv`
- Format: csv
- Contract: time (s), pressure (Pa)
- Scoring: scored by hidden verifier

### Step 5: Extract Charge Density Profile at t=6 s for Case 3
- Role: scored (load-bearing)
- Action: From the intermediate simulation output, extract the spatial distribution of electric charge density at the end of the current application (t = 6 s) and write to a CSV file.
- Output file: `/app/outputs/active_charge_density_case3.csv`
- Format: csv
- Contract: x (m), charge_density (C/m³)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/passive_time_histories.csv`
- `/app/outputs/active_pressure_case3.csv`
- `/app/outputs/active_charge_density_case3.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### passive_time_histories.csv
- path: `/app/outputs/passive_time_histories.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time histories of average fluid pressure, solid stress, and total stress during passive poroelastic stress relaxation.
- schema:
  - `type`: table
  - `required_columns`: `time`, `avg_pressure`, `solid_stress`, `total_stress`
  - `units`:
    - `time`: s
    - `avg_pressure`: Pa
    - `solid_stress`: Pa
    - `total_stress`: Pa

### active_pressure_case3.csv
- path: `/app/outputs/active_pressure_case3.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pressure evolution at the membrane centre during active cation insertion (case 3).
- schema:
  - `type`: table
  - `required_columns`: `time`, `pressure`
  - `units`:
    - `time`: s
    - `pressure`: Pa

### active_charge_density_case3.csv
- path: `/app/outputs/active_charge_density_case3.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spatial distribution of electric charge density at t=6 s for the active cation insertion case.
- schema:
  - `type`: table
  - `required_columns`: `x`, `charge_density`
  - `units`:
    - `x`: m
    - `charge_density`: C/m^3

Notes: The bipolymer strip bending simulation is excluded because the current pattern and several physical constants were not fully specified in the paper. Only the passive relaxation and active cation insertion (case 3) are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "passive_time_histories.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "avg_pressure",
          "solid_stress",
          "total_stress"
        ],
        "units": {
          "time": "s",
          "avg_pressure": "Pa",
          "solid_stress": "Pa",
          "total_stress": "Pa"
        }
      },
      "description": "Time histories of average fluid pressure, solid stress, and total stress during passive poroelastic stress relaxation."
    },
    {
      "file": "active_pressure_case3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "pressure"
        ],
        "units": {
          "time": "s",
          "pressure": "Pa"
        }
      },
      "description": "Pressure evolution at the membrane centre during active cation insertion (case 3)."
    },
    {
      "file": "active_charge_density_case3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "charge_density"
        ],
        "units": {
          "x": "m",
          "charge_density": "C/m^3"
        }
      },
      "description": "Spatial distribution of electric charge density at t=6 s for the active cation insertion case."
    }
  ],
  "notes": "The bipolymer strip bending simulation is excluded because the current pattern and several physical constants were not fully specified in the paper. Only the passive relaxation and active cation insertion (case 3) are scored."
}
```

## How you are scored
A hidden verifier inspects each scored output file independently and compares the computed values against reference gold values derived from the paper's published data, using pre‑set tolerances appropriate for a numerical re‑implementation. The verifier checks the passive time histories at selected time points, the active pressure evolution (pressure rise during current application and relaxation afterwards), and the shape and magnitude of the charge density profile. The stage scores are combined by weight to yield a final reward between 0 and 1. Reporting the paper's numbers without producing the corresponding simulation outputs will be detected by the verifier and will not receive credit.
