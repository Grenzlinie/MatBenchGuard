# Simulated DHC Velocity Curve and Stage I/II Transition via Stress-Driven Hydrogen Diffusion

## Problem background
Delayed hydride cracking (DHC) is a time-dependent fracture mechanism that can affect zirconium alloy pressure tubes in nuclear reactors. Under an applied stress intensity factor $K_I$, a crack propagates by repeated cycles of hydrogen diffusion, hydride precipitation, and hydride fracture. The resulting crack velocity typically shows a three-stage dependence on $K_I$: a steep increase in stage I, a plateau in stage II, and another increase in stage III. The physical origin of the stage I/II transition is an open question for materials performance and lifetime prediction. A proposed explanation associates the transition with the relative sizes of the hydride cluster required for fracture and the plastic zone at the crack tip. This task reproduces the computational evidence for that explanation: you will simulate the hydride growth process and derive the DHC velocity curve, then determine the $K_I$ at which the velocity behaviour switches from stage I to stage II and examine its connection to the plastic zone size.

## Approach
The analysis combines a numerical simulation of stress-driven hydrogen diffusion with an experimentally measured critical hydride length curve. The diffusion problem is treated with a cylindrical approximation of the crack-tip stress field under plane strain. Hydrogen transport is governed by Fick's laws with an additional drift term from the hydrostatic stress gradient. Hydride precipitation consumes hydrogen at the crack tip, causing the hydride cluster to grow with time. For several applied $K_I$ values, the time-dependent hydride length is computed at multiple fixed diffusion times, yielding a family of growth curves. Separately, a critical hydride cluster length curve (the minimum length needed for fracture at a given $K_I$) is provided as input data. For each $K_I$, the intersection of the appropriate growth curve with the critical length curve determines the hydride length and the diffusion time at fracture; the DHC velocity is then calculated as length divided by time. The resulting velocity vs. $K_I$ curve exhibits a sharp slope change that marks the stage I/II transition. To test the proposed mechanism, you will also compute the plane‑strain plastic zone size $r_P = \frac{1}{6\pi}\left(K_I/\sigma_{ys}\right)^2$ and find the $K_I$ where $r_P$ equals the critical hydride length. A consistency check between that $K_I$ and the transition $K_I$ from the velocity curve completes the analysis.

## Reproduction target
Produce a set of hydride growth curves (hydride length vs. $K_I$ at several diffusion times) by simulating stress-driven hydrogen diffusion at a crack tip. Use the provided critical hydride cluster length data to derive a DHC velocity vs. $K_I$ curve via the intersection method. From that velocity curve, locate the transition $K_I$ where the slope changes abruptly (the stage I/II transition). Finally, verify the relation to the plastic zone by computing the $K_I$ at which the plastic zone size matches the critical hydride length and comparing it with the transition $K_I$ from the velocity curve. The required outputs are the growth curve table, the velocity curve table, and a JSON summary of the transition analysis, all conforming to the contracts below.

## Assets

- Critical hydride cluster length vs KI data
- Python scientific computing packages: numpy scipy matplotlib

## Workflow steps

