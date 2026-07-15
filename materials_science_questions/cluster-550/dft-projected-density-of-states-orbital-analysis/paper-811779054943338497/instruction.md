# DFT Projected Density of States Orbital Analysis

## Problem background
Understanding hydrogen bonding in energetic molecular crystals is critical because it influences sensitivity and stability. The β-phase of octahydro-1,3,5,7-tetranitro-1,3,5,7-tetrazocine (β‑HMX) is a prototypical weak-hydrogen-bonded explosive, yet the precise nature and consequence of C–H···O interactions in its solid state remain debated. This task targets the electronic-structure origin of those interactions: by computing the projected density of states (PDOS) and performing Mulliken population analysis, one can quantify orbital overlaps between oxygen 2p and hydrogen 1s states and thereby identify specific intra- and intermolecular hydrogen bonds in the crystal.

## Approach
The reproduction strategy is a two-phase DFT computing protocol. First, the β-HMX crystal is relaxed from the experimentally known lattice parameters using the local density approximation (LDA) with Perdew–Zunger parameterization, a plane-wave basis, and ultrasoft pseudopotentials in an open‑source periodic DFT code (Quantum ESPRESSO). The relaxed structure yields the crystal‑phase bond lengths and angles. Second, the electronic structure is analyzed by computing the projected density of states (PDOS) for O‑2p and H‑1s orbitals. The overlap energy range where both orbitals hybridize reveals candidate hydrogen bonds, which are identified by locating pairs of O and H atoms whose PDOS resonances coincide. For comparison, a single β-HMX molecule is optimized in the gas phase at the B3LYP/6‑31G(d,p) level of theory using an open‑source quantum chemistry package (Psi4). Mulliken atomic charges and bond populations are then computed for both the relaxed crystal and the optimized gas‑phase molecule to quantify charge transfer and bond strength changes due to the crystal environment.

## Reproduction target
Produce three scored artifacts from the DFT workflow:

1. **Crystal geometry** (`crystal_geometry.json`): the bond lengths and bond angles of the β-HMX molecule in the relaxed crystal phase, covering the complete set of entries listed in the paper's structural comparison (the “Bulk” column).

2. **Mulliken population analysis** (`mulliken_population.json`): atomic charges and bond populations for all atoms and bonds listed in the paper's population tables, computed for both the relaxed crystal (LDA) and the gas‑phase molecule (B3LYP).

3. **Hydrogen bond identification from PDOS** (`pDOS_hb_output.json`): the overlap energy range found from the PDOS of O‑2p and H‑1s states, together with the list of intra- and intermolecular hydrogen bonds identified from the orbital overlaps, including the three specific pairs discussed in the paper.

## Assets

- β-HMX experimental crystal structure: 10.1107/S0365110X63001545
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Psi4: https://psicode.org/
- LDA pseudopotentials (Perdew-Zunger): https://materialscloud.org/sssp/

## Workflow steps

### Step 1: Prepare initial crystal structure
- Role: process
- Action: Construct the β-HMX unit cell from published experimental lattice parameters (a=6.54 Å, b=11.05 Å, c=8.70 Å, β=124.3°, space group P21/c) and atomic coordinates from Cady et al. (1963) or Choi & Boutin (1970).
- Evidence: `/app/outputs/initial_structure.txt`

### Step 2: Crystal geometry relaxation (LDA-PZ)
- Role: process
- Action: Run Quantum ESPRESSO to perform full geometry relaxation of β-HMX crystal using the local density approximation (LDA) with Perdew-Zunger parametrization, employing ultrasoft pseudopotentials and appropriate convergence criteria. Allow cell shape, volume, and ionic positions to relax.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Crystal geometry extraction
- Role: scored (load-bearing)
- Action: From the relaxed crystal structure, compute the bond lengths and bond angles of the β-HMX molecule in the crystal phase. Cover the full set of bonds and angles as listed in the paper's structural analysis (the 'Bulk' column), including all bond lengths (e.g., N8-C2, N8-C1, N15-C2, N15-C17, N8-N7, N15-N18, N7-O12, N7-O11, N18-O25, N18-O24, C2-H6, C2-H5, C17-H23, C17-H22, H5...O12) and all bond angles (e.g., O12-N7-O11, N8-N7-O12, N8-N7-O11, N7-N8-C1, N7-N8-C2, C2-N8-C1, N8-C2-N15, N8-C2-H6, N8-C2-H5, N15-C2-H6, N15-C2-H5, H6-C2-H5, O25-N18-O24, N15-N18-O25, N15-N18-O24, N18-N15-C2, N18-N15-C17, C2-N15-C17, N21-C17-N15, N15-C17-H22, N15-C17-H23, N21-C17-H22, N21-C17-H23, H23-C17-H22).
- Output file: `/app/outputs/crystal_geometry.json`
- Format: json
- Contract: Object with 'bond_lengths' (array of objects with 'id' (string, one of: N8-C2, N8-C1, N15-C2, N15-C17, N8-N7, N15-N18, N7-O12, N7-O11, N18-O25, N18-O24, C2-H6, C2-H5, C17-H23, C17-H22, H5...O12) and 'value_angstrom' (float)), and 'bond_angles' (array of objects with 'id' (string, one of: O12-N7-O11, N8-N7-O12, N8-N7-O11, N7-N8-C1, N7-N8-C2, C2-N8-C1, N8-C2-N15, N8-C2-H6, N8-C2-H5, N15-C2-H6, N15-C2-H5, H6-C2-H5, O25-N18-O24, N15-N18-O25, N15-N18-O24, N18-N15-C2, N18-N15-C17, C2-N15-C17, N21-C17-N15, N15-C17-H22, N15-C17-H23, N21-C17-H22, N21-C17-H23, H23-C17-H22) and 'value_degree' (float)).
- Scoring: scored by hidden verifier

