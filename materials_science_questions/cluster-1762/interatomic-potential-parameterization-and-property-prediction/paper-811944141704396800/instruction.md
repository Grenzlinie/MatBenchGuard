# Elastic Properties of Alpha Quartz from Two-Body Central-Force Model

## Problem background
Alpha quartz (SiO₂) is a structurally complex mineral with nine atoms per unit cell and low symmetry. Its elastic properties are geophysically important, yet predicting them from atomic interactions is challenging. This task explores whether a two‑body central‑force interatomic potential—with only radial, non‑directional forces between pairs of atoms—can capture the full set of six independent elastic constants and the bulk modulus of quartz. The approach accounts for Si–O bonds in the SiO₄ tetrahedra as well as several distances of O–O interactions, including those beyond the immediate tetrahedral neighbours (nontetrahedral O–O contacts).

## Approach
The forward‑problem formalism expresses stress as a sum of interatomic forces per unit area, and elastic constants as the derivative of stress with respect to infinitesimal strain. For quartz, the crystal symmetry (P3₁21 or P3₂21) and internal degrees of freedom require, under each applied strain, solving the mechanical equilibrium conditions—net force on every atom must vanish—to obtain the internal displacements of the atoms from their ideal lattice sites. Once these displacements are known, the stress response yields the elastic constants.

The model considers a limited set of two‑body interactions: the Si–O bond at 1.61 Å, and five distinct O–O distances at 2.60, 2.65, 3.33, 3.39, and 3.60 Å. Each interaction is described by two force parameters: the combination (−∂f/∂r + f/r) and the ratio (f/r), both in megabar‑ångströms (Mb·Å). The computational workflow therefore involves: (1) setting up the crystal structure from a public crystallographic database, (2) for each needed strain component, solving a linear system of equilibrium equations to find the atom displacements, and (3) evaluating the elastic constants c₁₁, c₁₂, c₁₃, c₁₄, c₄₄, and the bulk modulus K from the stress–strain relation.

An ablation test is performed by setting the force parameters of all O–O interactions with separation ≥ 3.33 Å to zero and recomputing the bulk modulus. This isolates the contribution of the nontetrahedral oxygen pairs and tests whether the long‑range O–O forces are essential for the bulk stiffness.

## Reproduction target
Compute the elastic constants c₁₁, c₁₂, c₁₃, c₁₄, c₄₄, and the bulk modulus K (in Mb) of α‑quartz from the given two‑body central‑force model, using the crystal structure and the force parameters listed in Step 1. Then, in Step 2, repeat the calculation for the bulk modulus after setting the force parameters for all O–O interactions with separation ≥ 3.33 Å to zero. Write the results to the specified CSV files.

## Assets

- Alpha quartz crystal structure (coordinates and cell parameters)

## Workflow steps

### Step 1: Compute full-model elastic constants
- Role: scored
- Action: Implement the forward-problem formalism (mechanical equilibrium and stress-strain relations) for alpha quartz. Use the known crystal structure (space group P3_121 or P3_221) and the two-body central-force model with the following interaction types and force parameters: Si-O at 1.61 Å ( −∂f/∂r + f/r = 57.14 Mb·Å, f/r = −17.391 Mb·Å); O-O at 2.60 Å (7.143, 4.346); O-O at 2.65 Å (7.143, 4.346); O-O at 3.33 Å (0.3829, 0.0); O-O at 3.39 Å (0.1714, 0.0); O-O at 3.60 Å (0.1143, 0.0). For each independent infinitesimal strain, solve the mechanical equilibrium equations (net force zero on each atom) to find internal displacements, then compute the elastic constants c11, c12, c13, c14, c44, and the bulk modulus K. Output results as CSV.
- Output file: `/app/outputs/step_01_full_model.csv`
- Format: csv
- Contract: Header row: c11,c12,c13,c14,c44,K. One data row with numeric values in Mb.
- Scoring: scored by hidden verifier

### Step 2: Ablation: bulk modulus without nontetrahedral O-O interactions
- Role: scored (load-bearing)
- Action: Modify the force model by setting both force parameters ( −∂f/∂r + f/r and f/r ) to zero for all O-O interactions with separation ≥ 3.33 Å (i.e., the 3.33, 3.39, and 3.60 Å pairs). Repeat the forward computation for alpha quartz under the same procedure, but compute only the bulk modulus K_ablated. Output as CSV.
- Output file: `/app/outputs/step_02_ablation.csv`
- Format: csv
- Contract: Header row: K_ablated. One data row with numeric value in Mb.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_full_model.csv`
- `/app/outputs/step_02_ablation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_full_model.csv
- path: `/app/outputs/step_01_full_model.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Six independent elastic constants and bulk modulus of alpha quartz computed from the full two-body central-force model. The hidden checker compares each value to the paper's reported model reference using appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `c11`, `c12`, `c13`, `c14`, `c44`, `K`
  - `units`:
    - `c11`: Mb
    - `c12`: Mb
    - `c13`: Mb
    - `c14`: Mb
    - `c44`: Mb
    - `K`: Mb

### step_02_ablation.csv
- path: `/app/outputs/step_02_ablation.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Bulk modulus after setting the force parameters for O-O interactions with separation ≥ 3.33 Å to zero. The hidden checker verifies that the value is negligibly small (< 0.05 Mb), confirming that nontetrahedral O:O interactions control the bulk modulus.
- schema:
  - `type`: table
  - `required_columns`: `K_ablated`
  - `units`:
    - `K_ablated`: Mb

Notes: The force parameters are provided in the step actions; the agent does not need to perform inverse fitting. The ablation step is load-bearing: the correct near-zero result can only be obtained if the forward computation is implemented correctly, preventing bypass of the main computation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_full_model.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "c11",
          "c12",
          "c13",
          "c14",
          "c44",
          "K"
        ],
        "units": {
          "c11": "Mb",
          "c12": "Mb",
          "c13": "Mb",
          "c14": "Mb",
          "c44": "Mb",
          "K": "Mb"
        }
      },
      "description": "Six independent elastic constants and bulk modulus of alpha quartz computed from the full two-body central-force model. The hidden checker compares each value to the paper's reported model reference using appropriate tolerances."
    },
    {
      "file": "step_02_ablation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "K_ablated"
        ],
        "units": {
          "K_ablated": "Mb"
        }
      },
      "description": "Bulk modulus after setting the force parameters for O-O interactions with separation ≥ 3.33 Å to zero. The hidden checker verifies that the value is negligibly small (< 0.05 Mb), confirming that nontetrahedral O:O interactions control the bulk modulus."
    }
  ],
  "notes": "The force parameters are provided in the step actions; the agent does not need to perform inverse fitting. The ablation step is load-bearing: the correct near-zero result can only be obtained if the forward computation is implemented correctly, preventing bypass of the main computation."
}
```

## How you are scored
A hidden verifier reads the two output CSV files and scores each step independently.
- **Step 1**: The verifier compares each of the six elastic constants and the bulk modulus to a set of hidden reference values (the experimentally measured elastic constants of quartz) using appropriate tolerances. Better‑than‑reference results are encouraged and never penalised; the score degrades only when the computed values deviate substantially from the references.
- **Step 2**: The verifier checks that the ablated bulk modulus falls below a threshold consistent with the claim that nontetrahedral O–O forces are the primary source of the bulk modulus.
The final reward is a weighted combination of the two step scores. Simply copying a known answer without implementing the forward problem will not succeed, because the verifier’s tolerances demand a physically correct computation.
