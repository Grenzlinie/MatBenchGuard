# Thermodynamic equilibrium composition of B-N-H-F-Si-C-O system for BN CVD/CVI

## Problem background
This task addresses the chemical vapor deposition/infiltration (CVD/CVI) of boron nitride (BN) from a BF3–NH3 precursor. BN interphases are critical in ceramic matrix composites for improving toughness and oxidation resistance. The CVD/CVI process involves complex gas-phase and surface reactions, and the properties of the deposited BN depend on the substrate material and possible contaminants. In particular, the interaction between the precursor gas mixture and various substrate materials (inert, carbon, silica, SiC, SiC/SiO2) can significantly alter the deposition chemistry, potentially attacking the substrate and influencing the BN conversion yield. Understanding these chemical phenomena is essential for designing robust manufacturing processes. This task aims to evaluate the equilibrium state of the B-N-H-F-Si-C-O system under relevant processing conditions by thermodynamic modeling, thereby providing insight into the conditions that favor BN formation and the extent of substrate corrosion.

## Approach
The analysis employs a Gibbs free energy minimization approach. For a given initial composition, temperature, and total pressure, the equilibrium composition of gas and condensed phases is computed by minimizing the total Gibbs free energy of the system subject to atomic mass balance constraints. The system includes many gaseous and condensed species containing the elements B, N, H, F, Si, C, O. Thermodynamic data (Gibbs free energies as functions of temperature) are obtained from public thermochemical databases and supplementary sources. The procedure is applied to a set of well-defined initial conditions that represent different substrate materials (inert, carbon, silica, SiC, SiC/SiO2) and an oxygen contamination case. From the equilibrium solution, gas-phase mole fractions, condensed-phase mole numbers, and derived quantities (BN conversion yield and substrate consumption values) are calculated and reported.

## Reproduction target
You must compute the equilibrium state of the B-N-H-F-Si-C-O system at temperature T = 1323 K and total pressure P = 10 kPa for the following six initial composition scenarios:

1. **Inert substrate**: no additional solid material; reactant ratio α = [NH3]in/[BF3]in = 4.6 with [BF3]in = 1 mol.
2. **Carbon substrate**: add 10 mol C (graphite); α = 4.6.
3. **Silica substrate**: add 10 mol SiO2 (solid); α = 4.6.
4. **SiC substrate**: add 10 mol SiC (solid); α = 4.6.
5. **SiC/SiO2 substrate**: add 8 mol SiC + 2 mol SiO2; α = 4.6.
6. **Oxygen contamination (inert substrate)**: α = 5 ([NH3]in = 5 mol), add 1 mol O2.

