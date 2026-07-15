## Problem background

Titanium alloys exposed to elevated temperatures develop an oxygen-enriched brittle surface layer known as alpha-case, which can embrittle the material and promote failure. This task addresses the prediction of alpha-case growth under combined thermal shock and mechanical loading, where mechanical damage enhances oxygen diffusivity through a percolation mechanism. The goal is to simulate a Ti-6Al-2Sn-4Zr-2Mo plate and observe the threshold-like increase in alpha-case depth when damage exceeds a critical threshold.

## Approach

Implement a two-dimensional finite-element solver for the coupled thermo-chemo-mechanical problem described in the paper. The model comprises:
- a steady-state heat conduction solver that provides the temperature distribution from a specified top-surface heat flux;
- an oxygen diffusion model in which the diffusivity depends on temperature and mechanical damage via a percolation-enhanced law;
- a mechanical response model based on a generalized Johnson-Cook yield stress that accounts for oxygen-induced hardening and embrittlement, with strain-based damage evolution;
- a penalty-based scale-bridging scheme that couples a finely meshed boundary region (top 60 µm) where alpha-case forms with a coarser substrate below;
- a staggered, semi-explicit coupling algorithm that alternately solves the mechanical and diffusion sub-problems.

The simulated component is a plate of thickness 2.286 mm. The top boundary receives a heat flux: a nominal 1.0 W/mm² that is elevated to 6.5 W/mm² at the centre (localised thermal shock). The bottom edge is held at 149 °C. The ambient surface oxygen concentration is 10 wt%, and the initial bulk concentration is 0.15 wt%. Uniform lateral tensile loading is applied at eight amplitudes: 0, 605, 610, 611, 612, 613, 614, 615 MPa; each load is ramped linearly to its target within the first hour and then held constant. The total simulation duration is 400 h.

## Model equations and material parameters

### General dimensions and discretisation
The plate is 2.286 mm thick and considered infinite in the lateral direction; a 2‑D plane‑strain slice is modelled. The top 60 μm is designated as the boundary region and must be meshed with high resolution (element size ≤ 2 μm) to capture steep oxygen gradients. The substrate below is coarsely meshed. Continuity across the transition interface is enforced by a penalty method (penalty parameter η ≥ 10⁴).

### Oxygen diffusion model
The 2‑D transient diffusion equation:
∂c/∂t = ∇·[D(ω,T) ∇c]   (Fick’s second law)

Initial condition: c(x,y,t=0) = c∞ = 0.15 wt%.
Boundary condition on the top edge: c = c₀ = 10 wt%.
Other boundaries are insulated (zero normal flux).

### Diffusivity
D(ω,T) = D₀ [1 + 𝒟(ω)] exp(‑Q / (R T))
with
D₀ = 0.62 cm²/s = 62 mm²/s,
Q = 203 kJ/mol,
R = 8.314 J/(mol·K) = 8.314 × 10⁻³ kJ/(mol·K).

𝒟(ω) = Dᵢ + Dₚ,
Dᵢ = a ω,   a = 3.56,
Dₚ = 0                                          for ω < ωc,
     (ω‑ωc)² / (ωₑc‑ωc)                         for ωc ≤ ω < ωₑc,
     ∞ (capped to a large finite number, e.g. 1 × 10⁶)   for ω ≥ ωₑc,
where ωc = 0.1 (conduction percolation threshold),
      ωₑc = 0.5 (elastic percolation threshold).

Alpha‑case: region where c ≥ cᶜʳᶦᵗ = 4.5 wt%.
Maximum alpha‑case depth: greatest vertical distance from the top surface to a point with c ≥ 4.5 wt%.

### Mechanical response (generalised Johnson–Cook model)
Yield surface: Von Mises.
Yield stress:
σ_Y = [A + B (ε̅ᴠᴾ)ⁿ + F c] [1 + C ln(ε̇*)] [1 + (T*)ᵐ]

with
A = 827 MPa,   B = 820 MPa,   C = 0.014,   F = 110 MPa,
n = 0.93,   m = 0.85,
T* = (T‑T_room) / (T_melt‑T_room),
T_room = 25 °C (298 K),
T_melt = 1700 °C (1973 K).  (The paper reports T_melt = 3092 °F; convert to °C:  (3092 ‑ 32) × 5/9 ≈ 1700 °C.)
ε̇* = ε̅̇ᴠᴾ / ε̇⁰,   ε̇⁰ = 1.0 s⁻¹.

Viscoplastic flow rule:
ε̇ᴠᴾ = γ ⟨f/σ_Y⟩^q (∂f/∂σ)   with γ = 1.0 MPa⁻¹ h⁻¹, q = 0.3.

### Damage model
ω = ε̅ᴠᴾ / ε_f,
where ε_f = [D₁(c) + D₂ exp(D₃ σ*)] [1 + D₄ ln(ε̇*)] [1 + D₅ T*],
with D₂ = 0.27, D₃ = 0.48, D₄ = 0.014, D₅ = 0.5,
σ* = tr(σ) / (3 σ̅), σ̅ the Von Mises effective stress.

D₁(c) is piecewise linear:
D₁(c) = D₁⁰                                     for c ≤ c∞_JC,
        D₁⁰ + (D₁ᴬ‑D₁⁰) (c‑c∞_JC) / (c_crit‑c∞_JC)   for c∞_JC < c < c_crit,
        D₁ᴬ                                     for c ≥ c_crit,
with D₁⁰ = ‑0.22, D₁ᴬ = ‑0.27,
c∞_JC = 0.295 wt%   (bulk alloy oxygen content for Johnson–Cook model),
c_crit = 4.5 wt%.

At failure (ω = 1) the stiffness is reduced to a small residual (e.g. 1 % of the original).

