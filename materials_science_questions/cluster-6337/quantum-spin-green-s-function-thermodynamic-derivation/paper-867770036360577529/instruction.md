# Field-Induced Magnetic Reorientation Transition in a Heisenberg Monolayer using Many-Body Green's Function Theory

## Problem background
Magnetic thin films can undergo a reorientation transition where the magnetization vector rotates as an external magnetic field or temperature changes. Understanding this transition is important for spintronics and magnetic storage. For a ferromagnetic Heisenberg monolayer with strong single-ion anisotropy, the transition can be continuous or discontinuous depending on how the anisotropy is treated in the theoretical model. The goal here is to compute the field-induced reorientation curves using a many-body Green's function theory that treats the single-ion anisotropy exactly, and to verify whether the reorientation is continuous for a large anisotropy where an approximate decoupling predicts a jump.

## Approach
Use the many-body Green's function formalism in a rotated frame: choose a coordinate system where the magnetization points along the new z-axis, so that the transverse components vanish. This allows an exact treatment of the single-ion anisotropy by introducing higher-order Green's functions and closing the hierarchy with operator-reduction identities, without any decoupling of the anisotropy terms. The exchange interaction is handled by a generalized RPA (Tyablikov) decoupling that preserves equal-site correlations. The resulting equations of motion lead to a non-symmetric matrix eigenvalue problem whose eigenvalues give the magnon energies. The correlation functions (magnetization moments) are obtained via the spectral theorem with Brillouin-zone integration. The reorientation angle is determined self-consistently from the condition that the commutator of the magnetization with the Hamiltonian vanishes in the rotated frame. Implement this self-consistent loop for a spin S=2 Heisenberg monolayer on a square lattice with nearest-neighbor exchange J=1, including an external transverse field B_x. Compute solutions for the two parameter sets given in the reproduction target.

## Reproduction target
Produce two CSV files, each containing at least 20 equally spaced rows over the specified B_x range:
- For K2=0.2 and T=100: compute normalized magnetizations <S^z>/S, <S^x>/S, and reorientation angle θ/(π/2) as functions of B_x in [0, 2.5].
- For K2=0.5 and T/J=4.9: compute the same quantities for B_x in [0, 1.5], and ensure that the reorientation angle θ/(π/2) increases monotonically with B_x (no discontinuous jump).

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/
- matplotlib: https://pypi.org/project/matplotlib/

## Workflow steps

### Step 1: Compute reorientation curve for K2=0.2, T=100
- Role: scored (load-bearing)
- Action: Implement the many-body Green's function formalism in a rotated frame for a Heisenberg monolayer with spin S=2 and single-ion anisotropy K2=0.2J at temperature T=100 (J=1). Use the generalised RPA decoupling for exchange, exact treatment of anisotropy via higher-order Green's functions with operator-reduction identities, and solve self-consistently for magnetization moments and reorientation angle via the condition that the commutator of magnetization with the Hamiltonian vanishes in the rotated frame. Compute normalized magnetization components <S^z>/S, <S^x>/S, and reorientation angle theta/(pi/2) for at least 20 equally spaced transverse field B^x values in [0, 2.5]. Write results to CSV.
- Output file: `/app/outputs/reorientation_K2_0.2_T100.csv`
- Format: csv
- Contract: Columns: B_x (float, units of J), Sz_over_S (float, dimensionless), Sx_over_S (float, dimensionless), theta_norm (float, angle/(pi/2), dimensionless)
- Scoring: scored by hidden verifier

### Step 2: Compute reorientation curve for K2=0.5, T/J=4.9
- Role: scored (load-bearing)
- Action: Using the same Green's function implementation, compute reorientation curve for parameters S=2, K2=0.5J, T/J=4.9, B^x in [0, 1.5] with at least 20 equally spaced points. Write CSV as specified.
- Output file: `/app/outputs/reorientation_K2_0.5_T4.9.csv`
- Format: csv
- Contract: Columns: B_x (float), Sz_over_S (float), Sx_over_S (float), theta_norm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reorientation_K2_0.2_T100.csv`
- `/app/outputs/reorientation_K2_0.5_T4.9.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reorientation_K2_0.2_T100.csv
- path: `/app/outputs/reorientation_K2_0.2_T100.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized magnetizations and reorientation angle vs transverse field for K2=0.2, T=100
- schema:
  - `type`: table
  - `required_columns`: `B_x`, `Sz_over_S`, `Sx_over_S`, `theta_norm`
  - `units`:
    - `B_x`: J
    - `Sz_over_S`: dimensionless
    - `Sx_over_S`: dimensionless
    - `theta_norm`: dimensionless (angle/(pi/2))

### reorientation_K2_0.5_T4.9.csv
- path: `/app/outputs/reorientation_K2_0.5_T4.9.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized magnetizations and reorientation angle vs transverse field for K2=0.5, T=4.9
- schema:
  - `type`: table
  - `required_columns`: `B_x`, `Sz_over_S`, `Sx_over_S`, `theta_norm`
  - `units`:
    - `B_x`: J
    - `Sz_over_S`: dimensionless
    - `Sx_over_S`: dimensionless
    - `theta_norm`: dimensionless (angle/(pi/2))

Notes: Each CSV must contain at least 20 rows uniformly spanning the specified B_x range. The checker compares each agent-reported value to hidden reference values digitised from the paper's figures. An absolute tolerance of 0.05 is applied for every component. For the K2=0.5 case, the checker also verifies that theta_norm is monotonically non-decreasing, confirming a continuous reorientation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reorientation_K2_0.2_T100.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "B_x",
          "Sz_over_S",
          "Sx_over_S",
          "theta_norm"
        ],
        "units": {
          "B_x": "J",
          "Sz_over_S": "dimensionless",
          "Sx_over_S": "dimensionless",
          "theta_norm": "dimensionless (angle/(pi/2))"
        }
      },
      "description": "Normalized magnetizations and reorientation angle vs transverse field for K2=0.2, T=100"
    },
    {
      "file": "reorientation_K2_0.5_T4.9.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "B_x",
          "Sz_over_S",
          "Sx_over_S",
          "theta_norm"
        ],
        "units": {
          "B_x": "J",
          "Sz_over_S": "dimensionless",
          "Sx_over_S": "dimensionless",
          "theta_norm": "dimensionless (angle/(pi/2))"
        }
      },
      "description": "Normalized magnetizations and reorientation angle vs transverse field for K2=0.5, T=4.9"
    }
  ],
  "notes": "Each CSV must contain at least 20 rows uniformly spanning the specified B_x range. The checker compares each agent-reported value to hidden reference values digitised from the paper's figures. An absolute tolerance of 0.05 is applied for every component. For the K2=0.5 case, the checker also verifies that theta_norm is monotonically non-decreasing, confirming a continuous reorientation."
}
```

## How you are scored
A hidden verifier independently processes each CSV. For the first parameter set, it checks that your reported Sz/S, Sx/S, and angle values at selected B_x points agree with reference values derived from the original work within an appropriate tolerance. For the second set, it additionally verifies that the angle curve is monotonically non-decreasing, confirming a continuous reorientation transition. Your final score is a weighted combination of these checks across both artifacts; simply reporting numbers that match the reference targets without implementing the correct physics will not pass.
