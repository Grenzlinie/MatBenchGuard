# Disorder model thermodynamic calculations for liquid helium II

## Problem background
Liquid helium II exhibits negative thermal expansion and exceptionally high thermal conductivity. A theoretical model attributes these properties to an order–disorder transformation in a diamond-type atomic lattice: the thermal energy is dominated by configurational energy of disorder rather than by lattice vibrations. To assess this model, one can examine experimental thermodynamic data for He II at a fixed density and compute several key quantities: the disorder Grüneisen parameter (β) obtained from thermal expansion and specific heat, the same parameter derived from the shift of the λ-point critical temperature with density, a vibrational Grüneisen parameter (γ) from the compressibility, and the resulting fraction of vibrational specific heat (Cv^(l)/Cv). The present task asks you to carry out these computations using the provided data.

## Approach
The calculation is based on thermodynamic identities that separate the total entropy into a configurational (disorder) part and a vibrational part.

**Disorder β from thermal expansion.**  For a pure disordering process the entropy is assumed to depend only on T / V₀ (where V₀ is the ordering energy). This leads to the relation

β = − (v / Cv) (∂p/∂T)_ρ ,

where v is the specific volume, Cv is the specific heat at constant volume, and (∂p/∂T)_ρ is the temperature derivative of pressure at constant density. The experimental data for ρ = 0.1684 g/cm³ are:

| T (K) | −(∂p/∂T)_ρ (atm/deg) | Cv (cal/g/deg) |
|-------|------------------------|----------------|
| 1.2   | 0.95                   | 0.14           |
| 1.4   | 2.10                   | 0.33           |
| 1.6   | 3.77                   | 0.61           |
| 1.8   | 6.7                    | 1.01           |

You must compute β for each temperature (using the relation above and appropriate unit conversions from atm to dyn/cm² and cal to erg) and then take the mean over the four temperatures.

**Disorder β from the λ-point.**  Along the λ-line the critical temperature T_c scales with the ordering energy, giving

β = d ln T_c / d ln v = − d ln T_c / d ln ρ .

From the published λ-point data the following pairs of density ρ (g/cm³) and β have been tabulated:

| ρ    | β    |
|------|------|
| 0.150 | 0.52 |
| 0.155 | 0.64 |
| 0.160 | 0.82 |
| 0.165 | 1.08 |
| 0.170 | 1.43 |

You should produce the list of β values for these densities and also interpolate (or use a suitable method) to obtain β at the density ρ = 0.1684.

**Vibrational γ from compressibility.**  For the vibrational part, a simple model gives γ = − d ln Θ / d ln v, where Θ is a Debye-like temperature. Using the relation ν ∝ χ^{−1/3} ρ^{−1/3} (χ is compressibility) leads to

γ = 1/3 − (1/2) ρ (d²ρ/dp²) / (dρ/dp)² .

The density ρ (in g/cm³) of He II at 1.25 K as a function of pressure p (in atm) is accurately described by the polynomial

10⁴ ρ = 1442 + 20.865 p − 0.8873 p² + 0.02208 p³ .

Evaluate γ at p = 0 using this formula (the polynomial at p=0 yields ρ = 0.1442 g/cm³, not 0.1684; following the paper, this γ value is taken as an approximation for the target density ρ = 0.1684 g/cm³ in the subsequent ratio calculation).

**Ratio Cv^(l)/Cv.**  When both disordering and vibrational contributions are present, the general expression is

β + (v / Cv) (∂p/∂T)_ρ = (β + γ) (Cv^(l) / Cv) ,

where Cv^(l) is the vibrational part of the specific heat. Use the mean left‑hand side obtained from the thermal expansion data, together with the β from the λ‑point (at ρ=0.1684) and the γ value, to solve for Cv^(l)/Cv.

Your script should perform the above calculations, write the results to a JSON file, and save it at the required output path.

