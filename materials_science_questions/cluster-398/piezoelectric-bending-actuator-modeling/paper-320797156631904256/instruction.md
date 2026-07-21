# Electro-mechanical coupling effects on shock and crack fronts in piezoelectric crystals

## Problem background
In piezoelectric crystals that possess mobile charged defects (e.g., vacancies) and conduction via diffusion, the interaction of defect charge with externally applied mechanical stress fields can produce a measurable electric current – the barocurrent. This coupling occurs through two mechanisms: dilatational (volume‑change) coupling, where stress gradients alter the local chemical potential of defects, and the direct piezoelectric effect, where stress generates an internal electric field that acts on the defects. The resulting redistribution of charge leads to surface charge densities and dipole moments on propagating shock wave fronts, on the tip of a moving crack, and gives an additional contribution to the absorption of transverse sound waves. This task asks you to compute these physically observable quantities for a concrete cubic piezoelectric material of T or T_d symmetry containing a single mobile defect species, using the analytical formulas and the set of material and geometric parameters provided below.

## Approach
Starting from linear non‑equilibrium thermodynamics, the defect fluxes are expressed in terms of concentration gradients, the electrostatic potential, and the gradient of the stress tensor. Poisson’s equation is modified to include a piezoelectric source term proportional to the divergence of the piezoelectric tensor contracted with the stress. The joint system of continuity equations for the defect concentration and Poisson’s equation is linearised and Fourier‑transformed. For the simplified case of a cubic crystal (isotropic dielectric constant, isotropic diffusion and dilatation tensors) with one mobile charge carrier on a static, electrically neutral background, the problem reduces to a single linear differential equation in Fourier space. Closed‑form solutions are then obtained for three canonical stress fields:

- a planar shock wave modelled as a step‑function stress front;
- a steadily moving crack under mode I (opening) and mode II (in‑plane shear);
- a monochromatic transverse sound wave.

You must implement the following analytical expressions. The same set of parameters applies to all cases unless noted otherwise.

### Parameters (common)
- σ0 = 1.0e8 Pa — shock wave stress amplitude (σ0 = -3ΔP, where ΔP is the pressure jump).
- ε = 10 ε₀ (ε₀ = 8.854187817e-12 F/m) — dielectric permittivity.
- q = 1.602176634e-19 C — defect charge (elementary charge).
- Ω = 1.0e-29 m³ — defect dilation volume.
- γ = 1.0e-12 C/N — piezoelectric constant (value of the non-zero components of the cubic piezoelectric tensor: γ_{x,yz}=γ_{y,zx}=γ_{z,xy}=γ; all others zero).
- a_D = 1.0e-7 m — Debye screening length (a_D² = ε k_B T / (4π q² n), where n is the defect concentration, but a_D is given directly as a parameter).
- λ = 1.0e3 — dimensionless parameter λ = (characteristic velocity)×a_D / D; for the crack and sound calculations, λ is treated as a given constant.
- ν = 0.9 — dimensionless crack speed (v = V/c, where c is the limiting speed).
- δ = 1.0e-6 m — crack‑tip opening.
- Γ_s = 1.0e3 a_D — regularisation length for the crack stress expansion.
- K_I = 1.0e6 Pa·m^{1/2} — mode‑I stress‑intensity factor (taken as the dynamic value K_I(ν)).
- K_II = 1.0e6 Pa·m^{1/2} — mode‑II stress‑intensity factor.
- n — unit vector along the crack propagation direction / shock wave normal: [111] direction, i.e., vector (1,1,1)/√3.
- m — unit vector normal to the crack plane: [1  -1  0] direction, i.e., vector (1,-1,0)/√2.
- For the sound‑absorption calculation you additionally need:
    ω = 1.0e6 rad/s — angular frequency of the sound wave.
    τ_σ = 1.0e-3 s — conductivity‑related time constant.
    ρ = 5.0e3 kg/m³ — mass density.
    c_t = 3.0e3 m/s — transverse sound speed.
    Elastic constants of the cubic crystal (in Pa): C₁₁ = 1.2e11, C₁₂ = 0.6e11, C_{44} = 0.6e11.
    Polarisation vector e of the transverse wave: [1  -1  0]/√2 (orthogonal to n).

