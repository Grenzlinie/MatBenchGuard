# Phase Diagram and Critical Exponents from Renormalization Group and Finite-Size Scaling

## Problem background
The Ashkin-Teller model is a two-dimensional classical lattice spin system (or its one-dimensional quantum Hamiltonian version) that generalises the Ising and Potts models. Its phase diagram is rich, with paramagnetic, partially ordered, fully ordered, and antiferromagnetic phases, as well as a line of critical points where the correlation-length critical exponent varies continuously. The Hamiltonian version is defined by couplings λ₁, λ₂ (two-spin interactions) and transverse fields h₁, h₂. Determining the phase boundaries, the locations and nature of the fixed points (including the four-state Potts point), and the critical exponent ν along the critical line is a challenge that requires numerical methods. This task computes these quantities using renormalisation group iteration and finite-size scaling on finite rings.

## Approach
Two complementary numerical approaches are used. First, real-space renormalisation group (RG) transformations: a self-dual transformation that iterates recursion relations derived from a cell eigenvalue problem to locate non-trivial fixed points and compute the thermal eigenvalue and ν; and a non-dual block transformation for blocks of size N=2,3,4 that yields improved estimates of the fixed-point properties and the marginal eigenvalue. Second, finite-size scaling: construct the Ashkin-Teller Hamiltonian for rings of length N=2,…,6 with periodic boundary conditions on the surface λ₂/λ₁ = h₂/h₁, diagonalise numerically to obtain low-lying eigenvalues, then form mass gaps between symmetry subspaces. Critical couplings are found where the scaled gap ratio (N-1)G_{N-1}/(N G_N) equals 1, and the critical exponent ν is extracted from the slope of the Callan-Symanzik β-function at the critical point. The workflow produces three scored outputs: fixed-point coordinates and critical properties from the RG analysis, the phase diagram on the restricted surface, and ν along the critical line.

## Reproduction target
Produce three numerical artifacts:

1. `rg_results.json` – a JSON file containing fixed-point ratios (h₁/λ₁, h₂/λ₁, λ₂/λ₁), thermal eigenvalues, and the correlation-length exponent ν obtained from both the self-dual and block RG transformations. For the block RG, include results for block sizes 2, 3, and 4 and report the marginal eigenvalue where applicable.
2. `fss_phase_diagram.csv` – a CSV table of the critical couplings h₁/λ₁ as a function of λ₂/λ₁ on the surface λ₂/λ₁ = h₂/h₁, identifying the phase regions (paramagnetic, partially ordered, fully ordered). Cover a range of λ₂/λ₁ that includes the Potts point and the ‘critical fan’ region.
3. `fss_nu.csv` – a CSV table of the critical exponent ν as a function of λ₂/λ₁ along the critical line, extracted from finite-size scaling of the mass gaps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: RG fixed point analysis
- Role: scored
- Action: Starting from the Ashkin-Teller Hamiltonian with couplings λ₁, λ₂, h₁, h₂, construct the cell eigenvalue problem and derive the duality-conserving recursion relations. Solve the cell eigenvalue problem and iterate the relations to find non-trivial fixed points. Also apply block-transformation RG for block sizes 2, 3, and 4, solving the corresponding eigenvalue problems. For each fixed point, compute the thermal eigenvalue and the correlation-length exponent ν from the linearized recursion relations. Save all fixed-point coordinates and critical properties to rg_results.json.
- Output file: `/app/outputs/rg_results.json`
- Format: json
- Contract: JSON containing fixed-point coordinates and critical properties from self-dual and block RG.
- Scoring: scored by hidden verifier

### Step 2: Finite-chain Hamiltonian diagonalization
- Role: process
- Action: Construct the Ashkin-Teller Hamiltonian for finite rings (lengths N=2,3,4,5,6) with periodic boundary conditions, restricted to the surface λ₂/λ₁ = h₂/h₁. For a range of λ₂/λ₁, compute the low-lying energy eigenvalues in each symmetry subspace using a sparse eigensolver. Save eigenvalues for later scaling steps.
- Evidence: `/app/outputs/eigenvalues.npz`

### Step 3: Phase boundary determination via finite-size scaling
- Role: scored (load-bearing)
- Action: From the previously computed eigenvalues, form mass gaps G_N between relevant low-lying states. For each λ₂/λ₁, find the critical h₁/λ₁ where (N-1)G_{N-1}/(N G_N) = 1 for pairs of chain lengths up to N=6; extrapolate to infinite N to obtain the thermodynamic critical couplings. Determine phase boundaries on the surface λ₂/λ₁ = h₂/h₁. Output the phase diagram to fss_phase_diagram.csv.
- Output file: `/app/outputs/fss_phase_diagram.csv`
- Format: csv
- Contract: Phase diagram on the surface λ₂/λ₁ = h₂/h₁.
- Scoring: scored by hidden verifier

