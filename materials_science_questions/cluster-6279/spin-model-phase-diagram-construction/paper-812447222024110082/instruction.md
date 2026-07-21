# MKRG Phase Diagram for p=7 Clock Model with Dipolar and Quadrupolar Interactions

## Problem background
Two-dimensional spin models with discrete symmetry exhibit rich phase behaviour due to the competition between dipolar and quadrupolar interactions. A particular class is the p-state clock model, where each spin can take p equally spaced orientations on a circle. For pure dipolar coupling, the model is known to support a massless (algebraically ordered) phase for sufficiently large p, separating the high-temperature disordered phase from the low-temperature dipolar phase. When an additional quadrupolar coupling is introduced, the phase diagram in the plane of coupling ratio and temperature can become more complex. Our goal is to compute the finite-temperature phase diagram of the odd p=7 clock model with both dipolar (J) and quadrupolar (K) interactions, and to determine the number and location of triple points where three phases (disorder, massless, dipolar) meet, as well as the sequence of transitions as the coupling ratio α = K/J is varied.

## Approach
We use the Migdal-Kadanoff renormalization group (MKRG), a real-space renormalization method that approximates the partition function by bond-moving followed by decimation of alternate sites. With a spatial rescaling factor b = 2, the renormalized Boltzmann factor f(θ) is obtained from the initial interaction potential V(θ) = βJ[1 − cos θ] + βK[1 − cos²θ] through an iterative trace over the intermediate spin angle φ. The recursion is applied numerically on a discrete grid of θ values covering the p=7 clock states. At each point in the (α, T) plane (α = K/J, temperature k_B T/J) we iterate the recursion until the distribution of f(θ) converges to a fixed point. The nature of the fixed point determines the phase: a uniform f(θ) → 1 corresponds to the disordered (high-temperature) phase; f(θ) → 0 for all θ ≠ 0 signals the dipolar (ordered) phase; and an irregular f(θ) with some values exceeding 1 indicates the massless (Kosterlitz-Thouless) phase. Scanning a suitable grid of (α, T) yields a full phase map from which we can locate the boundaries between phases and any triple points where three phases meet.

## Reproduction target
For the p=7 clock model, produce the phase diagram in the (α = K/J, k_B T/J) plane by scanning a sufficiently fine grid of α and temperature. Determine the two triple points where the disordered, massless, and dipolar phases meet, and report their coordinates (α, T). Extract the transition lines: for each α, find the critical temperatures for the disorder – massless (KT) transition and for the massless – dipolar (or disorder – dipolar) transition. The final outputs are a JSON file containing the two triple-point coordinates, and a CSV file listing the phase boundary points with transition type ('KT' or 'dipolar'). The required phase sequence – two distinct transitions outside a certain α interval, and a single transition inside it – should emerge from these data.

## Assets
This task is entirely compute-driven; no external datasets, models, or pre-built resources are required. The agent may implement the MKRG recursion from scratch using standard scientific Python libraries (e.g., NumPy, SciPy). The Hamiltonian and the recursion relation are described in the Approach section. No pre‑downloaded files are needed.

## Workflow steps

### Step 1: MKRG simulation
- Role: process
- Action: Implement the Migdal-Kadanoff renormalization group recursion for the p-state clock model with dipolar and quadrupolar interactions, using p=7. Scan a grid of α = K/J and dimensionless temperature k_B T/J. At each grid point, iterate the renormalization until the Boltzmann factor f(θ) converges. Classify the phase as disordered, dipolar, or massless according to the fixed-point behavior described in the literature. Save the full grid of phase labels to an intermediate NumPy file.
- Evidence: `/app/outputs/phase_grid.npy`

### Step 2: Locate triple points
- Role: scored (load-bearing)
- Action: Using the phase grid from the previous step, identify the two triple points where the disorder, massless, and dipolar phase boundaries meet. Record the coordinates (α, k_B T/J) of α_A and α_B. Output the result as a JSON file with keys p, alpha_A, T_A, alpha_B, T_B.
- Output file: `/app/outputs/triple_points.json`
- Format: json
- Contract: {"type": "object", "properties": {"p": {"type": "integer"}, "alpha_A": {"type": "number"}, "T_A": {"type": "number"}, "alpha_B": {"type": "number"}, "T_B": {"type": "number"}}, "required": ["p", "alpha_A", "T_A", "alpha_B", "T_B"]}
- Scoring: scored by hidden verifier

