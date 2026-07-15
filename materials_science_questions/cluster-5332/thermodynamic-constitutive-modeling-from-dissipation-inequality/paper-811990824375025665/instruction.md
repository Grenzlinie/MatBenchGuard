# Energetic Time‑Step Bounds for Characteristic Approximations in Rate‑Type Viscoelasticity

## Problem background
The one‑dimensional motion of a rate‑type viscoelastic body is governed by a semilinear hyperbolic system of PDEs. When the equilibrium stress–strain curve can have a negative slope (e.g., of van der Waals type), the discrete total energy of a numerical solution may fail to be non‑increasing over time unless the time step is bounded. The standard method of characteristics yields two numerical approximations: a first‑order scheme and a second‑order scheme. For isolated‑body problems, sufficient conditions on the time integration step have been derived that guarantee the discrete total energy is a non‑increasing function of the time level, consistent with the second law of thermodynamics. The main theoretical results are upper bounds $h'_m$ (first approximation) and $h''_m$ (second approximation) expressed in terms of the material constants, and the inequality $h''_m \leq h'_m$.

## Approach
The task considers an isolated viscoelastic bar of length $l = 1$. The governing system in characteristic variables $(p,q,r)$ reads:

$$
\frac{\partial p}{\partial t} - c\frac{\partial p}{\partial x} = G,\quad
\frac{\partial q}{\partial t} + c\frac{\partial q}{\partial x} = G,\quad
\frac{\partial r}{\partial t} = G,
$$
where $c = \sqrt{E/\varrho_0}$ and $G$ is a function of $p,q,r$ that encodes the viscoelastic relaxation $g(\varepsilon,\sigma) = -k(\varepsilon,\sigma)\,[\sigma - \sigma_R(\varepsilon)]$ with $k_1 \le k(\varepsilon,\sigma) \le k_2$.

The material constants are:

$$
E = 200,\quad E_3 = 50,\quad M = 20,\quad k_1 = 0.5,\quad k_2 = 1.0.
$$

The equilibrium curve $\sigma_R(\varepsilon)$ is piecewise linear:

$$
\sigma_R(\varepsilon) = \begin{cases}
E_3 \varepsilon, & \varepsilon \le \varepsilon_M,\\
\sigma_M - E_2 (\varepsilon - \varepsilon_M), & \varepsilon_M < \varepsilon < \varepsilon_m,\\
\sigma_m + E_1 (\varepsilon - \varepsilon_m), & \varepsilon \ge \varepsilon_m,
\end{cases}
$$
with $\varepsilon_M = 0.02$, $\varepsilon_m = 0.05$, $E_1 = 10$, $E_2 = 20$, $\sigma_M = E_3 \varepsilon_M$, and $\sigma_m = \sigma_M - E_2 (\varepsilon_m - \varepsilon_M)$.

The theoretical bounds derived for the isolated‑body problem are:

$$
h'_m = \frac{2(E - E_3)}{k_2 (E + M)},\qquad
h''_m = \frac{2}{k_2}\cdot \frac{E (E - E_3)}{E (E + M) + M (E - E_3)}.
$$

Implement the first‑order numerical scheme (one integration of $G$ per step) and the second‑order scheme (using a predictor step of $G$).  The discrete total energy at time level $j$ is

$$
e^j = \frac12 \Bigl(\sum_{i=0}^{N-1} + \sum_{i=1}^N\Bigr)
\biggl[ \frac{p_i^2 + q_i^2}{4E} + \varphi(r_i) \biggr],
$$
where $\varphi$ is the free‑energy contribution (to be derived from the equilibrium curve).

The initial conditions are a smooth strain perturbation on $[0,1]$:

$$
\varepsilon(x,0) = A \exp\!\bigl(-(x - 0.5)^2/(2\sigma^2)\bigr),\quad
v(x,0) = 0,\quad \sigma(x,0) = \sigma_R(\varepsilon(x,0))
$$
with $A = 0.02$, $\sigma = 0.05$, and $N = 200$ spatial points.

Simulate both approximations for two time‑step sizes: $h = 0.5\,h'_m$ and $h = 1.5\,h'_m$, each for a sufficient number of time levels (e.g., until $t=1$).  For each run examine the discrete total energy sequence $\{e^j\}$; set `energy_nonincreasing = true` if the maximum energy after the initial level never exceeds the initial energy.

Finally compute the ratio $h''_m / h'_m$ and check that $h''_m \le h'_m$ holds.

## Reproduction target
Produce a single JSON file `results.json` with the following fields:

- **bounds**: `h_m_prime` (computed $h'_m$) and `h_m_double_prime` (computed $h''_m$).
- **simulations**: an array of four objects, each reporting `approximation` ("first" or "second"), the time step `h` ($0.5\,h'_m$ or $1.5\,h'_m$), and the boolean `energy_nonincreasing`.
- **ratio_check**: `h_m_double_prime / h_m_prime` and `inequality_holds` (true if $h''_m \le h'_m$).

All quantities must be computed from the given material constants and the implemented numerical schemes; no external data or precomputed values are allowed.

## Assets

- NumPy: pypi:numpy
- SciPy: pypi:scipy

## Workflow steps

### Step 1: Implement the characteristic schemes
- Role: process
- Action: Implement the first-order and second-order numerical approximations for the isolated‑body problem in the characteristic variables (p, q, r) with the piecewise‑linear equilibrium function. Prepare a function that computes the discrete total energy at each time level.
- Evidence: none

### Step 2: Simulate and report bounds and energy monotonicity
- Role: scored (load-bearing)
- Action: Using the material constants E, E₃, M, k₁, k₂ and a consistent set of initial conditions, compute the theoretical bounds h′_m and h″_m from their algebraic formulas. Run the first and second approximations for two time steps: h = 0.5·h′_m and h = 1.5·h′_m, each for a sufficient number of time levels. For each run examine the discrete total energy sequence and set energy_nonincreasing = true if the maximum energy after the initial level is never greater than the initial energy. Collect all results into results.json with keys: bounds, simulations, ratio_check.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"bounds": {"h_m_prime": "float", "h_m_double_prime": "float"}, "simulations": [{"approximation": "first", "h": "float", "energy_nonincreasing": "bool"}, {"approximation": "first", "h": "float", "energy_nonincreasing": "bool"}, {"approximation": "second", "h": "float", "energy_nonincreasing": "bool"}, {"approximation": "second", "h": "float", "energy_nonincreasing": "bool"}], "ratio_check": {"h_m_double_prime/ h_m_prime": "float", "inequality_holds": "bool"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The agent's computed energetic time‑step bounds, energy‑monotonicity flags from simulations, and the inequality check. The checker recomputes all values (bounds, flags, ratio) from the same material constants and initial conditions, comparing each field with appropriate tolerance.
- schema:
  - `type`: object
  - `required`: `bounds`, `simulations`, `ratio_check`
  - `properties`:
    - `bounds`:
      - `type`: object
      - `required`: `h_m_prime`, `h_m_double_prime`
      - `properties`:
        - `h_m_prime`:
          - `type`: number
        - `h_m_double_prime`:
          - `type`: number
    - `simulations`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `approximation`, `h`, `energy_nonincreasing`
        - `properties`:
          - `approximation`:
            - `type`: string
            - `enum`: `first`, `second`
          - `h`:
            - `type`: number
          - `energy_nonincreasing`:
            - `type`: boolean
    - `ratio_check`:
      - `type`: object
      - `required`: `h_m_double_prime/ h_m_prime`, `inequality_holds`
      - `properties`:
        - `h_m_double_prime/ h_m_prime`:
          - `type`: number
        - `inequality_holds`:
          - `type`: boolean

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "bounds",
          "simulations",
          "ratio_check"
        ],
        "properties": {
          "bounds": {
            "type": "object",
            "required": [
              "h_m_prime",
              "h_m_double_prime"
            ],
            "properties": {
              "h_m_prime": {
                "type": "number"
              },
              "h_m_double_prime": {
                "type": "number"
              }
            }
          },
          "simulations": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "approximation",
                "h",
                "energy_nonincreasing"
              ],
              "properties": {
                "approximation": {
                  "type": "string",
                  "enum": [
                    "first",
                    "second"
                  ]
                },
                "h": {
                  "type": "number"
                },
                "energy_nonincreasing": {
                  "type": "boolean"
                }
              }
            }
          },
          "ratio_check": {
            "type": "object",
            "required": [
              "h_m_double_prime/ h_m_prime",
              "inequality_holds"
            ],
            "properties": {
              "h_m_double_prime/ h_m_prime": {
                "type": "number"
              },
              "inequality_holds": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "description": "The agent's computed energetic time‑step bounds, energy‑monotonicity flags from simulations, and the inequality check. The checker recomputes all values (bounds, flags, ratio) from the same material constants and initial conditions, comparing each field with appropriate tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently recompute the theoretical bounds $h'_m$ and $h''_m$ from the same material constants and compare them to your `bounds` within a tolerance. It will re‑run the first‑ and second‑order numerical schemes with the same parameters, time steps, and initial conditions, and verify that each `energy_nonincreasing` flag matches the behavior of the recomputed energy sequence. Finally, it will check that the ratio $h''_m / h'_m$ satisfies $0.5 < h''_m / h'_m \le 1$ and that `inequality_holds` is true. The final reward is a weighted combination of these checks. Simply reporting a number without underlying computation will not pass the verification.