### Thermal properties
The steady‑state temperature field must be computed using the temperature‑dependent thermal conductivity k(T) and specific heat cᵥ(T) of Ti‑6Al‑2Sn‑4Zr‑2Mo. Use the following data (T in K, k in W/(mm·K), cᵥ in J/(kg·K), density ρ = 4.539 × 10⁻⁶ kg/mm³):
T (K)   k (W/(mm·K))   cᵥ (J/(kg·K))
300     0.0072         523
400     0.0084         540
500     0.0100         560
600     0.0113         580
700     0.0125         600
800     0.0135         620
900     0.0142         640
1000    0.0148         660
1100    0.0152         680
Linearly interpolate between these values.
Quadratic polynomial approximations (optional): k = 6.5 × 10⁻⁶ T² + 0.0055 T + 0.0057, cᵥ = 0.0001 T² + 0.15 T + 480 (T in K). The exact choice of fit is not critical as long as the trend is captured.
The bottom edge is kept at 149 °C (422 K); the top edge receives the specified heat flux. Solve the steady‑state heat equation ∇·(k ∇T) = 0 with these boundary conditions.

### Staggered coupling algorithm
For each time step Δt:
1. Solve the mechanical problem (Eq. (48) in the paper) with current c, ω, T constant.
2. Update damage ω using the new strain.
3. Solve the nonlinear diffusion problem (Eq. (50)) with updated D(ω,T) using Newton‑Raphson.
4. If convergence fails, halve Δt and repeat; otherwise advance time.

## Reproduction target

Run the coupled chemo-mechanical simulation for all eight stress amplitudes, extract the maximum alpha-case depth at t = 400 h, and report the results. The expected outcome is a set of depths that reveal a significant increase between 611 and 612 MPa, driven by damage exceeding the percolation limit in the boundary layer.

## Assets

| Name | Type | Access hint |
|------|------|-------------|
| FEniCS (or equivalent FEM library) | package | https://fenicsproject.org/ (not strictly required; any open-source FEM toolkit or self-written code may be used) |

## Workflow steps

### Step 1: Implement the coupled solver
- Role: process
- Action: Implement a 2D finite-element solver for the coupled oxygen diffusion and mechanical response described in the approach. Incorporate the damage-dependent diffusivity, the generalized Johnson-Cook model, the penalty-based scale bridging between the boundary region and substrate, and the staggered coupling algorithm.
- Evidence: none

### Step 2: Compute steady-state temperature field
- Role: process
- Action: Using the implemented heat conduction solver, compute the steady-state temperature distribution in the plate. Apply the given flux distribution on the top edge, fix the bottom temperature at 149 °C, and use temperature-dependent conductivity and specific heat. The resulting nodal temperature field will be the thermal input for the subsequent chemo-mechanical runs.
- Evidence: none

### Step 3: Run coupled chemo-mechanical simulations for all stress levels
- Role: process
- Action: For each of the eight stress amplitudes (0, 605, 610, 611, 612, 613, 614, 615 MPa), run the coupled chemo-mechanical simulation for 400 h. Use the steady-state temperature field from Step 2, initial oxygen concentration c∞ = 0.15 wt%, surface concentration c0 = 10 wt%, and the material parameters given in the paper (Tables 1 and 2). The tensile load is ramped to the target amplitude in the first hour and then held constant. Retain the final oxygen concentration field for analysis.
- Evidence: `/app/outputs/simulation_log.txt` (a plain-text log summarising simulation progress and completion for each stress case)

### Step 4: Extract maximum alpha-case depths (load-bearing scored step)
- Role: scored
- Action: For each stress amplitude, from the final oxygen concentration field (t = 400 h), determine the maximum alpha-case depth, defined as the distance from the top surface to the deepest interior point where the local oxygen concentration meets or exceeds 4.5 wt%. Write the results to `/app/outputs/alpha_case_depths.csv`.
- Output file: `/app/outputs/alpha_case_depths.csv`
- Format: csv
- Contract: Two columns: `stress_MPa` (numeric) and `max_depth_um` (numeric). One row per stress amplitude, listed in ascending order: 0, 605, 610, 611, 612, 613, 614, 615.
- Scoring: The hidden verifier compares the reported depths against paper reference values and verifies the threshold trend.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alpha_case_depths.csv
- path: `/app/outputs/alpha_case_depths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum alpha-case depth for each applied tensile stress amplitude after 400 h of simulation.
- schema:
  - `type`: table
  - `required_columns`: `stress_MPa`, `max_depth_um`
  - `units`:
    - `stress_MPa`: MPa
    - `max_depth_um`: µm

Notes: The verifier compares the depths at 605 MPa and 615 MPa against paper reference values and checks for a threshold jump (depth ratio ≥ 2.0) between 611 and 612 MPa. The columns are strictly numeric and the rows must follow the given stress order.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alpha_case_depths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "stress_MPa",
          "max_depth_um"
        ],
        "units": {
          "stress_MPa": "MPa",
          "max_depth_um": "µm"
        }
      },
      "description": "Maximum alpha-case depth for each applied tensile stress amplitude after 400 h of simulation."
    }
  ],
  "notes": "The verifier compares the depths at 605 MPa and 615 MPa against paper reference values and checks for a threshold jump (depth ratio ≥ 2.0) between 611 and 612 MPa. The columns are strictly numeric and the rows must follow the given stress order."
}
```

## How you are scored

A hidden verifier reads your `alpha_case_depths.csv` and independently evaluates it against paper benchmark values and the expected threshold behaviour. Partial credit is awarded based on how closely your results match the reference depths and whether the jump between 611 and 612 MPa is reproduced. Simply reporting the paper’s numbers is not sufficient; the results must arise from a genuine simulation of the coupled model.
