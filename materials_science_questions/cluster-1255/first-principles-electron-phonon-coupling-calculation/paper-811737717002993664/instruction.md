# RPA calculation of spin-fluctuation spectral weight and quasiparticle spectral weight in a d-wave superconductor

## Problem background
Angle-resolved photoemission spectroscopy (ARPES) measurements on high-temperature superconductors, such as Bi-2212, typically show a sharp quasiparticle peak, a broad inelastic background, and—when the sample is cooled below the superconducting transition temperature Tc—a dip feature next to the main peak. The origin of this dip has been debated. This task implements a model in which the dip arises from the opening of a spin gap in the magnetic susceptibility. The model computes the momentum-integrated spin-fluctuation spectral weight D(E) and the total quasiparticle spectral weight A(k,E) that includes both an elastic coherent part and an incoherent background from spin-fluctuation emission and absorption. By evaluating D(E) and A(k,E) at temperatures above and below Tc, one can investigate whether a spin gap and a corresponding dip feature appear as a natural consequence of the superconducting state.

## Approach and key equations
The theoretical framework combines a tight-binding electronic band structure, a d-wave superconducting order parameter, and a random-phase approximation (RPA) treatment of the spin susceptibility. All equations below are taken from the paper's methods. The physical quantities are expressed in units of the nearest-neighbor hopping energy t. Temperatures are given in energy units (kB=1), and the superconducting critical temperature is taken as Tc = 0.05 t.

**Electronic band structure**
```
ξ_k = -2t [cos(k_x) + cos(k_y)] - 4t' cos(k_x) cos(k_y) - μ.
```
Here t is the nearest-neighbor hopping (energy scale), t' = -0.45 t, and the chemical potential μ = -1.75 t.

**d-wave order parameter**
```
Δ_k = Δ₀ [cos(k_x) - cos(k_y)] / 2,
```
with Δ₀ = 0.1 t.

**Electronic damping**
```
Γ = Γ₀ + Γ₁ (T/Tc)³,
```
where Γ₀ = 0.04 t and Γ₁ = 0.05 t. At T/Tc = 1.0, Γ = 0.09 t; at T/Tc = 0.3, Γ ≈ 0.04 t + 0.05 t × (0.3)³ ≈ 0.04 t + 0.00135 t = 0.04135 t (exact value to be used in calculations).

**Green’s function for the elastic channel**
The retarded Green’s function is
```
G(k,E) = (E + i Γ + ξ_k) / [(E + i Γ)² - ξ_k² - Δ_k²].
```
The imaginary part used in spectral weights is
```
Im G(k,E) = (1/π) Im{ (E + i Γ + ξ_k) / [(E + i Γ)² - ξ_k² - Δ_k²] }.
```
For numerical evaluation, one can also use the simpler form based on the Bogoliubov energies:
The bare spectral function for a single-particle state is
```
Im G(p,E) = (1/π) Γ / [(E - E_p)² + Γ²],
```
where the quasiparticle energy is
```
E_p = √(ξ_p² + Δ_p²).
```
The corresponding superconducting coherence factors are
```
u_p² = (1/2)[1 + ξ_p / E_p],
v_p² = (1/2)[1 - ξ_p / E_p].
```
(Note: In the Im χ⁰ expression below, the products of u and v appear as written in the paper.)

**Bare electronic spin susceptibility χ⁰(q,E)**
The imaginary part is
```
Im χ⁰(q,E) = ∫ d²p ∫_{-∞}^{+∞} dE' [f(E'+E) - f(E')]  * { ... },
```
where the integrand contains four terms involving combinations of u_p, v_p, u_{p+q}, v_{p+q} and the Green’s functions (see the full expression in the paper). In the continuum notation of the paper, equation (6) gives:
```
Im χ⁰(q,E) = Σ_p ∫ dE' [f(E'+E)-f(E')] * 
   { [u_{p+q}² u_p² + u_{p} v_{p} u_{p+q} v_{p+q}] Im G(p+q,E'+E) Im G(p,E')
   + [u_{p+q}² v_p² - u_{p} v_{p} u_{p+q} v_{p+q}] Im G(p+q,E'+E) Im G(p,-E')
   + [v_{p+q}² u_p² - u_{p} v_{p} u_{p+q} v_{p+q}] Im G(p+q,-E'-E) Im G(p,E')
   + [v_{p+q}² v_p² + u_{p} v_{p} u_{p+q} v_{p+q}] Im G(p+q,-E'-E) Im G(p,-E') }.
```
The momentum sum Σ_p runs over the first Brillouin zone (-π,π) in both directions; a discrete grid should be used. The frequency integral extends over a range wide enough to capture all spectral weight (e.g., from about -2t to 2t). The real part Re χ⁰(q,E) is obtained via the Kramers–Kronig transform:
```
Re χ⁰(q,E) = (1/π) P ∫_{-∞}^{+∞} dω Im χ⁰(q,ω) / (ω - E).
```

