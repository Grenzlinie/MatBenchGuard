# RCWA-Based Transmittance of Metallic Crossed Gratings with Finite-Substrate Correction

## Problem background
Metallic crossed gratings consisting of periodic arrays of metal dots (capacitive grids) or holes (inductive grids) exhibit resonant transmission features in the mid-infrared due to coupling of incident light into surface plasma waves (SPWs). Rigorous coupled-wave analysis (RCWA) can model these gratings, but a key challenge is correctly accounting for the finite thickness of the silicon substrate, which introduces multiple incoherent reflections that modify the transmittance. This task focuses on computing the normal-incidence transmittance spectrum of a capacitive gold dot grating on a silicon substrate and investigating how the transmittance at a fixed wavelength depends on the dot fill factor, using RCWA with a finite-substrate correction.

## Approach
The approach uses a vector diffraction method (RCWA) to solve Maxwell's equations for a crossed grating with circular gold scatterers on a silicon substrate. First, the RCWA solver computes the diffraction efficiencies (η^i and η^s) for all propagating orders under the infinite-substrate assumption. Then, the finite-substrate model (FSM) is applied: the diffracted orders inside the substrate undergo multiple incoherent reflections at the back surface. The corrected zeroth-order transmittance is obtained by solving a linear system involving the diffraction-efficiency matrix, the back-surface reflectances, and the initial incident intensity. The workflow repeats this calculation over wavelengths 2–5 μm to produce a transmittance spectrum, and then performs a fill-factor study at λ=4.3 μm by varying the dot diameter while keeping pitch and thickness fixed.

## Reproduction target
Compute the finite-substrate-corrected transmittance spectrum (2–5 μm) for a capacitive grating with pitch Λ=1.24 μm, dot diameter d=0.75 μm, gold thickness h=0.1 μm, gold optical constants from Palik, and silicon index n=3.44, using an open-source RCWA implementation. Subsequently, for a series of dot diameters (0.4–0.9 μm, step 0.05 μm), compute the transmittance at λ=4.3 μm and output the fill factor (πd²/(4Λ²)) versus transmittance. Output two CSV files: transmittance_spectrum.csv and fill_factor_transmittance.csv.

## Assets

- Gold complex refractive index (Palik, 1985): https://refractiveindex.info
- Silicon refractive index (constant n=3.44)
- Open-source RCWA solver (e.g., S4): https://github.com/victorliu/S4

## Workflow steps

### Step 1: RCWA Simulation (Infinite Substrate) for Spectrum
- Role: process
- Action: Set up and run an RCWA solver for a crossed grating of circular gold dots on a silicon substrate with pitch 1.24 μm, dot diameter 0.75 μm, and thickness 0.1 μm. Use gold complex refractive index from Palik and silicon index 3.44. Compute diffraction efficiencies for all propagating orders in the substrate (η^i and η^s) over the wavelength range 2–5 μm with step ≤0.025 μm for normal incidence (polarization along x-axis).
- Evidence: `/app/outputs/rcwa_log.txt`

### Step 2: Finite-Substrate Corrected Transmittance Spectrum
- Role: scored (load-bearing)
- Action: Apply the finite-substrate model (incoherent multiple reflections) to the RCWA diffraction efficiencies from the previous step. Compute the vector D^s using the scattering-matrix results and Fresnel coefficients, then obtain the zeroth-order diffracted intensity and multiply by the back-surface transmittance τ^s_00 to yield the corrected transmittance spectrum. Output the spectrum for wavelengths 2–5 μm.
- Output file: `/app/outputs/transmittance_spectrum.csv`
- Format: csv
- Contract: CSV with columns: wavelength_um (float, wavelength in μm, step ≤0.025), transmittance (float, fraction between 0 and 1).
- Scoring: scored by hidden verifier

