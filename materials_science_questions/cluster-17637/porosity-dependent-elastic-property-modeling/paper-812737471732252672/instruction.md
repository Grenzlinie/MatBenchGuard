# Porosity-Dependent Elastic Property Modeling of Porous Scaffolds

## Problem background
Bone tissue engineering relies on scaffolds that mimic the extracellular matrix, providing mechanical support and a porous environment for cell migration and nutrient transport. Extrusion-based 3D printing can fabricate bioceramic scaffolds with programmable architectures, but the interplay between geometry (strand diameter, pore diameter, layer orientation) and composite material choice on the resulting porosity and effective Young's modulus is not fully mapped. This task quantifies that relationship: you will generate a family of scaffold designs, compute their porosity, and determine their effective elastic modulus for several β‑TCP‑based composite formulations.

## Approach
The core idea is a computational pipeline that links scaffold geometry to mechanical properties. First, you will create parametric CAD models of the porous strut architecture by sweeping three geometric parameters: strand diameter (400, 600, 800 µm), pore diameter (300, 400, 500 µm), and a layer‑orientation pattern (four patterns that differ in the angular increment between successive printed layers). All 36 combinations of these parameters are modelled.

Next, macroporosity is determined from each model by comparing the solid volume to the total bounding volume. Material properties of the composite are derived from the Halpin–Tsai equations, which estimate the effective Young's modulus and Poisson's ratio of a matrix material (β‑TCP) reinforced with a secondary particle phase (ZrO₂, MgO, Al₂O₃, or HA) at a specified mixing ratio; the pure‑component properties are given in the literature and are provided within the workflow details. Finally, the pipeline proceeds to finite element analysis: for the designs that represent the two extremes of porosity, you will simulate a static compression test (fixed bottom, small downward displacement applied at the top) and extract the reaction force, from which the effective Young's modulus of the scaffold–composite combination is computed.

## Reproduction target
Your goal is to produce two scored datasets: (1) porosity values for every one of the 36 scaffold geometries, and (2) effective Young's modulus values for the four composite formulations (β‑TCP with ZrO₂, MgO, Al₂O₃, and HA) at the two models that span the porosity extremes (labelled 0.8_0.3_1 and 0.4_0.5_4 in the workflow). The verifier will check that the porosity values obey monotonic trends with respect to the geometric inputs, and that the effective modulus is physically consistent with the scaffold architecture.

## Assets

- FreeCAD: https://www.freecadweb.org/
- CalculiX: http://www.calculix.de/
- Python: python3

## Workflow steps

### Step 1: Generate scaffold CAD models
- Role: process
- Action: Create parametric CAD models of scaffold architectures using FreeCAD, varying strand diameter (400, 600, 800 µm), pore diameter (300, 400, 500 µm), and four layer orientation patterns (0-90, 0-45-90-135, 0-60-120, 0-30-60-90-120-150). Export the 36 models in a format suitable for FEA (e.g., STEP or UNV).
- Evidence: `/app/outputs/cad_generation.log`

### Step 2: Compute macroporosity
- Role: scored (load-bearing)
- Action: For each of the 36 scaffold CAD models, extract the solid volume and total bounding volume, then compute porosity = (1 − V_solid/V_total)×100. Collect the results in a CSV with columns D_um, d_um, theta_pattern (integer 1‑4 matching the patterns), porosity_percent.
- Output file: `/app/outputs/porosity.csv`
- Format: csv
- Contract: Columns: D_um (int, strand diameter in µm), d_um (int, pore diameter in µm), theta_pattern (int, 1‑4), porosity_percent (float). Expected 36 rows covering all parameter combinations.
- Scoring: scored by hidden verifier

### Step 3: Compute composite material properties
- Role: process
- Action: Compute the effective Young's modulus E_c and Poisson's ratio μ_c for each composite using the Halpin–Tsai equations. The pure material properties (from the literature) are:
  - β‑TCP: E_m = 120 GPa, μ_m = 0.3
  - ZrO₂: E_p = 210 GPa, μ_p = 0.31
  - MgO: E_p = 300 GPa, μ_p = 0.35
  - Al₂O₃: E_p = 320 GPa, μ_p = 0.23
  - HA: E_p = 13 GPa, μ_p = 0.27
  The mixing ratio is 90:10 (matrix:particle), i.e. matrix volume fraction V_m = 0.9, particle volume fraction V_p = 0.1. Use particle aspect ratio s = 1.
  Halpin–Tsai equations:
    E_c = E_m (1 + 2 s q V_p) / (1 - q V_p), where q = (E_p/E_m - 1) / (E_p/E_m + 2 s)
    μ_c = μ_m (1 + 2 s q_μ V_p) / (1 - q_μ V_p), where q_μ = (μ_p/μ_m - 1) / (μ_p/μ_m + 2 s)
  Compute E_c and μ_c for the four composites: β‑TCP:ZrO₂, β‑TCP:MgO, β‑TCP:Al₂O₃, β‑TCP:HA. Save the results to a CSV for later FEA.
