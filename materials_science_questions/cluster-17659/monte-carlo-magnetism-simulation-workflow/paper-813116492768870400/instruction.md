# Gaussian-broadened Gaussian Kubo-Toyabe Relaxation Function Verification

## Problem background
In zero-field muon spin relaxation (μSR), the time evolution of muon polarization in a static disordered magnetic environment is described by a Kubo‑Toyabe (KT) relaxation function. The standard Gaussian KT function assumes a single Gaussian width for the local field distribution, but some highly disordered magnets exhibit relaxation shapes with shallower minima than the Gaussian form can reproduce — in extreme cases, the relaxation becomes monotonic without a minimum. A “Gaussian‑broadened Gaussian” (GBG) model has been proposed, in which the single‑site Gaussian width itself follows a Gaussian distribution, leading to a closed‑form relaxation function with two parameters: an effective width Δ_eff and a relative broadening R. The target of this task is to implement the GBG relaxation function and examine its behavior at R=0 and R=1.

## Approach
The core method implements the closed‑form expression for the GBG relaxation function G_z^GBG(t; Δ_eff, R). The standard Gaussian Kubo‑Toyabe function, which serves as the R=0 reference, is

G_z^G(t) = 1/3 + (2/3)(1 − Δ² t²) exp(−Δ² t² / 2)

with Δ = Δ_eff.

The GBG function is

G_z^GBG(t) = 1/3 + (2/3) ((1+R²) / (1+R² + R² Δ_eff² t²))^(3/2)
              × (1 − Δ_eff² t² / (1+R² + R² Δ_eff² t²))
              × exp( −Δ_eff² t² / [2(1+R² + R² Δ_eff² t²)] ).

For Δ_eff = 1, compute the function for R = 0 and R = 1.  Compare the R=0 values to the standard Gaussian KT function with Δ = 1.  Check whether the R=1 sequence is monotonic non‑increasing.
The agent computes G_z^GBG(t) at a set of time points for both R values, compares the R=0 values against the standard Gaussian KT, and checks the monotonicity of the R=1 sequence. No external data are needed; all quantities are produced from the analytic formulas.

## Reproduction target
Implement G_z^GBG(t; Δ_eff, R) from the given expression. For Δ_eff = 1, compute its values at 11 equally spaced time points from 0 to 5 (inclusive) for two cases: R = 0 and R = 1.  
• Determine whether the R=0 values match the standard Gaussian Kubo‑Toyabe function G_z^G(t) with Δ = 1.  
• Determine whether the R=1 values form a monotonic non‑increasing sequence.  
Record the computed (t, G_z) pairs for both R values and the two boolean determinations in a JSON file.

## Assets
No external assets are required. The task uses only standard mathematical libraries and the formulas provided.

## Workflow steps

### Step 1: Compute GBG function and verify limits
- Role: scored (load-bearing)
- Action: Implement the Gaussian-broadened Gaussian (GBG) static zero-field Kubo-Toyabe relaxation function G_z^GBG(t; Δ_eff, R) using the closed-form expression involving Δ_eff and R. For Δ_eff = 1, compute the function at 11 equally spaced time points from 0 to 5 (inclusive) for R = 0 and R = 1. Determine whether the R=0 values match the standard Gaussian Kubo-Toyabe function G_z^G(t) with rms width Δ = 1, and whether the R=1 sequence is monotonic non-increasing. Write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: object with keys: R0_values (list of [t, Gz] pairs for 11 time points), R1_values (list of [t, Gz] pairs for 11 time points), R0_matches_Gaussian (bool), R1_monotonic (bool). All Gz values are floats.
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
- target_policy: metric_recompute
- description: Computed GBG relaxation function values for two parameter settings and corresponding verification booleans.
- schema:
  - `type`: object
  - `required`: `R0_values`, `R1_values`, `R0_matches_Gaussian`, `R1_monotonic`
  - `properties`:
    - `R0_values`:
      - `type`: array
      - `items`:
        - `type`: array
        - `prefixItems`:
          - `type`: number
          - `type`: number
        - `minItems`: 2
        - `maxItems`: 2
      - `minItems`: 11
      - `maxItems`: 11
    - `R1_values`:
      - `type`: array
      - `items`:
        - `type`: array
        - `prefixItems`:
          - `type`: number
          - `type`: number
        - `minItems`: 2
        - `maxItems`: 2
      - `minItems`: 11
      - `maxItems`: 11
    - `R0_matches_Gaussian`:
      - `type`: boolean
    - `R1_monotonic`:
      - `type`: boolean

Notes: The checker independently recomputes the GBG function and the standard Gaussian KT function, compares the agent's numerical values within tolerance, and verifies the boolean assertions.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "R0_values",
          "R1_values",
          "R0_matches_Gaussian",
          "R1_monotonic"
        ],
        "properties": {
          "R0_values": {
            "type": "array",
            "items": {
              "type": "array",
              "prefixItems": [
                {
                  "type": "number"
                },
                {
                  "type": "number"
                }
              ],
              "minItems": 2,
              "maxItems": 2
            },
            "minItems": 11,
            "maxItems": 11
          },
          "R1_values": {
            "type": "array",
            "items": {
              "type": "array",
              "prefixItems": [
                {
                  "type": "number"
                },
                {
                  "type": "number"
                }
              ],
              "minItems": 2,
              "maxItems": 2
            },
            "minItems": 11,
            "maxItems": 11
          },
          "R0_matches_Gaussian": {
            "type": "boolean"
          },
          "R1_monotonic": {
            "type": "boolean"
          }
        }
      },
      "description": "Computed GBG relaxation function values for two parameter settings and corresponding verification booleans."
    }
  ],
  "notes": "The checker independently recomputes the GBG function and the standard Gaussian KT function, compares the agent's numerical values within tolerance, and verifies the boolean assertions."
}
```

## How you are scored
A hidden verifier independently recomputes G_z^GBG(t) for both R=0 and R=1 from the same formulas, as well as the standard Gaussian KT reference. It compares your submitted numerical values to these recomputed values and checks whether your boolean assertions are correct. The final reward is a weighted combination of the numerical accuracy for the R=0 and R=1 values and the correctness of the two boolean flags. Submitting the correct values and booleans from an honest computation will earn full credit; reporting pre‑known numbers without a correct implementation will not.
