# DFT-based H2 adsorption site and configuration analysis on Fe(III)/ZSM-5 zeolite

## Problem background
Understanding how H₂ molecules adsorb on the Fe(III) active sites in ZSM‑5 zeolite is essential for catalyst preparation and reduction processes. The Fe(III)/ZSM‑5 system is promising for selective oxidation, and its activation under H₂ atmosphere determines the nature and dispersion of active iron species. The goal of this task is to determine, by density functional theory (DFT), the stable geometries and energetics of H₂ chemisorption on a realistic Fe(III)/ZSM‑5 cluster model, providing the adsorption configurations and their associated geometric, energetic, and vibrational signatures.

## Approach
A five‑T‑site cluster is cut from the ZSM‑5 (MFI) crystal structure (Olson et al.) with one Al substituted at a T12 site. Terminal Si–H groups are replaced with Si–OH; the boundary Si and O atoms are frozen at crystallographic coordinates. The Fe(III) centre is placed near the framework. The electronic structure is treated with the B3LYP hybrid functional. The Fe atom uses the LANL2DZ effective core potential with an additional f‑function; H₂ is described by 6‑311++G(d,p); all other atoms (Si, Al, O) use 6‑31G*. All calculations employ an open‑source DFT package (ORCA, PySCF, etc.) that supports these settings. The bare Fe(III)/ZSM‑5 cluster is first optimised in both the high‑spin (sextet) and low‑spin (quartet) states, and stationary points are verified by frequency analysis. Then H₂ is placed near the Fe centre in several initial orientations to obtain stable adsorption complexes. For the sextet state two distinct configurations (labelled ¹Ads and ²Ads) are obtained, and for the quartet state one configuration (³Ads) is obtained. Each adsorption structure is fully optimised and confirmed as a local minimum via harmonic vibrational frequency calculations. From the optimised geometries, key interatomic distances, angles, and the dihedral Oε–Fe–Hₐ–H_b are extracted. The adsorption energy is computed as the total energy difference between the adsorption complex, the bare cluster, and isolated H₂. The H–H stretching frequency is taken from the harmonic frequency calculation and scaled by the factor 0.94 (derived from the ratio of experimental to computed free‑H₂ frequency).

## Reproduction target
Produce a JSON file `adsorption_configurations.json` at `/app/outputs/` containing for each of the three configurations (1Ads, 2Ads, 3Ads) the following quantities: Fe–Hₐ, Fe–H_b, O–Hₐ, O–H_b, H–H, and Fe–Oε distances (in Å); ∠Oε–Fe–Hₐ and ∠Oε–Fe–H_b angles (in degrees); Oε–Fe–Hₐ–H_b dihedral angle (in degrees); the adsorption energy E_ad (in kJ mol⁻¹); and the scaled H–H stretching frequency ν_H–H (in cm⁻¹). All values should be computed by the workflow described, and reported to three decimal places (angles and dihedral to two decimal places, adsorption energy and frequency to one decimal place). The hidden verifier will compare each entry to reference values; a successful reproduction requires completing all DFT steps and extracting the quantities correctly.

## Assets

- ZSM-5 crystallographic structure (MFI topology): http://www.iza-structure.org/databases/
- Open-source DFT software: https://orcaforum.kofo.mpg.de/
- Basis set definitions (EMSL Basis Set Exchange): https://www.basissetexchange.org/

## Workflow steps

### Step 1: Construct the Fe(III)/ZSM-5 cluster model
- Role: process
- Action: Build the initial Fe(III)/ZSM-5 cluster model using the ZSM-5 crystallographic coordinates (Olson et al.). The cluster consists of five T sites with one Al atom substituted at a T12 site. Replace terminal Si–H groups with Si–OH terminations. Freeze the boundary Si and O atoms at their crystallographic positions. Produce a structure file suitable for DFT calculations.
- Evidence: none

### Step 2: Geometry optimisation of bare Fe(III)/ZSM-5 in sextet and quartet states
- Role: process
- Action: Perform DFT geometry optimisations of the bare Fe(III)/ZSM-5 cluster for both the high‑spin (sextet, S = 5/2) and low‑spin (quartet, S = 3/2) electronic states using the B3LYP functional. Use the LANL2DZ effective core potential (ECP) on Fe with an additional f‑function, 6‑31G* basis on Si, Al, and O atoms, and 6‑311++G(d,p) on H atoms (for later H₂ calculations). Confirm that the stationary points are minima via vibrational frequency analysis. Record the final total energies and optimised geometries (Cartesian coordinates).
- Evidence: none

