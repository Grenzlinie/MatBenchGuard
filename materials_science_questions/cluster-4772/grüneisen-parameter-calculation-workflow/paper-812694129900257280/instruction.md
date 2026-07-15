# Thermal Expansion Coefficient Calculation from Elastic Constants

## Problem background
Coefficients of thermal expansion (CTE) quantify how a material's dimensions change with temperature, a key property for designing structures under thermal loads. Room-temperature CTE of metals and semi-metals can be derived from elastic constants using a Debye-based thermodynamic identity. For a subset of metals, a binding-energy/longitudinal-wave relation can also be applied. This task computes the CTE for a set of 29 elements and a selected six-element subset by applying these formulas with provided material property data.

## Approach
The computation uses two independent routes. The first route applies a thermodynamic identity linking the linear coefficient of thermal expansion α to the heat capacities at constant pressure (C_P) and constant volume (C_V), the bulk modulus (B), the molar volume (V), and temperature T: α = (1/3) * sqrt((C_P − C_V) / (B * V * T)). At T = 300 K this yields a room-temperature estimate. The second route, applicable to a subset of six metals, expresses α in terms of the binding energy (E_B), the longitudinal elastic modulus (E_l), and a dimensionless relaxation factor ν. The factor ν is obtained from a nominal Poisson's ratio μ₀ via ν = 0.83 * μ₀ + 0.14, and the CTE is computed as α = ν * C_V * sqrt(1 / (E_l * V * E_B)). Appropriate unit conversions (eV to J, GPa to Pa) are required. Two bundled CSV files supply all necessary numeric inputs.

## Reproduction target
Using the provided input datasets (material_properties.csv for 29 elements and binding_input.csv for six elements), compute the room-temperature coefficient of thermal expansion α. For all 29 elements, produce `/app/outputs/alpha_eq5.csv` with columns element and alpha (units K⁻¹) by evaluating the Debye-based formula with T = 300 K. For the six elements Li, K, Pb, W, Cu, Au, produce `/app/outputs/alpha_eq6.csv` with the same schema by evaluating the binding-energy formula, using the provided ν factor or computing it from μ₀ as described. The output files will be checked for correctness against a hidden reference.

## Assets

- material_properties.csv
- binding_input.csv
- python3: python3

## Workflow steps

### Step 1: Load input data
- Role: process
- Action: Load the material properties dataset (material_properties.csv) with columns element, C_P, C_V, B, V for 29 elements, and the binding energy dataset (binding_input.csv) with columns element, E_l, E_B, μ0, C_V, V for six elements. Verify that all required columns are present.
- Evidence: none

### Step 2: Compute CTE via Debye–Grüneisen formula
- Role: scored
- Action: For each element in the material properties dataset, compute the room-temperature coefficient of thermal expansion α = (1/3) * sqrt((C_P − C_V) / (B * V * T)) using T = 300 K and consistent SI units. Write a CSV file with columns element and alpha (K⁻¹).
- Output file: `/app/outputs/alpha_eq5.csv`
- Format: csv
- Contract: Two columns: element (string), alpha (float, units K⁻¹). 29 data rows.
- Scoring: scored by hidden verifier

### Step 3: Compute CTE via binding energy method
- Role: scored
- Action: For the elements Li, K, Pb, W, Cu, Au in the binding energy dataset, compute the relaxation factor ν = 0.83*μ₀ + 0.14, then calculate α = ν * C_V * sqrt(1 / (E_l * V * E_B)), converting units appropriately (1 eV = 1.602e-19 J, 1 GPa = 1e9 Pa). Write a CSV file with columns element and alpha (K⁻¹).
- Output file: `/app/outputs/alpha_eq6.csv`
- Format: csv
- Contract: Two columns: element (string), alpha (float, units K⁻¹). 6 data rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/alpha_eq5.csv`
- `/app/outputs/alpha_eq6.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alpha_eq5.csv
- path: `/app/outputs/alpha_eq5.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed room-temperature coefficient of thermal expansion for 29 elements using the Debye–Grüneisen relation. Each row contains the element name and its alpha value.
- schema:
  - `type`: table
  - `required_columns`: `element`, `alpha`
  - `units`:
    - `alpha`: K⁻¹

### alpha_eq6.csv
- path: `/app/outputs/alpha_eq6.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed room-temperature coefficient of thermal expansion for six metals using the binding energy/longitudinal elastic wave energy method. Each row contains the element name and its alpha value.
- schema:
  - `type`: table
  - `required_columns`: `element`, `alpha`
  - `units`:
    - `alpha`: K⁻¹

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alpha_eq5.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "alpha"
        ],
        "units": {
          "alpha": "K⁻¹"
        }
      },
      "description": "Computed room-temperature coefficient of thermal expansion for 29 elements using the Debye–Grüneisen relation. Each row contains the element name and its alpha value."
    },
    {
      "file": "alpha_eq6.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "alpha"
        ],
        "units": {
          "alpha": "K⁻¹"
        }
      },
      "description": "Computed room-temperature coefficient of thermal expansion for six metals using the binding energy/longitudinal elastic wave energy method. Each row contains the element name and its alpha value."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently evaluates both output CSVs. For each file, the verifier compares every element's computed α to an expected reference value and assigns a partial score. The two partial scores are combined into a final reward. The closer your computed numbers are to the expected values, the higher your reward. Simply reporting numbers without actually computing them from the provided data will not satisfy the verifier.
