# DFT Evaluation of Co-doping and Oxygen Vacancy in Li4Ti5O12 for Enhanced Electronic Conductivity

## Problem background
Spinel Li4Ti5O12 (LTO) is a promising "zero-strain" anode material for lithium-ion batteries, but its poor electronic and ionic conductivity limits high-rate performance. Co-doping with Mg/Zr and introducing oxygen vacancies have been proposed to improve conductivity by modifying the electronic structure and Li+ migration pathways. This task reproduces the density functional theory (DFT) analysis that investigates how Mg/Zr co-doping and oxygen vacancies affect the total density of states (DOS) and Li+ migration barriers in LTO.

## Approach
The computational approach uses DFT with the GGA-PBE functional and Hubbard U corrections (U=4 eV on Ti 3d and Zr 4d) to model spinel LTO in three configurations: pristine LTO, Mg/Zr co-doped LTO (LMTZO), and the same co-doped system with one oxygen vacancy (LMTZO-Ov). After constructing supercells and relaxing the geometries, the total DOS is calculated for the pristine and vacancy-containing systems. The Li+ migration barrier is computed via the nudged elastic band (NEB) method for the doped and doped+vacancy systems. The analysis focuses on comparing the band gap, the position of the Fermi level relative to the conduction band, and the height of the migration barriers between the different systems.

## Reproduction target
Produce three output artifacts: (1) a CSV file dos_LTO.csv with the total DOS of pristine LTO, (2) a CSV file dos_LMTZO_Ov.csv with the total DOS of LMTZO-Ov, and (3) a JSON file migration_barriers.json containing the computed Li+ migration barriers (in eV) for LMTZO and LMTZO-Ov. A hidden verifier will later use these files to determine the band gaps, check whether the Fermi level enters the conduction band for LMTZO-Ov, and compare the migration barriers to the expected trend (barrier lowering with the oxygen vacancy). The objective is to replicate these computational results following the DFT protocol described in the workflow steps.

## Assets

- Li4Ti5O12 crystal structure (CIF): https://legacy.materialsproject.org/materials/mp-6611/
- Pseudopotentials for GGA-PBE (Li, Ti, O, Mg, Zr): https://www.materialscloud.org/discover/sssp
- Quantum ESPRESSO: https://www.quantum-espresso.org/download/
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Supercell Construction
- Role: process
- Action: Construct supercells of Li4Ti5O12 (LTO), Li3.8Mg0.2Ti4.9Zr0.1O12 (LMTZO), and the same doped system with one oxygen vacancy (LMTZO-Ov). Choose reasonable substitution and vacancy sites. Output initial atomic coordinates in a standard format (.cif or .in).
- Evidence: `/app/outputs/structures.log`

### Step 2: Geometry Optimization
- Role: process
- Action: Perform DFT structural relaxation on LTO, LMTZO, and LMTZO-Ov supercells using GGA-PBE+U functional (U=4 eV on Ti 3d and Zr 4d states) with Quantum ESPRESSO. Relax atomic positions until forces are below 0.01 eV/Å. Save the final relaxed coordinates.
- Evidence: `/app/outputs/relaxation_report.txt`

### Step 3: Density of States – pristine LTO
- Role: scored
- Action: Using the relaxed LTO structure, compute total density of states. Write a CSV file dos_LTO.csv with columns 'energy' (eV, relative to the Fermi level) and 'dos_total' (states/eV). Use at least 1000 energy points covering -5 to 5 eV.
- Output file: `/app/outputs/dos_LTO.csv`
- Format: csv
- Contract: Columns: energy (eV), dos_total (states/eV); energy axis relative to Fermi level (E=0).
- Scoring: scored by hidden verifier

### Step 4: Density of States – LMTZO-Ov
- Role: scored (load-bearing)
- Action: Using the relaxed LMTZO-Ov structure, compute total density of states. Write a CSV file dos_LMTZO_Ov.csv with columns 'energy' (eV, relative to the Fermi level) and 'dos_total' (states/eV) using the same energy grid as for LTO.
- Output file: `/app/outputs/dos_LMTZO_Ov.csv`
- Format: csv
- Contract: Columns: energy (eV), dos_total (states/eV); energy axis relative to Fermi level (E=0).
- Scoring: scored by hidden verifier

### Step 5: Li-ion Migration Barriers
- Role: scored
- Action: Perform nudged elastic band (NEB) calculations on LMTZO and LMTZO-Ov for a representative Li+ hop path. Extract the energy barrier (eV) as the difference between the saddle-point energy and the initial minimum. Write a JSON file migration_barriers.json with keys 'LMTZO' and 'LMTZO_Ov' (values: float, units: eV).
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: Object with keys 'LMTZO' (float) and 'LMTZO_Ov' (float), values in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_LTO.csv`
- `/app/outputs/dos_LMTZO_Ov.csv`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_LTO.csv
- path: `/app/outputs/dos_LTO.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total density of states for pristine Li4Ti5O12; used by the checker to recompute the band gap.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `dos_total`
  - `units`:
    - `energy`: eV
    - `dos_total`: states/eV

### dos_LMTZO_Ov.csv
- path: `/app/outputs/dos_LMTZO_Ov.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total density of states for Mg/Zr co-doped Li4Ti5O12 with one oxygen vacancy; used to recompute the band gap and Fermi level position.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `dos_total`
  - `units`:
    - `energy`: eV
    - `dos_total`: states/eV

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: NEB-computed Li+ migration barriers (eV) for LMTZO and LMTZO-Ov; compared against paper-reported values within tolerance.
- schema:
  - `type`: object
  - `required`: `LMTZO`, `LMTZO_Ov`
  - `items`:
    - `LMTZO`: float (eV)
    - `LMTZO_Ov`: float (eV)

Notes: All output files are machine-readable. The checker recomputes the band gap from the DOS CSV files and compares migration barriers to the paper’s hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_LTO.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "dos_total"
        ],
        "units": {
          "energy": "eV",
          "dos_total": "states/eV"
        }
      },
      "description": "Total density of states for pristine Li4Ti5O12; used by the checker to recompute the band gap."
    },
    {
      "file": "dos_LMTZO_Ov.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "dos_total"
        ],
        "units": {
          "energy": "eV",
          "dos_total": "states/eV"
        }
      },
      "description": "Total density of states for Mg/Zr co-doped Li4Ti5O12 with one oxygen vacancy; used to recompute the band gap and Fermi level position."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "LMTZO",
          "LMTZO_Ov"
        ],
        "items": {
          "LMTZO": "float (eV)",
          "LMTZO_Ov": "float (eV)"
        }
      },
      "description": "NEB-computed Li+ migration barriers (eV) for LMTZO and LMTZO-Ov; compared against paper-reported values within tolerance."
    }
  ],
  "notes": "All output files are machine-readable. The checker recomputes the band gap from the DOS CSV files and compares migration barriers to the paper’s hidden reference values."
}
```

## How you are scored
Your outputs are evaluated by a hidden automated verifier. For the DOS files, the verifier recomputes the band gap and the Fermi-level occupation using a common threshold; it then checks the relative changes between LTO and LMTZO-Ov. For the migration barriers, the verifier compares your barrier values to a hidden reference (derived from independent DFT runs with the same functional) within a tolerance and verifies that the barrier for LMTZO-Ov is lower than for LMTZO. Each artifact is scored individually, and the total reward is a weighted combination. Simply reporting numbers from the literature is not sufficient; the verifier tests that the physical trends emerge from your simulated data.
