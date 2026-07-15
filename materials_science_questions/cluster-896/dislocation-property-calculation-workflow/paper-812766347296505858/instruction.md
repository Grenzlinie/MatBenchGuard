# PDD-BEM Dislocation Convergence Benchmarks

## Problem background
Predicting the mechanical response of small-scale materials requires accurate modelling of dislocation behaviour in finite volumes. When a dislocation approaches a free surface or other internal boundaries, the classical infinite-medium stress fields must be corrected with image fields that enforce the boundary conditions. The coupled Parametric Dislocation Dynamics (PDD) and Boundary Element Method (BEM) framework addresses this by using a fast numerical sum for the dislocation stress in an infinite medium and a surface-only BEM discretisation to compute the image contribution. This task evaluates the numerical convergence of that coupled method on two canonical benchmarks: (1) a screw dislocation parallel to a planar free surface, and (2) a cylinder containing a coaxial screw dislocation. The goal is to quantify how the computed quantities (image stress and relative twist error) change as the surface mesh is refined.

## Approach
We adopt the superposition principle: the total stress acting on a dislocation is the sum of an infinite-medium contribution and an image contribution that corrects for the finite boundary. The infinite-medium part is computed with a fast numerical sum over dislocation loop elements using isotropic linear elasticity. The image part is obtained from a boundary element method (BEM) – the surface is discretised with quadratic elements, the Kelvin fundamental solution is used to assemble and solve a linear system for the unknown surface displacements and tractions, and the image stress is evaluated at any interior point via the appropriate integral kernels. The two components are combined to produce the net stress on the dislocation. For the two convergence cases, this pipeline is run repeatedly with different surface mesh densities (varying the number of elements) while holding all material and geometric parameters constant. The outputs are tables that record the mesh refinement measure and the corresponding computed physical quantity.

