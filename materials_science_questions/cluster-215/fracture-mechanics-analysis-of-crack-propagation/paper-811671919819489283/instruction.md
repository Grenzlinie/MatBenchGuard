# Compute Damage Sensitivity Constants for a Microcracked Viscoelastic Solid

## Problem background
Predicting the effective linear viscoelastic behavior of microcracked solids is a central question in the micromechanics of concrete and other quasi-brittle materials. The present work addresses this by deriving an approximate damage‑dependent Burger model for a non‑aging linear viscoelastic (NALV) solid containing an isotropic distribution of penny‑shaped cracks. Using a stress‑based dilute homogenization scheme, the effective compliance in Laplace‑Carson space is obtained, and an asymptotic series‑matching procedure identifies an equivalent Burger model whose parameters depend linearly on the crack‑density parameter. The key unknown quantities are the dimensionless damage sensitivity constants that govern how the spring moduli and dashpot viscosities of the Maxwell and Kelvin parts degrade with crack density. Computing these constants for a given undamaged concrete material validates the analytical derivation and provides the input needed for subsequent structural-scale simulations.

## Approach
The core idea is to approximate the true effective behavior of a cracked linear viscoelastic solid by a Burger model (a Maxwell unit in series with a Kelvin-Voigt unit). The approach proceeds as follows:

1. Undamaged material: Start from a set of eight undamaged Burger parameters — four bulk constants (spring moduli k_M, k_K and viscosities η_M^s, η_K^s) and four shear constants (spring moduli μ_M, μ_K and viscosities η_M^d, η_K^d).
2. Effective compliance: For an isotropic crack population, the Laplace‑Carson transformed bulk and shear compliances of the cracked solid are expressed in the forms k* / (1 + ε Q*) and μ* / (1 + ε M*), where ε is the crack density parameter and Q*, M* embody the crack-induced softening.
3. Kernel coefficients: Using the undamaged material constants, calculate the coefficients of the series expansions of Q* and M* near p = 0 (Q_o^o, M_o^o, Q_1^o, M_1^o) and near p = ∞ (Q_o^∞, M_o^∞, Q_{-1}^∞, M_{-1}^∞) from the closed‑form expressions that depend only on the undamaged Burger parameters.
4. Matching with Burger model: Write the asymptotic expansions of the compliance that a Burger model would produce, and equate the leading terms with the effective expansions from step 3. This yields two 2 × 2 linear systems: one for the bulk constants (κ_M, κ_K, v_M^s, v_K^s) and one for the shear constants (m_M, m_K, v_M^d, v_K^d). Solving these systems gives the eight dimensionless damage sensitivity constants.

The entire computation is deterministic and requires only standard numeric libraries; the only inputs are the eight undamaged Burger parameters specified below.

## Reproduction target
Using the undamaged concrete Burger parameters listed below, compute the eight dimensionless damage sensitivity constants that relate the cracked Burger parameters to the crack density ε via inverse linear laws.  Specifically:

- Evaluate the bulk-side damage kernel coefficients Q_o^o, Q_1^o, Q_o^∞, Q_{-1}^∞ and the shear-side coefficients M_o^o, M_1^o, M_o^∞, M_{-1}^∞ from the provided explicit formulas.
- Solve the 2 × 2 linear system for bulk (κ_M, κ_K, v_M^s, v_K^s) and the 2 × 2 linear system for shear (m_M, m_K, v_M^d, v_K^d).
- Write all eight constants into the structured JSON file `/app/outputs/damage_sensitivity_constants.json` with the required object layout.

Undamaged Burger parameters (concrete, from Le 2008):
- k_M = 24.42 GPa, μ_M = 13.27 GPa
- k_K = 39.27 GPa, μ_K = 14.07 GPa
- η_M^s = 22×10⁸ GPa·s, η_M^d = 7.75×10⁸ GPa·s
- η_K^s = 1.52×10⁸ GPa·s, η_K^d = 0.254×10⁸ GPa·s

## Assets

- NumPy: numpy

## Explicit formulas for damage kernel coefficients

All parameters refer to the undamaged concrete values given in the "Reproduction target" below.

### Bulk side

$Q_o^o = \frac{16}{9} \frac{\eta_M^s (\eta_M^s + 2\eta_M^d)}{\eta_M^d (2\eta_M^s + \eta_M^d)}$

$Q_1^o = \frac{16}{27} \eta_M^s \frac{\eta_M^s{}^2 + \eta_M^d \eta_M^s + \eta_M^d{}^2}{(2\eta_M^s + \eta_M^d)^2} \left( 3\left(\frac{1}{\mu_M} + \frac{1}{\mu_K}\right) - 2\frac{\eta_M^s}{\eta_M^d}\left(\frac{1}{k_M} + \frac{1}{k_K}\right) \right)$

$Q_o^\infty = \frac{4}{3} \frac{k_M (3k_M + 4\mu_M)}{\mu_M (3k_M + \mu_M)}$

$Q_{-1}^\infty = -\frac{4}{3} k_M \frac{9 k_M^2 + 6 \mu_M k_M + 4 \mu_M^2}{(3k_M + \mu_M)^2} \left( 3\frac{k_M}{\mu_M}\left(\frac{1}{\eta_M^s} + \frac{1}{\eta_K^s}\right) - 2\left(\frac{1}{\eta_M^d} + \frac{1}{\eta_K^d}\right) \right)$

### Shear side

$M_o^o = \frac{32}{45} \frac{(\eta_M^s + 2\eta_M^d)(3\eta_M^s + 2\eta_M^d)}{(\eta_M^s + \eta_M^d)(2\eta_M^s + \eta_M^d)}$

