# Short-Distance Correlation Functions of Massive XXZ Chain

## Problem background
Short-distance static correlation functions in the infinite XXZ quantum spin chain provide essential insight into many-body quantum systems. In the massive regime (Δ > 1), exact results are difficult to obtain. This work computes longitudinal ⟨σ₁ᶻσₙᶻ⟩ᶜ and transversal ⟨σ₁ˣσₙˣ⟩ᶜ connected two-point correlation functions for distances n = 2, 3, 4 at finite temperature and magnetic field using the b̄‑formulation. The numerical method reformulates the problem into Fourier‑space integral equations and factorized algebraic expressions. The goal is to produce these correlation values for three distinct parameter regimes: an Ising‑like limit (very large Δ), a paramagnetic limit (J = 0), and a point deep in the massive phase.

## Approach
The computational approach starts from the anisotropy η obtained from Δ = cosh(η) and discretizes the interval [−π/2, π/2]. Fourier‑series representations of the kernel functions d(x), κ(x), κ±(x), l(x), l±(x), c±(x) and the closed‑form functions K̃η(x), L̃η(x) are constructed. The coupled non‑linear integral equations for the auxiliary functions b(x) and b̄(x) are solved iteratively with fast Fourier transforms and the convolution theorem. Using these, linear integral equations for g±, g′± and their μ‑derivatives are solved. The physical quantities φ, ω, ω′ and their required partial derivatives (ω_x, ω_y, ω_xx, …) are then obtained by convolving the g‑functions with the kernels. Finally, the short‑distance correlation functions for n = 2, 3, 4 are evaluated from the factorized algebraic formulas. This procedure is repeated for each of the three parameter sets defined in the reproduction target.

## Reproduction target
Compute the longitudinal and transversal connected two‑point correlation functions of the XXZ chain for distances n = 2, 3, 4 at the following three parameter regimes:
- Ising limit: Δ = 1000, J = 1, h/J = 2, T/J = 0.5
- Paramagnet limit: Δ = 2, J = 0, h/J = 2, T/J = 0.5
- Massive‑regime: Δ = 2, J = 1, h/J = 2, T/J = 0.5

Output a JSON object `/app/outputs/correlation_values.json` with keys `condition_n_type`, where condition is `ising`, `paramagnet`, or `massive`; n is 2, 3, or 4; and type is `longitudinal` or `transversal`. Example keys: `ising_n2_longitudinal`, `massive_n4_transversal`. Each value must be the computed connected correlation function (float). All computations must use the b̄‑formulation pipeline described in the approach.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Setup Fourier-space representation and kernel functions
- Role: process
- Action: Define the anisotropy parameter η from Δ=cosh(η), discretize the interval [-π/2,π/2], and construct the Fourier-series representations of the kernel functions d(x), κ(x), κ±(x), l(x), l±(x), c±(x) and the closed-form K̃η(x), L̃η(x) for the given physical parameters.
- Evidence: `/app/outputs/kernel_data.txt`

### Step 2: Solve non-linear integral equations for auxiliary functions b and b̄
- Role: process
- Action: Iteratively solve the coupled non-linear integral equations for the auxiliary functions b(x) and b̄(x) using fast Fourier transforms and the convolution theorem.
- Evidence: `/app/outputs/b_bar_b.txt`

### Step 3: Solve linear integral equations for g and g′ functions
- Role: process
- Action: Solve the linear integral equations for gμ±(x) and gμ′±(x) at μ=0, as well as their required derivatives with respect to μ, using the previously obtained b, b̄.
- Evidence: `/app/outputs/g_functions.txt`

### Step 4: Compute φ, ω, ω′ and their derivatives
- Role: process
- Action: Evaluate the integral formulas and compute φ(0), ω(0,0), ω′(0,0) and all required partial derivatives (ω_x, ω_y, ω_{xx}, ω_{xy}, ω_{xxy}, ω_{xyy}, etc.) by convolving the g-functions with the kernels and using the closed-form expressions.
- Evidence: `/app/outputs/physical_quantities.txt`

### Step 5: Evaluate short‑distance correlation functions and output results
- Role: scored (load-bearing)
- Action: For each of the three predefined test regimes (Ising limit with very large anisotropy, paramagnet with J=0, and a massive-regime point with Δ=2, J=1, T/J=0.5, h/J=2) as specified in the instruction, compute the longitudinal and transversal connected two-point correlation functions ⟨σ₁ᶻσₙᶻ⟩c and ⟨σ₁ˣσₙˣ⟩c for n=2,3,4 using the factorized algebraic formulas and the previously computed φ, ω, ω′ and their derivatives. Write all values to correlation_values.json.
- Output file: `/app/outputs/correlation_values.json`
- Format: json
- Contract: {"type": "object", "key_pattern": "condition_n_type", "value_type": "number"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/correlation_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### correlation_values.json
- path: `/app/outputs/correlation_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed connected two-point correlation functions for the Ising limit, paramagnet, and massive regime test cases. The hidden checker compares each value to known analytic results or a paper-derived gold reference within specified tolerances.
- schema:
  - `type`: object
  - `key_pattern`: condition_n_type
  - `value_type`: number

Notes: The exact list of test case keys and their parameter definitions are provided in the instruction; the solving agent must compute them and populate this file.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "correlation_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "key_pattern": "condition_n_type",
        "value_type": "number"
      },
      "description": "Computed connected two-point correlation functions for the Ising limit, paramagnet, and massive regime test cases. The hidden checker compares each value to known analytic results or a paper-derived gold reference within specified tolerances."
    }
  ],
  "notes": "The exact list of test case keys and their parameter definitions are provided in the instruction; the solving agent must compute them and populate this file."
}
```

## How you are scored
Your submission is scored by a hidden verifier. It checks the presence and content of the intermediate process artifacts (kernel_data.txt, b_bar_b.txt, g_functions.txt, physical_quantities.txt) and scores the final correlation_values.json against known analytical limits for the Ising and paramagnet cases and against a hidden reference for the massive‑regime point. The final reward combines all workflow stages — simply reporting values without running the pipeline is insufficient. Do not attempt to guess the reference values; the verifier expects a correctly executed computational pipeline.
