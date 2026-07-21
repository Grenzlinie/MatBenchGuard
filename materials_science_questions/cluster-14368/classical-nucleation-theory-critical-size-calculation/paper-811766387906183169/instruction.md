# Cloud Droplet Activation with Analytical Surfactant Partitioning Model

## Problem background
Surfactants dissolved in cloud droplets tend to partition to the droplet surface, reducing the surface tension. For micron-sized droplets, this partitioning can strongly deplete the surfactant in the bulk interior, which in turn alters the droplet's activation behaviour (the point at which it spontaneously grows into a cloud droplet). Solving the surfactant partitioning equilibrium numerically is computationally expensive, making it impractical for large-scale cloud models. This benchmark explores simplified analytical equations that capture the partitioning effect, aiming to dramatically reduce computation time while preserving accuracy.

## Approach
You will implement two models for cloud droplet activation: (1) an **iterative numerical model** that solves the full Gibbs adsorption isotherm using root-finding, and (2) an **analytical model** based on a derived cubic equation for surfactant bulk concentration under a Szyskowski-type surface tension parameterisation. Both models use Köhler theory, with a constant dry particle size of 40 nm, temperature 298.15 K, and the surface tension parameters reported for SDS‑NaCl solutions. For a range of surfactant mass fractions from 0 to 1, you will locate the maximum of the Köhler curve (the critical supersaturation) and record the corresponding critical droplet diameter and the bulk surfactant concentration. The analytical model's predictions will be compared against the iterative reference to quantify the maximum absolute difference in critical supersaturation.

## Physical constants and particle properties
| Quantity | Symbol | Value | Unit |
|----------|--------|-------|------|
| Temperature | \(T\) | 298.15 | K |
| Gas constant | \(R\) | 8.314462618 | J mol⁻¹ K⁻¹ |
| Molar volume of pure water | \(v_w\) | 18.015 × 10⁻⁶ | m³ mol⁻¹ |
| Pure water surface tension | \(\sigma_w\) | 0.072 | N m⁻¹ |
| SDS molar mass | \(M_s\) | 0.28838 | kg mol⁻¹ |
| SDS density | \(\rho_s\) | 1010 | kg m⁻³ |
| SDS molar volume | \(v_s = M_s/\rho_s\) | (evaluate) | m³ mol⁻¹ |
| NaCl molar mass | \(M_N\) | 0.05844 | kg mol⁻¹ |
| NaCl density | \(\rho_N\) | 2160 | kg m⁻³ |
| NaCl molar volume | \(v_N = M_N/\rho_N\) | (evaluate) | m³ mol⁻¹ |
| Dry particle diameter | \(D_{\mathrm{dry}}\) | 40 × 10⁻⁹ | m |
| Dry particle volume | \(V_{\mathrm{dry}} = \frac{\pi}{6} D_{\mathrm{dry}}^3\) | (evaluate) | m³ |

### Szyskowski surface tension parameters (SDS in NaCl solution)
- \(RT\,\Gamma^\infty = 13.90 \times 10^{-3}\) N m⁻¹ → \(\Gamma^\infty = 13.90\times10^{-3} / (R T)\) mol m⁻².
- \(\beta = \dfrac{9.273\times10^{-6}}{c_{\mathrm{NaCl}} + 9.733\times10^{-3}}\) M, where \(c_{\mathrm{NaCl}}\) is the bulk NaCl molarity.
- When no NaCl is present (\(n_N^T = 0\)), use \(c_{\mathrm{NaCl}} = 0\) in the denominator.
- An additional linear salt‑effect parameter applies to the surface tension:
  \[
  \text{slope\_salt} = 1.61 \times 10^{-3} \;\; \text{N m}^{-1}\,\text{M}^{-1}
  \]

