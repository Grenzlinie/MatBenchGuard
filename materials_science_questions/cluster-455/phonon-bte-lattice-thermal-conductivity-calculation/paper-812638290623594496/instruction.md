# Lattice thermal conductivity of Bi2Se3 from phonon Boltzmann transport

## Problem background
Bi₂Se₃ is a layered topological insulator with highly anisotropic thermal properties. Its lattice thermal conductivity is critical for thermoelectric applications, yet its behaviour in thin films remains poorly understood. In bulk crystals, low-temperature thermal transport can be limited by lattice defects such as Se vacancies or Bi₂ intercalation layers. In thin films, phonon scattering with sample surfaces can further reduce heat conduction in the out-of-plane direction. This work aims to compute the lattice thermal conductivity from first principles and evaluate how scattering mechanisms and film thickness control the transport.

## Approach
The workflow uses first-principles density functional perturbation theory (DFPT) to obtain the harmonic and anharmonic phonon properties of Bi₂Se₃. Intrinsic phonon-phonon scattering rates are computed, and the single-mode relaxation-time approximation (SMA) is employed to solve the phonon Boltzmann transport equation. For bulk calculations, additional extrinsic scattering is included via Rayleigh point-defect scattering from Se vacancies and a finite-size boundary scattering model that accounts for intercalated Bi₂ layers acting as absorbing planes. For thin films, the finite-size model is applied to surface scattering (rough, fully absorbing surfaces) to compute the out-of-plane conductivity as a function of film thickness. The pipeline combines these scattering channels using Matthiessen's rule and renormalised velocities to extract the lattice thermal conductivity tensor.

## Reproduction target
Produce two independent results:

1. Bulk thermal conductivity: Compute the in-plane (κ∥) and out-of-plane (κ⊥) lattice thermal conductivity of Bi₂Se₃ as a function of temperature from 2 K to 400 K, using the single-mode approximation with intrinsic phonon-phonon scattering, Se-vacancy point-defect scattering (concentration 100 ppm), and boundary scattering from Bi₂ intercalation layers (average interlayer distance 5 µm, fully absorbing surfaces). Write the results to `bulk_thermal_conductivity.csv`.

2. Thin-film thermal conductivity: Compute the out-of-plane lattice thermal conductivity (κ⊥) of Bi₂Se₃ thin films at 300 K for film thicknesses of 18, 30, 53, 105, and 191 nm. Include intrinsic phonon scattering and surface boundary scattering (rough surfaces, absorption fraction f_a=1, reflection fraction f_r=0). Write the results to `thin_film_thermal_conductivity.csv`.

## Assets

- Quantum ESPRESSO suite (pw.x, ph.x, d3q.x, thermal2.x): https://www.quantum-espresso.org/
- SG15-ONCV norm‑conserving pseudopotentials (Bi, Se, scalar‑relativistic): http://www.quantum-simulation.org/potentials/sg15_oncv/
- Bi2Se3 crystal structure parameters

## Workflow steps

### Step 1: DFT structural relaxation
- Role: process
- Action: Perform relaxation of internal atomic coordinates of Bi2Se3 using the experimental lattice parameters (a=4.138 Å, c=28.64 Å) with Quantum ESPRESSO pw.x. Use PBE functional and scalar‑relativistic norm‑conserving pseudopotentials. The output is a relaxed geometry suitable for subsequent phonon calculations.
- Evidence: `/app/outputs/relax.log`

### Step 2: Harmonic phonon calculation
- Role: process
- Action: Compute harmonic force constants, phonon dispersion, and group velocities using Quantum ESPRESSO ph.x on a regular q‑point grid, starting from the relaxed structure of step_01. Born effective charges may be calculated but LO‑TO splitting can be omitted (screened by doping).
- Evidence: `/app/outputs/phonons.log`

### Step 3: Anharmonic third-order force constants
- Role: process
- Action: Compute third-order anharmonic force constants using the d3q.x module of Quantum ESPRESSO, employing the relaxed structure and the same q‑point grid as step_02.
- Evidence: `/app/outputs/d3q.log`

### Step 4: Intrinsic phonon relaxation times
- Role: process
- Action: Combine harmonic and anharmonic data to compute intrinsic phonon‑phonon scattering rates (linewidths / relaxation times) using the thermal2.x code or equivalent post‑processing, integrating over a fine q‑mesh.
- Evidence: `/app/outputs/lifetimes.npz`

