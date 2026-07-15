# Phonon symmetry decomposition via group theory

## Problem background
Transition metal dichalcogenides (TMDCs) are layered van der Waals materials where the number of atomic trilayers (N) and the stacking sequence determine the crystal symmetry. The most common polytypes are the trigonal prismatic 2Ha and 2Hc variants and the octahedral 1T polytype. As the number of layers changes, the space group of the few‑layer crystal can change, which in turn affects the symmetry of vibrational modes, their Raman and infrared activity, and the form of the Raman tensors. A complete group‑theoretical classification of phonon symmetries — space groups, irreducible representations of vibrational modes at all high‑symmetry points of the Brillouin zone, Raman/IR/acoustic/silent mode identification, and explicit Raman tensors — is needed for these polytypes as a function of N (odd, even, and bulk). This task is a self‑contained computational exercise in crystallographic group theory.

## Approach
The analysis follows a standard group‑theory workflow. For each polytype (2Ha, 2Hc, 1T) and layer case (bulk, single trilayer, N odd, N even), determine the crystallographic space group from the known stacking sequences and the Wyckoff positions of the atoms, then identify the group of the wave vector (isomorphic point group) at every high‑symmetry Brillouin‑zone point (Γ, K, K', M, Σ, T, T', u). Using the character tables of these wave‑vector groups, compute the lattice‑vibration irreducible representation Γ^vib = Γ^eq ⊗ Γ^vec via site‑symmetry analysis. At the zone center, classify each irreducible representation as Raman‑active, infrared‑active, acoustic, or silent by inspecting the basis functions of the wave‑vector group. Finally, for each Raman‑active representation, write the explicit 3×3 Raman tensor matrix using the standard forms tabulated in group‑theory references (e.g., the Bilbao Crystallographic Server or the International Tables for Crystallography). The entire procedure is deterministic and only requires public crystallographic data and character tables.

## Reproduction target
Produce the following four artifacts for all polytypes and layer cases (bulk, single trilayer 1TL, N odd (N≥3), N even):
1. `space_groups.json` — space group (Hermann‑Mauguin, Schönflies, number) and wave‑vector point group at each high‑symmetry BZ point.
2. `irreps.json` — irreducible representation decomposition of vibrational modes at each BZ high‑symmetry point/line, expressed as formulas in terms of the number of trilayers N.
3. `selection_rules.json` — classification of zone‑center phonon modes into Raman, infrared, acoustic, and silent categories.
4. `raman_tensors.json` — explicit 3×3 Raman tensor matrices for every Raman‑active mode.
These outputs are scored by a hidden verifier that compares the entries against reference symmetry data.

## Assets

- International Tables for Crystallography Volume A
- Bilbao Crystallographic Server: http://www.cryst.ehu.es

## Workflow steps

### Step 1: Space group and GWV assignment
- Role: scored
- Action: For each TMDC polytype (2Ha, 2Hc, 1T) and for the cases: bulk, single trilayer (1TL), odd number of layers (N odd, N≥3), even number of layers (N even), determine the crystallographic space group (Hermann-Mauguin, Schönflies, and International number) and the group of wave vector (isomorphic point group) at every high-symmetry Brillouin zone point: Γ, K, K', M, Σ, T, T', u. Use the known stacking sequences and standard space-group tables. Write the results to `space_groups.json`.
- Output file: `/app/outputs/space_groups.json`
- Format: json
- Contract: Array of objects. Each object has keys: polytype (string), layer_case (string: 'bulk','1TL','N_odd','N_even'), space_group_HM (string), space_group_Schoenflies (string), space_group_number (integer). Additionally, for each high-symmetry BZ point (Gamma, K, Kprime, M, Sigma, T, Tprime, u) a key mapping to the isomorphic point group (string).
- Scoring: scored by hidden verifier

