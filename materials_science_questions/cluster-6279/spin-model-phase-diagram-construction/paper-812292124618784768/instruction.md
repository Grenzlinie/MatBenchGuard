# Spin Model Phase Diagram Construction

## Problem background
In the molecular-field model of an orthorhombic antiferromagnet, the thermodynamic phases and transitions between them in the H_x–T plane (field applied along the preferred axis) are governed by a set of self-consistent equations for the sublattice magnetizations. Three types of solutions can occur: the antiferromagnetic 'a' state (unequal sublattice magnetizations along x), the paramagnetic/ferromagnetic 'p' state (equal magnetizations along x), and the 'b' state (magnetizations lying in the x-y plane with opposite y-components on the two sublattices). Transitions between these solutions may be second-order or first-order; a first-order transition can also occur entirely inside the a-phase. The existence and axis intercepts of the transition lines depend on the interaction parameters (A_x, D_x, A_y, D_y). Your task is to implement this model for a given set of parameters and compute the properties of all possible transition lines.

## Approach
The molecular-field treatment starts from an internal energy with antiferromagnetic (A) and intra-sublattice (D) coefficients and assumes spin-1/2, giving effective fields that depend linearly on the sublattice magnetizations. The average magnetizations are given by hyperbolic tangent functions of the effective fields divided by kT. For an external field along the preferred (x) direction, the equations reduce to self-consistent forms for each solution type.

- The p-solution is a single equation for the total magnetization M_x along x.
- The a-solution involves two coupled equations for the sublattice magnetizations along x.
- The b-solution includes x- and y-components, with equal x-components on the two sublattices and opposite y-components, leading to a temperature-dependent condition for the perpendicular component.

To build the phase diagram, you must:
1. Numerically solve the self-consistent equations (e.g., by root-finding) for a grid of H_x and T values, obtaining the magnetizations and Gibbs free energies for all solutions.
2. Identify the second-order a–p transition by detecting where the a-solution merges with the p-solution.
3. Apply the Maxwell construction (equal-area rule) to find first-order a–p and internal a transitions when the magnetization curves have multiple branches.
4. Solve the b-solution and find the second-order b–p transition from the condition that the y-component vanishes.
5. Compare Gibbs free energies of a and b solutions to locate the first-order a–b transition.

All steps must be carried out for the parameters provided; no external datasets are required.

## Reproduction target
For the specific parameter set A_x=1.0, D_x=0.5, A_y=1.0, D_y=0.0, μ_x=1.0, k=1.0, implement the molecular-field equations and numerically compute the following transition lines in the H_x–T plane:
- second-order a–p transition
- first-order a–p transition (if present)
- internal first-order a transition (if present)
- second-order b–p transition
- first-order a–b transition

For each transition type, determine:
- whether it exists (true/false)
- its order ('second' or 'first')
- its H_x-axis intercept (null if not applicable)
- its T-axis intercept (null if not applicable)
- for the internal a transition only, a 'critical_point' object with T_c and H_x_c (null if not applicable)

Compile the results into a JSON file `phase_diagram_lines.json` with a top-level key `transitions` containing an array of objects, one per transition type. The exact schema is given in the Output contract section.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Model Implementation and a/p Solution
- Role: process
- Action: Implement the molecular-field equations for an orthorhombic antiferromagnet with spin-1/2 and external field along the preferred axis. Write a Python script that defines the self-consistent equations for the internal energy, effective fields, and magnetizations. For the given parameter set (A_x=1.0, D_x=0.5, A_y=1.0, D_y=0.0, μ_x=1.0, k=1.0), solve numerically to obtain the magnetization M_x and Gibbs free energy G for the antiferromagnetic (a) and paramagnetic/ferromagnetic (p) solutions as functions of H_x and T. Save the solution status and implementation details as a log.
- Evidence: `/app/outputs/implementation_log.txt`

### Step 2: Second-order a-p transition line
- Role: process
- Action: From the a- and p-solutions, determine the continuous locus where the a-solution merges into the p-solution (second-order a-p transition). Compute the H_x-axis and T-axis intercepts using the analytic formulas derived from the model. Verify the existence condition A_x+D_x>0 for this transition line.
- Evidence: none

### Step 3: First-order a-p and internal a transition
- Role: process
- Action: Examine the a-solution for multi-valued magnetization branches. Apply Maxwell construction (equal-area rule) to identify any first-order a-p transition and an internal first-order transition inside the a-phase. Determine the critical point of the internal transition. Derive the parameter existence conditions for both: D_x>0 for first-order a-p, and 0<D_x<3A_x/5 for the internal transition.
- Evidence: none

### Step 4: b-solution and b-p transition
- Role: process
- Action: Solve the b-solution equations numerically to obtain magnetization and Gibbs free energy. Determine the second-order b-p transition line from the condition that the perpendicular magnetization component vanishes. Compute the H_x-axis and T-axis intercepts and verify the existence conditions A_x+A_y-D_x+D_y>0 and A_y+D_y>0.
- Evidence: none

