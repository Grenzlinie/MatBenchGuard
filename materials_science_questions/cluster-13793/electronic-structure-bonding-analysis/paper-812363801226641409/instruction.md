# DFT Structural Relaxation of Li_xMPn4 Electrode Materials for Bond-Breathing Analysis

## Problem background
Ternary transition metal pnictides Li_xMPn_4 (M=Ti,V; Pn=P,As) are promising negative electrode materials for Li-ion batteries. They adopt a cubic fcc-based structure and can accommodate large variations in lithium content (x) during charge/discharge while exhibiting only modest (<5%) cell-volume changes. Understanding the structural origin of this reversible capacity is essential for designing stable anodes. First-principles structural relaxations reveal how the cubic lattice parameter a and the M–Pn bond distance evolve as a function of lithium composition, providing direct insight into the redox-induced breathing mechanism of the (MPn_4)^{x-} tetrahedral entities.

## Approach
We use density functional theory (DFT) with the GGA-PBE exchange-correlation functional to perform full ionic and cell-shape relaxations of Li_xMPn_4 systems. Starting from the experimentally reported lattice constants and the fcc-based atomic positions (Pn at (0,0,0), M at (1/4,1/4,1/4)), initial structures are built for each lithium composition x = 3, 7, 9, 11 with the five Li distributions (0,3), (4,3), (0,7), (2,7), and (4,7). For the (2,7) distribution a 2×2×2 supercell is required. Each structure is relaxed without any symmetry constraints (P1) using an open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) with pseudopotentials suitable for GGA-PBE. After convergence the cubic lattice parameter a is extracted from the final cell vectors (verifying a≈b≈c and orthogonal angles) and the average M–Pn bond length is computed from the M position and its four nearest Pn neighbours. All results are collected into a single structured file for comparison across compositions and chemical families.

## Reproduction target
Produce a CSV file `relaxed_parameters.csv` that contains the relaxed lattice parameter a (in Å) and the average M–Pn bond length (in Å) for every combination of the three chemical systems (TiP, VP, VAs), the four lithium compositions (3, 7, 9, 11), and the five Li distributions ((0,3), (4,3), (0,7), (2,7), (4,7)). The file must have one row per calculation with the columns `system`, `composition_x`, `distribution`, `relaxed_a_Angstrom`, `MPn_bond_Angstrom`. For the (2,7) supercell, report the volume‑averaged unit‑cell parameter and the averaged M–Pn bond distance.

## Assets

- Quantum ESPRESSO (or another open-source plane-wave DFT code): https://www.quantum-espresso.org/
- GBRV pseudopotentials (or equivalent SSSP library): https://www.physics.rutgers.edu/gbrv/

## Workflow steps

### Step 1: Generate initial structures for all Li_xMPn_4 compositions and Li distributions
- Role: process
- Action: Construct initial crystal structures for Li_xTiP_4, Li_xVP_4, and Li_xVAs_4 at lithium compositions x = 3, 7, 9, 11 using the five distinct Li distributions (0,3), (4,3), (0,7), (2,7), (4,7). Use the experimental lattice constants (TiP: 6.01 Å, VP: 5.995 Å, VAs: 6.16 Å) and the fcc‑based space‑group coordinates (Pn at (0,0,0), M at (1/4,1/4,1/4)) placing Li in the specified octahedral and tetrahedral sites. For the (2,7) distribution, use a 2×2×2 supercell. Do NOT include implementation tuning parameters (k‑point mesh, energy cutoff, convergence criteria). The output is a set of DFT input files suitable for the chosen open‑source plane‑wave code.
- Evidence: `/app/outputs/structure_files.tar.gz`

### Step 2: DFT relaxations and extraction of a and M–Pn bond lengths
- Role: scored (load-bearing)
- Action: For every structure generated in the previous step, run a full ionic and cell‑shape relaxation (P1 symmetry, no constraints) using the DFT code with GGA‑PBE functional. After convergence, extract the relaxed cubic lattice parameter a (verifying a≈b≈c and orthogonal angles) and the average M–Pn bond distance (from the positions of M and the four nearest Pn atoms). Collect all results into a single CSV file.
- Output file: `/app/outputs/relaxed_parameters.csv`
- Format: csv
- Contract: Columns: system (string, one of TiP/VP/VAs), composition_x (integer, 3/7/9/11), distribution (string, e.g. '0,3' format), relaxed_a_Angstrom (float), MPn_bond_Angstrom (float). One row per calculation. For the (2,7) supercell, report the averaged unit‑cell parameter and the averaged M–Pn bond length.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_parameters.csv
- path: `/app/outputs/relaxed_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relaxed cubic lattice parameter a and M–Pn bond length for each Li_xMPn_4 composition and Li distribution. The checker compares these values to the paper's reported Table 2 within hidden tolerances and validates monotonic bond‑length trends and the a√3/4 geometrical relationship.
- schema:
  - `type`: table
  - `required_columns`: `system`, `composition_x`, `distribution`, `relaxed_a_Angstrom`, `MPn_bond_Angstrom`
  - `items`: object
  - `required`: object
  - `units`:
    - `relaxed_a_Angstrom`: Angstrom
    - `MPn_bond_Angstrom`: Angstrom

Notes: The agent must genuinely run DFT relaxations; the scored CSV is the only artifact that carries reward. The process step forces the generation of DFT input files, and the load‑bearing scored step requires the actual relaxations. The hidden checker validates structural trends besides absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "composition_x",
          "distribution",
          "relaxed_a_Angstrom",
          "MPn_bond_Angstrom"
        ],
        "items": {},
        "required": {},
        "units": {
          "relaxed_a_Angstrom": "Angstrom",
          "MPn_bond_Angstrom": "Angstrom"
        }
      },
      "description": "Relaxed cubic lattice parameter a and M–Pn bond length for each Li_xMPn_4 composition and Li distribution. The checker compares these values to the paper's reported Table 2 within hidden tolerances and validates monotonic bond‑length trends and the a√3/4 geometrical relationship."
    }
  ],
  "notes": "The agent must genuinely run DFT relaxations; the scored CSV is the only artifact that carries reward. The process step forces the generation of DFT input files, and the load‑bearing scored step requires the actual relaxations. The hidden checker validates structural trends besides absolute tolerances."
}
```

## How you are scored
A hidden verifier reads your `relaxed_parameters.csv`. It first validates that the file has the required columns and the correct number of rows. Then it compares each reported numerical value to a hidden reference derived from the original study. The comparison uses tolerances that account for typical run‑to‑run and code‑to‑code variations in DFT calculations. In addition, the verifier checks that the reported bond‑length values satisfy certain structural consistency requirements that follow from the geometry of the fcc lattice. The final reward (a float between 0 and 1) is a weighted combination of the accuracies across all rows, with larger weight given to the systems that are most diagnostic of the bonding mechanism. Simply reporting the published numbers without running the full DFT workflow will not yield a passing score under these hidden checks.
