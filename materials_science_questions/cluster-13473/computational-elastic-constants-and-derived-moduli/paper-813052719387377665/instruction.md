# Calibration of Length-Scale Parameters and Size Effect Demonstration for Gold Microbeams

## Problem background
Microelectromechanical systems (MEMS) often rely on gold microbeams only a few micrometers thick. Classical continuum beam theory fails to predict their bending stiffness at these scales because it ignores extra strain energy contributed by strain gradients ("size effects"). Two higher-order continuum theories—Modified Strain Gradient Theory (MSGT) and Modified Couple Stress Theory (MCST)—extend classical elasticity by introducing internal length-scale parameters that capture these gradient effects. These length-scale parameters are material constants that must be determined by comparing simulations to experiments. This task calibrates the length-scale parameters of gold microbeams against published experimental deflection data and then uses them to quantify the extent to which classical theory deviates from higher-order predictions for beams of different thicknesses.

## Approach
The approach follows the Euler–Bernoulli beam formulation with higher-order internal energy contributions. In addition to the usual Cauchy stress term, the energy includes contributions from the dilatation gradient, the deviatoric stretch gradient, and the rotation gradient, each tied to a length-scale parameter (l0, l1, l2 for MSGT; l2 only for MCST). A finite-element code is implemented to assemble and solve the static deflection of a beam given its geometry, loading, and length-scale parameters.

The unknown length-scale parameters for gold are calibrated with respect to the experimental load-deflection data reported by Espinosa et al. (2003) for freestanding gold thin-film beams. For MSGT the three length scales are assumed equal (l0 = l1 = l2) and a parameter sweep is performed for l0; for MCST only l2 is swept. At each candidate value the midpoint deflection of the experimental beam is simulated and the L2-norm error between computed and measured deflections is evaluated at an elastic modulus of 80 GPa. The value that minimizes the error is taken as the calibrated length scale.

With the calibrated parameters, the same finite-element solver is used to simulate a double-cantilevered gold microbeam under a central point load across a range of thicknesses (1–50 µm). For each thickness the midpoint deflection is computed using MSGT, MCST, and classical Euler–Bernoulli theory, producing the deflection ratio w_higher_order / w_classical.

## Reproduction target
Produce two scored artifacts:

1. **Calibrated length-scale parameters:** a JSON file (`length_scale_params.json`) containing the best-fit parameters for gold at an elastic modulus of 80 GPa. The file must contain keys `l0_MSGT_μm` (the common length scale for MSGT, with l0 = l1 = l2) and `l2_MCST_μm` (the length scale for MCST), both expressed in micrometers.

2. **Size‑effect deflection ratio table:** a CSV file (`deflection_ratios.csv`) with columns `thickness_µm`, `ratio_MSGT`, and `ratio_MCST`. Each row corresponds to a beam thickness in the range 1–50 µm (at least ten points, spanning the interval). The beam has a double-cantilevered boundary condition, an aspect ratio thickness:width:length = 1:5:20, and a point load applied at midpoint. For each thickness the ratio is the higher-order midpoint deflection (MSGT or MCST) divided by the classical Euler–Bernoulli deflection.

## Assets

- Espinosa et al. 2003 gold microbeam experimental data: 10.1016/S0022-5096(02)00062-5
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare experimental dataset for gold microbeams
- Role: process
- Action: Extract gold microbeam experimental data (beam geometry, boundary conditions, applied point load, measured midpoint deflection) for freestanding thin films from the published article Espinosa et al. (J. Mech. Phys. Solids 51, 47–72, 2003). The data serve as calibration targets.
- Evidence: none

### Step 2: Finite-element implementation of MSGT and MCST for Euler–Bernoulli beams
- Role: process
- Action: Implement a finite-element solver for static deflection of Euler–Bernoulli beams. The implementation must include the Modified Strain Gradient Theory (MSGT) formulation with three length-scale parameters (l0, l1, l2) and the Modified Couple Stress Theory (MCST) reduction (l0=l1=0, only l2). Use the variational internal energy expression that includes Cauchy stress, dilatation gradient, deviatoric stretch gradient, and rotation gradient contributions, together with the constitutive relations linking higher-order stress metrics to length scales (p = 2μ l0^2 ∇tr(ε), τ^S(1) = 2μ l1^2 η^S(1), m^S = 2μ l2^2 δχ^S). The code should assemble and solve the linear system for given beam geometry, load, and length-scale parameters to compute midpoint deflection.
- Evidence: none

