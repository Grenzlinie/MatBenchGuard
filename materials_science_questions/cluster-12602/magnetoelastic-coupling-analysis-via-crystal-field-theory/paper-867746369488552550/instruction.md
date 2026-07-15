# Magnetically induced deformations in twisted particle chains: scale-bridging derivation and evaluation

## Problem background
Soft magnetorheological elastomers containing embedded magnetic particles can be fabricated with twisted chain-like particle aggregates, enabling them to act as stimuli-responsive twist actuators. When a homogeneous magnetic field is applied along the twist axis, the material undergoes both axial deformation (expansion/contraction) and global torsional (twist) deformation. Understanding these magnetically induced deformations requires linking a discrete mesoscopic model of the particle chains to a macroscopic continuum description. The mesoscopic model provides explicit formulas for the axial deformation amplitude A and torsional deformation amplitude τ, as well as expressions for the macroscopic magnetic anisotropy parameters (α∥, α⊥) and magnetostrictive couplings (ζ₁, ζ₃, ζ₄, ζ₆) in terms of the mesoscopic parameters (particle radius, magnetic susceptibility, initial particle spacing, radial distance from the axis, particle number density, effective shear modulus, and cylinder radius). The task is to derive these relationships and compute the deformation amplitudes and macroscopic system parameters as functions of the initial twist per unit length q₀.

## Approach
You will implement a theoretical derivation consisting of three conceptual stages, then perform a numerical evaluation.

1. **Mesoscopic minimal model:** Define a twisted chain of point-like magnetic particles; compute the magnetic dipole moment of each particle including contributions from nearest-neighbor mutual magnetization; construct the free energy per volume as a function of the axial deformation amplitude A and torsional deformation amplitude τ; expand to linear order in A and τ; minimize to obtain closed-form analytic expressions for A and τ (the deformation amplitudes) in terms of the mesoscopic parameters and the external magnetic field.

2. **Macroscopic continuum theory:** Introduce a local anisotropy director that follows the twisted structure; write down a free‑energy density containing uniaxial magnetic terms (parametrized by unknown α∥, α⊥) and general magnetostrictive couplings (parametrized by unknown ζ₁, ζ₃, ζ₄, ζ₆); integrate over a cylindrical volume to obtain the total free energy; compute the macroscopic magnetization by minimizing the free energy with respect to M; expand the free energy and magnetization up to linear order in A and τ.

3. **Scale‑bridging:** Compare the mesoscopic energy and magnetization expansions with the volume‑averaged macroscopic ones term‑by‑term (terms independent of A,τ, linear in A, and linear in τ). The comparison yields a set of equations that determine the macroscopic parameters α∥, α⊥, ζ₁, ζ₃, ζ₄, ζ₆ as functions of the mesoscopic parameters. Solve this linear system to obtain analytic formulas for the six macroscopic parameters.

Finally, using the derived analytic expressions, evaluate A, τ, α∥, α⊥, ζ₁, ζ₃, ζ₄, ζ₆ numerically for a fixed set of mesoscopic parameters (listed in the reproduction target) over a range of scaled initial twist q₀h₀ ∈ [−2,2] and output the results as a CSV file.

## Reproduction target
Compute the magnetically induced axial deformation amplitude A, torsional deformation amplitude τ, and the six macroscopic system parameters α∥, α⊥, ζ₁, ζ₃, ζ₄, ζ₆ for the following fixed mesoscopic parameters:

- particle radius a = 85 × 10⁻⁶ m
- magnetic susceptibility χ = 13.1
- initial vertical particle spacing h₀ = 300 × 10⁻⁶ m
- initial radial distance from cylinder axis ρ₀ = 1.5 × 10⁻³ m
- particle number density n = 10¹⁰/(2π) m⁻³
- effective shear modulus μ = 1 Pa
- cylinder radius R = 2 × 10⁻³ m

The initial twist is quantified by the product q₀h₀, where q₀ is the initial pitch of the helix (the twist angle per unit length). Evaluate all quantities at q₀h₀ values evenly spaced from -2 to 2 (inclusive), using at least 50 points.

Output the results as a CSV file named `predicted_results.csv` with columns:
`q0h0, A, tau, alpha_parallel, alpha_perp, zeta1, zeta3, zeta4, zeta6`.
The file must contain one row per q₀h₀ value. All numbers should be computed from YOUR OWN derivations following the workflow steps — do not hard‑code any numbers from the literature.

## Assets

- NumPy: numpy
- SymPy: sympy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Derive mesoscopic energy and equilibrium deformations
- Role: process
- Action: Implement the mesoscopic minimal model using symbolic algebra (e.g., SymPy): define the twisted chain geometry, compute single-particle and nearest-neighbor mutual magnetic dipole moments, construct the total energy per volume as a function of deformation amplitudes A and τ, expand to linear order, and minimize to obtain closed-form expressions for A and τ. Log the derived formulas and a substitution verification.
- Evidence: `/app/outputs/meso_derivation.log`

