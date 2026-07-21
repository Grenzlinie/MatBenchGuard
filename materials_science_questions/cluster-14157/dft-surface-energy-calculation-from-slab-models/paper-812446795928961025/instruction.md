# Surface Energy and Critical Charge of Alkali Metal Nanoparticles

## Problem background
Small metal particles have surface properties that depend on particle size. The surface energy and work function govern a range of phenomena in clusters and fine-dispersed media. In this task, we address the size-dependent surface energy of alkali metal nanoparticles and the maximum electric charge they can retain before they become unstable (Coulomb explosion). The goal is to compute the planar surface energy and its first-order curvature correction from a first-principles variational model, and to determine the critical charge for positively charged sodium particles.

## Approach
We use the jellium model and density-functional theory within the local-density approximation. The electron density is described by a trial function with a single variational parameter (the inverse surface-layer thickness b). The energy functional includes kinetic (local Thomas-Fermi plus first gradient correction), exchange-correlation, and Coulomb contributions. Expanding the surface energy in powers of the inverse particle radius yields expressions for the planar part σ⁰ and the curvature correction σ¹, each composed of several terms with known coefficients (provided in the instruction). The optimal b⁰ is obtained by minimizing σ⁰, and first-order corrections b¹, σ¹, and μ¹ follow from the variational condition and the expansion. For the critical charge, macroscopic electrodynamics gives a simple relation involving the ion work function; the required work function for sodium is provided as a numeric constant together with the energy‑unit conversion factor.

## Reproduction target
Compute the planar surface energy σ⁰ and the first-order curvature correction σ¹ for the alkali metals Cs, Rb, K, Na, Li using the DFT variational model. Determine whether σ¹ is positive. Also compute the critical charge Z* for positively charged sodium particles as a function of the ionic radius R, and report the Z* values for R from 5 to 30 a₀.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute surface energy coefficients σ⁰, σ¹ and μ¹ for alkali metals
- Role: scored
- Action: Implement the variational surface energy model: For each metal (Cs, Rb, K, Na, Li) use its bulk electron density n+ (in a.u.) given below:
  Cs: 1.33e-3, Rb: 1.67e-3, K: 1.95e-3, Na: 3.77e-3, Li: 6.92e-3.
  The planar surface energy σ⁰(b) is expressed as
  σ⁰ = C_q⁰ n₊ b⁻³ − C_t⁰ n₊^{5/3} b⁻¹ + C_ex⁰ n₊^{4/3} b⁻¹ + C_c⁰ n₊ b⁻¹ + C_g⁰ n₊ b,
  with zeroth-order coefficients (j=0):
  C_q⁰ = 3.768, C_t⁰ = 2.184, C_ex⁰ = 0.329, C_c⁰ = 0.008556, C_g⁰ = 6.94.
  The first-order curvature correction σ¹(b) has the same functional form (substitute j=1 coefficients) and is evaluated at b=b⁰:
  σ¹(b) = C_q¹ n₊ b⁻³ − C_t¹ n₊^{5/3} b⁻¹ + C_ex¹ n₊^{4/3} b⁻¹ + C_c¹ n₊ b⁻¹ + C_g¹ n₊ b,
  with first-order coefficients (j=1):
  C_q¹ = 0, C_t¹ = 0.824, C_ex¹ = 0.275, C_c¹ = 0.016210, C_g¹ = 14.1.
  Solve dσ⁰/db = 0 to obtain b⁰ (the biquadratic equation reduces to a quadratic in b²; take the positive root). Then compute b¹, the first-order perturbation of the optimal thickness, using the formula derived from the variational condition:
  b¹ = - (∂σ¹/∂b) / (∂²σ⁰/∂b²) evaluated at b = b⁰.
  Compute σ¹ by evaluating σ¹(b⁰).
  Compute the chemical potential correction μ¹ using:
  Δφ = 2π³ n₊ / (3 b⁰³),
  μ¹ = -Δφ (1/2 + b¹/b⁰) - 2 σ⁰ b⁰ / n₊ + (b⁰)² / 72.
  Output the results as a CSV with columns metal, n_plus, b0, b1, sigma0, sigma1, mu1.
