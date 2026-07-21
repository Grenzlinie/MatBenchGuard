# Compute order parameters and transition temperatures from replica-symmetric saddle-point equations

## Problem background
This task addresses a classical XY spin-glass model where both spins (fast variables) and their exchange couplings (slow variables) evolve stochastically on widely separated time scales. The fast spins follow Langevin dynamics with an instantaneous Boltzmann distribution, while the couplings change slowly in response to local spin correlations and external quenched random biases. Using replica mean-field theory with two replica levels, the model yields a phase diagram with two spin-glass order parameters, q0 and q1, which characterize two distinct frozen phases. Your job is to compute the temperature dependence of these order parameters for two given temperature ratios n, thereby mapping the phase boundaries. The outcome is a pair of curves from which transition temperatures must be identified—an open quantitative problem whose solution verifies the replica-symmetric saddle-point analysis.

## Approach
The core mathematical objects are the replica-symmetric saddle-point equations that determine the spin-glass order parameters q0 and q1. Let β = 1/T (spin inverse temperature) and define

Ξ = β √[ ½ (\tilde{J} + \tilde{B}) q₁ − ½ \tilde{B} q₀ ] .

The fixed parameters are \tilde{B} = 1, \tilde{J} = 3 (and B₀ = 0). The replica ratio n = \tilde{β} / β is the given control parameter (2.0 or 5.0).

**Equation for q₀**

q₀ = ∫₀^∞ dx  x e^{−x²/2}  [  N₁(x) / D(x)  ]²

**Equation for q₁**

q₁ = ∫₀^∞ dx  x e^{−x²/2}   N₂(x) / D(x)

where the auxiliary integrals over z are:

N₁(x) = ∫₀^∞ dz  z e^{−z²/2}  I₀(z Ξ)^{n−1}  I₁(z Ξ)  I₁( z x β Ξ^{-1} √[½ \tilde{B} q₀] )

D(x)  = ∫₀^∞ dz  z e^{−z²/2}  I₀(z Ξ)^n        I₀( z x β Ξ^{-1} √[½ \tilde{B} q₀] )

N₂(x) = ∫₀^∞ dz  z e^{−z²/2}  I₀(z Ξ)^{n−2}  I₁(z Ξ)²  I₀( z x β Ξ^{-1} √[½ \tilde{B} q₀] )

Here I₀ and I₁ are modified Bessel functions of the first kind (scipy.special.iv). All integrals are over the positive real axis; the integrands decay rapidly for large arguments.

These two coupled equations must be solved self-consistently for q₀(T) and q₁(T) at each temperature. You will implement them numerically using standard tools such as scipy for integration and special functions, and solve for q₀ and q₁ over a temperature grid for n = 2.0 and n = 5.0 (at least 20 points each, covering 0.1 ≤ T ≤ 2.0). Once the curves q₀(T) and q₁(T) are obtained, you will estimate the temperature at which each order parameter first departs from zero—these mark the transitions between paramagnetic and spin-glass phases. The approach is purely numerical; no Monte Carlo simulation of the full dynamics is required, as the saddle-point equations are the minimal route to the phase diagram.

## Reproduction target
Produce two CSV files:
- `/app/outputs/step_01_order_parameters.csv`: For n = 2.0 and n = 5.0, compute q0 and q1 at no fewer than 20 temperature points each, distributed over the interval 0.1 ≤ T ≤ 2.0. The file must contain columns: `n` (float), `T` (float), `q0` (float), `q1` (float).
- `/app/outputs/step_02_transition_temperatures.csv`: From the computed curves, determine for each n the P→SG1 transition temperature `T_P_SG1` at which q1 first becomes positive, and the SG1→SG2 transition temperature `T_SG1_SG2` at which q0 becomes positive (if present). The file must contain columns: `n` (float), `T_P_SG1` (float), `T_SG1_SG2` (float). If a particular transition does not occur for a given n, leave the corresponding cell empty.

