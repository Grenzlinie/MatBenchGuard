# Degeneracy Pump Wavelength and Sensitivity Coefficients for GaAs-AlOx Multilayer Waveguide

## Problem background
Form-birefringence in multilayer semiconductor waveguides enables phase matching for nonlinear optical frequency conversion in cubic crystals such as GaAs, which normally lack birefringence. In these structures, the degenerate pump wavelength—the pump wavelength at which the parametric down‑conversion condition is exactly satisfied—and its sensitivity to layer thicknesses and temperature are crucial for device design, tolerancing, and thermal tuning. This task reproduces the numerical determination of the degenerate pump wavelength and its derivatives to GaAs layer thickness, AlOx layer thickness, and temperature for a specific GaAs–AlOx multilayer waveguide, providing insight into the fabrication tolerances and thermal stability of parametric sources.

## Approach
The waveguide is treated as a 1D multilayer stack. The effective indices of the fundamental TM (pump) and TE (signal/idler) modes are computed as functions of wavelength using the transfer‑matrix method. The AlGaAs layers are described by a published wavelength‑ and temperature‑dependent refractive index model that accounts for the bandgap shift; AlOx is taken as a constant low‑index material (n = 1.6). From the dispersion curves, the degenerate pump wavelength lambda_p0 is found by solving the phase‑matching condition beta_TM(lambda_p0) = 2 * beta_TE(2 * lambda_p0). Sensitivity coefficients are then obtained by finite‑difference perturbations of the GaAs and AlOx layer thicknesses (with respect to a relative change) and of the temperature.

## Reproduction target
Compute the following four quantities for the reference waveguide structure (layers defined in Step 1) and write them as a JSON object to `/app/outputs/reproduced_tolerances.json`:
- The degenerate pump wavelength lambda_p0 (nm).
- The derivative of lambda_p0 with respect to GaAs layer thickness, expressed in nm per 1% relative change in that thickness (nm/%).
- The derivative of lambda_p0 with respect to AlOx layer thickness, expressed in nm per 1% relative change in that thickness (nm/%).
- The derivative of lambda_p0 with respect to temperature near room temperature (nm/K).
The workflow steps detail the required numerical procedures.

## Assets

- AlGaAs refractive index model: 10.1016/0038-1098(74)90666-8
- AlOx refractive index constant
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Assemble waveguide structure and refractive index models
- Role: process
- Action: Define the 1D multilayer waveguide stack: GaAs substrate, 1000 nm Al0.92Ga0.08As, 1000 nm Al0.7Ga0.3As, 4x (34.5 nm AlOx, 272 nm GaAs), 34.5 nm AlOx, 1000 nm Al0.7Ga0.3As, 30 nm GaAs cap. Implement wavelength-dependent refractive index n(λ, x) for AlGaAs using a published model (e.g., Afromowitz formulation) and include temperature dependence via the bandgap shift. Set AlOx refractive index to constant 1.6 (no dispersion).
- Evidence: none

### Step 2: Compute 1D TE and TM effective indices
- Role: process
- Action: Using the transfer matrix method (or equivalent slab waveguide solver), compute the effective index of the fundamental TM mode (pump) and the fundamental TE mode (signal/idler) as a function of wavelength over a range covering the degeneracy region (approximately 1000–1200 nm). Record continuous β_TM(λ) and β_TE(λ) curves.
- Evidence: none

### Step 3: Find degeneracy pump wavelength and sensitivity coefficients
- Role: scored (load-bearing)
- Action: From the effective-index curves, numerically solve the phase-matching condition β_TM(λ_p0) = 2·β_TE(2·λ_p0) to obtain the degenerate pump wavelength λ_p0 (nm). Then, by finite differences, perturb GaAs layer thickness by ±1% relative and recompute λ_p0 to obtain ∂λ_p0/∂d_GaAs in nm/%. Similarly for AlOx layer thickness. For temperature, apply the temperature-dependent index shift to AlGaAs layers (AlOx constant) near room temperature (e.g., 300 K) and recompute λ_p0 to obtain ∂λ_p0/∂T in nm/K. Write all four values to reproduced_tolerances.json.
- Output file: `/app/outputs/reproduced_tolerances.json`
- Format: json
- Contract: {"type":"object","properties":{"ref_lambda_p0":{"type":"number","description":"Degenerate pump wavelength in nm"},"dlambda_dGaAs":{"type":"number","description":"Derivative with respect to GaAs thickness in nm per 1% relative change"},"dlambda_dAlox":{"type":"number","description":"Derivative with respect to AlOx thickness in nm per 1% relative change"},"dlambda_dT":{"type":"number","description":"Derivative with respect to temperature in nm/K"}},"required":["ref_lambda_p0","dlambda_dGaAs","dlambda_dAlox","dlambda_dT"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_tolerances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_tolerances.json
- path: `/app/outputs/reproduced_tolerances.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed degenerate pump wavelength and its sensitivities to GaAs layer thickness, AlOx layer thickness, and temperature.
- schema:
  - `type`: object
  - `required`: `ref_lambda_p0`, `dlambda_dGaAs`, `dlambda_dAlox`, `dlambda_dT`
  - `properties`:
    - `ref_lambda_p0`:
      - `type`: number
      - `unit`: nm
    - `dlambda_dGaAs`:
      - `type`: number
      - `unit`: nm per 1% relative GaAs thickness change
    - `dlambda_dAlox`:
      - `type`: number
      - `unit`: nm per 1% relative AlOx thickness change
    - `dlambda_dT`:
      - `type`: number
      - `unit`: nm/K

Notes: The four quantities are scored by comparison against the paper-reported values within tolerances (result-level compare, T0).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_tolerances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "ref_lambda_p0",
          "dlambda_dGaAs",
          "dlambda_dAlox",
          "dlambda_dT"
        ],
        "properties": {
          "ref_lambda_p0": {
            "type": "number",
            "unit": "nm"
          },
          "dlambda_dGaAs": {
            "type": "number",
            "unit": "nm per 1% relative GaAs thickness change"
          },
          "dlambda_dAlox": {
            "type": "number",
            "unit": "nm per 1% relative AlOx thickness change"
          },
          "dlambda_dT": {
            "type": "number",
            "unit": "nm/K"
          }
        }
      },
      "description": "Computed degenerate pump wavelength and its sensitivities to GaAs layer thickness, AlOx layer thickness, and temperature."
    }
  ],
  "notes": "The four quantities are scored by comparison against the paper-reported values within tolerances (result-level compare, T0)."
}
```

## How you are scored
A hidden verifier independently inspects your `reproduced_tolerances.json`. It compares each of the four quantities to a hidden reference value with an appropriate tolerance that accounts for legitimate re‑implementation differences (e.g., choice of refractive index model, solver discretisation). The total reward is the weighted sum across the four quantities. Reporting correct numbers without a correct numerical implementation is not sufficient—the verifier expects the results to be produced by the described workflow.
