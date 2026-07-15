# Computational Progressive Failure Analysis of a Notched Composite Laminate

## Problem background
Composite laminates under tensile loading can fail through a complex interaction of matrix cracking, delamination, fibre breakage, and shear nonlinearity. Reliable prediction of this progressive failure requires a computational model that captures these coupled damage mechanisms. This task simulates the failure of a notched cross-ply [90/0]_s laminate to quantify how the different failure processes interact and influence the load-bearing capacity.

## Approach
The computational model couples several material descriptions within a plane‑stress finite‑element framework. Fibre failure is represented by a continuum isotropic damage law with exponential softening, regularized by the crack‑band method (characteristic element length derived from element area). In‑plane shear nonlinearity is treated by a phenomenological damage/plasticity model that reproduces stiffness degradation and permanent strain; after the stress‑strain curve reaches its maximum, the model is extended with a perfectly plastic segment to avoid spurious softening. Matrix cracks are introduced as displacement discontinuities via the phantom‑node method: crack initiation follows a stress‑based criterion and the propagation direction is locked to the fibre direction. The cohesive law is a shifted bilinear mixed‑mode law. Delamination between plies is captured by interface elements with a bilinear mixed‑mode cohesive law. The simulations are driven by a dissipation‑based arc‑length solver that can trace the post‑peak equilibrium path.

Two simulations are performed:
- Baseline: all damage mechanisms (matrix cracking, delamination, fibre damage, shear nonlinearity) are active.
- No‑delamination ablation: delamination is disabled by setting the interface elements to perfect bonding or removing them.

The geometry is a half‑symmetry model of a centrally notched [90/0]_s plate. The full plate is 100 mm long, 30 mm wide, and contains a central notch of total length 10 mm with a notch‑root radius of 0.5 mm. Each unidirectional ply is 0.125 mm thick (total laminate thickness 0.5 mm). Remote tensile loading is applied along the plate axis.

Material properties used (from published sources):
- Elastic constants: E1 = 135 GPa, E2 = 9.6 GPa, ν12 = 0.31, G6 = 5.8 GPa.
- Strengths: fibre tensile strength F1t = 1673 MPa, transverse tensile strength (ply level) 60 MPa, in‑situ matrix tensile strength and shear strength both 75 MPa.
- Fracture energies: mode‑I matrix cracking GIc,m = 0.15 N/mm, mode‑II matrix cracking and delamination GIIc,m = GIId = 0.4 N/mm.
- Fibre fracture energy (input value): GIc,f = 50 N/mm.
- Shear nonlinearity constants: C1 = 22, C2 = −22, C3 = 35, C4 = −5.
- Thermal expansion coefficients: α1 = 0 °C⁻¹, α2 = 3×10⁻⁵ °C⁻¹.
- Minimum spacing between matrix cracks: 0.5 mm.

The baseline simulation records the applied displacement, the far‑field averaged stress (load divided by cross‑sectional area), and the length of the traction‑free split crack in the 0° ply. These data become the basis for the scored artifacts.

## Reproduction target
Run the baseline simulation with the parameters above and produce the following two artifacts:
1. Far‑field stress (MPa) versus applied displacement (mm).
2. Split length (mm) in the 0° ply as a function of applied far‑field stress (MPa).

Then run the no‑delamination simulation and record the peak far‑field stress. Collect the peak stresses from both the baseline and the no‑delamination cases and store them as a two‑row table.

The hidden verifier will compute derived quantities from these artifacts to compare against the expected reference; you do not need to extract the metrics yourself, only to provide the raw curves and peak values in the specified formats.

## Assets
No external dataset is required; all geometry and material parameters are provided above. The agent may use any open‑source finite‑element library (e.g., FEniCS, deal.II, or a custom code) together with scientific Python packages (numpy, scipy) to implement the models, assemble the system, and run the simulations.

## Workflow steps

### Step 1: Implement and run baseline finite-element simulation
- Role: process
- Action: Implement the continuum fibre-damage model (isotropic stiffness degradation driven by a state variable based on fibre tensile strain, exponential softening, crack-band regularization with characteristic element length from element area), the shear-nonlinearity model (phenomenological damage/plasticity with perfectly-plastic extension), and cohesive-zone models for matrix cracking (phantom-node with shifted bilinear traction-separation) and delamination (interface elements). Build a plane-stress mesh for the notched [90/0]_s laminate (half-symmetry, linear triangular elements) using the geometry and material parameters from the paper (including G_Ic,f = 50 N/mm). Apply remote tension and follow the equilibrium path with a dissipation‑based arc‑length solver. Record applied displacement, remote stress, and split‑length history.
- Evidence: `/app/outputs/baseline_simulation_log.txt`

### Step 2: Load‑displacement curve
- Role: scored
- Action: From the baseline simulation output, extract the far‑field averaged stress (MPa) and applied displacement (mm) at each recorded step, and write them to load_displacement.csv with columns displacement_mm and stress_MPa, ordered by increasing displacement.
- Output file: `/app/outputs/load_displacement.csv`
- Format: csv
- Contract: Two columns: displacement_mm (float, mm), stress_MPa (float, MPa). Rows ordered by increasing displacement.
- Scoring: scored by hidden verifier

