# Refractive Index Error from Fiber Diameter Variations in Tilted Fiber Bragg Gratings

## Problem background
Tilted fiber Bragg gratings (TFBGs) couple light from the fiber core into cladding modes, whose resonance wavelengths shift with the refractive index (RI) of the surrounding medium. This enables simultaneous measurement of RI and temperature of liquids. The resonance wavelengths depend sensitively on the geometry of the optical fiber, especially the core and cladding diameters. This task quantifies, through numerical simulation, how small variations in these diameters affect the refractive index inferred from a particular high-order cladding mode (the Y<sub>1,70</sub> mode) under identical measurement conditions. The goal is to determine the absolute error in the inferred external refractive index caused by a reduction in cladding diameter and by a reduction in core diameter, thereby evaluating which dimensional tolerance is more critical for measurement precision.

## Approach
The refractive index profile of a step-index optical fiber is modeled as a three-layer cylindrical structure: core, cladding, and external medium. A multilayer method is used to solve Maxwell's equations for the fiber's guided and cladding modes while avoiding numerical overflow for the large cladding-to-wavelength ratio. The multilayer approach expresses the tangential field components in each region and enforces continuity at the boundaries, leading to a characteristic equation whose root gives the effective refractive index of a mode.

For predetermined fiber parameters (core index, cladding index, core and cladding diameters, and a reference wavelength of 1550 nm for material indices), the effective index of the fundamental core mode is computed first. From the known core-mode resonance wavelength (1572.12 nm) and the TFBG tilt angle (7.3°), the grating period is derived using the phase-matching condition for core-mode backward coupling. Then, the effective index of the Y<sub>1,70</sub> cladding mode is computed as a function of the external refractive index (n3) over a range from 1.0 to 1.38. This computation is repeated for several fiber geometries: the nominal diameter pair (cladding 125 µm, core 9.6 µm), a cladding diameter of 123 µm (core unchanged), a cladding diameter of 127 µm (core unchanged), and a core diameter of 7.8 µm (cladding unchanged).

For each geometry, the relative wavelength shift of the Y<sub>1,70</sub> mode is calculated from the effective indices using the cladding-resonance condition. A reference shift value is identified from the nominal geometry at a specified external index. For the varied geometries, the external index that yields the same reference shift is determined by interpolation. The absolute differences between these interpolated indices and the nominal reference index constitute the refractive index errors due to cladding and core diameter variations.

## Reproduction target
Implement a multilayer mode solver for a cylindrical step-index fiber. Use the provided fiber parameters (core index n1 = 1.4491, cladding index n2 = 1.4443 at 1550 nm, core diameter 2a1 = 9.6 µm, cladding diameter 2a2 = 125 µm, TFBG tilt angle θ = 7.3°). Determine the grating period Λ such that the core-mode resonance occurs at 1572.12 nm. For the Y<sub>1,70</sub> cladding mode, compute the effective index as a function of external refractive index n3 for four geometries: (1) core 9.6 µm, cladding 125 µm; (2) core 9.6 µm, cladding 123 µm; (3) core 9.6 µm, cladding 127 µm; (4) core 7.8 µm, cladding 125 µm. From the nominal curve (case 1), read off the relative wavelength shift at n3 = 1.3727. For case 2 (123 µm cladding), find the external index that produces this same shift; the absolute difference from 1.3727 is delta_RI_cladding. For case 4 (7.8 µm core), find the external index that produces the reference shift; the absolute difference is delta_RI_core. Write a JSON file `results.json` containing the two values: `{"delta_RI_cladding": <float>, "delta_RI_core": <float>}`. Both are dimensionless refractive index differences.

## Assets

- Supplementary equations for the multilayer method (Data 1): http://stacks.iop.org/JJAP/55/068003/mmedia

## Workflow steps

### Step 1: Multilayer mode solver implementation
- Role: process
- Action: Implement the multilayer method for a cylindrical step-index optical fiber based on the equations provided in the supplementary data (Data 1). Using the fiber parameters (core index n1=1.4491, cladding index n2=1.4443, core diameter 2a1=9.6 µm, cladding diameter 2a2=125 µm, reference wavelength 1550 nm for material indices), compute the effective refractive index of the core mode (neff_core). Determine the grating period Λ from the core resonance condition: λ_core = 2 neff_core Λ / cosθ, with λ_core = 1572.12 nm and tilt angle θ = 7.3°. Then, for the Y_{1,70} cladding mode, compute its effective refractive index (neff_cladding) as a function of the external refractive index n3 (varying from 1.0 to 1.38) for the following fiber geometries: nominal (core 9.6 µm, cladding 125 µm), cladding diameter 123 µm (core 9.6 µm), cladding diameter 127 µm (core 9.6 µm), and core diameter 7.8 µm (cladding 125 µm). Store the computed neff_cladding values and the corresponding n3 for each geometry in a CSV file.
- Evidence: `/app/outputs/neff_cladding_data.csv`

### Step 2: Compute refractive index errors
- Role: scored (load-bearing)
- Action: Using the grating period Λ determined in the previous step and the computed neff_cladding values, calculate the relative wavelength shift Δλ of the Y_{1,70} mode as a function of n3 for each geometry using the cladding resonance condition: Δλ = (neff_core + neff_cladding)Λ/cosθ - λ_cladding_ref (or directly the shift relative to the value at n3=1). From the nominal cladding 125 µm curve, identify the Δλ value at external refractive index n3=1.3727 (reference shift). For the 123 µm cladding geometry, determine the external refractive index n3_123 that produces the same Δλ. Compute delta_RI_cladding = |n3_123 - 1.3727|. For the 7.8 µm core geometry (with cladding 125 µm), determine n3_7.8 that produces the reference shift, and compute delta_RI_core = |n3_7.8 - 1.3727|. Output the two values in a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"delta_RI_cladding": <float>, "delta_RI_core": <float>} (both in refractive index units, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The absolute differences in inferred refractive index due to cladding diameter variation (125 µm to 123 µm) and core diameter variation (9.6 µm to 7.8 µm). The checker will compare these values against expected results.
- schema:
  - `type`: object
  - `required`: `delta_RI_cladding`, `delta_RI_core`
  - `units`:
    - `delta_RI_cladding`: dimensionless (refractive index difference)
    - `delta_RI_core`: dimensionless (refractive index difference)

Notes: The hidden checker reads the JSON file and evaluates both delta values: one is compared to a hidden reference with a tolerance, and the other is verified to be below a hidden maximum. Both values must be plausible given the numerical reconstruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "delta_RI_cladding",
          "delta_RI_core"
        ],
        "units": {
          "delta_RI_cladding": "dimensionless (refractive index difference)",
          "delta_RI_core": "dimensionless (refractive index difference)"
        }
      },
      "description": "The absolute differences in inferred refractive index due to cladding diameter variation (125 µm to 123 µm) and core diameter variation (9.6 µm to 7.8 µm). The checker will compare these values against expected results."
    }
  ],
  "notes": "The hidden checker reads the JSON file and evaluates both delta values: one is compared to a hidden reference with a tolerance, and the other is verified to be below a hidden maximum. Both values must be plausible given the numerical reconstruction."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/results.json`. The verifier checks the two reported values against reference values derived from the original study. The check uses an absolute tolerance for the cladding-diameter-induced error (delta_RI_cladding) and a maximum allowed upper bound for the core-diameter-induced error (delta_RI_core). If both values meet their respective criteria, you receive the full reward. If only one of the two conditions is satisfied, you receive a partial reward. The verifier does not inspect your intermediate files; only the contents of `results.json` determine your score. The evaluation is fully automated and deterministic.
