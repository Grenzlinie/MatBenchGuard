# Torsional rigidity and stress intensity factors for cracked bars under torsion

## Problem background
Saint-Venant torsion of prismatic bars with a rectangular cross-section and an isotropic coating is a classic problem in elasticity. When the bar contains cracks, stress concentrations near crack tips reduce the effective torsional stiffness and can lead to fracture. Two quantities of primary engineering interest are the torsional rigidity of the bar and the mode III stress intensity factor (SIF) at crack tips. This task computes both for a rectangular bar with a coating under two crack configurations, using a semi-analytical approach based on a series solution for a Volterra screw dislocation and a distributed dislocation model.

## Approach
The computational procedure proceeds in several stages. First, implement the analytic series expressions for anti-plane shear stresses (τ_xz and τ_yz) caused by a single Volterra screw dislocation embedded in a coated rectangular bar. These formulas, derived from the warping function via Fourier series, involve the material shear moduli, bar and coating dimensions, and the dislocation position. The series are re‑summed into rapidly converging forms with the help of auxiliary functions. Second, build a solver for an arbitrary smooth crack by modeling the crack as a continuous distribution of dislocations with unknown density. This yields a system of Cauchy singular integral equations, which is discretized via the Erdogan method and solved numerically to obtain dislocation density functions. From these densities the torsional rigidity and mode III stress intensity factors are evaluated. Finally, apply the solver to two specific crack configurations: (1) a homogeneous bar with an edge crack bisecting and perpendicular to one side; (2) a coated bar with a straight inclined edge crack emanating from the midpoint of the left side. For each case, compute the desired quantities at a range of crack lengths and save the results in structured CSV files.

## Reproduction target
Produce the following four CSV artifacts:

- homogeneous_torsional_rigidity.csv, columns l/a and normalized_D (10^4 D/(μ1 a^4)) for l/a = 0.05, 0.1, 0.3, 0.5, 0.7, 0.9 for the homogeneous edge‑crack configuration.
- homogeneous_sif.csv, columns l/a and normalized_SIF (kIII a^{2.5}/M) for the same l/a values and configuration.
- coated_torsional_rigidity.csv, columns l/a and normalized_D for l/a = 0.1, 0.2, 0.3, 0.5, 0.7, 0.9 for the coated inclined‑crack configuration.
- coated_sif.csv, columns l/a and normalized_SIF for the same l/a values and configuration.

The homogeneous configuration uses μ=1, h1=0.5a, a=1, h2=0, with an edge crack that bisects one side perpendicularly (crack line from X=0 to X=l at Y=h1/2). The coated configuration uses μ2/μ1=80/26, h1=0.5a, h2=0.1a, a=1, with a crack from the midpoint of the left side (X=0, Y=h1/2) extending horizontally to the right. All results must be computed by re‑implementing the dislocation stress kernel and the singular integral equation solver, not by reading off pre‑existing values.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement screw dislocation stress kernel
- Role: process
- Action: Implement the series expressions for anti-plane stress components τ_Xz and τ_Yz as functions of geometry (a, h1, h2), material shear moduli (μ1, μ2), dislocation location (ξ, η), and field point (X, Y), using the analytical Fourier coefficients and the definitions of Γ_n and Ω_n. This kernel will later be used in the distributed dislocation formulation.
- Evidence: `/app/outputs/stress_kernel_verification.log`

### Step 2: Build distributed dislocation solver
- Role: process
- Action: Implement the Cauchy singular integral equation system for an arbitrary smooth crack described parametrically, discretize the equations via the Erdogan method, solve for dislocation density functions, and compute the torsional rigidity D and mode III stress intensity factors kIII.
- Evidence: `/app/outputs/solver_verification.log`

### Step 3: Homogeneous case – torsional rigidity
- Role: scored (load-bearing)
- Action: For a homogeneous bar (μ=1, h1=0.5a, a=1, h2=0) with an edge crack bisecting and perpendicular to one side (crack line from X=0 to X=l at Y=h1/2), compute 10^4 D/(μ1 a^4) for l/a = 0.05, 0.1, 0.3, 0.5, 0.7, 0.9. Save results to homogeneous_torsional_rigidity.csv.
- Output file: `/app/outputs/homogeneous_torsional_rigidity.csv`
- Format: csv
- Contract: {'l/a': float, 'normalized_D': float}
- Scoring: scored by hidden verifier

### Step 4: Homogeneous case – stress intensity factor
- Role: scored
- Action: For the same homogeneous configuration, compute kIII a^{2.5} / M for the same l/a values and save to homogeneous_sif.csv.
- Output file: `/app/outputs/homogeneous_sif.csv`
- Format: csv
- Contract: {'l/a': float, 'normalized_SIF': float}
- Scoring: scored by hidden verifier

