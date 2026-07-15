# Group-theoretical decomposition of lattice vibrations for potassium lithium niobate

## Problem background
Potassium lithium niobate (KLN) is a tetragonal tungsten bronze (TB) type ferroelectric material with potential nonlinear-optical applications. Understanding its lattice vibrations and their symmetry properties is essential for interpreting Raman and infrared spectra. The crystal structure is described by space group P4bm (No. 100) at room temperature, with two formula units per unit cell. The atomic positions (based on experimental crystallographic data) are given below. The task is to perform a factor-group analysis of these lattice vibrations at the Brillouin zone center (Γ point) to determine the irreducible representation contents of the optic phonon modes and their Raman and infrared activity according to the point group 4mm.

| Atom | Wyckoff position | Site label (TB framework) | Occupancy (if mixed) |
|------|-------------------|---------------------------|----------------------|
| Nb(1) | 2b | B1 | – |
| Nb(2) | 8d | B2 | – |
| 0.873 K(1) / 0.127 Li | 2a | A1 | mixed |
| 0.989 K(2) / 0.011 Li | 4c | A2 | mixed |
| 0.942 Li / 0.058 Nb | 4c | C | mixed |
| O(1) | 8d | – | – |
| O(2) | 8d | – | – |
| O(3) | 4c | – | – |
| O(4) | 2b | – | – |
| O(5) | 8d | – | – |

## Approach
The factor-group analysis proceeds by constructing the reducible representation for the vibrational degrees of freedom in the unit cell. For each Wyckoff site, one computes the character of the permutation representation under the symmetry operations of the point group 4mm (the factor group of P4bm at Γ). The reducible representation is then reduced into irreducible representations (A1, A2, B1, B2, E) using the character table of 4mm. Subtracting the three acoustic modes (which transform as A1 + E) from the total mechanical representation gives the optic phonon representation. Finally, each irreducible representation is classified as Raman active (R) and/or infrared active (IR) based on the transformation properties of the dipole moment and polarizability tensor in 4mm: A1 and E are both Raman and IR active; B1 and B2 are Raman active only; A2 is silent.

## Reproduction target
Produce a JSON file (`mode_decomposition.json`) containing an object with keys 'A1', 'A2', 'B1', 'B2', 'E'. Each key maps to an object with integer field 'count' (the number of optic phonon modes of that symmetry) and boolean fields 'raman' and 'ir' indicating activity. The decomposition must be consistent with the crystal structure given above and the point group 4mm character table.

## Assets

- pymatgen (Python Materials Genomics): pymatgen

## Workflow steps

### Step 1: Group-theoretical decomposition of lattice vibrations at Γ point
- Role: scored (load-bearing)
- Action: Using the KLN crystal structure (space group P4bm, atomic positions provided in the instruction), compute the reducible representations for each Wyckoff site, reduce them to irreducible representations of the point group 4mm, separate the optic phonon modes, and classify each irreducible representation as Raman active and/or infrared active. Write the results to the output JSON file.
- Output file: `/app/outputs/mode_decomposition.json`
- Format: json
- Contract: {"A1": {"count": <int>, "raman": <true|false>, "ir": <true|false>}, "A2": {"count": <int>, "raman": <true|false>, "ir": <true|false>}, "B1": {"count": <int>, "raman": <true|false>, "ir": <true|false>}, "B2": {"count": <int>, "raman": <true|false>, "ir": <true|false>}, "E": {"count": <int>, "raman": <true|false>, "ir": <true|false>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mode_decomposition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mode_decomposition.json
- path: `/app/outputs/mode_decomposition.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Group-theoretical decomposition of lattice vibrations into irreducible representations with Raman and IR activity classification.
- schema:
  - `type`: object
  - `required`: `A1`, `A2`, `B1`, `B2`, `E`
  - `properties`:
    - `A1`:
      - `type`: object
      - `required`: `count`, `raman`, `ir`
      - `properties`:
        - `count`:
          - `type`: integer
        - `raman`:
          - `type`: boolean
        - `ir`:
          - `type`: boolean
    - `A2`:
      - `type`: object
      - `required`: `count`, `raman`, `ir`
      - `properties`:
        - `count`:
          - `type`: integer
        - `raman`:
          - `type`: boolean
        - `ir`:
          - `type`: boolean
    - `B1`:
      - `type`: object
      - `required`: `count`, `raman`, `ir`
      - `properties`:
        - `count`:
          - `type`: integer
        - `raman`:
          - `type`: boolean
        - `ir`:
          - `type`: boolean
    - `B2`:
      - `type`: object
      - `required`: `count`, `raman`, `ir`
      - `properties`:
        - `count`:
          - `type`: integer
        - `raman`:
          - `type`: boolean
        - `ir`:
          - `type`: boolean
    - `E`:
      - `type`: object
      - `required`: `count`, `raman`, `ir`
      - `properties`:
        - `count`:
          - `type`: integer
        - `raman`:
          - `type`: boolean
        - `ir`:
          - `type`: boolean

Notes: Only the group-theoretical decomposition at the Γ point is scoped. The paper's infrared reflectivity multioscillator fitting is omitted because it requires the raw measured reflectivity spectra, which are not publicly available as digital data and are not part of the separable computational sub-result.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mode_decomposition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "A1",
          "A2",
          "B1",
          "B2",
          "E"
        ],
        "properties": {
          "A1": {
            "type": "object",
            "required": [
              "count",
              "raman",
              "ir"
            ],
            "properties": {
              "count": {
                "type": "integer"
              },
              "raman": {
                "type": "boolean"
              },
              "ir": {
                "type": "boolean"
              }
            }
          },
          "A2": {
            "type": "object",
            "required": [
              "count",
              "raman",
              "ir"
            ],
            "properties": {
              "count": {
                "type": "integer"
              },
              "raman": {
                "type": "boolean"
              },
              "ir": {
                "type": "boolean"
              }
            }
          },
          "B1": {
            "type": "object",
            "required": [
              "count",
              "raman",
              "ir"
            ],
            "properties": {
              "count": {
                "type": "integer"
              },
              "raman": {
                "type": "boolean"
              },
              "ir": {
                "type": "boolean"
              }
            }
          },
          "B2": {
            "type": "object",
            "required": [
              "count",
              "raman",
              "ir"
            ],
            "properties": {
              "count": {
                "type": "integer"
              },
              "raman": {
                "type": "boolean"
              },
              "ir": {
                "type": "boolean"
              }
            }
          },
          "E": {
            "type": "object",
            "required": [
              "count",
              "raman",
              "ir"
            ],
            "properties": {
              "count": {
                "type": "integer"
              },
              "raman": {
                "type": "boolean"
              },
              "ir": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "description": "Group-theoretical decomposition of lattice vibrations into irreducible representations with Raman and IR activity classification."
    }
  ],
  "notes": "Only the group-theoretical decomposition at the Γ point is scoped. The paper's infrared reflectivity multioscillator fitting is omitted because it requires the raw measured reflectivity spectra, which are not publicly available as digital data and are not part of the separable computational sub-result."
}
```

## How you are scored
Your submitted `mode_decomposition.json` will be evaluated by a hidden verifier. The verifier checks each irreducible representation's count and activity flags against the correct values. Each irrep is scored individually; the total reward is the weighted sum of correct entries. Exact counts are required; approximate counts receive no credit. The raman and ir flags must match the true symmetry-determined activity. Note that the verifier does not run any computation; it only validates your JSON structure and compares values.
