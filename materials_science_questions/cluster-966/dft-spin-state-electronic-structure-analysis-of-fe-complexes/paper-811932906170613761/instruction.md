# DFT Spin-State and Electronic Structure Analysis of Fe and Ni Diketone Radical Complexes

## Problem background
Transition-metal complexes with redox-active ligands can exhibit unusual electronic structures when the ligand is present as a singly reduced radical. While aromatic semiquinone radical ligands are well known, the coordination chemistry of acyclic 1,2-diketone radical anions has been largely unexplored until recently. Two such complexes—[FeIII L•3] and [NiI L•(cod)]—have been isolated and structurally characterized by X‑ray crystallography. The key open question is the electronic configuration of these species: whether the metal center is best described as high-spin or low-spin, how many ligand radicals are present, and how the unpaired electrons are distributed between the metal and the ligands. Broken-symmetry density functional theory (DFT) calculations provide a direct computational route to probe these questions by predicting bond lengths, spin populations, and the arrangement of singly occupied molecular orbitals, which can be compared against experimental structural data to validate the electronic structure assignment.

## Approach
The approach uses the broken-symmetry DFT method with the B3LYP functional to describe the open-shell electronic states of the Fe and Ni complexes. In this formalism, the system is treated as having separate alpha and beta electron populations that can localize on different parts of the molecule, thereby capturing antiferromagnetic coupling between metal and ligand radical spins. For the Fe complex, a BS(5,3) configuration (5 alpha, 3 beta unpaired electrons) is adopted, corresponding to a model with multiple ligand radicals coupled to the metal. For the Ni complex, a BS(1,1) configuration (1 alpha, 1 beta) is used. Starting from the crystallographic coordinates, a truncated molecular model is prepared by removing bulky substituents (isopropyl groups); the complexes are then fully optimized at the B3LYP level. From the optimized structures, the average C–O and C–C bond lengths in the diketone backbone are computed to gauge the degree of ligand reduction, and Mulliken atomic spin populations are extracted to quantify the distribution of unpaired spin density among the metal and the ligands. Additionally, the numbers of singly occupied alpha and beta molecular orbitals are recorded, revealing the net spin state of the system. The approach does not require fitting to any experimental magnetic data; it relies solely on first‑principles DFT to produce quantities that can be directly compared to the experimental X‑ray bond lengths, thereby assessing the accuracy of the optimized geometries and the implied electronic configuration.

## Reproduction target
From the deposited crystal structures (CCDC 668633 for the Fe complex, CCDC 668632 for the Ni complex), construct the truncated and full molecular models as described in the workflow steps. Perform broken-symmetry B3LYP geometry optimizations using BS(5,3) for the Fe complex and BS(1,1) for the Ni complex. For each complex, produce a single JSON file containing: (1) the optimized Cartesian coordinates (geometry) in Angstroms; (2) the average C–O bond length (C-O_avg) and the diketone carbon–carbon bond length (C-C) computed from the optimized structure; (3) the Mulliken atomic spin populations on the metal center and on each diketone ligand; (4) the counts of singly occupied alpha and beta molecular orbitals. The goal is to obtain optimized geometries whose bond lengths are consistent with the experimentally determined crystal structures, and spin populations and orbital occupancy patterns that reflect the underlying metal–ligand electronic coupling, thereby enabling an independent judgment of the electronic configuration of each complex.

## Assets

- CIF for [Fe^III L^•_3] (CCDC 668633): https://www.ccdc.cam.ac.uk/structures/
- CIF for [Ni^I L^•(cod)] (CCDC 668632): https://www.ccdc.cam.ac.uk/structures/
- Quantum chemistry software (ORCA, PySCF, NWChem, or equivalent): https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Build truncated Fe model
- Role: process
- Action: From crystal structure of [Fe^III L^•_3] (CCDC 668633), remove isopropyl groups to create a truncated model for DFT; save initial coordinates.
- Evidence: `/app/outputs/fe_truncated.xyz`

### Step 2: DFT optimization and analysis of Fe complex
- Role: scored (load-bearing)
- Action: Perform broken-symmetry BS(5,3) B3LYP geometry optimization on the truncated Fe model, then compute C–O and C–C bond lengths, Mulliken spin populations (Fe and each ligand), and number of alpha and beta singly occupied orbitals. Write results to fe_complex_results.json.
- Output file: `/app/outputs/fe_complex_results.json`
- Format: json
- Contract: JSON object with required keys: geometry (array of {symbol, x, y, z} in Angstrom), bond_lengths ({C-O_avg, C-C} in Angstrom), mulliken_spin_fe (float), mulliken_spin_ligands (array of 3 floats), num_alpha_singly_occupied (int), num_beta_singly_occupied (int).
- Scoring: scored by hidden verifier

