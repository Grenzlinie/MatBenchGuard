# Reflectance and Efficiency of a One-Dimensional Rectangular Diffraction Grating

## Problem background
UV-VIS spectrometry is widely used for quality analysis of nucleic acids and other components in vaccine manufacturing, requiring high-performance diffraction gratings. The grating is a key optical element that separates light into its constituent wavelengths. The reflectance and diffraction efficiency of a grating depend on the material and its geometric parameters (period, thickness). This task investigates four semiconductor materials — Si, GaN, InGaAs, and InP — as potential grating materials for a one-dimensional rectangular grating. The goal is to determine which material provides the highest reflectance across a range of incident angles and to compute the grating's absolute diffraction efficiency at the optimal geometry.

## Approach
The simulation uses rigorous coupled-wave analysis (RCWA), a method for solving Maxwell's equations in periodic structures by expanding fields into Floquet modes. A one-dimensional rectangular grating unit cell with period 340 nm, thickness 400 nm, and slit width 450 nm is modeled. For each of the four materials, the complex refractive index at the target wavelength (445 nm) is used as input. The 0th-order reflectance is computed for angles of incidence from 1° to 89° in 1° steps. The angle that yields the maximum reflectance for the best-reflecting material is then identified, and at that angle the absolute diffraction efficiency into the -1st order is evaluated. The procedure uses periodic boundary conditions on the unit cell. You must implement the RCWA solution yourself using an open-source solver.

## Reproduction target
Compute the reflectance vs. angle of incidence for all four materials (Si, GaN, InGaAs, InP) at the fixed grating geometry, and output the results in a CSV file. From these results, determine which material achieves the highest reflectance across the angle sweep, and note the angle at which its reflectance is maximized. Then, at that optimal angle, compute the absolute diffraction efficiency into the -1st order (as a percentage) and write it to a text file.

## Assets

- Open-source RCWA solver (pyRCWA, S4, or grrcwa): pyrcwa

## Workflow steps

### Step 1: Reflectance vs angle of incidence simulation
- Role: scored
- Action: Simulate a one-dimensional rectangular grating with period 340 nm, thickness 400 nm, slit width 450 nm for four semiconductor materials (Si, GaN, InGaAs, InP) using their complex refractive indices (Si: 3.9766+0.030209i, GaN: 2.3991, InGaAs: 3.9123+0.61589i, InP: 3.53635+0.3075118i). Sweep the angle of incidence from 1° to 89° in 1° steps and compute the 0th-order reflectance. Save the results to a CSV file.
- Output file: `/app/outputs/step_01_reflectance_vs_angle.csv`
- Format: csv
- Contract: Columns: angle (integer degrees), Si (float reflectance), GaN (float), InGaAs (float), InP (float). One row per integer angle from 1 to 89.
- Scoring: scored by hidden verifier

### Step 2: Grating diffraction efficiency at optimum angle
- Role: scored
- Action: Using the angle that maximizes InGaAs reflectance from the previous step, compute the absolute diffraction efficiency into the -1st order for the same grating geometry and material refractive indices (period 340 nm, thickness 400 nm, slit width 450 nm). Output the efficiency as a percentage (0-100) in a text file.
- Output file: `/app/outputs/step_02_efficiency.txt`
- Format: txt
- Contract: A single line containing a floating-point number (percentage, between 0 and 100).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_reflectance_vs_angle.csv`
- `/app/outputs/step_02_efficiency.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_reflectance_vs_angle.csv
- path: `/app/outputs/step_01_reflectance_vs_angle.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Reflectance vs. angle for four materials. The checker verifies the physically expected ordering of reflectance values among materials.
- schema:
  - `type`: table
  - `required_columns`: `angle`, `Si`, `GaN`, `InGaAs`, `InP`
  - `units`:
    - `angle`: degrees
    - `Si`: reflectance (0-1)
    - `GaN`: reflectance (0-1)
    - `InGaAs`: reflectance (0-1)
    - `InP`: reflectance (0-1)

### step_02_efficiency.txt
- path: `/app/outputs/step_02_efficiency.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Absolute diffraction efficiency into the -1st order for InGaAs grating at the optimal angle, compared to a hidden reference value.
- schema:
  - `type`: text
  - `unit`: percentage

Notes: The solver should use sufficient Fourier orders and periodic boundary conditions. The optimum angle is expected around 47° but must be determined from step_01 results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_reflectance_vs_angle.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle",
          "Si",
          "GaN",
          "InGaAs",
          "InP"
        ],
        "units": {
          "angle": "degrees",
          "Si": "reflectance (0-1)",
          "GaN": "reflectance (0-1)",
          "InGaAs": "reflectance (0-1)",
          "InP": "reflectance (0-1)"
        }
      },
      "description": "Reflectance vs. angle for four materials. The checker verifies the physically expected ordering of reflectance values among materials."
    },
    {
      "file": "step_02_efficiency.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "unit": "percentage"
      },
      "description": "Absolute diffraction efficiency into the -1st order for InGaAs grating at the optimal angle, compared to a hidden reference value."
    }
  ],
  "notes": "The solver should use sufficient Fourier orders and periodic boundary conditions. The optimum angle is expected around 47° but must be determined from step_01 results."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that reads your two output files. For the reflectance CSV, the verifier checks that the reflectance values at each angle satisfy a specific ordering among the four materials (the ordering is not disclosed here, but it is the physically expected one based on the material properties). For the efficiency text file, the verifier compares your reported value to a hidden reference value with an allowed tolerance. Each output file is weighted equally (50%). You must actually simulate the grating using RCWA; fabricating numbers will likely fail the verification.
