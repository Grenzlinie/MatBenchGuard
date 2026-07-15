# Non-monotonic First-Order Diffraction Efficiency in Decaying Gratings via RCWA

## Problem background
When a tall polymer grating is thermally annealed above its glass transition temperature, the pattern height decays monotonically as the structure relaxes toward a flat film. However, the first-order diffraction intensity from such a grating often exhibits a local maximum (a non-monotonic increase and decrease) rather than a simple monotonic decay. The goal is to understand whether this non-monotonic intensity evolution can arise purely from optical resonance and interference effects between the incident light and the evolving grating profile, independent of the polymer's rheological details.

## Approach
Use rigorous coupled-wave analysis (RCWA), an exact electromagnetic method for periodic structures, to model the first-order diffraction efficiency of a grating as its amplitude (height) decreases under material-volume conservation. Two idealized grating profiles are considered on a silicon substrate: (i) rectangular lines and (ii) a sinusoidal profile. The grating period is 400 nm, the initial grating amplitude is 360 nm, and the incident light is TE polarized at a wavelength of 405 nm with an incident angle of 64°. For each profile, the complex refractive indices of silicon (n = 5.47 + 0.24i) and polystyrene (n = 1.49) are used, and the polymer volume is conserved by adjusting the residual layer thickness as the amplitude decreases. The RCWA simulation can be implemented with an open-source solver (e.g., S4) or equivalent code.

## Reproduction target
For both rectangular and sinusoidal profiles, compute the first-order diffraction efficiency (the fraction of incident power diffracted into the first order) as the grating amplitude decreases from 360 nm down to 0 nm, using steps no larger than 10 nm. At each amplitude, conserve the total polymer volume by recalculating the residual layer thickness according to the profile geometry. Record the results in a CSV file with columns: amplitude_nm, efficiency_rect, efficiency_sin.

## Assets

- S4 (RCWA solver) or equivalent open-source implementation: https://github.com/victorliu/S4

## Workflow steps

### Step 1: RCWA Simulation of Diffraction Efficiency vs. Grating Amplitude
- Role: scored (load-bearing)
- Action: Implement rigorous coupled-wave analysis (RCWA) for two grating profiles on a 400 nm period substrate: (i) rectangular lines with initial height 360 nm, width 240 nm, residual layer 50 nm; (ii) sinusoidal profile with peak-to-valley amplitude 360 nm, initial residual layer 50 nm. For each profile, decrease the grating amplitude from 360 nm down to 0 nm while conserving the polymer material volume by increasing the residual layer thickness according to the volume-conservation mapping. Use s-polarization (TE), incident angle 64°, wavelength 405 nm, with substrate complex refractive index 5.47+0.24i and polymer refractive index 1.49. Compute the first-order diffraction efficiency at each amplitude. Write a CSV file with the columns amplitude_nm, efficiency_rect, efficiency_sin containing the amplitude and the two efficiency curves over the full amplitude range.
- Output file: `/app/outputs/step_01_rcwa_results.csv`
- Format: csv
- Contract: CSV with header: amplitude_nm, efficiency_rect, efficiency_sin. Each row has a float amplitude (nm) and two corresponding efficiency values (unitless, range [0,1]). The amplitude decreases monotonically over at least 20 rows covering the full range 360 nm to 0 nm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_rcwa_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_rcwa_results.csv
- path: `/app/outputs/step_01_rcwa_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: First-order diffraction efficiency as a function of decreasing grating amplitude for rectangular and sinusoidal profiles, computed via RCWA.
- schema:
  - `type`: table
  - `required_columns`: `amplitude_nm`, `efficiency_rect`, `efficiency_sin`
  - `units`:
    - `amplitude_nm`: nanometer
    - `efficiency_rect`: fraction
    - `efficiency_sin`: fraction

Notes: The verification method is automated and does not require comparison to specific numeric targets.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_rcwa_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "amplitude_nm",
          "efficiency_rect",
          "efficiency_sin"
        ],
        "units": {
          "amplitude_nm": "nanometer",
          "efficiency_rect": "fraction",
          "efficiency_sin": "fraction"
        }
      },
      "description": "First-order diffraction efficiency as a function of decreasing grating amplitude for rectangular and sinusoidal profiles, computed via RCWA."
    }
  ],
  "notes": "The verification method is automated and does not require comparison to specific numeric targets."
}
```

## How you are scored
A hidden verifier will evaluate your output CSV to determine whether the computed diffraction efficiency curves are physically correct. The verifier does not compare against a specific numeric target; it assesses the overall qualitative behavior of the curves.
