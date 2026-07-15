# Central Bursting Boundary in Strain-Hardening Metal Forming

## Problem background
In metal forming processes such as wire drawing and extrusion through conical converging dies, internal defects known as central bursts (chevron cracks) can develop under certain combinations of die semi‑cone angle, percent reduction in area, friction, and material strain‑hardening behaviour. An upper‑bound analysis for strain‑hardening materials yields a criterion that defines the boundary between safe parameter combinations and those that promote central bursting. The purpose of this task is to reproduce the critical boundary curves that separate the safe and central‑burst regions as a function of die angle and reduction, for specified values of the strain‑hardening coefficient and friction factor.

## Approach
The central bursting criterion is expressed as an inequality that must be ≤ 0 for central bursting to occur. At the boundary the inequality equals zero. The left‑hand side combines three closed‑form trigonometric auxiliary functions A(α), B(α), f(α) with the die semi‑cone angle α, the reduction ratio (which determines the percent reduction r%), the strain‑hardening coefficient β, and the friction factor m.

The following closed-form expressions define the necessary quantities. α is in radians unless otherwise noted; all trigonometric functions expect radian arguments.

A(α) = 0.378770 α + 0.111251 sin(2α) - 0.004847 sin(4α) + 0.000241 sin(6α)

B(α) = 0.779825 α + 0.190716 sin(2α) - 0.008309 sin(4α) + 0.000474 sin(6α) - sin(α) cos(α) (0.047833 + 0.018857 sin²(α) + 0.009834 sin⁴(α) + 0.005564 sin⁶(α) + 0.003158 sin⁸(α) + 0.001664 sin¹⁰(α))

f(α) = (1 / sin²(α)) * ( 1 - cos(α) sqrt(1 - (11/12) sin²(α)) + (1 / sqrt(11*12)) * ln( (1 + sqrt(11/12)) / ( sqrt(11/12) cos(α) + sqrt(1 - (11/12) sin²(α)) ) ) )

Let R = R_f / R_0 be the radius ratio. The percent reduction in area r% is related to R by r% = (1 - R²) * 100, so R = sqrt(1 - r%/100).

The central bursting criterion is H(α, R, m, β) ≤ 0, where H is defined by the expression below. For the boundary we solve H = 0. The full expression for H is:

H = sqrt(3) * sin(α) * f(α) * (1 - R + 2 ln(R))
    + 2 sqrt(3) * ( (R - 1) A(α) - B(α) ln(R) )
    + 1/R + 1 + ln(R) - 2 α / sin(α)
    + m cos(α) * (1 - R + ln(R))
    + β * {
        (1/√3)*(1/sin(α))*(5/√11)*arcsin(√(11/12) sin(α)) * (2 ln(R) + 1 - R)
        + (1/11)*√(1 - 11/12 sin²(α)) * (2 ln(R) + 3(1 - R))
        - (13/12) (ln(R))²
        + (1/√3) sin(α) (ln(R))²
        - (√3/2) sin(α) (R - 1) ln(R)
        + (38/33) ln(R)
        + (1/2)*(73/33) - (35/33) R + (1/2)*(13/3)*(1/R) + (1/2)*(7/3)*R ln(R)
        + (1/√3)*ln( (√(1 - 11/12 sin²(α)) - 1/√12) / (1 - 1/√12) ) * ln(R)
        - (1/2)*(1/√3)*ln(cos(α)) * (2 ln(R) + (ln(R))²)
        + (1/2)*(1/√3)*ln(sin(α) + 1) * (ln(R))²
        + (1/√3)*(1/sin(α))*ln( √(1 - 11/12 sin²(α)) + (1/√12) sin(α) ) * (2 ln(R) + 1 - R)
        + (1/√3)*(1/sin(α))*ln(cos(α)) * ( (ln(R))² - R ln(R) - ln(R) + R - 1 )
        + (2*m / √(1 - 11/12 sin²(α))) * (
            - (1/2)*(11/12) (ln(R))²
            - (1 - 5/12 * R) ln(R)
            - (7/12) (1 - R)
        )
        + (5/12) sin²(α) (ln(R))²
        + sin²(α) * ( (11/12 - (1/3) R) ln(R) - (7/12) (1 - R) )
      }. For each chosen pair (m, β), we sweep a range of die angles α and, at each α, numerically solve for the percent reduction r% that makes the inequality vanish. The resulting (α, r%) pairs form the boundary curve for that parameter combination. The calculations are purely analytical; no external dataset or training is required.

