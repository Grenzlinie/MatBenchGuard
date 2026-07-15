# Surface‑Enhanced Raman Scattering (SERS) Enhancement Factor Calculation for Langmuir‑Blodgett Film on Nanostructured Metal Surface

## Problem background
Surface-enhanced Raman scattering (SERS) is a technique that dramatically amplifies the weak Raman signal of molecules adsorbed on nanostructured metal surfaces. The commonly used |E|^4 approximation for the electromagnetic enhancement factor neglects collective emission effects and the correct angular emission pattern at the Raman-shifted frequency. This work introduces an electromagnetic model of the Raman-shifted emission from a dense Langmuir-Blodgett film deposited on a metal surface. The model fully accounts for the Raman-shifted emission so that meaningful SERS enhancement factors that do not depend only on the local field at the pump frequency are defined. The task is to compute and compare SERS enhancement factors from this collective model and from the |E|^4 approximation for both planar and rough silver surfaces, revealing their quantitative differences.

## Approach
The theoretical Raman response is described as a macroscopic dipole layer (the LB film) proportional to the local surface electric field at the pump frequency. For a planar metal surface, modified boundary conditions lead to analytic effective Raman Fresnel coefficients for p- and s-polarizations, normalized by the emission of a freestanding layer. For rough surfaces, the model is embedded into a rigorous Green's theorem surface integral equation solver for one-dimensional, Gaussian-correlated random rough surfaces. The numerical pipeline: (i) solve the scattering problem for p-polarized pump light to obtain near-field enhancement; (ii) repeat for the Raman-shifted frequency to compute the |E|^4 approximation; (iii) incorporate the Raman polarization source into the integral equations to compute far-field scattered intensity at the Raman frequency, and from it the collective SERS enhancement factor. The comparison is made between the collective model and the |E|^4 approximation for varying pump wavelength and Raman shift, using rough surfaces with given roughness parameters (rms height δ=255 nm, correlation length a=51 nm).

## Reproduction target
Produce three scored CSV files:
(1) `planar_fresnel_coefficients.csv` — squared moduli of the normalized effective Raman Fresnel coefficients (R_ppar^2, R_pperp^2, R_s^2) for a planar vacuum/Ag interface at pump wavelength λ0=514.5 nm, incident angles 0°–80° in 5° steps, for three Raman shifts (no shift λR=λ0, Stokes λR=614.5 nm, anti-Stokes λR=414.5 nm);
(2) `rough_sers_factors.csv` — average SERS electromagnetic enhancement factors G_SERS from the collective model and from the |E|^4 approximation, as a function of pump wavelength (400–800 nm in 10 nm steps) for roughness δ=255 nm, a=51 nm, assuming negligible Raman shift;
(3) `raman_shift_dependence.csv` — same enhancement factors as a function of fractional Raman shift Δλ/λ0 from -0.1 to 0.1 in 0.01 steps, at fixed pump λ0=620 nm, same roughness. The goal is to implement the full physics and numerical solver and compute these enhancement factors.

## Assets

- Silver dielectric function (Palik handbook): https://refractiveindex.info/?shelf=main&book=Ag&page=Johnson
- Green's theorem surface integral equation method for 1D rough surfaces: https://doi.org/10.1016/0003-4916(90)90015-G
- Gaussian random rough surface profile generator

## Workflow steps

### Step 1: Compute planar effective Raman Fresnel coefficients
- Role: scored
- Action: Using the analytic formulas for effective Raman Fresnel coefficients (p‑polarization: tangential and normal contributions; s‑polarization) and the public Ag dielectric function, compute the squared moduli of the normalized coefficients (R_ppar^2, R_pperp^2, R_s^2) for a vacuum/Ag planar interface at pump wavelength λ0=514.5 nm, incident angles from 0° to 80° in 5° steps, and for three Raman shifts: no shift (λR＝514.5 nm), Stokes (λR＝614.5 nm) and anti‑Stokes (λR＝414.5 nm).
- Output file: `/app/outputs/planar_fresnel_coefficients.csv`
- Format: csv
- Contract: columns: incident_angle_deg (float), raman_shift_nm (float), R_ppar_sq (float), R_pperp_sq (float), R_s_sq (float). Each row corresponds to a specific incident angle and Raman shift.
- Scoring: scored by hidden verifier

### Step 2: Generate Gaussian random rough surface profiles
- Role: process
- Action: Create an ensemble of at least 300 realizations of 1D randomly rough Ag surface profiles with Gaussian correlation (rms height δ=255 nm, correlation length a=51 nm), surface length 7 µm, sampled with ≥2000 points. Store the profiles for reuse.
- Evidence: `/app/outputs/surface_profiles.log`

### Step 3: Simulate pump-frequency near‑field on rough surfaces
- Role: process
- Action: For each surface realization, solve the p‑polarized scattering problem at the pump frequency ω0 (wavelengths covering 400–800 nm) using the Green's theorem surface integral equations. Compute the local electric field intensity enhancement factor σ(ω0)=|E|²/|E_i|² on the surface.
- Evidence: none

