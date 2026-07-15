# FLAPW-LDA Band Structure and Oscillator Strength Screening of Metal Silicides

## Problem background
Semiconducting metal silicides are candidates for silicon-based light-emitting materials. The light-emission capability of a compound is related to the oscillator strength of optical transitions between valence and conduction states near the band gap. This task screens twelve metal silicides by computing their electronic band structure and oscillator strengths from first principles, using full-potential linearized augmented plane-wave (FLAPW) calculations within the local density approximation (LDA).

## Approach
The approach is a computational high-throughput screening workflow. For each of the twelve silicides, you will obtain the crystal structure, perform self-consistent FLAPW-LDA density-functional theory (DFT) calculations to obtain the ground-state electronic structure, analyze the band structure to extract the band gap (energy, type, and location of valence-band maximum and conduction-band minimum), and compute the electric-dipole oscillator strength for selected direct transitions near the gap. Because LDA systematically underestimates band gaps, some materials that are experimental semiconductors may appear metallic in the calculation; this is expected and should be reported as Type='Metal'. The final output aggregates all computed results into a single tabular file (see Workflow steps).

## Reproduction target
Produce a CSV file `table_ii_results.csv` that reports the computed electronic properties for all twelve silicides: β-FeSi2, CrSi2, ReSi2, Ru2Si3, OsSi, OsSi2, MnSi, LaSi2, Ir3Si5, Mg2Si, Ca2Si, BaSi2. The file must follow the column layout described in the Output Contract (Silicide, Gap, Type, VBM, CBM, kpoint, Transition_energy, Oscillator_strength). For metallic compounds only the Silicide and Type='Metal' are required; other fields must be empty. For materials where no oscillator strength was evaluated (e.g., metals, Mg2Si), the oscillator-strength columns may be left empty. Multiple rows per silicide are allowed when more than one k-point transition is computed. The goal is to faithfully compute these quantities using the FLAPW-LDA workflow described in the Workflow steps, not to guess or look up previously reported numbers.

## Assets

- Crystallography Open Database (COD): https://www.crystallography.net/cod/
- ELK FLAPW code: https://elk.sourceforge.net/
- Python scientific stack: numpy, pandas

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: For each of the 12 semiconducting metal silicides (β-FeSi2, CrSi2, ReSi2, Ru2Si3, OsSi, OsSi2, MnSi, LaSi2, Ir3Si5, Mg2Si, Ca2Si, BaSi2), obtain the crystal structure (space group, lattice parameters, atomic positions) from the Crystallography Open Database or equivalent public source. Write a summary file listing the structures used.
- Evidence: `/app/outputs/crystal_structures_summary.txt`

### Step 2: Run DFT FLAPW-LDA calculations
- Role: process
- Action: For each silicide, perform self-consistent field (SCF) FLAPW-LDA calculations using an open-source FLAPW code (e.g., ELK) to obtain the ground-state charge density, eigenenergies, and wavefunctions. Converge total energy using suitable parameters. Save the band structure data on a fine k-point grid along high-symmetry lines.
- Evidence: `/app/outputs/dft_calculation_log.txt`

### Step 3: Analyze band structure and determine gap properties
- Role: process
- Action: Post-process the band structure of each silicide to extract: band gap energy (eV), gap type (direct/indirect/metal), valence band maximum (VBM) and conduction band minimum (CBM) k-point location(s). Record these for each material in a structured file.
- Evidence: `/app/outputs/band_gap_analysis.json`

### Step 4: Compute oscillator strengths
- Role: process
- Action: Compute the electric-dipole oscillator strengths for direct transitions at the following k‑points for each silicide: β‑FeSi₂ at Y and (Γ‑Z)/4; CrSi₂ at L and M; Ru₂Si₃ at Γ; OsSi at X; OsSi₂ at Γ and Y; Ir₃Si₅ at (Y‑C)/2 and (Γ‑Y)/2; Ca₂Si at Γ. For Mg₂Si and metallic compounds (ReSi₂, MnSi, LaSi₂, BaSi₂) no oscillator strengths are required; this step may be skipped or produce empty entries. Store raw results in a structured file.
- Evidence: `/app/outputs/oscillator_strengths_raw.json`

### Step 5: Compile final results table
- Role: scored (load-bearing)
- Action: Combine all computed band gap properties and oscillator strengths into a CSV file with columns: Silicide, Gap, Type, VBM, CBM, kpoint, Transition_energy, Oscillator_strength. The table must include all 12 silicides exactly as required, handling metallic entries (only Silicide and Type='Metal') and missing oscillator strength entries appropriately.
- Output file: `/app/outputs/table_ii_results.csv`
- Format: csv
- Contract: Columns: Silicide (string), Gap (float or empty), Type (string: Direct/Indirect/Metal), VBM (string, or empty), CBM (string, or empty), kpoint (string, or empty), Transition_energy (float, eV, or empty), Oscillator_strength (float, or empty). Multiple rows per silicide for multiple k-point transitions are allowed.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_ii_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_ii_results.csv
- path: `/app/outputs/table_ii_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: A CSV file reporting the band gap properties and oscillator strengths for all 12 semiconducting metal silicides as computed by FLAPW‑LDA. For metallic entries only Silicide and Type='Metal' are required; other fields empty. Multiple rows per silicide are allowed for multiple k‑point transitions. The checker compares each non‑empty entry against hidden reference values with defined tolerances, and checks exact match for string labels (Type, VBM, CBM, kpoint).
- schema:
  - `type`: table
  - `required_columns`: `Silicide`, `Gap`, `Type`, `VBM`, `CBM`, `kpoint`, `Transition_energy`, `Oscillator_strength`

Notes: The verifier reads the agent's CSV and compares every non‑empty numerical field against a hidden reference (derived from the paper's Table II) with appropriate tolerances; Type, VBM, CBM and kpoint labels are checked for exact match. The reward is based on the fraction of correctly matched entries, normalised across all expected rows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_ii_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Silicide",
          "Gap",
          "Type",
          "VBM",
          "CBM",
          "kpoint",
          "Transition_energy",
          "Oscillator_strength"
        ]
      },
      "description": "A CSV file reporting the band gap properties and oscillator strengths for all 12 semiconducting metal silicides as computed by FLAPW‑LDA. For metallic entries only Silicide and Type='Metal' are required; other fields empty. Multiple rows per silicide are allowed for multiple k‑point transitions. The checker compares each non‑empty entry against hidden reference values with defined tolerances, and checks exact match for string labels (Type, VBM, CBM, kpoint)."
    }
  ],
  "notes": "The verifier reads the agent's CSV and compares every non‑empty numerical field against a hidden reference (derived from the paper's Table II) with appropriate tolerances; Type, VBM, CBM and kpoint labels are checked for exact match. The reward is based on the fraction of correctly matched entries, normalised across all expected rows."
}
```

## How you are scored
Your solution is scored by a hidden verifier that inspects the final `/app/outputs/table_ii_results.csv`. For each non-empty entry, numerical fields (Gap, Transition_energy, Oscillator_strength) are compared against hidden reference values using tolerances that account for the typical spread of these calculations; categorical fields (Type, VBM, CBM, kpoint labels) must match exactly. The reward is the fraction of correctly matched entries, normalized across all expected rows. Intermediate evidence files (crystal_structures_summary.txt, dft_calculation_log.txt, band_gap_analysis.json, oscillator_strengths_raw.json) must be present to document that you actually executed the workflow, but they are not directly scored. Only the final table contributes to the reward.