### Step 2: Vibrational mode irreducible representations
- Role: scored (load-bearing)
- Action: Using the space groups and GWV from step 1 and the Wyckoff positions of the atoms, compute the lattice vibration irreducible representation (Γ^vib) at every high-symmetry point and line (Γ, K, K', M, Σ, T, T', u) for each polytype and layer case. Apply site-symmetry analysis: Γ^vib = Γ^eq ⊗ Γ^vec. Output the decomposition as formulas expressed in terms of N (number of trilayers). Write the results to `irreps.json`.
- Output file: `/app/outputs/irreps.json`
- Format: json
- Contract: JSON object with keys like '2Ha_N_odd', '2Ha_N_even', '2Hc_N_odd', etc. Each value is an object mapping a BZ point label (Gamma, K, Kprime, M, Sigma, T, u) to a string representation of the irrep decomposition formula, e.g. '(3N-1)/2(Γ1+ ⊕ Γ3+) ⊕ (3N+1)/2(Γ1+ ⊕ Γ2+)'.
- Scoring: scored by hidden verifier

### Step 3: Raman/IR/acoustic/silent classification
- Role: scored
- Action: For zone‑center (Γ) phonon modes, classify each irreducible representation as Raman-active, infrared-active, acoustic, or silent by examining the basis functions of the GWV from the character tables. Summarize the classification for each polytype and layer case. Write the summary to `selection_rules.json`.
- Output file: `/app/outputs/selection_rules.json`
- Format: json
- Contract: Array of objects. Each object has keys: polytype (string), layer_case (string), Gamma_vib_irrep (string: the total Γ‑point irrep decomposition), Raman_active_irreps (string), IR_active_irreps (string), acoustic_irreps (string), silent_irreps (string).
- Scoring: scored by hidden verifier

### Step 4: Raman tensor generation
- Role: scored
- Action: For each distinct space group and point group occurring at Γ, write the explicit Raman tensor matrices (3×3) for every Raman‑active irreducible representation, using the standard forms from group‑theory references (e.g., Bilbao Crystallographic Server). Write the tensors to `raman_tensors.json`.
- Output file: `/app/outputs/raman_tensors.json`
- Format: json
- Contract: Array of objects. Each object has keys: space_group (string), point_group (string), irrep_label (string), tensor (3×3 array of strings representing the matrix elements).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/space_groups.json`
- `/app/outputs/irreps.json`
- `/app/outputs/selection_rules.json`
- `/app/outputs/raman_tensors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### space_groups.json
- path: `/app/outputs/space_groups.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Space group and GWV assignments for all polytype/layer cases.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `polytype`, `layer_case`, `space_group_HM`, `space_group_Schoenflies`, `space_group_number`
    - `properties`:
      - `polytype`:
        - `type`: string
      - `layer_case`:
        - `type`: string
      - `space_group_HM`:
        - `type`: string
      - `space_group_Schoenflies`:
        - `type`: string
      - `space_group_number`:
        - `type`: integer
      - `GWV`:
        - `type`: object
        - `description`: Keys: Gamma, K, Kprime, M, Sigma, T, Tprime, u; values: point group string

### irreps.json
- path: `/app/outputs/irreps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Irreducible representation decompositions of vibrational modes at all BZ points.
- schema:
  - `type`: object
  - `description`: Top-level keys like '2Ha_N_odd', '2Ha_N_even', '2Hc_N_odd', etc. Each value is an object whose keys are BZ point labels (Gamma, K, Kprime, M, Sigma, T, u) and whose values are string representations of the irrep decomposition formula.

