# Shell Buckling Scaling and Transition Aspect Ratio in Single-Wall Carbon Nanotubes

## Problem background
Single-wall carbon nanotubes (SWNTs) under axial compression exhibit different mechanical responses depending on their length-to-diameter aspect ratio. For short tubes, shell buckling is expected, with critical strain depending on the tube diameter. As the aspect ratio increases, the deformation mode may transition to a rod-like Euler buckling. Determining the diameter scaling of the shell-buckling critical strain and locating the aspect ratio at which the shell-to-rod transition occurs are important for understanding the mechanics of nanoscale structures. This task aims to computationally reproduce these two relationships using classical molecular dynamics simulations.

## Approach
Use classical molecular dynamics (MD) with the Tersoff potential for covalent C–C bonds and a Lennard-Jones potential (σ=3.89 Å, ε=0.005 eV) for non-bonded van der Waals interactions. Construct armchair (N,N) SWNT atomic models. For the diameter-scaling part, build tubes with (4,4), (10,10), and (20,20) chirality, all at a small fixed aspect ratio of approximately μ ≈ 5. For the transition study, build (20,20) tubes at several lengths to cover aspect ratios from μ ≈ 5 to μ ≈ 30. In each simulation, fix the outermost atoms at both ends, impose a displacement-controlled compressive loading at a rate on the order of 5 m/s, and begin from a near-zero temperature configuration. The initiation of buckling can be identified, for example, by a sharp increase in potential energy or a drop in stress. Extract the critical compressive strain at buckling for each tube and analyze the relationship between critical strain and tube diameter, and between critical strain and aspect ratio.

## Reproduction target
1) For armchair SWNTs (4,4), (10,10), and (20,20) at a constant aspect ratio of approximately μ ≈ 5, determine the critical compressive strain at which shell buckling initiates. Verify whether the critical strain exhibits an inverse proportionality with tube diameter. 2) For the (20,20) SWNT, simulate several tube lengths yielding aspect ratios from about 5 to 30, determine the critical strain for each, and identify the aspect ratio at which the critical strain reaches a minimum — the transition point from shell buckling to Euler buckling. Report both the full curve of critical strain versus aspect ratio and the estimated transition aspect ratio.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- Tersoff potential for carbon: lammps

## Workflow steps

### Step 1: Generate SWNT atomic models
- Role: process
- Action: Construct armchair (N,N) SWNT initial configurations for N=4,10,20 with specified lengths. For diameter scaling, build tubes with aspect ratio μ≈5. For the aspect ratio scan, build a (20,20) tube at several lengths yielding μ from 5 to 30. Use standard C–C bond length and tube geometry.
- Evidence: `/app/outputs/tube_models.tar.gz`

### Step 2: Run MD compression simulations
- Role: process
- Action: For each tube, perform classical MD with the Tersoff potential for C–C bonds and Lennard‑Jones for van der Waals (σ=3.89 Å, ε=0.005 eV). Fix the outermost atoms at both ends, apply a displacement‑controlled compressive loading at ~5 m/s, and initialize at near‑zero temperature. Output trajectories and stress-strain data.
- Evidence: `/app/outputs/md_outputs.tar.gz`

### Step 3: Extract critical strain vs. diameter
- Role: scored (load-bearing)
- Action: From the MD simulations of tubes (4,4), (10,10), (20,20) at μ≈5, determine the compressive strain at which buckling initiates (e.g., by a sharp rise in potential energy or drop in stress). Record the critical strain ε_S for each tube. Output a JSON file with fields: tube_label, diameter_nm, critical_strain.
- Output file: `/app/outputs/critical_strain_diameter.json`
- Format: json
- Contract: A JSON array of objects, each with keys "tube_label" (string, e.g., "(4,4)"), "diameter_nm" (float, tube diameter in nm), "critical_strain" (float, dimensionless compressive strain at buckling).
- Scoring: scored by hidden verifier

