# Finite-displacement strain theory and pseudomagnetic field in point-stretched graphene

## Problem background
Strain in a material alters the positions of its atoms and, hence, its electronic properties. In graphene, strain is known to generate artificial vector potentials and pseudomagnetic fields, offering a way to engineer electronic behavior without external magnetic fields. Most existing theoretical frameworks use linear or finite strain theory, which are based on small displacements of infinitesimal length vectors. Extending the theory to large displacements of finite length vectors requires tracking how the strain itself changes as a deformation progresses. The present work develops such a large-displacement strain theory using differential geometry, which introduces an additional finite-displacement term. The theory is applied to a graphene ribbon subjected to a pair of opposing point forces at its centre (a “point stretch”). This configuration provides a non-trivial, spatially varying strain field and is a suitable testbed for evaluating the contribution of the finite-displacement term to the pseudomagnetic field.

## Approach
The reproduction task implements the large-displacement strain theory and computes the resulting pseudomagnetic field for the point-stretch geometry. The workflow is: (1) derive the strain tensor from the known analytical solution for a ribbon under point forces, using the material’s Young’s modulus, Poisson ratio, and effective thickness; (2) obtain the rotation tensor; (3) construct the metric and compute the Christoffel symbols; (4) numerically evaluate the finite-displacement tensor by integrating the Christoffel symbols along a line from the origin; (5) combine strain, rotation, and finite-displacement contributions into a bond-transformation matrix; (6) from this matrix, compute the artificial vector potential at the Dirac points and then the pseudomagnetic field B_z as the curl of the potential. All formulas are evaluated at y=0 for a range of x positions and several applied forces. For comparison, the field predicted by the linear strain theory (where rotation and finite-displacement terms are omitted) can also be computed, allowing one to assess the relative importance of the new terms. The computation relies only on standard numerical libraries and publicly available material parameters.

## Reproduction target
Reproduce two concrete artifacts: (1) a sanity check that the finite-displacement tensor Σ vanishes for a spatially constant strain; (2) the pseudomagnetic field profile B_z(x) at y=0 for the point-stretched ribbon under multiple applied forces. For the field profile, evaluate B_z for each combination of the following forces F0 (in nN) and x-coordinates (in Å): F0 ∈ {0.01, 0.05, 0.1, 0.2} nN; x from -100 Å to 100 Å in steps of 2 Å (include x=0, using the appropriate limit). The output is a CSV table (step_02_pseudomag_field.csv) with columns F_nN, x_A, B_z_T. The constant-strain check outputs a single-line verdict in step_01_const_strain_check.txt.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Verify vanishing of finite-displacement term for constant strain
- Role: scored
- Action: Implement the finite-displacement term Σ_ijk R_j R_k from the paper's differential-geometry formulas: metric g_ij = δ_ij + 2ε_ij, Christoffel symbols Γ_ijk, and the line integral Σ_ijk(R) = ∫_0^1 dλ λ Γ_ijk(λR). Choose a simple constant strain tensor (e.g., ε_xx = 0.01, all other components zero). Compute Σ·R for a test point and verify that all components evaluate to zero (within floating-point tolerance). Write the result to the output file.
- Output file: `/app/outputs/step_01_const_strain_check.txt`
- Format: txt
- Contract: Exact single line: either 'Σ vanishes: True' if the finite-displacement term is numerically zero, or 'Σ vanishes: False' otherwise.
- Scoring: scored by hidden verifier

### Step 2: Compute pseudomagnetic field for the point-stretch geometry
- Role: scored (load-bearing)
- Action: Implement the complete strain theory for the point-stretch configuration of a wide graphene ribbon. Use the analytical expressions for the strain tensor ε(x,y) (derived from stress equilibrium with material parameters: Young's modulus E, Poisson ratio ν, ribbon thickness Lz), the rotation tensor ω, the metric g_ij, Christoffel symbols Γ_ijk, the finite-displacement term Σ·R obtained by integrating Γ along the line from the origin, the bond transformation Ω, the artificial vector potential A at the K1,± Dirac points, and finally the pseudomagnetic field B_z = (ℏ/e)(∂_x A_y − ∂_y A_x). Evaluate B_z at y=0 for a range of x positions and several applied forces F0 (these will be specified in the task instructions). Handle the sign function and asymptotics carefully. Save the results to CSV.
- Output file: `/app/outputs/step_02_pseudomag_field.csv`
- Format: csv
- Contract: CSV with header row: F_nN,x_A,B_z_T. Each subsequent row corresponds to one combination of force (in nanonewtons) and x-coordinate (in angstroms). Columns F_nN, x_A, and B_z_T are numeric (float). B_z_T is the signed pseudomagnetic field in tesla.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_const_strain_check.txt`
- `/app/outputs/step_02_pseudomag_field.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_const_strain_check.txt
- path: `/app/outputs/step_01_const_strain_check.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Verification that the finite-displacement tensor Σ vanishes for spatially constant strain. The checker reads this line and expects 'Σ vanishes: True'.
- schema:
  - `type`: text
  - `required`:
    - `line`: exact string 'Σ vanishes: True' or 'Σ vanishes: False'

### step_02_pseudomag_field.csv
- path: `/app/outputs/step_02_pseudomag_field.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pseudomagnetic field values computed from the strain theory. The hidden checker independently recomputes the reference field for the same (F_nN, x_A) pairs and compares each B_z_T within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `F_nN`, `x_A`, `B_z_T`
  - `items`:
    - `F_nN`: float (nanonewtons)
    - `x_A`: float (angstroms)
    - `B_z_T`: float (tesla, signed)

Notes: The constant-strain sanity check is a low-weight step; the pseudomagnetic field CSV carries the main reward. The agent must implement all the analytical formulas; no pre-trained models or external data files are required. The checker uses a hidden reference implementation of the formulas to evaluate correctness.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_const_strain_check.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "line": "exact string 'Σ vanishes: True' or 'Σ vanishes: False'"
        }
      },
      "description": "Verification that the finite-displacement tensor Σ vanishes for spatially constant strain. The checker reads this line and expects 'Σ vanishes: True'."
    },
    {
      "file": "step_02_pseudomag_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "F_nN",
          "x_A",
          "B_z_T"
        ],
        "items": {
          "F_nN": "float (nanonewtons)",
          "x_A": "float (angstroms)",
          "B_z_T": "float (tesla, signed)"
        }
      },
      "description": "Pseudomagnetic field values computed from the strain theory. The hidden checker independently recomputes the reference field for the same (F_nN, x_A) pairs and compares each B_z_T within a tolerance."
    }
  ],
  "notes": "The constant-strain sanity check is a low-weight step; the pseudomagnetic field CSV carries the main reward. The agent must implement all the analytical formulas; no pre-trained models or external data files are required. The checker uses a hidden reference implementation of the formulas to evaluate correctness."
}
```

## How you are scored
Each workflow step’s output is independently scored by a hidden verifier. Step 1 (constant-strain check) receives partial credit if the file contains exactly the line “Σ vanishes: True”. Step 2 (pseudomagnetic field) is the main scored target: the verifier compares each B_z value in your CSV against a reference recomputed from the same analytical formulas; differences due to implementation or numerical choices are allowed within a tolerance. The two step scores are combined by weight to yield the final reward (the field CSV carries the larger weight). Reporting the correct paper numbers is not sufficient—you must faithfully implement the theory to produce the quantities.
