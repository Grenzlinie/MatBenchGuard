# Multi-band electron-phonon coupling and transition temperature analysis in doped SrTiO₃

## Problem background
Superconductivity in n-doped SrTiO₃ can be described by a model where electrons interact with longitudinal optical (LO) phonons in the nonadiabatic regime (phonon frequencies much larger than the Fermi energy). The conduction‑band minimum at the Γ‑point is three‑fold degenerate, but symmetry breaking lifts the degeneracy, giving three bands with effective masses m₁=1.8 mₑ, m₂=3.5 mₑ, m₃=6.0 mₑ. As the doping concentration increases, these bands fill successively, and the superconducting transition temperature exhibits a maximum in each band, creating a multi‑dome phase diagram. The model predicts the positions and relative heights of these maxima from the electron‑phonon coupling constants and band parameters.

## Approach
We implement the three‑band analytical model for doped SrTiO₃. The physical parameters are fixed: effective masses m₁=1.8 mₑ, m₂=3.5 mₑ, m₃=6.0 mₑ (in units of the free‑electron mass); the optical Bohr radius ā_B = 0.58×10⁻⁶ cm; and the critical concentrations n_{c1}=1.2×10¹⁸ cm⁻³ and n_{c2}=2.5×10¹⁹ cm⁻³ that mark the filling of the second and third bands.

A dimensionless variable x = π p_F ā_B / ℏ is introduced, where p_F is a characteristic Fermi momentum. The critical values of x corresponding to the band‑filling thresholds are
x_{c1} = 6.1   and   x_{c2} = 20.0 .

Two important mass ratios are defined:
α = m₂ / m₁ = 3.5 / 1.8 ≈ 1.9444444444444444
γ = m₃ / m₁ = 6.0 / 1.8 ≈ 3.3333333333333335

The electron‑phonon coupling constants λ_i are computed from the following analytical expressions derived from Thomas‑Fermi screening in the multi‑band system.

**Band 1 (single-band screening):**
For all x > 0,
λ₁(x) = (1 / x) * ln(1 + x) .

**Band 2 (screened by bands 1 and 2, active only when x > x_{c1}):**
If x ≤ x_{c1}, set λ₂(x) = 0.
If x > x_{c1}, compute
x₂ = √(α) * √(max(0, x² − x_{c1}²)) .
If x₂ > 0,
λ₂(x) = (α / x₂) * ln( 1 + x₂² / (x + α x₂) ),
otherwise λ₂(x) = 0.

**Band 3 (screened by all three bands, active only when x > x_{c2}):**
If x ≤ x_{c2}, set λ₃(x) = 0.
If x > x_{c2}, compute
x₂ = √(α) * √(max(0, x² − x_{c1}²))   (needed also for the denominator),
x₃ = √(γ) * √(max(0, x² − x_{c2}²)) .
If x₃ > 0,
λ₃(x) = (γ / x₃) * ln( 1 + x₃² / (x + α x₂ + γ x₃) ),
otherwise λ₃(x) = 0.

**Scaled transition temperatures:**
For each band i = 1, 2, 3,
Q_i(x) = (x² / m_i) * exp(−1 / λ_i)   if λ_i > 0,
otherwise Q_i(x) = 0.0.

The actual numerical values of the effective masses used in Q_i are m₁ = 1.8, m₂ = 3.5, m₃ = 6.0.

**Carrier concentration n_s:**
The physical carrier concentration n_s (in cm⁻³) is related to the dimensionless x by a monotonic, piecewise‑continuous function that ensures the correct filling thresholds. Use the following explicit relations (derived from the multi‑band Fermi‑momentum sum):

A = x_{c1} / (n_{c1} / 10^{18})^{1/3}   = 5.74
B ≈ 195.0   (numerical constant chosen so that n_s is continuous at x = x_{c2}; B itself is just a scale factor, and 195.0 reproduces the correct n_{c2}).

- If x ≤ x_{c1}:
  n_s(x) = (x / A)^3 × 10^{18}   cm⁻³ .
