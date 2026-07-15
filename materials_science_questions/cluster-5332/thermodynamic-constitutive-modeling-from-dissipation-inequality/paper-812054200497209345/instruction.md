# Strain Profiles for Gradient Elastic-Plastic Bar with Higher-Order Boundary Conditions

## Problem background
Strain‑gradient theories for elastic‑plastic materials introduce higher‑order (HO) boundary conditions that govern strain distributions near surfaces and material discontinuities. In a one‑dimensional bar, these conditions can be interpreted as the action of an idealized rigid substrate that imposes kinematic constraints (setting the strain to zero at the boundary) or static constraints (setting the strain gradient to zero). When the bar contains a discontinuity in material moduli at x=0, the resulting strain profiles display characteristic exponential decay with internal lengths that depend on the gradient coefficients. Reproducing the elastic (εᵉ) and plastic (εᵖ) strain profiles for a piecewise‑homogeneous bar demonstrates how these HO boundary conditions emerge from the limiting behaviour of the adjacent material.

## Approach
The bar is treated as infinite with a jump in moduli at x=0. The material in x<0 has (E₂, M₂, H₂, J₂); in x>0 it has (E₁, M₁, H₁, J₁). The bar is subjected to a remote uniaxial stress σ > σ_y (yield stress), and no unloading occurs, so a deformation‑theory‑like formulation applies. Equilibrium gives σ=const. Everywhere; the yield condition is σ − χ = σ_y with χ the drag stress. The governing ODEs are:

σ = E εᵉ − M εᵉ'''',    χ = H εᵖ − J εᵖ''''

where primes denote derivatives with respect to x. The internal length scales are ℓ = √(M/E) and ℓ_p = √(J/H).

The analytic solution for the general case (finite moduli on both sides) is:

**For x ≥ 0:**
εᵉ = (σ / E₁) · [1 − Ω_e ℓ₂ e^(−x/ℓ₁)]
εᵖ = (σ − σ_y) / H₁ · [1 − Ω_p ℓ₂^p e^(−x/ℓ₁^p)]

**For x ≤ 0:**
εᵉ = (σ / E₂) · [1 + Ω_e ℓ₁ e^(x/ℓ₂)]
εᵖ = (σ − σ_y) / H₂ · [1 + Ω_p ℓ₁^p e^(x/ℓ₂^p)]

where
ℓ₁ = √(M₁/E₁),   ℓ₂ = √(M₂/E₂),   ℓ₁^p = √(J₁/H₁),   ℓ₂^p = √(J₂/H₂),
Ω_e = (E₂ − E₁) / (E₁ ℓ₁ + E₂ ℓ₂),   Ω_p = (H₂ − H₁) / (H₁ ℓ₁^p + H₂ ℓ₂^p).

The usual HO boundary conditions (decay at infinity, continuity of strain and of the double tractions M εᵉ' and J εᵖ' at x=0) are automatically satisfied by these expressions.

The three limit cases correspond to making the left half (x<0) rigid in different ways:

- **case1 – rigid gradient substrate** (E₂→∞, H₂→∞, M₂,J₂ finite): the left half becomes elastically and plastically rigid while keeping gradient character, enforcing εᵉ(0)=εᵖ(0)=0. The solutions for x≥0 then become:
  εᵉ = (σ / E₁) (1 − e^(−x/ℓ₁)),
  εᵖ = (σ − σ_y) / H₁ (1 − e^(−x/ℓ₁^p)).
  For x<0, εᵉ = εᵖ = 0.

- **case2 – rigid local substrate** (E₂,H₂→∞, M₂=J₂=0): the left half becomes rigid and local, enforcing εᵉ'(0)=εᵖ'(0)=0. The solutions for x>0 are uniform:
  εᵉ = σ / E₁,   εᵖ = (σ − σ_y) / H₁.
  For x<0, εᵉ = εᵖ = 0.

- **case3 – mixed local‑elastic + gradient‑plastic substrate** (E₂,H₂→∞, M₂=0, J₂ finite): the left half is local in elasticity and gradient in plasticity, enforcing εᵉ'(0)=0 and εᵖ(0)=0. For x>0:
  εᵉ = σ / E₁,
  εᵖ = (σ − σ_y) / H₁ (1 − e^(−x/ℓ₁^p)).
  For x<0, εᵉ = εᵖ = 0.

