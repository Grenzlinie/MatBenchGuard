# Critical Aging Scaling in 3D Heisenberg Antiferromagnets via Hybrid Monte Carlo / Spin Precession Simulations

## Problem background
The phase transition in three-dimensional isotropic Heisenberg antiferromagnets belongs to a dynamic universality class (model G) where a non-conserved order parameter (staggered magnetization) couples reversibly to a conserved field (total magnetization). Far from equilibrium, after a sudden quench to the critical point, the system exhibits aging scaling in the two-time spin autocorrelation function C(t,s) — a slow relaxation that breaks time translation invariance. Renormalization group studies predict that the aging collapse exponent b is universal, while the autocorrelation decay exponent λ/z (and the initial-slip exponent θ) depends on the width of the initial distribution of spin orientations, a remarkable non-universal behavior. This task tests that prediction by numerically simulating the critical dynamics.

## Approach
We construct a hybrid numerical algorithm: each simulation step combines a reversible integration of the classical Heisenberg equations of motion (spin precession) using a fourth-order predictor-corrector method with Δt = 0.01/J and 10 Kawasaki spin-exchange Monte Carlo sweeps per integration step. The Kawasaki kinetics ensure local spin exchange moves that preserve total magnetization and are accepted according to the Metropolis criterion. Simulations are performed on a simple cubic lattice with periodic boundary conditions at the critical temperature k_B T_c / J = 1.446. For the dynamic exponent z, we run on lattices of linear size L = 32, 34, and 38, extract the relaxation time t_c(L) from the stationary spin autocorrelation function, and perform a finite-size scaling fit t_c(L) ~ L^z. For the aging exponents, we simulate a 70^3 lattice starting from two different initial spin orientation distributions: (i) a uniform distribution on the unit sphere, and (ii) a truncated Gaussian distribution of width σ = 0.55, both pinned to the unit sphere. From the resulting two-time autocorrelation C(t,s) at waiting times s = 30, 50, 70, and 100 simulation time steps, we perform aging scaling collapses C(t,s) ∼ s^{−b} (t/s)^{−λ/z} to extract the exponents b and λ/z for each distribution.

## Reproduction target
Your task is to implement the hybrid simulation pipeline described above, generate the required raw data, and produce a single scored artifact: `/app/outputs/results.json`. This JSON file must contain the dynamic critical exponent z (with its uncertainty), the aging collapse exponent b and the decay exponent λ/z for the uniform initial distribution, and the same exponents for the σ = 0.55 initial distribution, all as floating-point numbers with associated error estimates. The hidden verifier will compare these values to reference expectations to assess whether b is similar across the two distributions (universal) and whether λ/z for σ = 0.55 is larger than for the uniform distribution (non‑universal), in addition to checking the absolute values.

## Assets

- Python: python>=3.8
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Generate initial spin configurations
- Role: process
- Action: Generate initial spin configurations for the required lattice sizes and distributions. For L=32,34,38 use a random setup. For L=70, create two independent ensembles: one with uniform orientation distribution on the unit sphere, one with a truncated Gaussian orientation distribution of width σ=0.55.
- Evidence: `/app/outputs/init_configs.json`

### Step 2: Run simulations for dynamic exponent z
- Role: process
- Action: For each lattice size L=32,34,38, run the hybrid spin precession + Kawasaki Monte Carlo simulation at T_c/J=1.446 using Δt=0.01/J with 10 MC sweeps per integration step (fourth-order predictor-corrector). From the stationary spin autocorrelation function C(t), extract the relaxation time t_c(L) via exponential fits.
- Evidence: `/app/outputs/t_c_results.json`

### Step 3: Run simulations for aging scaling exponents
- Role: process
- Action: For L=70, perform critical quenches from initial configurations with uniform distribution and with σ=0.55 distribution. Run hybrid simulation and compute the two-time spin autocorrelation function C(t,s) for waiting times s=30,50,70,100 simulation time steps (STS).
- Evidence: `/app/outputs/aging_data.json`