$M_1^o = \frac{32}{45} \frac{\eta_M^s \eta_M^d (7\eta_M^s{}^2 + 10\eta_M^s \eta_M^d + 4\eta_M^d{}^2)}{(\eta_M^s + \eta_M^d)^2 (2\eta_M^s + \eta_M^d)^2} \left( \frac{\eta_M^s}{3k_K} + \frac{\eta_M^s}{3k_M} - \frac{\eta_M^d}{2\mu_K} - \frac{\eta_M^d}{2\mu_M} \right)$

$M_o^\infty = \frac{16}{45} \frac{(9k_M + 4\mu_M)(3k_M + 4\mu_M)}{(3k_M + 2\mu_M)(3k_M + \mu_M)}$

$M_{-1}^\infty = \frac{16}{15} \frac{k_M \mu_M (63 k_M^2 + 60 k_M \mu_M + 16 \mu_M^2)}{(3k_M + \mu_M)^2 (3k_M + 2\mu_M)^2} \left( \frac{3k_M}{\eta_M^s} + \frac{3k_M}{\eta_K^s} - \frac{2\mu_M}{\eta_M^d} - \frac{2\mu_M}{\eta_K^d} \right)$

### Linear systems

**Bulk constants** (κ_M, κ_K, v_M^s, v_K^s):

$\kappa_M = Q_o^\infty$,   $v_M^s = Q_o^o$

$\frac{\kappa_M - Q_o^o}{k_M} + \frac{\kappa_K - Q_o^o}{k_K} = 3 \frac{Q_1^o}{\eta_M^s}$

$\frac{v_M^s - Q_o^\infty}{\eta_M^s} + \frac{v_K^s - Q_o^\infty}{\eta_K^s} = \frac{Q_{-1}^\infty}{3 k_M}$

**Shear constants** (m_M, m_K, v_M^d, v_K^d):

$m_M = M_o^\infty$,   $v_M^d = M_o^o$

$\frac{m_M - M_o^o}{\mu_M} + \frac{m_K - M_o^o}{\mu_K} = 2 \frac{M_1^o}{\eta_M^d}$

$\frac{v_M^d - M_o^\infty}{\eta_M^d} + \frac{v_K^d - M_o^\infty}{\eta_K^d} = \frac{M_{-1}^\infty}{2 \mu_M}$

## Workflow steps

### Step 1: Compute damage sensitivity constants
- Role: scored (load-bearing)
- Action: Using the undamaged Burger parameters given below, evaluate the bulk-side damage kernel coefficients (Q_o^o, Q_1^o, Q_o^∞, Q_{-1}^∞) and shear-side coefficients (M_o^o, M_1^o, M_o^∞, M_{-1}^∞) from the formulas provided in the "Explicit formulas" section above. Then solve the two linear systems (bulk and shear) defined in that same section to obtain the eight dimensionless damage sensitivity constants: κ_M, κ_K, v_M^s, v_K^s (bulk) and m_M, m_K, v_M^d, v_K^d (shear). Write all eight values into a structured JSON file.
- Output file: `/app/outputs/damage_sensitivity_constants.json`
- Format: json
- Contract: {"bulk": {"kappa_M": <float>, "kappa_K": <float>, "v_M_s": <float>, "v_K_s": <float>}, "shear": {"m_M": <float>, "m_K": <float>, "v_M_d": <float>, "v_K_d": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/damage_sensitivity_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### damage_sensitivity_constants.json
- path: `/app/outputs/damage_sensitivity_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dimensionless damage sensitivity constants for the Burger model approximation of a microcracked solid.
- schema:
  - `type`: object
  - `required`:
    - `bulk`: object with keys kappa_M, kappa_K, v_M_s, v_K_s
    - `shear`: object with keys m_M, m_K, v_M_d, v_K_d
  - `properties`:
    - `bulk`:
      - `kappa_M`:
        - `type`: number
      - `kappa_K`:
        - `type`: number
      - `v_M_s`:
        - `type`: number
      - `v_K_s`:
        - `type`: number
    - `shear`:
      - `m_M`:
        - `type`: number
      - `m_K`:
        - `type`: number
      - `v_M_d`:
        - `type`: number
      - `v_K_d`:
        - `type`: number

Notes: All eight constants are deterministic given the fixed undamaged matrix parameters and the analytical formulas. The checker recomputes them independently using the same parameters and compares within a tight relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "damage_sensitivity_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk": "object with keys kappa_M, kappa_K, v_M_s, v_K_s",
          "shear": "object with keys m_M, m_K, v_M_d, v_K_d"
        },
        "properties": {
          "bulk": {
            "kappa_M": {
              "type": "number"
            },
            "kappa_K": {
              "type": "number"
            },
            "v_M_s": {
              "type": "number"
            },
            "v_K_s": {
              "type": "number"
            }
          },
          "shear": {
            "m_M": {
              "type": "number"
            },
            "m_K": {
              "type": "number"
            },
            "v_M_d": {
              "type": "number"
            },
            "v_K_d": {
              "type": "number"
            }
          }
        }
      },
      "description": "Dimensionless damage sensitivity constants for the Burger model approximation of a microcracked solid."
    }
  ],
  "notes": "All eight constants are deterministic given the fixed undamaged matrix parameters and the analytical formulas. The checker recomputes them independently using the same parameters and compares within a tight relative tolerance."
}
```

## How you are scored
A hidden verifier independently recomputes the damage sensitivity constants by evaluating the same closed‑form expressions and solving the same linear systems using the undamaged parameters provided in the task. The verifier compares each submitted constant to the recomputed gold value using a strict relative tolerance. Each scored artifact’s result is weighted according to the task’s breakdown, and the final reward (a single number between 0 and 1) aggregates the per‑stage outcomes. Reporting numbers that merely match a known reference without correct computation will not pass the verifier’s check; the constants must be derived from the given formulas and input parameters.
