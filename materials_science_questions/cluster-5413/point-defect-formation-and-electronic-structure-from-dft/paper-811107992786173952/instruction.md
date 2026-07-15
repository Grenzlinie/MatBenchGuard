# Defect electronic structure and optical absorption of an oxygen vacancy in cubic HfO₂ from DFT

## Problem background
Hafnia (HfO₂) is a promising material for resistive random access memory (ReRAM) devices, where resistive switching is widely attributed to electrically active defects. Oxygen vacancies are hypothesized to act as charge‑carrier traps responsible for many of the observed transport and optical signatures. Understanding the electronic structure and optical absorption of oxygen vacancies is therefore essential for identifying these defects experimentally and for engineering device performance. This task aims at computing the density of states and optical absorption spectrum of a single oxygen vacancy in cubic HfO₂ using first‑principles calculations.

## Approach
The calculations employ density functional theory (DFT) with the hybrid B3LYP functional, as implemented in Quantum ESPRESSO. A perfect crystal of cubic HfO₂ (space group Fm‑3m, lattice constant ≈5.08 Å) is used to build a 3×3×3 supercell containing 81 atoms. One oxygen atom is then removed to create a neutral oxygen monovacancy. A ground‑state calculation is performed for this defective supercell. From the ground‑state output, two quantities are derived: (1) the total density of states (TDOS), which reveals the energy position of defect‑induced gap states, and (2) the optical absorption spectrum, which probes electronic transitions involving the vacancy. Both spectra are saved as plain‑text data files for automated evaluation.

## Reproduction target
Compute and output two data files for the oxygen‑vacancy supercell:
- `/app/outputs/tdos.dat` – total density of states, containing energy (eV) and DOS (arbitrary units) as two whitespace‑separated columns.
- `/app/outputs/absorption.dat` – optical absorption spectrum, containing energy (eV) and absorption intensity (arbitrary units) as two whitespace‑separated columns.

A hidden verifier will automatically extract the defect‑state energy (the first prominent peak above the valence band maximum in the TDOS) and the dominant absorption peak energy (the energy of maximum absorption), and compare them against independently established reference values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- B3LYP pseudopotentials for Hf and O: https://www.quantum-espresso.org/pseudopotentials/
- Cubic HfO₂ crystal structure: ICSD CollCode 66795

## Workflow steps

### Step 1: DFT ground state calculation
- Role: process
- Action: Run Quantum ESPRESSO with the B3LYP hybrid functional on a 3×3×3 supercell (81 atoms) of cubic HfO₂ with one oxygen atom removed to obtain the ground state wavefunction and related outputs.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 2: Total density of states (TDOS) extraction
- Role: scored
- Action: From the DFT ground state output, compute the total density of states and write tdos.dat containing energy (eV) and DOS (arbitrary units).
- Output file: `/app/outputs/tdos.dat`
- Format: txt
- Contract: Two whitespace‑separated columns: energy (float, eV), density of states (float).
- Scoring: scored by hidden verifier

### Step 3: Optical absorption spectrum extraction
- Role: scored
- Action: From the DFT output, compute the optical absorption spectrum and write absorption.dat containing energy (eV) and absorption intensity (arbitrary units).
- Output file: `/app/outputs/absorption.dat`
- Format: txt
- Contract: Two whitespace‑separated columns: energy (float, eV), absorption (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tdos.dat`
- `/app/outputs/absorption.dat`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tdos.dat
- path: `/app/outputs/tdos.dat`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Total density of states for the oxygen‑vacancy supercell. The checker locates the first prominent peak above the valence band maximum (energy > 0) and compares its energy to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `dos`
  - `units`:
    - `energy_eV`: eV
    - `dos`: arbitrary

### absorption.dat
- path: `/app/outputs/absorption.dat`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Optical absorption spectrum for the oxygen‑vacancy supercell. The checker locates the energy of the maximum absorption value and compares it to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `absorption`
  - `units`:
    - `energy_eV`: eV
    - `absorption`: arbitrary

Notes: Both files are plain text with two whitespace‑separated columns. The checker recomputes the relevant peak positions from the supplied data and compares them to the paper‑reported values using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tdos.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "dos"
        ],
        "units": {
          "energy_eV": "eV",
          "dos": "arbitrary"
        }
      },
      "description": "Total density of states for the oxygen‑vacancy supercell. The checker locates the first prominent peak above the valence band maximum (energy > 0) and compares its energy to a hidden reference."
    },
    {
      "file": "absorption.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "absorption"
        ],
        "units": {
          "energy_eV": "eV",
          "absorption": "arbitrary"
        }
      },
      "description": "Optical absorption spectrum for the oxygen‑vacancy supercell. The checker locates the energy of the maximum absorption value and compares it to a hidden reference."
    }
  ],
  "notes": "Both files are plain text with two whitespace‑separated columns. The checker recomputes the relevant peak positions from the supplied data and compares them to the paper‑reported values using appropriate tolerances."
}
```

## How you are scored
A hidden verifier automatically reads the two scored output files you produce. For `/app/outputs/tdos.dat`, it locates the first clear peak in the density of states above the valence band maximum (energy > 0 eV) and records its energy. For `/app/outputs/absorption.dat`, it finds the energy at which the absorption intensity reaches its maximum. The verifier then compares these two extracted peak energies to hidden reference values; the closer your computed peaks are to the expected values, the higher your score for each stage. The final reward is a weighted sum of the two stage scores. Simply reporting numbers without writing the required data files is not sufficient – only the contents of the submitted files are evaluated.
