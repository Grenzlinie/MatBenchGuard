# Magnetic and Ferroelectric Properties of SrNbO3-xNx from First-Principles

## Problem background
Multi-anion oxynitride thin films, such as SrNbO3-xNx, can simultaneously host magnetic moments and structural distortions that break inversion symmetry, potentially leading to multiferroic behavior. Substituting oxygen with nitrogen introduces changes in the d-electron occupation of the transition metal and modifies the local structural environment, giving rise to magnetic ordering and polar displacements. Both the magnetic and ferroelectric properties depend sensitively on the nitrogen concentration x and on epitaxial strain. Understanding how these properties evolve as a function of composition and strain is essential for designing room-temperature multiferroics through anionic engineering. In this task, you will investigate the magnetic order and ferroelectric response of SrNbO3-xNx using first-principles density-functional theory (DFT) calculations.

## Approach
You will perform DFT+U calculations within the generalized-gradient approximation (PBEsol functional), applying an on-site Hubbard U correction to the Nb d states within the rotationally invariant Liechtenstein scheme. Starting from the I4/mcm parent structure of SrNbO2N, you will create supercells with different O/N ratios to represent compositions x = 0, 0.25, 0.5, 0.75, and 1.0, each in cis- and trans-type N-ordering configurations. After structural relaxation, you will evaluate the relative total energies of ferromagnetic (FM) and A-, C-, G-type antiferromagnetic (AFM) spin configurations to identify the magnetic ground state and the magnetic moment per formula unit for each composition. For the fully nitrogen-substituted end-member (x = 1), you will additionally investigate the ferroelectric properties: under unstrained, out-of-plane strained, and in-plane strained conditions, you will map the total energy as a function of the amplitude of the relevant polar distortion mode to extract the double-well energy depth and the polar space group. This procedure reveals how magnetic and ferroelectric properties evolve with nitrogen content and strain.

## Reproduction target
Compute and report the magnetic moment per formula unit and the magnetic ground state for SrNbO3-xNx at x = 0, 0.25, 0.5, 0.75, and 1.0. Additionally, compute the ferroelectric double-well depth (in meV per formula unit) and the polar space group for cis- and trans-type SrNbO2N under three distinct conditions: fully relaxed (unstrained), out-of-plane epitaxial constraint, and in-plane epitaxial constraint. Write these results to the two scored output files: `magnetic_properties.json` and `ferroelectric_properties.json`, following the formats and contracts defined in this document.

## Assets

- Crystal structure of SrNbO2N (I4/mcm space group): 10.1107/S010827010401511X
- Open-source DFT code (e.g., Quantum ESPRESSO) with PBEsol GGA and PAW pseudopotentials: https://www.quantum-espresso.org/
- SOD (Site Occupation Disorder) code (optional): https://doi.org/10.1088/0953-8984/19/25/256201

## Workflow steps

### Step 1: Generate N-substituted supercell structures
- Role: process
- Action: Using the parent I4/mcm structure of SrNbO2N, create initial atomic configurations for SrNbO3-xNx at x = 0, 0.25, 0.5, 0.75, 1.0 with cis- and trans-type N ordering. The supercell should contain 20 atoms (4 formula units) to match the paper.
- Evidence: `/app/outputs/structures_generated.log`

### Step 2: Geometry optimization (unstrained)
- Role: process
- Action: Perform DFT+U geometry optimization (ionic positions and cell volume/angles) for every structure from Step 1 without any epitaxial strain constraint. Use PBEsol GGA, Liechtenstein DFT+U with U = 4.0 eV on Nb d states, plane-wave cutoff ≥ 600 eV, Γ-centered k-mesh at least 8×8×6.
- Evidence: `/app/outputs/optimization_unstrained.log`

### Step 3: Magnetic ordering total-energy calculations (unstrained)
- Role: process
- Action: For each unstrained optimized structure, compute single-point DFT+U total energies and magnetic moments for four magnetic configurations: ferromagnetic (FM) and A-, C-, and G-type antiferromagnetic (AFM) orderings. Use the same DFT parameters as Step 2.
- Evidence: `/app/outputs/magnetic_energies_raw.json`

### Step 4: Determine magnetic ground state and moment per formula unit
- Role: scored (load-bearing)
- Action: Read the raw magnetic energies from Step 3, identify the lowest-energy magnetic ordering for each composition x (select the lower-energy between cis and trans configurations), extract the magnetic moment per formula unit (total magnetic moment per 20-atom cell divided by 4), and write the result to magnetic_properties.json.
- Output file: `/app/outputs/magnetic_properties.json`
- Format: json
- Contract: JSON array of objects with keys: x (number, 0.0, 0.25, 0.5, 0.75, 1.0), magnetic_moment_muB_per_fu (number), ground_state (string, one of 'A-AFM', 'C-AFM', 'G-AFM', 'FM', 'NM').
- Scoring: scored by hidden verifier

