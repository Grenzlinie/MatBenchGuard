# Elastic Constants of Monovalent Metals from Electrostatic and Exchange Interactions

## Problem background
The elastic behavior of monovalent metals (lithium, sodium, potassium, copper) is governed by the response of the crystal lattice to small deformations. For volume‑preserving distortions, the change in total energy depends only on the electrostatic lattice energy of the ions and valence electrons, and on the exchange interaction between the closed electron shells of the ions. The electrostatic contribution can be obtained from an Ewald lattice sum differentiated for two independent distortion types: a tetragonal strain and a shear. The exchange contribution arises from repulsive and van der Waals forces between ions and can be modeled using central‑force potentials with parameters derived from alkali‑halide studies (for the alkalis) or from statistical calculations (for copper). Combining these contributions yields the elastic constants A = c11 − c12 and 2B = c44, from which the full elastic tensor and the Debye characteristic temperatures can be derived. This task requires computing all of these quantities numerically.

## Approach
The overall method follows the Wigner–Seitz cellular approach: the crystal is divided into atomic polyhedra, and the wave function is taken to be nearly constant near the boundaries for slowly varying elastic distortions. For volume‑preserving strains the kinetic energy and the Fermi energy of the valence electrons remain unchanged; only the electrostatic lattice energy (ions treated as point charges plus a uniform negative background) and the closed‑shell ion‑ion interaction change.

The electrostatic part is computed via the Ewald technique. Starting from the lattice energy expression, the second derivatives with respect to the independent distortion variables are evaluated using the given lattice vector and reciprocal lattice vector expressions for fcc and bcc structures. The agent must implement the summations in reciprocal space and real space, using the formulas appropriate for tetragonal strain and shear.

The exchange interaction between ion cores is treated as a sum of central‑force two‑body potentials. For the alkali metals Li, Na, and K, the repulsive part is described by a Born‑Mayer potential with parameters (ionic radii, b, ρ) taken from work on alkali halides; for copper, the first and second derivatives of the repulsive energy are provided directly. A London van der Waals attraction is included via a −c/r^6 term with c values from the literature. The contribution of these forces to A and 2B is obtained by applying the formulas for nearest and next‑nearest neighbours listed in the workflow steps.

Once the total A and 2B are known, the full elastic constants c11, c12, c44 are obtained from the relations that involve the experimental compressibility 2C. Finally, the Debye characteristic temperatures for the alkalis are computed from the elastic constants via the Born–Kármán formula, using a numerical angular integration with a Hopf–Lechner expansion to sufficient order. All required physical constants, lattice constants, compressibilities, and interaction parameters are supplied in the task instructions.

## Reproduction target
The task is to compute the following quantities entirely from the provided formulas and parameters, and to write them as structured JSON files:

- The electrostatic contributions A^(l) and 2B^(l) for fcc and bcc lattices, in units of e^2/(2δ) (where δ is the lattice constant).
- For each metal (Li, Na, K, Cu): the decomposition of A = c11 − c12 and 2B = c44 into electrostatic, repulsive, van der Waals, and total contributions, in units of 10^11 dyn/cm².
- For each metal: the full elastic constants 2C (compressibility), A, 2B, c11, c12, and c44, in 10^11 dyn/cm². For copper, three separate sets corresponding to theoretical, experimental room‑temperature, and experimental absolute‑zero values must be provided.
- For the three alkali metals (Li, Na, K): the Debye characteristic temperature (in Kelvin) computed without closed‑shell ion interaction (using only the electrostatic part) and with the full ion interaction (using total A and 2B).

These quantities are to be saved in the four JSON files specified in the workflow steps, following the exact structure and naming described in the output contract.

## Assets

- Born-Mayer repulsive potential parameters for alkali ions
- London van der Waals coefficients for alkali ions
- Repulsive potential parameters for copper
- Experimental lattice constants and compressibilities

## Workflow steps

