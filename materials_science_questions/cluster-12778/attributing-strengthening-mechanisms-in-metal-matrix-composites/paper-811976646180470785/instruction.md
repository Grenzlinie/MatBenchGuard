# Reproduce Grain Refinement and Dislocation Strengthening Contributions in TiC/TiAl Composites

## Problem background
TiC particle reinforced γ-TiAl intermetallic matrix composites (IMCs) are fabricated by spark plasma sintering to improve room-temperature mechanical properties. The addition of TiC enhances bending strength, with an optimum performance at a particular TiC weight fraction. The strengthening is attributed to two primary mechanisms: indirect grain refinement of the matrix and direct interaction between dislocations and reinforcing particles. Quantifying the individual contributions of these two mechanisms is essential to understanding the composite's behaviour.

## Approach
The indirect grain refinement contribution is modelled using the Hall–Petch relation: δσ_i = k · (d^{-1/2} – d_0^{-1/2}), where k is the Hall–Petch slope constant, d is the grain size of the composite, and d_0 is the grain size of the unreinforced alloy. The direct dislocation contribution is estimated from the dislocation strengthening equation: δσ_p = C · μ · b · ρ_t^{1/2}, where C is a constant, μ is the matrix elastic modulus, b is the Burgers vector, and ρ_t is the dislocation density in the composite. Both increments are computed for the composite with the optimal TiC fraction, using the following paper‑reported parameters: k = 2.4 MPa·mm^{1/2}, d = 2 μm, d_0 = 8 μm, C = 1.25, μ = 173 GPa, b = 2×10^{-10} m, and ρ_t = 4×10^{13} m^{-2}. The results are written as two JSON files, one per mechanism.

## Reproduction target
Compute the grain refinement strengthening increment δσ_i and the dislocation strengthening increment δσ_p for the 7 wt% TiC composite using the equations and parameter values given in the approach. Write the computed δσ_i (in MPa) to `/app/outputs/step_01_grain_refinement_strength.json` and δσ_p (in MPa) to `/app/outputs/step_02_dislocation_strength.json`. The two JSON files constitute the full deliverable.

## Assets
No external datasets, models, or specialized tools are required. All necessary parameters are provided in the instruction, and the calculations can be carried out using standard Python libraries (e.g., `numpy`).

## Workflow steps

### Step 1: Compute grain refinement contribution (Hall–Petch)
- Role: scored (load‑bearing)
- Action: Using the Hall–Petch relation δσ_i = k·(d^{–1/2} – d_0^{–1/2}) with the provided parameter values for the Hall–Petch slope constant (k), composite grain size (d), and unreinforced grain size (d_0), compute the indirect strengthening increment δσ_i (in MPa) and write the result to the output file.
- Output file: `/app/outputs/step_01_grain_refinement_strength.json`
- Format: json
- Contract: {"delta_sigma_i": <float>}
- Scoring: scored by hidden verifier

### Step 2: Compute dislocation strengthening contribution
- Role: scored (load‑bearing)
- Action: Using the dislocation strengthening equation δσ_p = C μ b ρ_t^{1/2} with the provided constant C, matrix elastic modulus μ, Burgers vector b, and composite dislocation density ρ_t, compute the direct strengthening increment δσ_p (in MPa) and write the result to the output file.
- Output file: `/app/outputs/step_02_dislocation_strength.json`
- Format: json
- Contract: {"delta_sigma_p": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_grain_refinement_strength.json`
- `/app/outputs/step_02_dislocation_strength.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_grain_refinement_strength.json
- path: `/app/outputs/step_01_grain_refinement_strength.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed grain refinement strengthening increment δσ_i for the 7 wt% TiC IMC.
- schema:
  - `type`: object
  - `required`:
    - `delta_sigma_i`: number
  - `units`:
    - `delta_sigma_i`: MPa

### step_02_dislocation_strength.json
- path: `/app/outputs/step_02_dislocation_strength.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed dislocation strengthening increment δσ_p for the 7 wt% TiC IMC.
- schema:
  - `type`: object
  - `required`:
    - `delta_sigma_p`: number
  - `units`:
    - `delta_sigma_p`: MPa

Notes: The two scored outputs correspond to the two main strengthening mechanisms analysed in the paper. The hidden checker will recompute each quantity from the same public parameters and compare your submitted values against the expected computed values within a tolerance.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_grain_refinement_strength.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_sigma_i": "number"
        },
        "units": {
          "delta_sigma_i": "MPa"
        }
      },
      "description": "Computed grain refinement strengthening increment δσ_i for the 7 wt% TiC IMC."
    },
    {
      "file": "step_02_dislocation_strength.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_sigma_p": "number"
        },
        "units": {
          "delta_sigma_p": "MPa"
        }
      },
      "description": "Computed dislocation strengthening increment δσ_p for the 7 wt% TiC IMC."
    }
  ],
  "notes": "The two scored outputs correspond to the two main strengthening mechanisms analysed in the paper. The hidden checker will recompute each quantity from the same public parameters and compare your submitted values against the expected computed values within a tolerance."
}
```

## How you are scored
A hidden verifier independently recomputes the expected δσ_i and δσ_p from the same equations and parameters given in the Approach. Your submitted values are compared to these expected computed values within a tolerance. Each step is scored separately, and the final reward is the weighted sum of the per‑step scores. Simply reporting numbers without performing the computation will result in a low or zero score.