### Step 1: Simulate hydrogen diffusion and hydride growth
- Role: scored
- Action: Implement a finite-difference cylindrical approximation for stress-driven hydrogen diffusion (Fick's laws) to simulate hydride cluster growth at the crack tip for multiple applied KI values. Use specified inputs: temperature 150°C, initial hydrogen concentration 96% of the precipitation solvus, hydride thickness 3 µm. Compute hydride lengths at several diffusion times covering a range from hours to days. Output hydride lengths for each KI and time.
- Output file: `/app/outputs/hydride_growth_curves.csv`
- Format: csv
- Contract: CSV with columns: KI (float, MPa√m), time_label (string, e.g., 't1','t2','t3'), hydride_length (float, µm). Provide at least three distinct time labels covering different diffusion times.
- Scoring: scored by hidden verifier

### Step 2: Compute DHC velocity vs. KI
- Role: scored (load-bearing)
- Action: Load the hydride growth curves from the previous step and the provided critical hydride cluster length data. For each KI, find the intersection between the growth curves and the critical length curve to obtain the hydride length and the corresponding diffusion time at fracture. Compute DHC velocity as length divided by time. Output the resulting velocity vs. KI data.
- Output file: `/app/outputs/dhc_velocity_vs_KI.csv`
- Format: csv
- Contract: CSV with columns: KI (float, MPa√m), velocity (float, m/s). Provide KI values from 6 to 14 MPa√m at increments of 0.5 or 1.
- Scoring: scored by hidden verifier

### Step 3: Analyze stage I/II transition and plastic zone comparison
- Role: scored
- Action: From the velocity curve, identify the transition KI where the velocity slope changes abruptly (stage I/II transition). Compute the plane‑strain plastic zone size rP = (1/(6π))*(KI/σ_ys)² using σ_ys=630 MPa. Find the KI where rP equals the critical hydride length. Report the transition KI, the KI where rP matches the critical length, and a boolean indicating consistency (approximately equal).
- Output file: `/app/outputs/transition_analysis.json`
- Format: json
- Contract: JSON object with fields: transition_KI (float, MPa√m), K_I_where_rP_equals_lcrit (float, MPa√m), comparison (boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hydride_growth_curves.csv`
- `/app/outputs/dhc_velocity_vs_KI.csv`
- `/app/outputs/transition_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hydride_growth_curves.csv
- path: `/app/outputs/hydride_growth_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Hydride growth curves (length as function of KI for various diffusion times) used to derive DHC velocities.
- schema:
  - `type`: table
  - `required_columns`: `KI`, `time_label`, `hydride_length`
  - `units`:
    - `KI`: MPa√m
    - `hydride_length`: µm

### dhc_velocity_vs_KI.csv
- path: `/app/outputs/dhc_velocity_vs_KI.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: DHC velocity vs KI curve obtained from the intersection method. The checker recomputes velocities from hydride growth curves and the critical length data and compares against this curve.
- schema:
  - `type`: table
  - `required_columns`: `KI`, `velocity`
  - `units`:
    - `KI`: MPa√m
    - `velocity`: m/s

### transition_analysis.json
- path: `/app/outputs/transition_analysis.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Stage I/II transition point, plastic‑zone matching KI, and consistency flag.
- schema:
  - `type`: object
  - `required`:
    - `transition_KI`: float (MPa√m)
    - `K_I_where_rP_equals_lcrit`: float (MPa√m)
    - `comparison`: boolean

Notes: The critical hydride cluster length data (bundled) is an external experimental input. The checker independently derives velocities from the hydride growth curves, recomputes the plastic zone intersection, and verifies the transition point.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hydride_growth_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "KI",
          "time_label",
          "hydride_length"
        ],
        "units": {
          "KI": "MPa√m",
          "hydride_length": "µm"
        }
      },
      "description": "Hydride growth curves (length as function of KI for various diffusion times) used to derive DHC velocities."
    },
    {
      "file": "dhc_velocity_vs_KI.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "KI",
          "velocity"
        ],
        "units": {
          "KI": "MPa√m",
          "velocity": "m/s"
        }
      },
      "description": "DHC velocity vs KI curve obtained from the intersection method. The checker recomputes velocities from hydride growth curves and the critical length data and compares against this curve."
    },
    {
      "file": "transition_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "transition_KI": "float (MPa√m)",
          "K_I_where_rP_equals_lcrit": "float (MPa√m)",
          "comparison": "boolean"
        }
      },
      "description": "Stage I/II transition point, plastic‑zone matching KI, and consistency flag."
    }
  ],
  "notes": "The critical hydride cluster length data (bundled) is an external experimental input. The checker independently derives velocities from the hydride growth curves, recomputes the plastic zone intersection, and verifies the transition point."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage's output artifact and combine the partial scores into a single reward. For the hydride growth curves, the verifier checks that the table is well-formed, covers the required $K_I$ range and time labels, and is internally consistent. For the DHC velocity curve, the verifier will recompute velocities from your growth curves and the provided critical length data, then assess how well the curve reproduces the expected staged behaviour: a steep velocity increase over some $K_I$ range (stage I) followed by a plateau where velocity changes little (stage II). It will also test whether the transition $K_I$ derived from your velocity curve is in reasonable agreement with the transition $K_I$ implied by the plastic‑zone‑size comparison. For the transition analysis, the verifier will recompute the plastic zone size and the $K_I$ at which it equals the critical length, and check consistency with your reported values. Reporting the paper's numbers without a physically consistent workflow will not earn credit; your submitted artifacts must follow from the simulation and intersection procedure described in the steps.
