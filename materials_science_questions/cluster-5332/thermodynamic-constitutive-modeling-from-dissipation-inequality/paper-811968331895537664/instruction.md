# Reinforced Concrete Shell Yield Curves

## Problem background
In limit analysis of reinforced concrete shells, the yield condition is expressed in terms of generalized stresses: the reduced normal force \(n\) and the reduced bending moment \(m\). This task computes the yield curves for singly reinforced and symmetrically doubly reinforced shells using the dissipation function approach. The resulting piecewise analytic curve defines the permissible \((n,m)\) combinations. For given reinforcement parameters \(\gamma=0.2\) and \(\rho=0.3\), you will generate dense point clouds of the yield curve and output them as CSV files.

## Approach
The yield curve is derived from the dissipation per unit length of a yield line. The concrete is assumed to have zero tensile strength and a compressive yield strength \(\sigma_c'\). The reinforcement is rigid-perfectly plastic. Introducing reduced variables \(n = N/(\sigma_c' t)\), \(m = M/(\sigma_c' t^2/4)\), reduced reinforcement ratio \(\gamma = \frac{\sigma_y \Omega_s}{\sigma_c' t}\), and the neutral-axis ordinate \(\eta\) (dimensionless, between -1 and 1), the normality law of plasticity applied to the dissipation function yields piecewise parametric expressions for \(n\) and \(m\) in terms of \(\eta\).

For a **singly reinforced shell** (reinforcement at \(z = \rho \frac{t}{2}\)):
- Regime where reinforcement is fully in tension (\(-1 \le \eta < \rho\)):
  \(n = \gamma - \frac{1+\eta}{2}\),
  \(m = 2\gamma\rho + \frac{1-\eta^2}{2}\).
- Regime where reinforcement is fully in compression (\(\rho < \eta \le 1\)):
  \(n = -\gamma - \frac{1+\eta}{2}\),
  \(m = -2\gamma\rho + \frac{1-\eta^2}{2}\).
- At the subdifferential \(\eta = \rho\), the stress point lies on a straight segment connecting the endpoints of the two regimes.

For a **symmetric doubly reinforced shell** (reinforcement at \(z = \pm \rho \frac{t}{2}\) with the same \(\gamma\)):
- Regime \(\eta < -\rho\):
  \(n = -\frac{1+\eta}{2} - 2\gamma\),
  \(m = \frac{1-\eta^2}{2}\).
- Regime \(-\rho < \eta < \rho\):
  \(n = -\frac{1+\eta}{2}\),
  \(m = \frac{1-\eta^2}{2} + 4\gamma\rho\).
- Regime \(\eta > \rho\):
  \(n = -\frac{1+\eta}{2} - 2\gamma\),
  \(m = \frac{1-\eta^2}{2}\).
- Straight segments connect the adjacent regimes at \(\eta = \pm \rho\).

You will sample \(\eta\) in \([-1, 1]\) and for each point compute the corresponding \((n,m)\) according to the regime rules above. The resulting \((\eta, n, m)\) triplets form the yield curve.

## Reproduction target
For the fixed reinforcement parameters \(\gamma = 0.2\) and \(\rho = 0.3\), compute and output the following:
1. `/app/outputs/single_reinforced_yield_curve.csv` — a CSV file containing \((\eta, n, m)\) points for the singly reinforced yield curve.
2. `/app/outputs/double_reinforced_yield_curve.csv` — a CSV file containing \((\eta, n, m)\) points for the doubly reinforced yield curve.

Use a dense grid of \(\eta\) covering the full range \([-1, 1]\) to faithfully capture the piecewise shape, including the straight subdifferential segments. The required output schema and units are detailed in the Output contract section.

## Assets

- Python programming environment with scientific computing libraries: Python 3 with numpy, scipy, or sympy as preferred

## Workflow steps

