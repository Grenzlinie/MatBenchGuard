# Inverse Design of TE Mode Converter via Objective-First Optimization

## Problem background
Designing compact, high-performance nanophotonic components (such as mode converters, splitters, and couplers) typically requires expert hand-tuning of a small number of geometric parameters. This work introduces a computational inverse-design method that automatically produces three-dimensional, manufacturable linear photonic devices directly from a user’s performance specification. The method formulates the design as a constrained optimization that minimizes the physics residual of Maxwell’s equations while enforcing hard field-overlap constraints that encode the desired device functionality. Solving the optimization with an alternating direction method of multipliers (ADMM) together with a finite-difference frequency-domain (FDFD) Maxwell solver yields an optimized continuous permittivity distribution, which is then converted to a binary silicon / silica structure. The reproduction focuses on a TE mode converter as a canonical demonstration: the device must efficiently transfer optical power from the fundamental TE waveguide mode into the second-order TE mode while suppressing the transmitted fundamental mode to a very low level.

## Approach
The strategy is an objective-first formulation: instead of requiring exact satisfaction of Maxwell’s equations, the physics acts as a term to be minimized, and the user’s performance specification (field overlap integrals at the device ports) becomes a set of hard constraints. For the TE mode converter the design region is a 250 nm thick silicon slab (ε_Si = 12.25) completely surrounded by silica (ε_SiO₂ = 2.25). The input excitation is the fundamental TE-polarized waveguide mode at 1550 nm wavelength. The design goal is to couple the majority of the input power into the second-order TE mode while allowing at most a tiny fraction to remain in the transmitted fundamental mode. These requirements are expressed as constraints on the overlap amplitudes between the computed electric field and precomputed mode profiles. The constrained optimization is solved with the alternating direction method of multipliers (ADMM), which iteratively updates the electric field distributions and the permittivity distribution using a 3D finite-difference frequency-domain (FDFD) Maxwell solver. After convergence, the continuous permittivity map is turned into a binary silicon–silica layout by extracting boundaries (level-set or thresholding) and refining them with a steepest-descent procedure. Finally, a full-wave verification simulation is performed on the binary structure to compute the actual conversion efficiency and rejection power. The reproduction does not require the original home‑built solver; an open‑source Maxwell solver (e.g., Meep) can be used as the FDFD engine. All geometric, material, and wavelength parameters are fully specified below; no external datasets are needed.

## Reproduction target
Implement the objective-first inverse-design method for a TE mode converter. Define the design region as a 250 nm thick silicon slab with permittivity ε_Si = 12.25, surrounded by silica (ε_SiO₂ = 2.25). Compute the fundamental and second-order TE waveguide mode profiles at 1550 nm. Encode the design specification: at least 90 % of the input power from the fundamental TE mode must be transferred into the second-order TE mode, and no more than 1 % of the input power may remain in the transmitted fundamental mode. Set up the objective-first optimization problem and solve it using ADMM with a 3D FDFD Maxwell solver. Run the optimization to convergence. Convert the resulting continuous permittivity distribution to a binary silicon / silica structure using a boundary extraction and steepest-descent refinement. Finally, perform a full-wave verification simulation on the binary structure and write the results to `/app/outputs/final_results.json`. The file must be a JSON object with two keys: `conversion_efficiency` (the fraction of input power coupled into the second-order TE mode) and `rejection_power` (the fraction of input power remaining in the transmitted fundamental TE mode). The goal is to achieve a conversion efficiency as high as possible and a rejection power as low as possible.

## Assets

- Meep FDTD solver: https://github.com/NanoComp/meep
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Device Specification and Mode Calculation
- Role: process
- Action: Define the design region (250 nm thick silicon slab, ε_Si=12.25, ε_SiO2=2.25) and compute the electric field profiles of the fundamental TE mode and the second-order TE mode at 1550 nm wavelength. Set up the objective-first optimization problem: for the fundamental TE input mode, define output overlap vectors c_{11} (second-order mode) and c_{12} (fundamental mode), impose field-overlap constraints 0.9 ≤ |c_{11}† x_1| ≤ 1.0 and 0.0 ≤ |c_{12}† x_1| ≤ 0.01, and define the source term b_1 corresponding to a fundamental TE mode excitation.
- Evidence: `/app/outputs/mode_profiles.txt`