### Step 3: Phase boundary extraction
- Role: scored
- Action: Using the same phase grid, extract the phase boundary lines. For each α, determine the critical temperatures for the disorder–massless (Kosterlitz-Thouless) transition and the massless–dipolar (or disorder–dipolar) transition. Label each boundary point with 'KT' or 'dipolar'. Output a CSV file with columns alpha, temperature, transition_type.
- Output file: `/app/outputs/phase_boundary.csv`
- Format: csv
- Contract: {"type": "table", "required_columns": ["alpha", "temperature", "transition_type"], "columns": {"alpha": {"type": "float"}, "temperature": {"type": "float"}, "transition_type": {"type": "string"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/triple_points.json`
- `/app/outputs/phase_boundary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### triple_points.json
- path: `/app/outputs/triple_points.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Coordinates of the two triple points for the odd p=7 clock model, obtained from the MKRG simulation.
- schema:
  - `type`: object
  - `properties`:
    - `p`:
      - `type`: integer
    - `alpha_A`:
      - `type`: number
    - `T_A`:
      - `type`: number
    - `alpha_B`:
      - `type`: number
    - `T_B`:
      - `type`: number
  - `required`: `p`, `alpha_A`, `T_A`, `alpha_B`, `T_B`

### phase_boundary.csv
- path: `/app/outputs/phase_boundary.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phase boundary points in the (alpha, temperature) plane; transition_type is 'KT' for Kosterlitz-Thouless (disorder–massless) and 'dipolar' for the dipolar transition.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `temperature`, `transition_type`
  - `columns`:
    - `alpha`:
      - `type`: float
    - `temperature`:
      - `type`: float
    - `transition_type`:
      - `type`: string
      - `enum`: `KT`, `dipolar`

Notes: The scored outputs together verify the central claim: for p=7, the phase diagram exhibits two triple points and distinct transition sequences depending on alpha. The checker will validate the structural pattern (two transitions outside the triple-point interval, one inside) and compare triple point coordinates against hidden reference values within a tolerance suitable for a different implementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "triple_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "p": {
            "type": "integer"
          },
          "alpha_A": {
            "type": "number"
          },
          "T_A": {
            "type": "number"
          },
          "alpha_B": {
            "type": "number"
          },
          "T_B": {
            "type": "number"
          }
        },
        "required": [
          "p",
          "alpha_A",
          "T_A",
          "alpha_B",
          "T_B"
        ]
      },
      "description": "Coordinates of the two triple points for the odd p=7 clock model, obtained from the MKRG simulation."
    },
    {
      "file": "phase_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "temperature",
          "transition_type"
        ],
        "columns": {
          "alpha": {
            "type": "float"
          },
          "temperature": {
            "type": "float"
          },
          "transition_type": {
            "type": "string",
            "enum": [
              "KT",
              "dipolar"
            ]
          }
        }
      },
      "description": "Phase boundary points in the (alpha, temperature) plane; transition_type is 'KT' for Kosterlitz-Thouless (disorder–massless) and 'dipolar' for the dipolar transition."
    }
  ],
  "notes": "The scored outputs together verify the central claim: for p=7, the phase diagram exhibits two triple points and distinct transition sequences depending on alpha. The checker will validate the structural pattern (two transitions outside the triple-point interval, one inside) and compare triple point coordinates against hidden reference values within a tolerance suitable for a different implementation."
}
```

## How you are scored
A hidden verifier independently scores each output artifact and combines the scores into a final reward (float between 0 and 1). The triple-point coordinates in `triple_points.json` are compared to pre‑registered reference values within a tolerance that accounts for legitimate implementation differences (grid resolution, solver details). The phase-boundary file `phase_boundary.csv` is audited structurally: the verifier checks that for α values outside a certain interval the boundary contains two distinct transition lines (one labelled 'KT', one 'dipolar'), while for α values inside that interval there is only a single 'dipolar' transition line. Additionally, the verifier may extract the triple-point locations from the boundary data and compare them to its reference. Reporting a self‑consistent set of outputs that match the expected qualitative structure and reasonable numeric values yields full credit; supplying only one scored artifact or producing substantially incorrect triple-point locations reduces the reward.
