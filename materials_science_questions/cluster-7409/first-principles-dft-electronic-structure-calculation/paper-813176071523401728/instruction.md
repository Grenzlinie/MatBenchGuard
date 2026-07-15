# DFT band gap calculation for pure and Mg-doped anatase TiO2

## Problem background
Titanium dioxide (TiO2) in the anatase phase is a widely studied semiconductor photocatalyst. Replacing a small fraction of titanium atoms with magnesium (Mg) can alter the electronic structure, potentially narrowing the band gap and shifting absorption toward the visible region. Understanding how much the band gap changes at different doping levels is important for designing improved photocatalysts. This task focuses on the computational determination of the electronic band gap of pure and Mg-substituted anatase TiO2 using density functional theory (DFT).

## Approach
The electronic structure is modelled by constructing anatase supercells where a single Mg atom substitutes a Ti atom to achieve specific doping concentrations: 0 at.% (pure), 2 at.%, 5.1 at.%, and 6.2 at.%. The calculations are performed with Quantum ESPRESSO employing the LDA+U exchange-correlation functional with an on-site Hubbard correction (U = 8 eV). The procedure involves three stages: (1) building the supercells with the correct lattice parameters, (2) relaxing the atomic positions of all structures, and (3) computing the density of states (DOS) to extract the band gap energy for each composition. The same pseudopotentials and plane-wave cutoff (32 Ryd) are used throughout; pseudopotentials for Ti, O, and Mg are taken from the Quantum ESPRESSO library.

## Reproduction target
Compute the DFT band gap energies for pure anatase and Mg-doped anatase with Mg substituting Ti at the concentrations listed above (0, 2, 5.1, 6.2 at.%). Report the results in a CSV file named `band_gaps.csv` with columns `sample` (the identifier: 'pure', '2at%', '5.1at%', '6.2at%') and `band_gap_eV` (the calculated band gap in eV).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (Ti.pz-nd-rrkjus.UPF, O.pz-n-rrkjus.UPF, Mg.pz-n-vbc.UPF): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Construct supercells
- Role: process
- Action: Construct anatase supercells of sizes 1x1x4, 1x1x5, and 1x1x12 (unit cell a=b=3.785 Å, c=9.514 Å). For doping, substitute one Mg at a Ti site in appropriate cells to achieve concentrations: 2 at.% (1/48 Ti replaced), 5.1 at.% (1/20), and 6.2 at.% (1/16). Also create a pure anatase supercell.
- Evidence: `/app/outputs/supercells_info.txt`

### Step 2: DFT geometry optimization
- Role: process
- Action: Using Quantum ESPRESSO with the pseudopotentials (Ti.pz-nd-rrkjus.UPF, O.pz-n-rrkjus.UPF, Mg.pz-n-vbc.UPF), plane-wave cutoff 32 Ryd, LDA+U with U=8 eV, relax the atomic positions of each supercell (pure and doped). Save the optimized coordinates.
- Evidence: `/app/outputs/optimization_summary.txt`

### Step 3: Compute band gaps
- Role: scored (load-bearing)
- Action: From the relaxed structures, perform self-consistent and non-self-consistent calculations to obtain the density of states (DOS). Extract the band gap energy for each system. Output the band gaps to band_gaps.csv with columns 'sample' and 'band_gap_eV'.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: sample (string): identifier ('pure', '2at%', '5.1at%', '6.2at%'), band_gap_eV (float): computed band gap in eV.
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
- target_policy: exact_match
- description: Computed DFT band gap energies for pure anatase and Mg-doped anatase at 2 at.%, 5.1 at.%, and 6.2 at.% doping levels.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

Notes: The checker reads this CSV, extracts the four band gap values, and compares each to the paper-reported values with an absolute tolerance of ±0.1 eV. All four must pass; reward is proportional to number of matches.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Computed DFT band gap energies for pure anatase and Mg-doped anatase at 2 at.%, 5.1 at.%, and 6.2 at.% doping levels."
    }
  ],
  "notes": "The checker reads this CSV, extracts the four band gap values, and compares each to the paper-reported values with an absolute tolerance of ±0.1 eV. All four must pass; reward is proportional to number of matches."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently examines each scored artifact. For the main artifact `band_gaps.csv`, the verifier extracts the band gap value for each doping level and compares it against a hidden reference. The final reward is proportional to the number of entries that meet the verification criteria. The verifier does not require any additional knowledge beyond the public workflow description; accurate values can only be obtained by correctly executing the DFT pipeline.