### Step 3: Geometry optimisation of H₂ adsorption on sextet Fe(III)/ZSM-5
- Role: process
- Action: Starting from the optimised sextet cluster, place an H₂ molecule near the Fe(III) site with two distinct initial orientations to obtain the two adsorption configurations termed ¹Ads and ²Ads. Perform DFT geometry optimisations using the same settings as in Step 1. Run vibrational frequency analysis to confirm that each configuration is a true energy minimum. Record the optimised geometries, total energies, and unscaled harmonic H–H stretching frequencies.
- Evidence: none

### Step 4: Geometry optimisation of H₂ adsorption on quartet Fe(III)/ZSM-5
- Role: process
- Action: Starting from the optimised quartet cluster, place an H₂ molecule near Fe(III) to obtain the adsorption configuration ³Ads. Optimise the geometry and perform frequency analysis to confirm it is a minimum. Record the optimised geometry, total energy, and unscaled H–H stretching frequency.
- Evidence: none

### Step 5: Extract adsorption parameters and write scored JSON
- Role: scored (load-bearing)
- Action: From the DFT output files of Steps 1–3 and a separate gas‑phase calculation on isolated H₂ (same functional and basis), extract the following for each of the three adsorption configurations (¹Ads, ²Ads, ³Ads): (i) optimised interatomic distances: Fe–Hₐ, Fe–H_b, O–Hₐ, O–H_b, H–H, Fe–Oε (Å); (ii) angles: ∠Oε–Fe–Hₐ, ∠Oε–Fe–H_b (degrees); (iii) dihedral angle: Oε–Fe–Hₐ–H_b (degrees). Compute the adsorption energy E_ad (kJ mol⁻¹) as E_ad = E(ads complex) – E(bare cluster) – E(isolated H₂) using the total energies. Compute the scaled H–H stretching frequency ν_H–H (cm⁻¹) by taking the unscaled harmonic frequency from the frequency calculation and multiplying by a scaling factor of 0.94 (derived from the ratio of experimental to computed free‑H₂ frequency). Save all values into a JSON file with the structure described in the output contract. All numeric values should be reported to three decimal places.
- Output file: `/app/outputs/adsorption_configurations.json`
- Format: json
- Contract: The single scored artifact containing the reproduced geometric, energetic, and vibrational data for the three H₂ adsorption configurations. This file is unreachable without genuinely executing the DFT process steps.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_configurations.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_configurations.json
- path: `/app/outputs/adsorption_configurations.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains all reproduced geometric parameters, H–H stretching frequency, and adsorption energy for the three H₂ adsorption configurations. The numeric entries are compared to hidden reference values from the paper within tolerances; the file is load‑bearing for the entire workflow.
- schema:
  - `type`: object
  - `required`: `1Ads`, `2Ads`, `3Ads`
  - `properties`:
    - `1Ads`:
      - `type`: object
      - `required`: `Fe_Ha`, `Fe_Hb`, `O_Ha`, `O_Hb`, `H_H`, `Fe_O`, `angle_O_Fe_Ha`, `angle_O_Fe_Hb`, `dihedral_O_Fe_Ha_Hb`, `adsorption_energy_kJ_mol`, `HH_frequency_cm1`
      - `properties`:
        - `Fe_Ha`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `Fe_Hb`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `O_Ha`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `O_Hb`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `H_H`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `Fe_O`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `angle_O_Fe_Ha`:
          - `type`: number
          - `unit`: degree
          - `decimal_places`: 2
        - `angle_O_Fe_Hb`:
          - `type`: number
          - `unit`: degree
          - `decimal_places`: 2
        - `dihedral_O_Fe_Ha_Hb`:
          - `type`: number
          - `unit`: degree
          - `decimal_places`: 2
        - `adsorption_energy_kJ_mol`:
          - `type`: number
          - `unit`: kJ/mol
          - `decimal_places`: 1
        - `HH_frequency_cm1`:
          - `type`: number
          - `unit`: cm⁻¹
          - `decimal_places`: 1
    - `2Ads`:
      - `type`: object
      - `required`: `Fe_Ha`, `Fe_Hb`, `O_Ha`, `O_Hb`, `H_H`, `Fe_O`, `angle_O_Fe_Ha`, `angle_O_Fe_Hb`, `dihedral_O_Fe_Ha_Hb`, `adsorption_energy_kJ_mol`, `HH_frequency_cm1`
      - `properties`:
        - `Fe_Ha`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `Fe_Hb`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `O_Ha`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `O_Hb`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `H_H`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `Fe_O`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `angle_O_Fe_Ha`:
          - `type`: number
          - `unit`: degree
          - `decimal_places`: 2
        - `angle_O_Fe_Hb`:
          - `type`: number
          - `unit`: degree
          - `decimal_places`: 2
        - `dihedral_O_Fe_Ha_Hb`:
          - `type`: number
          - `unit`: degree
          - `decimal_places`: 2
        - `adsorption_energy_kJ_mol`:
          - `type`: number
          - `unit`: kJ/mol
          - `decimal_places`: 1
        - `HH_frequency_cm1`:
          - `type`: number
          - `unit`: cm⁻¹
          - `decimal_places`: 1
    - `3Ads`:
      - `type`: object
      - `required`: `Fe_Ha`, `Fe_Hb`, `O_Ha`, `O_Hb`, `H_H`, `Fe_O`, `angle_O_Fe_Ha`, `angle_O_Fe_Hb`, `dihedral_O_Fe_Ha_Hb`, `adsorption_energy_kJ_mol`, `HH_frequency_cm1`
      - `properties`:
        - `Fe_Ha`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `Fe_Hb`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `O_Ha`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `O_Hb`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `H_H`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `Fe_O`:
          - `type`: number
          - `unit`: Å
          - `decimal_places`: 3
        - `angle_O_Fe_Ha`:
          - `type`: number
          - `unit`: degree
          - `decimal_places`: 2
        - `angle_O_Fe_Hb`:
          - `type`: number
          - `unit`: degree
          - `decimal_places`: 2
        - `dihedral_O_Fe_Ha_Hb`:
          - `type`: number
          - `unit`: degree
          - `decimal_places`: 2
        - `adsorption_energy_kJ_mol`:
          - `type`: number
          - `unit`: kJ/mol
          - `decimal_places`: 1
        - `HH_frequency_cm1`:
          - `type`: number
          - `unit`: cm⁻¹
          - `decimal_places`: 1

Notes: No gold values or tolerances are disclosed. The checker will compare the numeric entries in each adsorption configuration to a reference set derived from the paper using prescribed tolerances (distances ±0.02 Å, angles ±2°, dihedral ±5°, energy ±2 kJ mol⁻¹, frequency ±20 cm⁻¹); additional structural consistency checks (H–H > 0.744 Å, negative adsorption energies, energy ordering) may be applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_configurations.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "1Ads",
          "2Ads",
          "3Ads"
        ],
        "properties": {
          "1Ads": {
            "type": "object",
            "required": [
              "Fe_Ha",
              "Fe_Hb",
              "O_Ha",
              "O_Hb",
              "H_H",
              "Fe_O",
              "angle_O_Fe_Ha",
              "angle_O_Fe_Hb",
              "dihedral_O_Fe_Ha_Hb",
              "adsorption_energy_kJ_mol",
              "HH_frequency_cm1"
            ],
            "properties": {
              "Fe_Ha": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "Fe_Hb": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "O_Ha": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "O_Hb": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "H_H": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "Fe_O": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "angle_O_Fe_Ha": {
                "type": "number",
                "unit": "degree",
                "decimal_places": 2
              },
              "angle_O_Fe_Hb": {
                "type": "number",
                "unit": "degree",
                "decimal_places": 2
              },
              "dihedral_O_Fe_Ha_Hb": {
                "type": "number",
                "unit": "degree",
                "decimal_places": 2
              },
              "adsorption_energy_kJ_mol": {
                "type": "number",
                "unit": "kJ/mol",
                "decimal_places": 1
              },
              "HH_frequency_cm1": {
                "type": "number",
                "unit": "cm⁻¹",
                "decimal_places": 1
              }
            }
          },
          "2Ads": {
            "type": "object",
            "required": [
              "Fe_Ha",
              "Fe_Hb",
              "O_Ha",
              "O_Hb",
              "H_H",
              "Fe_O",
              "angle_O_Fe_Ha",
              "angle_O_Fe_Hb",
              "dihedral_O_Fe_Ha_Hb",
              "adsorption_energy_kJ_mol",
              "HH_frequency_cm1"
            ],
            "properties": {
              "Fe_Ha": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "Fe_Hb": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "O_Ha": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "O_Hb": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "H_H": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "Fe_O": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "angle_O_Fe_Ha": {
                "type": "number",
                "unit": "degree",
                "decimal_places": 2
              },
              "angle_O_Fe_Hb": {
                "type": "number",
                "unit": "degree",
                "decimal_places": 2
              },
              "dihedral_O_Fe_Ha_Hb": {
                "type": "number",
                "unit": "degree",
                "decimal_places": 2
              },
              "adsorption_energy_kJ_mol": {
                "type": "number",
                "unit": "kJ/mol",
                "decimal_places": 1
              },
              "HH_frequency_cm1": {
                "type": "number",
                "unit": "cm⁻¹",
                "decimal_places": 1
              }
            }
          },
          "3Ads": {
            "type": "object",
            "required": [
              "Fe_Ha",
              "Fe_Hb",
              "O_Ha",
              "O_Hb",
              "H_H",
              "Fe_O",
              "angle_O_Fe_Ha",
              "angle_O_Fe_Hb",
              "dihedral_O_Fe_Ha_Hb",
              "adsorption_energy_kJ_mol",
              "HH_frequency_cm1"
            ],
            "properties": {
              "Fe_Ha": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "Fe_Hb": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "O_Ha": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "O_Hb": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "H_H": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "Fe_O": {
                "type": "number",
                "unit": "Å",
                "decimal_places": 3
              },
              "angle_O_Fe_Ha": {
                "type": "number",
                "unit": "degree",
                "decimal_places": 2
              },
              "angle_O_Fe_Hb": {
                "type": "number",
                "unit": "degree",
                "decimal_places": 2
              },
              "dihedral_O_Fe_Ha_Hb": {
                "type": "number",
                "unit": "degree",
                "decimal_places": 2
              },
              "adsorption_energy_kJ_mol": {
                "type": "number",
                "unit": "kJ/mol",
                "decimal_places": 1
              },
              "HH_frequency_cm1": {
                "type": "number",
                "unit": "cm⁻¹",
                "decimal_places": 1
              }
            }
          }
        }
      },
      "description": "Contains all reproduced geometric parameters, H–H stretching frequency, and adsorption energy for the three H₂ adsorption configurations. The numeric entries are compared to hidden reference values from the paper within tolerances; the file is load‑bearing for the entire workflow."
    }
  ],
  "notes": "No gold values or tolerances are disclosed. The checker will compare the numeric entries in each adsorption configuration to a reference set derived from the paper using prescribed tolerances (distances ±0.02 Å, angles ±2°, dihedral ±5°, energy ±2 kJ mol⁻¹, frequency ±20 cm⁻¹); additional structural consistency checks (H–H > 0.744 Å, negative adsorption energies, energy ordering) may be applied."
}
```

## How you are scored
Each configuration (1Ads, 2Ads, 3Ads) is scored individually by a hidden checker. For each configuration the checker compares your reported distances, angles, dihedral, adsorption energy, and H–H frequency to reference values using appropriate tolerances. Geometric parameters (distances, angles, dihedral) contribute a majority of the weight; adsorption energy and H–H frequency each contribute a substantial minority. The checker also verifies structural consistency: all H–H distances must be larger than the equilibrium bond length of free H₂ (0.744 Å), all adsorption energies must be negative, and the relative energies of the three configurations must meet a physically motivated ordering (which the checker verifies without disclosing the reference). Partial credit is awarded for each parameter based on how close it is to the reference, with larger deviations receiving progressively lower reward. The final reward is the weighted sum across all configurations and all fields, reported as a number between 0 and 1. You must faithfully execute the DFT workflow and extract the quantities from your calculations; simply copying numbers from an external source will fail because the checker expects values consistent with the specific basis sets, functional, and cluster model defined in this task.
