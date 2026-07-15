# DFT Study of Carbon Monolayer and SiC Film on Si(001)

## Problem background
The formation of a heterojunction between a Si(001) substrate and a very thin β‑SiC(001) film involves substantial lattice mismatch and structural distortions that affect the electronic properties at the interface. Characterizing the atomic geometry and charge distribution of the initial carbon monolayer and of a subsequently deposited SiC film is essential for understanding the band alignment and the electrostatic dipole that develops near the interface. This task requires you to compute, using first‑principles methods, the optimized structures and the corresponding electronic features for both a carbon monolayer and a three‑layer SiC film on Si(001).

## Approach
You will use a periodic density functional theory (DFT) approach to model the Si(001) substrate as a (4×1) slab containing six Si layers, with the bottom surface terminated by hydrogen in a dihydride configuration. The initial carbon monolayer is built by placing five carbon atoms per unit cell—three single carbon atoms and one C–C pair—each carbon atom saturated with two hydrogen atoms (CH₂ groups). The bridging pattern is such that every fourth Si pair is spanned by the C–C pair while the remaining Si pairs are bridged by single carbon atoms. A total‑energy geometry optimization is performed, relaxing the top four Si layers and all C and H atoms while keeping the bottom two Si layers and the bottom hydrogen atoms fixed. Next, you add one Si layer (five atoms) and one C layer (five atoms) on top of the relaxed monolayer to form a three‑layer SiC film, again terminated by hydrogen on the topmost carbon layer, and relax the new structure while fixing the third and deeper Si substrate layers and the bottom hydrogen. From the relaxed coordinates and valence charge densities of both the monolayer and the three‑layer film, you extract a standard set of structural and electronic quantities: bond lengths, bond angles, tilt angles of the CH₂ and Si–C–Si groups, displacement vectors of Si atoms from their ideal bulk positions, and average valence electron population per atom for each layer.

## Reproduction target
Your goal is to produce, for both the carbon monolayer and the three‑layer SiC film, the following quantities and write them as specified JSON files:
- All Si–C, C–C, C–H, and (for the three‑layer structure) Si–Si bond lengths.
- Bond angles for the relevant triples (C–C–Si, C–Si–C, and Si–C–Si).
- Tilt angles φ for the CH₂ groups (monolayer) and for the Si–C–Si groups (three‑layer).
- Displacement components δx and δz of each Si atom in substrate layers 1–4 relative to ideal bulk positions, using consistent atom labels (e.g., the Si atom bridged by the carbon pair is denoted 1′).
- Average valence electron population per atom for each layer (the carbon layer(s), the deposited silicon layer when present, and the four Si substrate layers).

Write these results for the monolayer to `/app/outputs/monolayer_results.json` and for the three‑layer film to `/app/outputs/three_layer_results.json`, following the JSON schema described in the 'Output contract' section. Your outputs will be checked against reference values for the same physical conditions.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Build monolayer slab model
- Role: process
- Action: Generate input structure for a (4×1) Si(001) slab with 6 Si layers, bottom surface terminated by H (dihydride). Place five C atoms per cell: three single C atoms (C₁, C₂) and one C–C pair (C₃–C₃), each with two H atoms (CH₂ groups), bridging every fourth Si pair by the carbon pair and remaining pairs by single C atoms. Write the initial geometry file.
- Evidence: `/app/outputs/initial_monolayer.xyz`

### Step 2: Relax monolayer geometry
- Role: process
- Action: Perform a geometry optimization (DFT) of the monolayer slab. Fix the bottom two Si layers and bottom H; relax top four Si layers, all C, and all H. Save the converged relaxed structure and charge density.
- Evidence: `/app/outputs/monolayer_relaxed.out`

### Step 3: Analyze monolayer properties
- Role: scored (load-bearing)
- Action: From the relaxed monolayer structure and valence charge density, compute the following quantities and output them as a JSON object: (i) all Si–C bond lengths, the C₃–C₃ bond length, and C–H bond lengths; (ii) bond angles for C–C–Si, C–Si–C, and Si–C–Si triples; (iii) tilt angles φ(HC₁H), φ(HC₂H), φ(HC₃H); (iv) displacements δx and δz of Si atoms in layers 1–4 from ideal bulk positions, labeling the Si atom bridged by the carbon pair as 1′; (v) average valence electron population per atom for the carbon layer (C₁C₂C₃) and each distinct Si substrate layer (1 1′, 2 2′, 3 3′ 3′′, 4 4′ 4′′).
- Output file: `/app/outputs/monolayer_results.json`
- Format: json
- Contract: JSON object with keys: bond_lengths (object, label pairs → Å), bond_angles (object, triple labels → °), tilt_angles (object, label → °), displacements (array of objects {atom, dx (Å), dz (Å)} for Si atoms in layers 1-4), electron_densities (object, layer label → e).
- Scoring: scored by hidden verifier