## Reproduction target
Case 1 (screw dislocation near a free surface): For a screw dislocation in isotropic nickel (shear modulus 76 GPa, Poisson's ratio 0.31, Burgers vector magnitude 0.256 nm) placed at a distance d = 0.5 μm from a free square surface of side 2d, compute the normalized image stress at the dislocation location using the coupled PDD-BEM method. Repeat the calculation for surface discretisations of 6×6, 8×8, 10×10, 12×12, and 20×10 elements. Write the mesh size label and the corresponding normalized image stress to case1_convergence.csv.

Case 2 (coaxial screw dislocation in a cylinder): For a finite cylinder of radius 1 μm and height 2 μm made of the same nickel, containing a coaxial screw dislocation, discretise the cylinder surface to obtain total element counts of approximately 100, 200, 400, and 800. For each mesh, compute the deformed configuration and then determine the relative error in the relative twist between the two end cross-sections. Write the number of elements and the relative twist error to case2_convergence.csv.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement PDD Infinite-Medium Stress Fast Sum
- Role: process
- Action: Implement the fast numerical sum for the stress field of dislocation loops in an infinite isotropic elastic medium (Ghoniem et al. formulation) to provide the infinite-medium stress contribution needed by the coupled solver.
- Evidence: `/app/outputs/pdd_stress_fast_sum.log`

### Step 2: Implement BEM Image Stress Calculation
- Role: process
- Action: Implement the boundary element method for an elastic solid with arbitrary surface geometry: discretize the surface into quadratic elements, assemble and solve the linear system for boundary displacements/tractions using the Kelvin fundamental solution, and compute image stress at arbitrary interior points.
- Evidence: `/app/outputs/bem_image_stress.log`

### Step 3: Convergence Study: Screw Dislocation Parallel to a Free Surface (Case 1)
- Role: scored
- Action: Combine the PDD and BEM implementations to compute the normalized image stress at a screw dislocation parallel to a free surface. Setup: infinite screw dislocation in isotropic nickel (shear modulus 76 GPa, Poisson's ratio 0.31, Burgers vector magnitude 0.256 nm) at distance d = 0.5 μm from a free surface of size 2d × 2d, centered above the dislocation. For each surface mesh density (6×6, 8×8, 10×10, 12×12, 20×10 elements), compute the normalized image stress. Record the mesh size and normalized stress in case1_convergence.csv.
- Output file: `/app/outputs/case1_convergence.csv`
- Format: csv
- Contract: mesh_size (string, e.g. '6x6'), normalized_stress (float, dimensionless)
- Scoring: scored by hidden verifier

### Step 4: Convergence Study: Cylinder Containing a Coaxial Screw Dislocation (Case 2)
- Role: scored
- Action: Use the PDD-BEM model to simulate a finite cylinder (radius 1 μm, height 2 μm) containing a coaxial screw dislocation. Discretize the cylinder surface with varying mesh densities to achieve approximately 100, 200, 400, and 800 total elements. For each mesh, compute the deformed configuration and the relative error in the relative twist between the two end cross-sections. Record the number of elements and the relative twist error in case2_convergence.csv.
- Output file: `/app/outputs/case2_convergence.csv`
- Format: csv
- Contract: num_elements (int), relative_twist_error (float, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/case1_convergence.csv`
- `/app/outputs/case2_convergence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### case1_convergence.csv
- path: `/app/outputs/case1_convergence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Mesh size identifier and corresponding computed normalized image stress. The checker will verify that the normalized_stress values converge as the mesh refines (e.g., standard deviation across the last three entries less than 0.05).
- schema:
  - `type`: table
  - `required_columns`: `mesh_size`, `normalized_stress`
  - `units`:
    - `mesh_size`: text (e.g. '6x6')
    - `normalized_stress`: dimensionless

### case2_convergence.csv
- path: `/app/outputs/case2_convergence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Number of surface elements and the corresponding computed relative error in relative twist. The checker will verify that the relative_twist_error decreases monotonically with increasing num_elements (e.g., Spearman correlation < -0.9).
- schema:
  - `type`: table
  - `required_columns`: `num_elements`, `relative_twist_error`
  - `units`:
    - `num_elements`: integer
    - `relative_twist_error`: dimensionless

Notes: Both scored artifacts are checked via a structural audit (T3). The checker does not require an absolute hidden reference value; it verifies the expected convergence trend from the agent's own computed numbers. This reflects the paper's conclusion that the PDD-BEM method produces convergent results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "case1_convergence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "mesh_size",
          "normalized_stress"
        ],
        "units": {
          "mesh_size": "text (e.g. '6x6')",
          "normalized_stress": "dimensionless"
        }
      },
      "description": "Mesh size identifier and corresponding computed normalized image stress. The checker will verify that the normalized_stress values converge as the mesh refines (e.g., standard deviation across the last three entries less than 0.05)."
    },
    {
      "file": "case2_convergence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "num_elements",
          "relative_twist_error"
        ],
        "units": {
          "num_elements": "integer",
          "relative_twist_error": "dimensionless"
        }
      },
      "description": "Number of surface elements and the corresponding computed relative error in relative twist. The checker will verify that the relative_twist_error decreases monotonically with increasing num_elements (e.g., Spearman correlation < -0.9)."
    }
  ],
  "notes": "Both scored artifacts are checked via a structural audit (T3). The checker does not require an absolute hidden reference value; it verifies the expected convergence trend from the agent's own computed numbers. This reflects the paper's conclusion that the PDD-BEM method produces convergent results."
}
```

## How you are scored
Each workflow stage that produces a scored artifact (case1_convergence.csv and case2_convergence.csv) is evaluated independently by a hidden verifier. The verifier performs a structural audit: it checks that the series of values in case1_convergence.csv converge as the mesh density increases (e.g., the normalized stress values become approximately constant for the finer meshes) and that the relative twist error in case2_convergence.csv decreases monotonically as the element count grows. No external absolute reference value is required; the verifier uses the trends present in your own submitted CSV files. The final reward (a number between 0 and 1) is a weighted combination of the scores from the two scored stages. Simply reporting a number that matches a literature value is not sufficient – you must produce the full convergence tables with the expected structural behaviour.
