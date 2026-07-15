# Effective Elastic Modulus of Porous Scaffolds via Finite Element Simulation

## Problem background
In tissue engineering, porous polymer scaffolds serve as three-dimensional supports for cell growth and must transmit mechanical loads. Understanding how the scaffold's pore architecture—shape and size—affects its effective elastic modulus is essential for designing scaffolds with appropriate stiffness. This task investigates the effective Young's modulus of porous poly(ethyl-acrylate) (PEA) scaffolds through finite element analysis. The scaffolds consist of an isotropic PEA matrix with a Young's modulus of 2.18 MPa and Poisson's ratio 0.3, containing a well-defined pore network at 60% porosity. The goal is to compute the effective moduli for different pore geometries and sizes, and to assess whether the modulus depends on pore diameter or pore shape.

## Approach
We employ linear elastic finite element simulations. The bulk PEA material is modeled as isotropic with known elastic constants. Several computational models representing different pore architectures are constructed: (1) 2D plane-stress models of a rectangular sheet containing a regular array of circular holes of different diameters but equal porosity; (2) 3D models of a cubical volume with interconnected cylindrical pores (diameter 80 µm) or interconnected spherical pores (diameter 80 µm), both at 60% porosity. For each model, a small compressive displacement is applied, reaction forces are computed, and the effective Young's modulus is derived from the force–displacement relation. The five computed moduli are compared to reveal the influence of pore geometry and pore size.

## Reproduction target
Produce the file `/app/outputs/computed_moduli.csv` containing the computed effective Young's moduli (in MPa) for the five scaffold models defined in Step 1: the 2D models with hole diameters of 100 µm, 320 µm, and 640 µm (labeled A, B, C), and the 3D models with cylindrical and spherical pores (labeled cylindrical, spherical). The hidden verifier will assess whether the computed moduli satisfy the expected physical trends for these architectures.

## Assets

- Open-source finite element solver: Any open-source FEM solver capable of linear elastic static analysis (e.g., CalculiX, Elmer FEM, FreeCAD FEM)

## Workflow steps

### Step 1: FEM simulation and effective modulus computation
- Role: scored (load-bearing)
- Action: Use an open-source finite element solver to construct and solve five linear elastic models of porous poly(ethyl-acrylate) scaffolds. The bulk material is isotropic with Young's modulus E = 2.18 MPa and Poisson's ratio ν = 0.3. All models must achieve a porosity of 60 ± 1%. (1) Three 2D plane-stress models: rectangular domain 2210 µm × 740 µm containing a regular array of circular holes with diameters of 100 µm (model A), 320 µm (model B), and 640 µm (model C). Apply a vertical downward displacement of 10 µm on the central region of the top edge; restrict horizontal displacement on the right boundary; fix the bottom edge in both directions. (2) 3D model with interconnected cylindrical pores of diameter 80 µm: a cuboid of 480 µm × 240 µm × 160 µm with a pore network achieving 60% porosity. Apply a vertical displacement of 10 µm on the top face, constrain the bottom face vertically, and laterally constrain one vertical face. (3) 3D model with interconnected spherical pores of diameter 80 µm: use a domain of 480 µm × 240 µm × 160 µm (or similar) with a connected spherical pore lattice yielding 60% porosity; apply the same loading and boundary conditions as the cylindrical model. For each model, compute the reaction force from the simulation, derive the effective Young's modulus from the force, dimensions, and imposed displacement, and write the results to a CSV file.
- Output file: `/app/outputs/computed_moduli.csv`
- Format: csv
- Contract: model_id (string, one of: A, B, C, cylindrical, spherical), computed_E_MPa (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_moduli.csv
- path: `/app/outputs/computed_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed effective Young's moduli for the five porous scaffold models from finite element analysis.
- schema:
  - `type`: table
  - `required_columns`: `model_id`, `computed_E_MPa`
  - `units`:
    - `computed_E_MPa`: MPa

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model_id",
          "computed_E_MPa"
        ],
        "units": {
          "computed_E_MPa": "MPa"
        }
      },
      "description": "Computed effective Young's moduli for the five porous scaffold models from finite element analysis."
    }
  ],
  "notes": ""
}
```

## How you are scored
The hidden verifier reads only `/app/outputs/computed_moduli.csv`. It checks two aspects: (a) structural consistency – the 2D moduli (A, B, C) should be approximately equal, and the 3D cylindrical modulus should be lower than the 3D spherical modulus; (b) proximity of each computed modulus to a hidden reference value. The final reward is a weighted combination of the structural pass/fail (40%) and the value proximity (60%). Simply reporting the paper’s published moduli without actually running the simulation will not satisfy the structural checks, because the verifier independently evaluates the relationships among the numbers you report.
