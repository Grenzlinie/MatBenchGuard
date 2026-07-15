# Zone-Center Optical Phonon Irreducible Representation Decomposition for FeF₃

## Problem background
FeF₃ is a rhombohedral crystal belonging to space group D₃ₕ⁶ (No. 167) with a bimolecular unit cell. At the Brillouin‑zone centre, the vibrational modes can be classified according to the irreducible representations of the point group D₃ₕ. This classification determines which modes are Raman‑active and infrared‑active, and is essential for interpreting spectroscopic measurements. In this task you will compute the decomposition of the zone‑centre optical phonon modes from the publicly available crystal structure.

## Approach
Perform a group‑theoretical analysis solely from the crystal structure. Start from the known space group (D₃ₕ⁶, No. 167), lattice vectors, and atomic positions of FeF₃. Determine the symmetry operations at the Γ point and construct the mechanical representation from the occupied Wyckoff positions. Reduce this representation into irreducible representations of D₃ₕ, then subtract the acoustic modes (determined from the translation representation) to obtain the optical phonon counts. Classify the optical irreps into Raman‑active and infrared‑active by applying the selection rules of point group D₃ₕ. Implement this using a symmetry analysis library such as spglib; the final output is a JSON file with the irreducible representation counts.

## Reproduction target
Using the crystal structure of FeF₃ (space group D₃ₕ⁶, No. 167, atomic positions from Acta Crystallographica 10 (1957) 63, DOI given in Assets), compute the irreducible representation decomposition of the zone‑centre optical phonon modes. Exclude the acoustic modes (obtained from the translation representation). Report the integer counts for each irreducible representation in a JSON object with the key `phonon_irreps`. Additionally, report the decomposition of Raman‑active and infrared‑active modes in the `raman_active` and `infrared_active` objects, following the output contract. Write the result to `/app/outputs/irrep_decomposition.json` following the exact output contract specified in the workflow step.

## Assets

- FeF₃ crystal structure: https://doi.org/10.1107/S0365110X57000053
- spglib: https://spglib.github.io/spglib/

## Workflow steps

