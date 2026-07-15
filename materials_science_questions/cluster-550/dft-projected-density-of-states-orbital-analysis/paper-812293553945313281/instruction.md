# DFT Projected Density of States Orbital Analysis

## Problem background
Chainlike polysilanes — polymers with a silicon backbone — exhibit semiconducting properties such as wide optical band gaps and photoluminescence. Understanding their electronic structure, in particular the direct band gap and the symmetry of the valence and conduction band edges, is essential for interpreting optical absorption and charge transport. This task reproduces the minimal electronic structure calculation that reveals whether the material has a directly allowed band-to-band transition at the Γ point, and how the band gap changes with simple alkyl substituents.

## Approach
The Slater‑Koster LCAO (linear combination of atomic orbitals) method is used in a semi‑empirical way. The valence basis includes Si 3s/3p, C 2s/2p, and H 1s orbitals. Interatomic Hamiltonian matrix elements are evaluated with the Harrison‑Froyen universal scaling formula V_{ll'm} = ζ_{ll'm} ℏ²/(m d²), where ζ are the universal coefficients (Vssσ, Vspσ, Vppσ, Vppπ) and d is the interatomic distance. On‑site energies for each species are taken from literature corrections that produce consistent ionisation potentials. The unit cell geometry is an ideal trans‑planar zigzag with bond lengths from Phillips rationalised radii. The secular equation is solved at the Γ point (k=0) for two model compounds: (SiH₂)ₙ and (SiHMe)ₙ (alternating H and methyl groups). The eigenvalues yield the direct band gap, and the eigenvectors are projected onto the appropriate point‑group character tables (D₂ₕ for (SiH₂)ₙ, C₂ₕ for (SiHMe)ₙ) to assign irreducible representation symmetries to the band edges.

## Reproduction target
Implement the LCAO‑Harrison‑Froyen procedure for the two trans‑planar polysilane models (SiH₂)ₙ and (SiHMe)ₙ. Build their geometry, compute all interatomic matrix elements including non‑nearest neighbours, and solve the secular equation at Γ. From the resulting eigenvalues and eigenvectors, extract for each compound:
- the direct band gap (in eV) between the highest occupied and lowest unoccupied orbital,
- the irreducible representation label of the valence band maximum (VBM),
- the irreducible representation label of the conduction band minimum (CBM).
Record these values in the scored artifact `results.json` as an array of two objects, each containing `compound`, `direct_gap_eV`, `vbm_symmetry`, and `cbm_symmetry`.

## Assets

- Harrison universal coefficients (Vssσ, Vspσ, Vppσ, Vppπ)
- Python scientific computing stack: numpy, scipy

## Workflow steps

### Step 1: Build trans-planar polysilane geometries
- Role: process
- Action: Construct atomic coordinates and lattice vectors for trans-planar (SiH2)n and (SiHMe)n chains using bond lengths from Phillips rationalized radii (Si-Si 2.34 Å, Si-C 1.94 Å, Si-H 1.54 Å, C-C 1.54 Å, C-H 1.09 Å). Assign point-group symmetries (D2h for (SiH2)n, C2h for (SiHMe)n). Define the unit cell and basis of atomic orbitals (Si 3s,3px,3py,3pz; C 2s,2px,2py,2pz; H 1s).
- Evidence: `/app/outputs/geometry_used.txt`

### Step 2: Compute interatomic LCAO matrix elements
- Role: process
- Action: For each polysilane model, compute interatomic Hamiltonian matrix elements between valence orbitals using the Harrison-Froyen formula V_{ll'm} = ζ_{ll'm} ℏ²/(m d²). Use the universal ζ coefficients (Vssσ, Vspσ, Vppσ, Vppπ) from the Harrison reference. Include non-nearest-neighbor interactions.
- Evidence: `/app/outputs/matrix_elements.csv`

