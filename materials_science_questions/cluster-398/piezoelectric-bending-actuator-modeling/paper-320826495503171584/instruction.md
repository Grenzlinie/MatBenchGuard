# Sound Absorption in Compensated Piezoelectric Semiconductors: Model Implementation and Trend Verification

## Problem background
Piezoelectric semiconductors such as CdS and CdSe exhibit sound absorption due to electron-phonon interaction. In a homogeneous crystal, the absorption coefficient α as a function of electrical conductivity σ is expected to follow a symmetric relaxation peak with its maximum at σ = εω (the Maxwell relaxation condition). However, experimental measurements reveal systematic deviations: when the conductivity is varied by temperature versus illumination, the conductivity at the absorption peak shifts, and the peak amplitude differs between crystals despite similar coupling coefficients. These anomalies suggest that an internal random large-scale potential arising from impurity compensation influences the absorption. This task implements a theoretical model that incorporates such a random potential and explores its effect on the absorption maximum.

## Approach
We consider a compensated piezoelectric semiconductor in which fluctuations in donor and acceptor concentrations produce a large-scale random potential. The potential distribution is modeled as Gaussian with rms amplitude Δ. Only electrons with energies above the percolation level contribute to low-frequency absorption (ω ≪ ω_d). By locally solving the coupled elasticity–Maxwell equations and then averaging the local absorption over the potential distribution, one obtains an expression for the macroscopic α.

In the strong-compensation limit (when Δ is large compared to the thermal energy), the absorption coefficient α (in cm⁻¹) is given by

\[
\alpha \approx 0.7\;\eta^{2}\;\frac{\omega\,T}{\Delta\,v_{0}}\;\arctan\!\left[\frac{\omega\,\tau_{c}\,\exp(2.1\,\Delta/T)}{1+\omega^{2}\tau_{c}^{2}\,\exp(2.1\,\Delta/T)}\right],
\]

where \(v_{0} = \sqrt{c/\rho}\) is the sound velocity,
\[
\tau_{c} = \frac{\varepsilon}{q\,\mu\,N_{c}}\exp\!\left(-\frac{\xi + 0.68\,\Delta}{T}\right),
\]
and the electron density and conductivity are linked by
\[
n_{c} = N_{c}\,\exp\!\left(\frac{\xi + 0.68\,\Delta}{T}\right),\qquad \sigma = q\,\mu\,n_{c}.
\]

(This is the strong-compensation limit from Eq. (15) of the original paper.) The task implements this limiting form for CdS using the given set of material constants.

Two distinct methods of controlling the conductivity are simulated:

1. **Temperature variation** (300–900 K): the electron density n_c depends exponentially on temperature through the chemical potential and the random potential, altering both σ and the effect of Δ/T simultaneously.
2. **Illumination variation** (fixed T = 300 K): the electron density n_c is varied directly, changing σ while keeping Δ/T constant.

For each scenario, α(σ) is evaluated on a dense grid. The conductivity at the absorption maximum (σ_T for temperature, σ_I for illumination) is extracted by peak detection. The homogeneous Maxwell relaxation conductivity σ_hom = ε ω is computed for comparison, and the results are used to test the predicted trends regarding the relative magnitudes of σ_T, σ_I, and σ_hom.

## Reproduction target
Implement the described strong-compensation absorption model for CdS using the prescribed physical parameters (ε, η, v₀, ρ, c, μ, N_c, Δ, ξ, T₀, ω, ω₀). Write the results to `/app/outputs/absorption_results.json` with the following contents:

- `params`: an object listing all used constants and model parameters.
- `curves`: an array of two objects, each with key `scenario` ("temperature" or "illumination") and parallel arrays `sigma` (conductivity in S/cm) and `alpha` (absorption coefficient in cm⁻¹) computed on a sufficiently dense grid.
- `temperature_maximum`: an object with `sigma_T` and `alpha_T`, the conductivity and absorption at the peak of the temperature-varied curve.
- `illumination_maximum`: an object with `sigma_I` and `alpha_I`, the corresponding values for the illumination-varied curve.
- `homogeneous_sigma`: the computed ε·ω product (S/cm).
- `verification`: an object with booleans `sigma_T_gt_sigma_I` (whether σ_T > σ_I) and `sigma_T_not_equal_homogeneous` (whether |σ_T − homogeneous_sigma| exceeds a negligible relative threshold).

The booleans must be derived from the extracted maxima, not hardcoded. The curves must be dense enough to resolve the maxima accurately.

## Assets

- numpy: numpy
- scipy: scipy
- matplotlib: matplotlib

## Workflow steps

