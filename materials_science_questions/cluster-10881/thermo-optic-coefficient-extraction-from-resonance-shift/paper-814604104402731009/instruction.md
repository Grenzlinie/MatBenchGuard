# Thermo-Optic Coefficient Relation for YAG Crystal

## Problem background
Solid-state lasers suffer from thermal lensing caused by temperature-dependent changes in the refractive index of the active medium. Accurately modeling these thermal effects requires distinguishing between the thermo-optic coefficient at constant stress (the conventionally measured quantity) and the coefficient at constant strain. This task addresses the relationship between these two coefficients for YAG-type cubic crystals and quantifies their difference using published material parameters.

## Approach
The core idea is to derive a relationship between the two thermo-optic coefficients from photoelastic theory, then evaluate the derived expression numerically for YAG at room temperature. You will implement the formula that connects the coefficient at zero strain to the experimentally measured coefficient at zero stress, using the known elasto-optic constants, thermal expansion coefficient, and refractive index. Additionally, you will compute the bulging contribution to the generalized thermo-optic coefficient, which accounts for end-face deformation. All required material parameters are provided below; no external data retrieval is needed.

## Material Parameters (all given, no retrieval needed)
Use the following values (taken from published literature for YAG at room temperature) for all calculations:

- Refractive index:  
  `n_0 = 1.82`
- Thermal expansion coefficient:  
  `α_T = 6.39 × 10⁻⁶ K⁻¹`
- Elasto-optic coefficients:  
  `p₁₁ = -0.029`, `p₁₂ = 0.0091`
- Thermo-optic coefficient at zero stress (the conventionally measured value):  
  `β_σ ≡ (∂n/∂T)σ = 8.48 × 10⁻⁶ K⁻¹`
- Poisson’s ratio:  
  `ν = 0.26`

All symbols are dimensionless or have units as indicated. Substitute them exactly as given into the formulas described below.

## Reproduction target
Using the material constants listed above, compute:

1. The thermo-optic coefficient at zero strain, `β_ε ≡ (∂n/∂T)ε`.
2. The relative difference between the zero-strain and zero-stress coefficients, defined as `(β_ε − β_σ) / β_σ`.
3. The bulging term `χ_bg⁽²⁾ = (n₀ − 1)(1 + ν)α_T`.

Report the first two quantities in `thermo_optic_results.json` and the bulging term in `bulging_coefficient.json`. The goal is to produce the numerical values that emerge from the formulas when the prescribed constants are substituted.

## Workflow steps

### Step 1: Compute thermo-optic coefficients and relative difference
- Role: scored (load-bearing)
- Action: Using the provided material constants, compute the thermo-optic coefficient at zero strain via the relation derived from photoelastic theory:
  ```
  β_σ = β_ε − (α_T · n₀³)/2 · (p₁₁ + 2 p₁₂)
  ```
  Then compute the relative difference `(β_ε − β_σ) / β_σ`.
- Output file: `/app/outputs/thermo_optic_results.json`
- Format: json
- Contract: `{"beta_epsilon": <float (K⁻¹)>, "relative_difference": <float (dimensionless)>}`
- Scoring: scored by hidden verifier

### Step 2: Compute bulging coefficient χ_bg⁽²⁾
- Role: scored
- Action: Compute the bulging term using the formula `χ_bg⁽²⁾ = (n₀ − 1) · (1 + ν) · α_T`, with the given refractive index, thermal expansion coefficient, and Poisson’s ratio.
- Output file: `/app/outputs/bulging_coefficient.json`
- Format: json
- Contract: `{"chi_bg_2": <float (K⁻¹)>}`
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
    - `beta_epsilon`: float (K⁻¹)
    - `relative_difference`: float (dimensionless)

### bulging_coefficient.json
- path: `/app/outputs/bulging_coefficient.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The bulging term χ_bg⁽²⁾ computed from the given material constants.
- schema:
  - `type`: object
  - `required`:
    - `chi_bg_2`: float (K⁻¹)

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