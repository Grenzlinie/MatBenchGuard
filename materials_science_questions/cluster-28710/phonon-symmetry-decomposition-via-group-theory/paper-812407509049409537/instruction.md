# Phonon symmetry decomposition via group theory

## Problem background
CuGeO3 undergoes a structural phase transition from a high-temperature undistorted phase to a low-temperature spin-Peierls phase, accompanied by a doubling of the unit cell. Group-theoretical analysis of the lattice vibrations provides the number and symmetry of allowed optical phonon modes in each phase. The predictions serve as a reference for interpreting infrared and Raman spectra and for testing structural models of the transition.

## Approach
Use the nuclear site group analysis method: for each occupied atomic site in the unit cell, decompose the site symmetry into the irreducible representations of the crystallographic point group; sum the contributions from all sites to obtain the total mechanical representation. Subtract the silent modes and the three acoustic modes to isolate the optical vibrations. Classify the optical modes into Raman-active (Ag, B1g, B2g, B3g) and infrared-active (B1u, B2u, B3u) symmetries using the character tables. Perform the analysis separately for the two crystal structures: the high-temperature phase (space group Pbmm, setting x||a, y||b, z||c) and the low-temperature spin-Peierls phase (space group Bbcm, same setting). The required structural information (space groups, lattice parameters, site symmetries) is detailed in the assets; no external retrieval is needed.

## Reproduction target
Compute the irreducible representations of the optical phonon modes at the Brillouin zone center for both phases. Write the results to the file `/app/outputs/phonon_mode_counts.json` following the exact schema shown in the output contract. The file must contain the integer counts of every Raman-active irreducible representation (Ag, B1g, B2g, B3g) and every IR-active irreducible representation (B1u, B2u, B3u) for the undistorted and distorted phases, together with the total number of Raman and IR modes for each phase. All numbers must be derived from the group-theoretical analysis, not by looking up external tables.

## Assets

- CuGeO3 crystal structure parameters (undistorted and distorted phases): explicitly listed below.
- Python environment with group-theory tools (spglib, numpy): python3, numpy, spglib

### Crystal structure data for CuGeO3

#### High-temperature undistorted phase (space group Pbmm, setting x||a, y||b, z||c)
- Unit cell: a=4.81 Å, b=8.47 Å, c=2.941 Å; 2 formula units (Cu2Ge2O6)
- Atomic sites (Wyckoff positions and point group of site):
  - Cu (2 atoms): site group C2h^y
  - Ge (2 atoms): site group C2v^z
  - O(1) (2 atoms): site group C2v^z
  - O(2) (4 atoms): site group Cs^xz

#### Low-temperature spin-Peierls phase (space group Bbcm, same setting)
- Unit cell: a'=2a, b'=b, c'=2c; 8 formula units (8 Cu, 8 Ge, 24 O)
- Atomic sites and site groups (from Braden et al.):
  - Cu (4 atoms): site group C2^x
  - O(1) (4 atoms): site group C2^y
  - Ge (4 atoms): site group Cs^yz
  - O(2a) (4 atoms): site group Cs^yz
  - O(2b) (4 atoms): site group Cs^yz

## Workflow steps

