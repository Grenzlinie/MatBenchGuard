# First-principles phonon modes and dielectric tensor of Bi₂Ti₂O₇

## Problem background
The insulating pyrochlore oxide Bi₂Ti₂O₇ exhibits structural distortions away from the ideal cubic pyrochlore structure, leading to unexpectedly large and anisotropic dielectric constants. First‑principles density‑functional theory (DFT) calculations can predict the relaxed ground‑state crystal structure, the vibrational phonon modes, and the phonon contribution to the static dielectric tensor. Computing these properties from the known ideal structure provides insights into the origin of the dielectric response and the symmetry‑lowering distortions in this material.

## Approach
This reproduction uses plane‑wave pseudopotential DFT within the generalized gradient approximation (GGA) to relax the atomic positions and cell of Bi₂Ti₂O₇ starting from the high‑symmetry cubic pyrochlore structure (space group Fd‑3̅m, 88 ions, initial lattice constant 10.376 Å). All symmetry constraints are removed during the first relaxation. The resulting low‑symmetry structure is analyzed with a symmetry‑finding tool to identify the primitive cell and approximate space group, which is then used as input for a second, symmetry‑constrained relaxation. From that relaxed lower‑symmetry cell, a frozen‑phonon or density‑functional perturbation theory (DFPT) calculation is performed at the Γ point to obtain phonon frequencies and eigenvectors. Born effective charge tensors are computed (via DFPT or finite‑difference dipole moments), and together with the phonon modes they yield the phonon contribution to the static dielectric constant tensor. All steps can be carried out with an open‑source DFT code (e.g., Quantum ESPRESSO) and publicly available pseudopotentials.

## Reproduction target
Your task is to produce three artifacts:

1. The fully relaxed crystal structure of Bi₂Ti₂O₇ in its lower‑symmetry phase, with lattice vectors (Å) and fractional coordinates of all unique atoms.
2. A list of all Γ‑point phonon frequencies (cm⁻¹) for that structure, each labeled by its irreducible representation and relative infrared intensity.
3. The three diagonal components of the phonon contribution to the static dielectric constant tensor (dimensionless).

## Assets

- Quantum ESPRESSO (or equivalent open‑source DFT code): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Symmetry analysis tool (e.g., spglib or FINDSYM): https://spglib.github.io/spglib/
- Python libraries (json, numpy, etc.): numpy

## Workflow steps

### Step 1: Structure relaxation and symmetry analysis
- Role: scored
- Action: Starting from the ideal cubic pyrochlore Bi₂Ti₂O₇ structure (Fd‑3̄m, 88 ions, lattice constant 10.376 Å), perform a full unconstrained DFT relaxation (atomic positions and cell) with no symmetry constraints. Analyze the resulting low‑symmetry structure with a symmetry‑finding tool to determine the approximate Pna2₁ primitive cell (44 ions). Perform a further constrained relaxation within the Pna2₁ symmetry. Output the final relaxed Pna2₁ lattice vectors (in Å) and fractional coordinates for all unique atoms.
- Output file: `/app/outputs/step_01_relaxed_structure.json`
- Format: json
- Contract: {"lattice_vectors_angstrom": [[a,0,0],[0,b,0],[0,0,c]], "fractional_coordinates": [{"element":"Bi1","frac":[x,y,z]}, ...], "lattice_constants_angstrom": [a,b,c]}
- Scoring: scored by hidden verifier

### Step 2: Phonon frequency calculation at Γ
- Role: scored (load-bearing)
- Action: Using the relaxed Pna2₁ structure from step 01, perform a frozen‑phonon or DFPT calculation to obtain the Γ‑point phonon frequencies and eigenvectors. Assign irreducible representations (A₁, B₁, B₂, etc.) to each mode. Write a list of all modes with their mode number, frequency (cm⁻¹), irreducible representation, and relative intensity (Zᵖ²/ωᵖ normalized to the most intense mode).
- Output file: `/app/outputs/step_02_phonon_frequencies.json`
- Format: json
- Contract: {"modes": [{"mode_number": int, "frequency_cm1": float, "irreducible_representation": str, "relative_intensity": float}], "unit": "cm-1"}
- Scoring: scored by hidden verifier

