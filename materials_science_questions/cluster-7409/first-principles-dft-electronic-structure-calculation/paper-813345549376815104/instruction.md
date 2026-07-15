# DFT electronic structure of defective CaTiO₃ with Pr and Zn doping

## Problem background
Pr-doped CaTiO3 is a red persistent phosphor displaying a sharp emission at 614 nm upon ultraviolet excitation. The luminescence mechanism is believed to involve in-gap electronic states introduced by the Pr activator, and experiments show that co-doping with Zn enhances the red emission and prolongs the afterglow. Understanding the nature and energy positions of these in-gap states, their orbital character, and how Zn impurities modify them is crucial for designing better phosphors. This task uses first-principles density functional theory (DFT) to compute the electronic structure of three defect configurations in orthorhombic CaTiO3: (1) a Ca vacancy compensated by a Pr on a Ca site (VCP), (2) Zn substituting on a Ca site with Pr on a Ca site (ZCP), and (3) Zn substituting on a Ti site with Pr on a Ca site (ZTP). The computed results will allow assignment of the observed optical transitions and quantification of the stabilization and structural distortion induced by Zn co-doping.

## Approach
Perform spin-polarized DFT calculations within the GGA+U framework to describe the correlated Pr‑4f states, using the Perdew–Burke–Ernzerhof (PBE) functional and a Hubbard U correction applied to Pr‑4f orbitals. Model the orthorhombic CaTiO3 host as a 2×2×2 supercell (160 atoms) and construct the three defective supercells listed in the workflow steps, together with the corresponding isolated defect cells needed for binding energy evaluation. For each structure, relax the atomic positions and compute the total energy, then obtain the electronic band structure along a high-symmetry path and the total and partial density of states (DOS). Analyze the DOS to identify in-gap levels and their dominant orbital contributions (Pr‑4f, O‑2p, Ti‑3d, Zn‑3d). From the relaxed geometries, extract the average Pr–O bond length. Calculate the binding energies of the (V_Ca,Pr_Ca), (Zn_Ca,Pr_Ca), and (Zn_Ti,Pr_Ca) complexes using the standard formulation that references the total energies of the pristine host and the isolated point defects. The approach directly reveals how the two principal in-gap states – one assigned to the red emission and one to a charge-transfer excitation – are affected by the presence and site preference of Zn.

## Reproduction target
Reproduce the electronic structure analysis by running the GGA+U DFT pipeline described above and extracting the key physical quantities for each defect configuration. Write a single JSON file named `electronic_structure_results.json` containing, for each of the three configurations VCP, ZCP, and ZTP: the direct band gap (in eV), a list of the two most prominent in-gap states (each with its energy above the valence band maximum in eV and its dominant orbital character as a string), the binding energy of the defect complex (in eV), and the average Pr–O bond length (in Å). The values must originate from the DFT calculations themselves, not from pre-existing tables or the source paper. This file is the sole scored artifact.

## Assets

- Quantum ESPRESSO open-source DFT code: https://www.quantum-espresso.org
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Orthorhombic CaTiO3 crystal structure: COD 9000398

## Workflow steps

### Step 1: Pristine CaTiO3 DFT reference calculation
- Role: process
- Action: Perform a DFT calculation for the pristine orthorhombic CaTiO3 supercell (2x2x2) to obtain the relaxed structure, band structure, total energy, and to verify the chosen computational setup.
- Evidence: `/app/outputs/pristine_calc.log`

### Step 2: Supercell construction for defect systems
- Role: process
- Action: Build the 2x2x2 supercell models for VCP (Ca vacancy + Pr on Ca), ZCP (Zn on Ca + Pr on Ca), ZTP (Zn on Ti + Pr on Ca), and the corresponding isolated defect cells (V_Ca, Pr_Ca, Zn_Ca, Zn_Ti) needed for binding energy calculations.
- Evidence: `/app/outputs/defect_structures.cif`

### Step 3: DFT geometry relaxation and total energy
- Role: process
- Action: Perform spin-polarized GGA+U calculations for all defect supercells (VCP, ZCP, ZTP and isolated defects). Converge the atomic positions and record the ground-state total energies.
- Evidence: `/app/outputs/relaxation.log`

### Step 4: Binding energy analysis
- Role: process
- Action: Calculate the binding energies of the (V_Ca,Pr_Ca), (Zn_Ca,Pr_Ca), and (Zn_Ti,Pr_Ca) complexes using the total energies from step03 and a standard binding energy formula.
- Evidence: `/app/outputs/binding_energies.txt`

### Step 5: Band structure and density of states calculation
- Role: process
- Action: Compute the electronic band structures, total density of states (TDOS), and partial density of states (PDOS) for the relaxed VCP, ZCP, and ZTP structures. Extract Pr-O bond distances from the relaxed geometries.
- Evidence: `/app/outputs/dos_data.json`

