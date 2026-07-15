# Finite element comparison of open-cell foam tensile behavior

## Problem background
Nickel foam is a lightweight open-cell porous metal widely used as electrode substrate in batteries. Its mechanical properties under tension, particularly the influence of cell geometry and porosity on load-bearing behavior, are critical for structural design. Finite element analysis can simulate the tensile response of idealized unit-cell models and help understand how different geometries and porosity levels affect the stress-strain relationship.

## Approach
The work builds static finite element models of open-cell nickel foam using two idealized unit-cell geometries: the Kelvin multi-cell assembly and the Gibson-Ashby cubic lattice. For each model, the foam is represented as a network of struts with given elastic-plastic material properties; the porosity is fixed by setting the strut cross-section to match a target relative density. A tensile test is simulated by fixing one end and applying a uniform tensile force on the opposite face. The overall stress-strain curve is extracted from the simulation. This comparison is first carried out at a single porosity. Then the Kelvin model is simulated at several additional porosities, using the corresponding material parameters associated with each porosity level, to examine how porosity affects the mechanical response.

## Reproduction target
Produce the tensile stress-strain curves for both the Kelvin and Gibson-Ashby models at a common porosity and for the Kelvin model at multiple porosities. The target is to resolve whether one model bears higher stress than the other at the same strain, and whether stress changes monotonically as porosity varies. The results are delivered as two CSV files, which will be checked by a hidden verifier against expected structural relationships (ordering and monotonic trends).

## Assets

- Open-source finite element solver: http://www.calculix.de/
- Mesh generation tool: http://gmsh.info/

## Workflow steps

### Step 1: Model comparison at fixed porosity
- Role: scored (load-bearing)
- Action: Build finite element models of the Kelvin multi-cell and Gibson-Ashby cubic unit-cell assemblies with porosity 96.1% (relative density 0.039). Apply material properties: elastic modulus E=93 MPa, Poisson's ratio ν=0.31, yield strength 0.43 MPa, shear modulus 36 MPa. Generate mesh, apply boundary conditions (left face fixed, uniform static tensile force on right face), run static analysis, and extract the global stress-strain curve for both models.
- Output file: `/app/outputs/step_01_stress_strain_comparison.csv`
- Format: csv
- Contract: CSV with header: model,strain,stress. model is string ('Kelvin' or 'Gibson-Ashby'), strain is float (dimensionless or %), stress is float (MPa). Sorted by strain per model.
- Scoring: scored by hidden verifier

### Step 2: Porosity effect for Kelvin model
- Role: scored (load-bearing)
- Action: Build Kelvin unit-cell models at porosities 89%, 92%, 95%, 97% using the cross-section radii and material parameters: radii 0.064, 0.051, 0.043, 0.033 mm; elastic moduli 261, 191, 119, 71.48 MPa; shear moduli 101, 74, 46, 27.7 MPa; Poisson's ratio 0.31. Apply identical boundary conditions, run static simulations, and extract stress-strain curves.
- Output file: `/app/outputs/step_02_stress_strain_porosity.csv`
- Format: csv
- Contract: CSV with header: porosity,strain,stress. porosity is float (percentage, e.g., 89.0), strain is float, stress is float (MPa). Sorted by strain per porosity.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_stress_strain_comparison.csv`
- `/app/outputs/step_02_stress_strain_porosity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_stress_strain_comparison.csv
- path: `/app/outputs/step_01_stress_strain_comparison.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Tensile stress-strain curves for Kelvin and Gibson-Ashby models at 96.1% porosity. The checker verifies that the relative stress levels between the two models follow the expected structural relationship across the common strain range.
- schema:
  - `type`: table
  - `required_columns`: `model`, `strain`, `stress`
  - `column_types`:
    - `model`: string
    - `strain`: float
    - `stress`: float
  - `units`:
    - `strain`: dimensionless or percent
    - `stress`: MPa

### step_02_stress_strain_porosity.csv
- path: `/app/outputs/step_02_stress_strain_porosity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stress-strain curves for Kelvin model at porosities 89%, 92%, 95%, 97%. The checker verifies that the stress values follow the expected monotonic trend with porosity at a fixed strain.
- schema:
  - `type`: table
  - `required_columns`: `porosity`, `strain`, `stress`
  - `column_types`:
    - `porosity`: float
    - `strain`: float
    - `stress`: float
  - `units`:
    - `porosity`: percentage
    - `strain`: dimensionless or percent
    - `stress`: MPa

Notes: The experimental comparison is qualitative and not scored. The checker performs structural checks: ordering of stress between models and monotonic trend with porosity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_stress_strain_comparison.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "strain",
          "stress"
        ],
        "column_types": {
          "model": "string",
          "strain": "float",
          "stress": "float"
        },
        "units": {
          "strain": "dimensionless or percent",
          "stress": "MPa"
        }
      },
      "description": "Tensile stress-strain curves for Kelvin and Gibson-Ashby models at 96.1% porosity. The checker verifies that the relative stress levels between the two models follow the expected structural relationship across the common strain range."
    },
    {
      "file": "step_02_stress_strain_porosity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "porosity",
          "strain",
          "stress"
        ],
        "column_types": {
          "porosity": "float",
          "strain": "float",
          "stress": "float"
        },
        "units": {
          "porosity": "percentage",
          "strain": "dimensionless or percent",
          "stress": "MPa"
        }
      },
      "description": "Stress-strain curves for Kelvin model at porosities 89%, 92%, 95%, 97%. The checker verifies that the stress values follow the expected monotonic trend with porosity at a fixed strain."
    }
  ],
  "notes": "The experimental comparison is qualitative and not scored. The checker performs structural checks: ordering of stress between models and monotonic trend with porosity."
}
```

## How you are scored
Your outputs are scored by a hidden verifier that independently evaluates each workflow step. For the model-comparison step, the verifier checks the relative stress levels between the two models across the strain range. For the porosity-effect step, it checks the stress trend across porosities at a representative strain. Each step is assigned a weight, and the final reward is a weighted combination. Simply self-reporting numbers that match a known reference is not sufficient; the verifier derives its scoring from your actual stress-strain data and the hidden expected relationships.
