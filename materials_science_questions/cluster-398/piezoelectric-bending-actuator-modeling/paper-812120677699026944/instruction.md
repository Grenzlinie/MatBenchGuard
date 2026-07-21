# Electro-mechanical coupled element-free Galerkin analysis of piezoelectric structures

## Problem background
Piezoelectric ceramic multilayer actuators are widely used in automotive sensors and transducers due to their small volume, quick response, and large generated forces. However, the high electric fields applied during operation lead to stress concentrations near internal electrode edges, which can initiate crack propagation and degrade reliability. Accurate numerical simulation of the coupled electro-mechanical fields is essential for understanding failure mechanisms and designing durable devices. Conventional finite element methods require frequent remeshing when modeling crack growth, which is computationally burdensome. The element-free Galerkin (EFG) method, a meshless approach based on moving least squares (MLS) interpolation, offers a promising alternative by discretizing the domain with scattered nodes without fixed element connectivity, simplifying the treatment of discontinuities such as cracks and holes. The target of this reproduction is to implement an electro-mechanical coupled EFG formulation and validate it on benchmark problems to assess its accuracy in predicting stress and electric field distributions.

## Approach
The EFG method for coupled electro-mechanical problems combines the MLS approximation with the weak form of piezoelectricity. The displacement and electric potential fields are interpolated from nodal values using MLS shape functions, constructed from a polynomial basis (optionally enriched with singular terms for nonconvex domains) and a compactly supported weight function. For problems involving holes or cracks, diffraction weight functions are employed to satisfy the discontinuity of mechanical and electric displacements across the boundaries. Essential boundary conditions are enforced via a penalty formulation that yields a sparse, symmetric, and positive-definite stiffness matrix. The constitutive behavior is governed by a transversely isotropic piezoelectric model (PZT-5H), where the electromechanical coupling is expressed through a 5×5 constitutive matrix relating stresses, strains, electric fields, and electric displacements under plane strain conditions. The global stiffness matrix and force vector are assembled by integrating over a background mesh of cells using Gauss quadrature, and the resulting linear system is solved for nodal displacements and electric potentials.

Two numerical experiments are conducted. The first simulates an infinite PZT-5H plate with a central circular hole, subjected to a remote uniaxial tensile stress and a positive electric field applied across the poling direction (y‑axis), under plane strain. The plate is represented by a square domain with side length ten times the hole radius; enriched basis functions and diffraction weight functions capture the hole’s influence. The second experiment models a half‑layer of a ceramic multilayer actuator. The geometry consists of a rectangular region of thickness H, extended on one side by 2H and on the other by 8H, with an electrode covering part of the bottom surface. An electric potential corresponding to an applied field of 0.72 × 0.4 MV/m is imposed on the electrode, while symmetry and far‑field boundary conditions are applied. The EFG model uses a uniform grid of integration cells with nodes refined around the electrode tip to resolve high field gradients.

## Reproduction target
From the hole problem, produce a CSV file containing the normalized hoop stress and the normalized hoop electric displacement at 36 equally spaced angular positions on the hole rim (angles from 0° to 360° inclusive, in steps of 10°). From the actuator problem, produce a CSV file containing the electric field component Ex (V/m) and the normal stress σyy (Pa) along the x‑axis at y = 0, for points from x/H = −8 to x/H = 2. Both outputs must be saved as CSV files in the exact location `/app/outputs/step_01_hole_results.csv` and `/app/outputs/step_02_actuator_results.csv`, following the schemas defined in the workflow steps and output contract.

## Assets
The only required external resource is the set of PZT-5H material constants, which are listed below. No other datasets, models, or downloads are needed.

**PZT-5H material parameters (plane‑strain piezoelectric):**

| Parameter | Value |
|-----------|-------|
| C₁₁ | 12.6 × 10¹⁰ N/m² |
| C₁₂ | 5.5 × 10¹⁰ N/m² |
| C₁₃ | 12.3 × 10¹⁰ N/m² |
| C₃₃ | 11.7 × 10¹⁰ N/m² |
| C₄₄ | 3.53 × 10¹⁰ N/m² |
| e₃₁ | −6.5 C/m² |
| e₃₃ | 23.2 C/m² |
| e₁₅ | 17.0 C/m² |
| ε₁₁ (=⁠​d₁₁) | 151 × 10⁻¹⁰ C/Vm |
| ε₃₃ (=⁠​d₃₃) | 130 × 10⁻¹⁰ C/Vm |

## Workflow steps

