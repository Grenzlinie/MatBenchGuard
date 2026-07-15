# First-principles Electron-Phonon Coupling and Tc in Alkali-Doped Fullerides

## Problem background
Alkali-doped fullerides A3C60 (A=K, Rb, Cs) form a prominent family of superconductors where the interplay of narrow molecular bands, high-frequency phonons, and electron correlations governs the superconducting transition temperature Tc. First-principles calculations based on density functional theory and density functional perturbation theory yield the electronic structure, phonon frequencies, and electron-phonon matrix elements that are essential inputs for estimating Tc. Reproducing these computed quantities enables quantitative analysis of how the phonon-mediated pairing varies with the alkali metal.

## Approach
The workflow employs plane-wave pseudopotential density functional theory (DFT) within the local density approximation (LDA) using Quantum ESPRESSO. For each compound (K3C60, Rb3C60, Cs3C60 at 7 kbar), the atomic positions are relaxed at fixed experimental lattice constants. The Kohn-Sham electronic structure and density of states are computed to obtain the Fermi level and N(0). Phonon dynamical matrices are then calculated via density functional perturbation theory (DFPT) on a 2×2×2 q-point grid, and the Γ-point Hg-derived mode frequencies are extracted. Electron-phonon matrix elements for the partially occupied t1u bands are evaluated on a (4×4×4) × (2×2×2) k×q grid. From these, the energy-dependent coupling coefficients λ_N(0), λ_N(ξ), ω_ln,N(0), and ω_ln,N(ξ) are derived using the Allen-Dynes definitions that explicitly treat energy conservation. Finally, the superconducting transition temperature Tc is estimated with the Allen-Dynes modified McMillan formula using λ_N(ξ) and ω_ln,N(ξ) (Coulomb pseudopotential μ* = 0). The full SCDFT gap equation is not required; the task captures the essential trends using the DFT/DFPT pipeline and the Allen-Dynes formula.

## Reproduction target
For the three compounds K3C60, Rb3C60, and Cs3C60 (at 7 kbar), compute and output:
- /app/outputs/phonon_frequencies.csv: the Γ-point frequencies (in cm⁻¹) of the eight fivefold-degenerate Hg-derived phonon modes (labelled Hg(1) through Hg(8)).
- /app/outputs/ep_coupling.csv: the electron-phonon coupling constants λ_N(0), λ_N(ξ), ω_ln,N(0), ω_ln,N(ξ), and the Tc (K) computed from the Allen-Dynes modified McMillan formula with λ_N(ξ) and ω_ln,N(ξ) (μ* = 0).
The goal is to faithfully execute the DFT/DFPT procedure and extract the parameters that determine the superconducting properties, without relying on precomputed results.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Perform DFT geometry optimization for fcc A3C60 (A=K,Rb,Cs) using LDA with norm-conserving pseudopotentials and the reported lattice constants (K3C60: 14.208 Å, Rb3C60: 14.404 Å, Cs3C60 at 7 kbar: 14.740 Å). Relax atomic positions until forces are converged.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Electronic structure and DOS
- Role: process
- Action: Compute Kohn-Sham eigenvalues and the density of states (DOS) for the relaxed structures. Extract the Fermi level and the DOS at the Fermi level N(0).
- Evidence: `/app/outputs/scf.log`

### Step 3: Phonon calculation (DFPT)
- Role: process
- Action: Calculate phonon dynamical matrices and frequencies using density functional perturbation theory from the Kohn-Sham states.
- Evidence: `/app/outputs/phonon.log`

### Step 4: Extract Hg phonon frequencies
- Role: scored (load-bearing)
- Action: From the computed Γ-point phonon frequencies, identify the eight fivefold-degenerate Hg-derived modes (Hg(1) to Hg(8)) for each compound and record one representative frequency (in cm⁻¹) per mode per compound.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: compound, mode, frequency_cm1
- Scoring: scored by hidden verifier

### Step 5: Electron-phonon matrix elements
- Role: process
- Action: Compute the electron-phonon matrix elements for the partially occupied t1u bands using the previously obtained wavefunctions and phonon eigenvectors.
- Evidence: `/app/outputs/epw.log`

