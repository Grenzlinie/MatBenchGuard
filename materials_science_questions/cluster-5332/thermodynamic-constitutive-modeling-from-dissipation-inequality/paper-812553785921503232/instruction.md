# Return Mapping Algorithm for Extrinsic Trapezoidal Traction-Separation Law

## Problem background
Ductile failure in metals involves the interaction of plasticity and damage. This work develops a thermodynamically consistent Discontinuous Galerkin (DG) formulation that couples finite-strain elastoplasticity in the bulk with an extrinsic traction–separation law (TSL) on the interface to model both brittle and ductile debonding. The TSL includes a transition gap parameter, ζ_b, that controls the amount of constant-traction plateau before softening, and a local return mapping algorithm updates the damage gap and interface traction at each load step. Verification of this return mapping is essential for the overall simulation framework. This task implements the stand-alone return mapping for the extrinsic trapezoidal TSL and obtains the normal traction–separation curves for two values of ζ_b, revealing the shape of the cohesive response.

## Approach
The return mapping uses a trial traction computed from the current opening jump and a penalty stiffness. The yield function is f = ||T|| - (P_c - Q^d), where P_c is the critical debonding traction and Q^d is a hardening/softening variable. The hardening law distinguishes three regions: (i) forward damage — when the residual gap is less than ζ_b, Q^d does not evolve, leading to a constant traction plateau if ζ_b>0; (ii) wake damage — for gaps between ζ_b and ζ_c, Q^d increases linearly with the incremental consistency parameter, driving softening; (iii) opening — beyond ζ_c the interface is fully separated and traction is zero. The incremental consistency parameter is obtained from the consistency condition for each region, and the gap is updated via an associative flow rule. Using fixed material parameters P_c = 5.5 MPa, ζ_c = 1.1 mm, and a user-chosen positive penalty stiffness, the algorithm will be applied to a monotonic normal opening history from 0.0 to 1.2 mm in small increments. Two cases will be run: ζ_b = 0 mm (no plateau, brittle behavior) and ζ_b = 0.2 mm (plateau, ductile behavior). At each opening step the traction magnitude and gap are recorded.

## Reproduction target
Produce a CSV file named traction_separation_curve.csv containing three columns: opening_gap_mm (float), traction_MPa (float), case (string, either 'zeta_b=0' or 'zeta_b=0.2'). The rows must be ordered by increasing opening gap for each case. The file must cover opening gaps from 0.0 to 1.2 mm inclusive, with a step size no larger than 0.01 mm. The required properties of the curves — presence of a plateau for ζ_b=0.2, immediate softening after the peak for ζ_b=0, and the correct peak traction level — will be verified by a hidden checker.

## Assets
No external datasets, models, or proprietary tools are required. The only software needed is a standard Python 3 environment with the numpy library. Both are freely available (Python from python.org, numpy via pip).

## Workflow steps

### Step 1: Generate traction-separation curves
- Role: scored (load-bearing)
- Action: Implement the piecewise return mapping formulas (forward, wake, opening regions) of the extrinsic trapezoidal traction-separation law using the closed-form expressions for the incremental consistency parameter and gap update. For two cases of the transition gap parameter (0 mm and 0.2 mm), apply a monotonic normal opening from 0.0 to 1.2 mm in steps ≤ 0.01 mm. At each step compute the trial normal traction, check the yield condition, perform the return mapping, and record the resulting normal traction magnitude and opening gap. Use the given material parameters (critical debonding traction = 5.5 MPa, maximum residual opening = 1.1 mm) and a reasonable positive penalty stiffness.
- Output file: `/app/outputs/traction_separation_curve.csv`
- Format: csv
- Contract: Columns: opening_gap_mm (float), traction_MPa (float), case (string, 'zeta_b=0' or 'zeta_b=0.2'). Rows ordered by increasing opening gap for each case, spanning [0.0, 1.2] mm in steps ≤ 0.01 mm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/traction_separation_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### traction_separation_curve.csv
- path: `/app/outputs/traction_separation_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The traction-separation response computed from the extrinsic trapezoidal TSL return mapping for two transition gap values. Structural checks verify peak traction equals Pc, a plateau for ζ_b>0, and immediate softening for ζ_b=0.
- schema:
  - `type`: table
  - `required_columns`: `opening_gap_mm`, `traction_MPa`, `case`
  - `units`:
    - `opening_gap_mm`: mm
    - `traction_MPa`: MPa

Notes: The checker applies a structural audit: derivative sign, peak magnitude, plateau extent and monotonicity per case. No absolute trajectory is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "traction_separation_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "opening_gap_mm",
          "traction_MPa",
          "case"
        ],
        "units": {
          "opening_gap_mm": "mm",
          "traction_MPa": "MPa"
        }
      },
      "description": "The traction-separation response computed from the extrinsic trapezoidal TSL return mapping for two transition gap values. Structural checks verify peak traction equals Pc, a plateau for ζ_b>0, and immediate softening for ζ_b=0."
    }
  ],
  "notes": "The checker applies a structural audit: derivative sign, peak magnitude, plateau extent and monotonicity per case. No absolute trajectory is required."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the CSV and performs numerical checks. For each case, the verifier examines: (1) that the traction increases with opening before reaching its maximum value; (2) that the maximum traction equals the critical traction of the TSL; (3) for the ζ_b=0 case, that the traction decreases in the first few steps after the peak; (4) for the ζ_b=0.2 case, that the traction remains approximately constant (within a tolerance) for opening gaps up to slightly above ζ_b and then decreases monotonically. The checks use finite differencing and tolerance comparisons. Passing all checks earns a score of 1.0 for the scored step.