- If x_{c1} < x ≤ x_{c2}:
  n_s(x) = [ x^3 + α^{3/2} * (x² − x_{c1}²)^{3/2} ] / B × 10^{18}   cm⁻³ .
- If x > x_{c2}:
  n_s(x) = [ x^3 + α^{3/2} * (x² − x_{c1}²)^{3/2} + γ^{3/2} * (x² − x_{c2}²)^{3/2} ] / B × 10^{18}   cm⁻³ .

The formula guarantees that n_s increases monotonically with x and the values at the thresholds match the critical concentrations.

**Grid construction:**
Construct a dense grid of x values covering the region 0.5 ≤ x ≤ 35.0. The total number of grid points must be at least 1000 (which automatically satisfies the requirement of ≥200 points per band). At each grid point compute λ₁, λ₂, λ₃ and Q₁, Q₂, Q₃ as described above, together with n_s(x).

**Maxima extraction:**
After obtaining the full scan, locate for each band i = 1, 2, 3 the x value for which Q_i attains its maximum (using argmax or parabolic interpolation). Record the band index, x_max, the corresponding n_s_max, and the maximal Q_max.

## Reproduction target
Produce two scored outputs:

1. **lambda_and_Tc.csv**: A table containing, for each grid point, the dimensionless parameter x, the carrier concentration n_s (cm⁻³), the three coupling constants λ₁, λ₂, λ₃ (dimensionless), and the three scaled transition temperatures Q₁, Q₂, Q₃ (dimensionless). The grid must contain at least 200 distinct x‑values for each band (band 1: x ≤ x_{c1}; band 2: x_{c1} < x ≤ x_{c2}; band 3: x > x_{c2}).

2. **maxima.csv**: For each band (1,2,3), the x value where Q_i is maximal, the corresponding carrier concentration n_s_max, and the maximal Q_max value. The reported doping concentrations of the maxima must satisfy n_s_max1 < n_s_max2 < n_s_max3.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute coupling constants and scaled transition temperatures
- Role: scored (load-bearing)
- Action: Implement the three-band model using the given effective masses (m₁=1.8, m₂=3.5, m₃=6.0), the optical Bohr radius ā_B = 0.58×10⁻⁶ cm, the critical concentrations n_{c1}=1.2×10¹⁸ cm⁻³, n_{c2}=2.5×10¹⁹ cm⁻³, the corresponding x thresholds (x_{c1}=6.1, x_{c2}=20.0), and the mass ratios α=m₂/m₁, γ=m₃/m₁. For a dense grid of the dimensionless parameter x (≥1000 total points, spanning at least 0.5 ≤ x ≤ 35.0), compute x₂ and x₃ as needed, then λ₁, λ₂, λ₃ and Q₁, Q₂, Q₃ using the explicit formulas above. Compute n_s(x) from the piecewise formula involving A=5.74 and B≈195.0. Write a CSV file with columns: x, n_s, lambda1, lambda2, lambda3, Q1, Q2, Q3.
- Output file: `/app/outputs/lambda_and_Tc.csv`
- Format: csv
- Contract: CSV with header: x (float, dimensionless), n_s (float, cm⁻³), lambda1, lambda2, lambda3 (float, dimensionless), Q1, Q2, Q3 (float, dimensionless). One row per grid point.
- Scoring: scored by hidden verifier

