# Effective Modulus of CNF-Reinforced Polymer with Graded Interphase

## Problem background
Carbon nanofiber (CNF) reinforcement enhances the mechanical properties of polymer matrices. Accurate prediction of the effective elastic modulus requires modeling the interphase region between CNF and matrix, which is often functionally graded. The multi-inclusion method provides a micromechanical framework to approximate a continuously varying interphase by subdivision into constant-property shells. This task computes the effective Young's modulus for a CNF-reinforced polymer using that method.

## Approach
The workflow uses two micromechanics homogenization schemes. First, the Mori-Tanaka method for a composite with ellipsoidal inclusions and random fiber orientations is implemented as a baseline for perfect bonding (no distinct interphase). Then the multi-inclusion method is built: the interphase region between the fiber and the matrix is modeled as a nested series of concentric ellipsoids, each with constant properties. The interphase modulus varies from the fiber property at the inner boundary to the matrix property at the outer boundary, following a power-law with exponent 1. The interphase is subdivided into a chosen number of layers (piecewise constant). The effective stiffness is obtained from the nested-inclusion formula, and the result is orientation-averaged for random fiber distribution. The methods rely on the Eshelby tensor, stiffness-tensor rotations, and numerical orientation integration. The effective Young's modulus is extracted from the computed stiffness tensor.

## Reproduction target
Compute the effective Young's modulus (E_c) of a short-fiber-reinforced polymer composite with an ellipsoidal fiber inclusion and a functionally graded interphase. Use the specified base parameters: fiber modulus E_f=240 GPa, matrix modulus E_0=3.15 GPa, fiber aspect ratio 100, fiber volume fraction 0.0382, Poisson's ratios 0.3 for both phases, and random fiber orientation. Compute E_c for (a) the no-interphase case (IPTR=0.0), (b) for an interphase modulus E_i=100 GPa at interphase thickness ratios (IPTR) of 0.1, 0.5, and 1.0, and (c) for E_i=2.0 GPa at the same IPTR values. Write the results to a CSV file effective_moduli.csv with columns: interphase_modulus_GPa, IPTR, E_c_GPa. The output must contain exactly seven rows (one for each condition).

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Mori-Tanaka baseline
- Role: process
- Action: Implement the Mori-Tanaka homogenization method for a composite with ellipsoidal inclusions using the Eshelby tensor and orientation averaging for random fiber orientations. Using the given parameters (E_f=240 GPa, E_0=3.15 GPa, aspect ratio 100, volume fraction 0.0382, Poisson's ratios 0.3 for both phases), compute the effective Young's modulus as a reference baseline for perfect bonding.
- Evidence: none

### Step 2: Multi-inclusion method verification
- Role: process
- Action: Implement the multi-inclusion method with piecewise constant interphase properties using a power-law gradation with a chosen number of subdivisions (e.g., N=10) and gradation exponent n=1. Set the interphase properties equal to the matrix properties (i.e., no distinct interphase) and verify that the computed effective modulus matches the Mori-Tanaka baseline from the previous step within a numerical tolerance. If mismatch, debug the implementation before proceeding.
- Evidence: none

### Step 3: Compute effective moduli with graded interphase
- Role: scored (load-bearing)
- Action: Using the validated multi-inclusion code, compute the effective Young's modulus E_c for two interphase moduli (100 GPa and 2.0 GPa) at interphase thickness ratios (IPTR = interphase thickness / fiber radius) of 0.1, 0.5, and 1.0, as well as the no-interphase case (IPTR=0.0). The interphase property variation follows a power-law from the fiber surface (property equal to fiber) to the matrix (property equal to matrix) with exponent n=1. Use the same base parameters as before. Write the results to effective_moduli.csv with columns: interphase_modulus_GPa, IPTR, E_c_GPa.
- Output file: `/app/outputs/effective_moduli.csv`
- Format: csv
- Contract: CSV with columns: interphase_modulus_GPa (float), IPTR (float), E_c_GPa (float). Seven rows: one for no interphase (0, 0.0, value), three for 100 GPa at 0.1, 0.5, 1.0, three for 2.0 GPa at 0.1, 0.5, 1.0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_moduli.csv
- path: `/app/outputs/effective_moduli.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV with seven rows: interphase_modulus_GPa (0 for no interphase, 100 or 2.0), IPTR (0.0, 0.1, 0.5, 1.0), and the computed effective Young's modulus E_c in GPa.
- schema:
  - `type`: table
  - `required_columns`: `interphase_modulus_GPa`, `IPTR`, `E_c_GPa`
  - `units`:
    - `interphase_modulus_GPa`: GPa
    - `E_c_GPa`: GPa

Notes: The hidden checker will compare the seven E_c values against the paper-reported gold values with an absolute tolerance. Only the values are scored; the CSV structure must match the schema.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "interphase_modulus_GPa",
          "IPTR",
          "E_c_GPa"
        ],
        "units": {
          "interphase_modulus_GPa": "GPa",
          "E_c_GPa": "GPa"
        }
      },
      "description": "CSV with seven rows: interphase_modulus_GPa (0 for no interphase, 100 or 2.0), IPTR (0.0, 0.1, 0.5, 1.0), and the computed effective Young's modulus E_c in GPa."
    }
  ],
  "notes": "The hidden checker will compare the seven E_c values against the paper-reported gold values with an absolute tolerance. Only the values are scored; the CSV structure must match the schema."
}
```

## How you are scored
A hidden verifier will examine effective_moduli.csv for correct format and columns. It will then compare each E_c value against the expected reference value for the corresponding condition. All seven computed values must fall within an allowed tolerance of the reference to earn full credit; the tolerance accounts for legitimate numerical differences between implementations. The final reward is the fraction of values that meet the tolerance criterion. Simply self-reporting a number without performing the correct micromechanical computation will not satisfy the verifier.
