# Zero Sound Velocity and Critical Bubble Radius in Fermi Liquid at Negative Pressure

## Problem background
Liquid helium‑3 under negative pressure exists in a metastable state; its stability limit (the spinodal) is the point where the first sound velocity vanishes. At low temperatures the liquid enters the degenerate Fermi‑liquid regime where a distinct collisionless collective mode — zero sound — can propagate even when first sound is overdamped. This task investigates the zero‑sound velocity and its consequences for cavitation by computing the zero‑sound velocity at the spinodal and the critical bubble radius as a function of pressure offset from the spinodal, using Landau’s Fermi‑liquid theory and a supplied equation of state.

## Approach
The computation proceeds in two conceptual stages. First, using a provided effective‑mass fit for liquid ³He and the condition that at the spinodal the Landau parameter F₀ = −1, one determines the spinodal density, the effective mass, the Fermi velocity, and the Landau parameter F₁. The zero‑sound velocity is then obtained by solving the Landau zero‑sound dispersion equation, a self‑consistency condition for a propagating distortion of the Fermi surface. At the spinodal the first‑sound velocity, which depends on the compressibility, vanishes, but zero sound may remain finite. Second, the critical bubble radius is computed by solving the Euler–Lagrange equation for the density profile of a critical bubble, using a phenomenological equation of state (the Maris EOS) that exhibits a singularity consistent with the spinodal. The radius is extracted as the distance at which the density reaches half its bulk value, for a series of pressure offsets above the spinodal. The results allow one to quantify the stiffness of the Fermi liquid at the spinodal and the scaling of the energy barrier for nucleation.

## Reproduction target
The task requires you to produce two numerically scored artifacts.
1) A JSON file **zero_sound_velocity.json** containing the zero‑sound velocity `c₀` and the first‑sound velocity `c₁` (both in m/s) at the spinodal, together with the Fermi velocity `v_F` (m/s). The first‑sound velocity must be computed as vanishing, and zero‑sound velocity must be computed by solving Landau’s equation.
2) A CSV file **critical_radius_scaling.csv** with columns `pressure_offset_mbar` and `critical_radius_nm`, giving the critical bubble radius `R_c` (in nm) as a function of the pressure distance `ΔP` to the spinodal (in mbar). You must include at least 5 data points spanning roughly 10⁻³ to 1 mbar, with one row corresponding to `ΔP = 0.02 mbar`. The critical radius must be obtained from the numerical solution of the bubble profile equation using the Maris EOS. Both output files will be checked for physical consistency and against hidden reference values.

## Assets
This task uses only parameters and formulas that are given directly in the instruction; no external dataset or software download is required. The needed inputs are:
- Greywall effective‑mass fit: `m/m* = a² (1 − ρ/ρ_c)²` with `a = 1.018` and `ρ_c = 198.6 kg/m³`.
- Maris equation of state: the Helmholtz free energy density (in J/m³) is `f(ρ) = (B/3) (ρ − ρ_s)^3`, where `B = 3.85e-2 J·m^6·kg⁻⁴` and `ρ_s = 52.0 kg/m³`. The spinodal condition `∂P/∂ρ = 0` (first‑sound velocity vanishes) is satisfied at `ρ = ρ_s`. The pressure is obtained from `P(ρ) = ρ f'(ρ) − f(ρ)`, and the chemical potential is `μ = f'(ρ)`. The gradient energy coefficient for the bubble profile is `κ = 4.0e-16 J·m⁵·kg⁻²`.
- Standard Fermi‑liquid relations: `F₁ = 3 ((m*/m) − 1)` and the condition `F₀ = −1` at the spinodal.
- The Landau zero‑sound equation: solve `(s − cosθ) ν(θ,φ) = cosθ Σ_{l=0}^{2} F_l ∫ P_l(cosχ) ν(θ′,φ′) dΩ′/(4π)`, where `s = c₀/v_F`, `ν` is the Fermi‑surface distortion, `χ` is the angle between directions `(θ,φ)` and `(θ′,φ′)`, `dΩ′` the solid‑angle element, and `P_l` Legendre polynomials. The Fermi parameters are `F₀ = −1`, `F₁` from the effective mass, and `F₂ ≈ 0`. A nontrivial solution exists only for `s > 1`; the zero‑sound velocity is then `c₀ = s v_F`. The first‑sound velocity is given by `c₁ = √(∂P/∂ρ)`.
All these are provided inline; there is no paper to retrieve and no remote resource to fetch.

## Workflow steps

### Step 1: Determine spinodal density and Fermi parameters
- Role: process
- Action: Use the Maris equation of state (free-energy density `f(ρ) = (B/3)(ρ − ρ_s)^3` with `B = 3.85e-2 J·m^6·kg⁻⁴` and `ρ_s = 52.0 kg/m³`). The spinodal condition `∂P/∂ρ = 0` is satisfied at `ρ = ρ_s`; confirm that `ρ_s` is the density where the first sound velocity vanishes. (Alternatively, solve `dP/dρ = 0` using `P(ρ) = ρ f'(ρ) − f(ρ)`.) From `ρ_s` and the Greywall effective-mass fit, compute the Fermi velocity `v_F`, the effective mass `m*`, and the Landau parameters: `F₀ = −1` (spinodal condition), `F₁ = 3(m*/m − 1)`.
- Evidence: `/app/outputs/spinodal_params.json`

