# Numerical solution of the first BBGKY equation for hard-sphere fcc crystal

## Problem background
The BBGKY hierarchy describes equilibrium correlations in classical fluids. Under the approximation that pair correlations in the solid can be described by the radial distribution function of a metastable fluid at the same density and temperature (the Kirkwood-Monroe approximation), the first BBGKY equation becomes a closed nonlinear integral equation for the one-particle density. This equation can possess spatially periodic solutions corresponding to a crystalline solid, even though the underlying Hamiltonian is translationally invariant. For a given interparticle potential, one can solve the equation iteratively in Fourier space to obtain the one-particle distribution function g₁(r), from which an order parameter ∥h₁∥ (measuring the degree of spatial nonuniformity) and the equation of state (pressure) can be computed. The existence and magnitude of such nonuniform solutions, as well as the resulting thermodynamic properties, depend on the density and the assumed crystal symmetry. This task focuses on the hard-sphere system with face-centred cubic (fcc) symmetry, for which the required fluid pair correlation input is available analytically.

## Approach
The equation to solve is
∇ ln g₁(r) = −βρ ∫ ds g₁(r + s) g₂^(fluid)(s) v′(s) (s / s),
where g₁(r)=ρ₁(r)/ρ, g₂^(fluid) is the fluid radial distribution function, and v′(s) is the derivative of the pair potential. For a periodic crystal g₁(r) and its logarithm are expanded in Fourier series over the reciprocal lattice vectors {k} of the chosen fcc lattice. This leads to an algebraic relation in k‑space: the Fourier coefficients satisfy Ĝ₁(k) = α(k) ĝ₁(k), where α(k) is a kernel that depends only on the magnitude of k and is computed from v(r) and g₂^(fluid).

The iterative scheme proceeds as follows:
1. Start with an initial periodic density g₁⁰(r), typically a sum of Gaussian functions centred on fcc lattice sites with adjustable width.
2. Fourier‑transform to obtain ĝ₁⁰(k).
3. Multiply by α(k) to obtain Ĝ₁¹(k).
4. Inverse Fourier‑transform to get ln g₁¹(r), exponentiate, and renormalize to obtain the next iterate g₁¹(r).
5. Repeat until the maximum change between successive iterates is sufficiently small.

By varying the width of the initial Gaussian, the iteration may converge to qualitatively different solutions at the same density: a highly nonuniform solid branch (large ∥h₁∥), a less nonuniform solid branch (small ∥h₁∥) where it exists, or the uniform fluid solution (∥h₁∥ = 0).

For hard spheres of diameter σ, the potential derivative is v′(s) = −δ(s−σ). The kernel α(k) then reduces to an expression involving the fluid radial distribution function at contact, g₂^(fluid)(σ). The contact value is provided by the Ree–Hoover formula, which is an analytic function of density. Using this kernel, the iterative solver can be executed over a range of densities to map out the behavior of the nonuniform solutions.

After obtaining a converged g₁(r) for a given density and branch, the order parameter ∥h₁∥ is computed as the root‑mean‑square of h₁(r) = g₁(r) − 1 over the unit cell. The pressure pV₀/Nk_B T (V₀ = σ³/√2 is the close‑packing volume per particle) is obtained from an effective pair correlation expression that involves g₂^(fluid) and the Fourier coefficients of g₁.

## Reproduction target
Using the iterative Fourier‑space method described above for the hard‑sphere system with fcc symmetry, perform the following for each of the densities (in units where σ=1) listed below:

0.809, 0.800, 0.790, 0.780, 0.775, 0.770, 0.760, 0.750, 0.740, 0.730, 0.725, 0.720, 0.710, 0.706, 0.705, 0.704, 0.703, 0.700.

At each density, attempt to obtain both the highly nonuniform solid branch (high ∥h₁∥) and the less nonuniform solid branch (low ∥h₁∥) by choosing suitable initial Gaussian widths. Also compute the properties of the uniform fluid state. For every converged solution extract:
- the order parameter ∥h₁∥ (the root‑mean‑square of g₁(r)−1 over the unit cell),
- the dimensionless pressure pV₀/Nk_B T, where V₀ = 1/√2 is the hard‑sphere close‑packing volume per particle.

