# Effective Critical Exponents from SCOZA PDE for Lattice Gas

## Problem background
The critical point of a three-dimensional lattice gas exhibits singular thermodynamic behavior described by critical exponents. The self-consistent Ornstein-Zernike approximation (SCOZA) is a liquid-state theory that yields a nonlinear partial differential equation for the inverse compressibility parameter ε as a function of inverse temperature β and density ρ. Numerical solution of this equation through the critical point and into the two-phase region is challenging because the spinodal curve ε=0 acts as a moving boundary where the equation becomes singular. The effective critical exponents derived from the solution determine how thermodynamic quantities such as susceptibility, isotherm slope, specific heat, and coexistence density scale with reduced temperature near the critical point. When the inverse range of the pair interaction γ_r is varied, the effective exponents can change. This task computes the effective exponents γ, δ, α, β, γ′, and α′ from the SCOZA PDE, using a simplified internal-energy kernel that captures the essential dependence on the interaction range.

## Approach
The SCOZA PDE is solved numerically with a predictor-corrector integration scheme in β, starting from the analytic mean-spherical approximation (MSA) initial condition at high temperature. The internal energy contribution from correlations is approximated by the simplified form F(z)=½ γ_r³ (1-ε), which embeds the inverse interaction range γ_r and has the correct singular behavior as ε→0. The integration is performed on a dense density grid from 0 to the critical density ρ_c. For each γ_r³ value in a prescribed set covering two orders of magnitude, the integration is carried through the critical point and into the two-phase region. The spinodal (ε=0) is located, and the coexistence densities are determined by the equal-pressure construction. From the solutions, the pressure, susceptibility, internal energy, and specific heat are derived. Effective critical exponents are then computed as logarithmic derivatives of the appropriate thermodynamic quantities with respect to reduced temperature t. The supercritical exponents (γ, δ, α) use t = 1−T_c/T; the subcritical exponents (β, γ′, α′) use t = 1−T/T_c. For one representative interaction range (γ_r³=0.34), a scaled equation of state is constructed using variables x = Δρ / t^β and y = Δp / t^{βδ} with β=0.38 and δ=5, for a set of super- and sub-critical isotherms.

## Reproduction target
For each γ_r³ in the set {10⁻³, 10⁻², 0.1, 0.2, 0.3, 0.34, 0.4, 0.5, 0.6, 0.7, 0.8}, compute the effective critical exponents γ, δ, α, β, γ′, α′ as functions of reduced temperature t over the interval t ∈ [10⁻⁴, 10⁰] with at least 20 points per decade, and write the results to a TSV file. For γ_r³ = 0.34 only, additionally compute the scaled equation-of-state data (t, x, y, temperature_type) over t ∈ [10⁻⁴, 10⁻¹] and write a second TSV file. The exact column specifications and output paths are listed in the workflow steps and output contract below.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Numerical integration of SCOZA PDE
- Role: process
- Action: Implement the SCOZA PDE (thermodynamic self-consistency relation) with the simplified internal-energy kernel F(z)=½ γ_r³ (1-ε). Use a predictor–corrector integration scheme in β (inverse temperature), starting from the MSA initial condition at high temperature. Discretise density over [0, ρ_c] with a dense grid (up to 10⁴ points). For each inverse-range parameter γ_r³ in {10⁻³, 10⁻², 0.1, 0.2, 0.3, 0.34, 0.4, 0.5, 0.6, 0.7, 0.8}, run the integration through the critical point and below T_c. Determine the spinodal (ε=0) and coexistence densities by equal‑pressure construction. Compute the susceptibility, pressure, internal energy, and specific heat. Store the raw fields ε(β,ρ) and derived thermodynamic functions for later exponent extraction.
- Evidence: `/app/outputs/scoza_simulation.log`

