# RCWA-based sensitivity and figure-of-merit analysis of thin planar dielectric grating SPR sensor

## Problem background
Surface plasmon resonance (SPR) sensors that couple light to surface plasmons via thin planar dielectric gratings on a flat metallic substrate promise high sensitivity and simple fabrication. In this work, rigorous coupled‑wave analysis (RCWA) is used to study how grating parameters — thickness, slant angle, and period — influence the resonant modes and sensing performance. The aim is to identify an optimal grating configuration and quantify its sensitivity and figure of merit for refractive index sensing.

## Approach
The method is based on RCWA, which computes the electromagnetic response of a periodic layered structure. The sensor consists of a planar sinusoidal dielectric grating of thickness d on a silver substrate. The grating’s relative permittivity is modulated as ε(x,z)=ε2 + δ cos[K (x sin φ + z cos φ)], where ε2 is the average permittivity, δ is the modulation amplitude, φ is the slant angle, and the grating vector magnitude is K=2π/Λ with period Λ. The silver substrate’s complex permittivity is modeled by a Drude function with plasma frequency ω_p = 1.37×10^16 rad/s and collision frequency γ = 7.29×10^13 rad/s. For p‑polarized incident light at 633 nm, RCWA yields the 0th‑order reflectivity as a function of incident angle. By scanning the incident angle, a sharp reflectance dip (the surface plasmon resonance) is observed; its angular position is the resonance angle and its width is the full‑width at half‑maximum (FWHM). For two configurations (slant φ=60° and unslant φ=90°, both with Λ=400 nm, d=60 nm, ε2=2.25, δ=0.33), the refractive index of the region above the grating (analyte) is varied, and the shift in resonance angle is recorded. A linear regression of resonance angle vs. refractive index gives the sensitivity in degrees per refractive index unit (deg/RIU). Finally, a figure of merit (FOM) is computed from the slant‑grating sensitivity and FWHM according to the definition FOM = m(eV/RIU) / FWHM(eV), where m is the sensitivity converted to energy units.

## Reproduction target
Implement an RCWA solver that can handle 1D dielectric gratings on a Drude‑metal substrate. Use it to:
1) Compute 0th‑order reflectivity vs. incident angle for three grating configurations (all with ε2=2.25, δ=0.33, d=60 nm):
   - unslant (φ=90°) with Λ=400 nm
   - slant (φ=60°) with Λ=400 nm
   - unslant (φ=90°) with Λ=500 nm
   For each, extract the resonance angle (angle of minimum reflectivity) and the FWHM of the dip.
2) For the unslant (φ=90°) and slant (φ=60°) configurations with Λ=400 nm, d=60 nm, vary the analyte refractive index (Region I) from 1.00 to 1.05 in steps of 0.01. At each index compute the 0th‑order reflectivity vs. angle and extract the resonance angle.
3) From the collected resonance angle vs. refractive index data, perform a linear regression for each configuration to obtain the sensitivity in deg/RIU. Using the slant configuration’s FWHM from step 1, compute the FOM according to the definition FOM = m(eV/RIU) / FWHM(eV), where m is the sensitivity expressed in energy units.
All results must be written to the exact output files and formats specified in the workflow steps.

## Assets

- RCWA solver (e.g., S4 or Python rcwa package): https://github.com/victorliu/S4

## Workflow steps

### Step 1: Compute resonance angles and FWHMs for three grating configurations
- Role: scored
- Action: Using RCWA at 633 nm p‑polarized light, compute the 0th‑order reflectivity versus incident angle for three grating configurations: (i) unslant φ=90°, Λ=400 nm, d=60 nm, ε2=2.25, δ=0.33; (ii) slant φ=60°, same Λ and d; (iii) unslant φ=90°, Λ=500 nm, d=60 nm. For each, locate the resonance angle (angle of minimum reflectivity) and compute the full‑width at half‑minimum (FWHM) of the dip. Write the three rows to step_01_resonance_angles.csv.
- Output file: `/app/outputs/step_01_resonance_angles.csv`
- Format: csv
- Contract: columns: configuration (string: one of 'unslant_90deg', 'slant_60deg', 'period_500nm'), resonance_angle_deg (float), FWHM_deg (float)
- Scoring: scored by hidden verifier

### Step 2: Sweep analyte refractive index and extract resonance angles for slant and unslant gratings
- Role: scored
- Action: For the two configurations with Λ=400 nm, d=60 nm (slant φ=60° and unslant φ=90°), vary the refractive index of Region I from 1.00 to 1.05 in steps of 0.01. At each index run RCWA to compute 0th‑order reflectivity versus incident angle and extract the resonance angle. Write the collected data to step_02_sensitivity_data.csv, with one row per configuration‑index pair.
- Output file: `/app/outputs/step_02_sensitivity_data.csv`
- Format: csv
- Contract: columns: configuration (string: 'slant_60deg' or 'unslant_90deg'), refractive_index (float from 1.00 to 1.05, step 0.01), resonance_angle_deg (float)
- Scoring: scored by hidden verifier

