# Optical absorption enhancement in textured organic photovoltaic cells via electromagnetic simulation

## Problem background
Organic photovoltaic (OPV) cells typically require thin active layers (on the order of 100–200 nm) to mitigate low charge carrier mobilities and reduce recombination losses. However, such thin layers absorb only a fraction of the incident sunlight, limiting device efficiency. One promising route to resolve this trade-off is to pattern the bottom electrode into a microscale grating texture that traps light inside the active layer via diffraction and total internal reflection, thereby enhancing absorption without increasing the electrical transport distance. This reproduction task investigates the optical absorption enhancement achievable with a tapered grating geometry by performing rigorous electromagnetic simulations and computing the spectrally integrated absorbed power in the active layer under solar illumination.

## Approach
The core idea is to model light propagation in a multilayer OPV stack — ITO (100 nm) / PEDOT:PSS (50 nm) / active layer (150 nm P3HT:PCBM blend) / Ti back contact (250 nm) — using an electromagnetic solver capable of handling two‑dimensional periodic structures. Two configurations are compared: a planar (flat) reference cell and a textured cell where the bottom electrode has a tapered grating profile (pitch 2 µm, height 1.5 µm, opening width 0.7×pitch, bottom width 0.1×pitch). The active layer and other layers conformally coat the grating. For each configuration, the electric field distribution is solved under transverse‑electric (TE) polarized normal incidence over the wavelength range 300–700 nm. The electromagnetic power dissipation density per unit volume in the active layer is then integrated spatially over the active region and spectrally weighted by the AM1.5 solar spectrum, yielding total absorbed power (W/m²) normalized to a 1 µm pitch area. To ensure the solver and material optical constants are correctly set up, the planar simulation is validated against an independent transfer‑matrix method (TMM) calculation before proceeding to the textured geometry.

## Reproduction target
Simulate the planar and textured (2 µm pitch, 1.5 µm height) OPV stacks, both with a 150 nm active layer, under TE‑polarized normal incidence. Compute the spectrally integrated (300–700 nm, AM1.5‑weighted) absorbed power in the active layer for each geometry, expressed in W/m² after normalizing to the incident power on a 1 µm wide unit cell. Output these two quantities together with their ratio (textured/planar) in the file `absorption_results.json`. As a required intermediate, validate the planar solver result against a TMM calculation of the same stack, documenting the agreement.

## Assets

- Optical constants of P3HT:PCBM (Lioudakis et al. 2007): 10.1063/1.2817639
- Optical constants of PEDOT:PSS (Pettersson et al. 1999): 10.1016/S0040-6090(98)00467-2
- Optical constants of ITO (Bartella et al. 2001): 10.1016/S0169-4332(01)00266-1
- Optical constants of Ti (Johnson and Christy 1974): 10.1103/PhysRevB.9.5056
- AM1.5 Global tilt solar spectrum: https://www.nrel.gov/grid/solar-resource/spectra-am1.5.html
- Open-source electromagnetic solver (e.g., S4, meep, FDTD): meep, or S4 (RCWA), or custom FDTD

## Workflow steps

### Step 1: Gather material optical constants and AM1.5 spectrum
- Role: process
- Action: Collect wavelength-dependent complex refractive indices (n+ik) for ITO, PEDOT:PSS, P3HT:PCBM, and Ti from the cited literature sources, and obtain the AM1.5 solar spectrum. Interpolate all data onto a common wavelength grid covering 300–700 nm with sufficient resolution.
- Evidence: `/app/outputs/data_gathered.log`

### Step 2: Compute TMM reference for planar stack
- Role: process
- Action: Implement a transfer-matrix method (TMM) code to calculate the absorptance (or absorbed power) spectrum of the planar OPV stack (ITO 100 nm / PEDOT:PSS 50 nm / active layer 150 nm / Ti 250 nm) under TE-polarized normal incidence, using the gathered optical constants.
- Evidence: `/app/outputs/tmm_absorption.csv`

### Step 3: Implement and validate electromagnetic solver on planar geometry
- Role: process
- Action: Set up an open-source electromagnetic solver for the planar multilayer stack. Compute the absorbed power spectrum using the same geometry and materials as in step2. Validate that the solver's integrated absorbed power (or reflectance spectrum) agrees with the TMM result within a small margin, confirming correct implementation of optical constants and solver settings. Document the comparison.
- Evidence: `/app/outputs/solver_validation.log`

### Step 4: Simulate textured geometry and compute absorption enhancement
- Role: scored (load-bearing)
- Action: Using the validated solver, simulate TE-polarized normal incidence on the textured geometry: tapered grating with pitch = 2 µm, height = 1.5 µm, opening width = 0.7×pitch, bottom width = 0.1×pitch, conformal coating of the active layer (150 nm), PEDOT:PSS (50 nm), ITO (100 nm), and Ti bottom. Also simulate the planar geometry (same layer thicknesses). For each, compute the electromagnetic power dissipation Q per unit volume in the active layer, integrate over the active volume at each wavelength, weight by the AM1.5 spectrum, sum over 300–700 nm, and normalize to the incident power on a 1 µm pitch area. Output the integrated absorbed powers and the enhancement ratio (textured/planar).
- Output file: `/app/outputs/absorption_results.json`
- Format: json
- Contract: {"planar_absorbed_power_W_m2": "float", "textured_absorbed_power_W_m2": "float", "enhancement_ratio": "float"}
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
- target_policy: threshold_or_better
- description: Integrated absorbed power (W/m²) under AM1.5, TE polarization, 150 nm active layer for planar and textured (2 µm pitch, 1.5 µm height) cells, and the ratio textured/planar.
- schema:
  - `type`: object
  - `required`:
    - `planar_absorbed_power_W_m2`: float
    - `textured_absorbed_power_W_m2`: float
    - `enhancement_ratio`: float

Notes: The hidden checker compares the enhancement_ratio to a reference and also verifies positive absorbed powers. TMM and solver validation are required process steps with load-bearing effect on this artifact.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "planar_absorbed_power_W_m2": "float",
          "textured_absorbed_power_W_m2": "float",
          "enhancement_ratio": "float"
        }
      },
      "description": "Integrated absorbed power (W/m²) under AM1.5, TE polarization, 150 nm active layer for planar and textured (2 µm pitch, 1.5 µm height) cells, and the ratio textured/planar."
    }
  ],
  "notes": "The hidden checker compares the enhancement_ratio to a reference and also verifies positive absorbed powers. TMM and solver validation are required process steps with load-bearing effect on this artifact."
}
```

## How you are scored
A hidden verifier reads your submitted `absorption_results.json` and compares the reported `enhancement_ratio` against a reference value, and checks that both `planar_absorbed_power_W_m2` and `textured_absorbed_power_W_m2` are positive. The reward is based on how closely your result meets or exceeds the reference threshold; a result that demonstrates equivalent or better enhancement earns full credit, while an insufficient or missing enhancement earns proportionally less. The intermediate TMM validation and solver agreement are mandatory process steps — they must be executed and documented in the evidence files, but their numerical agreement is not directly scored.
