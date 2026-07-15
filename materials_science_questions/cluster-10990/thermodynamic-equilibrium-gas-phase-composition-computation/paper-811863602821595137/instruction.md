# Bi and Bi-O Vapor Equilibrium Partial Pressure Computation

## Problem background
In high‑temperature pyrometallurgy, knowledge of vapor‑phase speciation over bismuth is critical for understanding impurity behavior, particularly in copper smelting. This task evaluates the vapor species of bismuth and bismuth oxides at elevated temperatures. Using published thermodynamic data, consistent standard Gibbs free energy equations are derived for gaseous Bi, Bi₂, Bi₃, Bi₄, BiO, Bi₂O (linear and angular configurations), Bi₂O₂, Bi₂O₃, Bi₃O₄, and Bi₄O₆. These equations are then employed to compute equilibrium partial pressures of the species as functions of temperature and imposed partial pressures of Bi and O₂, revealing which species dominate under conditions relevant to copper smelting.

## Approach
The thermodynamic analysis proceeds by compiling data from several public references:
- Heat capacities of solid and liquid bismuth, heat of fusion, standard Gibbs energy changes for vaporization of Bi(l) and dissociation of Bi₂ (from Pankratz 1982).
- Standard Gibbs energy functions and enthalpies of formation for all oxide species (from Sidorov et al. 1980).
- Thermochemical data for O₂ (from JANAF, 1971).
- Published partial pressure and dissociation data for Bi₃ and Bi₄ (from Sullivan et al. 1972, Rovner et al. 1967, and Kohl et al. 1967).

For the pure bismuth vapor species, standard Gibbs energy equations of the form ΔG° = A + B T are obtained. The values for Bi and Bi₂ are taken directly from Pankratz, while the coefficients for Bi₃ and Bi₄ are determined by linear regression of the combined experimental data. For the oxide species, the Gibbs energy function data from Sidorov et al. are fitted linearly over 800–1200 K and extrapolated to 1600 K. These functions are combined with the elemental Bi and O₂ thermodynamic functions and the standard enthalpies of formation to yield five‑parameter equations ΔG° = A + B T + C T ln(T) + D T² + E / T. All equations are then used to compute equilibrium partial pressures at specified temperature and gas‑phase compositions via ΔG° = –RT ln K and the law of mass action, assuming ideal gas behavior.

## Reproduction target
From the derived Gibbs energy equations, compute the equilibrium partial pressures (in Pa) of the 11 vapor species at T = 1400 K under two imposed gas conditions:
Condition A: P_Bi = 1.01 Pa, P_O₂ = 1.01 × 10⁻³ Pa.
Condition B: P_Bi = 1.01 × 10³ Pa, P_O₂ = 1.01 × 10⁻³ Pa.
Output the results to the file `step_04_partial_pressures.csv` with one row per species per condition. The hidden verifier will compare each partial pressure against reference values computed from the same thermodynamic procedure (using the standard‑state equations) and will assess whether the relative error falls within a pre‑defined tolerance for each species. Your goal is to have every species–condition pair within its tolerance by correctly re‑deriving the equations and solving the equilibrium relations.

## Assets

- Pankratz (1982) - Thermodynamic Properties of Elements and Oxides (USBM Bulletin 672)
- JANAF Thermochemical Tables (1971): https://janaf.nist.gov/
- Sidorov et al. (1980) - Gibbs energy functions for bismuth oxides
- Sullivan et al. (1972) - Data for Bi3
- Rovner et al. (1967) - Data for Bi3 and Bi4
- Kohl et al. (1967) - Data for Bi4

## Workflow steps

### Step 1: Compile Thermodynamic Data from Public Literature
- Role: process
- Action: Extract and organize the required thermodynamic values from the cited literature: heat capacities of Bi(s) and Bi(l), heat of fusion, standard Gibbs energy changes for vaporization of Bi(l) and dissociation of Bi2 (Pankratz 1982); Gibbs energy function tables and standard enthalpies of formation for all oxide species (Sidorov et al. 1980); experimental partial pressure data for Bi3 and Bi4 (Sullivan et al., Rovner et al., Kohl et al.). Store in a structured JSON file.
- Evidence: `/app/outputs/compiled_thermo_data.json`

### Step 2: Derive Pure Bismuth Gibbs Energy Equations
- Role: process
- Action: Using the compiled data, obtain standard Gibbs energy change equations of the form ΔG° = A + BT (J/mol) for: Bi(l) → Bi(g); Bi2(g) → 2 Bi(g); Bi3(g) → 3 Bi(g); Bi4(g) → 4 Bi(g). For Bi and Bi2, adopt the values directly from Pankratz. For Bi3 and Bi4, perform linear regression on the combined published data to determine A and B coefficients. Equations are valid for 544.59–1600 K.
- Evidence: `/app/outputs/pure_bi_equations.json`

