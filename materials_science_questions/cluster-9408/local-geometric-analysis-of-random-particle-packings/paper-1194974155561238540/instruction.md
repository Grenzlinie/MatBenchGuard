# Sedimentation Stacking Sequences for Polydisperse Hard Rounded Rectangles

## Problem background
This work investigates the sedimentation equilibrium of a polydisperse two-dimensional fluid of hard rounded rectangles (HRR) in a gravitational field. The particles have a fixed rectangular core and a variable roundness length \(l\), which follows a continuous parent distribution. The interplay between shape polydispersity and gravity can lead to complex vertical partitioning of the sample into stacks of different liquid‑crystalline phases — isotropic (I), tetratic (T), and nematic (N) — with potentially inverted or reentrant sequences. The goal is to compute, for a set of given model parameters, the equilibrium density and orientational order profiles along the vertical direction and to determine the stacking sequence from top to bottom.

## Approach
The theoretical framework is a local density functional theory built on scaled particle theory (SPT). The free energy functional consists of an ideal part, an excess part approximated via SPT, and an external gravitational potential. Minimising the functional with respect to the full density distribution \(\rho(l,z,\phi)\) yields a set of self‑consistent integral equations for a finite number of generalized Fourier moment profiles \(m_i^{(k)}(z)\). These equations are solved numerically on a one‑dimensional grid along the vertical coordinate \(z\) using an iterative method with Anderson acceleration. The equilibrium profiles then give, at each height \(z\), the local packing fraction \(\eta(z)\), the orientational distribution function, and the order parameters \(Q_2(z)\) and \(Q_4(z)\). The column is divided into stacks of distinct bulk phases according to the orientational symmetries: an isotropic stack has \(Q_2 = Q_4 \approx 0\); a tetratic stack has \(Q_2 \approx 0,\; Q_4 > 0\); and a nematic stack has \(Q_2 > 0,\; Q_4 > 0\). The stacking sequence is reported as a string of phase labels (I, T, N) from top to bottom.

## Reproduction target
You must implement the self‑consistent solver, run it for the three test cases specified below, and output the stacking sequence and height‑resolved profiles for each. The three cases share the same particle shape parameters and parent roundness distribution:
- Mean aspect ratio \(\kappa_0 = 1.75\)
- Roundness parameter \(\theta = 0.3\)
- Mean roundness length \(l_0 = 1\) (unit of length)
- Parent roundness distribution: truncated Schulz with exponent \(\nu = 0\), cut‑off \(l_{\text{max}} = 5\), yielding polydispersity \(s = 0.936\); the distribution is normalized so that \(\langle l \rangle = l_0 = 1\).

From these, the core dimensions \(L\) and \(D\) of the rectangles are obtained via \(\kappa_0 = (L+l_0)/(D+l_0)\) and \(\theta = l_0/(D+l_0)\).

The varying parameters are the mean packing fraction \(\bar{\eta}\) and the scaled sample height \(H/\langle\xi\rangle\), where \(\langle\xi\rangle\) is the average gravitational length:
- Case 1: \(\bar{\eta} = 0.913\), \(H/\langle\xi\rangle = 105\)
- Case 2: \(\bar{\eta} = 0.908\), \(H/\langle\xi\rangle = 105\)
- Case 3: \(\bar{\eta} = 0.910\), \(H/\langle\xi\rangle = 30.8\)

The gravitational field strength \(\tau\) is fixed by the relation \(\langle\xi\rangle = 1/(\tau \langle a\rangle_f)\); the solver must respect the given \(H/\langle\xi\rangle\).

For each case, run the solver to convergence, compute the profiles \(\eta(z)\), \(Q_2(z)\), \(Q_4(z)\) on a suitable set of \(z\) points, and determine the stacking sequence. Save the results as case_1_results.json, case_2_results.json, case_3_results.json, respectively, with the exact JSON schema described in the output contract.

## Assets

- NumPy: https://numpy.org
- SciPy: https://scipy.org

## Workflow steps

### Step 1: Compute sedimentation profile and stacking sequence for test case 1
- Role: scored (load-bearing)
- Action: For the test case 1 parameters (mean aspect ratio, polydispersity, roundness, sample height, mean packing fraction) provided in the instruction, implement and run the iterative self-consistent solver to obtain equilibrium moment profiles, then compute orientational order parameters Q2(z), Q4(z) and local packing fraction η(z), and determine the stacking sequence. Output the results to case_1_results.json.
- Output file: `/app/outputs/case_1_results.json`
- Format: json
- Contract: {
  "stacking_sequence": "string",
  "order_parameter_profiles": [
    { "z": "float", "Q2": "float", "Q4": "float", "eta": "float" }
  ]
}
- Scoring: scored by hidden verifier

### Step 2: Compute sedimentation profile and stacking sequence for test case 2
- Role: scored (load-bearing)
- Action: For the test case 2 parameters provided in the instruction, run the solver and compute order parameter profiles Q2(z), Q4(z), η(z) and the stacking sequence. Output to case_2_results.json.
- Output file: `/app/outputs/case_2_results.json`
- Format: json
- Contract: {
  "stacking_sequence": "string",
  "order_parameter_profiles": [
    { "z": "float", "Q2": "float", "Q4": "float", "eta": "float" }
  ]
}
- Scoring: scored by hidden verifier

