# Field-Induced Shear Modulus from a Gaussian Column Distribution Model for Anisotropic MREs

## Problem background
Magnetorheological elastomers (MREs) are smart materials whose stiffness can be altered by an external magnetic field. Designing MREs with a desired field‑induced shear modulus requires understanding how the modulus depends on the microstructure — the arrangement and dimensions of the magnetic particles embedded in the elastomer matrix. Under a magnetic field, the particles aggregate into column‑like structures; the lengths of these columns are not all equal but follow a certain distribution in real materials. This task implements a model that predicts the field‑induced shear modulus ΔG from the column microstructure: the particles are assumed to form body‑centered tetragonal (BCT) columns whose lengths obey a Gaussian distribution. Your job is to compute ΔG for several regimes of column length, column width, external magnetic field, and shear strain, producing a CSV file that can be compared with independent calculations.

## Physical constants and fixed parameters
- Vacuum permeability μ₀ = 4π×10⁻⁷ H·m⁻¹
- Particle radius R = 1.25×10⁻⁶ m
- Volume of a particle: Vₚ = (4/3)πR³
- Matrix relative permeability μₑ = 1.0
- Particle relative permeability μₚ = 1000
- Dielectric contrast factor: β = (μₚ − μₑ)/(μₚ + 2μₑ) ≈ 1 (use exact value)
- Saturation magnetization of particles: Mₛ = 1.7×10⁶ A/m
- Particle volume fraction φ = 0.11

## Microstructural model
The iron particles aggregate into a large number of parallel body‑centred tetragonal (BCT) columns. A column is characterised by:
- **Length**: number of particles along the magnetic‑field direction, denoted ℓ. ℓ follows a Gaussian distribution with mean L and standard deviation σ. ℓ is restricted to integers 1, 2, …, 2L.
- **Width**: integer parameter b describing the cross‑section. The physical width b′ is related to b by b′ = √6 R (b−1) (i.e. b = b′/(√6 R) + 1). The cross‑section contains b² + (b−1)² particles.

## Magnetic dipole moment of a particle
When a magnetic field H₀ is applied along the column axis (z‑direction) and a uniform shear strain γ is imposed, a particle acquires a dipole moment p (oriented along z). The magnetisation of a particle follows the Fröhlich–Kennelly law, which combines the low‑field linear behaviour with saturation at high fields:

\[
p = \frac{3\mu_e\mu_0\beta V_p H_{\mathrm{loc}}}{1 + \dfrac{3\mu_e\beta H_{\mathrm{loc}}}{M_s}} \tag{19}
\]

where H_loc is the local magnetic field at the particle’s centre.

The local field is the sum of the applied external field H₀ and the field produced by all other dipoles in the same BCT column:

\[
H_{\mathrm{loc}} = H_0 + H_{p,z}, \qquad H_{p,z} = f(\ell,b,\gamma)\, p_z,
\]
with p_z = p (all moments aligned with z). The scalar factor f is computed by summing the z‑component of the dipole field over all other particles in the column:

\[
H_{p,z} = \sum_{\text{other particles}} \frac{2z^2 - x^2 - y^2}{4\pi\mu_0\,(x^2+y^2+z^2)^{5/2}}\; p_z. \tag{12}
\]

The column is built from two interpenetrating simple‑cubic sublattices (class A and class B). The particle positions depend on γ and on integer indices.

**Class A chains**

\[
\begin{aligned}
x &= \sqrt{6}A_1 R + 2A_3 R \sin\gamma,\\
y &= \sqrt{6}A_2 R,\\
z &= 2A_3 R \cos\gamma. \tag{13}
\end{aligned}
\]

Indices A₁, A₂, A₃ are integers. For a column of width b and length ℓ the summation ranges are:

- If b is odd : A₁, A₂ ∈ [−(b−1)/2, (b−1)/2]
- If b is even: A₁, A₂ ∈ [−(b/2−1), b/2−1]
- If ℓ is odd : A₃ ∈ [−(ℓ−1)/2, (ℓ−1)/2]
- If ℓ is even: A₃ ∈ [−(ℓ/2−1), ℓ/2−1]

The particle at (A₁,A₂,A₃) = (0,0,0) is the central particle itself and must be **excluded** from the sum.

**Class B chains**