### 1. Shock wave front
Surface charge density Q and dipole moment D (per unit area) on a planar shock front that propagates with constant speed along n. The analytical formulas are:

Q_shock_dilat   = σ0 * (ε * Ω) / (12 * π * q)
Q_shock_piezo   = σ0 * (n^λ γ_{λ,μν} n^μ n^ν)
Q_shock_total   = Q_shock_dilat + Q_shock_piezo

D_shock_dilat   = σ0 * (ε * Ω) / (12 * π * q)
D_shock_piezo   = σ0 * λ * a_D * (n^λ γ_{λ,μν} n^μ n^ν)
D_shock_total   = D_shock_dilat + D_shock_piezo

where the triple contraction n^λ γ_{λ,μν} n^μ n^ν is computed with the cubic piezoelectric tensor using the given γ and the vector n.

### 2. Moving crack front
Linear charge density Q and dipole moment components D₁, D₂ (per unit length along the crack front) for a crack moving with speed ν. The dilatational contributions (superscript (d)) and piezoelectric contributions (superscript (p)) are evaluated separately, and totals are formed as indicated.

Define the quantity 
  Λ1 = (a_D λ)^{1/2} ν^{1/2} / (2 √(2π) √(1‑ν²)).

#### Mode I (opening)
- Q_I^(d) = (ε Ω/(4π q)) * [3 ν² K_I / (5 √(1‑ν²) √(2π δ)) ] * {1 + (5/24) ν^{1/2} √(λ δ a_D) / Γ_s}
- D1_I^(d) = (ε Ω/(4π q)) * [3 ν² K_I λ a_D / (5 √(1‑ν²) √(2π δ)) ] * {ν + (5/21) ν^{3/2} √(λ δ a_D) / Γ_s - (50/21) δ/(λ a_D)}
- Q_I^(p) = γ₀^I * a_D * √(a_D λ) * ν^{1/2} * K_I / ( √(1‑ν²) * 2 √(2π) )
- D1_I^(p) = (γ₀^I + γ₁^I) * (a_D λ)^{3/2} * ν^{3/2} * K_I / ( √(1‑ν²) * 2 √(2π) )
- D2_I^(p) = γ₂^I * (a_D λ)^{3/2} * ν^{3/2} * K_I / ( (1‑ν²) * 2 √(2π) )

Q_I_total = Q_I^(d) + Q_I^(p), similarly for D1, D2.

#### Mode II (in‑plane shear)
The formulas are identical to those for mode I except:
- K_I is replaced by -K_II,
- the coefficients γ_j^I are replaced by γ_j^II (j = 0,1,2).

Q_II_total = Q_II^(p)  (there is no dilatational contribution)
D1_II_total = D1_II^(d)  (no piezoelectric contribution)
D2_II_total = D2_II^(d) + D2_II^(p)

#### Coefficients γ₀, γ₁, γ₂ for modes I and II
These are computed from the crack geometry vectors n, m and the tabulated constants A–F according to

γ_j = γ_{λ,μν} { n^λ n^μ n^ν A_j + n^λ m^μ m^ν B_j + m^λ n^μ m^ν C_j + √(1‑ν²)[ m^λ n^μ n^ν D_j + m^λ m^μ m^ν E_j + n^λ n^μ m^ν F_j ] }.

The constants A–F are given in the table below (same for mode I and II; the superscript I/II distinguishes the different numerical values that must be used).

| j | mode |   A   |   B   |   C   |   D   |   E   |   F   |
|---|---|---|---|---|---|---|---|
| 0 |  I  |  8/21 |  -2   | -8/21 |   0   |   0   |   0   |
| 0 | II  |   0   |   0   |   0   |  6/7  | 8/21  | 8/21  |
| 1 |  I  | -8/15 | -12/15|  8/15 |   0   |   0   |   0   |
| 1 | II  |   0   |   0   |   0   | -44/15| -8/15 | -8/15 |
| 2 |  I  |   0   |   0   |   0   | -16/15| -8/15 |-16/15 |
| 2 | II  | 16/15 | -8/15 |-16/15 |   0   |   0   |   0   |

