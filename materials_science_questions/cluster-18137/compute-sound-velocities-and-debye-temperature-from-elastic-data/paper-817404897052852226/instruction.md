# Compute Sound Velocities and Debye Temperature from Elastic Data

## Problem background
KCaF₃ is a cubic fluoro-perovskite with potential applications in energy conversion and information storage. Understanding its mechanical and thermal properties is crucial for its practical use. Key derived properties include polycrystalline elastic moduli (bulk, shear, Young's), the Pugh ratio and Poisson ratio, sound velocities, the Debye temperature, and the directional variation of the Young's modulus. This task reproduces the computation of these properties by post-processing the single-crystal elastic constants using standard homogenization formulas, without performing the underlying DFT calculations.

## Approach
First, compute the mass density of KCaF₃ from its lattice constant, molar mass, and the number of atoms per formula unit. Then, using the Voigt and Reuss bounds and the Hill average, derive the polycrystalline bulk modulus and shear modulus, and from them the Young's modulus. Compute the Pugh ratio (B/G) for each bound and the Poisson ratio from the Hill moduli. Next, calculate the shear, longitudinal, and average sound velocities for each bound from the moduli and density. From the average velocity, compute the Debye temperature using the standard formula. Finally, compute the directional Young's moduli along the [100], [110], and [111] crystallographic directions using the cubic elastic constants. Implement all steps in Python (e.g., with numpy) and write the results to a structured JSON file.

## Reproduction target
Given the following fixed inputs:
- Single-crystal elastic constants: C₁₁ = 105.49 GPa, C₁₂ = 19.75 GPa, C₄₄ = 17.29 GPa
- Lattice constant a = 4.48 Å
- Molar mass 136.1703 g/mol, 5 atoms per formula unit

Compute and save to /app/outputs/results.json the following quantities, structured as specified in the output contract:
- Density (g/cm³)
- Bulk, shear, and Young’s moduli for Voigt, Reuss, and Hill bounds (GPa)
- Pugh ratio for each bound
- Poisson ratio (Hill)
- Shear, longitudinal, and average wave velocities for each bound (m/s)
- Debye temperature for each bound (K)
- Directional Young's moduli E₁₀₀, E₁₁₀, E₁₁₁ (GPa)

All calculations must be performed from the given inputs using standard formulas; the output file is the sole scored artifact.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute derived elastic and thermal properties
- Role: scored
- Action: From the given single-crystal elastic constants (C11=105.49 GPa, C12=19.75 GPa, C44=17.29 GPa), lattice constant a=4.48 Å, molar mass 136.1703 g/mol, and 5 atoms per formula unit, compute the mass density. Then apply the Voigt-Reuss-Hill averaging scheme to obtain the bulk, shear, and Young's moduli, Pugh ratios, and Poisson ratio. Subsequently, compute the shear, longitudinal, and average wave velocities and the Debye temperature for each bound using standard formulas. Finally, compute the directional Young's moduli along [100], [110], and [111] using the formulas for cubic crystals. Write all quantities to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "density": {"value": <float>, "unit": "g/cm^3"},
  "bulk_modulus": {"Voigt": <float>, "Reuss": <float>, "Hill": <float>, "unit": "GPa"},
  "shear_modulus": {"Voigt": <float>, "Reuss": <float>, "Hill": <float>, "unit": "GPa"},
  "youngs_modulus": {"Voigt": <float>, "Reuss": <float>, "Hill": <float>, "unit": "GPa"},
  "pugh_ratio": {"Voigt": <float>, "Reuss": <float>, "Hill": <float>},
  "poisson_ratio": {"Hill": <float>},
  "wave_velocities": {
    "shear": {"Voigt": <float>, "Reuss": <float>, "Hill": <float>, "unit": "m/s"},
    "longitudinal": {"Voigt": <float>, "Reuss": <float>, "Hill": <float>, "unit": "m/s"},
    "average": {"Voigt": <float>, "Reuss": <float>, "Hill": <float>, "unit": "m/s"}
  },
  "debye_temperature": {"Voigt": <float>, "Reuss": <float>, "Hill": <float>, "unit": "K"},
  "directional_youngs_moduli": {
    "E_100": <float>,
    "E_110": <float>,
    "E_111": <float>,
    "unit": "GPa"
  }
}
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
- target_policy: reference_match
- description: Contains all derived quantities: density, Voigt/Reuss/Hill moduli and ratios, wave velocities, Debye temperature, and directional Young's moduli. The checker compares each numeric field to hidden paper-reported values within tolerances.
- schema:
  - `type`: object
  - `required`: `density`, `bulk_modulus`, `shear_modulus`, `youngs_modulus`, `pugh_ratio`, `poisson_ratio`, `wave_velocities`, `debye_temperature`, `directional_youngs_moduli`
  - `properties`:
    - `density`:
      - `type`: object
      - `required`: `value`, `unit`
      - `properties`:
        - `value`:
          - `type`: number
        - `unit`:
          - `type`: string
          - `const`: g/cm^3
    - `bulk_modulus`:
      - `type`: object
      - `required`: `Voigt`, `Reuss`, `Hill`, `unit`
      - `properties`:
        - `Voigt`:
          - `type`: number
        - `Reuss`:
          - `type`: number
        - `Hill`:
          - `type`: number
        - `unit`:
          - `type`: string
          - `const`: GPa
    - `shear_modulus`:
      - `type`: object
      - `required`: `Voigt`, `Reuss`, `Hill`, `unit`
      - `properties`:
        - `Voigt`:
          - `type`: number
        - `Reuss`:
          - `type`: number
        - `Hill`:
          - `type`: number
        - `unit`:
          - `type`: string
          - `const`: GPa
    - `youngs_modulus`:
      - `type`: object
      - `required`: `Voigt`, `Reuss`, `Hill`, `unit`
      - `properties`:
        - `Voigt`:
          - `type`: number
        - `Reuss`:
          - `type`: number
        - `Hill`:
          - `type`: number
        - `unit`:
          - `type`: string
          - `const`: GPa
    - `pugh_ratio`:
      - `type`: object
      - `required`: `Voigt`, `Reuss`, `Hill`
      - `properties`:
        - `Voigt`:
          - `type`: number
        - `Reuss`:
          - `type`: number
        - `Hill`:
          - `type`: number
    - `poisson_ratio`:
      - `type`: object
      - `required`: `Hill`
      - `properties`:
        - `Hill`:
          - `type`: number
    - `wave_velocities`:
      - `type`: object
      - `required`: `shear`, `longitudinal`, `average`
      - `properties`:
        - `shear`:
          - `type`: object
          - `required`: `Voigt`, `Reuss`, `Hill`, `unit`
          - `properties`:
            - `Voigt`:
              - `type`: number
            - `Reuss`:
              - `type`: number
            - `Hill`:
              - `type`: number
            - `unit`:
              - `type`: string
              - `const`: m/s
        - `longitudinal`:
          - `type`: object
          - `required`: `Voigt`, `Reuss`, `Hill`, `unit`
          - `properties`:
            - `Voigt`:
              - `type`: number
            - `Reuss`:
              - `type`: number
            - `Hill`:
              - `type`: number
            - `unit`:
              - `type`: string
              - `const`: m/s
        - `average`:
          - `type`: object
          - `required`: `Voigt`, `Reuss`, `Hill`, `unit`
          - `properties`:
            - `Voigt`:
              - `type`: number
            - `Reuss`:
              - `type`: number
            - `Hill`:
              - `type`: number
            - `unit`:
              - `type`: string
              - `const`: m/s
    - `debye_temperature`:
      - `type`: object
      - `required`: `Voigt`, `Reuss`, `Hill`, `unit`
      - `properties`:
        - `Voigt`:
          - `type`: number
        - `Reuss`:
          - `type`: number
        - `Hill`:
          - `type`: number
        - `unit`:
          - `type`: string
          - `const`: K
    - `directional_youngs_moduli`:
      - `type`: object
      - `required`: `E_100`, `E_110`, `E_111`, `unit`
      - `properties`:
        - `E_100`:
          - `type`: number
        - `E_110`:
          - `type`: number
        - `E_111`:
          - `type`: number
        - `unit`:
          - `type`: string
          - `const`: GPa

