# Compute Phonon Frequencies and Debye Temperatures of Potassium Halides

## Problem background
Alkali halides are prototypical ionic crystals whose lattice dynamics govern thermal, optical, and electrical properties. For the potassium halides KCl, KBr, and KI, a 7‑parameter bond‑bending force model (BBFM) has been proposed. The model decomposes the total potential energy into short‑range central forces, bond‑bending forces arising from deformations in inter‑bond angles, and long‑range Coulomb interactions. Using published model parameters and lattice constants, this task computes the phonon dispersion relations at high‑symmetry points and the Debye characteristic temperature as a function of temperature, providing a quantitative test of the model’s predictive power.

## Approach
The approach implements the BBFM for NaCl‑structure crystals. For each compound, construct the 6×6 dynamical matrix D(q) at a given wavevector q using the analytic matrix elements that account for central forces (first‑ and second‑neighbour radial terms), bond‑bending forces (deformations of selected inter‑bond angles), and Coulomb interactions (a long‑range term summed in reciprocal space). The force‑constant parameters (α₁, β₁, α₂, γ₁′, γ₂′, γ₃′, Z²) and the lattice constant a are provided. Phonon frequencies are then obtained by solving the secular equation |D(q) − ω²I| = 0. For the high‑symmetry q‑points Γ, X, and L, the six eigenfrequencies are computed and sorted. To derive the temperature‑dependent Debye temperature, the same model is solved on a dense uniform mesh in the first Brillouin zone. The resulting eigenfrequencies are used to construct the vibrational density of states g(ν). From g(ν), the lattice heat capacity at constant volume Cᵥ(T) is calculated via Bose‑Einstein statistics. The Debye temperature θ_D(T) is then extracted by inverting the Debye model’s Cᵥ function, using standard reference tables or numerical root‑finding.

## Reproduction target
For each potassium halide — KCl, KBr, and KI — compute the phonon frequencies of all six vibrational branches at the high‑symmetry q‑points Γ, X, and L. Report the frequencies in ascending order and assign mode indices 1–6. Use the same model to compute the Debye characteristic temperature θ_D(T) for temperatures from 0 K to 300 K inclusive, with a step no larger than 10 K. The two results are written as structured CSV files and are evaluated by a hidden verifier against reference values.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Input parameters
All parameters are taken from Table I of the original work. The model uses the 7-parameter bond-bending force model for NaCl-structure. The force constants are given in units of (2e²/Vₐ) but the matrix elements in the Appendix are expressed in (e²/a³). Use the semilattice constant a (half of the cubic lattice constant) and atomic masses (in atomic mass units) as shown.

### KCl
- semilattice constant a = 3.1465 Å
- K mass = 39.0983 amu
- Cl mass = 35.453 amu
- α₁ = 2.7917
- β₁ = -0.1643
- α₂ = -0.0611
- γ₁' = 0.0348
- γ₂' = 0.2237
- γ₃' = -0.1834
- Z² = 0.5646

### KBr
- semilattice constant a = 3.299 Å
- K mass = 39.0983 amu
- Br mass = 79.904 amu
- α₁ = 3.0133
- β₁ = -0.1493
- α₂ = -0.0854
- γ₁' = 0.0428
- γ₂' = 0.3282
- γ₃' = -0.2745
- Z² = 0.5131

### KI
- semilattice constant a = 3.5325 Å
- K mass = 39.0983 amu
- I mass = 126.90447 amu
- α₁ = 3.0978
- β₁ = -0.1360
- α₂ = -0.1104
- γ₁' = 0.0256
- γ₂' = 0.4448
- γ₃' = -0.3242
- Z² = 0.4673

## Workflow steps

