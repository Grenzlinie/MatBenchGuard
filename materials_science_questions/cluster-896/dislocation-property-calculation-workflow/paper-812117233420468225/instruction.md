# Dislocation Superposition Method for Stress Intensity Factors of Complex Cracks

## Problem background
Accurate prediction of stress intensity factors in interacting, kinked, and branched cracks is essential for damage tolerance and life extension of aging structures. This task addresses the challenge of computing the stress field and stress intensity factors at crack tips and wedges in a two-dimensional infinite elastic plate containing cracks of complex geometry. The target quantities—Mode I and II stress intensity factors at tips, generalized stress intensity factors at kinks, and the traction-fit error—must be determined for several canonical crack configurations under specified far-field loading and material parameters.

## Approach
The method is based on superposition and dislocation theory. The problem is decomposed at a global level into a trivial problem (the uncracked plate under the applied loading) and an auxiliary problem where prescribed tractions are applied to the crack faces to restore traction-free conditions. Each crack is subdivided into straight segments; for each segment the crack-face displacement profile is represented by a series expansion drawn from three families: wedge series (capturing singular behavior at kinks), polynomial series (handling opening/rotation and mid-span shaping), and tip series (capturing the square-root singularity at crack tips). Coefficient constraints among adjoining segments enforce displacement continuity and eliminate non-physical singularities. Traction boundary conditions are enforced at a set of collocation points distributed along each segment, producing an overdetermined linear system. The system is solved via least squares, yielding the series coefficients. Stress intensity factors and the relative root-mean-square traction error are then extracted from the coefficient values.

## Reproduction target
Implement the dislocation superposition solver from scratch and use it to produce three output files:

1. `v_shape_results.json` — Stress intensity factors and traction errors for V‑shaped crack configurations, including:
   - a 120° V‑crack under unit tension with several approximations of the singular wedge eigenvalue,
   - a 60° V‑crack under combined tension and shear, with variants that use approximate eigenvalues or omit the second singular eigenvalue.

2. `multiply_kinked_results.json` — Stress intensity factors for a crack with two symmetric kinks under both unit tension (varying kink angle and outer‑to‑central segment length ratio) and pure shear (varying outer segment length at fixed kink angle).

3. `branched_results.json` — Stress intensity factors for two interacting branched cracks: a symmetric case with varying separation distance, and a non‑symmetric case with varying branch angle.

All computations use material parameters G=1, ν=0.3, plane strain (Kosolov constant κ=3−4ν). The exact geometric and loading specifications for each case are given in the Workflow steps.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement the dislocation superposition solver
- Role: process
- Action: Develop a Python module that implements the complete dislocation superposition method for 2D crack arrays. The solver must handle V-shaped, multiply kinked, and branched crack topologies, support arbitrary segment lengths and wedge angles, and include: (a) crack geometry definition (segments, lengths, angles); (b) trivial stress field and prescribed crack-face tractions; (c) series basis functions (wedge, polynomial, tip) with coefficient constraints to enforce continuity and eliminate non-physical singularities; (d) collocation point allocation; (e) analytical evaluation of Cauchy singular integrals; (f) assembly of the overdetermined linear system; (g) least-squares solution for weighting coefficients; (h) extraction of stress intensity factors at tips and wedges, and computation of the relative root-mean-square traction error. Material parameters: shear modulus G=1, Poisson\'s ratio ν=0.3, plane strain (Kosolov constant κ=3−4ν).
- Evidence: `/app/outputs/solver.py`

