# Formation of Stable Water Bridge between Disjoint Nanotubes with Single-File Chains of Water

## Problem background
Water transport through carbon nanotubes (CNTs) is important for desalination, drug delivery, and nanofluidic devices. When two disjoint CNTs are separated by a small gap, a water bridge can form, enabling fluid flow between them. This task studies the formation, stability, and flow efficiency of such bridges when the CNTs are small enough to allow only single-file water chains, using molecular dynamics (MD) simulations.

## Approach
Molecular dynamics simulations are performed with the LAMMPS package using the TIP3P water model and AMBER96 Lennard-Jones parameters for water–carbon interactions (ε_O-C = 478.4 J/mol, σ_O-C = 3.28 Å). The system consists of two water reservoirs bounded by graphene sheets (44.3×42.6 Å²) separated by 98 Å, each initially containing 2002 water molecules. Two coaxial (6,6) CNTs (diameter 0.806 nm) are separated by a gap of length l_g and connect to the reservoirs. A pressure difference ΔP is applied via piston graphene sheets (low-pressure side at 1 atm, high-pressure side adjusted to achieve the target ΔP). Temperature is maintained at 300 K with a Nosé–Hoover thermostat (excluding water inside the CNTs and within 5 Å of the entrances). After a short equilibration with capped CNTs, the caps are removed and production MD trajectories are collected. For each combination of gap length (8, 13, 18 Å) and pressure drop (3200, 3700, 4200 atm), the mean flow rate Q_L (molecules/ns) entering the low-pressure CNT is computed from the trajectories, averaged over a 10 ns steady-state window. The pressure drop that yields the maximum Q_L for each bridge-forming gap length is then identified.

## Reproduction target
Compute the mean water flow rate Q_L (molecules/ns) entering the low-pressure-side CNT for gap lengths l_g = 8, 13, and 18 Å at pressure drops ΔP = 3200, 3700, and 4200 atm. Based on the computed Q_L, determine whether a stable water bridge forms for each condition, and identify the pressure drop that maximizes Q_L for each bridge-forming gap length. Report all results in flow_results.json.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov

## Workflow steps

### Step 1: System Construction
- Role: process
- Action: Build the initial atomic configuration and LAMMPS input files for each combination of gap length (8, 13, 18 Å) and target pressure drop (3200, 3700, 4200 atm) using the specified geometry (two graphene reservoirs, two coaxial (6,6) CNTs, TIP3P water) and force-field parameters (AMBER96 LJ, PPPM).
- Evidence: `/app/outputs/lammps_input.tar.gz`

### Step 2: Equilibration MD
- Role: process
- Action: For each (l_g, ΔP) combination, run MD with caps on the CNTs for 0.2 ns using the Nosé-Hoover thermostat at 300 K (excluding molecules inside CNTs and within 5 Å of entrances) and applying the target pressure drop via piston graphene sheets.
- Evidence: `/app/outputs/equilibration_done.log`

### Step 3: Production MD
- Role: process
- Action: Remove caps from the CNTs and continue MD for up to 15 ns under the same thermostat and pressure conditions, saving atomic trajectories for each (l_g, ΔP) combination.
- Evidence: `/app/outputs/production_trajectories.tar.gz`

### Step 4: Flow Rate Analysis
- Role: scored (load-bearing)
- Action: From the production trajectories, compute the mean net number of water molecules entering the low-pressure CNT per nanosecond (Q_L) for each (l_g, ΔP) condition, averaged over a 10 ns steady-state window. Determine the pressure drop that yields the maximum Q_L for l_g = 8 and 13 Å. Output the results as flow_results.json.
- Output file: `/app/outputs/flow_results.json`
- Format: json
- Contract: {"results": [{"gap": "float (Å)", "dP": "float (atm)", "Q_L": "float (molecules/ns)"}], "peak_dP": {"8": "float (atm)", "13": "float (atm)"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/flow_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### flow_results.json
- path: `/app/outputs/flow_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mean water flow rate Q_L into the low-pressure CNT for each (l_g, ΔP) combination, and the ΔP giving maximum Q_L for each gap length.
- schema:
  - `type`: object
  - `properties`:
    - `results`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `gap`:
            - `type`: number
          - `dP`:
            - `type`: number
          - `Q_L`:
            - `type`: number
        - `required`: `gap`, `dP`, `Q_L`
    - `peak_dP`:
      - `type`: object
      - `properties`:
        - `8`:
          - `type`: number
        - `13`:
          - `type`: number
      - `required`: `8`, `13`
  - `required`: `results`, `peak_dP`

Notes: The checker compares the reported Q_L values and peak ΔP against hidden paper-derived references with tolerances. The agent must run the full MD pipeline to compute these values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "flow_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "gap": {
                  "type": "number"
                },
                "dP": {
                  "type": "number"
                },
                "Q_L": {
                  "type": "number"
                }
              },
              "required": [
                "gap",
                "dP",
                "Q_L"
              ]
            }
          },
          "peak_dP": {
            "type": "object",
            "properties": {
              "8": {
                "type": "number"
              },
              "13": {
                "type": "number"
              }
            },
            "required": [
              "8",
              "13"
            ]
          }
        },
        "required": [
          "results",
          "peak_dP"
        ]
      },
      "description": "Mean water flow rate Q_L into the low-pressure CNT for each (l_g, ΔP) combination, and the ΔP giving maximum Q_L for each gap length."
    }
  ],
  "notes": "The checker compares the reported Q_L values and peak ΔP against hidden paper-derived references with tolerances. The agent must run the full MD pipeline to compute these values."
}
```

## How you are scored
A hidden verifier reads your flow_results.json and compares your reported Q_L values and identified pressure drop of maximum flow against reference values derived from the original study. Most of the score (80%) comes from how many (gap length, pressure drop) conditions meet the hidden flow rate criteria; the remaining 20% comes from correctly identifying the pressure drop that maximizes Q_L for each bridge-forming gap length. Simply reproducing the paper’s numbers without running the full MD pipeline is not sufficient—the score is computed from your reported values, but only the verifier knows the acceptance thresholds. No tolerances or gold values are disclosed here.
