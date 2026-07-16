# Hydrogen Bubble Equilibrium Radius in Aluminum via Classical Nucleation Theory

## Problem background
Hydrogen gas dissolved in aluminum can precipitate into bubbles, causing embrittlement and reducing the material’s lifetime. Predicting the equilibrium size of such bubbles from thermodynamic parameters is essential for understanding and mitigating these effects. This task computes the equilibrium radius of a hydrogen bubble in aluminum at room temperature using a microscopic thermodynamic model based on classical nucleation theory. The result is a deterministic numerical prediction that can be compared with experimental observations.

## Approach
Hydrogen is treated as an ideal diatomic gas (ν = 0.5) inside a spherical cavity. The calculation proceeds in the following steps, using the supplied material constants and experimental conditions.

**Material constants and parameters**
- Surface tension (inside grain): σ = 1.200 N·m⁻¹
- Solubility pre‑factor: n_s⁰ = 2.20 × 10⁻³ mol % = 2.20 × 10⁻⁵ mole fraction (dimensionless)
- Binding energy: ε = 0.6027 eV
- Ambient pressure: p⁰ = 1 atm (the formula expects pressure in atm; do not convert to Pa).
- Temperature: T = 300 K
- Total hydrogen concentration: N_total = 2 × 10²³ m⁻³
- Bubble density: ρ_bub = 10¹³ m⁻³ (typical for commercial aluminium)
- Gas stoichiometric factor: ν = 0.5 (diatomic gas)
- Physical constants: Boltzmann constant k_B = 1.380649 × 10⁻²³ J K⁻¹ = 8.617333262145 × 10⁻⁵ eV K⁻¹

**Step‑by‑step formulas**

1. **Threshold radius** (Eq. 6 of the underlying theory):
   r_b^* = 2 × [ ( 3 ν² n_s⁰ (k_B T)^ν e^{-ε/(k_B T)} ) / ( 64 π (p⁰)^ν σ^{1-ν} ) ]^{1/(ν+2)}.
   Compute r_b^* in metres, then convert to micrometres (1 m = 10⁶ µm).

2. **Threshold number of gas molecules per bubble** (Eq. 6):
   n_b^* = (8 π / 3) × (σ / (k_B T)) × (r_b^*)².
   (Use k_B T in joules, so σ/(k_B T) has units m⁻¹.)

3. **Threshold concentration per unit volume**:
   n_t^* (per bubble) = ((ν+2)/ν²) × n_b^*,
   N_t^* = ρ_bub × n_t^*   (atoms m⁻³).

4. **Supersaturation**:
   Δ = (N_total − N_t^*) / N_t^*.

5. **Stationary‑radii relation** (Eq. 7):
   Δ + 1 = (ν/(ν+2)) × x² + (2/(ν+2)) × x^{-ν},
   where x = r_eq / r_b^*.
   Solve this equation numerically for the equilibrium (larger) root x > 1. For ν = 0.5 the exponents become x² and x^{-0.5}.

6. **Equilibrium radius**:
   r_eq = x × r_b^*,
   convert to micrometres and record the ratio x.

**Output**: the three quantities r_b_star_um (µm), ratio_r_eq_over_r_b_star (dimensionless), and r_eq_um (µm) are written to the JSON file as specified.

## Reproduction target
Compute the threshold radius r_b* in µm, the dimensionless ratio r_eq / r_b*, and the absolute equilibrium radius r_eq in µm for hydrogen bubbles in aluminum at 300 K. Write the results to the output file `bubble_calculation.json` as specified in the workflow steps.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute hydrogen bubble threshold and equilibrium radii in aluminum
- Role: scored
- Action: Using the classical nucleation theory threshold formulas for a diatomic ideal gas (ν=0.5), material surface tension σ=1.200 N/m (inside grain), solubility pre-factor n_s^0 = 2.20×10^{-3} mol%, binding energy ε=0.6027 eV, ambient pressure p^0=1 atm, temperature 300 K, total hydrogen concentration N_total = 2×10^{23} m^{-3}, and bubble density 10^{13} m^{-3}: compute the threshold radius r_b*, the ratio r_eq / r_b* from the stationary radii relation, and the absolute equilibrium radius r_eq in µm. Write these three values (r_b_star_um, ratio_r_eq_over_r_b_star, r_eq_um) to bubble_calculation.json.
- Output file: `/app/outputs/bubble_calculation.json`
- Format: json
- Contract: { "r_b_star_um": <float>, "ratio_r_eq_over_r_b_star": <float>, "r_eq_um": <float>, "units": "µm for radii, dimensionless for ratio" }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bubble_calculation.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bubble_calculation.json
- path: `/app/outputs/bubble_calculation.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Hydrogen bubble radii computed from provided material constants and parameters. The checker compares the submitted values to hidden paper-reported references within tolerance.
- schema:
  - `type`: object
  - `required`: `r_b_star_um`, `ratio_r_eq_over_r_b_star`, `r_eq_um`
  - `properties`:
    - `r_b_star_um`:
      - `type`: number
      - `description`: Threshold radius in µm
    - `ratio_r_eq_over_r_b_star`:
      - `type`: number
      - `description`: Ratio of equilibrium radius to threshold radius (dimensionless)
    - `r_eq_um`:
      - `type`: number
      - `description`: Equilibrium radius in µm

Notes: The calculation uses only provided constants and publicly known formulas; no external data or training is required. The three quantities must be self-consistent (r_eq_star = ratio * r_b_star).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bubble_calculation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "r_b_star_um",
          "ratio_r_eq_over_r_b_star",
          "r_eq_um"
        ],
        "properties": {
          "r_b_star_um": {
            "type": "number",
            "description": "Threshold radius in µm"
          },
          "ratio_r_eq_over_r_b_star": {
            "type": "number",
            "description": "Ratio of equilibrium radius to threshold radius (dimensionless)"
          },
          "r_eq_um": {
            "type": "number",
            "description": "Equilibrium radius in µm"
          }
        }
      },
      "description": "Hydrogen bubble radii computed from provided material constants and parameters. The checker compares the submitted values to hidden paper-reported references within tolerance."
    }
  ],
  "notes": "The calculation uses only provided constants and publicly known formulas; no external data or training is required. The three quantities must be self-consistent (r_eq_star = ratio * r_b_star)."
}
```

## How you are scored
A hidden verifier reads your `bubble_calculation.json` and independently checks each of the three values against the correct results derived from the theoretical model. It also verifies that the reported numbers are self‑consistent (r_eq = ratio × r_b*). Each stage carries a weight, and your final score is the weighted sum of the stage‑level scores. To succeed you must faithfully implement the calculation as described; simply reporting a number without a genuine computation will not yield a high score.
