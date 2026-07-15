# Multi-band electron-phonon coupling and transition temperature analysis in doped SrTiO₃

## Problem background
Superconductivity in n-doped SrTiO₃ is unusual because it appears at extremely low carrier densities where the Fermi energy is much smaller than the energies of longitudinal optical (LO) phonons. The pairing mechanism is therefore nonadiabatic: electrons interact with LO phonons via long‑range electric fields, and the static and optical dielectric constants of the doped material control the strength of the attraction. Lattice distortions lift the three‑fold degeneracy of the conduction‑band minimum at the Γ‑point, giving three distinct bands with different effective masses. As the doping concentration increases, these bands are filled successively. The superconducting transition temperature Tc exhibits a maximum in each band as a function of carrier concentration, leading to a multi‑dome phase diagram. The analytical model predicts the positions and relative heights of these maxima purely from the electron‑phonon coupling constants and the band parameters. The goal here is to compute the coupling constants and the scaled transition temperatures for all three bands, locate their maxima, and confirm that the maxima appear at successively higher dopant concentrations.

## Approach
We implement the three‑band analytical model for doped SrTiO₃. The physical parameters are fixed: effective masses m₁=1.8 mₑ, m₂=3.5 mₑ, m₃=6.0 mₑ (in units of the free‑electron mass); the optical Bohr radius ā_B = 0.58×10⁻⁶ cm; and the critical concentrations n_{c1}=1.2×10¹⁸ cm⁻³ and n_{c2}=2.5×10¹⁹ cm⁻³ that mark the filling of the second and third bands.

A dimensionless variable x = π p_F ā_B / ℏ is introduced, where p_F is a characteristic Fermi momentum. The carrier concentration n_s and the individual Fermi momenta of the occupied bands are related by multi‑band implicit equations. For each chosen x we solve for the occupied Fermi momenta and thus obtain n_s.

The electron‑phonon coupling constants λ_i are computed from the analytical expressions for Thomas‑Fermi screening:
- In the lowest band only (x < x_{c1}), λ₁ is obtained from single‑band screening.
- When the second band is occupied (x ≥ x_{c1}), λ₂ uses screening from both bands.
- When the third band is occupied (x ≥ x_{c2}), λ₃ includes screening from all three bands.
The functional forms involve the relative Fermi momenta and the optical Bohr radius.

From each λ_i we compute the scaled dimensionless transition temperature Q_i(x) = (x² / m_i) exp(−1/λ_i), where the m_i are the numerical effective‑mass values (1.8, 3.5, 6.0).

A dense grid of x values (at least 200 points per band) is constructed, covering from small x up to beyond the anticipated third‑band maximum. At each grid point we evaluate λ₁, λ₂, λ₃ and Q₁, Q₂, Q₃, and record them together with x and n_s.

After obtaining the full scan, we locate for each band the x where Q_i attains its maximum and report the corresponding n_s and Q_max.

## Reproduction target
Produce two scored outputs:

1. **lambda_and_Tc.csv**: A table containing, for each grid point, the dimensionless parameter x, the carrier concentration n_s (cm⁻³), the three coupling constants λ₁, λ₂, λ₃ (dimensionless), and the three scaled transition temperatures Q₁, Q₂, Q₃ (dimensionless). The grid must contain at least 200 distinct x‑values for each band.

2. **maxima.csv**: For each band (1,2,3), the x value where Q_i is maximal, the corresponding carrier concentration n_s_max, and the maximal Q_max value. The reported doping concentrations of the maxima must satisfy n_s_max1 < n_s_max2 < n_s_max3.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute coupling constants and scaled transition temperatures
- Role: scored (load-bearing)
- Action: Implement the three-band model using the given effective masses (m₁=1.8mₑ, m₂=3.5mₑ, m₃=6mₑ), the optical Bohr radius ā_B = 0.58×10⁻⁶ cm, and the critical concentrations n_{c1}=1.2×10¹⁸ cm⁻³ and n_{c2}=2.5×10¹⁹ cm⁻³. For a dense grid of dimensionless parameter x = π p_F ā_B / ℏ (≥200 points per band), compute the carrier concentration n_s and the Fermi momenta of the occupied bands, using the multi-band relations. Evaluate the electron-phonon coupling constants λ₁, λ₂, λ₃ from the analytical expressions (single-band screening for band 1; multi-band Thomas–Fermi screening for bands 2 and 3). Calculate the scaled transition temperature Q_i = (x²/m_i) exp(−1/λ_i) for each band. Write a CSV file with columns: x, n_s, lambda1, lambda2, lambda3, Q1, Q2, Q3.
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