**RPA interacting susceptibility**
```
Im χ(q,E) = Im χ⁰(q,E) / { [1 - U Re χ⁰(q,E)]² + [U Im χ⁰(q,E)]² },
```
where the spin-fluctuation coupling constant is U = 1.0 t.

**Spin-fluctuation spectral weight D(E)**
```
D(E) = (1/(2π)²) ∫_{BZ} d²q (g/t)² Im χ(q,E).
```
Here g = U = 1.0 t, so (g/t)² = 1. The integral extends over the full two-dimensional Brillouin zone (-π to π in both qx, qy). The units of D(E) are such that D(E)·t is dimensionless.

**Quasiparticle spectral weight**
The elastic main peak is
```
A⁰(k,E) = -(1/π) Im G(k,E),
```
with G(k,E) from equation (2) of the paper evaluated at the given k-point.

The inelastic background is
```
A_inel(k,E) = -(1/π) ∫_{-∞}^{+∞} dE' Im G(k,E') * 
  { D(E-E') [ n(E-E') + f(-E') ] Θ(E-E')
    + D(E'-E) [ n(E'-E) + f(E') ] Θ(E'-E) },
```
where n(E) = 1/(exp(E/T)-1) is the Bose-Einstein distribution and f(E) = 1/(exp(E/T)+1) is the Fermi-Dirac distribution. Θ is the Heaviside step function. The factor α controls the relative weight.

The total quasiparticle spectral weight is
```
A(k,E) = A⁰(k,E) + α A_inel(k,E),
```
with α = 4.0.

**Temperature definitions**
We work with energy units in which kB = 1. The critical temperature is taken as Tc = 0.05 t. Thus:
- At T/Tc = 1.0: T = 0.05 t.
- At T/Tc = 0.3: T = 0.015 t.

**Numerical implementation notes**
- Momentum grids for p and q can be taken as uniform meshes (e.g., 100×100) covering [-π,π]×[-π,π]. The integration over the Brillouin zone for D(E) uses the same q-grid.
- The energy integral in eq. (3) should be truncated at large enough energies (e.g., [-1.0, 1.0] in units of t) and discretized with a step much smaller than Γ.
- The Kramers–Kronig transform can be performed using a direct integration over a grid of ω with a small shift to avoid the pole, or via Hilbert transform routines.

## Reproduction target
Produce the following scored artifacts as CSV files:

- D_E.csv: Momentum-integrated spin-fluctuation spectral weight D(E)·t on a grid of energies from 0 to 0.5t with a step no larger than 0.01t. The file must contain three columns: energy (in units of t), D_E_T1 (value at T/Tc=1.0), and D_E_T2 (value at T/Tc=0.3).
- A_k_E.csv: Total quasiparticle spectral weight A(k,E)·t at the Fermi surface point k=(π,0.1624), on an energy grid from -0.2t to 0.4t with a step no larger than 0.01t. The file must contain three columns: energy (in units of t), A_T1 (value at T/Tc=1.0), and A_T2 (value at T/Tc=0.3).

All input model parameters are fixed: tight‑binding with t' = -0.45t, chemical potential μ = -1.75t; d-wave gap amplitude Δ₀ = 0.1t; electronic damping Γ = Γ₀ + Γ₁(T/Tc)³ with Γ₀ = 0.04t, Γ₁ = 0.05t; spin-fluctuation coupling constant g = U = 1.0t; inelastic/elastic mixing factor α = 4.0; critical temperature Tc = 0.05 t (energy units). The equations and parameter values given above must be used exactly.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute bare and RPA spin susceptibility
- Role: process
- Action: Using the tight-binding band, d-wave gap, damping, and coherence factors, compute Im χ⁰(q,E) via equation (6) by summing over momentum p and integrating over E' with the Fermi functions at the appropriate temperature. Then obtain Re χ⁰(q,E) from Kramers–Kronig, and construct the RPA susceptibility Im χ(q,E) with U=1.0t. Perform this for both T/Tc = 1.0 and 0.3.
- Evidence: none

### Step 2: Spin-fluctuation spectral weight D(E)
- Role: scored (load-bearing)
- Action: Compute D(E) by integrating (U/t)² Im χ(q,E) over the full Brillouin zone using equation (4). Compute for temperatures T/Tc=1.0 and 0.3. Output the curves as D_E.csv with columns: energy, D_E_T1, D_E_T2. Energy range 0 to 0.5t, step ≤0.01t.
- Output file: `/app/outputs/D_E.csv`
- Format: csv
- Contract: CSV with columns: energy (float, energy in units of t), D_E_T1 (float, D(E)·t at T/Tc=1.0), D_E_T2 (float, D(E)·t at T/Tc=0.3). Energy range [0, 0.5t], step ≤0.01t.
- Scoring: scored by hidden verifier

