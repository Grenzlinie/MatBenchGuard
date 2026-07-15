# Anisotropic Elastic Energy and Binding of Quasidipoles in Zn

## Problem background
In dislocation theory, a quasidipole is a pair of straight, infinite, parallel dislocations lying in neighbouring slip planes with an angle between their Burgers vectors. This task studies the total elastic energy per unit length of such quasidipoles situated in the basal plane of hexagonal zinc, using full anisotropic elasticity. The objective is to determine the stable equilibrium configurations (the relative lateral position of the two dislocations) and the associated binding and transition energies for configurations where the angle between the Burgers vectors, φ, is 120° or 180° — these are of particular interest for understanding dislocation interactions in this hexagonal metal.

## Approach
The total energy of a quasidipole is expressed as a closed-form formula involving the anisotropic elastic constants of zinc, the Burgers vectors of the two dislocations, their separation coordinates, and an orientation angle α describing the direction of the Burgers vectors relative to the dislocation line. The approach consists of three parts: (i) define all needed material and geometric parameters, including the elastic constants, the Burgers vector magnitude, the basal plane spacing, and derived auxiliary constants; (ii) implement a function that computes the total energy per unit length for given α, φ, lateral position x, and inter‑plane distance y; (iii) for each specified combination of φ, α, and y, solve numerically for the equilibrium x (where the derivative of the energy with respect to x vanishes) and compute the corresponding reduced coordinate ρ = x / y, the self‑energy U₀, the binding energy Ub = U₀ – Ud (Ud being the energy at the stable equilibrium), and, where applicable, the transition energy ΔUd between two stable positions. Screw‑type configurations that possess no finite‑x equilibrium are flagged by outputting null for the corresponding quantities.

## Total energy expression

The total elastic energy per unit length of a quasidipole with inter‑plane distance \(y\), lateral position \(x\), angle between Burgers vectors \(\varphi\), and orientation \(\alpha\) is given by equation (2) from the source:

