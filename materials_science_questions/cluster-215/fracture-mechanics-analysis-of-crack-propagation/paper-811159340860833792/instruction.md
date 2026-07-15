# Analytical Crack Area Computation for Bridged Composites

## Problem background
Fiber-reinforced composites, particularly titanium matrix composites with SiC fibers, develop bridged matrix cracks under tensile loading. The crack opening displacement is governed by the frictional sliding of fibers across the crack faces, described by a quadratic bridging law. The additional remote displacement due to cracks depends on the crack area (the integral of the crack opening profile). The analysis distinguishes two asymptotic regimes: short cracks, where the near-tip elliptical opening dominates the entire crack profile, and long cracks, where a steady-state region of constant opening coexists with a near-tip elliptical zone. Computing the nondimensional crack area as a function of nondimensional applied stress is essential for predicting inelastic strain and hysteresis in such composites.

## Approach
Model a fully bridged, through-thickness crack of length 2a in a unidirectional composite under far-field tensile stress. The crack opening displacement is obtained from the integral equation that couples the applied stress, the bridging tractions, and the crack geometry, with the bridging law u = lambda * sigma_b^2. The coefficient lambda depends on fiber diameter, volume fraction, fibre and matrix moduli, and the interface sliding stress. The longitudinal composite modulus E is given by the rule of mixtures.

Treat nondimensional applied stress as Sigma_a = lambda E sigma_a / a and nondimensional crack area as A* = lambda E^2 A / (2 a^3). For short cracks (Sigma_a > 1), assume an elliptical COD profile; enforce consistency with the elastic near-tip square-root singular field and the bridging law to obtain a quadratic equation for the peak bridging stress parameter. Solve it and integrate to get A*. For long cracks (Sigma_a <= 1), divide the crack into a near-tip zone of size a* (determined by requiring near-tip COD to match the bridging law) and a steady-state zone where the bridging stress equals the applied stress. Sum the area contributions from both zones to obtain A*. An unbridged reference area is pi * Sigma_a.

For cyclic loading, the range of crack area DeltaA is related to the monotonic solution by DeltaA(Delta Sigma_a) = 2 * A(Delta Sigma_a / 2). Compute DeltaA_short and DeltaA_long using this transformation.

Use the provided material constants (fibre diameter 140 μm, volume fraction 0.34, fiber modulus 410 GPa, matrix modulus 110 GPa, interface sliding stress 23 MPa, and geometry constants I0=1, I1=1.2) to compute E and lambda, then evaluate all quantities for a set of Sigma_a values.

## Reproduction target
For the nondimensional applied stress values Sigma_a = [0.01, 0.1, 1, 2, 5, 10, 20, 50, 100], compute the following:
- A_short: short-crack nondimensional area (valid for Sigma_a > 1; otherwise NaN)
- A_long: long-crack nondimensional area (valid for all Sigma_a)
- A_unbridged = pi * Sigma_a
- DeltaA_short = 2 * A_short(Sigma_a/2) if Sigma_a/2 > 1, otherwise NaN
- DeltaA_long = 2 * A_long(Sigma_a/2)
Write the results to a CSV file '/app/outputs/crack_area_analytical.csv' with header Sigma_a, A_short, A_long, A_unbridged, DeltaA_short, DeltaA_long.

## Assets

- NumPy: https://pypi.org/project/numpy/
- Material parameters from Table 1

## Workflow steps

### Step 1: Compute analytical crack area and cyclic range
- Role: scored (load-bearing)
- Action: Implement the analytical formulas for nondimensional crack area and cyclic range for a bridged crack with bridging law u = lambda*sigma_b^2. Compute the longitudinal Young's modulus E from the rule of mixtures (E = f*E_f + (1-f)*E_m) and the bridging-law coefficient lambda from the given material parameters. Then, for each prescribed Sigma_a in the list [0.01, 0.1, 1, 2, 5, 10, 20, 50, 100], calculate A_short (using the short-crack approximation, valid for Sigma_a>1, else NaN), A_long (using the long-crack approximation, valid for all Sigma_a), A_unbridged = pi*Sigma_a, DeltaA_short = 2*A_short evaluated at Sigma_a/2 if Sigma_a/2>1 else NaN, and DeltaA_long = 2*A_long evaluated at Sigma_a/2. Write all results to a CSV file.
- Output file: `/app/outputs/crack_area_analytical.csv`
- Format: csv
- Contract: CSV with header: Sigma_a,A_short,A_long,A_unbridged,DeltaA_short,DeltaA_long. Rows correspond to Sigma_a in [0.01,0.1,1,2,5,10,20,50,100]. All columns numeric; NaN allowed for A_short and DeltaA_short where undefined (i.e., Sigma_a<=1 for A_short, Sigma_a/2<=1 for DeltaA_short).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/crack_area_analytical.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### crack_area_analytical.csv
- path: `/app/outputs/crack_area_analytical.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed nondimensional crack areas and cyclic ranges for given Sigma_a values. The reference is recomputed by the checker using the same analytical formulas and material constants.
- schema:
  - `type`: table
  - `required_columns`: `Sigma_a`, `A_short`, `A_long`, `A_unbridged`, `DeltaA_short`, `DeltaA_long`
  - `units`:
    - `Sigma_a`: dimensionless
    - `A_short`: dimensionless
    - `A_long`: dimensionless
    - `A_unbridged`: dimensionless
    - `DeltaA_short`: dimensionless
    - `DeltaA_long`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "crack_area_analytical.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Sigma_a",
          "A_short",
          "A_long",
          "A_unbridged",
          "DeltaA_short",
          "DeltaA_long"
        ],
        "units": {
          "Sigma_a": "dimensionless",
          "A_short": "dimensionless",
          "A_long": "dimensionless",
          "A_unbridged": "dimensionless",
          "DeltaA_short": "dimensionless",
          "DeltaA_long": "dimensionless"
        }
      },
      "description": "Computed nondimensional crack areas and cyclic ranges for given Sigma_a values. The reference is recomputed by the checker using the same analytical formulas and material constants."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently recomputes the expected crack areas using the same analytical formulas and material constants. It compares each row of your CSV against the recomputed reference values using per-element relative and absolute tolerances (the exact tolerances are hidden). The verifier also checks two limiting behaviors: for Sigma_a > 10, A_short must be close to A_unbridged; for Sigma_a < 0.1, A_long must scale quadratically with Sigma_a. The final reward is the fraction of all comparisons (rows × columns plus the two limiting checks) that pass.
