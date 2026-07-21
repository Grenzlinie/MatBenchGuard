# Computation of Electrostrictive Hemisphere Force Coefficient for a Microdroplet

## Problem background
When a micrometer-sized fluid droplet is illuminated by a short laser pulse, optical forces include electrostriction (ES) which acts as a compressive volume force in the interior, countering the disruptive surface force. Under transient conditions before elastic pressure buildup, the ES force on the front and rear hemispheres of a spherical droplet can be described by an analytic formula. This task computes the dimensionless hemisphere force coefficient Q^ES for the front hemisphere of a droplet under circularly polarized plane-wave illumination. The target is to determine Q^ES as a function of the droplet size parameter for a given refractive index, which is important for understanding ultrashort-pulse droplet dynamics.

## Mathematical definitions
All quantities are derived from spherical Mie theory for a circularly polarized incident plane wave, as formulated by Barton et al. (J. Appl. Phys. 66, 4594 (1989)). The droplet refractive index is n (here n=1.33 for water) and the size parameter α = 2πa/λ is the number of circumferences per wavelength at frequency ω, where a is the sphere radius and λ is the vacuum wavelength.

### Spherical Riccati–Bessel functions
The radial functions are defined from spherical Bessel functions:
- ψ₁(z) = z·j₁(z)
- ψ₁'(z) = j₁(z) + z·j₁'(z)
and similarly for the outgoing-wave function ξ₁(z) = ψ₁(z) − iχ₁(z) with χ₁(z) = −z·y₁(z) and its derivative.

### First-order internal Mie coefficients c₁ and d₁
For circularly polarised illumination the internal field coefficients of order n=1 are:

Let x = α (the external size parameter) and let ρ = x, ρₛ = n·x = nα.

- c₁ (TE mode, internal):
  numerator_c = n·[ ψ₁(ρ)·ψ₁'(ρₛ) − ψ₁'(ρ)·ψ₁(ρₛ) ]
  denominator_c = ξ₁(ρ)·ψ₁'(ρₛ) − ξ₁'(ρ)·ψ₁(ρₛ)
  c₁ = numerator_c / denominator_c

- d₁ (TM mode, internal):
  numerator_d = ψ₁'(ρ)·ψ₁(ρₛ) − ψ₁(ρ)·ψ₁'(ρₛ)
  denominator_d = ξ₁'(ρ)·ψ₁(ρₛ) − ξ₁(ρ)·ψ₁'(ρₛ)
  d₁ = n·numerator_d / denominator_d

(These correspond to the TE and TM internal coefficients cₙ and dₙ for n=1 in the Barton et al. formalism.)

### Radial integrals I₁, I₂, I₃
These integrals appear in the analytic formula for Q^ES and are evaluated at x = nα:
- I₁(x) = (2x⁴ − 2x² − 1 + cos(2x) + 2x·sin(2x)) / (8x⁴)   (Eq. 7b)
- I₂(x) = ½·[ γ − 1 − Ci(2x) + ln(2x) + x⁻²·(2x·cos x − sin x)·sin x ]   (Eq. 7c)
- I₃(x) = I₁(x) + I₂(x) − (x² − 3·sin²x + x·sin(2x)) / (2x²)   (Eq. 7d)

Here γ = 0.57721566490153286060651209 is Euler’s constant, and Ci(z) = −∫_{z}^{∞} cos(t)/t dt is the cosine integral.

### Electrostrictive hemisphere force coefficient Q^ES
The front-hemisphere electrostrictive force is Fₛ<^ES = π a² ε₀ E₀² Q^ES with

Q^ES = 2·(n²−1)·(n²+2)·{ |c₁|²·[4·I₁(nα) + I₂(nα)] + |d₁|²·I₃(nα) } / (8·α²)   (Eq. 7a)

## Approach
Implement the above definitions in Python using scipy and numpy. For each size parameter α compute the complex Mie coefficients c₁ and d₁, evaluate the radial integrals I₁, I₂, I₃, and finally combine them to obtain Q^ES. The whole pipeline must be self‑contained; no external data or pre‑trained models may be used.

