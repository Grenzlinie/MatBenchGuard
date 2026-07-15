# DFT-B3LYP vibrational frequency reproduction of m-methylaniline

## Problem background
Vibrational spectroscopy is a key technique for identifying functional groups and understanding molecular structure. Reliable computational normal-mode assignments are essential for interpreting experimental IR and Raman spectra. m-Methylaniline (mMA) is an organic molecule whose 45 vibrational normal modes have been studied to assist in such assignments and to examine the effects of substituents on aromatic systems.

## Approach
Density functional theory (DFT) with the B3LYP hybrid functional and the 6-31G* basis set provides harmonic vibrational frequencies. After geometry optimization and frequency calculation, raw frequencies are systematically overestimated. To bring them closer to experimental values, scaling factors are applied to different classes of normal modes. The modes are classified by their dominant motion: stretching (C-C/C-N vs. N-H/C-H) and deformation (N-H/C-H vs. C-C/C-N/out-of-plane). Each class is then multiplied by a fixed scaling factor. The corrected frequencies are listed in the order they appear in the calculation output.

## Reproduction target
Produce the list of 45 scaled harmonic vibrational frequencies (in cm⁻¹) for m‑methylaniline computed at the DFT‑B3LYP/6‑31G* level. Use the scaling factors: 0.980 for C‑C/C‑N stretches, 0.953 for N‑H/C‑H stretches, 0.973 for N‑H/C‑H deformations, 0.996 for C‑C/C‑N and out‑of‑plane deformations. The frequencies must be written in the order they appear in the calculation. Save the result as a two‑column CSV with `mode_index` (integer from 1 to 45) and `corrected_frequency` (float in cm⁻¹).

## Assets

- Open-source quantum chemistry software (ORCA, Psi4, PySCF, etc.): https://orcaforum.kofo.mpg.de/ or https://psicode.org/ or https://github.com/pyscf/pyscf

## Workflow steps

### Step 1: Build initial geometry of m-methylaniline
- Role: process
- Action: Generate a reasonable 3D structure of m-methylaniline (e.g., from the SMILES string Cc1cccc(N)c1) using a molecular builder or a geometry generation tool.
- Evidence: none

### Step 2: DFT geometry optimization and harmonic frequency calculation
- Role: process
- Action: Perform a DFT B3LYP/6-31G* geometry optimization and harmonic vibrational frequency calculation on the initial structure to obtain the optimized geometry and raw harmonic frequencies.
- Evidence: none

### Step 3: Classify normal modes, apply scaling factors, and write corrected frequencies
- Role: scored (load-bearing)
- Action: Classify each raw harmonic normal mode by its dominant motion (C-C/C-N stretch, N-H/C-H stretch, N-H/C-H deformation, or C-C/C-N/out-of-plane deformation). Apply the scaling factors: 0.980 for C-C/C-N stretches, 0.953 for N-H/C-H stretches, 0.973 for N-H/C-H deformations, 0.996 for C-C/C-N/out-of-plane deformations. Output the list of 45 corrected frequencies in the order they appear in the calculation.
- Output file: `/app/outputs/corrected_frequencies.csv`
- Format: csv
- Contract: mode_index, corrected_frequency
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/corrected_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### corrected_frequencies.csv
- path: `/app/outputs/corrected_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The 45 DFT-B3LYP/6-31G* corrected vibrational frequencies (cm⁻¹) in the order they appear in the calculation, with mode_index and corrected_frequency.
- schema:
  - `type`: table
  - `required_columns`: `mode_index`, `corrected_frequency`
  - `units`:
    - `corrected_frequency`: cm⁻¹

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "corrected_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_index",
          "corrected_frequency"
        ],
        "units": {
          "corrected_frequency": "cm⁻¹"
        }
      },
      "description": "The 45 DFT-B3LYP/6-31G* corrected vibrational frequencies (cm⁻¹) in the order they appear in the calculation, with mode_index and corrected_frequency."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted `corrected_frequencies.csv` will be read by an automated verifier. The verifier compares each `corrected_frequency` value to a hidden gold reference. Every one of the 45 modes is checked individually. Your reward is the fraction of modes (0 to 1) whose absolute deviation from the reference is within a pre‑set tolerance. A perfect score requires executing the full DFT computation and applying the scaling factors correctly; guessing or copying values will not match all modes within the required tolerance.
