# Compute dynamical transition temperature and high-temperature expansion energy for a glass matrix model

## Problem background
The glass matrix model consists of N particles, each represented by a P-component Ising spin vector with entries ±1. The energy function is

H = (1/(4N)) Σ_{i≠j} (Σ_a S_i^a S_j^a)^2 – (1/4) P N.

When P is of the same order as N, the system exhibits glassy dynamics and a dynamical phase transition is expected. A replica mean-field theory predicts a glass temperature T_g that depends on the ratio α = P/N. This task focuses on two representative values: α = 0.3 (P = 30, N = 100) and α = 0.5 (P = 40, N = 80). The goal is to compute the high-temperature expansion energy density as a function of temperature and to determine the dynamical transition temperature from the replica theory with a one-step replica-symmetry-breaking ansatz and a marginal-stability condition.

## Approach
The analysis proceeds in two parts.

### High-temperature expansion
For small α = P/N, the leading-order high-temperature expansion gives the internal energy density (energy per degree of freedom) as

e(T) = (α/4) * ( 1/(1 + β) - 1 )   with β = 1/T.

This analytic formula is valid for the paramagnetic phase and will be evaluated on a temperature grid. (No Monte Carlo simulation is needed.)

### Replica mean-field equations (one-step RSB, marginal stability)
To find the dynamical transition temperature Tg, the replica theory with a one-step replica-symmetry-breaking (1-RSB) ansatz is used, assuming homogeneity among component indices. The order parameters are (q1, q0, Λ1, Λ0). The free energy density (βf) per degree of freedom is:

βf = (α/4)[ (1/m) ln(1+β X_m) + (1 - 1/m) ln(1+β X_1) + β Q0/(1+β X_m) - β ]
    + 1/4 [ (m-1) Λ1 Q1 - m Λ0 Q0 ] + 1/4 [ (m-1) q1^2 Λ1 - m q0^2 Λ0 ]
    + (1/2) q1 Λ1 - (1/m) ∫ Dx ln ∫ Dy (2 cosh A)^m

where
  X_1 = 1 - Q1,  X_m = 1 - Q1 + m (Q1 - Q0),
  Q1 = q1^2, Q0 = q0^2,
  A = √(q0 Λ0) x + √(q1 Λ1 - q0 Λ0) y,
  Dx = exp(-x^2/2) dx/√(2π), Dy analogously,
  m is the RSB block-size parameter.

The self-consistent equations for the order parameters are:

Λ0 = α β^2 Q0 / (1 + β X_m)^2
Λ1 = (α β / m)[ 1/(1+β X_1) - 1/(1+β X_m) ] + α β^2 Q0 / (1+β X_m)^2
q0 = ∫ Dx [ 〈S〉 ]^2
q1 = ∫ Dx 〈S^2 〉

where
  S = tanh A,
  the overline average 〈...〉 is defined as ∫ Dy (⋯) cosh^m A / ∫ Dy cosh^m A.

The dynamical transition temperature Tg is identified as the temperature at which a solution with m=1 exists and the replicon mode becomes marginal, i.e. the product of eigenvalues satisfies

1 - 2  λ_Λ  λ_Q  = 0

with
  λ_Q = α β^2 / (1 + β X_1)^2   (evaluated at m=1, q0=Λ0=0),
  λ_Λ = q1^2  ⟨⟨ [1 - (tanh A)^2]^2 ⟩⟩   where ⟨⟨·⟩⟩ denotes the average over x and y with the measure appropriate for m=1.

At m=1 the equations simplify considerably (q0=Λ0=0, and the y-average reduces to a simple Gaussian). The solver searches for the temperature T that simultaneously satisfies the saddle-point equations and the marginal-stability condition.

All calculations are numerical/analytic; no Monte Carlo simulation is required.

## Reproduction target
For each α = 0.3 and α = 0.5:

1. Compute the high-temperature expansion energy density e(T) on a temperature grid covering the low-temperature regime up to about 0.15. Store the results in `high_T_energy.csv` as a table with columns `temperature` (float), `energy` (float), and `alpha` (float).

2. Using the one-step RSB solver with the marginal-stability condition, find the dynamical transition temperature T_g. Write the two temperatures to `tg_values.json` as a JSON object with keys `"alpha_0_3"` and `"alpha_0_5"` mapping to the computed Tg values (floats).

