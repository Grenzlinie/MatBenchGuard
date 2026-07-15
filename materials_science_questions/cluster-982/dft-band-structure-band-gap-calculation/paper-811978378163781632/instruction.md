# DFT Band Gap Calculation of a Thermoelectric Arsenide

## Problem background
Thermoelectric materials can directly convert heat into electricity, making them attractive for waste-heat recovery and cooling applications. The best thermoelectrics are narrow-gap semiconductors made from heavy elements, with complex crystal structures that help lower the thermal conductivity. Electronic structure calculations, particularly the density of states (DOS) and band gap, are fundamental to understanding whether a compound is a good thermoelectric candidate. This task targets an arsenide with a complex cubic structure—a new thermoelectric candidate—by computing its electronic DOS and band gap from first principles.

## Approach
The electronic structure of the ordered compound will be treated with density functional theory (DFT) using the local density approximation (LDA). Because the experimental crystal structure has a mixed Ge/As site, a fully ordered model must be constructed: the high‑symmetry cubic cell (space group Im‑3m, a = 8.73180 Å) is reduced to rhombohedral symmetry (R‑3m) to assign Ge and As to distinct sites, while preserving the overall stoichiometry and lattice vectors. A plane‑wave DFT code (such as Quantum ESPRESSO) will then self‑consistently solve the Kohn–Sham equations for this ordered structure, followed by a density‑of‑states calculation on a fine k‑point mesh. From the resulting DOS, the band gap will be extracted as the energy interval where the DOS vanishes at the Fermi level.

## Reproduction target
Compute the total density of states of the ordered R‑3m model and save it as a two‑column file (`dos.dat`) covering at least the energy range −5 eV to +5 eV relative to the Fermi level (column 1: energy in eV, column 2: DOS in states/eV). From this DOS, determine the band gap—the energy difference between the highest occupied state and the lowest unoccupied state—and write that single number (in eV) to `band_gap.txt`.

## Assets

- Quantum ESPRESSO (or any open-source plane-wave DFT code that supports LDA): https://www.quantum-espresso.org/
- LDA pseudopotentials for Re, Ge, As: https://www.materialscloud.org/discover/sssp/table/efficiency
- Python scientific stack (ase, spglib, numpy, matplotlib): ase spglib numpy matplotlib

## Workflow steps

### Step 1: Prepare ordered structural model
- Role: process
- Action: Using the published crystallographic data (space group Im-3m, a = 8.73180 Å, atomic positions Re on 12e (0.3413, 0, 0), As1 on 12d (1/4, 0, 1/2), E2 on 16f (0.1663, 0.1663, 0.1663) with 0.25 Ge / 0.75 As occupancy), construct an ordered structural model for DFT. Reduce symmetry from Im-3m to R-3m to allow full Ge/As ordering: in the primitive rhombohedral cell, assign Ge to the 2-fold site that derives from the 16f position and As to the 6-fold site. Output a structure file (e.g., POSCAR or CIF) describing the ordered R-3m supercell (or primitive cell containing 2 formula units). Ensure the lattice vectors and atomic coordinates are consistent with the reported cubic lattice constant.
- Evidence: `/app/outputs/ordered_structure.cif`

### Step 2: DFT SCF calculation and DOS generation
- Role: scored (load-bearing)
- Action: Perform a self-consistent field (SCF) calculation using the LDA functional within a plane-wave code (e.g., Quantum ESPRESSO) on the ordered structural model from step01. After convergence, compute the total density of states (DOS) on a fine k-point grid, aligned with the Fermi level. Write the DOS to /app/outputs/dos.dat as two columns: energy (eV relative to Fermi level) and DOS (states/eV). Ensure the energy range covers at least −5 eV to +5 eV.
- Output file: `/app/outputs/dos.dat`
- Format: txt
- Contract: Two-column plain text: energy (eV), DOS (states/eV). Energy range must cover at least −5 eV to +5 eV relative to Fermi level.
- Scoring: scored by hidden verifier

### Step 3: Compute band gap from DOS
- Role: scored
- Action: From the computed DOS in dos.dat, determine the band gap by identifying the energy difference between the highest occupied and lowest unoccupied states (the energy window where DOS goes to zero at the Fermi level). Write the band gap value as a single floating-point number (in eV) to /app/outputs/band_gap.txt.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: A single line containing a floating-point number (the band gap in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos.dat`
- `/app/outputs/band_gap.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos.dat
- path: `/app/outputs/dos.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Total density of states as a function of energy, relative to the Fermi level. Used to verify the existence of a band gap and to recompute the band gap for scoring.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `dos`
  - `units`:
    - `energy`: eV
    - `dos`: states/eV

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: The band gap value in eV, as extracted by the agent from the DOS. The checker recomputes the gap from dos.dat and compares it to the hidden reference; meeting or exceeding the reference earns full credit.
- schema:
  - `type`: text
  - `units`: eV

Notes: The hidden checker recomputes the band gap from dos.dat and scores it against a paper‑derived reference with a tolerance that absorbs legitimate code/functional spread. The structural audit confirms a gap region exists around the Fermi level. No wett‑lab data or proprietary software is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "dos"
        ],
        "units": {
          "energy": "eV",
          "dos": "states/eV"
        }
      },
      "description": "Total density of states as a function of energy, relative to the Fermi level. Used to verify the existence of a band gap and to recompute the band gap for scoring."
    },
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "units": "eV"
      },
      "description": "The band gap value in eV, as extracted by the agent from the DOS. The checker recomputes the gap from dos.dat and compares it to the hidden reference; meeting or exceeding the reference earns full credit."
    }
  ],
  "notes": "The hidden checker recomputes the band gap from dos.dat and scores it against a paper‑derived reference with a tolerance that absorbs legitimate code/functional spread. The structural audit confirms a gap region exists around the Fermi level. No wett‑lab data or proprietary software is required."
}
```

## How you are scored
A hidden verifier will inspect your output files independently. For `dos.dat`, it checks that the file is correctly formatted, covers the required energy range, and exhibits a gap (a region of zero DOS) at the Fermi level. It then recomputes the band gap from your DOS and compares it to a hidden reference value; the scorer rewards results that are physically correct and compatible with an acceptable tolerance. A separate weight is assigned to the extracted band gap in `band_gap.txt`. The verifier combines these checks into a single reward score, so simply reporting a number without a physically consistent DOS will not earn full credit.
