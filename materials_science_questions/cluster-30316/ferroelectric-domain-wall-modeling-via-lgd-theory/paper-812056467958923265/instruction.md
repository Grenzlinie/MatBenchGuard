# Equilibrium 180° stripe domains in epitaxial PbTiO3 films via LGD theory

## Problem background
When a ferroelectric thin film such as PbTiO₃ is grown epitaxially on an insulating substrate like SrTiO₃, the out‑of‑plane polarization creates a depolarizing field that must be compensated. In the absence of free charge, this compensation occurs through the formation of 180° stripe domains — alternating regions of up and down polarization — whose period is determined by a balance between residual electrostatic energy and domain‑wall energy. In ultrathin films the residual depolarizing field and domain walls can substantially suppress the ferroelectric transition temperature Tc. Accurate predictions of the equilibrium stripe period and the film‑thickness‑dependent Tc suppression are important for understanding and engineering nanoscale ferroelectric devices. In this task you will implement a Landau‑Ginzburg‑Devonshire (LGD) theory that includes the full nonlinear polarization dependence to compute the equilibrium stripe period and Tc for a specific PbTiO₃ film on SrTiO₃.

## Approach
You will minimize a free energy functional for a coherently strained PbTiO₃ film with 180° stripe domains. The polarization and electric field are treated in a two‑dimensional geometry (coordinates r₁ in‑plane perpendicular to stripe walls, r₃ normal to the film), periodic along r₁ with period d. The film is bounded by semi‑infinite SrTiO₃ regions on both sides (symmetric dielectric boundaries, case I).

**Free energy density inside the film:**
The free energy density (per unit volume) is

A_in = A₀² + α₁² P₁² + α₃² P₃² + α₃₃² (P₁⁴ + P₃⁴) + α₁₃² P₁² P₃² 
      + α₁₁₁ (P₁⁶ + P₃⁶) + α₁₁₂ (P₁⁴ P₃² + P₃⁴ P₁²)
      + (ε₀/2)(E₁² + E₃²) + (κ⊥/2)[(∂P₃/∂r₁)² + (∂P₁/∂r₁)²],

where ε₀ = 8.854×10⁻¹² F/m is the vacuum permittivity and κ⊥ = 7.8×10⁻¹¹ V m³/C is the gradient coefficient. The electric field E = −∇φ, and φ satisfies Poisson’s equation ε₀∇²φ = ∇·P. Outside the film the SrTiO₃ is treated as a linear dielectric with relative permittivity ε_ex(T) = 8.3×10⁴/(T − 38 K), contributing a free energy density (ε₀ε_ex/2)|E|².

**Coefficient renormalization (epitaxial strain + stripe domains)**
The bulk PbTiO₃ Landau coefficients are renormalized by the epitaxial misfit strain xₘ(T) and by the fixed‑x₃ elastic solution appropriate for 180° stripe domains. 

Misfit strain:
  xₘ(T) = [a_SrTiO₃(T) − a_PbTiO₃^cub(T)] / a_PbTiO₃^cub(T).
The cubic lattice parameters are given by a = a₀[1 + Σ bₙ (T − T_ref)ⁿ] with the coefficients:
  SrTiO₃: a₀ = 0.39247 nm, T_ref = 765 K,
    b₁ = 1.133×10⁻⁵ K⁻¹, b₂ = 1.367×10⁻⁹ K⁻², b₃ = 1.923×10⁻¹³ K⁻³.
  PbTiO₃ (above T_C): a₀ = 0.39663 nm, T_ref = 765 K, b₁ = 1.29×10⁻⁵ K⁻¹.
  PbTiO₃ (below T_C): a₀ = 0.39663 nm, T_ref = 765 K, b₁ = 0.472×10⁻⁵ K⁻¹.

Bulk Landau and coupling coefficients (from experiment):
  θ = 752.0 K, C = 1.5×10⁵ K  (so that α₁ = (T−θ)/(2ε₀C)).
  α₁₁ = −7.25×10⁷ V m⁵/C³, α₁₂ = 7.5×10⁸ V m⁵/C³,
  α₁₁₁ = 2.61×10⁸ V m⁹/C⁵, α₁₁₂ = 6.1×10⁸ V m⁹/C⁵,
  α₁₂₃ = −3.7×10⁹ V m⁹/C⁵.
  Elastic compliances: s₁₁ = 8.0×10⁻¹² m²/N, s₁₂ = −2.5×10⁻¹² m²/N, s₄₄ = 9.0×10⁻¹² m²/N.
  Electrostrictive constants: Q₁₁ = 8.9×10⁻² m⁴/C², Q₁₂ = −2.6×10⁻² m⁴/C², Q₄₄ = 6.75×10⁻² m⁴/C².