### Step 3: Compute sensitivity and figure of merit
- Role: scored (load-bearing)
- Action: From step_02 data, perform a linear regression of resonance angle vs. refractive index for each configuration to obtain the sensitivity in degrees per refractive index unit (deg/RIU). Using the FWHM of the slant configuration from step_01, compute the figure of merit (FOM) according to the paper’s definition, where FOM = m(eV/RIU) / FWHM(eV), with m being the sensitivity expressed in energy units. Write the results to step_03_results_summary.json.
- Output file: `/app/outputs/step_03_results_summary.json`
- Format: json
- Contract: keys: slant_sensitivity_deg_per_RIU (float), unslant_sensitivity_deg_per_RIU (float), slant_FWHM_deg (float), slant_FOM (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_resonance_angles.csv`
- `/app/outputs/step_02_sensitivity_data.csv`
- `/app/outputs/step_03_results_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_resonance_angles.csv
- path: `/app/outputs/step_01_resonance_angles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Resonance angle and full‑width at half‑maximum for the unslant 90° (Λ=400 nm), slant 60° (Λ=400 nm), and period 500 nm (unslant 90°) grating configurations. Compared to the paper’s reported values within tight tolerances.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `resonance_angle_deg`, `FWHM_deg`
  - `units`:
    - `resonance_angle_deg`: degrees
    - `FWHM_deg`: degrees

### step_02_sensitivity_data.csv
- path: `/app/outputs/step_02_sensitivity_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Resonance angle measured at each analyte refractive index (1.00–1.05, step 0.01) for the slant 60° and unslant 90° gratings. The checker recomputes the sensitivity (slope) from this data and compares to the expected linear relation.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `refractive_index`, `resonance_angle_deg`
  - `units`:
    - `refractive_index`: dimensionless
    - `resonance_angle_deg`: degrees

### step_03_results_summary.json
- path: `/app/outputs/step_03_results_summary.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Agent‑computed sensitivities (deg/RIU) for both configurations, the FWHM of the slant configuration, and the figure of merit FOM. The checker recomputes FOM from the slant sensitivity and FWHM to confirm internal consistency, then compares slant_FOM to the paper’s value.
- schema:
  - `type`: object
  - `required`:
    - `slant_sensitivity_deg_per_RIU`: float
    - `unslant_sensitivity_deg_per_RIU`: float
    - `slant_FWHM_deg`: float
    - `slant_FOM`: float
  - `units`:
    - `slant_sensitivity_deg_per_RIU`: deg/RIU
    - `unslant_sensitivity_deg_per_RIU`: deg/RIU
    - `slant_FWHM_deg`: degrees
    - `slant_FOM`: dimensionless

Notes: All outputs derive from RCWA simulations using publicly specified grating parameters and the Drude model for silver. The checker verifies internal consistency (slope recomputation, FOM recomputation) and compares key numerical results to the paper’s reported numbers within tolerances that absorb implementation‑dependent spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_resonance_angles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "resonance_angle_deg",
          "FWHM_deg"
        ],
        "units": {
          "resonance_angle_deg": "degrees",
          "FWHM_deg": "degrees"
        }
      },
      "description": "Resonance angle and full‑width at half‑maximum for the unslant 90° (Λ=400 nm), slant 60° (Λ=400 nm), and period 500 nm (unslant 90°) grating configurations. Compared to the paper’s reported values within tight tolerances."
    },
    {
      "file": "step_02_sensitivity_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "refractive_index",
          "resonance_angle_deg"
        ],
        "units": {
          "refractive_index": "dimensionless",
          "resonance_angle_deg": "degrees"
        }
      },
      "description": "Resonance angle measured at each analyte refractive index (1.00–1.05, step 0.01) for the slant 60° and unslant 90° gratings. The checker recomputes the sensitivity (slope) from this data and compares to the expected linear relation."
    },
    {
      "file": "step_03_results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "slant_sensitivity_deg_per_RIU": "float",
          "unslant_sensitivity_deg_per_RIU": "float",
          "slant_FWHM_deg": "float",
          "slant_FOM": "float"
        },
        "units": {
          "slant_sensitivity_deg_per_RIU": "deg/RIU",
          "unslant_sensitivity_deg_per_RIU": "deg/RIU",
          "slant_FWHM_deg": "degrees",
          "slant_FOM": "dimensionless"
        }
      },
      "description": "Agent‑computed sensitivities (deg/RIU) for both configurations, the FWHM of the slant configuration, and the figure of merit FOM. The checker recomputes FOM from the slant sensitivity and FWHM to confirm internal consistency, then compares slant_FOM to the paper’s value."
    }
  ],
  "notes": "All outputs derive from RCWA simulations using publicly specified grating parameters and the Drude model for silver. The checker verifies internal consistency (slope recomputation, FOM recomputation) and compares key numerical results to the paper’s reported numbers within tolerances that absorb implementation‑dependent spread."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage’s output artifact.
- For Step 1, the verifier compares your extracted resonance angles and FWHMs against reference values (hidden gold) with appropriate tolerances.
- For Step 2, it checks the linearity of the resonance angle vs. refractive index data.
- For Step 3, it recomputes the sensitivity from your Step 2 data (linear regression) and then computes the FOM from the slant sensitivity and FWHM, comparing the result to a reference value.
The final reward is a weighted combination of the stage scores. Reporting a final number without the required intermediate artifacts will not earn full credit; the verifier requires the computed data in the specified output files. The exact reference values, tolerances, and weights are hidden.
