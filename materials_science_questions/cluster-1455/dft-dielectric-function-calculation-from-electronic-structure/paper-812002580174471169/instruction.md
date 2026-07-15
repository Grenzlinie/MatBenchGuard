# DFT dielectric function calculation for wurtzite ZnO

## Problem background
Zinc monochalcogenides (ZnX, X=O, S, Se, Te) are II-VI semiconductors widely used in optoelectronics. Their optical properties—dielectric function, reflectivity, absorption coefficient—are often computed from first principles using density functional theory (DFT) within the local-density approximation (LDA). LDA systematically underestimates the band gap, causing a rigid shift of the calculated optical spectra towards lower energies. A simple pragmatic correction applies a **scissor shift** to the conduction bands, aligning the gap with the experimental value, and then recalculates the optical spectra. This task focuses on wurtzite ZnO (ZnO‑w), a representative case where the scissor‑shifted LDA spectra are expected to agree reasonably with experiment. Your goal is to compute the imaginary dielectric function ε₂ and the normal‑incidence reflectivity from an LDA band structure with a scissor shift for the **E⊥c** polarization (electric field perpendicular to the c axis), producing a table that can be directly compared with published reference spectra.

## Approach
The core idea is to perform a plane‑wave DFT‑LDA calculation for wurtzite ZnO using an open‑source code (Quantum ESPRESSO) with PAW pseudopotentials. Starting from the experimentally known crystal structure, a self‑consistent field (SCF) run gives the ground‑state charge density. A subsequent non‑self‑consistent (NSCF) calculation on a dense k‑point grid supplies the Kohn‑Sham eigenvalues and wavefunctions. From these, the imaginary part of the dielectric function ε₂(ω) is obtained by summing momentum‑matrix‑element transitions between occupied and empty states (the standard dipolar formula). The conduction‑band energies are then rigidly shifted upward so that the DFT band gap matches the experimental gap of 3.4 eV for ZnO‑w. The real part ε₁(ω) is derived via Kramers‑Kronig transformation, and the normal‑incidence reflectivity is computed from the complex refractive index. The whole workflow replaces the proprietary VASP code used in the original study with the publicly available Quantum ESPRESSO, keeping the method conceptually identical.

## Reproduction target
Produce a single CSV file `spectra.csv` with the following columns:
- `energy` (photon energy in eV)
- `epsilon2` (dimensionless imaginary part of the dielectric function)
- `reflectivity` (dimensionless reflectivity at normal incidence)
The energy range must cover **0 to 20 eV**, and the step size must be **≤ 0.1 eV**. The values must correspond to wurtzite ZnO after a rigid scissor shift of 3.4 eV has been applied to the LDA conduction bands, and must be the component perpendicular to the c axis (**E⊥c**). The file must have a header line and use comma separation.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials for Zn and O (LDA): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Prepare crystal structure for wurtzite ZnO
- Role: process
- Action: Generate an input file for Quantum ESPRESSO describing the wurtzite ZnO unit cell with experimental lattice parameters a=3.244 Å, c=5.027 Å, and internal parameter u=0.380. Use a Γ‑centered k‑point grid equivalent to 10×10×10.
- Evidence: none

### Step 2: Self‑consistent LDA calculation
- Role: process
- Action: Run a self‑consistent field (SCF) calculation with Quantum ESPRESSO using the above structure, LDA exchange‑correlation, the chosen PAW pseudopotentials, and a 10×10×10 k‑mesh. Obtain the charge density and ground‑state wavefunctions.
- Evidence: `/app/outputs/scf.out`

### Step 3: Non‑self‑consistent band‑structure and band‑gap determination
- Role: process
- Action: Perform a non‑self‑consistent (NSCF) calculation on a dense Γ‑centered k‑mesh (at least 20×20×20) to obtain Kohn‑Sham eigenvalues and wavefunctions along a path. Determine the direct band gap at the Γ point from the resulting eigenvalues.
- Evidence: `/app/outputs/nscf.out`

### Step 4: Compute dielectric function and optical spectra
- Role: scored (load-bearing)
- Action: Using the NSCF output, run the QE post‑processing tool (epsilon.x) to obtain the unbroadened imaginary dielectric function ε2(ω) for the **E⊥c** polarization (electric field perpendicular to the c axis) from momentum matrix elements. Apply a rigid scissor shift to align the band gap to the experimental value of 3.4 eV, recalculating ε2 accordingly. Then perform Kramers‑Kronig transformation to obtain the real part ε1(ω), followed by computation of reflectivity R(ω)=|(√ε−1)/(√ε+1)|². Generate spectra.csv with columns 'energy' (eV), 'epsilon2' (dimensionless), 'reflectivity' (dimensionless) for photon energies from 0 to 20 eV in steps no larger than 0.1 eV.
- Output file: `/app/outputs/spectra.csv`
- Format: csv
- Contract: CSV with header: energy,epsilon2,reflectivity. energy in eV (float), epsilon2 dimensionless (float), reflectivity dimensionless (float). 0–20 eV, step ≤0.1 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spectra.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spectra.csv
- path: `/app/outputs/spectra.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Imaginary dielectric function (epsilon2) and reflectivity as a function of photon energy for wurtzite ZnO after a rigid scissor shift of 3.4 eV.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `epsilon2`, `reflectivity`
  - `units`:
    - `energy`: eV
    - `epsilon2`: dimensionless
    - `reflectivity`: dimensionless

Notes: Scope is limited to the LDA‑calculated optical spectra for wurtzite ZnO. The checker will recompute epsilon2 and reflectivity at selected photon energies from this file and compare against hidden gold digitized from the paper's Fig. 5; relative tolerance of 20% per value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "epsilon2",
          "reflectivity"
        ],
        "units": {
          "energy": "eV",
          "epsilon2": "dimensionless",
          "reflectivity": "dimensionless"
        }
      },
      "description": "Imaginary dielectric function (epsilon2) and reflectivity as a function of photon energy for wurtzite ZnO after a rigid scissor shift of 3.4 eV."
    }
  ],
  "notes": "Scope is limited to the LDA‑calculated optical spectra for wurtzite ZnO. The checker will recompute epsilon2 and reflectivity at selected photon energies from this file and compare against hidden gold digitized from the paper's Fig. 5; relative tolerance of 20% per value."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that:
1. Checks that `spectra.csv` exists, has the correct header, and covers 0–20 eV with a step ≤ 0.1 eV.
2. Reads the columns and extracts the values of `epsilon2` and `reflectivity` at several characteristic photon energies (selected as important spectral features for wurtzite ZnO).
3. Compares each extracted value against a hidden reference derived from published experimental data, using relative tolerances that account for differences between DFT codes and pseudopotentials.
4. Computes a **reward** proportional to the fraction of checked values that fall within tolerance. The reward also includes a small bonus for meeting the format and energy‑grid requirements.

You are **not** required to hit a specific numeric target; the verifier expects values that are physically reasonable and consistent with a correct DFT‑LDA calculation with scissor shift.
