# Phase diagram of 2D Coulomb plasma from Gaussian variational method

## Problem background
The two-dimensional classical Coulomb plasma (2D CPM) consists of positive and negative charges interacting via a logarithmic potential, with overall charge neutrality. At low temperature the charges are bound into neutral dipole pairs (insulator), while at high temperature they unbind into a conductive plasma. The charge-unbinding transition is known to be a Kosterlitz-Thouless (KT) continuous transition at small fugacity, but its nature can change at higher fugacity. By mapping the 2D CPM to the (1+1)-dimensional quantum sine-Gordon model, the grand canonical potential can be expressed in terms of a single order parameter. The goal is to numerically compute the phase diagram in the fugacity–temperature plane, identifying the boundaries between insulator and plasma phases, and to determine whether the transition is continuous or first-order for different fugacities.

## Approach
The method uses a Gaussian variational wave functional to approximate the ground state of the equivalent (1+1)D quantum sine-Gordon model. The grand canonical potential density Ω(ξ) is derived as a function of a renormalized order parameter ξ:

Ω(ξ) = (T/a²)[ (1/(4π)) √(1 + 4πzξ/T) - 2z K(ξ) - 1/(4π) ]

with

K(ξ) = exp[ - (1/(2T)) ln((1 + √(1 + 4πzξ/T)) / √(4πzξ/T)) ]

The lattice scale a cancels in the transition conditions and is set to 1 for convenience. The stable state is found by solving dΩ/dξ = 0 and requiring d²Ω/dξ² > 0. The continuous KT transition line is located where the stable non-zero solution disappears (merging with the unstable branch at d²Ω/dξ²=0). The first-order transition line is where the zero-solution and the finite-ξ solution have equal grand potential, Ω(0) = Ω(ξ). The tricritical point is the meeting point of these two lines. The computation involves scanning a grid of fugacity z ∈ (0,1] and temperature T ∈ [0.1,0.5], solving for stationary points numerically, and post-processing to extract the boundaries.

## Reproduction target
Produce two artifacts:
1. `transition_lines.csv` containing (z,T) points along the continuous (KT) and first-order phase boundaries, with an integer transition_type (0 for continuous, 1 for first-order).
2. `tricritical_point.json` giving the coordinates (z*, T*) of the tricritical point where the two lines meet.
The results must be self-consistently derived from the numerical solution of the variational equations. The CSV should sample enough points to resolve the curves over z∈(0,1] and T∈[0.1,0.5].

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve variational equations and determine stable states
- Role: process
- Action: Implement the grand canonical potential Ω(ξ) as a function of fugacity z and temperature T (set a=1). Define K(ξ) using the paper's Gaussian variational cosine expectation. On a grid of (z,T) covering z∈(0,1] and T∈[0.1,0.5], numerically solve dΩ/dξ=0 for stationary points ξ. Among these, retain stable states (d²Ω/dξ²>0) and record the zero-solution Ω(0). Save the computed stable ξ and Ω values for every (z,T) in an internal file.
- Evidence: `/app/outputs/stable_states.npz`

### Step 2: Generate phase diagram transition lines
- Role: scored (load-bearing)
- Action: From the stable-state data, locate the continuous Kosterlitz-Thouless transition line: for each z, find the temperature where the stable non-zero solution merges with the unstable branch (d²Ω/dξ²=0). Locate the first-order transition line: for each z, find the temperature where Ω(0)=Ω(ξ) for the stable non-zero solution. Collect these boundary points as (z,T) pairs and label them with transition_type=0 (continuous) or 1 (first-order). Write the result to transition_lines.csv.
- Output file: `/app/outputs/transition_lines.csv`
- Format: csv
- Contract: Columns: z (float, dimensionless fugacity), T (float, dimensionless temperature), transition_type (integer, 0 for continuous/KT line, 1 for first-order line). Each row is one sampled point on the respective boundary.
- Scoring: scored by hidden verifier

### Step 3: Identify tricritical point
- Role: scored
- Action: From the extracted transition lines, determine the coordinates (z*, T*) where the continuous line ends and the first-order line begins—the tricritical point. Save as a JSON object.
- Output file: `/app/outputs/tricritical_point.json`
- Format: json
- Contract: Keys: 'z_star' (float, dimensionless fugacity), 'T_star' (float, dimensionless temperature).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_lines.csv`
- `/app/outputs/tricritical_point.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_lines.csv
- path: `/app/outputs/transition_lines.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Points on the continuous (KT) and first-order transition lines in the fugacity-temperature plane.
- schema:
  - `type`: table
  - `required_columns`: `z`, `T`, `transition_type`
  - `units`:
    - `z`: dimensionless fugacity
    - `T`: dimensionless temperature
    - `transition_type`: integer flag (0=continuous, 1=first-order)

### tricritical_point.json
- path: `/app/outputs/tricritical_point.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Coordinates (z*, T*) of the tricritical point.
- schema:
  - `type`: object
  - `required`:
    - `z_star`: float
    - `T_star`: float

Notes: The transition_lines.csv points must satisfy the marginal-stability envelope (continuous line) or the equal-potential condition (first-order line) within prescribed tolerances. The tricritical point is compared to the exact values derived in the paper. The agent should generate a dense enough (z,T) grid to resolve the transition curves smoothly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_lines.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "T",
          "transition_type"
        ],
        "units": {
          "z": "dimensionless fugacity",
          "T": "dimensionless temperature",
          "transition_type": "integer flag (0=continuous, 1=first-order)"
        }
      },
      "description": "Points on the continuous (KT) and first-order transition lines in the fugacity-temperature plane."
    },
    {
      "file": "tricritical_point.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "z_star": "float",
          "T_star": "float"
        }
      },
      "description": "Coordinates (z*, T*) of the tricritical point."
    }
  ],
  "notes": "The transition_lines.csv points must satisfy the marginal-stability envelope (continuous line) or the equal-potential condition (first-order line) within prescribed tolerances. The tricritical point is compared to the exact values derived in the paper. The agent should generate a dense enough (z,T) grid to resolve the transition curves smoothly."
}
```

## How you are scored
A hidden verifier independently reads your output files. It recomputes the marginal-stability envelope condition for points on the continuous line (checking that the point satisfies the merger criterion) and the equal-potential condition for points on the first-order line. The tricritical point is compared against the exact analytic value. The verifier combines these checks into a single reward: full credit (1.0) if all points are correct within the specified tolerance, otherwise 0.0. The verifier does not trust your reported numbers alone; it assesses whether the underlying data satisfy the physical transition conditions. Simply stating the paper's reported coordinates without correct computed data will not pass the check.
