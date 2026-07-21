# Mean-field and Monte Carlo study of square artificial spin ice

## Problem background
Square artificial spin ice consists of elongated magnetic islands whose Ising-like magnetizations interact via frustrated dipolar couplings. The ground state is a checkerboard tiling of type I vertices. Understanding how thermal fluctuations induce domain formation and yield a critical temperature is essential for interpreting experiments and designing thermally active spin ice systems. This task asks you to compute the critical temperature and the type I vertex population for a specific set of coupling parameters and to verify the thermal stability of type I order via a Monte Carlo simulation.

## Approach
The system is described by three nearest-neighbour dipolar interactions (Jn, Jnn, Jnnn) and an anisotropy barrier K. In a mean-field approximation, each island's magnetization responds to a local effective field via the Langevin thermal average, and spins reverse when an instability condition is met. The critical temperature above which type I order is lost is obtained by linearizing the self-consistent equation for a uniform type I tiling. To study thermal effects beyond mean field, a Monte Carlo simulation using the heat-bath algorithm is performed for Ising-like spins, with the same reduced coupling parameters and zero disorder. Two complementary computational pathways are followed: (1) a self-consistent mean-field algorithm on a finite lattice without disorder, starting from a perfect type I configuration and sweeping temperature, yields the temperature-dependent type I population and the critical temperature; (2) a Monte Carlo simulation equilibrated from a random initial state at a fixed temperature provides the steady-state type I vertex population, testing the thermal formation of ground-state order in the absence of disorder.

## Reproduction target
Compute the mean-field critical temperature Tc (in reduced units T0 = J0/k_B) for the reduced couplings Jn = 1.5 J0, Jnn = 0.7 J0, Jnnn = 0.3 J0 and anisotropy barrier K = 10 J0, and record the temperature-dependent type I vertex population n1 from a zero-disorder mean-field simulation. Also, run a Monte Carlo simulation of the same system starting from a random configuration at temperature T = T0 with zero disorder, and report the final type I vertex population n1.

## Assets

- Python 3: python
- NumPy: numpy

## Workflow steps

### Step 1: Mean-field critical temperature and domain population
- Role: scored
- Action: From the reduced couplings Jn = 1.5 J0, Jnn = 0.7 J0, Jnnn = 0.3 J0 and anisotropy barrier K = 10 J0, compute the local effective field h_loc = 2(2Jn - Jnn + Jnnn) + K/2. Derive the mean-field self-consistency equation for a uniform type I tiling, linearize it to obtain the critical temperature condition k_B T_c = h_loc / 3, and evaluate Tc in units of T0 = J0/k_B. Then implement the iterative mean-field algorithm (Langevin thermal averaging with instability condition) on a finite square lattice of 640 vertices (open boundaries) for a range of temperatures without disorder, starting from a perfect type I tiling. Record the temperature-dependent type I vertex population n1.
- Output file: `/app/outputs/step_01_mean_field_results.json`
- Format: json
- Contract: {"Tc": number, "n1_vs_temperature": [{"temperature": number, "n1": number}]}
- Scoring: scored by hidden verifier

### Step 2: Monte Carlo simulation of square ice
- Role: scored (load-bearing)
- Action: Implement a heat-bath Monte Carlo simulation of Ising-like spins on a finite square lattice with the same nearest-neighbour couplings Jn, Jnn, Jnnn and anisotropy barrier K. Start from a random configuration at temperature T = T0 (with T0 = J0/k_B), use zero disorder, equilibrate for an appropriate number of Monte Carlo sweeps, and compute the final type I vertex population n1.
- Output file: `/app/outputs/step_02_mc_results.json`
- Format: json
- Contract: {"n1_at_T0": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mean_field_results.json`
- `/app/outputs/step_02_mc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mean_field_results.json
- path: `/app/outputs/step_01_mean_field_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Mean-field critical temperature and vertex population vs. temperature.
- schema:
  - `type`: object
  - `required`:
    - `Tc`: number (reduced units T0)
    - `n1_vs_temperature`: array of {temperature: number, n1: number}

### step_02_mc_results.json
- path: `/app/outputs/step_02_mc_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Type I vertex population from Monte Carlo simulation at T=T0.
- schema:
  - `type`: object
  - `required`:
    - `n1_at_T0`: number (type I population fraction)

Notes: The hidden checker compares Tc to the paper-reported value (absolute tolerance 0.1) and checks n1_at_T0 >= 0.8. Structural check on n1_vs_temperature (sharp drop near Tc) may be performed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mean_field_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc": "number (reduced units T0)",
          "n1_vs_temperature": "array of {temperature: number, n1: number}"
        }
      },
      "description": "Mean-field critical temperature and vertex population vs. temperature."
    },
    {
      "file": "step_02_mc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "n1_at_T0": "number (type I population fraction)"
        }
      },
      "description": "Type I vertex population from Monte Carlo simulation at T=T0."
    }
  ],
  "notes": "The hidden checker compares Tc to the paper-reported value (absolute tolerance 0.1) and checks n1_at_T0 >= 0.8. Structural check on n1_vs_temperature (sharp drop near Tc) may be performed."
}
```

## How you are scored
A hidden verifier will independently examine the contents of each scored output file listed in the output contract. For the mean-field results, it will compare the reported Tc against the correct value(s) and check that n1 vs temperature shows a sharp drop near the critical point. For the Monte Carlo results, the reported n1 at T=T0 will be checked against a required threshold. The final reward is a weighted combination of the scores from each artifact. The verifier does not trust self-reported numbers; your task is to produce the correct outputs through correct computations.
