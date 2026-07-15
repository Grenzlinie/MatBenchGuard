# Compton Profile Defect Slopes for Hydrogenic Orbitals

## Problem background
In Compton scattering from atoms, the impulse approximation (IA) neglects final‑state interactions, but precision measurements reveal asymmetries and a peak shift relative to the IA prediction — collectively called Compton defects. A theoretical treatment using a series expansion of the Born propagator yields corrective terms that depend only on the initial target state. For hydrogenic ions, the first antisymmetric correction J′(q,k) has been derived in closed form for the K‑ and L‑shell orbitals (1s, 2s, 2p_{x,y}, 2p_z). The slope of this correction at zero momentum transfer, Δ′ = dJ′/dq at q=0, provides a compact measure of the defect’s strength and sign. The work also uncovers a simple sign pattern tied to the parity of the orbital quantum numbers l+m, which relates the direction of the peak shift to the symmetry of the electron’s wavefunction. In this task you will compute the scaled slope KZΔ′ (where K is the scaled momentum transfer magnitude and Z the nuclear charge) for each of the four orbitals and verify the parity rule.

## Approach
The antisymmetric correction, when multiplied by the product KZ, depends only on the scaled variable Q = q/ζ (ζ = Z/n). The paper provides universal rational‑trigonometric functions F_orbital(Q) = KZ·J′(Q) for the four orbitals. These functions involve arctangents and polynomials and are given by:

$$
F_{1s}(Q) = \frac{16}{3\pi}\frac{Q}{(1+Q^{2})^{3}}\left(\frac{3}{4} - \frac{\arctan Q}{Q}\right)
$$

$$
F_{2s}(Q) = \frac{32}{\pi}\frac{Q}{(1+Q^{2})^{5}}\left[\frac{1}{3} - 4Q + Q^{4} + \frac{8}{3}\frac{\arctan Q}{Q}\left(-\frac{2}{5} + Q^{2} - Q^{4}\right)\right]
$$

$$
F_{2p_{xy}}(Q) = \frac{64}{15\pi}\frac{Q}{(1+Q^{2})^{4}}\left(5 - 6\frac{\arctan Q}{Q}\right)
$$

$$
F_{2p_{z}}(Q) = \frac{128}{15\pi}\frac{Q}{(1+Q^{2})^{5}}\left(5 + 10 Q^{2} - 24 Q\arctan Q\right)
$$

The scaled slope KZΔ′ is the derivative dF/dQ evaluated at Q = 0. You may obtain it by evaluating F on a fine grid of Q values near zero and estimating the slope (e.g., by finite differences or linear regression), or by differentiating the analytic expressions directly. The universal functions do not depend on K or Z, so the final scaled slopes are the same irrespective of K. The protocol uses the representative value K = 3 to isolate geometric orbital effects, but the required output is the slope of F at Q = 0, which is a dimensionless constant.

Implement each F_orbital(Q) using standard mathematical libraries (NumPy, SciPy), sample Q in a neighbourhood of 0, compute the derivative, and write the four scaled slopes to the output file. You should also check that the signs of the obtained slopes follow the parity rule derived from the orbital quantum numbers l and m (the rule involves the parity of l+m).

## Reproduction target
Compute the scaled slope KZΔ′ (i.e., the derivative of the universal function F_orbital(Q) at Q = 0) for the hydrogenic 1s, 2s, 2p_{x,y}, and 2p_z orbitals using the provided analytic expressions. Report the four numeric values in a JSON file named `/app/outputs/slopes.json` with the keys `1s`, `2s`, `2p_xy`, `2p_z`. Additionally, verify that the signs of your computed slopes are consistent with the parity rule (which links the sign to the parity of l+m).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Compton defect slopes for hydrogenic orbitals
- Role: scored (load-bearing)
- Action: Implement the analytic expressions for the antisymmetric Compton defect J'(Q) given in the reference paper for hydrogenic 1s, 2s, 2p_{x,y}, and 2p_z orbitals. The formula for each orbital involves the scaled variable Q and the product KZ. From the computed J'(Q) curve around Q=0, determine the slope Δ' = dJ'/dq at q=0 using the derived analytic constant or numerical differentiation. Report the four scaled slopes KZΔ' in a JSON file.
- Output file: `/app/outputs/slopes.json`
- Format: json
- Contract: {"1s": number, "2s": number, "2p_xy": number, "2p_z": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/slopes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### slopes.json
- path: `/app/outputs/slopes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed scaled slopes KZΔ' (derivative of J' with respect to q at q=0) for hydrogenic 1s, 2s, 2p_{x,y}, and 2p_z orbitals. The values are dimensionless and must be compared to exact analytic constants from the paper.
- schema:
  - `type`: object
  - `required_keys`: `1s`, `2s`, `2p_xy`, `2p_z`
  - `properties`:
    - `1s`:
      - `type`: number
    - `2s`:
      - `type`: number
    - `2p_xy`:
      - `type`: number
    - `2p_z`:
      - `type`: number
  - `units`:
    - `1s`: dimensionless (scaled slope KZΔ')
    - `2s`: dimensionless
    - `2p_xy`: dimensionless
    - `2p_z`: dimensionless

Notes: The scored artifact contains only the final slope values; the intermediate J'(Q) curves are not required as outputs. The hidden checker will compare each reported number against the paper's exact slopes with a tight tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "slopes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "1s",
          "2s",
          "2p_xy",
          "2p_z"
        ],
        "properties": {
          "1s": {
            "type": "number"
          },
          "2s": {
            "type": "number"
          },
          "2p_xy": {
            "type": "number"
          },
          "2p_z": {
            "type": "number"
          }
        },
        "units": {
          "1s": "dimensionless (scaled slope KZΔ')",
          "2s": "dimensionless",
          "2p_xy": "dimensionless",
          "2p_z": "dimensionless"
        }
      },
      "description": "Computed scaled slopes KZΔ' (derivative of J' with respect to q at q=0) for hydrogenic 1s, 2s, 2p_{x,y}, and 2p_z orbitals. The values are dimensionless and must be compared to exact analytic constants from the paper."
    }
  ],
  "notes": "The scored artifact contains only the final slope values; the intermediate J'(Q) curves are not required as outputs. The hidden checker will compare each reported number against the paper's exact slopes with a tight tolerance."
}
```

## How you are scored
A hidden verifier reads your `slopes.json`. It checks each reported slope against the exact expected value within a numerical tolerance (the reference values are derived from the same analytic expressions). It also verifies that the signs of the four slopes obey the parity rule determined by the orbital quantum numbers l and m. The final score is the fraction of checks that pass. Submitting pre‑looked numbers without implementing the formulas will not satisfy the tolerance requirement.
