# Critical Ising Correlation Functions Computation

## Problem background
The two-dimensional Ising model at its critical temperature exhibits power-law decay of spin-spin correlation functions with distance. Exact closed-form expressions exist for diagonal and next-to-diagonal correlations, and a quadratic difference equation can generate all small-distance correlations iteratively. Systematic asymptotic expansions including lattice corrections have been derived up to order R⁻⁶ for both symmetric and anisotropic couplings. This task computes the exact and asymptotic correlation values and the anisotropic correction coefficients from the explicit formulas, providing a numerical validation of the correspondence between exact results and asymptotic series.

## Approach
The computation proceeds in four stages. First, exact correlation values C(M,N) for the symmetric case (where the coupling ratio satisfies sinh(2Hc)=1) are built using the known diagonal ratio expressed with gamma functions, a hypergeometric formula for the next-to-diagonal correlation, and the quadratic difference equation with reflection symmetry to fill all entries for 0 ≤ M ≤ N ≤ 5. Second, the asymptotic expansion for the diagonal correlation lnC(M,M) is evaluated using Bernoulli numbers and a known amplitude constant, with the exact value obtained from the product of diagonal ratios. Third, the next-to-diagonal asymptotic expansion lnC(M,M+1) is computed using Bernoulli and Euler numbers; the exact value is obtained from the hypergeometric expression. Fourth, for the general anisotropic case defined by sinh(2Hc)·sinh(2Vc)=1 with anisotropy parameter u = cos(2α), the angle-dependent lattice correction coefficients A1(θ), A2(θ), A3(θ) are evaluated on a grid of α and θ using trigonometric polynomials. Each stage outputs a CSV or JSON artifact for verification.

## Reproduction target
Goal: compute the spin correlation function C(M,N) at critical temperature and compare exact values with asymptotic expansions. Specifically: (1) Produce the exact symmetric-case C(M,N) matrix for 0 ≤ M,N ≤ 5. (2) Compute the exact and asymptotic lnC(M,M) for M=1..20 and report both columns. (3) Compute the exact and asymptotic lnC(M,M+1) for M=1..20 and report both columns. (4) For the anisotropic case, evaluate the correction coefficients A1(θ), A2(θ), A3(θ) on a grid covering α from 0 to π/2 and θ from 0 to π/2 with step at least π/16, and output all values. The asymptotic expansions are to be compared with the exact values; the anisotropic coefficients are standalone. The default metric is absolute value of the computed quantity; the verifier checks agreement with independent recomputations.

## Assets

- NumPy: numpy
- SciPy: scipy
- mpmath: mpmath

## Workflow steps

### Step 1: Compute exact symmetric correlations C(M,N) for 0 le M,N le 5
- Role: scored
- Action: Compute the exact spin correlation function C(M,N) for the symmetric case (sinh(2Hc)=1) on a square lattice for distances 0 <= M, N <= 5. Use the diagonal ratio expressed in terms of gamma functions, the closed-form next-to-diagonal expression involving the hypergeometric function, and the quadratic difference equation with reflection symmetry. Fill all entries for 0 <= M <= N <= 5 and output the complete table.
- Output file: `/app/outputs/exact_symmetric.csv`
- Format: csv
- Contract: CSV with columns: M (int), N (int), C (float). Rows for 0 <= M <= N <= 5, symmetric case.
- Scoring: scored by hidden verifier

### Step 2: Compute diagonal asymptotic expansion ln C(M,M)
- Role: scored
- Action: Compute the exact natural logarithm of the diagonal correlation function, lnC(M,M), for M=1..20 from the product of ratios. Implement the asymptotic expansion for lnC(M,M) using Bernoulli numbers and the known amplitude A. Save both exact and asymptotic values for comparison.
- Output file: `/app/outputs/diagonal_asymptotic.csv`
- Format: csv
- Contract: CSV with columns: M (int), lnC_exact (float), lnC_asymp (float). M from 1 to 20.
- Scoring: scored by hidden verifier

### Step 3: Compute next-to-diagonal asymptotic expansion ln C(M,M+1)
- Role: scored
- Action: Compute the exact lnC(M,M+1) using the symmetric case hypergeometric expression. Implement the asymptotic expansion for lnC(M,M+1) expressed in terms of Bernoulli/Euler numbers. Output both exact and asymptotic values for M=1..20.
- Output file: `/app/outputs/nextdiagonal_asymptotic.csv`
- Format: csv
- Contract: CSV with columns: M (int), lnC_exact (float), lnC_asymp (float). M from 1 to 20.
- Scoring: scored by hidden verifier

