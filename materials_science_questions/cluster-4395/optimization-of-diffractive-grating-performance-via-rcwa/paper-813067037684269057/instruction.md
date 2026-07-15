# Optimization of Diffractive Grating Performance via RCWA

## Problem background
Sub-wavelength high-contrast gratings (HCGs) can locally control the phase of transmitted light, enabling flat optical components. A one-layer non-periodic silicon grating with varying bar thicknesses can act as a focusing lens for TE-polarized light (electric field parallel to the grating bars) at normal incidence. The design problem is to achieve high total transmission and a tight focal spot using a practical fabrication approach: a grating with two different bar thicknesses that together provide a full 0–2π phase shift range. The task is to computationally design such a lens and determine the achievable total transmissivity and focal‑plane full‑width at half‑maximum (FWHM).

## Approach
The design method uses Rigorous Coupled Wave Analysis (RCWA) to compute the transmitted amplitude and phase shift of periodic unit cells as functions of period (Λ) and duty cycle (τ) for two thicknesses (1.3 µm and 1.2 µm) of silicon bars (refractive index 3.48) in air (index 1.0), for TE polarization at 1550 nm. From these RCWA sweeps, only (Λ, τ) pairs with transmittance above 90% are retained for each thickness. The selected points are sorted by their transmitted phase, and the two sorted lists are concatenated to cover the full 0–2π range. The target phase profile for a focusing lens with focal length 7 µm is computed using the hyperbolic phase formula Φ(x) = (2π/λ)(√(x²+f²) – f) + Φ₀, taken modulo 2π. For each lateral position x across a 26 µm aperture, the nearest available phase in the combined list is chosen, and the corresponding (Λ, τ, thickness) triple is assigned to that grating bar. The resulting non‑periodic grating is then simulated with a full‑wave electromagnetic solver (FEM or FDTD) to obtain the steady‑state field distribution, from which total transmissivity and focal‑plane FWHM are extracted. All computations use open‑source tools (e.g., S4 or grcwa for RCWA, MEEP for FEM/FDTD).

## Reproduction target
Implement the design workflow and simulate the resulting lens. Evaluate the total transmissivity (the fraction of normally incident TE-polarized power at 1550 nm transmitted to the far side) and the full‑width at half‑maximum (FWHM, in µm) of the intensity distribution at the focal plane. Report these two values in the scored output file `performance.json`. The target focal length is 7 µm, and the lens aperture is 26 µm.

## Assets

- S4 RCWA simulation tool: https://web.stanford.edu/group/fan/S4/
- MEEP FDTD electromagnetic simulation tool: https://meep.readthedocs.io/

## Workflow steps

### Step 1: RCWA unit-cell scan for two thicknesses
- Role: process
- Action: Use an open-source RCWA solver to compute, for TE-polarized light at 1550 nm, the transmitted amplitude (transmittivity) and phase shift of periodic unit cells as functions of period Λ (0.4–1.2 µm) and duty cycle τ (0.2–0.9) for the two thicknesses tg = 1.3 µm and tg = 1.2 µm. Save the resulting 2D arrays.
- Evidence: `/app/outputs/rcwa_scan.npz`

### Step 2: Select high-transmittance points
- Role: process
- Action: For each thickness, filter the RCWA results to retain only the (Λ, τ) pairs whose transmittivity exceeds 90%.
- Evidence: `/app/outputs/selected_points.json`

### Step 3: Sort selected points by phase
- Role: process
- Action: For each thickness, sort the high-transmittance (Λ, τ) points by their associated transmitted phase shift to create an ordered list of attainable high‑transmission phases.
- Evidence: `/app/outputs/sorted_phase_lists.json`

### Step 4: Concatenate phase lists from two thicknesses
- Role: process
- Action: Concatenate the sorted phase lists: first the tg=1.3 µm list, then the tg=1.2 µm list, to form a single combined list that spans the full 0–2π rad range. Each entry carries the associated (Λ, τ, tg) triple.
- Evidence: `/app/outputs/combined_phase_list.json`

### Step 5: Compute target phase profile and assemble grating layout
- Role: process
- Action: Compute the target hyperbolic phase profile Φ(x) = (2π/λ)(√(x²+f²) – f) + Φ0 for focal length f = 7 µm at λ = 1550 nm, modulo 2π. Choose an appropriate initial phase. For each lateral position x across the lens aperture (total size 26 µm), map the target phase to the nearest available phase in the combined list and assign the corresponding (Λ, τ, tg) to that grating bar. Assemble the complete non-periodic grating layout.
- Evidence: `/app/outputs/grating_layout.json`

### Step 6: Full-device simulation and performance evaluation
- Role: scored (load-bearing)
- Action: Simulate the designed grating lens using an open-source electromagnetic solver for TE-polarized plane-wave illumination at normal incidence and λ = 1550 nm. Extract the total transmissivity (ratio of transmitted power to incident power) and the full-width at half-maximum (FWHM) of the intensity distribution at the focal plane. Write these two values as a JSON object with keys 'transmittance' and 'fwhm_um' into 'performance.json'.
- Output file: `/app/outputs/performance.json`
- Format: json
- Contract: {"transmittance": <float between 0 and 1>, "fwhm_um": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/performance.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### performance.json
- path: `/app/outputs/performance.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Total transmissivity and full-width half-maximum at the focal plane of the designed grating focusing lens, obtained from full-device electromagnetic simulation.
- schema:
  - `type`: object
  - `required`:
    - `transmittance`: number (float, 0 to 1)
    - `fwhm_um`: number (float, positive)

Notes: The hidden scoring checks that transmittance >= hidden threshold and FWHM <= hidden threshold. Both conditions must be met for full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "performance.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "transmittance": "number (float, 0 to 1)",
          "fwhm_um": "number (float, positive)"
        }
      },
      "description": "Total transmissivity and full-width half-maximum at the focal plane of the designed grating focusing lens, obtained from full-device electromagnetic simulation."
    }
  ],
  "notes": "The hidden scoring checks that transmittance >= hidden threshold and FWHM <= hidden threshold. Both conditions must be met for full credit."
}
```

## How you are scored
A hidden verifier inspects the intermediate evidence artifacts for each workflow step and applies weights to each stage. The final scored output (`performance.json`) carries the largest weight. The verifier compares the reported transmittance and FWHM against hidden thresholds derived from the reference design expectations. Simply reporting the paper’s values without executing the RCWA scan, phase mapping, and full-device simulation will not satisfy the scoring. To receive full credit, all required process steps must leave valid evidence, and the final performance metrics must meet or exceed the hidden quality thresholds.