The target is self-contained; your goal is simply to produce these numerical outputs according to the specifications.

## Assets

- scipy: scipy

## Workflow steps

### Step 1: Solve RS order parameter equations for q0(T) and q1(T)
- Role: scored (load-bearing)
- Action: Implement the replica-symmetric saddle-point equations that determine the spin-glass order parameters q0 and q1 as functions of temperature T for a given ratio n. The equations involve integrals over Gaussian distributions and modified Bessel functions I0 and I1. Use the parameters B0=0, \tilde{B}=1, \tilde{J}=3. For each n=2.0 and n=5.0, solve numerically for q0 and q1 over a grid of temperatures T from 0.1 to 2.0 (at least 20 points). Output the results to /app/outputs/step_01_order_parameters.csv.
- Output file: `/app/outputs/step_01_order_parameters.csv`
- Format: csv
- Contract: Columns: n (float), T (float), q0 (float), q1 (float).
- Scoring: scored by hidden verifier

### Step 2: Determine transition temperatures
- Role: scored
- Action: From the computed q1(T) and q0(T) curves, estimate the P→SG1 transition temperature T_P_SG1 where q1 first becomes positive (continuous or jump), and the SG1→SG2 transition temperature T_SG1_SG2 where q0 becomes positive. For n=5.0, where SG1→SG2 may not occur, leave the cell empty. Output to /app/outputs/step_02_transition_temperatures.csv.
- Output file: `/app/outputs/step_02_transition_temperatures.csv`
- Format: csv
- Contract: Columns: n (float), T_P_SG1 (float), T_SG1_SG2 (float); empty allowed.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_order_parameters.csv`
- `/app/outputs/step_02_transition_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_order_parameters.csv
- path: `/app/outputs/step_01_order_parameters.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: The temperature dependence of the spin-glass order parameters q0 and q1 for each n value. The checker will compute the mean absolute error between the submitted curves and a hidden reference solution; meeting or beating the threshold (MAE < 0.02) earns full credit.
- schema:
  - `type`: table
  - `required_columns`: `n`, `T`, `q0`, `q1`

### step_02_transition_temperatures.csv
- path: `/app/outputs/step_02_transition_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The estimated transition temperatures T_P_SG1 and T_SG1_SG2. The checker will compare the submitted values to hidden gold values within a tolerance of ±0.05.
- schema:
  - `type`: table
  - `required_columns`: `n`, `T_P_SG1`, `T_SG1_SG2`

Notes: The task is a minimal reproduction of the replica-symmetric phase diagram analysis. It does not require full Langevin dynamics simulations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_order_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "T",
          "q0",
          "q1"
        ]
      },
      "description": "The temperature dependence of the spin-glass order parameters q0 and q1 for each n value. The checker will compute the mean absolute error between the submitted curves and a hidden reference solution; meeting or beating the threshold (MAE < 0.02) earns full credit."
    },
    {
      "file": "step_02_transition_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "T_P_SG1",
          "T_SG1_SG2"
        ]
      },
      "description": "The estimated transition temperatures T_P_SG1 and T_SG1_SG2. The checker will compare the submitted values to hidden gold values within a tolerance of ±0.05."
    }
  ],
  "notes": "The task is a minimal reproduction of the replica-symmetric phase diagram analysis. It does not require full Langevin dynamics simulations."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage and combines the results into a final reward between 0 and 1. For step 1, the verifier recomputes the q0 and q1 curves from the same target equations and compares your submitted values to a hidden reference solution; the score is based on the mean absolute error across the curves, with full credit for solutions meeting a predefined accuracy threshold. For step 2, the verifier compares your extracted transition temperatures to hidden reference values within a fixed tolerance. Only the verifier's own recomputation determines the reward—reproducing a particular pre‑known number is neither required nor sufficient. The scoring is monotonic in solution quality: a result that equals or exceeds the reference quality never receives a lower score.
