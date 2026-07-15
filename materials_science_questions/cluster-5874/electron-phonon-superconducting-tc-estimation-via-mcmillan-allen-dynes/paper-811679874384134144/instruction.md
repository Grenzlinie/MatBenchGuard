# Electron-Phonon Superconducting Tc Estimation via McMillan-Allen-Dynes

## Problem background
Superconductivity in elemental solids at extreme conditions is often studied via first-principles methods. This task addresses the electron-phonon mechanism in the high-pressure fcc phase of boron. The goal is to compute the electron-phonon coupling strength (quantified by the Hopfield parameter η) and the resulting superconducting critical temperature Tc, using a combination of self-consistent full-potential linearized augmented plane-wave (LAPW) electronic structure calculations, the rigid-muffin-tin (RMT) approximation, and the McMillan equation for Tc. The computed quantities provide a first-principles estimate of whether and how strongly boron may superconduct at pressures around 300 GPa.

## Approach
The core idea is to perform a self-consistent LAPW calculation for fcc boron at a fixed high-pressure lattice constant to obtain the electronic density of states at the Fermi level, its angular-momentum components inside the muffin-tin spheres, and the single-scatterer densities of states and scattering phase shifts. These quantities are then fed into the RMT formula to compute the total Hopfield parameter η. From η, the electron-phonon coupling constant λ is derived using the boron atomic mass and an assumed range of RMS phonon frequencies. Finally, the McMillan equation (the widely used approximate formula for Tc) is evaluated over a grid of phonon frequencies and Coulomb pseudopotential values to produce Tc as a function of these two input parameters. The workflow consists of three stages: (1) LAPW calculation, (2) η computation, (3) Tc computation. The fcc crystal structure and the required lattice parameter are specified; no external datasets are needed—the physics inputs are the known boron atomic mass and the fixed pressure/lattice constant.

## Reproduction target
Use the open-source Elk code (or another LAPW implementation) to perform a self-consistent calculation for fcc boron at lattice constant a = 4.60 a.u. (which corresponds to a pressure of approximately 307 GPa). From the electronic structure output, compute the total Hopfield parameter η and write it, together with the lattice constant and pressure, to `/app/outputs/hopfield_eta.csv`. Subsequently, compute the electron-phonon coupling λ and evaluate Tc via the McMillan equation for a grid of RMS phonon frequencies ω ranging from 1200 K to 1400 K (step 50 K) and Coulomb pseudopotential μ* ranging from 0.09 to 0.13 (step 0.01). Store the resulting Tc values in `/app/outputs/tc_vs_params.csv`.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.io/

## Workflow steps

### Step 1: Run self-consistent LAPW calculation for fcc B
- Role: process
- Action: Perform a self-consistent full-potential LAPW calculation for fcc boron at the lattice constant a=4.60 a.u. using an open-source LAPW code (e.g., Elk). The calculation must produce the total density of states at the Fermi energy N(E_F), the angular-momentum-resolved densities of states inside the muffin-tin spheres (N_s, N_p, N_d), the single-scatterer densities of states N_l^(1), and the scattering phase shifts δ_l. Save these quantities in a structured file for later post-processing.
- Evidence: `/app/outputs/lapw_output.json`

### Step 2: Compute Hopfield parameter η
- Role: scored
- Action: Using the LAPW outputs from the previous step (total and angular-momentum-resolved DOS, single-scatterer DOS, phase shifts), compute the total Hopfield parameter η and write a CSV file with the lattice constant (a.u.), pressure (GPa, which can be taken as 307 GPa from the paper's reported equation of state), and the total η in eV/Å^2.
- Output file: `/app/outputs/hopfield_eta.csv`
- Format: csv
- Contract: Columns: lattice_constant (float), pressure_gpa (float), eta_total_eV_Ang2 (float). One data row.
- Scoring: scored by hidden verifier

### Step 3: Compute superconducting Tc
- Role: scored
- Action: Calculate the electron-phonon coupling constant λ = η_total / (M ⟨ω^2⟩) using the boron atomic mass (10.811 u) and a range of rms phonon frequencies ⟨ω⟩ from 1200 K to 1400 K (step 50 K). Then evaluate the McMillan equation (Tc = (⟨ω⟩/1.45) exp[ -1.04(1+λ) / (λ - μ*(1+0.62λ)) ]) for Coulomb pseudopotential μ* from 0.09 to 0.13 (step 0.01). Output a CSV file with columns omega_K, mu_star, Tc_K.
- Output file: `/app/outputs/tc_vs_params.csv`
- Format: csv
- Contract: Columns: omega_K (float), mu_star (float), Tc_K (float). Rows covering all combinations of omega in 1200..1400 step 50 and mu* in 0.09..0.13 step 0.01.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hopfield_eta.csv`
- `/app/outputs/tc_vs_params.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hopfield_eta.csv
- path: `/app/outputs/hopfield_eta.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed total Hopfield parameter η for fcc boron at a=4.60 a.u. (307 GPa).
- schema:
  - `type`: table
  - `required_columns`: `lattice_constant`, `pressure_gpa`, `eta_total_eV_Ang2`

### tc_vs_params.csv
- path: `/app/outputs/tc_vs_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Superconducting critical temperature Tc as a function of RMS phonon frequency and Coulomb pseudopotential, covering ω=1200..1400 K and μ*=0.09..0.13.
- schema:
  - `type`: table
  - `required_columns`: `omega_K`, `mu_star`, `Tc_K`

Notes: The checker verifies the reported η_total against a hidden reference value and checks Tc at a specific (ω,μ*) point and overall monotonic trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hopfield_eta.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice_constant",
          "pressure_gpa",
          "eta_total_eV_Ang2"
        ]
      },
      "description": "Computed total Hopfield parameter η for fcc boron at a=4.60 a.u. (307 GPa)."
    },
    {
      "file": "tc_vs_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega_K",
          "mu_star",
          "Tc_K"
        ]
      },
      "description": "Superconducting critical temperature Tc as a function of RMS phonon frequency and Coulomb pseudopotential, covering ω=1200..1400 K and μ*=0.09..0.13."
    }
  ],
  "notes": "The checker verifies the reported η_total against a hidden reference value and checks Tc at a specific (ω,μ*) point and overall monotonic trends."
}
```

## How you are scored
A hidden verifier will inspect the two output files and assign a score based on the correctness and completeness of the artifacts. For `hopfield_eta.csv`, the verifier will check that the file contains the required columns and a single data row, and will compare the reported η against a reference value using a tolerance appropriate for a re-run with a different LAPW code. For `tc_vs_params.csv`, the verifier will verify that the grid covers all combinations of ω and μ* as specified, that Tc increases monotonically with both ω and μ*, and will compare the computed Tc at a representative (ω, μ*) point against a hidden reference. The final reward is a weighted combination of these checks; simply reporting numbers is insufficient—the underlying workflow must produce the outputs from a genuine LAPW calculation.
