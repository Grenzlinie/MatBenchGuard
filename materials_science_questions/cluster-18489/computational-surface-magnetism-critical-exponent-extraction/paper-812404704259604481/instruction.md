# Amorphized Ising Surface Phase Diagrams via Reaction-Field Approximation

## Problem background
Magnetic order near a free surface can differ strongly from bulk behaviour. In a semi-infinite spin‑1/2 Ising ferromagnet, the surface may order above the bulk Curie temperature when the surface exchange is sufficiently enhanced, and disorder introduced by surface amorphization can shift or even suppress this ordering. This task studies the semi-infinite simple-cubic Ising ferromagnet with a free (100) surface and random exchange parameters—surface coupling $J_S$, surface‑to‑first‑layer coupling $J_1$, and bulk coupling $J_B$—using a reaction‑field approximation (RFA) that includes non‑trivial spin fluctuations. The central quantities to compute are the reduced surface critical temperature $t_c = T_c^s / T_c^b$ as a function of surface enhancement and disorder, the critical enhancement needed for surface‑before‑bulk ordering, and the possibility of a surface re‑entrant phenomenon where raising disorder can destroy surface order.

## Approach
The reaction‑field approximation (RFA) improves on mean‑field theory by letting the molecular field acting on a spin react to its own fluctuations. For the semi-infinite geometry, the method yields layer magnetizations described by a set of self‑consistent equations. Near the critical point these equations are linearised, leading to a secular equation that, together with a transfer‑function ansatz, determines the surface ordering temperature. The structural disorder is modelled by a discrete Handrich‑Kaneyoshi distribution for the exchange parameters, characterised by disorder amplitudes $D_S = \Delta J_S / J_B$ and $D_1 = \Delta J_1 / J_B$. A key derived parameter is the structural fluctuation $\delta_S = D_S / (1 + \Delta_S)$, where $\Delta_S = (J_S/J_B) - 1$ is the surface coupling enhancement. By solving the secular equation numerically under different fixed values of the parameters ($\Delta_1$, $D_1$, $D_S$, $\Delta_S$) one can obtain the reduced surface critical temperature $t_c \in [0,1]$ and the critical enhancement $\Delta_S^c$ where $t_c = 1$. The approach is implemented as a root‑finding exercise: for each set of conditions, the physical root of the secular equation is found and tabulated.

## Reproduction target
Produce three scored CSV artifacts:
1. **Phase diagram curves** (`phase_diagram.csv`): $t_c$ as a function of $\Delta_S$ from $-1.0$ to $5.0$ (step $0.1$) for two cases—a pure surface ($D_S=0$) and an amorphized surface ($D_S=2.0$)—with $\Delta_1=0$, $D_1=0$.
2. **Critical surface enhancement** (`critical_values.csv`): $\Delta_S^c$ (where $t_c=1$) for $D_S$ from $0.0$ to $5.0$ (step $0.5$) with $\Delta_1=0$, $D_1=0$.
3. **Re‑entrant phenomenon curve** (`reentrant_curve.csv`): $t_c$ as a function of $\delta_S = D_S/(1+\Delta_S)$ for $\delta_S$ from $0.0$ to $1.0$ (step $0.05$) at fixed $\Delta_S=7.0$, $\Delta_1=-0.9$, $D_1=0$.
All quantities are dimensionless; the bulk Curie temperature is taken as $k_B T_c^b / J_B = 5.0$.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute surface phase diagram curves
- Role: scored
- Action: Using the linearized RFA secular equation for the semi-infinite Ising model, compute the reduced surface critical temperature t_c = T_c^s / T_c^b as a function of the surface coupling enhancement Δ_S. Fix Δ_1 = 0 and D_1 = 0 for all curves. Produce two curves: (i) a pure surface with D_S = 0, and (ii) an amorphized surface with D_S = 2.0. For each Δ_S from -1.0 to 5.0 in steps of 0.1, find the physical root t_c ∈ [0,1] of the secular equation and write the results to a CSV.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: CSV table with columns: Delta_S (float, dimensionless enhancement), t_c (float, reduced critical temperature in [0,1]), param_label (string, 'pure' or 'amorphized').
- Scoring: scored by hidden verifier

### Step 2: Compute critical surface enhancement Δ_S^c
- Role: scored
- Action: For each surface amorphization parameter D_S in the set [0.0, 0.5, 1.0, ..., 5.0] (step 0.5), with Δ_1 = 0 and D_1 = 0, solve the linearized RFA secular equation for the value of Δ_S that gives t_c = 1 (i.e., the surface orders exactly at the bulk Curie temperature). Write the resulting D_S and critical Δ_S^c to a CSV.
- Output file: `/app/outputs/critical_values.csv`
- Format: csv
- Contract: CSV table with columns: D_S (float, amorphization parameter from 0.0 to 5.0 step 0.5), Delta_c_S (float, critical enhancement).
- Scoring: scored by hidden verifier

