# Phase Diagram of Spin-1 Non-Heisenberg Ferromagnet with Anisotropic Exchange

## Problem background
We study the magnetic phase diagram of a spin-1 ferromagnet with anisotropic bilinear and biquadratic exchange interactions. The Hamiltonian includes three inter-ion anisotropy parameters (Δ, Δ1, Δ2) that control the anisotropy in different tensor channels. In the mean-field approximation, the free energy depends on two variational angles (θ and α) that describe the orientation of the magnetic moment and the spin mixing. Minimizing the free energy yields the stable phase — ferromagnetic (FM∥, FM⊥, QFM⊥, QFM∠) or nematic (N1, N2, N∠) — and the corresponding order parameters. The magnon dispersion relations further determine stability boundaries and the character of phase transitions. The task: compute the phase boundaries and verify the predicted transition conditions by numerical minimization of the free energy and evaluation of magnon gaps.

## Approach
Implement the spin-1 Hamiltonian with anisotropic bilinear and biquadratic exchange, the Stevens operators, and the single-site mean-field Hamiltonian. Derive the free energy density as a function of θ and α and the model parameters (J0, K0, Δ, Δ1, Δ2). For the nematic case (⟨S⟩=0), fix α = -π/4 and minimize over θ. For ferromagnetic cases, minimize over both α and θ. Also implement the magnon dispersion relations and gap formulas for the relevant phases (FM∥, FM⊥, QFM⊥, QFM∠, N1, N2, N∠). Use numerical optimization (SciPy) to find the minimizing angles and compute magnon gaps at k=0. The workflow will scan the parameter space to map phases and check phase assignments and magnon gap vanishing on predicted transition lines.

## Reproduction target
1) **Nematic phase map:** For Δ=0.5, J0/K0=0.8 (positive anisotropy, J0/K0<1), scan Δ1∈[0.5,1.5] and Δ2∈[0,1] in steps of 0.005. For each (Δ1,Δ2), set α=-π/4 and minimize free energy over θ to assign the nematic phase label (N1, N2, or N_angle). Write the map to `nematic_phase_map.csv`. 2) **Ferromagnetic phase check:** For a set of test points covering positive and negative anisotropy regimes and various J0/K0 ratios, perform full free energy minimization over both α and θ to determine the stable phase (FM∥, FM⊥, QFM⊥, QFM∠, N1, N2, N∠) and report the phase label in `ferro_phase_check.json` (separate lists for positive and negative anisotropy cases). 3) **Magnon gap verification:** For points on the predicted second-order transition lines (e.g., Δ1=(1+Δ2)/2 for N1–N_angle, Δ1=1 for N_angle–N2, J0Δ=K0 for QFM⊥–N_angle, etc.), compute the magnon gaps ε1(k=0) and ε2(k=0) using the phase-appropriate dispersion relations. Write the results to `magnon_gap_check.json`.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Model implementation
- Role: process
- Action: Implement the spin-1 Hamiltonian with anisotropic bilinear and biquadratic exchange, the Stevens operators, the single-site mean-field Hamiltonian, the free energy density as a function of the angles θ and α, and the magnon dispersion relations and gap formulas for the relevant phases.
- Evidence: none

### Step 2: Nematic phase map
- Role: scored (load-bearing)
- Action: For the positive anisotropy regime (Δ, Δ₁, Δ₂ > 0) with J₀/K₀ < 1 and fixed Δ = 0.5, J₀/K₀ = 0.8, scan Δ₁ from 0.5 to 1.5 and Δ₂ from 0 to 1 (step 0.005). For each (Δ₁, Δ₂) point, set α = -π/4 (nematic condition ⟨S⟩ = 0) and minimize the free energy over θ to determine the nematic phase (N₁, N₂, or N_angle). Write a CSV file with the assigned phase for every grid point.
- Output file: `/app/outputs/nematic_phase_map.csv`
- Format: csv
- Contract: columns: delta1 (float), delta2 (float), phase (string, one of N1, N2, N_angle)
- Scoring: scored by hidden verifier

### Step 3: Ferromagnetic phase check
- Role: scored (load-bearing)
- Action: For a set of representative parameter points (covering positive and negative anisotropy regimes, various exchange ratios), perform full free energy minimization over both α and θ to determine the stable phase (FM∥, FM⊥, QFM⊥, QFM∠, or the nematic phases). Report the computed phase label in a JSON file with separate lists for positive and negative anisotropy cases.
- Output file: `/app/outputs/ferro_phase_check.json`
- Format: json
- Contract: Top-level keys: positive_tests (array) and negative_tests (array). Each array element is an object with keys: J0 (float), K0 (float), Delta (float), Delta1 (float), Delta2 (float), computed_phase (string, one of: FM_parallel, QFM_perp, QFM_angle, N1, N2, N_angle).
- Scoring: scored by hidden verifier

