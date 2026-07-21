# Divacancy Contribution to Resistivity Increase in Metals

## Problem background
Point defects such as simple vacancies (single missing atoms) and divacancies (pairs of adjacent vacancies) exist in all crystals and can significantly affect electrical properties, especially at high temperatures or in quenched samples. This task focuses on the temperature‑dependent part of the electrical resistivity caused by electron‑phonon scattering in a metal containing both types of defects. The goal is to quantify how much of the total increase in resistivity comes from divacancies alone, relative to the contribution from simple vacancies, under two distinct temperature regimes (high and low, separated by the Debye temperature).

## Approach
The analysis uses analytic expressions for two types of electron‑phonon scattering contributions to resistivity: one that conserves quasimomentum (ρ₁) and one that does not (ρ₂). These formulas give the increase in resistivity over the defect‑free crystal in terms of the simple‑vacancy concentration x_h and the divacancy concentration x_b. You will fix the concentration ratio x_b / x_h = 0.1 and examine two temperature regimes: T > Θ (high temperature) and T < Θ (low temperature), where Θ is the Debye temperature. For each regime, isolate the total resistivity increase (summing appropriate ρ₁ and ρ₂ terms) and the part coming solely from divacancies. Simplify these quantities to expressions that depend only on the ratio x_b/x_h, then evaluate the percentage contribution of divacancies to the total increase in both regimes.

## Reproduction target
Write a script that implements the resistivity formulas, uses the concentration ratio x_b = 0.1 x_h, and computes the percentage contribution of divacancies to the total resistivity increase separately for high‑temperature (T > Θ) and low‑temperature (T < Θ) conditions. Save the two percentages as a JSON file with the keys "high_temperature_percent" and "low_temperature_percent".

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Compute Divacancy Contribution Percentages
- Role: scored
- Action: Implement the resistivity formulas explicitly. For T > Θ (high T): ρ₁(T)=ρ₀(T), ρ₂(T)=[100(x_h+2x_b)+60x_b]ρ₀(T). For T < Θ (low T): ρ₁(T)=[1+6(x_h+4x_b)]ρ₀(T), ρ₂(T)=5(x_h+4x_b)(Θ/T)^3ρ₀(T). ρ₀(T) is the defect‑free resistivity and cancels when computing the increase Δρ = (ρ₁−ρ₀)+ρ₂. High‑T: Δρ = ρ₂, so Δρ = [100x_h + 260x_b]ρ₀(T). The divacancy part Δρ_div = 260x_b ρ₀(T). Percentage = (260x_b) / (100x_h + 260x_b) × 100. Low‑T: the (Θ/T)^3 term dominates, so Δρ ≈ ρ₂ = 5(x_h+4x_b)(Θ/T)^3 ρ₀(T). Δρ_div = 20x_b (Θ/T)^3 ρ₀(T). Percentage = (20x_b) / (5(x_h+4x_b)) × 100 = (4x_b) / (x_h+4x_b) × 100. Set x_b/x_h=0.1 and evaluate. Write the two percentages to JSON.
- Output file: `/app/outputs/divacancy_contributions.json`
- Format: json
- Contract: {"high_temperature_percent": <float>, "low_temperature_percent": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/divacancy_contributions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### divacancy_contributions.json
- path: `/app/outputs/divacancy_contributions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Divacancy contribution percentages to the total resistivity increase at high temperature (T>Θ) and low temperature (T<Θ).
- schema:
  - `type`: object
  - `required`:
    - `high_temperature_percent`: number
    - `low_temperature_percent`: number

Notes: The checker recomputes the expected percentages from the paper's analytic formulas using the same concentration ratio and compares with a tolerance of ±1 percentage point.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "divacancy_contributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "high_temperature_percent": "number",
          "low_temperature_percent": "number"
        }
      },
      "description": "Divacancy contribution percentages to the total resistivity increase at high temperature (T>Θ) and low temperature (T<Θ)."
    }
  ],
  "notes": "The checker recomputes the expected percentages from the paper's analytic formulas using the same concentration ratio and compares with a tolerance of ±1 percentage point."
}
```

## How you are scored
A hidden verifier will independently recompute the expected percentages from the same analytic formulas and the same concentration ratio. Your submitted percentages are compared to those expected values. Full credit is awarded when your numbers fall within an allowed tolerance; partial credit is given based on how many of the two results are within tolerance. The verifier combines the scores of all workflow stages to produce a final reward in the range 0 to 1.
