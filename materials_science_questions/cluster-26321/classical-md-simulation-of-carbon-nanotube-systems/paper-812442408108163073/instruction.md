# Classical MD Simulation of Water Reorientation in Carbon Nanotubes

## Problem background
Water confined in extremely narrow carbon nanotubes exhibits altered molecular dynamics compared to the bulk liquid. Molecular reorientation — the rotation of individual water molecules with respect to different molecular axes — is a fundamental dynamical property that influences transport and reactivity. Classical molecular dynamics simulations can capture these effects using flexible water models and appropriate wall‑water interactions. This task investigates the reorientational dynamics of water at ambient temperature (298 K) and density (0.83 g/cm³) inside carbon nanotubes of three different radii and compares them with bulk water.

## Approach
The system consists of carbon nanotubes of given chirality and length, with flexible SPC water molecules placed inside at the target density. Wall‑water interactions are modelled with Lennard‑Jones potentials. Equilibrium molecular dynamics simulations are performed at constant temperature using a Berendsen thermostat and Ewald summation for electrostatics. After equilibration, production trajectories are collected. From these trajectories, unit vectors along the molecular dipole, the hydrogen‑hydrogen direction, and the direction perpendicular to the instantaneous molecular plane are computed for each water molecule. The time correlation functions C1(t)=⟨cos θ(t)⟩ and C2(t)=½⟨3 cos²θ(t)−1⟩ are calculated for each vector. The characteristic reorientational times are obtained by integrating these correlation functions, and the dependence on tube radius is investigated.

## Reproduction target
Perform classical molecular dynamics simulations of water confined in (8,8), (10,10), and (12,12) carbon nanotubes and in bulk water at T=298 K and density ρ=0.83 g/cm³. From the production trajectories, compute the Legendre polynomial time correlation functions C1(t) and C2(t) for the molecular dipole, hydrogen‑hydrogen, and perpendicular‑to‑plane unit vectors. Integrate these functions to obtain the reorientational times τ₁ and τ₂ for each system and direction. Present these times to characterize how nanotube confinement affects the reorientational dynamics of water.

## Assets

- GROMACS: https://www.gromacs.org/
- Flexible SPC water model parameters: 10.1016/0167-7322(94)00725-3
- Carbon nanotube Lennard-Jones interaction parameters: 10.1016/S0009-2614(00)01015-0

## Workflow steps

### Step 1: Build simulation systems
- Role: process
- Action: Construct carbon nanotube geometries of chirality (8,8), (10,10), (12,12) with length 7.45 nm and place water molecules at density 0.83 g/cm³ at T=298 K using the flexible SPC water model. Also prepare a bulk water box at the same density. Generate topology and coordinate files for each system.
- Evidence: `/app/outputs/initial_config.gro`

### Step 2: MD equilibration
- Role: process
- Action: For each system, perform 500 ps NVT equilibration at 298 K using a leap‑frog Verlet integrator with 0.5 fs timestep, a Berendsen thermostat, Ewald summation for Coulombics, and the flexible SPC/LJ potentials. Separately equilibrate translational and internal degrees of freedom.
- Evidence: `/app/outputs/equil.log`

### Step 3: MD production run
- Role: process
- Action: Restart from the equilibrated configuration and run 250 ps production MD under the same conditions to collect atomic trajectories (positions and velocities).
- Evidence: `/app/outputs/production.log`

