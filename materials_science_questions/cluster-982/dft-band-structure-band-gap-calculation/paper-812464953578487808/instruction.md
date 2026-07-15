# Band Gaps of Alkaline-Earth Pnictides from DFT

## Problem background
The electronic properties of alkaline-earth pnictide compounds are of interest because they can exhibit either metallic or semiconducting behavior depending on composition and relativistic effects. This task investigates two prototype compounds: Mg3Bi2 and Mg3Sb2. Both crystallize in a hexagonal La2O3-type structure and their band structures can be computed using first-principles density functional theory (DFT). The goal is to determine whether each material has a band gap and, if so, its magnitude. Relativistic effects, especially spin-orbit coupling for the heavier Bi atoms, are known to play a critical role and must be included in the calculations.

## Approach
The reproduction uses a plane-wave pseudopotential DFT code (e.g., Quantum ESPRESSO) to compute the electronic band structure from the given crystal structures. For Mg3Bi2, fully relativistic pseudopotentials including spin-orbit coupling are required; for Mg3Sb2, scalar-relativistic pseudopotentials suffice. In both cases, the exchange-correlation functional should be a standard generalized-gradient approximation (PBE). The band structure is calculated along the high-symmetry path Γ–A–K–H–M–L–Γ of the hexagonal Brillouin zone. The band gap is determined by inspecting the eigenvalues relative to the Fermi level: for Mg3Bi2, whether any bands cross the Fermi level; for Mg3Sb2, the indirect gap between the valence band maximum (expected near Γ) and the conduction band minimum (expected along the M–L line).

## Reproduction target
Perform DFT band structure calculations for Mg3Bi2 and Mg3Sb2 using the crystal structures specified in the workflow steps. For Mg3Bi2, include spin-orbit coupling and output either the word "metallic" if no band gap exists, or the band gap value in eV if a gap is found. For Mg3Sb2, compute the indirect band gap between the valence band maximum at Γ and the conduction band minimum along M–L, and output a single numeric value in eV. The results must be saved to the specified output files under /app/outputs.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotential library

## Workflow steps

### Step 1: Mg3Bi2 band structure and band gap verdict
- Role: scored (load-bearing)
- Action: Perform a DFT band structure calculation for Mg3Bi2 using the provided crystal structure (hexagonal, space group P-3m1, a=4.666 Å, c=7.401 Å, atomic positions: Mg(1) at (0,0,0), Mg(2) at (0.57735,0,0.36682), Bi at (0.57735,0,1.01790)). Include spin-orbit coupling. Compute the electronic band structure along the high-symmetry path Γ–A–K–H–M–L–Γ. Determine whether the material has a band gap: if the Fermi level crosses bands, write the string "metallic"; if a gap exists, write its value in eV. Save the result to /app/outputs/step_01_mg3bi2_gap.txt.
- Output file: `/app/outputs/step_01_mg3bi2_gap.txt`
- Format: txt
- Contract: Single line: exactly 'metallic' or a floating-point number (e.g., 0.0).
- Scoring: scored by hidden verifier

### Step 2: Mg3Sb2 band structure and band gap
- Role: scored (load-bearing)
- Action: Perform a DFT band structure calculation for Mg3Sb2 using the provided crystal structure (hexagonal, space group P-3m1, a=4.573 Å, c=7.229 Å, atomic positions: Mg(1) at (0,0,0), Mg(2) at (0.57735,0,0.37154), Sb at (0.57735,0,0.99603)). Use scalar-relativistic pseudopotentials. Compute the band structure along the high-symmetry path Γ–A–K–H–M–L–Γ. Determine the indirect band gap between the valence band maximum at Γ and the conduction band minimum along the line M–L. Write the band gap value in eV to /app/outputs/step_02_mg3sb2_gap.txt.
- Output file: `/app/outputs/step_02_mg3sb2_gap.txt`
- Format: txt
- Contract: A floating-point number representing the indirect band gap in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mg3bi2_gap.txt`
- `/app/outputs/step_02_mg3sb2_gap.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mg3bi2_gap.txt
- path: `/app/outputs/step_01_mg3bi2_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Verdict on the band gap of Mg3Bi2 after a DFT calculation including spin-orbit coupling.
- schema:
  - `type`: text
  - `description`: Single line of text. If no band gap exists, write the word 'metallic' (case-insensitive). If a band gap exists, write its value in eV as a floating-point number.

### step_02_mg3sb2_gap.txt
- path: `/app/outputs/step_02_mg3sb2_gap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Computed indirect band gap of Mg3Sb2 from a scalar-relativistic DFT band structure calculation.
- schema:
  - `type`: text
  - `description`: Single line containing a floating-point number representing the indirect band gap of Mg3Sb2 in eV.

Notes: Both artifacts are scored by comparing to hidden paper-reported values. The checker for step_01 expects a case-insensitive match to 'metallic' (or a numeric gap if the calculation yields one). The checker for step_02 compares the submitted gap to a hidden reference with a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mg3bi2_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single line of text. If no band gap exists, write the word 'metallic' (case-insensitive). If a band gap exists, write its value in eV as a floating-point number."
      },
      "description": "Verdict on the band gap of Mg3Bi2 after a DFT calculation including spin-orbit coupling."
    },
    {
      "file": "step_02_mg3sb2_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single line containing a floating-point number representing the indirect band gap of Mg3Sb2 in eV."
      },
      "description": "Computed indirect band gap of Mg3Sb2 from a scalar-relativistic DFT band structure calculation."
    }
  ],
  "notes": "Both artifacts are scored by comparing to hidden paper-reported values. The checker for step_01 expects a case-insensitive match to 'metallic' (or a numeric gap if the calculation yields one). The checker for step_02 compares the submitted gap to a hidden reference with a tolerance."
}
```

## How you are scored
Each workflow step produces a scored artifact. A hidden verifier independently reads your output files and compares them against reference values derived from the original study. For Step 1, the verifier checks whether your file correctly reports that Mg3Bi2 is metallic (case-insensitive) or contains a numerical gap if your calculation found one. For Step 2, the verifier compares your reported band gap in eV to a reference value using an appropriate tolerance. Partial credit is awarded based on how close your result is to the expected answer. The final reward is a weighted combination of the two step scores. Simply writing the paper's reported numbers without performing the DFT calculations will not pass; the task requires genuine execution of the computational workflow.
