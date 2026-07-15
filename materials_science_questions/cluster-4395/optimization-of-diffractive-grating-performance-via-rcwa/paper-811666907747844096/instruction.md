# Simulation of Cross-Stacked Grating Broadband Reflector and Fabry-Perot Cavity Resonance

## Problem background
Subwavelength gratings can act as broadband mirrors, but single-layer gratings are inherently polarization-dependent because of the one-dimensional structure. By stacking two grating layers with orthogonal orientations (cross-stacked), it may be possible to achieve polarization-independent high reflectivity. However, the reflection phase experienced by the two polarizations may differ, which influences the behavior of Fabry-Perot cavities formed with such reflectors. This task aims to simulate a cross-stacked silicon grating to determine its reflectance and phase spectra for TE and TM polarizations, and to analyze whether a face-to-back Fabry-Perot cavity built from two such reflectors yields polarization-independent resonant modes.

## Approach
The cross-stacked grating is modeled as two silicon layers (refractive index 3.48) each 230 nm thick, with a period of 980 nm and a fill factor of 0.2, the two gratings oriented orthogonally. Using an open-source electromagnetic solver (e.g., rigorous coupled-wave analysis or finite-difference time-domain), the normal-incidence reflectance and unwrapped reflection phase for both TE and TM polarizations are computed over the wavelength range 1.4–1.65 μm. The obtained phase data are then used to solve the Fabry-Perot cavity resonance condition: \(4\pi L_c/\lambda - \phi_{\mathrm{TE}}(\lambda) - \phi_{\mathrm{TM}}(\lambda) = 2\pi m\) for integer \(m\), with cavity length \(L_c = 6\,\mu\mathrm{m}\) in the face-to-back configuration. This determines the resonant wavelength(s) and allows verification of whether the resonance is identical for both starting polarizations.

## Reproduction target
Produce two CSV files under `/app/outputs`:
- `csSWG_reflection.csv`: columns `wavelength_um` (float), `R_TE` (float), `R_TM` (float), `phi_TE_rad` (float), `phi_TM_rad` (float), `phi_diff_rad` (float). At least 20 rows covering 1.4–1.65 μm.
- `cavity_resonance.csv`: columns `cavity_config` (string, 'FtB'), `cavity_length_um` (float, 6.0), `resonance_wavelength_um` (float), `polarization_independent` (bool). One row.

The goal is to compute the broadband reflectance and phase behavior of the cross-stacked grating and to extract from those results the polarization-independent resonant wavelength of the face-to-back cavity. The exact values will be evaluated by a hidden verifier against reference data derived from the original study.

## Assets