### Step 4: Reorientational correlation functions
- Role: scored (load-bearing)
- Action: From the production trajectories, compute for each system (bulk, (12,12), (10,10), (8,8)) the time correlation functions C1(t)=⟨cos θ(t)⟩ and C2(t)=½⟨3 cos²θ(t)−1⟩ for the three molecular unit vectors: dipole (μ), hydrogen‑hydrogen (HH), and perpendicular‑to‑plane (⊥). Save the time series as a JSON file with arrays of t (ps), C1 and C2 for each vector.
- Output file: `/app/outputs/correlation_functions.json`
- Format: json
- Contract: Top‑level keys 'bulk', 'cnt12_12', 'cnt10_10', 'cnt8_8'. Each contains keys 'dipole', 'hh', 'perp'. Each direction contains 'time' (list of floats, ps), 'C1' (list of floats), 'C2' (list of floats).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/correlation_functions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### correlation_functions.json
- path: `/app/outputs/correlation_functions.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw C1 and C2 Legendre polynomial correlation functions for each water system and each molecular direction.
- schema:
  - `type`: object
  - `required`: `bulk`, `cnt12_12`, `cnt10_10`, `cnt8_8`
  - `additionalProperties`: False
  - `properties`:
    - `bulk`:
      - `type`: object
      - `required`: `dipole`, `hh`, `perp`
      - `properties`:
        - `dipole`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
        - `hh`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
        - `perp`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
    - `cnt12_12`:
      - `type`: object
      - `required`: `dipole`, `hh`, `perp`
      - `properties`:
        - `dipole`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
        - `hh`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
        - `perp`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
    - `cnt10_10`:
      - `type`: object
      - `required`: `dipole`, `hh`, `perp`
      - `properties`:
        - `dipole`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
        - `hh`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
        - `perp`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
    - `cnt8_8`:
      - `type`: object
      - `required`: `dipole`, `hh`, `perp`
      - `properties`:
        - `dipole`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
        - `hh`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`
        - `perp`:
          - `type`: object
          - `required`: `time`, `C1`, `C2`

Notes: The hidden checker will numerically integrate the C1(t) and C2(t) arrays to compute τ1 and τ2 for each system and direction, compare them to hidden reference values from the paper with tolerance, and verify the monotonic ordering τ_bulk > τ_(12,12) > τ_(10,10) > τ_(8,8).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "correlation_functions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "bulk",
          "cnt12_12",
          "cnt10_10",
          "cnt8_8"
        ],
        "additionalProperties": false,
        "properties": {
          "bulk": {
            "type": "object",
            "required": [
              "dipole",
              "hh",
              "perp"
            ],
            "properties": {
              "dipole": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              },
              "hh": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              },
              "perp": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              }
            }
          },
          "cnt12_12": {
            "type": "object",
            "required": [
              "dipole",
              "hh",
              "perp"
            ],
            "properties": {
              "dipole": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              },
              "hh": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              },
              "perp": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              }
            }
          },
          "cnt10_10": {
            "type": "object",
            "required": [
              "dipole",
              "hh",
              "perp"
            ],
            "properties": {
              "dipole": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              },
              "hh": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              },
              "perp": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              }
            }
          },
          "cnt8_8": {
            "type": "object",
            "required": [
              "dipole",
              "hh",
              "perp"
            ],
            "properties": {
              "dipole": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              },
              "hh": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              },
              "perp": {
                "type": "object",
                "required": [
                  "time",
                  "C1",
                  "C2"
                ]
              }
            }
          }
        }
      },
      "description": "Raw C1 and C2 Legendre polynomial correlation functions for each water system and each molecular direction."
    }
  ],
  "notes": "The hidden checker will numerically integrate the C1(t) and C2(t) arrays to compute τ1 and τ2 for each system and direction, compare them to hidden reference values from the paper with tolerance, and verify the monotonic ordering τ_bulk > τ_(12,12) > τ_(10,10) > τ_(8,8)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently integrates the correlation functions you provide to compute τ₁ and τ₂ for each system and direction. The verifier compares your computed values to established reference results and checks whether the reorientational times follow the expected systematic dependence on confinement. Because the raw correlation function data is reprocessed, simply reporting a plausible number is not sufficient; your final reward is based on how well your computed reorientational times agree with the reference and whether the trend across confinement radii is correctly reproduced. The scoring logic and tolerances are not disclosed to you.
