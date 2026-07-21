# Compute size-dependent superconducting gap in FeSe/STO nanoislands

## Problem background
Superconductivity in single-unit-cell FeSe on a SrTiO₃ (STO) substrate is strongly enhanced relative to bulk FeSe, likely due to coupling to interface phonons. Recent STM experiments on FeSe/STO nanoislands have revealed that the superconducting gap depends sensitively on the island’s size. This work develops a theoretical model to describe that size dependence. The model combines Eliashberg theory of superconductivity in the weak-coupling limit, forward-scattering-dominated pairing, and semiclassical periodic orbit theory to obtain an analytical expression for the superconducting gap as a function of the island's dimensions. Your task is to implement that analytical prediction and compute the gap for rectangular nanoislands across a range of areas and aspect ratios.

## Theory and formulas

### Bulk gap Δ₀
The model assumes phonon-mediated pairing with strong forward scattering and a sharp momentum cutoff of width ε₀. After solving the Eliashberg equations in the weak-coupling limit, the bulk gap Δ₀ is given by

```
Δ₀ = ε₀ / sinh[ (1/λ + 3/2) ε₀ / ω_D ]
```

where λ is the electron-phonon coupling constant, ω_D is the Debye energy, and ε₀ is the cutoff energy. All energies are in meV.

### Finite-size corrections
Quantum size effects are incorporated through a semiclassical expansion of the density of states for a rectangular billiard with Dirichlet boundary conditions. The superconducting gap for a rectangular island of side lengths L_x and L_y is

```
Δ(L) = Δ₀ ( 1 + f_{1/2} + f₁ )
```

The two correction terms are defined as follows.

#### Leading-order correction f_{1/2}
```
f_{1/2} = ( 1 − 3Δ₀/(2 ω_D) )  ∑_{(n,m)≠(0,0)}  J₀(k_F L_{nm})  sinc( L_{nm} / ξ )
```

- The sum runs over integer pairs (n,m) with n,m ≥ 0, excluding (0,0).
- L_{nm} = 2 √( (L_x n)² + (L_y m)² ) is the length of the two-dimensional periodic orbit labelled by (n,m).
- J₀ is the zeroth-order Bessel function of the first kind.
- k_F is the Fermi wave vector (nm⁻¹).
- sinc(x) = sin(x)/x with sinc(0)=1.
- ξ = 2 ε_F / ( k_F ε₀ ) is a coherence length that controls the cutoff of periodic-orbit contributions.

#### Next-to-leading-order correction f₁
```
f₁ = − ( 1 − 3Δ₀/(2 ω_D) ) [ W + S ]  −  ( 3Δ₀/(2 ω_D) )  ( f_{1/2} )²
```

The terms W (Weyl term) and S (one-dimensional periodic orbit sum) are:

- **Weyl term** (Dirichlet boundary conditions):  
  `W = (L_x + L_y) / ( k_F A )`  
  where A = L_x L_y is the area of the island.

- **One-dimensional periodic orbit sum**:  
  `S = Σ_{i ∈ {x,y}}  (2 L_i / (k_F A))  Σ_{n=1}^{∞} cos(k_F L_n^i) sinc( L_n^i / ξ )`  
  with L_n^i = 2 n L_i  (i = x or y).

### Truncation of infinite sums
All infinite sums over periodic orbits should be truncated when the argument of the sinc function, L / ξ, becomes larger than a threshold where the contribution is negligible. A natural choice is to truncate when L / ξ > 50 (or any similarly large value where sin(x)/x is numerically indistinguishable from zero for the required precision).

### Parameter values
Use the following fixed physical constants:
- λ = 0.22
- ε₀ = 4 meV
- k_F = 2.06 nm⁻¹
- ω_D = 100 meV
- ε_F = 60 meV

### Geometry
The rectangular islands have side lengths
```
L_x = α L,   L_y = L / α,   L = √(area)
```
where `area` is the island area in nm². Compute the gap for the two aspect ratios α = 1.2 and α = 1.4.

## Reproduction target
Implement the analytical expressions described above and compute the superconducting gap Δ(L) (in meV) for rectangular FeSe/STO nanoislands. Sweep the area `L²` from 25 nm² to 400 nm² in steps of 1 nm², for each of the two aspect ratios α = 1.2 and α = 1.4. Output a CSV file with three columns: `area_nm2` (the area in nm²), `aspect_ratio` (the aspect ratio), and `gap_meV` (the computed gap in meV).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute Δ(L) from analytical expressions
- Role: scored (load-bearing)
- Action: For rectangular FeSe/STO nanoislands with Dirichlet boundary conditions, compute the superconducting gap Δ(L) using the formulas in the "Theory and formulas" section. First compute the bulk gap Δ₀ from the closed-form expression. Then for each area and aspect ratio, compute L_x and L_y, the coherence length ξ, and evaluate f_{1/2} and f₁ by summing over periodic orbits as defined. Finally, compute Δ(L) = Δ₀ (1 + f_{1/2} + f₁). Truncate the infinite sums using the threshold described above.
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