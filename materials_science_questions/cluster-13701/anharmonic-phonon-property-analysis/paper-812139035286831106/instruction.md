# Debye Temperature and Intermediate-T Power-Law Exponent from Polyethylene Heat Capacity

## Problem background
The heat capacity of crystalline polyethylene at low temperatures is dominated by lattice vibrations. Continuum approximations, notably the Debye and Tarasov models, are used to describe this behavior, but their validity is limited by anisotropy and chain stiffness. This task quantitatively evaluates whether the Debye approximation holds only at very low temperatures and whether the Tarasov model's predicted linear temperature dependence appears in the intermediate range.

## Approach
Two independent analyses are performed. First, from the experimentally observed low-temperature T³ law (coefficient a₃ = 2.64 × 10⁻⁵ cal/(mol·K³)), the Debye characteristic temperature Θ₃ is derived using the Debye formula that relates heat capacity to the gas constant R and the T³ coefficient. Second, the heat capacity c_V values in the 100–190 K range (provided from the literature) are fit to a power law c_V = a·T^b via log-log linear regression; the slope b is the exponent. These computations test the Debye and Tarasov continuum approximations without performing a full multiparameter fit.

## Reproduction target
Using the supplied low-temperature coefficient a₃ and the Debye formula c_V = 3R·4π⁴/(5Θ₃³)·T³, compute the Debye temperature Θ₃ (in K) and output it along with a₃ and the formula used in `/app/outputs/low_T_fit.json`. Then parse the provided c_V data for temperatures 100–190 K (cal/(mol·K)), apply a log10 transform to both T and c_V, perform ordinary least-squares linear regression, and write the fitted slope, intercept, exponent b, and coefficient a to `/app/outputs/intermediate_T_fit.json`.

## Provided data

The following experimental heat capacity values ($c_V$ in cal/(mol·K)) for 100% crystalline polyethylene in the temperature range 100–190 K are taken from Table 1 of the paper.

| T (K) | c_V [cal/(mol·K)] |
|-------|-------------------|
| 100   | 2.261             |
| 110   | 2.435             |
| 120   | 2.599             |
| 130   | 2.760             |
| 140   | 2.919             |
| 150   | 3.068             |
| 160   | 3.234             |
| 170   | 3.379             |
| 180   | 3.542             |
| 190   | 3.684             |

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute low-temperature Debye parameters
- Role: scored
- Action: Using the given low-temperature T³ coefficient a₃ = 2.64 × 10⁻⁵ cal/(mol·K³) and the Debye formula for heat capacity in a continuum approximation, compute the Debye characteristic temperature Θ₃ (in K). The Debye relation links a₃, the gas constant R, and Θ₃. Output the coefficient a₃, the computed Θ₃, and the formula used.
- Output file: `/app/outputs/low_T_fit.json`
- Format: json
- Contract: type=object; required=['a3', 'Theta3_K', 'formula']; items={}; units={'a3': 'cal/(mol·K³)', 'Theta3_K': 'K'}
- Scoring: scored by hidden verifier

### Step 2: Perform log-log linear fit on intermediate-temperature c_V
- Role: scored
- Action: Parse the provided c_V data (Table 1 values for temperatures 100–190 K, in cal/(mol·K)). Apply log10 to both temperature T (in K) and c_V, then perform ordinary least-squares linear regression to obtain the slope b (power-law exponent) and intercept log10(a) in the relation c_V = a·T^b. Output the fitted slope, intercept, exponent b, and coefficient a.
- Output file: `/app/outputs/intermediate_T_fit.json`
- Format: json
- Contract: type=object; required=['slope', 'intercept', 'exponent_b', 'coefficient_a']; items={}; units={'slope': 'dimensionless', 'intercept': 'log10(cal/(mol·K))', 'exponent_b': 'dimensionless', 'coefficient_a': 'cal/(mol·K^(b+1))'}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/low_T_fit.json`
- `/app/outputs/intermediate_T_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### low_T_fit.json
- path: `/app/outputs/low_T_fit.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Debye temperature derived from the low-temperature T³ coefficient a₃ = 2.64e-5 cal/(mol·K³) using the Debye formula c_V = 3R·4π⁴/(5Θ₃³)·T³. The exact Θ₃ is scored against a hidden gold value with a tolerance of ±5 K.
- schema:
  - `type`: object
  - `required`: `a3`, `Theta3_K`, `formula`
  - `items`: object
  - `units`:
    - `a3`: cal/(mol·K³)
    - `Theta3_K`: K

### intermediate_T_fit.json
- path: `/app/outputs/intermediate_T_fit.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Power-law exponent (b) of the heat capacity c_V ∝ T^b in the intermediate temperature range 100–190 K, obtained from a log-log linear regression on the experimentally derived c_V values (Table 1). The exponent is scored against a hidden gold value with a tolerance of ±0.02.
- schema:
  - `type`: object
  - `required`: `slope`, `intercept`, `exponent_b`, `coefficient_a`
  - `items`: object
  - `units`:
    - `slope`: dimensionless
    - `intercept`: log10(cal/(mol·K))
    - `exponent_b`: dimensionless
    - `coefficient_a`: cal/(mol·K^(b+1))

Notes: The agent must compute Θ₃ from the explicitly provided a₃ and the Debye relation (which relates a₃, R, and Θ₃). The intermediate c_V data for the regression is supplied directly in the task instructions; the agent must parse it and perform the fit. The hidden gold values are 260 K for Theta3_K and 0.7576 for exponent_b, with tolerances as stated; these are not disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "low_T_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a3",
          "Theta3_K",
          "formula"
        ],
        "items": {},
        "units": {
          "a3": "cal/(mol·K³)",
          "Theta3_K": "K"
        }
      },
      "description": "Debye temperature derived from the low-temperature T³ coefficient a₃ = 2.64e-5 cal/(mol·K³) using the Debye formula c_V = 3R·4π⁴/(5Θ₃³)·T³. The exact Θ₃ is scored against a hidden gold value with a tolerance of ±5 K."
    },
    {
      "file": "intermediate_T_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "slope",
          "intercept",
          "exponent_b",
          "coefficient_a"
        ],
        "items": {},
        "units": {
          "slope": "dimensionless",
          "intercept": "log10(cal/(mol·K))",
          "exponent_b": "dimensionless",
          "coefficient_a": "cal/(mol·K^(b+1))"
        }
      },
      "description": "Power-law exponent (b) of the heat capacity c_V ∝ T^b in the intermediate temperature range 100–190 K, obtained from a log-log linear regression on the experimentally derived c_V values (Table 1). The exponent is scored against a hidden gold value with a tolerance of ±0.02."
    }
  ],
  "notes": "The agent must compute Θ₃ from the explicitly provided a₃ and the Debye relation (which relates a₃, R, and Θ₃). The intermediate c_V data for the regression is supplied directly in the task instructions; the agent must parse it and perform the fit. The hidden gold values are 260 K for Theta3_K and 0.7576 for exponent_b, with tolerances as stated; these are not disclosed to the agent."
}
```

## How you are scored
A hidden verifier checks each scored artifact independently. For `low_T_fit.json`, it reads the computed `Theta3_K` and compares it against an undisclosed gold value within a narrow tolerance. For `intermediate_T_fit.json`, it reads the exponent `exponent_b` and compares it similarly. Each artifact carries a weight; the final reward is the weighted combination. Reporting the paper's reported numbers without computing them from the given data will not satisfy the verifier.
