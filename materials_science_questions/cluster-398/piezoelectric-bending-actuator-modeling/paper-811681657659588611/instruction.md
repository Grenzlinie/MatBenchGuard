# Piezoelectric Fiber Composite Beam Tip Deflection by Asymptotic Beam Analysis

## Problem background
Piezoelectric fiber composite beams are slender structures that can be actuated via embedded piezoelectric fibers for bending control. Accurately predicting the tip deflection under electrical actuation is challenging because of cross-sectional warping and material inhomogeneity. The asymptotic beam analysis method tackles this by separating a three-dimensional piezoelectric problem into a two-dimensional cross-sectional analysis and a one-dimensional beam model. The goal of this reproduction task is to compute the static tip deflections of a specific composite cantilever beam at three applied voltages, thereby verifying the method's predictive capability.

## Approach
The method is based on a formal asymptotic expansion of the three-dimensional linear piezoelectricity equations. Exploiting the beam's slenderness decomposes the problem into a microscopic cross-sectional warping problem and a macroscopic one-dimensional beam problem. In the first stage, a two-dimensional finite element model of the cross-section is built using isoparametric shape functions. The cross-sectional stiffness matrices and right-hand-side matrices are assembled from the material properties and geometry. Rigid-body orthogonality constraints are imposed via Lagrange multipliers, and prescribed electric potentials are applied on the fiber boundaries. Solving this system yields the mechanical and electric warping functions driven by macroscopic strain measures and prescribed potentials. These warping functions are then used to obtain the homogenized 1D beam constitutive coefficients (stiffness and electric coupling). In the second stage, those coefficients are used to set up the 1D beam equilibrium equations for a cantilever with the specified electrical loading. The clamped boundary condition is imposed in an asymptotically correct way through the orthogonality of asymptotic displacements. The linear system is solved to obtain the macroscopic displacements, from which the tip deflection is extracted. Only the zeroth-order (classical Euler–Bernoulli) solution is required.

## Reproduction target
Compute the static tip deflection (vertical displacement at the free end) of a piezoelectric fiber composite cantilever beam. The beam has external dimensions 4.34 mm depth × 4.14 mm width × 47 mm length, with four 1 mm × 1 mm PZT-4 fibers placed at the centers of the quadrants of a square with 3 mm pitch, embedded in a silicone elastomer matrix. Apply the electrical potential with the top two fibers at +V, the bottom two fibers at –V, and the mid-plane grounded, for V = 50 V, 100 V, and 150 V. Use the asymptotic beam analysis at zeroth order (ABA-0th) with asymptotically correct clamped-free boundary conditions. Output the three tip deflections in micrometers.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Cross-sectional warping and homogenization
- Role: process
- Action: Implement the 2D cross-sectional finite element discretization for the composite beam cross-section (four square PZT-4 fibers in silicone elastomer, dimensions: 4.34 mm depth × 4.14 mm width, fibers 1 mm × 1 mm at 3 mm pitch) using isoparametric shape functions. Compute the cross-sectional stiffness matrices K_uu, K_uφ, K_φφ and right-hand-side matrices as defined in the asymptotic formulation. Apply rigid-body orthogonality constraints via Lagrange multipliers and prescribe electric potentials on the fiber boundaries. Solve for the warping functions driven by macroscopic strain measures and prescribed potentials. Then compute the homogenized 1D macroscopic stiffness coefficients (A_e, A_φ, A_p) and electric constitutive coefficients (B_e, B_φ, B_p).
- Evidence: `/app/outputs/cross_section_warping_matrices.npz`

### Step 2: 1D beam solution and tip deflection
- Role: scored (load-bearing)
- Action: Using the homogenized stiffness matrices from Step 1, set up the 1D macroscopic beam equilibrium equations for a cantilever beam (clamped-free) with the specified electrical loading: top two fibers at +V, bottom two fibers at –V, mid-plane ground, for V = 50 V, 100 V, 150 V. Apply the asymptotically correct displacement boundary conditions at the clamped end. Discretize the 1D domain with appropriate finite elements and solve the linear system to obtain the beam's macroscopic displacement along the axis. Extract the vertical tip deflection (at the free end) for each voltage.
- Output file: `/app/outputs/tip_deflections.json`
- Format: json
- Contract: {"voltages_V": [50.0, 100.0, 150.0], "deflections_micrometer": [float, float, float]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tip_deflections.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tip_deflections.json
- path: `/app/outputs/tip_deflections.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Tip deflections of the piezoelectric fiber composite beam at actuation voltages of 50 V, 100 V, and 150 V.
- schema:
  - `type`: object
  - `required`:
    - `voltages_V`: array of 3 numbers (V)
    - `deflections_micrometer`: array of 3 numbers (μm)

Notes: Only the zeroth-order asymptotic solution (ABA-0th) is required. Higher-order corrections, the pure piezoelectric bimorph validation, 3D FEM comparisons, and rule-of-mixture analysis are excluded from this reproduction task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tip_deflections.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "voltages_V": "array of 3 numbers (V)",
          "deflections_micrometer": "array of 3 numbers (μm)"
        }
      },
      "description": "Tip deflections of the piezoelectric fiber composite beam at actuation voltages of 50 V, 100 V, and 150 V."
    }
  ],
  "notes": "Only the zeroth-order asymptotic solution (ABA-0th) is required. Higher-order corrections, the pure piezoelectric bimorph validation, 3D FEM comparisons, and rule-of-mixture analysis are excluded from this reproduction task."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. The verifier first checks that the required output file(s) conform to the specified format. It then compares the reported tip deflection values against reference criteria and may verify that the results satisfy expected relative trends between the different voltage conditions. The score is a numeric reward in the range [0,1] that reflects how well your computed results meet the verification checks. Reporting numbers without genuinely executing the required computational pipeline is not sufficient to earn credit.
