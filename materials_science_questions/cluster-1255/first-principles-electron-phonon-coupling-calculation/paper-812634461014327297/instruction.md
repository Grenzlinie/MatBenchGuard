# Polaron Ground-State Energy Lower Bound and Effective Mass Computation

## Problem background
The polaron describes an electron moving in a polar crystal lattice, coupled to the quantized lattice vibrations (phonons). The strength of this electron-phonon interaction is governed by the dimensionless coupling constant α. Two fundamental quantities characterize the polaron: the ground-state energy E₀(α) and the effective mass m*(α). Despite decades of theoretical work, obtaining rigorous bounds for these quantities has been challenging. This task is based on a variational method that yields a rigorous lower bound for the ground-state energy and an analytic expression for the effective mass, valid for all coupling strengths. The method replaces the quartic (momentum‑squared) term in the Fröhlich Hamiltonian with a positive‑definite quadratic operator, leading to a set of algebraic equations that can be solved numerically for any α. The reproduction task focuses on computing E₀ and m*/m by implementing this procedure.

## Approach
The computation proceeds by introducing a vector operator Z(k) that modifies the original Hamiltonian H = H₂ + H₁, where H₂ is chosen to be manifestly positive‑definite. Optimizing the form of Z(k) reduces the problem to a single dimensionless parameter p. Maximizing the lower-bound energy expression with respect to p yields an implicit equation relating p and α:  
p⁴ [1 − 2α/(3p)] = 1  .  
Given a numerical solution for p, the ground‑state energy lower bound is  
E₀ = −3 (p²−1)(p²+3) / (4p²)  .  
The effective mass ratio is obtained from the same p via  
m*/m = ( (p²−1)(p⁴+2p²−2) / (p²+1) ) + 1  .  
The task is therefore to numerically solve the implicit equation for p for a range of coupling constants α, and then evaluate E₀ and m*/m using the closed‑form expressions. The work does not require any external dataset; all computations are self‑contained and can be performed with standard numerical tools (e.g., root‑finding in Python).

## Reproduction target
For the following set of coupling constants α: 0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, solve the parametric equation p⁴ [1 − 2α/(3p)] = 1 to obtain p. From each p compute the corresponding ground‑state energy lower bound E₀ and effective mass ratio m*/m using the formulas given in the Approach. Write the results to a CSV file /app/outputs/step_01_results.csv with columns: alpha, p, E0, m_star_over_m. The hidden verifier will check that each reported p satisfies the implicit equation, that E₀ and m*/m are correctly recomputed from p, and that the asymptotic behaviour for large α is consistent with the expected scaling (E₀ proportional to −α² and m*/m proportional to α⁴).

## Assets

- Python with NumPy and SciPy: python3, numpy, scipy

## Workflow steps

### Step 1: Compute lower bound and effective mass
- Role: scored (load-bearing)
- Action: Implement the polaron lower bound variational method: for the set of coupling constants α = 0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, numerically solve the maximization condition p⁴[1 − 2α/(3p)] = 1 to obtain p. Compute the ground-state energy lower bound E₀ = −3(p²−1)(p²+3)/(4p²) and the effective mass ratio m*/m = ( (p²−1)(p⁴+2p²−2)/(p²+1) + 1 ). Write results to the output CSV.
- Output file: `/app/outputs/step_01_results.csv`
- Format: csv
- Contract: CSV with header: alpha, p, E0, m_star_over_m. All values are dimensionless floating-point numbers. Must contain exactly one row for each α in {0.1, 0.5, 1, 2, 5, 10, 20, 50, 100}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.csv
- path: `/app/outputs/step_01_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file with columns: alpha (coupling constant), p (variational parameter), E0 (ground‑state energy lower bound), m_star_over_m (effective mass ratio). Must contain rows for α in {0.1, 0.5, 1, 2, 5, 10, 20, 50, 100}. The checker recomputes and verifies consistency and asymptotic scaling.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `p`, `E0`, `m_star_over_m`
  - `units`:
    - `alpha`: dimensionless
    - `p`: dimensionless
    - `E0`: dimensionless
    - `m_star_over_m`: dimensionless

Notes: The task focuses strictly on the ground-state energy lower bound and effective mass; expectation values of operators (Section 4 of the paper) are excluded. The agent must implement the full numerical procedure for all required α values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "p",
          "E0",
          "m_star_over_m"
        ],
        "units": {
          "alpha": "dimensionless",
          "p": "dimensionless",
          "E0": "dimensionless",
          "m_star_over_m": "dimensionless"
        }
      },
      "description": "CSV file with columns: alpha (coupling constant), p (variational parameter), E0 (ground‑state energy lower bound), m_star_over_m (effective mass ratio). Must contain rows for α in {0.1, 0.5, 1, 2, 5, 10, 20, 50, 100}. The checker recomputes and verifies consistency and asymptotic scaling."
    }
  ],
  "notes": "The task focuses strictly on the ground-state energy lower bound and effective mass; expectation values of operators (Section 4 of the paper) are excluded. The agent must implement the full numerical procedure for all required α values."
}
```

## How you are scored
A hidden verifier independently evaluates the artifact written in each workflow stage. For this single scored artifact (step_01_results.csv), the verifier performs several checks: (1) For every reported α, it verifies that the reported p satisfies p⁴ [1 − 2α/(3p)] = 1 within a strict numerical tolerance; (2) it recomputes E₀ and m*/m from that p using the closed‑form expressions and compares them to the reported values, requiring agreement within a given relative tolerance; (3) for the large‑α entries, it checks that the ratios E₀ / (−α²/3) and (m*/m) / ((16/81)α⁴) are close to 1 within a tolerance. The checks are combined into a weighted score between 0 and 1, where the majority of the weight is on the consistency of E₀ and m*/m, and the remainder on the asymptotic scaling. Simply reporting numbers from the literature is insufficient; the agent must produce values that correctly follow from the numerical solution of the maximization condition. The CSV must include exactly one row for each α in {0.1, 0.5, 1, 2, 5, 10, 20, 50, 100}. Missing α values will cause the verifier to assign zero for the asymptotic scaling checks and to penalize consistency scores accordingly.
