# DFT-calculated N2O adsorption and decomposition energies on Ga-ZSM-5

## Problem background
Nitrous oxide (N₂O) is a potent greenhouse gas that also contributes to ozone layer depletion. Catalytic decomposition over metal-exchanged zeolites, such as gallium-exchanged ZSM-5 (Ga-ZSM-5), is a promising abatement strategy. Understanding the reaction mechanism and energetics at the atomic level helps guide catalyst design. Density functional theory (DFT) calculations can provide quantitative insight into the adsorption, dissociation, and oxygen desorption steps on the active sites.

## Approach
Represent the zeolite active site using a 3T cluster (AlSi₂O₄H₈) cut from the ZSM-5 crystal structure (Al at the T12 position). Dangling bonds are saturated with hydrogen atoms. Two cation forms are considered: reduced mononuclear [Ga]⁺ and the oxo species [Ga=O]⁺, each coordinated to two framework oxygen atoms near the Al atom. DFT calculations at the B3LYP level with the 6-31+G(d) basis set are used for full geometry optimizations, harmonic vibrational frequency analyses, and transition state searches. The reaction pathway consists of N₂O adsorption (through both O-end and N-end orientations), O–N bond cleavage to release N₂ and form an oxidized surface species, and a second analogous step on the oxo site, followed by O₂ desorption. All thermodynamic corrections are evaluated at 298 K. The target quantities are computed from the electronic energies, zero-point energies, and thermal corrections of the optimized complexes and transition states.

## Reproduction target
Compute the key energetic and structural quantities for N₂O adsorption and decomposition on the 3T cluster models of Ga-ZSM-5 and GaO-ZSM-5. Specifically:
- Adsorption energies (ΔE_ads) and enthalpies at 298 K (ΔH_ads) for N₂O bound via O-end and N-end on both the reduced Ga⁺ site and the oxo GaO⁺ site.
- Activation energies for N₂O dissociation on the Ga and GaO sites.
- Enthalpy and Gibbs free energy change for O₂ desorption from the GaO₂ species.
- Selected bond distances (Ga–ligand, O–N, N–N, Ga=O) and Mulliken charges for each complex.
Report all results in a structured JSON file (`reproduction_results.json`) according to the schema specified in the output contract.

## Assets

- ZSM-5 zeolite crystal structure (MFI framework): https://www.iza-structure.org/databases/
- Open-source quantum chemistry software supporting DFT/B3LYP and 6-31+G(d) basis set: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Build ZSM-5 3T cluster models
- Role: process
- Action: Construct the 3T cluster (AlSi2O4H8) from the MFI ZSM-5 crystal structure (Al at T12 site), saturate dangling bonds with H atoms, and place Ga+ or GaO+ cation coordinated to two O atoms near Al. Prepare initial geometries for all required species: 3T-Ga, 3T-Ga=O, 3T-GaO2, and free N2O.
- Evidence: `/app/outputs/initial_structures.xyz`

### Step 2: Optimize isolated species and compute vibrational frequencies
- Role: process
- Action: Perform full geometry optimization and harmonic frequency calculation at B3LYP/6-31+G(d) level for 3T-Ga, 3T-Ga=O, 3T-GaO2, and free N2O. Obtain total electronic energies, zero-point energies, and thermodynamic corrections (H and G at 298 K).
- Evidence: `/app/outputs/isolated_energies.json`

### Step 3: Optimize N2O adsorption complexes on 3T-Ga
- Role: process
- Action: Starting from optimized 3T-Ga and N2O, build and optimize the O-end (3T-Ga ONN) and N-end (3T-Ga NNO) adsorption complexes. Run vibrational frequency analysis to obtain thermodynamic corrections and frequency shifts.
- Evidence: `/app/outputs/optimized_3t_ga_onn.xyz, optimized_3t_ga_nno.xyz`

### Step 4: Optimize N2O adsorption complexes on 3T-Ga=O
- Role: process
- Action: Similarly, build and optimize the O-end (3T-Ga=O ONN) and N-end (3T-Ga=O NNO) complexes. Compute vibrational frequencies.
- Evidence: `/app/outputs/optimized_3t_gao_onn.xyz, optimized_3t_gao_nno.xyz`