### Step 2: Compute effective critical exponents
- Role: scored (load-bearing)
- Action: From the SCOZA solutions (ε, pressure, internal energy) compute effective critical exponents γ, δ, α, β, γ′, α′ as logarithmic derivatives. For each γ_r³ and each exponent, sample t = 1−T_c/T (supercritical) or t = 1−T/T_c (subcritical) over t ∈ [10⁻⁴, 10⁰] with at least 20 points per decade. Write a TSV file with the results.
- Output file: `/app/outputs/step_01_effective_exponents.tsv`
- Format: tsv
- Contract: Columns: gamma_r3 (float), t (float), exponent_type (string, one of gamma, delta, alpha, beta, gamma_prime, alpha_prime), exponent_value (float). Sorted by gamma_r3, exponent_type, t.
- Scoring: scored by hidden verifier

### Step 3: Scaled equation of state
- Role: scored
- Action: For γ_r³ = 0.34 only, use the computed pressures and densities to form scaled variables x = Δρ / t^β and y = Δp / t^{δβ} using the effective critical exponents β and δ you determined from the analysis in Step 2. Generate points for several super‑ and sub‑critical isotherms covering t ∈ [10⁻⁴, 10⁻¹]. Write a TSV file with columns t, x, y, temperature_type.
- Output file: `/app/outputs/step_02_scaled_eos.tsv`
- Format: tsv
- Contract: Columns: t (float), x (float), y (float), temperature_type (string, either supercritical or subcritical).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_effective_exponents.tsv`
- `/app/outputs/step_02_scaled_eos.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_effective_exponents.tsv
- path: `/app/outputs/step_01_effective_exponents.tsv`
- format: tsv
- purpose: scored
- target_policy: metric_recompute
- description: Effective critical exponents for each interaction range and reduced temperature; main scored artifact.
- schema:
  - `columns`: `gamma_r3`, `t`, `exponent_type`, `exponent_value`
  - `types`:
    - `gamma_r3`: float
    - `t`: float
    - `exponent_type`: string (one of gamma, delta, alpha, beta, gamma_prime, alpha_prime)
    - `exponent_value`: float
  - `sorting`: gamma_r3, exponent_type, t

### step_02_scaled_eos.tsv
- path: `/app/outputs/step_02_scaled_eos.tsv`
- format: tsv
- purpose: scored
- target_policy: metric_recompute
- description: Scaled equation-of-state data for γ_r³=0.34.
- schema:
  - `columns`: `t`, `x`, `y`, `temperature_type`
  - `types`:
    - `t`: float
    - `x`: float
    - `y`: float
    - `temperature_type`: string (supercritical or subcritical)

Notes: The verifier recomputes logarithmic derivative metrics on effective_exponents.tsv and checks the scaling slope (δ) on scaled_eos.tsv against a hidden reference. The instruction now requires the agent to determine β and δ from Step 2, eliminating the explicit gold leak.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_effective_exponents.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          "gamma_r3",
          "t",
          "exponent_type",
          "exponent_value"
        ],
        "types": {
          "gamma_r3": "float",
          "t": "float",
          "exponent_type": "string (one of gamma, delta, alpha, beta, gamma_prime, alpha_prime)",
          "exponent_value": "float"
        },
        "sorting": "gamma_r3, exponent_type, t"
      },
      "description": "Effective critical exponents for each interaction range and reduced temperature; main scored artifact."
    },
    {
      "file": "step_02_scaled_eos.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          "t",
          "x",
          "y",
          "temperature_type"
        ],
        "types": {
          "t": "float",
          "x": "float",
          "y": "float",
          "temperature_type": "string (supercritical or subcritical)"
        }
      },
      "description": "Scaled equation-of-state data for γ_r³=0.34."
    }
  ],
  "notes": "The verifier recomputes logarithmic derivative metrics on effective_exponents.tsv and checks the scaling slope (δ) on scaled_eos.tsv against a hidden reference. The instruction now requires the agent to determine β and δ from Step 2, eliminating the explicit gold leak."
}
```

## How you are scored
A hidden verifier independently scores each output artifact. For the effective exponents file, it compares the reported exponent values for selected (γ_r³, t, exponent_type) points to reference values computed from the original study, with tolerances that account for numerical discretization and integration scheme differences. For the scaled equation-of-state file, a subset of isotherms is checked against reference curves. The two artifacts carry different weights; the final reward is a weighted combination of their scores. Simply reporting a plausible value without actually running the SCOZA simulation will not score well, because the verifier uses conditions and tolerances that require a genuine computation.