### Step 2: Compute SIFs for V-shaped crack cases
- Role: scored (load-bearing)
- Action: Using the implemented solver, compute stress intensity factors and normalized traction errors for the following V-shaped crack configurations and produce the specified output file. (1) V-shaped crack with unit-length segments (a1=a2=1), wedge angle ω=120° (θ=60°, ρ1 approximated as 8/13), under far-field unit tension (σ_y∞=1, σ_x∞=0, τ_xy∞=0). Report K_I, K_II at both crack tips, generalized Mode-I stress intensity factor at the kink (K_I,kink), and RRMS normal and shear traction errors. (2) Same geometry with ρ1 approximations 1/2, 8/13, and 274/445, recording the same quantities. (3) V-shaped crack with a1=a2=1, ω=60° (θ=120°, ρ1=0.5122214, ρ2=0.7309007), under combined unit tension and shear (σ_y∞=1, σ_x∞=0, τ_xy∞=1). Compute K_I, K_II for both segments, K_I,kink, K_II,kink, and RRMS errors. Also run two variant analyses: (a) using ρ1=ρ2=1/2, and (b) including only ρ1 while omitting ρ2, and report the same quantities.
- Output file: `/app/outputs/v_shape_results.json`
- Format: json
- Contract: JSON object with keys 'table2', 'table4', 'table5'. 'table2' is an array of objects, each with fields: K_I (float), K_II (float), K_I_kink (float), RRMS_normal (float), RRMS_shear (float). 'table4' is an array of objects, each with fields: rho (string, e.g., '1/2', '8/13', '274/445'), K_I (float), K_II (float), K_I_kink (float), RRMS_normal (float), RRMS_shear (float). 'table5' is an array of objects, each with fields: case (string, e.g., '1', '2', '3'), K_I_seg1 (float), K_I_seg2 (float), K_II_seg1 (float), K_II_seg2 (float), K_I_kink (float), K_II_kink (float), RRMS_normal (float), RRMS_shear (float).
- Scoring: scored by hidden verifier

### Step 3: Compute SIFs for multiply kinked crack cases
- Role: scored
- Action: Using the solver, compute stress intensity factors for a crack with two symmetric kinks (antisymmetric). Central segment length a2=2, outer segments lengths a1=a3. For far-field unit tension (σ_y∞=1, σ_x∞=0, τ_xy∞=0), vary a1/a2 = 0.1, 0.2 and kink angle θ = 30°, 45°, 60°; record K_I and K_II at the crack tips. For pure far-field shear (σ_x∞=0, σ_y∞=0, τ_xy∞=1), kink angle θ=60°, a2=2, vary a3 = 0.10, 0.20, 0.60, 1.0; record K_I and K_II at the tips. Write the results to the specified JSON file.
- Output file: `/app/outputs/multiply_kinked_results.json`
- Format: json
- Contract: JSON object with keys 'table7' and 'table8'. 'table7' is an array of objects, each with fields: a1_a2 (float), theta (float, degrees), K_I (float), K_II (float). 'table8' is an array of objects, each with fields: a3 (float), K_I (float), K_II (float).
- Scoring: scored by hidden verifier