### Step 1: Construct the electro-mechanical EFG solver
- Role: process
- Action: Implement the electro-mechanical coupled element-free Galerkin method with moving least squares shape functions, penalty enforcement of essential boundary conditions, and assembly of the global stiffness matrix using the published 5x5 plane-strain piezoelectric constitutive matrix for PZT-5H. The solver must support enriched basis functions and diffraction weight functions for nonconvex domains.
- Evidence: `/app/outputs/efg_solver.log`

### Step 2: Simulate infinite piezoelectric plate with a circular hole
- Role: scored (load-bearing)
- Action: Using the EFG solver with enriched basis and diffraction functions, model a square PZT-5H plate with a central circular hole under remote tensile stress and a positive electric field (plane strain, poling along y-axis). Compute the normalized hoop stress and normalized hoop electric displacement on the hole rim at 36 equally spaced angular positions from 0° to 360°.
- Output file: `/app/outputs/step_01_hole_results.csv`
- Format: csv
- Contract: angle_deg (degrees, 0 to 360 in steps of 10), sigma_normalized (dimensionless), D_normalized (dimensionless)
- Scoring: scored by hidden verifier

### Step 3: Simulate uncracked multilayer actuator
- Role: scored (load-bearing)
- Action: Using the EFG solver, model a half-layer of a ceramic multilayer actuator with geometry L1=2H, L2=8H and an applied electric field of 0.72*0.4 MV/m. Compute the electric field Ex (V/m) and the normal stress sigma_yy (Pa) along the x-axis at y=0 from x=-L2 to L1.
- Output file: `/app/outputs/step_02_actuator_results.csv`
- Format: csv
- Contract: x_over_H (dimensionless, range -8 to 2), Ex_field (V/m), sigma_yy (Pa)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_hole_results.csv`
- `/app/outputs/step_02_actuator_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_hole_results.csv
- path: `/app/outputs/step_01_hole_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Normalized hoop stress and electric displacement on the hole rim. The checker recomputes the analytical solution and scores via RMSE; lower error is better.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `sigma_normalized`, `D_normalized`
  - `units`:
    - `angle_deg`: degree
    - `sigma_normalized`: dimensionless
    - `D_normalized`: dimensionless

### step_02_actuator_results.csv
- path: `/app/outputs/step_02_actuator_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Electric field and normal stress along the x-axis near the electrode edge. The checker compares to digitized reference values; lower pointwise deviation is better.
- schema:
  - `type`: table
  - `required_columns`: `x_over_H`, `Ex_field`, `sigma_yy`
  - `units`:
    - `x_over_H`: dimensionless
    - `Ex_field`: V/m
    - `sigma_yy`: Pa

Notes: The PZT-5H material constants are provided in instruction.md. The scaling of the penalty coefficient and nodal refinement are implementation choices left to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_hole_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "sigma_normalized",
          "D_normalized"
        ],
        "units": {
          "angle_deg": "degree",
          "sigma_normalized": "dimensionless",
          "D_normalized": "dimensionless"
        }
      },
      "description": "Normalized hoop stress and electric displacement on the hole rim. The checker recomputes the analytical solution and scores via RMSE; lower error is better."
    },
    {
      "file": "step_02_actuator_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_over_H",
          "Ex_field",
          "sigma_yy"
        ],
        "units": {
          "x_over_H": "dimensionless",
          "Ex_field": "V/m",
          "sigma_yy": "Pa"
        }
      },
      "description": "Electric field and normal stress along the x-axis near the electrode edge. The checker compares to digitized reference values; lower pointwise deviation is better."
    }
  ],
  "notes": "The PZT-5H material constants are provided in instruction.md. The scaling of the penalty coefficient and nodal refinement are implementation choices left to the agent."
}
```

## How you are scored
Each scored artifact is independently evaluated by a hidden verifier. For the hole problem, the verifier recomputes the analytical solution for the normalized hoop stress and normalized electric displacement on the hole rim and compares your values using a root‑mean‑square error (RMSE) metric. For the actuator problem, the verifier compares your electric field and stress profiles to digitized reference curves along the x‑axis, using pointwise absolute deviation. Both comparisons are directional: lower error yields a higher reward. The final reward is a weighted combination of the per‑artifact scores. The EFG solver implementation (Step 1) is required to produce these outputs, but it is not directly scored; only the two CSV files carry weight. Meeting or exceeding the reference accuracy earns full credit, and credit degrades as the error increases. Hidden tolerances are set to account for legitimate implementation differences while ensuring that only a genuine re‑implementation of the EFG method can achieve a high score.
