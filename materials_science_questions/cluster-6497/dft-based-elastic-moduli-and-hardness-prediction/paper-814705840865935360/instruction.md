# DFT stability and bulk modulus of C3P4 phases

## Problem background
Carbon phosphide solids with stoichiometry C₃P₄ are hypothetical materials that could be obtained by substituting phosphorus for nitrogen in known C₃N₄ polymorphs. Predicting their structural stability and mechanical properties is of interest for high-performance engineering applications. This task investigates the energetics of five candidate C₃P₄ crystal structures—α, β, cubic, pseudocubic, and graphitic—to determine which arrangement is the most stable and to compute its bulk modulus.

## Approach
Use first-principles density-functional theory (DFT) in the local-density approximation (LDA) with ultra-soft pseudopotentials and a plane-wave basis. For each of the five C₃P₄ phases, the initial geometry is constructed by taking the corresponding C₃N₄ structure and replacing N with P. Total-energy calculations are performed on a grid of volumes obtained by uniform lattice scaling around the expected equilibrium. The energy–volume data points for each phase are fitted to a fourth-order polynomial to obtain the equilibrium energy and volume, and the bulk modulus is derived from the curvature at the minimum. The final results are the ranking of the five phases by total energy (stability order) and the bulk modulus of the most stable phase.

## Reproduction target
For each of the five C₃P₄ phases (α, β, cubic, pseudocubic, graphitic), perform DFT total-energy calculations over a range of volumes and collect the (volume, total energy) pairs. Fit each set to a fourth-order polynomial to extract the equilibrium total energy, equilibrium volume, and bulk modulus. Determine which phase has the lowest total energy (i.e., is the most stable) and report its bulk modulus. The relative stability ordering and the absolute bulk modulus value are the key quantities to reproduce.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Ultrasoft pseudopotentials for C and P: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Prepare initial crystal structures
- Role: process
- Action: Construct crystal structures for the five C3P4 phases (α, β, cubic, pseudocubic, graphitic) by substituting P for N in known C3N4 polymorph structures. Save as DFT input files.
- Evidence: none

### Step 2: Compute total energy vs. volume for each C3P4 phase
- Role: scored (load-bearing)
- Action: Run DFT total energy calculations for each C3P4 phase over a range of volumes around equilibrium (uniform scaling). Write volume and total energy per C3P4 unit to CSV.
- Output file: `/app/outputs/energy_vs_volume.csv`
- Format: csv
- Contract: CSV columns: phase (str), volume_ang3 (float, cubic Angstrom per C3P4 unit), total_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 3: Extract equilibrium properties by E(V) fitting
- Role: scored
- Action: Fit the energy-volume data for each phase to a 4th-order polynomial, determine equilibrium volume, total energy, and bulk modulus. Write the fitted properties to CSV.
- Output file: `/app/outputs/properties.csv`
- Format: csv
- Contract: CSV columns: phase (str), equilibrium_energy_eV (float), equilibrium_volume_ang3 (float), bulk_modulus_GPa (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_vs_volume.csv`
- `/app/outputs/properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_vs_volume.csv
- path: `/app/outputs/energy_vs_volume.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw DFT total energy vs. volume data for all C3P4 phases. Checker refits to derive equilibrium properties.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `volume_ang3`, `total_energy_eV`
  - `units`:
    - `volume_ang3`: cubic Angstrom
    - `total_energy_eV`: eV per C3P4 unit

### properties.csv
- path: `/app/outputs/properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Fitted equilibrium properties from 4th-order polynomial E(V) fit. Checker recomputes from raw data and verifies stability ordering and bulk modulus value.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `equilibrium_energy_eV`, `equilibrium_volume_ang3`, `bulk_modulus_GPa`
  - `units`:
    - `equilibrium_energy_eV`: eV per C3P4 unit
    - `equilibrium_volume_ang3`: cubic Angstrom
    - `bulk_modulus_GPa`: GPa

Notes: The checker will refit the raw E(V) data to verify that pseudocubic-C3P4 has the lowest total energy (most stable) and the highest bulk modulus among the five phases, within acceptable tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_vs_volume.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "volume_ang3",
          "total_energy_eV"
        ],
        "units": {
          "volume_ang3": "cubic Angstrom",
          "total_energy_eV": "eV per C3P4 unit"
        }
      },
      "description": "Raw DFT total energy vs. volume data for all C3P4 phases. Checker refits to derive equilibrium properties."
    },
    {
      "file": "properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "equilibrium_energy_eV",
          "equilibrium_volume_ang3",
          "bulk_modulus_GPa"
        ],
        "units": {
          "equilibrium_energy_eV": "eV per C3P4 unit",
          "equilibrium_volume_ang3": "cubic Angstrom",
          "bulk_modulus_GPa": "GPa"
        }
      },
      "description": "Fitted equilibrium properties from 4th-order polynomial E(V) fit. Checker recomputes from raw data and verifies stability ordering and bulk modulus value."
    }
  ],
  "notes": "The checker will refit the raw E(V) data to verify that pseudocubic-C3P4 has the lowest total energy (most stable) and the highest bulk modulus among the five phases, within acceptable tolerance."
}
```

## How you are scored
A hidden verifier reads your output files and independently refits the energy-volume data to a fourth-order polynomial to derive equilibrium energies and bulk moduli. It then checks two things: (1) that the phase with the lowest total energy (most stable) and the highest bulk modulus matches the expected phase among the five candidates, and (2) that the bulk modulus of that phase is within an acceptable tolerance of the reference value. Both the raw energy-volume CSV and the properties CSV contribute to the final score, with the raw data carrying the highest weight because the verifier recomputes properties from it. Submitting the expected stability outcome without the underlying DFT data will not pass.
