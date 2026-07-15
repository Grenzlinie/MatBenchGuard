# Superconducting Critical Temperature and Isotope Effect in Alkali-Doped C60: Combined Phonon-Bond-Polarization Model

## Problem background
Alkali-doped C60 superconductors, such as K3C60 and Rb3C60, show a remarkable pressure dependence of their superconducting critical temperature Tc, isotope effect coefficient α, energy gap ratio β = 2Δ/(k_B T_c), and pressure derivative dTc/dP. The experimentally observed Tc decreases with increasing pressure, and the measured isotope effect coefficient is substantially smaller than the BCS value, suggesting that a purely phonon-mediated pairing mechanism may not be the only operative channel. A combined mechanism that includes, in addition to conventional phonon-mediated pairing, a high-energy electronic pairing arising from bond polarization within the C60 molecules has been proposed. The resulting model yields analytical predictions for Tc, α, β, and dTc/dP as functions of pressure. Your task is to compute these predicted quantities using the model’s formulation and given parameters, outputting the numerical predictions for a suite of pressure points for both systems.

## Approach
The pairing is assumed to originate from two additive contributions: a conventional electron–phonon interaction characterised by a coupling constant λ_ph and Debye temperature θ_D, and a higher-energy electronic mechanism from bond polarization with coupling constant λ_bp and characteristic energy θ_bp. The bond-polarization channel is renormalised because the pairing interaction extends to energies beyond the Debye scale. This renormalisation leads to an effective bond-polarisation coupling λ*_bp. The critical temperature Tc follows a modified BCS-like exponential expression that depends on the sum λ*_bp + λ_ph. From Tc, the isotope effect coefficient α, the energy gap ratio β, and the pressure derivative dTc/dP are obtained via closed‑form formulas derived from the theory. The pressure dependence is introduced by assuming that both coupling constants decrease exponentially with pressure: λ(P) = λ(0)·exp(–A·P), where the constant A is determined from the high‑pressure Tc data for each system. You will implement these analytical expressions using the numerical parameters provided in the workflow step, compute Tc, α, β, and dTc/dP for K3C60 and Rb3C60 at the specified pressure grid, and save the table of predicted properties.

## Reproduction target
Compute the predicted superconducting critical temperature Tc (K), isotope effect coefficient α, energy gap ratio β, and pressure derivative dTc/dP (K/GPa) for K3C60 and Rb3C60 at the pressure points listed in the workflow step. Write the results to a CSV file with columns: system, pressure_GPa, Tc_K, alpha, beta, dTc_dP_K_GPa. The file must contain the exact rows for all specified pressures in increasing pressure order for each system. No other outputs are required.

## Assets
No external datasets, model weights, or tools are required. All necessary parameters and formulas are provided directly in the workflow step below. A Python environment with standard libraries (e.g., numpy, pandas) is sufficient to carry out the computation.

## Workflow steps

### Step 1: Compute Tc, alpha, beta, dTc/dP for K3C60 and Rb3C60
- Role: scored
- Action: Implement the analytical expressions from the combined phonon-mediated and bond-polarization pairing model to compute the superconducting critical temperature Tc, isotope effect coefficient α, energy gap ratio β = 2Δ/(k_B T_c), and pressure derivative dTc/dP for K3C60 and Rb3C60 at multiple pressures. Use the given parameters: Debye temperature θ_D = 80 K, bond-polarization characteristic energy θ_bp = 3000 K; zero-pressure coupling constants λ_ph(0)=0.2575 and λ_bp(0)=0.1609 for K3C60, λ_ph(0)=0.4355 and λ_bp(0)=0.1715 for Rb3C60. The pressure-dependent coupling constants follow λ(P) = λ(0) * exp(-A*P), with A = 0.14091 for K3C60 and A = 0.1936 for Rb3C60. First compute the renormalised bond-polarization coupling λ*_bp = λ_bp / (1 - λ_bp * ln(θ_bp/θ_D)). Then the critical temperature is Tc = 1.14 * θ_D * exp(-1/(λ*_bp + λ_ph)). The isotope effect coefficient is α = 0.5 * [1 - (1 + λ_ph * ln(Tc/(1.14*θ_D)))^2]. The energy gap ratio is β = 4 / (1.14 - Tc/θ_D). The pressure derivative is dTc/dP = -A * Tc * [ln(1.14*θ_D/Tc) + (1-2α) * ln(θ_bp/θ_D)]. Compute these quantities for the pressure points: K3C60 at P = 0.0, 0.08, 0.33, 0.68, 1.02, 2.33 GPa; Rb3C60 at P = 0.0, 0.18, 0.58, 1.03, 1.50, 1.92 GPa. Write the results to a CSV file with columns: system, pressure_GPa, Tc_K, alpha, beta, dTc_dP_K_GPa, in increasing pressure order for each system.
- Output file: `/app/outputs/calculated_properties.csv`
- Format: csv
- Contract: CSV with columns: system (string, 'K3C60' or 'Rb3C60'), pressure_GPa (float), Tc_K (float), alpha (float), beta (float), dTc_dP_K_GPa (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_properties.csv
- path: `/app/outputs/calculated_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed superconducting properties: critical temperature Tc (K), isotope effect coefficient α, gap ratio β, and pressure derivative dTc/dP (K/GPa) for K3C60 and Rb3C60 at the specified pressures.
- schema:
  - `type`: table
  - `required_columns`: `system`, `pressure_GPa`, `Tc_K`, `alpha`, `beta`, `dTc_dP_K_GPa`
  - `units`:
    - `pressure_GPa`: GPa
    - `Tc_K`: K
    - `dTc_dP_K_GPa`: K/GPa

Notes: All required parameters are provided in the step; no external data retrieval is needed. The checker compares each entry against the hidden gold values from the paper's Tables 1 and 2 using a small absolute and relative tolerance to absorb floating-point rounding.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "pressure_GPa",
          "Tc_K",
          "alpha",
          "beta",
          "dTc_dP_K_GPa"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "Tc_K": "K",
          "dTc_dP_K_GPa": "K/GPa"
        }
      },
      "description": "Computed superconducting properties: critical temperature Tc (K), isotope effect coefficient α, gap ratio β, and pressure derivative dTc/dP (K/GPa) for K3C60 and Rb3C60 at the specified pressures."
    }
  ],
  "notes": "All required parameters are provided in the step; no external data retrieval is needed. The checker compares each entry against the hidden gold values from the paper's Tables 1 and 2 using a small absolute and relative tolerance to absorb floating-point rounding."
}
```

## How you are scored
Your submitted CSV file will be evaluated by a hidden verifier. For each system (K3C60 or Rb3C60) and each pressure, the verifier compares your computed Tc, α, β, and dTc/dP to the correct model predictions, which are not disclosed. Entries that fall within a tight numerical tolerance (accounting for minor floating‑point rounding) are considered correct. The overall score is proportional to the fraction of entries that match within tolerance, with a higher weight assigned to the Tc values. The verifier does not provide feedback on which entries passed; only the final score is returned. You must therefore compute each quantity exactly as described in the workflow steps, using the given parameters. Simply writing down a plausible estimate or copying numbers from elsewhere will not succeed unless they genuinely match the expected predictions.
