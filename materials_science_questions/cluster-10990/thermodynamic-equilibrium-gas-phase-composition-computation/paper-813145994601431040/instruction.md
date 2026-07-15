# Equilibrium Distribution of Alkali Metal Species in Co-combustion of Coal and Biomass

## Problem background
Co-combustion of coal and biomass is a promising route to reduce net CO₂ emissions, but biomass fuels often contain high levels of alkali metals (K, Na) and chlorine, leading to ash-related operational problems such as slagging, fouling, and corrosion. Understanding the thermodynamic equilibrium distribution of potassium and sodium species under combustion conditions is crucial to predict which solid and gaseous compounds form and how they depend on fuel composition and temperature. This task computes the equilibrium mole fractions of major K and Na species for blends of wheat straw and coal at various shares and temperatures using Gibbs free energy minimization, providing insight into the speciation that governs ash behavior.

## Approach
Perform thermodynamic equilibrium calculations using the method of Gibbs energy minimization. Given the elemental composition of the fuel blend (mass fractions of C, H, N, O, S, Cl, Si, Na, K, Ca, Mg, Al, Fe, Ti), temperature, pressure, and excess air ratio, the equilibrium state of a multi-phase system (ideal gas + stoichiometric condensed phases) is found by minimizing the total Gibbs free energy. The calculation is carried out with an open-source chemical thermodynamics library (e.g., Cantera) that provides thermodynamic data for the species of interest.

The fuel compositions used in this study are given below (wt%, air-dry basis). Blend compositions are obtained by mass-weighted averaging of the two pure fuels.

| Component               | Wheat straw | Coal   |
|-------------------------|-------------|--------|
| Proximate analysis      |             |        |
| Ash                     | 7.59        | 15.10  |
| Volatile matter         | 72.32       | 39.06  |
| Fixed carbon            | 8.84        | 42.48  |
| Moisture                | 5.52        | 3.36   |
| Ultimate analysis       |             |        |
| C                       | 43.81       | 64.88  |
| H                       | 6.08        | 4.28   |
| N                       | 0.47        | 0.72   |
| S                       | 0.69        | 0.39   |
| O                       | 35.84       | 11.27  |
| Cl                      | 0.90        | 0.01   |
| Ash composition         |             |        |
| K                       | 1.79        | 0.05   |
| Na                      | 0.11        | 0.10   |
| Ca                      | 0.14        | 0.43   |
| Mg                      | 0.33        | 0.16   |
| Al                      | 0.20        | 1.17   |
| Si                      | 2.18        | 3.47   |
| Fe                      | 0.11        | 0.51   |
| Ti                      | 0.01        | 0.06   |

The calculation domain includes C, H, N, O, S, Cl, Si, Na, K, Ca, Mg, Al, Fe, Ti. The excess air ratio is 1.2, and the total pressure is 0.1 MPa. Only the equilibrium mole fractions of selected gaseous and solid alkali species are required for the scored outputs; all other stable phases are included in the equilibrium calculation to correctly partition the elements.

## Reproduction target
Produce two CSV files containing equilibrium mole fractions of the specified potassium and sodium species:

1. **Blend series** – For wheat straw mass fractions of 0, 20, 50, 80, and 100 wt% at 850 °C, 0.1 MPa, and excess air ratio 1.2, write the mole fractions of KCl(g), K₂SO₄(s), KAlSiO₄(s), K₂Fe₂O₄(s), K₂TiO₃(s), NaCl(g), Na₂SO₄(s), Na₂SiO₃(s), NaAlSiO₄(s), and Na₂CO₃(s) to `k_na_species_vs_blend.csv`.

2. **Temperature series** – For a blend of 80 wt% wheat straw (remainder coal) at temperatures of 600, 700, 800, 900, and 1000 °C, with pressure 0.1 MPa and excess air ratio 1.2, write the mole fractions of KCl(g), K₂SO₄(s), KAlSiO₄(s), KAlSiO₆(s), NaCl(g), Na₂SO₄(s), Na₂SiO₃(s), NaAlSiO₄(s), and Na₂CO₃(s) to `k_na_species_vs_temperature.csv`.

