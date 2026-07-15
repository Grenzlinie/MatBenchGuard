# DFT Band Gap Calculation for Silver Delafossites

## Problem background
Silver delafossite oxides (AgBO2 with B = Al, Ga, In) are layered materials with potential applications as transparent conducting oxides. Electronic structure calculations reveal an interplay between the fundamental direct band gap at the Γ point and the optically active direct gap at the M point. How these two gaps vary as the B‑site cation size changes determines the materials' optical transparency and is essential for validating the electronic structure predictions for this class of compounds. This task focuses on computing these gaps to investigate the trends across the AgAlO2, AgGaO2, AgInO2 series.

## Approach
Use scalar‑relativistic density functional theory (DFT) within the local density approximation (LDA). Any open‑source DFT code that supports LDA (e.g., Quantum ESPRESSO) may be used. For each compound (AgAlO2, AgGaO2, AgInO2), obtain the crystal structure data for the 2H polytype (space group P6₃/mmc) from published crystallographic data (Kandpal and Seshadri, Solid State Sci. 2002). The calculation proceeds by: (i) setting up the input files for a self‑consistent field (SCF) calculation, (ii) computing the band structure along the high‑symmetry path Γ–M–K–Γ with a non‑self‑consistent calculation, and (iii) extracting the direct band gaps at Γ and M as the energy difference between the highest valence band and lowest conduction band at those points. The computed gaps should reflect the systematic influence of the B‑site cation size.

## Reproduction target
Compute the direct band gaps at the Γ and M high‑symmetry points for 2H‑AgAlO2, AgGaO2, and AgInO2. Save the six gap values (in eV) to `/app/outputs/band_gaps.csv` with columns: compound, gap_Gamma, gap_M. The results must capture the expected variation of the Γ‑point gap and the M‑point gap across the series; the hidden verifier will evaluate both the numerical values and the trend correctness.

## Assets

- Crystal structure data for 2H AgAlO₂, AgGaO₂, AgInO₂: 10.1016/S1293-2558(02)01375-3
- DFT software (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Obtain or generate input structure files for 2H AgAlO₂, AgGaO₂, and AgInO₂ in the space group P6₃/mmc using published crystallographic data (Kandpal and Seshadri 2002). Write the structure files in a format suitable for the chosen DFT code.
- Evidence: `/app/outputs/structure_preparation.log`

### Step 2: Run DFT band structure calculations
- Role: process
- Action: For each compound, perform a scalar‑relativistic LDA DFT calculation with sufficient k‑point sampling to converge the band structure. Run a self‑consistent field calculation followed by a non‑self‑consistent band structure calculation along the high‑symmetry path Γ‑M‑K‑Γ.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 3: Extract band gaps and report
- Role: scored (load-bearing)
- Action: From the computed band structures, identify the highest valence band and lowest conduction band at Γ and M for each compound. Compute the direct band gap as the energy difference. Write the six values to /app/outputs/band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: CSV with header compound,gap_Gamma,gap_M. Rows for AgAlO2, AgGaO2, AgInO2. All values in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed direct band gaps at Γ and M points for AgAlO₂, AgGaO₂, and AgInO₂.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `gap_Gamma`, `gap_M`
  - `units`:
    - `gap_Gamma`: eV
    - `gap_M`: eV

Notes: The task reproduces the LMTO‑LDA band gap trends using any open‑source LDA DFT code. The checker compares the reported gaps to the paper's reference values with tolerance and verifies the monotonic trend at Γ and the dip at M.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "gap_Gamma",
          "gap_M"
        ],
        "units": {
          "gap_Gamma": "eV",
          "gap_M": "eV"
        }
      },
      "description": "Computed direct band gaps at Γ and M points for AgAlO₂, AgGaO₂, and AgInO₂."
    }
  ],
  "notes": "The task reproduces the LMTO‑LDA band gap trends using any open‑source LDA DFT code. The checker compares the reported gaps to the paper's reference values with tolerance and verifies the monotonic trend at Γ and the dip at M."
}
```

## How you are scored
Your submission is automatically scored by a hidden verifier. It reads `/app/outputs/band_gaps.csv`, compares each gap value to a reference within a tolerance that accounts for implementation differences, and checks that the relative ordering of the gaps across the three compounds matches the physically expected trend. The final reward (0–1) is a weighted sum: individual gap values contribute partial credit, and correctly reproducing the trend across the series receives additional weight. Reporting numbers without performing the DFT calculations will not satisfy the trend checks.
