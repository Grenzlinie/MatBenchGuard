# FDTD Simulation of Ultranarrow EIT in Gold Grating Multilayer Nanosystem

## Problem background
Realizing ultranarrow electromagnetically induced transparency (EIT) in solid‑state nanostructures is important for applications such as slow light, sensing, and metamaterials. This work proposes a nanosystem consisting of a gold grating on a three‑layer waveguide that can produce an ultranarrow spectral EIT peak via destructive interference between a Fabry‑Pérot resonance and a waveguide mode. The central result is demonstrated through finite‑difference time‑domain (FDTD) simulations of the reflection spectra.

## Approach
The nanosystem (referred to as nanosystem I) consists of an Au grating of period P, slit width a, and thickness t placed on top of a three‑layer waveguide: a fluoropolymer layer (refractive index n1, thickness d1), a ZnO‑doped SiO₂ layer (n2, d2), and a fluoropolymer substrate (n3, d3). The gold permittivity is described by a Drude–Lorentz model with five parameters that capture the interband transitions in the visible and near‑infrared. The EIT phenomenon arises from destructive interference between a broadband Fabry‑Pérot resonance (acting as a bright mode) and a narrow waveguide mode (dark mode) that is indirectly excited through coupling with the grating. The task is to reproduce the FDTD‑simulated reflection spectra for two incident angles: normal incidence (θ=0°) and oblique incidence (θ=5°), using an open‑source FDTD solver such as MEEP. p‑polarized plane waves illuminate the structure from the grating side, and the reflectance as a function of wavelength is recorded. The Au Drude–Lorentz parameters and all geometric dimensions are specified in the workflow steps.

## Reproduction target
Produce the raw reflection spectrum for nanosystem I at normal incidence (θ=0°) over the wavelength range 700–750 nm, and at oblique incidence (θ=5°) over 670–700 nm. Each spectrum must be saved as a CSV file with columns for wavelength (in nm) and reflectance (dimensionless, 0–1). The verifier will analyze each spectrum to identify the EIT peak—a sharp local maximum in reflectance—and extract its central wavelength and full width at half maximum (FWHM). The objective is that the extracted linewidths are consistent with the ultranarrow EIT phenomenon, i.e., the peaks are exceptionally narrow. No self‑reported metrics will be accepted; the checker recomputes these quantities from the raw CSV data.

## Assets

- Open‑source FDTD solver (e.g., MEEP): https://meep.readthedocs.io

## Workflow steps

### Step 1: FDTD simulation – normal incidence
- Role: scored (load-bearing)
- Action: Run an FDTD simulation of the nanosystem consisting of an Au grating (period P=500 nm, slit width a=100 nm, thickness t=419 nm) on a three-layer waveguide: top fluoropolymer (n1=1.34, d1=700 nm), middle ZnO‑doped SiO2 (n2=2.198, d2=100 nm), bottom fluoropolymer substrate (n3=1.34, sufficiently thick, e.g., 500 nm). Use the Drude‑Lorentz model for Au with parameters εr=5.97, ωp0=1.33e16 rad/s, γ0=9.87e13 rad/s, Ω0=4.08e15 rad/s, Γ0=6.58e14 rad/s, Δε0=1.09. Incident light: p‑polarized plane wave at normal incidence (θ=0°) from the grating side. Compute the reflection spectrum over the wavelength range 700–750 nm with at least 500 points. Save as a CSV with columns 'wavelength_nm' (float) and 'reflectance' (float, dimensionless, 0–1).
- Output file: `/app/outputs/reflection_spectrum_normal.csv`
- Format: csv
- Contract: CSV with header row, two columns: wavelength_nm (float) and reflectance (float). At least 500 wavelength points covering 700–750 nm.
- Scoring: scored by hidden verifier

### Step 2: FDTD simulation – oblique incidence 5°
- Role: scored
- Action: Run an FDTD simulation with the same geometry and Au model as Step 1, except incident angle θ=5°. Compute the reflection spectrum over 670–700 nm with at least 500 points. Save as a CSV with the same two columns.
- Output file: `/app/outputs/reflection_spectrum_oblique5.csv`
- Format: csv
- Contract: CSV with header row, two columns: wavelength_nm (float) and reflectance (float). At least 500 wavelength points covering 670–700 nm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reflection_spectrum_normal.csv`
- `/app/outputs/reflection_spectrum_oblique5.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reflection_spectrum_normal.csv
- path: `/app/outputs/reflection_spectrum_normal.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw reflection spectrum for normal incidence. The checker extracts the EIT peak wavelength and FWHM and scores them against the paper‑reported reference.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `reflectance`
  - `units`:
    - `wavelength_nm`: nm
    - `reflectance`: dimensionless (0–1)

### reflection_spectrum_oblique5.csv
- path: `/app/outputs/reflection_spectrum_oblique5.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw reflection spectrum for oblique incidence at 5°. The checker extracts the EIT peak wavelength and FWHM and scores them against the paper‑reported reference.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `reflectance`
  - `units`:
    - `wavelength_nm`: nm
    - `reflectance`: dimensionless (0–1)

Notes: Both spectra must be computed with the specified Au Drude–Lorentz parameters and geometry. The checker recomputes the EIT peak wavelength and FWHM from the raw data and compares them to the paper’s values using a metric that rewards a correctly located, ultranarrow peak. No self‑reported metrics are accepted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reflection_spectrum_normal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "reflectance"
        ],
        "units": {
          "wavelength_nm": "nm",
          "reflectance": "dimensionless (0–1)"
        }
      },
      "description": "Raw reflection spectrum for normal incidence. The checker extracts the EIT peak wavelength and FWHM and scores them against the paper‑reported reference."
    },
    {
      "file": "reflection_spectrum_oblique5.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "reflectance"
        ],
        "units": {
          "wavelength_nm": "nm",
          "reflectance": "dimensionless (0–1)"
        }
      },
      "description": "Raw reflection spectrum for oblique incidence at 5°. The checker extracts the EIT peak wavelength and FWHM and scores them against the paper‑reported reference."
    }
  ],
  "notes": "Both spectra must be computed with the specified Au Drude–Lorentz parameters and geometry. The checker recomputes the EIT peak wavelength and FWHM from the raw data and compares them to the paper’s values using a metric that rewards a correctly located, ultranarrow peak. No self‑reported metrics are accepted."
}
```

## How you are scored
A hidden verifier inspects your two output CSV files. For each file, the verifier locates the EIT peak by searching for a sharp local maximum in reflectance within the expected wavelength window, then computes the peak wavelength and the full width at half maximum (FWHM) by interpolation. These extracted values are compared against reference values derived from the paper’s reported ultranarrow EIT benchmarks using appropriate tolerances. The final reward is a weighted combination of the scores from the two stages: the reflection spectrum at normal incidence (Step 1) and the spectrum at oblique incidence (Step 2), each contributing a substantial share. Meeting or exceeding the reference linewidth criteria earns full credit for that stage; larger deviations are penalized. Exact reproduction of the paper’s own absolute numbers is not required, as small numerical differences between FDTD implementations are expected.
