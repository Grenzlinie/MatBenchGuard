# Thermo-mechanical Properties of B2-type FeAl Alloy under Pressure via Statistical Moment Method

## Problem background
B2-type intermetallic FeAl is a candidate for high-temperature applications due to its high melting point and oxidation resistance. Reliable prediction of its thermo‑mechanical properties under pressure is crucial for engineering design. The statistical moment method (SMM) in quantum statistical mechanics provides analytical formulas for the Helmholtz free energy, equation-of-state, and elastic/thermal properties while capturing anharmonic effects and quantum vibrations. This task requires you to implement the SMM for a B2-type FeAl alloy (Fe-40 at.% Al) to compute its lattice constant, elastic moduli, and specific heat at ambient conditions and as functions of pressure.

## Approach
The Helmholtz free energy of the binary alloy is written as a weighted sum of sublattice contributions for Fe and Al, each given by the SMM. Each sublattice free energy depends on a harmonic force constant k, anharmonic coefficients γ₁ and γ₂, and an equilibrium pair interaction energy U₀. These quantities are computed from the interatomic pair potential by summing over the neighbor shells of the B2 (CsCl) structure using the derivatives of the pair potential.

The interatomic interaction is described by the universal binding-energy relation potential:

φ(r) = -p₀ [1 + q₀ (r - r₀)] exp[-q₀ (r - r₀)]

with different parameter sets for Fe-Fe, Al-Al, and Fe-Al pairs (given below). The SMM harmonic parameter k and anharmonic coefficients γ₁, γ₂ are obtained by evaluating the second and fourth derivatives of this potential at the equilibrium neighbor distances.

Once the sublattice parameters are known, the SMM equation-of-state (EOS) relating pressure, temperature, and the nearest-neighbor distance r₁ is formed. Solving this EOS numerically yields r₁(P,T), from which the lattice parameter aₕ = 2/√3·r₁ follows. Isothermal bulk modulus K_T is then obtained from partial contributions of each sublattice, and Young's and shear moduli are derived from K_T using the Poisson's ratio of the alloy (ν = C_Fe·ν_Fe + C_Al·ν_Al with ν_Fe = 0.29, ν_Al = 0.35). The specific heats at constant volume and constant pressure are computed from the temperature derivative of the total energy and the thermal expansion coefficient.

The workflow proceeds in four stages: (1) compute the SMM parameters from the pair potential; (2) solve the EOS for r₁ on the required pressure-temperature grid; (3) evaluate all ambient‑condition properties at T = 300 K, P = 0 GPa; (4) evaluate the pressure‑dependent bulk modulus and specific heat at T = 300 K for P = 0–10 GPa.

## Reproduction target
Compute the following quantities for B2-type Fe–40 at.% Al:
- At T = 300 K and P = 0 GPa: lattice constant aₕ (Å), isothermal bulk modulus K_T (GPa), Young's modulus E_Y (GPa), shear modulus G (GPa), and specific heat at constant pressure C_P (J/(mol·K)).
- At T = 300 K for a set of pressures P = 0, 2, 4, 6, 8, 10 GPa: isothermal bulk modulus K_T (GPa) and specific heat at constant pressure C_P (J/(mol·K)).
Your implementation should follow the SMM procedure outlined above. Submit the results as the two CSV files ambient_properties.csv and pressure_dependence_KT_CP.csv with the exact formats specified in the output contract.

## Assets
No external datasets or pre‑trained models are required. You will need the pair potential parameters for the FeAl system, given below. The crystal structure is B2 (CsCl) with lattice sites occupied by Fe (40 at.%) and Al (60 at.%) – the task uses the Fe‑40 at.% Al composition. Use the following neighbor distances and coordination numbers for the B2 lattice: 1st neighbor (ν₁=1, z₁=8), 2nd neighbor (ν₂=√(4/3) ≈ 1.155, z₂=6), 3rd neighbor (ν₃=√(8/3) ≈ 1.633, z₃=12), 4th neighbor (ν₄=√(11/3) ≈ 1.915, z₄=24), 5th neighbor (ν₅=2, z₅=24). Include at least these shells in your summations.

Pair potential parameters (universal binding-energy relation, φ(r) = -p₀ [1 + q₀ (r - r₀)] exp[-q₀ (r - r₀)]):

| α–β | r₀ (Å) | p₀ (eV) | q₀ (Å⁻¹) |
|------|--------|----------|----------|
| Fe–Fe | 2.803 | 0.482 | 2.020 |
| Al–Al | 3.252 | 0.343 | 1.162 |
| Fe–Al | 2.880 | 0.379 | 1.896 |