## Reproduction target
Produce a single JSON file named `disorder_model_numbers.json` under `/app/outputs` that contains the four computed quantities:

- `beta_thermal_expansion`: the mean β from the thermal‑expansion table (unitless).
- `beta_lambda_point`: a list of β values obtained from the λ‑point data for the densities 0.150, 0.155, 0.160, 0.165, 0.170, and the interpolated value at ρ = 0.1684.
- `gamma_compressibility`: the vibrational γ computed from the polynomial at p = 0 (unitless).
- `Cv_l_ratio`: the vibrational specific heat fraction Cv^(l)/Cv obtained from equation (10).

The exact structure and required keys are given in the output contract. Submit only this file as your primary result.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute disorder model quantities
- Role: scored (load-bearing)
- Action: Using the experimental data tables and polynomial coefficients provided in the instruction, compute the four quantities that validate the disorder model for liquid helium II: (1) the disorder Grüneisen parameter beta from thermal expansion and specific heat data at density rho=0.1684 g/cm³ (mean over the available temperatures), using equation (6) with proper unit conversions; (2) beta from the lambda-point critical temperature vs. volume data (list of values at given densities and interpolation at rho=0.1684), using equation (7); (3) the vibrational Grüneisen parameter gamma from the density-pressure polynomial fit (equation 12) and its derivatives, using equation (11) at p=0 (where the polynomial actually yields rho = 0.1442 g/cm³; this gamma value is then taken as an approximation for rho = 0.1684 in the Cv^(l)/Cv calculation, consistent with the paper); (4) the ratio Cv^(l)/Cv by evaluating equation (10) with the computed left-hand side and the values of beta and gamma. Output a single JSON file containing these four quantities.
- Output file: `/app/outputs/disorder_model_numbers.json`
- Format: json
- Contract: {"type":"object","required":["beta_thermal_expansion","beta_lambda_point","gamma_compressibility","Cv_l_ratio"],"properties":{"beta_thermal_expansion":{"type":"number"},"beta_lambda_point":{"type":"array","items":{"type":"number"}},"gamma_compressibility":{"type":"number"},"Cv_l_ratio":{"type":"number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/disorder_model_numbers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### disorder_model_numbers.json
- path: `/app/outputs/disorder_model_numbers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Disorder model quantities: Grüneisen parameters and vibrational specific heat ratio.
- schema:
  - `type`: object
  - `required`: `beta_thermal_expansion`, `beta_lambda_point`, `gamma_compressibility`, `Cv_l_ratio`
  - `properties`:
    - `beta_thermal_expansion`:
      - `type`: number
    - `beta_lambda_point`:
      - `type`: array
      - `items`:
        - `type`: number
    - `gamma_compressibility`:
      - `type`: number
    - `Cv_l_ratio`:
      - `type`: number

Notes: All quantities are dimensionless. The checker compares each to hidden reference values with appropriate absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "disorder_model_numbers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "beta_thermal_expansion",
          "beta_lambda_point",
          "gamma_compressibility",
          "Cv_l_ratio"
        ],
        "properties": {
          "beta_thermal_expansion": {
            "type": "number"
          },
          "beta_lambda_point": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "gamma_compressibility": {
            "type": "number"
          },
          "Cv_l_ratio": {
            "type": "number"
          }
        }
      },
      "description": "Disorder model quantities: Grüneisen parameters and vibrational specific heat ratio."
    }
  ],
  "notes": "All quantities are dimensionless. The checker compares each to hidden reference values with appropriate absolute tolerances."
}
```

## How you are scored
A hidden verifier will independently recompute the same four quantities from the provided data using a reference implementation. Your submitted numbers will be compared against these recomputed references. Each numeric field is compared with an appropriate tolerance; the verifier then combines the results into a final reward score between 0 and 1. To receive full credit, your computed values must agree with the expected values within the tolerances. The verifier does not require matching specific figures from the original paper; it only checks the correctness of your calculation.
