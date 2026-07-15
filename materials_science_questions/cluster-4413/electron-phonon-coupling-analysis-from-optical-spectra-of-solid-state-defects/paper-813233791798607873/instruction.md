# Electron-vibrational interaction parameter estimation from optical spectra

## Problem background
The electron–vibrational interaction (EVI) describes the coupling between electronic transitions and lattice vibrations in luminescent materials. For Ce³⁺-doped hexafluoride phosphors, the Huang–Rhys factor S, effective phonon energy ℏω, and zero‑phonon line energy E0 are key parameters that determine luminescence line shapes and the strength of the electron–lattice coupling. These parameters can be estimated from room‑temperature photoluminescence excitation and emission spectra using a single configurational coordinate model. This task reproduces the estimation of S and ℏω for three Ce³⁺-doped complex hexafluorides (LiMgBF6, Li2NaBF6, Li3BF6) from the observed Stokes shift and emission line width.

## Approach
In the single configurational coordinate model, the Stokes shift ΔE_S (the energy difference between the absorption and emission maxima) is related to the Huang–Rhys factor S and the effective phonon energy ℏω by the equation ΔE_S = (2S – 1)ℏω. The full width at half‑maximum (FWHM) of the emission band at temperature T is given by Γ(T) = √(8 ln 2) ℏω √(S coth(ℏω/(2k_B T))), where k_B is the Boltzmann constant. Given the measured ΔE_S and Γ(T) for each compound, these two coupled equations can be solved numerically to obtain S and ℏω. The coupling regime is then classified from the value of S: weak (S < 1), intermediate (1 ≤ S ≤ 5), or strong (S > 5). The required experimental inputs (ΔE_S and Γ(T) at room temperature) are provided for the three hexafluorides in the reproduction target below. The temperature is fixed to T = 300 K and k_B = 0.69503476 cm⁻¹/K.

## Reproduction target
Using the following room‑temperature experimental inputs (from the published photoluminescence spectra), estimate the EVI parameters for each compound and classify its coupling regime.

Inputs:
- LiMgBF6:Ce³⁺  → Stokes shift ΔE_S = 7296 cm⁻¹, emission FWHM Γ(T) = 5636 cm⁻¹
- Li2NaBF6:Ce³⁺  → Stokes shift ΔE_S = 9063 cm⁻¹, emission FWHM Γ(T) = 6300 cm⁻¹
- Li3BF6:Ce³⁺   → Stokes shift ΔE_S = 11906 cm⁻¹, emission FWHM Γ(T) = 5853 cm⁻¹

Temperature T = 300 K, Boltzmann constant k_B = 0.69503476 cm⁻¹/K.

Solve the two coupled equations numerically to obtain the Huang–Rhys factor S (dimensionless) and the effective phonon energy ℏω (in cm⁻¹). Classify the coupling regime as weak (S < 1), intermediate (1 ≤ S ≤ 5), or strong (S > 5) for each compound. Produce a single CSV file `/app/outputs/evi_parameters.csv` with one row per compound and columns: compound, S, hbar_omega, regime.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Solve EVI equations and classify coupling regime
- Role: scored (load-bearing)
- Action: Solve numerically the system of equations: Stokes shift ΔE_S = (2S - 1)ℏω and emission FWHM Γ(T) = √(8 ln 2) ℏω √(S coth(ℏω/(2kT))) for each of the three compounds (LiMgBF6, Li2NaBF6, Li3BF6) using the provided ΔE_S and Γ(T) values, temperature T = 300 K, and Boltzmann constant k_B = 0.69503476 cm⁻¹/K. Obtain the Huang–Rhys factor S and effective phonon energy ℏω (in cm⁻¹). Classify coupling regime as weak (S < 1), intermediate (1 ≤ S ≤ 5), or strong (S > 5). Write results to evi_parameters.csv.
- Output file: `/app/outputs/evi_parameters.csv`
- Format: csv
- Contract: Columns: compound (string), S (float, dimensionless), hbar_omega (float, cm⁻¹), regime (string, one of: weak, intermediate, strong). One row per compound: LiMgBF6, Li2NaBF6, Li3BF6.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/evi_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### evi_parameters.csv
- path: `/app/outputs/evi_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electron-vibrational interaction parameters (Huang–Rhys factor S, effective phonon energy ℏω) and coupling regime for LiMgBF6:Ce3+, Li2NaBF6:Ce3+, and Li3BF6:Ce3+ derived by solving the coupled Stokes-shift and FWHM equations.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `S`, `hbar_omega`, `regime`
  - `units`:
    - `S`: dimensionless
    - `hbar_omega`: cm^-1
    - `regime`: string (weak/intermediate/strong)

Notes: The input Stokes shifts ΔE_S and emission FWHM Γ(T) for each compound are provided in the task instruction. The agent must solve the equations numerically to obtain S and ℏω, then classify the regime. No raw spectral data extraction or band-shape modeling is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "evi_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "S",
          "hbar_omega",
          "regime"
        ],
        "units": {
          "S": "dimensionless",
          "hbar_omega": "cm^-1",
          "regime": "string (weak/intermediate/strong)"
        }
      },
      "description": "Electron-vibrational interaction parameters (Huang–Rhys factor S, effective phonon energy ℏω) and coupling regime for LiMgBF6:Ce3+, Li2NaBF6:Ce3+, and Li3BF6:Ce3+ derived by solving the coupled Stokes-shift and FWHM equations."
    }
  ],
  "notes": "The input Stokes shifts ΔE_S and emission FWHM Γ(T) for each compound are provided in the task instruction. The agent must solve the equations numerically to obtain S and ℏω, then classify the regime. No raw spectral data extraction or band-shape modeling is required."
}
```

## How you are scored
Your submitted evi_parameters.csv is evaluated by a hidden verifier. The verifier independently computes the correct S and ℏω from the same inputs using the same equations and compares your reported values to its reference within allowed tolerances. The regime string for each compound is checked against the classification derived from the reference S value. The verifier assigns a reward between 0.0 and 1.0 that reflects the accuracy of your results across the three compounds. The more compounds you solve correctly, the higher your score. Simply reporting the inputs, or providing a file that does not originate from a genuine numerical solution of the equations, will yield a low or zero reward.
