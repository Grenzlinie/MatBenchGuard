# Resonance Poles and Transmission Bands in an Elastically-Supported String with Point Defects

## Problem background
In many waveguides, local obstacles (defects) cause resonance blocking of propagating waves at certain frequencies, while at others waves may be transmitted almost completely. Understanding how the number and arrangement of defects control transmission and blocking is important for designing filters and phononic structures. This task explores the phenomenon using a one-dimensional model: an elastically supported infinite string containing point defects modelled as pointwise jumps in mass and/or foundation stiffness. As the number of defects increases, the frequency-dependent transmission is expected to develop distinct pass and gap bands. The connection between these bands and the complex resonance poles (roots of a characteristic determinant) is to be investigated by direct numerical computation.

## Approach
The method is based on a semianalytical Green's function solution for forced vibrations. The wave equation with concentrated mass/stiffness changes is transformed into an equation with constant coefficients and source terms at the defect positions. The solution is expressed as the Green's function of the pristine string plus contributions from each defect, yielding a linear algebraic system `A(ω) w = g(ω)`. The resonance frequencies (poles) are the complex roots of `det A(ω) = 0`. The frequency-dependent transmission coefficient `κ⁺(ω)` for waves beyond the defect zone is defined as the squared ratio of the string displacement at an observation point behind the defects to the displacement of the defect‑free string at the same point. For an infinite periodic array of identical defects, the pass bands can be obtained from the Bloch–Floquet characteristic equation, which reduces to an inequality involving the wave number, defect parameters, and spacing. The task is to implement these formulas, perform the root‑finding and transmission calculations for several defect configurations, and compare the resulting transmission bands (from the largest computed `N`) with the Bloch–Floquet band structure.

## Reproduction target
For two defect parameter sets (mass‑defect: α = 0.5, ε = 0.5, spacing a = 1.0, cutoff c = 4.0; stiffness‑only defect: α = 0.0, ε = 1.0, a = 1.0, c = 4.0) and for each number of defects N in {1, 2, 5, 10, 20, 50}, produce the following three scored artifacts:

1. **Complex resonance poles** – a list of roots of the characteristic determinant `det A(ω)=0` in the complex ω‑plane, reporting real and imaginary parts for each configuration.
2. **Transmission coefficient κ⁺(ω)** – for the same configurations, compute κ⁺ over a fine grid of real frequencies ω > c, storing ω and κ⁺ values.
3. **Pass band edges comparison** – infer the transmission pass bands from the κ⁺ curve for N=50; independently compute the Bloch–Floquet pass bands from the characteristic inequality; report the lower and upper edges of each band from both methods.

The collected results should show how the pole distribution and transmission behaviour evolve with N, and how the Bloch–Floquet bands are approached in the large‑N limit.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Build the Green's function model
- Role: process
- Action: Implement the dimensionless wave number k0(ω) with branch cuts, the Green's function g(x,ω), the matrix A(ω) and right-hand side vector g(ω) for N point defects at positions x_j = (j+0.5)*a, and the formula for the transmission coefficient κ⁺(ω) at a chosen output point x⁺ = x_N + 1.0.
- Evidence: `/app/outputs/model_log.txt`

### Step 2: Compute complex resonance poles
- Role: scored
- Action: For the two defect parameter sets: (i) α=0.5, ε=0.5, a=1.0, c=4.0; (ii) α=0.0, ε=1.0, a=1.0, c=4.0, and for each N in {1,2,5,10,20,50}, numerically solve det A(ω)=0 in the complex ω-plane. Use an appropriate root-finding method with scanning/initial guesses that cover the lower half-plane. Collect all roots (real and complex) with their real and imaginary parts.
- Output file: `/app/outputs/poles_all_N.csv`
- Format: csv
- Contract: Columns: N (int), real_part (float), imag_part (float), alpha (float), epsilon (float), a (float), c (float). Each row corresponds to one pole for a given configuration.
- Scoring: scored by hidden verifier

### Step 3: Compute transmission coefficient κ⁺(ω)
- Role: scored (load-bearing)
- Action: For the same two parameter sets and N values, for a fine grid of real ω > c (e.g., from c to 5c, step 0.01), solve A(ω) w = g(ω) and evaluate κ⁺(ω) = |w(x⁺,ω)/g(x⁺,ω)|² with x⁺ = x_N + 1.0. Store the ω values and corresponding κ⁺.
- Output file: `/app/outputs/transmission_coefficient_N.csv`
- Format: csv
- Contract: Columns: N (int), omega (float), kappa_plus (float). Each row records κ⁺ at a given ω for a specific N and defect set.
- Scoring: scored by hidden verifier

