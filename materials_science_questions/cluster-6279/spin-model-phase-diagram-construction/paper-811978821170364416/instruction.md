# Spin-1 Heisenberg Ferromagnet Phase Diagram via Constant-Coupling Approach

## Problem background
A spin-1 anisotropic Heisenberg ferromagnet with biquadratic exchange is studied within the constant-coupling approximation. The spin Hamiltonian is

H = -2J [ S1·S2 + α (S1·S2)^2 ] - μ H (S1z + S2z) - D (S1z + S2z)^2

where J is the ferromagnetic exchange integral, αJ is the biquadratic exchange strength, μH is an effective field contribution, and D is an anisotropy parameter. The chosen anisotropy term D(S1z+S2z)^2 makes the Hamiltonian diagonal in the total spin basis (S,M) with M=S1z+S2z, so the partition function for a spin pair can be expressed in closed form. Using this partition function, the constant-coupling approximation yields a self-consistency equation for the magnetization per spin, m = ⟨S_z⟩, as a function of temperature T, α, and D/J. The task is to compute the finite-temperature magnetic phase diagram: locate the transition temperature T_c as a function of α and D/J, determine whether each transition is second-order (m continuously goes to zero) or first-order (m drops discontinuously to zero), find the critical biquadratic exchange α_c that separates the two regimes, and generate magnetization vs. temperature curves for representative parameter combinations that exhibit both second-order and first-order behavior.

## Approach
The spin pair Hamiltonian is diagonal in the joint basis |S, M⟩ where S is the total spin quantum number (S = 0, 1, 2) and M = S1z + S2z (M = -S,…, S). The energy eigenvalues can be written explicitly in terms of S, M, α, D, and μH. From these, the partition function Z_pair(α, D, H_eff, T) for the pair is constructed. Within the constant-coupling approximation, the thermal average of the magnetization per spin m = ⟨S_z⟩ satisfies

m = ⟨M⟩_pair / 2 = (k_B T / 2) ∂ ln Z_pair / ∂ H_eff,

with the effective field H_eff chosen self-consistently to reproduce the mean magnetization of the surrounding lattice. This leads to a self-consistency equation of the form m = f(m; α, D/J, T). For given material parameters (α, D/J) the task is to:
- Solve this equation numerically for m as a function of temperature T, using a robust root-finding method that can handle multiple roots.
- Determine the transition temperature T_c: for a second-order transition it is the temperature where the only solution is m=0 (the magnetization continuously vanishes); for a first-order transition it is the temperature where the free energies of the m=0 and m≠0 solutions become equal, resulting in a discontinuous jump in the equilibrium magnetization.
- By sweeping over α and D/J, map out the boundary between ferromagnetic and paramagnetic phases and identify the critical α_c at which the order changes from second to first.
- Finally, produce magnetization vs. temperature curves at selected (α, D) points that clearly show the continuous or discontinuous character of the transition.

## Reproduction target
Produce two CSV files under `/app/outputs`:

1. `phase_boundary.csv` — the phase boundary table. For D_over_J ∈ {0.0, 0.5, 1.0, 1.5} and α ranging from 0.0 to 3.0 (step 0.1, finer near the crossover if needed), record the transition temperature T_c and the order of the transition ("second" or "first").

2. `magnetization.csv` — magnetization versus temperature curves. For the following (D_over_J, α) pairs: (0.0, 0.0), (0.0, 0.5), (0.0, 1.0), (0.0, 1.1), (1.0, 1.0), (1.0, 1.5), (1.0, 1.9), (1.0, 2.0), compute the equilibrium magnetization m as a function of temperature from T = 0 up to a value above the corresponding T_c, using a temperature step no larger than 0.01.

The goal is to obtain the complete phase boundary (including the separation into second-order and first-order regions) and magnetization curves that illustrate the continuous vs. discontinuous behavior of the magnetization at the transition. The hidden verifier will check for internal consistency between these two artifacts (e.g., the T_c implied by the magnetization curves should agree with the values in the phase boundary table).

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement closed-form partition function
- Role: process
- Action: Using the total spin basis (S,M) where the Hamiltonian H = -2J[S1·S2 + α(S1·S2)^2] - μH(S1z+S2z) - D(S1z+S2z)^2 is diagonal, compute the energy eigenvalues and implement a function that returns the partition function Z(α, D, H, T) for the spin pair.
- Evidence: none

