# Group-theoretical decomposition of optical phonons for FeSi

## Problem background
FeSi is a correlated-electron material that crystallizes in the cubic B20 structure (space group P2₁3, No. 198). Each primitive cell contains four Fe and four Si atoms at equivalent Wyckoff positions, yielding 24 vibrational degrees of freedom. After subtracting the three acoustic branches, 21 optical phonon modes remain. The symmetry classification of these 21 modes dictates which ones are infrared (IR) and Raman active. Determining the irreducible representation of the optical phonons — and identifying exactly how many triply-degenerate T‑symmetry modes are IR‑active — is essential for assigning the sharp far‑infrared absorption lines observed inside the material’s low‑temperature optical gap and for distinguishing phononic from excitonic contributions to the optical response.

## Approach
Apply the group‑theoretical correlation method to decompose the optical vibrations. The procedure: (1) Identify the Wyckoff positions and site symmetry (C₃) for the Fe and Si atoms in space group P2₁3. (2) For each atom type, determine the site‑symmetry representation (the mechanical representation of the atomic displacements). (3) Correlate these site representations to the irreducible representations of the factor group T (isomorphic to the point group 23). (4) Sum the contributions over all atoms and subtract the acoustic modes (the three translations that transform as T) to obtain the irreducible representation of the optical phonons. (5) Among the resulting symmetry species, the triply‑degenerate T modes are infrared‑active because they transform as a vector. The analysis uses publicly available crystallographic data and standard character tables; it can be carried out with pen‑and‑paper or with open‑source tools (e.g., the Bilbao Crystallographic Server). The output is a single label indicating the direct sum of irreducible representations and the integer count of infrared‑active T modes.

## Reproduction target
Compute, from the crystal structure alone, the full irreducible representation of the 21 optical phonon modes of FeSi (cubic B20, space group P2₁3, factor group T, site group C₃ for both Fe and Si, 4 formula units per cell). Count how many of the triply‑degenerate T‑symmetry optical modes are infrared‑active. Package the result as a JSON object with two fields: `irreducible_representation` (a string representation of the direct‑sum label) and `infrared_active_count` (an integer). No experimental data, fitting, or external software licences are required; the computation is entirely deterministic from the publicly known structure.

## Assets

- FeSi crystal structure data (space group P2₁3, site symmetry C₃)

## Workflow steps

### Step 1: Phonon symmetry decomposition
- Role: scored (load-bearing)
- Action: Perform a group-theoretical decomposition of optical phonon modes for FeSi (cubic B20, space group P2₁3, factor group T(23), site group C₃ for Fe and Si, 4 formula units per cell) using the correlation method (or equivalent group-theoretical approach). Determine the full irreducible representation of the 21 optical phonon modes and count the number of triply-degenerate T symmetry modes that are infrared-active. Write the result to /app/outputs/phonon_symmetry.json.
- Output file: `/app/outputs/phonon_symmetry.json`
- Format: json
- Contract: {"type": "object", "required": {"irreducible_representation": "string", "infrared_active_count": "integer"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_symmetry.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_symmetry.json
- path: `/app/outputs/phonon_symmetry.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The irreducible representation of optical phonons as a string like 'nA+mE+pT' and the integer count of infrared-active T modes (the agent must compute them).
- schema:
  - `type`: object
  - `required`:
    - `irreducible_representation`: string
    - `infrared_active_count`: integer

Notes: Only the group-theoretical decomposition is scored. Experimental data analysis (Kramers-Kronig, gap extraction) is excluded because raw data is private.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_symmetry.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "irreducible_representation": "string",
          "infrared_active_count": "integer"
        }
      },
      "description": "The irreducible representation of optical phonons as a string like 'nA+mE+pT' and the integer count of infrared-active T modes (the agent must compute them)."
    }
  ],
  "notes": "Only the group-theoretical decomposition is scored. Experimental data analysis (Kramers-Kronig, gap extraction) is excluded because raw data is private."
}
```

## How you are scored
Your submitted `/app/outputs/phonon_symmetry.json` is the only scored artifact. A hidden verifier independently derives the correct irreducible representation and IR‑active count from the same crystal structure using group theory. It compares your `irreducible_representation` string and `infrared_active_count` integer to the expected values. Because the result is a fixed deterministic group‑theory outcome, full credit is awarded only when both fields match the expected values (within negligible typographic formatting tolerance). The reward is 1.0 if both fields are correct and 0.0 otherwise.