### Step 3: Elastic spectral weight A⁰(k,E)
- Role: process
- Action: Compute A⁰(k,E) = -(1/π) Im G(k,E) using the Green’s function from equation (2) with the tight-binding band, d-wave gap, and damping, at the Fermi surface point k=(π,0.1624). Compute for both temperatures.
- Evidence: none

### Step 4: Inelastic spectral weight A_inel(k,E)
- Role: process
- Action: Compute A_inel(k,E) using the convolution integral (equation (3) of the paper) with Im G(k,E) and the previously obtained D(E). Use the correct occupation factors (Fermi and Bose) for each temperature, the step functions, and the scale factor α=4.0. Implement numerical integration over E' with sufficient range.
- Evidence: none

### Step 5: Quasiparticle spectral weight A(k,E)
- Role: scored (load-bearing)
- Action: Combine elastic and inelastic contributions as A(k,E)=A⁰(k,E)+α A_inel(k,E). Output the curves as A_k_E.csv with columns: energy, A_T1, A_T2. Energy range -0.2t to 0.4t, step ≤0.01t.
- Output file: `/app/outputs/A_k_E.csv`
- Format: csv
- Contract: CSV with columns: energy (float, energy in units of t), A_T1 (float, A(k,E)·t at T/Tc=1.0), A_T2 (float, A(k,E)·t at T/Tc=0.3). Energy range [-0.2t, 0.4t], step ≤0.01t.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/D_E.csv`
- `/app/outputs/A_k_E.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### D_E.csv
- path: `/app/outputs/D_E.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Momentum-integrated spin-fluctuation spectral weight D(E)·t, for two temperatures. The structural audit evaluates whether the curve shapes are physically plausible according to the model, without requiring exact numerical references.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `D_E_T1`, `D_E_T2`
  - `units`:
    - `energy`: t (nearest-neighbor hopping energy unit)
    - `D_E_T1`: dimensionless (D(E)·t)
    - `D_E_T2`: dimensionless (D(E)·t)

### A_k_E.csv
- path: `/app/outputs/A_k_E.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total quasiparticle spectral weight A(k,E)·t, at k=(π,0.1624) on the Fermi surface, for two temperatures. The structural audit evaluates whether the curve shapes are physically plausible according to the model, without requiring exact numerical references.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `A_T1`, `A_T2`
  - `units`:
    - `energy`: t (nearest-neighbor hopping energy unit)
    - `A_T1`: dimensionless (A(k,E)·t)
    - `A_T2`: dimensionless (A(k,E)·t)

Notes: The model parameters are fixed as given in the approach. The structural audit does not require exact numerical agreement, only the qualitative physical characteristics described in the model.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "D_E.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "D_E_T1",
          "D_E_T2"
        ],
        "units": {
          "energy": "t (nearest-neighbor hopping energy unit)",
          "D_E_T1": "dimensionless (D(E)*t)",
          "D_E_T2": "dimensionless (D(E)*t)"
        }
      },
      "description": "Momentum-integrated spin-fluctuation spectral weight D(E) multiplied by t, for two temperatures. The structural audit evaluates whether the curve shapes are physically plausible according to the model, without requiring exact numerical references."
    },
    {
      "file": "A_k_E.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "A_T1",
          "A_T2"
        ],
        "units": {
          "energy": "t (nearest-neighbor hopping energy unit)",
          "A_T1": "dimensionless (A(k,E)*t)",
          "A_T2": "dimensionless (A(k,E)*t)"
        }
      },
      "description": "Total quasiparticle spectral weight A(k,E) multiplied by t, at k=(π,0.1624) on the Fermi surface, for two temperatures. The structural audit evaluates whether the curve shapes are physically plausible according to the model, without requiring exact numerical references."
    }
  ],
  "notes": "The model parameters are fixed: tight-binding with t'=-0.45t, μ=-1.75t, d-wave gap Δ0=0.1t, damping Γ0=0.04t, Γ1=0.05t, coupling U=1.0t, α=4.0, and the k-point is (π,0.1624). All equations are as given in the paper's methods; energies are in units of t. The structural audit does not require exact numerical agreement, only the qualitative physical characteristics described in the model."
}
```

## How you are scored
A hidden automatic verifier will read your submitted D_E.csv and A_k_E.csv. It will first validate that both files follow the declared format (correct columns, energy ranges, no missing values). It will then analyze the physical content of the curves through a series of structural checks that do not require matching specific numerical reference values from the literature. The verifier will evaluate whether the computed curves exhibit the qualitative physical characteristics predicted by the model (e.g., signatures of superconductivity, changes between normal and superconducting states). The analysis uses techniques such as local extrema detection, monotonicity testing, and comparison of the two temperature curves. The final reward is a weighted combination of the scores from the two artifacts, with D_E.csv and A_k_E.csv each carrying substantial weight. To obtain a high score, your implementation must faithfully execute the physical model described in the approach and produce numerically well‑resolved output files.