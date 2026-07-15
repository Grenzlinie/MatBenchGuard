# Zone-center phonon irreducible representation decomposition in tetragonal phase of Ca3X2O7

## Problem background
The Ruddlesden-Popper compounds Ca3X2O7 (X=Mn,Ti) adopt a high-temperature tetragonal phase with space group I4/mmm. Understanding the vibrational properties of this parent lattice is essential for interpreting infrared and Raman spectra, because the symmetry of zone-center (q=0) phonon modes determines their optical activity (polarization selection rules). The present task addresses the determination of which irreducible representations of the I4/mmm point group are spanned by the atomic displacement vectors of the occupied Wyckoff orbits, and consequently how many IR-active and Raman-active phonon modes exist at the zone center.

## Approach
We use standard group-theoretical decomposition. The input data are: (i) the character table of the little group at q=0 for space group I4/mmm (point group D4h), shown below; (ii) the occupied Wyckoff positions and their multiplicities in the primitive cell.

**Character table (D4h) – relevant irreps and optical activity**

| Irrep      | Dipole (IR)                   | Raman tensor                     |
|------------|-------------------------------|----------------------------------|
| Γ1+        | –                             | a(ṽᵢ+ṽⱼ) + b k̂k̂                  |
| Γ2+        | –                             | c(ṽᵢ–ṽⱼ)                         |
| Γ3+        | –                             | –                                |
| Γ4+        | –                             | d(ṽᵢ+? actually none; silent)    |
| Γ5+ (2‑dim)| –                             | e(ṽᵢ k̂ + k̂ ṽᵢ), e(ṽⱼ k̂ + k̂ ṽⱼ)   |
| Γ1−        | –                             | –                                |
| Γ2−        | –                             | –                                |
| Γ3−        | g k̂ (z-polarized)             | –                                |
| Γ4−        | –                             | –                                |
| Γ5− (2‑dim)| h ṽᵢ, h ṽⱼ (x,y-polarized)    | –                                |

(The full character table with all symmetry operations is provided separately; the agent may use the known D4h character table or the embedded version below.)

**Wyckoff orbits** (occupied sites in the primitive unit cell):
- Orbit a (Wyckoff letter a, site symmetry 4/mmm): two equivalent oxygen atoms at (0,0,0) and (0,0,1/2).
- Orbit e (Wyckoff letter e, site symmetry 4mm): three independent sets, each containing two atoms related by the 4-fold axis, at (0,0,±z) with z = ρ+½, –ρ+½ (Ca atoms), z = ±ξ (Ti/Mn atoms), and z = ±χ (apical oxygen atoms). Thus orbit e comprises 6 atoms in total.
- Orbit g (Wyckoff letter g, site symmetry 2mm): one set of four equatorial oxygen atoms at (0,½,τ), (0,½,–τ), (½,0,τ), (½,0,–τ).

Multiplicities per orbit as used in the total decomposition: a appears 2 times, e appears 3 times, g appears 1 time (i.e., the total primitive cell contains 2 a-type atoms, 6 e-type atoms, and 4 g-type atoms).

**Procedure:**
1. For each Wyckoff orbit, construct the reducible displacement representation Γ(orbit) by taking the direct product of the permutation representation of the atoms in the orbit and the 3‑dimensional vector representation. Using the D4h character table, determine the character of Γ(orbit) for every symmetry operation, then decompose Γ(orbit) into irreducible components using orthogonality relations.
2. Multiply each per-orbit decomposition by the orbit multiplicity (2 for a, 3 for e, 1 for g) and sum to obtain the total decomposit ion Γtot.
3. Using the dipole/Raman entries in the character table, classify each irrep as IR-active (x,y from Γ5−, z from Γ3−) or Raman-active (Γ1+, Γ2+, Γ5+). For each active irrep, assign the appropriate polarization labels following the convention in the table above. For doubly degenerate irreps, note that two orthogonal polarisations exist (e.g., Γ5− gives x- and y-polarized modes).
4. Assemble the results into a JSON file with three sections: (a) `orbit_decompositions` listing the irreps for a single a, e, and g orbit, (b) `total_decomposition` giving the integer multiplicity of each irrep in Γtot, and (c) `mode_counts` a table that, for each orbit, indicates the number of IR-active and Raman-active modes and their polarisations.