### Step 3: RCWA Simulations for Fill Factor Study
- Role: process
- Action: Repeat the RCWA simulation for capacitive gratings with the same pitch (1.24 μm), thickness (0.1 μm), and materials, but vary the dot diameter from 0.4 to 0.9 μm in steps of 0.05 μm. For each diameter, compute the diffraction efficiencies η^i and η^s at the single wavelength λ=4.3 μm using the same RCWA settings (normal incidence, polarization along x-axis).
- Evidence: `/app/outputs/fillfactor_rcwa_log.txt`

### Step 4: Transmittance at 4.3 μm vs Fill Factor
- Role: scored
- Action: For each diameter from the previous step, apply the finite-substrate model to compute the zeroth-order transmittance at 4.3 μm. Compute the fill factor as (π/4)*(d/1.24)^2. Output the fill factor and corresponding transmittance.
- Output file: `/app/outputs/fill_factor_transmittance.csv`
- Format: csv
- Contract: CSV with columns: fill_factor (float, 0–1), transmittance_at_4.3um (float, 0–1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transmittance_spectrum.csv`
- `/app/outputs/fill_factor_transmittance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transmittance_spectrum.csv
- path: `/app/outputs/transmittance_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Zeroth-order transmittance spectrum of the capacitive grid with finite-substrate correction, covering 2–5 μm. The checker compares transmittance at key spectral features (e.g., SPW peak, Wood's anomaly) against paper-derived tolerances.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_um`, `transmittance`
  - `units`:
    - `wavelength_um`: μm
    - `transmittance`: fraction (0 to 1)

### fill_factor_transmittance.csv
- path: `/app/outputs/fill_factor_transmittance.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Transmittance at λ=4.3 μm as a function of dot fill factor. The checker verifies monotonic decrease of transmittance with fill factor and that values are within ±0.05 of the expected trend.
- schema:
  - `type`: table
  - `required_columns`: `fill_factor`, `transmittance_at_4.3um`
  - `units`:
    - `fill_factor`: dimensionless (0 to 1)
    - `transmittance_at_4.3um`: fraction (0 to 1)

Notes: The agent must run RCWA with finite-conductivity metals and the scattering-matrix algorithm. Use at least N=10 Fourier harmonics and a 100×100 unit-cell grid as per the paper's convergence discussion. The finite-substrate model corrects for incoherent multiple reflections in the thick silicon substrate.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transmittance_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_um",
          "transmittance"
        ],
        "units": {
          "wavelength_um": "μm",
          "transmittance": "fraction (0 to 1)"
        }
      },
      "description": "Zeroth-order transmittance spectrum of the capacitive grid with finite-substrate correction, covering 2–5 μm. The checker compares transmittance at key spectral features (e.g., SPW peak, Wood's anomaly) against paper-derived tolerances."
    },
    {
      "file": "fill_factor_transmittance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "fill_factor",
          "transmittance_at_4.3um"
        ],
        "units": {
          "fill_factor": "dimensionless (0 to 1)",
          "transmittance_at_4.3um": "fraction (0 to 1)"
        }
      },
      "description": "Transmittance at λ=4.3 μm as a function of dot fill factor. The checker verifies monotonic decrease of transmittance with fill factor and that values are within ±0.05 of the expected trend."
    }
  ],
  "notes": "The agent must run RCWA with finite-conductivity metals and the scattering-matrix algorithm. Use at least N=10 Fourier harmonics and a 100×100 unit-cell grid as per the paper's convergence discussion. The finite-substrate model corrects for incoherent multiple reflections in the thick silicon substrate."
}
```

## How you are scored
Your submitted CSV files will be evaluated by a hidden verifier. Each scored artifact is checked independently: the spectrum CSV is compared to reference transmittance values at key spectral features (SPW peaks, Wood's anomaly dips) with preset tolerances; the fill-factor CSV is checked for a monotonic decrease in transmittance with increasing fill factor and for agreement with a reference trend within allowed bounds. Structure and format compliance (correct columns, header names, no extra data) is also verified. The verifier computes a combined reward (0–1) based on the weighted results of these checks. Simply reporting known numbers without executing the full RCWA pipeline will not satisfy the checks.
