# Brittle Fracture Initiation Parameters for Ellipsoidal Cracks

## Problem background
The initiation of brittle fracture under triaxial stress is modeled using Griffith's theory, treating cracks as flattened ellipsoidal cavities in an isotropic elastic solid. The key quantity is the maximum tensile stress on the cavity surface, which determines whether tensile or shear fracture occurs. From this theory, important dimensionless parameters can be derived that characterize the fracture initiation envelope, the uniaxial strength ratio, the transition stress between fracture modes, and the shear stress at a high confining pressure. These quantities depend on the crack shape (axis ratio b/a) and the material's Poisson's ratio (ν), and they can be computed from the analytical expressions that arise from the Eshelby inclusion theory.

## Approach
The fracture initiation criteria are expressed in terms of elliptic integrals of the first and second kind (ℱ and ℰ) with modulus k² = 1 − b²/a², and a set of derived coefficients that combine these integrals and ν. The critical parameters – A (a coefficient in the Mohr envelope), the uniaxial compressive strength ratio K₃*/K₁*, the transition stress ratio K₃(tr.)/K₁*, and the normalized shear stress p₁₃⁴/K₁* at p₃₃⁴/K₁* = −35 – are obtained by evaluating these integrals and performing simple arithmetic. The workflow consists of a single compute step: implement the relevant formulas using numerical libraries (numpy, scipy), then evaluate them for the three specified (b/a, ν) pairs and output the results in a CSV file.

## Reproduction target
Compute the four fracture initiation parameters (A, compressive_strength_ratio, transition_stress_ratio, shear_stress_ratio_at_minus35) for the following three (b/a, ν) pairs: (0.8, 0.1), (1.0, 0.3), (1.0, 0.4). Write the results to /app/outputs/table1.csv, with columns: b_over_a, nu, A, compressive_strength_ratio, transition_stress_ratio, shear_stress_ratio_at_minus35.

## Assets

- numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compute Table 1 fracture parameters
- Role: scored (load-bearing)
- Action: For each (b/a, ν) pair: (0.8, 0.1), (1.0, 0.3), (1.0, 0.4), compute the four parameters using numpy and scipy:

1. Compute m = 1 − (b/a)².  Then evaluate the complete elliptic integrals: K = scipy.special.ellipk(m), E = scipy.special.ellipe(m) (these are the symbols ℱ and ℰ used in the theory).  The modulus is k = √m.

2. Compute the coefficient η1313 = 1 / ( E + (ν/(1−ν))·(K − E)·(b/(a·k))² ).

3. Compute Δ1 = (E / (2·(1−ν))) · ((1−2ν)/(1−ν)).

4. Compute A = ( (1−2ν)/(1−ν) ) / ( Δ1 · η1313 ).

5. Compute compressive_strength_ratio = −A·(2 + A).

6. Compute transition_stress_ratio = 1 − A².

7. Compute shear_stress_ratio_at_minus35 = A·√(1 − (−35)) = 6·A (derived from the Mohr envelope (p₁₃⁴/K₁*)² = A²·(1 − p₃₃⁴/K₁*) with p₃₃⁴/K₁* = −35).

Write the three rows to /app/outputs/table1.csv as described.
- Output file: `/app/outputs/table1.csv`
- Format: csv
- Contract: Columns: b_over_a (float, crack axis ratio b/a), nu (float, Poisson's ratio), A (float, Mohr envelope coefficient), compressive_strength_ratio (float, K3*/K1*), transition_stress_ratio (float, K3(tr.)/K1*), shear_stress_ratio_at_minus35 (float, p13^4/K1* at p33^4/K1*=-35). Three rows, one for each (b/a, nu) pair.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table1.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table1.csv
- path: `/app/outputs/table1.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed fracture initiation parameters for three (b/a, nu) pairs: (0.8,0.1), (1.0,0.3), (1.0,0.4). Values are compared to the paper's Table 1 with a relative tolerance of 5e-2.
- schema:
  - `type`: table
  - `required_columns`: `b_over_a`, `nu`, `A`, `compressive_strength_ratio`, `transition_stress_ratio`, `shear_stress_ratio_at_minus35`
  - `columns`:
    - `b_over_a`: float
    - `nu`: float
    - `A`: float
    - `compressive_strength_ratio`: float
    - `transition_stress_ratio`: float
    - `shear_stress_ratio_at_minus35`: float

Notes: The hidden checker compares each numeric cell to the paper-reported gold value using a relative tolerance of 5e-2. Reward is the fraction of correctly matched cells.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "b_over_a",
          "nu",
          "A",
          "compressive_strength_ratio",
          "transition_stress_ratio",
          "shear_stress_ratio_at_minus35"
        ],
        "columns": {
          "b_over_a": "float",
          "nu": "float",
          "A": "float",
          "compressive_strength_ratio": "float",
          "transition_stress_ratio": "float",
          "shear_stress_ratio_at_minus35": "float"
        }
      },
      "description": "Computed fracture initiation parameters for three (b/a, nu) pairs: (0.8,0.1), (1.0,0.3), (1.0,0.4). Values are compared to the paper's Table 1 with a relative tolerance of 5e-2."
    }
  ],
  "notes": "The hidden checker compares each numeric cell to the paper-reported gold value using a relative tolerance of 5e-2. Reward is the fraction of correctly matched cells."
}
```

## How you are scored
A hidden verifier will read your /app/outputs/table1.csv and compare each numeric cell against the expected reference values. Your score is the fraction of cells that agree within a prescribed relative tolerance. All four quantities must be computed for all three parameter pairs; the verifier will count each cell independently. The reward is a number between 0 and 1.
