# Phonon symmetry classification of Janus and symmetric chromium trihalide monolayers

## Problem background
Monolayer chromium trihalides (X3-Cr2-X3) and their Janus counterparts Y3-Cr2-X3 exhibit phonon modes that are essential for interpreting infrared and Raman optical spectra. Group theory provides a systematic classification of all zone-center (Γ) vibrational modes: each phonon transforms according to an irreducible representation of the point group of the crystal. These representations determine whether a mode is IR‑active, Raman‑active, or silent, and the compatibility relations between the inversion‑symmetric (D3d) and non‑centrosymmetric (C3v) structures clarify the spectral changes induced by breaking inversion symmetry. Reproducing this symmetry decomposition is a prerequisite for identifying features in experimental optical spectra and for studying spin‑phonon coupling and chiral phonon effects.

## Approach
The approach uses standard group‑theoretical analysis without any heavy computation. For each crystal structure (Janus Y3-Cr2-X3 with space group P31m, No. 157, point group C3v; symmetric X3-Cr2-X3 with space group P‑31m, No. 162, point group D3d), the following steps are performed:

1. Determine the **vector representation** (how a polar vector transforms) from the point‑group character table.
2. Build the **equivalent‑atom representation** by counting atoms that remain invariant under each symmetry operation, using the Wyckoff positions given in the paper (Janus: halogen on 3c, Cr on 2b; symmetric: I on 6k, Cr on 2c).
3. Compute the **full vibrational representation** as the direct product of the vector and equivalent‑atom representations.
4. Identify the **acoustic modes** as the irreducible representations that span the vector representation.
5. Subtract the acoustic contribution to obtain the **optic mode decomposition**.
6. Classify each irreducible component of the optic modes as IR‑active, Raman‑active, or silent by consulting the basis functions listed in the character tables (e.g., linear basis functions for IR activity, quadratic basis functions for Raman activity).

The resulting decomposition is written into a single JSON file that records, for both structures, the total vibrational, acoustic, and optic representations, and the sets of IR‑active, Raman‑active, and silent modes. The character tables for C3v and D3d (including basis functions) are provided in the paper and can be implemented as numeric arrays; no external group‑theory library is required.

## Reproduction target
Produce a JSON file `phonon_irrep_decomposition.json` that contains the irreducible representation decomposition of all 24 phonon modes at Γ for both the Janus (C3v) and symmetric (D3d) monolayers. The file must include, for each structure, the strings for total vibrational, acoustic, and optic representations, as well as the lists of IR‑active, Raman‑active, and silent modes, using Mulliken notation with multiplicities and the '⊕' separator (no spaces). The decomposition must satisfy internal consistency: exactly 24 total modes, 3 acoustic modes, and 21 optic modes for each structure, with disjoint IR‑ and Raman‑active sets for the D3d case. The output schema is detailed in the workflow step.

## Assets

- Crystal structure data for Janus Y3-Cr2-X3 (space group P31m, No.157) and symmetric X3-Cr2-X3 (P-31m, No.162)
- Character tables for point groups C3v and D3d
- spglib (optional)
- phonopy (optional)

## Workflow steps