### Step 1: Electrostatic contributions to elastic constants
- Role: scored
- Action: Compute the electrostatic contributions A^(l) and 2B^(l) for face-centred cubic (fcc) and body-centred cubic (bcc) lattices. Use the Ewald lattice sum differentiation method for volume-preserving distortions (tetragonal strain and shear) with the appropriate lattice vectors and numerical evaluations. Output the results in units of e^2/(2δ), where δ is the lattice constant.
- Output file: `/app/outputs/step_01_table1.json`
- Format: json
- Contract: object with keys fcc and bcc; each is an object with keys A_l (number) and 2B_l (number); all values dimensionless (units e^2/(2δ)).
- Scoring: scored by hidden verifier

### Step 2: Composition of elastic constants (exchange and total)
- Role: scored
- Action: For Li, Na, K, and Cu, compute the closed‑shell exchange contributions A^(I) and 2B^(I) using the provided repulsive potentials (Born‑Mayer for alkalis, derived values for Cu) and van der Waals potentials. For each metal, sum the electrostatic contribution (from step_01) with the repulsive and van der Waals contributions to obtain the total A (c11−c12) and 2B (c44). Output the breakdown as shown in Table V, with all values in units of 10^11 dyn/cm².
- Output file: `/app/outputs/step_02_table5.json`
- Format: json
- Contract: object with keys Li, Na, K, Cu. Each metal is an object containing A and 2B. Each of A and 2B is an object with keys: electrostatic (number), repulsive (number), van_der_Waals (number), total (number). All numbers in 10^11 dyn/cm².
- Scoring: scored by hidden verifier

### Step 3: Full elastic constants c11, c12, c44
- Role: scored
- Action: Using the total A and 2B from step_02 together with the provided experimental compressibilities 2C, compute the full elastic constants c11, c12, and c44 for Li, Na, K, and Cu using the relations c11 = (2C)/3 + (2/3)A, c12 = (2C)/3 − (1/3)A, c44 = B. For Cu, also include the experimental values at room temperature and extrapolated to absolute zero. Output all values in units of 10^11 dyn/cm².
- Output file: `/app/outputs/step_03_table4.json`
- Format: json
- Contract: object with keys Li, Na, K, Cu. Li, Na, K each an object with keys: 2C, A, 2B, c11, c12, c44 (all numbers, 10^11 dyn/cm²). Cu is an object with three sub-keys: theoretical, experimental_room, experimental_absolute_zero; each an object with the same structure. All numbers in 10^11 dyn/cm².
- Scoring: scored by hidden verifier

