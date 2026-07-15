# Porosity-Dependent Pore-Load Modulus Modeling via FEM and Analytical Model

## Problem background
Mesoporous silicon membranes with parallel, non-interconnected cylindrical pores deform linearly when a fluid inside the pores exerts pressure (e.g., during capillary condensation). The proportionality constant relating the pressure in the pores to the macroscopic strain of the membrane is called the pore-load modulus M. For a material with a regular pore geometry, M is expected to depend on the porosity φ and on the elastic properties (Young’s modulus E, Poisson’s ratio ν) of the solid pore walls. This task reproduces finite-element method (FEM) simulations of a hexagonal lattice of cylindrical pores to compute M at several porosities, and assesses agreement with an analytical model that expresses M as a function of φ, E, and ν. In addition, a previously measured experimental pore-load modulus at a given porosity is used to infer the Young’s modulus of the pore walls via the same analytical model.

## Approach
The computational experiment models a repeating hexagonal unit cell containing a single cylindrical pore. The geometry is a 2D plane‑strain cross section perpendicular to the pore axes. Symmetry boundary conditions are imposed on four sides of the unit cell: zero normal displacement on the lines of symmetry, and a uniform normal pressure P applied on the pore wall. Linear elastic material behaviour with known E = 130 GPa and ν = 0.28 is assumed. For each porosity φ (0.3, 0.4, 0.5, 0.6, 0.7), the pore radius is set to match φ, and the FEM solve yields the full displacement field. From this, the average vertical engineering strain ε_yy over the unit cell is calculated. The pore‑load modulus is then M_FEM = P / ε_yy. Separately, an analytical expression M_analytical = (E / (2(1-ν²))) * (1/φ - 1) is evaluated for each porosity. Finally, using an experimental M value (obtained from macroscopic strain measurements of a real pSi membrane at φ = 0.60), the analytical model is inverted to deduce an implied wall Young’s modulus E_wall_implied. All computed quantities—M_FEM, M_analytical, and the inferred E_wall_implied—are collected in a single CSV file.

## Reproduction target
Your goal is to produce a single CSV file `/app/outputs/porosity_modulus_data.csv` with the following columns: porosity, M_FEM (GPa), M_analytical (GPa), E_wall_implied (GPa). The file must contain one row for each porosity φ = 0.3, 0.4, 0.5, 0.6, 0.7. The M_FEM and M_analytical columns must be filled for every row, while the E_wall_implied column must be filled for the row with φ = 0.60 (the value is computed from the experimental pore‑load modulus M = 34.5 GPa); for other porosities the column may be left empty or zero. The hidden verifier will examine this file and determine how well the FEM results agree with the analytical model, and whether the inferred wall modulus matches the expected answer.

## Assets

- FreeFem++: https://freefem.org/
- Python scientific stack: numpy pandas scipy

## Workflow steps

### Step 1: FEM simulation and analytical model evaluation
- Role: scored (load-bearing)
- Action: Set up a 2D plane-strain finite element model of a hexagonal unit cell with a cylindrical pore (radius determined by porosity). Apply symmetry boundary conditions and uniform pressure P on the pore wall. Solve linear elasticity using Young's modulus E=130 GPa and Poisson's ratio ν=0.28 for five porosities φ = 0.3, 0.4, 0.5, 0.6, 0.7. For each φ compute the average vertical engineering strain ε_yy and the pore-load modulus M_FEM = P/ε_yy. Also evaluate the analytical expression M_analytical = (E/(2(1-ν²)))*(1/φ - 1) for each porosity. Using the experimental M=34.5 GPa at φ=0.60, compute the implied pore-wall Young's modulus E_wall_implied from the analytical model. Write all results to a CSV file.
- Output file: `/app/outputs/porosity_modulus_data.csv`
- Format: csv
- Contract: Columns: porosity (float), M_FEM (float in GPa), M_analytical (float in GPa), E_wall_implied (float in GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/porosity_modulus_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### porosity_modulus_data.csv
- path: `/app/outputs/porosity_modulus_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV with the FEM and analytical pore-load moduli for five porosities, and the implied wall Young's modulus at φ=0.60.
- schema:
  - `type`: table
  - `required_columns`: `porosity`, `M_FEM`, `M_analytical`, `E_wall_implied`
  - `units`:
    - `M_FEM`: GPa
    - `M_analytical`: GPa
    - `E_wall_implied`: GPa

Notes: The experimental pore-load modulus (34.5 GPa) is a fixed input parameter used to infer the wall modulus; it is not an output. The checker recomputes the R² between M_FEM and M_analytical and verifies the E_wall_implied value against a hidden reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "porosity_modulus_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "porosity",
          "M_FEM",
          "M_analytical",
          "E_wall_implied"
        ],
        "units": {
          "M_FEM": "GPa",
          "M_analytical": "GPa",
          "E_wall_implied": "GPa"
        }
      },
      "description": "CSV with the FEM and analytical pore-load moduli for five porosities, and the implied wall Young's modulus at φ=0.60."
    }
  ],
  "notes": "The experimental pore-load modulus (34.5 GPa) is a fixed input parameter used to infer the wall modulus; it is not an output. The checker recomputes the R² between M_FEM and M_analytical and verifies the E_wall_implied value against a hidden reference."
}
```

## How you are scored
After you submit your CSV, a hidden verifier (checker) reads the file and independently computes a statistical measure of agreement between your M_FEM and M_analytical columns (such as the coefficient of determination R²). It also reads the E_wall_implied value you provided for φ = 0.60 and compares it to a reference value derived from the paper’s analysis. Your score is based on how closely your FEM calculations reproduce the expected analytical relationship (high R²) and on the accuracy of your inferred wall modulus. The verifier combines these two checks into a single reward between 0 and 1. Reporting a number that does not originate from genuine FEM computations will not pass the hidden consistency checks.