### Step 4: Build three-layer SiC film model
- Role: process
- Action: Starting from the relaxed monolayer structure, add one Si layer (five Si atoms) and one C layer (five C atoms) on top, preserving (4×1) periodicity and bridging pattern, with H termination on the topmost C. Generate the initial structure file.
- Evidence: `/app/outputs/three_layer_initial.xyz`

### Step 5: Relax three-layer structure
- Role: process
- Action: Perform a geometry optimization (DFT) for the three-layer slab. Fix the third and deeper Si substrate layers and bottom H; relax the top two Si substrate layers, all deposited atoms (Si and C layers), and top H. Save the converged relaxed structure and charge density.
- Evidence: `/app/outputs/three_layer_relaxed.out`

### Step 6: Analyze three-layer properties
- Role: scored (load-bearing)
- Action: From the relaxed three-layer structure and valence charge density, compute the same set of quantities as for the monolayer: all Si–C, C–C, C–H, Si–Si bond lengths; bond angles (including Si–C–Si, C–Si–C); tilt angles φ(Si₁C₁Si₁), φ(Si₂C₂Si₂), φ(Si₃C₃Si₃); displacements δx, δz of Si atoms in substrate layers 1–4; average valence electron population per deposited layer (C₄C₅C₆, Si₁Si₂Si₃, C₁C₂C₃) and per Si substrate layer. Output as JSON.
- Output file: `/app/outputs/three_layer_results.json`
- Format: json
- Contract: JSON object with the same keys as monolayer_results.json: bond_lengths, bond_angles, tilt_angles, displacements (array of {atom, dx (Å), dz (Å)}), electron_densities.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monolayer_results.json`
- `/app/outputs/three_layer_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monolayer_results.json
- path: `/app/outputs/monolayer_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized bond lengths, angles, tilt angles, Si atom displacements from bulk positions, and layer-resolved valence electron densities for the carbon monolayer on Si(001).
- schema:
  - `type`: object
  - `properties`:
    - `bond_lengths`:
      - `type`: object
      - `description`: bond label pairs to lengths in Å, e.g. 'C1-1': 1.9
      - `additionalProperties`:
        - `type`: number
        - `unit`: Å
    - `bond_angles`:
      - `type`: object
      - `description`: triple atom labels to angles in degrees
      - `additionalProperties`:
        - `type`: number
        - `unit`: deg
    - `tilt_angles`:
      - `type`: object
      - `description`: tilt angle labels (e.g. 'HC1H') to degrees
      - `additionalProperties`:
        - `type`: number
        - `unit`: deg
    - `displacements`:
      - `type`: array
      - `description`: displacement vectors for each Si atom in layers 1-4
      - `items`:
        - `type`: object
        - `properties`:
          - `atom`:
            - `type`: string
            - `description`: atom label, e.g. '1', '1''', '2', '2'''
          - `dx`:
            - `type`: number
            - `unit`: Å
          - `dz`:
            - `type`: number
            - `unit`: Å
        - `required`: `atom`, `dx`, `dz`
    - `electron_densities`:
      - `type`: object
      - `description`: average valence electrons per atom for each layer (e.g. 'C1C2C3', '1 1''', '2 2''')
      - `additionalProperties`:
        - `type`: number
        - `unit`: e
  - `required`: `bond_lengths`, `bond_angles`, `tilt_angles`, `displacements`, `electron_densities`

### three_layer_results.json
- path: `/app/outputs/three_layer_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized structural and electronic parameters for the three-layer SiC film on Si(001), analogous to the monolayer output.
- schema:
  - `type`: object
  - `properties`:
    - `bond_lengths`:
      - `type`: object
      - `description`: bond label pairs to lengths in Å (includes Si-C, C-C, C-H, Si-Si)
      - `additionalProperties`:
        - `type`: number
        - `unit`: Å
    - `bond_angles`:
      - `type`: object
      - `description`: triple atom labels to angles in degrees
      - `additionalProperties`:
        - `type`: number
        - `unit`: deg
    - `tilt_angles`:
      - `type`: object
      - `description`: tilt angles for Si-C-Si groups, e.g. 'Si1C1Si1' in degrees
      - `additionalProperties`:
        - `type`: number
        - `unit`: deg
    - `displacements`:
      - `type`: array
      - `description`: displacement vectors for each Si atom in substrate layers 1-4
      - `items`:
        - `type`: object
        - `properties`:
          - `atom`:
            - `type`: string
          - `dx`:
            - `type`: number
            - `unit`: Å
          - `dz`:
            - `type`: number
            - `unit`: Å
        - `required`: `atom`, `dx`, `dz`
    - `electron_densities`:
      - `type`: object
      - `description`: average valence electrons per atom for deposited layers and Si substrate layers
      - `additionalProperties`:
        - `type`: number
        - `unit`: e
  - `required`: `bond_lengths`, `bond_angles`, `tilt_angles`, `displacements`, `electron_densities`