### Step 4: Magnon gap verification
- Role: scored (load-bearing)
- Action: Select parameter points that lie on the predicted second-order transition lines (e.g., Δ₁ = (1+Δ₂)/2 for N₁–N_angle, Δ₁ = 1 for N_angle–N₂, J₀Δ = K₀ for QFM⊥–N_angle). For each point, evaluate the magnon gaps ε₁(k=0) and ε₂(k=0) using the phase-appropriate dispersion relations. Report the computed gaps in a JSON file.
- Output file: `/app/outputs/magnon_gap_check.json`
- Format: json
- Contract: Top-level key: test_points (array). Each element is an object with keys: phase (string), transition_line (string), J0 (float), K0 (float), Delta (float), Delta1 (float), Delta2 (float), epsilon1_gap (float), epsilon2_gap (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nematic_phase_map.csv`
- `/app/outputs/ferro_phase_check.json`
- `/app/outputs/magnon_gap_check.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nematic_phase_map.csv
- path: `/app/outputs/nematic_phase_map.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file with nematic phase assigned to each grid point in the (Δ₁, Δ₂) plane. The phase label must be one of N1, N2, or N_angle.
- schema:
  - `type`: table
  - `required`:
    - `delta1`: float
    - `delta2`: float
    - `phase`: string
  - `items`: object
  - `required_columns`: `delta1`, `delta2`, `phase`
  - `units`: object

### ferro_phase_check.json
- path: `/app/outputs/ferro_phase_check.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing the agent-determined stable phase for a set of test points in both positive and negative anisotropy regimes. The computed_phase must exactly match one of the allowed strings.
- schema:
  - `type`: object
  - `required`: `positive_tests`, `negative_tests`
  - `properties`:
    - `positive_tests`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `J0`:
            - `type`: number
          - `K0`:
            - `type`: number
          - `Delta`:
            - `type`: number
          - `Delta1`:
            - `type`: number
          - `Delta2`:
            - `type`: number
          - `computed_phase`:
            - `type`: string
            - `enum`: `FM_parallel`, `QFM_perp`, `QFM_angle`, `N1`, `N2`, `N_angle`
        - `required`: `J0`, `K0`, `Delta`, `Delta1`, `Delta2`, `computed_phase`
    - `negative_tests`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `J0`:
            - `type`: number
          - `K0`:
            - `type`: number
          - `Delta`:
            - `type`: number
          - `Delta1`:
            - `type`: number
          - `Delta2`:
            - `type`: number
          - `computed_phase`:
            - `type`: string
            - `enum`: `FM_parallel`, `QFM_perp`, `QFM_angle`, `N1`, `N2`, `N_angle`
        - `required`: `J0`, `K0`, `Delta`, `Delta1`, `Delta2`, `computed_phase`

### magnon_gap_check.json
- path: `/app/outputs/magnon_gap_check.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file with magnon gaps at k=0 on selected transition lines. Each gap value is checked against the expected zero with a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `test_points`: array of objects with keys phase (string), transition_line (string), J0 (float), K0 (float), Delta (float), Delta1 (float), Delta2 (float), epsilon1_gap (float), epsilon2_gap (float)
  - `items`: object
  - `required_columns`: None
  - `units`: object

Notes: The scored artifacts are recomputed by the checker against hidden expected values derived from the paper's analytical conditions. Phase labels must match exactly; magnon gap values must be within a very small tolerance of zero.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nematic_phase_map.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required": {
          "delta1": "float",
          "delta2": "float",
          "phase": "string"
        },
        "items": {},
        "required_columns": [
          "delta1",
          "delta2",
          "phase"
        ],
        "units": {}
      },
      "description": "CSV file with nematic phase assigned to each grid point in the (Δ₁, Δ₂) plane. The phase label must be one of N1, N2, or N_angle."
    },
    {
      "file": "ferro_phase_check.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "positive_tests",
          "negative_tests"
        ],
        "properties": {
          "positive_tests": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "J0": {
                  "type": "number"
                },
                "K0": {
                  "type": "number"
                },
                "Delta": {
                  "type": "number"
                },
                "Delta1": {
                  "type": "number"
                },
                "Delta2": {
                  "type": "number"
                },
                "computed_phase": {
                  "type": "string",
                  "enum": [
                    "FM_parallel",
                    "QFM_perp",
                    "QFM_angle",
                    "N1",
                    "N2",
                    "N_angle"
                  ]
                }
              },
              "required": [
                "J0",
                "K0",
                "Delta",
                "Delta1",
                "Delta2",
                "computed_phase"
              ]
            }
          },
          "negative_tests": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "J0": {
                  "type": "number"
                },
                "K0": {
                  "type": "number"
                },
                "Delta": {
                  "type": "number"
                },
                "Delta1": {
                  "type": "number"
                },
                "Delta2": {
                  "type": "number"
                },
                "computed_phase": {
                  "type": "string",
                  "enum": [
                    "FM_parallel",
                    "QFM_perp",
                    "QFM_angle",
                    "N1",
                    "N2",
                    "N_angle"
                  ]
                }
              },
              "required": [
                "J0",
                "K0",
                "Delta",
                "Delta1",
                "Delta2",
                "computed_phase"
              ]
            }
          }
        }
      },
      "description": "JSON file containing the agent-determined stable phase for a set of test points in both positive and negative anisotropy regimes. The computed_phase must exactly match one of the allowed strings."
    },
    {
      "file": "magnon_gap_check.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "test_points": "array of objects with keys phase (string), transition_line (string), J0 (float), K0 (float), Delta (float), Delta1 (float), Delta2 (float), epsilon1_gap (float), epsilon2_gap (float)"
        },
        "items": {},
        "required_columns": null,
        "units": {}
      },
      "description": "JSON file with magnon gaps at k=0 on selected transition lines. Each gap value is checked against the expected zero with a tolerance."
    }
  ],
  "notes": "The scored artifacts are recomputed by the checker against hidden expected values derived from the paper's analytical conditions. Phase labels must match exactly; magnon gap values must be within a very small tolerance of zero."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact. For the nematic phase map, the verifier recomputes the free energy minima for each grid point and checks whether your assigned phase labels match the expected ones. For the ferromagnetic phase check, the verifier recomputes the stable phase for each test point and compares labels. For the magnon gap check, the verifier recomputes the gaps at k=0 on the transition lines and verifies that they are near zero. Each stage carries a weight; the final reward is a weighted average of the stage scores. Reporting the paper's numbers without genuine computation will not pass.
