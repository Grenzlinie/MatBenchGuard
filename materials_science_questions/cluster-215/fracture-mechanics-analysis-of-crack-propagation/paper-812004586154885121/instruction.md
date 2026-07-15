# Rotation Transformation of Fracture Compliance Matrix to Zero an Off-Diagonal Element

## Problem background
In a medium with aligned plane-parallel fractures, the elastic response is described by a symmetric 3×3 fracture compliance matrix Z. For the most general (triclinic) fracture system, Z possesses six independent entries because the matrix is symmetric and no additional symmetry constraints exist. This task investigates whether a coordinate rotation about the fracture normal can reduce the number of independent parameters in Z by setting one off-diagonal element to zero. You will compute the required rotation angle and the resulting rotated matrix, which is expected to have a simpler structure. This simplification has implications for the parameterization of fracture-induced anisotropy in the Earth's crust.

## Approach
To simplify the fracture compliance matrix, we apply a coordinate rotation by an angle φ around the axis normal to the fractures (the x3 axis). Under such a rotation, the elements of Z transform according to standard tensor transformation rules for a symmetric 3×3 matrix. The rotated entries are given by rotation formulas that express each new element in terms of the original entries and trigonometric functions of φ (see the workflow step for the explicit expressions). By setting the rotated off-diagonal element Z12′ to zero, one obtains a transcendental equation in φ: cs(Z2 − Z1) + (c² − s²) Z12 = 0, where c = cos φ and s = sin φ. Solving this equation within the interval (−π/2, π/2) yields the angle φ that zeros Z12′. The full rotated matrix Z′ is then obtained by substituting the computed φ and the original Z entries into the rotation formulas.

## Reproduction target
Given a specific numeric fracture compliance matrix Z with elements:
- ZN = 1.0
- Z1 = 2.0
- Z2 = 3.0
- Z12 = 0.5
- Z13 = 0.3
- Z23 = 0.4

You must:
1. Solve the transcendental equation cs(Z2 − Z1) + (c² − s²) Z12 = 0 for the rotation angle φ in radians, with φ chosen from the interval (−π/2, π/2).
2. Using the obtained φ, compute the six elements of the rotated matrix Z′ according to the rotation formulas (see the workflow step).
3. Write a single JSON file `rotated_matrix.json` to `/app/outputs` with the following keys: `rotation_angle` (float, radians), `Z_N_prime`, `Z1_prime`, `Z2_prime`, `Z12_prime` (which should be numerically 0.0), `Z23_prime`, `Z13_prime`.

The resulting rotated matrix must have `Z12_prime` essentially zero, demonstrating the elimination of one off-diagonal element.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute rotation angle and rotated fracture compliance matrix
- Role: scored (load-bearing)
- Action: Given the numeric 6-element fracture compliance matrix Z (ZN, Z1, Z2, Z12, Z13, Z23), solve for the rotation angle φ within the interval (-π/2, π/2) that satisfies the condition Z12' = 0: cs(Z2 - Z1) + (c^2 - s^2) Z12 = 0, where c = cos(φ) and s = sin(φ). Using the obtained φ, compute the full rotated matrix Z' according to the rotation formulas: ZN' = ZN, Z2' = c^2 Z2 + s^2 Z1 - 2cs Z12, Z1' = s^2 Z2 + c^2 Z1 + 2cs Z12, Z12' = cs(Z2 - Z1) + (c^2 - s^2) Z12 (expected to be zero), Z23' = c Z23 - s Z13, Z13' = s Z23 + c Z13. Write the rotation angle in radians and all six rotated elements to the output file.
- Output file: `/app/outputs/rotated_matrix.json`
- Format: json
- Contract: {"rotation_angle": <float (radians)>, "Z_N_prime": <float>, "Z1_prime": <float>, "Z2_prime": <float>, "Z12_prime": <float (0.0)>, "Z23_prime": <float>, "Z13_prime": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rotated_matrix.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rotated_matrix.json
- path: `/app/outputs/rotated_matrix.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The agent-computed rotation angle and the six elements of the rotated fracture compliance matrix. The hidden checker compares every element against a reference computed from the same input Z with an absolute tolerance of 1e-6 and verifies that Z12_prime is within 1e-6 of zero.
- schema:
  - `type`: object
  - `required`:
    - `rotation_angle`: float (radians)
    - `Z_N_prime`: float
    - `Z1_prime`: float
    - `Z2_prime`: float
    - `Z12_prime`: float (should be 0.0)
    - `Z23_prime`: float
    - `Z13_prime`: float
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The input fracture compliance matrix Z is provided as a fixed numeric dictionary in the instruction (do not look up the paper). The task requires no external data downloads.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rotated_matrix.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "rotation_angle": "float (radians)",
          "Z_N_prime": "float",
          "Z1_prime": "float",
          "Z2_prime": "float",
          "Z12_prime": "float (should be 0.0)",
          "Z23_prime": "float",
          "Z13_prime": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "The agent-computed rotation angle and the six elements of the rotated fracture compliance matrix. The hidden checker compares every element against a reference computed from the same input Z with an absolute tolerance of 1e-6 and verifies that Z12_prime is within 1e-6 of zero."
    }
  ],
  "notes": "The input fracture compliance matrix Z is provided as a fixed numeric dictionary in the instruction (do not look up the paper). The task requires no external data downloads."
}
```

## How you are scored
Your output will be evaluated by a hidden verifier. The verifier compares every field in your `rotated_matrix.json` (`rotation_angle`, `Z_N_prime`, `Z1_prime`, `Z2_prime`, `Z12_prime`, `Z23_prime`, `Z13_prime`) against a reference solution that is computed from the same input Z using the correct rotation angle. The comparison is performed with a very tight absolute tolerance. Additionally, the verifier checks that `Z12_prime` is within tolerance of zero. Your score is the fraction of fields that match the reference within tolerance; full credit is awarded only when all fields are correct. Simply reporting a number from the literature or guessing will not pass — you must implement the solver and the rotation formulas yourself.
