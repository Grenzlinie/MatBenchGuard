# C60 Fullerite Molecular Form Factor Analysis

## Problem background
Solid C60 (fullerite) crystallises in a face-centred cubic lattice at ambient pressure. Under compression the diffraction pattern of fullerite changes in a way that can be explained by a molecular form factor model that treats each C60 molecule as a hollow spherical shell of electronic charge. The form factor can interfere destructively with the crystal structure factor, causing specific reflections to vanish when the lattice spacing and molecular radius satisfy a zero condition. The task is to compute, from the given lattice constants and molecular radius, which of the (200) and (111) reflections, if any, satisfy this zero condition under ambient and compressed conditions.

## Approach
Model each C60 molecule as a hollow spherical shell of charge at radius r_c. The molecular form factor f(E) is obtained by integrating the charge distribution against the diffraction condition; it has zeros when the spherical shell radius satisfies 2 r_c / d = n, where d is the interplanar spacing for the reflection and n is a positive integer. For a cubic lattice, d is related to the lattice constant a and Miller indices (h, k, l) by 1/d = √(h² + k² + l²) / a. Substituting this relation gives a condition for the reflection to be extinct (zero): a / r_c = 2 √(h² + k² + l²) / n. Using the provided ambient and compressed lattice constants and the molecular radius, evaluate this zero condition for the (200) and (111) reflections. For each condition and reflection, compute the actual a/r_c ratio, the required a/r_c ratio for a zero (for an appropriate integer n), and determine whether the reflection is extinct (is_zero).

## Reproduction target
Compute the molecular form factor zero condition for the (200) and (111) reflections of solid C60 under two pressure states: ambient (lattice constant a ≈ 14.2 Å, molecular radius r_c ≈ 3.5 Å) and compressed (a ≈ 12.12 Å, r_c ≈ 3.5 Å). For each state, output the lattice constant, molecular radius, and for each reflection the computed a/r_c ratio, the required ratio for a zero, and a boolean is_zero indicating whether the reflection is extinct according to the spherical-shell model. The results must be written to the JSON file /app/outputs/step_01_zero_analysis.json with the structure specified in the output contract.

## Assets

- Python 3 with numpy and math: numpy

## Workflow steps

