# Temperature-dependent properties of V3Si from a microscopic two-band tight-binding model

## Problem background
A-15 intermetallic compounds such as V3Si display a structural martensitic transition from a cubic to a tetragonal phase at low temperature. This transition is accompanied by strongly temperature-dependent anomalies in the shear elastic modulus, magnetic susceptibility, and electronic specific heat. A successful microscopic model must explain all these phenomena from the underlying electronic band structure. Here we implement a three-dimensional two-band tight-binding model based on the transition-metal δ1 orbitals that captures both Peierls-like and Jahn-Teller effects, with the goal of computing the temperature variation of the key observables.

## Model specification

### 1. Tight-binding Hamiltonian
The electronic structure is described by a 6×6 tight-binding matrix H(k, Δ) in the Bloch basis
{|X1⟩, |X2⟩, |Y1⟩, |Y2⟩, |Z1⟩, |Z2⟩}, where |α1⟩ and |α2⟩ are the two δ1 (x²−y²) orbitals on the
transition-metal chain oriented along α (α = x, y, z). The lattice constant is set to unity, so
the Brillouin zone is k = (k_x, k_y, k_z) ∈ [−π, π]³.

The Hamiltonian matrix elements (in eV) are:

**Intra‑chain (diagonal blocks)**
For each chain α, the 2×2 block is
```
H_α(k,Δ) = |  0                                2 β (1 − g Δ_α) cos(k_α/2)  |
           |  2 β (1 − g Δ_α) cos(k_α/2)       0                              |
```
where the collective distortion coordinate Δ is distributed on the three chains according to:
```
Δ_x = Δ,    Δ_y = −Δ/2,    Δ_z = −Δ/2 .
```

**Inter‑chain (off‑diagonal blocks)**
Only nearest‑neighbour chain‑chain couplings are retained, all with a single hopping γ (real).
For the block connecting chain X with chain Y:
```
H_{X1,Y1} = γ
H_{X1,Y2} = γ e^{i k_y/2}
H_{X2,Y1} = γ e^{−i k_x/2}
H_{X2,Y2} = γ e^{i (k_y − k_x)/2}
```
with the Hermitian‑conjugate elements implied. The blocks (X,Z) and (Y,Z) are obtained by
cyclically permuting the indices (x,y,z) in the above expressions.

**Parameter values for V₃Si Case I**
```
α = 0 (not used),   β = −0.165 eV,   γ = 0.014 eV,   g = 3.8 Å⁻¹.
```
The parameter g is a coupling constant that converts the distortion Δ (a dimensionless strain)
into a change of the inter‑atomic distance: the effective hopping on chain α is
β_eff(α) = β (1 − g d_α) where d_α is the bond‑length change on that chain.  Because the lattice
constant a₀ ≈ 4.72 Å for V₃Si, a strain Δ produces a distance change d_α = a₀ Δ_α, so the
product g d_α is dimensionless and the Hamiltonian only depends on the parameters above.

For a given (k, Δ), diagonalise the 6×6 matrix H(k, Δ).  The two lowest eigenvalues
Eⁿ(k, Δ) (n = 1, 2) constitute the two relevant bands that dominate the density of states
near the Fermi level.

### 2. Electron number
The system contains one formula unit (V₃Si) per unit cell.  The two low‑lying bands can each
accommodate one electron per spin, so the maximum filling is 2 electrons per cell per spin.
We set the total electron number per unit cell (both spins) to
```
N_cell = 2   (one electron in each of the two bands when counted per spin).
```
This fills the first band completely at zero temperature and places the Fermi level near the
density‑of‑states peak, exactly where the model is designed to work.

### 3. Density of states
The density of states (DOS) N(E, Δ) and its first two energy derivatives N'(E, Δ), N''(E, Δ)
are computed from the band energies on a uniform k‑mesh using the Gilat–Raubenheimer
linear‑interpolation scheme, which is essential for obtaining accurate, smooth DOS curves
from a moderate number of k‑points. The method proceeds as follows:

- **Mesh subdivision** – The irreducible wedge of the Brillouin zone is covered by a uniform grid of small cubes (or rectangular parallelepipeds) with side lengths Δk_x, Δk_y, Δk_z.
- **Energy and gradient at cube centres** – For each small cube centered at k_c, evaluate the band energies Eⁿ(k_c, Δ) and approximate the energy gradient ∇_k Eⁿ(k_c, Δ) using finite differences (e.g. central differences with step ~Δk/10).
- **Linear expansion** – Inside the cube, the band energy is approximated by
  E(k) ≈ E_c + G·(k − k_c),
  where G = ∇_k E(k_c) and E_c = E(k_c).
