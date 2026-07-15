# Graphene Nanoribbon Wrinkling and Nanoindentation via Molecular Dynamics

## Problem background
Graphene nanoribbons (GNRs) are atomically thin strips of graphene that exhibit unique mechanical properties depending on their edge chirality (armchair or zigzag) and shape (planar, convex, or concave). Under boundary confinement, curved GNRs can develop out-of-plane wrinkles, which influence their mechanical response. Molecular dynamics (MD) simulations allow investigation of these phenomena at the atomic scale. In this task, we aim to reproduce MD simulations of curved and planar GNRs to determine the formation of wrinkles and to measure their contact stiffness during nanoindentation. Specifically, we will examine how chirality and curvature affect wrinkle formation and contact stiffness.

## Approach
The approach is to construct atomic-scale models of monolayer GNRs with armchair and zigzag edges, with width 10 nm and curvature radius 5 nm for curved geometries. Fixed boundary atoms and thermal control atoms are defined. A rigid single-walled carbon nanotube (SWCNT) indenter is built. MD simulations are performed using LAMMPS, an open-source MD code. The Tersoff many-body potential describes carbon-carbon interactions within the graphene, while the Lennard-Jones potential models the interaction between the GNR and the indenter. The system is equilibrated in a constant-temperature, constant-volume (NTV) ensemble at 300 K with a 1 fs timestep. After equilibration, the out-of-plane atomic positions of curved GNRs are analyzed to detect any periodic wrinkle patterns. Subsequently, nanoindentation is simulated by driving the SWCNT indenter into the GNR at a constant velocity of 10 m/s, recording the force on the indenter versus its displacement. Contact stiffness is computed from the slope of the linear elastic region of the force-displacement curve. The complete workflow consists of model building, equilibration, indentation, and post-processing analysis.

## Reproduction target
For a GNR width of 10 nm, curvature radius R = 5 nm, temperature 300 K, and indentation velocity 10 m/s:
1. Determine whether periodic out-of-plane wrinkles are present in curved armchair and curved zigzag GNRs after equilibration, and measure the wrinkle wavelength (if present).
2. Compute contact stiffness (N/m) for convex, concave, and planar GNRs with both armchair and zigzag edges. Compare the stiffness values to assess the relative ordering between armchair and zigzag GNRs, and between convex and concave geometries.
All outputs must be generated from the MD simulations and analysis; no pre-computed results may be used.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/download.html

## Workflow steps

### Step 1: Build atomic models
- Role: process
- Action: Build atomic models for convex, concave, and planar monolayer graphene nanoribbons with both armchair and zigzag edge orientations, width 10 nm, curvature radius R=5 nm. Define fixed boundary atoms and thermostat atoms. Build a rigid closed-edge SWCNT (10,10) indenter model.
- Evidence: none

### Step 2: MD equilibration for wrinkling
- Role: process
- Action: Run MD simulation for each curved GNR model (armchair and zigzag) at 300 K using Tersoff potential for graphene, NTV ensemble, 1 fs timestep, to equilibrate and observe wrinkle formation. No indenter at this stage.
- Evidence: none

### Step 3: Analyze wrinkling
- Role: scored (load-bearing)
- Action: From the final equilibrium atomic positions of curved armchair and zigzag GNRs, determine presence of periodic out-of-plane wrinkles and measure wavelength (nm). Output results to wrinkling_analysis.json.
- Output file: `/app/outputs/wrinkling_analysis.json`
- Format: json
- Contract: {"armchair": {"wrinkles_present": true/false, "wavelength_nm": number or null}, "zigzag": {"wrinkles_present": true/false, "wavelength_nm": number or null}}
- Scoring: scored by hidden verifier

### Step 4: Nanoindentation MD runs
- Role: process
- Action: For each equilibrated GNR model (convex, concave, planar, armchair and zigzag), perform nanoindentation with the rigid SWCNT indenter at 10 m/s loading rate, 300 K. Use Tersoff potential for graphene, Lennard-Jones for GNR-indenter interaction, NTV ensemble, 1 fs timestep. Record force on indenter vs. displacement as intermediate evidence.
- Evidence: `/app/outputs/force_displacement.csv`

