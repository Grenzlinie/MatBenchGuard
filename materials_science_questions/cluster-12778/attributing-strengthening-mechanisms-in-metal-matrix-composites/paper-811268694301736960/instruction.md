# Attributing Strengthening Mechanisms in Al-Zn-Mg-Cu Alloys: Predicting Yield Strength at 250 °C

## Problem background
Al-Zn-Mg-Cu alloys are used in applications requiring strength at elevated temperatures. Powder metallurgy (PM) processing with different oxygen contents can introduce varying amounts of nanoscale γ‑Al₂O₃ particles, which pin grain boundaries and dislocations, resulting in different grain sizes and different high‑temperature strengths. This task focuses on two PM Al-Zn-Mg-Cu alloy variants, labelled BL (0.15 wt% oxygen) and BM (0.33 wt% oxygen), after hot extrusion and heat treatment. The microstructural parameters of interest are their grain sizes (BL: 5.15 μm, BM: 3.16 μm) and the oxide particles (γ‑Al₂O₃, diameter ≤100 nm; we assume an effective diameter of 50 nm for calculation). Using classical strengthening models — Hall‑Petch grain boundary strengthening, Orowan dispersion strengthening from the γ‑Al₂O₃ particles, and a solid‑solution contribution — we can compute the predicted yield strength at 250 °C for each alloy. The goal of the computation is to attribute the strengthening to these mechanisms and to quantify the expected yield strengths.

## Approach
The predicted yield strength at 250 °C, σ_y, is built from three additive contributions:

1. **Hall‑Petch grain boundary strengthening**:  
   σ_HP = k_HP / √d, where d is the average grain diameter (m). Use the Hall‑Petch coefficient k_HP = 0.12 MPa·m^{1/2}.

2. **Orowan dispersion strengthening** from the γ‑Al₂O₃ particles:  
   First, estimate the oxide volume fraction f from the oxygen content using the relation  
   f = (ρ_Al / ρ_Al₂O₃) × (M_Al₂O₃ / (3 M_O)) × (wt% oxygen / 100),  
   with ρ_Al = 2.70 g cm⁻³, ρ_Al₂O₃ = 3.95 g cm⁻³, M_Al₂O₃ = 101.96 g mol⁻¹ and M_O = 16.00 g mol⁻¹.  
   Then compute the Orowan strengthening increment (in MPa) as  
   σ_Or = (0.81 G b M) / (2π √(1−ν)) × (1 / λ) × ln(d_p / b),  
   where λ = d_p (√(π/(6f)) − 1) is the effective inter‑particle spacing (m), d_p = 50 nm, G = 26.4 GPa (shear modulus at 250 °C), b = 0.286 nm (Burgers vector), M = 3.06 (Taylor factor), ν = 0.33 (Poisson’s ratio). The result is in Pa; convert to MPa.

3. **Solid‑solution strengthening**:  
   Because the two alloys have essentially the same nominal composition (Zn, Mg, Cu), the solid‑solution contribution is considered identical and is taken as a constant σ_ss = 25 MPa.

Total predicted yield strength: σ_y = σ_HP + σ_Or + σ_ss (MPa).  
All required parameters are listed above; no further data lookup is needed. Implement these equations for the BL (d = 5.15 μm, oxygen 0.15 wt%) and BM (d = 3.16 μm, oxygen 0.33 wt%) variants.

## Reproduction target
Compute the predicted yield strength at 250 °C for both the BL and BM alloys using the strengthening models and constants described in the Approach. Sum the contributions from Hall‑Petch grain boundary strengthening, Orowan dispersion strengthening, and the fixed solid‑solution contribution of 25 MPa. Write the two resulting values (in MPa) to a CSV file with columns 'alloy' (containing the strings 'BL' or 'BM') and 'predicted_YS_MPa' (the predicted yield strength as a float). Exactly two rows are expected. The output file must be written to `/app/outputs/predicted_strengths_250C.csv`.

## Assets

- Standard material constants for Al alloys

## Workflow steps

### Step 1: Calculate predicted yield strengths
- Role: scored (load-bearing)
- Action: Using the provided microstructural parameters (grain sizes: BL 5.15 μm, BM 3.16 μm; oxygen contents: BL 0.15 wt%, BM 0.33 wt%; γ‑Al₂O₃ particles, assume effective diameter 50 nm) and the supplied standard material constants, compute the yield strength contributions at 250 °C from Hall‑Petch grain boundary strengthening, Orowan dispersion strengthening, and solid solution strengthening from Zn, Mg, Cu. Sum the contributions to obtain the total predicted yield strength for each alloy. Write the two values to a CSV file with columns alloy and predicted_YS_MPa.
- Output file: `/app/outputs/predicted_strengths_250C.csv`
- Format: csv
- Contract: CSV with columns: alloy (string, 'BL' or 'BM'), predicted_YS_MPa (float). Exactly two rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_strengths_250C.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_strengths_250C.csv
- path: `/app/outputs/predicted_strengths_250C.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Predicted yield strength at 250 °C for BL and BM Al-Zn-Mg-Cu alloys; the hidden checker compares these against the paper-reported experimental values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `predicted_YS_MPa`
  - `units`:
    - `predicted_YS_MPa`: MPa

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_strengths_250C.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "predicted_YS_MPa"
        ],
        "units": {
          "predicted_YS_MPa": "MPa"
        }
      },
      "description": "Predicted yield strength at 250 °C for BL and BM Al-Zn-Mg-Cu alloys; the hidden checker compares these against the paper-reported experimental values with tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted CSV file will be evaluated by a hidden verifier against the correct computed predictions (derived from the same equations and constants). The verifier compares the two predicted yield strength values in your file with the expected values, using a narrow relative tolerance to account for minor floating‑point differences. Credit is proportional to the closeness of your values to the expected ones; perfect agreement within tolerance earns full credit for this stage. No other artifacts are scored for this task. The scoring is fully automatic and does not require manual inspection.
