# Compute Standard Deviation and Spectral Noise Density of Magnetic Field Noise from Randomized Barrier Spins

## Problem background
MgO-based magnetic tunnel junction sensors can achieve pT/√Hz sensitivity, but are limited by intrinsic magnetic noise from spins in the barrier. Both ²⁵Mg nuclear spins (I=5/2) and electronic Mg vacancies (S=1) create fluctuating dipole fields that the sensor averages over its free-layer volume. The statistical properties of this noise—its integrated amplitude and frequency spectrum—depend on device geometry, spin density, and external magnetic field/gradient. This task computes the standard deviation of the in-plane noise field and its spectral density for two barrier spin species, to determine the noise levels and spectral features that affect sensor performance.

## Approach
The magnetic field averaged over the free-layer volume can be expressed as a linear combination of the barrier spin moments, with coefficients given by a geometry tensor Ξ that depends only on the device dimensions and spin positions. Assuming uncorrelated, randomized spins, the variance of the in-plane field component σ²_Bx is proportional to the sum of squared tensor components, with a prefactor determined by the spin quantum numbers and magnetic moment. The frequency-dependent noise spectrum S_x(f) is obtained by convolving the spin correlation function with a Lorentzian broadening that accounts for finite relaxation time T1. For the vacancy spectrum, a linear magnetic field gradient along the barrier thickness introduces position-dependent Larmor frequencies, leading to a multi-peaked structure.

## Reproduction target
Compute the standard deviation σ_Bx of the in-plane detector-averaged magnetic field noise from ²⁵Mg nuclear spins for two sensor radii (100 nm and 50 nm), with free-layer thickness 3 nm and barrier thickness 0.5 nm. Produce the noise spectral density S_x(f) for nuclear spins over 0.1–100 MHz under a uniform external field B_ext=0.1 T and T1=10 ms, and for Mg vacancies over 1–10 GHz under B_ext=0.1 T, a linear gradient 1 mT/nm along z, and T1=5 μs. For the nuclear spectrum, also report the Larmor frequency peak positions.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Nuclear spin geometry computation
- Role: process
- Action: Define cylindrical detector geometry (radius R = 100 nm and 50 nm, free layer thickness w = 3 nm, barrier thickness d = 0.5 nm). Generate random ²⁵Mg nuclear spin positions (10% abundance, MgO lattice constant 4.212 Å) within the barrier, and numerically integrate the detector-averaged field formula over the free-layer volume to obtain the geometry tensor components Ξ_ab(i) for each nuclear spin and compute the sum of squares sum_{i,b} Ξ_ab(i)^2 for a = x (the in-plane noise component). Save to nuclear_geometry.npz.
- Evidence: `/app/outputs/nuclear_geometry.npz`

### Step 2: Static nuclear noise variance
- Role: scored (load-bearing)
- Action: Using the nuclear spin geometry data from step_01 and the known spin parameters (g* = 0.342, I = 5/2, μ_N), compute the standard deviation σ_Bx of the in-plane field component via the formula σ_Bx² = (g*μ_N)² I(I+1) · sum_Xi2 for R=100 nm and R=50 nm. Output the results as CSV.
- Output file: `/app/outputs/sigma_Bx_results.csv`
- Format: csv
- Contract: R (nm):float, sigma_Bx (T):float, sum_Xi2 (nm^-4):float
- Scoring: scored by hidden verifier

### Step 3: Nuclear spin noise spectrum
- Role: scored (load-bearing)
- Action: Using the per-spin geometry tensors from step_01, compute the frequency-dependent noise spectral density S_x(f) for nuclear spins under a uniform external field B_ext = 0.1 T. For each spin, evaluate the spin correlation function in the frequency domain using the quantum statistical average over the I=5/2 eigenstates: ⟨m_b m_b'⟩[ω] = (1/(2I+1)) Σ_{n,n'} ⟨n|m_b|n'⟩⟨n'|m_b'|n⟩ L(ω - ω_{nn'}), where L is a Lorentzian with width 2π/T1 (T1=10 ms) and ω_{nn'} = (n - n') g* μ_N B_ext / ħ. Then compute the squared spectral density S_x(ω)^2 = Σ_{i,b,b'} Ξ_{xb}(i) Ξ_{xb'}(i) ⟨m_b m_b'⟩[ω], and output S_x(ω) = sqrt(S_x(ω)^2) as a two-column CSV (frequency in Hz, S_x in T/√Hz) covering 0.1–100 MHz.
- Output file: `/app/outputs/nuclear_spectrum.csv`
- Format: csv
- Contract: frequency_Hz:float, S_x (T/sqrt(Hz)):float
- Scoring: scored by hidden verifier

