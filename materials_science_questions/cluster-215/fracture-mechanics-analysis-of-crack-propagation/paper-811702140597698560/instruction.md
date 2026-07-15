# Parametric Finite Element Analysis of Stress Triaxiality in Side-Grooved Tension Specimens

## Problem background
Stress triaxiality has a major influence on crack‑driven phenomena such as fatigue crack growth, diffusion, and ductile fracture. Isolating pure plane strain conditions is crucial for fundamental material studies but is difficult to achieve experimentally. This work proposes an optimized side‑grooved M(T) specimen geometry to yield a nearly uniform plane strain state along the crack front. The aim is to determine, via parametric three‑dimensional finite element simulations, the portion of thickness (pt) where the stress triaxiality parameter h exceeds 0.97 as a function of the groove radius r, groove depth b, and reduced thickness t. The objective is to identify geometric combinations that produce a high fraction of thickness in a nearly pure plane strain condition.

## Approach
The analysis is performed with linear elastic finite element models of the side‑grooved middle‑crack tension (M(T)) specimen. Symmetry is exploited to model only one eighth of the specimen. The mesh uses 20‑node hexahedral isoparametric elements with quarter‑point singular elements around the crack front. A spider‑web pattern with three concentric rings refines the crack tip, and 50 through‑thickness layers are graded from the surface using a geometric progression (surface layer 1 µm, factor 1.1). The specimen deforms under remote tension; the material is isotropic linear elastic with Young’s modulus E = 74 GPa and Poisson’s ratio ν = 0.33. For each (r, b, t) geometry, the nodal normal stresses (σ_xx, σ_yy, σ_zz) are extracted along the crack front. The triaxiality parameter h is computed as h = σ_zz / [ν (σ_xx + σ_yy)] at each through‑thickness position (z/t). The portion of thickness pt is defined as the fraction of the thickness where h ≥ 0.97. The workflow runs a parametric sweep over multiple (r, b, t) combinations to build the relation between geometry and pt.

## Reproduction target
Produce a CSV file `pt_table.csv` that reports the computed pt values for a set of (r, b, t) geometry combinations. The file must minimally include the specific combination r = 0.5 mm, b = 1 mm, t = 10.56 mm and several additional points chosen to capture the parametric trend (for example, other t values for r = 0.5, b = 1; r = 1, b = 1; r = 2, b = 1; r = 0.5, b = 2). For every geometry, execute the finite element simulation and post‑processing described in the workflow steps to obtain a genuine pt value. The checker will verify that the entries in the CSV are consistent with the required criteria for the optimal condition and with the expected trend across the parameter range.

## Assets

- CalculiX (open-source finite element solver): https://www.calculix.de/
- Python scientific stack: numpy scipy meshio matplotlib pandas

## Workflow steps

### Step 1: Generate parametric 3D FE mesh
- Role: process
- Action: Create a parametric finite element mesh for the side-grooved M(T) specimen exploiting symmetry (1/8 model). Use 20-node hexahedral isoparametric elements, quarter-point singular elements around the crack front, a spider-web concentric ring refinement (3 rings) at the crack tip, and 50 through-thickness layers with a geometric progression (surface layer 1 μm, factor 1.1). The mesh must be parametric with respect to groove radius r, groove depth b, and reduced thickness t.
- Evidence: `/app/outputs/mesh_info.json`

### Step 2: Run parametric FE stress analyses
- Role: process
- Action: For a set of (r,b,t) combinations that minimally includes the optimal combination (r=0.5, b=1, t=10.56) and enough additional points to capture the trend (e.g., r=0.5,b=1; r=1,b=1; r=2,b=1; r=0.5,b=2 with several t values), run a linear elastic FE simulation under remote tension. Use isotropic linear elastic material (E=74 GPa, ν=0.33). Save the nodal normal stress components (σ_xx, σ_yy, σ_zz) along the crack front.
- Evidence: `/app/outputs/simulation_log.json`

### Step 3: Compute triaxiality parameter h and portion-of-thickness pt
- Role: scored (load-bearing)
- Action: Post-process the nodal stresses from each simulation to compute the triaxiality parameter h = σ_zz / [ν(σ_xx+σ_yy)] at each through-thickness position (z/t). For each geometry, determine the portion of thickness pt where h ≥ 0.97. Compile all results into a single CSV file.
- Output file: `/app/outputs/pt_table.csv`
- Format: csv
- Contract: CSV with header: r,b,t,pt. Columns: r (float, mm) — groove radius; b (float, mm) — groove depth; t (float, mm) — reduced thickness; pt (float, 0–1) — fraction of thickness with h ≥ 0.97.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pt_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pt_table.csv
- path: `/app/outputs/pt_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of (r, b, t) geometry combinations and the corresponding portion-of-thickness pt where h ≥ 0.97.
- schema:
  - `type`: table
  - `required_columns`: `r`, `b`, `t`, `pt`
  - `units`:
    - `r`: mm
    - `b`: mm
    - `t`: mm
    - `pt`: fraction (0-1)

Notes: The checker will compare the submitted pt values against hidden reference values (the optimal-condition threshold and digitized trend from the paper) using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pt_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "b",
          "t",
          "pt"
        ],
        "units": {
          "r": "mm",
          "b": "mm",
          "t": "mm",
          "pt": "fraction (0-1)"
        }
      },
      "description": "Table of (r, b, t) geometry combinations and the corresponding portion-of-thickness pt where h ≥ 0.97."
    }
  ],
  "notes": "The checker will compare the submitted pt values against hidden reference values (the optimal-condition threshold and digitized trend from the paper) using appropriate tolerances."
}
```

## How you are scored
A hidden verifier will inspect your submitted `/app/outputs/pt_table.csv`. The scoring has two components:  
1. **Optimal‑condition check** – the pt value for the combination (r = 0.5, b = 1, t = 10.56) is compared against a hidden threshold derived from the paper’s claim. Full credit on this component requires that your computed pt meets or exceeds that threshold.  
2. **Trend agreement** – for a selection of other (r, b, t) rows in the table, your pt values are compared against hidden reference values digitised from the paper’s parametric chart. Agreement is judged with a relative tolerance.  
The overall reward is a weighted combination of these two checks (50 % optimal condition, 50 % trend accuracy). Full credit demands genuine execution of the finite element pipeline; self‑reporting numbers without running the simulations is not sufficient. The exact thresholds and reference values are withheld – your task is to faithfully implement the described method and let the verifier evaluate the outputs.
