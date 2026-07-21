# Piezoelectric shunt damping: optimal switching law and stationary voltage amplitude model

## Problem background
Piezoelectric shunt damping converts mechanical vibration into electrical energy and dissipates it through an external network. Among semi-active techniques, synchronized switch damping on inductor (SSDI) and on voltage source (SSDV) offer adaptivity and strong damping. The key design choices are when to connect the shunt (switching sequence) and what electrical resonant frequency to use relative to the mechanical excitation frequency. This work analytically models the stationary voltage amplitude of the piezoceramics and investigates how the switching times and the frequency ratio affect it. The central goal is to determine what switching law maximizes the voltage amplitude and how the enhanced SSDV technique relates to SSDI.

## Mathematical model and solver

The dynamics of the piezoelectric voltage u_p during the closed-switch period (switch connects LR network to piezoceramics) are described by the normalized ordinary differential equation

u_p'' + (1/Q) u_p' + u_p = F(τ) - sign(u0) * γ * x̂_p    (1)

where prime denotes derivative w.r.t. normalized time τ = t/√(C_p L), and

F(τ) = (α x̂_p / C_p) [ η^2 cos(η τ) + (η/Q) sin(η τ) ]   (2)

with η = ω √(C_p L) (frequency ratio), Q the electrical quality factor, α the force factor, C_p the capacitance, and x̂_p the amplitude of the harmonic mechanical deformation. The voltage source factor γ appears only for enhanced SSDV (γ = 0 recovers SSDI). The sign of the constant term is chosen to oppose the initial voltage u0 so that the voltage source assists the inversion. Without loss of generality, set the normalization constants α = 1, C_p = 1, and deformation amplitude x̂_p = 1; all voltages then scale accordingly.

The initial condition at τ = 0 (the instant the switch closes) is

u_p(0) = u0,
u_p'(0) = η sin(η τ_close),

where τ_close is the normalized time at which the switch closes. The initial derivative follows from the open-circuit condition i_p = 0 ⇒ u̇_p = (-α/C_p) ẋ_p, giving u_p'(0) = η sin(η τ_close) under the normalization.

The switching sequence is defined by two dimensionless parameters a and b normalized by the electrical period T_elec = 2π/ν, with ν = √(1 - 1/(4Q²)). The parameter b gives the closed-switch duration Δτ_close = b * (2π/ν). The parameter a determines the shift of the center of the closed interval relative to the moment of maximum deformation (x_p = x̂_p). With the maximum deformation at τ = 0, the center of the closed interval occurs at τ_center = a * (2π/ν). Thus

τ_close = τ_center - Δτ_close/2 = (a - b/2) * (2π/ν).

During the open-switch period, the voltage changes by

Δu_p,open = cos((2a - b) π η) + cos((2a + b) π η)   (3)

(using the normalization x̂_p = 1, α/C_p = 1).

The steady-state voltage magnitude u_stat (> 0) is the positive solution of

|u_p(Δτ_close)| - u_stat + Δu_p,open = 0,   (4)

where u_p(Δτ_close) is the voltage at the end of the closed-switch period obtained by integrating (1) from τ = 0 to τ = Δτ_close with initial voltage u0 = u_stat. Equation (4) can be solved numerically for u_stat using a root-finding method (e.g., bisection or Newton) over a reasonable interval [0, 5] (typical voltage magnitudes are of order 1–10).



## Reproduction target

Implement the numerical steady-state solver described above. Then:

1. Compute u_stat for each tuple in the provided test set (see Step 2) and store the results in the voltage_table.
2. For the baseline η = 0.5, Q = 10, γ = 0, perform a grid search over a ∈ [-0.5, 0.5] and b ∈ [0.3, 0.7] with step sizes of at most 0.01 to find the (a_opt, b_opt) that maximizes u_stat. Record a_opt, b_opt, and that peak_voltage.
3. Using the same baseline with optimal switching (a = 0, b = 1/(2ν)), compute u_stat for γ = 0 (call it u0) and for γ = 0.2 (call it uγ). Compute the effective force factor α* = uγ / u0 (since α = 1, C_p = 1). Compute α_plus = 1 + 0.2. If |α* - α_plus| / α* ≤ 1e-5 set match = true, otherwise false.

Write all results into a single JSON file `/app/outputs/analytical_results.json` with the exact schema given in the Output contract section.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Implement steady-state solver
- Role: process
- Action: Write a Python module that implements the numerical steady-state solver described in the Mathematical model section. The module must provide a function `compute_u_stat(eta, Q, a, b, gamma)` that solves the normalized ODE (1) during the closed-switch period, computes the voltage change during the open period via (3), and finds u_stat by numerically solving equation (4) (e.g., using bisection or scipy.optimize). Use the fixed normalization α=1, C_p=1, x̂_p=1. The function returns u_stat as a float.
- Evidence: none

### Step 2: Compute voltage table, optimal switching, and equivalence
- Role: scored (load-bearing)
- Action: Using the implemented solver, generate a single JSON file `/app/outputs/analytical_results.json` containing three parts:

(I) `voltage_table`: compute `u_stat` for each of the following parameter tuples (all with α=1, C_p=1, x̂_p=1). The tuples to evaluate are:
- (η=0.5, Q=10, a=0.0, b=0.5, γ=0.0)
- (η=0.5, Q=10, a=0.25, b=0.5, γ=0.0)
- (η=0.2, Q=5, a=0.0, b=0.5, γ=0.0)
- (η=0.8, Q=20, a=0.0, b=0.45, γ=0.0)
- (η=0.5, Q=10, a=0.0, b=0.5, γ=0.1)
- (η=0.5, Q=20, a=0.1, b=0.55, γ=0.0)
- (η=0.3, Q=15, a=0.0, b=0.5, γ=0.2)
- (η=0.7, Q=8, a=0.0, b=0.5, γ=0.0)
- (η=0.5, Q=5, a=0.0, b=0.5, γ=0.0)
- (η=0.5, Q=30, a=-0.05, b=0.5, γ=0.0)
Store each result as an object with keys `eta`, `Q`, `a`, `b`, `gamma`, `u_stat`.

