# Ausforming Strength Contribution Calculation

## Problem background
Ausforming—deforming metastable austenite prior to quenching—can increase the yield strength of a Cr-Mo-V steel. The strengthening arises from three effects: increased dislocation density, a more effective dispersion of alloy carbides, and a loss of interstitial solid solution strengthening due to carbon depletion (carbon is consumed to form carbides). The task is to compute each contribution and their combined effect on the tensile yield strength increment, using the mechanistic superposition model described below.

## Approach
The yield strength of martensite can be written as the sum of three shear‑stress contributions:

```
(1)  τ_ρ   = α₁ μ b ρ^(1/2)       (dislocation strengthening)
(2)  τ_λ   = α₂ μ b (1/λ)         (precipitate strengthening)
(3)  τ_f   = (α₃ / (b a₀³)) f     (interstitial solid‑solution strengthening)
```

For a 25 % rolling deformation of austenite at 1000 °F prior to quenching, experiments measured the following changes in substructural parameters:

- Δ(ρ^(1/2)) = 0.32 × 10⁶ cm⁻¹
- Δ(1/λ)     = 0.23 × 10⁶ cm⁻¹

The corresponding change in the atom fraction of interstitial carbon, Δf, is not directly measured. It is estimated from the observed increase in the martensite start temperature, ΔM_s = 65 °F, using the empirical relation:

```
ΔM_s (°F) = 650 × Δ(wt% C) + 70 × Δ(wt% Cr) + 50 × Δ(wt% Mo)
```

The strain‑induced precipitates are assumed to be alloy carbides of type **M₂C**, where **M** denotes the carbide‑forming elements Cr and Mo. Furthermore, the atomic ratio of Cr to Mo in the precipitated M₂C is assumed to be the same as in the original alloy. This assumption, together with the stoichiometry of M₂C, allows us to express the weight‑percent changes Δ(wt% Cr) and Δ(wt% Mo) as functions of Δ(wt% C) alone.

After Δ(wt% C) is computed, it is converted to the change in interstitial atom fraction, Δf, and then used in equation (3) to obtain Δτ_f. Equations (1) and (2) directly use the given Δ(ρ^(1/2)) and Δ(1/λ). The coefficients α₁ and α₂ are each in the range 0.3 to 0.4; compute each increment for both extremes (α=0.3 giving the lower bound and α=0.4 the upper bound). The coefficient α₃ = 38 × 10⁻²⁰ dyn·cm².

**Physical constants and conversion factors (use consistent cgs units):**

- μ  = 8.25 × 10¹¹ dyn/cm²
- b  = 2.48 Å = 2.48 × 10⁻⁸ cm
- a₀ = 2.87 Å = 2.87 × 10⁻⁸ cm
- 1 ksi = 6.89476 × 10⁷ dyn/cm²   (i.e. 1 dyn/cm² ≈ 1.45038 × 10⁻⁸ ksi)

**Alloy composition (weight percent of the Cr‑Mo‑V steel):**

| Element | wt%  |
|---------|------|
| C       | 0.39 |
| Cr      | 5.08 |
| Mo      | 1.40 |
| V       | 0.54 |
| Mn      | 0.26 |
| Si      | 0.98 |
| P       | 0.011|
| S       | 0.008|
| Fe      | balance |

**Atomic masses (g/mol) to be used:**

- C: 12.01, Cr: 52.00, Mo: 95.95, Fe: 55.85, V: 50.94, Mn: 54.94, Si: 28.09, P: 30.97, S: 32.06

## Reproduction target
Compute Δτ_ρ, Δτ_λ, and Δτ_f (in both dyn/cm² and ksi) for the two coefficient extremes, their sum, and the tensile yield strength increment Δσ = 2 × Δτ_sum. Write the resulting ranges to `contributions.csv` with columns: `contribution` (string), `dyn_per_cm2_min`, `dyn_per_cm2_max`, `ksi_min`, `ksi_max`. Rows: `delta_tau_rho`, `delta_tau_lambda`, `delta_tau_f`, `sum`, `tensile_yield_increment`.

## Assets
No external datasets, models, or special software are needed. All required constants and formulas are stated above. A standard Python 3 environment with built‑in `csv` and `math` modules is sufficient.

