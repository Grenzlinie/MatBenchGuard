# Eliashberg Superconducting Threshold and Thermodynamic Ratios on a Square Lattice

## Problem background
The emergence of superconductivity from a phonon‑mediated pairing interaction is studied using the Eliashberg equations, which describe the self‑consistent interplay between the order parameter and the wave‑function renormalisation. This task focuses on a two‑dimensional square lattice with a tight‑binding electron dispersion, acoustic phonons, and an electron–phonon interaction that depends on the momentum transfer. The model includes a parameter γ that controls the degree of unbalance between the diagonal and the off‑diagonal (pairing) channels of the self‑energy; a balanced state corresponds to γ = 0. The central question is to determine the threshold value γ_C above which superconductivity is destroyed, and to characterise the thermodynamic properties of the superconducting state in the balanced case.

## Approach
You will implement the full, momentum‑ and frequency‑resolved Eliashberg equations for the order‑parameter function φ and the wave‑function renormalisation factor Z on a square lattice. The equations are solved self‑consistently on a discrete momentum grid and a finite set of Matsubara frequencies. The electronic dispersion, phonon dispersion, and electron–phonon matrix elements are prescribed. The unbalance parameter γ appears only in the equation for Z, multiplying the interaction kernel. You will iterate the equations until convergence, then perform two numerical sweeps: (i) varying γ from 0 upwards to find the critical value γ_C where the averaged order parameter vanishes; (ii) at γ = 0, solving the equations at multiple temperatures to derive the thermodynamic ratios R_Δ, R_C, and R_H from the free‑energy difference, critical field, and specific heat.

## Reproduction target
Produce two JSON artifacts:
- `step_01_gamma_c.json` containing the critical unbalance parameter γ_C.
- `step_02_thermo_ratios.json` containing the three dimensionless ratios R_Δ, R_C, and R_H for the balanced case γ = 0.

## Assets

