# Multilayer van der Waals film stability: two-layer vs three-layer transition

## Problem background
Multilayer thin films consisting of two distinct van der Waals materials, A and B, can form either a two-layer configuration (AB) or a three-layer configuration (ABA) depending on the layer thicknesses. The equilibrium structure emerges from a competition between surface energies, interfacial energies, and long-range van der Waals interactions between interfaces. The goal is to determine which structure is thermodynamically stable as a function of the total thicknesses D_A and D_B, and to find the threshold that separates the two regimes.

## Approach
We model the film as a planar multilayer system with the following fixed material parameters:
  σ_A = 0.626 eV/nm², σ_B = 0.647 eV/nm², σ_AB = 0.016 eV/nm²,
  ε_AA = 0.33 eV, ε_BB = 0.053 eV, ε_AB = 0.042 eV.

The energies per unit area of the two- and three-layer configurations are (D_A, D_B > 0):

- Two-layer (AB) energy, with total layer thicknesses D_A and D_B:
  U_AB = σ_A + σ_B + σ_AB - ε_AB/(D_A + D_B)^2 + (ε_AB - ε_AA)/D_A^2 + (ε_AB - ε_BB)/D_B^2

- Three-layer (ABA) energy, assuming the two outer A layers have equal thickness (D_A/2 each) and the middle B layer has thickness D_B:
  U_ABA = 2σ_A + 2σ_AB - ε_AA/(D_A + D_B)^2 
         - (ε_AB - ε_AA) * [ -2/(D_A/2)^2 + 2/(D_A/2 + D_B)^2 ] 
         + (2ε_AB - ε_AA - ε_BB)/D_B^2

- Energy difference (ABA vs AB):
  ΔU = U_ABA - U_AB = (σ_A - σ_B + σ_AB) 
       + (ε_AB - ε_AA) * [ 7/D_A^2 + 1/D_B^2 - 2/(D_A/2 + D_B)^2 + 1/(D_A + D_B)^2 ]

By comparing U_AB and U_ABA for a grid of D_A and D_B, determine the stable structure (the one with lower energy). In the limit D_B → ∞, the transition threshold D_A* is the value of D_A where ΔU = 0; solve this equation numerically (e.g., by root-finding) from the ΔU expression with D_B set to a very large number.

## Reproduction target
Using the provided material parameters, produce a stability map that records, for each pair of thicknesses D_A and D_B, whether the AB or ABA structure is lower in energy. Also, compute the transition value of D_A² in the limit of large D_B and provide the corresponding analytic expression. The results must be written to the file `stability_results.json` as specified in the output contract.

## Assets

- Film material parameters

## Workflow steps

### Step 1: Compute film stability map and transition threshold
- Role: scored (load-bearing)
- Action: Implement the analytic energy expressions for two-layer (AB) and three-layer (ABA) flat films using the given material parameters. For a grid of total layer thicknesses D_A and D_B across a wide range, compute the energy per unit area of each configuration and record which structure (AB or ABA) has lower energy. Then, from the energy difference expression between the two configurations in the limit of a very thick B layer, derive the transition threshold value of D_A^2 and compare it with the analytic condition. Output the stability map and the threshold in a single JSON file.
- Output file: `/app/outputs/stability_results.json`
- Format: json
- Contract: Object with keys: 'stability_map' (array of objects with numeric keys 'D_A' and 'D_B' and string 'structure' taking values 'AB' or 'ABA') and 'transition_threshold' (object with string 'formula_D_A_sq' and numeric 'computed_D_A_sq').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stability_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stability_results.json
- path: `/app/outputs/stability_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reproduced multilayer film stability map (which structure is thermodynamically preferred for each pair of layer thicknesses) and the analytic transition threshold D_A^2 in the limit of large B-layer thickness.
- schema:
  - `type`: object
  - `required`: `stability_map`, `transition_threshold`
  - `properties`:
    - `stability_map`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `D_A`, `D_B`, `structure`
        - `properties`:
          - `D_A`:
            - `type`: number
          - `D_B`:
            - `type`: number
          - `structure`:
            - `type`: string
            - `enum`: `AB`, `ABA`
    - `transition_threshold`:
      - `type`: object
      - `required`: `formula_D_A_sq`, `computed_D_A_sq`
      - `properties`:
        - `formula_D_A_sq`:
          - `type`: string
        - `computed_D_A_sq`:
          - `type`: number

Notes: The hidden checker holds a gold stability map recomputed from the same energy expressions and a gold transition threshold. The agent's structure labels are compared point-by-point (fraction of matches must be high); the threshold is compared with a 1% relative tolerance. No gold values are revealed in this contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stability_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "stability_map",
          "transition_threshold"
        ],
        "properties": {
          "stability_map": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "D_A",
                "D_B",
                "structure"
              ],
              "properties": {
                "D_A": {
                  "type": "number"
                },
                "D_B": {
                  "type": "number"
                },
                "structure": {
                  "type": "string",
                  "enum": [
                    "AB",
                    "ABA"
                  ]
                }
              }
            }
          },
          "transition_threshold": {
            "type": "object",
            "required": [
              "formula_D_A_sq",
              "computed_D_A_sq"
            ],
            "properties": {
              "formula_D_A_sq": {
                "type": "string"
              },
              "computed_D_A_sq": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Reproduced multilayer film stability map (which structure is thermodynamically preferred for each pair of layer thicknesses) and the analytic transition threshold D_A^2 in the limit of large B-layer thickness."
    }
  ],
  "notes": "The hidden checker holds a gold stability map recomputed from the same energy expressions and a gold transition threshold. The agent's structure labels are compared point-by-point (fraction of matches must be high); the threshold is compared with a 1% relative tolerance. No gold values are revealed in this contract."
}
```

## How you are scored
A hidden verifier independently recomputes the expected stability map and the transition threshold from the same energy model and material parameters. It compares your submitted structure labels point by point and checks your computed threshold against the expected value. Both measurements contribute to your final score; a correct implementation of the energy expressions and the threshold derivation earns full credit. Simply reporting expected numbers without executing the computation will not pass.