## Reproduction target
Produce the central bursting boundary curves for the parameter combinations defined by strain‑hardening coefficient β ∈ {0, 0.05, 0.10, 0.15, 0.20} and friction factor m ∈ {0, 0.05, 0.10, 0.15, 0.20}. For each (m, β) pair, vary the die semi‑cone angle α over a reasonable interval (e.g., 5° to 80°) and determine the corresponding critical percent reduction in area r% where the central bursting criterion transitions from safe to danger. Output the resulting points as a CSV file with columns: alpha_deg (die semi‑cone angle in degrees), reduction_percent (critical percent reduction), m (friction factor), and beta (strain‑hardening coefficient).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Central Bursting Criterion Boundary Curves
- Role: scored (load-bearing)
- Action: Implement the analytical central bursting criterion (the inequality that predicts central bursting occurrence) and the associated closed-form trigonometric functions A(α), B(α), f(α). For specified strain-hardening coefficient β and friction factor m pairs (e.g., β ∈ {0, 0.05, 0.10, 0.15, 0.20} and m ∈ {0, 0.05, 0.10, 0.15, 0.20}), sweep a range of die semi-cone angles α (e.g., 5° to 80°) and, for each α, numerically solve for the percent reduction in area r% that makes the criterion expression equal to zero. Output the boundary points as a CSV file.
- Output file: `/app/outputs/boundary_curves.csv`
- Format: csv
- Contract: CSV with columns: alpha_deg (float, die semi-cone angle in degrees), reduction_percent (float, critical percent reduction in area), m (float, friction factor), beta (float, strain-hardening coefficient). Each row corresponds to one point on the boundary curve for a given (m, β) pair.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/boundary_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### boundary_curves.csv
- path: `/app/outputs/boundary_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Boundary points of central bursting criterion curves (critical percent reduction vs. die angle for given friction and strain-hardening coefficient).
- schema:
  - `type`: table
  - `required_columns`: `alpha_deg`, `reduction_percent`, `m`, `beta`
  - `units`:
    - `alpha_deg`: degrees
    - `reduction_percent`: percent
    - `m`: dimensionless
    - `beta`: dimensionless

Notes: The set of (m, β) parameter pairs should be chosen to match the paper's central bursting criterion figures; e.g., β ∈ {0, 0.05, 0.10, 0.15, 0.20} and m ∈ {0, 0.05, 0.10, 0.15, 0.20}. The agent may select a reasonable α sweep and root-finding tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "boundary_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha_deg",
          "reduction_percent",
          "m",
          "beta"
        ],
        "units": {
          "alpha_deg": "degrees",
          "reduction_percent": "percent",
          "m": "dimensionless",
          "beta": "dimensionless"
        }
      },
      "description": "Boundary points of central bursting criterion curves (critical percent reduction vs. die angle for given friction and strain-hardening coefficient)."
    }
  ],
  "notes": "The set of (m, β) parameter pairs should be chosen to match the paper's central bursting criterion figures; e.g., β ∈ {0, 0.05, 0.10, 0.15, 0.20} and m ∈ {0, 0.05, 0.10, 0.15, 0.20}. The agent may select a reasonable α sweep and root-finding tolerance."
}
```

## How you are scored
The hidden verifier reads your `boundary_curves.csv` and compares the boundary curves to a hidden reference set for the same (m, β) pairs. For each parameter combination, the verifier interpolates your predicted reduction_percent at a set of hidden test alpha values. The reward is the fraction of test points for which the absolute error in reduction_percent is within a pre‑defined tolerance band (the tolerance accounts for expected numerical and implementation differences). The final score is this fraction, a float between 0 and 1.