- Python numerical libraries (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: Implement the full Eliashberg solver
- Role: process
- Action: Implement the fully self-consistent Eliashberg equations (order-parameter function equation and wave-function renormalisation factor equation) with explicit dependence on electron momentum k and Matsubara frequency iω_n. Use the following model definitions: tight-binding electronic dispersion ε_k = -2t(cos k_x + cos k_y) + 4t' cos k_x cos k_y with t'=0.1t (energy in units of t), acoustic phonon dispersion ω_q = ω0 √(2 - cos q_x - cos q_y) with ω0=0.15t, electron-phonon matrix elements g_q = g0 |q| / √(ω_q) with g0=0.031 t^{3/2}. The equations are: φ_k(iω_n) = (1/(βN)) Σ_{m,q} K_q(ω_n-ω_m) φ_{k-q}(iω_m) / D_{k-q}(iω_m) and Z_k(iω_n) = 1 + (γ/(βN)) Σ_{m,q} (ω_m/ω_n) K_q(ω_n-ω_m) Z_{k-q}(iω_m) / D_{k-q}(iω_m) where K_q(ω_n-ω_m) = 2 g_q^2 ω_q / ((ω_n-ω_m)^2+ω_q^2) and D_k(iω_n) = (ω_n Z_k(iω_n))^2 + ε_k^2 + φ_k(iω_n)^2. The unbalance parameter γ appears only in the Z equation. Implement an iterative self-consistent solver on a user-chosen momentum lattice and Matsubara frequency cutoff, with appropriate initialization (e.g., Z≈1, φ positive) and convergence criteria.
- Evidence: `/app/outputs/solver_log.txt`

### Step 2: Critical unbalance parameter γ_C
- Role: scored (load-bearing)
- Action: Using the implemented Eliashberg solver, compute the averaged order parameter ⟨Δ(iω_{n=1})⟩ = (1/N) Σ_k Δ_k(iω_{n=1}) for a sweep of the unbalance parameter γ (starting from γ=0 and increasing until the order parameter vanishes). Determine the critical value γ_C at which superconductivity disappears (⟨Δ⟩ → 0). Report γ_C as a single floating-point number.
- Output file: `/app/outputs/step_01_gamma_c.json`
- Format: json
- Contract: {"gamma_c": <floating-point number>}
- Scoring: scored by hidden verifier

### Step 3: Thermodynamic ratios for γ=0
- Role: scored
- Action: Using the same Eliashberg solver, set the unbalance parameter γ=0. Solve the equations self-consistently at a range of temperatures to obtain the temperature dependence of the order parameter Δ_k(iω_n) and the wave-function renormalisation factor Z_k(iω_n). From these solutions, compute the following thermodynamic quantities: (i) the free-energy difference between superconducting and normal states ΔF, (ii) the thermodynamic critical field H_C = √(-8π ΔF), (iii) the specific heat jump ΔC(T_C) = C^S(T_C) - C^N(T_C), and (iv) the Sommerfeld constant γ_0 = (2π²/3) k_B² ρ(0)(1+λ_B), where λ_B is the electron‑phonon coupling constant computed from the isotropic Eliashberg function α²F(ω) obtained from g_q and ρ(0). Determine the dimensionless ratios: R_Δ = 2Δ(0)/(k_B T_C), R_C = ΔC(T_C)/C^N(T_C), and R_H = T_C C^N(T_C)/H_C^2(0). Report these three ratios as floating-point numbers.
- Output file: `/app/outputs/step_02_thermo_ratios.json`
- Format: json
- Contract: {"R_delta": <floating-point number>, "R_C": <floating-point number>, "R_H": <floating-point number>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_gamma_c.json`
- `/app/outputs/step_02_thermo_ratios.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_gamma_c.json
- path: `/app/outputs/step_01_gamma_c.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed critical unbalance parameter γ_C at which the averaged order parameter vanishes.
- schema:
  - `type`: object
  - `required`: `gamma_c`
  - `properties`:
    - `gamma_c`:
      - `type`: number

### step_02_thermo_ratios.json
- path: `/app/outputs/step_02_thermo_ratios.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The dimensionless thermodynamic ratios R_Δ, R_C, and R_H for the balanced state γ=0.
- schema:
  - `type`: object
  - `required`: `R_delta`, `R_C`, `R_H`
  - `properties`:
    - `R_delta`:
      - `type`: number
    - `R_C`:
      - `type`: number
    - `R_H`:
      - `type`: number

Notes: The hidden checker compares the agent's reported γ_C and the three ratios to the paper's reported values, using absolute tolerances that account for numerical differences in a re-implementation. No other condition (trend, ordering) is required beyond the numerical closeness.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_gamma_c.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "gamma_c"
        ],
        "properties": {
          "gamma_c": {
            "type": "number"
          }
        }
      },
      "description": "The computed critical unbalance parameter γ_C at which the averaged order parameter vanishes."
    },
    {
      "file": "step_02_thermo_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "R_delta",
          "R_C",
          "R_H"
        ],
        "properties": {
          "R_delta": {
            "type": "number"
          },
          "R_C": {
            "type": "number"
          },
          "R_H": {
            "type": "number"
          }
        }
      },
      "description": "The dimensionless thermodynamic ratios R_Δ, R_C, and R_H for the balanced state γ=0."
    }
  ],
  "notes": "The hidden checker compares the agent's reported γ_C and the three ratios to the paper's reported values, using absolute tolerances that account for numerical differences in a re-implementation. No other condition (trend, ordering) is required beyond the numerical closeness."
}
```

## How you are scored
A hidden verifier reads each scored JSON file and independently checks your computed γ_C and the three ratios. It compares your results to a hidden reference and computes a reward for each stage. The rewards are then combined with the weights given in the output contract to produce your final score. Reporting numbers alone is not sufficient; the verifier expects that the self‑consistent solver you built actually produced these results, but does not inspect the solver’s internals.