### Step 3: Compute sedimentation profile and stacking sequence for test case 3
- Role: scored (load-bearing)
- Action: For the test case 3 parameters provided in the instruction, run the solver and compute order parameter profiles Q2(z), Q4(z), η(z) and the stacking sequence. Output to case_3_results.json.
- Output file: `/app/outputs/case_3_results.json`
- Format: json
- Contract: {
  "stacking_sequence": "string",
  "order_parameter_profiles": [
    { "z": "float", "Q2": "float", "Q4": "float", "eta": "float" }
  ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/case_1_results.json`
- `/app/outputs/case_2_results.json`
- `/app/outputs/case_3_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### case_1_results.json
- path: `/app/outputs/case_1_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Sedimentation profile and stacking sequence for case 1.
- schema:
  - `type`: object
  - `required`: `stacking_sequence`, `order_parameter_profiles`
  - `properties`:
    - `stacking_sequence`:
      - `type`: string
    - `order_parameter_profiles`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `z`, `Q2`, `Q4`, `eta`
        - `properties`:
          - `z`:
            - `type`: number
          - `Q2`:
            - `type`: number
          - `Q4`:
            - `type`: number
          - `eta`:
            - `type`: number

### case_2_results.json
- path: `/app/outputs/case_2_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Sedimentation profile and stacking sequence for case 2, plus a partial stacking diagram grid.
- schema:
  - `type`: object
  - `required`: `stacking_sequence`, `order_parameter_profiles`
  - `properties`:
    - `stacking_sequence`:
      - `type`: string
    - `order_parameter_profiles`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `z`, `Q2`, `Q4`, `eta`
        - `properties`:
          - `z`:
            - `type`: number
          - `Q2`:
            - `type`: number
          - `Q4`:
            - `type`: number
          - `eta`:
            - `type`: number
    - `grid`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `eta`, `H`, `stacking_sequence`
        - `properties`:
          - `eta`:
            - `type`: number
          - `H`:
            - `type`: number
          - `stacking_sequence`:
            - `type`: string

### case_3_results.json
- path: `/app/outputs/case_3_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Sedimentation profile and stacking sequence for case 3.
- schema:
  - `type`: object
  - `required`: `stacking_sequence`, `order_parameter_profiles`
  - `properties`:
    - `stacking_sequence`:
      - `type`: string
    - `order_parameter_profiles`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `z`, `Q2`, `Q4`, `eta`
        - `properties`:
          - `z`:
            - `type`: number
          - `Q2`:
            - `type`: number
          - `Q4`:
            - `type`: number
          - `eta`:
            - `type`: number

Notes: Removed standalone stacking_diagram_cut.json to avoid a missing solve block. The required partial stacking diagram is now an optional 'grid' field inside case_2_results.json. Later edits will update the instruction and checker to use this field.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "case_1_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "stacking_sequence",
          "order_parameter_profiles"
        ],
        "properties": {
          "stacking_sequence": {
            "type": "string"
          },
          "order_parameter_profiles": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "z",
                "Q2",
                "Q4",
                "eta"
              ],
              "properties": {
                "z": {
                  "type": "number"
                },
                "Q2": {
                  "type": "number"
                },
                "Q4": {
                  "type": "number"
                },
                "eta": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Sedimentation profile and stacking sequence for case 1."
    },
    {
      "file": "case_2_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "stacking_sequence",
          "order_parameter_profiles"
        ],
        "properties": {
          "stacking_sequence": {
            "type": "string"
          },
          "order_parameter_profiles": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "z",
                "Q2",
                "Q4",
                "eta"
              ],
              "properties": {
                "z": {
                  "type": "number"
                },
                "Q2": {
                  "type": "number"
                },
                "Q4": {
                  "type": "number"
                },
                "eta": {
                  "type": "number"
                }
              }
            }
          },
          "grid": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "eta",
                "H",
                "stacking_sequence"
              ],
              "properties": {
                "eta": {
                  "type": "number"
                },
                "H": {
                  "type": "number"
                },
                "stacking_sequence": {
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "description": "Sedimentation profile and stacking sequence for case 2, plus a partial stacking diagram grid."
    },
    {
      "file": "case_3_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "stacking_sequence",
          "order_parameter_profiles"
        ],
        "properties": {
          "stacking_sequence": {
            "type": "string"
          },
          "order_parameter_profiles": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "z",
                "Q2",
                "Q4",
                "eta"
              ],
              "properties": {
                "z": {
                  "type": "number"
                },
                "Q2": {
                  "type": "number"
                },
                "Q4": {
                  "type": "number"
                },
                "eta": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Sedimentation profile and stacking sequence for case 3."
    }
  ],
  "notes": "Removed standalone stacking_diagram_cut.json to avoid a missing solve block. The required partial stacking diagram is now an optional 'grid' field inside case_2_results.json. Later edits will update the instruction and checker to use this field."
}
```

## How you are scored
The hidden verifier reads the three output JSON files. For each test case, the reported `stacking_sequence` string is compared to the correct sequence for those parameters. The correctness of the sequence is the primary scoring criterion; the order‑parameter profiles may be used for a consistency check (e.g., verifying that \(Q_2 \approx 0\) in a stack labeled as I or T). The final reward is the fraction of test cases with a correct stacking sequence (0, 1/3, 2/3, or 1).
