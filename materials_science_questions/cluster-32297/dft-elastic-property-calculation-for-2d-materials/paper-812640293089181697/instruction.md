# Stability and Catalytic Activity of 2D Pentagonal MS Monolayers from DFT

## Problem background
Two-dimensional (2D) materials exhibit a wide range of electronic, magnetic, and catalytic properties, making them attractive for applications in nanoelectronics, energy storage, and catalysis. An open challenge is to design new 2D systems that combine robust stability with desirable functionalities, such as activity for the hydrogen evolution reaction (HER). This task explores, using density functional theory (DFT), whether a specific family of pentagonal transition‑metal sulphide monolayers (MS, with M = Fe, Mn, V) can be simultaneously stable as free‑standing layers and catalytically active for HER. The central questions are: Are these monolayers dynamically, thermally, and mechanically stable? What are their electronic and magnetic ground states? And do they possess hydrogen adsorption free energies near the ideal zero value?

## Approach
The investigation relies on first‑principles DFT calculations at the PBE‑GGA level of theory. For each material, the crystal structure is first relaxed to its ground state. Then a series of stability assessments are carried out: (1) phonon dispersion is computed to detect soft modes (imaginary frequencies) that would signal dynamic instability; (2) ab initio molecular dynamics (AIMD) simulations are performed at elevated temperature to gauge thermal stability by monitoring potential energy drift and structural deformation; (3) the 2D elastic constants are extracted from strain‑energy relations and checked against the Born mechanical stability criteria. The electronic and magnetic character is determined by comparing total energies of different spin configurations (nonmagnetic, ferromagnetic, and two antiferromagnetic orderings) and by inspecting the density of states. To evaluate catalytic activity, hydrogen atoms are adsorbed at the hollow site of the FeS and VS monolayers at various coverages, and the differential and average Gibbs free energies of adsorption are calculated, incorporating zero‑point energy and entropy corrections. The entire workflow is implemented using the open‑source plane‑wave DFT code Quantum ESPRESSO and the phonon analysis tool Phonopy, with PBE‑PAW pseudopotentials from the SSSP library.

## Reproduction target
Produce the following computed quantities, saved as structured JSON files under `/app/outputs`:
- `electronic_properties.json`: magnetic ground state (FM, AFM1, AFM2, or NM), metallic character (boolean), and total magnetic moment per unit cell for FeS, MnS, and VS.
- `phonon_max_imaginary.json`: maximum imaginary phonon frequency (THz) for each monolayer.
- `aimd_stability.json`: potential energy drift (eV/ps/atom) and a structural stability flag (boolean) from AIMD runs for FeS and VS at 673 K and MnS at 300 K.
- `elastic_constants.json`: 2D elastic constants c11, c12, and c66 (GPa) for each monolayer.
- `her_gibbs_free_energy.json`: differential and average Gibbs free energies (eV) of hydrogen adsorption on FeS and VS at coverages n = 1 through 8.

All outputs must follow the schemas described in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP Precision Pseudopotentials: https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Relax the atomic positions and lattice parameters of the FeS, MnS, and VS pentagonal monolayers using DFT with the PBE functional and a vacuum layer to avoid interlayer interactions. This provides ground-state structures for all subsequent calculations.
- Evidence: none

### Step 2: Electronic and magnetic ground state
- Role: scored
- Action: Determine the magnetic ground state for each monolayer by comparing total energies of nonmagnetic (NM), ferromagnetic (FM), and two antiferromagnetic (AFM1, AFM2) configurations. For the identified ground state, compute the electronic density of states to confirm metallic character and extract atomic magnetic moments. Report the ground state label, a boolean indicating metallic nature, and the total magnetic moment per unit cell.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: JSON object with keys 'FeS', 'MnS', 'VS'; each value is an object containing 'is_metallic' (boolean), 'magnetic_moment' (number in μB per unit cell), and 'ground_state' (string, one of 'NM', 'FM', 'AFM1', 'AFM2').
- Scoring: scored by hidden verifier

