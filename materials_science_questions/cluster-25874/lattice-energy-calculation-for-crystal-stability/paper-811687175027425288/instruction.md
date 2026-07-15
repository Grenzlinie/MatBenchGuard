# Relative Specific Impulse Calculation for Aliphatic Polynitrates

## Problem background
Aliphatic polynitrates are potential high-energy density compounds for use as plasticizers in solid propellants. A critical performance parameter for propellant components is the specific impulse (I_s), which characterizes the thrust produced per unit mass of propellant. This study theoretically computes the I_s of a series of aliphatic polynitrates using a semiempirical method and the Politzer approach. The relative specific impulse, compared to the widely used energetic material HMX, indicates the viability of these compounds as energetic plasticizers.

## Approach
The specific impulse I_s is approximated by the Politzer method as proportional to sqrt(Tc * N), where Tc is the combustion temperature and N is the number of moles of gaseous products per gram of explosive. 

First, gas-phase heats of formation are obtained for each compound using the semiempirical PM3 method. Idealized stoichiometric decomposition reactions are then determined based on the largest exothermic principle: all nitrogen atoms form N2, carbon atoms form CO2 if enough oxygen is available (otherwise elemental carbon), and oxygen preferentially forms H2O before any excess O2 is considered. 

Using the standard heats of formation of the product gases and the computed heat of formation of the explosive, the enthalpy of combustion (ΔH_comb) is calculated. N is derived from the total moles of gaseous products and the molecular weight of the explosive. The combustion temperature Tc is obtained by assuming that the heat of combustion entirely heats the product gases from an initial temperature of 298.15 K, using constant heat capacities for each product gas. Finally, I_s = sqrt(Tc * N) is computed for each compound, and the relative I_s is reported as the ratio of the compound's I_s to the I_s of HMX, which is treated as a reference.

## Reproduction target
Compute the specific impulse I_s and the relative specific impulse (I_s divided by the I_s of HMX) for the eight aliphatic polynitrates: methyl nitrate (MN), ethylene glycol dinitrate (EGDN), nitroglycerine (NG), erythritol tetranitrate (ETN), xylitol pentanitrate (XPN), mannitol hexanitrate (MHN), volemitol heptanitrate (VHN), and 1,2,3,4,5,6,7,8-octanitrate n-octane (ONO), as well as the reference compound HMX. 

Follow the Politzer method: use PM3 to compute gas-phase heats of formation, apply the decomposition rules as described, and use the constant heat capacities (H2O: 33.33, CO2: 37.65, N2: 28.86, C: 8.53 J/(mol·K)) and product heats of formation (H2O: -241.83, CO2: -393.51, N2: 0, C: 0 kJ/mol). Output the results in a CSV file with columns compound, N (mol/g), delta_H_comb (kJ/mol), Tc (K), Is, relative_Is, with one row per compound.

## Assets

- Semiempirical quantum chemistry package (e.g., MOPAC): http://openmopac.net/
- Standard heats of formation and heat capacities of product gases

## Workflow steps

### Step 1: Build structures and compute PM3 heats of formation
- Role: process
- Action: Build molecular structures of MN, EGDN, NG, ETN, XPN, MHN, VHN, ONO, and HMX. Perform geometry optimization and single-point energy calculation using the PM3 semiempirical method to obtain gas-phase heats of formation. Save compound names and their ΔfH values.
- Evidence: `/app/outputs/pm3_heats.csv`

### Step 2: Compute relative specific impulse
- Role: scored (load-bearing)
- Action: For each compound: (1) determine the idealized stoichiometric decomposition reaction based on the largest exothermic principle (N→N2, C→CO2 if oxygen is sufficient, else C; O first to H2O); (2) using the heat of formation from step_01 and the standard heats of formation (H2O: -241.83, CO2: -393.51, N2: 0, C: 0 kJ/mol) compute the enthalpy of combustion ΔH_comb; (3) compute the number of moles of gaseous products per gram N = n/M; (4) compute the combustion temperature Tc assuming the heat of combustion is entirely used to heat the products: -ΔH_comb = Cp_gases (Tc - 298.15 K) with constant Cp (J/(mol·K)): H2O:33.33, CO2:37.65, N2:28.86, C:8.53; (5) compute I_s = sqrt(Tc * N) and relative I_s = I_s / I_s(HMX). Output a CSV file with all intermediate and final results.
- Output file: `/app/outputs/specific_impulse.csv`
- Format: csv
- Contract: Columns: compound (string), N (float, mol/g), delta_H_comb (float, kJ/mol), Tc (float, K), Is (float), relative_Is (float). One row per compound including HMX as reference.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/specific_impulse.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### specific_impulse.csv
- path: `/app/outputs/specific_impulse.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed specific impulse and relative specific impulse for a series of aliphatic polynitrates and HMX.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `N`, `delta_H_comb`, `Tc`, `Is`, `relative_Is`
  - `units`:
    - `N`: mol/g
    - `delta_H_comb`: kJ/mol
    - `Tc`: K
    - `Is`: 
    - `relative_Is`:

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "specific_impulse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "N",
          "delta_H_comb",
          "Tc",
          "Is",
          "relative_Is"
        ],
        "units": {
          "N": "mol/g",
          "delta_H_comb": "kJ/mol",
          "Tc": "K",
          "Is": "",
          "relative_Is": ""
        }
      },
      "description": "Computed specific impulse and relative specific impulse for a series of aliphatic polynitrates and HMX."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted output file specific_impulse.csv will be evaluated by a hidden verifier. The verifier compares your computed Is and relative_Is values for each compound to the correct values that follow from properly executing the Politzer method. Each correctly computed value contributes to the overall reward, which is a weighted sum across all compounds. The primary weighting is on the Is and relative_Is columns. Simply reporting known numbers without having performed the PM3 calculations and the subsequent derivation steps will not receive credit.
