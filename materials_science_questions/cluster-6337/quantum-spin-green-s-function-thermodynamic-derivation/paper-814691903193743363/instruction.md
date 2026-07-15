# Weak Pseudogap from Spin-Fermion Model: Spectral Density and NMR Crossover

## Problem background
Underdoped cuprate superconductors display a 'weak pseudogap' regime above the superconducting transition temperature, characterized by a high-energy feature in the spectral density at momenta near (π,0) seen in ARPES and by a crossover in the NMR-derived quantity ⁶³T₁T/(⁶³T₂G)². The nearly antiferromagnetic spin-fermion model attributes these phenomena to planar quasiparticles interacting with strong, low-frequency antiferromagnetic spin fluctuations. In the limit where the temperature exceeds the characteristic spin-fluctuation energy (πT ≫ ω_sf), the spin fluctuations act as a static disorder potential for hot quasiparticles (those connected by the antiferromagnetic wave vector), and a complete diagrammatic summation yields recursion relations for the single-particle Green's function and the electron-spin fluctuation vertex. This task asks: can numerical evaluation of these recursion relations reproduce the emergence of a precursor spin-density-wave (SDW) state for moderate correlation lengths, giving rise to the observed high-energy spectral peak and the temperature-dependent NMR crossover?

## Approach
The calculation follows the spin-fermion model in the quasistatic limit. After a Hubbard-Stratonovich transformation and integration over fermions, the effective action is expanded diagrammatically. In the static limit all diagrams can be resummed, leading to closed recursion relations for the Green's function and the vertex function:

- Green's function recursion: G_k^{(l)}(ω)^{-1} = g_k^{(l)}(ω)^{-1} − κ_{l+1} Δ_0^2 G_k^{(l+1)}(ω), where κ_l = (l+2)/3 if l is odd, else κ_l = l/3; and g_k^{(l)}(ω) is the Fourier transform of −i Θ(t) exp(−i ε_{k+Q} t) [K_0(t |v_{k+Q}|/ξ) / (2π)]^l with modified Bessel function K_0.
- Vertex recursion: Γ_{k,k+q}^{(l)}(ω+i0^+, ω+ν+i0^+) = 1 − r_{l+1} Δ_0^2 G_k^{(l+1)}(ω) G_{k+q}(ω+ν) Γ_{k,k+q}^{(l+1)}, with r_l = l if l is even, else r_l = (l+2)/9; Δ_0 is the characteristic SDW energy scale (approximately g/2).

These recursions involve modified Bessel functions and depend on a tight-binding band dispersion (nearest and next-nearest neighbour hopping) and the antiferromagnetic correlation length ξ. The single-particle spectral function A(k,ω) is extracted from the imaginary part of the resummed Green's function on the Fermi surface. The irreducible spin susceptibility is then computed from the Green's functions and the vertex, yielding the antiferromagnetic spin damping γ_Q and the ratio χ_Q²/γ_Q, which is proportional to the NMR product ⁶³T₁T/(⁶³T₂G)². To track the temperature evolution, the calculation is repeated for a range of temperatures using a piecewise ξ(T) relation that mimics the experimentally observed behaviour. The two main computational objectives are: (1) evaluate A(k,ω) at ξ=3 and T=500 K for a hot spot near (π,0) and a cold spot near the zone diagonal, and (2) compute γ_Q(T) and the ratio χ_Q²/γ_Q(T) for temperatures 200–600 K to reveal the crossover at the point where ξ≈2.

## Reproduction target
Produce the following two numerical artifacts under /app/outputs:
1. `step_01_spectral_data.csv`: spectral density A(k,ω) on the Fermi surface for the hot spot (k_x=π, k_y=0) and a cold spot (k_x=π/2, k_y adjusted to lie on the Fermi surface) at ξ=3, T=500 K, over an ω grid from -1.0 eV to 0.2 eV. Use the model parameters t = 0.25 eV, t' = -0.0625 eV, coupling g = 0.6 eV.
2. `step_02_crossover_data.csv`: temperature series for γ_Q(T) and χ_Q²/γ_Q(T) for at least 10 points from 200 K to 600 K. The correlation length ξ(T) follows the given formulas: for 220 K ≤ T ≤ 470 K, ξ^{-1} = 1/4 + (1/4)(T-220)/(470-220); for T > 470 K, ξ^{-2} = 1/4 + (1/7)(T-470)/(700-470).
The computed data should allow the verifier to assess whether the numerical solution reproduces the weak pseudogap signatures: a high-energy peak at negative energy for the hot spot, and a change in the temperature trend of χ_Q²/γ_Q near the critical temperature T_cr≈470 K.

## Assets

- Python 3 with NumPy and SciPy: python3 numpy scipy

## Workflow steps

### Step 1: Compute Hot and Cold Spectral Density
- Role: scored (load-bearing)
- Action: Implement the Green's function recursion as described in the Approach section by numerically evaluating the auxiliary propagators g_k^(l)(ω) containing modified Bessel functions, then solve backwards from a large cutoff L to obtain the resummed Green's function. From its imaginary part, extract the spectral density A(k,ω) on the Fermi surface for a hot spot (k_x=π, k_y=0) and a cold spot (k_x=π/2, k_y such that the point lies on the Fermi surface). Use model parameters: t=0.25 eV, t'=-0.0625 eV, coupling g=0.6 eV, correlation length ξ=3, temperature T=500 K.
- Output file: `/app/outputs/step_01_spectral_data.csv`
- Format: csv
- Contract: csv with columns: kx (float, in units of π/a), ky (float), omega (float, eV), spectral_density (float, 1/eV). Rows for (kx=1.0, ky=0.0) (hot spot) and (kx=0.5, ky such that the point lies on the Fermi surface) (cold spot), over an omega grid covering at least -1.0 eV to 0.2 eV.
- Scoring: scored by hidden verifier