### Step 5: Coated case – torsional rigidity
- Role: scored
- Action: For a coated bar (μ2/μ1=80/26, h1=0.5a, h2=0.1a, a=1) with an inclined edge crack emanating from the midpoint of the left side (X=0, Y=h1/2) and extending horizontally toward the right side, compute 10^4 D/(μ1 a^4) for l/a = 0.1, 0.2, 0.3, 0.5, 0.7, 0.9. Save to coated_torsional_rigidity.csv.
- Output file: `/app/outputs/coated_torsional_rigidity.csv`
- Format: csv
- Contract: {'l/a': float, 'normalized_D': float}
- Scoring: scored by hidden verifier

### Step 6: Coated case – stress intensity factor
- Role: scored
- Action: For the same coated configuration, compute kIII a^{2.5} / M for the same l/a values and save to coated_sif.csv.
- Output file: `/app/outputs/coated_sif.csv`
- Format: csv
- Contract: {'l/a': float, 'normalized_SIF': float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/homogeneous_torsional_rigidity.csv`
- `/app/outputs/homogeneous_sif.csv`
- `/app/outputs/coated_torsional_rigidity.csv`
- `/app/outputs/coated_sif.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### homogeneous_torsional_rigidity.csv
- path: `/app/outputs/homogeneous_torsional_rigidity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized torsional rigidity for homogeneous bar with bisecting edge crack.
- schema:
  - `type`: table
  - `required_columns`: `l/a`, `normalized_D`
  - `units`:
    - `l/a`: dimensionless
    - `normalized_D`: dimensionless (10^4 D/(μ1 a^4))

### homogeneous_sif.csv
- path: `/app/outputs/homogeneous_sif.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized SIF for homogeneous crack.
- schema:
  - `type`: table
  - `required_columns`: `l/a`, `normalized_SIF`
  - `units`:
    - `l/a`: dimensionless
    - `normalized_SIF`: dimensionless (kIII a^{2.5}/M)

### coated_torsional_rigidity.csv
- path: `/app/outputs/coated_torsional_rigidity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized torsional rigidity for coated bar with inclined edge crack.
- schema:
  - `type`: table
  - `required_columns`: `l/a`, `normalized_D`
  - `units`:
    - `l/a`: dimensionless
    - `normalized_D`: dimensionless

### coated_sif.csv
- path: `/app/outputs/coated_sif.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized SIF for coated crack.
- schema:
  - `type`: table
  - `required_columns`: `l/a`, `normalized_SIF`
  - `units`:
    - `l/a`: dimensionless
    - `normalized_SIF`: dimensionless

Notes: All output files must be placed in /app/outputs. Values computed from proper implementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "homogeneous_torsional_rigidity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "l/a",
          "normalized_D"
        ],
        "units": {
          "l/a": "dimensionless",
          "normalized_D": "dimensionless (10^4 D/(μ1 a^4))"
        }
      },
      "description": "Normalized torsional rigidity for homogeneous bar with bisecting edge crack."
    },
    {
      "file": "homogeneous_sif.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "l/a",
          "normalized_SIF"
        ],
        "units": {
          "l/a": "dimensionless",
          "normalized_SIF": "dimensionless (kIII a^{2.5}/M)"
        }
      },
      "description": "Normalized SIF for homogeneous crack."
    },
    {
      "file": "coated_torsional_rigidity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "l/a",
          "normalized_D"
        ],
        "units": {
          "l/a": "dimensionless",
          "normalized_D": "dimensionless"
        }
      },
      "description": "Normalized torsional rigidity for coated bar with inclined edge crack."
    },
    {
      "file": "coated_sif.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "l/a",
          "normalized_SIF"
        ],
        "units": {
          "l/a": "dimensionless",
          "normalized_SIF": "dimensionless"
        }
      },
      "description": "Normalized SIF for coated crack."
    }
  ],
  "notes": "All output files must be placed in /app/outputs. Values computed from proper implementation."
}
```

## How you are scored
Your submitted CSV files will be evaluated by a hidden verifier that checks both the computed values and their physical trends. For the homogeneous case the verifier compares the normalized torsional rigidity and SIF values against reference results derived from an independent validated solution. For the coated case the verifier confirms that the torsional rigidity decreases monotonically with increasing crack length, that the SIF first increases then decreases (peaking at intermediate crack lengths), and that the numerical values fall within a plausible range. The final reward is an average over the four scored artifacts, with higher weight given to accurate values and correct trends. Simply reporting a number is not sufficient; the entire computational pipeline from the dislocation kernel through the singular‑integral‑equation solver must be correctly implemented to produce results that satisfy the checks.