For each scenario, report:
- **Gas-phase mole fractions** of all gaseous species present in the equilibrium mixture.
- **Condensed-phase mole numbers** (in mol) of all solid/liquid phases.
- **η_BN**: the thermodynamic conversion yield of BF3 into BN, expressed as a percentage.
- **γ_BF3**: the consumption value of BF3 (in mol).
- Additional consumption values **γ_C**, **γ_SiC**, **γ_SiO2** when the corresponding substrate is present (as defined in the paper's Appendix A).

The final output must be a single JSON file with the exact structure described in the output contract.

## Assets

- NIST-JANAF Thermochemical Tables: https://janaf.nist.gov/
- Thermodynamic data for SiB3, SiB6 (Métais DEA report, 1987)
- Thermodynamic data for Si2N2O, Si3N4 (Hendry, Nitrogen Ceramics, 1977)
- Cantera (open-source thermodynamic library): cantera

## Workflow steps

### Step 1: Compile thermochemical dataset and species list
- Role: process
- Action: Assemble the thermodynamic dataset for all gaseous and condensed species in the B-N-H-F-Si-C-O system listed in Table 1 of the paper. Obtain standard free energy data from NIST-JANAF and supplementary sources for SiB3, SiB6 (Métais) and Si2N2O, Si3N4 (Hendry). Represent each species' Gibbs free energy as a function of temperature (e.g., NASA polynomial coefficients). Produce a structured dataset ready for use in a Gibbs free energy minimizer.
- Evidence: `/app/outputs/step_01_thermo_data.json`

### Step 2: Gibbs free energy minimization and derived quantities
- Role: scored (load-bearing)
- Action: Perform Gibbs free energy minimization for the B-N-H-F-Si-C-O system at T=1323 K and total pressure P=10 kPa for six initial compositions: (i) inert substrate, α=4.6; (ii) carbon substrate (10 mol C), α=4.6; (iii) silica substrate (10 mol SiO2), α=4.6; (iv) SiC substrate (10 mol SiC), α=4.6; (v) SiC/SiO2 substrate (8 mol SiC + 2 mol SiO2), α=4.6; (vi) inert substrate with O2 contamination (1 mol O2), α=5. Use the thermodynamic data from step 01 and enforce elemental mass balances. From the equilibrium solution, compute: gas-phase mole fractions for all present species, mole numbers of all condensed phases, the BN thermodynamic conversion yield η_BN (%), and the consumption values γ_BF3, γ_C, γ_SiC, γ_SiO2 where applicable, following the definitions in Appendix A of the paper.
- Output file: `/app/outputs/step_02_equilibrium_results.json`
- Format: json
- Contract: A JSON object with keys for each scenario: "inert", "carbon", "silica", "SiC", "SiC_SiO2", "inert_O2". Each scenario value is an object with keys: "gas" (object mapping species name to mole fraction float), "condensed" (object mapping species name to mole number float), "eta_BN" (float, percentage), "gamma_BF3" (float, mol), and substrate-specific keys "gamma_C", "gamma_SiC", "gamma_SiO2" (floats) only when applicable. Example: {"inert": {"gas": {"H2": 0.66476, ...}, "condensed": {"BN": 0.075899, ...}, "eta_BN": 7.58, "gamma_BF3": 0.0816}}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_equilibrium_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_equilibrium_results.json
- path: `/app/outputs/step_02_equilibrium_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing equilibrium gas-phase mole fractions, condensed-phase mole numbers, and derived BN yield and substrate consumption values for six substrate conditions at T=1323 K, P=10 kPa. All numeric values are compared to hidden reference data extracted from the paper's Tables 2, 3, 5 and 6 within hidden tolerances.
- schema:
  - `type`: object
  - `required`:
    - `inert`: object with gas, condensed, eta_BN, gamma_BF3
    - `carbon`: object with gas, condensed, eta_BN, gamma_BF3, gamma_C
    - `silica`: object with gas, condensed, eta_BN, gamma_BF3, gamma_SiO2
    - `SiC`: object with gas, condensed, eta_BN, gamma_BF3, gamma_SiC
    - `SiC_SiO2`: object with gas, condensed, eta_BN, gamma_BF3, gamma_SiC, gamma_SiO2
    - `inert_O2`: object with gas, condensed, eta_BN, gamma_BF3
  - `items`: object
  - `required_columns`:
  - `units`:
    - `gas`: mole fraction (unitless, sum ~1)
    - `condensed`: mole number (mol)
    - `eta_BN`: percentage (%)
    - `gamma_*`: mole number (mol)

Notes: The hidden gold values are taken from the published tables in the source work. Tolerances are set to account for differences in the minimizer implementation and thermodynamic data representation, while ensuring a faithful reproduction of the main equilibrium features.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_equilibrium_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "inert": "object with gas, condensed, eta_BN, gamma_BF3",
          "carbon": "object with gas, condensed, eta_BN, gamma_BF3, gamma_C",
          "silica": "object with gas, condensed, eta_BN, gamma_BF3, gamma_SiO2",
          "SiC": "object with gas, condensed, eta_BN, gamma_BF3, gamma_SiC",
          "SiC_SiO2": "object with gas, condensed, eta_BN, gamma_BF3, gamma_SiC, gamma_SiO2",
          "inert_O2": "object with gas, condensed, eta_BN, gamma_BF3"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "gas": "mole fraction (unitless, sum ~1)",
          "condensed": "mole number (mol)",
          "eta_BN": "percentage (%)",
          "gamma_*": "mole number (mol)"
        }
      },
      "description": "Scored artifact containing equilibrium gas-phase mole fractions, condensed-phase mole numbers, and derived BN yield and substrate consumption values for six substrate conditions at T=1323 K, P=10 kPa. All numeric values are compared to hidden reference data extracted from the paper's Tables 2, 3, 5 and 6 within hidden tolerances."
    }
  ],
  "notes": "The hidden gold values are taken from the published tables in the source work. Tolerances are set to account for differences in the minimizer implementation and thermodynamic data representation, while ensuring a faithful reproduction of the main equilibrium features."
}
```

## How you are scored
Your work is scored by a hidden verifier that reads the output file `step_02_equilibrium_results.json`. The verifier independently checks each numeric value (gas mole fractions, condensed mole numbers, η_BN, γ values) against reference values derived from thermodynamic calculations. Rewards are awarded per scenario, with partial credit based on how closely your computed numbers agree with the reference. The scores from all scenarios and all validated quantities are combined with weights to produce a final reward between 0 and 1. To earn full credit, your minimization must accurately capture the equilibrium compositions and derived yields. Providing only the paper's reported numbers without actually performing the computation will not pass, because the verifier checks detailed values that cannot be guessed.