### Step 4: Gas‑phase molecule optimization (B3LYP)
- Role: process
- Action: Optimize the geometry of a single β-HMX molecule (extracted from the initial crystal structure) at the B3LYP/6‑31G(d,p) level of theory using an open‑source quantum chemistry code (e.g., Psi4).
- Evidence: `/app/outputs/gas_optimization.log`

### Step 5: Mulliken population analysis
- Role: scored (load-bearing)
- Action: Compute Mulliken atomic charges and bond populations for the relaxed β-HMX crystal (LDA) and for the gas‑phase molecule (B3LYP). Assemble results covering all atoms and bonds as listed in the paper's population tables, including atom-type labels C1, C2, H3, H4, H5, H6, N7, N8, N9, N10, O11, O12, O13, O14 and bond labels N8-N7, N7-O12, N7-O11, N8-C2, C2-H5, C2-H6, C2-N15, N15-N18, N18-O24, N18-O25, N15-C17, C17-H23, C17-H22, C17-N21, H5...O12, H19...O24.
- Output file: `/app/outputs/mulliken_population.json`
- Format: json
- Contract: Object with keys 'crystal' and 'gas'. Each contains 'atomic_charges' (object mapping atom-type labels (C1, C2, H3, H4, H5, H6, N7, N8, N9, N10, O11, O12, O13, O14) to floats) and 'bond_populations' (object mapping bond labels (N8-N7, N7-O12, N7-O11, N8-C2, C2-H5, C2-H6, C2-N15, N15-N18, N18-O24, N18-O25, N15-C17, C17-H23, C17-H22, C17-N21, H5...O12, H19...O24) to floats).
- Scoring: scored by hidden verifier

### Step 6: PDOS and hydrogen bond identification
- Role: scored
- Action: Compute the projected density of states (PDOS) for O-2p and H-1s orbitals from the relaxed crystal. Analyze the overlap between these orbital projections to identify candidate hydrogen bonds. Determine the energy range(s) where strong overlap occurs, and for each identified hydrogen bond record the donor H atom, acceptor O atom, and whether it is intra- or intermolecular.
- Output file: `/app/outputs/pDOS_hb_output.json`
- Format: json
- Contract: Object with 'overlap_energy_range' (string, e.g. '-7 eV to -6 eV') and 'hydrogen_bonds' (array of objects each with 'donor' (string, e.g. 'H5'), 'acceptor' (string, e.g. 'O12'), 'type' ('intramolecular' or 'intermolecular'), 'max_overlap_energy' (float, eV)). Include all hydrogen bonds identified from the PDOS analysis.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/crystal_geometry.json`
- `/app/outputs/mulliken_population.json`
- `/app/outputs/pDOS_hb_output.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### crystal_geometry.json
- path: `/app/outputs/crystal_geometry.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed bond lengths and angles of the β-HMX molecule in the crystal phase, covering the full set of entries from the paper's Table 1 'Bulk' column.
- schema:
  - `type`: object
  - `required`: `bond_lengths`, `bond_angles`
  - `properties`:
    - `bond_lengths`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `id`, `value_angstrom`
        - `properties`:
          - `id`:
            - `type`: string
          - `value_angstrom`:
            - `type`: number
    - `bond_angles`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `id`, `value_degree`
        - `properties`:
          - `id`:
            - `type`: string
          - `value_degree`:
            - `type`: number

### mulliken_population.json
- path: `/app/outputs/mulliken_population.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mulliken atomic charges and bond populations for the crystal (LDA) and gas-phase (B3LYP) β-HMX molecule, covering all atoms and bonds listed in the paper's Tables 2 and 3.
- schema:
  - `type`: object
  - `required`: `crystal`, `gas`
  - `properties`:
    - `crystal`:
      - `type`: object
      - `required`: `atomic_charges`, `bond_populations`
      - `properties`:
        - `atomic_charges`:
          - `type`: object
          - `additionalProperties`:
            - `type`: number
        - `bond_populations`:
          - `type`: object
          - `additionalProperties`:
            - `type`: number
    - `gas`:
      - `type`: object
      - `required`: `atomic_charges`, `bond_populations`
      - `properties`:
        - `atomic_charges`:
          - `type`: object
          - `additionalProperties`:
            - `type`: number
        - `bond_populations`:
          - `type`: object
          - `additionalProperties`:
            - `type`: number