### Step 3: Calibrate length-scale parameters for gold
- Role: scored (load-bearing)
- Action: Using the experimental data and the FE codes, calibrate the length-scale parameters for gold microbeams under MSGT and MCST at an elastic modulus E = 80 GPa. For MSGT, set l0 = l1 = l2 and perform a parameter sweep for l0 with a step size ≤ 0.05 µm; for MCST, set l0 = l1 = 0 and sweep l2. At each trial, compute the L2-norm error between computed and measured deflections. Identify the length-scale values that minimize the error. Save the best-fit parameters as a JSON file.
- Output file: `/app/outputs/length_scale_params.json`
- Format: json
- Contract: { "l0_MSGT_μm": float, "l2_MCST_μm": float }
- Scoring: scored by hidden verifier

### Step 4: Simulate deflection ratios and quantify size effects
- Role: scored
- Action: Using the calibrated length-scale parameters from the previous step, simulate a double-cantilevered gold microbeam with an aspect ratio thickness:width:length = 1:5:20 under a point load applied at midpoint. For a set of beam thicknesses covering the range 1–50 µm (at least 10 points, including values around 30 µm), compute the midpoint deflection using MSGT, MCST, and classical Euler–Bernoulli beam theory. Calculate the deflection ratio w_higher_order / w_classical for each theory. Save the results as a CSV file with columns thickness_µm, ratio_MSGT, ratio_MCST.
- Output file: `/app/outputs/deflection_ratios.csv`
- Format: csv
- Contract: Columns: thickness_μm, ratio_MSGT, ratio_MCST. One row per thickness value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/length_scale_params.json`
- `/app/outputs/deflection_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### length_scale_params.json
- path: `/app/outputs/length_scale_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Calibrated length-scale parameters for gold microbeams at E = 80 GPa. The hidden checker verifies these values against paper-reported reference values within a narrow tolerance.
- schema:
  - `type`: object
  - `required`:
    - `l0_MSGT_μm`: float
    - `l2_MCST_μm`: float
  - `units`:
    - `l0_MSGT_μm`: μm
    - `l2_MCST_μm`: μm

### deflection_ratios.csv
- path: `/app/outputs/deflection_ratios.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Deflection ratio table for size effect demonstration. The hidden checker performs a structural audit: it confirms that the ratios decrease monotonically with decreasing thickness, that they never exceed 1.0, and that at two reference thicknesses the error exceeds the thresholds claimed in the paper.
- schema:
  - `type`: table
  - `required_columns`: `thickness_µm`, `ratio_MSGT`, `ratio_MCST`
  - `units`:
    - `thickness_µm`: μm
    - `ratio_MSGT`: dimensionless
    - `ratio_MCST`: dimensionless

Notes: The experimental data must be obtained from the cited literature. The FE codes must be implemented from scratch; the parameter calibration requires a sweep that may be computationally intensive but is fully specified. The hidden checker audits structural trends in the deflection ratios, including threshold crossings consistent with the paper's claims.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "length_scale_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "l0_MSGT_μm": "float",
          "l2_MCST_μm": "float"
        },
        "units": {
          "l0_MSGT_μm": "μm",
          "l2_MCST_μm": "μm"
        }
      },
      "description": "Calibrated length-scale parameters for gold microbeams at E = 80 GPa. The hidden checker verifies these values against paper-reported reference values within a narrow tolerance."
    },
    {
      "file": "deflection_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_µm",
          "ratio_MSGT",
          "ratio_MCST"
        ],
        "units": {
          "thickness_µm": "μm",
          "ratio_MSGT": "dimensionless",
          "ratio_MCST": "dimensionless"
        }
      },
      "description": "Deflection ratio table for size effect demonstration. The hidden checker performs a structural audit: it confirms that the ratios decrease monotonically with decreasing thickness, that they never exceed 1.0, and that at two reference thicknesses the error exceeds the thresholds claimed in the paper."
    }
  ],
  "notes": "The experimental data must be obtained from the cited literature. The FE codes must be implemented from scratch; the parameter calibration requires a sweep that may be computationally intensive but is fully specified. The hidden checker audits structural trends in the deflection ratios, including threshold crossings consistent with the paper's claims."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently examines each artifact. The verifier does not re-run your finite-element code; it compares the submitted artifacts to the expected results.

- For `length_scale_params.json`, the verifier checks that the file contains the required keys and that the submitted length-scale values match the reference calibration (obtained by the same procedure) within a tolerance that reflects the precision of the parameter sweep.
- For `deflection_ratios.csv`, the verifier performs a structural audit: it confirms that the deflection ratios decrease monotonically as the beam thickness decreases, and that at the thickness where classical theory becomes inaccurate the ratios indicate a size effect consistent with the paper’s claims.

Simply reporting numbers without performing the finite-element implementation and calibration sweep will not earn credit.