### Step 3: Derive Oxide Gibbs Energy Equations
- Role: process
- Action: For each oxide species (BiO, Bi2O linear, Bi2O angular, Bi2O2, Bi2O3, Bi3O4, Bi4O6): (1) fit a linear curve to the Gibbs energy function vs. temperature using Sidorov's tabulated data over 800–1200 K and extrapolate to 1600 K; (2) combine the extrapolated functions with elemental Bi (Pankratz) and O2 (JANAF) thermodynamic data and the standard enthalpy of formation (Sidorov) to derive the five-parameter equation ΔG° = A + B T + C T ln T + D T^2 + E T^{-1}. Validate that correlation coefficients exceed 0.99.
- Evidence: `/app/outputs/oxide_equations.json`

### Step 4: Compute Equilibrium Partial Pressures
- Role: scored (load-bearing)
- Action: Using all derived Gibbs energy equations, calculate the equilibrium partial pressures (Pa) of the 11 vapor species under two conditions assuming ideal gas behavior and using ΔG° = -RT ln K with the law of mass action. Condition A: T = 1400 K, P_Bi = 1.01 Pa, P_O2 = 1.01e-3 Pa. Condition B: T = 1400 K, P_Bi = 1.01e3 Pa, P_O2 = 1.01e-3 Pa. Write results to a CSV file.
- Output file: `/app/outputs/step_04_partial_pressures.csv`
- Format: csv
- Contract: CSV with columns: species (string), T (float, K), P_Bi_set (float, Pa), P_O2_set (float, Pa), P_partial (float, Pa). The species column must contain exactly the following 11 names (one row per species per condition): Bi, Bi2, Bi3, Bi4, BiO, Bi2O_linear, Bi2O_angular, Bi2O2, Bi2O3, Bi3O4, Bi4O6.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_partial_pressures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_partial_pressures.csv
- path: `/app/outputs/step_04_partial_pressures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium partial pressures of the 11 Bi and Bi-O vapor species at T=1400 K under the two specified (P_Bi, P_O2) conditions. The species column must exclusively use the listed names. The hidden checker compares each species' partial pressure against a reference derived from the same thermodynamic procedure using the public data, with species-specific relative error tolerances.
- schema:
  - `type`: table
  - `required_columns`: `species`, `T`, `P_Bi_set`, `P_O2_set`, `P_partial`
  - `column_types`:
    - `species`: string
    - `T`: float
    - `P_Bi_set`: float
    - `P_O2_set`: float
    - `P_partial`: float
  - `units`:
    - `T`: K
    - `P_Bi_set`: Pa
    - `P_O2_set`: Pa
    - `P_partial`: Pa
  - `allowed_species`: `Bi`, `Bi2`, `Bi3`, `Bi4`, `BiO`, `Bi2O_linear`, `Bi2O_angular`, `Bi2O2`, `Bi2O3`, `Bi3O4`, `Bi4O6`

Notes: The hidden reference values are computed from the standard Gibbs energy equations that would result from correctly following the preceding process steps. The agent must implement the full derivation pipeline; the scored step is load-bearing and only yields correct pressures if the equations are correctly derived. Listing the required species names ensures the checker can map rows unambiguously.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_partial_pressures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "T",
          "P_Bi_set",
          "P_O2_set",
          "P_partial"
        ],
        "column_types": {
          "species": "string",
          "T": "float",
          "P_Bi_set": "float",
          "P_O2_set": "float",
          "P_partial": "float"
        },
        "units": {
          "T": "K",
          "P_Bi_set": "Pa",
          "P_O2_set": "Pa",
          "P_partial": "Pa"
        },
        "allowed_species": [
          "Bi",
          "Bi2",
          "Bi3",
          "Bi4",
          "BiO",
          "Bi2O_linear",
          "Bi2O_angular",
          "Bi2O2",
          "Bi2O3",
          "Bi3O4",
          "Bi4O6"
        ]
      },
      "description": "Equilibrium partial pressures of the 11 Bi and Bi-O vapor species at T=1400 K under the two specified (P_Bi, P_O2) conditions. The species column must exclusively use the listed names. The hidden checker compares each species' partial pressure against a reference derived from the same thermodynamic procedure using the public data, with species-specific relative error tolerances."
    }
  ],
  "notes": "The hidden reference values are computed from the standard Gibbs energy equations that would result from correctly following the preceding process steps. The agent must implement the full derivation pipeline; the scored step is load-bearing and only yields correct pressures if the equations are correctly derived. Listing the required species names ensures the checker can map rows unambiguously."
}
```

## How you are scored
A hidden verifier reads your `step_04_partial_pressures.csv` and, for each of the 11 species at both conditions, computes the relative error of your reported partial pressure against a hidden reference value. The reference values are generated from the standard‑state equations that would result from correctly executing the preceding data‑compilation and equation‑derivation steps. The species are grouped into major (Bi, Bi₂, BiO, Bi₂O) and minor (all others), with a tighter tolerance for the major species. Your final reward is the fraction of the 22 species–condition pairs whose relative error meets the tolerance for that species; a perfect score of 1.0 requires all pairs to pass. The hidden tolerances are chosen to distinguish a genuine re‑derivation from a generic guess, so simply reporting plausible‑looking pressures without properly following the workflow will not yield a high reward.
