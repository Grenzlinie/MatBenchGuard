# DFT and TD-DFT computational reproduction of a perylene derivative

## Problem background
Organic semiconductors based on perylene diimides, such as N,N'-Dioctyl-3,4,9,10-perylenedicarboximide (PTCDI-C8), are widely studied for optoelectronic applications. The gas-phase electronic and vibrational properties of PTCDI-C8 serve as benchmark data for understanding its intrinsic behaviour before considering environmental effects. Computational quantum chemistry can predict the equilibrium geometry, vibrational frequencies, and electronic absorption spectrum of this molecule, providing reference values that can be validated against experimental measurements.

## Approach
The investigation uses density functional theory (DFT) to compute the ground-state structure and properties of PTCDI-C8 in the gas phase. First, a reasonable starting geometry is generated from the molecular connectivity and pre-optimised with a force field. Then a full DFT geometry optimisation is carried out to locate the minimum-energy structure. The obtained geometry is verified as a true local minimum by computing harmonic vibrational frequencies—no imaginary frequencies should be present. Using the optimised geometry, a time-dependent DFT (TD‑DFT) calculation is performed to obtain the electronic excited states and thus the UV‑vis absorption spectrum. The B3LYP exchange‑correlation functional and the 6‑311G(d,p) basis set are used throughout. All calculations are performed with an open‑source quantum chemistry code.

## Reproduction target
Reproduce the gas‑phase DFT/B3LYP/6‑311G(d,p) optimised ground‑state geometry of PTCDI‑C8, confirm that it is a non‑centrosymmetric C1 local minimum (all vibrational frequencies real), compute the set of harmonic vibrational frequencies, and obtain the TD‑DFT absorption spectrum. Identify the wavelength of maximum absorption (the peak with the largest oscillator strength) in the computed spectrum.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Cheminformatics toolkit (RDKit or OpenBabel): rdkit or openbabel
- PTCDI-C8 molecular structure (SMILES): CCCCCCCCN1C(=O)c2ccc3c4ccc5c6c(ccc7c8ccc(c2c8c3c1=O)c9c7c(=O)n(c9=O)CCCCCCCC)C(=O)N(c(=O)c6c5c4=O)CCCCCCCC

## Workflow steps

### Step 1: Generate initial 3D structure
- Role: process
- Action: Build a 3D molecular model of PTCDI-C8 from the provided SMILES using a cheminformatics toolkit (e.g., RDKit or OpenBabel) and perform a force-field pre-optimization to obtain a reasonable starting geometry.
- Evidence: `/app/outputs/initial_structure.xyz`

### Step 2: DFT geometry optimization
- Role: scored
- Action: Run DFT geometry optimization of PTCDI-C8 using the B3LYP functional and 6-311G(d,p) basis set with an open-source quantum chemistry package (e.g., ORCA). Save the final converged geometry as optimized_geometry.xyz.
- Output file: `/app/outputs/optimized_geometry.xyz`
- Format: txt
- Contract: XYZ format: first line number of atoms, second line comment, then element_symbol x y z in Angstroms. The file must contain exactly 88 atoms and correspond to a local minimum with C1 symmetry (no imaginary frequencies).
- Scoring: scored by hidden verifier

### Step 3: Harmonic vibrational frequency calculation
- Role: scored (load-bearing)
- Action: Compute harmonic vibrational frequencies at the same B3LYP/6-311G(d,p) level on the optimized geometry. Write all frequencies in ascending order to harmonic_frequencies.csv.
- Output file: `/app/outputs/harmonic_frequencies.csv`
- Format: csv
- Contract: Single column 'frequency_cm-1' (float, unit cm⁻¹), 258 rows sorted ascending.
- Scoring: scored by hidden verifier