### Step 3: Phonon dispersion and dynamic stability
- Role: scored
- Action: Compute phonon dispersion curves for each monolayer using the finite-displacement method on a supercell. From the frequency data, determine the maximum imaginary phonon frequency (in THz). Report this value for each system as an indicator of dynamic stability (negligible imaginary frequencies indicate stability).
- Output file: `/app/outputs/phonon_max_imaginary.json`
- Format: json
- Contract: JSON object with keys 'FeS', 'MnS', 'VS'; each value is an object with key 'max_imaginary_frequency' (number in THz).
- Scoring: scored by hidden verifier

### Step 4: Ab initio molecular dynamics (thermal stability)
- Role: scored
- Action: Run AIMD simulations on supercells for FeS and VS at 673 K and for MnS at 300 K. Monitor the potential energy versus time to compute the linear drift (eV/ps/atom) and visually inspect the final structure to decide whether significant deformation occurred. Report the drift and a boolean stability flag for each run.
- Output file: `/app/outputs/aimd_stability.json`
- Format: json
- Contract: JSON object with keys 'FeS_673K', 'VS_673K', 'MnS_300K'; each value is an object containing 'potential_energy_drift' (number in eV/ps/atom) and 'structural_stable' (boolean).
- Scoring: scored by hidden verifier

### Step 5: Elastic constants and mechanical stability
- Role: scored (load-bearing)
- Action: Calculate the 2D elastic constants c11, c12, and c66 for each monolayer by applying a set of small in-plane strains to the relaxed unit cell and fitting the resulting stress or energy change to the elastic tensor. Report the values in GPa and verify that the Born stability criteria are satisfied.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: JSON object with keys 'FeS', 'MnS', 'VS'; each value is an object with keys 'c11_2D' (number), 'c12_2D' (number), 'c66_2D' (number), all in GPa.
- Scoring: scored by hidden verifier

