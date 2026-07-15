# Relative energies of Al-sublattice configurations in 5 Å alumina films

## Problem background
Ultrathin alumina (Al₂O₃) films about 5 Å thick grown on close-packed metal surfaces serve as model supports for catalysis and as components in microelectronics. When the film consists of two oxygen layers, the arrangement of aluminium (Al) ions in the cation sublattice—whether they occupy octahedral, tetrahedral, or mixed sites—determines the film's stability and adsorption properties. Understanding which Al-sublattice configuration yields the lowest-energy flat film is important for interpreting experimental observations of short-range order and for predicting film behaviour.

## Approach
Use plane-wave density functional theory (DFT) in the local density approximation (LDA) to model periodic slab geometries of a two-oxygen-layer alumina film on two metal substrates: Ru(0001) and Al(111). For each substrate, construct slabs with four distinct Al-sublattice patterns that satisfy a normal coordination constraint (each surface oxygen has two Al neighbours): (i) all Al ions in octahedral sites (pure-o, 1×1 unit cell), (ii) all Al ions in tetrahedral sites (pure-t, 1×1), (iii) alternating zig-zag rows of tetrahedral and octahedral Al (zig-zag, 2×1), and (iv) alternating stripes of tetrahedral and octahedral Al (stripe, 3×1). Perform geometry relaxations while keeping the lower metal layers frozen, and then obtain total energies for each relaxed supercell. Compute the relative energy per Al₂O₃ formula unit of each configuration with respect to the zig-zag pattern on the same substrate, and output the results in a structured CSV file.

## Reproduction target
Produce a CSV file (`/app/outputs/relative_energies.csv`) that reports the relative LDA total energy per Al₂O₃ unit for the four Al-sublattice configurations (pure-o, pure-t, zig-zag, stripe) on both Ru(0001) and Al(111) substrates. Each row must contain the substrate name, the pattern name, the unit-cell designation, and the relative energy (in eV per Al₂O₃) computed with the zig-zag configuration as the zero-energy reference. The table must include all configurations that were computed: pure-o, pure-t, zig-zag, and stripe on Ru(0001); pure-o, pure-t, and zig-zag on Al(111) (the stripe pattern on Al(111) is optional). The columns are: `substrate`, `pattern`, `unit_cell`, `relative_energy_eV_per_Al2O3`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (precision set): https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: Convergence testing for alumina film DFT parameters
- Role: process
- Action: Perform convergence testing on a representative alumina film slab on Ru(0001) to determine k‑point sampling and slab thickness that yield relative energy convergence within ~0.1 eV. Use a 2×1 supercell and vary k‑point meshes and substrate layers.
- Evidence: `/app/outputs/convergence_report.txt`

### Step 2: Construction of slab supercells for Al‑sublattice structures
- Role: process
- Action: Generate initial atomic coordinates for each of the four Al‑sublattice configurations (pure-o 1×1, pure-t 1×1, zig‑zag 2×1, stripe 3×1) on Al(111) and Ru(0001) substrates, using bulk lattice parameters and stoichiometric, normally coordinated constraints. Prepare input files for DFT.
- Evidence: `/app/outputs/supercells.zip`

### Step 3: DFT relaxation and total energy calculation of supercells
- Role: process
- Action: For each supercell, perform LDA‑DFT geometry relaxation and total energy calculation using Quantum ESPRESSO. Use the k‑point grid determined in step 0, freeze the bottom layers of the metal substrate, and relax atomic positions until forces are below 0.05 eV/Å.
- Evidence: `/app/outputs/dft_outputs.zip`

### Step 4: Computation of relative energies per Al₂O₃ unit
- Role: scored (load-bearing)
- Action: From the total energies obtained in step 2, calculate the relative energy per Al₂O₃ unit for each configuration with respect to the zig‑zag 2×1 reference on the same substrate. Write the results to a structured CSV file.
- Output file: `/app/outputs/relative_energies.csv`
- Format: csv
- Contract: CSV with columns: substrate (str), pattern (str), unit_cell (str), relative_energy_eV_per_Al2O3 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.csv
- path: `/app/outputs/relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Relative LDA total energies per Al₂O₃ unit for the pure-o, pure-t, zig-zag (2×1), and stripe (3×1) Al-sublattice configurations on Ru(0001) and Al(111). The zig-zag pattern serves as the zero-energy reference.
- schema:
  - `type`: table
  - `required_columns`: `substrate`, `pattern`, `unit_cell`, `relative_energy_eV_per_Al2O3`
  - `units`:
    - `relative_energy_eV_per_Al2O3`: eV

Notes: The agent must install Quantum ESPRESSO and fetch the SSSP pseudopotential library. All values are checked against the paper's published energies with an absolute tolerance; the checker also verifies that all reported energies are non‑negative and the zig‑zag structure is lowest.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "substrate",
          "pattern",
          "unit_cell",
          "relative_energy_eV_per_Al2O3"
        ],
        "units": {
          "relative_energy_eV_per_Al2O3": "eV"
        }
      },
      "description": "Relative LDA total energies per Al₂O₃ unit for the pure-o, pure-t, zig-zag (2×1), and stripe (3×1) Al-sublattice configurations on Ru(0001) and Al(111). The zig-zag pattern serves as the zero-energy reference."
    }
  ],
  "notes": "The agent must install Quantum ESPRESSO and fetch the SSSP pseudopotential library. All values are checked against the paper's published energies with an absolute tolerance; the checker also verifies that all reported energies are non‑negative and the zig‑zag structure is lowest."
}
```

## How you are scored
A hidden verifier reads your `relative_energies.csv` and scores it by comparing your reported relative energies to a hidden set of reference values, using a preset absolute tolerance. The verifier may also check for internal consistency and correctness of the reported values. You must run the full DFT relaxation and energy extraction workflow described in the steps; reporting numbers without executing the computation is not sufficient to satisfy the scoring criteria.
