# Stability analysis of MgO–H2O compounds at megabar pressures

## Problem background
Magnesium oxide (MgO) and water (H₂O) are among the most abundant materials in planetary interiors, and their chemical interaction at extreme pressures directly influences planetary structure, thermal evolution, and volatile storage. At low pressures MgO and H₂O form brucite (Mg(OH)₂), which decomposes upon further compression, but it is unknown whether they recombine into new compounds at the megabar conditions found inside ice-giant planets and water-rich exoplanets. Computational structure searches and first‑principles calculations have identified several new MgO–H₂O phases at these pressures, whose thermodynamic and dynamical stability, as well as their pressure-dependent stability ranges, are the subject of this task. The aim is to determine, from provided crystal structures, whether these phases are stable against decomposition into the pure end‑members, and to verify that they are dynamically stable by checking for the absence of imaginary phonon modes.

## Approach
The central hypothesis is that three specific MgO–H₂O compounds — Mg₂O₃H₂, MgO₃H₄, and MgO₄H₆ — are thermodynamically stable at megabar pressures and show no imaginary phonon frequencies. To test this, the workflow uses density functional theory (DFT) calculations and lattice‑dynamics analysis. Starting from the published crystal structures of the three compounds (CIF files), as well as the reference phases MgO in the B1 and B2 structures and high‑pressure water ice polymorphs (ice‑X, Pbcm, Pbca, P3₁21), geometry relaxations are performed at a series of pressures between 200 and 1000 GPa. The relaxed total energies are combined with zero‑point energy corrections obtained from phonon calculations to compute formation enthalpies per formula unit. At each pressure, a convex hull of formation enthalpy as a function of composition is constructed; any compound whose enthalpy lies on the hull is considered thermodynamically stable with respect to decomposition into the end‑members. The pressure intervals where each compound appears on the hull define its thermodynamic stability range. Dynamical stability is assessed by computing the phonon dispersion at a representative pressure inside each compound's stability range and confirming the absence of imaginary (negative) frequencies.

## Reproduction target
Produce two JSON artifacts under /app/outputs: 1) step_01_convex_hull.json, containing the formation enthalpy data and convex hull analysis that determine the pressure ranges where Mg₂O₃H₂, MgO₃H₄, and MgO₄H₆ are thermodynamically stable; and 2) step_02_phonon_stability.json, confirming that each compound is dynamically stable (no imaginary phonon modes) at a pressure within its predicted stability range. The calculations must use an open‑source plane‑wave DFT code (e.g. Quantum ESPRESSO) with the PBE functional and PAW pseudopotentials, and a phonon code (e.g. PHONOPY) to obtain zero‑point energies and phonon dispersions. The reference end‑member phases must be included in the convex hull construction. The output schemas and scoring criteria are detailed in the workflow steps and output contract below.

## Assets

- Crystal structure CIF files for Mg₂O₃H₂, MgO₃H₄, MgO₄H₆: https://www.nature.com/articles/s41467-023-36802-8
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/
- Reference crystal structures (MgO B1, B2; high‑pressure water ice phases)

## Workflow steps

### Step 1: DFT geometry relaxations and total energies
- Role: process
- Action: For each of the three MgO–H₂O compounds (from the provided CIF files) and for all required reference phases (MgO B1, B2 and the high‑pressure water ice phases), prepare input files for Quantum ESPRESSO (or an equivalent open‑source DFT code). Perform structural relaxations at a series of pressures ranging from 200 GPa to 1000 GPa (e.g., every 50 GPa) using the PBE functional and PAW pseudopotentials. Store the relaxed total energies and final geometries.
- Evidence: `/app/outputs/dft_energies.log`

### Step 2: Phonon calculations and zero‑point energies
- Role: process
- Action: Using the relaxed structures from step_dft_relax, run phonon calculations with PHONOPY (or the phonon routines of the chosen DFT code) to obtain phonon densities of states and zero‑point energies (ZPE) for each compound at each pressure. Save the ZPE values for the convex‑hull construction.
- Evidence: `/app/outputs/zpe_data.json`