### Step 5: Locate transition state for N2O dissociation on 3T-Ga
- Role: process
- Action: From the 3T-Ga ONN complex, perform a transition state search for O-N bond cleavage (→ N2 + 3T-Ga=O). Verify with a single imaginary frequency and intrinsic reaction coordinate (IRC). Save TS geometry and energy.
- Evidence: `/app/outputs/ts1_geometry.xyz`

### Step 6: Locate transition state for N2O dissociation on 3T-Ga=O
- Role: process
- Action: From the 3T-Ga=O ONN complex, locate the transition state for the second decomposition step (→ N2 + 3T-GaO2). Verify with one imaginary frequency and IRC. Save TS geometry and energy.
- Evidence: `/app/outputs/ts2_geometry.xyz`

### Step 7: Optimize 3T-GaO2 complex
- Role: process
- Action: Optimize the geometry of the 3T-GaO2 cluster (product of the second dissociation). Compute frequencies to obtain thermodynamic corrections needed for O2 desorption energy.
- Evidence: `/app/outputs/optimized_3t_gao2.xyz`

### Step 8: Compute all reportable quantities and write reproduction_results.json
- Role: scored (load-bearing)
- Action: Using the total energies and thermodynamic corrections from all previous steps, calculate: (a) adsorption energies ΔE_ads and ΔH_ads for the four adsorption complexes; (b) activation energies E_act for dissociation on Ga and GaO sites; (c) O2 desorption ΔH and ΔG from 3T-GaO2; (d) selected bond distances (Ga-ligand, O-N, N-N, Ga=O) from optimized geometries; (e) Mulliken charges (Q(Ga), Q(N2O), and Q(O) for oxo) from wavefunctions. Write these numerical results into `reproduction_results.json` according to the schema.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: {
  "adsorption_energies": {
    "3T-Ga_ONN": { "Delta_E_ads_kcal_per_mol": float, "Delta_H_ads_kcal_per_mol": float, "Ga_molecule_distance_A": float, "O_N_bond_A": float, "N_N_bond_A": float, "Mulliken_Q_Ga": float, "Mulliken_Q_N2O": float },
    "3T-Ga_NNO": { ... },
    "3T-Ga=O_ONN": { ..., "Ga=O_bond_A": float, "Mulliken_Q_O_oxo": float },
    "3T-Ga=O_NNO": { ... }
  },
  "activation_energies_kcal_per_mol": { "Ga_site": float, "GaO_site": float },
  "O2_desorption": { "Delta_H_kcal_per_mol": float, "Delta_G_kcal_per_mol": float }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the key reproduced quantities: adsorption energies and structures for the four adsorption complexes (3T-Ga and 3T-Ga=O, both O-end and N-end), activation energies for N2O dissociation on Ga and GaO sites, and O2 desorption thermodynamics from 3T-GaO2.
- schema:
  - `type`: object
  - `required`: `adsorption_energies`, `activation_energies_kcal_per_mol`, `O2_desorption`
  - `properties`:
    - `adsorption_energies`:
      - `type`: object
      - `required`: `3T-Ga_ONN`, `3T-Ga_NNO`, `3T-Ga=O_ONN`, `3T-Ga=O_NNO`
      - `properties`:
        - `3T-Ga_ONN`:
          - `type`: object
          - `required`: `Delta_E_ads_kcal_per_mol`, `Delta_H_ads_kcal_per_mol`, `Ga_molecule_distance_A`, `O_N_bond_A`, `N_N_bond_A`, `Mulliken_Q_Ga`, `Mulliken_Q_N2O`
        - `3T-Ga_NNO`:
          - `type`: object
          - `required`: `Delta_E_ads_kcal_per_mol`, `Delta_H_ads_kcal_per_mol`, `Ga_molecule_distance_A`, `O_N_bond_A`, `N_N_bond_A`, `Mulliken_Q_Ga`, `Mulliken_Q_N2O`
        - `3T-Ga=O_ONN`:
          - `type`: object
          - `required`: `Delta_E_ads_kcal_per_mol`, `Delta_H_ads_kcal_per_mol`, `Ga_molecule_distance_A`, `O_N_bond_A`, `N_N_bond_A`, `Ga=O_bond_A`, `Mulliken_Q_Ga`, `Mulliken_Q_N2O`, `Mulliken_Q_O_oxo`
        - `3T-Ga=O_NNO`:
          - `type`: object
          - `required`: `Delta_E_ads_kcal_per_mol`, `Delta_H_ads_kcal_per_mol`, `Ga_molecule_distance_A`, `O_N_bond_A`, `N_N_bond_A`, `Ga=O_bond_A`, `Mulliken_Q_Ga`, `Mulliken_Q_N2O`, `Mulliken_Q_O_oxo`
    - `activation_energies_kcal_per_mol`:
      - `type`: object
      - `required`: `Ga_site`, `GaO_site`
    - `O2_desorption`:
      - `type`: object
      - `required`: `Delta_H_kcal_per_mol`, `Delta_G_kcal_per_mol`

Notes: All energies in kcal/mol, distances in Å, charges in e. The hidden checker compares each numeric field to the paper-reported reference values using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "adsorption_energies",
          "activation_energies_kcal_per_mol",
          "O2_desorption"
        ],
        "properties": {
          "adsorption_energies": {
            "type": "object",
            "required": [
              "3T-Ga_ONN",
              "3T-Ga_NNO",
              "3T-Ga=O_ONN",
              "3T-Ga=O_NNO"
            ],
            "properties": {
              "3T-Ga_ONN": {
                "type": "object",
                "required": [
                  "Delta_E_ads_kcal_per_mol",
                  "Delta_H_ads_kcal_per_mol",
                  "Ga_molecule_distance_A",
                  "O_N_bond_A",
                  "N_N_bond_A",
                  "Mulliken_Q_Ga",
                  "Mulliken_Q_N2O"
                ]
              },
              "3T-Ga_NNO": {
                "type": "object",
                "required": [
                  "Delta_E_ads_kcal_per_mol",
                  "Delta_H_ads_kcal_per_mol",
                  "Ga_molecule_distance_A",
                  "O_N_bond_A",
                  "N_N_bond_A",
                  "Mulliken_Q_Ga",
                  "Mulliken_Q_N2O"
                ]
              },
              "3T-Ga=O_ONN": {
                "type": "object",
                "required": [
                  "Delta_E_ads_kcal_per_mol",
                  "Delta_H_ads_kcal_per_mol",
                  "Ga_molecule_distance_A",
                  "O_N_bond_A",
                  "N_N_bond_A",
                  "Ga=O_bond_A",
                  "Mulliken_Q_Ga",
                  "Mulliken_Q_N2O",
                  "Mulliken_Q_O_oxo"
                ]
              },
              "3T-Ga=O_NNO": {
                "type": "object",
                "required": [
                  "Delta_E_ads_kcal_per_mol",
                  "Delta_H_ads_kcal_per_mol",
                  "Ga_molecule_distance_A",
                  "O_N_bond_A",
                  "N_N_bond_A",
                  "Ga=O_bond_A",
                  "Mulliken_Q_Ga",
                  "Mulliken_Q_N2O",
                  "Mulliken_Q_O_oxo"
                ]
              }
            }
          },
          "activation_energies_kcal_per_mol": {
            "type": "object",
            "required": [
              "Ga_site",
              "GaO_site"
            ]
          },
          "O2_desorption": {
            "type": "object",
            "required": [
              "Delta_H_kcal_per_mol",
              "Delta_G_kcal_per_mol"
            ]
          }
        }
      },
      "description": "JSON file containing the key reproduced quantities: adsorption energies and structures for the four adsorption complexes (3T-Ga and 3T-Ga=O, both O-end and N-end), activation energies for N2O dissociation on Ga and GaO sites, and O2 desorption thermodynamics from 3T-GaO2."
    }
  ],
  "notes": "All energies in kcal/mol, distances in Å, charges in e. The hidden checker compares each numeric field to the paper-reported reference values using appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently scores each scored workflow stage's output artifact. It compares the numeric values in your `reproduction_results.json` against reference values using appropriate tolerances and checks required relative trends. The final reward is a weighted combination of these stage scores. Simply reporting the paper's published numbers is not sufficient; the verifier expects results derived from your own DFT calculations following the described workflow.
