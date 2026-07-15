# Quartz Ordinary-Ray Dispersion Parameter Fitting at 1.5 K

## Problem background
Crystal quartz is a birefringent material whose far‑infrared optical constants (refractive index n and absorption coefficient α) are governed by lattice‑vibration resonances. At low temperatures these resonances shift and sharpen, revealing changes in the underlying oscillator parameters. For the ordinary ray, the measured n(σ) and α(σ) at 1.5 K over the range 30–330 cm⁻¹ show two strong features that correspond to the two lowest‑frequency transverse‑optic modes. Extracting the center wavenumber σ₀, oscillator strength S, and linewidth γ for these resonances via a Lorentzian‑oscillator model provides a quantitative description of the temperature‑dependent dielectric response. This task reproduces the dispersion‑parameter determination for those two modes by fitting the reflectance spectrum computed from the reported optical constants.

## Approach
The core method consists of two stages. First, the optical constants are converted into a normal‑incidence reflectance spectrum using the standard relation: k = α/(4πσ), R = [(n−1)² + k²]/[(n+1)² + k²]. In the spectral region of interest the absorption is moderate, so k contributes little but is included for completeness. Second, a Lorentzian‑oscillator model is set up. Each resonance j (j = 1,2) contributes a term to the frequency‑dependent dielectric function:

ε(σ) = ε∞ + Σⱼ [ Sⱼ σ₀,ⱼ² / (σ₀,ⱼ² − σ² − i γⱼ σ) ].

The reflectance predicted by this model (via the usual Fresnel formula for complex refractive index ñ = √ε) is compared with the target reflectance across the available wavenumber grid. The six parameters (σ₀₁, S₁, γ₁, σ₀₂, S₂, γ₂) are optimized by a least‑squares algorithm (or any equivalent nonlinear fitting routine) to minimize the sum of squared residuals between the model and target reflectances. The high‑frequency dielectric constant ε∞ is fixed at 2.2, a value taken from prior literature. The optimization is started from the room‑temperature dispersion parameters that have been measured for the same two resonances (provided as part of the task assets); those parameters serve as an initial guess and are expected to be close enough to the 1.5 K optimum that the fit converges within a few tens of iterations. Because the two resonances are well separated in energy, the coupling between their parameters is weak, and a simultaneous or sequential fit both lead to a reliable result.

## Reproduction target
From the provided 1.5 K optical constants of quartz ordinary ray (n and α as functions of wavenumber), compute the target reflectance and fit the two‑resonance Lorentzian oscillator model described above. The fitted parameters must be written to `/app/outputs/dispersion_fit_1.5K.json` as a JSON object with the following structure:
{ "resonance1": {"sigma0": <float, cm⁻¹>, "S": <float>, "gamma": <float>}, "resonance2": {"sigma0": <float, cm⁻¹>, "S": <float>, "gamma": <float>} }.
The resonance labelled “resonance1” corresponds to the lower‑wavenumber mode (near 131 cm⁻¹) and “resonance2” to the higher‑wavenumber mode (near 264 cm⁻¹). The task is to deliver these six numbers as the output of the fitting procedure; the model and the dataset are fully specified, so the result must be obtained by actual computation.

## Assets

- Quartz ordinary-ray optical constants at 300 K and 1.5 K (n and alpha vs wavenumber)
- Room-temperature dispersion parameters from Russell & Bell used as initial guess
- High-frequency dielectric constant epsilon_inf for quartz
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute target reflectance from optical constants
- Role: process
- Action: From the provided n(sigma) and alpha(sigma) data at 1.5 K, compute k(sigma) = alpha/(4*pi*sigma) and the reflectance R(sigma) = ((n-1)^2 + k^2)/((n+1)^2 + k^2). Save the wavenumber-reflectance pairs as a CSV file.
- Evidence: `/app/outputs/target_reflectance.csv`

### Step 2: Fit two-resonance Lorentzian model
- Role: scored (load-bearing)
- Action: Using the target reflectance from the previous step, epsilon_inf = 2.2, and the provided room-temperature dispersion parameters as initial guess, fit a Lorentzian oscillator model with two resonances (each described by center wavenumber sigma0, strength S, and width gamma) to minimize the difference between model reflectance and target reflectance. Output the optimized 1.5 K resonance parameters as JSON.
- Output file: `/app/outputs/dispersion_fit_1.5K.json`
- Format: json
- Contract: {
  "resonance1": {"sigma0": float (cm-1), "S": float, "gamma": float},
  "resonance2": {"sigma0": float (cm-1), "S": float, "gamma": float}
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dispersion_fit_1.5K.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dispersion_fit_1.5K.json
- path: `/app/outputs/dispersion_fit_1.5K.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dispersion parameters (center wavenumber, strength, width) for the two lowest-frequency ordinary-ray resonances of quartz at 1.5 K. The checker compares each parameter to the paper's reference values within tolerances; all parameters must be within allowed absolute deviation. This is a deterministic scalar set, so exact_match within tolerance is used (no monotonic 'better' direction).
- schema:
  - `type`: object
  - `required`:
    - `resonance1`:
      - `sigma0`: float (cm-1)
      - `S`: float
      - `gamma`: float
    - `resonance2`:
      - `sigma0`: float (cm-1)
      - `S`: float
      - `gamma`: float

Notes: The target_policy is exact_match because the dispersion parameters are fixed values determined from a specific fitting procedure; 'better' is undefined for a single resonance parameter. The checker will check each numeric value against hidden gold using absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dispersion_fit_1.5K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "resonance1": {
            "sigma0": "float (cm-1)",
            "S": "float",
            "gamma": "float"
          },
          "resonance2": {
            "sigma0": "float (cm-1)",
            "S": "float",
            "gamma": "float"
          }
        }
      },
      "description": "Dispersion parameters (center wavenumber, strength, width) for the two lowest-frequency ordinary-ray resonances of quartz at 1.5 K. The checker compares each parameter to the paper's reference values within tolerances; all parameters must be within allowed absolute deviation. This is a deterministic scalar set, so exact_match within tolerance is used (no monotonic 'better' direction)."
    }
  ],
  "notes": "The target_policy is exact_match because the dispersion parameters are fixed values determined from a specific fitting procedure; 'better' is undefined for a single resonance parameter. The checker will check each numeric value against hidden gold using absolute tolerances."
}
```

## How you are scored
The verifier compares your reported σ₀, S, and γ for both resonances to hidden reference values (the original paper’s published 1.5 K fit). Each of the six parameters is checked against an absolute tolerance. If every parameter lies within its tolerance, you receive the maximum score. For any parameter whose deviation exceeds its tolerance, the reward decreases linearly, reaching zero when the deviation is twice the tolerance. The exact tolerances are not disclosed; they are chosen to accommodate genuine small differences that arise from choice of optimization algorithm, convergence criteria, and floating‑point arithmetic, while still requiring a faithful reproduction of the intended physical result. The verifier reads only the final JSON artifact; intermediate files are not scored. No other artifact or self‑reported metric is considered in the reward.
