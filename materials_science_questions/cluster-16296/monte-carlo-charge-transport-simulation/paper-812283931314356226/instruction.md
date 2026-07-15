# Calibration of Effective Potential for Quantum Correction in AlGaN/GaN HEMT

## Problem background
AlGaN/GaN high-electron-mobility transistors (HEMTs) exhibit strong quantum confinement of electrons at the heterointerface due to the high sheet charge density from piezoelectric and spontaneous polarization. Accurately describing the electron density near the interface requires accounting for size‑quantization effects, which can be done by solving the self-consistent Schrödinger‑Poisson equations. An efficient alternative is the effective potential method, where the classical electrostatic potential is convolved with a Gaussian kernel whose width a0 controls the quantum correction. The effectiveness of this method depends on the choice of a0; the task is to calibrate a0 for a specific AlGaN/GaN HEMT structure by comparing electron density profiles from the effective potential approach with those from a full Schrödinger‑Poisson calculation.

## Approach
Implement a 1D Poisson‑Schrödinger solver for the HEMT structure: 15 nm doped Al0.2Ga0.8N layer, 5 nm unintentionally doped Al0.2Ga0.8N spacer, and 100 nm unintentionally doped GaN channel. The background doping concentration is 1e17 cm⁻³. First, solve the classical Poisson equation to obtain the electrostatic potential and the classical electron density. Second, self‑consistently solve the coupled Schrödinger and Poisson equations to produce the quantum‑mechanical electron density as a reference. Third, convolve the classical potential with a Gaussian kernel of width a0 = 3 Å to construct the effective potential, then compute the electron density from this effective potential. Finally, assemble the three density profiles (classical, effective potential, Schrödinger‑Poisson) on a uniform spatial grid perpendicular to the interface and output them as a CSV file.

## Reproduction target
Produce a CSV file named `step_01_density_profiles.csv` containing electron density as a function of position (in nm) for the classical solution, the effective potential method with a0 = 3 Å, and the self‑consistent Schrödinger‑Poisson solution. 

## Assets

- GaN/AlGaN material constants
- Python scientific stack: numpy

## Workflow steps

### Step 1: Classical Poisson solution
- Role: process
- Action: Solve the 1D Poisson equation for the given AlGaN/GaN HEMT structure to obtain the classical electrostatic potential and electron density profile.
- Evidence: `/app/outputs/classical_solution.npy`

### Step 2: Schrödinger-Poisson reference
- Role: process
- Action: Self-consistently solve the 1D Schrödinger and Poisson equations for the same HEMT structure to obtain the quantum-mechanical electron density profile.
- Evidence: `/app/outputs/sp_solution.npy`

### Step 3: Effective potential convolution
- Role: process
- Action: Convolve the classical potential with a Gaussian kernel of width a0=3 Å to obtain the effective potential, then compute the electron density using the effective potential.
- Evidence: `/app/outputs/effpot_density.npy`

### Step 4: Write density profiles
- Role: scored (load-bearing)
- Action: Collect the three computed density profiles (classical, effective potential, Schrödinger-Poisson) and write them to step_01_density_profiles.csv.
- Output file: `/app/outputs/step_01_density_profiles.csv`
- Format: csv
- Contract: CSV with columns: position_nm (float, position perpendicular to the interface in nm), classical_density (float, electron density in cm^-3), effective_density (float, electron density in cm^-3), schrodinger_poisson_density (float, electron density in cm^-3). Rows correspond to a uniform spatial grid.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_density_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_density_profiles.csv
- path: `/app/outputs/step_01_density_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file containing electron density profiles for the classical, effective potential (a0=3 Å), and Schrödinger-Poisson solutions.
- schema:
  - `type`: table
  - `required_columns`: `position_nm`, `classical_density`, `effective_density`, `schrodinger_poisson_density`
  - `units`:
    - `position_nm`: nm
    - `classical_density`: cm^{-3}
    - `effective_density`: cm^{-3}
    - `schrodinger_poisson_density`: cm^{-3}

Notes: The checker will recompute normalized error metrics (e.g., normalised root-mean-square deviation) between the effective potential density profile and the Schrödinger-Poisson profile, and verify that the classical density profile substantially deviates from the quantum ones.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_density_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "position_nm",
          "classical_density",
          "effective_density",
          "schrodinger_poisson_density"
        ],
        "units": {
          "position_nm": "nm",
          "classical_density": "cm^{-3}",
          "effective_density": "cm^{-3}",
          "schrodinger_poisson_density": "cm^{-3}"
        }
      },
      "description": "CSV file containing electron density profiles for the classical, effective potential (a0=3 Å), and Schrödinger-Poisson solutions."
    }
  ],
  "notes": "The checker will recompute normalized error metrics (e.g., normalised root-mean-square deviation) between the effective potential density profile and the Schrödinger-Poisson profile, and verify that the classical density profile substantially deviates from the quantum ones."
}
```

## How you are scored
A hidden verifier reads your `step_01_density_profiles.csv`. It recomputes a normalized error metric between the effective potential density profile and the Schrödinger‑Poisson density profile, and also checks that the classical density profile substantially deviates from the quantum ones. Each workflow stage contributes to a weighted final score. Simply reporting a number is not sufficient; the verifier evaluates the actual computed profiles. The reference profiles and tolerances used by the verifier are not disclosed in this instruction.