### Step 5: Compute contact stiffness
- Role: scored (load-bearing)
- Action: For each simulation, compute contact stiffness from the linear elastic region of the force-displacement curve (e.g., slope over an appropriate depth range). Output results to contact_stiffness.csv.
- Output file: `/app/outputs/contact_stiffness.csv`
- Format: csv
- Contract: geometry,chirality,contact_stiffness_Nm
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/wrinkling_analysis.json`
- `/app/outputs/contact_stiffness.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### wrinkling_analysis.json
- path: `/app/outputs/wrinkling_analysis.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Wrinkle analysis results for curved armchair and zigzag GNRs at R=5nm, T=300K. Contains fields 'wrinkles_present' (boolean) and 'wavelength_nm' (number or null) for each chirality.
- schema:
  - `type`: object
  - `properties`:
    - `armchair`:
      - `type`: object
      - `properties`:
        - `wrinkles_present`:
          - `type`: boolean
        - `wavelength_nm`:
          - `type`: `number`, `null`
      - `required`: `wrinkles_present`, `wavelength_nm`
    - `zigzag`:
      - `type`: object
      - `properties`:
        - `wrinkles_present`:
          - `type`: boolean
        - `wavelength_nm`:
          - `type`: `number`, `null`
      - `required`: `wrinkles_present`, `wavelength_nm`
  - `required`: `armchair`, `zigzag`

### contact_stiffness.csv
- path: `/app/outputs/contact_stiffness.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Contact stiffness values for each GNR geometry (convex, concave, planar) and chirality (armchair, zigzag). Columns: geometry, chirality, contact_stiffness_Nm (N/m). Each row corresponds to one configuration at R=5nm, T=300K, v=10m/s.
- schema:
  - `type`: table
  - `required_columns`: `geometry`, `chirality`, `contact_stiffness_Nm`
  - `units`:
    - `contact_stiffness_Nm`: N/m

Notes: Only the two outputs above are scored. The force_displacement.csv intermediate is not scored but serves as evidence that the nanoindentation simulation was executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "wrinkling_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "armchair": {
            "type": "object",
            "properties": {
              "wrinkles_present": {
                "type": "boolean"
              },
              "wavelength_nm": {
                "type": [
                  "number",
                  "null"
                ]
              }
            },
            "required": [
              "wrinkles_present",
              "wavelength_nm"
            ]
          },
          "zigzag": {
            "type": "object",
            "properties": {
              "wrinkles_present": {
                "type": "boolean"
              },
              "wavelength_nm": {
                "type": [
                  "number",
                  "null"
                ]
              }
            },
            "required": [
              "wrinkles_present",
              "wavelength_nm"
            ]
          }
        },
        "required": [
          "armchair",
          "zigzag"
        ]
      },
      "description": "Wrinkle analysis results for curved armchair and zigzag GNRs at R=5nm, T=300K. Contains fields 'wrinkles_present' (boolean) and 'wavelength_nm' (number or null) for each chirality."
    },
    {
      "file": "contact_stiffness.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "geometry",
          "chirality",
          "contact_stiffness_Nm"
        ],
        "units": {
          "contact_stiffness_Nm": "N/m"
        }
      },
      "description": "Contact stiffness values for each GNR geometry (convex, concave, planar) and chirality (armchair, zigzag). Columns: geometry, chirality, contact_stiffness_Nm (N/m). Each row corresponds to one configuration at R=5nm, T=300K, v=10m/s."
    }
  ],
  "notes": "Only the two outputs above are scored. The force_displacement.csv intermediate is not scored but serves as evidence that the nanoindentation simulation was executed."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that reads the two required output files: wrinkling_analysis.json and contact_stiffness.csv. First, the format and schema of each file are checked (compliance with the output contract). Then, for wrinkling analysis, the verifier assesses whether the wrinkle presence and wavelength values are physically consistent with MD simulation results for the given conditions. For contact stiffness, the verifier checks that the reported values are internally consistent with the geometry and chirality of each configuration (e.g., by evaluating monotonic trends or ratios). The verifier combines these component scores into a final reward between 0 and 1. Note that simply copying numeric values from any external source without performing the simulation will not yield outputs that pass the consistency checks built into the verifier. You must execute the workflow steps and produce the outputs from your own MD runs and analysis.
