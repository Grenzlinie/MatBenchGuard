# Renormalization Group Decimation for Classical 1D Heisenberg Chain

## Problem background
The classical one-dimensional Heisenberg chain consists of unit-length spins on a line, interacting via nearest-neighbor exchange K and an external magnetic field k. The thermodynamic properties (partition function, free energy per spin, magnetization) can be obtained from the Boltzmann weight of a spin configuration. While the zero-field case admits a closed-form solution, the presence of a nonzero magnetic field prevents an elementary exact expression. An exact renormalization-group decimation transformation provides an iterative numerical scheme that avoids solving the full eigenvalue problem. This transformation yields a rapidly converging series for the free energy per spin and produces an effective single-spin Hamiltonian $H_{\text{eff}}(S^z)$, whose departure from a simple linear (Zeeman) form quantifies the quality of a mean-field description. The task is to implement this renormalization transformation, compute the free energy for several specified coupling/field pairs, and extract the effective Hamiltonian together with a goodness-of-fit measure $\chi$ that indicates how well $H_{\text{eff}}$ can be approximated by a parabola.

## Approach
The method employs an exact decimation renormalization group for the azimuthally symmetric ($m=0$) component of the Boltzmann kernel. Starting from the original two-spin kernel $A_0(\theta_1,\theta_2)$ (which contains the modified Bessel function $I_0$ and exponential factors), the kernel is repeatedly convolved with itself over the polar angle $\theta$ and normalized, generating a sequence of kernels $B^{(n)}$ and normalization scalars $g_n$. In the limit of many iterations the kernel factorizes: $B^{(\infty)}(\theta_1,\theta_2) = f(\theta_1)f(\theta_2)$. The fixed-point vector $f(\theta)$ encodes the effective single-spin physics. The free energy per spin is obtained by summing the series $\hat{f} = -\sum_{n} g_n / 2^{n+1}$ (plus a negligible tail). From $f(\theta)$ and the free energy one constructs $H_{\text{eff}}(S^z\!=\!\cos\theta)$ and fits it to a parabola $a S^{z2} + b S^z + c$ over 30 equidistant points in $[-1,1]$. The standard error of this parabolic fit, $\chi$, measures the deviation from a pure linear-in-field effective Hamiltonian. The entire computation is carried out using 16-point Gaussian quadrature on $\theta\in[0,\pi]$, and the procedure is iterated until the matrix $B^{(n)}$ converges to the factorized form. All required mathematical functions (Bessel $I_0$, Legendre nodes/weights) are available in standard numerical libraries.

## Reproduction target
Execute the full renormalization pipeline for the four parameter pairs $(K=5.0, k=5.0)$, $(K=1.0, k=1.0)$, $(K=-1.0, k=1.0)$, and $(K=-5.0, k=5.0)$. For each pair:
- Compute the free energy per spin via the renormalization series and write a CSV file `free_energy_results.csv` with columns `K`, `k`, `free_energy_per_spin`.
- From the fixed point of the iteration, extract the effective Hamiltonian $H_{\text{eff}}$, perform the parabolic fit, and compute $\chi$ as defined in the approach. Record the $\chi$ values in a JSON file `chi_max_results.json` with keys `K5_chi_max`, `K1_chi_max`, `Kminus1_chi_max`, `Kminus5_chi_max`. The required outputs are exactly these two files placed under `/app/outputs`.

## Assets

- numpy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Set up Gaussian quadrature grid
- Role: process
- Action: Generate 16-point Gaussian quadrature nodes and weights for integration over θ∈[0,π] using Legendre polynomials, producing the discrete cosθ values and corresponding sinθ dθ weights.
- Evidence: `/app/outputs/quadrature_grid.json`

### Step 2: Compute initial kernel matrix B^(0)
- Role: process
- Action: Evaluate the explicit initial condition for the kernel B^(0)(θ1,θ2) on the quadrature grid for a given coupling K and field k, forming a matrix using the modified Bessel function I0 and exponential functions.
- Evidence: `/app/outputs/B0_matrix.npy`