### Step 6: Electron-phonon coupling parameters and Tc
- Role: scored (load-bearing)
- Action: From the electron-phonon matrix elements, Kohn-Sham eigenvalues, and phonon frequencies, compute the coupling coefficients λ_N(0), λ_N(ξ), ω_ln,N(0), and ω_ln,N(ξ) using the Allen-Dynes energy-dependent definitions, then compute the superconducting transition temperature Tc (in K) using the Allen-Dynes modified McMillan formula with λ_N(ξ) and ω_ln,N(ξ) (Coulomb pseudopotential μ* = 0). Output these values for each compound.
- Output file: `/app/outputs/ep_coupling.csv`
- Format: csv
- Contract: compound, lambda_N0, lambda_Nxi, omega_ln_N0, omega_ln_Nxi, Tc_MAD_K
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/ep_coupling.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Γ-point frequencies of the eight Hg-derived modes for each compound. The checker compares each frequency to the paper's reported ranges (Table II) within a tolerance and verifies the alkali-metal dependence.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `mode`, `frequency_cm1`
  - `units`:
    - `frequency_cm1`: cm⁻¹

### ep_coupling.csv
- path: `/app/outputs/ep_coupling.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electron-phonon coupling coefficients and Allen-Dynes Tc. The checker compares λ and ωln values to paper Table I within a relative tolerance and verifies that Tc_MAD_K increases monotonically from K3C60 to Rb3C60 to Cs3C60 and lies within a factor of 2 of the paper's SCDFT Tc.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `lambda_N0`, `lambda_Nxi`, `omega_ln_N0`, `omega_ln_Nxi`, `Tc_MAD_K`
  - `units`:
    - `lambda_N0`: dimensionless
    - `lambda_Nxi`: dimensionless
    - `omega_ln_N0`: K
    - `omega_ln_Nxi`: K
    - `Tc_MAD_K`: K

Notes: The full SCDFT gap equation solver is omitted from the reproduction scope because it relies on a non-public custom code. The essential alkali-metal dependence of Tc is captured by the Allen-Dynes formula using the energy-dependent coupling parameters λ_N(ξ) and ω_ln,N(ξ), which are derived from the DFT/DFPT results. The electron-electron kernel K^el and the full SCDFT Tc are not required.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "mode",
          "frequency_cm1"
        ],
        "units": {
          "frequency_cm1": "cm⁻¹"
        }
      },
      "description": "Γ-point frequencies of the eight Hg-derived modes for each compound. The checker compares each frequency to the paper's reported ranges (Table II) within a tolerance and verifies the alkali-metal dependence."
    },
    {
      "file": "ep_coupling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "lambda_N0",
          "lambda_Nxi",
          "omega_ln_N0",
          "omega_ln_Nxi",
          "Tc_MAD_K"
        ],
        "units": {
          "lambda_N0": "dimensionless",
          "lambda_Nxi": "dimensionless",
          "omega_ln_N0": "K",
          "omega_ln_Nxi": "K",
          "Tc_MAD_K": "K"
        }
      },
      "description": "Electron-phonon coupling coefficients and Allen-Dynes Tc. The checker compares λ and ωln values to paper Table I within a relative tolerance and verifies that Tc_MAD_K increases monotonically from K3C60 to Rb3C60 to Cs3C60 and lies within a factor of 2 of the paper's SCDFT Tc."
    }
  ],
  "notes": "The full SCDFT gap equation solver is omitted from the reproduction scope because it relies on a non-public custom code. The essential alkali-metal dependence of Tc is captured by the Allen-Dynes formula using the energy-dependent coupling parameters λ_N(ξ) and ω_ln,N(ξ), which are derived from the DFT/DFPT results. The electron-electron kernel K^el and the full SCDFT Tc are not required."
}
```

## How you are scored
A hidden verifier will score your submission automatically. The verifier inspects /app/outputs/phonon_frequencies.csv and /app/outputs/ep_coupling.csv. For phonon frequencies, each mode's frequency is checked to lie within an expected range derived from published measurements and calculations. For the electron-phonon coupling parameters, the values of λ and ωln are compared against reference data within a relative tolerance. Additionally, the verifier checks whether the computed Tc values across the three alkali metals form a physically consistent pattern (e.g., respecting the known volume dependence). The final reward (0–1) is a weighted sum of the scores from each artifact. A submitted value that does not result from executing the required DFT/DFPT pipeline will not pass the checks, even if it numerically matches a reference.