### Step 6: Extract electronic structure results
- Role: scored (load-bearing)
- Action: From the DFT outputs (total energies, band structures, DOS, relaxed geometries), determine for each of the three defect configurations (VCP, ZCP, ZTP): the direct band gap (eV), the energies above the VBM and dominant orbital character of the two principal in-gap states, the binding energy of the defect complex (eV), and the average Pr-O bond length (Å). Write the results to electronic_structure_results.json.
- Output file: `/app/outputs/electronic_structure_results.json`
- Format: json
- Contract: {
  "VCP": {
    "band_gap_eV": <float>,
    "in_gap_levels": [
      {"energy_above_VBM_eV": <float>, "dominant_orbital": <string>},
      ...
    ],
    "binding_energy_eV": <float>,
    "average_Pr_O_bond_length_A": <float>
  },
  "ZCP": { ... },
  "ZTP": { ... }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_structure_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_structure_results.json
- path: `/app/outputs/electronic_structure_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The required electronic structure parameters for the three defect configurations. The hidden checker compares the reported values to paper reference values. For binding energies, a negative (more stable) value is considered correct.
- schema:
  - `type`: object
  - `required`: `VCP`, `ZCP`, `ZTP`
  - `properties`:
    - `VCP`:
      - `type`: object
      - `required`: `band_gap_eV`, `in_gap_levels`, `binding_energy_eV`, `average_Pr_O_bond_length_A`
      - `properties`:
        - `band_gap_eV`:
          - `type`: number
        - `in_gap_levels`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `energy_above_VBM_eV`, `dominant_orbital`
            - `properties`:
              - `energy_above_VBM_eV`:
                - `type`: number
              - `dominant_orbital`:
                - `type`: string
        - `binding_energy_eV`:
          - `type`: number
        - `average_Pr_O_bond_length_A`:
          - `type`: number
    - `ZCP`:
      - `type`: object
      - `required`: `band_gap_eV`, `in_gap_levels`, `binding_energy_eV`, `average_Pr_O_bond_length_A`
      - `properties`:
        - `band_gap_eV`:
          - `type`: number
        - `in_gap_levels`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `energy_above_VBM_eV`, `dominant_orbital`
            - `properties`:
              - `energy_above_VBM_eV`:
                - `type`: number
              - `dominant_orbital`:
                - `type`: string
        - `binding_energy_eV`:
          - `type`: number
        - `average_Pr_O_bond_length_A`:
          - `type`: number
    - `ZTP`:
      - `type`: object
      - `required`: `band_gap_eV`, `in_gap_levels`, `binding_energy_eV`, `average_Pr_O_bond_length_A`
      - `properties`:
        - `band_gap_eV`:
          - `type`: number
        - `in_gap_levels`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `energy_above_VBM_eV`, `dominant_orbital`
            - `properties`:
              - `energy_above_VBM_eV`:
                - `type`: number
              - `dominant_orbital`:
                - `type`: string
        - `binding_energy_eV`:
          - `type`: number
        - `average_Pr_O_bond_length_A`:
          - `type`: number

Notes: All DFT quantities are method-dependent; the hidden tolerances account for typical spread between different DFT implementations (GGA+U). The agent must reproduce the full pipeline, not just print known numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "VCP",
          "ZCP",
          "ZTP"
        ],
        "properties": {
          "VCP": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "in_gap_levels",
              "binding_energy_eV",
              "average_Pr_O_bond_length_A"
            ],
            "properties": {
              "band_gap_eV": {
                "type": "number"
              },
              "in_gap_levels": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "energy_above_VBM_eV",
                    "dominant_orbital"
                  ],
                  "properties": {
                    "energy_above_VBM_eV": {
                      "type": "number"
                    },
                    "dominant_orbital": {
                      "type": "string"
                    }
                  }
                }
              },
              "binding_energy_eV": {
                "type": "number"
              },
              "average_Pr_O_bond_length_A": {
                "type": "number"
              }
            }
          },
          "ZCP": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "in_gap_levels",
              "binding_energy_eV",
              "average_Pr_O_bond_length_A"
            ],
            "properties": {
              "band_gap_eV": {
                "type": "number"
              },
              "in_gap_levels": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "energy_above_VBM_eV",
                    "dominant_orbital"
                  ],
                  "properties": {
                    "energy_above_VBM_eV": {
                      "type": "number"
                    },
                    "dominant_orbital": {
                      "type": "string"
                    }
                  }
                }
              },
              "binding_energy_eV": {
                "type": "number"
              },
              "average_Pr_O_bond_length_A": {
                "type": "number"
              }
            }
          },
          "ZTP": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "in_gap_levels",
              "binding_energy_eV",
              "average_Pr_O_bond_length_A"
            ],
            "properties": {
              "band_gap_eV": {
                "type": "number"
              },
              "in_gap_levels": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "energy_above_VBM_eV",
                    "dominant_orbital"
                  ],
                  "properties": {
                    "energy_above_VBM_eV": {
                      "type": "number"
                    },
                    "dominant_orbital": {
                      "type": "string"
                    }
                  }
                }
              },
              "binding_energy_eV": {
                "type": "number"
              },
              "average_Pr_O_bond_length_A": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "The required electronic structure parameters for the three defect configurations. The hidden checker compares the reported values to paper reference values. For binding energies, a negative (more stable) value is considered correct."
    }
  ],
  "notes": "All DFT quantities are method-dependent; the hidden tolerances account for typical spread between different DFT implementations (GGA+U). The agent must reproduce the full pipeline, not just print known numbers."
}
```

## How you are scored
A hidden verifier evaluates your submission automatically. It reads `electronic_structure_results.json` and compares each reported quantity (band gaps, in-gap level energies, binding energies, Pr–O bond lengths) to reference values derived from the paper, using tolerances that accommodate legitimate differences between DFT implementations. The verifier also checks that the dominant orbital character for each in-gap state aligns with expectations (e.g., Pr‑4f dominated). Each quantity contributes a defined weight to the overall reward. Merely writing down expected numbers without actually performing the full computational workflow will not satisfy the verifier.
