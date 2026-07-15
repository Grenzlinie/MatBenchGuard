# Compute thermodynamic properties of aqueous B(OH)₃ using the Akinfiev–Diamond equation of state

## Problem background
Thermodynamic properties of aqueous boric acid (B(OH)₃) over a wide temperature and pressure range are important for geothermal fluid modelling and steam-cycle technology. The Akinfiev–Diamond (2003) equation of state for aqueous nonelectrolytes at infinite dilution provides a compact semi‑empirical framework that predicts chemical potential, partial molar volume, heat capacity, and vapour‑liquid distribution from only three solute‑specific parameters (ξ, a, b) together with the properties of pure water. In this task you will compute a full set of thermodynamic predictions for B(OH)₃ from the given set of parameters.

## Approach
The core of the method is the Akinfiev–Diamond equation of state, which expresses the standard‑state chemical potential of an aqueous nonelectrolyte as a function of water density, water fugacity, the three empirical constants ξ, a, b, and the ideal‑gas properties of the solute. From this master relation one can derive the Henry constant, vapour‑liquid distribution constant, partial molar volume, partial molar heat capacity, and the Krichevskii parameter.

You are provided with the EoS parameters for B(OH)₃:
- ξ = −1.057
- a = −4.2561 cm³ g⁻¹
- b = 4.0194 cm³ K^0.5 g⁻¹

Ideal‑gas properties are also given:
- ΔfG°₂₉₈ = −931.04 kJ mol⁻¹
- S°₂₉₈ = 278.61 J mol⁻¹ K⁻¹
- Cₚ⁰(T) = 195.7 − 0.406×10⁻³ T + 2.482×10⁵ T⁻² − 2.186×10³ T⁻⁰·⁵ J mol⁻¹ K⁻¹

Water (solvent) properties (density, fugacity, and their temperature and pressure derivatives) must be obtained from the IAPWS IF97 formulation using the `iapws` Python package.

The workflow consists of implementing the EoS and water‑property helper, then evaluating the model:
1. Compute vapour‑liquid distribution constants (ln K_D) along the water saturation curve.
2. Compute partial molar volumes and heat capacities at selected isobars.
3. Compute the Krichevskii parameter A_Kr and the standard‑state aqueous properties ΔfG∞ and S₂° at 298.15 K and 0.1 MPa.
All quantities are evaluated at infinite dilution.

## Reproduction target
Your goal is to produce the following three scored artifacts by implementing the Akinfiev–Diamond equation of state and the water‑property interface exactly as described:

- **`kd_predictions_boh3.csv`**: natural logarithm of the vapour‑liquid distribution constant ln K_D for aqueous B(OH)₃ at the temperatures 373.15 K, 500 K, 520 K, 573 K, and 623 K along the water saturation curve.
- **`v2_cp2_predictions_boh3.csv`**: partial molar volume V2∞ (cm³ mol⁻¹) and partial molar heat capacity Cp2∞ (J mol⁻¹ K⁻¹) at temperatures 298, 350, 400, 450, and 500 K for the two pressures 28 MPa and 35 MPa.
- **`thermodynamic_properties_boh3.json`**: the Krichevskii parameter A_Kr (MPa), the standard‑state Gibbs free energy of formation ΔfG∞ (kJ mol⁻¹), and the standard‑state entropy S₂° (J mol⁻¹ K⁻¹) for aqueous B(OH)₃ at 298.15 K and 0.1 MPa.

All outputs must be written to `/app/outputs/` and match the required schemas (columns/keys and units) listed in the workflow steps.

## Assets

- IAPWS IF97 Python package: iapws

## Workflow steps

### Step 1: Implement Akinfiev-Diamond EoS and water property interface
- Role: process
- Action: Implement the Akinfiev-Diamond (2003) equation of state for aqueous B(OH)₃ at infinite dilution: chemical potential, Henry's constant, vapour-liquid distribution constant, partial molar volume, partial molar heat capacity, and Krichevskii parameter. Write Python functions that use the given EoS parameters (ξ=-1.057, a=-4.2561 cm³ g⁻¹, b=4.0194 cm³ K^0.5 g⁻¹) and the ideal-gas properties (ΔfG°₂₉₈=-931.04 kJ mol⁻¹, S°₂₉₈=278.61 J mol⁻¹ K⁻¹, Cₚ(T) function). Implement a water property helper that retrieves pure-water density, fugacity, and needed derivatives along the saturation curve and at specified P,T using the IAPWS IF97 model via the `iapws` package.
- Evidence: none

### Step 2: Compute vapour-liquid distribution constants ln KD
- Role: scored
- Action: Using the implemented EoS and the water properties along the saturation curve, compute ln K_D (natural logarithm of the vapour-liquid distribution constant) for aqueous B(OH)₃ at temperatures 373.15 K, 500 K, 520 K, 573 K, and 623 K. Write the results to a CSV file.
- Output file: `/app/outputs/kd_predictions_boh3.csv`
- Format: csv
- Contract: Columns: Temp_K (temperature in K), ln_KD (dimensionless natural logarithm of the distribution constant). One row per temperature.
- Scoring: scored by hidden verifier