The surface tension of the ternary solution is given by a modified Szyskowski equation that includes the explicit salt contribution:
\[
\sigma = \sigma_w - R T \Gamma^\infty \ln\!\Bigl(1 + \frac{c_s^{\mathrm{B}}}{\beta}\Bigr) - \text{slope\_salt} \cdot c_{\mathrm{NaCl}},
\]
where \(c_s^{\mathrm{B}}\) is the bulk surfactant concentration in molarity (M).
The salt term vanishes when no NaCl is present (\(c_{\mathrm{NaCl}} = 0\)).
**Important:** the derivative \(d\sigma / d\ln n_s^{\mathrm{B}}\) used in the adsorption equation remains unchanged by the constant salt term, so the cubic equation for \(n_s^{\mathrm{B}}\) derived below is still valid.

## Model description

### 1. Droplet composition from dry particle
For a given surfactant mass fraction \(f_s\) (\(0 \le f_s \le 1\)), the total number of moles of surfactant and NaCl in the dry particle are calculated using volume additivity:
- If \(f_s = 0\) (pure NaCl): \(n_s^{\mathrm{T}} = 0\), \(n_N^{\mathrm{T}} = V_{\mathrm{dry}} \, \rho_N / M_N\).
- If \(f_s = 1\) (pure SDS): \(n_s^{\mathrm{T}} = V_{\mathrm{dry}} \, \rho_s / M_s\), \(n_N^{\mathrm{T}} = 0\).
- Otherwise:
  1. Compute the inverse density of the mixture: \(\rho_{\mathrm{mix}}^{-1} = \dfrac{f_s}{\rho_s} + \dfrac{1-f_s}{\rho_N}\).
  2. Total dry mass: \(m_{\mathrm{tot}} = V_{\mathrm{dry}} / \rho_{\mathrm{mix}}^{-1}\).
  3. \(n_s^{\mathrm{T}} = f_s \, m_{\mathrm{tot}} / M_s\),  \(n_N^{\mathrm{T}} = (1-f_s) \, m_{\mathrm{tot}} / M_N\).

### 2. Köhler curve and supersaturation
For a given droplet diameter \(D_{\mathrm{aq}}\) (m), the aqueous-phase volume is
\[
V_{\mathrm{aq}} = \frac{\pi}{6} D_{\mathrm{aq}}^3, \qquad V_w = V_{\mathrm{aq}} - V_{\mathrm{dry}} \;\; (>0).
\]
The number of moles of water is \(n_w = V_w / v_w\).

Both solutes are assumed to dissociate completely: SDS → Na⁺ + DS⁻, NaCl → Na⁺ + Cl⁻. The water mole fraction \(x_w\) is therefore
\[
x_w = \frac{n_w}{n_w + 2\,n_s^{\mathrm{B}} + 2\,n_N^{\mathrm{T}}},
\]
where \(n_s^{\mathrm{B}}\) is the number of bulk surfactant moles (the unknown). We use the ideal solution approximation (\(a_w = x_w\)).

The equilibrium saturation ratio \(S\) is given by the Köhler equation (Eq. 1):
\[
S = x_w \, \exp\!\Bigl( \frac{4 v_w \sigma}{R T D_{\mathrm{aq}}} \Bigr).
\]
The supersaturation (in percent) is \(SS = (S - 1) \times 100\%\).

### 3. Iterative numerical model (reference)
The bulk surfactant moles \(n_s^{\mathrm{B}}\) must satisfy the Gibbs adsorption isotherm. For the common-ion system (SDS + NaCl) with ideal behaviour the equation (derived from Eq. 6 in the paper) becomes:

\[
(n_s^{\mathrm{T}} - n_s^{\mathrm{B}})\,
\Bigl( 2 + \frac{n_s^{\mathrm{B}}}{n_s^{\mathrm{B}} + n_N^{\mathrm{T}}} \Bigr)
\;=\;
\frac{A \, \Gamma^\infty \, n_s^{\mathrm{B}}}{\beta c_0 + n_s^{\mathrm{B}}},
\]