### Step 2: Compute Temperature-Dependent NMR Crossover
- Role: scored (load-bearing)
- Action: Using the same recursion for the Green's function, also solve the vertex recursion as described in the Approach section to obtain the electron-spin fluctuation vertex. Combine Green's function and vertex to compute the irreducible spin susceptibility and derive the spin damping γ_Q = lim_{ω→0} χ̃_Q''(ω)/ω and the ratio χ_Q²/γ_Q. Evaluate these quantities for a temperature grid from 200 K to 600 K using the ξ(T) functional forms: between T_*=220 K and T_cr=470 K, ξ^{-1} = 1/4 + (1/4)(T-T_*)/(T_cr-T_*); above T_cr, ξ^{-2} = 1/4 + (1/7)(T-T_cr)/(700 K).
- Output file: `/app/outputs/step_02_crossover_data.csv`
- Format: csv
- Contract: csv with columns: temperature_K (float), correlation_length_xi (float), spin_damping_gamma_Q (float, eV^-1), ratio_chiQ2_over_gammaQ (float, dimensionless). At least 10 temperature points spanning 200 K to 600 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_spectral_data.csv`
- `/app/outputs/step_02_crossover_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_spectral_data.csv
- path: `/app/outputs/step_01_spectral_data.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Spectral density A(k,ω) on the Fermi surface for hot (kx=1.0,ky=0.0) and cold (kx=0.5,ky~0.5) quasiparticles at ξ=3, T=500 K. The hidden checker locates the maximum spectral density for ω<0 at the hot spot and verifies its frequency within a tolerance, and checks that the cold spot maximum lies near zero.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `ky`, `omega`, `spectral_density`
  - `units`:
    - `kx`: units of π/a
    - `ky`: units of π/a
    - `omega`: eV
    - `spectral_density`: 1/eV

### step_02_crossover_data.csv
- path: `/app/outputs/step_02_crossover_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature dependence of spin damping γ_Q and the product χ_Q²/γ_Q (proportional to ⁶³T₁T/(⁶³T₂G)²). The hidden checker computes the numerical derivative of ratio_chiQ2_over_gammaQ with respect to temperature and verifies it is positive for T<470 K and non-positive for T>470 K, confirming the crossover.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `correlation_length_xi`, `spin_damping_gamma_Q`, `ratio_chiQ2_over_gammaQ`
  - `units`:
    - `temperature_K`: K
    - `correlation_length_xi`: dimensionless
    - `spin_damping_gamma_Q`: eV^-1
    - `ratio_chiQ2_over_gammaQ`: dimensionless

Notes: All model parameters (t, t', g, ξ(T) forms) are extracted from the source paper. Only standard scientific Python libraries are required; no proprietary software or external datasets needed. The agent must perform the full numerical evaluation of the recursion relations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_spectral_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "ky",
          "omega",
          "spectral_density"
        ],
        "units": {
          "kx": "units of π/a",
          "ky": "units of π/a",
          "omega": "eV",
          "spectral_density": "1/eV"
        }
      },
      "description": "Spectral density A(k,ω) on the Fermi surface for hot (kx=1.0,ky=0.0) and cold (kx=0.5,ky~0.5) quasiparticles at ξ=3, T=500 K. The hidden checker locates the maximum spectral density for ω<0 at the hot spot and verifies its frequency within a tolerance, and checks that the cold spot maximum lies near zero."
    },
    {
      "file": "step_02_crossover_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "correlation_length_xi",
          "spin_damping_gamma_Q",
          "ratio_chiQ2_over_gammaQ"
        ],
        "units": {
          "temperature_K": "K",
          "correlation_length_xi": "dimensionless",
          "spin_damping_gamma_Q": "eV^-1",
          "ratio_chiQ2_over_gammaQ": "dimensionless"
        }
      },
      "description": "Temperature dependence of spin damping γ_Q and the product χ_Q²/γ_Q (proportional to ⁶³T₁T/(⁶³T₂G)²). The hidden checker computes the numerical derivative of ratio_chiQ2_over_gammaQ with respect to temperature and verifies it is positive for T<470 K and non-positive for T>470 K, confirming the crossover."
    }
  ],
  "notes": "All model parameters (t, t', g, ξ(T) forms) are extracted from the source paper. Only standard scientific Python libraries are required; no proprietary software or external datasets needed. The agent must perform the full numerical evaluation of the recursion relations."
}
```

## How you are scored
A hidden verifier inspects each required artifact. For `step_01_spectral_data.csv`, the verifier locates the maximum spectral density for ω<0 at the hot spot and compares its frequency to a hidden reference derived from the paper's results, awarding credit if the peak lies within an expected tolerance. It also checks that the cold spot maximum lies near zero. For `step_02_crossover_data.csv`, the verifier computes the numerical derivative of `ratio_chiQ2_over_gammaQ` with respect to temperature and verifies that it is positive for T<470 K and non-positive for T>470 K, thereby confirming the crossover. Both files are validated for structural correctness (columns, positive values). The final reward is a weighted combination of the scores from the two artifacts. Simply reporting the paper’s numbers without genuinely solving the recursion will not pass the structural and cross‑check verifications.
