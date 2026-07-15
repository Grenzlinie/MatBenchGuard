# DFT Mechanistic Study of Silane Redistribution by an Organocalcium Complex

## Problem background
The selective redistribution of hydrosilanes presents a powerful route to diversify silane reagents, yet the catalytic mechanisms and the origin of substituent effects are often poorly understood. The present work investigates the mechanism of Ph(Me)SiH₂ redistribution catalyzed by an organocalcium complex. Determining the key activation energies and the overall thermodynamic driving force is essential for rationalizing the observed reactivity. This task targets a computational reproduction of the catalytic cycle energetics at the DFT level.

## Approach
The catalytic cycle is modelled using density functional theory (DFT) at the B3PW91 level. Starting from the crystal structure of calcium alkyl complex 4, molecular models of all reactants, intermediates, and transition states for the three-step σ‑bond metathesis mechanism are constructed for two substrates: Ph(Me)SiH₂ and p‑CF₃‑C₆H₄(Me)SiH₂. Geometry optimizations and transition state searches are performed, and each transition state is confirmed by vibrational frequency analysis and intrinsic reaction coordinate (IRC) calculations. The extracted electronic energies, zero‑point corrected enthalpies, and Gibbs free energies at 298 K are used to construct the reaction energy profiles and to quantify the substituent effect on the rate‑determining step.

## Reproduction target
Compute the activation barriers (in kcal mol⁻¹) for the three elementary steps of the redistribution of Ph(Me)SiH₂: Si–H activation, Si–C activation, and catalyst regeneration. Also compute the overall reaction exothermicity and, for the regeneration step, the difference in transition‑state energy between the parent (p‑H) and p‑CF₃ substituted substrates. The target values must be derived from the DFT energies extracted at the B3PW91 level.

## Assets

- Crystal structure of calcium alkyl complex 4 (CCDC 2043283): 10.5517/ccdc.csd.cc25wlkm
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Build molecular models for the catalytic cycles
- Role: process
- Action: Obtain the crystal structure of calcium alkyl complex 4 (CCDC 2043283) and construct initial Cartesian coordinates for all stationary points involved in the redistribution of Ph(Me)SiH₂ and p‑CF₃‑C₆H₄(Me)SiH₂: reactants, adducts, transition states (Si–H activation, Si–C activation, regeneration), intermediates, and products. Generate input coordinate files for DFT calculations.
- Evidence: `/app/outputs/model_building_log.txt`

### Step 2: DFT geometry optimizations, transition state searches, and frequency analyses
- Role: process
- Action: Perform DFT geometry optimizations, transition state searches, and vibrational frequency calculations at the B3PW91 level for all species from the model‑building step. Use an appropriate basis set (6‑31G(d) for light atoms, Stuttgart/Dresden ECP for Ca). Confirm each transition state by vibrational frequency analysis and intrinsic reaction coordinate (IRC) calculations. Extract electronic energies (E), zero‑point corrected enthalpies (H), and Gibbs free energies (G) at 298 K.
- Evidence: `/app/outputs/dft_summary.txt`

### Step 3: Extract and report computed energetics
- Role: scored (load-bearing)
- Action: Collect the computed E, H, and G energies (in Hartree) for every stationary point in the Ph(Me)SiH₂ and p‑CF₃‑C₆H₄(Me)SiH₂ catalytic cycles and write them to a JSON file.
- Output file: `/app/outputs/computed_energies.json`
- Format: json
- Contract: Array of objects with required `system` identifiers as listed below. Each object has fields `system` (string), `substrate` (string), `E` (number, Hartree), `H` (number, Hartree), `G` (number, Hartree).
- Required system identifiers: `catalyst_4`, `Ph(Me)SiH2`, `calcium_hydride`, `MeSiH3`, `Ph2(Me)SiH`, `CaPh`, `tertiary_silane`, `react_4_and_silane`, `TS1`, `hydride_and_silane`, `TS2`, `CaPh_and_MeSiH3`, `TS3`, `products`. Each must appear once for `substrate` = `parent` and once for `substrate` = `pCF3`.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_energies.json
- path: `/app/outputs/computed_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw computed energies for all stationary points in both catalytic cycles; the hidden checker recomputes activation barriers, exothermicity, and substituent TS energy difference from these values. The `system` field must be one of the enumerated identifiers; each must appear for both `parent` and `pCF3` substrates.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `system`:
        - `type`: string
        - `enum`: `catalyst_4`, `Ph(Me)SiH2`, `calcium_hydride`, `MeSiH3`, `Ph2(Me)SiH`, `CaPh`, `tertiary_silane`, `react_4_and_silane`, `TS1`, `hydride_and_silane`, `TS2`, `CaPh_and_MeSiH3`, `TS3`, `products`
      - `substrate`:
        - `type`: string
        - `enum`: `parent`, `pCF3`
      - `E`:
        - `type`: number
      - `H`:
        - `type`: number
      - `G`:
        - `type`: number
    - `required`: `system`, `substrate`, `E`, `H`, `G`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "system": {
              "type": "string",
              "enum": [
                "catalyst_4",
                "Ph(Me)SiH2",
                "calcium_hydride",
                "MeSiH3",
                "Ph2(Me)SiH",
                "CaPh",
                "tertiary_silane",
                "react_4_and_silane",
                "TS1",
                "hydride_and_silane",
                "TS2",
                "CaPh_and_MeSiH3",
                "TS3",
                "products"
              ]
            },
            "substrate": {
              "type": "string",
              "enum": [
                "parent",
                "pCF3"
              ]
            },
            "E": {
              "type": "number"
            },
            "H": {
              "type": "number"
            },
            "G": {
              "type": "number"
            }
          },
          "required": [
            "system",
            "substrate",
            "E",
            "H",
            "G"
          ]
        }
      },
      "description": "Raw computed energies for all stationary points in both catalytic cycles; the hidden checker recomputes activation barriers, exothermicity, and substituent TS energy difference from these values. The `system` field must be one of the enumerated identifiers; each must appear for both `parent` and `pCF3` substrates."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your submitted `computed_energies.json` and recomputes the three activation barriers, the overall exothermicity, and the substituent TS energy difference. These recomputed quantities are compared against hidden reference values derived from the paper. Each scored stage carries a weight, and the final reward is a weighted sum of the individual scores. Simply reporting the paper’s numbers without performing the DFT calculations will not suffice—the verifier derives the metrics from your raw energies, so only a genuine computation can achieve a high score.