where
- \(A = \pi D_{\mathrm{aq}}^2\) is the droplet surface area (m²),
- \(c_0 = V_{\mathrm{aq}} \times 1000\) converts molarity to moles (L → m³),
- \(\beta c_0\) therefore has units of moles.

For each droplet diameter \(D_{\mathrm{aq}}\), solve this equation for \(n_s^{\mathrm{B}}\) using a root‑finding algorithm (e.g., bisection) in the interval \((0,\, n_s^{\mathrm{T}}]\). From the solution compute:
- \(c_s^{\mathrm{B}} = n_s^{\mathrm{B}} / c_0\) (M),
- \(\sigma\) from the modified Szyskowski equation (including the `slope_salt` term),
- \(SS\) from the Köhler equation.

Vary \(D_{\mathrm{aq}}\) (suggested range 10 nm – 1 µm) and locate the maximum of \(SS\); the corresponding values are the critical supersaturation, critical diameter, and critical bulk surfactant concentration.

Write the results for at least 15 mass fractions covering 0 – 1 to `/app/outputs/iterative_reference.csv`.

### 4. Analytical partitioning model (cubic equation)
The same equation can be rearranged into a cubic polynomial for \(n_s^{\mathrm{B}}\) (see paper Eq. 15). With \(k_1 = k_2 = n_N^{\mathrm{T}}\) and \(\hat\beta = \beta c_0\) the coefficients are:

\[
\begin{aligned}
a_3 &= -2, \\
a_2 &= 2\,n_s^{\mathrm{T}} - n_N^{\mathrm{T}} - 2\,\hat\beta - A\,\Gamma^\infty, \\
a_1 &= n_s^{\mathrm{T}} n_N^{\mathrm{T}} + (2\,n_s^{\mathrm{T}} - n_N^{\mathrm{T}})\,\hat\beta - n_N^{\mathrm{T}}\,A\,\Gamma^\infty, \\
a_0 &= -\,n_s^{\mathrm{T}} n_N^{\mathrm{T}} \hat\beta .
\end{aligned}
\]

For each droplet diameter, solve \(a_3 x^3 + a_2 x^2 + a_1 x + a_0 = 0\) for \(x = n_s^{\mathrm{B}}\) and select the real root in \((0,\, n_s^{\mathrm{T}}]\). Use the root to compute \(c_s^{\mathrm{B}}\), \(\sigma\) (using the **same** modified Szyskowski equation with `slope_salt`), \(SS\) and then find the critical point exactly as for the iterative model.

Output: `/app/outputs/critical_properties.csv` containing the critical properties of the analytical model for the same mass fraction grid.

### 5. Error analysis
Compute the absolute difference in critical supersaturation between the iterative reference and the analytical model for each mass fraction. Report the **maximum** absolute difference in `/app/outputs/error_analysis.json` as a JSON object with the key `max_abs_diff_supersat_percent` (float).

## Reproduction target
Produce a CSV file (`critical_properties.csv`) containing for at least 15 surfactant mass fractions (covering 0 to 1) the critical supersaturation (%), critical droplet diameter (m), and surfactant bulk concentration (M) as computed by the analytical model. Also produce a JSON file (`error_analysis.json`) with the key `max_abs_diff_supersat_percent` holding the maximum absolute deviation.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute critical properties with iterative numerical model
- Role: process
- Action: Implement the iterative numerical model as described above. For at least 15 surfactant mass fractions covering 0 – 1, find the critical point of the Köhler curve. Write the results as a CSV file.
- Evidence: `/app/outputs/iterative_reference.csv`

### Step 2: Compute critical properties with analytical partitioning model
- Role: scored
- Action: Implement the analytical cubic model. For the same mass fraction points, compute the critical supersaturation (%), critical droplet diameter (m), and surfactant bulk concentration (M). Write the results to a CSV file.
- Output file: `/app/outputs/critical_properties.csv`
- Format: csv
- Contract: CSV with columns: mass_fraction_surfactant, critical_supersaturation, critical_diameter, surfactant_bulk_concentration
- Scoring: scored by hidden verifier