### Step 4: Simulate Raman‑frequency near‑field for |E|^4 approximation
- Role: process
- Action: Repeat the scattering simulation with the incident frequency set to the Raman‑shifted frequency ωR for each required Raman shift (including zero shift), computing σ(ωR).
- Evidence: none

### Step 5: Simulate Raman‑shifted emission and far‑field angular intensities
- Role: process
- Action: Incorporate the Raman polarization term into the surface integral equations and solve for the scattered field at ωR for each surface realization, pump wavelength, and Raman shift. Compute the far‑field angular intensity distribution.
- Evidence: none

### Step 6: Compute average SERS enhancement factors vs pump wavelength
- Role: scored (load-bearing)
- Action: Averaging over the surface ensemble, compute the electromagnetic SERS enhancement factor G_SERS^EM from the collective model (far‑field intensity normalized by the freestanding layer and planar reference) and from the |E|^4 approximation (product of near‑field enhancement factors), for pump wavelengths from 400 nm to 800 nm in 10 nm steps, assuming negligible Raman shift. Write the results.
- Output file: `/app/outputs/rough_sers_factors.csv`
- Format: csv
- Contract: columns: pump_wavelength_nm (float), G_SERS_collective (float), G_SERS_approx (float).
- Scoring: scored by hidden verifier

### Step 7: Compute average SERS enhancement factors vs Raman shift
- Role: scored
- Action: Using the far‑field and near‑field data for a fixed pump wavelength λ0=620 nm and fractional Raman shifts Δλ/λ0 from -0.1 to 0.1 in 0.01 steps, compute G_SERS^EM (collective) and G_SERS^EM (|E|^4 approximation) and write to file.
- Output file: `/app/outputs/raman_shift_dependence.csv`
- Format: csv
- Contract: columns: fractional_raman_shift (float), G_SERS_collective (float), G_SERS_approx (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/planar_fresnel_coefficients.csv`
- `/app/outputs/rough_sers_factors.csv`
- `/app/outputs/raman_shift_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### planar_fresnel_coefficients.csv
- path: `/app/outputs/planar_fresnel_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized squared effective Raman Fresnel coefficients for planar vacuum/Ag interface at λ0=514.5 nm for three Raman shifts.
- schema:
  - `type`: table
  - `required_columns`: `incident_angle_deg`, `raman_shift_nm`, `R_ppar_sq`, `R_pperp_sq`, `R_s_sq`

### rough_sers_factors.csv
- path: `/app/outputs/rough_sers_factors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average SERS electromagnetic enhancement factors from collective model and |E|^4 approximation as a function of pump wavelength (roughness δ=255 nm, a=51 nm, negligible Raman shift).
- schema:
  - `type`: table
  - `required_columns`: `pump_wavelength_nm`, `G_SERS_collective`, `G_SERS_approx`

### raman_shift_dependence.csv
- path: `/app/outputs/raman_shift_dependence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: SERS enhancement factors as a function of Raman shift at fixed pump λ0=620 nm for the same rough surface.
- schema:
  - `type`: table
  - `required_columns`: `fractional_raman_shift`, `G_SERS_collective`, `G_SERS_approx`

Notes: The checker performs result‑level comparison against hidden reference values derived from the paper (T0). Values are checked with appropriate relative tolerances; additionally, the checker verifies that the collective model yields lower enhancement factors than the |E|^4 approximation by at least the expected factor.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "planar_fresnel_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "incident_angle_deg",
          "raman_shift_nm",
          "R_ppar_sq",
          "R_pperp_sq",
          "R_s_sq"
        ]
      },
      "description": "Normalized squared effective Raman Fresnel coefficients for planar vacuum/Ag interface at λ0=514.5 nm for three Raman shifts."
    },
    {
      "file": "rough_sers_factors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pump_wavelength_nm",
          "G_SERS_collective",
          "G_SERS_approx"
        ]
      },
      "description": "Average SERS electromagnetic enhancement factors from collective model and |E|^4 approximation as a function of pump wavelength (roughness δ=255 nm, a=51 nm, negligible Raman shift)."
    },
    {
      "file": "raman_shift_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "fractional_raman_shift",
          "G_SERS_collective",
          "G_SERS_approx"
        ]
      },
      "description": "SERS enhancement factors as a function of Raman shift at fixed pump λ0=620 nm for the same rough surface."
    }
  ],
  "notes": "The checker performs result‑level comparison against hidden reference values derived from the paper (T0). Values are checked with appropriate relative tolerances; additionally, the checker verifies that the collective model yields lower enhancement factors than the |E|^4 approximation by at least the expected factor."
}
```

## How you are scored
A hidden verifier reads your submitted CSV files and compares your computed values to hidden reference data. Each scored file is assigned a weight, and the final reward is a weighted sum of per-file scores (0–1). The comparison uses appropriate tolerances to account for numerical spread. Merely reporting values without genuine computation will not pass. In addition, the verifier checks structural relationships, such as that the collective model produces lower enhancement factors than the |E|^4 approximation. You do not need to match any specific paper figure; the check is automated.
