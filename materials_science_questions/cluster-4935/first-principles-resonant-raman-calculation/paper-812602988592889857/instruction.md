# Resonance Shift Spin Noise Spectroscopy: Faraday Rotation Noise Spectrum from Gaussian Spin Fluctuations

## Problem background
Resonance shift spin noise spectroscopy probes quantum spin fluctuations by measuring the noise of the Faraday rotation angle of light transmitted through a paramagnetic medium. In diluted magnetic semiconductors, the spins of magnetic impurities (e.g., Mn²⁺ ions) shift the optical resonance of a localized exciton via the sp‑d exchange interaction, producing polarization noise that contains high‑order spin correlation functions. The present task computes the Faraday rotation noise spectrum for a model system of N=50 Mn²⁺ spins in a CdTe‑based quantum well, in the adiabatic limit and at zero temperature, to reveal the spectral signatures of multispin correlations.

## Approach
The computation proceeds in two stages. (1) Derive the time‑dependent spin correlation function ⟨m(0)m(τ)⟩ for the total Mn²⁺ spin I_z in Voigt geometry, where the external magnetic field is perpendicular to the light propagation direction. Use the Gaussian approximation for many independent spins, the Zeeman Hamiltonian with Larmor frequency Ω_L, and transverse relaxation with time constant τ_s. The correlation function is of the form ⟨m(0)m(τ)⟩ = (μ₊ e^{-iΩ_Lτ} + μ₋ e^{iΩ_Lτ}) e^{-|τ|/τ_s}, where the parameters μ± are expressed in terms of ω_ex/γ and the spin expectation values. (2) In the adiabatic regime (Ω_L ≪ γ), the dimensionless polarization correlation function ⟨p_y*(0)p_y(τ)⟩ is obtained via the Gaussian cumulant expansion, which yields an integral over an internal variable k. The Faraday rotation noise spectrum S_FR(Ω) follows from its Fourier transform. The result is a comb of peaks at odd multiples of Ω_L with intensities dictated by the high‑order correlators. All calculations use only numpy and scipy; the physical parameters are fixed as given in the reproduction target.

## Reproduction target
Compute the dimensionless Faraday rotation noise spectrum S_FR(Ω) for the following parameters: N = 50 Mn²⁺ spins, temperature T = 0 K, dimensionless exchange ratio ω_ex/γ = 5, dimensionless Larmor parameter Ω_L τ_s = 20. Output the spectrum as a CSV file over the frequency range [-10 Ω_L, 0] with a frequency step ≤ 0.05 Ω_L. Your submission will be checked against a hidden reference spectrum: the verifier will compare the overall spectrum shape (including peak positions and relative intensities) using a metric recompute approach, and will also assess conformance to the physical model underlying the resonant shift spin noise spectroscopy.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute Mn²⁺ spin correlation function
- Role: process
- Action: Using the given physical parameters (N=50 spins, temperature T=0 K, dimensionless exchange ratio ω_ex/γ=5, dimensionless Larmor parameter Ω_L τ_s=20, adiabatic limit), compute the dimensionless time-dependent spin correlation function ⟨m(0)m(τ)⟩ in the Gaussian approximation for independent Mn²⁺ spins. Derive the parameters μ± and the functional form ⟨m(0)m(τ)⟩ = (μ_+ e^{-i Ω_L τ} + μ_- e^{i Ω_L τ}) e^{-|τ|/τ_s}. Save the computed parameters and correlation function details to spin_corr_parameters.json.
- Evidence: `/app/outputs/spin_corr_parameters.json`

### Step 2: Compute Faraday rotation noise spectrum
- Role: scored (load-bearing)
- Action: Using the spin correlation parameters from step0, numerically evaluate the polarization correlation function in the adiabatic limit via the Gaussian cumulant expansion. Perform the integration over the internal variable k and apply a Fourier transform to obtain the Faraday rotation noise spectrum S_FR(Ω). Output the spectrum over the frequency range covering at least -10 Ω_L to 0 with a frequency step no larger than 0.05 Ω_L.
- Output file: `/app/outputs/faraday_noise_spectrum.csv`
- Format: csv
- Contract: Two columns: frequency (float, units of Ω_L) and intensity (float, dimensionless). The frequency range must cover at least [-10, 0] Ω_L with a resolution ≤ 0.05 Ω_L.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/faraday_noise_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### faraday_noise_spectrum.csv
- path: `/app/outputs/faraday_noise_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Faraday rotation noise spectrum S_FR(Ω) in dimensionless units. The checker recomputes the mean absolute percentage error (MAPE) against a hidden reference and verifies that the spectrum conforms to the expected physical structure (peak positions, absence of spurious harmonics).
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `intensity`
  - `units`:
    - `frequency`: units of Ω_L
    - `intensity`: dimensionless

Notes: The spectrum is computed in the adiabatic Gaussian limit for N=50 Mn²⁺ spins, T=0 K, ω_ex/γ=5, Ω_L τ_s=20. All parameters are fixed; no input files are required. The hidden reference is derived analytically from the same model.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "faraday_noise_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "intensity"
        ],
        "units": {
          "frequency": "units of Ω_L",
          "intensity": "dimensionless"
        }
      },
      "description": "Faraday rotation noise spectrum S_FR(Ω) in dimensionless units. The checker recomputes the mean absolute percentage error (MAPE) against a hidden reference and verifies that the spectrum conforms to the expected physical structure (peak positions, absence of spurious harmonics)."
    }
  ],
  "notes": "The spectrum is computed in the adiabatic Gaussian limit for N=50 Mn²⁺ spins, T=0 K, ω_ex/γ=5, Ω_L τ_s=20. All parameters are fixed; no input files are required. The hidden reference is derived analytically from the same model."
}
```

## How you are scored
After you submit the required artifacts, an automated verifier will: (1) verify that `faraday_noise_spectrum.csv` exists, has the correct two‑column format, and covers the required frequency range and resolution; (2) compare your spectrum against a hidden reference by computing a dimensionless error metric (lower error yields higher score); (3) verify that the spectrum satisfies the required structural properties (as defined by the hidden reference). The error metric and structural checks together determine a single reward between 0 and 1. Reporting the paper’s numbers without genuinely computing the spectrum will not pass the verifier. You do not need to install anything beyond numpy and scipy; the verifier will handle the comparison.
