# Pressure-dependent thermo-mechanical properties of B2-type FeAl intermetallic alloy

## Problem background
B2-type FeAl (iron aluminide) intermetallic alloys exhibit high-temperature strength, oxidation resistance, and corrosion resistance, making them candidates for high-temperature structural applications. While many studies have characterized FeAl at ambient pressure, the pressure dependence of its fundamental thermo-mechanical properties — lattice parameter, elastic moduli, and specific heats — has been much less explored. Pressure can significantly alter atomic vibrations and lattice spacing, thereby affecting mechanical and thermal behavior. Understanding these pressure effects is needed to guide applications where the material may experience compressive loading or higher pressures. This task aims to compute the pressure evolution of key thermo-mechanical quantities of B2-type Fe-40 at% Al from a statistical mechanics model, providing theoretical predictions that can help fill the gap left by the scarcity of experimental data at elevated pressures.

## Approach
The calculation uses the statistical moment method (SMM) in quantum statistical mechanics. In this approach, the Helmholtz free energy of the system is expressed as a function of lattice vibration anharmonicity, and the equation of state is derived from the pressure–volume relation. The method accounts for both harmonic and anharmonic (up to fourth-order) contributions to the atomic displacements, capturing the leading effects of thermal expansion and nonlinear elasticity.

For the B2 (CsCl) structure, the free energy is written as a concentration-weighted sum of contributions from Fe and Al atoms, each with its own harmonic parameter k and anharmonic coefficients γ₁, γ₂. These parameters are obtained by taking lattice sums of the derivatives of the interatomic pair potentials over neighbor shells. The equilibrium nearest-neighbor distance (and hence the lattice parameter) at each temperature T and pressure P is found by numerically solving the SMM equation of state.

Once the lattice spacing is known, the isothermal bulk modulus K_T, specific heats at constant volume C_V and constant pressure C_P, and the linear thermal expansion coefficient α_T are computed from the free energy using thermodynamic identities. The alloy's Young's modulus E_Y and shear modulus G are then derived from the bulk modulus using the alloy Poisson ratio ν obtained from Vegard's law: ν = C_Fe ν_Fe + C_Al ν_Al, with the elemental Poisson ratios ν_Fe = 0.29 and ν_Al = 0.35.

The interatomic interactions are described by a universal binding-energy relation (UBER) potential of the form φ(r) = −p₀[1 + q₀(r − r₀)] exp[−q₀(r − r₀)]. The parameters for the three pair types (Fe–Fe, Al–Al, Fe–Al) are given in the following table:

| α–β   | r₀ (Å) | p₀ (eV) | q₀ (Å⁻¹) |
|--------|--------|---------|-----------|
| Fe–Fe | 2.803  | 0.482   | 2.020     |
| Al–Al | 3.252  | 0.343   | 1.162     |
| Fe–Al | 2.880  | 0.379   | 1.896     |

These parameters are used throughout the calculation to evaluate the potential derivatives and lattice sums.

## Reproduction target
Implement the SMM formalism described above and compute the lattice parameter, isothermal bulk modulus, Young's modulus, shear modulus, specific heat at constant volume (C_V), and specific heat at constant pressure (C_P) for a B2-type Fe-40 at% Al alloy at every combination of temperature T ∈ {100, 300, 500, 700, 900} K and pressure P ∈ {0, 2, 4, 6, 8, 10} GPa. Produce the final table of results as a CSV file at /app/outputs/thermo_mechanical_properties.csv with columns: T(K), P(GPa), lattice_parameter(A), bulk_modulus(GPa), youngs_modulus(GPa), shear_modulus(GPa), specific_heat_CV(J/mol.K), specific_heat_CP(J/mol.K). The workflow is outlined in the steps below; all intermediate artifacts must be written to /app/outputs as specified.

## Assets

- FeAl interatomic pair potential parameters
- Poisson's ratios of Fe and Al

## Workflow steps

### Step 1: Compute SMM harmonic and anharmonic parameters
- Role: process
- Action: Using the provided pair potential parameters for Fe-Fe, Al-Al, Fe-Al and the CsCl crystal structure, compute the harmonic parameter k and anharmonic coefficients gamma1 and gamma2 for Fe and Al via lattice sums over neighbor shells, as defined in the statistical moment method.
- Evidence: `/app/outputs/smm_parameters.json`

