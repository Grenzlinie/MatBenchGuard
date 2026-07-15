# Ausforming Strength Contribution Calculation

## Problem background
Ausforming—deforming metastable austenite prior to quenching—can increase the yield strength of a Cr-Mo-V steel. The paper partitions this increase into three contributions: increased dislocation density, increased dispersion of alloy carbides, and loss of interstitial solid solution strengthening due to carbon depletion. The task is to compute the magnitude of each contribution and their combined effect on the tensile yield strength increment.

## Approach
Based on Conrad's equations, the shear stress contribution from dislocations is proportional to the square root of dislocation density, from precipitated particles is proportional to the inverse of inter-particle spacing, and from interstitials is proportional to the atom fraction of interstitial carbon. The paper reports the measured changes in dislocation density and particle spacing after ausforming, and estimates the depletion of carbon from the observed increase in martensite start temperature using an empirical relation that links Ms shift to changes in carbon and alloy content. Using given materials constants (shear modulus, Burgers vector, lattice parameter, interaction constants), compute each shear stress increment for both the lower and upper bounds of the dislocation/particle strengthening coefficients (α). Sum the three increments and convert the total shear stress increase to a tensile yield strength increment Δσ via the factor 2.

## Reproduction target
Compute Δτρ, Δτλ, Δτf (in dyn/cm² and ksi) for the two coefficient extremes, their sum, and the tensile yield strength increment Δσ = 2 × sum. Write the resulting ranges to contributions.csv with columns: contribution (string), dyn_per_cm2_min, dyn_per_cm2_max, ksi_min, ksi_max. Rows: delta_tau_rho, delta_tau_lambda, delta_tau_f, sum, tensile_yield_increment.

## Assets
No external datasets, models, or special software are needed. All required physical constants and substructural parameter values are stated in the task description. A standard Python 3 environment with built‑in csv and math modules is sufficient.

## Workflow steps

### Step 1: Compute ausforming strength contributions
- Role: scored
- Action: Compute the change in interstitial carbon atom fraction Δf from the given Ms temperature increase (65°F) and alloy composition (0.39C-5.08Cr-1.40Mo-0.54V-0.26Mn-0.98Si-0.011P-0.008S, in wt%) using the empirical relation ΔMs(°F)=650×Δ(wt% C) + 70×Δ(wt% Cr) + 50×Δ(wt% Mo) and convert to atom fraction. Then compute the three shear stress contributions using Conrad's equations: Δτρ = α1 μ b Δ(ρ^1/2), Δτλ = α2 μ b Δ(1/λ), and Δτf = (α3 / (b a0^3)) Δf. Use μ=8.25×10^11 dyn/cm², b=2.48 Å, a0=2.87 Å, α3=38×10^{-20} dyn·cm², Δ(ρ^1/2)=0.32×10^6 cm^{-1}, Δ(1/λ)=0.23×10^6 cm^{-1}. For α1 and α2, use the range [0.3, 0.4] to produce minimum and maximum values. Sum the three increments and multiply by 2 to obtain the tensile yield strength increment Δσ. Write the computed ranges (in dyn/cm² and ksi) to contributions.csv.
- Output file: `/app/outputs/contributions.csv`
- Format: csv
- Contract: Columns: contribution (string), dyn_per_cm2_min (float), dyn_per_cm2_max (float), ksi_min (float), ksi_max (float). Rows: delta_tau_rho, delta_tau_lambda, delta_tau_f, sum, tensile_yield_increment.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/contributions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### contributions.csv
- path: `/app/outputs/contributions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ausforming strength contributions: Δτρ (dislocation density), Δτλ (particle spacing), Δτf (interstitial loss), their sum, and the tensile yield increment Δσ = 2×sum.
- schema:
  - `type`: table
  - `required_columns`: `contribution`, `dyn_per_cm2_min`, `dyn_per_cm2_max`, `ksi_min`, `ksi_max`
  - `description`: Each row gives the name of the contribution, and the computed minimum and maximum values in dyn/cm² and ksi.

Notes: All input constants and formulas are given in the step. The scores will be compared against the paper-reported ranges with a reasonable tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "contributions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "contribution",
          "dyn_per_cm2_min",
          "dyn_per_cm2_max",
          "ksi_min",
          "ksi_max"
        ],
        "description": "Each row gives the name of the contribution, and the computed minimum and maximum values in dyn/cm² and ksi."
      },
      "description": "Ausforming strength contributions: Δτρ (dislocation density), Δτλ (particle spacing), Δτf (interstitial loss), their sum, and the tensile yield increment Δσ = 2×sum."
    }
  ],
  "notes": "All input constants and formulas are given in the step. The scores will be compared against the paper-reported ranges with a reasonable tolerance."
}
```

## How you are scored
A hidden verifier reads your contributions.csv and compares the reported minimum and maximum values to reference ranges derived from the paper's analysis. The evaluation rewards computed ranges that fall within a reasonable tolerance of the expected values; merely printing the expected numbers without correct computation will not produce the correct ranges. Each sub‑contribution and the total tensile increment contribute to the final score.