### Step 1: Compute phonon frequencies at high-symmetry points
- Role: scored
- Action: For each compound (KCl, KBr, KI), construct the 6×6 dynamical matrix using the provided 7-parameter bond-bending force model parameters (α1, β1, α2, γ1', γ2', γ3', Z²) and the lattice constant a. Solve the secular determinant |D(q) − ω²I| = 0 at the Γ, X, and L points to obtain all six phonon eigenfrequencies in THz. Sort each set of six frequencies in ascending order and assign mode indices 1–6. Write the results to phonon_frequencies.csv.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: Columns: compound (string: KCl, KBr, KI), qpoint_label (string: Gamma, X, L), mode_index (integer: 1–6 in ascending frequency order), frequency_THz (float).
- Scoring: scored by hidden verifier

### Step 2: Compute Debye characteristic temperature curve
- Role: scored (load-bearing)
- Action: For each compound, sample a dense uniform q-point mesh (at least 8×8×8) in the first Brillouin zone, compute all phonon eigenfrequencies using the same dynamical matrix, and construct the vibrational density of states g(ν). From g(ν) compute the lattice specific heat Cv(T) via Bose-Einstein statistics, then derive the temperature-dependent Debye temperature θD(T) by inverting the Debye Cv function (using standard reference tables or numerical root finding). Output θD(T) for temperatures T = 0 to 300 K inclusive, with a step no larger than 10 K, to debye_temperature.csv.
- Output file: `/app/outputs/debye_temperature.csv`
- Format: csv
- Contract: Columns: compound (string: KCl, KBr, KI), temperature_K (float), debye_temperature_K (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/debye_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Phonon frequencies of all six branches at the high-symmetry q-points Gamma, X, and L for each potassium halide.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `qpoint_label`, `mode_index`, `frequency_THz`
  - `columns_desc`:
    - `compound`: string, one of KCl, KBr, KI
    - `qpoint_label`: string, one of Gamma, X, L
    - `mode_index`: integer from 1 to 6, sorted by ascending frequency
    - `frequency_THz`: float, phonon frequency in THz

### debye_temperature.csv
- path: `/app/outputs/debye_temperature.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Debye characteristic temperature as a function of temperature for each potassium halide.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `temperature_K`, `debye_temperature_K`
  - `columns_desc`:
    - `compound`: string, one of KCl, KBr, KI
    - `temperature_K`: float, temperature in Kelvin, 0 to 300 inclusive, step ≤10 K
    - `debye_temperature_K`: float, Debye temperature in Kelvin

Notes: All necessary model parameters and lattice constants will be provided in the instruction document; no external data download is needed. The scoring compares the reported frequencies and Debye temperatures to hidden gold experimental references with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "qpoint_label",
          "mode_index",
          "frequency_THz"
        ],
        "columns_desc": {
          "compound": "string, one of KCl, KBr, KI",
          "qpoint_label": "string, one of Gamma, X, L",
          "mode_index": "integer from 1 to 6, sorted by ascending frequency",
          "frequency_THz": "float, phonon frequency in THz"
        }
      },
      "description": "Phonon frequencies of all six branches at the high-symmetry q-points Gamma, X, and L for each potassium halide."
    },
    {
      "file": "debye_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "temperature_K",
          "debye_temperature_K"
        ],
        "columns_desc": {
          "compound": "string, one of KCl, KBr, KI",
          "temperature_K": "float, temperature in Kelvin, 0 to 300 inclusive, step ≤10 K",
          "debye_temperature_K": "float, Debye temperature in Kelvin"
        }
      },
      "description": "Debye characteristic temperature as a function of temperature for each potassium halide."
    }
  ],
  "notes": "All necessary model parameters and lattice constants will be provided in the instruction document; no external data download is needed. The scoring compares the reported frequencies and Debye temperatures to hidden gold experimental references with tolerances."
}
```

## How you are scored
A hidden verifier independently scores each of the two output artifacts. For the phonon frequencies, it extracts the frequencies of selected optical and acoustic modes at the Γ and X points and compares them to withheld reference values. Credit is awarded based on how closely the computed values match the references within a prescribed tolerance. For the Debye temperature, the verifier reads θ_D at several specified temperatures, compares them to reference values within a tolerance, and checks physically required properties (monotonic decrease with temperature, non‑negative values). The final reward combines these scores: 60 % from the frequency match and 40 % from the Debye temperature match. Simply reporting the paper’s numbers is insufficient; the verifier expects the output to reflect a genuine computation of the model.