### pDOS_hb_output.json
- path: `/app/outputs/pDOS_hb_output.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Hydrogen bond identification from PDOS orbital overlaps, including donor, acceptor, type, and overlap energy for each bond found.
- schema:
  - `type`: object
  - `required`: `overlap_energy_range`, `hydrogen_bonds`
  - `properties`:
    - `overlap_energy_range`:
      - `type`: string
    - `hydrogen_bonds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `donor`, `acceptor`, `type`, `max_overlap_energy`
        - `properties`:
          - `donor`:
            - `type`: string
          - `acceptor`:
            - `type`: string
          - `type`:
            - `type`: string
            - `enum`: `intramolecular`, `intermolecular`
          - `max_overlap_energy`:
            - `type`: number
            - `units`: eV

Notes: Hydrogen bond identification must include the donor-acceptor pairs detected from PDOS analysis. The overlap energy range is expected to be around the valence band region. Tolerance details are hidden in grading_spec.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "crystal_geometry.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "bond_lengths",
          "bond_angles"
        ],
        "properties": {
          "bond_lengths": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "id",
                "value_angstrom"
              ],
              "properties": {
                "id": {
                  "type": "string"
                },
                "value_angstrom": {
                  "type": "number"
                }
              }
            }
          },
          "bond_angles": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "id",
                "value_degree"
              ],
              "properties": {
                "id": {
                  "type": "string"
                },
                "value_degree": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Computed bond lengths and angles of the β-HMX molecule in the crystal phase, covering the full set of entries from the paper's Table 1 'Bulk' column."
    },
    {
      "file": "mulliken_population.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "crystal",
          "gas"
        ],
        "properties": {
          "crystal": {
            "type": "object",
            "required": [
              "atomic_charges",
              "bond_populations"
            ],
            "properties": {
              "atomic_charges": {
                "type": "object",
                "additionalProperties": {
                  "type": "number"
                }
              },
              "bond_populations": {
                "type": "object",
                "additionalProperties": {
                  "type": "number"
                }
              }
            }
          },
          "gas": {
            "type": "object",
            "required": [
              "atomic_charges",
              "bond_populations"
            ],
            "properties": {
              "atomic_charges": {
                "type": "object",
                "additionalProperties": {
                  "type": "number"
                }
              },
              "bond_populations": {
                "type": "object",
                "additionalProperties": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Mulliken atomic charges and bond populations for the crystal (LDA) and gas-phase (B3LYP) β-HMX molecule, covering all atoms and bonds listed in the paper's Tables 2 and 3."
    },
    {
      "file": "pDOS_hb_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "overlap_energy_range",
          "hydrogen_bonds"
        ],
        "properties": {
          "overlap_energy_range": {
            "type": "string"
          },
          "hydrogen_bonds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "donor",
                "acceptor",
                "type",
                "max_overlap_energy"
              ],
              "properties": {
                "donor": {
                  "type": "string"
                },
                "acceptor": {
                  "type": "string"
                },
                "type": {
                  "type": "string",
                  "enum": [
                    "intramolecular",
                    "intermolecular"
                  ]
                },
                "max_overlap_energy": {
                  "type": "number",
                  "units": "eV"
                }
              }
            }
          }
        }
      },
      "description": "Hydrogen bond identification from PDOS orbital overlaps, including donor, acceptor, type, and overlap energy for each bond found."
    }
  ],
  "notes": "Hydrogen bond identification must include the donor-acceptor pairs detected from PDOS analysis. The overlap energy range is expected to be around the valence band region. Tolerance details are hidden in grading_spec."
}
```

## How you are scored
A hidden verifier scores each workflow stage independently and combines the stage scores into a single final reward. **Reporting the paper’s original numbers is not sufficient.** The verifier compares your computed artifacts against reference values derived from the paper’s own results, using appropriate tolerances. Bond lengths and angles are compared to the reference geometry; Mulliken charges and populations are compared to the reference population tables; and the hydrogen bond list is audited for the required donor–acceptor pairs and the correct overlap energy range. The three scored artifacts together carry most of the reward, with the crystal geometry and Mulliken population making up the bulk. You must submit all three output files to receive credit.
