# Tricritical Points of Classical Heisenberg Model with Trimodal Random Field

## Problem background
The classical Heisenberg model (n=3) with quenched bond disorder and a trimodal random magnetic field distribution exhibits complex phase behaviour, including tricritical points and reentrant transitions. Understanding how the disorder in exchange interactions (parametrized by α) and the shape of the trimodal field distribution (parametrized by p) control the existence and location of tricritical points is the central question. This task asks you to compute the tricritical temperature (T_t = k_B T_t / J) and tricritical field (h_t) for given parameter combinations.

## Approach
The effective field theory (EFT) for the classical Heisenberg model on a simple cubic lattice (coordination Z=6) is formulated using a two-spin cluster. The exchange interactions follow a bimodal distribution (strength K with disorder α) and the random field follows a trimodal distribution (strength h, concentration p). The average magnetization is expanded in odd powers; the coefficients A1(K,α,h,p) and A3(K,α,h,p) are obtained from thermal and random averages involving a generalized hyperbolic tangent function that uses modified Bessel functions (I_{3/2} and I_{1/2}). A continuous transition line satisfies A1=1 with A3<0, and the tricritical point is the solution of A1=1 and A3=0 simultaneously. The task is to implement these coefficients, then numerically solve for K_t and h_t and convert to temperature T_t = 1/K_t (with J=k_B=1).

## Reproduction target
Produce a JSON file, tricritical_points.json, containing an array of objects, one for each of the eight required (α, p) combinations: α = 0.0 for p = 0.0, 0.1, 0.2, 0.3; and α = 0.5 for p = 0.0, 0.1, 0.2, 0.3. Each object must have keys alpha (float), p (float), T_t (float or null), h_t (float or null), exists (bool). The solver must be applied to each pair; the boolean exists indicates whether a tricritical point was found. If exists is false, set T_t and h_t to null.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: EFT coefficient implementation
- Role: process
- Action: Implement the effective field theory (EFT) for the classical Heisenberg model (n=3) on a simple cubic lattice (coordination Z=6) with bimodal bond disorder (parametrized by alpha) and trimodal random field distribution (parametrized by p and h). Derive the magnetization expansion coefficients A1(K,alpha,h,p) and A3(K,alpha,h,p) using the two-spin cluster formulation with the function of generalized hyperbolic tangent defined via modified Bessel functions. Provide callable functions that compute A1 and A3 for given parameter values.
- Evidence: none

### Step 2: Tricritical point solver
- Role: process
- Action: Implement a numerical solver that, for given alpha and p, finds the tricritical point by simultaneously solving A1(K,alpha,h,p)=1 and A3(K,alpha,h,p)=0. Use root-finding (e.g., scipy.optimize) to solve for K and h. Convert the solution K_t to temperature T_t = J/(k_B K_t) with J=1, k_B=1. The solver must return T_t, h_t, and a boolean indicating whether a tricritical point exists.
- Evidence: none

### Step 3: Tricritical point evaluation
- Role: scored (load-bearing)
- Action: For each (alpha, p) pair in {(0.0,0.0), (0.0,0.1), (0.0,0.2), (0.0,0.3), (0.5,0.0), (0.5,0.1), (0.5,0.2), (0.5,0.3)}, use the solver from Step 2 to compute the tricritical point. Write the results to tricritical_points.json as an array of objects, each containing keys: alpha, p, T_t, h_t, exists. Use null for T_t and h_t when exists is false.
- Output file: `/app/outputs/tricritical_points.json`
- Format: json
- Contract: JSON array of objects with keys: alpha (float), p (float), T_t (float or null), h_t (float or null), exists (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tricritical_points.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tricritical_points.json
- path: `/app/outputs/tricritical_points.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Tricritical points for the classical Heisenberg model with trimodal random field, evaluated for the eight parameter combinations listed in the paper's Table 1.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `alpha`, `p`, `T_t`, `h_t`, `exists`
    - `properties`:
      - `alpha`:
        - `type`: number
      - `p`:
        - `type`: number
      - `T_t`:
        - `type`: `number`, `null`
      - `h_t`:
        - `type`: `number`, `null`
      - `exists`:
        - `type`: boolean

Notes: The scorer compares the reported T_t and h_t to hidden paper gold values with relative tolerances (1% for T_t, 2% for h_t). Full credit if within tolerance, linear decay outside. For combinations where exists=false, T_t and h_t must be null.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tricritical_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "alpha",
            "p",
            "T_t",
            "h_t",
            "exists"
          ],
          "properties": {
            "alpha": {
              "type": "number"
            },
            "p": {
              "type": "number"
            },
            "T_t": {
              "type": [
                "number",
                "null"
              ]
            },
            "h_t": {
              "type": [
                "number",
                "null"
              ]
            },
            "exists": {
              "type": "boolean"
            }
          }
        }
      },
      "description": "Tricritical points for the classical Heisenberg model with trimodal random field, evaluated for the eight parameter combinations listed in the paper's Table 1."
    }
  ],
  "notes": "The scorer compares the reported T_t and h_t to hidden paper gold values with relative tolerances (1% for T_t, 2% for h_t). Full credit if within tolerance, linear decay outside. For combinations where exists=false, T_t and h_t must be null."
}
```

## How you are scored
A hidden verifier inspects tricritical_points.json and compares the reported T_t and h_t for each (α, p) pair to hidden reference values. Full credit is earned when the computed values fall within a prescribed tolerance of the reference; partial credit is given on a linear decay if they deviate. The verifier also checks that exists is true for these parameter combinations and that null values are returned when exists is false. Simply reporting pre-obtained numbers will not pass – your code must compute the results.