All output files must be placed under `/app/outputs`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement high-temperature expansion formulas
- Role: process
- Action: Implement the high-temperature expansion formulas for the glass matrix model: Hamiltonian parameters, partition function, free energy, entropy, and internal energy density for small alpha (P/N). The formulas correspond to the leading-order expansion and yield analytic expressions for thermodynamic densities.
- Evidence: none

### Step 2: Compute high-temperature expansion energy
- Role: scored (load-bearing)
- Action: Using the implemented formulas, compute the energy density e(T) for alpha = 0.3 (P=30, N=100) and alpha = 0.5 (P=40, N=80) over a temperature grid covering the low-temperature regime up to about 0.15. Write the results to high_T_energy.csv with columns for temperature, energy, and alpha.
- Output file: `/app/outputs/high_T_energy.csv`
- Format: csv
- Contract: temperature (float, dimensionless), energy (float, energy density), alpha (float, ratio P/N)
- Scoring: scored by hidden verifier

### Step 3: Implement RSB saddle-point solver with marginal stability
- Role: process
- Action: Implement the one-step replica-symmetry-breaking (RSB) saddle-point equations and the marginal stability condition for the glass matrix model. Solve the combined system numerically to find the dynamical transition temperature Tg for a given alpha. Implementation includes the free energy expression, order-parameter equations, marginality condition, and an iterative temperature search to locate the point where the replicon mode becomes marginal (m=1).
- Evidence: `/app/outputs/rsb_solver_log.txt`

### Step 4: Report dynamical transition temperatures
- Role: scored (load-bearing)
- Action: Write the computed dynamical transition temperatures Tg for alpha = 0.3 and alpha = 0.5 to tg_values.json. The JSON object must contain keys 'alpha_0_3' and 'alpha_0_5' with the predicted temperatures.
- Output file: `/app/outputs/tg_values.json`
- Format: json
- Contract: {"alpha_0_3": float, "alpha_0_5": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/high_T_energy.csv`
- `/app/outputs/tg_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### high_T_energy.csv
- path: `/app/outputs/high_T_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with three columns: temperature (float), energy (float), and alpha (float). Each row is one temperature point for one alpha value. The energy must be computed from the high-temperature expansion formula.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `energy`, `alpha`
  - `units`:
    - `temperature`: dimensionless temperature
    - `energy`: energy density
    - `alpha`: ratio P/N

### tg_values.json
- path: `/app/outputs/tg_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON object with keys 'alpha_0_3' and 'alpha_0_5', each mapping to the predicted dynamical transition temperature Tg (float) for that alpha value.
- schema:
  - `type`: object
  - `required`:
    - `alpha_0_3`: number
    - `alpha_0_5`: number
  - `items`:
    - `alpha_0_3`:
      - `type`: number
    - `alpha_0_5`:
      - `type`: number

Notes: The high-temperature expansion energy is deterministic from the input alpha and temperature; the agent must implement the formula correctly. The RSB solver is a numerical procedure; the output Tg values must match the paper's reported values within a tolerance determined by the hidden checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "high_T_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "energy",
          "alpha"
        ],
        "units": {
          "temperature": "dimensionless temperature",
          "energy": "energy density",
          "alpha": "ratio P/N"
        }
      },
      "description": "CSV file with three columns: temperature (float), energy (float), and alpha (float). Each row is one temperature point for one alpha value. The energy must be computed from the high-temperature expansion formula."
    },
    {
      "file": "tg_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha_0_3": "number",
          "alpha_0_5": "number"
        },
        "items": {
          "alpha_0_3": {
            "type": "number"
          },
          "alpha_0_5": {
            "type": "number"
          }
        }
      },
      "description": "JSON object with keys 'alpha_0_3' and 'alpha_0_5', each mapping to the predicted dynamical transition temperature Tg (float) for that alpha value."
    }
  ],
  "notes": "The high-temperature expansion energy is deterministic from the input alpha and temperature; the agent must implement the formula correctly. The RSB solver is a numerical procedure; the output Tg values must match the paper's reported values within a tolerance determined by the hidden checker."
}
```

## How you are scored
A hidden verifier checks each scored artifact independently.

- For `high_T_energy.csv`, the verifier recomputes the expected energy from the known high-temperature expansion formula and compares each row within a small absolute tolerance. This check confirms that the formula is implemented correctly.
- For `tg_values.json`, the reported transition temperatures are compared to hidden reference values with a relative tolerance that accounts for minor numerical differences from the solver.

The final reward (0 to 1) is a weighted combination of the scores from these two checks. Reporting a plausible number is not sufficient; the verifier recomputes or cross-checks the submitted results.
