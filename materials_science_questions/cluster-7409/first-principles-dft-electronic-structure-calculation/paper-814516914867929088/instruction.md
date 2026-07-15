# DFT Calculation of Ti-Ce Co-doped AlN: Structural, Energetic, Magnetic, and Electronic Properties

## Problem background
Diluted magnetic semiconductors based on transition-metal and rare-earth co-doped III-nitrides are promising for spintronic devices because they offer control over both charge and spin. This work focuses on Ti-Ce co-doped wurtzite AlN, a wide-bandgap semiconductor. The open questions are whether the nearest-neighbor substitutional arrangement of Ti and Ce is thermodynamically more stable than a next-nearest arrangement, whether the material exhibits a ferromagnetic ground state, and whether the electronic structure shows a hybrid intermediate band arising from Ti-3d and Ce-4f states. Answering these questions requires first-principles calculations of the structural, energetic, magnetic, and electronic properties of the co-doped system.

## Approach
The calculations use spin-polarized density functional theory with the GGA-PBE exchange-correlation functional and Hubbard U corrections (U=4.4 eV for Ti, 5.4 eV for Ce) to describe the localized 3d and 4f electrons. A 32-atom wurtzite AlN supercell is constructed, and two Al atoms are substitutionally replaced by one Ti and one Ce atom. Three configurations are compared: (i) Ti and Ce at nearest-neighbor cation sites with ferromagnetic spin alignment, (ii) the same composition with next-nearest dopant separation and ferromagnetic alignment, and (iii) the nearest-neighbor arrangement with antiferromagnetic alignment. For each configuration, the total energy is computed and the lattice vectors and atomic positions are fully relaxed. For the ferromagnetic nearest-neighbor case, the total and atom-projected density of states (PDOS) and the magnetic moments on Ti and Ce are also extracted. The relative stability is determined from total-energy differences, the magnetic ground state from the energy difference between antiferromagnetic and ferromagnetic arrangements, and the electronic structure from the PDOS analysis to identify any gap states and their orbital character.

## Reproduction target
Produce a single JSON file, `results.json`, containing the computed quantities for the three configurations:
- nearest-neighbor ferromagnetic (key `nearest_fm`): total energy (eV), relaxed lattice parameters `a_Ang` and `c_Ang` (Å), total magnetic moment `total_moment_muB` (μB), and atom-projected moments `ti_moment_muB` and `ce_moment_muB` (μB).
- next-nearest ferromagnetic (key `nextnearest_fm`): total energy (eV) and relaxed lattice parameters `a_Ang`, `c_Ang`.
- nearest-neighbor antiferromagnetic (key `afm_nearest`): total energy (eV).
- density of states for the nearest-neighbor ferromagnetic configuration (key `dos`): an energy grid `energy_list` (eV) and partial DOS arrays `pdos_ti_3d`, `pdos_ce_4f`, `pdos_n_2p`, `pdos_al_3p` of equal length.

From these data, the relative stability of the dopant arrangements, the magnetic ground state (the energy difference between antiferromagnetic and ferromagnetic states), the degree of lattice expansion, and the presence of an intermediate band with Ti-Ce hybridization are to be evaluated.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP pseudopotential library (PBE, efficient precision): https://www.materialscloud.org/discover/sssp/package

## Workflow steps

### Step 1: Generate supercell structures
- Role: process
- Action: Create input geometry files for the three 32-atom wurtzite AlN supercells required: (A) Al14Ti1Ce1N16 with Ti and Ce at nearest-neighbor cation sites and ferromagnetic spin alignment; (B) same composition with next-nearest separation and ferromagnetic alignment; (C) the nearest-neighbor configuration with antiferromagnetic spin alignment. Use experimental lattice constants a=3.11 Å, c=4.98 Å as starting points.
- Evidence: none