- **Constant‑energy surface intersection** – For a target energy E, the plane E = E_c + G·(k − k_c) cuts the cube. The intersection is a convex polygon whose vertices lie on the cube edges. The area A_c(E) of this polygon is computed analytically.
- **DOS contribution** – The contribution from one band and one cube to the density of states (per spin, per unit cell) at energy E is
  ΔN(E) = (1/ (2π)³) · A_c(E) / |G|,
  if the plane intersects the cube; otherwise ΔN(E) = 0.
- **Summation** – Sum the contributions over all bands and all cubes to obtain N(E, Δ).
- **Derivatives** – The energy derivatives N'(E, Δ) and N''(E, Δ) can be obtained by numerical differentiation of N(E, Δ) on a fine energy grid or by extending the Gilat‑Raubenheimer formulas to higher order (see the paper’s appendix).

A mesh that resolves the sharp DOS structures is necessary; **a k‑mesh of at least 100³ points in the full Brillouin zone** (or an equivalent density in the irreducible wedge) is recommended.

### 4. Thermodynamic potential and chemical potential
The electronic grand potential per unit cell is
```
Ω_el(Δ, μ, T) = −k_B T  Σ_{n=1,2}  ∫_BZ (dk/(2π)³)  ln[ 1 + exp(−(Eⁿ(k,Δ)−μ)/k_B T) ],
```
and the total free energy (Landau potential) is
```
F(Δ, T) = min_μ { Ω_el(Δ, μ, T) + μ N_cell } + ½ K Δ² ,
```
where the elastic term ½ K Δ² accounts for the bare lattice stiffness.

The chemical potential μ(Δ, T) is determined by the electron‑number constraint:
```
−∂Ω_el/∂μ = N_cell .
```
For each temperature we minimise F(Δ, T) with respect to the distortion Δ; the minimiser
Δ_eq(T) is the equilibrium distortion.

The bare elastic constant K is **not** a fixed input; the model must determine it by requiring
that the martensitic transition temperature T_m matches the experimental value for V₃Si,
which is **T_m,exp = 21 K** (as reported in the paper, e.g. T_m ∼ 21 K for V₃Si).
A practical self‑consistent procedure:
1. Choose an initial guess for K.
2. For a dense set of temperatures 0 K … 50 K (step ≤ 0.5 K), compute the equilibrium Δ_eq(T).
3. Identify the temperature where Δ_eq(T) first becomes zero (or the free‑energy crossover); this is the model’s T_m(K).
4. Adjust K (e.g. by bisection or root‑finding) until |T_m(K) − 21 K| < 0.5 K.
5. Use the converged K for all subsequent property calculations.

Low‑temperature series expansions are recommended for the integration over the bulk of the
Brillouin zone, while a fine quadrature (adaptive grid) should be used in the flat regions
near the Fermi energy.

### 5. Tetragonal distortion
For the cubic‑to‑tetragonal transition, the lattice constants are related to Δ by
```
c = a₀ (1 + Δ),    a = a₀ (1 − Δ/2),
```
where a₀ is the cubic lattice constant.  The observable tetragonal distortion is then
```
ε(T) = |c/a − 1| = | (1+Δ)/(1−Δ/2) − 1 |.
```
In the small‑Δ regime (Δ ≪ 1) this simplifies to ε ≈ (3/2) Δ, but the exact expression must be
used for numerical accuracy.

### 6. Magnetic susceptibility
The total magnetic susceptibility χ(T) consists of a temperature‑dependent electronic part and
a constant background:
```
χ(T) [emu/g] = χ_bkg + χ_el(T).
```
The electronic contribution is given by
```
χ_el(T) = ( N_A μ_B² / (M k_B) ) × 2 ∫_−∞^∞ N(E, Δ_eq(T)) ( −∂f(E−μ(T))/∂E ) dE,
```
where
* N_A = 6.02214076 × 10²³ mol⁻¹ (Avogadro’s number),
* μ_B = 9.27400915 × 10⁻²¹ emu (Bohr magneton in CGS‑emu),
* M = 180.91 g mol⁻¹ (molar mass of V₃Si),
* k_B = 8.617333262 × 10⁻⁵ eV K⁻¹ (Boltzmann constant),
* N(E, Δ) is the band DOS per eV per unit cell per spin (i.e. the DOS summed over the two bands
  but **without** the spin factor of 2, which is included explicitly in the formula),
* f(E − μ) = 1/(1 + exp((E−μ)/k_B T)) is the Fermi–Dirac distribution,
* −∂f/∂E is its energy derivative.

