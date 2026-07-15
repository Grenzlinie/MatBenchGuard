# Generalized Debye model limit verification

## Problem background
The Debye model accurately describes the specific heat of crystalline solids: at high temperatures the molar specific heat approaches the Dulong–Petit value 3R (R is the universal gas constant), and at low temperatures a T³ law holds. Extending such a description to liquids and gases is not obvious. A generalized Debye approximation has been proposed in which the ordinary Debye temperature Θ_D is multiplied by a factor (1+L), where L is a Lindemann‑like parameter that measures the ratio of the thermal vibration amplitude to the interparticle distance. In the solid state L ≪ 1, recovering the standard Debye theory; in the gas limit L → ∞ the effective Debye temperature grows and the thermodynamic functions transition to those of an ideal gas. The model gives expressions for entropy, energy, pressure, and constant‑volume specific heat, all stated in terms of the Debye function D(x) and the renormalized Debye temperature Θ = Θ_D(1+L). In the high‑temperature limit (T ≫ Θ_D) the specific heat for a solid is known to approach 3R/μ per mole, while that of an ideal gas approaches 3R/(2μ). Similarly, the entropy should reduce to the ideal‑gas Sackur–Tetrode expression when L is large. This task verifies that an implementation of the core formulas correctly produces these limiting behaviours.