### Step 5: Strained geometry optimization for SrNbO2N (x=1)
- Role: process
- Action: For the cis- and trans-type SrNbO2N structures (x=1), perform geometry optimizations under three strain conditions: (a) unstrained (full relaxation), (b) out-of-plane strained (in-plane lattice constants fixed to a≈4.00 Å, b≈4.00 Å, with the N-Nb-N zig-zag chains aligned in-plane), and (c) in-plane strained (in-plane a,b fixed to same values but with chains aligned out-of-plane). Use same DFT parameters.
- Evidence: `/app/outputs/strained_optimized.log`

### Step 6: Double-well energy scan along polar distortion mode
- Role: process
- Action: For each strained structure from Step 05, compute the DFT total energy as a function of the amplitude of the polar distortion mode (e.g., Γ3- mode for trans, Sr-O displacement mode for cis). Displace atoms along the mode eigenvector, fixing the distortion amplitude, and collect energy vs amplitude.
- Evidence: `/app/outputs/double_well_scans.json`

### Step 7: Extract ferroelectric double-well depth and polar space group
- Role: scored (load-bearing)
- Action: From the energy scans of Step 06, determine the double-well depth (energy difference between the relaxed polar minimum and the symmetric undistorted structure) for each cis and trans configuration under the three strain conditions. Identify the polar space group of the distorted structure. Write results to ferroelectric_properties.json.
- Output file: `/app/outputs/ferroelectric_properties.json`
- Format: json
- Contract: JSON object with keys 'cis' and 'trans'. Each contains sub-objects 'unstrained', 'out_of_plane_strain', 'in_plane_strain'. Each sub-object has keys 'double_well_depth_meV_per_fu' (number) and 'polar_space_group' (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_properties.json`
- `/app/outputs/ferroelectric_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_properties.json
- path: `/app/outputs/magnetic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Magnetic ground state and moment per formula unit for x = 0, 0.25, 0.5, 0.75, 1.0. The moment is compared to the paper's nonmonotonic trend with tolerance ±0.1 μB/f.u.; the ground state label is matched exactly against A-AFM, FM, NM, etc.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `x`:
        - `type`: number
      - `magnetic_moment_muB_per_fu`:
        - `type`: number
      - `ground_state`:
        - `type`: string
    - `required`: `x`, `magnetic_moment_muB_per_fu`, `ground_state`

### ferroelectric_properties.json
- path: `/app/outputs/ferroelectric_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ferroelectric double-well depth and polar space group for cis- and trans-type SrNbO2N (x=1) under unstrained, out-of-plane strained, and in-plane strained conditions. Depths compared within ±50 meV/f.u.; space groups matched exactly.
- schema:
  - `type`: object
  - `properties`:
    - `cis`:
      - `type`: object
      - `properties`:
        - `unstrained`:
          - `type`: object
          - `properties`:
            - `double_well_depth_meV_per_fu`:
              - `type`: number
            - `polar_space_group`:
              - `type`: string
          - `required`: `double_well_depth_meV_per_fu`, `polar_space_group`
        - `out_of_plane_strain`:
          - `type`: object
          - `properties`:
            - `double_well_depth_meV_per_fu`:
              - `type`: number
            - `polar_space_group`:
              - `type`: string
          - `required`: `double_well_depth_meV_per_fu`, `polar_space_group`
        - `in_plane_strain`:
          - `type`: object
          - `properties`:
            - `double_well_depth_meV_per_fu`:
              - `type`: number
            - `polar_space_group`:
              - `type`: string
          - `required`: `double_well_depth_meV_per_fu`, `polar_space_group`
      - `required`: `unstrained`, `out_of_plane_strain`, `in_plane_strain`
    - `trans`:
      - `type`: object
      - `properties`:
        - `unstrained`:
          - `type`: object
          - `properties`:
            - `double_well_depth_meV_per_fu`:
              - `type`: number
            - `polar_space_group`:
              - `type`: string
          - `required`: `double_well_depth_meV_per_fu`, `polar_space_group`
        - `out_of_plane_strain`:
          - `type`: object
          - `properties`:
            - `double_well_depth_meV_per_fu`:
              - `type`: number
            - `polar_space_group`:
              - `type`: string
          - `required`: `double_well_depth_meV_per_fu`, `polar_space_group`
        - `in_plane_strain`:
          - `type`: object
          - `properties`:
            - `double_well_depth_meV_per_fu`:
              - `type`: number
            - `polar_space_group`:
              - `type`: string
          - `required`: `double_well_depth_meV_per_fu`, `polar_space_group`
      - `required`: `unstrained`, `out_of_plane_strain`, `in_plane_strain`
  - `required`: `cis`, `trans`

Notes: The workflow omits COHP analysis, exchange parameter calculations, full phonon dispersion, and electron doping analysis, consistent with the taskability do_not_attempt list. The agent must re-run the DFT calculations to produce these scored artifacts; no pre-computed data is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "x": {
              "type": "number"
            },
            "magnetic_moment_muB_per_fu": {
              "type": "number"
            },
            "ground_state": {
              "type": "string"
            }
          },
          "required": [
            "x",
            "magnetic_moment_muB_per_fu",
            "ground_state"
          ]
        }
      },
      "description": "Magnetic ground state and moment per formula unit for x = 0, 0.25, 0.5, 0.75, 1.0. The moment is compared to the paper's nonmonotonic trend with tolerance ±0.1 μB/f.u.; the ground state label is matched exactly against A-AFM, FM, NM, etc."
    },
    {
      "file": "ferroelectric_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "cis": {
            "type": "object",
            "properties": {
              "unstrained": {
                "type": "object",
                "properties": {
                  "double_well_depth_meV_per_fu": {
                    "type": "number"
                  },
                  "polar_space_group": {
                    "type": "string"
                  }
                },
                "required": [
                  "double_well_depth_meV_per_fu",
                  "polar_space_group"
                ]
              },
              "out_of_plane_strain": {
                "type": "object",
                "properties": {
                  "double_well_depth_meV_per_fu": {
                    "type": "number"
                  },
                  "polar_space_group": {
                    "type": "string"
                  }
                },
                "required": [
                  "double_well_depth_meV_per_fu",
                  "polar_space_group"
                ]
              },
              "in_plane_strain": {
                "type": "object",
                "properties": {
                  "double_well_depth_meV_per_fu": {
                    "type": "number"
                  },
                  "polar_space_group": {
                    "type": "string"
                  }
                },
                "required": [
                  "double_well_depth_meV_per_fu",
                  "polar_space_group"
                ]
              }
            },
            "required": [
              "unstrained",
              "out_of_plane_strain",
              "in_plane_strain"
            ]
          },
          "trans": {
            "type": "object",
            "properties": {
              "unstrained": {
                "type": "object",
                "properties": {
                  "double_well_depth_meV_per_fu": {
                    "type": "number"
                  },
                  "polar_space_group": {
                    "type": "string"
                  }
                },
                "required": [
                  "double_well_depth_meV_per_fu",
                  "polar_space_group"
                ]
              },
              "out_of_plane_strain": {
                "type": "object",
                "properties": {
                  "double_well_depth_meV_per_fu": {
                    "type": "number"
                  },
                  "polar_space_group": {
                    "type": "string"
                  }
                },
                "required": [
                  "double_well_depth_meV_per_fu",
                  "polar_space_group"
                ]
              },
              "in_plane_strain": {
                "type": "object",
                "properties": {
                  "double_well_depth_meV_per_fu": {
                    "type": "number"
                  },
                  "polar_space_group": {
                    "type": "string"
                  }
                },
                "required": [
                  "double_well_depth_meV_per_fu",
                  "polar_space_group"
                ]
              }
            },
            "required": [
              "unstrained",
              "out_of_plane_strain",
              "in_plane_strain"
            ]
          }
        },
        "required": [
          "cis",
          "trans"
        ]
      },
      "description": "Ferroelectric double-well depth and polar space group for cis- and trans-type SrNbO2N (x=1) under unstrained, out-of-plane strained, and in-plane strained conditions. Depths compared within ±50 meV/f.u.; space groups matched exactly."
    }
  ],
  "notes": "The workflow omits COHP analysis, exchange parameter calculations, full phonon dispersion, and electron doping analysis, consistent with the taskability do_not_attempt list. The agent must re-run the DFT calculations to produce these scored artifacts; no pre-computed data is provided."
}
```

## How you are scored
A hidden verifier independently checks your scored artifact files. It does not simply read self-reported claims; it validates your computed results against reference expectations. The verifier assigns a reward for each scored stage, and the final task reward is a weighted combination of these rewards. Completing all workflow steps correctly is necessary to produce accurate artifacts and achieve a high score. Simply writing expected numbers without executing the required simulations will not pass.