## Reproduction target
Work for a water droplet (refractive index n = 1.33) at size parameters α = 2, 4, 6, 8, 10. Produce two CSV files under /app/outputs:

1. `mie_internal_data.csv` – intermediate evidence containing the Mie coefficients and radial integrals for each α.
2. `q_es_values.csv` – the final scored quantity with columns `alpha` and `Q_ES`, where Q_ES is the dimensionless electrostrictive hemisphere force coefficient for the front hemisphere (positive sign).

## Assets
- scipy: pip install scipy
- numpy: pip install numpy

## Workflow steps

### Step 1: Compute Mie internal coefficients and radial integrals
- Action: For each size parameter α in {2, 4, 6, 8, 10} and refractive index n=1.33, compute the complex coefficients c₁ and d₁ using the definitions above (spherical Riccati–Bessel functions, ψ₁, ξ₁). Evaluate the radial integrals I₁, I₂, I₃ at x = nα using the cosine integral (available from `scipy.special.sici`) and Euler’s constant. Save all intermediate results to `mie_internal_data.csv`.
- Evidence: `/app/outputs/mie_internal_data.csv`
- Format: csv with header `alpha,c1_real,c1_imag,d1_real,d1_imag,I1,I2,I3`

### Step 2: Compute electrostrictive force coefficient Q^ES
- Role: scored (load-bearing)
- Action: Read the intermediate data from `mie_internal_data.csv` (optional) or recompute the same quantities. For each α, compute Q^ES using the formula Eq. 7a and write the results to `q_es_values.csv`.
- Output file: `/app/outputs/q_es_values.csv`
- Format: csv
- Contract: Header: `alpha, Q_ES`. alpha: float, Q_ES: float (positive).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mie_internal_data.csv`
- `/app/outputs/q_es_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### q_es_values.csv
- path: `/app/outputs/q_es_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The computed electrostrictive hemisphere force coefficient Q^ES for the front hemisphere at specified size parameters. The hidden checker independently computes Q^ES from the analytic formulas and compares your reported value; it must match within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `Q_ES`
  - `units`:
    - `alpha`: dimensionless
    - `Q_ES`: dimensionless

### mie_internal_data.csv
- path: `/app/outputs/mie_internal_data.csv`
- format: csv
- purpose: evidence (intermediate)
- description: Mie internal coefficients and radial integrals that demonstrate the computation pipeline.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `c1_real`, `c1_imag`, `d1_real`, `d1_imag`, `I1`, `I2`, `I3`
  - `units`:
    - `alpha`: dimensionless
    - `c1_real`, `c1_imag`, `d1_real`, `d1_imag`: dimensionless
    - `I1`, `I2`, `I3`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "q_es_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": ["alpha", "Q_ES"],
        "units": {"alpha": "dimensionless", "Q_ES": "dimensionless"}
      },
      "description": "The computed electrostrictive hemisphere force coefficient Q^ES for the front hemisphere at specified size parameters. The hidden checker independently computes Q^ES from the analytic formulas and compares your reported value; it must match within a tolerance."
    },
    {
      "file": "mie_internal_data.csv",
      "format": "csv",
      "purpose": "evidence",
      "schema": {
        "type": "table",
        "required_columns": ["alpha", "c1_real", "c1_imag", "d1_real", "d1_imag", "I1", "I2", "I3"],
        "units": {
          "alpha": "dimensionless",
          "c1_real": "dimensionless", "c1_imag": "dimensionless",
          "d1_real": "dimensionless", "d1_imag": "dimensionless",
          "I1": "dimensionless", "I2": "dimensionless", "I3": "dimensionless"
        }
      },
      "description": "Mie internal coefficients and radial integrals that demonstrate the computation pipeline."
    }
  ]
}
```

## How you are scored
A hidden verifier independently computes the reference Q^ES values for the specified α values using the same analytic formulas (Eqs. 7a–7d together with the Mie coefficients) and compares them to your reported `Q_ES` column in `q_es_values.csv`. The scorer checks that each Q_ES is positive and matches the reference within a relative tolerance of 0.001 and absolute tolerance of 1e‑5. Your final reward is based on the number of correct α values.