### Step 4: Debye characteristic temperatures
- Role: scored (load-bearing)
- Action: Using the elastic constants c11, c12, c44 from step_03 and the density derived from the lattice constant, compute the Debye characteristic temperatures for Li, Na, and K via the Born‑Kármán formula. Compute both the case without closed‑shell ion interaction (using only electrostatic contributions to A and 2B) and the case with the full ion interaction (total A and 2B). Perform the angular integration numerically. Output the temperatures in Kelvin.
- Output file: `/app/outputs/step_04_table6.json`
- Format: json
- Contract: object with keys Li, Na, K. Each metal is an object with keys: without_ion_interaction (number, K) and with_ion_interaction (number, K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_table1.json`
- `/app/outputs/step_02_table5.json`
- `/app/outputs/step_03_table4.json`
- `/app/outputs/step_04_table6.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_table1.json
- path: `/app/outputs/step_01_table1.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electrostatic contributions A^(l) and 2B^(l) in units of e^2/(2δ).
- schema:
  - `type`: object
  - `required`: `fcc`, `bcc`
  - `properties`:
    - `fcc`:
      - `type`: object
      - `required`: `A_l`, `2B_l`
      - `properties`:
        - `A_l`:
          - `type`: number
        - `2B_l`:
          - `type`: number
    - `bcc`:
      - `type`: object
      - `required`: `A_l`, `2B_l`
      - `properties`:
        - `A_l`:
          - `type`: number
        - `2B_l`:
          - `type`: number

### step_02_table5.json
- path: `/app/outputs/step_02_table5.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Composition of A and 2B (10^11 dyn/cm²).
- schema:
  - `type`: object
  - `required`: `Li`, `Na`, `K`, `Cu`
  - `properties`:
    - `Li`:
      - `$ref`: #/$defs/contribution
    - `Na`:
      - `$ref`: #/$defs/contribution
    - `K`:
      - `$ref`: #/$defs/contribution
    - `Cu`:
      - `$ref`: #/$defs/contribution
  - `$defs`:
    - `contribution`:
      - `type`: object
      - `required`: `A`, `2B`
      - `properties`:
        - `A`:
          - `type`: object
          - `required`: `electrostatic`, `repulsive`, `van_der_Waals`, `total`
          - `properties`:
            - `electrostatic`:
              - `type`: number
            - `repulsive`:
              - `type`: number
            - `van_der_Waals`:
              - `type`: number
            - `total`:
              - `type`: number
        - `2B`:
          - `type`: object
          - `required`: `electrostatic`, `repulsive`, `van_der_Waals`, `total`
          - `properties`:
            - `electrostatic`:
              - `type`: number
            - `repulsive`:
              - `type`: number
            - `van_der_Waals`:
              - `type`: number
            - `total`:
              - `type`: number

### step_03_table4.json
- path: `/app/outputs/step_03_table4.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Full elastic constants (10^11 dyn/cm²).
- schema:
  - `type`: object
  - `required`: `Li`, `Na`, `K`, `Cu`
  - `properties`:
    - `Li`:
      - `$ref`: #/$defs/elastic
    - `Na`:
      - `$ref`: #/$defs/elastic
    - `K`:
      - `$ref`: #/$defs/elastic
    - `Cu`:
      - `type`: object
      - `required`: `theoretical`, `experimental_room`, `experimental_absolute_zero`
      - `properties`:
        - `theoretical`:
          - `$ref`: #/$defs/elastic
        - `experimental_room`:
          - `$ref`: #/$defs/elastic
        - `experimental_absolute_zero`:
          - `$ref`: #/$defs/elastic
  - `$defs`:
    - `elastic`:
      - `type`: object
      - `required`: `2C`, `A`, `2B`, `c11`, `c12`, `c44`
      - `properties`:
        - `2C`:
          - `type`: number
        - `A`:
          - `type`: number
        - `2B`:
          - `type`: number
        - `c11`:
          - `type`: number
        - `c12`:
          - `type`: number
        - `c44`:
          - `type`: number

### step_04_table6.json
- path: `/app/outputs/step_04_table6.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Debye temperatures (K) for alkali metals.
- schema:
  - `type`: object
  - `required`: `Li`, `Na`, `K`
  - `properties`:
    - `Li`:
      - `type`: object
      - `required`: `without_ion_interaction`, `with_ion_interaction`
      - `properties`:
        - `without_ion_interaction`:
          - `type`: number
        - `with_ion_interaction`:
          - `type`: number
    - `Na`:
      - `type`: object
      - `required`: `without_ion_interaction`, `with_ion_interaction`
      - `properties`:
        - `without_ion_interaction`:
          - `type`: number
        - `with_ion_interaction`:
          - `type`: number
    - `K`:
      - `type`: object
      - `required`: `without_ion_interaction`, `with_ion_interaction`
      - `properties`:
        - `without_ion_interaction`:
          - `type`: number
        - `with_ion_interaction`:
          - `type`: number

Notes: All inputs (potential parameters, lattice constants, compressibilities) are provided in the task instructions. The agent must implement the numerical computations and produce the indicated JSON files with the specified structure. The hidden checker compares the agent’s submitted values against the paper‑reported reference values with appropriate absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_table1.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "fcc",
          "bcc"
        ],
        "properties": {
          "fcc": {
            "type": "object",
            "required": [
              "A_l",
              "2B_l"
            ],
            "properties": {
              "A_l": {
                "type": "number"
              },
              "2B_l": {
                "type": "number"
              }
            }
          },
          "bcc": {
            "type": "object",
            "required": [
              "A_l",
              "2B_l"
            ],
            "properties": {
              "A_l": {
                "type": "number"
              },
              "2B_l": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Electrostatic contributions A^(l) and 2B^(l) in units of e^2/(2δ)."
    },
    {
      "file": "step_02_table5.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Li",
          "Na",
          "K",
          "Cu"
        ],
        "properties": {
          "Li": {
            "$ref": "#/$defs/contribution"
          },
          "Na": {
            "$ref": "#/$defs/contribution"
          },
          "K": {
            "$ref": "#/$defs/contribution"
          },
          "Cu": {
            "$ref": "#/$defs/contribution"
          }
        },
        "$defs": {
          "contribution": {
            "type": "object",
            "required": [
              "A",
              "2B"
            ],
            "properties": {
              "A": {
                "type": "object",
                "required": [
                  "electrostatic",
                  "repulsive",
                  "van_der_Waals",
                  "total"
                ],
                "properties": {
                  "electrostatic": {
                    "type": "number"
                  },
                  "repulsive": {
                    "type": "number"
                  },
                  "van_der_Waals": {
                    "type": "number"
                  },
                  "total": {
                    "type": "number"
                  }
                }
              },
              "2B": {
                "type": "object",
                "required": [
                  "electrostatic",
                  "repulsive",
                  "van_der_Waals",
                  "total"
                ],
                "properties": {
                  "electrostatic": {
                    "type": "number"
                  },
                  "repulsive": {
                    "type": "number"
                  },
                  "van_der_Waals": {
                    "type": "number"
                  },
                  "total": {
                    "type": "number"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Composition of A and 2B (10^11 dyn/cm²)."
    },
    {
      "file": "step_03_table4.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Li",
          "Na",
          "K",
          "Cu"
        ],
        "properties": {
          "Li": {
            "$ref": "#/$defs/elastic"
          },
          "Na": {
            "$ref": "#/$defs/elastic"
          },
          "K": {
            "$ref": "#/$defs/elastic"
          },
          "Cu": {
            "type": "object",
            "required": [
              "theoretical",
              "experimental_room",
              "experimental_absolute_zero"
            ],
            "properties": {
              "theoretical": {
                "$ref": "#/$defs/elastic"
              },
              "experimental_room": {
                "$ref": "#/$defs/elastic"
              },
              "experimental_absolute_zero": {
                "$ref": "#/$defs/elastic"
              }
            }
          }
        },
        "$defs": {
          "elastic": {
            "type": "object",
            "required": [
              "2C",
              "A",
              "2B",
              "c11",
              "c12",
              "c44"
            ],
            "properties": {
              "2C": {
                "type": "number"
              },
              "A": {
                "type": "number"
              },
              "2B": {
                "type": "number"
              },
              "c11": {
                "type": "number"
              },
              "c12": {
                "type": "number"
              },
              "c44": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Full elastic constants (10^11 dyn/cm²)."
    },
    {
      "file": "step_04_table6.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Li",
          "Na",
          "K"
        ],
        "properties": {
          "Li": {
            "type": "object",
            "required": [
              "without_ion_interaction",
              "with_ion_interaction"
            ],
            "properties": {
              "without_ion_interaction": {
                "type": "number"
              },
              "with_ion_interaction": {
                "type": "number"
              }
            }
          },
          "Na": {
            "type": "object",
            "required": [
              "without_ion_interaction",
              "with_ion_interaction"
            ],
            "properties": {
              "without_ion_interaction": {
                "type": "number"
              },
              "with_ion_interaction": {
                "type": "number"
              }
            }
          },
          "K": {
            "type": "object",
            "required": [
              "without_ion_interaction",
              "with_ion_interaction"
            ],
            "properties": {
              "without_ion_interaction": {
                "type": "number"
              },
              "with_ion_interaction": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Debye temperatures (K) for alkali metals."
    }
  ],
  "notes": "All inputs (potential parameters, lattice constants, compressibilities) are provided in the task instructions. The agent must implement the numerical computations and produce the indicated JSON files with the specified structure. The hidden checker compares the agent’s submitted values against the paper‑reported reference values with appropriate absolute tolerances."
}
```

## How you are scored
A hidden verifier reads the four scored JSON files you produce and compares each numerical value against a reference computed from the same formulas. The comparison uses absolute tolerance bands appropriate for each kind of quantity (electrostatic coefficients, elastic constants, temperatures). Each file contributes a score, and the overall reward is the average of those contributions. Simply copying numbers from a table will not succeed because the verifier checks for correct implementation through the entire computation chain; only a correct numerical implementation of the described electrostatic, exchange, elastic‑constant, and Debye‑temperature calculations will place all values within the required tolerances.
