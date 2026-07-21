# Time evolution and average interaction energy of a two-level dimer under resonant excitation

## Problem background
Two identical molecules form a dimer and are modeled as two-level systems. An excitation quantum can be shared between the molecules with initial probability amplitudes α and β satisfying α²+β²=1. The molecules interact via a dipole‑dipole coupling of strength V. The goal is to understand how the time evolution of the excitation wave functions and the resulting average interaction energy depend on the initial excitation amplitudes. This information reveals whether the dimer interaction can be tuned under resonant excitation, which is relevant for applications in gas‑phase chemistry and surface science.

## Mathematical model
The time evolution of the excitation wave functions ψ₁(t) and ψ₂(t) is governed by the coupled Schrödinger equations with an impulsive excitation at t = 0:

$$i\frac{d\psi_1}{dt} = V\psi_2 + i\alpha\,\delta(t),\qquad i\frac{d\psi_2}{dt} = V\psi_1 + i\beta\,\delta(t)\tag{1}$$

where δ(t) is the Dirac delta function, V is the dipole‑dipole coupling strength (a real constant), and α, β are real initial probability amplitudes obeying α²+β²=1.

Solving (1) via Fourier transformation yields the analytic time‑dependent wave functions:

$$\psi_1(t) = \frac{(\alpha+\beta)e^{-iVt} + (\alpha-\beta)e^{iVt}}{2},\qquad \psi_2(t) = \frac{(\alpha+\beta)e^{-iVt} - (\alpha-\beta)e^{iVt}}{2}\tag{5}$$

From these wave functions the average interaction energy is obtained:

$$\langle V \rangle = 2V\alpha\beta\tag{7}$$

Equations (5) and (7) are the exact analytic solutions that your solver must reproduce.

## Approach
Model each molecule as a two‑level system. The Schrödinger equation for the coupled system is written with a delta‑function initial excitation at t=0, leading to the pair of coupled differential equations (1). The solution proceeds by Fourier transformation, which converts the time‑domain equations into algebraic equations in the frequency domain. The time‑dependent wave functions are recovered by inverse Fourier transformation, giving the closed‑form results (5). From these wave functions the average interaction energy ⟨V⟩ is obtained by integration over frequency, yielding the compact expression (7). The task requires implementing a solver that, given arbitrary α, β, V, and a list of time points, can compute ψ₁(t), ψ₂(t), and ⟨V⟩. The solver may directly evaluate the analytic solutions (5) and (7), or numerically solve the time‑dependent Schrödinger equation (1); the outputs must match the analytic predictions within numerical tolerances.

## Reproduction target
Implement the solver described in the approach. Then, for the following test cases, compute the wave functions ψ₁(t) and ψ₂(t) at the specified time points and the average interaction energy ⟨V⟩. Write all results into `/app/outputs/verification_results.json` according to the output contract.

Test cases:
1. α = 1/√2, β = 1/√2, V = 1.0, time points: [0, 1, 2, 3, 4]
2. α = -1/√2, β = 1/√2, V = 1.0, time points: [0, 1, 2, 3, 4]
3. α = 0.6, β = 0.8, V = 0.5, time points: [0, 0.5, 1.0, 1.5]
4. α = 0.8, β = -0.6, V = 2.0, time points: [0, 0.2, 0.4, 0.6, 0.8, 1.0]

## Assets

- Python 3: python3
- NumPy: numpy

## Workflow steps

### Step 1: Implement the dimer model and solver
- Role: process
- Action: Implement the two‑level dimer system described in the mathematical model: two identical molecules with excitation amplitudes α and β (α²+β²=1) and dipole‑dipole coupling V. Write a function or script that, given α, β, V and an array of time points, computes the time‑dependent wave functions ψ₁(t) and ψ₂(t) and the average interaction energy ⟨V⟩ using either direct evaluation of the analytic solutions (Eqs. 5 and 7) or numerical integration of the differential equations (Eq. 1).
- Evidence: none

### Step 2: Evaluate test cases and write verification results
- Role: scored (load‑bearing)
- Action: Run the implemented solver on the specified test cases. For each case, compute the wave functions ψ₁(t), ψ₂(t) at the given time points and the average interaction energy ⟨V⟩. Write the results to verification_results.json.
- Output file: `/app/outputs/verification_results.json`
- Format: json
- Contract: {"test_cases": [{"alpha": float, "beta": float, "V": float, "time_points": [float,...], "psi1": [[real,imag],...], "psi2": [[real,imag],...], "average_energy": float}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/verification_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### verification_results.json
- path: `/app/outputs/verification_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Contains the computed excitation wave functions and average interaction energy for all test cases. The checker will recompute expected values from the analytic formulas and compare.
- schema:
  - `type`: object
  - `required`:
    - `test_cases`: array of test case objects
  - `items`:
    - `test_cases`:
      - `type`: object
      - `required`: `alpha`, `beta`, `V`, `time_points`, `psi1`, `psi2`, `average_energy`
      - `properties`:
        - `alpha`: float
        - `beta`: float
        - `V`: float
        - `time_points`: array of float
        - `psi1`: array of [float, float] pairs (real and imaginary parts)
        - `psi2`: array of [float, float] pairs (real and imaginary parts)
        - `average_energy`: float

Notes: The checker will recompute the expected average energy and wave functions using the analytic expressions derived in the model (average_energy = 2*V*alpha*beta, wave functions via exponential combinations of alpha, beta, V, and t). Comparisons will use appropriate floating‑point tolerances.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "verification_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "test_cases": "array of test case objects"
        },
        "items": {
          "test_cases": {
            "type": "object",
            "required": [
              "alpha",
              "beta",
              "V",
              "time_points",
              "psi1",
              "psi2",
              "average_energy"
            ],
            "properties": {
              "alpha": "float",
              "beta": "float",
              "V": "float",
              "time_points": "array of float",
              "psi1": "array of [float, float] pairs (real and imaginary parts)",
              "psi2": "array of [float, float] pairs (real and imaginary parts)",
              "average_energy": "float"
            }
          }
        }
      },
      "description": "Contains the computed excitation wave functions and average interaction energy for all test cases. The checker will recompute expected values from the analytic formulas and compare."
    }
  ],
  "notes": "The checker will recompute the expected average energy and wave functions using the analytic expressions derived in the model (average_energy = 2*V*alpha*beta, wave functions via exponential combinations of alpha, beta, V, and t). Comparisons will use appropriate floating‑point tolerances."
}
```

## How you are scored
A hidden verifier will read your `verification_results.json`. For each test case it will recompute the expected wave functions and average interaction energy using the analytic solutions derived from the two‑level dimer model. It will compare your computed ψ1, ψ2, and ⟨V⟩ to these expected values within appropriate numerical tolerances. All test cases must pass the comparison to receive full credit. The verifier does not rely on external data; it only uses the same parameters (α, β, V, time points) that you were given.