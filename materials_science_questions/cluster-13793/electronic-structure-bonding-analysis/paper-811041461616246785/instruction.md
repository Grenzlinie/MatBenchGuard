# Valence Band Counting in Intermetallic Compounds via DFT

## Problem background
Intermetallic compounds between aluminum/gallium and transition metals, such as AlIr, RuAl<sub>2</sub>, and RuGa<sub>3</sub>, can exhibit pseudogaps or narrow bandgaps in their electronic density of states. Knowing the number of valence bands (occupied bands per primitive unit cell, without spin degeneracy) is important for testing bonding models and electron-counting rules. This reproduction task computes the number of valence bands for these three compounds using first‑principles density functional theory (DFT).

## Approach
The electronic structure of each compound is computed with an all‑electron full‑potential linearised augmented plane‑wave (LAPW) code within the local density approximation (LDA) of density functional theory. Spin polarization and spin‑orbit coupling are not included.

Crystal structures are taken from experimental literature:
- **AlIr** (CsCl‑type, space group *Pm* 3 *m*, a = 3.177 Å): Al at (0, 0, 0), Ir at (½, ½, ½).
- **RuAl<sub>2</sub>** (TiSi<sub>2</sub>‑type, space group *Fddd*, a = 8.028 Å, b = 4.721 Å, c = 8.797 Å): Ru at (0, 0, 0) and (¼, ¼, ¼); Al at (0, 0, z) and (¼, ¼, z + ¼) with z ≈ 0.319.
- **RuGa<sub>3</sub>** (CoGa<sub>3</sub>‑type, space group *P*4<sub>2</sub>/ *mnm*, a = 6.367 Å, c = 6.796 Å): Ru at (0, 0, 0); Ga at (0, 0, z) with z ≈ 0.343, and (x, x + ½, 0) with x ≈ 0.226, plus symmetry‑equivalent positions.

Self‑consistent calculations use unshifted Monkhorst‑Pack k‑point grids: 16 × 16 × 16 for AlIr, 8 × 8 × 8 for RuAl<sub>2</sub>, and 4 × 4 × 4 for RuGa<sub>3</sub>. From the converged Kohn–Sham eigenvalues, the number of occupied bands (valence bands per primitive unit cell, without spin degeneracy) is counted for each material.

## Reproduction target
Perform the DFT calculations for AlIr, RuAl<sub>2</sub>, and RuGa<sub>3</sub> as described, extract the eigenvalues, and determine the number of occupied valence bands per primitive unit cell for each compound. Write the three integer counts to the JSON file `/app/outputs/valence_bands.json` with the exact structure
```json
{"AlIr": <integer>, "RuAl2": <integer>, "RuGa3": <integer>}
```

## Assets

- Elk all-electron full-potential LAPW code: https://elk.sourceforge.net
- AlIr crystal structure
- RuAl2 crystal structure
- RuGa3 crystal structure

## Workflow steps

### Step 1: DFT ground-state calculation for AlIr
- Role: process
- Action: Perform self-consistent DFT calculation for AlIr using the experimental CsCl-type structure (Pm-3m, a=3.177 Å) with an all-electron full-potential LAPW code, LDA functional, unshifted 16×16×16 k-point grid, no spin polarization. Save eigenvalues.
- Evidence: `/app/outputs/alir_eig.txt`

### Step 2: DFT ground-state calculation for RuAl2
- Role: process
- Action: Perform self-consistent DFT calculation for RuAl2 using the experimental TiSi2-type structure (Fddd, a=8.028 Å, b=4.721 Å, c=8.797 Å) with LDA, unshifted 8×8×8 k-point grid, no spin polarization. Save eigenvalues.
- Evidence: `/app/outputs/rual2_eig.txt`

### Step 3: DFT ground-state calculation for RuGa3
- Role: process
- Action: Perform self-consistent DFT calculation for RuGa3 using the experimental CoGa3-type structure (P42/mnm, a=6.367 Å, c=6.796 Å) with LDA, unshifted 4×4×4 k-point grid, no spin polarization. Save eigenvalues.
- Evidence: `/app/outputs/ruga3_eig.txt`

### Step 4: Count valence bands and output JSON
- Role: scored (load-bearing)
- Action: From the Kohn-Sham eigenvalues obtained for AlIr, RuAl2, and RuGa3, determine the number of occupied bands per primitive unit cell (without spin degeneracy) for each compound. Write a JSON file with integer fields for AlIr, RuAl2, and RuGa3.
- Output file: `/app/outputs/valence_bands.json`
- Format: json
- Contract: {"AlIr": <int>, "RuAl2": <int>, "RuGa3": <int>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/valence_bands.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### valence_bands.json
- path: `/app/outputs/valence_bands.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Number of occupied valence bands (per primitive unit cell, without spin degeneracy) for AlIr, RuAl2, and RuGa3 computed from DFT eigenvalues.
- schema:
  - `type`: object
  - `required`:
    - `AlIr`: integer
    - `RuAl2`: integer
    - `RuGa3`: integer
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The checker will read the three integer values and compare each to the paper-reported hidden gold using exact match with tolerance 0. If any value differs, reward is 0; if all match, reward is 1.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "valence_bands.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "AlIr": "integer",
          "RuAl2": "integer",
          "RuGa3": "integer"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Number of occupied valence bands (per primitive unit cell, without spin degeneracy) for AlIr, RuAl2, and RuGa3 computed from DFT eigenvalues."
    }
  ],
  "notes": "The checker will read the three integer values and compare each to the paper-reported hidden gold using exact match with tolerance 0. If any value differs, reward is 0; if all match, reward is 1."
}
```

## How you are scored
A hidden verifier will read the three integers from your `/app/outputs/valence_bands.json` file and compare each to the correct reference values for the given crystal structures and computational settings. The comparison uses exact equality: if any of the three integers does not match the expected value, the overall reward is 0; if all three match exactly, the reward is 1. The reference values are not provided to you; you must obtain them by faithfully executing the DFT calculations.