## Reproduction target
Produce a JSON file (`step_01_phonon_decomposition.json`) that contains the irreducible representation decomposition of the zone-centre phonon displacement space for the tetragonal I4/mmm phase of Ca3X2O7. The file must include:
- The per-orbit decomposition for the a, e, and g Wyckoff orbits (each orbit considered once, before applying multiplicities).
- The total decomposition after summing with the correct orbit multiplicities (2×a + 3×e + 1×g).
- A table of mode counts per orbit, separately for IR-active and Raman-active modes, with their polarization descriptions (e.g., “x,y from Γ5−”, “z from Γ3−”, and similarly for Raman modes).
All counts are integer; the decompositions are unique. Your output will be compared against the correct group-theoretical result.

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Phonon irrep decomposition and mode counting
- Role: scored
- Action: Using the provided character table (I4/mmm little group at q=0) and the occupied Wyckoff orbits a, e, g with their multiplicities, compute the reducible displacement representation for each orbit, decompose into irreps, sum with multiplicities (2,3,1) to obtain the total decomposition, and classify modes as IR- or Raman-active based on the character table's dipole and Raman entries. Output the results to step_01_phonon_decomposition.json.
- Output file: `/app/outputs/step_01_phonon_decomposition.json`
- Format: json
- Contract: {
  "orbit_decompositions": [
    {
      "orbit": "a",
      "multiplicity": 2,
      "irreps": ["Γ5−", "Γ3−"]
    },
    {
      "orbit": "e",
      "multiplicity": 3,
      "irreps": ["Γ5−", "Γ3−", "Γ5+", "Γ1+"]
    },
    {
      "orbit": "g",
      "multiplicity": 1,
      "irreps": ["Γ5−", "Γ5−", "Γ4−", "Γ3−", "Γ5+", "Γ5+", "Γ2+", "Γ1+"]
    }
  ],
  "total_decomposition": {
    "Γ5−": 7,
    "Γ4−": 1,
    "Γ3−": 6,
    "Γ5+": 5,
    "Γ1+": 4,
    "Γ2+": 1
  },
  "mode_counts": [
    {
      "orbit": "a",
      "activity": "IR",
      "polarization": "x,y from Γ5− (doubly degenerate), z from Γ3−",
      "count": "1 each"
    },
    {
      "orbit": "a",
      "activity": "Raman",
      "polarization": "none",
      "count": "0"
    },
    {
      "orbit": "e",
      "activity": "IR",
      "polarization": "x,y from Γ5−, z from Γ3−",
      "count": "1 each"
    },
    {
      "orbit": "e",
      "activity": "Raman",
      "polarization": "x,y from Γ5+, z^2 from Γ1+",
      "count": "1 each"
    },
    {
      "orbit": "g",
      "activity": "IR",
      "polarization": "x,y from two Γ5−, z from Γ3−",
      "count": "2 (doubly degenerate) each for x/y, 1 for z"
    },
    {
      "orbit": "g",
      "activity": "Raman",
      "polarization": "two Γ5+ pairs, Γ2+, Γ1+",
      "count": "2 (doubly degenerate) each for x,y, 1 for Γ2+, 1 for Γ1+"
    }
  ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_decomposition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_decomposition.json
- path: `/app/outputs/step_01_phonon_decomposition.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zone-center phonon displacement representation decomposition and mode classification for the tetragonal I4/mmm phase. The checker verifies that the total decomposition equals the weighted sum of per-orbit decompositions and that all irrep multiplicities and mode counts per orbit exactly match the paper's reported values.
- schema:
  - `type`: object
  - `required`: `orbit_decompositions`, `total_decomposition`, `mode_counts`
  - `properties`:
    - `orbit_decompositions`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `orbit`, `multiplicity`, `irreps`
        - `properties`:
          - `orbit`:
            - `type`: string
          - `multiplicity`:
            - `type`: integer
          - `irreps`:
            - `type`: array
            - `items`:
              - `type`: string
    - `total_decomposition`:
      - `type`: object
      - `description`: Mapping from irrep label (string) to integer multiplicity
    - `mode_counts`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `orbit`, `activity`, `polarization`, `count`
        - `properties`:
          - `orbit`:
            - `type`: string
          - `activity`:
            - `type`: string
            - `enum`: `IR`, `Raman`
          - `polarization`:
            - `type`: string
          - `count`:
            - `type`: string

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_decomposition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "orbit_decompositions",
          "total_decomposition",
          "mode_counts"
        ],
        "properties": {
          "orbit_decompositions": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "orbit",
                "multiplicity",
                "irreps"
              ],
              "properties": {
                "orbit": {
                  "type": "string"
                },
                "multiplicity": {
                  "type": "integer"
                },
                "irreps": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              }
            }
          },
          "total_decomposition": {
            "type": "object",
            "description": "Mapping from irrep label (string) to integer multiplicity"
          },
          "mode_counts": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "orbit",
                "activity",
                "polarization",
                "count"
              ],
              "properties": {
                "orbit": {
                  "type": "string"
                },
                "activity": {
                  "type": "string",
                  "enum": [
                    "IR",
                    "Raman"
                  ]
                },
                "polarization": {
                  "type": "string"
                },
                "count": {
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "description": "Zone-center phonon displacement representation decomposition and mode classification for the tetragonal I4/mmm phase. The checker verifies that the total decomposition equals the weighted sum of per-orbit decompositions and that all irrep multiplicities and mode counts per orbit exactly match the paper's reported values."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `step_01_phonon_decomposition.json`. It checks:
- that the per-orbit irreps match the true decomposition for each Wyckoff orbit;
- that the `total_decomposition` equals the weighted sum of the per-orbit decompositions (2×a + 3×e + g);
- that the `mode_counts` table correctly reports the number of IR‑ and Raman‑active modes per orbit, with the right polarizations derived from the character table’s dipole/Raman entries.

Because the group-theoretical analysis yields deterministic integer counts, the verifier uses exact comparison. Your reward is the fraction of correct entries across these checks. Simply reporting a plausible-looking set of numbers without performing the correct decomposition will not pass.
