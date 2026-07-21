# Generalized FK Model Phase Diagram: Tongue Splitting and Symmetry Types

## Problem background
Commensurate-incommensurate (CI) transitions and modulated phases in one-dimensional systems are widely studied using the Frenkel-Kontorova (FK) model. This task considers a generalized FK model with a double-well interatomic interaction and a perturbed sinusoidal external potential. For model 1, when the period D of the external potential is less than or equal to the inter-well distance, the rational 'tongues' in the phase diagram can split into subregions with distinct atomic symmetry types (A-type and B-type) while the rotation number Ω remains constant. Understanding the structure of these split tongues and the associated symmetry labels requires ground-state calculations across a range of misfit γ and coupling strength K. We will computationally reproduce the ground-state analysis for one specific parameter regime and build the corresponding phase diagram.

## Approach
The ground states are obtained via the effective potential eigenvalue method. The atomic positions U_n are reduced to coordinates u_n that folded into the interval [-D/2, D/2]. An unknown effective potential R(u) and an eigenvalue λ are determined by solving a self‑consistent eigenvalue equation that minimizes the total energy. Numerically, we discretize u and solve the eigenvalue problem iteratively for a given period Q (≤5, as in the paper). From the converged configuration {u_i}, we compute the winding number ω as the fraction P/Q (the number of external potential periods traversed across Q atoms) and the rotation number Ω = (1/Q) Σ Θ(u_{i-1} − u_i), where Θ is the step function. The symmetry type is A if no atom sits at a maximum of the external potential V(x), and B if at least one atom occupies a maximum.

## Reproduction target
For model 1 with D = 0.5 and perturbation ε = 0.1, implement the ground‑state solver and compute the winding number ω, rotation number Ω, and symmetry type (A or B) at each of the following (K, γ) points:

(0.4, 0.67)
(1.4, 0.7)
(0.8, 0.65)
(1.2, 0.67)
(0.4, 0.7)
(0.7, 0.705)
(1.2, 0.71)
(1.4, 0.705)
(0.5, 0.6)
(1.0, 0.68)
(0.9, 0.72)
(0.6, 0.635)
(1.1, 0.69)
(0.3, 0.62)

Output a CSV file with columns K, gamma, omega, Omega, symmetry_type. Additionally, scan a grid of γ ∈ [0, 1] and K ∈ [0, 2] (suggest 200×200 points) to generate a phase diagram image that color‑codes each point by its rotation number Ω and visibly labels A and B symmetry regions.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/
- matplotlib: https://pypi.org/project/matplotlib/

## Workflow steps

### Step 1: Implement effective potential ground-state solver
- Role: process
- Action: Implement a numerical solver for the ground state of the generalized Frenkel-Kontorova model with double-well interatomic potential (model 1) using the effective potential eigenvalue method. For given parameters D=0.5, epsilon=0.1, misfit gamma, and strength K, find the periodic ground-state configuration {u_i}, period Q, and atomic positions. The solver must handle periods Q <= 5. Write a small proof-of-run log file solver_log.txt showing convergence for a few test points.
- Evidence: `/app/outputs/solver_log.txt`

### Step 2: Compute topological and symmetry characteristics for scored points
- Role: scored (load-bearing)
- Action: For each (K, gamma) pair specified in the instruction, use the ground-state solver to obtain the configuration. Compute the winding number ω (fraction P/Q), rotation number Ω (fraction), and symmetry type (A if no atom occupies a maximum of the external potential V(x), otherwise B). Output a CSV file model1_D0.5_results.csv with columns: K, gamma, omega, Omega, symmetry_type.
- Output file: `/app/outputs/model1_D0.5_results.csv`
- Format: csv
- Contract: CSV with header: K, gamma, omega, Omega, symmetry_type. Columns: K (float), gamma (float), omega (string in P/Q format), Omega (string in P/Q format), symmetry_type (string 'A' or 'B').
- Scoring: scored by hidden verifier

### Step 3: Generate phase diagram in (γ,K) plane
- Role: scored
- Action: Scan a grid of γ ∈ [0,1] and K ∈ [0,2] (suggest 200×200 points). For each grid point, compute the ground state and determine Ω and symmetry type using the solver. Produce a phase diagram figure: γ on the x-axis, K on the y-axis, points colored by Ω (distinct colormap), with visible markers (e.g., dashed lines or letters) to distinguish A and B symmetry regions. Save as phase_diagram.png.
- Output file: `/app/outputs/phase_diagram.png`
- Format: other
- Contract: PNG image with labeled axes, color-coded by rotation number Ω, and visible A/B symmetry annotations.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model1_D0.5_results.csv`
- `/app/outputs/phase_diagram.png`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model1_D0.5_results.csv
- path: `/app/outputs/model1_D0.5_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Scored ground-state quantities for model 1 at D=0.5: ω, Ω, symmetry type for given (K,γ) points. Values compared to hidden reference results.
- schema:
  - `type`: table
  - `required_columns`: `K`, `gamma`, `omega`, `Omega`, `symmetry_type`
  - `items`: object
  - `units`: object

### phase_diagram.png
- path: `/app/outputs/phase_diagram.png`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Phase diagram image for model 1 D=0.5 showing tongue splitting and A/B symmetry regions.
- schema:
  - `type`: other
  - `required`: object
  - `items`: object
  - `units`: object

Notes: Model 1 D=0.5 reproduction: tongue splitting, A/B symmetry types, and phase diagram. The agent must implement the effective potential method; no pre-existing FK solver is provided. Scored points include published and hidden (K,γ) values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model1_D0.5_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "K",
          "gamma",
          "omega",
          "Omega",
          "symmetry_type"
        ],
        "items": {},
        "units": {}
      },
      "description": "Scored ground-state quantities for model 1 at D=0.5: ω, Ω, symmetry type for given (K,γ) points. Values compared to hidden reference results."
    },
    {
      "file": "phase_diagram.png",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "required": {},
        "items": {},
        "units": {}
      },
      "description": "Phase diagram image for model 1 D=0.5 showing tongue splitting and A/B symmetry regions."
    }
  ],
  "notes": "Model 1 D=0.5 reproduction: tongue splitting, A/B symmetry types, and phase diagram. The agent must implement the effective potential method; no pre-existing FK solver is provided. Scored points include published and hidden (K,γ) values."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact and combines them into a final reward.

- **model1_D0.5_results.csv** (highest weight): Each row is compared against reference values for ω, Ω, and symmetry_type. ω and Ω are checked as exact fraction strings (e.g., '7/3'), and symmetry_type must be 'A' or 'B'. Points that are not published in the paper are included, so merely copying known entries from Table 1 will not suffice.
- **phase_diagram.png** (lower weight): The verifier checks that the image exists, has labeled axes, and shows a meaningful color mapping for Ω and distinguishable symmetry regions.

The overall reward reflects how many scored points are correct, with the CSV rows accounting for the dominant share. Reporting the paper's numbers without genuinely executing the solver will fail because the hidden points require an actual computation.
