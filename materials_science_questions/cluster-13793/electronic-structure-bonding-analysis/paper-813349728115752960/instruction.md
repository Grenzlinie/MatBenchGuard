# First-Principles Study of Structural Stability and Bonding in YAlO3 Crystal

## Problem background
Orthorhombic YAlO3 (YAP) is a crystalline material with potential applications in lasers, scintillators, and high-temperature ceramics. Understanding its structural stability and chemical bonding is essential for its technological use. This task uses first-principles density functional theory (DFT) calculations to investigate these properties. The goal is to compute optimized lattice parameters, formation energy, and Mulliken atomic charges and bond overlap populations, which characterize the stability and bonding nature of YAP.

## Approach
The method employs plane-wave pseudopotential DFT with the generalized gradient approximation (GGA) for exchange and correlation. Geometry optimizations are performed for orthorhombic YAlO3 (space group Pnma) and the reference compounds cubic Y2O3 and α-Al2O3. Total energies are extracted from the optimized structures, and the formation energy of YAP is derived from the energy balance among the three crystals. Mulliken population analysis yields orbital charges, atomic charges, and bond overlap populations, revealing the character of chemical bonding. All simulations are executed using an open-source DFT code (e.g., Quantum ESPRESSO) with publicly available pseudopotentials.

## Reproduction target
Produce the following five artifacts that correspond to the main quantities reported in the original DFT study:

- Optimized lattice parameters a, b, c (in Å) of YAP, written to `yap_optimized_lattice.csv`.
- Total energies (in eV) of YAP, Y2O3, and α-Al2O3, written to `total_energies.csv`.
- Formation energy ΔE = E(YAP) − 0.5·E(Y2O3) − 0.5·E(Al2O3) (in eV), written to `formation_energy.txt`.
- Mulliken atomic charges for the symmetry-inequivalent atoms (O_a, O_b, Al, Y), with s, p, d orbital populations and total charge, written to `mulliken_charges.csv`.
- Mulliken bond overlap populations and bond lengths for distinct O–Al, O–Y, and O–O bonds, written to `mulliken_overlap.csv`.

## Assets

- Orthorhombic YAP crystal structure: 10.1016/0025-5408(75)90125-7
- Cubic Y2O3 crystal structure: 10.1103/PhysRevB.42.7587
- α-Al2O3 (corundum) crystal structure: 10.1016/j.fuel.2005.10.006
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE) for Y, Al, O: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: DFT geometry optimization and total-energy calculation
- Role: process
- Action: Perform density functional theory (DFT) geometry optimization and self-consistent field (SCF) calculations for orthorhombic YAlO3 (space group Pnma), cubic Y2O3, and α-Al2O3 using an open-source plane-wave pseudopotential code (e.g., Quantum ESPRESSO). Use GGA-PBE exchange-correlation functional and appropriate pseudopotentials. Relax both atomic positions and cell parameters until forces and stresses converge. Save final total energies and optimized structures.
- Evidence: `/app/outputs/optimizations.log`

### Step 2: Optimized lattice parameters of YAlO3
- Role: scored
- Action: Extract the optimized lattice parameters a, b, c (in Å) of YAlO3 from the DFT output and write them to yap_optimized_lattice.csv.
- Output file: `/app/outputs/yap_optimized_lattice.csv`
- Format: csv
- Contract: Columns: parameter (string, one of a,b,c), value_angstrom (float), reference (string, 'calculated').
- Scoring: scored by hidden verifier

### Step 3: Total energies of YAlO3, Y2O3, Al2O3
- Role: scored
- Action: Extract the final total energies (in eV) of YAlO3, Y2O3, and α-Al2O3 from the DFT output and write them to total_energies.csv.
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: Columns: system (string, one of YAP, Y2O3, Al2O3), total_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 4: Formation energy of YAlO3
- Role: scored
- Action: Compute the formation energy ΔE = E(YAlO3) - 0.5*E(Y2O3) - 0.5*E(Al2O3) using the total energies from total_energies.csv and write the result as a single floating-point number (in eV) to formation_energy.txt.
- Output file: `/app/outputs/formation_energy.txt`
- Format: txt
- Contract: A single floating-point number (e.g., -3.73).
- Scoring: scored by hidden verifier

### Step 5: Mulliken atomic charges
- Role: scored (load-bearing)
- Action: Perform a Mulliken population analysis on the optimized YAlO3 structure to obtain orbital charges and Mulliken charges for the symmetry-inequivalent atoms: O_a, O_b, Al, and Y. Write the results to mulliken_charges.csv.
- Output file: `/app/outputs/mulliken_charges.csv`
- Format: csv
- Contract: Columns: atom (string, O_a,O_b,Al,Y), s (float), p (float), d (float), total (float), mulliken_charge (float).
- Scoring: scored by hidden verifier

