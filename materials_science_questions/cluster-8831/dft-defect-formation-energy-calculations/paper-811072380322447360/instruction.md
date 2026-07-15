# DFT Defect Formation Volume Calculations in B2-FeAl using Supercell Approach

## Problem background
Intermetallic compounds like B2-FeAl are promising for high-temperature applications. Understanding point-defect properties is essential for interpreting pressure-dependent experiments such as positron annihilation spectroscopy and diffusion measurements. In a compound, individual defects cannot be created in isolation; instead, multiple defect types must appear simultaneously to preserve composition and homogeneity. Their concentrations are therefore governed by a generalized grandcanonical formalism, which implies that the effective formation volume of a defect (defined as the pressure derivative of its concentration at constant temperature) depends on the energies and local relaxation volumes of all defect types, not solely on the simple geometrical volume change of an isolated defect. This task computes these defect parameters from first-principles density functional theory (DFT) and uses them to obtain the effective formation volumes for four atomic defects in B2-FeAl.

## Approach
The workflow uses ab-initio pseudopotential DFT supercell calculations on 32-atom B2-FeAl supercells containing one point defect (Fe vacancy, Al vacancy, Fe antisite, Al antisite) plus a perfect supercell reference. For each supercell, total energies are computed at several fixed volumes, atomic positions are relaxed at fixed volume, and then the supercell volume is relaxed by uniform scaling; a universal binding energy curve is fitted to determine the equilibrium volume. The local relaxation volume ΔV_i is the equilibrium volume change relative to the perfect supercell, and the defect formation energy ε_i = E_i − E is taken at mechanical equilibrium. These parameters are then used in a generalized grandcanonical formalism (formation entropies neglected) to solve self-consistently for the chemical potentials and defect concentrations as functions of pressure at T = 1300 K for two compositions: stoichiometric FeAl and Fe0.52Al0.48. Finally, the effective formation volumes Ω̃_i = −k_B T ∂ ln c_i / ∂ p are evaluated numerically. Results are reported in units of the mean atomic volume (the equilibrium volume per atom of the perfect supercell).

## Reproduction target
Produce a JSON file containing the local relaxation volumes ΔV_i and effective formation volumes Ω̃_i for Fe vacancy, Al vacancy, Fe antistructure atom, and Al antistructure atom in B2-FeAl at T = 1300 K, for both stoichiometric FeAl and Fe0.52Al0.48 compositions. All quantities are in units of the mean atomic volume Ω̃_0 (the equilibrium volume per atom of the perfect B2-FeAl supercell).

## Assets

- Quantum ESPRESSO (or equivalent DFT code): https://www.quantum-espresso.org/
- Pseudopotentials for Fe and Al: https://www.materialscloud.org/discover/sssp/table/efficiency
- B2-FeAl crystal structure

## Workflow steps

### Step 1: DFT supercell calculations of defect parameters
- Role: process
- Action: Perform ab-initio pseudopotential DFT calculations on 32-atom B2-FeAl supercells for the perfect lattice and four defect types (Fe vacancy, Al vacancy, Fe antisite, Al antisite). For each supercell, compute total energies at several volumes, relax atomic positions at fixed volume, then relax supercell volume uniformly and fit a universal binding energy curve to determine the equilibrium volume. Obtain local relaxation volume ΔV_i as the change relative to the perfect supercell equilibrium volume, and defect formation energy ε_i = E_i - E (both at mechanical equilibrium). Save the raw energy-volume data as evidence.
- Evidence: `/app/outputs/total_energy_data.csv`

