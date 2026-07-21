# Magnetization Relaxation in Weakly Interacting Dipolar Moment Clusters

## Problem background
Thermally activated magnetization decay in systems of interacting single-domain magnetic nanoparticles is modeled via a master-equation formalism. This study investigates how geometrical symmetry of spin clusters (e.g., collinear chains vs. symmetric pyramids) affects the validity of the conventional energy-barrier picture and leads to initialization-dependent memory effects. The semi-analytical approach maps microstates, computes single-spin transition barriers, assembles and diagonalizes a transition matrix, and aggregates eigen-barriers to obtain ensemble magnetization decay M(t) and the eigen-barrier distribution f(ε).

## Approach
The thermal relaxation of weakly dipolar-interacting spin clusters is described by a master-equation (ME) that treats transitions between discrete microstates as an Arrhenius-rate Markov process. For each cluster geometry (4-spin chains aligned along the z-axis and 4-spin pyramids with tetrahedral arrangement), the procedure is:

1. **Energy model** – Each spin is a unit vector with uniaxial anisotropy of uniform strength and random orientation (uniform on sphere); dipolar interactions between spins are included with strength I. The energy landscape defines local minima (microstates) and saddle points for single-spin transitions.
2. **Microstate enumeration** – Starting from all non‑interacting bistable spin configurations, the orientations are relaxed iteratively in the presence of dipolar fields to obtain the interacting microstates.
3. **Barrier and rate matrix construction** – For each microstate, the energy barriers for all single‑spin-flip transitions are computed. Transition rates follow the Arrhenius form with a constant attempt time τ₀, giving a transition matrix W.
4. **Eigenvalue problem** – Diagonalizing W yields eigenvalues (converted to eigen‑barriers ε via τ = τ₀ exp(ε)) and right eigenvectors. Combining them with the initial microstate (determined by athermal energy minimization from a saturating field history either parallel or perpendicular to the chain axis) gives weights ξₙ for each relaxation mode.
5. **Ensemble aggregation** – Repeating the above for an ensemble of 10,000 clusters (for each geometry and for interaction strengths I = 0.0, 0.1, …, 1.0 relative to a reference I₀) produces a set of (ε, ξ) pairs. These are histogrammed to obtain the probability density f(ε) and then integrated to give the magnetization decay M(t) = M₀ ∫ f(ε) exp(-t/τ(ε)) dε. The weighted mean eigen‑barrier ε̄ = (∑ ξ ε) / (∑ |ξ|) summarizes the relaxation time scale.

## Reproduction target
Implement the full semi‑analytical master‑equation pipeline and produce the following three CSV artifacts:

1. **Magnetization decay curves** – For an ensemble of 4‑spin chains at interaction strength I = I₀, compute M(t) for a suitable time grid for both initialization directions (saturating field parallel and perpendicular to the chain axis). Output columns: `t` (seconds), `M_parallel` (0–1), `M_perpendicular` (0–1).

2. **Eigen‑barrier distribution** – For the same chains and conditions, compute the normalized probability density f(ε) for both initializations. Output columns: `epsilon` (energy units of k_B T), `f_parallel`, `f_perpendicular`.

3. **Mean eigen‑barrier vs. interaction strength** – For both 4‑spin chains and 4‑spin pyramids, compute ε̄ as a function of relative interaction strength I/I₀ (0 to 1 in steps of 0.1) for both initialization directions. Output columns: `I_relative`, `epsilon_bar_chain_parallel`, `epsilon_bar_chain_perp`, `epsilon_bar_pyramid_parallel`, `epsilon_bar_pyramid_perp`. All ε̄ values are in units of k_B T.

The results must clearly distinguish the behavior of chains vs. pyramids and demonstrate the influence of the initialization direction on the relaxation properties.

## Assets

- Python scientific computing stack: numpy scipy

## Workflow steps

### Step 1: Generate spin cluster ensembles
- Role: process
- Action: Define the geometry of 4-spin chains (collinear along z-axis, spacing a) and 4-spin pyramids (tetrahedron with nearest-neighbor contact distance a). For each geometry, generate an ensemble of 10,000 clusters with randomly oriented uniaxial anisotropy axes (uniform on sphere).
- Evidence: `/app/outputs/none`

### Step 2: Semi-analytical master-equation simulation
- Role: process
- Action: For each geometry and for interaction strengths I_relative = 0.0, 0.1, ..., 1.0 (I = I_relative * I₀, where I₀ is the reference interaction strength): (a) Enumerate all microstates by relaxing non-interacting bistable spin configurations under the dipolar energy; (b) Identify single-spin transition paths and compute energy barriers δe; (c) Determine the initial microstate for two field histories (saturating field parallel and perpendicular to the chain axis) by athermal energy minimization; (d) Assemble the transition rate matrix W using Arrhenius rates with constant attempt time τ₀; (e) Diagonalize W to obtain eigenvalues (convert to eigen-barriers ε_r via τ_r = τ₀ exp(ε_r)) and right eigenvectors, compute weights ξ_r using initial condition. Save all (ε_r, ξ_r) pairs for each cluster, geometry, I, and initialization to a compact file.
- Evidence: `/app/outputs/eigen_data.h5`

### Step 3: Magnetization decay M(t) for chains
- Role: scored (load-bearing)
- Action: From the eigen_data, extract the (ε, ξ) pairs for 4-spin chains at I_relative = 1.0 and for both initializations. Build a normalized joint histogram D(ε,ξ), marginalize to obtain f(ε) (probability density), then compute magnetization decay M(t) = M₀ ∫ f(ε) exp(-t / (τ₀ exp(ε))) dε on a suitable time grid (t in seconds). Output the decay curves for parallel and perpendicular initializations.
- Output file: `/app/outputs/step_01_magnetization_decay.csv`
- Format: csv
- Contract: t (float), M_parallel (float 0-1), M_perpendicular (float 0-1)
- Scoring: scored by hidden verifier