The constant background χ_bkg is an adjustable parameter chosen so that the high‑temperature
(normal‑state) susceptibility matches the absolute level observed in experiment.  For V₃Si
a typical value is χ_bkg ≈ (1 − 3) × 10⁻⁴ emu/g; the final number should be determined self‑
consistently from the fit.  The electron‑phonon enhancement factor (1+λ) is set to 1 for V₃Si,
as it is already absorbed in the effective parameters β, γ, g and in the background.

### 7. Electronic specific heat
The electronic contribution to the specific heat (per mole) is obtained from the temperature
derivative of the electronic entropy:
```
C_el(T) [J/(mol·K)] = N_A × dU_el/dT,
U_el(T) = Σ_{n=1,2} ∫_BZ (dk/(2π)³)  Eⁿ(k, Δ_eq(T))  f( Eⁿ(k, Δ_eq(T)) − μ(T) ).

```
Equivalently, one may first compute the entropy per cell
```
S_el(T) = −k_B Σ_{n=1,2} ∫_BZ (dk/(2π)³) [ f_n ln f_n + (1−f_n) ln(1−f_n) ]
```
and then C_el(T) = N_A × T × dS_el/dT.  Both routes give the same result.  The conversion
factor to J/mol is 1 eV = 1.602176634 × 10⁻¹⁹ J.

No lattice (phonon) contribution is added; the model only addresses the electronic part, which
dominates the anomaly near the transition.

### 8. Overall workflow
The computation proceeds in four stages:

1. **Tight‑binding solver** – For a grid of k‑points and a range of Δ values, build H(k, Δ) and
   diagonalise it to obtain the two lowest bands Eⁿ(k, Δ).  Store the band energies on a fine
   grid for later interpolation.
2. **DOS calculation** – Use the Gilat–Raubenheimer linear interpolation described above to
   generate N(E, Δ), N'(E, Δ), and N''(E, Δ) on a dense energy mesh.  Save the DOS tables.
3. **Equilibrium thermodynamics** – Iteratively adjust the bare elastic constant K so that
   T_m matches the experimental transition temperature for V₃Si (**21 K**).  For each temperature
   in the range 0 K … 50 K solve the electron‑number constraint to obtain μ(Δ, T) and then
   minimise the free energy to find Δ_eq(T).  Record the converged K, Δ_eq(T), μ(T), and the
   temperature steps.
4. **Observable curves** – From Δ_eq(T) compute ε(T) using the relation above.  Evaluate χ(T)
   with the susceptibility formula, adjusting χ_bkg to match the high‑temperature data.
   Compute C(T) from the entropy derivative.  Save the four columns to the CSV file.

The agent is free to store intermediate results in temporary files under `/app/outputs`,
but the only scored outputs are the final CSV and JSON files listed below.

## Reproduction target
Using the tight‑binding model and the self‑consistently determined elastic constant K, produce
the temperature‑dependent curves and key scalar quantities for V₃Si Case I. Output a CSV file
(`step_01_thermodynamic_curves.csv`) with columns `T` (K), `epsilon` (dimensionless),
`chi` (emu/g), and `C` (J/mol·K), covering at least 20 temperatures from 0 to 50 K, densely
sampled near the transition. Also output a JSON file (`step_02_derived_values.json`) containing
the zero‑temperature tetragonal distortion `epsilon_0` (dimensionless), the martensitic
transition temperature `Tm` (K), the slope of the magnetic susceptibility at Tm
`dchi_dT_at_Tm` (in units of 10⁻⁶ emu/g·K), and the specific heat jump `Delta_Cv` (J/mol·K).

## Assets
- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermodynamic_curves.csv`
- `/app/outputs/step_02_derived_values.json`

## Output contract
Every file the hidden verifier reads is described below. Write each file under `/app/outputs`
and follow its schema exactly.

### step_01_thermodynamic_curves.csv
- path: `/app/outputs/step_01_thermodynamic_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature‑dependent tetragonal distortion ε(T), magnetic susceptibility χ(T) and electronic specific heat C(T) computed from the tight‑binding model. The checker compares these curves against hidden reference curves using tolerance bands.
- schema:
  - `type`: table
  - `required_columns`: ["T", "epsilon", "chi", "C"]
  - `units`:
    - `T`: K
    - `epsilon`: dimensionless
    - `chi`: emu/g
    - `C`: J/mol·K

### step_02_derived_values.json
- path: `/app/outputs/step_02_derived_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Derived scalar values (zero‑temperature distortion, transition temperature, susceptibility slope, specific heat jump) extracted from the thermodynamic curves. The checker compares each value to hidden reference scalar values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Tm`: K
    - `epsilon_0`: dimensionless
    - `dchi_dT_at_Tm`: 10⁻⁶ emu/g·K
    - `Delta_Cv`: J/mol·K