Poisson's ratios: ν_Fe = 0.29, ν_Al = 0.35. The alloy Poisson's ratio is ν = C_Fe·ν_Fe + C_Al·ν_Al (Vegard's law).

## Workflow steps

### Step 1: Compute SMM harmonic and anharmonic parameters
- Role: process
- Action: From the universal binding-energy relation pair potential parameters for Fe-Fe, Al-Al, Fe-Al (given) and the B2 crystal structure, compute the SMM harmonic parameter k, anharmonic coefficients γ1, γ2, and equilibrium interaction energy U0 for each sublattice (Fe and Al). Use the coordination shells and neighbor distances of the B2 lattice. Save the computed parameters to a JSON file.
- Evidence: `/app/outputs/smm_parameters.json`

### Step 2: Solve SMM equation-of-state for nearest-neighbor distance
- Role: process
- Action: Form the SMM equation-of-state using the parameters from step 1. Numerically solve for the nearest-neighbor distance r1 as a function of temperature T and pressure P on a grid covering T=300 K and pressures 0, 2, 4, 6, 8, 10 GPa. Compute the lattice parameter a = 2/√3 * r1. Save the solved r1 and a values to a CSV file.
- Evidence: `/app/outputs/solved_r1.csv`

### Step 3: Compute ambient-condition thermo-mechanical properties
- Role: scored (load-bearing)
- Action: Using the solved r1 at T=300 K and P=0 GPa from step 2, compute the lattice constant (Å), isothermal bulk modulus (GPa), Young's modulus (GPa), shear modulus (GPa), and specific heat at constant pressure (J/(mol·K)) via the SMM formulas. Write the results to ambient_properties.csv.
- Output file: `/app/outputs/ambient_properties.csv`
- Format: csv
- Contract: CSV with columns: property (string), value (float). Valid property names: lattice_constant_A, bulk_modulus_GPa, young_modulus_GPa, shear_modulus_GPa, specific_heat_CP_J_per_mol_K.
- Scoring: scored by hidden verifier

### Step 4: Compute pressure-dependent bulk modulus and specific heat
- Role: scored
- Action: Using the solved r1 at T=300 K for pressures 0, 2, 4, 6, 8, 10 GPa from step 2, compute the isothermal bulk modulus (GPa) and specific heat at constant pressure (J/(mol·K)) via the same SMM formulas. Write the results to pressure_dependence_KT_CP.csv.
- Output file: `/app/outputs/pressure_dependence_KT_CP.csv`
- Format: csv
- Contract: CSV with columns: pressure_GPa (float), bulk_modulus_Kt_GPa (float), specific_heat_CP_J_per_mol_K (float). One row per pressure in [0,2,4,6,8,10].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ambient_properties.csv`
- `/app/outputs/pressure_dependence_KT_CP.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ambient_properties.csv
- path: `/app/outputs/ambient_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ambient-condition thermo-mechanical properties of B2 FeAl at T=300 K, P=0 GPa. The checker compares each property to hidden reference values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`
  - `units`:
    - `property`: string (one of lattice_constant_A, bulk_modulus_GPa, young_modulus_GPa, shear_modulus_GPa, specific_heat_CP_J_per_mol_K)
    - `value`: float

### pressure_dependence_KT_CP.csv
- path: `/app/outputs/pressure_dependence_KT_CP.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Pressure-dependent bulk modulus and specific heat at T=300 K for pressures 0–10 GPa. The checker verifies linear trends (slope, R²) and consistency with the ambient file.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `bulk_modulus_Kt_GPa`, `specific_heat_CP_J_per_mol_K`
  - `units`:
    - `pressure_GPa`: float (GPa)
    - `bulk_modulus_Kt_GPa`: float (GPa)
    - `specific_heat_CP_J_per_mol_K`: float (J/(mol·K))

Notes: The hidden checker compares each ambient property to reference values with appropriate tolerances. For the pressure series it checks that the bulk modulus data follows a linear trend with a slope in a specified range and R²>0.99, and that the specific heat decreases with pressure. It also cross-checks the zero-pressure specific heat with the ambient file for consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ambient_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value"
        ],
        "units": {
          "property": "string (one of lattice_constant_A, bulk_modulus_GPa, young_modulus_GPa, shear_modulus_GPa, specific_heat_CP_J_per_mol_K)",
          "value": "float"
        }
      },
      "description": "Ambient-condition thermo-mechanical properties of B2 FeAl at T=300 K, P=0 GPa. The checker compares each property to hidden reference values with tolerances."
    },
    {
      "file": "pressure_dependence_KT_CP.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "bulk_modulus_Kt_GPa",
          "specific_heat_CP_J_per_mol_K"
        ],
        "units": {
          "pressure_GPa": "float (GPa)",
          "bulk_modulus_Kt_GPa": "float (GPa)",
          "specific_heat_CP_J_per_mol_K": "float (J/(mol·K))"
        }
      },
      "description": "Pressure-dependent bulk modulus and specific heat at T=300 K for pressures 0–10 GPa. The checker verifies linear trends (slope, R²) and consistency with the ambient file."
    }
  ],
  "notes": "The hidden checker compares each ambient property to reference values with appropriate tolerances. For the pressure series it checks that the bulk modulus data follows a linear trend with a slope in a specified range and R²>0.99, and that the specific heat decreases with pressure. It also cross-checks the zero-pressure specific heat with the ambient file for consistency."
}
```

## How you are scored
A hidden verifier will independently score each output file and combine the results into a final reward between 0 and 1.

For ambient_properties.csv, the verifier reads the five property values and compares each to a hidden reference result, awarding full credit when the value lies within an allowed tolerance. The weighted sum over the five properties forms the ambient score.

For pressure_dependence_KT_CP.csv, the verifier checks the structural consistency of the pressure series: it verifies that the bulk modulus data follow a precise linear trend with a slope that falls inside a specified range (high R² required), that the specific heat decreases with pressure, and that the specific heat at P = 0 matches the corresponding value in the ambient file. Credit is awarded based on these structural and cross‑consistency checks.

The overall reward is a weighted combination (majority from the ambient file, remainder from the pressure‑series file). Reporting the correct trends and self‑consistent numbers is essential; guessing or hard‑coding numbers from memory will not pass the hidden checks.