\[
\begin{aligned}
x &= \frac{\sqrt{6}}{2}(2B_1-1)R + 2(B_3-1)R\sin\gamma,\\
y &= \frac{\sqrt{6}}{2}(2B_2-1)R,\\
z &= 2(B_3-1)R\cos\gamma. \tag{14}
\end{aligned}
\]

Indices B₁, B₂, B₃ are integers and must all be **non‑zero**. Their ranges are:

- If b is odd : B₁, B₂ ∈ [−(b−1)/2, (b−1)/2] \ {0}
- If b is even: B₁, B₂ ∈ [−b/2, b/2] \ {0}
- If ℓ is odd : B₃ ∈ [−(ℓ−1)/2, (ℓ−1)/2] \ {0}
- If ℓ is even: B₃ ∈ [−ℓ/2, ℓ/2] \ {0}

The total factor f(ℓ,b,γ) is obtained by summing the contribution from all A‑chain particles (except the central one) and all B‑chain particles:

\[
f(\ell,b,\gamma) = \sum_{\text{A, exclude }(0,0,0)} \frac{2z^2 - x^2 - y^2}{4\pi\mu_0 r^5}
+ \sum_{\text{B}} \frac{2z^2 - x^2 - y^2}{4\pi\mu_0 r^5},
\qquad r = \sqrt{x^2+y^2+z^2}.
\]

## Gaussian distribution of column lengths
The number of columns (per unit volume of elastomer) with length ℓ is

\[
\frac{n_\ell}{V} = \frac{\varphi}{\,V_p\,(b^2+(b-1)^2)}\,
\frac{\exp\!\bigl(-\tfrac{(\ell-L)^2}{2\sigma^2}\bigr)}
{\displaystyle\sum_{j=1}^{2L} j\,\exp\!\bigl(-\tfrac{(j-L)^2}{2\sigma^2}\bigr)}. \tag{7}
\]

The total dipole moment of one column of length ℓ is

\[
p_\ell = n'_\ell\, p_z(\ell), \qquad
n'_\ell = b^2\ell + (b-1)^2(\ell-1),
\]
where n'_\ell is the number of particles in that column and p_z(ℓ) is the (self‑consistent) z‑component of a particle’s dipole moment in such a column.

## Macroscopic quantities
The average particle polarisation in the field direction is

\[
J = \sum_{\ell=1}^{2L} \frac{n_\ell}{V}\; p_\ell
= \sum_{\ell=1}^{2L} \frac{n_\ell}{V}\; n'_\ell\, p_z(\ell). \tag{3}
\]

The effective magnetic susceptibility in the field direction is

\[
\chi_{\mathrm{eff}} = \frac{J}{\mu_0 H_0}. \tag{2}
\]

The magnetic‑field‑induced shear stress at a strain γ is

\[
\tau(\gamma) = -\frac{1}{2}\,\mu_0\left(\frac{H_0}{1+\chi_{\mathrm{eff}}(\gamma)}\right)^2
\frac{\partial\chi_{\mathrm{eff}}(\gamma)}{\partial\gamma}. \tag{1}
\]

The field‑induced shear modulus ΔG is the derivative of τ with respect to γ:

\[
\Delta G = \frac{d\tau}{d\gamma} \approx
\frac{\tau(\gamma+\delta\gamma) - \tau(\gamma-\delta\gamma)}{2\,\delta\gamma},
\qquad \delta\gamma = 10^{-6}.
\]

## Numerical implementation notes
- Pre‑compute f(ℓ,b,γ) for ℓ = 1,…,2L_max (L_max = 100) for each required (b,γ) combination by direct summation over the integer indices.
- For a given ℓ and H₀, solve for p_z self‑consistently using Eq. (19) and H_loc = H₀ + f·p_z (simple iteration to convergence, e.g. relative change < 10⁻¹²).
- Compute χ_eff(γ) via Eq. (2) and (3) using the column‑length distribution (7).
- For ∂χ_eff/∂γ use a central finite difference with γ step δγ = 10⁻⁶ (i.e. evaluate χ_eff at γ−δγ, γ+δγ). Alternatively, compute ∂χ_eff/∂γ by first computing ∂J/∂γ using the chain rule through p_z(ℓ,γ) and f(ℓ,γ); either method is acceptable provided it yields a second‑order accurate derivative.
- Finally, evaluate ΔG using the second‑order formula given above.