### Step 2: ADMM Inverse Design Optimization
- Role: process
- Action: Implement the objective-first optimization (minimizing physics residual sum subject to hard field-overlap constraints) using an alternating direction method of multipliers (ADMM) algorithm with a 3D finite-difference frequency-domain (FDFD) Maxwell solver. Initialize the permittivity uniformly in the design region and iteratively update the electric fields x_i and permittivity z until convergence. Output the optimized continuous permittivity distribution.
- Evidence: `/app/outputs/optimized_permittivity.npy`

### Step 3: Boundary Extraction and Binary Conversion
- Role: process
- Action: Convert the continuously optimized permittivity map into a binary silicon/silica structure. Apply a level-set or thresholding method to extract boundaries and refine them with a steepest-descent procedure to ensure a manufacturable two-material layout.
- Evidence: `/app/outputs/binary_structure.png`

### Step 4: Final Performance Verification
- Role: scored (load-bearing)
- Action: Run a full-wave FDFD simulation on the final binary structure with the fundamental TE mode input excitation. Compute the squared magnitudes of the overlap integrals |c_{11}† x_1|^2 and |c_{12}† x_1|^2 and convert them to power fractions relative to the input power. Output the conversion efficiency (power fraction into the second-order TE mode) and the rejection power (power fraction into the transmitted fundamental TE mode).
- Output file: `/app/outputs/final_results.json`
- Format: json
- Contract: {"type": "object", "properties": {"conversion_efficiency": {"type": "number"}, "rejection_power": {"type": "number"}}, "required": ["conversion_efficiency", "rejection_power"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/final_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### final_results.json
- path: `/app/outputs/final_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Device performance: conversion efficiency (fraction of input power into the second-order TE mode) and rejection power (fraction remaining in the fundamental TE mode). Meeting or beating the hidden gold thresholds earns full credit.
- schema:
  - `type`: object
  - `properties`:
    - `conversion_efficiency`:
      - `type`: number
    - `rejection_power`:
      - `type`: number
  - `required`: `conversion_efficiency`, `rejection_power`

Notes: The hidden checker compares the agent's reported values to gold baseline efficiencies from the paper. The conversion efficiency uses a 'higher is better' criterion; rejection power uses 'lower is better'. Both are scored with threshold_or_better — achieving the gold value or better yields full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "final_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "conversion_efficiency": {
            "type": "number"
          },
          "rejection_power": {
            "type": "number"
          }
        },
        "required": [
          "conversion_efficiency",
          "rejection_power"
        ]
      },
      "description": "Device performance: conversion efficiency (fraction of input power into the second-order TE mode) and rejection power (fraction remaining in the fundamental TE mode). Meeting or beating the hidden gold thresholds earns full credit."
    }
  ],
  "notes": "The hidden checker compares the agent's reported values to gold baseline efficiencies from the paper. The conversion efficiency uses a 'higher is better' criterion; rejection power uses 'lower is better'. Both are scored with threshold_or_better — achieving the gold value or better yields full credit."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/final_results.json` and extracts the `conversion_efficiency` and `rejection_power` numbers. Each number is compared to a hidden reference value (derived from the original paper’s reported result for this specific device). Scoring uses a threshold‑or‑better policy: for conversion efficiency (higher is better) you earn full credit if your value equals or exceeds the hidden threshold, and partial credit decreases as the efficiency falls below it; for rejection power (lower is better) you earn full credit if your value is less than or equal to the hidden threshold, and partial credit decreases as it rises above it. Better‑than‑reference results never reduce your score. The intermediate process artifacts (`mode_profiles.txt`, `optimized_permittivity.npy`, `binary_structure.png`) are required by the pipeline but are not directly scored; the final numerical reward depends entirely on the performance numbers in `final_results.json`.
