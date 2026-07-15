# Direct Exchange Energy Computation for First-Row Transition-Metal Dimer Series

## Problem background
The paper investigates whether the direct exchange interaction between two transition-metal atoms can serve as a simple indicator of ferromagnetic properties in a lattice. It focuses on first-row transition-metal homodimers (Sc₂ through Zn₂) and computes the electronic energy difference between the high-spin and singlet states using several quantum chemistry methods. The task is to recalculate these direct exchange energies to understand their pattern across the series and assess the influence of the choice of electronic-structure method.

## Approach
The direct exchange energy is defined as the electronic energy of the high-spin state minus that of the singlet state. To compute it, perform single-point energy calculations on each homodimer at the equilibrium bond lengths provided in the resource file `dimer_geometries.csv`. Use four electronic-structure methods: Hartree–Fock (HF), the local spin density approximation SVWN (Slater exchange with VWN correlation functional III), the meta-GGA MPW1PW91, and a modified version of the hybrid functional B3PW91 with custom parameters P1=1.0, P2=0.06, P3=0.9, P4=0.85, P5=1.0, P6=1.0. All calculations employ the LanL2MB basis set. For each dimer, run both the singlet and the high‑spin multiplicity listed in the geometry file. The raw electronic energies are then used to obtain the direct exchange energies.

## Reproduction target
Produce a CSV file `direct_exchange_energies.csv` containing the computed direct exchange energies for all ten dimers (Sc₂, Ti₂, V₂, Cr₂, Mn₂, Fe₂, Co₂, Ni₂, Cu₂, Zn₂) and all four methods. For each dimer–method pair, calculate the direct exchange energy as (high‑spin energy − singlet energy) and convert it to electronvolts using 1 hartree = 27.2114 eV. The CSV must have columns: `dimer` (string, e.g. Sc2), `method` (string: HF, SVWN, MPW1PW91, B3PW91), `direct_exchange_energy_eV` (float). Provide exactly one row per dimer–method pair (40 rows total). No other variants (zero‑point corrected energies, triplet‑state energies, exchange constants) are required.

## Assets

- PySCF: https://pyscf.org/
- LanL2MB basis set: pyscf
- dimer_geometries.csv

## Workflow steps

### Step 1: Compute electronic energies
- Role: process
- Action: For each first-row transition-metal homodimer (Sc₂, Ti₂, V₂, Cr₂, Mn₂, Fe₂, Co₂, Ni₂, Cu₂, Zn₂), perform single-point energy calculations in both singlet and high-spin states at the bond lengths provided in dimer_geometries.csv. Use four electronic-structure methods: Hartree–Fock (HF), local spin density approximation SVWN (Slater exchange with VWN correlation, functional III), MPW1PW91, and a modified B3PW91 functional (with custom parameters P1=1.0, P2=0.06, P3=0.9, P4=0.85, P5=1.0, P6=1.0). Use the LanL2MB basis set for all atoms. Save the raw electronic energies (in hartree) to a JSON file energies.json.
- Evidence: `/app/outputs/energies.json`

### Step 2: Compute direct exchange energies
- Role: scored (load-bearing)
- Action: From the singlet and high-spin energies in energies.json, compute the direct exchange energy as (high-spin energy minus singlet energy) for each dimer and method. Convert the difference from hartree to electronvolts using 1 hartree = 27.2114 eV. Output the results to direct_exchange_energies.csv.
- Output file: `/app/outputs/direct_exchange_energies.csv`
- Format: csv
- Contract: CSV with columns: dimer (string, e.g. Sc2, Ti2, ..., Zn2), method (string: HF, SVWN, MPW1PW91, B3PW91), direct_exchange_energy_eV (float). One row per dimer–method pair (40 rows total).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/direct_exchange_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### direct_exchange_energies.csv
- path: `/app/outputs/direct_exchange_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed direct exchange energies (high-spin minus singlet) in eV for each dimer and each of the four methods.
- schema:
  - `type`: table
  - `required_columns`: `dimer`, `method`, `direct_exchange_energy_eV`
  - `units`:
    - `direct_exchange_energy_eV`: eV

Notes: Only the electronic energy difference (variant without zero-point correction) is scored. The hidden checker compares each value to reference data within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "direct_exchange_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dimer",
          "method",
          "direct_exchange_energy_eV"
        ],
        "units": {
          "direct_exchange_energy_eV": "eV"
        }
      },
      "description": "Computed direct exchange energies (high-spin minus singlet) in eV for each dimer and each of the four methods."
    }
  ],
  "notes": "Only the electronic energy difference (variant without zero-point correction) is scored. The hidden checker compares each value to reference data within a tolerance."
}
```

## How you are scored
Your submission is scored by a hidden verifier that compares your `direct_exchange_energy_eV` values against reference data derived from the paper. Each value is checked against an allowed tolerance, and the overall score is the fraction of entries that fall within that tolerance. The verifier does not disclose the reference values or the tolerance magnitude. Only the electronic energy difference (without zero‑point correction) is assessed. Make sure you output the CSV file exactly as specified; missing columns, extra rows, or incorrect formatting will cause validation failures before scoring.
