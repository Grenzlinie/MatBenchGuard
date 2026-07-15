# Compute size-dependent superconducting gap in FeSe/STO nanoislands

## Problem background
Superconductivity in single-unit-cell FeSe on a SrTiO₃ (STO) substrate is strongly enhanced relative to bulk FeSe, likely due to coupling to interface phonons. Recent STM experiments on FeSe/STO nanoislands have revealed that the superconducting gap depends sensitively on the island’s size. This work develops a theoretical model to describe that size dependence. The model combines Eliashberg theory of superconductivity in the weak-coupling limit, forward-scattering-dominated pairing, and semiclassical periodic orbit theory to obtain an analytical expression for the superconducting gap as a function of the island's dimensions. Your task is to implement that analytical prediction and compute the gap for rectangular nanoislands across a range of areas and aspect ratios.

## Approach
The model assumes phonon-mediated pairing in the weak-coupling regime with strong forward scattering, described by the Eliashberg equations with a sharp momentum cutoff of width ε₀. In the bulk limit this yields a closed-form expression for the bulk gap Δ₀ in terms of the electron-phonon coupling λ, the Debye energy ω_D, and the cutoff energy ε₀.

Quantum size effects enter through fluctuations of the spectral density. These are treated by a semiclassical expansion of the density of states for a rectangular billiard using periodic orbit theory. The leading-order finite-size correction, f₁/₂, arises from two-dimensional periodic orbits (n,m) with lengths Lₙ = 2√(Lₓ² n² + L_y² m²) and is weighted by the zeroth-order Bessel function J₀(k_F Lₙ) and a sinc cutoff. The next-to-leading-order correction, f₁, includes a Weyl term (negative sign for Dirichlet boundary conditions), contributions from one-dimensional periodic orbits involving cos(k_F Lₙⁱ) and a sinc factor, and a quadratic term in f₁/₂.

The total gap is written as Δ(L) = Δ₀ (1 + f₁/₂ + f₁). You will evaluate it for rectangular islands of side lengths Lₓ = α L, L_y = L/α, with L ≡ √(L²), for the aspect ratios α = 1.2 and α = 1.4, using the fixed physical parameters λ = 0.22, ε₀ = 4 meV, k_F = 2.06 nm⁻¹, ω_D = 100 meV, ε_F = 60 meV. The infinite sums are truncated when the sinc factor becomes negligible.

## Reproduction target
Implement the analytical expressions described above and compute the superconducting gap Δ(L) (in meV) for rectangular FeSe/STO nanoislands. Sweep the area L² from 25 nm² to 400 nm² in steps of 1 nm², for each of the two aspect ratios α = 1.2 and α = 1.4. Output a CSV file with three columns: area_nm2 (the area in nm²), aspect_ratio (the aspect ratio), and gap_meV (the computed gap in meV).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute Δ(L) from analytical expressions
- Role: scored (load-bearing)
- Action: For rectangular FeSe/STO nanoislands with Dirichlet boundary conditions, compute the superconducting gap Δ(L) using the paper's analytical formulas. The bulk gap Δ₀ is obtained from a closed-form expression involving the electron-phonon coupling constant λ, Debye energy ω_D, and cutoff energy ε₀. The leading finite-size correction f₁/₂ is a sum over periodic orbits of lengths Lₙ = 2√(L_x² n² + L_y² m²) for integer pairs (n,m) with (n,m)≠(0,0), weighted by J₀(k_F Lₙ) and a sinc cutoff factor. The next-to-leading correction f₁ includes a Weyl term (negative sign for Dirichlet), sums over single-integer periodic orbits involving cos(k_F Lₙⁱ) and sinc, and a quadratic term in f₁/₂. Use the constants: λ=0.22, ε₀=4 meV, k_F=2.06 nm⁻¹, ω_D=100 meV, ε_F=60 meV. For each area L² from 25 nm² to 400 nm² (step 1 nm²) and for aspect ratios α=1.2 and α=1.4, set L_x = α L, L_y = L/α where L = √(L²). Compute Δ(L) = Δ₀ (1 + f₁/₂ + f₁). Truncate the infinite sums when the sinc factor becomes negligible.
- Output file: `/app/outputs/delta_vs_area.csv`
- Format: csv
- Contract: area_nm2 (float), aspect_ratio (float), gap_meV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_vs_area.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_vs_area.csv
- path: `/app/outputs/delta_vs_area.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed superconducting gap Δ(L) for rectangular FeSe/STO nanoislands. Each row gives the area, aspect ratio, and gap value.
- schema:
  - `type`: table
  - `required_columns`: `area_nm2`, `aspect_ratio`, `gap_meV`
  - `columns`:
    - `area_nm2`:
      - `type`: float
    - `aspect_ratio`:
      - `type`: float
    - `gap_meV`:
      - `type`: float
  - `units`:
    - `area_nm2`: nm^2
    - `aspect_ratio`: dimensionless
    - `gap_meV`: meV

Notes: All physical parameters are fixed as given; the output is deterministic. The checker will compare the submitted gap values to recomputed gold values with a hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_vs_area.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "area_nm2",
          "aspect_ratio",
          "gap_meV"
        ],
        "columns": {
          "area_nm2": {
            "type": "float"
          },
          "aspect_ratio": {
            "type": "float"
          },
          "gap_meV": {
            "type": "float"
          }
        },
        "units": {
          "area_nm2": "nm^2",
          "aspect_ratio": "dimensionless",
          "gap_meV": "meV"
        }
      },
      "description": "Computed superconducting gap Δ(L) for rectangular FeSe/STO nanoislands. Each row gives the area, aspect ratio, and gap value."
    }
  ],
  "notes": "All physical parameters are fixed as given; the output is deterministic. The checker will compare the submitted gap values to recomputed gold values with a hidden tolerance."
}
```

## How you are scored
Your submitted CSV will be evaluated by a hidden verifier. The verifier recomputes the superconducting gap for a set of hidden area values (different from the sweep range you are asked to compute) using the same analytical formulas and physical parameters. For each hidden test point, it compares your reported gap_meV to the recomputed value within a tolerance that accounts for numerical truncation differences. The reward is proportional to the fraction of test points where the absolute error falls within that tolerance. The verifier also checks that the CSV contains the required columns covering all the area–aspect-ratio combinations described in the task. Reporting numbers without actually computing them will not satisfy the verifier.