### Step 2: Calculate zero sound velocity at the spinodal
- Role: scored (load-bearing)
- Action: Solve Landau's zero-sound equation using the Fermi parameters obtained in step 01. Extract the zero-sound phase velocity c0 and the first-sound velocity c1 at the spinodal. Record the results together with the Fermi velocity.
- Output file: `/app/outputs/zero_sound_velocity.json`
- Format: json
- Contract: {"c0_spinodal_mps": <float>, "c1_spinodal_mps": <float>, "Fermi_velocity_mps": <float>}
- Scoring: scored by hidden verifier

### Step 3: Compute critical bubble radius as function of pressure offset
- Role: process
- Action: Using the Maris equation of state (`f(ρ) = (B/3)(ρ − ρ_s)^3` with `B = 3.85e-2 J·m^6·kg⁻⁴`, `ρ_s = 52.0 kg/m³`, and gradient energy coefficient `κ = 4.0e-16 J·m⁵·kg⁻²`), compute the critical bubble density profile for several pressures `P` above the spinodal (`P > P_s = 0`). For each pressure `P`, the bulk liquid density `ρ_l` is the larger root of `P = ρ f'(ρ) − f(ρ)`. The chemical potential is `μ = f'(ρ_l)`. The critical profile `ρ(r)` obeys the Euler–Lagrange equation: `κ (d²ρ/dr² + (2/r) dρ/dr) = f'(ρ) − μ`, with boundary conditions `dρ/dr = 0` at `r = 0` and `ρ → ρ_l` as `r → ∞`. Solve numerically (e.g., shooting with RK4). Define the critical radius `R_c` as the radial distance where `ρ(r) = (ρ_l + ρ_s)/2`. Save a sample critical density profile for auditing.
- Evidence: `/app/outputs/critical_profile_sample.npy`

### Step 4: Output critical radius scaling data
- Role: scored
- Action: Save the computed pairs of pressure offset ΔP (mbar) and critical radius Rc (nm) to a CSV file. Include at least 5 points spanning roughly 0.001 to 1 mbar, and ensure one row corresponds to ΔP = 0.02 mbar.
- Output file: `/app/outputs/critical_radius_scaling.csv`
- Format: csv
- Contract: pressure_offset_mbar (float), critical_radius_nm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zero_sound_velocity.json`
- `/app/outputs/critical_radius_scaling.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zero_sound_velocity.json
- path: `/app/outputs/zero_sound_velocity.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Physics quantities at the spinodal: zero sound velocity, first sound velocity, and Fermi velocity, all in m/s. Checked against reference values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `c0_spinodal_mps`: float
    - `c1_spinodal_mps`: float
    - `Fermi_velocity_mps`: float

### critical_radius_scaling.csv
- path: `/app/outputs/critical_radius_scaling.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tabulated critical radius Rc (nm) as a function of the pressure offset from the spinodal ΔP (mbar). Checked against hidden reference values and a power-law exponent fit.
- schema:
  - `type`: table
  - `required_columns`: `pressure_offset_mbar`, `critical_radius_nm`

Notes: The solver must implement numerical methods for the zero-sound equation and the critical bubble profile. All required formulas and parameters (Maris EOS, Greywall fit) are provided inline; no external data download is needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zero_sound_velocity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "c0_spinodal_mps": "float",
          "c1_spinodal_mps": "float",
          "Fermi_velocity_mps": "float"
        }
      },
      "description": "Physics quantities at the spinodal: zero sound velocity, first sound velocity, and Fermi velocity, all in m/s. Checked against reference values with tolerances."
    },
    {
      "file": "critical_radius_scaling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_offset_mbar",
          "critical_radius_nm"
        ]
      },
      "description": "Tabulated critical radius Rc (nm) as a function of the pressure offset from the spinodal ΔP (mbar). Checked against hidden reference values and a power-law exponent fit."
    }
  ],
  "notes": "The solver must implement numerical methods for the zero-sound equation and the critical bubble profile. All required formulas and parameters (Maris EOS, Greywall fit) are provided inline; no external data download is needed."
}
```

## How you are scored
A hidden verifier will score your work by examining the two scored output files. For `zero_sound_velocity.json`, the verifier will check that the zero‑sound velocity and Fermi velocity are consistent with physical expectations and that the first‑sound velocity is essentially zero, comparing your reported values to hidden reference values within predetermined tolerances. For `critical_radius_scaling.csv`, the verifier will verify that the row with `pressure_offset_mbar = 0.02` yields a critical radius within a physically reasonable tolerance, and will perform a power‑law fit (R_c ∝ (ΔP)^b) on all your data points, checking that the exponent `b` matches the expected scaling law. Each scored artifact contributes a portion of the total reward. Simply reporting the paper’s numbers without having performed the required computations will not satisfy the checker, because the hidden tolerances and scaling checks are designed to be sensitive to implementation details.