### Step 2: Grandcanonical calculation of effective formation volumes
- Role: scored (load-bearing)
- Action: Using the defect formation energies ε_i and local relaxation volumes ΔV_i from the DFT step, apply the generalized grandcanonical formalism (neglect defect formation entropies) to solve self-consistently for chemical potentials and defect concentrations at T=1300 K for stoichiometric FeAl and Fe0.52Al0.48. Numerically compute the effective formation volumes Ω̃_i = -k_B T ∂ ln c_i / ∂ p. Output a JSON file with the resulting ΔV_i and Ω̃_i values, in units of the mean atomic volume.
- Output file: `/app/outputs/defect_formation_volumes.json`
- Format: json
- Contract: JSON object with top-level keys 'stoichiometric' and 'Fe0.52Al0.48'. Each key maps to an object with keys 'Fe_vacancy', 'Al_vacancy', 'Fe_antistructure', 'Al_antistructure'. Each defect entry is an object with numeric fields 'ΔV' and 'Ω̃', both in units of the mean atomic volume (Ω̃_0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_formation_volumes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_formation_volumes.json
- path: `/app/outputs/defect_formation_volumes.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed local relaxation volumes ΔV and effective formation volumes Ω̃ for Fe vacancy, Al vacancy, Fe antistructure, and Al antistructure in B2-FeAl at T=1300 K for both stoichiometric FeAl and Fe0.52Al0.48, in units of the mean atomic volume.
- schema:
  - `type`: object
  - `required`: `stoichiometric`, `Fe0.52Al0.48`
  - `properties`:
    - `stoichiometric`:
      - `type`: object
      - `required`: `Fe_vacancy`, `Al_vacancy`, `Fe_antistructure`, `Al_antistructure`
      - `properties`:
        - `Fe_vacancy`:
          - `type`: object
          - `required`: `ΔV`, `Ω̃`
          - `additionalProperties`: False
        - `Al_vacancy`:
          - `type`: object
          - `required`: `ΔV`, `Ω̃`
          - `additionalProperties`: False
        - `Fe_antistructure`:
          - `type`: object
          - `required`: `ΔV`, `Ω̃`
          - `additionalProperties`: False
        - `Al_antistructure`:
          - `type`: object
          - `required`: `ΔV`, `Ω̃`
          - `additionalProperties`: False
      - `additionalProperties`: False
    - `Fe0.52Al0.48`:
      - `type`: object
      - `required`: `Fe_vacancy`, `Al_vacancy`, `Fe_antistructure`, `Al_antistructure`
      - `properties`:
        - `Fe_vacancy`:
          - `type`: object
          - `required`: `ΔV`, `Ω̃`
          - `additionalProperties`: False
        - `Al_vacancy`:
          - `type`: object
          - `required`: `ΔV`, `Ω̃`
          - `additionalProperties`: False
        - `Fe_antistructure`:
          - `type`: object
          - `required`: `ΔV`, `Ω̃`
          - `additionalProperties`: False
        - `Al_antistructure`:
          - `type`: object
          - `required`: `ΔV`, `Ω̃`
          - `additionalProperties`: False
      - `additionalProperties`: False
  - `additionalProperties`: False

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_formation_volumes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "stoichiometric",
          "Fe0.52Al0.48"
        ],
        "properties": {
          "stoichiometric": {
            "type": "object",
            "required": [
              "Fe_vacancy",
              "Al_vacancy",
              "Fe_antistructure",
              "Al_antistructure"
            ],
            "properties": {
              "Fe_vacancy": {
                "type": "object",
                "required": [
                  "ΔV",
                  "Ω̃"
                ],
                "additionalProperties": false
              },
              "Al_vacancy": {
                "type": "object",
                "required": [
                  "ΔV",
                  "Ω̃"
                ],
                "additionalProperties": false
              },
              "Fe_antistructure": {
                "type": "object",
                "required": [
                  "ΔV",
                  "Ω̃"
                ],
                "additionalProperties": false
              },
              "Al_antistructure": {
                "type": "object",
                "required": [
                  "ΔV",
                  "Ω̃"
                ],
                "additionalProperties": false
              }
            },
            "additionalProperties": false
          },
          "Fe0.52Al0.48": {
            "type": "object",
            "required": [
              "Fe_vacancy",
              "Al_vacancy",
              "Fe_antistructure",
              "Al_antistructure"
            ],
            "properties": {
              "Fe_vacancy": {
                "type": "object",
                "required": [
                  "ΔV",
                  "Ω̃"
                ],
                "additionalProperties": false
              },
              "Al_vacancy": {
                "type": "object",
                "required": [
                  "ΔV",
                  "Ω̃"
                ],
                "additionalProperties": false
              },
              "Fe_antistructure": {
                "type": "object",
                "required": [
                  "ΔV",
                  "Ω̃"
                ],
                "additionalProperties": false
              },
              "Al_antistructure": {
                "type": "object",
                "required": [
                  "ΔV",
                  "Ω̃"
                ],
                "additionalProperties": false
              }
            },
            "additionalProperties": false
          }
        },
        "additionalProperties": false
      },
      "description": "Computed local relaxation volumes ΔV and effective formation volumes Ω̃ for Fe vacancy, Al vacancy, Fe antistructure, and Al antistructure in B2-FeAl at T=1300 K for both stoichiometric FeAl and Fe0.52Al0.48, in units of the mean atomic volume."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your output file `defect_formation_volumes.json` will be assessed by a hidden verifier that compares each ΔV and Ω̃ value you report (for each defect and each composition) against reference values derived from the original study, using pre-defined tolerances that absorb legitimate differences arising from the choice of DFT code, pseudopotentials, and numerical settings. Full credit is awarded when a value falls within the allowed tolerance; for values outside the tolerance, partial credit is assigned on a linear decay scale. The overall reward is the average of the per-value scores.
