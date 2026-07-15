# Evaluation of J‑integrals and Plasticity Influence Term in an Elastic‑Plastic C(T) Specimen using Configurational Forces

## Problem background
In fracture mechanics of elastic-plastic materials, plastic deformation complicates the crack driving force. The configurational forces approach yields a near-tip J‑integral J_tip and a "plasticity influence term" C_p that captures the effect of plastic deformation on the relationship between far‑field and near‑tip J‑integrals. This task computationally evaluates these quantities for a stationary crack in a compact tension (C(T)) specimen under plane‑strain incremental plasticity, covering contained, uncontained, and general yielding conditions.

## Approach
A 2D plane‑strain finite element model of the C(T) specimen (width W=50 mm, crack length a=25 mm) is built with St37 steel material properties and a hardening curve from Chen et al. (2003). Incremental loading is applied via a prescribed load‑line displacement v_LL from 0 to 0.44 mm using an open‑source FE solver that supports large‑deformation, quasi‑static analysis (e.g., CalculiX). After the stress analysis, the configurational body force vector f is computed at each node from the elastic strain energy density, Cauchy stress, and displacement gradient. The far‑field J‑integral J_far^ep is obtained by integrating the projection of f onto the crack‑growth direction over all interior elements (excluding external boundary elements), and the near‑tip J‑integral J_Γ2^ep is computed from the same integral restricted to elements within a 2‑mm contour of the crack tip. The plasticity influence term is C_p = J_Γ2^ep − J_far^ep. These quantities are evaluated at eight load‑line displacement values spanning the contained‑ to general‑yielding regime.

## Reproduction target
Set up a 2D plane‑strain finite element model of a C(T) specimen (thickness B=25 mm, width W=50 mm, crack length a=25 mm) with St37 steel material properties: Young’s modulus E=200 GPa, Poisson's ratio ν=0.3, yield strength σ_y=270 MPa, ultimate tensile strength σ_u=426 MPa, and a true‑stress vs. true‑plastic‑strain hardening curve from Chen et al. (2003) (a power‑law approximation with n=0.2 may be used). Apply incremental loading via prescribed load‑line displacement v_LL from 0 to 0.44 mm using an open‑source FE solver capable of large‑deformation, quasi‑static analysis. Post‑process the results to compute the configurational body force f, then compute the far‑field J‑integral J_far^ep (integrated over all interior elements, excluding those on the external boundary), the near‑tip J‑integral J_Γ2^ep (integrated over elements within a 2‑mm contour of the crack tip), and the plasticity influence term C_p = J_Γ2^ep − J_far^ep. Produce a CSV file with columns v_LL_mm, J_far_ep_kJ_m2, J_Gamma2_ep_kJ_m2, Cp_kJ_m2 for the load‑line displacements v_LL = 0.00, 0.10, 0.20, 0.25, 0.30, 0.35, 0.40, 0.44 mm. All values are in kJ/m²; missing values as empty cells.

## Assets

- CalculiX (open‑source FE solver): http://www.calculix.de/
- Python with numpy, scipy, matplotlib: pip install numpy scipy matplotlib
- True stress vs true plastic strain curve for St37 steel (Chen et al. 2003): 10.1023/A:1027353521867

## Workflow steps

### Step 1: Set up finite element model of C(T) specimen
- Role: process
- Action: Define the 2D plane‑strain geometry (width W=50 mm, crack length a=25 mm), create a uniform mesh of four‑node elements with mesh size 0.5 mm near the crack tip, assign material properties (E=200 GPa, ν=0.3, yield stress 270 MPa, hardening curve from Chen et al. 2003), and define boundary conditions (prescribed load‑line displacement v_LL, symmetry, traction‑free crack faces). Prepare input files for the chosen FE solver.
- Evidence: `/app/outputs/CT_model.inp`

### Step 2: Run incremental plasticity simulation
- Role: process
- Action: Using the FE solver, perform a large‑deformation, quasi‑static analysis with incremental loading via increasing load‑line displacement v_LL from 0 to 0.44 mm. Solve for stress, strain (total, elastic, plastic) and displacement fields at each increment. Save the results in a format suitable for post‑processing (e.g., .frd or .vtk).
- Evidence: `/app/outputs/simulation_results.frd`

### Step 3: Post‑process configurational body forces
- Role: process
- Action: From the simulation output fields, compute the configurational body force vector f at each node according to the small‑strain expression (or the finite‑strain equivalent) using f = -∇·(φ I - ∇u^T σ), where φ is the elastic strain energy density, σ is Cauchy stress, u is displacement, and the gradient is with respect to reference coordinates. Save the force field data, excluding elements on the external boundary.
- Evidence: `/app/outputs/config_forces.npy`

### Step 4: Compute far‑field and near‑tip J‑integrals and plasticity influence term
- Role: scored (load-bearing)
- Action: For each load‑line displacement value v_LL = 0.00, 0.10, 0.20, 0.25, 0.30, 0.35, 0.40, 0.44 mm, compute J_far^ep as the negative sum over all interior elements of (ê·f) ΔA (excluding boundary elements), and J_Γ2^ep as the same sum restricted to elements within a contour 2 mm from the crack tip. Compute Cp = J_Γ2^ep - J_far^ep. Write a CSV with the columns specified below.
- Output file: `/app/outputs/C(T)_J_integrals.csv`
- Format: csv
- Contract: Header: v_LL_mm, J_far_ep_kJ_m2, J_Gamma2_ep_kJ_m2, Cp_kJ_m2. All numeric values in kJ/m²; missing values as empty cells.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/C(T)_J_integrals.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### C(T)_J_integrals.csv
- path: `/app/outputs/C(T)_J_integrals.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV of computed far‑field J‑integral, near‑tip J‑integral (within 2‑mm contour), and plasticity influence term Cp for the C(T) specimen at the specified load‑line displacements.
- schema:
  - `type`: table
  - `required_columns`: `v_LL_mm`, `J_far_ep_kJ_m2`, `J_Gamma2_ep_kJ_m2`, `Cp_kJ_m2`
  - `units`:
    - `v_LL_mm`: mm
    - `J_far_ep_kJ_m2`: kJ/m²
    - `J_Gamma2_ep_kJ_m2`: kJ/m²
    - `Cp_kJ_m2`: kJ/m²

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "C(T)_J_integrals.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "v_LL_mm",
          "J_far_ep_kJ_m2",
          "J_Gamma2_ep_kJ_m2",
          "Cp_kJ_m2"
        ],
        "units": {
          "v_LL_mm": "mm",
          "J_far_ep_kJ_m2": "kJ/m²",
          "J_Gamma2_ep_kJ_m2": "kJ/m²",
          "Cp_kJ_m2": "kJ/m²"
        }
      },
      "description": "CSV of computed far‑field J‑integral, near‑tip J‑integral (within 2‑mm contour), and plasticity influence term Cp for the C(T) specimen at the specified load‑line displacements."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your submitted CSV, compare the reported numerical values for J_far^ep and C_p against hidden reference ranges derived from the underlying paper's data, and check expected trends (e.g., sign and approximate zero region). It will also validate the CSV format, column names, and row count. The total reward is a weighted combination of these checks; reporting the paper’s published numbers without actually running the simulation will not satisfy the numerical checks.
