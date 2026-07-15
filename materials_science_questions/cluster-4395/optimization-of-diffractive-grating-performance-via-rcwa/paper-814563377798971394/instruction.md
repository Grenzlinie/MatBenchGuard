# Numerical investigation of guided-mode resonance in curved grating structures

## Problem background
Guided-mode resonance (GMR) occurs when a periodic waveguide couples an incident wave to a leaky waveguide mode, producing narrowband high-reflectivity filtering. Most GMR studies have focused on flat grating structures under plane-wave illumination. When the grating is curved, it is not obvious whether the coherent coupling that underpins GMR can be maintained, and if so, how the resonance properties—peak reflectivity and spectral width—vary with curvature. This task investigates curved grating waveguides to determine whether they support GMR and to quantify the curvature dependence of the reflection characteristics.

## Approach
The analysis is carried out with cylindrical-coordinate finite-difference time-domain (FDTD) simulations. A TE-polarized (Ez) resonant grating waveguide is modeled with the following refractive-index profile: core index = 2.1, upper cladding (air) index = 1.0, lower substrate index = 1.45. The flat grating has a pitch Λ0, a duty ratio of 1:1, a core thickness of 0.45Λ0, and a groove depth of 0.05Λ0. For curved cases the structure is bent to a radius ρ; the azimuthal unit-cell angle θ0 is set to approximately Λ0/ρ. An arc-shaped Ez source is launched from the inner region. The time-domain average Ez and Hθ are recorded at an outer monitor surface. After Fourier transformation, the radial Poynting vector is computed, normalized by the launched power spectrum to obtain transmittance T(λ), and reflectivity is taken as R(λ) = 1 − T(λ). Simulations are performed for the flat limit (ρ→∞) and at least two finite curvature radii (ρ = 8Λ0 and ρ = 2.9Λ0). From each reflectance spectrum the lowest-order GMR peak is identified, and its peak reflectivity and full-width at half-maximum (FWHM) bandwidth are extracted.

## Reproduction target
Produce two scored artifacts from the FDTD simulations:

1. `reflection_spectra.csv` – Reflection spectra for the flat and curved cases. Columns: `wavelength` (normalized wavelength λ/Λ0), `reflectivity_flat`, `reflectivity_rho8`, `reflectivity_rho2_9`. Additional columns for other radii are allowed.

2. `curvature_dependence.csv` – Extracted resonance properties. Columns: `curvature` (dimensionless, e.g., Λ0/ρ, with 0 for flat), `peak_reflectivity`, `bandwidth` (FWHM, normalized wavelength units). Include at least three rows covering the flat case and the two finite radii.

The spectra must contain a clear resonance peak, and the extracted quantities must reflect the variation with curvature.

## Assets

- MEEP FDTD solver (or equivalent open‑source cylindrical‑coordinate FDTD): https://meep.readthedocs.io
- Python scientific stack (numpy, scipy, pandas, matplotlib): numpy scipy pandas matplotlib

## Workflow steps

### Step 1: Cylindrical FDTD simulation and reflectance spectra
- Role: scored
- Action: Implement a cylindrical-coordinate FDTD simulation for the TE‑mode grating structure (pitch Λ0, duty ratio 1:1, core index 2.1, upper cladding 1.0, substrate index 1.45, core thickness 0.45Λ0, groove depth 0.05Λ0). Run simulations for the flat case (ρ → ∞) and for at least two finite curvature radii (ρ = 8Λ0 and ρ = 2.9Λ0), using an arc‑shaped Ez source at the inner region and absorbing/periodic boundaries. Record time‑domain average Ez and Hθ at the outer monitor surface, Fourier‑transform the signals, compute the radial component of the Poynting vector, normalise by the launched power spectrum to obtain transmittance T(λ), and derive reflectivity R(λ) = 1 − T(λ). Output the reflection spectra for all curvatures as a CSV file.
- Output file: `/app/outputs/reflection_spectra.csv`
- Format: csv
- Contract: CSV with header: wavelength (float, normalised wavelength λ/Λ0), reflectivity_flat (float, flat case), reflectivity_rho8 (float, ρ=8Λ0), reflectivity_rho2_9 (float, ρ=2.9Λ0). Additional columns for further radii are allowed but not required.
- Scoring: scored by hidden verifier

