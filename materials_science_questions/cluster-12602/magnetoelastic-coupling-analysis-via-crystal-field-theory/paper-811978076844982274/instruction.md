# Magnetoelastic Metamagnetism Simulation via Molecular Field Approximation

## Problem background
The magnetization of two‑sublattice axial magnets is described by a magnetoelastic Hamiltonian that includes Ising exchange, exchange-strain coupling, and strain-coupled single-ion anisotropy. Within the mean-field approximation (MFA) this leads to coupled self-consistency equations for the sublattice magnetizations, quadrupole moments, and the equilibrium strain. For certain choices of the dimensionless material parameters, the system can undergo a temperature-induced phase transition from an antiferromagnetic (A) phase to a ferromagnetic (F) phase. This task investigates whether such a transition occurs for a specific parameter set.

## Approach
The MFA provides self-consistency equations for the sublattice magnetization σ and the equilibrium strain ε in the A phase (σ₁ = –σ₂ = σ) and the F phase (σ₁ = σ₂ = σ). The equations are transcendental: σ is given by a hyperbolic function of σ, ε, and the fixed parameters (k, l, m, c) and the reduced temperature t; the strain ε is given by a quadratic expression involving σ² and another hyperbolic function. By simultaneously solving the pair (σ_A, ε_A) from the A-phase equations and (σ_F, ε_F) from the F-phase equations on a dense grid of t from 0 to 2, one can obtain the equilibrium values. The free energy density f for each phase is then computed from the full variational free-energy expression, which involves ln terms, the order parameters, and the strain. The entire analysis is performed for the fixed dimensionless parameter set k = -1.1, c = 1, l = 1, m = 2, producing a CSV table of all quantities as functions of t.

## Reproduction target
For the parameter set k = -1.1, c = 1, l = 1, m = 2, solve the MFA self-consistency equations for the antiferromagnetic (A) and ferromagnetic (F) phases on a grid of reduced temperature t spanning at least 100 evenly spaced points from 0 to 2. For each t and each phase, compute the sublattice magnetization σ, the equilibrium strain ε, and the free energy density f. Write all results to `/app/outputs/magnetoelastic_results.csv` with columns: t, sigma_A, sigma_F, epsilon_A, epsilon_F, f_A, f_F (all floating-point numbers). The key scientific question is: does the free energy of the F phase become lower than that of the A phase at some finite temperature? Your numerical solution should reveal whether an A→F transition exists for this parameter set and, if so, approximately where it occurs.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Magnetoelastic simulation for A and F phases
- Role: scored (load-bearing)
- Action: Implement the molecular-field (MFA) self-consistency equations for the antiferromagnetic (A) and ferromagnetic (F) phases of a two‑sublattice magnet with axial symmetry, using the magnetoelastic coupling model described in the paper. For the fixed dimensionless parameter set k = -1.1, c = 1, l = 1, m = 2, solve the coupled transcendental equations numerically for a grid of reduced temperature t from 0 to 2 (at least 100 evenly spaced points). For each phase, compute the sublattice magnetization σ, equilibrium strain ε, and free energy density f. Output all results to a CSV file.
- Output file: `/app/outputs/magnetoelastic_results.csv`
- Format: csv
- Contract: columns: t (float), sigma_A (float), sigma_F (float), epsilon_A (float), epsilon_F (float), f_A (float), f_F (float); header required; at least 100 evenly spaced t points in [0.0, 2.0]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetoelastic_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetoelastic_results.csv
- path: `/app/outputs/magnetoelastic_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Table of reduced temperature t, sublattice magnetizations sigma_A/F, equilibrium strains epsilon_A/F, and free energy densities f_A/F for the antiferromagnetic and ferromagnetic phases. The checker will recompute the free energy RMSE against hidden gold values and verify the A→F phase transition crossing.
- schema:
  - `type`: table
  - `required_columns`: `t`, `sigma_A`, `sigma_F`, `epsilon_A`, `epsilon_F`, `f_A`, `f_F`
  - `units`: object

Notes: The task reproduces the main numerical result (Fig. 5) of the paper. The earlier critical‑temperature parameter scan is not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetoelastic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "sigma_A",
          "sigma_F",
          "epsilon_A",
          "epsilon_F",
          "f_A",
          "f_F"
        ],
        "units": {}
      },
      "description": "Table of reduced temperature t, sublattice magnetizations sigma_A/F, equilibrium strains epsilon_A/F, and free energy densities f_A/F for the antiferromagnetic and ferromagnetic phases. The checker will recompute the free energy RMSE against hidden gold values and verify the A→F phase transition crossing."
    }
  ],
  "notes": "The task reproduces the main numerical result (Fig. 5) of the paper. The earlier critical‑temperature parameter scan is not required."
}
```

## How you are scored
Your submission will be evaluated by a hidden autograder. For the scored output file `magnetoelastic_results.csv`, the grader independently recomputes the free energy density f_A and f_F at several probe temperatures using the same model parameters and equations. It computes the relative root-mean-square error (RMSE) between your free energy values and the recomputed ”gold” values; this RMSE determines a performance score. In addition, the grader checks whether your data shows a temperature at which f_A and f_F cross (i.e., the F phase becomes more stable than the A phase) within a physically plausible range. The final reward is a weighted combination of these checks, with the primary weight on the free-energy RMSE. There is no need to match the paper’s exact numerical method; as long as your solutions are correct to within the accuracy of floating-point computation, you will receive full credit.