### Step 4: TD‑DFT excited‑state calculation
- Role: scored (load-bearing)
- Action: Run a TD-DFT calculation at B3LYP/6-311G(d,p) on the optimized geometry to obtain excited states. Write all computed states (wavelength nm, oscillator strength) to tddft_absorption.csv.
- Output file: `/app/outputs/tddft_absorption.csv`
- Format: csv
- Contract: Columns: wavelength_nm (float), oscillator_strength (float). Sorted by ascending wavelength.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_geometry.xyz`
- `/app/outputs/harmonic_frequencies.csv`
- `/app/outputs/tddft_absorption.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_geometry.xyz
- path: `/app/outputs/optimized_geometry.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized ground‑state geometry of PTCDI‑C8.
- schema:
  - `type`: text
  - `description`: XYZ format: first line number of atoms (88), second line comment, then element_symbol x y z in Angstroms. The geometry must exhibit C1 symmetry and correspond to a local minimum (no imaginary frequencies).

### harmonic_frequencies.csv
- path: `/app/outputs/harmonic_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Harmonic vibrational frequencies of PTCDI‑C8.
- schema:
  - `type`: table
  - `required_columns`: `frequency_cm-1`
  - `units`:
    - `frequency_cm-1`: cm⁻¹
  - `description`: All 258 harmonic vibrational frequencies in ascending order. The first few frequencies will be compared against hidden reference values within a tolerance.

### tddft_absorption.csv
- path: `/app/outputs/tddft_absorption.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: TD‑DFT UV‑vis absorption spectrum of PTCDI‑C8.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `oscillator_strength`
  - `units`:
    - `wavelength_nm`: nm
    - `oscillator_strength`: dimensionless
  - `description`: All TD‑DFT excited states sorted by ascending wavelength. The wavelength with maximum oscillator strength will be compared against a hidden reference value within a tolerance.

Notes: The hidden checker will verify: 1) geometry – atom count, C1 symmetry, and absence of imaginary frequencies; 2) frequencies – all values positive, and the first few within ±1.0 cm⁻¹ of the paper's reported values; 3) absorption – the wavelength with maximum oscillator strength within ±5 nm of the paper's gold. The agent must run the full DFT workflow and produce these artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_geometry.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "XYZ format: first line number of atoms (88), second line comment, then element_symbol x y z in Angstroms. The geometry must exhibit C1 symmetry and correspond to a local minimum (no imaginary frequencies)."
      },
      "description": "Optimized ground‑state geometry of PTCDI‑C8."
    },
    {
      "file": "harmonic_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_cm-1"
        ],
        "units": {
          "frequency_cm-1": "cm⁻¹"
        },
        "description": "All 258 harmonic vibrational frequencies in ascending order. The first few frequencies will be compared against hidden reference values within a tolerance."
      },
      "description": "Harmonic vibrational frequencies of PTCDI‑C8."
    },
    {
      "file": "tddft_absorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "oscillator_strength"
        ],
        "units": {
          "wavelength_nm": "nm",
          "oscillator_strength": "dimensionless"
        },
        "description": "All TD‑DFT excited states sorted by ascending wavelength. The wavelength with maximum oscillator strength will be compared against a hidden reference value within a tolerance."
      },
      "description": "TD‑DFT UV‑vis absorption spectrum of PTCDI‑C8."
    }
  ],
  "notes": "The hidden checker will verify: 1) geometry – atom count, C1 symmetry, and absence of imaginary frequencies; 2) frequencies – all values positive, and the first few within ±1.0 cm⁻¹ of the paper's reported values; 3) absorption – the wavelength with maximum oscillator strength within ±5 nm of the paper's gold. The agent must run the full DFT workflow and produce these artifacts."
}
```

## How you are scored
A hidden verifier will independently inspect each required artifact. For the optimised geometry, it checks the atom count and that the structure is a C1 local minimum with no imaginary frequencies. For the harmonic frequencies, it verifies that all frequencies are positive and compares the first few frequencies to reference values within a tolerance. For the TD‑DFT absorption, it checks the wavelength of the maximum oscillator strength peak against an expected value within a tolerance. The final reward is a weighted sum of these stage‑level scores; simply reporting a number is not sufficient—your computational workflow must produce the correct output files.