### Step 4: Extract critical strain vs. aspect ratio and transition
- Role: scored (load-bearing)
- Action: For the (20,20) tube simulated at various lengths covering μ from 5 to 30, determine the critical compressive strain for buckling at each aspect ratio. Identify the aspect ratio at which the critical strain is minimal (the shell‑to‑Euler transition). Output a JSON file with the full curve and the estimated transition aspect ratio.
- Output file: `/app/outputs/critical_strain_aspect_ratio.json`
- Format: json
- Contract: A JSON object with two keys: "curve" – an array of objects with keys "aspect_ratio" (float) and "critical_strain" (float), ordered by increasing aspect ratio; "transition_aspect_ratio" – a float representing the aspect ratio where the critical strain reaches a minimum.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_strain_diameter.json`
- `/app/outputs/critical_strain_aspect_ratio.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_strain_diameter.json
- path: `/app/outputs/critical_strain_diameter.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Critical compressive strains for shell buckling of armchair SWNTs of different diameters at constant small aspect ratio (~5). Checker compares against hidden reference values and verifies ε_S ∝ 1/d trend.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `tube_label`, `diameter_nm`, `critical_strain`
    - `properties`:
      - `tube_label`:
        - `type`: string
      - `diameter_nm`:
        - `type`: number
      - `critical_strain`:
        - `type`: number

### critical_strain_aspect_ratio.json
- path: `/app/outputs/critical_strain_aspect_ratio.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Critical strain vs. aspect ratio curve for a (20,20) SWNT and the estimated shell-to-Euler transition aspect ratio. Checker compares to hidden gold values and verifies the curve has a minimum near the expected transition.
- schema:
  - `type`: object
  - `required`: `curve`, `transition_aspect_ratio`
  - `properties`:
    - `curve`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `aspect_ratio`, `critical_strain`
        - `properties`:
          - `aspect_ratio`:
            - `type`: number
          - `critical_strain`:
            - `type`: number
    - `transition_aspect_ratio`:
      - `type`: number

Notes: The wire-like folding regime is omitted because it requires aspect ratios >100 and yields only qualitative observations. The core verifiable claims are the shell buckling scaling and the shell-to-rod transition.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_strain_diameter.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "tube_label",
            "diameter_nm",
            "critical_strain"
          ],
          "properties": {
            "tube_label": {
              "type": "string"
            },
            "diameter_nm": {
              "type": "number"
            },
            "critical_strain": {
              "type": "number"
            }
          }
        }
      },
      "description": "Critical compressive strains for shell buckling of armchair SWNTs of different diameters at constant small aspect ratio (~5). Checker compares against hidden reference values and verifies ε_S ∝ 1/d trend."
    },
    {
      "file": "critical_strain_aspect_ratio.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "curve",
          "transition_aspect_ratio"
        ],
        "properties": {
          "curve": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "aspect_ratio",
                "critical_strain"
              ],
              "properties": {
                "aspect_ratio": {
                  "type": "number"
                },
                "critical_strain": {
                  "type": "number"
                }
              }
            }
          },
          "transition_aspect_ratio": {
            "type": "number"
          }
        }
      },
      "description": "Critical strain vs. aspect ratio curve for a (20,20) SWNT and the estimated shell-to-Euler transition aspect ratio. Checker compares to hidden gold values and verifies the curve has a minimum near the expected transition."
    }
  ],
  "notes": "The wire-like folding regime is omitted because it requires aspect ratios >100 and yields only qualitative observations. The core verifiable claims are the shell buckling scaling and the shell-to-rod transition."
}
```

## How you are scored
Your outputs are scored by a hidden verifier that independently evaluates each scored artifact. The verifier checks whether the reported critical strains are physically plausible, whether the diameter scaling follows the expected inverse trend, whether the critical strain versus aspect ratio curve has a clear minimum, and whether the estimated transition aspect ratio falls within an acceptable range. The scoring rewards correct physical behavior derived from your MD simulations; exact reproduction of any specific numeric value from a reference is not required, but the outputs must reflect a genuine re‑run of the described workflow. Each scored artifact contributes a weighted portion to the final reward. Simply copying reported values without running the simulations will not pass.