The task uses a specific parameter set that produces meaningful profiles:

E₁ = 200e9 Pa,   M₁ = 1e‑6 Pa·m²,   H₁ = 20e9 Pa,   J₁ = 1e‑6 Pa·m²,
E₂ = 100e9 Pa,   M₂ = 5e‑7 Pa·m²,   H₂ = 10e9 Pa,   J₂ = 5e‑7 Pa·m²,
σ = 300e6 Pa,   σ_y = 250e6 Pa.

For the limit cases the above formulas for the right half should be used; the precise values of E₂,H₂,M₂,J₂ in those formulas are not needed because the simplified expressions hold exactly.

## Reproduction target
Produce a single CSV file `strain_profiles.csv` with columns: case, x, epsilon_e, epsilon_p. The column `case` must be one of 'general', 'case1', 'case2', 'case3'. For each case sample x uniformly over the interval [−5·max(ℓ₁,ℓ₁^p), +5·max(ℓ₁,ℓ₁^p)] with at least 500 equally spaced points, compute the elastic and plastic strains using the exact analytic expressions given in the Approach section. The CSV should contain all points from all cases, each row identifying the corresponding case.

## Assets

- Python packages (numpy, scipy, pandas): numpy scipy pandas

## Workflow steps

### Step 1: Compute strain profiles for the 1D gradient bar
- Role: scored (load-bearing)
- Action: Implement the analytic closed-form expressions for elastic strain ε^e(x) and plastic strain ε^p(x) for the general discontinuous-moduli case and the three limit cases (rigid gradient substrate, rigid local substrate, mixed local-elastic + gradient-plastic substrate) using the provided material parameters (E1, M1, H1, J1, E2, M2, H2, J2, applied stress σ, yield stress σ_y). Evaluate the functions on a uniform x-grid spanning from -5*max(ℓ1, ℓ1^p) to +5*max(ℓ1, ℓ1^p) with at least 500 points per case. Assemble a CSV file with columns: case, x, epsilon_e, epsilon_p.
- Output file: `/app/outputs/strain_profiles.csv`
- Format: csv
- Contract: CSV file with columns: case (string, one of 'general', 'case1', 'case2', 'case3'), x (float, coordinate in meters), epsilon_e (float, elastic strain), epsilon_p (float, plastic strain). Each case must contain at least 500 sampled points equally spaced over the x range.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/strain_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### strain_profiles.csv
- path: `/app/outputs/strain_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Strain profiles for the four cases. The checker recomputes the exact analytic profiles and checks element-wise relative tolerance and HO boundary condition satisfaction.
- schema:
  - `type`: table
  - `required_columns`: `case`, `x`, `epsilon_e`, `epsilon_p`
  - `columns`:
    - `case`: string, one of 'general', 'case1', 'case2', 'case3'
    - `x`: float, coordinate in meters
    - `epsilon_e`: float, elastic strain
    - `epsilon_p`: float, plastic strain
  - `units`: object

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "strain_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "x",
          "epsilon_e",
          "epsilon_p"
        ],
        "columns": {
          "case": "string, one of 'general', 'case1', 'case2', 'case3'",
          "x": "float, coordinate in meters",
          "epsilon_e": "float, elastic strain",
          "epsilon_p": "float, plastic strain"
        },
        "units": {}
      },
      "description": "Strain profiles for the four cases. The checker recomputes the exact analytic profiles and checks element-wise relative tolerance and HO boundary condition satisfaction."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently recomputes the exact strain profiles for the same material parameters and the same x‑grid using the same analytic formulas. It then compares your submitted CSV element‑wise (per case, per x) with those recomputed profiles within a demanding relative tolerance. Additionally, the verifier checks satisfaction of the HO boundary conditions at x=0: for case1 it verifies that εᵉ(0) and εᵖ(0) are sufficiently close to zero; for case2 it evaluates numerical derivatives near x=0 and checks that εᵉ'(0) and εᵖ'(0) are near zero; for case3 it checks that εᵉ'(0) and εᵖ(0) are near zero. Your reward is proportional to the fraction of points that pass the element‑wise tolerance and the degree to which the boundary conditions are met. Simply reporting a number from the paper is not sufficient – the entire strain profiles must be accurate.
