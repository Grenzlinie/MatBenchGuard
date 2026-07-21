# Phase Boundaries of the Spin-1 BEG Model on Bethe Lattice

## Problem background
The spin-1 Blume-Emery-Griffiths (BEG) model is defined by the Hamiltonian

$$ -\beta\mathcal{H} = J \sum_{\langle ij\rangle} s_i s_j + K \sum_{\langle ij\rangle} s_i^2 s_j^2 - \Delta \sum_i s_i^2 $$

with spin variables $s_i \in \{\pm 1, 0\}$. It describes multicomponent physical systems such as $^3$He–$^4$He mixtures, metamagnets, and liquid crystals. On a Bethe lattice with coordination number $z=4$, the model can be solved exactly using recursion relations, and its phase diagram exhibits diverse phases—disordered, ferromagnetic, antiquadrupolar, and ferrimagnetic—characterised by the order parameters of magnetisation $m$ and quadrupolar moment $q$. This task requires numerically solving the recursion equations to determine the phase boundaries for eight representative biquadratic coupling ratios, thereby mapping the possible phase transitions in the temperature–crystal-field plane.

## Approach
The reproduction follows a two‑stage procedure.

1. **Parameter grid and fixed‑point solution.** For each given $K/J$ ratio you will define a fine grid of reduced temperature $T/(zJ)$ and crystal field $\Delta/(zJ)$. Implement the Bethe‑lattice recursion relations for the branch partition‑function ratios $x$ and $y$: at each iteration,
$$x_{n+1} = \varphi(x_n, y_n), \qquad y_{n+1} = \varphi(y_n, x_n)$$
where
$$\varphi(u, v) = \frac{e^{\Delta} + e^{K}\left(e^{J} u^{z-1} + e^{-J} v^{z-1}\right)}{e^{\Delta} + u^{z-1} + v^{z-1}}$$
with $z=4$. Iterate these relations to convergence at every grid point to find all stable fixed points. Uniform phases correspond to simple fixed points, while staggered phases (antiquadrupolar and ferrimagnetic) appear as period‑2 cycles of the recursion, reflecting sublattice symmetry breaking. From the fixed points compute the order parameters, magnetisation $m$ and quadrupolar moment $q$, as well as the local free energy.

2. **Phase boundary extraction.** Classify each grid point into one of the four phases (disordered d, ferromagnetic f, antiquadrupolar a, ferrimagnetic i) based on the order‑parameter patterns and fixed‑point structure. Second‑order transition points are located where the stable solutions of two different phases intersect. First‑order transitions are identified as coexistence lines where the free energies of two phases cross. Collect all such transition points for the full set of $K/J$ values.

## Reproduction target
A CSV file `/app/outputs/phase_boundaries.csv` containing phase transition points for the eight coupling ratios:

$K/J = 5, 3, -0.1, -0.8, -1, -2.5, -3, -3.5$.

The file must have the following columns:

- `K_over_J` (float): the biquadratic coupling ratio.
- `delta_over_zJ` (float): the reduced crystal field $\Delta/(zJ)$ at the transition point.
- `temperature_over_zJ` (float): the reduced temperature $T/(zJ)$ at the transition point.
- `transition_type` (string): either `second_order` or `first_order`.
- `phase_from` (string): the phase before the transition (`d`, `f`, `a`, or `i`).
- `phase_to` (string): the phase after the transition (`d`, `f`, `a`, or `i`).

Each row represents one point on a phase boundary. The resolution and coverage must be sufficient to capture all qualitatively distinct topologies and transition lines that occur at these coupling values.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Parameter grid and fixed-point solution
- Role: process
- Action: Define a fine grid of temperature (T/zJ) and crystal field (Δ/zJ) for each of the eight K/J values (5, 3, -0.1, -0.8, -1, -2.5, -3, -3.5). Implement the recursion equations for the BEG model on the Bethe lattice with coordination number z=4. Iterate to find stable fixed points (including period-2 cycles for staggered phases) for every grid point. Compute the order parameters (magnetization m and quadrupolar moment q) and free energy from the fixed points. Save the full set of solutions (K/J, T/zJ, Δ/zJ, fixed-point values, m, q, free energy) to solutions.csv.
- Evidence: `/app/outputs/solutions.csv`

### Step 2: Phase boundary extraction
- Role: scored (load-bearing)
- Action: From the full solutions, classify each grid point into phases (d, f, a, i) based on order parameters and fixed-point patterns. Locate second-order transitions (intersection of stable solutions) and first-order transitions (coexistence and free-energy crossing). Output the transition points as rows covering all transition lines for each K/J value.
- Output file: `/app/outputs/phase_boundaries.csv`
- Format: csv
- Contract: CSV with columns: K_over_J (float), delta_over_zJ (float), temperature_over_zJ (float), transition_type (string: 'second_order' or 'first_order'), phase_from (string: 'd','f','a','i'), phase_to (string). Each row is one transition point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundaries.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundaries.csv
- path: `/app/outputs/phase_boundaries.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed phase boundaries for the BEG model on Bethe lattice (z=4) for eight K/J values. The checker will recompute gold boundaries and compare using a distance-based metric.
- schema:
  - `type`: table
  - `required_columns`: `K_over_J`, `delta_over_zJ`, `temperature_over_zJ`, `transition_type`, `phase_from`, `phase_to`

Notes: The solving agent must compute transitions for all eight specified K/J values. The checker will compare the agent's phase_boundaries.csv to a reference implementation using a distance-based metric with tolerances that account for differences in grid resolution and numerical variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundaries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "K_over_J",
          "delta_over_zJ",
          "temperature_over_zJ",
          "transition_type",
          "phase_from",
          "phase_to"
        ]
      },
      "description": "Computed phase boundaries for the BEG model on Bethe lattice (z=4) for eight K/J values. The checker will recompute gold boundaries and compare using a distance-based metric."
    }
  ],
  "notes": "The solving agent must compute transitions for all eight specified K/J values. The checker will compare the agent's phase_boundaries.csv to a reference implementation using a distance-based metric with tolerances that account for differences in grid resolution and numerical variation."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that performs an independent reference implementation of the recursion equations and phase‑boundary detection. For each $K/J$ value the verifier compares your `phase_boundaries.csv` to its own gold set of transition points using a distance‑based metric: for every gold point it locates the nearest point in your file that matches the transition type and both phases, and checks whether the temperature and crystal‑field differences fall within tolerances that account for numerical variations and grid resolution. In addition, structural checks verify that the sequence of phases along representative cuts agrees with the correct ordering for that coupling. The final reward is a weighted combination of these per‑condition and structural assessments. Reporting approximate numbers without a genuine numerical solution of the recursion relations will not earn full credit.
