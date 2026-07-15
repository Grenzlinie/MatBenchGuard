# DFT Band Structure Band Gap Calculation of Cs4[Ho26Cd7Se48]

## Problem background
Quaternary semiconducting chalcogenides have attracted attention for their ultralow thermal conductivity, making them candidates for thermoelectric applications. The compound Cs₄[Ho₂₆Cd₇Se₄₈] crystallizes in a tetragonal structure (space group I4₁/a) featuring a 3D framework assembled from [HoSe₆] and mixed-occupancy [MSe₆] (M = Ho/Cd) octahedra, and embedded closed-cavity polyanions. Understanding its electronic structure is essential for interpreting its optical properties and thermal transport. A key quantity is the direct band gap: the energy separation between the valence band maximum and conduction band minimum at the same k-point. This task computes that direct band gap via density functional theory (DFT) from the published crystal structure.

## Approach
The calculation follows a standard plane-wave pseudopotential DFT approach. Using the published crystal structure (CIF file for CCDC 2034252), you will construct a supercell or unit cell input suitable for a plane-wave DFT code (e.g., Quantum ESPRESSO or equivalent). The structure contains mixed Ho/Cd occupancy on several sites (M1–M4 with a 5:3 ratio), a distinct Cd site (Cd5), and additional Ho, Cs, and Se sites; you must map these to pseudopotentials. For the electronic exchange-correlation, use the PBE functional. Perform a self-consistent field (SCF) calculation to obtain the ground-state charge density. Then carry out a non-self-consistent band structure calculation along a standard high-symmetry k-point path for the tetragonal I4₁/a space group. From the resulting band structure, identify the valence band maximum (VBM) and conduction band minimum (CBM) that occur at the same k-point (a direct gap), and compute the energy difference in eV. You are free to choose the DFT code, pseudopotential library, and convergence parameters (k-point grid, plane-wave cutoff), but the workflow must be a plane-wave pseudopotential method with PBE functional.

## Reproduction target
Produce a single file, band_gap.txt, containing the computed direct band gap of Cs₄[Ho₂₆Cd₇Se₄₈] in electronvolts (eV). The value is obtained from a plane-wave pseudopotential DFT calculation using the published crystal structure (CCDC 2034252). The workflow includes preparing the DFT input from the CIF, running the SCF and band structure calculations, and extracting the direct gap as described in the Approach section. The output is a plain text file with one line containing the numeric gap value (e.g., a floating-point number).

## Assets

- Crystal structure (CIF) for Cs4[Ho26Cd7Se48] (CCDC 2034252): 10.1039/d0qi01240h
- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO, ABINIT, CASTEP): https://www.quantum-espresso.org
- Pseudopotential libraries (SSSP efficiency or JTH for QE, VASP PBE pseudopotentials): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare DFT input structure from CIF
- Role: process
- Action: Generate the DFT input file (e.g., POSCAR or QE scf input) from the published CIF (CCDC 2034252). Map the crystallographic sites: mixed-occupancy Ho/Cd sites (M1-M4 with 5:3 ratio), distinct Cd5 at 4b, and the Ho5-Ho8, Cs, Se sites. Select appropriate pseudopotentials for all elements.
- Evidence: `/app/outputs/input_structure.txt`

### Step 2: DFT SCF and band structure calculation
- Role: process
- Action: Perform a self-consistent field (SCF) calculation using a plane-wave basis set and PBE functional. Then run a non-self-consistent band structure calculation along a standard high-symmetry k-point path for the tetragonal I4_1/a space group. Ensure convergence with respect to k-point density and plane-wave energy cutoff. The exact code and parameters can be chosen by the solver, but must be a plane-wave pseudopotential approach.
- Evidence: `/app/outputs/band_structure.dat`

### Step 3: Extract direct band gap
- Role: scored
- Action: From the band structure output, locate the valence band maximum (VBM) and conduction band minimum (CBM) that share the same k-point (direct gap). Compute the energy difference (E_CBM - E_VBM) in eV. Write this single numeric value to band_gap.txt.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: A single line containing the floating-point value of the direct band gap in eV (e.g., 1.67).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Computed direct band gap of Cs4[Ho26Cd7Se48] in eV.
- schema:
  - `type`: text
  - `description`: The file contains a single line with the computed direct band gap in eV.

Notes: The computed band gap is method-dependent; the scoring accounts for expected spread from different plane-wave codes and pseudopotentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "The file contains a single line with the computed direct band gap in eV."
      },
      "description": "Computed direct band gap of Cs4[Ho26Cd7Se48] in eV."
    }
  ],
  "notes": "The computed band gap is method-dependent; the scoring accounts for expected spread from different plane-wave codes and pseudopotentials."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. The verifier reads band_gap.txt, parses the numeric value, and compares it to a reference value derived from the original study. If the absolute difference between your computed gap and the reference is within a predetermined tolerance, you receive a score of 1.0; otherwise 0.0. The tolerance is set to accommodate legitimate variation due to the choice of DFT code and pseudopotentials, but it is not disclosed. The process steps (preparing the input structure and running the DFT calculations) are not directly scored but are essential to produce the correct output. There is no partial credit. The verifier does not inspect the input_structure.txt or band_structure.dat; only band_gap.txt is scored.
