# Classical Nucleation Theory for Dropwise Condensation: Critical Nucleus Size and Heat Transfer Coefficient

## Problem background
Dropwise condensation of steam on a cooled metal surface can achieve much higher heat transfer coefficients than filmwise condensation because the condensate does not form an insulating liquid film. However, the process is limited by the need to nucleate liquid droplets on the non‑wettable surface. Classical nucleation theory provides a framework to determine the smallest viable droplet radius (critical nucleus) and the temperature drop (undercooling) required before stable droplets can form. Once nucleation occurs, the heat transfer is governed by the kinetic gas‑theory limited arrival rate of vapor molecules (the phase‑transition coefficient) and by the fraction of surface covered by growing droplets. The cover fraction and the growth dynamics depend on the temperature difference, the wall height, the surface roughness, and the promoter that makes the surface hydrophobic. This task reproduces the theoretical pipeline that combines these elements to compute the critical nucleus size and the mean heat transfer coefficient for a specific promoter/surface combination.

## Approach
The reproduction follows two stages. First, classical nucleation theory is applied to water at 100 °C. The Thomson–Kelvin relation gives the vapor‑pressure increase over a curved droplet surface, and the Clausius–Clapeyron equation converts that pressure increase into a required undercooling as a function of droplet radius. The work required to create a droplet of radius r is computed from surface and volume energies, taking a contact angle of 90°. The nucleation frequency I(r) is then proportional to exp(‑A/kT), multiplied by an attempt frequency of about 10²⁶ s⁻¹. The critical nucleus radius r_crit is the radius that maximizes I(r), and the corresponding undercooling is ΔT_nucl. All quantities are expressed in SI units.

Second, the mean heat‑transfer coefficient α_m is computed from a semi‑empirical model. The phase‑transition coefficient α_p is given by kinetic theory (α_p ∝ s²·P/(T³·√T), with condensation coefficient f = 0.045) and represents the maximum possible heat transfer to a bare surface. For a real surface partially covered by droplets, the effective coefficient is reduced by a factor (1−φ). For the copper‑plus‑stearic‑acid promoter at 1 atm, the combined factor f(1−φ) is taken as 0.016. Droplet run‑off and interference further reduce the mean coefficient according to α_m = α_p (1−φ) [1 − K H α_p ΔT], where K = 5×10⁻⁶ m·h/kcal and H = 0.019 m. For temperature differences smaller than ΔT_nucl, no stable droplets exist and α_m is set to zero. The model is evaluated for ΔT from 0.5 °C to 10 °C in 0.5 °C steps, and all results are converted to SI units (W/(m²·K) for α_m, K for ΔT).

## Reproduction target
Produce two artifacts:
1. `nucleation.csv` – the critical nucleus radius `r_crit` (meters) and the corresponding undercooling `ΔT_nucl` (Kelvin) for water at 100 °C, using the described nucleation theory with a contact angle of 90° and an attempt frequency of 10²⁶ s⁻¹.
2. `heat_transfer.csv` – the mean heat transfer coefficient `α_m` (W/(m²·K)) as a function of temperature difference `ΔT` (K) for the copper+stearic‑acid promoter at 1 atm and H = 0.019 m. Evaluate ΔT from 0.5 K to 10 K in 0.5 K steps, using the undercooling threshold from nucleation.csv and the model above. The resulting α_m(ΔT) curve should show a characteristic shape: zero below the threshold, then a rise to a maximum, followed by a linear decrease.

## Assets

- Standard thermodynamic properties of water (surface tension, molar volumes, vapor pressure curve, Clausius-Clapeyron slope)
- Condensation coefficient f value (0.045)

## Workflow steps

