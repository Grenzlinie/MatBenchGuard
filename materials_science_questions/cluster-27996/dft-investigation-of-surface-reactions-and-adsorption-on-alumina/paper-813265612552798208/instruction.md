# DFT Energetics of Methanol Reaction on Aluminum Superatom Clusters

## Problem background
Electronegative ligands, such as iodine, can stabilize aluminum clusters by completing their electronic shell, making them resistant to oxygen etching. However, it is hypothesized that the ligands may also induce uneven charge distribution on the metallic core, creating Lewis acid–base active sites that could enable reaction with protic molecules like methanol. This task investigates through first-principles DFT whether and how iodine ligands activate otherwise inert Al13⁻ and Al14⁻ cluster anions toward methanol, by computing the reaction pathway energies and examining the role of ligand placement and core structure.

## Approach
Use density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and an all-electron basis set to compute the reaction pathway of methanol on aluminum cluster anions. For each cluster, the following stationary points are optimized: isolated cluster, isolated methanol molecule, non-dissociative adsorption complex, transition state for O–H bond dissociation, and the final dissociated product. From the total energies, the non-dissociative binding energy (difference between complex energy and the sum of isolated cluster and methanol energies), transition-state energy (TS energy minus sum of isolated cluster and methanol energies), activation energy (TS energy minus bound complex energy), and reaction energy (product energy minus sum of isolated cluster and methanol energies) are calculated. The HOMO–LUMO gap of each isolated cluster is also extracted. The calculations are performed for three representative systems: (1) bare Al13⁻, (2) the adjacent-iodine isomer of Al13I₂⁻, and (3) Al14I₃⁻ reacting at the adatom site. This setup allows comparison of a bare closed-shell cluster, an isomer suspected to harbor ligand-induced active sites opposite adjacent iodine ligands, and an adatom-decorated core where a ligand on the adatom may activate the reaction.

## Reproduction target
Compute, via DFT, the reaction pathway for methanol on three aluminum cluster systems: (1) bare Al13⁻, (2) the adjacent-iodine isomer of Al13I₂⁻, and (3) Al14I₃⁻ at the adatom site. For each system, produce the nondissociative binding energy E_B, transition-state energy E_T, activation energy E_A, reaction energy E_R, and the HOMO–LUMO gap of the isolated cluster. The computed energetics should reflect the reactivity signatures: compare the magnitude and sign of E_T across systems to assess gas-phase reactivity, and compare E_B and E_A magnitudes to assess Lewis acidity and the reaction barrier. All results are to be assembled into the JSON file described in the output contract.

## Assets

- DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/

## Input structures

The following Cartesian coordinates are given in Ångströms. Use them as initial geometries for DFT calculations.

### Methanol (CH3OH)

```xyz
O   0.000000   0.000000   0.000000
H  -0.956000   0.745000   0.000000
C   1.430000   0.000000   0.000000
H   1.856000   1.029000   0.000000
H   1.856000  -0.514500   0.891000
H   1.856000  -0.514500  -0.891000
```

### Al13⁻ (icosahedral core)

```xyz
Al   0.000000   0.000000   0.000000
Al   0.000000   1.399000   2.264000
Al   0.000000   1.399000  -2.264000
Al   0.000000  -1.399000   2.264000
Al   0.000000  -1.399000  -2.264000
Al   2.264000   0.000000   1.399000
Al   2.264000   0.000000  -1.399000
Al  -2.264000   0.000000   1.399000
Al  -2.264000   0.000000  -1.399000
Al   1.399000   2.264000   0.000000
Al  -1.399000   2.264000   0.000000
Al   1.399000  -2.264000   0.000000
Al  -1.399000  -2.264000   0.000000
```

### Al13I₂⁻ adjacent isomer

```xyz
Al   0.000000   0.000000   0.000000
Al   0.000000   1.399000   2.264000
Al   0.000000   1.399000  -2.264000
Al   0.000000  -1.399000   2.264000
Al   0.000000  -1.399000  -2.264000
Al   2.264000   0.000000   1.399000
Al   2.264000   0.000000  -1.399000
Al  -2.264000   0.000000   1.399000
Al  -2.264000   0.000000  -1.399000
Al   1.399000   2.264000   0.000000
Al  -1.399000   2.264000   0.000000
Al   1.399000  -2.264000   0.000000
Al  -1.399000  -2.264000   0.000000
I    0.000000   1.314000   2.127000
I    1.314000   2.127000   0.000000
```

### Al14I₃⁻ adatom (iodine on adatom)

