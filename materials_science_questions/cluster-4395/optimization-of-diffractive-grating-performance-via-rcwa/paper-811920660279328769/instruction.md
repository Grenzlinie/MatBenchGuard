# Evanescent Near-Field Contrast Simulation for Subwavelength Chrome Gratings

## Problem background
Optical contact lithography in the evanescent near field (ENFOL) promises sub-wavelength resolution. This task computationally investigates, via full-vector electromagnetic simulations, the contrast and intensity of TM-polarized light transmitted through subwavelength chrome gratings. The goal is to assess whether periods as small as λ/20 (20 nm) can provide sufficient image contrast for lithography. The original investigation used the multiple multipole method (MMP), but any full-vector electromagnetic solver can reproduce the results.

## Approach
The approach is to simulate the electromagnetic wave propagation through a periodic chrome grating using a full-vector solver (e.g., finite-difference time-domain or rigorous coupled-wave analysis). A 2D unit cell with periodic boundary conditions in the grating direction and absorbing boundaries in the propagation direction represents the infinite grating. TM-polarized plane-wave illumination at 436 nm is normally incident. Chrome is modeled with a complex permittivity εr = -13.24 + 14.616i. The solver computes the normalized intensity distribution behind the mask. From the intensity profiles, the contrast V = (Ia - Is) / (Ia + Is) is derived at each depth, where Ia is the intensity at the aperture centre and Is is the intensity at the shadow centre. The half-contrast depth is the depth at which V first drops below 0.5. The procedure is repeated for grating periods of 200, 140, 80, and 20 nm.

## Reproduction target
The objective is to compute two artifacts:
1) A table (contrast_vs_depth_20nm.csv) containing the contrast V as a function of depth for the 20 nm period grating, from depth 0 to at least 100 nm with a step no larger than 2 nm.
2) A table (half_contrast_depths.csv) listing the grating period and the corresponding half-contrast depth (depth where V first drops below 0.5) for the periods 200, 140, 80, and 20 nm.

## Assets

- Meep (open-source FDTD solver): https://github.com/NanoComp/meep
- S4 (open-source RCWA solver): https://github.com/victorliu/S4
- Chrome optical constants at 436 nm (epsilon_r = -13.24 + 14.616i)

## Workflow steps

### Step 1: Simulate electromagnetic near-fields for all grating periods
- Role: process
- Action: Construct a 2D simulation of chrome gratings (thickness 40 nm, line:space ratio 1:1) with periods 200, 140, 80, and 20 nm, using TM-polarized plane-wave illumination at 436 nm, chrome permittivity εr = -13.24 + 14.616i. Use periodic boundary conditions in the grating direction and absorbing boundaries (PML) in the propagation direction. Run the simulation for each period to obtain the normalized intensity (|E|^2 or Poynting vector) in a region behind the mask from contact to at least 100 nm depth, with spatial resolution sufficient to resolve the aperture and shadow regions. Save the computed field data for post-processing.
- Evidence: `/app/outputs/simulation_data_dir`

### Step 2: Compute contrast vs depth for 20 nm period grating
- Role: scored
- Action: Using the simulated intensity data for the 20 nm period grating, compute at each depth the intensity at the center of the aperture (Ia) and center of the shadow (Is) as defined in the paper, then compute contrast V = (Ia-Is)/(Ia+Is). Save the depth and contrast values.
- Output file: `/app/outputs/contrast_vs_depth_20nm.csv`
- Format: csv
- Contract: columns: depth_nm (float), contrast (float). Rows from depth 0 to at least 100 nm, step <= 2 nm.
- Scoring: scored by hidden verifier

### Step 3: Compute half-contrast depths for all grating periods
- Role: scored (load-bearing)
- Action: From the simulated intensity data for each period (200, 140, 80, 20 nm), compute the contrast V as a function of depth. Determine for each period the depth where V first drops below 0.5 (the half-contrast depth), using interpolation if needed. Output the period and half-contrast depth.
- Output file: `/app/outputs/half_contrast_depths.csv`
- Format: csv
- Contract: columns: period_nm (int), half_contrast_depth_nm (float). One row per period (200, 140, 80, 20).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/contrast_vs_depth_20nm.csv`
- `/app/outputs/half_contrast_depths.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### contrast_vs_depth_20nm.csv
- path: `/app/outputs/contrast_vs_depth_20nm.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Contrast V = (Ia-Is)/(Ia+Is) as a function of depth behind the grating for the 20 nm period case. The checker will compare the reported contrast at selected depths and verify that contrast at the exit plane exceeds a threshold.
- schema:
  - `type`: table
  - `required_columns`: `depth_nm`, `contrast`
  - `units`:
    - `depth_nm`: nm
    - `contrast`: dimensionless

### half_contrast_depths.csv
- path: `/app/outputs/half_contrast_depths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Depth where contrast first drops below 0.5 for each grating period. The checker will compare these depths to hidden reference values and verify the linear relationship between period and half-contrast depth.
- schema:
  - `type`: table
  - `required_columns`: `period_nm`, `half_contrast_depth_nm`
  - `units`:
    - `period_nm`: nm
    - `half_contrast_depth_nm`: nm

Notes: The scored artifacts are derived entirely from the agent's own simulation data. No paper-specific constants beyond the public chrome permittivity and geometry are required. The checker uses hidden reference values extracted from the paper to evaluate accuracy with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "contrast_vs_depth_20nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "depth_nm",
          "contrast"
        ],
        "units": {
          "depth_nm": "nm",
          "contrast": "dimensionless"
        }
      },
      "description": "Contrast V = (Ia-Is)/(Ia+Is) as a function of depth behind the grating for the 20 nm period case. The checker will compare the reported contrast at selected depths and verify that contrast at the exit plane exceeds a threshold."
    },
    {
      "file": "half_contrast_depths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "period_nm",
          "half_contrast_depth_nm"
        ],
        "units": {
          "period_nm": "nm",
          "half_contrast_depth_nm": "nm"
        }
      },
      "description": "Depth where contrast first drops below 0.5 for each grating period. The checker will compare these depths to hidden reference values and verify the linear relationship between period and half-contrast depth."
    }
  ],
  "notes": "The scored artifacts are derived entirely from the agent's own simulation data. No paper-specific constants beyond the public chrome permittivity and geometry are required. The checker uses hidden reference values extracted from the paper to evaluate accuracy with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently checks each output file. For `contrast_vs_depth_20nm.csv`, it reads the reported contrast at selected depths and verifies that the contrast at the exit plane (depth 0) meets a required criterion. For `half_contrast_depths.csv`, it compares the submitted half‑contrast depths for each period to hidden reference values and also checks that the four data points follow a strong linear relationship. The verifier uses tolerances appropriate for numerical simulations with different solvers. The final reward is a weighted combination of these checks.
