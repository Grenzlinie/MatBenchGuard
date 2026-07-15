# Polynomial approximation of universal M-shell ionization cross-sections

## Problem background
Ionisation cross-sections for M-shell electrons induced by H+ and He2+ ions are needed for simulating X-ray intensities in particle-induced X-ray emission (PIXE) analysis. The ECPSSR theory provides accurate cross-sections, but its direct evaluation requires time‑consuming numerical integration of atomic form factors. This work produces compact polynomial approximations that replace the expensive integration, enabling fast cross‑section computation in simulation codes. This reproduction package computes the polynomial coefficients that define those approximations.

## Approach
The approach starts by computing ionisation cross-sections in the plane‑wave Born approximation (PWBA) using the atomic form factor polynomials from Choi (1973). The PWBA integral is evaluated with Lobatto quadrature over exact integration limits, omitting the finite maximum momentum transfer correction. The ECPSSR ionisation cross‑sections are then obtained by applying the Coulomb deflection and other corrections. These cross‑sections are rescaled to a universal form by dividing out the Coulomb deflection term and introducing an extra weight with the sub‑shell screening parameter, following definitions from Taborda et al. (2011). Tuning constants bU and cU (provided per sub‑shell) control the rescaling such that the universal curves collapse for all target elements and both projectile types. Universal cross‑sections are computed for target atomic numbers Z = 62 to 92, for incident H+ and He2+ ions, and for 70 beam energies between 100 keV and 10 MeV. For each M sub‑shell (M1–M5), the universal cross‑sections are then fit with a seventh‑order polynomial P(x) = Σ a_i x^i, where the variable x is derived from the relativistic reduced velocity and the screening parameter, and P = −ln(σ^U θ^(c^U)). For the M1 sub‑shell, two separate fits are performed: one for x < 1.55 and another for x ≥ 1.55. The fitted polynomial coefficients a0–a7 are the primary output of this work.

## Reproduction target
Produce a JSON file (polynomial_coefficients.json) containing the seventh‑order polynomial coefficients (a0 through a7) that best approximate the universal M‑shell ionisation cross‑sections for all five sub‑shells. For M1, provide two sets of coefficients corresponding to the two branches split at x = 1.55. The file must also list the tuning constants bU and cU used for each sub‑shell. The coefficients should be obtained by following the integration and fitting procedure described in the workflow steps; the verifier will compare them against a hidden reference.

## Assets

- Choi B.-H. (1973) Form factor polynomial functions for ionisation cross-sections: https://doi.org/10.1103/PhysRevA.7.2056
- Bambynek et al. (1972) Atomic parameters (binding energies, Coster-Kronig yields, etc.): https://doi.org/10.1103/RevModPhys.44.716
- Taborda et al. (2011) Universal ionisation cross‑section definitions and rescaling variables: https://doi.org/10.1002/xrs.1312

## Workflow steps

### Step 1: Compute universal M-shell ionisation cross-sections
- Role: process
- Action: Implement the PWBA form-factor integration using Choi's polynomial functions, Lobatto quadrature (10 points per subinterval) and exact integration limits, without the finite maximum momentum transfer correction. Perform calculations for target atomic numbers Z_target = 62 to 92, incident H+ (Z_proj=1) and He2+ (Z_proj=2) ions, and 70 beam energy values in the range 0.1–10.0 MeV. Compute ECPSSR cross‑sections and rescale to universal cross‑sections σ^U_{M,o} using the given tuning constants b^U = [0.2, 0.2, 0.32, 0.4, 0.4] and c^U = [2.0, 2.0, 4.0, 8.0, 9.0] for sub-shells M1–M5. Use atomic parameters from Bambynek et al. and the rescaling variables from Taborda et al. (2011).
- Evidence: `/app/outputs/universal_data.csv`

### Step 2: Fit seventh-order polynomials and output coefficients
- Role: scored (load-bearing)
- Action: For each M sub‑shell o=1..5, transform the computed universal cross‑section data to the polynomial variable x_{M,o} = (1/(ξ^R_{M,o} θ_{M,o}^{b^U_{M,o}}))^{1/2} and the polynomial value P = −ln(σ^U_{M,o} θ_{M,o}^{c^U_{M,o}}). Fit a seventh‑order polynomial P_{M,o}(x) = Σ_{i=0}^{7} a_i x^i to the (x,P) points using least‑squares. For M1, perform two separate fits: one for x < 1.55 and another for x ≥ 1.55. Write the coefficients a0..a7 for each sub‑shell (and each branch for M1) to polynomial_coefficients.json. Also include the tuning constants b^U and c^U used.
- Output file: `/app/outputs/polynomial_coefficients.json`
- Format: json
- Contract: A JSON object with keys: "M1_left" (array of 8 floats), "M1_right" (array of 8 floats), "M2" (array of 8 floats), "M3" (array of 8 floats), "M4" (array of 8 floats), "M5" (array of 8 floats); and top‑level keys "bU" (array of 5 floats) and "cU" (array of 5 floats) containing the tuning constants used.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/polynomial_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### polynomial_coefficients.json
- path: `/app/outputs/polynomial_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Seventh-order polynomial coefficients for M1–M5 sub-shells (including two branches for M1) and the tuning constants used.
- schema:
  - `type`: object
  - `required`: `M1_left`, `M1_right`, `M2`, `M3`, `M4`, `M5`, `bU`, `cU`
  - `properties`:
    - `M1_left`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 8
      - `maxItems`: 8
    - `M1_right`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 8
      - `maxItems`: 8
    - `M2`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 8
      - `maxItems`: 8
    - `M3`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 8
      - `maxItems`: 8
    - `M4`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 8
      - `maxItems`: 8
    - `M5`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 8
      - `maxItems`: 8
    - `bU`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 5
      - `maxItems`: 5
    - `cU`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 5
      - `maxItems`: 5

Notes: The hidden checker compares each coefficient to the paper's reported values with a relative tolerance. The tuning constants must match the provided values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "polynomial_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "M1_left",
          "M1_right",
          "M2",
          "M3",
          "M4",
          "M5",
          "bU",
          "cU"
        ],
        "properties": {
          "M1_left": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 8,
            "maxItems": 8
          },
          "M1_right": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 8,
            "maxItems": 8
          },
          "M2": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 8,
            "maxItems": 8
          },
          "M3": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 8,
            "maxItems": 8
          },
          "M4": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 8,
            "maxItems": 8
          },
          "M5": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 8,
            "maxItems": 8
          },
          "bU": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 5,
            "maxItems": 5
          },
          "cU": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 5,
            "maxItems": 5
          }
        }
      },
      "description": "Seventh-order polynomial coefficients for M1–M5 sub-shells (including two branches for M1) and the tuning constants used."
    }
  ],
  "notes": "The hidden checker compares each coefficient to the paper's reported values with a relative tolerance. The tuning constants must match the provided values."
}
```

## How you are scored
A hidden verifier reads your polynomial_coefficients.json, extracts the coefficients for each sub‑shell and branch, and compares them to reference values. Each coefficient is checked for agreement within a relative tolerance. Your score is the fraction of coefficients that fall within the tolerance. The tuning constant arrays are also checked for exact correctness. No additional reward is given for intermediate artifacts; only the final polynomial coefficients count toward the score.