### Step 6: Gibbs free energies for HER
- Role: scored
- Action: Construct supercells of FeS and VS in their ground magnetic state. Adsorb hydrogen atoms at the hollow site for coverages n = 1 to 8. For each coverage, compute the differential and average Gibbs free energies of hydrogen adsorption, incorporating a zero‑point energy and entropy correction. Report ΔG_H values in eV.
- Output file: `/app/outputs/her_gibbs_free_energy.json`
- Format: json
- Contract: JSON object with keys 'FeS', 'VS'; each value is an object with keys 'differential' (object mapping coverage integer to number in eV) and 'average' (object mapping coverage integer to number in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_properties.json`
- `/app/outputs/phonon_max_imaginary.json`
- `/app/outputs/aimd_stability.json`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/her_gibbs_free_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Magnetic ground state, metallic character, and magnetic moments of the three MS monolayers, to be compared against paper‑reported reference values.
- schema:
  - `type`: object
  - `required`: `FeS`, `MnS`, `VS`
  - `properties`:
    - `FeS`:
      - `type`: object
      - `required`: `is_metallic`, `magnetic_moment`, `ground_state`
      - `properties`:
        - `is_metallic`:
          - `type`: boolean
        - `magnetic_moment`:
          - `type`: number
          - `description`: total magnetic moment per unit cell in μB
        - `ground_state`:
          - `type`: string
          - `enum`: `NM`, `FM`, `AFM1`, `AFM2`
    - `MnS`:
      - `type`: object
      - `required`: `is_metallic`, `magnetic_moment`, `ground_state`
    - `VS`:
      - `type`: object
      - `required`: `is_metallic`, `magnetic_moment`, `ground_state`

### phonon_max_imaginary.json
- path: `/app/outputs/phonon_max_imaginary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum imaginary phonon frequency for each system; the checker verifies that the values are below the stability threshold.
- schema:
  - `type`: object
  - `required`: `FeS`, `MnS`, `VS`
  - `properties`:
    - `FeS`:
      - `type`: object
      - `required`: `max_imaginary_frequency`
      - `properties`:
        - `max_imaginary_frequency`:
          - `type`: number
          - `description`: maximum imaginary phonon frequency in THz (≤0.1 THz satisfies dynamic stability)
    - `MnS`:
      - `type`: object
      - `required`: `max_imaginary_frequency`
    - `VS`:
      - `type`: object
      - `required`: `max_imaginary_frequency`

### aimd_stability.json
- path: `/app/outputs/aimd_stability.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: AIMD stability indicators; the checker verifies that the potential energy drift is below a threshold and that structural_stable is true.
- schema:
  - `type`: object
  - `required`: `FeS_673K`, `VS_673K`, `MnS_300K`
  - `properties`:
    - `FeS_673K`:
      - `type`: object
      - `required`: `potential_energy_drift`, `structural_stable`
      - `properties`:
        - `potential_energy_drift`:
          - `type`: number
          - `description`: linear drift of potential energy in eV/ps/atom
        - `structural_stable`:
          - `type`: boolean
    - `VS_673K`:
      - `type`: object
      - `required`: `potential_energy_drift`, `structural_stable`
    - `MnS_300K`:
      - `type`: object
      - `required`: `potential_energy_drift`, `structural_stable`

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: 2D elastic constants; the checker compares the reported values to paper‑reported reference values within a tolerance, and verifies the Born stability criteria.
- schema:
  - `type`: object
  - `required`: `FeS`, `MnS`, `VS`
  - `properties`:
    - `FeS`:
      - `type`: object
      - `required`: `c11_2D`, `c12_2D`, `c66_2D`
      - `properties`:
        - `c11_2D`:
          - `type`: number
          - `description`: 2D elastic constant c11 in GPa
        - `c12_2D`:
          - `type`: number
        - `c66_2D`:
          - `type`: number
    - `MnS`:
      - `type`: object
      - `required`: `c11_2D`, `c12_2D`, `c66_2D`
    - `VS`:
      - `type`: object
      - `required`: `c11_2D`, `c12_2D`, `c66_2D`

### her_gibbs_free_energy.json
- path: `/app/outputs/her_gibbs_free_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gibbs free energies of hydrogen adsorption for FeS and VS at various coverages; the checker compares the reported values to paper‑reported references within a tolerance.
- schema:
  - `type`: object
  - `required`: `FeS`, `VS`
  - `properties`:
    - `FeS`:
      - `type`: object
      - `required`: `differential`, `average`
      - `properties`:
        - `differential`:
          - `type`: object
          - `description`: mapping from hydrogen coverage integer n (1‑8) to differential Gibbs free energy in eV
        - `average`:
          - `type`: object
          - `description`: mapping from hydrogen coverage integer n (1‑8) to average Gibbs free energy in eV
    - `VS`:
      - `type`: object
      - `required`: `differential`, `average`

Notes: The hidden checker compares the agent's computed quantities against the paper's reported values and stability criteria using appropriate tolerances. No gold values or tolerances are disclosed in this public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "FeS",
          "MnS",
          "VS"
        ],
        "properties": {
          "FeS": {
            "type": "object",
            "required": [
              "is_metallic",
              "magnetic_moment",
              "ground_state"
            ],
            "properties": {
              "is_metallic": {
                "type": "boolean"
              },
              "magnetic_moment": {
                "type": "number",
                "description": "total magnetic moment per unit cell in μB"
              },
              "ground_state": {
                "type": "string",
                "enum": [
                  "NM",
                  "FM",
                  "AFM1",
                  "AFM2"
                ]
              }
            }
          },
          "MnS": {
            "type": "object",
            "required": [
              "is_metallic",
              "magnetic_moment",
              "ground_state"
            ]
          },
          "VS": {
            "type": "object",
            "required": [
              "is_metallic",
              "magnetic_moment",
              "ground_state"
            ]
          }
        }
      },
      "description": "Magnetic ground state, metallic character, and magnetic moments of the three MS monolayers, to be compared against paper‑reported reference values."
    },
    {
      "file": "phonon_max_imaginary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "FeS",
          "MnS",
          "VS"
        ],
        "properties": {
          "FeS": {
            "type": "object",
            "required": [
              "max_imaginary_frequency"
            ],
            "properties": {
              "max_imaginary_frequency": {
                "type": "number",
                "description": "maximum imaginary phonon frequency in THz (≤0.1 THz satisfies dynamic stability)"
              }
            }
          },
          "MnS": {
            "type": "object",
            "required": [
              "max_imaginary_frequency"
            ]
          },
          "VS": {
            "type": "object",
            "required": [
              "max_imaginary_frequency"
            ]
          }
        }
      },
      "description": "Maximum imaginary phonon frequency for each system; the checker verifies that the values are below the stability threshold."
    },
    {
      "file": "aimd_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "FeS_673K",
          "VS_673K",
          "MnS_300K"
        ],
        "properties": {
          "FeS_673K": {
            "type": "object",
            "required": [
              "potential_energy_drift",
              "structural_stable"
            ],
            "properties": {
              "potential_energy_drift": {
                "type": "number",
                "description": "linear drift of potential energy in eV/ps/atom"
              },
              "structural_stable": {
                "type": "boolean"
              }
            }
          },
          "VS_673K": {
            "type": "object",
            "required": [
              "potential_energy_drift",
              "structural_stable"
            ]
          },
          "MnS_300K": {
            "type": "object",
            "required": [
              "potential_energy_drift",
              "structural_stable"
            ]
          }
        }
      },
      "description": "AIMD stability indicators; the checker verifies that the potential energy drift is below a threshold and that structural_stable is true."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "FeS",
          "MnS",
          "VS"
        ],
        "properties": {
          "FeS": {
            "type": "object",
            "required": [
              "c11_2D",
              "c12_2D",
              "c66_2D"
            ],
            "properties": {
              "c11_2D": {
                "type": "number",
                "description": "2D elastic constant c11 in GPa"
              },
              "c12_2D": {
                "type": "number"
              },
              "c66_2D": {
                "type": "number"
              }
            }
          },
          "MnS": {
            "type": "object",
            "required": [
              "c11_2D",
              "c12_2D",
              "c66_2D"
            ]
          },
          "VS": {
            "type": "object",
            "required": [
              "c11_2D",
              "c12_2D",
              "c66_2D"
            ]
          }
        }
      },
      "description": "2D elastic constants; the checker compares the reported values to paper‑reported reference values within a tolerance, and verifies the Born stability criteria."
    },
    {
      "file": "her_gibbs_free_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "FeS",
          "VS"
        ],
        "properties": {
          "FeS": {
            "type": "object",
            "required": [
              "differential",
              "average"
            ],
            "properties": {
              "differential": {
                "type": "object",
                "description": "mapping from hydrogen coverage integer n (1‑8) to differential Gibbs free energy in eV"
              },
              "average": {
                "type": "object",
                "description": "mapping from hydrogen coverage integer n (1‑8) to average Gibbs free energy in eV"
              }
            }
          },
          "VS": {
            "type": "object",
            "required": [
              "differential",
              "average"
            ]
          }
        }
      },
      "description": "Gibbs free energies of hydrogen adsorption for FeS and VS at various coverages; the checker compares the reported values to paper‑reported references within a tolerance."
    }
  ],
  "notes": "The hidden checker compares the agent's computed quantities against the paper's reported values and stability criteria using appropriate tolerances. No gold values or tolerances are disclosed in this public contract."
}
```

## How you are scored
The hidden verifier scores each output file independently. For quantities that have a clear direction of goodness (e.g., lower potential energy drift, Gibbs free energy closer to zero, elastic constants consistent with stability criteria), the verifier checks whether your reported value satisfies the required performance level. If your result meets or exceeds that level, you receive full credit for that artifact; otherwise, the score decreases as the result deviates further. For categorical properties (ground state, metallic character), an exact match is required. The overall reward is a weighted sum of the individual artifact scores, with the elastic constants and the HER Gibbs free energies carrying the highest weights. The specific reference values and tolerance margins are not disclosed — you must compute the properties honestly to obtain a high score.
