# Low-Temperature Bethe Expansion Coefficients and Phase Boundaries for the Chiral Clock Model

## Problem background
The three-state chiral clock (CC3) model is a layered spin system with ferromagnetic intra-layer interactions and competitively chirally coupled inter-layer interactions. At zero temperature a multiphase point exists where all sequences of spins satisfying a local rule are degenerate ground states. The finite-temperature phase diagram is complex and features modulated long-wavelength phases. A central question is to determine the structural coefficients of the low-temperature free-energy expansion and the resulting phase boundaries between the shortest-period modulated phases. This task focuses on computing those coefficients and phase-boundary temperatures from the Bethe approximation, a cluster variation method that improves upon mean-field theory.

## Approach
The Bethe approximation treats not only single-spin probabilities but also nearest-neighbor pair probabilities as independent variational parameters. The free energy is expressed in terms of these probabilities and minimized subject to consistency constraints, yielding equilibrium equations for the layer magnetizations and pair correlations. For the low-temperature regime, one expands the probabilities in small quantities around a ground state and iteratively solves the equilibrium equations to obtain a series for the free energy. Grouping the free energy into structural variables corresponding to bands of identical spin orientation reduces the minimization to a linear programming problem whose coefficients (structural coefficients) determine the phase stabilities. The numerical computation proceeds by minimizing the Bethe free energy directly via Newton iteration for candidate periodic magnetization patterns with periods up to four, using the first-order low-temperature mean-field expressions as initial guesses, on a grid of chirality Δ and temperature T. The free-energy crossings then locate the phase boundaries.

## Reproduction target
Implement the Bethe approximation for the CC3 model and produce two results. First, derive the low-temperature expansion of the free energy up to third order and compute the structural coefficients a0(1), a1(1), a∞(1), a1(2), a12(2), and a112(3) for the <2>, <1>, and <21> phases. Second, numerically minimize the Bethe free energy for the <2>, <1>, <21>, and <211> phases over a grid of Δ (0.4 to 0.5) and T (0 to 2.5 J) and determine the first-order phase boundary Δ(T) between <2> and <1> and the second-order phase boundary Δ(T) between <21> and <1>. Output the structural coefficients and the (Δ, T_c) points for each boundary. Additionally, verify the sign of the coefficient a112 on the <21>:<1> boundary to assess the low-temperature stability of the <211> phase.

## Assets

- Python 3 scientific environment: python3, numpy, scipy, sympy

## Workflow steps

### Step 1: Derive low-temperature expansion coefficients
- Role: scored
- Action: Set up the Bethe free energy and equilibrium equations, expand the small layer variables up to third order, and compute the structural coefficients a0(1), a1(1), a∞(1), a1(2), a12(2), a112(3).
- Output file: `/app/outputs/structural_coefficients.csv`
- Format: csv
- Contract: phase,coefficient,value,order
- Scoring: scored by hidden verifier

### Step 2: Numerically minimize Bethe free energy for short periods
- Role: process
- Action: Implement the Bethe free energy minimization for period‑2 (<2>), period‑1 (<1>), period‑3 (<21>), and period‑4 (<211>) magnetization patterns using Newton iteration. Use first-order low‑temperature mean‑field expressions as initial guesses. Compute converged free energy densities on a grid of Δ (0.4 to 0.5) and T (0 to 2.5 J).
- Evidence: `/app/outputs/free_energy_grid.csv`

### Step 3: Determine phase boundaries
- Role: scored (load-bearing)
- Action: From the free energy grid, locate the crossing points where the free energies of <2> and <1> become equal (first‑order boundary) and where <21> and <1> become equal (second‑order boundary). Output the corresponding (Δ, T_c) pairs.
- Output file: `/app/outputs/phase_boundaries.csv`
- Format: csv
- Contract: boundary,delta,T_c
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_coefficients.csv`
- `/app/outputs/phase_boundaries.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_coefficients.csv
- path: `/app/outputs/structural_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Low‑temperature expansion structural coefficients for <2>, <1>, <21> phases up to third order.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `coefficient`, `value`, `order`
  - `units`:
    - `value`: dimensionless

### phase_boundaries.csv
- path: `/app/outputs/phase_boundaries.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Phase boundary points (Δ, T_c) for the <2>:<1> first‑order and <21>:<1> second‑order transitions.
- schema:
  - `type`: table
  - `required_columns`: `boundary`, `delta`, `T_c`
  - `units`:
    - `delta`: dimensionless
    - `T_c`: energy (in units of J)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "coefficient",
          "value",
          "order"
        ],
        "units": {
          "value": "dimensionless"
        }
      },
      "description": "Low‑temperature expansion structural coefficients for <2>, <1>, <21> phases up to third order."
    },
    {
      "file": "phase_boundaries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "boundary",
          "delta",
          "T_c"
        ],
        "units": {
          "delta": "dimensionless",
          "T_c": "energy (in units of J)"
        }
      },
      "description": "Phase boundary points (Δ, T_c) for the <2>:<1> first‑order and <21>:<1> second‑order transitions."
    }
  ],
  "notes": ""
}
```

## How you are scored
Each scored workflow step produces a specific CSV file under /app/outputs. A hidden verifier will independently read your artifacts and compare the values you report against hidden gold references. The structural coefficients (step 1) are compared to reference values derived from the system’s exact low-temperature expansion; the phase boundaries (step 3) are compared to reference boundary points. For both metrics, the reward is monotonic in quality: meeting or exceeding the reference threshold earns full credit, and reward decreases linearly as the result deviates in the direction of worse performance. The final reward is a weighted combination: 0.5 from the structural coefficients and 0.5 from the phase boundaries. Do not attempt to hard-code any reference numbers—the verifier will score the outputs you compute after running the Bethe procedure.