### 3. Transverse sound absorption coefficient
Additional absorption coefficient γ^t (in m⁻¹) due to the barocurrent for a transverse wave of polarisation e, wave‑vector direction n, frequency ω:

 γ_t = 2 ω² τ_σ | n^λ γ_{λ,μν} Λ^{μν;αβ} n_α e_β |²  /  ( ρ c_t³ ω² τ_σ² + (1 + ω² τ_σ²/λ²)² ).

The fourth‑rank elastic stiffness tensor Λ for a cubic crystal has non‑zero components:
  Λ^{xxxx}=Λ^{yyyy}=Λ^{zzzz} = C₁₁,
  Λ^{xxyy}=Λ^{xxzz}=… = C₁₂,
  Λ^{xyxy}=Λ^{xzxz}=Λ^{yzyz} = C_{44},
with all other components zero. Use standard tensor contraction to evaluate the numerator.

## Reproduction target
Using the formulas and the concrete parameter set listed above, compute all of the following quantities (each as a float) and write them into a CSV file at `/app/outputs/results.csv` with columns `quantity`, `value`, `unit`. The required rows and their units are:

- Q_shock_dilat (C/m²)
- Q_shock_piezo (C/m²)
- Q_shock_total (C/m²)
- D_shock_dilat (C/m)
- D_shock_piezo (C/m)
- D_shock_total (C/m)
- Q_I_dilat (C/m)
- Q_I_piezo (C/m)
- Q_I_total (C/m)
- D1_I_dilat (C/m)
- D1_I_piezo (C/m)
- D1_I_total (C/m)
- D2_I_piezo (C/m)
- D2_I_total (C/m)
- Q_II_piezo (C/m)
- Q_II_total (C/m)
- D1_II_dilat (C/m)
- D1_II_total (C/m)
- D2_II_dilat (C/m)
- D2_II_piezo (C/m)
- D2_II_total (C/m)
- gamma_t (m⁻¹)

Your implementation must evaluate the analytical expressions exactly as given and write the numeric results with full double‑precision accuracy. The verifier will check each value against independently computed reference numbers.

## Assets

- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Compute all target quantities
- Role: scored (load-bearing)
- Action: Implement the closed-form analytical expressions for surface charge density and dipole moment on a shock wave front, for linear charge density and dipole moment components on a moving crack front (modes I and II), and for the transverse sound absorption coefficient, using a provided set of material parameters and directional vectors. Write all computed quantities to a CSV file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: quantity (string), value (float), unit (string). Rows must include: Q_shock_dilat, Q_shock_piezo, Q_shock_total, D_shock_dilat, D_shock_piezo, D_shock_total, Q_I_dilat, Q_I_piezo, Q_I_total, D1_I_dilat, D1_I_piezo, D1_I_total, D2_I_piezo, D2_I_total, Q_II_piezo, Q_II_total, D1_II_dilat, D1_II_total, D2_II_dilat, D2_II_piezo, D2_II_total, gamma_t (unit: m⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file containing computed physical quantities: surface charge densities, dipole moments, and sound absorption coefficient. The checker recomputes each value from the same analytical formulas and parameters and compares within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `quantity`, `value`, `unit`
  - `units`: object

Notes: All quantities are deterministic; the checker uses the same parameter set to recompute and compares each row’s value against a hidden gold value with a relative tolerance of 1e-6. Reward is proportional to the fraction of rows meeting tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "quantity",
          "value",
          "unit"
        ],
        "units": {}
      },
      "description": "CSV file containing computed physical quantities: surface charge densities, dipole moments, and sound absorption coefficient. The checker recomputes each value from the same analytical formulas and parameters and compares within a relative tolerance."
    }
  ],
  "notes": "All quantities are deterministic; the checker uses the same parameter set to recompute and compares each row’s value against a hidden gold value with a relative tolerance of 1e-6. Reward is proportional to the fraction of rows meeting tolerance."
}
```

## How you are scored
A hidden verifier will recompute every quantity listed above using the identical formulas and the identical parameter set. It compares each row’s `value` against its own reference value with a predefined relative numerical tolerance. The total reward is proportional to the fraction of rows that satisfy the tolerance; a row that does not match receives zero credit for that row. Reporting numbers that are not actually computed from a correct implementation of the provided analytical expressions will not lead to a passing score, even if some rows coincidentally fall within tolerance. There is no partial credit: only rows that match within tolerance contribute to the reward.