### Step 3: Static dielectric constant tensor from phonons
- Role: scored
- Action: Compute the Born effective charge tensors (from DFPT or finite differences of the dipole moment with respect to atomic displacements). Combine them with the phonon eigenvectors and frequencies to calculate the phonon contribution to the static dielectric constant tensor ε(ω=0). Output the three diagonal components ε_aa, ε_bb, ε_cc.
- Output file: `/app/outputs/step_03_dielectric_constants.json`
- Format: json
- Contract: {"epsilon_aa": float, "epsilon_bb": float, "epsilon_cc": float, "unit": "dimensionless (static phonon contribution)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_relaxed_structure.json`
- `/app/outputs/step_02_phonon_frequencies.json`
- `/app/outputs/step_03_dielectric_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_relaxed_structure.json
- path: `/app/outputs/step_01_relaxed_structure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final relaxed Pna2₁ structure with lattice vectors, lattice constants, and fractional coordinates for all unique atoms.
- schema:
  - `type`: object
  - `required`: `lattice_vectors_angstrom`, `fractional_coordinates`, `lattice_constants_angstrom`
  - `properties`:
    - `lattice_vectors_angstrom`:
      - `type`: array
      - `items`:
        - `type`: array
        - `items`:
          - `type`: number
    - `fractional_coordinates`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `element`, `frac`
        - `properties`:
          - `element`:
            - `type`: string
          - `frac`:
            - `type`: array
            - `items`:
              - `type`: number
    - `lattice_constants_angstrom`:
      - `type`: array
      - `items`:
        - `type`: number

### step_02_phonon_frequencies.json
- path: `/app/outputs/step_02_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Γ‑point phonon frequencies (cm⁻¹) with symmetry labels and relative IR intensities.
- schema:
  - `type`: object
  - `required`: `modes`, `unit`
  - `properties`:
    - `modes`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `mode_number`, `frequency_cm1`, `irreducible_representation`, `relative_intensity`
        - `properties`:
          - `mode_number`:
            - `type`: integer
          - `frequency_cm1`:
            - `type`: number
          - `irreducible_representation`:
            - `type`: string
          - `relative_intensity`:
            - `type`: number
    - `unit`:
      - `type`: string

### step_03_dielectric_constants.json
- path: `/app/outputs/step_03_dielectric_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Phonon contribution to the diagonal components of the static dielectric constant tensor (dimensionless).
- schema:
  - `type`: object
  - `required`: `epsilon_aa`, `epsilon_bb`, `epsilon_cc`, `unit`
  - `properties`:
    - `epsilon_aa`:
      - `type`: number
    - `epsilon_bb`:
      - `type`: number
    - `epsilon_cc`:
      - `type`: number
    - `unit`:
      - `type`: string

Notes: The checker compares the agent’s submitted structure, phonon frequencies, and dielectric constants against hidden reference values with appropriate tolerances to account for code/pseudopotential differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_relaxed_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "lattice_vectors_angstrom",
          "fractional_coordinates",
          "lattice_constants_angstrom"
        ],
        "properties": {
          "lattice_vectors_angstrom": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "number"
              }
            }
          },
          "fractional_coordinates": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "element",
                "frac"
              ],
              "properties": {
                "element": {
                  "type": "string"
                },
                "frac": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "lattice_constants_angstrom": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        }
      },
      "description": "Final relaxed Pna2₁ structure with lattice vectors, lattice constants, and fractional coordinates for all unique atoms."
    },
    {
      "file": "step_02_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "modes",
          "unit"
        ],
        "properties": {
          "modes": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "mode_number",
                "frequency_cm1",
                "irreducible_representation",
                "relative_intensity"
              ],
              "properties": {
                "mode_number": {
                  "type": "integer"
                },
                "frequency_cm1": {
                  "type": "number"
                },
                "irreducible_representation": {
                  "type": "string"
                },
                "relative_intensity": {
                  "type": "number"
                }
              }
            }
          },
          "unit": {
            "type": "string"
          }
        }
      },
      "description": "Γ‑point phonon frequencies (cm⁻¹) with symmetry labels and relative IR intensities."
    },
    {
      "file": "step_03_dielectric_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "epsilon_aa",
          "epsilon_bb",
          "epsilon_cc",
          "unit"
        ],
        "properties": {
          "epsilon_aa": {
            "type": "number"
          },
          "epsilon_bb": {
            "type": "number"
          },
          "epsilon_cc": {
            "type": "number"
          },
          "unit": {
            "type": "string"
          }
        }
      },
      "description": "Phonon contribution to the diagonal components of the static dielectric constant tensor (dimensionless)."
    }
  ],
  "notes": "The checker compares the agent’s submitted structure, phonon frequencies, and dielectric constants against hidden reference values with appropriate tolerances to account for code/pseudopotential differences."
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier. For each output file, the verifier compares your computed values to reference targets with pre‑defined tolerances. The structure is checked for symmetry and coordinate deviations; phonon frequencies of infrared‑active modes are compared to reference frequencies; dielectric constant components are compared with a relative tolerance. A combined weighted score is assigned, reflecting the accuracy of all three outputs. You must run the full DFT and phonon workflow — submitting numbers without evidence of computation will not earn credit. The verifier does not re‑run the calculations; it only reads your JSON files.