### Step 4: Compute anisotropic correction coefficients A1, A2, A3
- Role: scored (load-bearing)
- Action: For the general anisotropic case, compute the angle-dependent correction coefficients A1(theta), A2(theta), A3(theta) using the explicit analytical expressions (which involve the anisotropy parameter u = cos(2alpha) and trigonometric functions). Evaluate these coefficients on a grid of alpha and theta values (both from 0 to pi/2, with step at least pi/16) and output the results as a JSON array.
- Output file: `/app/outputs/anisotropic_coefficients.json`
- Format: json
- Contract: JSON array of objects with keys: alpha (float, in [0,pi/2]), theta (float, in [0,pi/2]), A1 (float), A2 (float), A3 (float). Grid step: at least pi/16 for both alpha and theta.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exact_symmetric.csv`
- `/app/outputs/diagonal_asymptotic.csv`
- `/app/outputs/nextdiagonal_asymptotic.csv`
- `/app/outputs/anisotropic_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exact_symmetric.csv
- path: `/app/outputs/exact_symmetric.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Exact spin correlation values C(M,N) for small distances.
- schema:
  - `type`: table
  - `required_columns`: `M`, `N`, `C`
  - `columns`:
    - `M`: int
    - `N`: int
    - `C`: float
  - `description`: Rows for 0 <= M <= N <= 5, symmetric case (sinh(2Hc)=1).

### diagonal_asymptotic.csv
- path: `/app/outputs/diagonal_asymptotic.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Exact and asymptotic lnC(M,M) for diagonal correlation.
- schema:
  - `type`: table
  - `required_columns`: `M`, `lnC_exact`, `lnC_asymp`
  - `columns`:
    - `M`: int
    - `lnC_exact`: float
    - `lnC_asymp`: float
  - `description`: M from 1 to 20.

### nextdiagonal_asymptotic.csv
- path: `/app/outputs/nextdiagonal_asymptotic.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Exact and asymptotic lnC(M,M+1) for next-to-diagonal correlation.
- schema:
  - `type`: table
  - `required_columns`: `M`, `lnC_exact`, `lnC_asymp`
  - `columns`:
    - `M`: int
    - `lnC_exact`: float
    - `lnC_asymp`: float
  - `description`: M from 1 to 20.

### anisotropic_coefficients.json
- path: `/app/outputs/anisotropic_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Anisotropic correction coefficients.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `alpha`, `theta`, `A1`, `A2`, `A3`
    - `properties`:
      - `alpha`: float
      - `theta`: float
      - `A1`: float
      - `A2`: float
      - `A3`: float
  - `description`: Grid of alpha and theta values from 0 to pi/2, step at least pi/16.

Notes: All formulas are deterministic and the checker recomputes the same expressions. Tolerances are set to accommodate floating-point differences across implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exact_symmetric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "M",
          "N",
          "C"
        ],
        "columns": {
          "M": "int",
          "N": "int",
          "C": "float"
        },
        "description": "Rows for 0 <= M <= N <= 5, symmetric case (sinh(2Hc)=1)."
      },
      "description": "Exact spin correlation values C(M,N) for small distances."
    },
    {
      "file": "diagonal_asymptotic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "M",
          "lnC_exact",
          "lnC_asymp"
        ],
        "columns": {
          "M": "int",
          "lnC_exact": "float",
          "lnC_asymp": "float"
        },
        "description": "M from 1 to 20."
      },
      "description": "Exact and asymptotic lnC(M,M) for diagonal correlation."
    },
    {
      "file": "nextdiagonal_asymptotic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "M",
          "lnC_exact",
          "lnC_asymp"
        ],
        "columns": {
          "M": "int",
          "lnC_exact": "float",
          "lnC_asymp": "float"
        },
        "description": "M from 1 to 20."
      },
      "description": "Exact and asymptotic lnC(M,M+1) for next-to-diagonal correlation."
    },
    {
      "file": "anisotropic_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "alpha",
            "theta",
            "A1",
            "A2",
            "A3"
          ],
          "properties": {
            "alpha": "float",
            "theta": "float",
            "A1": "float",
            "A2": "float",
            "A3": "float"
          }
        },
        "description": "Grid of alpha and theta values from 0 to pi/2, step at least pi/16."
      },
      "description": "Anisotropic correction coefficients."
    }
  ],
  "notes": "All formulas are deterministic and the checker recomputes the same expressions. Tolerances are set to accommodate floating-point differences across implementations."
}
```

## How you are scored
A hidden verifier independently recomputes each scored artifact using the same formulas and compares against your submitted files. Each stage (exact symmetric, diagonal asymptotic, next-diagonal asymptotic, anisotropic coefficients) contributes a weighted fraction to the total reward. The verifier reads your output files, recomputes the exact same quantities from the underlying expressions, and checks that the values agree within predetermined tolerances. Reporting a number without actually executing the computations is not sufficient; the verifier's recomputation ensures that the values are derived from the correct procedure. The final reward is a weighted sum of the per-stage scores, normalized to [0,1].
