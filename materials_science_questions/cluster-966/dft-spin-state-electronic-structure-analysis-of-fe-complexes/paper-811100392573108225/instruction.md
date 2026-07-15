# Weak-field ligand-field analysis of tetrahedral d⁵ high-spin Fe³⁺: compute lowest quartet energy and Δ

## Problem background
The electronic absorption spectra of AFeS2 (A = K, Rb, Cs) compounds show spin-forbidden d⁵ transitions of tetrahedral high-spin Fe³⁺. Assigning these bands is challenging because the excited electronic states are not simply derived from the free-ion term energies; ligand-field interactions mix the quartet terms. A weak-field secular determinant provides a quantitative model for the lowest sextet-to-quartet transition energy and the crystal-field parameter Δ. This task reproduces that computational analysis by solving the secular determinant for the interacting ⁴P, ⁴F, and ⁴G parent terms under a tetrahedral field.

## Approach
The weak-field secular determinant for the interacting quartet terms is a 3×3 matrix whose diagonal entries are the free-ion term energies relative to the ⁶S ground term, scaled by a nephelauxetic reduction factor β. Off-diagonal entries couple the ⁴P, ⁴F, and ⁴G parent terms via the crystal-field parameter Dq. Given β = 0.5 and a chosen Dq in the range 450–500 cm⁻¹, the lowest eigenvalue of this matrix corresponds to the energy of the ⁴T(⁴G) state (the lowest quartet level). The ligand-field parameter Δ is defined as −10·Dq. The task is to construct the matrix, solve for the lowest eigenvalue, and output the results.

## Reproduction target
Produce a JSON file `/app/outputs/calculated_results.json` containing the chosen β, Dq, the computed lowest eigenvalue (⁴T(⁴G) energy, in cm⁻¹), and the parameter Δ = −10·Dq (in cm⁻¹). Use β = 0.5 and select one value of Dq in the range 450–500 cm⁻¹. The output schema must have keys `"beta"`, `"Dq"`, `"quartet_energy_cm-1"`, and `"delta_cm-1"` with numeric values.

## Assets

- NumPy (and optionally SciPy) for linear algebra: https://pypi.tuna.tsinghua.edu.cn/simple/numpy

## Workflow steps

### Step 1: Solve the weak-field secular determinant
- Role: scored
- Action: Construct the 3×3 secular determinant matrix for interacting quartet parent terms ⁴P, ⁴F, ⁴G of Fe³⁺. The diagonal entries are 35100·β, 52100·β, 32000·β. The off-diagonal entries are (1,3)=(3,1)= -4·√5·Dq and (2,3)=(3,2)= -2·√5·Dq; all other off-diagonals are zero. Use β=0.5 and select a single Dq value from the range 450–500 cm⁻¹. Compute the lowest eigenvalue λ (in cm⁻¹). Also compute Δ = -10·Dq (cm⁻¹). Save the results to a JSON file.
- Output file: `/app/outputs/calculated_results.json`
- Format: json
- Contract: {"beta": float, "Dq": float (cm⁻¹), "quartet_energy_cm-1": float (cm⁻¹), "delta_cm-1": float (cm⁻¹)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_results.json
- path: `/app/outputs/calculated_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The agent's computed lowest quartet energy and Δ; the checker will reconstruct the matrix using the reported β and Dq, recompute the lowest eigenvalue, and compare within tolerance, as well as verify the result falls within the physically acceptable range.
- schema:
  - `type`: object
  - `required`: `beta`, `Dq`, `quartet_energy_cm-1`, `delta_cm-1`
  - `properties`:
    - `beta`:
      - `type`: number
      - `description`: Nephelauxetic reduction factor (dimensionless)
    - `Dq`:
      - `type`: number
      - `unit`: cm⁻¹
      - `description`: Crystal-field parameter
    - `quartet_energy_cm-1`:
      - `type`: number
      - `unit`: cm⁻¹
      - `description`: Lowest eigenvalue (⁴T(⁴G) energy)
    - `delta_cm-1`:
      - `type`: number
      - `unit`: cm⁻¹
      - `description`: Ligand-field parameter Δ = -10·Dq

Notes: The agent may choose any Dq within 450–500 cm⁻¹. Only one parameter set is required. The checker recomputes the eigenvalue from the provided β and Dq.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "beta",
          "Dq",
          "quartet_energy_cm-1",
          "delta_cm-1"
        ],
        "properties": {
          "beta": {
            "type": "number",
            "description": "Nephelauxetic reduction factor (dimensionless)"
          },
          "Dq": {
            "type": "number",
            "unit": "cm⁻¹",
            "description": "Crystal-field parameter"
          },
          "quartet_energy_cm-1": {
            "type": "number",
            "unit": "cm⁻¹",
            "description": "Lowest eigenvalue (⁴T(⁴G) energy)"
          },
          "delta_cm-1": {
            "type": "number",
            "unit": "cm⁻¹",
            "description": "Ligand-field parameter Δ = -10·Dq"
          }
        }
      },
      "description": "The agent's computed lowest quartet energy and Δ; the checker will reconstruct the matrix using the reported β and Dq, recompute the lowest eigenvalue, and compare within tolerance, as well as verify the result falls within the physically acceptable range."
    }
  ],
  "notes": "The agent may choose any Dq within 450–500 cm⁻¹. Only one parameter set is required. The checker recomputes the eigenvalue from the provided β and Dq."
}
```

## How you are scored
A hidden verifier independently checks your submitted artifact. It reads your reported β and Dq, reconstructs the same 3×3 matrix, recomputes the lowest eigenvalue numerically, and verifies that your `quartet_energy_cm-1` matches the recomputed value within a small tolerance. It also checks that your `quartet_energy_cm-1` and `delta_cm-1` lie in physically acceptable ranges (based on the experimental and theoretical context). The final reward is based on both checks; you must actually run the eigenvalue computation to pass.