### Step 4: Eigen-barrier distribution f(ε) for chains
- Role: scored (load-bearing)
- Action: From the same eigen_data for chains at I_relative = 1.0, compute the normalized probability density f(ε) for parallel and perpendicular initializations. Output the histogram as a table of ε and f values.
- Output file: `/app/outputs/step_02_f_epsilon.csv`
- Format: csv
- Contract: epsilon (float), f_parallel (float), f_perpendicular (float)
- Scoring: scored by hidden verifier

### Step 5: Mean eigen-barrier ε̄ vs interaction strength
- Role: scored (load-bearing)
- Action: For each geometry (chains and pyramids), each I_relative value, and each initialization, compute the weighted mean eigen-barrier ε̄ = (∑ ξ ε) / (∑ |ξ|) from the corresponding eigen_data entries. Assemble a table of ε̄ vs I_relative for all four cases.
- Output file: `/app/outputs/step_03_epsilon_bar_I.csv`
- Format: csv
- Contract: I_relative (float 0-1), ε̄_chain_parallel (float), ε̄_chain_perp (float), ε̄_pyramid_parallel (float), ε̄_pyramid_perp (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_magnetization_decay.csv`
- `/app/outputs/step_02_f_epsilon.csv`
- `/app/outputs/step_03_epsilon_bar_I.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_magnetization_decay.csv
- path: `/app/outputs/step_01_magnetization_decay.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetization decay curves for 4-spin chains at reference interaction strength I₀, for two initializations (parallel and perpendicular to chain axis).
- schema:
  - `type`: table
  - `required_columns`: `t`, `M_parallel`, `M_perpendicular`
  - `units`:
    - `t`: seconds
    - `M_parallel`: normalized magnetization (0-1)
    - `M_perpendicular`: normalized magnetization (0-1)

### step_02_f_epsilon.csv
- path: `/app/outputs/step_02_f_epsilon.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Eigen-barrier probability density for 4-spin chains at I₀, for both initializations.
- schema:
  - `type`: table
  - `required_columns`: `epsilon`, `f_parallel`, `f_perpendicular`
  - `units`:
    - `epsilon`: energy (units of k_B T)
    - `f_parallel`: probability density
    - `f_perpendicular`: probability density

### step_03_epsilon_bar_I.csv
- path: `/app/outputs/step_03_epsilon_bar_I.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Weighted mean eigen-barrier as a function of interaction strength for chains and pyramids, both initializations.
- schema:
  - `type`: table
  - `required_columns`: `I_relative`, `ε̄_chain_parallel`, `ε̄_chain_perp`, `ε̄_pyramid_parallel`, `ε̄_pyramid_perp`
  - `units`:
    - `I_relative`: interaction strength relative to I₀ (unitless, 0-1)
    - `ε̄_chain_parallel`: energy (units of k_B T)
    - `ε̄_chain_perp`: energy (units of k_B T)
    - `ε̄_pyramid_parallel`: energy (units of k_B T)
    - `ε̄_pyramid_perp`: energy (units of k_B T)

Notes: The verification checks the trend directions: ε̄_chain_parallel should be non-decreasing with I, ε̄_chain_perp non-increasing, and the two pyramid curves should remain nearly equal (small difference) across I.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_magnetization_decay.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "M_parallel",
          "M_perpendicular"
        ],
        "units": {
          "t": "seconds",
          "M_parallel": "normalized magnetization (0-1)",
          "M_perpendicular": "normalized magnetization (0-1)"
        }
      },
      "description": "Magnetization decay curves for 4-spin chains at reference interaction strength I₀, for two initializations (parallel and perpendicular to chain axis)."
    },
    {
      "file": "step_02_f_epsilon.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "epsilon",
          "f_parallel",
          "f_perpendicular"
        ],
        "units": {
          "epsilon": "energy (units of k_B T)",
          "f_parallel": "probability density",
          "f_perpendicular": "probability density"
        }
      },
      "description": "Eigen-barrier probability density for 4-spin chains at I₀, for both initializations."
    },
    {
      "file": "step_03_epsilon_bar_I.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "I_relative",
          "ε̄_chain_parallel",
          "ε̄_chain_perp",
          "ε̄_pyramid_parallel",
          "ε̄_pyramid_perp"
        ],
        "units": {
          "I_relative": "interaction strength relative to I₀ (unitless, 0-1)",
          "ε̄_chain_parallel": "energy (units of k_B T)",
          "ε̄_chain_perp": "energy (units of k_B T)",
          "ε̄_pyramid_parallel": "energy (units of k_B T)",
          "ε̄_pyramid_perp": "energy (units of k_B T)"
        }
      },
      "description": "Weighted mean eigen-barrier as a function of interaction strength for chains and pyramids, both initializations."
    }
  ],
  "notes": "The verification checks the trend directions: ε̄_chain_parallel should be non-decreasing with I, ε̄_chain_perp non-increasing, and the two pyramid curves should remain nearly equal (small difference) across I."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the three output files:

- The magnetization decay curves and the eigen‑barrier distribution will be compared against hidden reference values using relative and structural checks.
- The mean eigen‑barrier data will be audited for internal consistency and for required qualitative trends (e.g., geometry‑dependent behavior of ε̄ as a function of interaction strength).

Each file contributes a weighted score, and the final reward is the sum of these contributions. Simply reporting numbers without executing the full computational pipeline will not satisfy the scoring criteria; the verifier assesses whether the submitted artifacts are the genuine product of the described master‑equation workflow.
