# DFT Band Gap Calculation for SbBiI3 Alloys

## Problem background
Sb_xBi_{1-x}I_3 alloys are wide-band-gap materials of interest for room-temperature gamma-ray detection. The fundamental band-gap energy changes with the Sb fraction x. One way to predict this composition-dependent trend is through electronic-structure calculations using density functional theory (DFT). A previous study performed such calculations and found that the computed band-gap energies qualitatively followed the experimental measurements but exhibited a roughly composition-independent offset. This task isolates the purely theoretical prediction: you are asked to compute, from first principles, the unshifted DFT band-gap energies for a series of Sb_xBi_{1-x}I_3 compositions before any empirical correction. Your results will demonstrate how the band gap evolves as Bi atoms are replaced by Sb.

## Approach
The method is based on plane-wave density functional theory with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation (GGA) for exchange–correlation. For each composition, you will first relax the crystal structure to its equilibrium geometry, then calculate the electronic band structure along high-symmetry directions in the Brillouin zone. The fundamental gap is obtained as the energy difference between the valence band maximum and the conduction band minimum. The workflow will be carried out using Quantum ESPRESSO, an open-source DFT code, and appropriate pseudopotentials for Sb, Bi, and I. This computational protocol mirrors the one used in the literature and is expected to reproduce the DFT band-gap trend of the Sb_xBi_{1-x}I_3 system.

## Reproduction target
Produce a CSV file, band_gaps.csv, containing the computed fundamental band-gap energies (in eV) for six alloy compositions: x = 0.0, 0.1, 0.3, 0.5, 0.9, and 1.0. The file must have columns 'composition' and 'band_gap_eV', with one row per x value. The band gaps should decrease monotonically as the Sb fraction x increases from 0 (pure BiI3) to 1 (pure SbI3). The verifier will compare your computed values against a hidden reference that represents the raw DFT band gaps from the original study, and it will also check the monotonic trend. No empirical shift or experimental correction should be applied.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE-GGA pseudopotentials for Sb, Bi, I: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Lattice optimization
- Role: process
- Action: For each composition x in {0.0,0.1,0.3,0.5,0.9,1.0}, perform total energy minimization using a plane-wave DFT code (Quantum ESPRESSO) with PBE-GGA to obtain equilibrium lattice parameters.
- Evidence: `/app/outputs/lattice_constants.csv`

### Step 2: Band structure calculation
- Role: process
- Action: For each optimized structure, run a self-consistent field (SCF) calculation followed by a non-SCF band structure calculation along high-symmetry paths in the Brillouin zone to obtain eigenvalues.
- Evidence: `/app/outputs/scf_summary.txt`

### Step 3: Band gap extraction
- Role: scored (load-bearing)
- Action: Identify the valence band maximum (VBM) and conduction band minimum (CBM) from the band structure results to determine the fundamental band-gap energy for each composition. Save a CSV file with columns composition and band_gap_eV.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: Two columns: 'composition' (float, allowed values 0.0,0.1,0.3,0.5,0.9,1.0) and 'band_gap_eV' (float, unit eV). One row per composition.
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
- target_policy: threshold_or_better
- description: Fundamental band-gap energies for Sb_xBi_{1-x}I_3 alloys at six compositions. The band gaps should monotonically decrease with increasing Sb fraction.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

Notes: Scoring will evaluate the accuracy of the reported band-gap energies and the expected monotonic trend. No optical absorption calculation is required.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Fundamental band-gap energies for Sb_xBi_{1-x}I_3 alloys at six compositions. The band gaps should monotonically decrease with increasing Sb fraction."
    }
  ],
  "notes": "Scoring will evaluate the accuracy of the reported band-gap energies and the expected monotonic trend. No optical absorption calculation is required."
}
```

## How you are scored
A hidden verifier examines the band_gaps.csv file you submit. It first verifies the file format, required columns, and data types. Then it scores your reported band_gap_eV values by comparing them to a hidden reference derived from the paper's unshifted DFT results. It also evaluates whether the band gaps strictly decrease as x increases. The scoring rule rewards both quantitative agreement with the reference and correct gap ordering. Additional evidence files (lattice_constants.csv, scf_summary.txt) are inspected to confirm that the intermediate computational steps were carried out, but the primary score comes from the band-gap values and their trend. Importantly, the verifier expects that the numbers you report originate from an actual DFT execution, not from quoting external results.