- Output file: `/app/outputs/surface_energy_results.csv`
- Format: csv
- Contract: Columns: metal (string), n_plus (float, a.u.), b0 (float, a.u.), b1 (float, a.u.), sigma0 (float, a.u.), sigma1 (float, a.u.), mu1 (float, a.u.). One row per metal.
- Scoring: scored by hidden verifier

### Step 2: Compute critical charge Z* for positively charged sodium particles
- Role: scored
- Action: Using the ion work function for Na W+ = 3.7 eV, convert to atomic units by multiplying with the conversion factor **1 eV = 0.036749322 Hartree** (atomic units of energy). For ionic radii R from 5 to 30 a₀ in steps of 1 a₀, compute the critical charge Z* = W+ * R + 1/2, with W+ now in atomic units. Output a CSV with columns R and Z_star.
- Output file: `/app/outputs/critical_charge_Na.csv`
- Format: csv
- Contract: Columns: R (float, a.u.), Z_star (float, dimensionless). R from 5.0 to 30.0 in steps of 1.0. Z_star computed as (W+ in a.u.) * R + 0.5.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_energy_results.csv`
- `/app/outputs/critical_charge_Na.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_energy_results.csv
- path: `/app/outputs/surface_energy_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed planar surface energy σ⁰, first-order curvature correction σ¹, optimal surface-layer inverse thickness b⁰ and its first-order correction b¹, and chemical potential correction μ¹ for Cs, Rb, K, Na, Li (from the DFT variational model).
- schema:
  - `type`: table
  - `required_columns`: `metal`, `n_plus`, `b0`, `b1`, `sigma0`, `sigma1`, `mu1`
  - `units`:
    - `n_plus`: atomic units
    - `b0`: atomic units
    - `b1`: atomic units
    - `sigma0`: atomic units
    - `sigma1`: atomic units
    - `mu1`: atomic units

### critical_charge_Na.csv
- path: `/app/outputs/critical_charge_Na.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical charge Z* for a positively charged sodium particle as a function of ionic radius R, computed from macroscopic electrodynamics formula Z* = W+ R + 1/2 with W+ = 3.7 eV (converted to a.u. using 1 eV = 0.036749322 Hartree).
- schema:
  - `type`: table
  - `required_columns`: `R`, `Z_star`
  - `units`:
    - `R`: atomic units
    - `Z_star`: dimensionless

Notes: All values are in atomic units unless noted otherwise.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_energy_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "n_plus",
          "b0",
          "b1",
          "sigma0",
          "sigma1",
          "mu1"
        ],
        "units": {
          "n_plus": "atomic units",
          "b0": "atomic units",
          "b1": "atomic units",
          "sigma0": "atomic units",
          "sigma1": "atomic units",
          "mu1": "atomic units"
        }
      },
      "description": "Computed planar surface energy σ⁰, first-order curvature correction σ¹, optimal surface-layer inverse thickness b⁰ and its first-order correction b¹, and chemical potential correction μ¹ for Cs, Rb, K, Na, Li (from the DFT variational model)."
    },
    {
      "file": "critical_charge_Na.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "Z_star"
        ],
        "units": {
          "R": "atomic units",
          "Z_star": "dimensionless"
        }
      },
      "description": "Critical charge Z* for a positively charged sodium particle as a function of ionic radius R, computed from macroscopic electrodynamics formula Z* = W+ R + 1/2 with W+ = 3.7 eV (converted to a.u. using 1 eV = 0.036749322 Hartree)."
    }
  ],
  "notes": "All values are in atomic units unless noted otherwise."
}
```

## How you are scored
Each scored output file is checked by a hidden verifier. The verifier compares your computed σ⁰, σ¹, and μ¹ values for each metal against reference benchmarks, allowing for numerical differences that arise from implementation details. It separately checks that σ¹ > 0 for all five metals and that Z* increases monotonically with R. The output files are weighted and combined into a single reward score. Producing the correct numerical values is essential; the verifier does not consider qualitative statements alone.