### Step 2: Formulate and solve the constant-coupling self-consistency equation
- Role: process
- Action: From the partition function, derive the effective field relation and set up the constant-coupling self-consistency equation for magnetization m. Implement a root-finding routine (e.g., using scipy.optimize) that, for given (α, D/J, T), finds stable magnetization solutions. The solver must handle both continuous (second-order) and discontinuous (first-order) transitions by scanning for multiple roots.
- Evidence: none

### Step 3: Compute phase boundary and critical αc
- Role: scored (load-bearing)
- Action: For a grid of parameters: D_over_J in {0.0, 0.5, 1.0, 1.5} and α from 0.0 to 3.0 in steps of 0.1 (finer steps near the transition if necessary), determine the transition temperature Tc for each (α, D) point. For second-order transitions, Tc is the temperature where the magnetization continuously vanishes. For first-order transitions, Tc is the temperature where the free energies of the zero-magnetization and finite-magnetization solutions cross, and the magnetization exhibits a discontinuity. Record the order of transition ("second" or "first") along with Tc.
- Output file: `/app/outputs/phase_boundary.csv`
- Format: csv
- Contract: Columns: D_over_J (float), alpha (float), T_c (float), transition_order (string, 'second' or 'first'). Rows cover D_over_J ∈ {0.0, 0.5, 1.0, 1.5} and α ∈ [0.0, 3.0] with step 0.1.
- Scoring: scored by hidden verifier

### Step 4: Produce magnetization vs temperature curves
- Role: scored
- Action: For the specific parameter combinations: (D_over_J=0.0, α=0.0, 0.5, 1.0, 1.1) and (D_over_J=1.0, α=1.0, 1.5, 1.9, 2.0), solve the self-consistency equation for temperatures from 0 up to a value above the corresponding Tc, using a temperature step of at most 0.01 (or finer to resolve the transition). For each combination, output the temperature and the equilibrium magnetization.
- Output file: `/app/outputs/magnetization.csv`
- Format: csv
- Contract: Columns: D_over_J (float), alpha (float), temperature (float), magnetization (float). Rows for D_over_J=0.0: α=0.0, 0.5, 1.0, 1.1. Rows for D_over_J=1.0: α=1.0, 1.5, 1.9, 2.0. Temperature from 0 to above Tc with spacing ≤ 0.01.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundary.csv`
- `/app/outputs/magnetization.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundary.csv
- path: `/app/outputs/phase_boundary.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Transition temperature and order for a grid of (α, D/J) values.
- schema:
  - `type`: table
  - `required_columns`: `D_over_J`, `alpha`, `T_c`, `transition_order`
  - `units`:
    - `T_c`: arbitrary (J/kB)

### magnetization.csv
- path: `/app/outputs/magnetization.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetization vs temperature curves for selected parameter combinations.
- schema:
  - `type`: table
  - `required_columns`: `D_over_J`, `alpha`, `temperature`, `magnetization`
  - `units`:
    - `temperature`: arbitrary (J/kB)
    - `magnetization`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "D_over_J",
          "alpha",
          "T_c",
          "transition_order"
        ],
        "units": {
          "T_c": "arbitrary (J/kB)"
        }
      },
      "description": "Transition temperature and order for a grid of (α, D/J) values."
    },
    {
      "file": "magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "D_over_J",
          "alpha",
          "temperature",
          "magnetization"
        ],
        "units": {
          "temperature": "arbitrary (J/kB)",
          "magnetization": "dimensionless"
        }
      },
      "description": "Magnetization vs temperature curves for selected parameter combinations."
    }
  ],
  "notes": ""
}
```

## How you are scored
Each scored artifact is verified independently by a hidden verifier that has access to reference values derived from the original study. The verifier will:

- **phase_boundary.csv**: Extract the T_c and transition order for a set of (α, D) points. For second-order transitions it checks that the T_c matches the reference value (within an appropriate tolerance). For first-order transitions it checks that the T_c and the presence of a discontinuity are consistent with the reference. It also identifies the smallest α for which the transition is first-order at each D_over_J; these critical α_c values are compared to reference numbers.
- **magnetization.csv**: It verifies that for every parameter pair the magnetization decreases monotonically from the low-temperature value towards zero. For parameters where α > α_c (first-order regime), it confirms that the magnetization stays finite at the transition temperature and drops discontinuously (the curve shows a gap at T_c). The verifier also cross-checks that the T_c inferred from the magnetization curve matches the T_c reported in `phase_boundary.csv` for the same (D_over_J, α).

The final reward is a weighted combination of the scores from the phase boundary table and the magnetization curves. Outputting the paper's numbers without a genuine self-consistent computation that reproduces the expected physical behavior will not yield a passing score.
