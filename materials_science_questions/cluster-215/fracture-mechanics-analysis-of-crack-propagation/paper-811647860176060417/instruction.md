# Fracture Mechanics Analysis of Crack Propagation: Effect of Initial Crack Length and Specimen Size on Delayed Failure Time

## Problem background
In static fatigue of brittle ceramics, the relationship between applied load, crack growth rate, and time to failure is governed by linear elastic fracture mechanics. When a constant load is applied to a specimen containing an initial crack, subcritical crack growth occurs according to a power‑law dependence on the stress intensity factor. The time required for the crack to grow to a critical size and cause failure depends on the initial stress intensity factor, the specimen dimensions, and the initial crack length. Understanding how these parameters influence the failure time—especially the roles of specimen width and initial crack size—is essential for designing accelerated tests and identifying lower‑bound thresholds for crack growth. This task addresses that question by implementing a fracture‑mechanics model for a three‑point bend specimen and computing the nondimensional failure time across a wide range of geometric conditions.

## Approach
The model is built around the geometry factor F(x) for a three‑point bend specimen with span S=4W. Use the specific polynomial: F(x) = 1.107 - 1.65*x + 0.93*x**2. The central quantity is the nondimensional integral I(x0, n) = ∫ from x0 to 1 of [ sqrt(x0) F(x0) / ( sqrt(x) F(x) ) ]^n dx, where x = a/W is the nondimensional crack length. This integral encapsulates the specimen geometry and the crack‑growth exponent n. Once I is determined, the nondimensional failure time T_f is obtained from the fracture‑mechanics relation (constant load case) that connects the initial stress intensity factor K_Ii, specimen width W, initial crack length a0, and the integral I. The crack‑velocity exponent n is treated as a parameter, and the geometry factor F(x) is a known standard expression for the three‑point bend configuration. The workflow proceeds in two stages: first, numerically evaluate I(x0,n) for a dense grid of x0 and several n values; second, use that relation to compute T_f for selected conditions that span the large‑crack and small‑crack regimes, thereby revealing how failure time scales with specimen width and initial crack length.

## Reproduction target
Your goal is to produce two scored artifacts that together verify the predicted scaling laws for delayed failure.

1. **Integral table (I_vs_x0.csv)** – Compute the nondimensional integral I for a range of dimensionless initial crack lengths x0 (covering both the small‑crack and large‑crack regimes) and for several crack‑growth exponents n (e.g., n = 5, 10, 20). The output table must contain one row per (x0, n) pair with columns x0, n, and I_value.

2. **Scaling verification table (scaling_verification.csv)** – Using the same fracture‑mechanics relation and geometry factor, compute the nondimensional failure time T_f for:
   - **Large‑crack regime (x0 > 0.05):** fix the initial stress intensity factor K_Ii and initial crack length a0, then vary the specimen width W, recording T_f to demonstrate the dependence on W.
   - **Small‑crack regime (x0 < 0.05):** fix K_Ii and W, then vary a0 (so that x0 varies), recording T_f to demonstrate the dependence on a0.

The table must contain columns W, a0, K_Ii, and T_f. All geometric quantities should be reported in consistent length units, and K_Ii in MPa·√m.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute integral I(x0, n) curves
- Role: scored (load-bearing)
- Action: Define the geometry factor F(x) for a three‑point bend specimen (span S=4W) using the specific polynomial F(x) = 1.107 - 1.65*x + 0.93*x**2. For a range of nondimensional initial crack lengths x0 and several crack‑growth exponents n, numerically evaluate the integral I = ∫_{x0}^{1} [ √x0 F(x0) / ( √x F(x) ) ]^n dx. Write the results to I_vs_x0.csv.
- Output file: `/app/outputs/I_vs_x0.csv`
- Format: csv
- Contract: Columns: x0 (float, nondimensional initial crack length), n (integer, crack‑growth exponent), I_value (float, computed integral). One row per (x0, n) pair.
- Scoring: scored by hidden verifier

### Step 2: Verify T_f scaling with specimen width and initial crack length
- Role: scored
- Action: Using the same fracture‑mechanics relation and geometry factor F(x), compute the nondimensional failure time T_f for (a) large‑crack regime (x0>0.05): fix initial K_Ii and a0, vary specimen width W; (b) small‑crack regime (x0<0.05): fix initial K_Ii and W, vary initial crack length a0. Record W, a0, K_Ii and T_f. Write the results to scaling_verification.csv.
- Output file: `/app/outputs/scaling_verification.csv`
- Format: csv
- Contract: Columns: W (float, specimen width in consistent length units), a0 (float, initial crack length in same units), K_Ii (float, initial stress intensity factor in MPa·√m), T_f (float, nondimensional failure time). One row per (W, a0, K_Ii) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/I_vs_x0.csv`
- `/app/outputs/scaling_verification.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### I_vs_x0.csv
- path: `/app/outputs/I_vs_x0.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Numerical values of the integral I(x0,n) obtained by numerical integration with the known three‑point bend geometry factor.
- schema:
  - `type`: table
  - `required_columns`: `x0`, `n`, `I_value`

### scaling_verification.csv
- path: `/app/outputs/scaling_verification.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Verification of the scaling relations: for large cracks T_f ∝ W, for small cracks T_f ∝ a0.
- schema:
  - `type`: table
  - `required_columns`: `W`, `a0`, `K_Ii`, `T_f`

Notes: All quantities are nondimensional where specified. The geometry factor F(x) for a three‑point bend specimen with span S=4W is a publicly available standard expression.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "I_vs_x0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x0",
          "n",
          "I_value"
        ]
      },
      "description": "Numerical values of the integral I(x0,n) obtained by numerical integration with the known three‑point bend geometry factor."
    },
    {
      "file": "scaling_verification.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "W",
          "a0",
          "K_Ii",
          "T_f"
        ]
      },
      "description": "Verification of the scaling relations: for large cracks T_f ∝ W, for small cracks T_f ∝ a0."
    }
  ],
  "notes": "All quantities are nondimensional where specified. The geometry factor F(x) for a three‑point bend specimen with span S=4W is a publicly available standard expression."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently scores each workflow stage’s artifact and combines the scores into a single reward.

- **For I_vs_x0.csv:** the verifier re‑computes the same integral using the known geometry factor and numerical integration, then compares your I_value entries against its recomputed values with a relative tolerance. Only rows that closely match the verifier’s numbers receive credit.

- **For scaling_verification.csv:** the verifier performs a structural audit. In the large‑crack subset (x0 > 0.05), it verifies that T_f / W is constant (within a small tolerance) across different W at fixed K_Ii and a0, consistent with the predicted proportionality T_f ∝ W. In the small‑crack subset (x0 < 0.05), it verifies that T_f / a0 is constant across different a0 at fixed K_Ii and W, consistent with the predicted proportionality T_f ∝ a0. It may also recompute a few selected T_f values to confirm the model implementation.

Merely reporting the paper’s numbers without generating the artifacts via the described computational workflow will not pass these checks.