- Open-source electromagnetic solver (S4/RCWA or MEEP/FDTD): https://github.com/vlnvu/S4
- Python scientific stack (numpy, scipy, matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Simulate cs‑SWG reflection and phase
- Role: scored
- Action: Set up a cross-stacked grating: two orthogonally oriented silicon layers (refractive index 3.48), each with thickness 230 nm, period 980 nm, fill factor 0.2. Using an electromagnetic solver (RCWA or FDTD), compute the normal-incidence reflection amplitude and unwrapped reflection phase for TE and TM polarizations over 1.4–1.65 µm (at least 20 wavelength samples). Write the extracted data to the output CSV.
- Output file: `/app/outputs/csSWG_reflection.csv`
- Format: csv
- Contract: columns: wavelength_um (float), R_TE (float), R_TM (float), phi_TE_rad (float), phi_TM_rad (float), phi_diff_rad (float). Each row corresponds to a wavelength sample.
- Scoring: scored by hidden verifier

### Step 2: Compute cavity resonance
- Role: scored (load-bearing)
- Action: Read the reflection phases φ_TE(λ) and φ_TM(λ) from the output of the previous step. For a cavity length Lc=6 µm in the face-to-back configuration, evaluate the round-trip phase condition and find the resonant wavelength(s) where 4πLc/λ − φ_TE(λ) − φ_TM(λ) = 2π m for integer m within the 1.4–1.65 µm range. Confirm that the resonance is identical for both starting polarizations (polarization-independent). Write one result row to the output CSV.
- Output file: `/app/outputs/cavity_resonance.csv`
- Format: csv
- Contract: columns: cavity_config (string, 'FtB'), cavity_length_um (float, 6.0), resonance_wavelength_um (float), polarization_independent (bool, True).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/csSWG_reflection.csv`
- `/app/outputs/cavity_resonance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### csSWG_reflection.csv
- path: `/app/outputs/csSWG_reflection.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Scored on whether broadband reflectance exceeds 0.99 for both polarizations and the phase difference lies within the expected range, using thresholds that absorb legitimate numerical toolchain differences.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_um`, `R_TE`, `R_TM`, `phi_TE_rad`, `phi_TM_rad`, `phi_diff_rad`
  - `units`:
    - `wavelength_um`: µm
    - `R_TE`: reflectance (0-1)
    - `R_TM`: reflectance (0-1)
    - `phi_TE_rad`: radians
    - `phi_TM_rad`: radians
    - `phi_diff_rad`: radians

### cavity_resonance.csv
- path: `/app/outputs/cavity_resonance.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Scored on the computed polarization-independent resonant wavelength for the face-to-back cavity with Lc=6 µm. The hidden reference value is compared within a tolerance that accounts for simulation toolchain differences.
- schema:
  - `type`: table
  - `required_columns`: `cavity_config`, `cavity_length_um`, `resonance_wavelength_um`, `polarization_independent`
  - `units`:
    - `cavity_config`: string
    - `cavity_length_um`: µm
    - `resonance_wavelength_um`: µm
    - `polarization_independent`: boolean

Notes: The parameter variation studies and the face-to-face cavity are omitted from this minimal reproduction, as stated in the approved scope. The solver grid/convergence settings are left to the agent’s discretion.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "csSWG_reflection.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_um",
          "R_TE",
          "R_TM",
          "phi_TE_rad",
          "phi_TM_rad",
          "phi_diff_rad"
        ],
        "units": {
          "wavelength_um": "µm",
          "R_TE": "reflectance (0-1)",
          "R_TM": "reflectance (0-1)",
          "phi_TE_rad": "radians",
          "phi_TM_rad": "radians",
          "phi_diff_rad": "radians"
        }
      },
      "description": "Scored on whether broadband reflectance exceeds 0.99 for both polarizations and the phase difference lies within the expected range, using thresholds that absorb legitimate numerical toolchain differences."
    },
    {
      "file": "cavity_resonance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cavity_config",
          "cavity_length_um",
          "resonance_wavelength_um",
          "polarization_independent"
        ],
        "units": {
          "cavity_config": "string",
          "cavity_length_um": "µm",
          "resonance_wavelength_um": "µm",
          "polarization_independent": "boolean"
        }
      },
      "description": "Scored on the computed polarization-independent resonant wavelength for the face-to-back cavity with Lc=6 µm. The hidden reference value is compared within a tolerance that accounts for simulation toolchain differences."
    }
  ],
  "notes": "The parameter variation studies and the face-to-face cavity are omitted from this minimal reproduction, as stated in the approved scope. The solver grid/convergence settings are left to the agent’s discretion."
}
```

## How you are scored
A hidden verifier will independently score each output file and combine them into a final reward.

- For `csSWG_reflection.csv`, the checker will verify that the reflectance values for both TE and TM polarizations satisfy a high-reflectance criterion over the broadband range and that the TE–TM phase difference lies within a specified numerical range. The thresholds and tolerances are hidden.
- For `cavity_resonance.csv`, the checker will confirm that the cavity configuration and length match the required values, that the resonant wavelength falls within an allowed tolerance of the expected value, and that the polarization independence flag is correctly set to `True`.

Both files must be present and adhere to the column schema. Reporting values that meet these hidden acceptance criteria yields full credit; deviations reduce the reward. Exact scoring weights are defined in the grading specification and are not disclosed.