### Step 1: Classical nucleation calculation
- Role: scored
- Action: Compute the critical nucleus radius r_crit and required undercooling ΔT_nucl for dropwise condensation of steam using classical nucleation theory. Use the Thomson/Kelvin relation, Clausius–Clapeyron equation, and the nucleation work expression for a contact angle of 90°. Determine r_crit as the radius where the nucleation frequency I(r) reaches its maximum, using an attempt frequency of approximately 10²⁶ s⁻¹. Output the results to nucleation.csv.
- Output file: `/app/outputs/nucleation.csv`
- Format: csv
- Contract: CSV with columns: r_crit_m (float, critical nucleus radius in meters), undercooling_K (float, required undercooling in Kelvin).
- Scoring: scored by hidden verifier

### Step 2: Heat transfer coefficient α_m vs ΔT
- Role: scored (load-bearing)
- Action: Compute the mean heat transfer coefficient α_m for dropwise condensation as a function of temperature difference ΔT. Use the undercooling threshold ΔT_nucl from nucleation.csv. For each ΔT from 0.5 °C to 10 °C in steps of 0.5 °C, if ΔT < ΔT_nucl set α_m = 0; otherwise compute α_m from the model: α_m = α_p (1−φ) [1 − K H α_p ΔT], where α_p is the phase‑transition heat transfer coefficient evaluated for water vapor at 1 atm with condensation coefficient f=0.045, f(1−φ)=0.016, H=0.019 m, K=5×10⁻⁶ m·h/kcal. Convert all quantities to SI units for the output (α_m in W/(m²·K), ΔT in K). Output the results as a CSV.
- Output file: `/app/outputs/heat_transfer.csv`
- Format: csv
- Contract: CSV with columns: Delta_T_K (float, temperature difference in Kelvin), alpha_m_W_m2K (float, heat transfer coefficient in W/(m²·K)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleation.csv`
- `/app/outputs/heat_transfer.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleation.csv
- path: `/app/outputs/nucleation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Critical nucleus radius (meters) and required undercooling (Kelvin) for steam condensation at 100 °C.
- schema:
  - `type`: table
  - `required_columns`: `r_crit_m`, `undercooling_K`
  - `units`:
    - `r_crit_m`: meters
    - `undercooling_K`: Kelvin

### heat_transfer.csv
- path: `/app/outputs/heat_transfer.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Heat transfer coefficient α_m (W/(m²·K)) as a function of temperature difference ΔT (K).
- schema:
  - `type`: table
  - `required_columns`: `Delta_T_K`, `alpha_m_W_m2K`
  - `units`:
    - `Delta_T_K`: Kelvin
    - `alpha_m_W_m2K`: W/(m^2·K)

Notes: The checker recomputes the nucleation quantities and α_m(ΔT) using the same theoretical model. For nucleation: comparison of critical radius and undercooling against recomputed values. For heat transfer: comparison of α_m at each ΔT point and verification of the qualitative trend (peak location).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_crit_m",
          "undercooling_K"
        ],
        "units": {
          "r_crit_m": "meters",
          "undercooling_K": "Kelvin"
        }
      },
      "description": "Critical nucleus radius (meters) and required undercooling (Kelvin) for steam condensation at 100 °C."
    },
    {
      "file": "heat_transfer.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Delta_T_K",
          "alpha_m_W_m2K"
        ],
        "units": {
          "Delta_T_K": "Kelvin",
          "alpha_m_W_m2K": "W/(m^2·K)"
        }
      },
      "description": "Heat transfer coefficient α_m (W/(m²·K)) as a function of temperature difference ΔT (K)."
    }
  ],
  "notes": "The checker recomputes the nucleation quantities and α_m(ΔT) using the same theoretical model. For nucleation: comparison of critical radius and undercooling against recomputed values. For heat transfer: comparison of α_m at each ΔT point and verification of the qualitative trend (peak location)."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently recomputes the expected outputs from the same theoretical model. For `nucleation.csv`, it compares your `r_crit` and undercooling values against its own reference (relative tolerance allowed). For `heat_transfer.csv`, it recomputes α_m for every ΔT point and compares against your reported values (relative tolerance per point). In addition, it checks that the α_m curve reaches its maximum at a temperature difference consistent with the model. Both artifacts contribute to the final reward, which is a single number between 0 and 1. Reporting numbers without a correct computational trace will not receive credit.