### Step 4: Compute and output critical exponents
- Role: scored (load-bearing)
- Action: Read t_c_results.json and aging_data.json. Fit t_c(L) ~ L^z to obtain the dynamic exponent z. For each initial distribution, perform aging scaling collapse C(t,s) ~ s^{-b} (t/s)^{-λ/z} to extract b and λ/z. Write the results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {z: float, z_err: float, b_uniform: float, b_err_uniform: float, lambda_z_uniform: float, lambda_z_err_uniform: float, b_sigma0.55: float, b_err_sigma0.55: float, lambda_z_sigma0.55: float, lambda_z_err_sigma0.55: float}
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
- target_policy: reference_match
- description: Critical exponents extracted from hybrid Monte Carlo / spin precession simulations of the 3D isotropic Heisenberg antiferromagnet. z from finite-size scaling of relaxation times for L=32,34,38. b and λ/z from aging scaling collapse of two-time spin autocorrelations at L=70 for uniform and σ=0.55 initial orientation distributions.
- schema:
  - `type`: object
  - `required`:
    - `z`: float (dynamic critical exponent)
    - `z_err`: float (uncertainty in z)
    - `b_uniform`: float (aging collapse exponent for uniform initial distribution)
    - `b_err_uniform`: float (uncertainty in b_uniform)
    - `lambda_z_uniform`: float (autocorrelation decay exponent λ/z for uniform distribution)
    - `lambda_z_err_uniform`: float (uncertainty in lambda_z_uniform)
    - `b_sigma0.55`: float (aging collapse exponent for σ=0.55 distribution)
    - `b_err_sigma0.55`: float (uncertainty in b_sigma0.55)
    - `lambda_z_sigma0.55`: float (autocorrelation decay exponent λ/z for σ=0.55 distribution)
    - `lambda_z_err_sigma0.55`: float (uncertainty in lambda_z_sigma0.55)

Notes: The hidden checker compares the reported exponents to the paper's measured values with tolerances appropriate for an independent re-implementation (different code, seeds, discretisation details). The checker also verifies the paper's qualitative claims: |b_uniform - b_sigma0.55| is small (universal b) and λ/z_sigma0.55 > λ/z_uniform (non-universal decay).

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "z": "float (dynamic critical exponent)",
          "z_err": "float (uncertainty in z)",
          "b_uniform": "float (aging collapse exponent for uniform initial distribution)",
          "b_err_uniform": "float (uncertainty in b_uniform)",
          "lambda_z_uniform": "float (autocorrelation decay exponent λ/z for uniform distribution)",
          "lambda_z_err_uniform": "float (uncertainty in lambda_z_uniform)",
          "b_sigma0.55": "float (aging collapse exponent for σ=0.55 distribution)",
          "b_err_sigma0.55": "float (uncertainty in b_sigma0.55)",
          "lambda_z_sigma0.55": "float (autocorrelation decay exponent λ/z for σ=0.55 distribution)",
          "lambda_z_err_sigma0.55": "float (uncertainty in lambda_z_sigma0.55)"
        }
      },
      "description": "Critical exponents extracted from hybrid Monte Carlo / spin precession simulations of the 3D isotropic Heisenberg antiferromagnet. z from finite-size scaling of relaxation times for L=32,34,38. b and λ/z from aging scaling collapse of two-time spin autocorrelations at L=70 for uniform and σ=0.55 initial orientation distributions."
    }
  ],
  "notes": "The hidden checker compares the reported exponents to the paper's measured values with tolerances appropriate for an independent re-implementation (different code, seeds, discretisation details). The checker also verifies the paper's qualitative claims: |b_uniform - b_sigma0.55| is small (universal b) and λ/z_sigma0.55 > λ/z_uniform (non-universal decay)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your `/app/outputs/results.json`. The verifier compares your reported exponents to reference values (derived from the original study) with tolerances that reflect the expected spread from different implementations, random seeds, and finite simulation details. It also evaluates the consistency with the theoretical expectations: the two b values should be close (indicating a universal collapse exponent), and λ/z for σ = 0.55 should be larger than λ/z for the uniform distribution (indicating non‑universal decay). The final reward is a weighted combination of individual exponent agreements and these qualitative trend checks; merely quoting numbers from the literature without executing the simulation steps will not yield the reward.