- Evidence: `/app/outputs/composite_properties.csv`

### Step 4: Run finite element simulations
- Role: process
- Action: For the two scaffold architectures with extreme porosity (0.8_0.3_1 and 0.4_0.5_4) and each of the four composites (S1–S4) at the 90:10 ratio, set up a static compression FEA in CalculiX. Use a fixed bottom support, a downward displacement at the top (0.001–0.004 mm), and extract the reaction force at the fixed support. Record the force data in a CSV.
- Evidence: `/app/outputs/fea_reaction_forces.csv`

### Step 5: Compute effective Young's modulus
- Role: scored (load-bearing)
- Action: From the FEA reaction force R, scaffold cross‑sectional area A, original length l, and applied displacement dl, compute effective Young's modulus as E_eff = (R/A) / (dl/l). Report the results for each composite (S1–S4) at the two extreme porosity models 0.8_0.3_1 and 0.4_0.5_4. Write a CSV with columns composite_id, model_name, E_eff_GPa.
- Output file: `/app/outputs/effective_modulus.csv`
- Format: csv
- Contract: Columns: composite_id (string, one of S1, S2, S3, S4), model_name (string, '0.8_0.3_1' or '0.4_0.5_4'), E_eff_GPa (float). Expected 8 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/porosity.csv`
- `/app/outputs/effective_modulus.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### porosity.csv
- path: `/app/outputs/porosity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Porosity values for all 36 scaffold architectures. Scores compare the reported values, range, and monotonic trends to the paper’s reference data.
- schema:
  - `type`: table
  - `required_columns`: `D_um`, `d_um`, `theta_pattern`, `porosity_percent`
  - `units`:
    - `D_um`: µm
    - `d_um`: µm
    - `theta_pattern`: integer 1-4
    - `porosity_percent`: %

### effective_modulus.csv
- path: `/app/outputs/effective_modulus.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective Young's modulus for the four composites at the extreme porosity models. Scores compare values to paper gold and check physical consistency with scaffold architecture.
- schema:
  - `type`: table
  - `required_columns`: `composite_id`, `model_name`, `E_eff_GPa`
  - `units`:
    - `composite_id`: string (S1–S4)
    - `model_name`: string (0.8_0.3_1 or 0.4_0.5_4)
    - `E_eff_GPa`: GPa

Notes: All pure material properties and Halpin–Tsai formulas are now fully specified in the workflow description; the agent does not need any external data beyond the public tools.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "porosity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "D_um",
          "d_um",
          "theta_pattern",
          "porosity_percent"
        ],
        "units": {
          "D_um": "µm",
          "d_um": "µm",
          "theta_pattern": "integer 1-4",
          "porosity_percent": "%"
        }
      },
      "description": "Porosity values for all 36 scaffold architectures. Scores compare the reported values, range, and monotonic trends to the paper’s reference data."
    },
    {
      "file": "effective_modulus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composite_id",
          "model_name",
          "E_eff_GPa"
        ],
        "units": {
          "composite_id": "string (S1–S4)",
          "model_name": "string (0.8_0.3_1 or 0.4_0.5_4)",
          "E_eff_GPa": "GPa"
        }
      },
      "description": "Effective Young's modulus for the four composites at the extreme porosity models. Scores compare values to paper gold and check physical consistency with scaffold architecture."
    }
  ],
  "notes": "All pure material properties and Halpin–Tsai formulas are now fully specified in the workflow description; the agent does not need any external data beyond the public tools."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact (`porosity.csv` and `effective_modulus.csv`) and combines them with weights into a final reward between 0 and 1. For `porosity.csv`, it checks that the reported values fall within an expected range and respect the predicted geometric trends; for `effective_modulus.csv`, it compares the values and the ordering (modulus higher for the denser scaffold) against a hidden reference derived from published results. Simply printing a number is not enough — the verifier reconstructs the mechanical quantities your pipeline produced and validates their physical consistency. A perfect score requires the pipeline to generate internally consistent results that align with the expected behaviour, not to match a published figure exactly.