### Step 3: Split‑length evolution
- Role: scored (load-bearing)
- Action: From the baseline simulation, extract the length of the traction‑free matrix crack in the 0° ply (split length, mm) and the corresponding applied far‑field stress (MPa), and write them to split_length.csv with columns stress_MPa and split_length_mm, ordered by increasing stress.
- Output file: `/app/outputs/split_length.csv`
- Format: csv
- Contract: Two columns: stress_MPa (float, MPa), split_length_mm (float, mm). Rows ordered by increasing stress.
- Scoring: scored by hidden verifier

### Step 4: Run no‑delamination simulation
- Role: process
- Action: Repeat the same finite‑element model setup, but disable delamination (set interface elements to perfect bonding or remove them). Run the simulation under the same remote tension and arc‑length control, and record the stress‑displacement history and the peak far‑field stress.
- Evidence: `/app/outputs/no_delam_simulation_log.txt`

### Step 5: Ablation peak loads
- Role: scored
- Action: Collect the peak far‑field stresses from the baseline and no‑delamination simulations, and write ablation_peak_loads.csv with columns case (either 'baseline' or 'no_delamination') and peak_stress_MPa (float, MPa). Include exactly two rows, one for each case.
- Output file: `/app/outputs/ablation_peak_loads.csv`
- Format: csv
- Contract: Two columns: case (string, 'baseline' or 'no_delamination'), peak_stress_MPa (float, MPa). Exactly two rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/load_displacement.csv`
- `/app/outputs/split_length.csv`
- `/app/outputs/ablation_peak_loads.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### load_displacement.csv
- path: `/app/outputs/load_displacement.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Far‑field stress vs. displacement from the full simulation; checker recomputes the maximum stress and compares it to the paper‑reported value within a tolerance.
- schema:
  - `type`: table
  - `required_columns`:
    - `name`: displacement_mm
    - `type`: float
    - `unit`: mm
    - `name`: stress_MPa
    - `type`: float
    - `unit`: MPa
  - `description`: Rows in order of increasing displacement.

### split_length.csv
- path: `/app/outputs/split_length.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Split length vs. applied stress; checker finds the stress at which split length first reaches a threshold and compares to the paper‑reported value within a tolerance.
- schema:
  - `type`: table
  - `required_columns`:
    - `name`: stress_MPa
    - `type`: float
    - `unit`: MPa
    - `name`: split_length_mm
    - `type`: float
    - `unit`: mm
  - `description`: Rows ordered by increasing stress.

### ablation_peak_loads.csv
- path: `/app/outputs/ablation_peak_loads.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Peak stresses from the two simulations; checker computes the ratio baseline_peak / no_delamination_peak and checks it lies within the paper‑reported range.
- schema:
  - `type`: table
  - `required_columns`:
    - `name`: case
    - `type`: string
    - `enum`: `baseline`, `no_delamination`
    - `name`: peak_stress_MPa
    - `type`: float
    - `unit`: MPa

Notes: All scored CSVs contain raw simulation data that the checker recomputes to extract the relevant quantities (max stress, split-length threshold stress, peak ratio). The agent must implement the constitutive models and run the FE simulations; no pre‑computed artifacts are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "load_displacement.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          {
            "name": "displacement_mm",
            "type": "float",
            "unit": "mm"
          },
          {
            "name": "stress_MPa",
            "type": "float",
            "unit": "MPa"
          }
        ],
        "description": "Rows in order of increasing displacement."
      },
      "description": "Far‑field stress vs. displacement from the full simulation; checker recomputes the maximum stress and compares it to the paper‑reported value within a tolerance."
    },
    {
      "file": "split_length.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          {
            "name": "stress_MPa",
            "type": "float",
            "unit": "MPa"
          },
          {
            "name": "split_length_mm",
            "type": "float",
            "unit": "mm"
          }
        ],
        "description": "Rows ordered by increasing stress."
      },
      "description": "Split length vs. applied stress; checker finds the stress at which split length first reaches a threshold and compares to the paper‑reported value within a tolerance."
    },
    {
      "file": "ablation_peak_loads.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          {
            "name": "case",
            "type": "string",
            "enum": [
              "baseline",
              "no_delamination"
            ]
          },
          {
            "name": "peak_stress_MPa",
            "type": "float",
            "unit": "MPa"
          }
        ]
      },
      "description": "Peak stresses from the two simulations; checker computes the ratio baseline_peak / no_delamination_peak and checks it lies within the paper‑reported range."
    }
  ],
  "notes": "All scored CSVs contain raw simulation data that the checker recomputes to extract the relevant quantities (max stress, split-length threshold stress, peak ratio). The agent must implement the constitutive models and run the FE simulations; no pre‑computed artifacts are provided."
}
```

## How you are scored
A hidden verifier will independently read your three output CSV files. It will compute:
- The maximum far‑field stress from the load‑displacement curve.
- The applied stress at which the split length first reaches a fixed reference value from the split‑length evolution.
- The ratio of the baseline peak stress to the no‑delamination peak stress from the ablation file.

Each computed quantity is compared against a hidden gold using tolerances that account for the spread expected from a re‑implementation with a different finite‑element code and solver settings. The final reward is a weighted sum of these three checks. Submitting the correct raw simulation data is essential; simply reporting a guessed number is not sufficient.