### Step 3: Prepare Ni complex model
- Role: process
- Action: From crystal structure of [Ni^I L^•(cod)] (CCDC 668632), prepare initial coordinates for DFT optimization.
- Evidence: `/app/outputs/ni_input.xyz`

### Step 4: DFT optimization and analysis of Ni complex
- Role: scored (load-bearing)
- Action: Perform broken-symmetry BS(1,1) B3LYP geometry optimization on the Ni complex, then compute C–O and C–C bond lengths, Mulliken spin populations (Ni and diketonate ligand), and number of alpha and beta singly occupied orbitals. Write results to ni_complex_results.json.
- Output file: `/app/outputs/ni_complex_results.json`
- Format: json
- Contract: JSON object with required keys: geometry (array of {symbol, x, y, z} in Angstrom), bond_lengths ({C-O_avg, C-C} in Angstrom), mulliken_spin_ni (float), mulliken_spin_ligand (float), num_alpha_singly_occupied (int), num_beta_singly_occupied (int).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fe_complex_results.json`
- `/app/outputs/ni_complex_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fe_complex_results.json
- path: `/app/outputs/fe_complex_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Optimized geometry, average C-O and C-C bond lengths, Mulliken spin density on Fe and the three ligands, and number of singly occupied alpha and beta molecular orbitals from a broken-symmetry BS(5,3) B3LYP DFT calculation on a truncated model of [Fe^III L^•_3].
- schema:
  - `type`: object
  - `required`: `geometry`, `bond_lengths`, `mulliken_spin_fe`, `mulliken_spin_ligands`, `num_alpha_singly_occupied`, `num_beta_singly_occupied`
  - `properties`:
    - `geometry`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `symbol`, `x`, `y`, `z`
        - `properties`:
          - `symbol`:
            - `type`: string
          - `x`:
            - `type`: number
            - `unit`: Angstrom
          - `y`:
            - `type`: number
            - `unit`: Angstrom
          - `z`:
            - `type`: number
            - `unit`: Angstrom
    - `bond_lengths`:
      - `type`: object
      - `required`: `C-O_avg`, `C-C`
      - `properties`:
        - `C-O_avg`:
          - `type`: number
          - `unit`: Angstrom
        - `C-C`:
          - `type`: number
          - `unit`: Angstrom
    - `mulliken_spin_fe`:
      - `type`: number
      - `description`: Mulliken atomic spin population on Fe
    - `mulliken_spin_ligands`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
      - `description`: Mulliken atomic spin populations on the three diketonate ligands
    - `num_alpha_singly_occupied`:
      - `type`: integer
      - `description`: Number of singly occupied alpha-spin molecular orbitals
    - `num_beta_singly_occupied`:
      - `type`: integer
      - `description`: Number of singly occupied beta-spin molecular orbitals

### ni_complex_results.json
- path: `/app/outputs/ni_complex_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Optimized geometry, average C-O and C-C bond lengths, Mulliken spin density on Ni and the diketonate ligand, and number of singly occupied alpha and beta molecular orbitals from a broken-symmetry BS(1,1) B3LYP DFT calculation on [Ni^I L^•(cod)].
- schema:
  - `type`: object
  - `required`: `geometry`, `bond_lengths`, `mulliken_spin_ni`, `mulliken_spin_ligand`, `num_alpha_singly_occupied`, `num_beta_singly_occupied`
  - `properties`:
    - `geometry`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `symbol`, `x`, `y`, `z`
        - `properties`:
          - `symbol`:
            - `type`: string
          - `x`:
            - `type`: number
            - `unit`: Angstrom
          - `y`:
            - `type`: number
            - `unit`: Angstrom
          - `z`:
            - `type`: number
            - `unit`: Angstrom
    - `bond_lengths`:
      - `type`: object
      - `required`: `C-O_avg`, `C-C`
      - `properties`:
        - `C-O_avg`:
          - `type`: number
          - `unit`: Angstrom
        - `C-C`:
          - `type`: number
          - `unit`: Angstrom
    - `mulliken_spin_ni`:
      - `type`: number
      - `description`: Mulliken atomic spin population on Ni
    - `mulliken_spin_ligand`:
      - `type`: number
      - `description`: Mulliken atomic spin population on the diketonate radical ligand
    - `num_alpha_singly_occupied`:
      - `type`: integer
      - `description`: Number of singly occupied alpha-spin molecular orbitals
    - `num_beta_singly_occupied`:
      - `type`: integer
      - `description`: Number of singly occupied beta-spin molecular orbitals

