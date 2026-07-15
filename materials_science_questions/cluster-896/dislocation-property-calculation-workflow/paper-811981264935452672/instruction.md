## Problem background

Dislocation pile-ups in crystalline materials govern many mechanical properties such as fracture nucleation and yield. When a group of dislocations is driven by an applied stress against a barrier, the spacing between the leading dislocations is a critical quantity. Exact equilibrium solutions for many discrete dislocations are difficult; a simple analytical approach replaces most dislocations with a “super-dislocation” while keeping a few leaders discrete. This task reproduces that approach for a pile-up of edge dislocations and evaluates the accuracy of the resulting approximations.

## Approach

The system consists of (n-1) free edge dislocations on a slip plane forced by an applied shear stress σ against a fixed edge dislocation of strength m at the origin. The dislocations interact through their elastic stress fields. The goal is to estimate the equilibrium distance x1 between the fixed obstacle and the leading free dislocation.

The forces per unit length on a dislocation arise from the stress field of other dislocations and from the applied stress. For an edge dislocation on the plane y=0, the interaction force between two dislocations separated by Δx is A/Δx, where A = μb/(2π(1-ν)) (μ shear modulus, ν Poisson’s ratio). The applied shear stress σ produces a force of magnitude σ per unit length pushing the dislocations toward the obstacle (the sign is such that the equilibrium condition is given below).

First, solve the exact equilibrium for a small number p of free dislocations (p = 1,…,9) without any super-dislocation approximation. The positions x_i (i = 1,…,p) with x_1 < x_2 < … < x_p satisfy the force-balance equations:

  m·A / x_i  +  A · Σ_{j≠i} 1/(x_i - x_j)  =  σ   for i = 1,…,p.

Solve these coupled nonlinear equations numerically to obtain the leading distance x1_p (the position of the first free dislocation) as a function of p and m. Express the result in dimensionless form as u_p = (2σ/A) · x1_p.  This provides the exact reference distances for small systems.

Next, the super-dislocation concept is used to approximate the leading distance for a pile-up of (n-1) free dislocations. By representing all but the first p dislocations as a single super-dislocation and using an effective stress argument, the scaling law is:

  x1_approx (physical) = x1_p (physical) · (m + p) / n.

Using the dimensionless x1_p values, the approximations in the required reporting units are:

- Table 1 (large n, units A/(2nσ)):  x1_approx = x1_p · (m + p)
- Table 2 (n = 10, units A/(2σ)):    x1_approx = x1_p · (m + p) / 10

The asymptotic formula for the leading distance in the limit n → ∞ is derived as:

  x1 = m·(m+1)·A/(n·σ)

These approximations are compared with exact many-dislocation results.

## Reproduction target

Produce tables of approximate leading dislocation distances for the obstacle strengths m = 0.5, 1, 2:
- Table 1: for large n (n → ∞) and p = 1,…,9, x1_approx in units A/(2nσ).
- Table 2: for n = 10 and p = 1,2,3, x1_approx in units A/(2σ).
- State the asymptotic formula as a string.
All numerical values must be reported to at least three decimal places.

## Assets

- Python 3 with NumPy and SciPy. Install via:
  `python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy`

## Workflow steps

### Step 1: Solve exact equilibrium for small p
- Role: process
- Action: For p = 1,2,…,9 and m ∈ {0.5, 1.0, 2.0}, set up the force-balance equations for p free edge dislocations plus the fixed obstacle as described in the Approach. Solve the system numerically to obtain the equilibrium positions x_i, ensuring x_1 < x_2 < … < x_p. Record the leading distance x1_p (the position of the first free dislocation) in dimensionless units (2σ/A)·x1_p. Write these computed values to a JSON file `/app/outputs/exact_x1_p.json` with an array of objects, each having keys `p` (integer), `m` (number), and `x1_p` (number).
- Evidence: `/app/outputs/exact_x1_p.json`

### Step 2: Compute super-dislocation approximations and asymptotic formula
- Role: scored (load-bearing)
- Action: Load the exact x1_p values from `/app/outputs/exact_x1_p.json`. For each combination of p and m, compute the approximate leading dislocation distances as follows:
  · Table 1 (large n, units A/(2nσ)):  x1_approx = x1_p × (m + p)
  · Table 2 (n=10, units A/(2σ)):      x1_approx = x1_p × (m + p) / 10   (only for p = 1,2,3)
  · Asymptotic formula: the string `"x1 = m(m+1)A/(nσ)"`
  Assemble a JSON object with keys `"table1"`, `"table2"`, and `"asymptotic_formula"`. Write it to `/app/outputs/results.json`.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: See Output contract section.
- Scoring: scored by hidden verifier.

## Output files

- `/app/outputs/exact_x1_p.json`  (process evidence)
- `/app/outputs/results.json`      (scored final answer)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Table 1 and Table 2 of approximate leading dislocation distances, plus the asymptotic formula.
- schema:
  - `type`: object
  - `required`: `table1`, `table2`, `asymptotic_formula`
  - `properties`:
    - `table1`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `p`, `m`, `x1_approx`
        - `properties`:
          - `p`:
            - `type`: integer
          - `m`:
            - `type`: number
          - `x1_approx`:
            - `type`: number
    - `table2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `p`, `m`, `n`, `x1_approx`
        - `properties`:
          - `p`:
            - `type`: integer
          - `m`:
            - `type`: number
          - `n`:
            - `type`: integer
          - `x1_approx`:
            - `type`: number
    - `asymptotic_formula`:
      - `type`: string

Notes: Values in table1 are in units A/(2nσ), table2 in units A/(2σ). The asymptotic formula string must be 'x1 = m(m+1)A/(nσ)'.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "table1",
          "table2",
          "asymptotic_formula"
        ],
        "properties": {
          "table1": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "p",
                "m",
                "x1_approx"
              ],
              "properties": {
                "p": {
                  "type": "integer"
                },
                "m": {
                  "type": "number"
                },
                "x1_approx": {
                  "type": "number"
                }
              }
            }
          },
          "table2": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "p",
                "m",
                "n",
                "x1_approx"
              ],
              "properties": {
                "p": {
                  "type": "integer"
                },
                "m": {
                  "type": "number"
                },
                "n": {
                  "type": "integer"
                },
                "x1_approx": {
                  "type": "number"
                }
              }
            }
          },
          "asymptotic_formula": {
            "type": "string"
          }
        }
      },
      "description": "Table 1 and Table 2 of approximate leading dislocation distances, plus the asymptotic formula."
    }
  ],
  "notes": "Values in table1 are in units A/(2nσ), table2 in units A/(2σ). The asymptotic formula string must be 'x1 = m(m+1)A/(nσ)'."
}
```

## How you are scored

A hidden verifier will read `/app/outputs/results.json` and compare the values in `table1` and `table2` to reference values. The verifier checks the numerical values with appropriate tolerances and verifies the asymptotic formula string. Reporting numbers without correctly performing the workflow steps will not earn credit. The final reward is a weighted combination of the checks.
