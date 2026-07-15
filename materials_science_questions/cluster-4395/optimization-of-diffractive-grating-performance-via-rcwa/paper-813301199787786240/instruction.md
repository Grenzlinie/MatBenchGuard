# Optimized SIM-SG Reflectivity Spectra for Polarization-insensitive Operation

## Problem background
Subwavelength grating reflectors can provide broadband high reflectivity, but they are often polarization‑sensitive, favoring either TM (electric field perpendicular to the grating stripes) or TE (parallel) polarization. Designing a single grating that achieves high reflectivity for both polarizations over a wide wavelength range would enable applications where polarization control is not practical. This task investigates a semiconductor‑insulator‑metal subwavelength grating (SIM‑SG) that stacks a high‑contrast dielectric grating with a metallic layer separated by an insulator. The goal is to compute the normal‑incidence reflectivity spectra for both polarizations and determine the continuous wavelength intervals where reflectivity remains above a very high threshold, and the overlap bandwidth where both polarizations are simultaneously above that threshold.

## Approach
The computational method is rigorous coupled-wave analysis (RCWA), a widely used approach for simulating diffraction from periodic structures. RCWA expands the electromagnetic fields and permittivity in Fourier series and solves Maxwell's equations in the grating region to obtain the diffraction efficiencies. Here it is applied to a one‑dimensional binary grating at normal incidence. The grating geometry consists of ridges of semiconductor (Al₀.₆Ga₀.₄As, refractive index 3.2137) separated by air, on top of a lossless insulator layer, atop a gold (Au) film. The gold is modeled by a Drude dispersion: plasma frequency ωₚ = 1.37×10¹⁶ rad/s, damping frequency ω_τ = 4.05×10¹³ rad/s. The simulation sweeps the incident wavelength from 0.6 µm to 1.0 µm, recording the zero‑order reflectivity for TM (E⊥ stripes) and TE (E∥ stripes) polarizations. The resulting spectra reveal the high‑reflectivity bands and the polarization‑overlap bandwidth.

## Reproduction target
Produce two CSV files: `tm_reflectivity.csv` and `te_reflectivity.csv`, each containing the wavelength (in micrometres) and the reflectivity (as a fraction) for the simulated SIM‑SG over the range 0.6–1.0 µm, with a wavelength step of ≤ 1 nm. The files must have a header line, comma‑separated floating‑point values, and wavelengths in ascending order. From these raw spectra, the hidden verifier will extract the wavelength intervals where reflectivity exceeds a threshold, compute the overlapped bandwidth where both polarizations are above that threshold, and compare the band edges and overlap width against reference values. The verification is fully automatic and does not require you to report any summary numbers.

## Assets

- RCWA implementation
- Au Drude model parameters: 10.1364/AO.24.004493

## Workflow steps

### Step 1: TM reflectivity spectrum
- Role: scored
- Action: Use RCWA to compute the reflectivity spectrum for TM polarization (E perpendicular to grating stripes) of the SIM-SG with optimized parameters: period 380 nm, grating strip width 250 nm, Al0.6Ga0.4As layer thickness 235 nm (refractive index 3.2137), insulator layer thickness 400 nm (lossless dielectric), metal Au layer thickness 100 nm (Drude model with plasma frequency 1.37e16 rad/s, damping frequency 4.05e13 rad/s). Normal incidence. Compute over wavelength range 0.6 μm to 1.0 μm with a fine step (≤1 nm).
- Output file: `/app/outputs/tm_reflectivity.csv`
- Format: csv
- Contract: wavelength (μm), reflectivity
CSV with header, comma separated, floating point values. Wavelength ascending. Reflectivity as a fraction.
- Scoring: scored by hidden verifier

### Step 2: TE reflectivity spectrum
- Role: scored
- Action: Use RCWA to compute the reflectivity spectrum for TE polarization (E parallel to grating stripes) of the same SIM-SG structure as in step_tm, same wavelength range and resolution.
- Output file: `/app/outputs/te_reflectivity.csv`
- Format: csv
- Contract: wavelength (μm), reflectivity
CSV with header, comma separated, floating point values. Wavelength ascending. Reflectivity as a fraction.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tm_reflectivity.csv`
- `/app/outputs/te_reflectivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tm_reflectivity.csv
- path: `/app/outputs/tm_reflectivity.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: TM-polarization reflectivity spectrum of the optimized SIM-SG. The checker identifies continuous wavelength intervals where reflectivity exceeds a hidden high-reflectivity threshold and compares the band edges to the paper-reported values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `wavelength`, `reflectivity`
  - `units`:
    - `wavelength`: μm
    - `reflectivity`: fraction

### te_reflectivity.csv
- path: `/app/outputs/te_reflectivity.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: TE-polarization reflectivity spectrum of the optimized SIM-SG. The checker identifies continuous wavelength intervals where reflectivity exceeds a hidden high-reflectivity threshold and compares the band edges to the paper-reported values with tolerances; the overlapped high-reflectivity bandwidth between TM and TE is also verified.
- schema:
  - `type`: table
  - `required_columns`: `wavelength`, `reflectivity`
  - `units`:
    - `wavelength`: μm
    - `reflectivity`: fraction

Notes: The checker will recompute the high-reflectivity bands from the raw reflectivity spectra, compare band edges to the paper's reported values with tolerances, and verify that the overlapped bandwidth where both TM and TE reflectivities exceed the hidden threshold meets the paper's specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tm_reflectivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength",
          "reflectivity"
        ],
        "units": {
          "wavelength": "μm",
          "reflectivity": "fraction"
        }
      },
      "description": "TM-polarization reflectivity spectrum of the optimized SIM-SG. The checker identifies continuous wavelength intervals where reflectivity exceeds a hidden high-reflectivity threshold and compares the band edges to the paper-reported values with tolerances."
    },
    {
      "file": "te_reflectivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength",
          "reflectivity"
        ],
        "units": {
          "wavelength": "μm",
          "reflectivity": "fraction"
        }
      },
      "description": "TE-polarization reflectivity spectrum of the optimized SIM-SG. The checker identifies continuous wavelength intervals where reflectivity exceeds a hidden high-reflectivity threshold and compares the band edges to the paper-reported values with tolerances; the overlapped high-reflectivity bandwidth between TM and TE is also verified."
    }
  ],
  "notes": "The checker will recompute the high-reflectivity bands from the raw reflectivity spectra, compare band edges to the paper's reported values with tolerances, and verify that the overlapped bandwidth where both TM and TE reflectivities exceed the hidden threshold meets the paper's specification."
}
```

## How you are scored
Your submission is scored exclusively from the two output CSV files. The hidden checker reads each file, identifies the continuous wavelength regions where reflectivity exceeds a hidden threshold, and extracts the start and end wavelengths of the high‑reflectivity bands for both polarizations. It then computes the total wavelength span where both TM and TE reflectivities stay above the threshold (overlap bandwidth). The checker compares your band intervals and overlap width against reference values with appropriate tolerances and produces a reward between 0 and 1. The reward is a weighted combination of how well the TM band edges, the TE band edges, and the overlap bandwidth match the expected ranges. There is no need to report any single aggregated figure; only the spectra count.