The exact column schemas are stated in the workflow steps and output contract.

## Assets

- Cantera: cantera

## Workflow steps

### Step 1: Compute equilibrium distribution vs. wheat straw share
- Role: scored
- Action: For wheat straw mass fractions of 0, 20, 50, 80, and 100 wt%, perform a Gibbs energy minimization at 850 °C, 0.1 MPa, and excess air ratio 1.2 using the provided fuel elemental compositions (C, H, N, O, S, Cl, Si, Na, K, Ca, Mg, Al, Fe, Ti). Write the equilibrium mole fractions of the specified K and Na species to the output CSV.
- Output file: `/app/outputs/k_na_species_vs_blend.csv`
- Format: csv
- Contract: CSV with columns: wheat_straw_wt% (0,20,50,80,100), KCl_g, K2SO4_s, KAlSiO4_s, K2Fe2O4_s, K2TiO3_s, NaCl_g, Na2SO4_s, Na2SiO3_s, NaAlSiO4_s, Na2CO3_s. All species mole fractions are dimensionless.
- Scoring: scored by hidden verifier

### Step 2: Compute equilibrium distribution vs. temperature
- Role: scored
- Action: For the blend with 80 wt% wheat straw, perform a Gibbs energy minimization at temperatures of 600, 700, 800, 900, and 1000 °C, keeping pressure at 0.1 MPa and excess air ratio 1.2. Write the equilibrium mole fractions of the specified K and Na species to the output CSV.
- Output file: `/app/outputs/k_na_species_vs_temperature.csv`
- Format: csv
- Contract: CSV with columns: temperature_C (600,700,800,900,1000), KCl_g, K2SO4_s, KAlSiO4_s, KAlSiO6_s, NaCl_g, Na2SO4_s, Na2SiO3_s, NaAlSiO4_s, Na2CO3_s. All species mole fractions are dimensionless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/k_na_species_vs_blend.csv`
- `/app/outputs/k_na_species_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### k_na_species_vs_blend.csv
- path: `/app/outputs/k_na_species_vs_blend.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium mole fractions of K and Na species at 850 °C as a function of wheat straw share in the fuel.
- schema:
  - `type`: table
  - `required_columns`: `wheat_straw_wt%`, `KCl_g`, `K2SO4_s`, `KAlSiO4_s`, `K2Fe2O4_s`, `K2TiO3_s`, `NaCl_g`, `Na2SO4_s`, `Na2SiO3_s`, `NaAlSiO4_s`, `Na2CO3_s`
  - `units`:
    - `wheat_straw_wt%`: weight percent
    - `KCl_g`: dimensionless mole fraction
    - `K2SO4_s`: dimensionless mole fraction
    - `KAlSiO4_s`: dimensionless mole fraction
    - `K2Fe2O4_s`: dimensionless mole fraction
    - `K2TiO3_s`: dimensionless mole fraction
    - `NaCl_g`: dimensionless mole fraction
    - `Na2SO4_s`: dimensionless mole fraction
    - `Na2SiO3_s`: dimensionless mole fraction
    - `NaAlSiO4_s`: dimensionless mole fraction
    - `Na2CO3_s`: dimensionless mole fraction

### k_na_species_vs_temperature.csv
- path: `/app/outputs/k_na_species_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium mole fractions of K and Na species for 80 wt% wheat straw blend as a function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `KCl_g`, `K2SO4_s`, `KAlSiO4_s`, `KAlSiO6_s`, `NaCl_g`, `Na2SO4_s`, `Na2SiO3_s`, `NaAlSiO4_s`, `Na2CO3_s`
  - `units`:
    - `temperature_C`: degree Celsius
    - `KCl_g`: dimensionless mole fraction
    - `K2SO4_s`: dimensionless mole fraction
    - `KAlSiO4_s`: dimensionless mole fraction
    - `KAlSiO6_s`: dimensionless mole fraction
    - `NaCl_g`: dimensionless mole fraction
    - `Na2SO4_s`: dimensionless mole fraction
    - `Na2SiO3_s`: dimensionless mole fraction
    - `NaAlSiO4_s`: dimensionless mole fraction
    - `Na2CO3_s`: dimensionless mole fraction

