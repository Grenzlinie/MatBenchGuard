# Closed-Form Spin-Scaling Expressions for the High-Density Uniform Electron Gas λ1 Coefficient

## Problem background
The uniform electron gas (UEG) is a fundamental model in density-functional theory, used to develop exchange-correlation functionals for real materials. In the high-density limit, the correlation energy per electron can be expanded in powers of the Seitz radius r_s and its logarithm, with the leading r_s ln r_s term governed by a coefficient λ_1(ζ) that depends on the relative spin polarization ζ. While the lower-order coefficients λ_0(ζ) and ε_0(ζ) were known, an exact closed-form expression for λ_1(ζ) valid for all ζ—including its paramagnetic (ζ=0) and ferromagnetic (ζ=1) limits—remained unresolved. Deriving this coefficient and resolving its spin-resolved contributions is the core computational problem.

## Approach
The coefficient λ_1(ζ) is the sum of a random-phase-approximation (RPA) term λ_1^a(ζ) and a second-order-exchange term λ_1^b(ζ). Both are given by definite integrals whose integrands involve auxiliary functions R_0, R_1, R_2 (defined in terms of arctan and rational functions) combined with the spin-dependent Fermi momenta k_↑,↓ = (1±ζ)^{1/3}. These integrals can be evaluated analytically, yielding closed-form spin-scaling functions Λ_1^a(ζ) and Λ_1^b(ζ) that are expressed in terms of elementary functions and the dilogarithm. Evaluating the closed-form results (or performing high-precision numerical integration) at ζ=0 and ζ=1 yields the paramagnetic and ferromagnetic limits, which are then compared with previously reported values to identify and correct a mistaken ferromagnetic value. The same framework also provides the spin-resolved pair contributions at intermediate polarizations such as ζ=0.5, and a correction term δλ_1^a(1) that explains the discrepancy.

## Reproduction target
Compute the following numeric quantities and write them to the specified JSON output files:

1. The total λ_1 and its RPA (λ_1^a) and second-order-exchange (λ_1^b) components at ζ=0 and ζ=1 (six floating-point numbers).
2. The spin-resolved fractions Λ_1^{a,↑↑}(0.5) and Λ_1^{b,↑↑}(0.5) at ζ=0.5.
3. The correction term δλ_1^a(1) = 2^{-1/3} α / (8π^3), where α = (9π/4)^{-1/3}.

These values are to be derived from the integral definitions of λ_1^a and λ_1^b, either by symbolic integration leading to closed-form expressions or by high-precision numerical integration. The target is to reproduce the exact numeric results that follow from those definitions.

## Assets

- SymPy: sympy
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement λ1 integral definitions
- Role: process
- Action: Define the auxiliary functions R0, R1, R2 and their spin‑dependent combinations as given by the integral representations.  Build the integrands for the RPA (λ1^a) and second‑order exchange (λ1^b) contributions.  Implement a numerical integration scheme (e.g., adaptive Gauss quadrature) or use symbolic integration to derive the closed‑form spin‑scaling functions, so that accurate evaluation for any spin polarization ζ (including the limits ζ=0 and ζ=1) becomes possible.
- Evidence: none

### Step 2: Compute λ1(0) and λ1(1) limits
- Role: scored
- Action: Using the implemented evaluation routines (or the closed‑form results), compute the numerical values of λ1^a, λ1^b, and the total λ1 for ζ=0 and ζ=1.  Write a JSON file containing the six required floating‑point numbers.
- Output file: `/app/outputs/step_01_lambda1_values.json`
- Format: json
- Contract: JSON object with float fields: lambda1_0, lambda1_1, lambda1_a_0, lambda1_a_1, lambda1_b_0, lambda1_b_1.
- Scoring: scored by hidden verifier

### Step 3: Compute spin resolution at ζ=0.5
- Role: scored
- Action: Using the scaling functions Λ1^a and Λ1^b (or directly the spin‑resolved integrals), compute the spin‑resolved fractions Λ1^{a,↑↑}(0.5) and Λ1^{b,↑↑}(0.5).  Write a JSON file with the two values.
- Output file: `/app/outputs/step_02_spin_resolution.json`
- Format: json
- Contract: JSON object with float fields: Lambda1_a_upup_05, Lambda1_b_upup_05.
- Scoring: scored by hidden verifier