### Step 2: Locate Q_i maxima
- Role: scored
- Action: From the lambda_and_Tc.csv, for each band i = 1,2,3 locate the x value at which Q_i attains its maximum (by argmax or parabolic interpolation). Record the band index, x_max, the corresponding carrier concentration n_s_max, and the maximal Q_max. Write a CSV file with columns: band, x_max, n_s_max, Q_max.
- Output file: `/app/outputs/maxima.csv`
- Format: csv
- Contract: CSV with header: band (int, 1 or 2 or 3), x_max (float, dimensionless), n_s_max (float, cm⁻³), Q_max (float, dimensionless). One row per band.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lambda_and_Tc.csv`
- `/app/outputs/maxima.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lambda_and_Tc.csv
- path: `/app/outputs/lambda_and_Tc.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Full scan of the three-band model giving x, carrier concentration, coupling constants and the scaled transition temperatures Q₁, Q₂, Q₃ for each grid point. The checker will recompute Qᵢ at several hidden test x‑points using the same analytical model and compare with the agent’s reported values; it will also verify grid density requirements.
- schema:
  - `type`: table
  - `required_columns`: `x`, `n_s`, `lambda1`, `lambda2`, `lambda3`, `Q1`, `Q2`, `Q3`
  - `units`:
    - `x`: dimensionless
    - `n_s`: cm^-3
    - `lambda1`: dimensionless
    - `lambda2`: dimensionless
    - `lambda3`: dimensionless
    - `Q1`: dimensionless
    - `Q2`: dimensionless
    - `Q3`: dimensionless
  - `items`: object

### maxima.csv
- path: `/app/outputs/maxima.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Summary of the maxima of Qᵢ(x) for the three bands. The checker will compare the reported x_max, n_s_max and Q_max against hidden reference values (the model’s analytical predictions), and verify that the doping concentrations of the maxima increase monotonically (n_s_max1 < n_s_max2 < n_s_max3).
- schema:
  - `type`: table
  - `required_columns`: `band`, `x_max`, `n_s_max`, `Q_max`
  - `units`:
    - `band`: integer
    - `x_max`: dimensionless
    - `n_s_max`: cm^-3
    - `Q_max`: dimensionless
  - `items`: object

Notes: All physical parameters are fixed and provided in the problem description. The agent must implement the model from scratch; no pre‑computed data or external files are needed. The checker performs a metric‑recompute: it evaluates Qᵢ at hidden x‑points and checks the extracted maxima positions and the monotonic ordering of doping concentrations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lambda_and_Tc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "n_s",
          "lambda1",
          "lambda2",
          "lambda3",
          "Q1",
          "Q2",
          "Q3"
        ],
        "units": {
          "x": "dimensionless",
          "n_s": "cm^-3",
          "lambda1": "dimensionless",
          "lambda2": "dimensionless",
          "lambda3": "dimensionless",
          "Q1": "dimensionless",
          "Q2": "dimensionless",
          "Q3": "dimensionless"
        },
        "items": {}
      },
      "description": "Full scan of the three-band model giving x, carrier concentration, coupling constants and the scaled transition temperatures Q₁, Q₂, Q₃ for each grid point. The checker will recompute Qᵢ at several hidden test x‑points using the same analytical model and compare with the agent’s reported values; it will also verify grid density requirements."
    },
    {
      "file": "maxima.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "band",
          "x_max",
          "n_s_max",
          "Q_max"
        ],
        "units": {
          "band": "integer",
          "x_max": "dimensionless",
          "n_s_max": "cm^-3",
          "Q_max": "dimensionless"
        },
        "items": {}
      },
      "description": "Summary of the maxima of Qᵢ(x) for the three bands. The checker will compare the reported x_max, n_s_max and Q_max against hidden reference values (the model’s analytical predictions), and verify that the doping concentrations of the maxima increase monotonically (n_s_max1 < n_s_max2 < n_s_max3)."
    }
  ],
  "notes": "All physical parameters are fixed and provided in the problem description. The agent must implement the model from scratch; no pre‑computed data or external files are needed. The checker performs a metric‑recompute: it evaluates Qᵢ at hidden x‑points and checks the extracted maxima positions and the monotonic ordering of doping concentrations."
}
```

## How you are scored
A hidden verifier independently scores each of the two output files. For lambda_and_Tc.csv, it recomputes Q_i at several hidden x‑points using the same analytical model and compares with your reported values within a small relative tolerance; it also verifies that the grid density meets the minimum requirement per band. For maxima.csv, it extracts the maximum of Q_i for each band from your grid (argmax or parabolic fit) and compares x_max and Q_max against hidden reference values derived from the model’s analytical predictions; it further checks that n_s_max1 < n_s_max2 < n_s_max3. Merely writing down expected numbers is not sufficient – the verifier reads your raw files and recomputes the quantities. The final reward is a weighted combination of these checks.