All calculations must be performed in SI units. Convert the final ΔG to MPa (1 MPa = 10⁶ Pa) for output.

## Reproduction target
Compute the field‑induced shear modulus ΔG (in MPa) for the following parameter sets, using the physical constants listed above.

(a) **Variation of mean column length L**  
L = 10, 20, 30, …, 100 (step 10)  
for each standard deviation σ = 3, 6, 9 (do **not** use the variance σ²).  
Fixed: b = 2, H₀ = 1 MA/m, γ = 0.003.

(b) **Variation of column width b**  
Set σ = 9.  
- Compute the four pairs (L, b) = (10,2), (20,3), (30,4), (40,5) with H₀ = 1 MA/m, γ = 0.003.  
- Compute a continuous curve with L = 30, b = 2, 3, 4, 5, 6, 7, same H₀ and γ.

(c) **Variation of external magnetic field H₀**  
H₀ = 0.1, 0.2, …, 1.0 MA/m (step 0.1 MA/m)  
for each shear strain γ = 0.001, 0.003, 0.005.  
Fixed: L = 30, σ = 3, b = 2.

Store all results in a CSV file at `/app/outputs/results.csv`. The file must contain exactly seven columns: `condition_id` (a string that identifies the parameter set), `L` (integer), `sigma` (integer, the standard deviation), `b` (integer), `H0` (float, in MA/m), `gamma` (float), `Delta_G` (float, in MPa). Include one row per computed condition.

## Assets
- Python standard libraries and numpy/scipy: numpy, scipy

## Workflow steps

### Step 1: Model parameters and geometry setup
- Role: process
- Action: Define the fixed physical constants and parameter grids for L, σ, b, H₀, γ as specified in the reproduction target.
- Evidence: none

### Step 2: Self‑consistent dipole moment and macroscopic shear modulus computation
- Role: process
- Action: For each required (b,γ) combination, pre‑compute the local field factor f(ℓ,b,γ) for ℓ = 1,…,200 by directly summing the dipole field over the BCT lattice. Solve the Fröhlich–Kennelly self‑consistent equation for p_z(ℓ). Aggregate over the Gaussian distribution of column lengths to obtain χ_eff and its derivative, then compute ΔG for every (L,σ,b,H₀,γ) set using the finite‑difference scheme described above.
- Evidence: none

### Step 3: Generate results CSV
- Role: scored (load‑bearing)
- Action: Write the computed ΔG values into a file named `results.csv` under `/app/outputs`. The file must contain the columns: `condition_id` (string), `L` (int), `sigma` (int), `b` (int), `H0` (float, MA/m), `gamma` (float), `Delta_G` (float, MPa). Include all rows for the three parameter sweeps.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: Columns: condition_id, L, sigma, b, H0, gamma, Delta_G.
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
- target_policy: reference_match
- description: Field‑induced shear modulus ΔG computed from the Gaussian distribution model for the specified parameter sweeps. The checker will recompute ΔG independently and compare values within predefined tolerances.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `L`, `sigma`, `b`, `H0`, `gamma`, `Delta_G`
  - `units`:
    - `H0`: MA/m
    - `Delta_G`: MPa

Notes: The agent must implement the complete model as described in the workflow steps. All input constants are public and no external data are required.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "L",
          "sigma",
          "b",
          "H0",
          "gamma",
          "Delta_G"
        ],
        "units": {
          "H0": "MA/m",
          "Delta_G": "MPa"
        }
      },
      "description": "Field‑induced shear modulus ΔG computed from the Gaussian distribution model for the specified parameter sweeps. The checker will recompute ΔG independently and compare values within predefined tolerances."
    }
  ],
  "notes": "The agent must implement the complete model as described in the workflow steps. All input constants are public and no external data are required."
}
```

## How you are scored
Your submitted `results.csv` will be evaluated by a hidden verifier that runs after you finish. The verifier independently computes ΔG for every condition using its own implementation of the same model (without relying on your code). It compares your reported ΔG values to its computed values, accepting small deviations that are reasonable for different numerical implementations.

In addition, the verifier checks that your results satisfy the physically expected trends: ΔG should increase with mean column length L, decrease with column width b, increase with external magnetic field H₀, and decrease with shear strain γ. The final reward combines the numerical agreement and the trend consistency; both are needed for a high score. Reporting the correct file format and including all required rows are prerequisites before value comparisons are performed.