First, compute the intermediate *‑renormalized coefficients for a single‑domain film:
  α₁* = α₁ − xₘ (Q₁₁+Q₁₂)/(s₁₁+s₁₂),
  α₃* = α₁ − 2 xₘ Q₁₂/(s₁₁+s₁₂),
  α₁₁* = 4.2×10⁸ V m⁵/C³,
  α₃₃* = 5.0×10⁷ V m⁵/C³,
  α₁₃* = 4.5×10⁸ V m⁵/C³,
  α₁₂* = 7.3×10⁸ V m⁵/C³.
  (A₀* = xₘ²/(s₁₁+s₁₂); the arbitrary constant A₀ can be set to zero for energy differences.)

Next, the renormalization for stripe domains (fixed‑x₃ elastic solution) introduces a self‑consistent average polarization P† and two constant coefficients:
  C₃₃² = 3.73×10⁸ V m⁵/C³,  C₁₃² = 3.01×10⁷ V m⁵/C³.
  Then
    α₁² = α₁* − C₁₃² P†²,
    α₃² = α₃* − 2 C₃₃² P†²,
    α₃₃² = α₃₃* + C₃₃²,
    α₁₃² = α₁₃* + C₁₃² + Q₄₄²/(2 s₄₄),
  with P†² = ⟨P₃² + (C₁₃²/(2C₃₃²)) P₁²⟩ ≈ ⟨P₃²⟩ (the rms average over the film volume, to be determined self‑consistently during the minimization).

**Numerical minimization for a given stripe period**
Express P₁, P₃ and φ as Fourier series with only odd harmonics (n = 1,3,5,…):
  P₁ = Σ aₙ(r₃) exp(i n k₀ r₁),
  P₃ = i Σ bₙ(r₃) exp(i n k₀ r₁),
  φ  = i Σ vₙ(r₃) exp(i n k₀ r₁),
with k₀ = 2π/d. The aₙ, bₙ, vₙ are real functions satisfying aₙ = a_{-n}, bₙ = −b_{-n}, etc. In the SrTiO₃ regions the potential can be integrated analytically: vₙ(r₃) = vₙ⁰ exp(−|n k₀ r₃|) (for r₃<0) and analogously for r₃>t. The field-induced contribution to the free energy per unit area from each interface is (ε₀ε_ex k₀) Σ n (vₙ⁰)².

For a fixed k₀, the total free energy functional 𝒜 (per unit area) is a function of the profiles aₙ(r₃), bₙ(r₃) and the interface potentials vₙ⁰, vₙ^t. Use a relaxation (iterative) method to find the distribution that minimizes 𝒜, enforcing Poisson’s equation and the self‑consistency condition on P†. This yields the minimum free energy 𝒜_min(k₀) for that period. Scan a range of k₀ values (or d) and determine the equilibrium stripe period d_eq as the one that gives the lowest 𝒜_min. For the required condition (t=24.2 nm, T=700 K) use at least 11 odd harmonics to achieve convergence. 

**Determination of Tc**
At each candidate temperature T, perform the above minimization to obtain 𝒜_min(T) for the striped state. Compute the paraelectric reference free energy per unit area: 𝒜_para(T) = t A₀*(T). The transition temperature Tc is defined by the condition 𝒜_min(Tc) = 𝒜_para(Tc). Since the striped free energy decreases with decreasing temperature, one can find Tc by bisection or root‑finding. This Tc corresponds to the same film thickness (24.2 nm) and case-I boundary conditions.

## Reproduction target
For a PbTiO₃ film of thickness t = 24.2 nm, epitaxially strained to an SrTiO₃ substrate, with symmetric SrTiO₃ top boundary (case I, i.e., SrTiO₃ on both sides), compute:
1. The equilibrium 180° stripe period d (in nanometers) at a temperature T = 700 K. This is the period of the domain pattern that minimizes the total free energy.
2. The transition temperature Tc (in kelvin) at which the free energy of the striped state equals that of the strain‑renormalized paraelectric phase. This Tc is for the same film thickness and boundary conditions.