### Step 3: Compare analytical and iterative predictions
- Role: scored (load-bearing)
- Action: Load the iterative reference and analytical model outputs, align by mass fraction, and compute the absolute difference in critical supersaturation (in %). Record the maximum absolute difference as a JSON object.
- Output file: `/app/outputs/error_analysis.json`
- Format: json
- Contract: JSON object with key 'max_abs_diff_supersat_percent' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/iterative_reference.csv`
- `/app/outputs/critical_properties.csv`
- `/app/outputs/error_analysis.json`

## Output contract

### critical_properties.csv
- path: `/app/outputs/critical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Analytical model predictions of critical droplet properties for 40 nm SDS‑NaCl particles as a function of surfactant mass fraction.
- schema:
  - `type`: table
  - `required_columns`: `mass_fraction_surfactant`, `critical_supersaturation`, `critical_diameter`, `surfactant_bulk_concentration`
  - `units`:
    - `mass_fraction_surfactant`: dimensionless (0–1)
    - `critical_supersaturation`: percent (%)
    - `critical_diameter`: meters (m)
    - `surfactant_bulk_concentration`: molarity (M)

### error_analysis.json
- path: `/app/outputs/error_analysis.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum absolute difference in critical supersaturation between analytical and iterative models.
- schema:
  - `type`: object
  - `required`:
    - `max_abs_diff_supersat_percent`: float
  - `units`: object

### iterative_reference.csv
- path: `/app/outputs/iterative_reference.csv`
- format: csv
- purpose: internal (not scored, used as reference)
- description: Iterative numerical model predictions, used for error analysis.
- schema:
  - `type`: table
  - `required_columns`: `mass_fraction_surfactant`, `critical_supersaturation`, `critical_diameter`, `surfactant_bulk_concentration`
  - `units`: same as `critical_properties.csv`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "iterative_reference.csv",
      "format": "csv",
      "purpose": "internal",
      "schema": {
        "type": "table",
        "required_columns": [
          "mass_fraction_surfactant",
          "critical_supersaturation",
          "critical_diameter",
          "surfactant_bulk_concentration"
        ],
        "units": {
          "mass_fraction_surfactant": "dimensionless (0-1)",
          "critical_supersaturation": "percent (%)",
          "critical_diameter": "meters (m)",
          "surfactant_bulk_concentration": "molarity (M)"
        }
      }
    },
    {
      "file": "critical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mass_fraction_surfactant",
          "critical_supersaturation",
          "critical_diameter",
          "surfactant_bulk_concentration"
        ],
        "units": {
          "mass_fraction_surfactant": "dimensionless (0-1)",
          "critical_supersaturation": "percent (%)",
          "critical_diameter": "meters (m)",
          "surfactant_bulk_concentration": "molarity (M)"
        }
      },
      "description": "Analytical model predictions of critical droplet properties for 40 nm SDS-NaCl particles as a function of surfactant mass fraction."
    },
    {
      "file": "error_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "max_abs_diff_supersat_percent": "float"
        },
        "units": {}
      },
      "description": "Maximum absolute difference in critical supersaturation between analytical and iterative models."
    }
  ],
  "notes": "The iterative reference CSV is an internal intermediate, not scored. The analytical model output is the primary reproduction target."
}
```

## How you are scored
The hidden verifier will inspect your submitted artifacts. For `critical_properties.csv` it performs a structural audit (required columns, positive supersaturation, decreasing trend with surfactant mass fraction) and verifies consistency with the iterative reference model through the recomputed error metric. For `error_analysis.json` the verifier recomputes the maximum absolute difference between your analytical and iterative critical supersaturations and checks that it is within a very small tolerance (reflecting the paper's claim of negligible numerical error). These checks are weighted to produce the final reward.