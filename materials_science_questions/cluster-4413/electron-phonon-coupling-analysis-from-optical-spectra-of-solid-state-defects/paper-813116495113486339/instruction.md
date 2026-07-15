# Phonon symmetry classification at the M point of 4H-SiC

## Problem background
In 4H‑SiC the conduction‑band minimum sits at the M point of the Brillouin zone, so phonon‑assisted optical recombination involves M‑point phonons. Classifying these phonons by symmetry is essential for interpreting photoluminescence spectra and for deriving polarization selection rules. The unit cell contains 8 atoms, yielding 24 phonon branches, and the little group of the wave‑vector at M is C₂v. The classification reduces the displacement representation of the crystal to a direct sum of the four one‑dimensional irreducible representations M₁, M₂, M₃, M₄. This task reproduces that group‑theoretical decomposition: you will determine how many phonon modes transform under each irreducible representation (the multiplicities) and you will construct the orthonormal symmetry‑mode vectors that bring the displacement representation into block‑diagonal form.

## Approach
Use the character method of group theory. First, build the 24‑dimensional displacement representation Γ^disp for the eight atoms in the unit cell under the operations of the C₂v little group. The representation is the direct product of the permutation representation (telling how the atoms are permuted by each symmetry operation) and the 3‑dimensional vector representation (the rotational part). Compute the characters χ^disp(T) for each of the four group elements: E, C₂, σ_v, σ_v′. Then apply the standard projection formula (the scalar product of the Γ^disp character with each irreducible character, divided by the group order) to obtain the multiplicity, i.e. the number n_p of phonons transforming as M_p. In a second step, use projection operators to generate an orthonormal set of 24‑component symmetry‑mode vectors that block‑diagonalize Γ^disp. These vectors pin the displacement patterns that belong to each symmetry species.

## Reproduction target
Produce two scored artifacts:
1. The integer multiplicities n1, n2, n3, n4 of the irreducible representations M1, M2, M3, M4 at the M point.
2. The corresponding orthonormal symmetry‑mode vectors: 8 vectors transforming as M1, 4 as M2, 4 as M3, and 8 as M4. Each vector is a real 24‑element array that describes a relative displacement pattern of the eight atoms.

## Assets

- 4H-SiC crystal structure
- C₂v character table

## Workflow steps

### Step 1: Compute phonon symmetry multiplicities
- Role: scored
- Action: Construct the 24‑dimensional displacement representation Γ^disp for the eight atoms in the unit cell under the C₂v little group at the M point. Express the representation as a direct product of the permutation representation and the vector representation. Compute the characters χ^disp(T) for the four group elements E, C₂, σ_v, σ_v'. Apply the standard projection formula n_p = (1/4) Σ_T χ^disp(T) χ^p(T) to obtain the multiplicity n_p of each irreducible representation M_p (p=1,2,3,4).
- Output file: `/app/outputs/step_01_multiplicities.json`
- Format: json
- Contract: {"n1": <int>, "n2": <int>, "n3": <int>, "n4": <int>}
- Scoring: scored by hidden verifier

### Step 2: Generate symmetry‑mode vectors
- Role: scored
- Action: Using projection operators, compute the orthonormal symmetry‑adapted basis vectors that block‑diagonalize the displacement representation. Produce the sets of real 24‑component vectors transforming as M1 (8 vectors), M2 (4 vectors), M3 (4 vectors), and M4 (8 vectors). Each vector describes a relative displacement pattern of the eight atoms in the unit cell.
- Output file: `/app/outputs/step_02_symmetry_modes.json`
- Format: json
- Contract: {"M1": [ [float; 24], … 8 vectors ], "M2": [ [float; 24], … 4 vectors ], "M3": [ [float; 24], … 4 vectors ], "M4": [ [float; 24], … 8 vectors ]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_multiplicities.json`
- `/app/outputs/step_02_symmetry_modes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_multiplicities.json
- path: `/app/outputs/step_01_multiplicities.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Integer multiplicities of the four one‑dimensional irreducible representations M1,M2,M3,M4 of C₂v in the displacement representation at the M point. Exact match required (no tolerance).
- schema:
  - `type`: object
  - `required`:
    - `n1`: int
    - `n2`: int
    - `n3`: int
    - `n4`: int
  - `items`: object
  - `required_columns`:
  - `units`: object

### step_02_symmetry_modes.json
- path: `/app/outputs/step_02_symmetry_modes.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Orthonormal symmetry‑mode vectors (real 24‑element arrays) that bring Γ^disp into block‑diagonal form. Checker will verify correct transformation under the four group operations, orthonormality, and that they span the 24‑dimensional space.
- schema:
  - `type`: object
  - `required`:
    - `M1`: float[8][24]
    - `M2`: float[4][24]
    - `M3`: float[4][24]
    - `M4`: float[8][24]
  - `items`: object
  - `required_columns`:
  - `units`: object

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_multiplicities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "n1": "int",
          "n2": "int",
          "n3": "int",
          "n4": "int"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Integer multiplicities of the four one‑dimensional irreducible representations M1,M2,M3,M4 of C₂v in the displacement representation at the M point. Exact match required (no tolerance)."
    },
    {
      "file": "step_02_symmetry_modes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "M1": "float[8][24]",
          "M2": "float[4][24]",
          "M3": "float[4][24]",
          "M4": "float[8][24]"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Orthonormal symmetry‑mode vectors (real 24‑element arrays) that bring Γ^disp into block‑diagonal form. Checker will verify correct transformation under the four group operations, orthonormality, and that they span the 24‑dimensional space."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks each stage. For the multiplicities, it recomputes the characters and the projection formula and requires an exact match. For the symmetry‑mode vectors, it verifies three properties: (a) each vector transforms correctly under the four group operations (multiplying by the appropriate representation matrix yields the expected sign change), (b) all vectors within and across symmetry species are mutually orthonormal, and (c) the set spans the full 24‑dimensional space. The two stages are weighted and combined into a single reward between 0 and 1; merely reporting numbers without genuine computation is insufficient, because the checker performs its own independent recomputation and structural audits.
