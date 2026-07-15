# RCWA Simulation and Resonance Peak Extraction for a Tunable GMR Color Filter

## Problem background
Guided-mode resonance (GMR) in a periodic waveguide structure produces narrowband reflectance peaks that can be tuned by varying the angle of incidence. This enables color filters that cover the visible spectrum with a single device. A key practical challenge is reducing fabrication difficulty; one approach is to use a grating period that is not strictly smaller than the resonant wavelength (non-subwavelength operation). This work investigates a double-layer GMR filter consisting of a Ta2O5 grating on a BK7 substrate, with the goal of computing the filter's reflectance response across visible wavelengths and extracting its resonance characteristics as a function of incidence angle.

## Approach
Rigorous coupled-wave analysis (RCWA) is the standard numerical method for computing the reflectance and transmittance of periodic dielectric structures. Using an open-source RCWA implementation, simulate the TM-polarized reflectance spectrum of the filter. The structure parameters are: substrate index 1.51 (BK7), waveguide layer of Ta2O5 (index 2.16, thickness 170 nm), grating layer with alternating Ta2O5 (index 2.16) and air (index 1), period 574 nm, fill factor 0.5 (equal Ta2O5 and air widths), grating depth 106 nm. For each specified incidence angle (20° through 50°), compute the reflectance as a function of free-space wavelength from 350 to 850 nm. Then, from the reflectance curve, identify the resonant peak (wavelength of maximum reflectance) within that range, and record the peak reflectance and full width at half maximum (FWHM). Use sufficient Fourier orders (e.g., at least 15) to ensure convergence.

## Reproduction target
Produce a CSV file, resonant_peaks.csv, with columns: angle_deg, peak_wavelength_nm, peak_reflectance, FWHM_nm. Include exactly seven rows, one per angle: 20, 25, 30, 35, 40, 45, 50 degrees, in that order. Additionally, verify the non-subwavelength condition: for angles ≥35°, the peak resonant wavelength should be less than the grating period (574 nm).

## Assets

- RCWA Python package (rcwa by Jordan Edmund): rcwa

## Workflow steps

### Step 1: RCWA simulation and resonance peak extraction
- Role: scored (load-bearing)
- Action: Using an open-source RCWA package, simulate the TM-polarized reflectance of a double-layer GMR filter with: substrate index ns=1.51, waveguide index nw=2.16 (Ta2O5, thickness dw=170 nm), grating indices nh=2.16 (Ta2O5) and nc=1 (air), period Λ=574 nm, fill factor f=0.5, grating depth dg=106 nm. Compute reflectance versus wavelength from 350 to 850 nm for incidence angles of 20°, 25°, 30°, 35°, 40°, 45°, and 50°. For each angle, find the resonant wavelength (wavelength of maximum reflectance), the peak reflectance at that wavelength, and the full width at half maximum (FWHM) of the reflectance peak. Write these results to resonant_peaks.csv.
- Output file: `/app/outputs/resonant_peaks.csv`
- Format: csv
- Contract: Header: angle_deg, peak_wavelength_nm, peak_reflectance, FWHM_nm. Seven rows in order: 20,25,30,35,40,45,50.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/resonant_peaks.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### resonant_peaks.csv
- path: `/app/outputs/resonant_peaks.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: TM-polarized GMR filter resonance characteristics for the seven specified incidence angles.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `peak_wavelength_nm`, `peak_reflectance`, `FWHM_nm`
  - `units`:
    - `peak_wavelength_nm`: nm
    - `peak_reflectance`: dimensionless
    - `FWHM_nm`: nm

Notes: The checker compares the reported peak_wavelength_nm to hidden gold values derived from the paper's experimental measurements, and verifies the non-subwavelength condition: for angles ≥35°, peak_wavelength_nm must be less than the grating period (574 nm).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "resonant_peaks.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "peak_wavelength_nm",
          "peak_reflectance",
          "FWHM_nm"
        ],
        "units": {
          "peak_wavelength_nm": "nm",
          "peak_reflectance": "dimensionless",
          "FWHM_nm": "nm"
        }
      },
      "description": "TM-polarized GMR filter resonance characteristics for the seven specified incidence angles."
    }
  ],
  "notes": "The checker compares the reported peak_wavelength_nm to hidden gold values derived from the paper's experimental measurements, and verifies the non-subwavelength condition: for angles ≥35°, peak_wavelength_nm must be less than the grating period (574 nm)."
}
```

## How you are scored
Your CSV file is checked by a hidden verifier. The primary scored metric is the resonant peak wavelength for each angle; secondary metrics are peak reflectance and FWHM. The verifier compares your reported values against expected values with appropriate tolerances (not disclosed). It also checks that the non-subwavelength condition holds for angles ≥35°. The overall reward (0 to 1) combines the weights of primary and secondary metrics and the structural condition. You must not hard‑code values; the reward reflects how accurately your RCWA simulation reproduces the expected filter characteristics.
