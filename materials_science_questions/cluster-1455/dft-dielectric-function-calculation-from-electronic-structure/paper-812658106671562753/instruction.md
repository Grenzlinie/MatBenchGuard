# DFT Dielectric and Electronic Properties of Mixed-Halide Perovskites

## Problem background
Inorganic cesium lead halide perovskites, particularly the black-phase γ-CsPbI₃, are promising for optoelectronics but are unstable at room temperature. Partial substitution of iodide by bromide is believed to stabilize the black phase and tune electronic and optical properties. Understanding how the lattice volume, cohesive energy, band gap, and dielectric response change with bromide content is essential for designing stable, efficient perovskite solar cells. This task requires computing these properties for γ-CsPb(I₁₋ₓBrₓ)₃ across the full composition range using density functional theory.

## Approach
Use plane-wave pseudopotential density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation to model the mixed-halide perovskite series γ-CsPb(I₁₋ₓBrₓ)₃ for x = 0, 0.17, 0.33, 0.5, 0.67, 0.83, and 1. Starting from the orthorhombic black-phase crystal structure, generate supercells for each Br concentration, relax both atomic positions and lattice vectors, then compute the electronic band structure without spin-orbit coupling and the frequency-dependent dielectric function. Extract the equilibrium volume, the total energy, the direct band gap at the Γ point, and the static dielectric constant ε₁(ω→0). Compute cohesive energies by subtracting isolated-atom reference energies from the bulk total energies. Collect all quantities into one comprehensive table.

## Reproduction target
Produce a CSV file, results.csv, containing the equilibrium volume (Å³), cohesive energy (eV per formula unit), band gap (eV), and static dielectric constant (dimensionless) for each of the seven Br contents x = 0, 0.17, 0.33, 0.5, 0.67, 0.83, 1. The file must have the columns: composition, volume_ang3, cohesive_energy_eV, band_gap_eV, static_dielectric_const. The csv should include exactly one row per composition.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotential library (SSSP or GBRV, PBE functional): https://www.quantum-espresso.org/pseudopotentials
- Crystal structure of orthorhombic γ-CsPbI3 (black phase)

## Workflow steps

### Step 1: Generate mixed-halide supercell structures
- Role: process
- Action: Using the orthorhombic γ-CsPbI3 unit cell as template (obtain from public crystallographic databases), create separate supercell structures for the seven Br compositions x = 0, 0.167, 0.33, 0.5, 0.67, 0.83, 1 by substituting I with Br. Select the most energetically favorable symmetry-broken configuration as the initial structure for each composition.
- Evidence: `/app/outputs/structures.summary`

### Step 2: Compute atomic reference energies
- Role: process
- Action: Perform spin-polarized DFT total-energy calculations for isolated Cs, Pb, I, and Br atoms using the same exchange-correlation functional and pseudopotentials as the bulk calculations. Record the total energies.
- Evidence: `/app/outputs/atomic_energies.json`

### Step 3: DFT geometry optimization of all compositions
- Role: process
- Action: For each composition, perform DFT geometry optimization (relax atomic coordinates and cell parameters) using a plane-wave pseudopotential code with GGA-PBE. Converge forces to <0.02 eV/Å and maximum stress to <0.02 GPa. Record the optimized total energy and equilibrium lattice volume.
- Evidence: `/app/outputs/opt_log.txt`

### Step 4: Band structure and band gap calculation
- Role: process
- Action: For each optimized structure, compute the electronic band structure along high-symmetry k-paths and determine the direct band gap at the Γ point. Do not include spin-orbit coupling.
- Evidence: `/app/outputs/band_gaps.csv`

### Step 5: Static dielectric constant extraction
- Role: process
- Action: For each composition, compute the frequency-dependent dielectric function from the DFT electronic structure and extract the static dielectric constant ε_s = ε₁(ω→0).
- Evidence: `/app/outputs/dielectric_constants.csv`

### Step 6: Compile final quantitative table
- Role: scored (load-bearing)
- Action: Assemble the equilibrium volume (Å³), cohesive energy (E_total – sum of atomic reference energies, in eV per formula unit), band gap (eV), and static dielectric constant (dimensionless) for all seven compositions x = 0, 0.17, 0.33, 0.5, 0.67, 0.83, 1 into a single CSV file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: composition, volume_ang3, cohesive_energy_eV, band_gap_eV, static_dielectric_const
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of the four headline quantities for all seven Br contents. The checker compares each value to hidden paper references and also verifies the expected monotonic trends and quadratic/linear fits.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `volume_ang3`, `cohesive_energy_eV`, `band_gap_eV`, `static_dielectric_const`
  - `units`:
    - `volume_ang3`: Å³
    - `cohesive_energy_eV`: eV
    - `band_gap_eV`: eV
    - `static_dielectric_const`: 

Notes: The intermediate DFT logs (structures, atomic energies, optimization logs, raw band gaps, raw dielectric constants) are not scored but act as supporting evidence for the pipeline.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "volume_ang3",
          "cohesive_energy_eV",
          "band_gap_eV",
          "static_dielectric_const"
        ],
        "units": {
          "volume_ang3": "Å³",
          "cohesive_energy_eV": "eV",
          "band_gap_eV": "eV",
          "static_dielectric_const": ""
        }
      },
      "description": "Table of the four headline quantities for all seven Br contents. The checker compares each value to hidden paper references and also verifies the expected monotonic trends and quadratic/linear fits."
    }
  ],
  "notes": "The intermediate DFT logs (structures, atomic energies, optimization logs, raw band gaps, raw dielectric constants) are not scored but act as supporting evidence for the pipeline."
}
```

## How you are scored
A hidden checker will read your results.csv and compare each entry to accurate reference values. It will also verify that the quantities exhibit the physically expected systematic variation with Br content and that the data can be fitted to the expected functional forms. The final reward is a weighted combination of the numerical agreement and the trend quality. Producing the correct table with high fidelity to the reference values earns full credit; large deviations or missing entries reduce the score. The checker runs automatically and its detailed thresholds are not public.
