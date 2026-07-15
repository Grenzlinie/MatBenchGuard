# Sinusoidal Grating UV Reflectance via RCWA

## Problem background
Certain unicellular microalgae (euglenoids) possess a pellicle — a patterned outer layer with periodic grooves — while other species have an essentially smooth (planar) surface. Because UV radiation penetrating natural waters can harm phytoplankton, it is of interest to understand whether the periodic surface structure might provide protection by reflecting more ultraviolet light than a smooth interface would. The electromagnetic diffraction problem involves a sinusoidal grating profile separating water (refractive index 1.33) from the cell interior (approximated as a homogeneous medium with index 1.5). The key quantity is the total normalized reflectance R, defined as the sum of all reflected diffraction efficiencies for TE and TM polarizations divided by the sum of the planar Fresnel reflectivities (which are equal at normal incidence). A value R > 1 means the corrugated interface reflects more than a planar interface; R ≤ 1 means it does not. This task computes R for several grating periods and depths across the UV range and determines whether the periodic profile yields enhanced UV reflectance relative to the planar reference.

## Approach
Model the pellicle as a one-dimensional sinusoidal grating: y = 0.5 h cos(2π x / d), where d is the period and h is the groove depth. The incident medium is water (n₁ = 1.33) and the substrate is the cell interior (n₂ = 1.5). The analysis is performed under normal incidence (incoming light perpendicular to the mean plane of the grating) for a series of ultraviolet wavelengths: 280, 300, 320, 340, 360, and 380 nm. For each combination of period, depth, and wavelength, use a rigorous coupled-wave analysis (RCWA) or equivalent Chandezon method to compute the diffraction efficiencies of all reflected orders for both TE (electric field parallel to grooves) and TM (magnetic field parallel to grooves) polarizations. Sum these efficiencies and normalize by the sum of the corresponding planar Fresnel coefficients (which are identical for TE and TM at normal incidence) to obtain the total normalized reflectance R. As a baseline, also compute R for a planar interface (h = 0), which by definition yields R = 1. The result is a table of R values for several biologically relevant periods (d = 0.256, 0.276, 0.315, 0.495 μm) with a fixed depth-to-period ratio h/d = 0.4, plus the planar reference.

## Reproduction target
Compute the total normalized reflectance R for the following cases:
- Planar reference: d = 0.256 μm, h = 0 μm.
- Corrugated gratings with h/d = 0.4 (i.e., h = 0.4 × d) for periods d = 0.256, 0.276, 0.315, and 0.495 μm.
All calculations are at normal incidence for the UV wavelengths 280, 300, 320, 340, 360, and 380 nm.
Write all results to uv_reflectance.csv (one row per combination, columns: d_um, h_um, wavelength_nm, R).
The primary measurable outcome is: for the three smaller periods (d = 0.256, 0.276, 0.315 μm), is R > 1 for every UV wavelength? For the planar reference and for d = 0.495 μm, is it not (R ≤ 1 for all checked wavelengths)? Answer this yes/no question; it will be evaluated against independent recomputation.

## Assets

- S4 (Stanford Stratified Structure Solver): https://web.stanford.edu/group/fan/S4/
- NumPy: numpy
- h5py: h5py

## Workflow steps

### Step 1: Parameter Setup
- Role: process
- Action: Define the grating geometries (periods d=[0.256,0.276,0.315,0.495] μm, depth-to-period ratio h/d=0.4, and planar reference h=0), refractive indices (n1=1.33, n2=1.5), normal incidence, and UV wavelengths (280,300,320,340,360,380 nm).
- Evidence: none

### Step 2: RCWA Simulation and Reflectance Calculation
- Role: scored (load-bearing)
- Action: For each combination of grating period d (0.256,0.276,0.315,0.495 μm), depth h (0 for planar reference, or h=0.4*d for other), and each wavelength (280,300,320,340,360,380 nm), run an RCWA solver to compute reflected diffraction efficiencies for TE and TM polarizations under normal incidence. Sum the efficiencies and normalize by the sum of planar Fresnel reflectivities to obtain total normalized reflectance R. Write a row per combination to uv_reflectance.csv with columns d_um, h_um, wavelength_nm, R.
- Output file: `/app/outputs/uv_reflectance.csv`
- Format: csv
- Contract: Columns: d_um (float), h_um (float), wavelength_nm (float), R (float). One row per combination. Required combinations: planar reference (d=0.256, h=0.0) and d=0.256,0.276,0.315,0.495 with h/d=0.4 (h=0.4*d). Each combination must have rows for wavelengths 280,300,320,340,360,380 nm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/uv_reflectance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### uv_reflectance.csv
- path: `/app/outputs/uv_reflectance.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total normalized reflectance R computed by RCWA for sinusoidal gratings with specified parameters. Reflectance values are compared to a checker-recomputed reference within tolerance; structural trend (R > 1 for small periods) is also assessed.
- schema:
  - `type`: table
  - `required_columns`: `d_um`, `h_um`, `wavelength_nm`, `R`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "uv_reflectance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "d_um",
          "h_um",
          "wavelength_nm",
          "R"
        ]
      },
      "description": "Total normalized reflectance R computed by RCWA for sinusoidal gratings with specified parameters. Reflectance values are compared to a checker-recomputed reference within tolerance; structural trend (R > 1 for small periods) is also assessed."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently compute the normalized reflectance using an RCWA solver with the identical parameters (period, depth, refractive indices, normal incidence, wavelengths). It will compare each R value in your uv_reflectance.csv to its own recomputed values and also check whether the structural trend (R > 1 for the three small periods across all UV wavelengths, and R ≤ 1 for the planar case and for d = 0.495 μm) holds in your submission. The final reward is a weighted combination of the proportion of individually correct values and the correctness of the trend, yielding a score between 0 and 1. Reporting the paper's numbers without genuine computation will not produce the full set of values the verifier expects.
