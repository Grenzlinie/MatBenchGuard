# DFT‑Optimized Lattice Parameters of Proton‑Inserted LaFeO₃ and LaCrO₃

## Problem background
Perovskite-type oxides LaFeO₃ and LaCrO₃ can incorporate hydrogen as protons (H⁺) that bind to lattice oxygen atoms. This hydrogen‑uptake ability makes them candidate anode materials for nickel–metal hydride (Ni/MH) batteries. This task uses density‑functional theory (DFT) to determine the relaxed crystal structures of these oxides when different amounts of protons are inserted — 0, 3, 6, 9, and 12 H⁺ per formula unit — and to assess whether a stable structure is obtained in each case. The central quantities to compute are the optimized lattice parameters (a, b, c) and the unit‑cell volume as a function of the proton content.

## Approach
The crystal structures of orthorhombic LaFeO₃ and LaCrO₃ are taken from published experimental lattice parameters. Protons (H⁺) are placed near lattice oxygen atoms in the unit cell (or supercell) to create hydride‑like insertion phases with 3, 6, 9, and 12 H⁺ per formula unit. For each composition, a spin‑unpolarized DFT geometry optimization is performed using the PBE generalized‑gradient approximation, ultrasoft pseudopotentials, a plane‑wave basis with a 340 eV cutoff, and a 6×6×6 Monkhorst–Pack k‑point grid. The cell parameters and atomic positions are relaxed to minimize the total energy. After convergence, the optimized lattice constants a, b, c and the unit‑cell volume are recorded. For the composition with 12 H⁺ in LaFeO₃, the relaxation is attempted to see whether a stable equilibrium can be reached.

## Reproduction target
Perform DFT geometry optimizations for LaFeO₃ with 0, 3, 6, and 9 inserted H⁺ per formula unit, and for LaCrO₃ with 0, 3, and 6 inserted H⁺, using Quantum ESPRESSO with the PBE functional, ultrasoft pseudopotentials, a 340 eV plane‑wave cutoff, a 6×6×6 k‑point grid, and non‑spin‑polarized settings. For LaFeO₃ with 12 H⁺, attempt the relaxation. From the converged calculations extract the optimized lattice parameters a, b, c (Å) and the unit‑cell volume (Å³). For each system and proton count, record whether the geometry relaxation converged to a stable structure (true) or not (false). Compile the results into a CSV file with columns: system, n, a, b, c, volume, converged.

## Assets

- LaFeO3 crystal structure (Sangaletti 2001): https://doi.org/10.1016/S0955-2219(00)00204-5
- LaCrO3 crystal structure (Oikawa 2000): https://doi.org/10.1006/jssc.2000.8753
- Quantum ESPRESSO (open‑source DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE, ultrasoft): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Prepare input structures
- Role: process
- Action: Build initial atomic structures for orthorhombic LaFeO₃ (Pbnm) and LaCrO₃ unit cells using published experimental lattice parameters (Sangaletti 2001, Oikawa 2000). Construct supercells with 3, 6, 9, and 12 H⁺ ions per formula unit inserted near lattice oxygen atoms. Output initial structure files in Quantum ESPRESSO input format.
- Evidence: `/app/outputs/initial_structures.tar.gz`

### Step 2: Perform DFT geometry optimizations
- Role: process
- Action: For each prepared structure, run DFT geometry relaxation using Quantum ESPRESSO with PBE functional, ultrasoft pseudopotentials (La, Fe, Cr, O), plane‑wave cutoff 340 eV, 6×6×6 k‑point grid, non‑spin‑polarized. Relax cell parameters and atomic positions. For LaFeO₃ n=12, attempt relaxation but record whether it fails to reach a stable equilibrium.
- Evidence: `/app/outputs/relaxed_geometries.tar.gz`

### Step 3: Compile lattice parameters and volumes
- Role: scored (load-bearing)
- Action: Extract the final relaxed lattice constants a, b, c (Å) and unit‑cell volume (Å³) from the converged DFT outputs. For each system (LaFeO₃ n=0,3,6,9,12; LaCrO₃ n=0,3,6) record whether the relaxation converged (true/false). Write the compiled results to relaxed_lattice_parameters.csv.
- Output file: `/app/outputs/relaxed_lattice_parameters.csv`
- Format: csv
- Contract: csv table with columns: system (LaFeO3 or LaCrO3), n (integer, number of H+ per formula unit: 0,3,6,9,12), a (float, Å), b (float, Å), c (float, Å), volume (float, Å³), converged (boolean; true if relaxation converged, false for LaFeO3 n=12). For n=12 LaFeO3, converged=false and a,b,c,volume may be empty or NaN.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_lattice_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_lattice_parameters.csv
- path: `/app/outputs/relaxed_lattice_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice parameters for LaFeO₃ and LaCrO₃ with 0,3,6,9,12 inserted H⁺ ions per formula unit. Values are compared against the paper‑reported results with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `system`, `n`, `a`, `b`, `c`, `volume`, `converged`
  - `units`:
    - `a`: Å
    - `b`: Å
    - `c`: Å
    - `volume`: Å³
    - `converged`: boolean

Notes: The primary scored artifact is the final CSV of relaxed lattice parameters and convergence flags. All intermediate DFT outputs (initial structures, relaxed geometries) are supporting evidence.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_lattice_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "n",
          "a",
          "b",
          "c",
          "volume",
          "converged"
        ],
        "units": {
          "a": "Å",
          "b": "Å",
          "c": "Å",
          "volume": "Å³",
          "converged": "boolean"
        }
      },
      "description": "Optimized lattice parameters for LaFeO₃ and LaCrO₃ with 0,3,6,9,12 inserted H⁺ ions per formula unit. Values are compared against the paper‑reported results with tolerance."
    }
  ],
  "notes": "The primary scored artifact is the final CSV of relaxed lattice parameters and convergence flags. All intermediate DFT outputs (initial structures, relaxed geometries) are supporting evidence."
}
```

## How you are scored
A hidden verifier will independently check the relaxed_lattice_parameters.csv file you produce. It compares each reported lattice constant and volume against a hidden reference that represents the expected converged DFT results for each composition, using tolerances that account for differences between DFT codes and computational settings. It also verifies that the convergence flags are correct. Your reward is based on how many entries match within tolerance, scaled by the number of rows. The final reward is a single float between 0 and 1. Reporting the hidden reference values without running the calculations will not pass.
