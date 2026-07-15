# Linear Elastic Finite Element Analysis of Unbonded Length Effects on Internal Replacement Pipe Axial Response

## Problem background
Internal replacement pipe (IRP) systems are used to rehabilitate pipelines that have developed circumferential discontinuities, such as cracks or failed joints. When the ground temperature changes seasonally, the host pipe and IRP expand or contract at different rates because their materials have different thermal expansion coefficients. This differential thermal response induces axial stresses within the IRP and opens the discontinuity. In practice, the bonding between the IRP and the host pipe may fail over a portion of the interface near the discontinuity, creating an unbonded length. The presence of an unbonded length is known to alter the axial stress in the IRP and the opening of the discontinuity, but the quantitative relationship requires analysis. This task uses finite element analysis to compute, for a specific IRP system with a steel host pipe and known material and geometry, how the axial stress and discontinuity opening change as a function of the unbonded length, expressed as ratios relative to the fully bonded case.

## Approach
A linear elastic finite element model of a tubular quarter-symmetry section is used. The model includes a steel host pipe and an ALTRA10® IRP with specified diameters, thicknesses, length, and a circumferential discontinuity of fixed width. A thermal loading equivalent to a temperature change of 27.8 °C is simulated by applying a computed axial displacement to the free end. The fully bonded interface is modeled by gluing the contacting surfaces. One-sided unbonded segments of increasing length are introduced, each starting at the edge of the discontinuity. For each configuration, the average axial stress through the IRP thickness at the mid-span of the discontinuity segment and the opening displacement of the discontinuity are extracted. The ratios of these quantities to the corresponding fully-bonded values are reported for each unbonded length.

## Reproduction target
Produce a CSV file that contains, for each unbonded length (expressed as the dimensionless ratio l_u/c = 1, 2, 4, 6, 8, 10), the ratio of the average axial stress in the IRP (unbonded relative to fully bonded) and the ratio of the discontinuity opening (unbonded relative to fully bonded). The model geometry, material properties, and the applied axial displacement are fully specified in the workflow steps. The file must have columns l_u_c, stress_ratio, opening_ratio, with one row per l_u/c value. The target is to produce these stress and opening ratios; the numerical values are determined by the finite element analysis you perform.

## Assets

- Finite element solver (e.g., CalculiX): http://www.calculix.de/

## Workflow steps

### Step 1: Compute applied axial displacement
- Role: process
- Action: Compute the axial displacement δ_T to be applied at the free end of the pipe that simulates the thermal loading of ΔT=27.8°C, using the analytical expression that depends on geometry (D_oH, t_H, t_I, c, L) and material properties (E_I, E_H, α_I, α_H). The specific parameter values are: D_oH=323.85 mm, t_H=6.35 mm, t_I=4.115 mm, c=12.7 mm, L=3048 mm, E_I=3.77 GPa, E_H=210.7 GPa, α_I=45e-6 /°C, α_H=12e-6 /°C. Write the computed displacement to a text file as evidence.
- Evidence: `/app/outputs/displacement_value.txt`

### Step 2: FE analysis and ratio computation
- Role: scored (load-bearing)
- Action: Build a linear elastic finite element model of the IRP system with one end fixed and the other free, using quarter symmetry. Use SOLID185 elements (or equivalent). The host pipe is steel, IRP is ALTRA10 with the properties above. Model a fully bonded interface (Glue condition) for the reference case. Apply the computed axial displacement at the free end. Then introduce a one-sided unbonded segment at the interface starting from the discontinuity edge, with no bonding condition over the unbonded length. For the fully bonded case and for each unbonded length l_u = 12.7, 25.4, 50.8, 76.2, 101.6, 127.0 mm (corresponding to l_u/c = 1,2,4,6,8,10), extract the IRP average axial stress along the thickness at the midspan of the discontinuity segment and the discontinuity opening (difference in axial displacement of the two upper edges). Compute the ratios: stress_ratio = (axial stress in unbonded model) / (axial stress in fully bonded model) and opening_ratio = (opening in unbonded model) / (opening in fully bonded model). Write the results to a CSV file.
- Output file: `/app/outputs/unbonded_ratios.csv`
- Format: csv
- Contract: l_u_c (float, dimensionless ratio l_u/c), stress_ratio (float, dimensionless), opening_ratio (float, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/unbonded_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### unbonded_ratios.csv
- path: `/app/outputs/unbonded_ratios.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: File containing six rows (one per l_u/c value) with the computed axial stress ratio and discontinuity opening ratio (unbonded relative to fully bonded). The checker will compare the ratios to hidden reference values within tolerances and verify that stress_ratio strictly decreases and opening_ratio strictly increases with l_u_c.
- schema:
  - `type`: table
  - `required_columns`: `l_u_c`, `stress_ratio`, `opening_ratio`
  - `units`:
    - `l_u_c`: dimensionless
    - `stress_ratio`: dimensionless
    - `opening_ratio`: dimensionless

Notes: The scoring will additionally audit the monotonic trends (stress_ratio decreasing, opening_ratio increasing) as part of verification. The agent must use a public finite element solver and all geometry/material inputs are specified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "unbonded_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "l_u_c",
          "stress_ratio",
          "opening_ratio"
        ],
        "units": {
          "l_u_c": "dimensionless",
          "stress_ratio": "dimensionless",
          "opening_ratio": "dimensionless"
        }
      },
      "description": "File containing six rows (one per l_u/c value) with the computed axial stress ratio and discontinuity opening ratio (unbonded relative to fully bonded). The checker will compare the ratios to hidden reference values within tolerances and verify that stress_ratio strictly decreases and opening_ratio strictly increases with l_u_c."
    }
  ],
  "notes": "The scoring will additionally audit the monotonic trends (stress_ratio decreasing, opening_ratio increasing) as part of verification. The agent must use a public finite element solver and all geometry/material inputs are specified."
}
```

## How you are scored
A hidden verifier will read your submitted CSV file. It will compare each stress_ratio and opening_ratio against hidden reference values derived from the source paper, and will also check that the stress_ratio values are strictly decreasing with increasing l_u/c and that the opening_ratio values are strictly increasing with increasing l_u/c. Your reward will be based on how many of the reported ratios fall within the allowed tolerance and whether the monotonic trends hold. The verifier combines the scores from each workflow stage into a final reward. Simply reporting pre-known numbers is not sufficient; you must produce the ratios through your own finite element analysis.