### Step 3: Convex hull analysis and stability ranges
- Role: scored (load-bearing)
- Action: Combine the DFT total energies (from step_dft_relax) with the ZPE corrections (from step_phonon_zpe) to obtain formation enthalpies per formula unit for all compounds and reference end‑members at each pressure. Construct the formation enthalpy convex hull; identify which compositions lie on the hull (thermodynamically stable). Determine the pressure ranges over which Mg₂O₃H₂, MgO₃H₄, and MgO₄H₆ are predicted to be stable. Output the hull data and inferred stability ranges as a JSON file.
- Output file: `/app/outputs/step_01_convex_hull.json`
- Format: json
- Contract: JSON object with keys: pressures (array of numbers, GPa), compounds (array of strings: "Mg2O3H2", "MgO3H4", "MgO4H6"), formation_enthalpy_per_fu (object mapping compound names to arrays of numbers in eV/f.u.), reference_enthalpies (object with exactly the following keys: "MgO_B1", "MgO_B2", "ice_X", "ice_Pbcm", "ice_Pbca", "ice_P3121", each an array of same length as pressures), stable_ranges (object mapping compound names to 2-element arrays [min_GPa, max_GPa]).
- Scoring: scored by hidden verifier

### Step 4: Dynamical stability check
- Role: scored
- Action: For each of the three compounds at a representative pressure within its predicted stability range (e.g., ~400 GPa for Mg₂O₃H₂, ~600 GPa for MgO₃H₄, ~500 GPa for MgO₄H₆), inspect the phonon spectrum from step_phonon_zpe for imaginary modes. Verify that no imaginary phonon frequencies exist. Output a JSON file with the stability verdict.
- Output file: `/app/outputs/step_02_phonon_stability.json`
- Format: json
- Contract: JSON object with key 'compounds' mapping each compound name to an object with fields 'pressure' (number, GPa) and 'has_imaginary_modes' (boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_convex_hull.json`
- `/app/outputs/step_02_phonon_stability.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_convex_hull.json
- path: `/app/outputs/step_01_convex_hull.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Convex hull data and inferred pressure stability ranges for Mg2O3H2, MgO3H4, MgO4H6.
- schema:
  - `type`: object
  - `required`: `pressures`, `compounds`, `formation_enthalpy_per_fu`, `reference_enthalpies`, `stable_ranges`
  - `properties`:
    - `pressures`:
      - `type`: array
      - `items`:
        - `type`: number
      - `units`: GPa
    - `compounds`:
      - `type`: array
      - `items`:
        - `type`: string
      - `minItems`: 3
      - `maxItems`: 3
      - `contains`:
        - `enum`: `Mg2O3H2`, `MgO3H4`, `MgO4H6`
    - `formation_enthalpy_per_fu`:
      - `type`: object
      - `properties`:
        - `Mg2O3H2`:
          - `type`: array
          - `items`:
            - `type`: number
        - `MgO3H4`:
          - `type`: array
          - `items`:
            - `type`: number
        - `MgO4H6`:
          - `type`: array
          - `items`:
            - `type`: number
      - `required`: `Mg2O3H2`, `MgO3H4`, `MgO4H6`
    - `reference_enthalpies`:
      - `type`: object
      - `required`: `MgO_B1`, `MgO_B2`, `ice_X`, `ice_Pbcm`, `ice_Pbca`, `ice_P3121`
      - `properties`:
        - `MgO_B1`:
          - `type`: array
          - `items`:
            - `type`: number
        - `MgO_B2`:
          - `type`: array
          - `items`:
            - `type`: number
        - `ice_X`:
          - `type`: array
          - `items`:
            - `type`: number
        - `ice_Pbcm`:
          - `type`: array
          - `items`:
            - `type`: number
        - `ice_Pbca`:
          - `type`: array
          - `items`:
            - `type`: number
        - `ice_P3121`:
          - `type`: array
          - `items`:
            - `type`: number
      - `additionalProperties`: False
    - `stable_ranges`:
      - `type`: object
      - `properties`:
        - `Mg2O3H2`:
          - `type`: array
          - `minItems`: 2
          - `maxItems`: 2
          - `items`:
            - `type`: number
        - `MgO3H4`:
          - `type`: array
          - `minItems`: 2
          - `maxItems`: 2
          - `items`:
            - `type`: number
        - `MgO4H6`:
          - `type`: array
          - `minItems`: 2
          - `maxItems`: 2
          - `items`:
            - `type`: number
      - `required`: `Mg2O3H2`, `MgO3H4`, `MgO4H6`

### step_02_phonon_stability.json
- path: `/app/outputs/step_02_phonon_stability.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dynamical stability verdicts (no imaginary phonon modes) for the three compounds at representative pressures.
- schema:
  - `type`: object
  - `required`: `compounds`
  - `properties`:
    - `compounds`:
      - `type`: object
      - `required`: `Mg2O3H2`, `MgO3H4`, `MgO4H6`
      - `additionalProperties`: False
      - `properties`:
        - `Mg2O3H2`:
          - `type`: object
          - `required`: `pressure`, `has_imaginary_modes`
          - `properties`:
            - `pressure`:
              - `type`: number
              - `units`: GPa
            - `has_imaginary_modes`:
              - `type`: boolean
        - `MgO3H4`:
          - `type`: object
          - `required`: `pressure`, `has_imaginary_modes`
          - `properties`:
            - `pressure`:
              - `type`: number
              - `units`: GPa
            - `has_imaginary_modes`:
              - `type`: boolean
        - `MgO4H6`:
          - `type`: object
          - `required`: `pressure`, `has_imaginary_modes`
          - `properties`:
            - `pressure`:
              - `type`: number
              - `units`: GPa
            - `has_imaginary_modes`:
              - `type`: boolean

Notes: The reference phases include MgO B1, B2 and relevant high‑pressure ice polymorphs; their structures are publicly available and must be included in the convex hull construction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_convex_hull.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "pressures",
          "compounds",
          "formation_enthalpy_per_fu",
          "reference_enthalpies",
          "stable_ranges"
        ],
        "properties": {
          "pressures": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "units": "GPa"
          },
          "compounds": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "minItems": 3,
            "maxItems": 3,
            "contains": {
              "enum": [
                "Mg2O3H2",
                "MgO3H4",
                "MgO4H6"
              ]
            }
          },
          "formation_enthalpy_per_fu": {
            "type": "object",
            "properties": {
              "Mg2O3H2": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "MgO3H4": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "MgO4H6": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            },
            "required": [
              "Mg2O3H2",
              "MgO3H4",
              "MgO4H6"
            ]
          },
          "reference_enthalpies": {
            "type": "object",
            "required": [
              "MgO_B1",
              "MgO_B2",
              "ice_X",
              "ice_Pbcm",
              "ice_Pbca",
              "ice_P3121"
            ],
            "properties": {
              "MgO_B1": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "MgO_B2": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "ice_X": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "ice_Pbcm": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "ice_Pbca": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "ice_P3121": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            },
            "additionalProperties": false
          },
          "stable_ranges": {
            "type": "object",
            "properties": {
              "Mg2O3H2": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": {
                  "type": "number"
                }
              },
              "MgO3H4": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": {
                  "type": "number"
                }
              },
              "MgO4H6": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": {
                  "type": "number"
                }
              }
            },
            "required": [
              "Mg2O3H2",
              "MgO3H4",
              "MgO4H6"
            ]
          }
        }
      },
      "description": "Convex hull data and inferred pressure stability ranges for Mg2O3H2, MgO3H4, MgO4H6."
    },
    {
      "file": "step_02_phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "compounds"
        ],
        "properties": {
          "compounds": {
            "type": "object",
            "required": [
              "Mg2O3H2",
              "MgO3H4",
              "MgO4H6"
            ],
            "additionalProperties": false,
            "properties": {
              "Mg2O3H2": {
                "type": "object",
                "required": [
                  "pressure",
                  "has_imaginary_modes"
                ],
                "properties": {
                  "pressure": {
                    "type": "number",
                    "units": "GPa"
                  },
                  "has_imaginary_modes": {
                    "type": "boolean"
                  }
                }
              },
              "MgO3H4": {
                "type": "object",
                "required": [
                  "pressure",
                  "has_imaginary_modes"
                ],
                "properties": {
                  "pressure": {
                    "type": "number",
                    "units": "GPa"
                  },
                  "has_imaginary_modes": {
                    "type": "boolean"
                  }
                }
              },
              "MgO4H6": {
                "type": "object",
                "required": [
                  "pressure",
                  "has_imaginary_modes"
                ],
                "properties": {
                  "pressure": {
                    "type": "number",
                    "units": "GPa"
                  },
                  "has_imaginary_modes": {
                    "type": "boolean"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Dynamical stability verdicts (no imaginary phonon modes) for the three compounds at representative pressures."
    }
  ],
  "notes": "The reference phases include MgO B1, B2 and relevant high‑pressure ice polymorphs; their structures are publicly available and must be included in the convex hull construction."
}
```

## How you are scored
A hidden verifier reads your submitted artifacts and compares them to reference results extracted from the original study. For step_01_convex_hull.json, the verifier inspects the formation enthalpies, the convex hull construction, and the inferred stability pressure ranges. It checks that the stability ranges overlap with the expected intervals within permitted tolerances that account for different DFT implementations and pseudopotentials. For step_02_phonon_stability.json, the verifier checks that the reported has_imaginary_modes field is false for each compound, confirming dynamical stability. The two artifacts are weighted; the convex hull artifact receives a higher weight, while the phonon stability artifact contributes a smaller but essential fraction. The final reward is a float between 0 and 1 that measures how well your computed results reproduce the key stability properties. You do NOT need to guess the paper's exact numbers; you must execute the described workflow to obtain the properties from first‑principles calculations.