## Assets

- Python 3 standard library: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare renormalized coefficients
- Role: process
- Action: Using the bulk Landau expansion coefficients, elastic constants, electrostrictive constants, and lattice parameters from the paper, compute the epitaxial misfit strain and renormalized coefficients for the stripe-domain elastic solution (fixed-x3). Derive the temperature-dependent coefficient alpha_3^oplus and the spontaneous polarization P0*. Implement the fixed-x3 elastic renormalization with the self-consistent average polarization P_dagger.
- Evidence: `/app/outputs/coeffs_log.txt`

### Step 2: Compute equilibrium stripe period at 700 K
- Role: scored (load-bearing)
- Action: For a PbTiO3 film of thickness 24.2 nm at 700 K with case I (symmetric SrTiO3) boundary conditions, set up the nonlinear free energy functional using the coefficients from step_00. Express polarization and electric potential as Fourier series with a sufficient number of odd harmonics. For a range of stripe wave numbers k0, minimize the integrated free energy numerically via a relaxation method. Determine the equilibrium stripe period d that yields the lowest total free energy. Write a CSV with column 'stripe_period_nm' containing the period in nanometers.
- Output file: `/app/outputs/step_01_equilibrium_stripe_period.csv`
- Format: csv
- Contract: single column 'stripe_period_nm' (float)
- Scoring: scored by hidden verifier

### Step 3: Compute transition temperature Tc
- Role: scored
- Action: For the same film thickness (24.2 nm) and boundary condition (case I), determine the temperature Tc at which the free energy of the equilibrium striped state equals that of the paraelectric reference phase. At candidate temperatures, run the minimization procedure of step_01 to obtain the minimum free energy of the striped state. Compare with the paraelectric free energy t*A0* (where A0* is the temperature-dependent reference coefficient). Locate Tc as the temperature where these two energies become equal. Write a CSV with column 'Tc_K' containing Tc in Kelvin.
- Output file: `/app/outputs/step_02_transition_temperature.csv`
- Format: csv
- Contract: single column 'Tc_K' (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_equilibrium_stripe_period.csv`
- `/app/outputs/step_02_transition_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_equilibrium_stripe_period.csv
- path: `/app/outputs/step_01_equilibrium_stripe_period.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium stripe period in nanometers at T=700 K, t=24.2 nm, case I boundary conditions.
- schema:
  - `type`: table
  - `required_columns`: `stripe_period_nm`
  - `units`:
    - `stripe_period_nm`: nm

### step_02_transition_temperature.csv
- path: `/app/outputs/step_02_transition_temperature.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Transition temperature Tc in Kelvin for the same film thickness and boundary condition.
- schema:
  - `type`: table
  - `required_columns`: `Tc_K`
  - `units`:
    - `Tc_K`: K

Notes: The checker compares the submitted values against hidden reference numbers using predefined tolerances. Both unitless numeric values are deterministic physical quantities derived from the specified conditions and the LGD theory.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_equilibrium_stripe_period.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "stripe_period_nm"
        ],
        "units": {
          "stripe_period_nm": "nm"
        }
      },
      "description": "Equilibrium stripe period in nanometers at T=700 K, t=24.2 nm, case I boundary conditions."
    },
    {
      "file": "step_02_transition_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Tc_K"
        ],
        "units": {
          "Tc_K": "K"
        }
      },
      "description": "Transition temperature Tc in Kelvin for the same film thickness and boundary condition."
    }
  ],
  "notes": "The checker compares the submitted values against hidden reference numbers using predefined tolerances. Both unitless numeric values are deterministic physical quantities derived from the specified conditions and the LGD theory."
}
```

## How you are scored
Your results will be evaluated by an automated verifier that reads the two CSV files you write. The equilibrium stripe period value (stripe_period_nm) is compared to a hidden reference value within a tolerance; a correct‑within‑tolerance period earns 0.5 points. The transition temperature (Tc_K) is similarly compared to a hidden reference within a tolerance; a correct‑within‑tolerance Tc earns another 0.5 points. Both output files must exist, follow the specified CSV schema, and contain physically reasonable numbers. The verifier does not inspect your code or intermediate files.