## Workflow steps

### Step 1: Compute ausforming strength contributions
- **Role:** scored
- **Action:**
  1. **Determine the depletion of carbon Δ(wt% C)**
     - From the empirical M_s relation, ΔM_s = 65 °F.
     - Using the alloy composition, calculate the atom (molar) fractions of Cr and Mo among the M atoms.
       - In 100 g of alloy, compute moles of Cr and Mo:
         n_Cr = 5.08 / 52.00, n_Mo = 1.40 / 95.95.
       - x_Cr = n_Cr / (n_Cr + n_Mo), x_Mo = 1 – x_Cr.
     - From the stoichiometry M₂C: for every 1 mole of carbon consumed, 2 moles of metal M are consumed. Hence, in weight‑percent terms:
       ```
       Δ(wt% Cr) = (2 × 52.00 / 12.01) × x_Cr × Δ(wt% C)
       Δ(wt% Mo) = (2 × 95.95 / 12.01) × x_Mo × Δ(wt% C)
       ```
     - Substitute these expressions into the ΔM_s equation and solve for Δ(wt% C). (Solve the linear equation algebraically, retaining full precision.)

  2. **Convert Δ(wt% C) to the change in interstitial atom fraction Δf**
     - For 100 g of the original alloy, compute the total number of moles `n_total` by summing the moles of all elements (use the balance Fe; Fe mass = 100 – sum of all other given masses).
     - The change in the number of moles of carbon is Δn_C = Δ(wt% C) / 12.01.
     - Then Δf = Δn_C / n_total (neglect the tiny change in total moles due to precipitation).

  3. **Calculate the three shear‑stress increments in dyn/cm²**
     - Use the equations at the top.
     - For α₁ and α₂, compute the lower bound using 0.3 and the upper bound using 0.4.
     - α₃ is constant.
     - `Δτ_f` will be negative because carbon is removed from solid solution.

  4. **Compute the net shear stress increment and tensile yield increment**
     - Sum the three Δτ values for each α extreme → Δτ_sum_min, Δτ_sum_max.
     - Tensile yield strength increment: Δσ_min = 2 × Δτ_sum_min, Δσ_max = 2 × Δτ_sum_max.
     - Convert all dyn/cm² values to ksi using the factor 1.45038 × 10⁻⁸ ksi per dyn/cm².

  5. **Write the output**
     - Create the CSV file `/app/outputs/contributions.csv` with the exact columns and rows specified. Provide the numeric values computed in the previous steps; do **not** simply copy known results from the literature.
- **Output file:** `/app/outputs/contributions.csv`
- **Format:** csv
- **Contract:** Columns: `contribution` (string), `dyn_per_cm2_min` (float), `dyn_per_cm2_max` (float), `ksi_min` (float), `ksi_max` (float). Rows: `delta_tau_rho`, `delta_tau_lambda`, `delta_tau_f`, `sum`, `tensile_yield_increment`.
- **Scoring:** scored by hidden verifier

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
- description: Ausforming strength contributions: Δτ_ρ (dislocation density), Δτ_λ (particle spacing), Δτ_f (interstitial loss), their sum, and the tensile yield increment Δσ = 2×sum.
- schema:
  - `type`: table
  - `required_columns`: `contribution`, `dyn_per_cm2_min`, `dyn_per_cm2_max`, `ksi_min`, `ksi_max`
  - `description`: Each row gives the name of the contribution, and the computed minimum and maximum values in dyn/cm² and ksi.

## Self-check before finishing (optional, not scored)
A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, and CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

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
      "description": "Ausforming strength contributions: Δτ_ρ (dislocation density), Δτ_λ (particle spacing), Δτ_f (interstitial loss), their sum, and the tensile yield increment Δσ = 2×sum."
    }
  ],
  "notes": "All input constants and formulas are given in the step. The scores will be compared against the paper‑reported ranges with a reasonable tolerance."
}
```

## How you are scored
A hidden verifier reads your `contributions.csv` and compares the reported minimum and maximum values to reference ranges. The evaluation rewards computed ranges that fall within a reasonable tolerance of the expected values; merely printing the expected numbers without correct computation will not produce the correct ranges. Each sub‑contribution and the total tensile increment contribute to the final score.