### Step 4: Compute SIFs for interacting branched cracks
- Role: scored
- Action: Using the solver, compute stress intensity factors for two interacting branched cracks. (a) Symmetric case: main crack lengths a1=a4=2, branch lengths a2=a3=a5=a6=1, branch angles β1=β2=30°. Vary the separation distance d = 1.05, 1.10, 1.25, 1.50. Compute K_I and K_II at the interacting crack tips. (b) Non‑symmetric case: a1=a4=2, a2=a3=1, a5=a6=0.1, β1=30°, d=0.3; vary β2 = 30°, 60°. Compute K_I and K_II at tip 2 and tip 6. Write results to the specified JSON file.
- Output file: `/app/outputs/branched_results.json`
- Format: json
- Contract: JSON object with keys 'table9' and 'table10'. 'table9' is an array of objects, each with fields: d (float), K_I (float), K_II (float). 'table10' is an array of objects, each with fields: beta2 (float), K_I_tip2 (float), K_II_tip2 (float), K_I_tip6 (float), K_II_tip6 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/v_shape_results.json`
- `/app/outputs/multiply_kinked_results.json`
- `/app/outputs/branched_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### v_shape_results.json
- path: `/app/outputs/v_shape_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Stress intensity factors and traction fit errors for V-shaped crack configurations.
- schema:
  - `type`: object
  - `required`: `table2`, `table4`, `table5`
  - `properties`:
    - `table2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `K_I`, `K_II`, `K_I_kink`, `RRMS_normal`, `RRMS_shear`
        - `properties`:
          - `K_I`:
            - `type`: number
          - `K_II`:
            - `type`: number
          - `K_I_kink`:
            - `type`: number
          - `RRMS_normal`:
            - `type`: number
          - `RRMS_shear`:
            - `type`: number
    - `table4`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `rho`, `K_I`, `K_II`, `K_I_kink`, `RRMS_normal`, `RRMS_shear`
        - `properties`:
          - `rho`:
            - `type`: string
          - `K_I`:
            - `type`: number
          - `K_II`:
            - `type`: number
          - `K_I_kink`:
            - `type`: number
          - `RRMS_normal`:
            - `type`: number
          - `RRMS_shear`:
            - `type`: number
    - `table5`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `case`, `K_I_seg1`, `K_I_seg2`, `K_II_seg1`, `K_II_seg2`, `K_I_kink`, `K_II_kink`, `RRMS_normal`, `RRMS_shear`
        - `properties`:
          - `case`:
            - `type`: string
          - `K_I_seg1`:
            - `type`: number
          - `K_I_seg2`:
            - `type`: number
          - `K_II_seg1`:
            - `type`: number
          - `K_II_seg2`:
            - `type`: number
          - `K_I_kink`:
            - `type`: number
          - `K_II_kink`:
            - `type`: number
          - `RRMS_normal`:
            - `type`: number
          - `RRMS_shear`:
            - `type`: number

### multiply_kinked_results.json
- path: `/app/outputs/multiply_kinked_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Stress intensity factors for multiply kinked crack configurations.
- schema:
  - `type`: object
  - `required`: `table7`, `table8`
  - `properties`:
    - `table7`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `a1_a2`, `theta`, `K_I`, `K_II`
        - `properties`:
          - `a1_a2`:
            - `type`: number
          - `theta`:
            - `type`: number
          - `K_I`:
            - `type`: number
          - `K_II`:
            - `type`: number
    - `table8`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `a3`, `K_I`, `K_II`
        - `properties`:
          - `a3`:
            - `type`: number
          - `K_I`:
            - `type`: number
          - `K_II`:
            - `type`: number

### branched_results.json
- path: `/app/outputs/branched_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Stress intensity factors for interacting branched crack configurations.
- schema:
  - `type`: object
  - `required`: `table9`, `table10`
  - `properties`:
    - `table9`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `d`, `K_I`, `K_II`
        - `properties`:
          - `d`:
            - `type`: number
          - `K_I`:
            - `type`: number
          - `K_II`:
            - `type`: number
    - `table10`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `beta2`, `K_I_tip2`, `K_II_tip2`, `K_I_tip6`, `K_II_tip6`
        - `properties`:
          - `beta2`:
            - `type`: number
          - `K_I_tip2`:
            - `type`: number
          - `K_II_tip2`:
            - `type`: number
          - `K_I_tip6`:
            - `type`: number
          - `K_II_tip6`:
            - `type`: number

