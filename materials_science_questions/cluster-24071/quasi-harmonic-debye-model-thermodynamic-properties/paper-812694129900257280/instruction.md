# Compute Room-Temperature Thermal Expansion Coefficient from Elastic Constants

## Problem background
The thermal expansion of metals and semi-metals is a fundamental material property. Predicting the room-temperature coefficient of thermal expansion (CTE) from basic elastic and thermal data would avoid costly experimental measurements. This challenge has been addressed using Debye–Grüneisen theory, which connects vibrational properties to volume changes. It remains an open question whether a simple algebraic expression built solely on specific heats, bulk modulus, and density can yield CTE values consistent with experimental observation across a broad set of elements.

## Approach
A Debye–Grüneisen inspired relation expresses the CTE in terms of the difference between the constant-pressure and constant-volume specific heats (Cp and Cv), the bulk modulus B, and the specific volume V at room temperature. For a given element, one computes the specific volume from the standard density (V = 1/ρ). The CTE is then obtained from the formula that involves (Cp − Cv), B, V, and temperature T = 298.15 K, after converting to the target units of 10⁻⁶ K⁻¹. The paper identifies a subset of elements (polymorphic or ferromagnetic metals) for which the raw calculated value must be halved to align with experiment; a flag column in the provided input table indicates when this correction applies.

## Reproduction target
Compute the room-temperature linear coefficient of thermal expansion (α) in units of 10⁻⁶ K⁻¹ for a list of 27 metals and 2 semi-metals. Use the bundled file `input_params.csv` (which supplies Cp, Cv, B and a correction flag for each element) together with standard publicly available elemental atomic masses and densities. Output a CSV file `alpha_calc.csv` with two columns: `element` (string) and `alpha_calc` (float).

## Assets

- input_params.csv
- Standard elemental atomic masses and densities: https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ascii=ascii2

## Workflow steps

### Step 1: Compute room-temperature thermal expansion coefficient
- Role: scored (load-bearing)
- Action: Read the bundled input_params.csv to get Cp, Cv, B, and special_flag for each element. Obtain standard density (g/cm³) for each element from public reference data. Compute specific volume V = 1/density (cm³/g). Compute the formula alpha = (1/3) * sqrt((Cp - Cv) / (B * V * 298.15 * 1000)) (this gives alpha in K⁻¹). Convert to units of 10⁻⁶ K⁻¹ by multiplying by 1e6. For elements with special_flag true (Be, Ti, Fe, Ni, Si), multiply the result by 0.5. Write alpha_calc.csv with columns 'element' and 'alpha_calc'.
- Output file: `/app/outputs/alpha_calc.csv`
- Format: csv
- Contract: CSV with header: element,alpha_calc. Each row corresponds to an element. alpha_calc is a floating-point number in units of 10⁻⁶ K⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/alpha_calc.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alpha_calc.csv
- path: `/app/outputs/alpha_calc.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Room-temperature CTE values computed from elastic constants and heat capacities using the Debye–Grüneisen derived formula (eq 5). The checker will recompute each alpha_calc from hidden inputs and public elemental densities, then score element-wise agreement.
- schema:
  - `type`: table
  - `required_columns`: `element`, `alpha_calc`
  - `units`:
    - `alpha_calc`: 10⁻⁶ K⁻¹

Notes: The formula uses Cp, Cv (J/(g·K)), B (GPa), V (cm³/g) from density, and T=298.15 K. The correction factor (multiply by 0.5) applies to Be, Ti, Fe, Ni, Si. The output must be in units of 10⁻⁶ K⁻¹.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alpha_calc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "alpha_calc"
        ],
        "units": {
          "alpha_calc": "10⁻⁶ K⁻¹"
        }
      },
      "description": "Room-temperature CTE values computed from elastic constants and heat capacities using the Debye–Grüneisen derived formula (eq 5). The checker will recompute each alpha_calc from hidden inputs and public elemental densities, then score element-wise agreement."
    }
  ],
  "notes": "The formula uses Cp, Cv (J/(g·K)), B (GPa), V (cm³/g) from density, and T=298.15 K. The correction factor (multiply by 0.5) applies to Be, Ti, Fe, Ni, Si. The output must be in units of 10⁻⁶ K⁻¹."
}
```

## How you are scored
A hidden verifier independently recomputes the CTE for every element using the same formula, a hidden copy of the input parameters, and the same public density data. It compares your computed α value for each element against its own reference. Your final score is the fraction of elements that agree within a predetermined tolerance. Reporting numbers that are not the direct result of the prescribed computation will not suffice; you must faithfully execute the calculation from the given inputs.
