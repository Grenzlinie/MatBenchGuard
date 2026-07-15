# Exact Computation of Nucleation Rate and Spatial Distribution for Irreversible Dimer Nucleation on Terraces

## Problem background
During epitaxial growth, atoms deposited onto a crystalline terrace diffuse and, upon meeting, can nucleate an immobile dimer. The nucleation rate and the spatial distribution of where the first nucleation occurs are central quantities for understanding growth, yet they are strongly affected by interactions between diffusing adatoms. Standard mean-field theory treats the adatoms as non-interacting and overestimates the nucleation rate because it counts every encounter, not just the first one. This task addresses the EXACT computation of the nucleation probability and rate for irreversible dimer nucleation, where two adatoms stop diffusing as soon as they meet. You will study the case of zero step-edge (Ehrlich-Schwoebel) barrier, where adatoms leave the terrace only by reaching its edges, which act as absorbing boundaries. For one-dimensional terraces of size L=100 and two-dimensional terraces of size L=32, you will compute the exact spatial distribution of first-nucleation events (1D) and the exact dimensionless nucleation rates (1D and 2D). The exact results differ markedly from the mean-field estimates, and your task is to produce these exact quantities using the mapping method described below.

## Approach
The key idea is to map the diffusion of two identical adatoms on a d-dimensional terrace onto the motion of a single random walker in a d' = 2d-dimensional space. A nucleation event corresponds to the walker reaching the hyperplane where the coordinates of the two adatoms are equal; the irreversibility of dimer formation imposes an absorbing boundary condition on that hyperplane. This transforms the problem into a first-passage problem. For the one-dimensional terrace (d=1), the 2D random walker moves on an L×L square with absorbing diagonal. The problem is solved analytically by separation of variables in a sine basis. You will use an antisymmetric initial condition that automatically satisfies the absorption on the diagonal. The spatial distribution P(n) for nucleation on site n is obtained by summing the probability current onto the diagonal over all times; you will compute the eigenmode coefficients, perform the mode sums to convergence, and extract P(n) for n = 1,…,100. For the two-dimensional terrace (d=2), the mapping leads to a 4D random walker on a hypercube of side L=32 with an absorbing 2D hyperplane. An analytic solution is not available here, so you will numerically integrate the discrete 4D master equation forward in time. You will record the probability current onto the absorbing hyperplane at each time step and accumulate the total meeting probability W. From W you will then compute the dimensionless nucleation rates as defined below. A mean‑field (non‑interacting) reference calculation is also performed as a sanity check, but it is not part of the scored outputs.

## Reproduction target
Your goal is to produce two scored artifacts from the exact (interacting) solution for the zero‑barrier case:

1. A CSV file `spatial_distribution_d1.csv` containing the unnormalised first‑meeting probability P(n) for every site n = 1,…,100 on a 1D terrace of size L=100. The columns are n (integer) and P_n (non‑negative float).

2. A JSON file `nucleation_rates.json` containing three numeric fields:
   - `d1_W`: the total meeting probability W for the 1D zero‑barrier interacting adatoms, obtained from summing P(n) over all n.
   - `d1_omega_dimless`: the dimensionless nucleation rate for the 1D case, defined as ω D / (F² L⁴) with L = 100.
   - `d2_omega_dimless`: the dimensionless nucleation rate for the 2D case, defined as ω D / (F² L⁶) with L = 32.

These quantities must be computed from the exact mapping solutions; the 1D rate follows from d1_omega_dimless = d1_W / 12, and the 2D rate is extracted directly from the numerical integration.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Model parameter and initial distribution setup
- Role: process
- Action: Define all parameters for the zero barrier case: lattice sizes L=100 (1D) and L=32 (2D), diffusion constants D and D', flux F (not needed for dimensionless rates), Ehrlich-Schwoebel length ℓ_ES=0 → boundary parameter a=0. Construct the uniform initial distribution p^U(n)=1/L^d and the stationary distribution p^S(n): in 1D, p^S(n)=6 n(L+1-n)/(L(L+1)(L+2)); in 2D, the normalized discrete solution of the stationary diffusion equation with absorbing boundaries (parabolic shape).
- Evidence: `/app/outputs/params.json`

### Step 2: Compute mean-field (noninteracting) reference results
- Role: process
- Action: For zero barriers, compute the reference nucleation statistics for noninteracting adatoms in 1D (L=100) and 2D (L=32) using the analytical formulas (e.g., eigenmode sums from the paper). Obtain the total meeting number W_NI and, optionally, the spatial distribution P_NI(n). This step provides a baseline check but is not required for the scored artifacts.
- Evidence: `/app/outputs/mf_results.json`

### Step 3: Exact analytical solution for interacting adatoms in 1D
- Role: process
- Action: Implement the mapping of two adatoms on a 1D terrace to a 2D random walker with an absorbing diagonal. Use separation of variables in a sine basis and the antisymmetric initial condition trick. Compute the eigenmode coefficients and the cumulative first-meeting probability P(n) for n=1..L. Summation over eigenmodes must be carried to convergence (all k,j from 1 to L or until contributions are negligible). Record the total meeting probability W from this solution.
- Evidence: `/app/outputs/d1_analysis.log`

