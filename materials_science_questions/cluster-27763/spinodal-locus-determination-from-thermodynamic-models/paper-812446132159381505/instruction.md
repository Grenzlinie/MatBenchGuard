# Binodal Threshold Determination from Cahn-Hilliard Equilibrium Solutions

## Problem background
The Cahn-Hilliard equation models phase separation in binary mixtures. For a quartic free energy, the one-dimensional equilibrium configurations form a family of periodic solutions expressed in Jacobi elliptic functions. These solutions are subject to a composition conservation constraint that restricts the admissible parameters. Above the spinodal (where the uniform state is linearly stable), non-trivial equilibrium solutions exist only for a certain range of the model parameter B². Determining the lower boundary of this range—the binodal limit—sheds light on the transition between the stable and metastable regions and on the character of equilibrium solutions in the one-dimensional setting.

## Approach
The equilibrium condition reduces to an autonomous ordinary differential equation, c_{xx} = c + B c² + c³ − γ, where γ is an integration constant. Multiplying by c_x and integrating yields a first integral. The family of periodic solutions can be expressed in closed form using Jacobi elliptic functions. Introduce two parameters C₂ (0<C₂<1) and C₁>1 such that the elliptic modulus is k² = C₁C₂, with 0<k²<1. The solution over one period is

c(x) = (α − √(C₂) β sn(f x, k²)) / (1 − √(C₂) sn(f x, k²))

where sn(u, m) is the Jacobi elliptic sn function with parameter m=k²,

α = −B/3 + (−2C₂ + 1 + C₁C₂) √Δ,
β = −B/3 + (2C₁ − 1 − C₁C₂) √Δ,

with

Δ = (B²/3 − 1) / [ (1+C₁C₂)² − 12 C₁C₂ + 2(C₁+C₂)(1+C₁C₂) ].

The period L is given by

L² = 8 K(k)(1+k²) / [ 1 + B(α+β) + 3αβ ],

where K(k) is the complete elliptic integral of the first kind, and

γ = (B/3)(α²+4αβ+β²)/2 + (α+β)(1+αβ)/2.

The parameter f is obtained from f = √( K(k) [1 + B(α+β) + 3αβ] / [2(1+k²)] ).

The above expressions correspond to the branch that reaches the binodal limit; the opposite sign choice in the vector (α,β) yields a second branch that does not approach the binodal.

Imposing the composition conservation constraint ∫₀ᴸ c(x) dx = 0 reduces the two free parameters (C₂,k²) to a one-parameter branch. For a given B², the integral is evaluated numerically over a grid of (C₂,k²) or solved via root-finding to find admissible combinations. The binodal threshold is the minimum B² for which such a constrained solution exists; it corresponds to the limit k²→1 and C₂→1, where the period diverges. Numerical root-finding, integration, and elliptic function evaluation (available in SciPy and NumPy) are used to trace the existence boundary and locate that critical B² value.

## Reproduction target
Compute the minimum value of the squared model parameter B² above the spinodal for which nontrivial one-dimensional periodic equilibrium solutions of the Cahn-Hilliard equation with a quartic free energy satisfy the composition conservation constraint. Output the result in a JSON file named `binodal_threshold.json` containing the field `B_min_squared` (float) and a `method` string describing the numerical procedure used.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Numerical evaluation of composition constraint and binodal search
- Role: process
- Action: Implement the one-dimensional equilibrium ODE first integral and express the family of periodic solutions in terms of Jacobi elliptic functions. For a range of model parameter B above the spinodal, numerically evaluate the composition conservation constraint over the (C₂, k²) parameter plane using root-finding or grid scanning. Determine the minimum B² for which constrained solutions exist (where k²→1, C₂→1, period diverges).
- Evidence: none

### Step 2: Report binodal threshold
- Role: scored (load-bearing)
- Action: Write the computed binodal threshold to a JSON file. The file must contain the field B_min_squared (float) giving the minimum squared model parameter B² above the spinodal for which nontrivial one-dimensional periodic equilibrium solutions satisfy the composition conservation constraint, and a field method (string) briefly describing the numerical procedure used.
- Output file: `/app/outputs/binodal_threshold.json`
- Format: json
- Contract: {"B_min_squared": float, "method": string}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binodal_threshold.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binodal_threshold.json
- path: `/app/outputs/binodal_threshold.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The value of the squared model parameter B² that marks the binodal limit above the spinodal, where nontrivial constrained equilibrium solutions first appear. The checker compares this value to a hidden reference with a tolerance appropriate for numerical differences.
- schema:
  - `type`: object
  - `required`:
    - `B_min_squared`: number (float)
    - `method`: string (non-empty)

Notes: The scoring is based solely on the B_min_squared field. The method field is advisory and is not part of the numerical check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binodal_threshold.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "B_min_squared": "number (float)",
          "method": "string (non-empty)"
        }
      },
      "description": "The value of the squared model parameter B² that marks the binodal limit above the spinodal, where nontrivial constrained equilibrium solutions first appear. The checker compares this value to a hidden reference with a tolerance appropriate for numerical differences."
    }
  ],
  "notes": "The scoring is based solely on the B_min_squared field. The method field is advisory and is not part of the numerical check."
}
```

## How you are scored
A hidden verifier reads your `binodal_threshold.json` and independently compares the numeric value of `B_min_squared` against a reference threshold with a tolerance chosen to account for reasonable numerical differences. Full credit (1.0) is awarded if your computed value falls within that tolerance of the hidden baseline; otherwise the reward is 0.0. The `method` field is required but is used only for documentation and does not affect the score.
