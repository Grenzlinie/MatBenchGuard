# BBGKY Hierarchy Truncation Dynamics for Long-Range Quantum Spin Models

## Problem background
Equilibration and thermalization in closed quantum many-body systems is a fundamental topic in statistical mechanics, with long-range interactions introducing unusual features such as extremely slow relaxation and quasi-stationary non-equilibrium states. The quantum Bogoliubov-Born-Green-Kirkwood-Yvon (BBGKY) hierarchy provides a powerful framework for studying reduced spin density operators, but practical application requires truncating the hierarchy. The choice of closure condition is crucial: it determines whether the truncated dynamics can capture the approach to equilibrium. This task investigates the long-time dynamics of a prototypical long-range anisotropic quantum Heisenberg model with Curie-Weiss-type interactions, for which analytic progress is feasible. For special parameter values and initial conditions, the relevant hierarchy equations reduce to a simple recurrence relation. We examine the time evolution of a single-spin observable under explicit truncations of varying orders, and also in the thermodynamic limit, to assess how truncation affects the relaxation behavior.

## Approach
We focus on the Heisenberg model with zero external field and coupling matrix J = diag(0,0,1), i.e., only the z-z spin interaction is present. The initial mean spin is aligned along the x-direction: (sˣ, sʸ, sᶻ) = (1,0,0). Under these conditions a particular family of expansion coefficients of the reduced density operators decouples from the rest. Their equations of motion combine into a single complex-valued recurrence for a sequence uₙ(τ), where u₁(τ) = f₁ˣ + i f₁ʸ is proportional to the transverse spin component and τ is a rescaled time.

A correlation closure of order ℓ is imposed by setting u_{ℓ+k}=0, which truncates the recurrence to a finite linear system. Solving it in Laplace space yields u₁ as a continued fraction that can be expressed as a rational function. The denominator of this rational function defines an orthogonal polynomial; its real zeros (frequencies) and residues (amplitudes) determine the time-domain solution. After an inverse Laplace transform, u₁(τ) is obtained as a finite sum of cosine terms. For the thermodynamic limit λ=0 the recurrence simplifies and an exact closed-form solution can be derived directly.

The computational workflow therefore consists of: (i) generating the orthogonal polynomial recurrence from the given β coefficients, (ii) finding the zeros of the polynomial, (iii) computing the residues, and (iv) assembling the time series by evaluating the cosine sum over the required τ range. For the λ=0 case, the solution is evaluated from its known closed-form expression.

## Reproduction target
Produce time series of u₁(τ) = f₁ˣ + i f₁ʸ for the following two sets of conditions.

1. Finite‑N quasi‑periodic dynamics: N = 10 spins, truncation orders ℓ = 2 and ℓ = 4. Parameters: J = diag(0,0,1), h = 0, λ = 1/N = 0.1, initial condition (sˣ, sʸ, sᶻ) = (1,0,0). Time range τ ∈ [0, 20] with step size ≤ 0.01. Output a CSV file with columns: tau, u1_real, u1_imag, closure_order, N. Each row is one time step for one closure order.

2. Thermodynamic-limit decay: λ = 0 (infinite N) with the same Hamiltonian and initial condition. Time range τ ∈ [0, 5] with step size ≤ 0.01. Output a CSV file with columns: tau, u1_real, u1_imag. One row per time step.

The computed time series will reveal how the spin relaxation differs between a finite, truncated system and the full hierarchy taken at the thermodynamic limit.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Finite-N quasi-periodic dynamics
- Role: scored (load-bearing)
- Action: For N=10 spins with parameters J=diag(0,0,1), h=0 (λ=0.1), initial condition (sˣ,sʸ,sᶻ)=(1,0,0), compute the one-spin coefficient u₁(τ)=f₁ˣ+ i f₁ʸ using the analytic solution derived from the ℓ-th order correlation closure of the BBGKY hierarchy. For each closure order ℓ=2 and 4: (i) generate the orthogonal polynomial recurrence from the continued fraction with βₙ = n(1−nλ) up to degree ℓ; (ii) find the real simple zeros x_{ℓk} of the denominator polynomial; (iii) compute the residues a_{ℓk} from the polynomials; (iv) assemble the time-domain solution as a finite sum of cosine terms. Produce a CSV with one row per time step per order, covering τ ∈ [0, 20] with step ≤0.01.
- Output file: `/app/outputs/finite_N_timeseries.csv`
- Format: csv
- Contract: CSV with header: tau (float), u1_real (float), u1_imag (float), closure_order (int, 2 or 4), N (int, always 10). Each row is one time step for one closure order.
- Scoring: scored by hidden verifier