```xyz
Al   0.000000   0.000000   0.000000
Al   0.000000   1.399000   2.264000
Al   0.000000   1.399000  -2.264000
Al   0.000000  -1.399000   2.264000
Al   0.000000  -1.399000  -2.264000
Al   2.264000   0.000000   1.399000
Al   2.264000   0.000000  -1.399000
Al  -2.264000   0.000000   1.399000
Al  -2.264000   0.000000  -1.399000
Al   1.399000   2.264000   0.000000
Al  -1.399000   2.264000   0.000000
Al   1.399000  -2.264000   0.000000
Al  -1.399000  -2.264000   0.000000
Al   2.500000   2.500000   2.500000
I    3.943000   3.943000   3.943000
I    0.000000  -1.314000  -2.127000
I   -2.127000   0.000000  -1.314000
```

## Workflow steps

### Step 1: Prepare input structures
- Role: process
- Action: Generate DFT input files for methanol and for the three target clusters: (1) Al13⁻, (2) the adjacent-iodine isomer of Al13I₂⁻, and (3) Al14I₃⁻ with an iodine ligand on the adatom, using the Cartesian coordinates provided in the instructions.
- Evidence: none

### Step 2: Optimize isolated methanol molecule
- Role: process
- Action: Perform DFT geometry optimization of the isolated methanol molecule at the PBE level with an all-electron basis set. Record the total energy.
- Evidence: none

### Step 3: Optimize isolated clusters and obtain HOMO–LUMO gaps
- Role: process
- Action: For each of the three clusters, perform DFT geometry optimization of the isolated cluster. From the converged ground-state electronic structure, extract the total energy and the HOMO–LUMO gap.
- Evidence: none

### Step 4: Optimize nondissociative adsorption complexes
- Role: process
- Action: For each cluster, build an initial nondissociative methanol–cluster adsorption complex at the designated reactive site and perform DFT geometry optimization. Save the total energy of the bound complex.
- Evidence: none

### Step 5: Locate transition states for O–H dissociation
- Role: process
- Action: For each cluster, locate the transition state corresponding to O–H bond breaking using a linear transit or NEB approach. Perform DFT optimization of the transition-state structure and record its total energy.
- Evidence: none

### Step 6: Optimize dissociated product complexes
- Role: process
- Action: For each cluster, build and optimize the geometry of the final dissociated product (methanol O–H broken, hydrogen transferred to a nearby aluminum site). Save the total energy of the product complex.
- Evidence: none

