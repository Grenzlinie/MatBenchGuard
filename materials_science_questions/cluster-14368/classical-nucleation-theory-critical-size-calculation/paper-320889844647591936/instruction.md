# Classical Nucleation Theory Critical Size Calculation

## Problem background
When saturated air free of all foreign nuclei undergoes a very sudden expansion, condensation can occur in distinct regimes depending on the volume ratio v2/v1. Experiments identified critical expansion ratios at which rain‑like condensation (few large drops), cloud‑like condensation (dense fog), and a sensitive colour tint appear. These thresholds, together with adiabatic cooling and classical nucleation theory, allow one to compute the maximum supersaturation reached in the gas and the equivalent radius of the critical droplet (the smallest water aggregate that can grow spontaneously). This task extracts those quantitative, compute‑driven results for saturated air initially at 20 °C.

## Approach
The computation proceeds in two conceptual stages. First, the final temperature after adiabatic expansion is obtained from the initial temperature and the measured volume ratio, using the adiabatic relation for an ideal gas. With the final temperature known, the saturated vapour pressure of water above a flat surface is calculated at both the initial and final temperatures via a standard empirical relation (Antoine equation). The degree of supersaturation S is defined as the ratio of the actual vapour density after expansion to the equilibrium density at the final temperature; it is computed from the initial and final vapour pressures and the volume ratio, assuming the vapour behaves as a nearly perfect gas. Second, the critical droplet radius r is evaluated from the Kelvin equation, which relates the equilibrium vapour pressure over a curved surface to the surface tension, the liquid density, and the temperature. The surface tension of water is approximated by a linear function of temperature. All required constants (specific heat ratio for air, liquid density of water, specific gas constant for water vapour) are specified in the workflow step. The procedure is applied to three fixed volume ratios that correspond to the experimentally observed condensation thresholds.

## Reproduction target
Produce a JSON file `/app/outputs/results.json` that contains, for each of three condensation thresholds (rain‑like, cloud‑like, and the sensitive tint), the computed supersaturation ratio (dimensionless) and the critical droplet radius (in metres). The initial conditions are saturated air at 20 °C. The three volume ratios are provided in the workflow step. Your result must be derived by faithfully implementing the adiabatic cooling, vapour‑pressure, and Kelvin‑equation calculations described there.

## Assets

- Python 3.8+: python>=3.8

## Workflow steps

### Step 1: Compute supersaturation and critical radius
- Role: scored
- Action: For each of the three given volume ratios (v2/v1 = 1.252, 1.38, 1.42) and initial conditions (T1=20°C = 293.15 K, γ=1.41, initial saturated vapor pressure π1 computed via Antoine equation), perform the following: 1) Compute final temperature T2 using adiabatic cooling: T2 = T1 * (v1/v2)^(γ-1). 2) Compute saturated vapor pressure π2 at T2 using the Antoine equation for water: log10(P_mmHg) = 8.07131 - 1730.63 / (233.426 + T_°C), where T_°C is temperature in Celsius. 3) Compute supersaturation ratio S = (π1/π2) * (v1/v2)^γ. 4) Compute surface tension σ (N/m) at T2 using σ_mN/m = 75.6 - 0.14*(T2_K - 273), then convert to N/m. 5) Compute critical droplet radius r = (2σ) / (ρ_L * R_v * T2 * ln S), with ρ_L = 1000 kg/m³ and R_v = 461.5 J/(kg·K). 6) Write an array of objects with keys: threshold (string: one of 'rain', 'cloud', 'sensitive'), volume_ratio (number), supersaturation (float, dimensionless), critical_radius_m (float, in meters) to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON array of objects, each with keys: 'threshold' (string, one of 'rain', 'cloud', 'sensitive'), 'volume_ratio' (number), 'supersaturation' (float), 'critical_radius_m' (float).
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
- description: The computed supersaturation (dimensionless) and critical droplet radius (meters) for each of the three condensation thresholds, compared to the paper-reported reference values within specified relative tolerances.
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

Notes: The hidden checker will compare each reported supersaturation and radius to the paper's gold values using relative tolerances (2% for supersaturation, 5% for radius). Full credit if all six values are within tolerance; partial credit scales linearly with the number of in-tolerance values.

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
      "description": "The computed supersaturation (dimensionless) and critical droplet radius (meters) for each of the three condensation thresholds, compared to the paper-reported reference values within specified relative tolerances."
    }
  ],
  "notes": "The hidden checker will compare each reported supersaturation and radius to the paper's gold values using relative tolerances (2% for supersaturation, 5% for radius). Full credit if all six values are within tolerance; partial credit scales linearly with the number of in-tolerance values."
}
```

## How you are scored
A hidden verifier compares each computed supersaturation and critical radius in your `results.json` against independently obtained reference values using appropriate relative tolerances. It then combines the per‑stage checks into a single weighted reward between 0 and 1. The more of the computed quantities that fall within tolerance, the higher your score. Simply reporting a number without performing the required calculation will not satisfy the checker, as the reference values are derived from the same physical constants and equations and are not disclosed to you.