### Step 4: Critical exponent calculation via finite-size scaling
- Role: scored
- Action: Compute the Callan-Symanzik β-function from the mass gaps and extract the correlation length critical exponent ν as a function of λ₂/λ₁ along the critical line. Output ν values to fss_nu.csv.
- Output file: `/app/outputs/fss_nu.csv`
- Format: csv
- Contract: Critical exponent ν along the critical line.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rg_results.json`
- `/app/outputs/fss_phase_diagram.csv`
- `/app/outputs/fss_nu.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rg_results.json
- path: `/app/outputs/rg_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fixed points and critical properties from self-dual and block renormalization group.
- schema:
  - `type`: object
  - `required`: `self_dual_fixed_points`, `block_fixed_points`
  - `properties`:
    - `self_dual_fixed_points`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `name`:
            - `type`: string
          - `h1_over_lambda1`:
            - `type`: number
          - `h2_over_lambda1`:
            - `type`: number
          - `lambda2_over_lambda1`:
            - `type`: number
          - `thermal_eigenvalue`:
            - `type`: number
          - `nu`:
            - `type`: number
    - `block_fixed_points`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `name`:
            - `type`: string
          - `block_size`:
            - `type`: integer
          - `a`:
            - `type`: number
          - `b`:
            - `type`: number
          - `x_equal_y`:
            - `type`: number
          - `nu`:
            - `type`: number
          - `lambda_t2`:
            - `type`: number

### fss_phase_diagram.csv
- path: `/app/outputs/fss_phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Phase boundaries on the surface λ₂/λ₁ = h₂/h₁.
- schema:
  - `type`: table
  - `required_columns`: `lambda2_lambda1`, `h1_lambda1_critical`, `phase_region`
  - `units`:
    - `lambda2_lambda1`: dimensionless ratio
    - `h1_lambda1_critical`: dimensionless ratio
    - `phase_region`: string category

### fss_nu.csv
- path: `/app/outputs/fss_nu.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Critical exponent ν as a function of λ₂/λ₁ along the critical line.
- schema:
  - `type`: table
  - `required_columns`: `lambda2_lambda1`, `nu`
  - `units`:
    - `lambda2_lambda1`: dimensionless ratio
    - `nu`: dimensionless exponent

Notes: Hidden checker compares reported values to predetermined reference results within tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rg_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "self_dual_fixed_points",
          "block_fixed_points"
        ],
        "properties": {
          "self_dual_fixed_points": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "h1_over_lambda1": {
                  "type": "number"
                },
                "h2_over_lambda1": {
                  "type": "number"
                },
                "lambda2_over_lambda1": {
                  "type": "number"
                },
                "thermal_eigenvalue": {
                  "type": "number"
                },
                "nu": {
                  "type": "number"
                }
              }
            }
          },
          "block_fixed_points": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "block_size": {
                  "type": "integer"
                },
                "a": {
                  "type": "number"
                },
                "b": {
                  "type": "number"
                },
                "x_equal_y": {
                  "type": "number"
                },
                "nu": {
                  "type": "number"
                },
                "lambda_t2": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Fixed points and critical properties from self-dual and block renormalization group."
    },
    {
      "file": "fss_phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda2_lambda1",
          "h1_lambda1_critical",
          "phase_region"
        ],
        "units": {
          "lambda2_lambda1": "dimensionless ratio",
          "h1_lambda1_critical": "dimensionless ratio",
          "phase_region": "string category"
        }
      },
      "description": "Phase boundaries on the surface λ₂/λ₁ = h₂/h₁."
    },
    {
      "file": "fss_nu.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda2_lambda1",
          "nu"
        ],
        "units": {
          "lambda2_lambda1": "dimensionless ratio",
          "nu": "dimensionless exponent"
        }
      },
      "description": "Critical exponent ν as a function of λ₂/λ₁ along the critical line."
    }
  ],
  "notes": "Hidden checker compares reported values to predetermined reference results within tolerances."
}
```

## How you are scored
Each scored workflow step produces an artifact under `/app/outputs`. A hidden verifier reads those files and compares the reported quantities to reference values using appropriate tolerances. The verifier checks, for example, that the fixed-point ratios, thermal eigenvalues, and ν from the RG match the expected results; that the phase diagram includes the correct phases and that the Potts point appears near the expected location; and that ν along the critical line shows the correct trend. The reward is a weighted combination of the scores from the individual artifacts. Reporting plausible numbers without actually implementing the methods will not pass the verifier.