Notes: The checker will recompute C-O and C-C bond lengths from the submitted coordinates and compare them to experimental crystallographic values within a tolerance typical of DFT; it will verify Mulliken spin populations against reference spin density distributions and check that the reported singly occupied orbital counts match the expected broken-symmetry configurations (Fe: 5 alpha, 3 beta; Ni: 1 alpha, 1 beta).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fe_complex_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "geometry",
          "bond_lengths",
          "mulliken_spin_fe",
          "mulliken_spin_ligands",
          "num_alpha_singly_occupied",
          "num_beta_singly_occupied"
        ],
        "properties": {
          "geometry": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "symbol",
                "x",
                "y",
                "z"
              ],
              "properties": {
                "symbol": {
                  "type": "string"
                },
                "x": {
                  "type": "number",
                  "unit": "Angstrom"
                },
                "y": {
                  "type": "number",
                  "unit": "Angstrom"
                },
                "z": {
                  "type": "number",
                  "unit": "Angstrom"
                }
              }
            }
          },
          "bond_lengths": {
            "type": "object",
            "required": [
              "C-O_avg",
              "C-C"
            ],
            "properties": {
              "C-O_avg": {
                "type": "number",
                "unit": "Angstrom"
              },
              "C-C": {
                "type": "number",
                "unit": "Angstrom"
              }
            }
          },
          "mulliken_spin_fe": {
            "type": "number",
            "description": "Mulliken atomic spin population on Fe"
          },
          "mulliken_spin_ligands": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3,
            "description": "Mulliken atomic spin populations on the three diketonate ligands"
          },
          "num_alpha_singly_occupied": {
            "type": "integer",
            "description": "Number of singly occupied alpha-spin molecular orbitals"
          },
          "num_beta_singly_occupied": {
            "type": "integer",
            "description": "Number of singly occupied beta-spin molecular orbitals"
          }
        }
      },
      "description": "Optimized geometry, average C-O and C-C bond lengths, Mulliken spin density on Fe and the three ligands, and number of singly occupied alpha and beta molecular orbitals from a broken-symmetry BS(5,3) B3LYP DFT calculation on a truncated model of [Fe^III L^•_3]."
    },
    {
      "file": "ni_complex_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "geometry",
          "bond_lengths",
          "mulliken_spin_ni",
          "mulliken_spin_ligand",
          "num_alpha_singly_occupied",
          "num_beta_singly_occupied"
        ],
        "properties": {
          "geometry": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "symbol",
                "x",
                "y",
                "z"
              ],
              "properties": {
                "symbol": {
                  "type": "string"
                },
                "x": {
                  "type": "number",
                  "unit": "Angstrom"
                },
                "y": {
                  "type": "number",
                  "unit": "Angstrom"
                },
                "z": {
                  "type": "number",
                  "unit": "Angstrom"
                }
              }
            }
          },
          "bond_lengths": {
            "type": "object",
            "required": [
              "C-O_avg",
              "C-C"
            ],
            "properties": {
              "C-O_avg": {
                "type": "number",
                "unit": "Angstrom"
              },
              "C-C": {
                "type": "number",
                "unit": "Angstrom"
              }
            }
          },
          "mulliken_spin_ni": {
            "type": "number",
            "description": "Mulliken atomic spin population on Ni"
          },
          "mulliken_spin_ligand": {
            "type": "number",
            "description": "Mulliken atomic spin population on the diketonate radical ligand"
          },
          "num_alpha_singly_occupied": {
            "type": "integer",
            "description": "Number of singly occupied alpha-spin molecular orbitals"
          },
          "num_beta_singly_occupied": {
            "type": "integer",
            "description": "Number of singly occupied beta-spin molecular orbitals"
          }
        }
      },
      "description": "Optimized geometry, average C-O and C-C bond lengths, Mulliken spin density on Ni and the diketonate ligand, and number of singly occupied alpha and beta molecular orbitals from a broken-symmetry BS(1,1) B3LYP DFT calculation on [Ni^I L^•(cod)]."
    }
  ],
  "notes": "The checker will recompute C-O and C-C bond lengths from the submitted coordinates and compare them to experimental crystallographic values within a tolerance typical of DFT; it will verify Mulliken spin populations against reference spin density distributions and check that the reported singly occupied orbital counts match the expected broken-symmetry configurations (Fe: 5 alpha, 3 beta; Ni: 1 alpha, 1 beta)."
}
```

## How you are scored
A hidden verifier will automatically evaluate your submission by reading the two JSON artifacts. The verifier recomputes bond lengths from your reported coordinates and checks them against reference data, compares your reported spin populations and singly occupied orbital counts against expected physical values, and ensures the artifacts conform to the required JSON schema. The reward is a weighted sum of per‑stage scores: each scored output contributes a fraction of the total, with larger weight on the main structural and electronic quantities. Simply writing down numbers that match known literature values will not satisfy the checks, because the verifier examines internal consistency, the structure of your output, and how well your data recreates the expected relationships. No specific tolerance or gold value is disclosed here, but you should aim for DFT‑quality accuracy (i.e., bond lengths within typical B3LYP error bars and physically reasonable spin populations and orbital counts).