### Step 2: Extraction of peak reflectivity and bandwidth
- Role: scored
- Action: From reflection_spectra.csv, identify the lowest‑order guided‑mode resonance peak for each curvature, extract its peak reflectivity value and its full width at half maximum (FWHM, bandwidth). Output the results as a CSV file.
- Output file: `/app/outputs/curvature_dependence.csv`
- Format: csv
- Contract: CSV with header: curvature (float, dimensionless, e.g. Λ0/ρ; use 0 for flat), peak_reflectivity (float, dimensionless), bandwidth (float, FWHM in normalised wavelength units).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reflection_spectra.csv`
- `/app/outputs/curvature_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reflection_spectra.csv
- path: `/app/outputs/reflection_spectra.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Reflection spectra for the flat grating and two curved gratings (ρ=8Λ0, ρ=2.9Λ0). The checker verifies the presence of a distinct resonance peak and that the spectral shape varies systematically with curvature.
- schema:
  - `type`: table
  - `required_columns`: `wavelength`, `reflectivity_flat`, `reflectivity_rho8`, `reflectivity_rho2_9`
  - `units`:
    - `wavelength`: normalised wavelength λ/Λ0
    - `reflectivity_flat`: dimensionless
    - `reflectivity_rho8`: dimensionless
    - `reflectivity_rho2_9`: dimensionless

### curvature_dependence.csv
- path: `/app/outputs/curvature_dependence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Extracted peak reflectivity and FWHM bandwidth for each curvature. The checker verifies that the extracted quantities vary systematically with curvature.
- schema:
  - `type`: table
  - `required_columns`: `curvature`, `peak_reflectivity`, `bandwidth`
  - `units`:
    - `curvature`: dimensionless (Λ0/ρ or similar; 0 for flat)
    - `peak_reflectivity`: dimensionless
    - `bandwidth`: normalised wavelength units (FWHM)

Notes: The fundamental quantities are the computed spectra and the curvature‑dependence table. The checker uses structural criteria (peak presence, threshold crossing, monotonic trends) with tolerances derived from the paper‑reported behaviour; no absolute gold values are disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reflection_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength",
          "reflectivity_flat",
          "reflectivity_rho8",
          "reflectivity_rho2_9"
        ],
        "units": {
          "wavelength": "normalised wavelength λ/Λ0",
          "reflectivity_flat": "dimensionless",
          "reflectivity_rho8": "dimensionless",
          "reflectivity_rho2_9": "dimensionless"
        }
      },
      "description": "Reflection spectra for the flat grating and two curved gratings (ρ=8Λ0, ρ=2.9Λ0). The checker verifies the presence of a distinct resonance peak and that the spectral shape varies systematically with curvature."
    },
    {
      "file": "curvature_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "curvature",
          "peak_reflectivity",
          "bandwidth"
        ],
        "units": {
          "curvature": "dimensionless (Λ0/ρ or similar; 0 for flat)",
          "peak_reflectivity": "dimensionless",
          "bandwidth": "normalised wavelength units (FWHM)"
        }
      },
      "description": "Extracted peak reflectivity and FWHM bandwidth for each curvature. The checker verifies that the extracted quantities vary systematically with curvature."
    }
  ],
  "notes": "The fundamental quantities are the computed spectra and the curvature‑dependence table. The checker uses structural criteria (peak presence, threshold crossing, monotonic trends) with tolerances derived from the paper‑reported behaviour; no absolute gold values are disclosed to the agent."
}
```

## How you are scored
A hidden verifier reads your two CSV files and evaluates them against structural criteria derived from the original study. For `reflection_spectra.csv` it checks that each spectrum shows a distinct resonance peak near the expected region and that the reflectivity deviates significantly from the baseline. For `curvature_dependence.csv` it inspects the trends: peak reflectivity and bandwidth must vary systematically with curvature. The verifier combines the scores from both stages into a single reward. The verifier examines the computed data; simply reporting numbers without a genuine simulation run will not pass the check.