### Step 4: Vacancy spin geometry computation
- Role: process
- Action: Generate random Mg vacancy positions in the barrier (using a nominal volume concentration of 10¹⁹ cm⁻³ for the given device dimensions) and compute the geometry tensors Ξ_ab(i) for each vacancy via numerical integration, analogous to step_01. Save to vacancy_geometry.npz.
- Evidence: `/app/outputs/vacancy_geometry.npz`

### Step 5: Vacancy spin noise spectrum
- Role: scored (load-bearing)
- Action: Using the geometry data from step_04 and vacancy spin properties (S=1, magnetic moment 1.9 μ_B, g≈2), compute the noise spectral density S_x(f) for Mg vacancies under an external field B_ext = 0.1 T with a linear gradient of 1 mT/nm along z. For each vacancy, determine its Larmor frequency from the local field: ω_L(z_i) = g μ_B (B_ext + (dB/dz) z_i) / ħ. Evaluate the spin correlation function for S=1 analogous to the nuclear case: ⟨m_b m_b'⟩[ω] = (1/3) Σ_{n,n'=-1,0,1} ⟨n|m_b|n'⟩⟨n'|m_b'|n⟩ L(ω - ω_{nn'}) with Lorentzian width 2π/T1 (T1=5 μs) and ω_{nn'} = (n - n') ω_L(z_i). Sum contributions to obtain S_x(ω)^2 = Σ_{i,b,b'} Ξ_{xb}(i) Ξ_{xb'}(i) ⟨m_b m_b'⟩[ω], and output S_x(ω) = sqrt(S_x(ω)^2) as a two-column CSV covering 1–10 GHz.
- Output file: `/app/outputs/vacancy_spectrum.csv`
- Format: csv
- Contract: frequency_Hz:float, S_x (T/sqrt(Hz)):float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sigma_Bx_results.csv`
- `/app/outputs/nuclear_spectrum.csv`
- `/app/outputs/vacancy_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sigma_Bx_results.csv
- path: `/app/outputs/sigma_Bx_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Standard deviation of the in-plane magnetic field noise for two device radii; checker recomputes σ_Bx from the sum of squared geometry tensor components.
- schema:
  - `type`: table
  - `required_columns`: `R (nm)`, `sigma_Bx (T)`, `sum_Xi2 (nm^-4)`

### nuclear_spectrum.csv
- path: `/app/outputs/nuclear_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Nuclear spin noise spectral density; checker integrates spectrum and compares with variance derived from geometry.
- schema:
  - `type`: table
  - `required_columns`: `frequency_Hz`, `S_x (T/sqrt(Hz))`

### vacancy_spectrum.csv
- path: `/app/outputs/vacancy_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Vacancy spin noise spectral density under field gradient; checker integrates spectrum and verifies multiple peaks in GHz range.
- schema:
  - `type`: table
  - `required_columns`: `frequency_Hz`, `S_x (T/sqrt(Hz))`

Notes: Only the spin-noise computation is scored; comparison to 1/f noise is not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sigma_Bx_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "R (nm)",
          "sigma_Bx (T)",
          "sum_Xi2 (nm^-4)"
        ]
      },
      "description": "Standard deviation of the in-plane magnetic field noise for two device radii; checker recomputes σ_Bx from the sum of squared geometry tensor components."
    },
    {
      "file": "nuclear_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_Hz",
          "S_x (T/sqrt(Hz))"
        ]
      },
      "description": "Nuclear spin noise spectral density; checker integrates spectrum and compares with variance derived from geometry."
    },
    {
      "file": "vacancy_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_Hz",
          "S_x (T/sqrt(Hz))"
        ]
      },
      "description": "Vacancy spin noise spectral density under field gradient; checker integrates spectrum and verifies multiple peaks in GHz range."
    }
  ],
  "notes": "Only the spin-noise computation is scored; comparison to 1/f noise is not required."
}
```

## How you are scored
Your solution will be evaluated by a hidden verifier that scores each required output file separately and combines the scores into a final reward. For sigma_Bx_results.csv, the verifier recomputes σ_Bx from the sum of squared geometry tensor components you provide and compares it to your reported σ_Bx. For nuclear_spectrum.csv and vacancy_spectrum.csv, the verifier integrates your spectral density over frequency, compares the result with the variance inferred from your geometry data, and checks that the spectrum exhibits the expected peak structure. The final score reflects how well your computed results satisfy these internal consistency and structural checks.