(II) `optimal_law`: for the baseline η=0.5, Q=10, γ=0, perform a grid search over `a` in [-0.5, 0.5] and `b` in [0.3, 0.7] with a step size of at most 0.01 (you may use a finer grid). Find the pair `(a_opt, b_opt)` that yields the largest `u_stat`. Record `a_opt`, `b_opt`, and `peak_voltage` (the max u_stat).

(III) `equivalence`: with the baseline (η=0.5, Q=10) and using optimal switching (a=0, b=1/(2ν)), compute `u_stat` for γ=0 (call it `u0`) and for γ=0.2 (call it `uγ`). Compute the effective force factor `alpha_eff = uγ / u0`. Compute `alpha_plus = 1 + 0.2`. Set `match = true` if `|alpha_eff - alpha_plus| / alpha_eff <= 1e-5`, else `false`. Store the object with keys `gamma` (0.2), `alpha_eff`, `alpha_plus`, `match`.

- Output file: `/app/outputs/analytical_results.json`
- Format: json
- Contract: {"voltage_table": [{"eta": float, "Q": float, "a": float, "b": float, "gamma": float, "u_stat": float}], "optimal_law": {"a_opt": float, "b_opt": float, "peak_voltage": float}, "equivalence": {"gamma": float, "alpha_eff": float, "alpha_plus": float, "match": bool}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/analytical_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### analytical_results.json
- path: `/app/outputs/analytical_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed stationary voltage amplitudes, optimal switching law parameters, and force factor equivalence verification. The voltage table now includes the gamma parameter per entry.
- schema:
  - `type`: object
  - `required`: `voltage_table`, `optimal_law`, `equivalence`
  - `properties`:
    - `voltage_table`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `eta`, `Q`, `a`, `b`, `gamma`, `u_stat`
        - `properties`:
          - `eta`:
            - `type`: number
          - `Q`:
            - `type`: number
          - `a`:
            - `type`: number
          - `b`:
            - `type`: number
          - `gamma`:
            - `type`: number
          - `u_stat`:
            - `type`: number
    - `optimal_law`:
      - `type`: object
      - `required`: `a_opt`, `b_opt`, `peak_voltage`
      - `properties`:
        - `a_opt`:
          - `type`: number
        - `b_opt`:
          - `type`: number
        - `peak_voltage`:
          - `type`: number
    - `equivalence`:
      - `type`: object
      - `required`: `gamma`, `alpha_eff`, `alpha_plus`, `match`
      - `properties`:
        - `gamma`:
          - `type`: number
        - `alpha_eff`:
          - `type`: number
        - `alpha_plus`:
          - `type`: number
        - `match`:
          - `type`: boolean

Notes: The exact parameter tuples for the voltage table are listed in the instruction. The checker will recompute the gold values from the same ODE-based numerical steady-state solver and compare the agents results within appropriate hidden tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "analytical_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "voltage_table",
          "optimal_law",
          "equivalence"
        ],
        "properties": {
          "voltage_table": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "eta",
                "Q",
                "a",
                "b",
                "gamma",
                "u_stat"
              ],
              "properties": {
                "eta": {
                  "type": "number"
                },
                "Q": {
                  "type": "number"
                },
                "a": {
                  "type": "number"
                },
                "b": {
                  "type": "number"
                },
                "gamma": {
                  "type": "number"
                },
                "u_stat": {
                  "type": "number"
                }
              }
            }
          },
          "optimal_law": {
            "type": "object",
            "required": [
              "a_opt",
              "b_opt",
              "peak_voltage"
            ],
            "properties": {
              "a_opt": {
                "type": "number"
              },
              "b_opt": {
                "type": "number"
              },
              "peak_voltage": {
                "type": "number"
              }
            }
          },
          "equivalence": {
            "type": "object",
            "required": [
              "gamma",
              "alpha_eff",
              "alpha_plus",
              "match"
            ],
            "properties": {
              "gamma": {
                "type": "number"
              },
              "alpha_eff": {
                "type": "number"
              },
              "alpha_plus": {
                "type": "number"
              },
              "match": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "description": "Computed stationary voltage amplitudes, optimal switching law parameters, and force factor equivalence verification. The voltage table now includes the gamma parameter per entry."
    }
  ],
  "notes": "The exact parameter tuples for the voltage table are listed in the instruction. The checker will recompute the gold values from the same ODE-based numerical steady-state solver and compare the agents results within appropriate hidden tolerances."
}
```

## How you are scored
A hidden verifier will independently recompute the stationary voltage amplitudes from the same approximate analytical model for the same parameter tuples, using a reference implementation. For each entry in your voltage_table, the absolute difference will be compared to a hidden tolerance. For the optimal switching law, the verifier checks that a_opt is within a tight range around the theoretically expected value of 0, that b_opt is within an appropriate range around 1/(2 ν) (where ν depends on Q), and that the peak voltage matches the value computed at (a=0, b=1/(2 ν)) to within a small tolerance. For the equivalence check, the verifier compares the computed α_eff to α + Cp γ with a strict relative tolerance. Each section is weighted, and the total reward is a weighted sum of the per-section scores. The exact tolerances and weights are hidden; you must compute accurate values from the model.