### Step 4: Compute correction term δλ1^a(1)
- Role: scored
- Action: Compute the correction term δλ1^a(1) = 2^{-1/3} * α / (8π^3).  Write a JSON file with this single value.
- Output file: `/app/outputs/step_03_delta_lambda1a.json`
- Format: json
- Contract: JSON object with float field: delta_lambda1a_1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lambda1_values.json`
- `/app/outputs/step_02_spin_resolution.json`
- `/app/outputs/step_03_delta_lambda1a.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lambda1_values.json
- path: `/app/outputs/step_01_lambda1_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Exact numeric limits of the λ1 coefficient and its components at ζ=0 and ζ=1.
- schema:
  - `type`: object
  - `required`: `lambda1_0`, `lambda1_1`, `lambda1_a_0`, `lambda1_a_1`, `lambda1_b_0`, `lambda1_b_1`
  - `properties`:
    - `lambda1_0`:
      - `type`: number
      - `description`: total λ1(0)
    - `lambda1_1`:
      - `type`: number
      - `description`: total λ1(1)
    - `lambda1_a_0`:
      - `type`: number
      - `description`: RPA contribution λ1^a(0)
    - `lambda1_a_1`:
      - `type`: number
      - `description`: RPA contribution λ1^a(1)
    - `lambda1_b_0`:
      - `type`: number
      - `description`: second‑order exchange contribution λ1^b(0)
    - `lambda1_b_1`:
      - `type`: number
      - `description`: second‑order exchange contribution λ1^b(1)
  - `additionalProperties`: False

### step_02_spin_resolution.json
- path: `/app/outputs/step_02_spin_resolution.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin‑resolved pair contributions at ζ=0.5.
- schema:
  - `type`: object
  - `required`: `Lambda1_a_upup_05`, `Lambda1_b_upup_05`
  - `properties`:
    - `Lambda1_a_upup_05`:
      - `type`: number
      - `description`: spin‑resolved RPA fraction Λ1^{a,↑↑}(0.5)
    - `Lambda1_b_upup_05`:
      - `type`: number
      - `description`: spin‑resolved exchange fraction Λ1^{b,↑↑}(0.5)
  - `additionalProperties`: False

### step_03_delta_lambda1a.json
- path: `/app/outputs/step_03_delta_lambda1a.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Numerical value of the correction term that explains the discrepancy in the published ferromagnetic limit.
- schema:
  - `type`: object
  - `required`: `delta_lambda1a_1`
  - `properties`:
    - `delta_lambda1a_1`:
      - `type`: number
      - `description`: correction term δλ1^a(1)
  - `additionalProperties`: False

Notes: All outputs are derived from the analytical integral definitions or the closed‑form expressions given in the paper.  The verifier compares the submitted floating‑point numbers against the exact reference values with a small relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lambda1_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "lambda1_0",
          "lambda1_1",
          "lambda1_a_0",
          "lambda1_a_1",
          "lambda1_b_0",
          "lambda1_b_1"
        ],
        "properties": {
          "lambda1_0": {
            "type": "number",
            "description": "total λ1(0)"
          },
          "lambda1_1": {
            "type": "number",
            "description": "total λ1(1)"
          },
          "lambda1_a_0": {
            "type": "number",
            "description": "RPA contribution λ1^a(0)"
          },
          "lambda1_a_1": {
            "type": "number",
            "description": "RPA contribution λ1^a(1)"
          },
          "lambda1_b_0": {
            "type": "number",
            "description": "second‑order exchange contribution λ1^b(0)"
          },
          "lambda1_b_1": {
            "type": "number",
            "description": "second‑order exchange contribution λ1^b(1)"
          }
        },
        "additionalProperties": false
      },
      "description": "Exact numeric limits of the λ1 coefficient and its components at ζ=0 and ζ=1."
    },
    {
      "file": "step_02_spin_resolution.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Lambda1_a_upup_05",
          "Lambda1_b_upup_05"
        ],
        "properties": {
          "Lambda1_a_upup_05": {
            "type": "number",
            "description": "spin‑resolved RPA fraction Λ1^{a,↑↑}(0.5)"
          },
          "Lambda1_b_upup_05": {
            "type": "number",
            "description": "spin‑resolved exchange fraction Λ1^{b,↑↑}(0.5)"
          }
        },
        "additionalProperties": false
      },
      "description": "Spin‑resolved pair contributions at ζ=0.5."
    },
    {
      "file": "step_03_delta_lambda1a.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "delta_lambda1a_1"
        ],
        "properties": {
          "delta_lambda1a_1": {
            "type": "number",
            "description": "correction term δλ1^a(1)"
          }
        },
        "additionalProperties": false
      },
      "description": "Numerical value of the correction term that explains the discrepancy in the published ferromagnetic limit."
    }
  ],
  "notes": "All outputs are derived from the analytical integral definitions or the closed‑form expressions given in the paper.  The verifier compares the submitted floating‑point numbers against the exact reference values with a small relative tolerance."
}
```

## How you are scored
A hidden verifier checks each of the three scored output files independently. For each file, the verifier recomputes the expected reference values from the exact closed-form expressions and compares your submitted numbers against them using a relative tolerance appropriate for a correct re‑computation. To earn credit for a stage, your computed values must fall within that tolerance. The final reward is a weighted combination of the scores from all three stages, with the λ_1 limits carrying the largest weight. Simply reporting the numbers without executing the required derivation or computation will not satisfy the verifier.