### Step 1: Compute singly reinforced yield curve
- Role: scored
- Action: For reinforcement parameters gamma=0.2 and rho=0.3, implement the piecewise parametric equations for n(eta) and m(eta) derived from the dissipation function and normality law, covering the plastic regimes (reinforcement fully in tension, fully in compression, and the subdifferential at eta=rho). Use a dense grid of eta values in the range [-1, 1] and output the resulting (eta, n, m) triplets as a CSV file.
- Output file: `/app/outputs/single_reinforced_yield_curve.csv`
- Format: csv
- Contract: CSV with columns: eta, n, m. eta is the nondimensional neutral-axis ordinate; n = N/(sigma_c' t); m = M/(sigma_c' t^2/4).
- Scoring: scored by hidden verifier

### Step 2: Compute doubly reinforced yield curve (symmetric)
- Role: scored
- Action: For the same reinforcement parameters gamma=0.2 and rho=0.3, implement the parametric equations for the symmetrically doubly reinforced case, derived from the corresponding dissipation function. Handle the appropriate plastic regimes and the straight segments at eta=±rho. Sample eta in [-1, 1] and output (eta, n, m) points.
- Output file: `/app/outputs/double_reinforced_yield_curve.csv`
- Format: csv
- Contract: CSV with columns: eta, n, m. eta is the nondimensional neutral-axis ordinate; n = N/(sigma_c' t); m = M/(sigma_c' t^2/4).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/single_reinforced_yield_curve.csv`
- `/app/outputs/double_reinforced_yield_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### single_reinforced_yield_curve.csv
- path: `/app/outputs/single_reinforced_yield_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reduced yield curve points for a singly reinforced shell with gamma=0.2, rho=0.3. Each row is an (eta, n, m) triplet covering the full plastic regime.
- schema:
  - `type`: table
  - `required_columns`: `eta`, `n`, `m`
  - `items`: object
  - `units`:
    - `eta`: dimensionless
    - `n`: dimensionless (N/(sigma_c' t))
    - `m`: dimensionless (M/(sigma_c' t^2/4))

### double_reinforced_yield_curve.csv
- path: `/app/outputs/double_reinforced_yield_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reduced yield curve points for a doubly reinforced symmetric shell with gamma=0.2, rho=0.3. Each row is an (eta, n, m) triplet.
- schema:
  - `type`: table
  - `required_columns`: `eta`, `n`, `m`
  - `items`: object
  - `units`:
    - `eta`: dimensionless
    - `n`: dimensionless (N/(sigma_c' t))
    - `m`: dimensionless (M/(sigma_c' t^2/4))

Notes: Both yield curves are computed analytically from the dissipation function and normality law. The checker recomputes the reference points from the same parametric equations and compares pointwise with an absolute tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "single_reinforced_yield_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "n",
          "m"
        ],
        "items": {},
        "units": {
          "eta": "dimensionless",
          "n": "dimensionless (N/(sigma_c' t))",
          "m": "dimensionless (M/(sigma_c' t^2/4))"
        }
      },
      "description": "Reduced yield curve points for a singly reinforced shell with gamma=0.2, rho=0.3. Each row is an (eta, n, m) triplet covering the full plastic regime."
    },
    {
      "file": "double_reinforced_yield_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "n",
          "m"
        ],
        "items": {},
        "units": {
          "eta": "dimensionless",
          "n": "dimensionless (N/(sigma_c' t))",
          "m": "dimensionless (M/(sigma_c' t^2/4))"
        }
      },
      "description": "Reduced yield curve points for a doubly reinforced symmetric shell with gamma=0.2, rho=0.3. Each row is an (eta, n, m) triplet."
    }
  ],
  "notes": "Both yield curves are computed analytically from the dissipation function and normality law. The checker recomputes the reference points from the same parametric equations and compares pointwise with an absolute tolerance."
}
```

## How you are scored
A hidden verifier independently recomputes the expected \((n,m)\) values for each \(\eta\) point from the same parametric equations and compares your submitted points (absolute tolerance will be applied). For each output file, if every point is within the hidden tolerance, you receive full credit for that file; otherwise, that file receives zero. The final reward is the average of the scores from the two scored artifacts (each weighted equally). Reporting the paper’s numbers is not sufficient; the verifier checks your raw computed CSV values directly.