### Step 2: DFT relaxations, property extraction, and DOS computation
- Role: scored (load-bearing)
- Action: For each configuration (A, B, C), perform spin-polarized DFT calculations using an open-source plane-wave code with GGA-PBE+U (U_Ti=4.4 eV, U_Ce=5.4 eV) and the pseudopotential library listed. Fully relax ionic positions and lattice vectors, ensuring sufficient energy convergence. For configuration (A), additionally compute the total and partial density of states (DOS). Extract the following: total energy and final lattice parameters for all configurations; total and atom-resolved magnetic moments (on Ti and Ce) for configuration (A); and the DOS data for configuration (A). Write all results to 'results.json' with the schema defined in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: 'nearest_fm' (object: total_energy_eV, a_Ang, c_Ang, total_moment_muB, ti_moment_muB, ce_moment_muB), 'nextnearest_fm' (object: total_energy_eV, a_Ang, c_Ang), 'afm_nearest' (object: total_energy_eV), 'dos' (object: energy_list, pdos_ti_3d, pdos_ce_4f, pdos_n_2p, pdos_al_3p, all arrays of equal length).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Contains all re-derivable quantities from DFT calculations: energies, lattice parameters, magnetic moments, and PDOS arrays for the Ti-Ce co-doped AlN configurations.
- schema:
  - `type`: object
  - `required`: `nearest_fm`, `nextnearest_fm`, `afm_nearest`, `dos`
  - `properties`:
    - `nearest_fm`:
      - `type`: object
      - `properties`:
        - `total_energy_eV`:
          - `type`: number
        - `a_Ang`:
          - `type`: number
        - `c_Ang`:
          - `type`: number
        - `total_moment_muB`:
          - `type`: number
        - `ti_moment_muB`:
          - `type`: number
        - `ce_moment_muB`:
          - `type`: number
    - `nextnearest_fm`:
      - `type`: object
      - `properties`:
        - `total_energy_eV`:
          - `type`: number
        - `a_Ang`:
          - `type`: number
        - `c_Ang`:
          - `type`: number
    - `afm_nearest`:
      - `type`: object
      - `properties`:
        - `total_energy_eV`:
          - `type`: number
    - `dos`:
      - `type`: object
      - `properties`:
        - `energy_list`:
          - `type`: array
          - `items`:
            - `type`: number
        - `pdos_ti_3d`:
          - `type`: array
          - `items`:
            - `type`: number
        - `pdos_ce_4f`:
          - `type`: array
          - `items`:
            - `type`: number
        - `pdos_n_2p`:
          - `type`: array
          - `items`:
            - `type`: number
        - `pdos_al_3p`:
          - `type`: array
          - `items`:
            - `type`: number

Notes: The output file aggregates all scored targets: energetic ordering (nearest vs next-nearest), lattice expansion, FM ground state (ΔE > 0), magnetic moments, and DOS evidence for an intermediate band. The checker recomputes trends and structural features from this single artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "nearest_fm",
          "nextnearest_fm",
          "afm_nearest",
          "dos"
        ],
        "properties": {
          "nearest_fm": {
            "type": "object",
            "properties": {
              "total_energy_eV": {
                "type": "number"
              },
              "a_Ang": {
                "type": "number"
              },
              "c_Ang": {
                "type": "number"
              },
              "total_moment_muB": {
                "type": "number"
              },
              "ti_moment_muB": {
                "type": "number"
              },
              "ce_moment_muB": {
                "type": "number"
              }
            }
          },
          "nextnearest_fm": {
            "type": "object",
            "properties": {
              "total_energy_eV": {
                "type": "number"
              },
              "a_Ang": {
                "type": "number"
              },
              "c_Ang": {
                "type": "number"
              }
            }
          },
          "afm_nearest": {
            "type": "object",
            "properties": {
              "total_energy_eV": {
                "type": "number"
              }
            }
          },
          "dos": {
            "type": "object",
            "properties": {
              "energy_list": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "pdos_ti_3d": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "pdos_ce_4f": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "pdos_n_2p": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "pdos_al_3p": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Contains all re-derivable quantities from DFT calculations: energies, lattice parameters, magnetic moments, and PDOS arrays for the Ti-Ce co-doped AlN configurations."
    }
  ],
  "notes": "The output file aggregates all scored targets: energetic ordering (nearest vs next-nearest), lattice expansion, FM ground state (ΔE > 0), magnetic moments, and DOS evidence for an intermediate band. The checker recomputes trends and structural features from this single artifact."
}
```

## How you are scored
A hidden verifier will score your submitted `results.json` against reference quantities derived from the DFT reference. The scoring weights are distributed across several checks:
- **Energetic ordering**: The total energy of the nearest-neighbor ferromagnetic configuration must be lower than that of the next-nearest configuration, and the exchange energy ΔE = E_AFM − E_FM must be positive. Full credit for correct relative ordering and sign; partial credit if the gaps are small or the sign is incorrect.
- **Lattice parameters**: The relaxed lattice constants for the nearest-neighbor configuration must fall within generous tolerance windows derived from the paper’s reported expansion. Full credit within tolerance, decaying linearly outside.
- **Magnetic moments**: The total and atom-resolved moments on Ti and Ce must fall within tolerance of reference values, with credit decreasing for larger deviations.
- **Density of states**: The verifier scans the energy region between the valence band maximum and conduction band minimum and checks for a peak where the sum of `pdos_ti_3d` and `pdos_ce_4f` accounts for at least 30% of the total DOS at that energy, indicating a hybridized intermediate band. Full credit if such a peak is found, zero otherwise.
The final reward is a weighted sum of these sub-scores, ranging from 0.0 to 1.0. The tolerances are tight enough that merely reporting the paper’s numbers without genuine re-computation will not suffice; the intermediate band detection is based solely on the PDOS arrays you submit.