### Step 1: Compute absorption curves and extract maxima
- Role: scored (load-bearing)
- Action: Implement the strong-compensation limit of the sound absorption coefficient model for a compensated piezoelectric semiconductor with a Gaussian random potential. For CdS, using the provided material constants (ε, η, v0, ρ, c, μ, Nc, Δ, ξ, T0, ω, ω0), compute the absorption coefficient α as a function of electrical conductivity σ for two scenarios: (a) varying temperature T from 300 to 900 K, where the electron density n_c depends exponentially on T through the chemical potential and rms potential; (b) varying n_c directly at fixed T = 300 K (simulating illumination variation). For each scenario, record the computed (σ, α) pairs on a dense grid. Locate the conductivity σ_T and σ_I at the respective absorption maxima by peak detection. Compute the homogeneous Maxwell relaxation conductivity σ_hom = ε ω. Write absorption_results.json with all results and boolean flags for the trends σ_T > σ_I and σ_T ≠ σ_hom.
- Output file: `/app/outputs/absorption_results.json`
- Format: json
- Contract: JSON object with keys: params (object with all physical constants and model parameters used), curves (array of two objects, each containing 'scenario' (string 'temperature' or 'illumination'), 'sigma' (list of conductivities in S/cm), 'alpha' (list of absorption coefficients in cm^{-1})), temperature_maximum (object with 'sigma_T' (S/cm) and 'alpha_T' (cm^{-1})), illumination_maximum (object with 'sigma_I' (S/cm) and 'alpha_I' (cm^{-1})), homogeneous_sigma (float, εω in S/cm), verification (object with booleans 'sigma_T_gt_sigma_I' and 'sigma_T_not_equal_homogeneous').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/absorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### absorption_results.json
- path: `/app/outputs/absorption_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Scored artifact providing the raw absorption curves and derived quantities that the verifier will recompute against hidden reference parameters to evaluate correct implementation and trend verification.
- schema:
  - `type`: object
  - `required`:
    - `params`: object
    - `curves`: array of objects
    - `temperature_maximum`: object
    - `illumination_maximum`: object
    - `homogeneous_sigma`: number
    - `verification`: object
  - `properties_description`: params: object containing all physical constants and model parameters used (e.g., epsilon, eta, v0, Delta, xi, Nc, mu, omega, T0). curves: array of two objects, each with 'scenario' (string 'temperature' or 'illumination'), 'sigma' (list of floats in S/cm), 'alpha' (list of floats in cm^{-1}). temperature_maximum: object with 'sigma_T' (float in S/cm) and 'alpha_T' (float in cm^{-1}) extracted from the temperature-varied computation. illumination_maximum: object with 'sigma_I' (float in S/cm) and 'alpha_I' (float in cm^{-1}) extracted from the illumination-varied computation. homogeneous_sigma: epsilon * omega (float in S/cm). verification: object with 'sigma_T_gt_sigma_I' (bool) indicating whether σ_T > σ_I, and 'sigma_T_not_equal_homogeneous' (bool) indicating whether |σ_T - σ_hom| exceeds a small relative threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "absorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "params": "object",
          "curves": "array of objects",
          "temperature_maximum": "object",
          "illumination_maximum": "object",
          "homogeneous_sigma": "number",
          "verification": "object"
        },
        "properties_description": "params: object containing all physical constants and model parameters used (e.g., epsilon, eta, v0, Delta, xi, Nc, mu, omega, T0). curves: array of two objects, each with 'scenario' (string 'temperature' or 'illumination'), 'sigma' (list of floats in S/cm), 'alpha' (list of floats in cm^{-1}). temperature_maximum: object with 'sigma_T' (float in S/cm) and 'alpha_T' (float in cm^{-1}) extracted from the temperature-varied computation. illumination_maximum: object with 'sigma_I' (float in S/cm) and 'alpha_I' (float in cm^{-1}) extracted from the illumination-varied computation. homogeneous_sigma: epsilon * omega (float in S/cm). verification: object with 'sigma_T_gt_sigma_I' (bool) indicating whether σ_T > σ_I, and 'sigma_T_not_equal_homogeneous' (bool) indicating whether |σ_T - σ_hom| exceeds a small relative threshold."
      },
      "description": "Scored artifact providing the raw absorption curves and derived quantities that the verifier will recompute against hidden reference parameters to evaluate correct implementation and trend verification."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently reconstructs the same absorption model using reference parameters (the same physical constants, rms potential Δ, chemical potential ξ, etc.) and the strong-compensation formula. It recomputes the absorption curves, extracts the peak conductivities, and evaluates the verification booleans. Your submission is scored by comparing your `curves`, `temperature_maximum`, `illumination_maximum`, and `verification` fields against the verifier's own recomputed values. Full credit is earned when the curves match within a tight relative tolerance, the extracted peak conductivities are consistent, and the booleans are correct. The final reward is a weighted combination of these per-stage scores. Simply reporting numbers from the literature without a correct underlying computation will not satisfy the scoring criteria.