### Step 4: Output 1D spatial distribution of first nucleation events
- Role: scored (load-bearing)
- Action: Write the unnormalized probabilities P(n) computed from the interacting adatom exact solution for L=100 into a CSV file with columns n (1..100) and P_n.
- Output file: `/app/outputs/spatial_distribution_d1.csv`
- Format: csv
- Contract: Two columns: n (integer, 1 ≤ n ≤ 100), P_n (non‑negative float)
- Scoring: scored by hidden verifier

### Step 5: Numerical integration of 4D master equation for 2D
- Role: process
- Action: Discretize the 4D probability p_{m1,n1,m2,n2}(t) for L=32 with zero barrier (a=0) and the initial symmetrized distribution. Iterate the discrete evolution equation forward in time, recording at each step the probability current onto the absorbing hyperplane (m1=m2, n1=n2) to accumulate the temporal distribution. Terminate when the temporal distribution has decayed to a negligible level. From the accumulated nucleations, compute the total meeting probability W and the dimensionless nucleation rate ω D/(F² L⁶) for the 2D case.
- Evidence: `/app/outputs/d2_simulation.log`

### Step 6: Compile nucleation rates JSON
- Role: scored (load-bearing)
- Action: Collect the 1D results (W from the analytical solution, compute d1_omega_dimless = W / 12) and the 2D results (numerically determined W and d2_omega_dimless). Write a JSON file with keys 'd1_W', 'd1_omega_dimless', and 'd2_omega_dimless'. The dimensionless rates are defined as: d1_omega_dimless = ω D / (F² L⁴) for L=100; d2_omega_dimless = ω D / (F² L⁶) for L=32.
- Output file: `/app/outputs/nucleation_rates.json`
- Format: json
- Contract: {'d1_W': float, 'd1_omega_dimless': float, 'd2_omega_dimless': float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spatial_distribution_d1.csv`
- `/app/outputs/nucleation_rates.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spatial_distribution_d1.csv
- path: `/app/outputs/spatial_distribution_d1.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Unnormalized first-meeting probability P(n) for each site n=1..100 on a 1D terrace of size L=100 with zero Ehrlich-Schwoebel barrier. The checker recomputes total meeting probability W = sum(P_n) and dimensionless rate ω D/(F² L⁴) = W/12 from this artifact.
- schema:
  - `type`: table
  - `required_columns`: `n`, `P_n`
  - `units`:
    - `P_n`: dimensionless probability

### nucleation_rates.json
- path: `/app/outputs/nucleation_rates.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total meeting probability for 1D zero-barrier interacting adatoms and the dimensionless nucleation rates for both 1D (L=100) and 2D (L=32) zero-barrier cases, computed exactly by the mapping method.
- schema:
  - `type`: object
  - `required`:
    - `d1_W`: float (dimensionless probability)
    - `d1_omega_dimless`: float (dimensionless rate, ω D/(F² L⁴))
    - `d2_omega_dimless`: float (dimensionless rate, ω D/(F² L⁶))

Notes: The dimensionless rates are derived from the total meeting probability W. For 1D, ω D/(F² L⁴) = W/12; for 2D, the 4D numerical integration directly yields ω D/(F² L⁶). The hidden reference values are the paper‐reported quantities for these exact conditions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spatial_distribution_d1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "P_n"
        ],
        "units": {
          "P_n": "dimensionless probability"
        }
      },
      "description": "Unnormalized first-meeting probability P(n) for each site n=1..100 on a 1D terrace of size L=100 with zero Ehrlich-Schwoebel barrier. The checker recomputes total meeting probability W = sum(P_n) and dimensionless rate ω D/(F² L⁴) = W/12 from this artifact."
    },
    {
      "file": "nucleation_rates.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "d1_W": "float (dimensionless probability)",
          "d1_omega_dimless": "float (dimensionless rate, ω D/(F² L⁴))",
          "d2_omega_dimless": "float (dimensionless rate, ω D/(F² L⁶))"
        }
      },
      "description": "Total meeting probability for 1D zero-barrier interacting adatoms and the dimensionless nucleation rates for both 1D (L=100) and 2D (L=32) zero-barrier cases, computed exactly by the mapping method."
    }
  ],
  "notes": "The dimensionless rates are derived from the total meeting probability W. For 1D, ω D/(F² L⁴) = W/12; for 2D, the 4D numerical integration directly yields ω D/(F² L⁶). The hidden reference values are the paper‐reported quantities for these exact conditions."
}
```

## How you are scored
A hidden verifier will independently check your submitted artifacts. It will:
- Read `spatial_distribution_d1.csv`, verify that it contains 100 rows with the correct n indices and non‑negative P_n values, then recompute the total meeting probability W = sum(P_n) and the 1D dimensionless rate W/12. It will compare these recomputed values against hidden reference values using a tolerance appropriate for an analytical solution with finite mode summation.
- Read `nucleation_rates.json`, extract the three reported numbers, and compare them to hidden reference values (derived from the exact solution under the specified parameters). The comparison uses a relative tolerance that accounts for minor differences due to summation truncation or floating‑point arithmetic.

Your reward is a weighted combination of the two scored stages: the spatial distribution CSV and the nucleation rates JSON. The verifier does not rely on any single reported performance metric; it recomputes the desired quantities from your raw artifacts. Therefore, simply reporting the paper's numbers is not sufficient – you must actually implement the computations described in the workflow steps.
