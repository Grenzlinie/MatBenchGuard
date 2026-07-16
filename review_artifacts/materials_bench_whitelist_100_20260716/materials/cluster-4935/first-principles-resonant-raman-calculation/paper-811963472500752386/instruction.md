# Resonant Raman Continuous Emission from a Single GaAs Quantum Well

## Problem background
In resonant Raman spectroscopy of semiconductor multiple quantum wells (MQWs), a broad continuous acoustic-phonon emission background appears that cannot be explained by crystal-momentum conserving folded-phonon doublets. This background arises from crystal-momentum nonconserving Raman scattering originating from individual quantum wells, where the loss of translational periodicity along the growth direction relaxes the usual q-selection rule. The intensity of this continuous emission is governed by the single-quantum-well electron–phonon interaction matrix element, and it is strongly enhanced near electronic interband resonances. Computing the theoretical spectral shape for a model GaAs quantum well tests the fundamental understanding of this phenomenon.

## Approach
Model the quantum well as a 100 Å wide GaAs layer with infinite barriers, using simple sine or cosine wave functions for the confined electrons and holes. The electron–phonon interaction is described by a deformation potential D that couples the strain field of a longitudinal acoustic phonon propagating along the growth direction to the electronic states. The matrix element M_N(q_z) for scattering within subband N is given by

  M_N(q_z) ∝ (q_z/√ω) * D * sin(a q_z/2)/(a q_z/2) * 4N² / (4N² - (a q_z/π)²),

where ω = v·q_z is the phonon frequency with sound velocity v ≈ 5000 m/s. The Raman intensity is I(ω) ∝ |M_N(q_z)|² * n_Bose(ω,T), with the Bose‑Einstein factor n_Bose accounting for the thermal population at T = 6 K. The homogeneous linewidth Γ_hom = 0.7 meV is included as a broadening of the electronic resonance; under the resonant condition (detuning Δ = 0) the spectral shape is independent of Γ_hom, so the model reduces to the squared matrix element times the Bose factor. The calculation is performed for subband indices N = 1 and N = 2, for Raman shifts from 0 to 50 cm⁻¹ in 1 cm⁻¹ steps, and the resulting intensity profile is normalized to a maximum of 1.

## Reproduction target
Produce two CSV files containing the normalized theoretical continuous emission Raman intensity profile for a single 100 Å GaAs quantum well under resonant conditions (Δ = 0). The files must be:
- ce_spectrum_N1.csv: subband index N=1.
- ce_spectrum_N2.csv: subband index N=2.
Each file must have columns 'Raman_shift_cm1' (Raman shift in cm⁻¹, values 0,1,2,…,50) and 'Intensity_arb_units' (normalized intensity, maximum 1.0). The intensity is computed from the model described in the Approach using the stated parameters (a=100 Å, v=5000 m/s, T=6 K, Δ=0).

## Assets

- GaAs material parameters and physical constants

## Workflow steps

### Step 1: Compute continuous emission spectrum for N=1
- Role: scored
- Action: Implement the single-quantum-well continuous emission model for resonant Raman scattering by acoustic phonons. For a GaAs quantum well of width 100 Å, compute the electron–phonon matrix element M_N(q_z) (proportional to (q_z/√ω) * sin(aq_z/2)/(aq_z/2) * 4N²/(4N²−(a q_z/π)²)), the phonon frequency ω = v*q_z with v ≈ 5000 m/s, and the intensity I(ω) ∝ |M|² * n_Bose(ω,T) with T=6 K and a homogeneous linewidth of 0.7 meV. Use subband index N=1, detuning Δ=0. Compute intensities for Raman shifts from 0 to 50 cm⁻¹ in steps of 1 cm⁻¹, normalize the maximum to 1. Write the result to ce_spectrum_N1.csv.
- Output file: `/app/outputs/ce_spectrum_N1.csv`
- Format: csv
- Contract: CSV with header. Columns: 'Raman_shift_cm1' (float, from 0 to 50 step 1), 'Intensity_arb_units' (float, normalized to max=1).
- Scoring: scored by hidden verifier

### Step 2: Compute continuous emission spectrum for N=2
- Role: scored
- Action: Repeat the calculation for subband index N=2 using the same parameters (a=100 Å, v=5000 m/s, T=6 K, Γ_hom=0.7 meV, Δ=0). Compute intensities for Raman shifts 0–50 cm⁻¹ in steps of 1 cm⁻¹, normalize to maximum 1, and write to ce_spectrum_N2.csv.
- Output file: `/app/outputs/ce_spectrum_N2.csv`
- Format: csv
- Contract: CSV with header. Columns: 'Raman_shift_cm1' (float, from 0 to 50 step 1), 'Intensity_arb_units' (float, normalized to max=1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ce_spectrum_N1.csv`
- `/app/outputs/ce_spectrum_N2.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ce_spectrum_N1.csv
- path: `/app/outputs/ce_spectrum_N1.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Theoretical continuous emission spectrum for N=1: Raman shift (cm⁻¹) vs normalized intensity.
- schema:
  - `type`: table
  - `required_columns`: `Raman_shift_cm1`, `Intensity_arb_units`
  - `units`:
    - `Raman_shift_cm1`: cm^-1
    - `Intensity_arb_units`: arbitrary

### ce_spectrum_N2.csv
- path: `/app/outputs/ce_spectrum_N2.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Theoretical continuous emission spectrum for N=2: Raman shift (cm⁻¹) vs normalized intensity.
- schema:
  - `type`: table
  - `required_columns`: `Raman_shift_cm1`, `Intensity_arb_units`
  - `units`:
    - `Raman_shift_cm1`: cm^-1
    - `Intensity_arb_units`: arbitrary

Notes: The checker recomputes the theoretical spectra using the same model and parameters. Scoring uses normalized cross-correlation (NCC) ≥ 0.98 for each spectrum and additionally requires the position of the first intensity minimum (zero) to be within ±2 cm⁻¹ of the reference. No absolute tolerances on individual intensity values are enforced; the spectrum shape and zero positions are the targets.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ce_spectrum_N1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Raman_shift_cm1",
          "Intensity_arb_units"
        ],
        "units": {
          "Raman_shift_cm1": "cm^-1",
          "Intensity_arb_units": "arbitrary"
        }
      },
      "description": "Theoretical continuous emission spectrum for N=1: Raman shift (cm⁻¹) vs normalized intensity."
    },
    {
      "file": "ce_spectrum_N2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Raman_shift_cm1",
          "Intensity_arb_units"
        ],
        "units": {
          "Raman_shift_cm1": "cm^-1",
          "Intensity_arb_units": "arbitrary"
        }
      },
      "description": "Theoretical continuous emission spectrum for N=2: Raman shift (cm⁻¹) vs normalized intensity."
    }
  ],
  "notes": "The checker recomputes the theoretical spectra using the same model and parameters. Scoring uses normalized cross-correlation (NCC) ≥ 0.98 for each spectrum and additionally requires the position of the first intensity minimum (zero) to be within ±2 cm⁻¹ of the reference. No absolute tolerances on individual intensity values are enforced; the spectrum shape and zero positions are the targets."
}
```

## How you are scored
A hidden verifier will independently recompute the theoretical spectra for N=1 and N=2 using the same model and parameters. It will compare the shape of your submitted intensity profiles to the reference via normalized cross-correlation and verify that key features such as the position of the first intensity minimum (zero) match within an allowed tolerance. The reward is a weighted combination of the scores for the two artifacts (N=1 and N=2). Simply reporting a number from the literature is not sufficient; the verifier checks that the full computed curve is correct.