### Step 5: Bulk thermal conductivity with defects
- Role: scored (load-bearing)
- Action: Using the intrinsic phonon lifetimes, group velocities, and frequencies from step_04, implement the single‑mode approximation (SMA) for lattice thermal conductivity. Add Rayleigh point‑defect scattering from Se vacancies at 100 ppm concentration. Add boundary scattering from intercalated Bi2 layers using the finite‑size model with characteristic length L_inter=5 µm and fully absorbing surfaces (f_a=1, f_r=0). Combine scattering rates via Matthiessen's rule, compute renormalized velocities, and evaluate in‑plane (κ∥) and out‑of‑plane (κ⊥) thermal conductivity for temperatures from 2 K to 400 K. Write the results to 'bulk_thermal_conductivity.csv'.
- Output file: `/app/outputs/bulk_thermal_conductivity.csv`
- Format: csv
- Contract: CSV with header: T, kappa_parallel, kappa_perp. T in K, kappa values in W/m·K. Rows covering 2 K to 400 K; finer spacing at low T (≤100 K) e.g. every 10 K, above every 50 K.
- Scoring: scored by hidden verifier

### Step 6: Out‑of‑plane thermal conductivity of thin films
- Role: scored (load-bearing)
- Action: Using the same intrinsic phonon data as step_04, apply the finite‑size boundary scattering model for thin films: for each thickness L in [18, 30, 53, 105, 191] nm, set phonon boundary scattering rate as τ_a⁻¹ = v_z/L (rough surface limit f_a=1, f_r=0). Combine boundary scattering with intrinsic scattering via Matthiessen's rule, use renormalized velocities, and compute the out‑of‑plane thermal conductivity κ⊥ at 300 K for each L. Write the results to 'thin_film_thermal_conductivity.csv'.
- Output file: `/app/outputs/thin_film_thermal_conductivity.csv`
- Format: csv
- Contract: CSV with header: thickness_nm, kappa_perp. thickness_nm integer, kappa_perp in W/m·K. Rows for thicknesses 18, 30, 53, 105, 191 nm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_thermal_conductivity.csv`
- `/app/outputs/thin_film_thermal_conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_thermal_conductivity.csv
- path: `/app/outputs/bulk_thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Temperature‑dependent bulk lattice thermal conductivity including contributions from Se vacancies and Bi2 intercalation boundary scattering.
- schema:
  - `type`: table
  - `required_columns`: `T`, `kappa_parallel`, `kappa_perp`
  - `units`:
    - `T`: K
    - `kappa_parallel`: W/m·K
    - `kappa_perp`: W/m·K

### thin_film_thermal_conductivity.csv
- path: `/app/outputs/thin_film_thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Out‑of‑plane lattice thermal conductivity of Bi2Se3 thin films as a function of film thickness at 300 K, with surface boundary scattering.
- schema:
  - `type`: table
  - `required_columns`: `thickness_nm`, `kappa_perp`
  - `units`:
    - `thickness_nm`: nm
    - `kappa_perp`: W/m·K

Notes: The hidden checker extracts values at specific temperatures (for bulk) and at the listed thicknesses (for thin films) and compares them to paper‑reported gold within appropriate tolerances. The agent must write the complete CSV files as described; no gold values or tolerances are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "kappa_parallel",
          "kappa_perp"
        ],
        "units": {
          "T": "K",
          "kappa_parallel": "W/m·K",
          "kappa_perp": "W/m·K"
        }
      },
      "description": "Temperature‑dependent bulk lattice thermal conductivity including contributions from Se vacancies and Bi2 intercalation boundary scattering."
    },
    {
      "file": "thin_film_thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_nm",
          "kappa_perp"
        ],
        "units": {
          "thickness_nm": "nm",
          "kappa_perp": "W/m·K"
        }
      },
      "description": "Out‑of‑plane lattice thermal conductivity of Bi2Se3 thin films as a function of film thickness at 300 K, with surface boundary scattering."
    }
  ],
  "notes": "The hidden checker extracts values at specific temperatures (for bulk) and at the listed thicknesses (for thin films) and compares them to paper‑reported gold within appropriate tolerances. The agent must write the complete CSV files as described; no gold values or tolerances are disclosed."
}
```

## How you are scored
A hidden verifier will independently read each of your output CSV files, extract specific entries (e.g., at selected temperatures or thicknesses), and compare them to hidden reference values with appropriate tolerances. The reward is a weighted combination of scores for the bulk and thin-film artifacts. Simply reporting the paper's numbers is not sufficient; you must execute the computational pipeline to produce results that agree with the hidden references within the expected tolerances, which account for differences in toolchains and numerical approximations.