### Step 3: Compute partial molar volume and heat capacity
- Role: scored (load-bearing)
- Action: Using the EoS and water properties, compute the partial molar volume V2∞ (cm³ mol⁻¹) and partial molar heat capacity Cp2∞ (J mol⁻¹ K⁻¹) for aqueous B(OH)₃ at temperatures 298, 350, 400, 450, 500 K for pressures 28 MPa and 35 MPa. Write the results to a CSV file.
- Output file: `/app/outputs/v2_cp2_predictions_boh3.csv`
- Format: csv
- Contract: Columns: Temp_K (temperature in K), Pressure_MPa (pressure in MPa), V2infty_cm3_mol (partial molar volume in cm³ mol⁻¹), Cp2infty_J_mol_K (partial molar heat capacity in J mol⁻¹ K⁻¹). One row per (T,P) combination.
- Scoring: scored by hidden verifier

### Step 4: Compute Krichevskii parameter and standard-state properties
- Role: scored
- Action: Compute the Krichevskii parameter A_Kr (MPa) using the EoS parameters and the critical constants of water (from IAPWS). Compute the standard-state Gibbs free energy of formation ΔfG∞ (kJ mol⁻¹) and standard-state entropy S₂° (J mol⁻¹ K⁻¹) for aqueous B(OH)₃ at 298.15 K and 0.1 MPa using the ideal-gas properties and the EoS. Write the results to a JSON file.
- Output file: `/app/outputs/thermodynamic_properties_boh3.json`
- Format: json
- Contract: JSON object with keys: A_Kr_MPa (number, MPa), delta_f_G_infinity_kJ_mol (number, kJ mol⁻¹), S2_infinity_J_mol_K (number, J mol⁻¹ K⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kd_predictions_boh3.csv`
- `/app/outputs/v2_cp2_predictions_boh3.csv`
- `/app/outputs/thermodynamic_properties_boh3.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kd_predictions_boh3.csv
- path: `/app/outputs/kd_predictions_boh3.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The computed ln K_D values for B(OH)₃ are compared to the paper-reported values at the specified temperatures within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `Temp_K`, `ln_KD`
  - `units`:
    - `Temp_K`: K
    - `ln_KD`: dimensionless

### v2_cp2_predictions_boh3.csv
- path: `/app/outputs/v2_cp2_predictions_boh3.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The computed V2∞ and Cp2∞ for B(OH)₃ are compared to paper-reported values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `Temp_K`, `Pressure_MPa`, `V2infty_cm3_mol`, `Cp2infty_J_mol_K`
  - `units`:
    - `Temp_K`: K
    - `Pressure_MPa`: MPa
    - `V2infty_cm3_mol`: cm³ mol⁻¹
    - `Cp2infty_J_mol_K`: J mol⁻¹ K⁻¹

### thermodynamic_properties_boh3.json
- path: `/app/outputs/thermodynamic_properties_boh3.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed A_Kr, ΔfG∞, and S₂° for B(OH)₃ are compared to the paper-reported values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `A_Kr_MPa`: number
    - `delta_f_G_infinity_kJ_mol`: number
    - `S2_infinity_J_mol_K`: number

Notes: Fully functional B(OH)₃ task. Si(OH)₄ and As(OH)₃ to be added in subsequent repair turns.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kd_predictions_boh3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temp_K",
          "ln_KD"
        ],
        "units": {
          "Temp_K": "K",
          "ln_KD": "dimensionless"
        }
      },
      "description": "The computed ln K_D values for B(OH)₃ are compared to the paper-reported values at the specified temperatures within tolerances."
    },
    {
      "file": "v2_cp2_predictions_boh3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temp_K",
          "Pressure_MPa",
          "V2infty_cm3_mol",
          "Cp2infty_J_mol_K"
        ],
        "units": {
          "Temp_K": "K",
          "Pressure_MPa": "MPa",
          "V2infty_cm3_mol": "cm³ mol⁻¹",
          "Cp2infty_J_mol_K": "J mol⁻¹ K⁻¹"
        }
      },
      "description": "The computed V2∞ and Cp2∞ for B(OH)₃ are compared to paper-reported values within tolerances."
    },
    {
      "file": "thermodynamic_properties_boh3.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "A_Kr_MPa": "number",
          "delta_f_G_infinity_kJ_mol": "number",
          "S2_infinity_J_mol_K": "number"
        }
      },
      "description": "The computed A_Kr, ΔfG∞, and S₂° for B(OH)₃ are compared to the paper-reported values within tolerances."
    }
  ],
  "notes": "Fully functional B(OH)₃ task. Si(OH)₄ and As(OH)₃ to be added in subsequent repair turns."
}
```

## How you are scored
A hidden verifier checks each of the three scored output files (Steps 2–4) independently and combines them into a final reward between 0 and 1. Every artifact is compared to the correct expected results for this model and these input parameters; reporting a number without a genuine computation will not earn full credit. The verifier may recompute derived quantities from your raw output or compare them against reference values, applying appropriate tolerances. The three scored stages carry roughly equal weight, with a slightly higher contribution from the bulk property predictions (ln K_D, V2∞, Cp2∞). Structure and format compliance are also checked but carry near‑zero weight.
