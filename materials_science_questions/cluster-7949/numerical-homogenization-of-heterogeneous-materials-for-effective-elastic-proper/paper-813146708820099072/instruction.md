# Numerical Homogenization of Two-Phase Planar RVE: Energy Comparison of Voigt/Taylor, Reuss/Sachs, and Partial Rank-One Models

## Problem background
Phase-field models for solid‑solid phase transformations need a physically sound way to average the bulk energy inside interfacial regions where two phases coexist. The homogenization assumption chosen directly affects the driving force on the interface and therefore the predicted microstructure evolution. This task compares three different assumptions for a two‑phase representative volume element (RVE) containing a planar interface: the classic Voigt/Taylor model (uniform deformation gradient), the Reuss/Sachs model (uniform stress), and a partial rank‑one convexification model that enforces both kinematic compatibility and traction continuity across the interface. The aim is to compute the fully relaxed effective Helmholtz energy of the RVE as a function of the interface orientation and to establish how each model responds to the mismatch between the Bain strains of the two phases.

## Approach
Each phase is described by an isotropic neo‑Hookean Helmholtz energy. The only difference between the phases is the Bain strain, given by the parameters α=1.0619, β=0.9178, γ=1.0231. The two Bain strains are related by a rotation Q and are designed such that the twinning equation has solutions at normal vectors parallel to the Cartesian axes e₁ and e₂ (coherent interfaces).

For each homogenization model, the average Helmholtz energy of the RVE is defined as a function of the macroscopic deformation gradient F and the internal variables that capture the jump of the deformation gradient across the interface. In the Voigt/Taylor model there are no internal variables (F(1)=F(2)=F). In the Reuss/Sachs model the full deformation gradient jump ΔF is the internal variable. In the partial rank‑one convexification model the jump is constrained to be of rank‑one form a⊗N, where N is the interface normal and a is the jump vector to be determined. The phase fraction is fixed to p=0.5.

Interfaces normal directions N are parameterized by polar angle θ and azimuthal angle φ on a grid that must include the coherent orientations (N = (±1,0,0) and N = (0,±1,0)) as well as several non‑coherent orientations. For each orientation, the energy functional is minimized numerically over F (and over the internal variables for the Reuss/Sachs and partial rank‑one models) to obtain the fully relaxed Helmholtz energy. The three models are evaluated at identical orientations, and the resulting energies for all orientations and models are recorded in a single CSV file.

## Reproduction target
Produce a CSV file `orientation_energies.csv` with columns `theta`, `phi`, `energy_VoigtTaylor`, `energy_ReussSachs`, `energy_PartialRankOne`. Each row gives the relaxed Helmholtz energy for the three models at one interface normal direction N = (sinθ cosφ, sinθ sinφ, cosθ). The grid must cover at least the two coherent orientations (N = (±1,0,0) and N = (0,±1,0)) and several non‑coherent orientations. The energies must be the result of minimising the respective energy functional over the macroscopic deformation gradient and the relevant internal variables.

The hidden checker will verify that your submitted energies satisfy the physically expected relative trends for the three homogenization assumptions.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute effective Helmholtz energies for the planar interface RVE
- Role: scored (load-bearing)
- Action: Implement the Voigt/Taylor, Reuss/Sachs, and partial rank-one convexification homogenization models for a two-phase representative volume element with a planar interface. Use an isotropic neo-Hookean Helmholtz energy and Bain strains defined by parameters alpha=1.0619, beta=0.9178, gamma=1.0231. The phase fraction is p=0.5. For each model, define the average bulk Helmholtz energy as a function of the macroscopic deformation gradient F and the internal variables (full deformation gradient jump for Reuss/Sachs, jump vector a for partial rank-one model). Generate a grid of interface normal directions N parameterized by polar angle theta and azimuthal angle phi. For each orientation, numerically minimize the energy functional over F and the internal variables to obtain the fully relaxed Helmholtz energy. Record the resulting energies for all orientations and models in a CSV file.
- Output file: `/app/outputs/orientation_energies.csv`
- Format: csv
- Contract: Columns: theta (float, radians), phi (float, radians), energy_VoigtTaylor (float), energy_ReussSachs (float), energy_PartialRankOne (float). Each row corresponds to a distinct interface normal direction N = (sin(theta)cos(phi), sin(theta)sin(phi), cos(theta)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/orientation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### orientation_energies.csv
- path: `/app/outputs/orientation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing the fully relaxed Helmholtz energies for the three homogenization models as a function of interface orientation. Used to verify energy ordering (Voigt/Taylor >= partial rank-one >= Reuss/Sachs), constancy of Voigt/Taylor and Reuss/Sachs energies, and that minima of the partial rank-one model occur at coherent orientations.
- schema:
  - `type`: table
  - `required_columns`: `theta`, `phi`, `energy_VoigtTaylor`, `energy_ReussSachs`, `energy_PartialRankOne`
  - `columns`:
    - `theta`:
      - `type`: float
      - `unit`: radians
      - `description`: Polar angle of interface normal vector N
    - `phi`:
      - `type`: float
      - `unit`: radians
      - `description`: Azimuthal angle of interface normal vector N
    - `energy_VoigtTaylor`:
      - `type`: float
      - `description`: Fully relaxed Helmholtz energy for Voigt/Taylor model
    - `energy_ReussSachs`:
      - `type`: float
      - `description`: Fully relaxed Helmholtz energy for Reuss/Sachs model
    - `energy_PartialRankOne`:
      - `type`: float
      - `description`: Fully relaxed Helmholtz energy for partial rank-one convexification model

Notes: The checker will verify structural properties of the submitted CSV without comparing to absolute hidden gold values. The task only requires the planar interface RVE analysis; the 1D example and spherical inclusion FEM are excluded as noted in the plan.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "orientation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "phi",
          "energy_VoigtTaylor",
          "energy_ReussSachs",
          "energy_PartialRankOne"
        ],
        "columns": {
          "theta": {
            "type": "float",
            "unit": "radians",
            "description": "Polar angle of interface normal vector N"
          },
          "phi": {
            "type": "float",
            "unit": "radians",
            "description": "Azimuthal angle of interface normal vector N"
          },
          "energy_VoigtTaylor": {
            "type": "float",
            "description": "Fully relaxed Helmholtz energy for Voigt/Taylor model"
          },
          "energy_ReussSachs": {
            "type": "float",
            "description": "Fully relaxed Helmholtz energy for Reuss/Sachs model"
          },
          "energy_PartialRankOne": {
            "type": "float",
            "description": "Fully relaxed Helmholtz energy for partial rank-one convexification model"
          }
        }
      },
      "description": "CSV file containing the fully relaxed Helmholtz energies for the three homogenization models as a function of interface orientation. Used to verify energy ordering (Voigt/Taylor >= partial rank-one >= Reuss/Sachs), constancy of Voigt/Taylor and Reuss/Sachs energies, and that minima of the partial rank-one model occur at coherent orientations."
    }
  ],
  "notes": "The checker will verify structural properties of the submitted CSV without comparing to absolute hidden gold values. The task only requires the planar interface RVE analysis; the 1D example and spherical inclusion FEM are excluded as noted in the plan."
}
```

## How you are scored
A hidden verifier reads your `orientation_energies.csv` and checks that the energies satisfy the physically expected relative trends and orderings for the three homogenization models. Your reward is based on how well your computed energies reproduce these trends; tolerances and exact criteria are hidden. Reporting paper‑reported numbers without correct minimisation will not pass.