### Step 7: Compute reaction energetics and write final JSON
- Role: scored (load-bearing)
- Action: Collect all total energies (isolated cluster, methanol, bound complex, TS, product). For each cluster, compute the nondissociative binding energy (difference between complex energy and sum of isolated cluster and methanol energies), transition-state energy (TS energy minus sum of isolated cluster and methanol energies), activation energy (TS energy minus bound complex energy), and reaction energy (product energy minus sum of isolated cluster and methanol energies). Assemble total energies, derived energies, and HOMO–LUMO gaps into a single JSON file named computed_energies.json.
- Output file: `/app/outputs/computed_energies.json`
- Format: json
- Contract: {"type": "object", "required": ["Al13_minus", "Al13I2_adjacent", "Al14I3_adatom"], "properties": {"Al13_minus": {"type": "object", "properties": {"total_energies": {"type": "object", "required": ["cluster", "methanol", "complex", "ts", "product"], "properties": {"cluster": {"type": "number", "units": "eV"}, "methanol": {"type": "number", "units": "eV"}, "complex": {"type": "number", "units": "eV"}, "ts": {"type": "number", "units": "eV"}, "product": {"type": "number", "units": "eV"}}}, "derived": {"type": "object", "required": ["EB", "ET", "EA", "ER"], "properties": {"EB": {"type": "number", "units": "eV"}, "ET": {"type": "number", "units": "eV"}, "EA": {"type": "number", "units": "eV"}, "ER": {"type": "number", "units": "eV"}}}, "HOMO_LUMO_gap": {"type": "number", "units": "eV"}}}, "Al13I2_adjacent": {"type": "object", "properties": {"total_energies": {"type": "object", "required": ["cluster", "methanol", "complex", "ts", "product"], "properties": {"cluster": {"type": "number", "units": "eV"}, "methanol": {"type": "number", "units": "eV"}, "complex": {"type": "number", "units": "eV"}, "ts": {"type": "number", "units": "eV"}, "product": {"type": "number", "units": "eV"}}}, "derived": {"type": "object", "required": ["EB", "ET", "EA", "ER"], "properties": {"EB": {"type": "number", "units": "eV"}, "ET": {"type": "number", "units": "eV"}, "EA": {"type": "number", "units": "eV"}, "ER": {"type": "number", "units": "eV"}}}, "HOMO_LUMO_gap": {"type": "number", "units": "eV"}}}, "Al14I3_adatom": {"type": "object", "properties": {"total_energies": {"type": "object", "required": ["cluster", "methanol", "complex", "ts", "product"], "properties": {"cluster": {"type": "number", "units": "eV"}, "methanol": {"type": "number", "units": "eV"}, "complex": {"type": "number", "units": "eV"}, "ts": {"type": "number", "units": "eV"}, "product": {"type": "number", "units": "eV"}}}, "derived": {"type": "object", "required": ["EB", "ET", "EA", "ER"], "properties": {"EB": {"type": "number", "units": "eV"}, "ET": {"type": "number", "units": "eV"}, "EA": {"type": "number", "units": "eV"}, "ER": {"type": "number", "units": "eV"}}}, "HOMO_LUMO_gap": {"type": "number", "units": "eV"}}}}}
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
- target_policy: reference_match
- description: This file contains the total energies of all stationary points and the derived reaction energetics (binding, transition-state, activation, and reaction energies) plus the HOMO–LUMO gap for the three target clusters. The values are compared to hidden paper-derived references with tolerances and qualitative trend checks.
- schema:
  - `type`: object
  - `required`: `Al13_minus`, `Al13I2_adjacent`, `Al14I3_adatom`
  - `properties`:
    - `Al13_minus`:
      - `type`: object
      - `required`: `total_energies`, `derived`, `HOMO_LUMO_gap`
      - `properties`:
        - `total_energies`:
          - `type`: object
          - `required`: `cluster`, `methanol`, `complex`, `ts`, `product`
          - `properties`:
            - `cluster`:
              - `type`: number
              - `units`: eV
            - `methanol`:
              - `type`: number
              - `units`: eV
            - `complex`:
              - `type`: number
              - `units`: eV
            - `ts`:
              - `type`: number
              - `units`: eV
            - `product`:
              - `type`: number
              - `units`: eV
        - `derived`:
          - `type`: object
          - `required`: `EB`, `ET`, `EA`, `ER`
          - `properties`:
            - `EB`:
              - `type`: number
              - `units`: eV
            - `ET`:
              - `type`: number
              - `units`: eV
            - `EA`:
              - `type`: number
              - `units`: eV
            - `ER`:
              - `type`: number
              - `units`: eV
        - `HOMO_LUMO_gap`:
          - `type`: number
          - `units`: eV
    - `Al13I2_adjacent`:
      - `type`: object
      - `required`: `total_energies`, `derived`, `HOMO_LUMO_gap`
      - `properties`:
        - `total_energies`:
          - `type`: object
          - `required`: `cluster`, `methanol`, `complex`, `ts`, `product`
          - `properties`:
            - `cluster`:
              - `type`: number
              - `units`: eV
            - `methanol`:
              - `type`: number
              - `units`: eV
            - `complex`:
              - `type`: number
              - `units`: eV
            - `ts`:
              - `type`: number
              - `units`: eV
            - `product`:
              - `type`: number
              - `units`: eV
        - `derived`:
          - `type`: object
          - `required`: `EB`, `ET`, `EA`, `ER`
          - `properties`:
            - `EB`:
              - `type`: number
              - `units`: eV
            - `ET`:
              - `type`: number
              - `units`: eV
            - `EA`:
              - `type`: number
              - `units`: eV
            - `ER`:
              - `type`: number
              - `units`: eV
        - `HOMO_LUMO_gap`:
          - `type`: number
          - `units`: eV
    - `Al14I3_adatom`:
      - `type`: object
      - `required`: `total_energies`, `derived`, `HOMO_LUMO_gap`
      - `properties`:
        - `total_energies`:
          - `type`: object
          - `required`: `cluster`, `methanol`, `complex`, `ts`, `product`
          - `properties`:
            - `cluster`:
              - `type`: number
              - `units`: eV
            - `methanol`:
              - `type`: number
              - `units`: eV
            - `complex`:
              - `type`: number
              - `units`: eV
            - `ts`:
              - `type`: number
              - `units`: eV
            - `product`:
              - `type`: number
              - `units`: eV
        - `derived`:
          - `type`: object
          - `required`: `EB`, `ET`, `EA`, `ER`
          - `properties`:
            - `EB`:
              - `type`: number
              - `units`: eV
            - `ET`:
              - `type`: number
              - `units`: eV
            - `EA`:
              - `type`: number
              - `units`: eV
            - `ER`:
              - `type`: number
              - `units`: eV
        - `HOMO_LUMO_gap`:
          - `type`: number
          - `units`: eV

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Al13_minus",
          "Al13I2_adjacent",
          "Al14I3_adatom"
        ],
        "properties": {
          "Al13_minus": {
            "type": "object",
            "required": [
              "total_energies",
              "derived",
              "HOMO_LUMO_gap"
            ],
            "properties": {
              "total_energies": {
                "type": "object",
                "required": [
                  "cluster",
                  "methanol",
                  "complex",
                  "ts",
                  "product"
                ],
                "properties": {
                  "cluster": {
                    "type": "number",
                    "units": "eV"
                  },
                  "methanol": {
                    "type": "number",
                    "units": "eV"
                  },
                  "complex": {
                    "type": "number",
                    "units": "eV"
                  },
                  "ts": {
                    "type": "number",
                    "units": "eV"
                  },
                  "product": {
                    "type": "number",
                    "units": "eV"
                  }
                }
              },
              "derived": {
                "type": "object",
                "required": [
                  "EB",
                  "ET",
                  "EA",
                  "ER"
                ],
                "properties": {
                  "EB": {
                    "type": "number",
                    "units": "eV"
                  },
                  "ET": {
                    "type": "number",
                    "units": "eV"
                  },
                  "EA": {
                    "type": "number",
                    "units": "eV"
                  },
                  "ER": {
                    "type": "number",
                    "units": "eV"
                  }
                }
              },
              "HOMO_LUMO_gap": {
                "type": "number",
                "units": "eV"
              }
            }
          },
          "Al13I2_adjacent": {
            "type": "object",
            "required": [
              "total_energies",
              "derived",
              "HOMO_LUMO_gap"
            ],
            "properties": {
              "total_energies": {
                "type": "object",
                "required": [
                  "cluster",
                  "methanol",
                  "complex",
                  "ts",
                  "product"
                ],
                "properties": {
                  "cluster": {
                    "type": "number",
                    "units": "eV"
                  },
                  "methanol": {
                    "type": "number",
                    "units": "eV"
                  },
                  "complex": {
                    "type": "number",
                    "units": "eV"
                  },
                  "ts": {
                    "type": "number",
                    "units": "eV"
                  },
                  "product": {
                    "type": "number",
                    "units": "eV"
                  }
                }
              },
              "derived": {
                "type": "object",
                "required": [
                  "EB",
                  "ET",
                  "EA",
                  "ER"
                ],
                "properties": {
                  "EB": {
                    "type": "number",
                    "units": "eV"
                  },
                  "ET": {
                    "type": "number",
                    "units": "eV"
                  },
                  "EA": {
                    "type": "number",
                    "units": "eV"
                  },
                  "ER": {
                    "type": "number",
                    "units": "eV"
                  }
                }
              },
              "HOMO_LUMO_gap": {
                "type": "number",
                "units": "eV"
              }
            }
          },
          "Al14I3_adatom": {
            "type": "object",
            "required": [
              "total_energies",
              "derived",
              "HOMO_LUMO_gap"
            ],
            "properties": {
              "total_energies": {
                "type": "object",
                "required": [
                  "cluster",
                  "methanol",
                  "complex",
                  "ts",
                  "product"
                ],
                "properties": {
                  "cluster": {
                    "type": "number",
                    "units": "eV"
                  },
                  "methanol": {
                    "type": "number",
                    "units": "eV"
                  },
                  "complex": {
                    "type": "number",
                    "units": "eV"
                  },
                  "ts": {
                    "type": "number",
                    "units": "eV"
                  },
                  "product": {
                    "type": "number",
                    "units": "eV"
                  }
                }
              },
              "derived": {
                "type": "object",
                "required": [
                  "EB",
                  "ET",
                  "EA",
                  "ER"
                ],
                "properties": {
                  "EB": {
                    "type": "number",
                    "units": "eV"
                  },
                  "ET": {
                    "type": "number",
                    "units": "eV"
                  },
                  "EA": {
                    "type": "number",
                    "units": "eV"
                  },
                  "ER": {
                    "type": "number",
                    "units": "eV"
                  }
                }
              },
              "HOMO_LUMO_gap": {
                "type": "number",
                "units": "eV"
              }
            }
          }
        }
      },
      "description": "This file contains the total energies of all stationary points and the derived reaction energetics (binding, transition-state, activation, and reaction energies) plus the HOMO–LUMO gap for the three target clusters. The values are compared to hidden paper-derived references with tolerances and qualitative trend checks."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads your `computed_energies.json`. The verifier independently recomputes derived energies from your reported total energies to check internal consistency, and compares your derived E_B, E_T, E_A, E_R, and HOMO–LUMO gap against hidden reference values with preset tolerances. Additionally, it checks qualitative trends among the three clusters: for example, relative magnitudes of binding energies and the sign of transition-state energies. Each check contributes a fraction of the total reward. Reporting numbers that match expected values is not sufficient; the verifier also validates that the submitted total energies self-consistently yield the derived quantities. The final reward is a combination of exact-value matches and trend verifications.
