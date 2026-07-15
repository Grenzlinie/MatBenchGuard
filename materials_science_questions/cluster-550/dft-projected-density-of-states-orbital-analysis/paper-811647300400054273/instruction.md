# Au25 Nanocluster Simulated EXAFS Peaks and Local Density of States Electron Counts

## Problem background
Gold‑thiolate nanoclusters such as Au25(SR)18 combine a metallic Au13 icosahedral core with six surrounding RS–Au–S(R)–Au–SR staple motifs. Extended X‑ray absorption fine structure (EXAFS) can resolve the local bonding, but deconvolving the multiple Au–Au coordination shells is challenging. A site‑specific EXAFS fitting scheme using one Au–S and three distinct Au–Au shells has been proposed to separate the short (core–surface), mid‑length (surface–surface), and long‑range (surface–staple) interactions. Computational EXAFS simulations and ab initio calculations of the angular‑momentum‑projected local density of states (l‑DOS) provide a basis for validating this separation and for correlating the electronic structure with the structural domains. The present task requires reproducing those two computations: simulating the k³‑weighted Fourier‑transformed EXAFS to extract the three Au–Au peak positions, and computing the site‑specific l‑DOS to obtain the 6s, 6p, and 5d electron counts for each distinct Au environment (central, surface, staple).

## Approach
The workflow uses the FEFF8 ab initio multiple‑scattering code, starting from the publicly available crystal structure of Au25(SCH2CH2Ph)18⁻ (CCDC 654133). FEFF8 calculates the EXAFS phase and amplitude functions and the projected density of states self‑consistently. For the EXAFS simulation, the k³‑weighted spectrum is obtained by averaging contributions from all symmetry‑inequivalent Au sites; its Fourier transform reveals distinct peaks corresponding to the three Au–Au coordination shells, whose R‑space positions are extracted. For the l‑DOS calculation, the angular‑momentum‑resolved densities of states are computed for representative Au atoms from each site type: the central Au, the surface Au atoms, and the staple Au atoms. The integrated 6s, 6p, and 5d electron counts are then collected. The procedure is fully deterministic given the crystal structure and the FEFF8 implementation.

## Reproduction target
Produce two output artifacts from the FEFF8 computations:
- A JSON file containing the three Au–Au peak positions (in Å) extracted from the simulated EXAFS Fourier transform: (Au‑Au)₁ (short), (Au‑Au)₂ (mid), and (Au‑Au)₃ (long).
- A CSV file with one row per distinct Au environment (central, surface, staple) and columns for the 6s, 6p, and 5d electron counts derived from the projected l‑DOS.
Both files must follow the exact format and column names specified in the workflow steps.

## Assets

- Au25(SCH2CH2Ph)18- crystal structure (CCDC 654133): CCDC entry 654133; also available from Supporting Information of Zhu et al., J. Am. Chem. Soc. 2008, 130, 5883 (DOI: 10.1021/ja800805b)
- FEFF8 EXAFS and electronic structure code: https://github.com/feff-project/feff or the Demeter (Athena/Artemis) package (http://bruceravel.github.io/demeter/)

## Workflow steps

### Step 1: FEFF8 EXAFS simulation – Au–Au shell peak positions
- Role: scored (load-bearing)
- Action: Using FEFF8 and the published Au25(SCH2CH2Ph)18− crystal structure (CCDC 654133), compute the k³‑weighted Fourier‑transformed EXAFS spectrum. Extract the R‑space peak positions (in Å) corresponding to the three distinct Au–Au coordination shells: (Au–Au)₁ (short), (Au–Au)₂ (mid), and (Au–Au)₃ (long). Write the three peak positions to a JSON file.
- Output file: `/app/outputs/simulated_exafs_peaks.json`
- Format: json
- Contract: {"(Au-Au)1_peak_R": <float, Å>, "(Au-Au)2_peak_R": <float, Å>, "(Au-Au)3_peak_R": <float, Å>}
- Scoring: scored by hidden verifier

### Step 2: Site‑specific local density of states (l‑DOS) electron counts
- Role: scored (load-bearing)
- Action: Using FEFF8 and the same crystal structure, compute the angular‑momentum‑projected density of states (l‑DOS) for each unique Au site type: central, surface, and staple. Extract the integrated 6s, 6p, and 5d electron counts for each site and write them to a CSV file.
- Output file: `/app/outputs/site_specific_l_dos.csv`
- Format: csv
- Contract: columns: site (one of: central, surface, staple), s_count (float), p_count (float), d_count (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulated_exafs_peaks.json`
- `/app/outputs/site_specific_l_dos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulated_exafs_peaks.json
- path: `/app/outputs/simulated_exafs_peaks.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The three Au–Au peak positions extracted from the simulated FT‑EXAFS spectrum. The checker recomputes the reference peaks from the crystal structure with FEFF8 and compares the agent’s reported values within a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `(Au-Au)1_peak_R`: float (Å)
    - `(Au-Au)2_peak_R`: float (Å)
    - `(Au-Au)3_peak_R`: float (Å)

### site_specific_l_dos.csv
- path: `/app/outputs/site_specific_l_dos.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with one row per Au site type. The checker recomputes the site‑specific l‑DOS electron counts with FEFF8 and compares the agent’s reported values within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `site`, `s_count`, `d_count`, `p_count`

Notes: The experimental EXAFS data fitting and refinement stages are excluded because raw synchrotron data are not publicly available. The task is scoped to the computational validation via FEFF8 simulations, which use only public inputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulated_exafs_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "(Au-Au)1_peak_R": "float (Å)",
          "(Au-Au)2_peak_R": "float (Å)",
          "(Au-Au)3_peak_R": "float (Å)"
        }
      },
      "description": "The three Au–Au peak positions extracted from the simulated FT‑EXAFS spectrum. The checker recomputes the reference peaks from the crystal structure with FEFF8 and compares the agent’s reported values within a hidden tolerance."
    },
    {
      "file": "site_specific_l_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "s_count",
          "d_count",
          "p_count"
        ]
      },
      "description": "CSV file with one row per Au site type. The checker recomputes the site‑specific l‑DOS electron counts with FEFF8 and compares the agent’s reported values within a hidden tolerance."
    }
  ],
  "notes": "The experimental EXAFS data fitting and refinement stages are excluded because raw synchrotron data are not publicly available. The task is scoped to the computational validation via FEFF8 simulations, which use only public inputs."
}
```

## How you are scored
A hidden verifier independently reruns FEFF8 with the same crystal structure (CCDC 654133) and default parameters. It recomputes the k³‑weighted EXAFS Fourier transform and locates the three Au–Au peaks; your reported peak positions are compared against this reference. Separately, the verifier recomputes the site‑specific l‑DOS and extracts the 6s, 6p, and 5d electron counts, then compares them to your submitted values. Each artifact is scored individually: full credit is given when the deviation from the reference is within a predefined tolerance, and credit decays continuously for larger deviations. The final reward is a weighted average of the two stage scores (with the EXAFS peaks carrying the highest weight). Only the exact output files and formats described in the workflow are evaluated; no other files contribute to the score.
