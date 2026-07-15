# Variable thermal resistance of a TEC: compute curve and minimum

## Problem background
Thermoelectric coolers (TECs) can actively pump heat via the Peltier effect and are used for precise temperature management in electronics. When a TEC is operated at different currents, its effective thermal resistance (the variable thermal resistance θ_thv) changes, which can be exploited to dynamically control the temperature of a heat-dissipating chip. This task reproduces the variable thermal resistance characteristic of a commercial TES1-00708 TEC using an analytical model that couples the TEC device equations with a cold-side energy balance.

## Approach
The variable thermal resistance model follows the approach of Szekely and Mezosi (2006). The TEC is described by its Seebeck coefficient S, electrical resistance R, and basic thermal resistance θ_th. The cold side of the TEC is assumed to be attached to a chip that dissipates a constant heat load Q, with an interface thermal resistance θ_a between the chip junction and the TEC cold side. The chip junction temperature T_j is treated as a known operating point.

For a given TEC current I_tec, the cold-side temperature is T_c = T_j − θ_a·Q. The cold-side heat balance equation

    Q = S·I_tec·T_c − 0.5·I_tec²·R − (T_h − T_c) / θ_th

is solved for the temperature difference (T_h − T_c) between the hot and cold sides. The TEC electrical power is then

    P_tec = S·I_tec·(T_h − T_c) + I_tec²·R.

The variable thermal resistance is computed as

    θ_thv = (P_tec / I_tec² − R)·θ_th / [ (P_tec / I_tec² − R) + (0.5·S·I_tec·R − S²·(T_j − θ_a·Q))·θ_th ].

For I_tec = 0 the formula is undefined; the sweep therefore begins at 0.1 A.

Use the following numerical values (taken from the TEC datasheet and the experimental conditions):
- S = 0.0027 V/K
- R = 1.035 Ω
- θ_th = 102 K/W
- T_j = 353 K
- θ_a = 50 K/W
- Q = 0.5 W

Sweep I_tec from 0.1 A to 1.5 A in steps of 0.1 A, compute θ_thv for each current, and write the results as a CSV file.

## Reproduction target
Produce the variable thermal resistance curve θ_thv(I_tec) for the TES1-00708 TEC under the given operating conditions, and from that curve identify the minimum θ_thv value and the corresponding current. The deliverables are:
- `theta_thv_vs_I.csv`: a table with columns `I_tec` (A) and `theta_thv` (K/W) for I_tec from 0.1 A to 1.5 A in 0.1 A steps.
- `minimum_theta_thv.json`: a JSON file containing the minimum θ_thv and the current at which it occurs.

The verification will check that the reported minimum is consistent with the submitted curve and that the curve exhibits the expected qualitative behavior (steep initial drop, a minimum, then a slow rise).

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute variable thermal resistance vs current
- Role: scored (load-bearing)
- Action: Using the standard one-dimensional TEC device equations for cold-side heat absorption, hot-side heat rejection, and electrical power, together with the cold-side energy balance that relates the basic thermal resistance to the variable thermal resistance (following the model from Szekely and Mezosi, 2006), compute the variable thermal resistance θ_thv as a function of TEC current I_tec. The TEC parameters are: Seebeck coefficient S=0.0027 V/K, electrical resistance R=1.035 Ω, basic thermal resistance θ_th=102 K/W. The chip operating conditions (junction temperature T_j, interface thermal resistance θ_a, and heat load Q) are provided in the instruction. For each I_tec value from 0.1 A to 1.5 A in steps of 0.1 A, solve the coupled equations to obtain θ_thv. Write the results to a CSV file with columns I_tec (A) and theta_thv (K/W).
- Output file: `/app/outputs/theta_thv_vs_I.csv`
- Format: csv
- Contract: CSV with header: I_tec,theta_thv. Values: I_tec from 0.1 to 1.5 in 0.1 A steps (inclusive), theta_thv in K/W.
- Scoring: scored by hidden verifier

### Step 2: Extract minimum thermal resistance
- Role: scored
- Action: Read theta_thv_vs_I.csv, locate the row with the smallest theta_thv value, and report that minimum value and the corresponding current. Output a JSON file with keys 'minimum_value' (K/W) and 'current_at_minimum' (A).
- Output file: `/app/outputs/minimum_theta_thv.json`
- Format: json
- Contract: {"minimum_value": <float>, "current_at_minimum": <float>} (units: K/W and A)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/theta_thv_vs_I.csv`
- `/app/outputs/minimum_theta_thv.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### theta_thv_vs_I.csv
- path: `/app/outputs/theta_thv_vs_I.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed variable thermal resistance curve. The checker recomputes theta_thv from the reported I_tec values using the hidden parameters and compares the agent's values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `I_tec`, `theta_thv`
  - `units`:
    - `I_tec`: A
    - `theta_thv`: K/W

### minimum_theta_thv.json
- path: `/app/outputs/minimum_theta_thv.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Minimum thermal resistance and current. The checker verifies that the reported minimum is indeed the minimum in the CSV and that the value and current are consistent with the recomputed curve.
- schema:
  - `type`: object
  - `required`:
    - `minimum_value`: float (K/W)
    - `current_at_minimum`: float (A)

Notes: Only the single-TEC variable thermal resistance model is reproduced. The full multi-chip temperature uniformity control experiments are omitted as they require specialized hardware and non-public experimental data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "theta_thv_vs_I.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "I_tec",
          "theta_thv"
        ],
        "units": {
          "I_tec": "A",
          "theta_thv": "K/W"
        }
      },
      "description": "Computed variable thermal resistance curve. The checker recomputes theta_thv from the reported I_tec values using the hidden parameters and compares the agent's values within tolerance."
    },
    {
      "file": "minimum_theta_thv.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "minimum_value": "float (K/W)",
          "current_at_minimum": "float (A)"
        }
      },
      "description": "Minimum thermal resistance and current. The checker verifies that the reported minimum is indeed the minimum in the CSV and that the value and current are consistent with the recomputed curve."
    }
  ],
  "notes": "Only the single-TEC variable thermal resistance model is reproduced. The full multi-chip temperature uniformity control experiments are omitted as they require specialized hardware and non-public experimental data."
}
```

## How you are scored
A hidden verifier will independently evaluate each output artifact. For the CSV, it will recompute the θ_thv values using the same physical model and parameters, compare your reported values to the recomputed ones, and award credit based on agreement within a tolerance. It will also verify that the minimum you report indeed corresponds to the smallest value in your CSV and is consistent with the recomputed curve. Structural checks will assess whether the curve has the correct qualitative shape. The final reward is a weighted combination of the scores from both steps.
