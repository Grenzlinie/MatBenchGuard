# Grüneisen parameter from tephroite thermal expansion

## Problem background
The anharmonic properties of silicate minerals are critical for interpreting the state of the Earth's interior. Thermal expansion data for olivine-group minerals provide key thermodynamic parameters — in particular, the Grüneisen parameter γ, which links thermal expansion to lattice dynamics and elastic properties. This task uses published observed linear thermal expansion measurements of tephroite (Mn₂SiO₄) to compute the volume expansion, fit a thermal expansion model, and determine the Grüneisen parameter γ.

## Approach
The approach is a computational re-analysis of measured thermal expansion data. Linear thermal expansion Y (in %) along the three crystallographic axes (a, b, c) is available as a function of temperature. First, the volume expansion Y_v is derived from the linear expansions via the exact geometric relation. A Wachtman-type model that uses Debye thermal energy E(θ, T) is then fitted separately to each of the four expansion curves (a, b, c, and volume) using least-squares optimisation. The model has four fitted parameters per curve: Q₀ (related to the Grüneisen parameter γ through γ = B₀·V₀ / Q₀), a characteristic Debye temperature θ, an anharmonic parameter k, and a factor a − 1 that accounts for the thermal expansion from 0 K to reference temperature. After fitting, the volume Q₀ is combined with the given product B₀·V₀ = 6.28 × 10⁶ J/mol to compute the Grüneisen parameter γ. The pressure derivative of rigidity is deliberately omitted because the required empirical relation is not fully specified in the original source.

## Reproduction target
Starting from the bundled observed linear expansion data (observed_data.csv, columns: Temperature(degC), Y_a, Y_b, Y_c), compute the volume expansion Y_v at each temperature. Fit the Wachtman-type thermal expansion model to the linear data (a, b, c) and to the derived volume data. Output all fitted parameters (Q₀, θ, k, a_minus_1) for each axis and for the volume, plus the derived Grüneisen parameter γ, as a single JSON file fitted_parameters.json conforming to the output contract below. The pressure derivative of rigidity is not required.

## Assets

- observed_thermal_expansion_data
- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute volume thermal expansion
- Role: process
- Action: Read observed linear expansion data (Y_a, Y_b, Y_c) from observed_data.csv, compute volume expansion Y_v = (1+Y_a)*(1+Y_b)*(1+Y_c)-1 for each temperature, and write the result to volume_expansion.csv.
- Evidence: `/app/outputs/volume_expansion.csv`

