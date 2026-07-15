# Superconducting Tc Estimation in V3B (B=Ni,Pd,Pt) via DFT and McMillan Formula

## Problem background
The superconducting transition temperature \(T_c\) varies among the isoelectronic A15 compounds V\(_3\)Ni, V\(_3\)Pd, and V\(_3\)Pt despite their similar crystal structures and electron count. Understanding the origin of this variation requires knowledge of the electronic structure near the Fermi level and the strength of the electron-phonon coupling. The paper addresses this by performing first-principles density functional theory (DFT) calculations of the band structure and density of states, and then estimating the electron-phonon coupling constant \(\lambda\) via the McMillan formula, linking the computed density of states at the Fermi level \(N(\epsilon_F)\) with the experimentally measured \(T_c\).

## Approach
The approach consists of two stages. First, for each compound, the crystal structure is prepared at the experimental lattice constant. A DFT calculation is performed with the GGA-PBE exchange-correlation functional to obtain a self-consistent charge density and the total density of states (DOS) on a fine energy grid. The DOS at the Fermi level \(N(\epsilon_F)\) is extracted from this calculation. Second, the McMillan formula for the superconducting transition temperature is used together with the experimental \(T_c\) values and a fixed logarithmic average phonon frequency to estimate the electron-phonon coupling constant \(\lambda\). The Coulomb pseudopotential \(\mu^*\) is computed from \(N(\epsilon_F)\) expressed in states per eV and per atom. Solving the McMillan equation numerically then yields \(\lambda\).

## Reproduction target
Produce a CSV file `dft_results.csv` containing, for each compound V\(_3\)Ni, V\(_3\)Pd, V\(_3\)Pt, the DFT-calculated density of states at the Fermi level \(N(\epsilon_F)\) (in states/Ry.cell) and the estimated electron-phonon coupling constant \(\lambda\) (dimensionless). The values must be derived from first-principles total DOS data (the evidence files `dos_V3*.csv`) and from the experimental superconducting critical temperatures \(T_c = 0.57~\text{K}\) (V\(_3\)Ni), \(0.08~\text{K}\) (V\(_3\)Pd), \(2.7~\text{K}\) (V\(_3\)Pt) using a fixed logarithmic average phonon frequency \(\omega_{\log}=180~\text{K}\).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT self-consistent and total DOS calculations
- Role: process
- Action: For each compound (V3Ni, V3Pd, V3Pt), prepare the A15 crystal structure using experimental lattice constants (4.710, 4.816, 4.808 Å) and run a self-consistent field (SCF) calculation followed by a non-SCF calculation to obtain the total density of states on a fine energy grid. Use the GGA-PBE exchange-correlation functional. Save the total DOS (energy in eV and DOS in states/eV) as CSV files: dos_V3Ni.csv, dos_V3Pd.csv, dos_V3Pt.csv.
- Evidence: `/app/outputs/dos_V3Ni.csv,dos_V3Pd.csv,dos_V3Pt.csv`

### Step 2: Extract N(ε_F) and estimate λ
- Role: scored (load-bearing)
- Action: Read the DOS CSV files from step_dft. For each compound, determine N(ε_F) as the DOS value at the Fermi energy (E=0) in states/eV, then convert to states/Ry.cell (multiply by 13.605693). Use the experimental superconducting critical temperatures Tc (0.57 K for V3Ni, 0.08 K for V3Pd, 2.7 K for V3Pt) and a fixed logarithmic average phonon frequency ω_log = 180 K. Compute the Coulomb pseudopotential μ* = 0.26 * N(ε_F) / (1 + N(ε_F)) where N(ε_F) is in states/eV·atom (convert total cell N to per atom by dividing by number of atoms in the unit cell). Numerically solve the McMillan formula Tc = (ω_log / 1.2) exp[ -1.04(1+λ) / (λ - μ*(1+0.62λ)) ] to find the electron-phonon coupling constant λ. Output a CSV file dft_results.csv with columns compound, N_EF (states/Ry.cell), lambda.
- Output file: `/app/outputs/dft_results.csv`
- Format: csv
- Contract: CSV with columns: compound (string: V3Ni, V3Pd, V3Pt), N_EF (float, states/Ry.cell), lambda (float, dimensionless). One row per compound.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.csv
- path: `/app/outputs/dft_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: DFT-calculated density of states at the Fermi level and the estimated electron-phonon coupling constant λ for V3Ni, V3Pd, V3Pt. The checker recomputes N(ε_F) from the raw DOS evidence files and then computes λ, comparing both to the paper's hidden gold with asymmetric tolerances (meeting or beating the target earns full credit).
- schema:
  - `type`: table
  - `required_columns`: `compound`, `N_EF`, `lambda`
  - `units`:
    - `N_EF`: states/Ry.cell
    - `lambda`: dimensionless

Notes: The raw total DOS CSV files (dos_V3Ni.csv, dos_V3Pd.csv, dos_V3Pt.csv) are required process evidence; the scored file dft_results.csv must match them self-consistently. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "N_EF",
          "lambda"
        ],
        "units": {
          "N_EF": "states/Ry.cell",
          "lambda": "dimensionless"
        }
      },
      "description": "DFT-calculated density of states at the Fermi level and the estimated electron-phonon coupling constant λ for V3Ni, V3Pd, V3Pt. The checker recomputes N(ε_F) from the raw DOS evidence files and then computes λ, comparing both to the paper's hidden gold with asymmetric tolerances (meeting or beating the target earns full credit)."
    }
  ],
  "notes": "The raw total DOS CSV files (dos_V3Ni.csv, dos_V3Pd.csv, dos_V3Pt.csv) are required process evidence; the scored file dft_results.csv must match them self-consistently. No gold values or tolerances are disclosed here."
}
```

## How you are scored
Your submission will be scored by a hidden verifier. The verifier reads the total DOS evidence files (`dos_V3Ni.csv`, `dos_V3Pd.csv`, `dos_V3Pt.csv`) produced in Step 1 and independently recomputes the density of states at the Fermi level \(N(\epsilon_F)\) from those raw data. It then uses the same McMillan procedure as in Step 2 to calculate \(\lambda\) and compares the recomputed values, as well as the values you reported in `dft_results.csv`, to hidden reference criteria. The scoring function rewards solutions whose computed \(N(\epsilon_F)\) and \(\lambda\) are consistent with the raw DOS data and are physically accurate, with errors penalized monotonically (meeting or beating the target earns full credit). Each compound (V\(_3\)Ni, V\(_3\)Pd, V\(_3\)Pt) contributes equally to the total score. You must ensure that your raw DOS evidence and your submitted `dft_results.csv` are self-consistent.