### Step 1: Group-theoretical phonon decomposition for both phases
- Role: scored (load-bearing)
- Action: Using the provided crystal structure information (space groups, site symmetries) perform a nuclear site group analysis for the high-temperature (Pbmm) and low-temperature (Bbcm) phases of CuGeO3. Compute the contribution of each occupied site to the total irreducible representation, subtract silent and acoustic modes, and obtain the irreducible representations of the optical vibrations. Classify the modes into Raman-active (Ag, B1g, B2g, B3g) and infrared-active (B1u, B2u, B3u) symmetries, and count the number of modes for each representation in both phases. Write the results to phonon_mode_counts.json according to the specified schema.
- Output file: `/app/outputs/phonon_mode_counts.json`
- Format: json
- Contract: {
  "undistorted": {
    "Raman": {"Ag": <int>, "B1g": <int>, "B2g": <int>, "B3g": <int>},
    "IR": {"B1u": <int>, "B2u": <int>, "B3u": <int>},
    "Raman_total": <int>,
    "IR_total": <int>
  },
  "distorted": {
    "Raman": {"Ag": <int>, "B1g": <int>, "B2g": <int>, "B3g": <int>},
    "IR": {"B1u": <int>, "B2u": <int>, "B3u": <int>},
    "Raman_total": <int>,
    "IR_total": <int>
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_mode_counts.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_mode_counts.json
- path: `/app/outputs/phonon_mode_counts.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Group-theoretical phonon mode decomposition for the high-temperature undistorted phase (Pbmm) and the low-temperature spin-Peierls phase (Bbcm) of CuGeO3. Contains counts of Raman-active and infrared-active optical phonon modes, broken down by irreducible representation, together with total Raman and IR counts for each phase. All values are fixed integers determined by the crystal structure and group theory.
- schema:
  - `type`: object
  - `required`: `undistorted`, `distorted`
  - `properties`:
    - `undistorted`:
      - `type`: object
      - `required`: `Raman`, `IR`, `Raman_total`, `IR_total`
      - `properties`:
        - `Raman`:
          - `type`: object
          - `required`: `Ag`, `B1g`, `B2g`, `B3g`
          - `properties`:
            - `Ag`:
              - `type`: integer
            - `B1g`:
              - `type`: integer
            - `B2g`:
              - `type`: integer
            - `B3g`:
              - `type`: integer
        - `IR`:
          - `type`: object
          - `required`: `B1u`, `B2u`, `B3u`
          - `properties`:
            - `B1u`:
              - `type`: integer
            - `B2u`:
              - `type`: integer
            - `B3u`:
              - `type`: integer
        - `Raman_total`:
          - `type`: integer
        - `IR_total`:
          - `type`: integer
    - `distorted`:
      - `type`: object
      - `required`: `Raman`, `IR`, `Raman_total`, `IR_total`
      - `properties`:
        - `Raman`:
          - `type`: object
          - `required`: `Ag`, `B1g`, `B2g`, `B3g`
          - `properties`:
            - `Ag`:
              - `type`: integer
            - `B1g`:
              - `type`: integer
            - `B2g`:
              - `type`: integer
            - `B3g`:
              - `type`: integer
        - `IR`:
          - `type`: object
          - `required`: `B1u`, `B2u`, `B3u`
          - `properties`:
            - `B1u`:
              - `type`: integer
            - `B2u`:
              - `type`: integer
            - `B3u`:
              - `type`: integer
        - `Raman_total`:
          - `type`: integer
        - `IR_total`:
          - `type`: integer
  - `additionalProperties`: False

Notes: No gold values or tolerances are disclosed here. The scoring compares each integer count against hidden reference values using exact match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_mode_counts.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "undistorted",
          "distorted"
        ],
        "properties": {
          "undistorted": {
            "type": "object",
            "required": [
              "Raman",
              "IR",
              "Raman_total",
              "IR_total"
            ],
            "properties": {
              "Raman": {
                "type": "object",
                "required": [
                  "Ag",
                  "B1g",
                  "B2g",
                  "B3g"
                ],
                "properties": {
                  "Ag": {
                    "type": "integer"
                  },
                  "B1g": {
                    "type": "integer"
                  },
                  "B2g": {
                    "type": "integer"
                  },
                  "B3g": {
                    "type": "integer"
                  }
                }
              },
              "IR": {
                "type": "object",
                "required": [
                  "B1u",
                  "B2u",
                  "B3u"
                ],
                "properties": {
                  "B1u": {
                    "type": "integer"
                  },
                  "B2u": {
                    "type": "integer"
                  },
                  "B3u": {
                    "type": "integer"
                  }
                }
              },
              "Raman_total": {
                "type": "integer"
              },
              "IR_total": {
                "type": "integer"
              }
            }
          },
          "distorted": {
            "type": "object",
            "required": [
              "Raman",
              "IR",
              "Raman_total",
              "IR_total"
            ],
            "properties": {
              "Raman": {
                "type": "object",
                "required": [
                  "Ag",
                  "B1g",
                  "B2g",
                  "B3g"
                ],
                "properties": {
                  "Ag": {
                    "type": "integer"
                  },
                  "B1g": {
                    "type": "integer"
                  },
                  "B2g": {
                    "type": "integer"
                  },
                  "B3g": {
                    "type": "integer"
                  }
                }
              },
              "IR": {
                "type": "object",
                "required": [
                  "B1u",
                  "B2u",
                  "B3u"
                ],
                "properties": {
                  "B1u": {
                    "type": "integer"
                  },
                  "B2u": {
                    "type": "integer"
                  },
                  "B3u": {
                    "type": "integer"
                  }
                }
              },
              "Raman_total": {
                "type": "integer"
              },
              "IR_total": {
                "type": "integer"
              }
            }
          }
        },
        "additionalProperties": false
      },
      "description": "Group-theoretical phonon mode decomposition for the high-temperature undistorted phase (Pbmm) and the low-temperature spin-Peierls phase (Bbcm) of CuGeO3. Contains counts of Raman-active and infrared-active optical phonon modes, broken down by irreducible representation, together with total Raman and IR counts for each phase. All values are fixed integers determined by the crystal structure and group theory."
    }
  ],
  "notes": "No gold values or tolerances are disclosed here. The scoring compares each integer count against hidden reference values using exact match."
}
```

## How you are scored
A hidden verifier will read your `phonon_mode_counts.json` and compare each integer count, including the totals, against the correct reference values obtained from the same group-theoretical analysis. Every individual count is checked; an exact match is required. No approximation or tolerance is allowed because the counts are fixed integers determined by the crystal symmetry. The final reward is the fraction of correctly matching fields. You must execute the full site group analysis correctly — guessing the numbers will not receive credit.