### selection_rules.json
- path: `/app/outputs/selection_rules.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Classification of Γ-point modes into Raman, IR, acoustic, and silent categories for each polytype/layer case.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `polytype`, `layer_case`, `Gamma_vib_irrep`, `Raman_active_irreps`, `IR_active_irreps`, `acoustic_irreps`, `silent_irreps`
    - `properties`:
      - `polytype`:
        - `type`: string
      - `layer_case`:
        - `type`: string
      - `Gamma_vib_irrep`:
        - `type`: string
      - `Raman_active_irreps`:
        - `type`: string
      - `IR_active_irreps`:
        - `type`: string
      - `acoustic_irreps`:
        - `type`: string
      - `silent_irreps`:
        - `type`: string

### raman_tensors.json
- path: `/app/outputs/raman_tensors.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Raman tensors for all Raman‑active modes at Γ.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `space_group`, `point_group`, `irrep_label`, `tensor`
    - `properties`:
      - `space_group`:
        - `type`: string
      - `point_group`:
        - `type`: string
      - `irrep_label`:
        - `type`: string
      - `tensor`:
        - `type`: array
        - `items`:
          - `type`: array
          - `items`:
            - `type`: string
        - `description`: 3×3 matrix of strings representing tensor elements

Notes: All output files must be written under /app/outputs. Irrep label notation may be converted between space group and point group conventions; exact‑match scoring will account for equivalent label formats.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "space_groups.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "polytype",
            "layer_case",
            "space_group_HM",
            "space_group_Schoenflies",
            "space_group_number"
          ],
          "properties": {
            "polytype": {
              "type": "string"
            },
            "layer_case": {
              "type": "string"
            },
            "space_group_HM": {
              "type": "string"
            },
            "space_group_Schoenflies": {
              "type": "string"
            },
            "space_group_number": {
              "type": "integer"
            },
            "GWV": {
              "type": "object",
              "description": "Keys: Gamma, K, Kprime, M, Sigma, T, Tprime, u; values: point group string"
            }
          }
        }
      },
      "description": "Space group and GWV assignments for all polytype/layer cases."
    },
    {
      "file": "irreps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "description": "Top-level keys like '2Ha_N_odd', '2Ha_N_even', '2Hc_N_odd', etc. Each value is an object whose keys are BZ point labels (Gamma, K, Kprime, M, Sigma, T, u) and whose values are string representations of the irrep decomposition formula."
      },
      "description": "Irreducible representation decompositions of vibrational modes at all BZ points."
    },
    {
      "file": "selection_rules.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "polytype",
            "layer_case",
            "Gamma_vib_irrep",
            "Raman_active_irreps",
            "IR_active_irreps",
            "acoustic_irreps",
            "silent_irreps"
          ],
          "properties": {
            "polytype": {
              "type": "string"
            },
            "layer_case": {
              "type": "string"
            },
            "Gamma_vib_irrep": {
              "type": "string"
            },
            "Raman_active_irreps": {
              "type": "string"
            },
            "IR_active_irreps": {
              "type": "string"
            },
            "acoustic_irreps": {
              "type": "string"
            },
            "silent_irreps": {
              "type": "string"
            }
          }
        }
      },
      "description": "Classification of Γ-point modes into Raman, IR, acoustic, and silent categories for each polytype/layer case."
    },
    {
      "file": "raman_tensors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "space_group",
            "point_group",
            "irrep_label",
            "tensor"
          ],
          "properties": {
            "space_group": {
              "type": "string"
            },
            "point_group": {
              "type": "string"
            },
            "irrep_label": {
              "type": "string"
            },
            "tensor": {
              "type": "array",
              "items": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "description": "3×3 matrix of strings representing tensor elements"
            }
          }
        }
      },
      "description": "Raman tensors for all Raman‑active modes at Γ."
    }
  ],
  "notes": "All output files must be written under /app/outputs. Irrep label notation may be converted between space group and point group conventions; exact‑match scoring will account for equivalent label formats."
}
```

## How you are scored
A hidden verifier scores each output file independently. It parses your JSON artifacts and compares every entry — space group names and numbers, irrep decomposition formulas, mode classification strings, and tensor matrix elements — against a hidden reference derived from standard group‑theory tables. Equivalence of irrep labels (e.g., point‑group vs. space‑group notation) is handled. Each file earns partial credit for correctly reproduced entries, and the final reward is a weighted sum over the four output stages. Simply reporting values without correctly executing the group‑theory analysis will not earn full credit, because the verifier checks the internal consistency of the computed formulas across multiple points and polytypes.
