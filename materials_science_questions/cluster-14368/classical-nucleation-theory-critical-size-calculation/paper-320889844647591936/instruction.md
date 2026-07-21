# Classical Nucleation Theory Critical Size Calculation

## Problem background
When saturated water-vapour air free of extraneous nuclei undergoes a very sudden adiabatic expansion, condensation can occur in distinct regimes depending on the volume ratio \(v_2/v_1\). Classical experiments identified critical expansion ratios at which rain‑like condensation (few large drops), cloud‑like condensation (dense fog), and a sensitive colour tint appear. These thresholds, together with adiabatic cooling and classical nucleation theory, allow one to compute the maximum supersaturation reached in the gas and the equivalent radius of the critical droplet—the smallest water aggregate that can grow spontaneously. This task extracts those quantitative, compute‑driven results for saturated air initially at 20 °C.

## Approach
The computation proceeds in two conceptual stages. First, the final temperature after adiabatic expansion is obtained from the initial temperature and the measured volume ratio, using the adiabatic relation for an ideal gas. With the final temperature known, the saturated vapour pressure of water above a flat surface is calculated at both the initial and final temperatures via a standard empirical relation (Antoine equation). The degree of supersaturation \(S\) is defined as the ratio of the actual vapour density after expansion to the equilibrium density at the final temperature; it is computed from the initial and final vapour pressures and the volume ratio, assuming the vapour behaves as a nearly perfect gas. Second, the critical droplet radius \(r\) is evaluated from the Kelvin equation, which relates the equilibrium vapour pressure over a curved surface to the surface tension, the liquid density, and the temperature. The surface tension of water is approximated by a linear function of temperature. All required constants (specific heat ratio for air, liquid density of water, specific gas constant for water vapour) are specified in the workflow step. The procedure is applied to three fixed volume ratios that correspond to the experimentally observed condensation thresholds.

## Reproduction target
Produce a JSON file `/app/outputs/results.json` that contains, for each of the three condensation thresholds (rain‑like, cloud‑like, and the sensitive tint), the computed supersaturation ratio (dimensionless) and the critical droplet radius (in metres). The initial conditions are saturated air at 20 °C. The three volume ratios are provided in the workflow step, along with their exact correspondences to the threshold labels. Your result must be derived by faithfully implementing the adiabatic cooling, vapour‑pressure, and Kelvin‑equation calculations described there.

## Assets

- Python 3.8+: python>=3.8

## Workflow steps

### Step 1: Compute supersaturation and critical radius
- Role: scored
- Action: For each of the three condensation thresholds, use the volume ratio explicitly associated with that threshold: **rain** (\(v_2/v_1 = 1.252\)), **cloud** (\(v_2/v_1 = 1.38\)), and **sensitive** (\(v_2/v_1 = 1.42\)). Initial conditions: \(T_1 = 20\,^\circ\text{C} = 293.15\ \text{K}\), \(\gamma = 1.41\), and the initial saturated vapour pressure \(\pi_1\) is computed with the Antoine equation. For each threshold, perform the following:
  1) Compute final temperature \(T_2\) using adiabatic cooling: \(T_2 = T_1 \cdot (v_1/v_2)^{\gamma-1}\).
  2) Compute saturated vapour pressure \(\pi_2\) at \(T_2\) using the Antoine equation for water:
     \[
     \log_{10}(P_\text{mmHg}) = 8.07131 - \frac{1730.63}{233.426 + T_\text{°C}},
     \]
     where \(T_\text{°C} = T_2 - 273.15\).
  3) Compute supersaturation ratio:
     \[
     S = \frac{\pi_1}{\pi_2} \cdot \left(\frac{v_1}{v_2}\right)^\gamma.
     \]
  4) Compute surface tension \(\sigma\) (N m⁻¹) at \(T_2\):
     \[
     \sigma_{\text{mN/m}} = 75.6 - 0.14\,(T_{2\text{K}} - 273),
     \]
     then convert to N m⁻¹ (\(\sigma = \sigma_{\text{mN/m}} \times 10^{-3}\)).
  5) Compute critical droplet radius:
     \[
     r = \frac{2\sigma}{\rho_L \, R_v \, T_{2\text{K}} \, \ln S},
     \]
     with \(\rho_L = 1000\ \text{kg m}^{-3}\) and \(R_v = 461.5\ \text{J kg}^{-1}\text{K}^{-1}\).
  6) Write an array of objects to `/app/outputs/results.json`. Each object must have keys: `threshold` (one of `"rain"`, `"cloud"`, `"sensitive"`), `volume_ratio` (the numerical value used), `supersaturation` (float, dimensionless), and `critical_radius_m` (float, in metres). The array must contain exactly three entries, one for each threshold, with the volume ratios given above.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON array of objects, each with keys: `threshold` (string, one of `"rain"`, `"cloud"`, `"sensitive"`), `volume_ratio` (number), `supersaturation` (float), `critical_radius_m` (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The computed supersaturation (dimensionless) and critical droplet radius (metres) for each of the three condensation thresholds, compared to the experimentally determined reference values within specified relative tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `threshold`, `volume_ratio`, `supersaturation`, `critical_radius_m`
    - `properties`:
      - `threshold`:
        - `type`: string
        - `enum`: `rain`, `cloud`, `sensitive`
      - `volume_ratio`:
        - `type`: number
      - `supersaturation`:
        - `type`: number
      - `critical_radius_m`:
        - `type`: number
        - `units`: meters

Notes: The hidden checker will compare each reported supersaturation and radius to the paper’s gold values using relative tolerances (2 % for supersaturation, 5 % for radius). Full credit if all six values are within tolerance; partial credit scales linearly with the number of in‑tolerance values.

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
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "threshold",
            "volume_ratio",
            "supersaturation",
            "critical_radius_m"
          ],
          "properties": {
            "threshold": {
              "type": "string",
              "enum": [
                "rain",
                "cloud",
                "sensitive"
              ]
            },
            "volume_ratio": {
              "type": "number"
            },
            "supersaturation": {
              "type": "number"
            },
            "critical_radius_m": {
              "type": "number",
              "units": "meters"
            }
          }
        }
      },
      "description": "The computed supersaturation (dimensionless) and critical droplet radius (metres) for each of the three condensation thresholds, compared to the experimentally determined reference values within specified relative tolerances."
    }
  ],
  "notes": "The hidden checker will compare each reported supersaturation and radius to the paper's gold values using relative tolerances (2% for supersaturation, 5% for radius). Full credit if all six values are within tolerance; partial credit scales linearly with the number of in-tolerance values."
}
```

## How you are scored
The hidden verifier compares each computed supersaturation and critical radius in your `results.json` against the gold‑standard values obtained from the original experiments. The comparison uses relative tolerances: ±2 % for supersaturation and ±5 % for critical radius. It then combines the per‑element checks into a single weighted reward between 0 and 1. The more of the six values that fall within tolerance, the higher your score. Simply reporting a number without performing the required calculation will not satisfy the checker, as the reference values are the exact physical results reported by the paper.