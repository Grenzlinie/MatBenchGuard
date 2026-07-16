# Mössbauer fraction and temperature shift for impurity nucleus in Debye model

## Problem background
The Mössbauer effect provides a sharp probe of nuclear transitions, and its intensity and line position depend on the lattice vibrations of the host crystal. When a radioactive nucleus is embedded as an impurity in a solid solution, the Mössbauer fraction (recoilless fraction) and the temperature shift of the emitted gamma-ray line are modified relative to the pure host. Understanding how these quantities vary with host properties and with the mass of the impurity is important for designing Mössbauer sources and for interpreting experiments. In this task, we consider the case of a substitutional impurity in a monatomic cubic crystal, where the impurity–host force constants are assumed unchanged (κ=0), and the lattice vibrations are described within the Debye approximation (single Debye temperature, degenerate phonon branches). Under these assumptions, closed-form expressions can be derived for the Mössbauer fraction and for the temperature shift as functions of the host Debye temperature, the impurity and host masses, and the gamma-ray energy. Your goal is to implement these formulas for a specific system: ⁵⁷Fe impurity in a beryllium (Be) lattice, using experimentally known parameters, and to compute the resulting fraction ratios and temperature shifts.

## Approach
The Mössbauer fraction f for the impurity nucleus in the Debye model (κ = 0) is given by

f = exp( - (3R / (2 k_B Θ)) Λ(ξ) )

where the dimensionless recoil energy is R = (ħ² k_γ²) / (2 m), with k_γ = E_γ/(ħ c), E_γ = 14.4 keV, m = mass of ⁵⁷Fe (57 u), and the temperature‑dependent function

Λ(ξ) = (2ξ/π) ∑_{n=-∞}^{∞} (1 − nξ arctan(1/(nξ))) / [1 + μ − 3μ (nξ)² (1 − nξ arctan(1/(nξ)))].

Here ξ = 2π k_B T / (k_B Θ) with Θ = 1160 K, μ = M_Be / m_Fe − 1, M_Be = 9.012 u, m_Fe = 57 u. The n = 0 term is taken as the limit n→0.

The temperature shift of the Mössbauer line between two temperatures T₁ and T₂ (energy difference Δ(δE) arising from the mass change upon γ emission) is obtained from

δE(T) = − (3 k_B Θ / (2 m c²)) χ(ξ),

with

χ(ξ) = (T/Θ) { 1 + 2(1+μ) ∑_{n=1}^{∞} (1 − 3 (nξ)² [1 − nξ arctan(1/(nξ))]) / (1 + μ − 3μ (nξ)² [1 − nξ arctan(1/(nξ))]) }.

The shift in velocity units (mm/s) is Δv = (Δ(δE) / E_γ) c, where c is the speed of light. Compute δE at 80 K, 295 K, and 425 K; the scored shifts are Δv(80→295 K) and Δv(295→425 K).

All sums converge rapidly; truncating at |n| ~ 1000 yields 5-digit accuracy. Use consistent units (SI or atomic) and take care with unit conversions to obtain dimensionless Λ and χ, and finally mm/s for the velocity shifts.

## Reproduction target
Produce two output files:
- `/app/outputs/step_01_f_ratios.json` containing the two ratios f295_80 and f425_80 (dimensionless).
- `/app/outputs/step_02_shifts.json` containing the two shifts shift_80_295 and shift_295_425 (in mm/s).
These quantities are defined by the Debye-model formulas for κ=0 with the given parameters. The target is to compute them accurately; the hidden verifier will compare your numbers to benchmark values.

## Assets

- Physical constants for Fe-57 in Be

## Workflow steps

### Step 1: Compute Mössbauer fraction ratios
- Role: scored
- Action: Implement the Mössbauer fraction using f = exp( - (3R/(2 k_B Θ)) Λ(ξ) ) with Λ(ξ) as defined in the Approach section. Use Θ = 1160 K, M_Be = 9.012 u, m_Fe = 57 u, E_γ = 14.4 keV. Evaluate f at T = 80 K, 295 K, and 425 K, then compute the ratios f295_80 = f(295 K)/f(80 K) and f425_80 = f(425 K)/f(80 K) and write a JSON object with keys "f295_80" and "f425_80".
- Output file: `/app/outputs/step_01_f_ratios.json`
- Format: json
- Contract: {"f295_80": number (dimensionless ratio), "f425_80": number (dimensionless ratio)}
- Scoring: scored by hidden verifier

### Step 2: Compute temperature shifts of Mössbauer line
- Role: scored
- Action: Implement the temperature shift using χ(ξ) as defined in the Approach section. With Θ = 1160 K, M_Be = 9.012 u, m_Fe = 57 u, E_γ = 14.4 keV, compute δE at 80 K, 295 K, and 425 K, then take the differences ΔδE between 80→295 K and 295→425 K. Convert each ΔδE to mm/s via Δv = (ΔδE / E_γ) c. Write a JSON object with keys "shift_80_295" and "shift_295_425".
- Output file: `/app/outputs/step_02_shifts.json`
- Format: json
- Contract: {"shift_80_295": number (mm/s), "shift_295_425": number (mm/s)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_f_ratios.json`
- `/app/outputs/step_02_shifts.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_f_ratios.json
- path: `/app/outputs/step_01_f_ratios.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-computed ratios f(295K)/f(80K) and f(425K)/f(80K) for ⁵⁷Fe in Be under the Debye model. The hidden checker compares these values to the paper-reported results within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `f295_80`: number
    - `f425_80`: number

### step_02_shifts.json
- path: `/app/outputs/step_02_shifts.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-computed temperature shifts (in mm/s) for ⁵⁷Fe in Be between 80→295 K and 295→425 K. The hidden checker compares to the paper's values.
- schema:
  - `type`: object
  - `required`:
    - `shift_80_295`: number
    - `shift_295_425`: number

Notes: Both outputs are derived from the same physical constants and formulas. The agent must truncate the infinite sums appropriately. The hidden checker uses predetermined tolerances to decide correctness.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_f_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "f295_80": "number",
          "f425_80": "number"
        }
      },
      "description": "Agent-computed ratios f(295K)/f(80K) and f(425K)/f(80K) for ⁵⁷Fe in Be under the Debye model. The hidden checker compares these values to the paper-reported results within a tolerance."
    },
    {
      "file": "step_02_shifts.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "shift_80_295": "number",
          "shift_295_425": "number"
        }
      },
      "description": "Agent-computed temperature shifts (in mm/s) for ⁵⁷Fe in Be between 80→295 K and 295→425 K. The hidden checker compares to the paper's values."
    }
  ],
  "notes": "Both outputs are derived from the same physical constants and formulas. The agent must truncate the infinite sums appropriately. The hidden checker uses predetermined tolerances to decide correctness."
}
```

## How you are scored
Each scored step (step_01_f_ratios.json and step_02_shifts.json) is independently evaluated by an automated checker. The checker reads your JSON artifacts, compares the reported numbers to hidden reference values, and assigns a score for that step. The scores are combined (weighted) to produce a final reward between 0 and 1. You must implement the underlying physics; simply fabricating numbers that happen to match the paper's reported values is unlikely to succeed because the checker uses precise tolerances derived from the expected accuracy of a correct numerical implementation. The checker is concealed, so you cannot see the reference values or the tolerances. Do not attempt to hard-code answers—perform the computation as described.