## Approach
Implement the Debye function D(x) = (3/x³) ∫₀ˣ y³/(eʸ−1) dy using numerical quadrature (e.g., SciPy's `integrate.quad`). Then implement the generalized Debye formulas for the constant‑volume specific heat C_v and the entropy S. These formulas depend on the renormalized Debye temperature Θ = Θ_D(1+L), the temperature T, the atomic weight μ (dimensionless), and for entropy additionally on the specific volume v (m³/mol), the atomic mass m (kg), and a partition‑function factor g_a. Choose three parameter sets that represent: (1) the solid limit—L very small (e.g. 0.001) and T ≫ Θ_D; (2) the gas limit—L large (e.g. 100) and T ≫ Θ_D; (3) an entropy check—L large, with physically plausible v, μ, m, g_a. For the solid and gas cases compute C_v and compare to the theoretical limits 3R/μ and 3R/(2μ). For the entropy case compute S and compare to the ideal‑gas entropy from the Sackur–Tetrode equation. Record every input parameter, the computed thermodynamic value, the expected theoretical value, and the relative error in a JSON file. All calculations use standard Python scientific packages (NumPy, SciPy); no external dataset is required—the agent supplies the numerical constants.

## Reproduction target
Produce a JSON file at `/app/outputs/verification_results.json` with three top‑level objects: `solid_limit`, `gas_limit`, and `entropy_check`. Each object must contain the chosen input parameters and both the computed and expected values of the thermodynamic quantity, together with the relative error `|computed − expected| / |expected|`. For `solid_limit`, show that for a small L the computed C_v is close to the solid limit 3R/μ. For `gas_limit`, show that for a large L the computed C_v approaches the ideal‑gas limit 3R/(2μ). For `entropy_check`, show that for a large L the computed S matches the ideal‑gas entropy derived from the Sackur–Tetrode equation. The exact numerical values of the parameters are your choice; they must be reported in the file so the verifier can recompute the expected limits independently.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement generalized Debye model and verify limits
- Role: scored
- Action: Implement the Debye function D(x) via numerical integration and the generalized Debye formulas for specific heat C_v and entropy S. Choose two parameter sets to represent the solid limit and the gas limit, and a third set to check the ideal-gas entropy. For each set, compute the thermodynamic quantity, compare it to the expected theoretical limit (3R/μ for solid, 3R/(2μ) for gas, and the ideal-gas entropy expression), and record all parameters, computed values, expected values, and relative errors.
- Output file: `/app/outputs/verification_results.json`
- Format: json
- Contract: {
  "solid_limit": {
    "mu": "number (dimensionless atomic weight)",
    "L": "number (Lindemann parameter)",
    "T": "number (temperature in K)",
    "Theta_D": "number (Debye temperature in K)",
    "computed_Cv": "number (C_v in J/(mol·K))",
    "expected_Cv": "number (theoretical solid limit)",
    "relative_error": "number"
  },
  "gas_limit": {
    "mu": "number",
    "L": "number",
    "T": "number",
    "Theta_D": "number",
    "computed_Cv": "number",
    "expected_Cv": "number",
    "relative_error": "number"
  },
  "entropy_check": {
    "L": "number",
    "T": "number",
    "v": "number (specific volume in m³/mol)",
    "mu": "number",
    "m": "number (atomic mass in kg)",
    "g_a": "number (partition function factor)",
    "computed_S": "number (S in J/(mol·K))",
    "ideal_gas_S": "number",
    "relative_error": "number"
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/verification_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### verification_results.json
- path: `/app/outputs/verification_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Verification of the generalized Debye model limits: the file provides parameters and computed thermodynamic quantities for the solid-limit, gas-limit specific heat, and an ideal-gas entropy check, along with computed relative errors. The checker recomputes the expected limits from the parameters and validates that the reported relative errors do not exceed a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `solid_limit`:
      - `mu`: number
      - `L`: number
      - `T`: number
      - `Theta_D`: number
      - `computed_Cv`: number
      - `expected_Cv`: number
      - `relative_error`: number
    - `gas_limit`:
      - `mu`: number
      - `L`: number
      - `T`: number
      - `Theta_D`: number
      - `computed_Cv`: number
      - `expected_Cv`: number
      - `relative_error`: number
    - `entropy_check`:
      - `L`: number
      - `T`: number
      - `v`: number
      - `mu`: number
      - `m`: number
      - `g_a`: number
      - `computed_S`: number
      - `ideal_gas_S`: number
      - `relative_error`: number

Notes: The task is scoped to the limit-verification aspect of the generalized Debye model. Full neon-specific determination of Θ_D(v) and construction of p(v,T) surfaces are excluded because they require external tabulated data that is not publicly accessible.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "verification_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "solid_limit": {
            "mu": "number",
            "L": "number",
            "T": "number",
            "Theta_D": "number",
            "computed_Cv": "number",
            "expected_Cv": "number",
            "relative_error": "number"
          },
          "gas_limit": {
            "mu": "number",
            "L": "number",
            "T": "number",
            "Theta_D": "number",
            "computed_Cv": "number",
            "expected_Cv": "number",
            "relative_error": "number"
          },
          "entropy_check": {
            "L": "number",
            "T": "number",
            "v": "number",
            "mu": "number",
            "m": "number",
            "g_a": "number",
            "computed_S": "number",
            "ideal_gas_S": "number",
            "relative_error": "number"
          }
        }
      },
      "description": "Verification of the generalized Debye model limits: the file provides parameters and computed thermodynamic quantities for the solid-limit, gas-limit specific heat, and an ideal-gas entropy check, along with computed relative errors. The checker recomputes the expected limits from the parameters and validates that the reported relative errors do not exceed a hidden tolerance."
    }
  ],
  "notes": "The task is scoped to the limit-verification aspect of the generalized Debye model. Full neon-specific determination of Θ_D(v) and construction of p(v,T) surfaces are excluded because they require external tabulated data that is not publicly accessible."
}
```

## How you are scored
A hidden verifier reads `verification_results.json` after you submit. It recomputes the theoretical limits (3R/μ, 3R/(2μ), and the ideal‑gas entropy) from the parameters you recorded, and checks that the relative errors you reported are computed correctly. It also verifies that each relative error does not exceed a hidden tolerance. In addition, the verifier may recompute a sample of the Debye function to confirm that the implementation is sound. The total reward is a weighted combination of these checks, with the largest weight on the two specific‑heat limits and the entropy check. Simply writing the expected numbers without actually evaluating the Debye function and the generalized formulas will not pass the hidden verification.