### Step 1: Irreducible representation decomposition of phonon modes at Γ
- Role: scored
- Action: Using the provided crystal structure data (space groups P31m No.157 and P3̄1m No.162) and character tables for C3v and D3d, compute the symmetry representations of lattice vibrations at the Brillouin-zone center for both the Janus Y3-Cr2-X3 (C3v) and symmetric X3-Cr2-X3 (D3d) monolayer. Determine the vector representation, equivalent-atom representation, and the full vibrational representation. Subtract the acoustic representation to obtain the optic modes. Classify each irreducible representation as IR-active, Raman-active, or silent based on basis functions. Write a single JSON file containing the decomposition and activity labels for both structures.
- Output file: `/app/outputs/phonon_irrep_decomposition.json`
- Format: json
- Contract: JSON object with keys 'janus_C3v' and 'symmetric_D3d'. Each value is an object with fields:
- point_group: string (e.g. 'C3v' or 'D3d')
- total_vibrational: string (e.g. '?A1⊕?A2⊕?E' for C3v, '?A1g⊕?A1u⊕?A2g⊕?A2u⊕?Eg⊕?Eu' for D3d)
- acoustic: string (e.g. '?A1⊕?E' for C3v, '?A2u⊕?Eu' for D3d)
- optic: string (e.g. '?A1⊕?A2⊕?E' for C3v, '?A1g⊕?A1u⊕?A2g⊕?A2u⊕?Eg⊕?Eu' for D3d)
- ir_active: string (e.g. '?A1⊕?E' for C3v, '?A2u⊕?Eu' for D3d)
- raman_active: string (e.g. '?A1⊕?E' for C3v, '?A1g⊕?Eg' for D3d)
- silent: string (e.g. '?A2' for C3v, '?A1u⊕?A2g' for D3d)
All decomposition strings use Mulliken notation with multiplicities and '⊕' separator, no spaces. Irreps are listed in alphabetical order within each string (A1, A2, E for C3v; A1g, A1u, A2g, A2u, Eg, Eu for D3d). For D3d, IR-active modes are u-type and Raman-active modes are g-type. The silent modes consist of A1u and A2g representations (multiplicities unspecified here).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_irrep_decomposition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_irrep_decomposition.json
- path: `/app/outputs/phonon_irrep_decomposition.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Decomposition of phonon modes into irreducible representations and activity labels for both monolayer structures.
- schema:
  - `type`: object
  - `required`:
    - `janus_C3v`: object
    - `symmetric_D3d`: object
  - `janus_C3v`:
    - `point_group`: string
    - `total_vibrational`: string
    - `acoustic`: string
    - `optic`: string
    - `ir_active`: string
    - `raman_active`: string
    - `silent`: string
  - `symmetric_D3d`:
    - `point_group`: string
    - `total_vibrational`: string
    - `acoustic`: string
    - `optic`: string
    - `ir_active`: string
    - `raman_active`: string
    - `silent`: string

Notes: The checker compares the reported strings to hidden reference values after normalizing whitespace. Internal consistency checks (total mode count = 24, acoustic = 3, optic = 21; for D3d, IR and Raman active sets are disjoint) are also applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_irrep_decomposition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "janus_C3v": "object",
          "symmetric_D3d": "object"
        },
        "janus_C3v": {
          "point_group": "string",
          "total_vibrational": "string",
          "acoustic": "string",
          "optic": "string",
          "ir_active": "string",
          "raman_active": "string",
          "silent": "string"
        },
        "symmetric_D3d": {
          "point_group": "string",
          "total_vibrational": "string",
          "acoustic": "string",
          "optic": "string",
          "ir_active": "string",
          "raman_active": "string",
          "silent": "string"
        }
      },
      "description": "Decomposition of phonon modes into irreducible representations and activity labels for both monolayer structures."
    }
  ],
  "notes": "The checker compares the reported strings to hidden reference values after normalizing whitespace. Internal consistency checks (total mode count = 24, acoustic = 3, optic = 21; for D3d, IR and Raman active sets are disjoint) are also applied."
}
```

## How you are scored
A hidden verifier independently scores the single output file `phonon_irrep_decomposition.json`. The verifier reads the file, normalizes whitespace, and performs two kinds of checks:

1. **Exact string comparison** – each decomposition string (total_vibrational, acoustic, optic, ir_active, raman_active, silent) is compared to hidden reference values obtained from the paper, using canonical ordering of irreducible representations. This comparison carries the highest weight.
2. **Internal consistency checks** – the verifier confirms that the total mode count is 24, the acoustic count is 3, and the optic count is 21; for the symmetric D3d structure it also ensures that the IR‑active and Raman‑active sets are disjoint.

The final reward is a weighted sum of these checks, distributed across the two structures. Reporting plausible numbers is not sufficient; the agent must compute the decomposition from first principles to match the hidden references. No tolerances are published – the verifier applies appropriate near‑exact matching internally.