### Step 2: Fit thermal expansion models and compute Grüneisen parameter
- Role: scored (load-bearing)
- Action: Fit the following Wachtman-type thermal expansion models using Debye thermal energy E(θ,T). For each axis i ∈ {a,b,c}: Y_i(T) = E(θ_i,T) / [3 a_i (Q_{0i} - k_i E(θ_i,T))] + (1 - a_i)/a_i, where a_i = 1 + a_minus_1_i. For volume V: Y_V(T) = E(θ,T) / [a_V (Q_{0V} - k_V E(θ,T))] + (1 - a_V)/a_V, where a_V = 1 + a_minus_1_V. Determine parameters Q0, θ, k, a_minus_1 for each axis and volume via least-squares. Compute Grüneisen parameter γ = B0*V0 / Q0 using the volume Q0 and B0*V0 = 6.28e6 J/mol. Output all fitted parameters and γ to fitted_parameters.json.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: {"a": {"Q0": "float (J/mol)", "theta": "float (K)", "k": "float", "a_minus_1": "float"}, "b": {"Q0": "float", "theta": "float", "k": "float", "a_minus_1": "float"}, "c": {"Q0": "float", "theta": "float", "k": "float", "a_minus_1": "float"}, "V": {"Q0": "float", "theta": "float", "k": "float", "a_minus_1": "float"}, "gamma": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted thermal expansion parameters (Q0, theta, k, a_minus_1) for crystallographic axes a, b, c and volume V, plus the derived Grüneisen parameter gamma.
- schema:
  - `type`: object
  - `required`: `a`, `b`, `c`, `V`, `gamma`
  - `properties`:
    - `a`:
      - `type`: object
      - `properties`:
        - `Q0`:
          - `type`: number
          - `units`: J/mol
        - `theta`:
          - `type`: number
          - `units`: K
        - `k`:
          - `type`: number
        - `a_minus_1`:
          - `type`: number
    - `b`:
      - `type`: object
      - `properties`:
        - `Q0`:
          - `type`: number
          - `units`: J/mol
        - `theta`:
          - `type`: number
          - `units`: K
        - `k`:
          - `type`: number
        - `a_minus_1`:
          - `type`: number
    - `c`:
      - `type`: object
      - `properties`:
        - `Q0`:
          - `type`: number
          - `units`: J/mol
        - `theta`:
          - `type`: number
          - `units`: K
        - `k`:
          - `type`: number
        - `a_minus_1`:
          - `type`: number
    - `V`:
      - `type`: object
      - `properties`:
        - `Q0`:
          - `type`: number
          - `units`: J/mol
        - `theta`:
          - `type`: number
          - `units`: K
        - `k`:
          - `type`: number
        - `a_minus_1`:
          - `type`: number
    - `gamma`:
      - `type`: number

Notes: The pressure derivative of rigidity (∂G/∂P) is excluded because the paper's required empirical relation is not fully specified. Scoring compares each parameter to a hidden reference value within tolerances (Q0, theta within ±5%; k, a_minus_1 within ±10%; gamma within ±5%).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "b",
          "c",
          "V",
          "gamma"
        ],
        "properties": {
          "a": {
            "type": "object",
            "properties": {
              "Q0": {
                "type": "number",
                "units": "J/mol"
              },
              "theta": {
                "type": "number",
                "units": "K"
              },
              "k": {
                "type": "number"
              },
              "a_minus_1": {
                "type": "number"
              }
            }
          },
          "b": {
            "type": "object",
            "properties": {
              "Q0": {
                "type": "number",
                "units": "J/mol"
              },
              "theta": {
                "type": "number",
                "units": "K"
              },
              "k": {
                "type": "number"
              },
              "a_minus_1": {
                "type": "number"
              }
            }
          },
          "c": {
            "type": "object",
            "properties": {
              "Q0": {
                "type": "number",
                "units": "J/mol"
              },
              "theta": {
                "type": "number",
                "units": "K"
              },
              "k": {
                "type": "number"
              },
              "a_minus_1": {
                "type": "number"
              }
            }
          },
          "V": {
            "type": "object",
            "properties": {
              "Q0": {
                "type": "number",
                "units": "J/mol"
              },
              "theta": {
                "type": "number",
                "units": "K"
              },
              "k": {
                "type": "number"
              },
              "a_minus_1": {
                "type": "number"
              }
            }
          },
          "gamma": {
            "type": "number"
          }
        }
      },
      "description": "Fitted thermal expansion parameters (Q0, theta, k, a_minus_1) for crystallographic axes a, b, c and volume V, plus the derived Grüneisen parameter gamma."
    }
  ],
  "notes": "The pressure derivative of rigidity (∂G/∂P) is excluded because the paper's required empirical relation is not fully specified. Scoring compares each parameter to a hidden reference value within tolerances (Q0, theta within ±5%; k, a_minus_1 within ±10%; gamma within ±5%)."
}
```

## How you are scored
A hidden verifier reads your fitted_parameters.json and compares each fitted parameter (Q₀, θ, k, a_minus_1 for a, b, c, V) and the Grüneisen parameter γ to a hidden reference. Each parameter contributes a portion of the total reward; the reward is computed solely from the content of your submitted JSON artifact. Simply reporting the paper's numbers is not sufficient — the verifier expects that the values are the product of the required fitting procedure. The verifier applies appropriate tolerances defined in its scoring logic.