### Step 2: Thermodynamic limit Gaussian decay
- Role: scored
- Action: In the thermodynamic limit λ=0 (infinite N) and the same initial condition (sˣ,sʸ)=(1,0), compute u₁(τ) by solving the scaled BBGKY recurrence, which yields a superexponential relaxation to a known closed-form decay. Evaluate u₁(τ) for τ ∈ [0, 5] with step ≤0.01 and output a CSV.
- Output file: `/app/outputs/thermodynamic_limit_timeseries.csv`
- Format: csv
- Contract: CSV with header: tau (float), u1_real (float), u1_imag (float). One row per time step.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/finite_N_timeseries.csv`
- `/app/outputs/thermodynamic_limit_timeseries.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### finite_N_timeseries.csv
- path: `/app/outputs/finite_N_timeseries.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time-series of the one-spin coefficient u₁(τ) = f₁ˣ + i f₁ʸ for N=10 and closure orders ℓ=2,4. The checker recomputes pointwise absolute error against reference time series generated from the same analytic formulas, and verifies that the solution does not decay (envelope stays above a threshold).
- schema:
  - `type`: table
  - `required_columns`: `tau`, `u1_real`, `u1_imag`, `closure_order`, `N`
  - `units`:
    - `tau`: dimensionless rescaled time
    - `u1_real`: dimensionless
    - `u1_imag`: dimensionless

### thermodynamic_limit_timeseries.csv
- path: `/app/outputs/thermodynamic_limit_timeseries.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time-series of u₁(τ) in the thermodynamic limit λ=0, exhibiting Gaussian decay. The checker recomputes pointwise absolute error against the reference Gaussian solution.
- schema:
  - `type`: table
  - `required_columns`: `tau`, `u1_real`, `u1_imag`
  - `units`:
    - `tau`: dimensionless rescaled time
    - `u1_real`: dimensionless
    - `u1_imag`: dimensionless

Notes: The checker performs T1 recompute: it generates reference time series from the same analytic solution (for finite N/ℓ via continued fraction, orthogonal polynomial zeros, and cosine sums; for λ=0 via the Gaussian expression), then computes the maximum absolute difference between the agent's series and the reference at common τ points, using a tolerance appropriate for numerical root-finding and floating-point evaluation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "finite_N_timeseries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "u1_real",
          "u1_imag",
          "closure_order",
          "N"
        ],
        "units": {
          "tau": "dimensionless rescaled time",
          "u1_real": "dimensionless",
          "u1_imag": "dimensionless"
        }
      },
      "description": "Time-series of the one-spin coefficient u₁(τ) = f₁ˣ + i f₁ʸ for N=10 and closure orders ℓ=2,4. The checker recomputes pointwise absolute error against reference time series generated from the same analytic formulas, and verifies that the solution does not decay (envelope stays above a threshold)."
    },
    {
      "file": "thermodynamic_limit_timeseries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "u1_real",
          "u1_imag"
        ],
        "units": {
          "tau": "dimensionless rescaled time",
          "u1_real": "dimensionless",
          "u1_imag": "dimensionless"
        }
      },
      "description": "Time-series of u₁(τ) in the thermodynamic limit λ=0, exhibiting Gaussian decay. The checker recomputes pointwise absolute error against the reference Gaussian solution."
    }
  ],
  "notes": "The checker performs T1 recompute: it generates reference time series from the same analytic solution (for finite N/ℓ via continued fraction, orthogonal polynomial zeros, and cosine sums; for λ=0 via the Gaussian expression), then computes the maximum absolute difference between the agent's series and the reference at common τ points, using a tolerance appropriate for numerical root-finding and floating-point evaluation."
}
```

## How you are scored
A hidden verifier will independently evaluate each workflow artifact. For both output files, the verifier recomputes the expected time series using the same analytic recipe: for the finite‑N case it constructs the continued fraction, finds orthogonal polynomial zeros, residues, and evaluates the cosine sum; for the λ=0 case it uses the known thermodynamic‑limit closed form. It then compares the agent’s submitted values pointwise at common τ points and measures the accuracy. Additionally, a structural check for the finite‑N file verifies that the solution does not decay below a threshold over the full time interval, confirming its quasi‑periodic nature. The two artifacts contribute with different weights to the overall score, with the finite‑N result being the main load‑bearing component. Tolerances are set to absorb the typical numerical spread from root‑finding and floating‑point evaluation. Reporting a number without backing it with the correct computation will not satisfy the verifier.