### Step 2: Solve SMM equation-of-state for lattice parameter
- Role: process
- Action: Using the SMM parameters from step01, numerically solve the SMM equation-of-state to obtain the equilibrium nearest-neighbor distance and lattice parameter for each combination of temperature (100,300,500,700,900 K) and pressure (0,2,4,6,8,10 GPa).
- Evidence: `/app/outputs/lattice_parameter_vs_TP.npy`

### Step 3: Compute thermo-mechanical properties
- Role: scored (load-bearing)
- Action: For each (T,P) combination, compute the isothermal bulk modulus, Young's modulus (using Poisson's ratio from Vegard's law with the provided elemental Poisson's ratios), shear modulus, specific heat at constant volume, and specific heat at constant pressure using the SMM formulas. Write the results to a CSV file.
- Output file: `/app/outputs/thermo_mechanical_properties.csv`
- Format: csv
- Contract: required_columns: ["T(K)", "P(GPa)", "lattice_parameter(A)", "bulk_modulus(GPa)", "youngs_modulus(GPa)", "shear_modulus(GPa)", "specific_heat_CV(J/mol.K)", "specific_heat_CP(J/mol.K)"]; all float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_mechanical_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_mechanical_properties.csv
- path: `/app/outputs/thermo_mechanical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of computed thermo-mechanical properties at the specified (T,P) grid. The checker compares selected entries to hidden reference values from the paper within tolerances and verifies consistency trends (e.g., lattice parameter decreases with pressure, bulk modulus increases linearly).
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `P(GPa)`, `lattice_parameter(A)`, `bulk_modulus(GPa)`, `youngs_modulus(GPa)`, `shear_modulus(GPa)`, `specific_heat_CV(J/mol.K)`, `specific_heat_CP(J/mol.K)`
  - `units`:
    - `lattice_parameter(A)`: angstrom
    - `bulk_modulus(GPa)`: GPa
    - `youngs_modulus(GPa)`: GPa
    - `shear_modulus(GPa)`: GPa
    - `specific_heat_CV(J/mol.K)`: J/(mol·K)
    - `specific_heat_CP(J/mol.K)`: J/(mol·K)

Notes: All property values derive from the SMM free energy expressions and the solved lattice parameter. The hidden reference values are the paper-reported results; scoring uses tolerances that absorb legitimate numerical spread from different solver implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_mechanical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "P(GPa)",
          "lattice_parameter(A)",
          "bulk_modulus(GPa)",
          "youngs_modulus(GPa)",
          "shear_modulus(GPa)",
          "specific_heat_CV(J/mol.K)",
          "specific_heat_CP(J/mol.K)"
        ],
        "units": {
          "lattice_parameter(A)": "angstrom",
          "bulk_modulus(GPa)": "GPa",
          "youngs_modulus(GPa)": "GPa",
          "shear_modulus(GPa)": "GPa",
          "specific_heat_CV(J/mol.K)": "J/(mol·K)",
          "specific_heat_CP(J/mol.K)": "J/(mol·K)"
        }
      },
      "description": "Table of computed thermo-mechanical properties at the specified (T,P) grid. The checker compares selected entries to hidden reference values from the paper within tolerances and verifies consistency trends (e.g., lattice parameter decreases with pressure, bulk modulus increases linearly)."
    }
  ],
  "notes": "All property values derive from the SMM free energy expressions and the solved lattice parameter. The hidden reference values are the paper-reported results; scoring uses tolerances that absorb legitimate numerical spread from different solver implementations."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that examines the artifacts you produce in /app/outputs. For each scored step, the verifier compares your output to reference criteria (hidden from you) that capture the expected physical behavior of the statistical moment method. Simply writing down pre‑existing numbers — whether from a publication or from fabricated data — is not sufficient; you must genuinely execute the computational workflow described in the steps. The verifier checks both the final property table and intermediate evidence, and may also audit internal consistency (e.g., that elastic moduli obey the expected relationship with the alloy Poisson ratio). The final reward is a weighted combination of the step scores; a correct, reproducible computation will achieve a score near 1.0.