### Step 1: Group‑theoretical decomposition of zone‑center optical phonons
- Role: scored (load-bearing)
- Action: Using the crystal structure of FeF₃ (space group D₃ₕ⁶, No. 167, with atomic positions from Acta Crystallographica 10 (1957) 63), determine the irreducible representations of the vibrational modes at the Γ point. Exclude the acoustic modes (determined from the translation representation) and report only the optical modes. Classify the optical irreps into Raman‑active and infrared‑active by applying the selection rules of point group D₃ₕ. Write the result to irrep_decomposition.json.
- Output file: `/app/outputs/irrep_decomposition.json`
- Format: json
- Contract: {"type": "object", "required": ["phonon_irreps", "raman_active", "infrared_active"], "properties": {"phonon_irreps": {"type": "object", "required": ["Γ1+", "Γ2+", "Γ3+", "Γ1-", "Γ2-", "Γ3-"], "additionalProperties": false, "properties": {"Γ1+": {"type": "integer"}, "Γ2+": {"type": "integer"}, "Γ3+": {"type": "integer"}, "Γ1-": {"type": "integer"}, "Γ2-": {"type": "integer"}, "Γ3-": {"type": "integer"}}}, "raman_active": {"type": "object", "required": ["Γ1+", "Γ3+"], "additionalProperties": false, "properties": {"Γ1+": {"type": "integer"}, "Γ3+": {"type": "integer"}}}, "infrared_active": {"type": "object", "required": ["Γ2+", "Γ3-"], "additionalProperties": false, "properties": {"Γ2+": {"type": "integer"}, "Γ3-": {"type": "integer"}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/irrep_decomposition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### irrep_decomposition.json
- path: `/app/outputs/irrep_decomposition.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Phonon irreducible representation counts for optical zone‑center modes, with Raman and infrared activity classification.
- schema:
  - `type`: object
  - `required`: `phonon_irreps`, `raman_active`, `infrared_active`
  - `properties`:
    - `phonon_irreps`:
      - `type`: object
      - `required`: `Γ1+`, `Γ2+`, `Γ3+`, `Γ1-`, `Γ2-`, `Γ3-`
      - `additionalProperties`: False
      - `properties`:
        - `Γ1+`:
          - `type`: integer
        - `Γ2+`:
          - `type`: integer
        - `Γ3+`:
          - `type`: integer
        - `Γ1-`:
          - `type`: integer
        - `Γ2-`:
          - `type`: integer
        - `Γ3-`:
          - `type`: integer
    - `raman_active`:
      - `type`: object
      - `required`: `Γ1+`, `Γ3+`
      - `additionalProperties`: False
      - `properties`:
        - `Γ1+`:
          - `type`: integer
        - `Γ3+`:
          - `type`: integer
    - `infrared_active`:
      - `type`: object
      - `required`: `Γ2+`, `Γ3-`
      - `additionalProperties`: False
      - `properties`:
        - `Γ2+`:
          - `type`: integer
        - `Γ3-`:
          - `type`: integer

Notes: The hidden checker compares the integer counts per irrep exactly against the paper‑reported decomposition (1 Γ₁⁺, 2 Γ₂⁺, 3 Γ₃⁺, 2 Γ₁⁻, 2 Γ₂⁻, 4 Γ₃⁻) and verifies that raman_active sums to 4 (1 Γ₁⁺ + 3 Γ₃⁺). Because these are discrete symmetry‑determined values, an exact match policy is appropriate.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "irrep_decomposition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "phonon_irreps",
          "raman_active",
          "infrared_active"
        ],
        "properties": {
          "phonon_irreps": {
            "type": "object",
            "required": [
              "Γ1+",
              "Γ2+",
              "Γ3+",
              "Γ1-",
              "Γ2-",
              "Γ3-"
            ],
            "additionalProperties": false,
            "properties": {
              "Γ1+": {
                "type": "integer"
              },
              "Γ2+": {
                "type": "integer"
              },
              "Γ3+": {
                "type": "integer"
              },
              "Γ1-": {
                "type": "integer"
              },
              "Γ2-": {
                "type": "integer"
              },
              "Γ3-": {
                "type": "integer"
              }
            }
          },
          "raman_active": {
            "type": "object",
            "required": [
              "Γ1+",
              "Γ3+"
            ],
            "additionalProperties": false,
            "properties": {
              "Γ1+": {
                "type": "integer"
              },
              "Γ3+": {
                "type": "integer"
              }
            }
          },
          "infrared_active": {
            "type": "object",
            "required": [
              "Γ2+",
              "Γ3-"
            ],
            "additionalProperties": false,
            "properties": {
              "Γ2+": {
                "type": "integer"
              },
              "Γ3-": {
                "type": "integer"
              }
            }
          }
        }
      },
      "description": "Phonon irreducible representation counts for optical zone‑center modes, with Raman and infrared activity classification."
    }
  ],
  "notes": "The hidden checker compares the integer counts per irrep exactly against the paper‑reported decomposition (1 Γ₁⁺, 2 Γ₂⁺, 3 Γ₃⁺, 2 Γ₁⁻, 2 Γ₂⁻, 4 Γ₃⁻) and verifies that raman_active sums to 4 (1 Γ₁⁺ + 3 Γ₃⁺). Because these are discrete symmetry‑determined values, an exact match policy is appropriate."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/irrep_decomposition.json`. It will extract every integer count declared in the required fields (`phonon_irreps`, `raman_active`, `infrared_active`) and compare each against the correct value determined by a rigorous group‑theoretical calculation with the same crystal structure. Because these values are discrete symmetry‑dependent integers, the comparison is exact with no tolerance. Your reward is the fraction of integer fields that match correctly. For example, if the total number of integer fields is N and M of them are exact, your score will be M/N. The verifier does not inspect any other file.