Notes: The checker compares the agent's computed mole fractions to hidden reference values digitized from the paper's equilibrium distribution figures, using appropriate tolerances. The comparison accounts for differences due to using a different Gibbs energy minimization tool (Cantera vs. HSC 6.0).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "k_na_species_vs_blend.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wheat_straw_wt%",
          "KCl_g",
          "K2SO4_s",
          "KAlSiO4_s",
          "K2Fe2O4_s",
          "K2TiO3_s",
          "NaCl_g",
          "Na2SO4_s",
          "Na2SiO3_s",
          "NaAlSiO4_s",
          "Na2CO3_s"
        ],
        "units": {
          "wheat_straw_wt%": "weight percent",
          "KCl_g": "dimensionless mole fraction",
          "K2SO4_s": "dimensionless mole fraction",
          "KAlSiO4_s": "dimensionless mole fraction",
          "K2Fe2O4_s": "dimensionless mole fraction",
          "K2TiO3_s": "dimensionless mole fraction",
          "NaCl_g": "dimensionless mole fraction",
          "Na2SO4_s": "dimensionless mole fraction",
          "Na2SiO3_s": "dimensionless mole fraction",
          "NaAlSiO4_s": "dimensionless mole fraction",
          "Na2CO3_s": "dimensionless mole fraction"
        }
      },
      "description": "Equilibrium mole fractions of K and Na species at 850 °C as a function of wheat straw share in the fuel."
    },
    {
      "file": "k_na_species_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "KCl_g",
          "K2SO4_s",
          "KAlSiO4_s",
          "KAlSiO6_s",
          "NaCl_g",
          "Na2SO4_s",
          "Na2SiO3_s",
          "NaAlSiO4_s",
          "Na2CO3_s"
        ],
        "units": {
          "temperature_C": "degree Celsius",
          "KCl_g": "dimensionless mole fraction",
          "K2SO4_s": "dimensionless mole fraction",
          "KAlSiO4_s": "dimensionless mole fraction",
          "KAlSiO6_s": "dimensionless mole fraction",
          "NaCl_g": "dimensionless mole fraction",
          "Na2SO4_s": "dimensionless mole fraction",
          "Na2SiO3_s": "dimensionless mole fraction",
          "NaAlSiO4_s": "dimensionless mole fraction",
          "Na2CO3_s": "dimensionless mole fraction"
        }
      },
      "description": "Equilibrium mole fractions of K and Na species for 80 wt% wheat straw blend as a function of temperature."
    }
  ],
  "notes": "The checker compares the agent's computed mole fractions to hidden reference values digitized from the paper's equilibrium distribution figures, using appropriate tolerances. The comparison accounts for differences due to using a different Gibbs energy minimization tool (Cantera vs. HSC 6.0)."
}
```

## How you are scored
After you submit your outputs, a hidden verifier will read the two CSV files and compare every reported mole fraction to reference values obtained from a faithful implementation of the Gibbs energy minimization. Agreement is checked with per-species tolerances that account for typical numerical differences and variations in thermodynamic databases. The verifier also inspects monotonic trends (e.g., whether certain species increase consistently with wheat straw share or temperature) and flags physically impossible results. The final reward is a weighted average of the per-species scores, with higher weight given to the major species. The tolerances are set so that a physically correct calculation achieves a high score, while random guesses or unphysical results score near zero. The exact tolerance values are hidden to ensure honest computation.