### Step 2: Derive macroscopic free-energy density and magnetization
- Role: process
- Action: Implement the macroscopic continuum theory using symbolic algebra: define the local anisotropy director, write the free-energy density with uniaxial magnetic terms and general magnetostrictive couplings (unknown parameters α∥, α⊥, ζ1, ζ3, ζ4, ζ6), integrate over the cylindrical volume, and expand up to linear order in A and τ to obtain the macroscopic energy and magnetization components. Log the expressions.
- Evidence: `/app/outputs/macro_derivation.log`

### Step 3: Scale-bridging: equate mesoscopic and macroscopic expressions
- Role: process
- Action: Compare the mesoscopic and macroscopic energy and magnetization expansions term-by-term (parts independent of A,τ, linear in A, and linear in τ) using symbolic algebra. Solve the resulting linear system for the six macroscopic parameters α∥, α⊥, ζ1, ζ3, ζ4, ζ6 as functions of the mesoscopic model parameters. Log the obtained closed-form expressions.
- Evidence: `/app/outputs/scale_bridging.log`

### Step 4: Compute and output deformation amplitudes and macroscopic parameters vs initial twist
- Role: scored (load-bearing)
- Action: Using the derived analytic formulas, numerically evaluate A, τ, α∥, α⊥, ζ1, ζ3, ζ4, ζ6 for the fixed mesoscopic parameters (a=85e-6 m, χ=13.1, h0=300e-6 m, ρ0=1.5e-3 m, n=10^10/(2π) m^-3, μ=1 Pa, R=2e-3 m) at q0h0 values evenly spaced from -2 to 2 (at least 50 points). Write the results as a CSV file `predicted_results.csv` with columns: q0h0, A, tau, alpha_parallel, alpha_perp, zeta1, zeta3, zeta4, zeta6.
- Output file: `/app/outputs/predicted_results.csv`
- Format: csv
- Contract: Columns: q0h0 (float), A (float), tau (float), alpha_parallel (float), alpha_perp (float), zeta1 (float), zeta3 (float), zeta4 (float), zeta6 (float). One row per q0h0 value, covering at least 50 equally spaced points from -2 to 2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_results.csv
- path: `/app/outputs/predicted_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed deformation amplitudes A and τ, and macroscopic parameters α∥, α⊥, ζ1, ζ3, ζ4, ζ6 as functions of scaled initial twist q0h0. The checker recomputes each quantity from known analytical formulas and compares within appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `q0h0`, `A`, `tau`, `alpha_parallel`, `alpha_perp`, `zeta1`, `zeta3`, `zeta4`, `zeta6`
  - `column_types`:
    - `q0h0`: float
    - `A`: float
    - `tau`: float
    - `alpha_parallel`: float
    - `alpha_perp`: float
    - `zeta1`: float
    - `zeta3`: float
    - `zeta4`: float
    - `zeta6`: float

Notes: The agent must symbolically derive all required expressions before the final numerical evaluation. The scored CSV must be computed from those derivations and contain at least 50 q0h0 points.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q0h0",
          "A",
          "tau",
          "alpha_parallel",
          "alpha_perp",
          "zeta1",
          "zeta3",
          "zeta4",
          "zeta6"
        ],
        "column_types": {
          "q0h0": "float",
          "A": "float",
          "tau": "float",
          "alpha_parallel": "float",
          "alpha_perp": "float",
          "zeta1": "float",
          "zeta3": "float",
          "zeta4": "float",
          "zeta6": "float"
        }
      },
      "description": "Computed deformation amplitudes A and τ, and macroscopic parameters α∥, α⊥, ζ1, ζ3, ζ4, ζ6 as functions of scaled initial twist q0h0. The checker recomputes each quantity from known analytical formulas and compares within appropriate tolerances."
    }
  ],
  "notes": "The agent must symbolically derive all required expressions before the final numerical evaluation. The scored CSV must be computed from those derivations and contain at least 50 q0h0 points."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently evaluates each step's artifact and produces a combined reward. The verifier recomputes the expected values of A, τ, α∥, α⊥, ζ₁, ζ₃, ζ₄, ζ₆ from the known analytic formulas that follow from the mesoscopic model and scale‑bridging procedure (i.e., the same physical model you are required to implement). It compares your reported CSV against these recomputed values with appropriate tolerances. The reward is split evenly between the mesoscopic quantities (A, τ) and the macroscopic parameters (the six ζ/α quantities). Simply reporting a table of numbers is not sufficient — you must implement the full derivation pipeline and compute the values from your own derivations.