Notes: The agent is given the elastic constants and structural parameters; the computation is deterministic from standard formulas. The checker uses reference_match with tolerances (1% for moduli, 2% for velocities and Debye temperature, 0.01 absolute for Poisson ratio, 2% for density) to score the results.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "density",
          "bulk_modulus",
          "shear_modulus",
          "youngs_modulus",
          "pugh_ratio",
          "poisson_ratio",
          "wave_velocities",
          "debye_temperature",
          "directional_youngs_moduli"
        ],
        "properties": {
          "density": {
            "type": "object",
            "required": [
              "value",
              "unit"
            ],
            "properties": {
              "value": {
                "type": "number"
              },
              "unit": {
                "type": "string",
                "const": "g/cm^3"
              }
            }
          },
          "bulk_modulus": {
            "type": "object",
            "required": [
              "Voigt",
              "Reuss",
              "Hill",
              "unit"
            ],
            "properties": {
              "Voigt": {
                "type": "number"
              },
              "Reuss": {
                "type": "number"
              },
              "Hill": {
                "type": "number"
              },
              "unit": {
                "type": "string",
                "const": "GPa"
              }
            }
          },
          "shear_modulus": {
            "type": "object",
            "required": [
              "Voigt",
              "Reuss",
              "Hill",
              "unit"
            ],
            "properties": {
              "Voigt": {
                "type": "number"
              },
              "Reuss": {
                "type": "number"
              },
              "Hill": {
                "type": "number"
              },
              "unit": {
                "type": "string",
                "const": "GPa"
              }
            }
          },
          "youngs_modulus": {
            "type": "object",
            "required": [
              "Voigt",
              "Reuss",
              "Hill",
              "unit"
            ],
            "properties": {
              "Voigt": {
                "type": "number"
              },
              "Reuss": {
                "type": "number"
              },
              "Hill": {
                "type": "number"
              },
              "unit": {
                "type": "string",
                "const": "GPa"
              }
            }
          },
          "pugh_ratio": {
            "type": "object",
            "required": [
              "Voigt",
              "Reuss",
              "Hill"
            ],
            "properties": {
              "Voigt": {
                "type": "number"
              },
              "Reuss": {
                "type": "number"
              },
              "Hill": {
                "type": "number"
              }
            }
          },
          "poisson_ratio": {
            "type": "object",
            "required": [
              "Hill"
            ],
            "properties": {
              "Hill": {
                "type": "number"
              }
            }
          },
          "wave_velocities": {
            "type": "object",
            "required": [
              "shear",
              "longitudinal",
              "average"
            ],
            "properties": {
              "shear": {
                "type": "object",
                "required": [
                  "Voigt",
                  "Reuss",
                  "Hill",
                  "unit"
                ],
                "properties": {
                  "Voigt": {
                    "type": "number"
                  },
                  "Reuss": {
                    "type": "number"
                  },
                  "Hill": {
                    "type": "number"
                  },
                  "unit": {
                    "type": "string",
                    "const": "m/s"
                  }
                }
              },
              "longitudinal": {
                "type": "object",
                "required": [
                  "Voigt",
                  "Reuss",
                  "Hill",
                  "unit"
                ],
                "properties": {
                  "Voigt": {
                    "type": "number"
                  },
                  "Reuss": {
                    "type": "number"
                  },
                  "Hill": {
                    "type": "number"
                  },
                  "unit": {
                    "type": "string",
                    "const": "m/s"
                  }
                }
              },
              "average": {
                "type": "object",
                "required": [
                  "Voigt",
                  "Reuss",
                  "Hill",
                  "unit"
                ],
                "properties": {
                  "Voigt": {
                    "type": "number"
                  },
                  "Reuss": {
                    "type": "number"
                  },
                  "Hill": {
                    "type": "number"
                  },
                  "unit": {
                    "type": "string",
                    "const": "m/s"
                  }
                }
              }
            }
          },
          "debye_temperature": {
            "type": "object",
            "required": [
              "Voigt",
              "Reuss",
              "Hill",
              "unit"
            ],
            "properties": {
              "Voigt": {
                "type": "number"
              },
              "Reuss": {
                "type": "number"
              },
              "Hill": {
                "type": "number"
              },
              "unit": {
                "type": "string",
                "const": "K"
              }
            }
          },
          "directional_youngs_moduli": {
            "type": "object",
            "required": [
              "E_100",
              "E_110",
              "E_111",
              "unit"
            ],
            "properties": {
              "E_100": {
                "type": "number"
              },
              "E_110": {
                "type": "number"
              },
              "E_111": {
                "type": "number"
              },
              "unit": {
                "type": "string",
                "const": "GPa"
              }
            }
          }
        }
      },
      "description": "Contains all derived quantities: density, Voigt/Reuss/Hill moduli and ratios, wave velocities, Debye temperature, and directional Young's moduli. The checker compares each numeric field to hidden paper-reported values within tolerances."
    }
  ],
  "notes": "The agent is given the elastic constants and structural parameters; the computation is deterministic from standard formulas. The checker uses reference_match with tolerances (1% for moduli, 2% for velocities and Debye temperature, 0.01 absolute for Poisson ratio, 2% for density) to score the results."
}
```

## How you are scored
A hidden verifier reads your submitted results.json. For each numeric field, the verifier compares your value to a reference value computed from the same inputs using a known correct implementation. The comparison uses tolerances appropriate for each quantity (e.g., percentage tolerances for moduli and velocities, absolute tolerance for the Poisson ratio). Fields within tolerance earn partial credit; the final reward is a weighted sum over all fields, scaled to the range [0,1]. Only your computed results.json is evaluated; the verifier does not provide the reference values, and there is no partial credit for derivations or intermediate steps.
