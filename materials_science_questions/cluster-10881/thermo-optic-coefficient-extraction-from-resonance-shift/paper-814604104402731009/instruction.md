# Thermo-Optic Coefficient Relation for YAG Crystal

## Problem background
Solid-state lasers suffer from thermal lensing caused by temperature-dependent changes in the refractive index of the active medium. Accurately modeling these thermal effects requires distinguishing between the thermo-optic coefficient at constant stress (the conventionally measured quantity) and the coefficient at constant strain. This task addresses the relationship between these two coefficients for YAG-type cubic crystals and quantifies their difference using published material parameters.

## Approach
The core idea is to derive a relationship between the two thermo-optic coefficients from photoelastic theory, then evaluate the derived expression numerically for YAG at room temperature. You will implement the formula that connects the coefficient at zero strain to the experimentally measured coefficient at zero stress, using the known elasto-optic constants, thermal expansion coefficient, and refractive index. Additionally, you will compute the bulging contribution to the generalized thermo-optic coefficient, which accounts for end-face deformation. All required material parameters are provided; no external data retrieval is needed.

## Reproduction target
Using the provided YAG material constants, compute the thermo-optic coefficient at zero strain (∂n/∂T)ₑ and the relative difference between it and the zero-stress coefficient (∂n/∂T)σ, defined as ((∂n/∂T)ₑ − (∂n/∂T)σ) / (∂n/∂T)σ. Report these in thermo_optic_results.json. Independently compute the bulging term χ_bg^(2) = (n₀−1)(1+ν)α_T and report it in bulging_coefficient.json. The goal is to produce the numerical values that emerge from the formulas when the prescribed constants are substituted.

## Assets

- YAG Material Parameters

## Workflow steps

### Step 1: Compute thermo-optic coefficients and relative difference
- Role: scored (load-bearing)
- Action: Using the provided material constants (n_0, alpha_T, p_11, p_12, beta_sigma), compute the thermo-optic coefficient at zero strain beta_epsilon via the relation (∂n/∂T)_σ = (∂n/∂T)_ε - (alpha_T * n_0^3)/2 * (p_11 + 2 p_12). Then compute the relative difference (beta_epsilon - beta_sigma) / beta_sigma.
- Output file: `/app/outputs/thermo_optic_results.json`
- Format: json
- Contract: {"beta_epsilon": "float (unit K^{-1})", "relative_difference": "float (dimensionless decimal)"}
- Scoring: scored by hidden verifier

### Step 2: Compute bulging coefficient chi_bg^(2)
- Role: scored
- Action: Compute the bulging term chi_bg^(2) using the formula chi_bg^(2) = (n_0 - 1) * (1 + nu) * alpha_T, with the given refractive index, thermal expansion coefficient, and Poisson's ratio.
- Output file: `/app/outputs/bulging_coefficient.json`
- Format: json
- Contract: {"chi_bg_2": "float (unit K^{-1})"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_optic_results.json`
- `/app/outputs/bulging_coefficient.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_optic_results.json
- path: `/app/outputs/thermo_optic_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The derived thermo-optic coefficient at zero strain and the relative difference computed from the given fixed material constants.
- schema:
  - `type`: object
  - `required`:
    - `beta_epsilon`: float (K^{-1})
    - `relative_difference`: float (dimensionless)

### bulging_coefficient.json
- path: `/app/outputs/bulging_coefficient.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The bulging term chi_bg^(2) computed from the given material constants.
- schema:
  - `type`: object
  - `required`:
    - `chi_bg_2`: float (K^{-1})

Notes: Both quantities are obtained by substituting provided material constants into formulas derived in the paper. The agent must implement the arithmetic and report the values. The checker compares the reported values to the paper's gold numbers within tight tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_optic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "beta_epsilon": "float (K^{-1})",
          "relative_difference": "float (dimensionless)"
        }
      },
      "description": "The derived thermo-optic coefficient at zero strain and the relative difference computed from the given fixed material constants."
    },
    {
      "file": "bulging_coefficient.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "chi_bg_2": "float (K^{-1})"
        }
      },
      "description": "The bulging term chi_bg^(2) computed from the given material constants."
    }
  ],
  "notes": "Both quantities are obtained by substituting provided material constants into formulas derived in the paper. The agent must implement the arithmetic and report the values. The checker compares the reported values to the paper's gold numbers within tight tolerances."
}
```

## How you are scored
A hidden verifier reads the artifacts you write to /app/outputs and compares the reported numerical values to the expected results (the paper's published values) within undisclosed tolerances. Each output file contributes a portion of the total reward, with the main results carrying the largest weight. The verifier does not inspect your code; only the contents of the output files are evaluated. Honest re‑implementation of the formulas is expected; merely guessing the numbers is unlikely to match the hidden gold precisely.