\[
\begin{aligned}
U(\alpha, x, \varphi, y) = & \frac{b^2}{4\pi} \left[K_e (\cos^2\alpha + \cos^2(\alpha+\varphi)) + K_s (\sin^2\alpha + \sin^2(\alpha+\varphi))\right] \ln\frac{R}{r_0} \\
& + \frac{b^2}{2\pi} \Bigg\{ \frac{1}{2} \cos\alpha \cos(\alpha+\varphi) \Bigg[ K_e \ln \sqrt{ \frac{(R'^2 - \lambda^2 y^2)^2 + \lambda^2 d^2 R'^2 y^2}{(x^2 - \lambda^2 y^2)^2 + \lambda^2 d^2 x^2 y^2} } \\
& \qquad + K_1 \left( \arctan\frac{K_3 y^2}{R'^2 - K_2 y^2} - \arctan\frac{K_3 y^2}{x^2 - K_2 y^2} \right) \Bigg] \\
& \qquad + \sin\alpha \sin(\alpha+\varphi) \, K_s \ln \sqrt{ \frac{R'^2 + \eta^2 y^2}{x^2 + \eta^2 y^2} } \Bigg\}.
\end{aligned}
\]

The self-energy of each dislocation is embedded in the first term. The boundary terms \(R'\) and the function evaluation use the outer cutoff \(R = 10^6 b\) and the current inter‑plane distance \(y\):
- \(h = y\) (the inter‑plane distance itself),
- \(R' = \sqrt{R^2 - h^2}\).

The auxiliary constants are defined in terms of the anisotropic elastic moduli \(c_{ij}\) (in units of \(10^{12}\,\mathrm{dyn/cm^2}\)):

\[
\begin{aligned}
\bar{c}_{13} &= \sqrt{c_{11}c_{33}}, \\
\lambda^4 &= \frac{c_{11}}{c_{33}}, \qquad \lambda = (\lambda^4)^{1/4}, \\
\eta^2 &= \frac{c_{11}-c_{12}}{2c_{44}}, \\
K_e &= (\bar{c}_{13}+c_{13}) \sqrt{ \frac{c_{44}(\bar{c}_{13}-c_{13})}{c_{33}(\bar{c}_{13}+c_{13}+2c_{44})} }, \\
K_s &= \sqrt{ \tfrac12 (c_{11}-c_{12}) c_{44} }, \\
C &= \frac{(\bar{c}_{13}+c_{13})(\bar{c}_{13}-c_{13}-2c_{44})}{\bar{c}_{13} c_{44}}, \\
d^2 &= C + 4, \\
K_2 &= \frac{c_{13}(c_{13}+2c_{44}) - \bar{c}_{13}^2}{2c_{33}c_{44}}, \\
K_1 &= \lambda \frac{\bar{c}_{13}^2 - c_{13}^2}{2\bar{c}_{13} \sqrt{1 - \frac{(\bar{c}_{13}+c_{13}+2c_{44})(\bar{c}_{13}-c_{13})}{4\bar{c}_{13}c_{44}}}}, \\
K_3 &= \sqrt{\lambda^4 - K_2^2}.
\end{aligned}
\]

All logarithms are natural logarithms; \(\arctan\) returns the principal value in radians. The term involving \(R'\) ensures that when \(x = R'\) and \(y = h\) the total energy reduces to the sum of the self‑energies (the first line), i.e. \(U(R', \alpha, \varphi, h) = U_0\).

## Reproduction target
Produce a JSON file named `reproduced_results.json` containing, for every combination of φ ∈ {120, 180} and the α values listed in the step description, and for each inter‑plane distance y = 2, 5, 10, 50, 100 (in units of 0.928b), the computed equilibrium reduced coordinate ρ, the binding energy Ub, and the transition energy ΔUd. The file must be a JSON array of objects with integer fields phi, alpha, y, and nullable numeric fields rho, Ub, delta_ud. The goal is to obtain these physical quantities from the anisotropic energy expression using only the public elastic constants and geometric data; the agreement of these computed values with the known reference results demonstrates a correct reproduction of the paper’s main numerical findings.

## Assets

- Anisotropic elastic constants of Zn (c11, c33, c44, c12, c13): 10.1016/S0081-1947(08)60496-8
- Burgers vector length b=2.6649 Å, basal plane spacing 0.928b: 10.1080/14786436608213519

## Workflow steps

### Step 1: Set up material and geometric parameters
- Role: process
- Action: Define the anisotropic elastic constants of Zn (c11=1.628, c33=1.567, c44=0.387, c12=0.564, c13=0.508 ×10^12 dyn/cm^2), the Burgers vector length b=2.6649 Å, basal plane spacing 0.928b, outer cutoff R=10^6 b, core radius r0=b/2. Compute all derived auxiliary quantities (K1, K2, K3, Ke, Ks, C, d^2, lambda^4, eta^2) as defined in the paper.
- Evidence: none

### Step 2: Implement total energy function
- Role: process
- Action: Implement a callable function U(alpha, x, phi, y) that returns the total elastic energy per unit length according to the anisotropic formula involving the auxiliary constants. The function must handle the logarithmic and arctangent terms correctly.
- Evidence: none

### Step 3: Compute equilibrium positions, binding energies and output results
- Role: scored (load-bearing)
- Action: For each combination: phi in {120, 180}, alpha values: for phi=120: 30°, 60°, 90°, 120°; for phi=180: 0°, 30°, 60°, 90°; y values: 2, 5, 10, 50, 100 (in units of 0.928b). Compute the equilibrium x_eq by solving dU/dx = 0 (or minimizing U numerically). Compute rho = x_eq / y. Compute the self-energy U0 and the energy at equilibrium Ud, then binding energy Ub = U0 - Ud. When two stable positions exist (for phi=120, alpha=30°,60°), compute the local maximum energy U_lm between them and delta_ud = U_lm - Ud. For screw-type configurations with no equilibrium, output null for rho, Ub, delta_ud. Write all results as an array of JSON objects to 'reproduced_results.json' with keys: phi (integer), alpha (integer), y (integer), rho (number or null), Ub (number or null), delta_ud (number or null).
- Output file: `/app/outputs/reproduced_results.json`
- Format: json
- Contract: Array of objects with integer fields phi, alpha, y, and nullable numeric fields rho, Ub, delta_ud.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.json
- path: `/app/outputs/reproduced_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Reproduced equilibrium positions (ρ) and binding energies Ub (and transition energies ΔUd for φ=120°) for quasidipole configurations in Zn.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `phi`:
        - `type`: integer
        - `enum`: `120`, `180`
      - `alpha`:
        - `type`: integer
        - `enum`: `0`, `30`, `60`, `90`, `120`
      - `y`:
        - `type`: integer
        - `enum`: `2`, `5`, `10`, `50`, `100`
      - `rho`:
        - `type`: `number`, `null`
        - `description`: Reduced equilibrium position x_eq / y
      - `Ub`:
        - `type`: number
      - `delta_ud`:
        - `type`: `number`, `null`
    - `required`: `phi`, `alpha`, `y`, `Ub`

Notes: Values are numerically recomputed from the total energy expression; they correspond to Table I and Table II of the source paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "phi": {
              "type": "integer",
              "enum": [
                120,
                180
              ]
            },
            "alpha": {
              "type": "integer",
              "enum": [
                0,
                30,
                60,
                90,
                120
              ]
            },
            "y": {
              "type": "integer",
              "enum": [
                2,
                5,
                10,
                50,
                100
              ]
            },
            "rho": {
              "type": [
                "number",
                "null"
              ],
              "description": "Reduced equilibrium position x_eq / y"
            },
            "Ub": {
              "type": "number"
            },
            "delta_ud": {
              "type": [
                "number",
                "null"
              ]
            }
          },
          "required": [
            "phi",
            "alpha",
            "y",
            "Ub"
          ]
        }
      },
      "description": "Reproduced equilibrium positions (ρ) and binding energies Ub (and transition energies ΔUd for φ=120°) for quasidipole configurations in Zn."
    }
  ],
  "notes": "Values are numerically recomputed from the total energy expression; they correspond to Table I and Table II of the source paper."
}
```

## How you are scored
A hidden verifier will read your `reproduced_results.json` and compare each entry’s rho, Ub, and delta_ud to reference values using an appropriate numerical tolerance. It will also verify structural requirements: for each (phi, alpha) pair, Ub and delta_ud must decrease monotonically as y increases, and screw‑type rows (where no finite equilibrium exists) must have null for rho, Ub, and delta_ud. The final reward is computed as a weighted combination of the proportion of entries that satisfy the numerical comparison and the satisfaction of the monotonicity and null‑handling rules. You do not need to know the reference numbers or tolerances; you must faithfully implement the energy expression and the equilibrium search as described, and report the raw computed values.
