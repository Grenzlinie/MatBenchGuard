# Stochastic Landau-Lifshitz-Gilbert Spin-Wave Stability and Correlation

## Problem background
The stochastic Landau-Lifshitz-Gilbert (LLG) equation describes the dynamics of magnetic moments in a ferromagnet. When a uniaxial anisotropy is present and the system is driven by a randomly fluctuating field with a finite correlation time, the interplay between deterministic Gilbert damping and stochastic multiplicative noise can produce nontrivial stability behaviour and correlation effects. This task derives, within a small-noise-correlation-time expansion, closed evolution equations for the mean spin‑wave amplitude and the spin‑spin correlation function. The stability of spin‑wave solutions depends on the Gilbert damping α, the noise strength D, and the noise correlation time τ. A key finding is the existence of a critical correlation time τ_c at which the deterministic and stochastic damping mechanisms compensate, yielding undamped oscillations. The numerical evaluation of the derived coefficients and the correlation function provides insight into these regimes.

## Approach
Implement the theory by first constructing the drift vector Ω and the multiplicative-noise coupling matrix Λ that describe the linearized LLG dynamics around the uniform magnetization. The system is parameterized by the constant magnetization component μ (set to 0.9) and the dimensionless Gilbert damping α. The noise is colored with correlation time τ and strength D. The effective field includes exchange and uniaxial anisotropy, leading to the following expressions (with the shorthand ξ = 1/(1+α²) and β=1 for the long-wavelength limit q=0):

Drift vector Ω (3‑component):
Ω₁ = ξ μ [ - (α μ ψ₁ + ψ₂) ]
Ω₂ = ξ μ [ ψ₁ - α μ ψ₂ ]
Ω₃ = 0

Coupling matrix Λ (3×3, entries are linear in ψ):
Λ₁₁ =   α μ ψ₃
Λ₁₂ =   ψ₃
Λ₁₃ = -(ψ₂ + α μ ψ₁)
Λ₂₁ = -ψ₃
Λ₂₂ =   α μ ψ₃
Λ₂₃ =  ψ₁ - α μ ψ₂
Λ₃₁ =  ψ₂
Λ₃₂ = -ψ₁
Λ₃₃ =  0

From these, the effective spin‑wave damping/frequency coefficients A₁, A₂, A₃ (determining the matrix G) are given explicitly by:
ξ = 1/(1 + α²)
A₁ = -D² τ (6 μ² α² - 1) ξ⁴ + 2 μ² α D τ ξ³ - D (μ² α² - 2) ξ² + μ² α ξ
A₂ = ½ μ α D² τ (11 - 3 μ² α²) ξ⁴ + μ D τ (μ² α² - 1) ξ³ + 3 μ D α ξ² - μ ξ
A₃ = + D² τ (3 μ² α² + 1) ξ⁴ - 4 μ² α D τ ξ³ + 2 D ξ²

The matrix G is then (index order 1,2,3):
    ( -A₁   A₂   0 )
G = ( -A₂  -A₁   0 )
    (  0    0   -A₃)

The critical correlation time τ_c at which the effective damping vanishes is:
τ_c = - [ μ² (α³ - D α² + α) + 2 D ] (1 + α²)²  /  [ 2 D μ² (α³ - 3 D α² + α) + D² ]
(If the denominator is zero or the result is negative, τ_c is set to NaN.)

For the correlation function C_{ij}(s) = ⟨ψ_i(t'+s) ψ_j(t')⟩ (in the stationary state), the evolution equation (derived from the small‑τ approximation) reads:
d C_{ij}(s) / ds = Σ_k G_{ik} C_{kj}(s) + D exp(-s/τ) Σ_{p,q} M_{ij,pq} C_{pq}(s),
where the 9×9 coupling matrix M_{ij,pq} is obtained from the linear expansion of Λ:
  Λ_{ik}(ψ) = Σ_p L_{ikp} ψ_p,   with L_{ikp} extracted from the matrix above,
  M_{ij,pq} = Σ_k L_{ikp} L_{jkq}.
Because the noise coupling matrix Λ is linear in ψ, this forms a closed system of linear ODEs for the nine components C_{ij}(s). The integration starts at s=0 with all C_{ij}(0) set to the same nonzero constant C₀ (for instance C₀ = 1.0).