### Step 4: Determine Bloch–Floquet pass bands and compare
- Role: scored
- Action: For the same two parameter sets (now treating the defects as a periodic array with spacing a), determine the pass bands from the Bloch–Floquet characteristic equation: find all frequency intervals where |cos(a k0) + (d a/k0) sin(a k0)| < 1 (inequality (30)). Compare these bands with the transmission bands observed from κ⁺(ω) for the largest N (N=50). Report the band edges from both methods.
- Output file: `/app/outputs/band_edges_comparison.csv`
- Format: csv
- Contract: Columns: band_type (string, one of 'transmission' or 'Bloch-Floquet'), lower_edge (float), upper_edge (float), method (string, one of 'kappa_plus' or 'inequality'). Each row records the lower and upper frequency edge of one pass band.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/poles_all_N.csv`
- `/app/outputs/transmission_coefficient_N.csv`
- `/app/outputs/band_edges_comparison.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### poles_all_N.csv
- path: `/app/outputs/poles_all_N.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Complex resonance poles for each defect configuration. The checker recomputes the poles from the same parameters and compares real and imaginary parts within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `N`, `real_part`, `imag_part`, `alpha`, `epsilon`, `a`, `c`
  - `units`: object

### transmission_coefficient_N.csv
- path: `/app/outputs/transmission_coefficient_N.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Transmission coefficient κ⁺ as a function of frequency for all N and parameter sets. The checker recomputes κ⁺ at the agent's reported ω values and checks absolute difference.
- schema:
  - `type`: table
  - `required_columns`: `N`, `omega`, `kappa_plus`
  - `units`: object

### band_edges_comparison.csv
- path: `/app/outputs/band_edges_comparison.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pass band edges determined from transmission coefficient (N=50) and from Bloch–Floquet inequality. The checker recomputes Bloch–Floquet pass bands and verifies agreement within absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `band_type`, `lower_edge`, `upper_edge`, `method`
  - `units`: object

Notes: The hidden checker implements the same mathematical model (k0, Green's function, matrix A, transmission coefficient) using the specified parameters. For poles and transmission coefficient it recomputes reference values; for band edges it solves the Bloch–Floquet inequality independently. Comparison tolerances are chosen to absorb legitimate toolchain spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "poles_all_N.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "real_part",
          "imag_part",
          "alpha",
          "epsilon",
          "a",
          "c"
        ],
        "units": {}
      },
      "description": "Complex resonance poles for each defect configuration. The checker recomputes the poles from the same parameters and compares real and imaginary parts within tolerances."
    },
    {
      "file": "transmission_coefficient_N.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "omega",
          "kappa_plus"
        ],
        "units": {}
      },
      "description": "Transmission coefficient κ⁺ as a function of frequency for all N and parameter sets. The checker recomputes κ⁺ at the agent's reported ω values and checks absolute difference."
    },
    {
      "file": "band_edges_comparison.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "band_type",
          "lower_edge",
          "upper_edge",
          "method"
        ],
        "units": {}
      },
      "description": "Pass band edges determined from transmission coefficient (N=50) and from Bloch–Floquet inequality. The checker recomputes Bloch–Floquet pass bands and verifies agreement within absolute tolerance."
    }
  ],
  "notes": "The hidden checker implements the same mathematical model (k0, Green's function, matrix A, transmission coefficient) using the specified parameters. For poles and transmission coefficient it recomputes reference values; for band edges it solves the Bloch–Floquet inequality independently. Comparison tolerances are chosen to absorb legitimate toolchain spread."
}
```

## How you are scored
A hidden verifier evaluates each scored output file independently, and the individual scores are combined by weight into a final reward.

- For the pole positions, the verifier recomputes the determinant roots from the same parameters and checks agreement of the reported real and imaginary parts against a reference solution within suitable tolerances.
- For the transmission coefficient, the verifier recomputes κ⁺ at the reported frequency points and compares the values.
- For the band edges, the verifier independently solves the Bloch–Floquet inequality and checks that the reported pass band intervals (both from transmission data and from the inequality) match the reference.

Accurate computation of the required quantities is rewarded; simply quoting numbers without correct underlying calculations will not pass.