Notes: All stress intensity factors are computed for material parameters G=1, ν=0.3 under plane strain. The results are compared to paper-reported reference values with relative tolerance 1% (or absolute tolerance 1e-3 for near-zero values) using a result-level compare.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "v_shape_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "table2",
          "table4",
          "table5"
        ],
        "properties": {
          "table2": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "K_I",
                "K_II",
                "K_I_kink",
                "RRMS_normal",
                "RRMS_shear"
              ],
              "properties": {
                "K_I": {
                  "type": "number"
                },
                "K_II": {
                  "type": "number"
                },
                "K_I_kink": {
                  "type": "number"
                },
                "RRMS_normal": {
                  "type": "number"
                },
                "RRMS_shear": {
                  "type": "number"
                }
              }
            }
          },
          "table4": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "rho",
                "K_I",
                "K_II",
                "K_I_kink",
                "RRMS_normal",
                "RRMS_shear"
              ],
              "properties": {
                "rho": {
                  "type": "string"
                },
                "K_I": {
                  "type": "number"
                },
                "K_II": {
                  "type": "number"
                },
                "K_I_kink": {
                  "type": "number"
                },
                "RRMS_normal": {
                  "type": "number"
                },
                "RRMS_shear": {
                  "type": "number"
                }
              }
            }
          },
          "table5": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "case",
                "K_I_seg1",
                "K_I_seg2",
                "K_II_seg1",
                "K_II_seg2",
                "K_I_kink",
                "K_II_kink",
                "RRMS_normal",
                "RRMS_shear"
              ],
              "properties": {
                "case": {
                  "type": "string"
                },
                "K_I_seg1": {
                  "type": "number"
                },
                "K_I_seg2": {
                  "type": "number"
                },
                "K_II_seg1": {
                  "type": "number"
                },
                "K_II_seg2": {
                  "type": "number"
                },
                "K_I_kink": {
                  "type": "number"
                },
                "K_II_kink": {
                  "type": "number"
                },
                "RRMS_normal": {
                  "type": "number"
                },
                "RRMS_shear": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Stress intensity factors and traction fit errors for V-shaped crack configurations."
    },
    {
      "file": "multiply_kinked_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "table7",
          "table8"
        ],
        "properties": {
          "table7": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "a1_a2",
                "theta",
                "K_I",
                "K_II"
              ],
              "properties": {
                "a1_a2": {
                  "type": "number"
                },
                "theta": {
                  "type": "number"
                },
                "K_I": {
                  "type": "number"
                },
                "K_II": {
                  "type": "number"
                }
              }
            }
          },
          "table8": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "a3",
                "K_I",
                "K_II"
              ],
              "properties": {
                "a3": {
                  "type": "number"
                },
                "K_I": {
                  "type": "number"
                },
                "K_II": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Stress intensity factors for multiply kinked crack configurations."
    },
    {
      "file": "branched_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "table9",
          "table10"
        ],
        "properties": {
          "table9": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "d",
                "K_I",
                "K_II"
              ],
              "properties": {
                "d": {
                  "type": "number"
                },
                "K_I": {
                  "type": "number"
                },
                "K_II": {
                  "type": "number"
                }
              }
            }
          },
          "table10": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "beta2",
                "K_I_tip2",
                "K_II_tip2",
                "K_I_tip6",
                "K_II_tip6"
              ],
              "properties": {
                "beta2": {
                  "type": "number"
                },
                "K_I_tip2": {
                  "type": "number"
                },
                "K_II_tip2": {
                  "type": "number"
                },
                "K_I_tip6": {
                  "type": "number"
                },
                "K_II_tip6": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Stress intensity factors for interacting branched crack configurations."
    }
  ],
  "notes": "All stress intensity factors are computed for material parameters G=1, ν=0.3 under plane strain. The results are compared to paper-reported reference values with relative tolerance 1% (or absolute tolerance 1e-3 for near-zero values) using a result-level compare."
}
```

## How you are scored
Each scored output file is checked by a hidden verifier. The verifier reads the submitted artifact, extracts the required numeric fields, and compares them to independently computed reference values using appropriate tolerances. A separate reward weight is assigned to each scored stage; the final reward is the weighted sum. Simply reporting numbers that happen to match the hidden gold is not sufficient—the verifier expects the results to be produced by correctly implementing and running the described solver. Every scored artifact contributes to the final score; failure to produce a valid artifact or large deviations from the reference will reduce the reward.