Compile the results into a single CSV file named `hard_sphere_results.csv` with the following columns:
- rho (the density),
- h1_norm_HI (order parameter for the high nonuniform branch),
- h1_norm_LO (order parameter for the low nonuniform branch),
- pressure_HI (pressure of the high‑branch solid),
- pressure_FL (pressure of the uniform fluid).

For any density where a branch does not exist (i.e., the iteration never produces that solution branch), mark the corresponding entries with NaN. The CSV must contain the densities in exactly the order given above.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Setup fcc lattice and compute alpha(k)
- Role: process
- Action: Define the fcc unit cell and reciprocal lattice vectors up to a convergence cutoff. Evaluate the Fourier-space kernel alpha(k) for all required k-vectors using the hard-sphere potential (expressed as a delta-function at contact) and the Ree-Hoover formula for the fluid radial distribution function at contact, g2_fluid(sigma).
- Evidence: none

### Step 2: Iterative solution for g1(r) across densities
- Role: process
- Action: For each density in the set [0.809, 0.800, 0.790, 0.780, 0.775, 0.770, 0.760, 0.750, 0.740, 0.730, 0.725, 0.720, 0.710, 0.706, 0.705, 0.704, 0.703, 0.700], run the iterative Fourier-space scheme starting from a Gaussian initial guess. Sweep the Gaussian width omega to obtain the high nonuniform branch (omega << omega0), the low nonuniform branch (omega approx omega0) where it exists, and the fluid solution (omega >> omega0). Iterate until the maximum pointwise change in g1(r) reaches a tight tolerance. Keep the converged g1(r) and its Fourier coefficients.
- Evidence: none

### Step 3: Compute order parameter and pressure; output CSV
- Role: scored (load-bearing)
- Action: From the converged g1(r) for each density compute the order parameter ||h1|| using the norm of h1(r)=g1(r)-1 and the pressure pV0/NkBT using the effective pair correlation expression. Compile the values for the high-branch solid (HI), the low-branch solid (LO) if present, and the fluid (FL) state into a CSV file with columns rho, h1_norm_HI, h1_norm_LO, pressure_HI, pressure_FL. For densities where a branch does not exist, set the corresponding entry to NaN.
- Output file: `/app/outputs/hard_sphere_results.csv`
- Format: csv
- Contract: Columns: rho (float), h1_norm_HI (float), h1_norm_LO (float), pressure_HI (float), pressure_FL (float). Densities appear in the exact order listed in step_02. Missing branches are marked with NaN.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hard_sphere_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hard_sphere_results.csv
- path: `/app/outputs/hard_sphere_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed order parameter ||h1|| and pressure for the hard-sphere fcc crystal at the specified densities.
- schema:
  - `type`: table
  - `required_columns`: `rho`, `h1_norm_HI`, `h1_norm_LO`, `pressure_HI`, `pressure_FL`

Notes: The hidden checker compares each numeric cell against reference values extracted from the paper's Table I with appropriate tolerances. The order of densities must match the list given in step_02.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hard_sphere_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "rho",
          "h1_norm_HI",
          "h1_norm_LO",
          "pressure_HI",
          "pressure_FL"
        ]
      },
      "description": "Computed order parameter ||h1|| and pressure for the hard-sphere fcc crystal at the specified densities."
    }
  ],
  "notes": "The hidden checker compares each numeric cell against reference values extracted from the paper's Table I with appropriate tolerances. The order of densities must match the list given in step_02."
}
```

## How you are scored
Your solution is evaluated by a hidden verifier that examines the final CSV file `hard_sphere_results.csv`. The verifier compares each numeric entry against independently determined reference values, using an appropriate tolerance that accounts for legitimate run‑to‑run differences. In addition, the verifier checks structural properties: the correct density ordering, the presence of NaN entries where a solution branch is absent, and the expected monotonic trend of the order parameter ∥h₁∥ with density (where applicable). The checks are combined with predefined weights to produce a final reward between 0 and 1. The evaluation is fully automatic and depends only on the content of the output file; it does not read any self‑reported summary from you. Simply copying the correct numbers is not sufficient — the file must be generated by executing the iterative solver described in the workflow steps. You are not given the exact tolerance or the reference values; your task is to implement the method faithfully and output the computed quantities.