### Step 3: Solve Slater-Koster secular equation at Γ and extract band gap and symmetries
- Role: scored (load-bearing)
- Action: Form the Slater-Koster Hamiltonian at the Γ-point (k=0) using the computed matrix elements and the corrected atomic on-site energies: ε_{3s}(Si)=8.0 eV, ε_{3p}(Si)=-2.0 eV, ε_{2s}(C)=-11.5 eV, ε_{2p}(C)=-8.0 eV, ε_{1s}(H)=-12.0 eV. Diagonalize to obtain eigenvalues and eigenvectors. Determine the direct band gap as the difference between the lowest unoccupied and highest occupied molecular orbitals (LUMO and HOMO). Identify the irreducible representations of the HOMO and LUMO by projecting the eigenvectors onto the point group's character table. Write the results for (SiH2)n and (SiHMe)n to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON array with two objects, one for each compound. Each object has keys: compound (string, e.g., 'SiH2', 'SiHMe'), direct_gap_eV (float, the band gap in eV), vbm_symmetry (string, irreducible representation of the valence band maximum), cbm_symmetry (string, irreducible representation of the conduction band minimum).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct band gap at Γ and band-edge symmetry labels for four trans-planar polysilane model compounds: (SiH2)n, (SiHMe)n, (SiHPh)n, and (SiMePh)n. The checker compares direct_gap_eV to the paper's values with a hidden tolerance and requires exact match for symmetry strings. (SiPh2)n is excluded from this reproduction scope because the paper's discussion of its band structure focuses on complex σ-π mixing producing multiple intruder states and does not report a single definitive skeleton band gap value.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `direct_gap_eV`, `vbm_symmetry`, `cbm_symmetry`
    - `properties`:
      - `compound`:
        - `type`: string
      - `direct_gap_eV`:
        - `type`: number
      - `vbm_symmetry`:
        - `type`: string
      - `cbm_symmetry`:
        - `type`: string

Notes: Scoring compares the computed band gaps (with tolerance) and symmetry labels (exact) against hidden reference values from the paper for all four compounds. The agent must produce results.json containing the specified keys for SiH2, SiHMe, SiHPh, and SiMePh. (SiPh2)n is excluded per the justification in the output description.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "direct_gap_eV",
            "vbm_symmetry",
            "cbm_symmetry"
          ],
          "properties": {
            "compound": {
              "type": "string"
            },
            "direct_gap_eV": {
              "type": "number"
            },
            "vbm_symmetry": {
              "type": "string"
            },
            "cbm_symmetry": {
              "type": "string"
            }
          }
        }
      },
      "description": "Direct band gap at Γ and band-edge symmetry labels for four trans-planar polysilane model compounds: (SiH2)n, (SiHMe)n, (SiHPh)n, and (SiMePh)n. The checker compares direct_gap_eV to the paper's values with a hidden tolerance and requires exact match for symmetry strings. (SiPh2)n is excluded from this reproduction scope because the paper's discussion of its band structure focuses on complex σ-π mixing producing multiple intruder states and does not report a single definitive skeleton band gap value."
    }
  ],
  "notes": "Scoring compares the computed band gaps (with tolerance) and symmetry labels (exact) against hidden reference values from the paper for all four compounds. The agent must produce results.json containing the specified keys for SiH2, SiHMe, SiHPh, and SiMePh. (SiPh2)n is excluded per the justification in the output description."
}
```

## How you are scored
After submission, a hidden verifier reads your `results.json`. It compares the reported band gaps and symmetry labels for each compound to reference values derived from the original paper. The gap is checked with a tolerance that accounts for implementation differences, and the symmetry strings are matched exactly. Each step’s artifacts are scored independently, and the scores are combined (with the main weight on `results.json`) into a final reward between 0 and 1. Reaching the paper’s numbers is not enough — you must genuinely run the described procedure; the verifier expects self‑consistent intermediate evidence files (`geometry_used.txt`, `matrix_elements.csv`) that align with the final result.
