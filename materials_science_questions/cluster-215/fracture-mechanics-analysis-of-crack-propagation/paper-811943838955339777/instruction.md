# Crack-Asperity Interaction Simulation: Mastercurve and Multiple-Asperity Shielding Analysis

## Problem background
In fatigue crack growth, premature contact of crack faces (crack closure) due to surface asperities can alter the effective stress intensity factor experienced at the crack tip. One long-standing debate concerns whether compliance-based closure measurements overestimate the true local driving force. This task investigates the elastic interaction between a mode‑I semi‑infinite crack and rigid asperities to quantify the ratio of the local crack‑tip stress intensity factor k_local to the far‑field closure stress intensity factor K_cl, as a function of asperity geometry and position.

## Approach
The analysis uses linear elastic fracture mechanics. The crack is modelled as an unbounded body cut along the negative x-axis loaded by a far-field mode‑I stress intensity factor. A rigid parabolic asperity placed behind the tip prescribes the crack‑face displacement between X and X−ΔX. The mixed boundary value problem (displacement prescribed on the asperity interval, traction‑free elsewhere) is reduced to a Muskhelishvili‑type singular integral equation for the unknown contact stress distribution P(x). The kernel involves an arctan term that admits closed‑form integration when the contact stress is approximated by piecewise-constant elements (step functions). Solving the resulting linear system yields the contact stresses, from which the local stress intensity factor is computed via a weighted sum of the piecewise‑constant values. By sweeping the dimensionless asperity position X/ΔX, a mastercurve of k_local/K_cl can be obtained. The same framework is extended to multiple asperities by superimposing several contact intervals; all asperity heights are set such that first crack face contact occurs at the same far‑field closure level K_cl. Two configurations are considered: four equal‑width asperities at increasing positions, and four asperities of increasing width (proportional to position), both listed in the workflow steps.

## Reproduction target
Compute and submit the single‑asperity mastercurve as a CSV file containing at least 20 points of (X_over_dX, k_local_over_K_cl) covering the range from approximately 1 to 1000. Separately, compute the k_local_over_K_cl ratio for the two multiple‑asperity arrangements described in Step 2 and submit the results as a JSON object with keys 'equal_widths' and 'equal_effectiveness'.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Single-asperity elastic interaction mastercurve
- Role: scored
- Action: Implement a numerical solver for the Muskhelishvili-type singular integral equation describing a semi-infinite mode-I crack in contact with a single rigid parabolic asperity. Discretize the asperity contact interval using piecewise-constant elements, compute element integrals via the closed-form kernel (arctan function of endpoint ratios), assemble and solve the linear system for contact stresses. Compute the local stress intensity factor k_local and record the dimensionless ratio k_local/K_cl for a range of asperity positions X/ΔX spanning near 1 to at least 1000, ensuring at least 20 points to capture the mastercurve trend.
- Output file: `/app/outputs/single_asperity_mastercurve.csv`
- Format: csv
- Contract: columns: X_over_dX (float), k_local_over_K_cl (float). At least 20 rows covering X/ΔX from approximately 1 to 1000.
- Scoring: scored by hidden verifier

### Step 2: Multiple-asperity elastic interaction results
- Role: scored
- Action: Extend the integral-equation solver to handle four rigid asperities arranged in two configurations from the literature: equal-width asperities at dimensionless positions 1000,2000,4000,8000 with width ΔX₁; and equal-effectiveness asperities at the same positions with widths proportional to position (widths ΔX₁,2ΔX₁,4ΔX₁,8ΔX₁). All asperity heights are set so that first contact occurs at the same far-field closure level K_cl. Solve for contact stresses, compute the local stress intensity factor k_local, and record the resulting ratio k_local/K_cl for each configuration.
- Output file: `/app/outputs/multiple_asperity_results.json`
- Format: json
- Contract: JSON object with keys 'equal_widths' and 'equal_effectiveness', each mapping to a float value representing the computed k_local_over_K_cl.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/single_asperity_mastercurve.csv`
- `/app/outputs/multiple_asperity_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### single_asperity_mastercurve.csv
- path: `/app/outputs/single_asperity_mastercurve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mastercurve of the ratio of local crack-tip stress intensity factor to closure stress intensity factor as a function of dimensionless asperity position.
- schema:
  - `type`: table
  - `required_columns`: `X_over_dX`, `k_local_over_K_cl`
  - `units`:
    - `X_over_dX`: dimensionless
    - `k_local_over_K_cl`: dimensionless

### multiple_asperity_results.json
- path: `/app/outputs/multiple_asperity_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed k_local/K_cl ratios for the two multiple-asperity configurations (equal widths and equal effectiveness).
- schema:
  - `type`: object
  - `required`:
    - `equal_widths`: number
    - `equal_effectiveness`: number
  - `units`:
    - `equal_widths`: dimensionless
    - `equal_effectiveness`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "single_asperity_mastercurve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "X_over_dX",
          "k_local_over_K_cl"
        ],
        "units": {
          "X_over_dX": "dimensionless",
          "k_local_over_K_cl": "dimensionless"
        }
      },
      "description": "Mastercurve of the ratio of local crack-tip stress intensity factor to closure stress intensity factor as a function of dimensionless asperity position."
    },
    {
      "file": "multiple_asperity_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "equal_widths": "number",
          "equal_effectiveness": "number"
        },
        "units": {
          "equal_widths": "dimensionless",
          "equal_effectiveness": "dimensionless"
        }
      },
      "description": "Computed k_local/K_cl ratios for the two multiple-asperity configurations (equal widths and equal effectiveness)."
    }
  ],
  "notes": ""
}
```

## How you are scored
After you finish, a hidden verifier reads your two output files. It independently evaluates the mastercurve by comparing your computed (X_over_dX, k_local_over_K_cl) points to a hidden reference curve, and checks that the results for the two multiple‑asperity configurations match hidden reference values within numerical tolerances. The final score is a weighted combination of the scores from each artifact. Reporting a number is not enough — your numerical solver must actually produce the curve and ratios.