Notes: The scoring compares extracted numeric values for stated quantities (bond lengths, angles, displacements, electron densities) with reference values within tolerances, and verifies qualitative structural trends (e.g., displacement ordering, bond length changes, dipole direction).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monolayer_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "bond_lengths": {
            "type": "object",
            "description": "bond label pairs to lengths in Å, e.g. 'C1-1': 1.9",
            "additionalProperties": {
              "type": "number",
              "unit": "Å"
            }
          },
          "bond_angles": {
            "type": "object",
            "description": "triple atom labels to angles in degrees",
            "additionalProperties": {
              "type": "number",
              "unit": "deg"
            }
          },
          "tilt_angles": {
            "type": "object",
            "description": "tilt angle labels (e.g. 'HC1H') to degrees",
            "additionalProperties": {
              "type": "number",
              "unit": "deg"
            }
          },
          "displacements": {
            "type": "array",
            "description": "displacement vectors for each Si atom in layers 1-4",
            "items": {
              "type": "object",
              "properties": {
                "atom": {
                  "type": "string",
                  "description": "atom label, e.g. '1', '1''', '2', '2'''"
                },
                "dx": {
                  "type": "number",
                  "unit": "Å"
                },
                "dz": {
                  "type": "number",
                  "unit": "Å"
                }
              },
              "required": [
                "atom",
                "dx",
                "dz"
              ]
            }
          },
          "electron_densities": {
            "type": "object",
            "description": "average valence electrons per atom for each layer (e.g. 'C1C2C3', '1 1''', '2 2''')",
            "additionalProperties": {
              "type": "number",
              "unit": "e"
            }
          }
        },
        "required": [
          "bond_lengths",
          "bond_angles",
          "tilt_angles",
          "displacements",
          "electron_densities"
        ]
      },
      "description": "Optimized bond lengths, angles, tilt angles, Si atom displacements from bulk positions, and layer-resolved valence electron densities for the carbon monolayer on Si(001)."
    },
    {
      "file": "three_layer_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "bond_lengths": {
            "type": "object",
            "description": "bond label pairs to lengths in Å (includes Si-C, C-C, C-H, Si-Si)",
            "additionalProperties": {
              "type": "number",
              "unit": "Å"
            }
          },
          "bond_angles": {
            "type": "object",
            "description": "triple atom labels to angles in degrees",
            "additionalProperties": {
              "type": "number",
              "unit": "deg"
            }
          },
          "tilt_angles": {
            "type": "object",
            "description": "tilt angles for Si-C-Si groups, e.g. 'Si1C1Si1' in degrees",
            "additionalProperties": {
              "type": "number",
              "unit": "deg"
            }
          },
          "displacements": {
            "type": "array",
            "description": "displacement vectors for each Si atom in substrate layers 1-4",
            "items": {
              "type": "object",
              "properties": {
                "atom": {
                  "type": "string"
                },
                "dx": {
                  "type": "number",
                  "unit": "Å"
                },
                "dz": {
                  "type": "number",
                  "unit": "Å"
                }
              },
              "required": [
                "atom",
                "dx",
                "dz"
              ]
            }
          },
          "electron_densities": {
            "type": "object",
            "description": "average valence electrons per atom for deposited layers and Si substrate layers",
            "additionalProperties": {
              "type": "number",
              "unit": "e"
            }
          }
        },
        "required": [
          "bond_lengths",
          "bond_angles",
          "tilt_angles",
          "displacements",
          "electron_densities"
        ]
      },
      "description": "Optimized structural and electronic parameters for the three-layer SiC film on Si(001), analogous to the monolayer output."
    }
  ],
  "notes": "The scoring compares extracted numeric values for stated quantities (bond lengths, angles, displacements, electron densities) with reference values within tolerances, and verifies qualitative structural trends (e.g., displacement ordering, bond length changes, dipole direction)."
}
```

## How you are scored
A hidden verifier reads your `monolayer_results.json` and `three_layer_results.json` and compares the reported numeric quantities—bond lengths, bond angles, tilt angles, displacement components, and electron densities—to reference values within appropriate tolerances. In addition, it verifies several qualitative structural trends, such as the ordering of certain Si atom displacements, the change in the C–C pair bond length between the monolayer and the three‑layer film, and the relative electron densities of the first and second Si substrate layers. The overall score is the fraction of the quantitative comparisons and trend assertions that are satisfied. A complete structural optimization and property extraction are required; simply reporting the expected numbers does not guarantee a high score.
