# Phonon symmetry decomposition for 2D space groups

## Problem background
In crystallography and solid-state physics, lattice vibrations (phonons) are classified by symmetry using group theory. The irreducible representations (irreps) of the space group of the crystal label the normal modes and predict degeneracies. For two-dimensional (2D) crystals, there are 17 possible space groups (wallpaper groups). For each space group, the possible atomic arrangements are captured by Wyckoff positions, each corresponding to a simple crystal. The vibrational modes of such a crystal can be decomposed into contributions from each irrep of the group. Determining the multiplicity — the number of modes transforming as each irrep — for every Wyckoff position of all 17 2D space groups provides a complete reference for interpreting 2D phonon spectra. This task asks you to compute that full classification: for each of the 17 2D space groups and each Wyckoff position, determine the integer multiplicity of every irreducible representation at the high-symmetry points of the Brillouin zone.

## Approach
The standard group-theoretical procedure decomposes the vibrational representation, which is the direct product of two sub‑representations: (i) the permutation representation D_PERM, which counts how many atoms remain fixed under each symmetry operation of the space group G, and (ii) the polar vector representation D_V, a 2‑dimensional representation whose characters are obtained from the rotation/reflection matrices of the symmetry operations. The direct product D = D_PERM × D_V is then reduced into irreducible components using character orthogonality. The required input data are the irreducible representations of the 17 2D space groups at all high‑symmetry k‑points, which are publicly available from crystallographic servers (e.g., Bilbao Crystallographic Server) or can be derived from standard reference tables. Also needed are the Wyckoff positions with their generating coordinates for each space group. For each Wyckoff position of a given space group, you compute D_PERM, form D, and project onto the irreps to obtain integer multiplicities. The output is a structured table of these multiplicities for all 17 space groups.

## Reproduction target
Produce a JSON file, `phonon_decomposition.json`, that contains, for each of the 17 two-dimensional space groups (keys: 'p1', 'p2', 'pm', 'pg', 'cm', 'pmm', 'pmg', 'pgg', 'cmm', 'p4', 'p4m', 'p4g', 'p3', 'p3m1', 'p31m', 'p6', 'p6m'), an array of objects for every Wyckoff position. Each object must have fields: `wyckoff` (the Wyckoff letter, e.g., 'a'), `position` (the generating coordinate string, e.g., '(0,0)'), and `irreps` — an object mapping each irreducible representation symbol (using the notation from standard 2D space group tables, e.g., 'Γ1', 'Σ1', 'M5') to the integer multiplicity of vibrational modes of that symmetry. The list of Wyckoff positions to include is the full set given for each space group in the standard published classification (including all positions labeled a, b, c, ...). All positions must be present. The IR symbols must be unambiguous and consistent with standard crystallographic conventions.

## Assets

- Bilbao Crystallographic Server (k-space representations and Wyckoff positions): https://www.cryst.ehu.es/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare irreducible representation data
- Role: process
- Action: Obtain or compute the irreducible representations of the 17 two-dimensional space groups at the high-symmetry k-points listed in standard crystallographic references (e.g., Bilbao Crystallographic Server, International Tables for Crystallography Vol. A). This includes character tables for all relevant point groups and matrices for non-symmorphic space groups. Data can be fetched from the Bilbao Crystallographic Server or constructed from standard reference tables. For each space group, also retrieve the Wyckoff positions (site-symmetry and generating coordinates). Save the structured irrep data as irrep_data.json for use in the decomposition step.
- Evidence: `/app/outputs/irrep_data.json`

### Step 2: Compute phonon decomposition table
- Role: scored (load-bearing)
- Action: For each of the 17 two-dimensional space groups, and for each simple crystal (Wyckoff position), perform the group-theoretical decomposition: 1) Determine the permutation representation D_G^PERM (character = number of atoms fixed under each symmetry element of G). 2) Determine the polar vector representation D_G^V (2D representation derived from the rotation/reflection matrices). 3) Compute the direct product representation D = D_G^PERM × D_G^V. 4) Use character orthogonality to decompose D into irreducible components, yielding the multiplicity (integer) of each irreducible representation. 5) Output all multiplicities for all space groups and Wyckoff positions into phonon_decomposition.json, using standard irreducible representation labels consistent with crystallographic conventions (e.g., 'Γ1', 'Σ1', 'M5').
- Output file: `/app/outputs/phonon_decomposition.json`
- Format: json
- Contract: Top-level object with keys: 'p1','p2','pm','pg','cm','pmm','pmg','pgg','cmm','p4','p4m','p4g','p3','p3m1','p31m','p6','p6m'. Each value is an array of objects with fields: 'wyckoff' (string, e.g., 'a'), 'position' (string, e.g., '(0,0)'), 'irreps' (object mapping string IR symbol to integer multiplicity). All Wyckoff positions listed in standard crystallographic tables must be present; IR symbols must follow standard crystallographic notation (e.g., 'Γ1', 'Σ1', 'M5').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_decomposition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_decomposition.json
- path: `/app/outputs/phonon_decomposition.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Complete mode-count table for all 17 two-dimensional space groups and their Wyckoff positions, providing the number of lattice vibrational modes labeled by each irreducible representation.
- schema:
  - `type`: object
  - `required`:
    - `p1`: array of Wyckoff objects
    - `p2`: array
    - `pm`: array
    - `pg`: array
    - `cm`: array
    - `pmm`: array
    - `pmg`: array
    - `pgg`: array
    - `cmm`: array
    - `p4`: array
    - `p4m`: array
    - `p4g`: array
    - `p3`: array
    - `p3m1`: array
    - `p31m`: array
    - `p6`: array
    - `p6m`: array
  - `items`:
    - `wyckoff`: string
    - `position`: string
    - `irreps`:
      - `type`: object
      - `additional_properties`: integer

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_decomposition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "p1": "array of Wyckoff objects",
          "p2": "array",
          "pm": "array",
          "pg": "array",
          "cm": "array",
          "pmm": "array",
          "pmg": "array",
          "pgg": "array",
          "cmm": "array",
          "p4": "array",
          "p4m": "array",
          "p4g": "array",
          "p3": "array",
          "p3m1": "array",
          "p31m": "array",
          "p6": "array",
          "p6m": "array"
        },
        "items": {
          "wyckoff": "string",
          "position": "string",
          "irreps": {
            "type": "object",
            "additional_properties": "integer"
          }
        }
      },
      "description": "Complete mode-count table for all 17 two-dimensional space groups and their Wyckoff positions, providing the number of lattice vibrational modes labeled by each irreducible representation."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verification script will read your `phonon_decomposition.json` and compare each multiplicity value (space group, Wyckoff position, irrep) against the correct, expected integer count — derived from the same group‑theoretical procedure using the accepted irreducible representations. Scoring rewards exact matches of integer multiplicities; any deviation, even by 1, indicates a mistake in the decomposition and loses credit. The final score is the fraction of correctly reproduced entries aggregated over all 17 space groups. Because the computation is deterministic when the correct character tables and projection formulas are used, a fully correct implementation will receive full credit. The evaluation is fully automated, and no manual judgment is applied. There are no tolerance margins, because the result is a set of fixed integers; the only acceptable output is the exact, correct multiplicity for each entry.