### Step 6: Mulliken bond overlap populations
- Role: scored (load-bearing)
- Action: Compute Mulliken bond overlap populations for the distinct O-Al, O-Y, and O-O bonds in the optimized YAlO3 structure and write them to mulliken_overlap.csv, including bond lengths.
- Output file: `/app/outputs/mulliken_overlap.csv`
- Format: csv
- Contract: Columns: bond (string, e.g., O-Al, O-Y, O-O), population (float), length_angstrom (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/yap_optimized_lattice.csv`
- `/app/outputs/total_energies.csv`
- `/app/outputs/formation_energy.txt`
- `/app/outputs/mulliken_charges.csv`
- `/app/outputs/mulliken_overlap.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### yap_optimized_lattice.csv
- path: `/app/outputs/yap_optimized_lattice.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice parameters a, b, c of orthorhombic YAlO3 crystal.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `value_angstrom`, `reference`
  - `columns`:
    - `parameter`: string, one of a, b, c
    - `value_angstrom`: float
    - `reference`: string, 'calculated'

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Total energies of YAP, Y2O3, and Al2O3 in eV.
- schema:
  - `type`: table
  - `required_columns`: `system`, `total_energy_eV`
  - `columns`:
    - `system`: string, one of YAP, Y2O3, Al2O3
    - `total_energy_eV`: float

### formation_energy.txt
- path: `/app/outputs/formation_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Formation energy of YAlO3 computed from total energies, in eV.
- schema:
  - `type`: text
  - `required`: `value`
  - `value`: float

### mulliken_charges.csv
- path: `/app/outputs/mulliken_charges.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mulliken atomic charges for symmetry-inequivalent atoms in YAlO3.
- schema:
  - `type`: table
  - `required_columns`: `atom`, `s`, `p`, `d`, `total`, `mulliken_charge`
  - `columns`:
    - `atom`: string, e.g., O_a, O_b, Al, Y
    - `s`: float
    - `p`: float
    - `d`: float
    - `total`: float
    - `mulliken_charge`: float

### mulliken_overlap.csv
- path: `/app/outputs/mulliken_overlap.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mulliken bond overlap populations for distinct bonds in YAlO3.
- schema:
  - `type`: table
  - `required_columns`: `bond`, `population`, `length_angstrom`
  - `columns`:
    - `bond`: string, e.g., O-Al, O-Y, O-O
    - `population`: float
    - `length_angstrom`: float

Notes: All scored outputs are compared against the paper's reported values with appropriate tolerances (exact_match policy). The verifier recomputes the formation energy from total_energies.csv for cross-checking. Mulliken steps are load-bearing; they cannot be faked without running the DFT simulation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "yap_optimized_lattice.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "value_angstrom",
          "reference"
        ],
        "columns": {
          "parameter": "string, one of a, b, c",
          "value_angstrom": "float",
          "reference": "string, 'calculated'"
        }
      },
      "description": "Optimized lattice parameters a, b, c of orthorhombic YAlO3 crystal."
    },
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "total_energy_eV"
        ],
        "columns": {
          "system": "string, one of YAP, Y2O3, Al2O3",
          "total_energy_eV": "float"
        }
      },
      "description": "Total energies of YAP, Y2O3, and Al2O3 in eV."
    },
    {
      "file": "formation_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": [
          "value"
        ],
        "value": "float"
      },
      "description": "Formation energy of YAlO3 computed from total energies, in eV."
    },
    {
      "file": "mulliken_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom",
          "s",
          "p",
          "d",
          "total",
          "mulliken_charge"
        ],
        "columns": {
          "atom": "string, e.g., O_a, O_b, Al, Y",
          "s": "float",
          "p": "float",
          "d": "float",
          "total": "float",
          "mulliken_charge": "float"
        }
      },
      "description": "Mulliken atomic charges for symmetry-inequivalent atoms in YAlO3."
    },
    {
      "file": "mulliken_overlap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "bond",
          "population",
          "length_angstrom"
        ],
        "columns": {
          "bond": "string, e.g., O-Al, O-Y, O-O",
          "population": "float",
          "length_angstrom": "float"
        }
      },
      "description": "Mulliken bond overlap populations for distinct bonds in YAlO3."
    }
  ],
  "notes": "All scored outputs are compared against the paper's reported values with appropriate tolerances (exact_match policy). The verifier recomputes the formation energy from total_energies.csv for cross-checking. Mulliken steps are load-bearing; they cannot be faked without running the DFT simulation."
}
```

## How you are scored
Each output file is checked independently by a hidden verifier. The verifier compares your computed values against a reference set of correct values (obtained from the original study) using tolerances that account for code-to-code and numerical variation. Every artifact contributes to the final score with equal weight. You must genuinely run the DFT simulations and produce these outputs from your own calculations; simply copying or reporting numbers from the literature without the corresponding computations will not meet the scoring requirements.