### Step 3: Compute re-entrant phenomenon curve
- Role: scored (load-bearing)
- Action: Compute the surface ordering temperature t_c as a function of the surface structural fluctuation parameter δ_S (defined as δ_S = D_S / (1+Δ_S)). Use fixed parameters Δ_S = 7.0, Δ_1 = -0.9, D_1 = 0. For δ_S from 0.0 to 1.0 in steps of 0.05, solve the secular equation (expressed in terms of δ_S) for the physical root t_c ∈ [0,1]. Write the results to a CSV.
- Output file: `/app/outputs/reentrant_curve.csv`
- Format: csv
- Contract: CSV table with columns: delta_S (float, structural fluctuation parameter from 0.0 to 1.0 step 0.05), t_c (float, reduced critical temperature in [0,1]).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/critical_values.csv`
- `/app/outputs/reentrant_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Surface phase diagram: reduced critical temperature vs. Δ_S for pure and amorphized surfaces.
- schema:
  - `type`: table
  - `required_columns`: `Delta_S`, `t_c`, `param_label`
  - `units`:
    - `Delta_S`: dimensionless
    - `t_c`: dimensionless (fraction of bulk Tc)
    - `param_label`: string

### critical_values.csv
- path: `/app/outputs/critical_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical enhancement Δ_S^c vs. disorder D_S at the special surface-bulk transition (t_c=1).
- schema:
  - `type`: table
  - `required_columns`: `D_S`, `Delta_c_S`
  - `units`:
    - `D_S`: dimensionless
    - `Delta_c_S`: dimensionless

### reentrant_curve.csv
- path: `/app/outputs/reentrant_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Re-entrant curve: surface ordering temperature vs. structural fluctuation δ_S for Δ_S=7.0, Δ_1=-0.9.
- schema:
  - `type`: table
  - `required_columns`: `delta_S`, `t_c`
  - `units`:
    - `delta_S`: dimensionless
    - `t_c`: dimensionless

Notes: The verifier implements the same linearized RFA secular equation and recomputes t_c (or Δ_S^c) for each submitted parameter set. For phase_diagram.csv, the verifier recomputes t_c for every (Δ_S, param_label) point and checks absolute deviation within tolerance. For critical_values.csv, it solves for the root giving t_c=1 and compares submitted Δ_c_S to its recomputed value within tolerance, and checks monotonicity. For reentrant_curve.csv, it recomputes t_c for each δ_S point. The hidden reference is the verifier’s own recomputation using the publicly known equations; no external gold dataset is used.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Delta_S",
          "t_c",
          "param_label"
        ],
        "units": {
          "Delta_S": "dimensionless",
          "t_c": "dimensionless (fraction of bulk Tc)",
          "param_label": "string"
        }
      },
      "description": "Surface phase diagram: reduced critical temperature vs. Δ_S for pure and amorphized surfaces."
    },
    {
      "file": "critical_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "D_S",
          "Delta_c_S"
        ],
        "units": {
          "D_S": "dimensionless",
          "Delta_c_S": "dimensionless"
        }
      },
      "description": "Critical enhancement Δ_S^c vs. disorder D_S at the special surface-bulk transition (t_c=1)."
    },
    {
      "file": "reentrant_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta_S",
          "t_c"
        ],
        "units": {
          "delta_S": "dimensionless",
          "t_c": "dimensionless"
        }
      },
      "description": "Re-entrant curve: surface ordering temperature vs. structural fluctuation δ_S for Δ_S=7.0, Δ_1=-0.9."
    }
  ],
  "notes": "The verifier implements the same linearized RFA secular equation and recomputes t_c (or Δ_S^c) for each submitted parameter set. For phase_diagram.csv, the verifier recomputes t_c for every (Δ_S, param_label) point and checks absolute deviation within tolerance. For critical_values.csv, it solves for the root giving t_c=1 and compares submitted Δ_c_S to its recomputed value within tolerance, and checks monotonicity. For reentrant_curve.csv, it recomputes t_c for each δ_S point. The hidden reference is the verifier’s own recomputation using the publicly known equations; no external gold dataset is used."
}
```

## How you are scored
A hidden verifier independently recomputes the same RFA secular equation from your submitted CSV artifacts. For the phase diagram and re‑entrant curves it recomputes $t_c$ for each data row and checks agreement against your values; for the critical‑values curve it solves for the root $\Delta_S$ that gives $t_c=1$ and compares with your submitted $\Delta_c_S$. The verifier may also check expected structural properties such as monotonicity. Each scored stage carries a fraction of the total reward; the final reward is the weighted sum of per‑stage credit. Reporting a number from the literature without genuinely solving the secular equation will not satisfy the verifier, because the check is against a self‑contained recomputation, not a pre‑recorded reference.