### Step 3: Iterate renormalization transformation
- Role: process
- Action: Apply the decimation iteration (matrix convolution and normalization) and compute the normalization scalars g_n until the matrix B^(n) converges to the factorized form f(θ1)f(θ2). Record the sequence of g_n values and the final fixed-point vector f(θ).
- Evidence: `/app/outputs/gn_values.csv`

### Step 4: Compute free energy from renormalization series
- Role: scored
- Action: For the parameter pairs (K=5.0, k=5.0), (K=1.0, k=1.0), (K=-1.0, k=1.0), (K=-5.0, k=5.0), run the full pipeline (steps 1–3) and sum the free-energy series using the computed g_n values. Write the per-spin free energy to free_energy_results.csv.
- Output file: `/app/outputs/free_energy_results.csv`
- Format: csv
- Contract: CSV with columns K (float), k (float), free_energy_per_spin (float).
- Scoring: scored by hidden verifier

### Step 5: Extract effective Hamiltonian and compute χ
- Role: scored (load-bearing)
- Action: From the fixed-point f(θ) and free energy construct the effective Hamiltonian H_eff(S^z = cosθ). Fit H_eff to a parabola a (S^z)^2 + b S^z + c on 30 equidistant points S^z ∈ [-1,1] and compute the standard error χ = sqrt( (1/27) * Σ_{i=1}^{30} (H_eff(x_i) - (a x_i^2 + b x_i + c))^2 ). Do this for the same four (K,k) pairs as the free-energy step. Produce chi_max_results.json with keys K5_chi_max, K1_chi_max, Kminus1_chi_max, Kminus5_chi_max.
- Output file: `/app/outputs/chi_max_results.json`
- Format: json
- Contract: JSON object with keys: K5_chi_max (float), K1_chi_max (float), Kminus1_chi_max (float), Kminus5_chi_max (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_results.csv`
- `/app/outputs/chi_max_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_results.csv
- path: `/app/outputs/free_energy_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Free energy per spin for four (K,k) pairs computed via renormalization series.
- schema:
  - `type`: table
  - `required_columns`: `K`, `k`, `free_energy_per_spin`

### chi_max_results.json
- path: `/app/outputs/chi_max_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Maximum χ values for parabolic fit quality for K=5.0, 1.0, -1.0, -5.0.
- schema:
  - `type`: object
  - `required`:
    - `K5_chi_max`: float
    - `K1_chi_max`: float
    - `Kminus1_chi_max`: float
    - `Kminus5_chi_max`: float

Notes: The hidden checker compares the free energy values to a hidden gold (Blume et al. Table IV) with an appropriate relative tolerance and the χ values to the paper's Table I with an appropriate absolute tolerance. Only the four specified (K,k) pairs are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "K",
          "k",
          "free_energy_per_spin"
        ]
      },
      "description": "Free energy per spin for four (K,k) pairs computed via renormalization series."
    },
    {
      "file": "chi_max_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "K5_chi_max": "float",
          "K1_chi_max": "float",
          "Kminus1_chi_max": "float",
          "Kminus5_chi_max": "float"
        }
      },
      "description": "Maximum χ values for parabolic fit quality for K=5.0, 1.0, -1.0, -5.0."
    }
  ],
  "notes": "The hidden checker compares the free energy values to a hidden gold (Blume et al. Table IV) with an appropriate relative tolerance and the χ values to the paper's Table I with an appropriate absolute tolerance. Only the four specified (K,k) pairs are required."
}
```

## How you are scored
Each required output file is evaluated by a hidden verifier that independently checks your computed results against a reference standard. The verifier reads `free_energy_results.csv` and `chi_max_results.json` and compares the values to hidden gold data (derived from well-known published calculations) using appropriate tolerances. For the free energy, meeting or exceeding the reference precision earns full credit; for the goodness-of-fit $\chi$, closeness to the reference earns full credit. The final reward is a weighted combination of the scores from both artifacts. Reporting correct numbers is essential; the verifier does not award credit for merely producing output files with the right schema — the numeric content must match the expected values within tolerance. No paper-specific tolerances or reference values are revealed in this document.
