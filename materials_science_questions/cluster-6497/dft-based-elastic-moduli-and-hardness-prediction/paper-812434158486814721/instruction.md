# Physical and mechanical moduli and gamma-ray attenuation of BVBL glasses

## Problem background
Radiation shielding materials require high density and effective photon attenuation. Glass systems offer compositional flexibility and transparency. A lanthanum-barium-borovanadate (BVBL) glass series, doped with varying amounts of bismuth oxide (Bi2O3), has been proposed for gamma‑ray shielding. This task investigates the effect of Bi2O3 concentration on physical properties (density, molar volume, oxygen packing), mechanical moduli (Young's, bulk, shear, longitudinal), and mass attenuation coefficients (MAC) for photon energies from 0.015 to 15 MeV, in order to identify the composition with the best shielding performance.

## Approach
The six glass compositions are defined by the formula 5La2O3‑10BaO‑(65−x)B2O3‑20V2O5‑xBi2O3, with x = 0, 3, 6, 9, 12, 15 mol% (labelled BVBL0 to BVBL15). The constituent oxides have known bulk densities and molecular weights. 
Physical properties are calculated from the oxide composition using standard relations: glass density is obtained from the inverse of the weighted sum of specific volumes; average molecular weight, molar volume, oxygen molar volume, and oxygen packing density are then derived. 
Mechanical moduli are estimated with the Makishima‑Mackenzie model, which relates the glass composition to Young’s modulus via total dissociation energy and packing density factors. The required input parameters (dissociation energies, ionic radii) for each oxide are available in the literature. Bulk, shear, and longitudinal moduli are subsequently computed from Young’s modulus. 
Mass attenuation coefficients (MAC) are obtained for each glass at twelve photon energies (0.015, 0.03, 0.1, 0.3, 0.5, 0.8, 1, 3, 5, 8, 10, 15 MeV) using the Phy‑X/PSD online database or an equivalent open‑source attenuation library (e.g., the pyear package). From MAC and density, the linear attenuation coefficient (LAC) and half‑value layer (HVL) can also be computed to assess shielding performance.

## Reproduction target
Produce three CSV files containing the computed quantities for all six glass codes:
- physical_properties.csv: density (g/cm³), molar volume (cm³/mol), oxygen molar volume (cm³/mol), oxygen packing density (cm³/mol).
- mechanical_moduli.csv: Young’s modulus, bulk modulus, shear modulus, longitudinal modulus (all in GPa).
- mac_table.csv: mass attenuation coefficient (cm²/g) for each glass at each of the 12 photon energies (72 rows total).
The verifier will also evaluate structural shielding performance: it will compute the linear attenuation coefficient (LAC) from the submitted MAC and density values and assess its trend across the BVBL series; it will compute the half‑value layer (HVL) and compare the undoped and most‑doped glass; it will derive the effective atomic number (Zeff) and the transmission factor (TF) at a reference thickness from the composition and MAC data and evaluate them for consistency with expected shielding behaviour.

## Assets

- Standard oxide densities and molecular weights (B2O3, V2O5, BaO, La2O3, Bi2O3)
- Makishima-Mackenzie model parameters: dissociation energies and ionic radii for constituent oxides: 10.1016/0022-3093(73)90053-7 and 10.1111/j.1151-2916.1999.tb02272.x
- Phy-X/PSD online radiation shielding database: https://phy-x.net/PSD
- Standard atomic weights and oxide composition data

## Workflow steps

### Step 1: Calculate physical properties
- Role: scored
- Action: Compute density, molar volume, oxygen molar volume, and oxygen packing density for each glass composition (BVBL0–BVBL15) using the standard oxide density values and the formulas for physical property calculation. Write the results to physical_properties.csv.
- Output file: `/app/outputs/physical_properties.csv`
- Format: csv
- Contract: columns: glass_code (str), density_g_cm3 (float), molar_volume_cm3_mol (float), oxygen_molar_volume_cm3_mol (float), oxygen_packing_density_cm3_mol (float). Six rows, one per glass.
- Scoring: scored by hidden verifier

### Step 2: Calculate mechanical moduli
- Role: scored
- Action: Using the Makishima-Mackenzie model, compute Young's modulus, bulk modulus, shear modulus, and longitudinal modulus for each glass, employing the dissociation energies and ionic radii from literature and the density/molecular weight from step 1. Write the results to mechanical_moduli.csv.
- Output file: `/app/outputs/mechanical_moduli.csv`
- Format: csv
- Contract: columns: glass_code (str), Young_modulus_GPa (float), bulk_modulus_GPa (float), shear_modulus_GPa (float), longitudinal_modulus_GPa (float). Six rows.
- Scoring: scored by hidden verifier

### Step 3: Determine mass attenuation coefficients
- Role: scored (load-bearing)
- Action: For each glass, use Phy-X/PSD (or an equivalent open-source attenuation library) to compute mass attenuation coefficients (MAC, cm²/g) at the twelve photon energies: 0.015, 0.03, 0.1, 0.3, 0.5, 0.8, 1, 3, 5, 8, 10, 15 MeV. Write the results to mac_table.csv.
- Output file: `/app/outputs/mac_table.csv`
- Format: csv
- Contract: columns: glass_code (str), energy_MeV (float), mac_cm2_g (float). 72 rows (6 glasses × 12 energies).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/physical_properties.csv`
- `/app/outputs/mechanical_moduli.csv`
- `/app/outputs/mac_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### physical_properties.csv
- path: `/app/outputs/physical_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Glass density, molar volume, oxygen molar volume, and oxygen packing density for the six BVBL glasses.
- schema:
  - `type`: table
  - `required_columns`: `glass_code`, `density_g_cm3`, `molar_volume_cm3_mol`, `oxygen_molar_volume_cm3_mol`, `oxygen_packing_density_cm3_mol`

### mechanical_moduli.csv
- path: `/app/outputs/mechanical_moduli.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Young's, bulk, shear, and longitudinal moduli for the six glasses.
- schema:
  - `type`: table
  - `required_columns`: `glass_code`, `Young_modulus_GPa`, `bulk_modulus_GPa`, `shear_modulus_GPa`, `longitudinal_modulus_GPa`

### mac_table.csv
- path: `/app/outputs/mac_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mass attenuation coefficients for all six glasses at twelve photon energies (0.015–15 MeV).
- schema:
  - `type`: table
  - `required_columns`: `glass_code`, `energy_MeV`, `mac_cm2_g`

Notes: The checker additionally verifies derived shielding parameters (LAC, HVL) for monotonic trends and ratio conditions using the submitted physical properties and MAC values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "physical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "glass_code",
          "density_g_cm3",
          "molar_volume_cm3_mol",
          "oxygen_molar_volume_cm3_mol",
          "oxygen_packing_density_cm3_mol"
        ]
      },
      "description": "Glass density, molar volume, oxygen molar volume, and oxygen packing density for the six BVBL glasses."
    },
    {
      "file": "mechanical_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "glass_code",
          "Young_modulus_GPa",
          "bulk_modulus_GPa",
          "shear_modulus_GPa",
          "longitudinal_modulus_GPa"
        ]
      },
      "description": "Young's, bulk, shear, and longitudinal moduli for the six glasses."
    },
    {
      "file": "mac_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "glass_code",
          "energy_MeV",
          "mac_cm2_g"
        ]
      },
      "description": "Mass attenuation coefficients for all six glasses at twelve photon energies (0.015–15 MeV)."
    }
  ],
  "notes": "The checker additionally verifies derived shielding parameters (LAC, HVL) for monotonic trends and ratio conditions using the submitted physical properties and MAC values."
}
```

## How you are scored
A hidden verifier independently evaluates your outputs. It first checks that each CSV file contains the correct columns and row count. Then it compares your computed values against reference values derived from the same computational protocol; each quantity must fall within a predetermined tolerance. Additionally, the verifier computes derived shielding parameters (LAC, HVL, Zeff, TF) from your submitted MAC and density values and assesses them against structural benchmarks. The final reward is a weighted sum of the scores across all outputs, with the mass attenuation coefficients and structural trend checks carrying the highest weight. Simply reporting paper‑derived numbers is not sufficient; the verifier recomputes the expected results from the public inputs and scoring rules.