## Reproduction target
Generate two scored artifacts: (1) a CSV file, stability_output.csv, containing the computed values of A₁, A₂, A₃ and τ_c on a grid of α ∈ [0, 2] and D ∈ [−2, 2] (at least 20×20 points) with fixed μ=0.9, τ=1; and (2) a CSV file, correlation_C12.csv, containing the time series of C₁₂(s) for s = 0, 0.1, …, 10, obtained by integrating the ODE for the parameter set μ=0.9, α=0.005, D=0.1, τ=1 with initial correlation C₀=1.0 for all ij components.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute spin‑wave damping/frequency coefficients and critical correlation time
- Role: scored
- Action: Compute the coefficients A₁, A₂, A₃ using the explicit formulas above. Use ξ = 1/(1+α²). For each (α,D) pair on a grid with α ∈ [0, 2] (at least 20 points) and D ∈ [−2, 2] (at least 20 points) and fixed μ=0.9, τ=1, evaluate A₁, A₂, A₃. Also compute τ_c from its formula; if denominator is zero or τ_c<0 set to NaN. Write the results to /app/outputs/stability_output.csv.
- Output file: `/app/outputs/stability_output.csv`
- Format: csv
- Contract: CSV with columns: alpha, D, A1, A2, A3, tau_c. Each row corresponds to one (α, D) point on the grid. tau_c can be NaN. All numeric values are floating-point.
- Scoring: scored by hidden verifier

### Step 2: Solve correlation function ODE for C₁₂(s)
- Role: scored
- Action: Form the G matrix from the previously computed A₁, A₂, A₃ for the parameters μ=0.9, α=0.005, D=0.1, τ=1. Extract the linear coupling tensor L from Λ (Λ_{ik}(ψ) = Σ_p L_{ikp} ψ_p) and construct the 9×9 matrix M with M_{ij,pq} = Σ_k L_{ikp} L_{jkq}. Assemble the ODE system for the 9 components C_{ij} as:
  d C_{ij} / ds = Σ_k G_{ik} C_{kj} + D e^{-s/τ} Σ_{p,q} M_{ij,pq} C_{pq}.
Set initial condition C_{ij}(0) = 1.0 for all i,j. Numerically integrate from s=0 to s=10 using a dense output at spacing 0.1 (or any method that yields values at s=0,0.1,…,10). Extract the component C₁₂(s) and write to /app/outputs/correlation_C12.csv.
- Output file: `/app/outputs/correlation_C12.csv`
- Format: csv
- Contract: CSV with columns: s, C12. s ranges from 0 to 10 in steps of 0.1. C12 is a floating‑point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stability_output.csv`
- `/app/outputs/correlation_C12.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stability_output.csv
- path: `/app/outputs/stability_output.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Table of spin-wave damping/frequency coefficients and critical correlation time computed from analytic formulas for given (alpha, D) grid.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `D`, `A1`, `A2`, `A3`, `tau_c`
  - `units`: object

### correlation_C12.csv
- path: `/app/outputs/correlation_C12.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time evolution of the spin-spin correlation component C₁₂(s) for s in [0,10] step 0.1, computed from the ODE.
- schema:
  - `type`: table
  - `required_columns`: `s`, `C12`
  - `units`: object

Notes: The checker recomputes the coefficients and ODE solution from the same formulas and compares point-wise with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stability_output.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "D",
          "A1",
          "A2",
          "A3",
          "tau_c"
        ],
        "units": {}
      },
      "description": "Table of spin-wave damping/frequency coefficients and critical correlation time computed from analytic formulas for given (alpha, D) grid."
    },
    {
      "file": "correlation_C12.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "s",
          "C12"
        ],
        "units": {}
      },
      "description": "Time evolution of the spin-spin correlation component C₁₂(s) for s in [0,10] step 0.1, computed from the ODE."
    }
  ],
  "notes": "The checker recomputes the coefficients and ODE solution from the same formulas and compares point-wise with tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden checker that independently implements the same analytic formulas and ODE solution. For stability_output.csv, the checker recomputes A1, A2, A3 and τ_c for each (α, D) pair and compares them to your values using appropriate numerical tolerances. For correlation_C12.csv, the checker recomputes the C₁₂(s) time series by solving the ODE system and compares your values at each s. Both artifacts contribute weight to the final score; simply providing the correct file structure without matching the expected values will not earn full credit. The checker does not require any network access and runs in a controlled environment.