### Step 1: Molecular Form Factor Zero Analysis
- Role: scored
- Action: Using the spherical shell model for C60 (hollow charge shell at radius r_c), compute the molecular form factor zero condition for the (200) and (111) reflections under ambient and compressed conditions. Write the results to a JSON file.
- Output file: `/app/outputs/step_01_zero_analysis.json`
- Format: json
- Contract: object with keys 'ambient' and 'compressed', each having 'a' (float), 'r_c' (float), and 'reflections' (object with keys '200' and '111' each having 'a_r_c_ratio' (float), 'required_ratio_for_zero' (float), 'is_zero' (boolean)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_zero_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_zero_analysis.json
- path: `/app/outputs/step_01_zero_analysis.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Analysis of diffraction line extinction for (200) and (111) reflections of C60 fullerite under ambient and compressed conditions based on the spherical-shell molecular form factor model.
- schema:
  - `type`: object
  - `description`: Contains ambient and compressed conditions with computed zero-condition ratios and extinction booleans.
  - `properties`:
    - `ambient`:
      - `type`: object
      - `properties`:
        - `a`:
          - `type`: number
          - `description`: Lattice constant in Angstrom
        - `r_c`:
          - `type`: number
          - `description`: Molecular radius in Angstrom
        - `reflections`:
          - `type`: object
          - `properties`:
            - `200`:
              - `type`: object
              - `properties`:
                - `a_r_c_ratio`:
                  - `type`: number
                - `required_ratio_for_zero`:
                  - `type`: number
                - `is_zero`:
                  - `type`: boolean
              - `required`: `a_r_c_ratio`, `required_ratio_for_zero`, `is_zero`
            - `111`:
              - `type`: object
              - `properties`:
                - `a_r_c_ratio`:
                  - `type`: number
                - `required_ratio_for_zero`:
                  - `type`: number
                - `is_zero`:
                  - `type`: boolean
              - `required`: `a_r_c_ratio`, `required_ratio_for_zero`, `is_zero`
          - `required`: `200`, `111`
      - `required`: `a`, `r_c`, `reflections`
    - `compressed`:
      - `type`: object
      - `properties`:
        - `a`:
          - `type`: number
        - `r_c`:
          - `type`: number
        - `reflections`:
          - `type`: object
          - `properties`:
            - `200`:
              - `type`: object
              - `properties`:
                - `a_r_c_ratio`:
                  - `type`: number
                - `required_ratio_for_zero`:
                  - `type`: number
                - `is_zero`:
                  - `type`: boolean
              - `required`: `a_r_c_ratio`, `required_ratio_for_zero`, `is_zero`
            - `111`:
              - `type`: object
              - `properties`:
                - `a_r_c_ratio`:
                  - `type`: number
                - `required_ratio_for_zero`:
                  - `type`: number
                - `is_zero`:
                  - `type`: boolean
              - `required`: `a_r_c_ratio`, `required_ratio_for_zero`, `is_zero`
          - `required`: `200`, `111`
      - `required`: `a`, `r_c`, `reflections`
  - `required`: `ambient`, `compressed`

Notes: The hidden checker recomputes the expected zero conditions using the same equations and verifies that the reported is_zero values match the expected extinction behavior (200 extinct at ambient, appearing under compression; 111 vice versa) with tolerances on ratios.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_zero_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "description": "Contains ambient and compressed conditions with computed zero-condition ratios and extinction booleans.",
        "properties": {
          "ambient": {
            "type": "object",
            "properties": {
              "a": {
                "type": "number",
                "description": "Lattice constant in Angstrom"
              },
              "r_c": {
                "type": "number",
                "description": "Molecular radius in Angstrom"
              },
              "reflections": {
                "type": "object",
                "properties": {
                  "200": {
                    "type": "object",
                    "properties": {
                      "a_r_c_ratio": {
                        "type": "number"
                      },
                      "required_ratio_for_zero": {
                        "type": "number"
                      },
                      "is_zero": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "a_r_c_ratio",
                      "required_ratio_for_zero",
                      "is_zero"
                    ]
                  },
                  "111": {
                    "type": "object",
                    "properties": {
                      "a_r_c_ratio": {
                        "type": "number"
                      },
                      "required_ratio_for_zero": {
                        "type": "number"
                      },
                      "is_zero": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "a_r_c_ratio",
                      "required_ratio_for_zero",
                      "is_zero"
                    ]
                  }
                },
                "required": [
                  "200",
                  "111"
                ]
              }
            },
            "required": [
              "a",
              "r_c",
              "reflections"
            ]
          },
          "compressed": {
            "type": "object",
            "properties": {
              "a": {
                "type": "number"
              },
              "r_c": {
                "type": "number"
              },
              "reflections": {
                "type": "object",
                "properties": {
                  "200": {
                    "type": "object",
                    "properties": {
                      "a_r_c_ratio": {
                        "type": "number"
                      },
                      "required_ratio_for_zero": {
                        "type": "number"
                      },
                      "is_zero": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "a_r_c_ratio",
                      "required_ratio_for_zero",
                      "is_zero"
                    ]
                  },
                  "111": {
                    "type": "object",
                    "properties": {
                      "a_r_c_ratio": {
                        "type": "number"
                      },
                      "required_ratio_for_zero": {
                        "type": "number"
                      },
                      "is_zero": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "a_r_c_ratio",
                      "required_ratio_for_zero",
                      "is_zero"
                    ]
                  }
                },
                "required": [
                  "200",
                  "111"
                ]
              }
            },
            "required": [
              "a",
              "r_c",
              "reflections"
            ]
          }
        },
        "required": [
          "ambient",
          "compressed"
        ]
      },
      "description": "Analysis of diffraction line extinction for (200) and (111) reflections of C60 fullerite under ambient and compressed conditions based on the spherical-shell molecular form factor model."
    }
  ],
  "notes": "The hidden checker recomputes the expected zero conditions using the same equations and verifies that the reported is_zero values match the expected extinction behavior (200 extinct at ambient, appearing under compression; 111 vice versa) with tolerances on ratios."
}
```

## How you are scored
A hidden verifier independently recomputes the expected zero conditions using the same equations and the given lattice constants and molecular radius. It compares the agent's submitted a/r_c ratios and is_zero booleans against the expected values within a tolerance on the ratios. The verifier checks that the ratios are correctly computed and that the extinction flags follow the physics of the model. The reward is a weighted combination of the correctness of the ratios and the extinction flags across both pressure states. The entire workflow is scored as a single stage; the final reward is written to the verifier log.