### Step 5: First-order a-b switch-over transition
- Role: process
- Action: Compare the Gibbs free energies of the a- and b-solutions as functions of H_x and T to locate the first-order a-b threshold line. Calculate its H_x-axis intercept. Verify the condition for absence of the a-b transition (A_y+D_y<D_x).
- Evidence: none

### Step 6: Phase Diagram Lines Summary
- Role: scored (load-bearing)
- Action: Compile all determined transition line properties into a single JSON file. For each transition type (second-order a-p, first-order a-p, internal a first-order, second-order b-p, first-order a-b), record: 'exists' (boolean), 'order' (string, 'second' or 'first' or null if not applicable), 'H_x_intercept' (float, null if not applicable), 'T_intercept' (float, null if not applicable), and for the internal a transition, a 'critical_point' object with keys 'T_c' (float) and 'H_x_c' (float). Save the file as phase_diagram_lines.json.
- Output file: `/app/outputs/phase_diagram_lines.json`
- Format: json
- Contract: An object with a single key 'transitions', whose value is an array of objects. Each object has: 'type' (string, one of 'a-p second-order', 'a-p first-order', 'internal a first-order', 'b-p second-order', 'a-b first-order'), 'exists' (boolean), 'order' (string, 'second' or 'first' or null if not applicable), 'H_x_intercept' (float, null if not applicable), 'T_intercept' (float, null if not applicable), and 'critical_point' (an object with keys 'T_c' (float) and 'H_x_c' (float), present only for 'internal a first-order' when exists is true, else null).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram_lines.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram_lines.json
- path: `/app/outputs/phase_diagram_lines.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structured summary of all transition lines (existence, order, axis intercepts, and internal critical point) for the given parameter set, to be compared against analytic formulas.
- schema:
  - `type`: object
  - `required`: `transitions`
  - `properties`:
    - `transitions`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `type`, `exists`, `order`, `H_x_intercept`, `T_intercept`
        - `properties`:
          - `type`:
            - `type`: string
            - `enum`: `a-p second-order`, `a-p first-order`, `internal a first-order`, `b-p second-order`, `a-b first-order`
          - `exists`:
            - `type`: boolean
          - `order`:
            - `type`: string
            - `enum`: `second`, `first`, `None`
          - `H_x_intercept`:
            - `type`: `number`, `null`
          - `T_intercept`:
            - `type`: `number`, `null`
          - `critical_point`:
            - `oneOf`:
              - `type`: object
              - `required`: `T_c`, `H_x_c`
              - `properties`:
                - `T_c`:
                  - `type`: number
                - `H_x_c`:
                  - `type`: number
              - `type`: null

Notes: The hidden checker compares each boolean/string field for exact match and numeric fields with relative tolerance 1e-6 and absolute 1e-10 against the paper's analytic formulas. The overall score is the fraction of correctly predicted properties.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram_lines.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "transitions"
        ],
        "properties": {
          "transitions": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "type",
                "exists",
                "order",
                "H_x_intercept",
                "T_intercept"
              ],
              "properties": {
                "type": {
                  "type": "string",
                  "enum": [
                    "a-p second-order",
                    "a-p first-order",
                    "internal a first-order",
                    "b-p second-order",
                    "a-b first-order"
                  ]
                },
                "exists": {
                  "type": "boolean"
                },
                "order": {
                  "type": "string",
                  "enum": [
                    "second",
                    "first",
                    null
                  ]
                },
                "H_x_intercept": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "T_intercept": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "critical_point": {
                  "oneOf": [
                    {
                      "type": "object",
                      "required": [
                        "T_c",
                        "H_x_c"
                      ],
                      "properties": {
                        "T_c": {
                          "type": "number"
                        },
                        "H_x_c": {
                          "type": "number"
                        }
                      }
                    },
                    {
                      "type": "null"
                    }
                  ]
                }
              }
            }
          }
        }
      },
      "description": "Structured summary of all transition lines (existence, order, axis intercepts, and internal critical point) for the given parameter set, to be compared against analytic formulas."
    }
  ],
  "notes": "The hidden checker compares each boolean/string field for exact match and numeric fields with relative tolerance 1e-6 and absolute 1e-10 against the paper's analytic formulas. The overall score is the fraction of correctly predicted properties."
}
```

## How you are scored
A hidden verifier will read your `phase_diagram_lines.json` file and compare each field (exists boolean, order string, numeric intercepts, and critical point) against the correct reference values for this parameter set, which are derived from the analytic structure of the molecular-field model. Boolean and string fields must match exactly; numeric fields are compared with appropriate relative and absolute tolerances to allow for numerical inaccuracies. Your final score is the fraction of correctly predicted properties, weighted equally across all transition types unless otherwise specified in the verifier's rubric. Reporting the paper’s numbers alone is not sufficient; you must produce the result by running your own implementation of the model.
