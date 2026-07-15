# Band Gap Estimation of Pb/Bi Hybrid Perovskites with AK13/GAM Density Functional Theory

## Problem background
Hybrid metal halide perovskites (HaPs) with Pb and Bi are promising materials for solar cells, but accurately computing their band gaps with standard density functional theory (DFT) is challenging because spin-orbit coupling (SOC) significantly reduces the gap size. Conventional semilocal functionals strongly underestimate band gaps in these compounds, while more accurate methods like GW or hybrid functionals come with high computational cost, limiting their use for large or defective structures. There is a need for a computationally efficient DFT approach that can estimate band gaps with accuracy comparable to higher-level methods.

## Approach
We employ full-relativistic DFT calculations using the parameter‑free AK13 exchange functional (Armiento–Kümmel, as implemented in the libxc library) combined with the GAM (Nonseparable Gradient Approximation Minnesota) correlation functional. This functional combination is applied via the Quantum ESPRESSO code (QE v6.8) to compute the electronic structure and fundamental band gaps of Pb- and Bi‑based HaPs.

Crystal structures are taken from the literature (PBEsol‑optimized conventional unit cells). Full‑relativistic norm‑conserving PBE pseudopotentials are generated using the ONCVPSP tool (version 4.0.1) from SG15 input files, covering the required elements (H, C, N, Cl, Br, Ag, I, Cs, Pb, Bi). The plane‑wave cutoff is 60 Ry, density convergence threshold 1×10⁻¹² Ry, and Grimme’s D2 van der Waals correction is applied. For each compound, a Monkhorst‑Pack k‑point mesh is used with the sizes specified in the workflow step. From the converged Kohn–Sham eigenvalues we obtain the fundamental (VBM–CBM) band gap.

## Reproduction target
Produce a comma‑separated‑value (CSV) file `band_gaps_ak13_gam.csv` containing the computed AK13/GAM fundamental band gaps (in eV) for the following 13 Pb‑ and Bi‑based hybrid perovskites:

MAPbCl₃, FAPbCl₃, CsPbCl₃‑orth, MAPbBr₃, FAPbBr₃, CsPbBr₃‑orth, MAPbI₃‑tetr, FAPbI₃, CsPbI₃‑orth, HdAPbI₄‑mon, Cs₂AgBiCl₆, Cs₂AgBiBr₆, Cs₂AgBiI₆.

The CSV must have two columns, 'compound' and 'band_gap' (float), with exactly one row per compound. The verifier will compare the reported band gaps to hidden reference values to assess the quality of the reproduction.

## Assets

- Quantum ESPRESSO v6.8: https://www.quantum-espresso.org/
- ONCVPSP v4.0.1: http://www.mat-simresearch.com/
- libxc v5.1.6: https://www.tddft.org/programs/libxc/
- SG15 pseudopotential input files: https://github.com/PrincetonUniversity/SG15
- Hybrid perovskite crystal structures (Pb/Bi-based): https://github.com/WMD-group/hybrid-perovskites

## Workflow steps

### Step 1: Acquire crystal structures
- Role: process
- Action: Download or construct the PBEsol-optimized crystal structures for the 13 target Pb/Bi-based hybrid perovskites from the Walsh group repository (hybrid-perovskites) and the cited references. Ensure the conventional unit cell geometries match those used in the paper.
- Evidence: none

### Step 2: Prepare full-relativistic pseudopotentials
- Role: process
- Action: Generate full-relativistic norm-conserving PBE pseudopotentials using ONCVPSP v4.0.1 from the SG15 input files, or use equivalently generated pre-existing full-relativistic PBE norm-conserving pseudopotentials (e.g., from the SG15 ONCVPSP release or similar). Required elements: H, C, N, Cl, Br, Ag, Sn, I, Cs, Pb, Bi.
- Evidence: none

### Step 3: Compute AK13/GAM band gaps for Pb/Bi HaPs
- Role: scored (load-bearing)
- Action: For each of the 13 Pb/Bi-based perovskites, run a full-relativistic DFT calculation using Quantum ESPRESSO v6.8 with the AK13 exchange functional (from libxc v5.1.6) and the GAM correlation functional. Use plane-wave cutoff 60 Ry, density convergence threshold 1e-12 Ry, Grimme D2 van der Waals correction, PBEsol-optimized structures, and Monkhorst-Pack k-point meshes as specified: MAPbCl3 10×10×10, FAPbCl3 10×10×10, CsPbCl3-orth 8×8×10, MAPbBr3 10×10×10, FAPbBr3 10×10×10, CsPbBr3-orth 8×8×6, MAPbI3-tetr 6×6×6, FAPbI3 10×10×10, CsPbI3-orth 8×8×6, HdAPbI4-mon 4×6×6, Cs2AgBiCl6 10×10×10, Cs2AgBiBr6 10×10×10, Cs2AgBiI6 10×10×10. Determine the fundamental band gap from the Kohn-Sham eigenvalues. Write results to a CSV file.
- Output file: `/app/outputs/band_gaps_ak13_gam.csv`
- Format: csv
- Contract: Columns: compound (string), band_gap (float, eV). Exactly 13 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps_ak13_gam.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps_ak13_gam.csv
- path: `/app/outputs/band_gaps_ak13_gam.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: AK13/GAM band gaps (eV) for the 13 Pb/Bi hybrid perovskites. The checker computes mean absolute error against hidden reference values and scores based on a tolerance threshold.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `band_gap`
  - `columns`:
    - `compound`: string
    - `band_gap`: float (eV)

Notes: Checker compares reported band gaps to hidden reference values and scores based on mean absolute error.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps_ak13_gam.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "band_gap"
        ],
        "columns": {
          "compound": "string",
          "band_gap": "float (eV)"
        }
      },
      "description": "AK13/GAM band gaps (eV) for the 13 Pb/Bi hybrid perovskites. The checker computes mean absolute error against hidden reference values and scores based on a tolerance threshold."
    }
  ],
  "notes": "Checker compares reported band gaps to hidden reference values and scores based on mean absolute error."
}
```

## How you are scored
A hidden verifier reads your output file `band_gaps_ak13_gam.csv` and compares your computed band gaps to undisclosed reference values. It computes a quantitative measure of agreement (closeness); better agreement yields a higher reward. The verifier also checks that the output file has the correct format, required columns, and the expected number of rows. Your final reward is a number between 0 and 1, where 1 represents near‑perfect reproduction and 0 indicates large deviations or an invalid file. Simply run the described DFT workflow — do not attempt to guess the reference values.
