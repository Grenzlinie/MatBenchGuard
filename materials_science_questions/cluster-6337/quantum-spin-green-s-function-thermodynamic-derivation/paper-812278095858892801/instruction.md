# Impurity Electron Spectral Function in the s-d Model via Method of Moments

## Problem background
Understanding the temperature dependence of impurity levels in ferromagnetic semiconductors is crucial for optical and transport properties. The s-d model describes a localized impurity electron interacting with a background of localized spins via the s-d exchange term. A central challenge is whether the electronic spectrum depends on long-range magnetization ⟨Sᶻ⟩ or only on short-range spin-spin correlations. This task addresses that question by applying the method of moments to construct the impurity spectral function in a way that respects the independence from magnetization. The result is a spectral function that can be verified in two limiting regimes: a highly localized impurity state and a large-impurity-radius limit, including the zero-temperature case.

## Approach
The impurity s-d Hamiltonian consists of a localized electron level (energy ε₀ set to zero) coupled to a set of localized magnetic spins S_m via an s-d exchange parameter I, with an envelope function f_m describing the spatial extent of the impurity state. The spectral function A_σ(E) for spin σ is defined via its moments M_σ⁽ⁿ⁾, which can be computed exactly from nested commutators of the electron creation/annihilation operators with the Hamiltonian. The method of moments approximates A_σ(E) as a sum of two contributions (a two-peak model), each parameterized by a weight p_iσ, a central energy ε_i, and a shape function f_i(E−ε_i) whose low-order moments q_i⁽ⁿ⁾ are unknown. By demanding that the lowest exact moments are reproduced, one obtains constraints that link the quasiparticle energies ε₁, ε₂, the weights, and the q_i⁽ⁿ⁾. In the highly localized limit (f_m = δ_{m,N}) the shape functions reduce to delta peaks and the exact spectral function can be constructed. In the large-radius limit (neglecting powers of |f_m|⁴ and higher) the moment-fitting conditions simplify and impose a relation between ε₁ and ε₂; solving this relation yields ε₁ expressed solely in terms of spin-spin correlations. Finally, the moment-method energies are compared to exact zero-temperature eigenenergies obtained from a direct solution of the Schrödinger equation with fully aligned spins. All derivations are performed symbolically using SymPy and numerically evaluated with NumPy.

## Reproduction target
1. Highly localized impurity: with parameters I = 1, S = 1, ⟨Sᶻ⟩ = 0.5, and f_m = δ_{m,N} (impurity at site N), compute the exact spectral moments M⁽⁰⁾ through M⁽⁴⁾ for σ = +1 and −1. Using the moment-matching conditions, construct the exact spectral function as a sum of two delta peaks with weights p₁σ, p₂σ and energies ε₁, ε₂, and save both the moments and the peak parameters to `moments_and_spectral_function.json`.

2. Large impurity radius: neglecting terms of order |f_m|⁴ and higher, derive the relationship between ε₁ and ε₂ from the moment-fitting equations, compute both energies using the spin-spin correlation formulas, and verify the resulting symmetry condition Verify the symmetry condition (|ε₁ + ε₂| < 1e-6). Then, in the zero-temperature limit, compute the exact eigenenergies for the two eigenstates (one with the electron spin-up and the other a mixture of spin-down and spin-flip). Confirm that the moment-method energies match these T=0 eigenenergies. Save the results to `large_radius_condition.json`.

## Assets

- SymPy: sympy
- NumPy: numpy

## Workflow steps

### Step 1: Derive exact spectral moments and two-peak model constraints
- Role: process
- Action: Formulate the impurity s-d Hamiltonian with a localized electron coupled to background spins via an s-d exchange term. Compute exact low-order spectral moments (first through fourth) using nested commutators of electron creation/annihilation operators with the Hamiltonian. Derive the two-peak model parameterization and the general moment-matching equations, leading to constraints linking quasiparticle energies and weights.
- Evidence: `/app/outputs/moment_derivation.log`

### Step 2: Highly localized impurity spectral function
- Role: scored (load-bearing)
- Action: For a highly localized impurity (f_m = δ_mN) with parameters I=1, S=1, ⟨S^z⟩=0.5, evaluate the exact spectral moments M^{(0)}–M^{(4)} for σ = +1 and −1. Construct the exact spectral function A_σ(E) as a sum of two delta peaks with weights p_{iσ} and energies ε_i from the moment-fitting conditions, and verify that the computed moments from these peaks match the exact ones.
- Output file: `/app/outputs/moments_and_spectral_function.json`
- Format: json
- Contract: JSON object with keys: 'M0', 'M1', 'M2', 'M3', 'M4' (each a list of two numbers for σ=+1 and σ=-1), and 'localized_A_sigma' with keys 'sigma_plus' and 'sigma_minus', each containing 'p1', 'p2' (weights), 'epsilon1', 'epsilon2' (energies).
- Scoring: scored by hidden verifier

### Step 3: Large impurity radius quasiparticle energies and zero‑temperature verification
- Role: scored (load-bearing)
- Action: Neglect terms of order |f_m|^4 and higher (large impurity radius limit). From the moment-fitting conditions derive the relationship between ε₁ and ε₂, compute both energies using spin-spin correlations, and verify the resulting symmetry condition. Then evaluate the T=0 limit of these energies using the exact zero-temperature eigenstate analysis, and confirm that the moment‑method energies match the exact T=0 eigenenergies. Assume the envelope function is normalised such that sum_m |f_m|^2 = 1.
- Output file: `/app/outputs/large_radius_condition.json`
- Format: json
- Contract: JSON object with keys: 'epsilon_1' (numeric), 'epsilon_2' (numeric), 'condition_holds' (boolean, true if |epsilon_1 + epsilon_2| < 1e-6), 'zero_temp_E1' (numeric from exact T=0 solution), 'zero_temp_E2' (numeric from exact T=0 solution).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/moments_and_spectral_function.json`
- `/app/outputs/large_radius_condition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### moments_and_spectral_function.json
- path: `/app/outputs/moments_and_spectral_function.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Exact spectral moments and two-delta-peak parameters for the highly localized impurity with I=1, S=1, ⟨S^z⟩=0.5.
- schema:
  - `type`: object
  - `required`:
    - `M0`: array of 2 numbers
    - `M1`: array of 2 numbers
    - `M2`: array of 2 numbers
    - `M3`: array of 2 numbers
    - `M4`: array of 2 numbers
    - `localized_A_sigma`: object with keys sigma_plus and sigma_minus, each containing p1, p2 (weights) and epsilon1, epsilon2 (energies) as numbers

### large_radius_condition.json
- path: `/app/outputs/large_radius_condition.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Quasiparticle energies in the large impurity radius limit and verification of symmetry and zero‑temperature match.
- schema:
  - `type`: object
  - `required`:
    - `epsilon_1`: number
    - `epsilon_2`: number
    - `condition_holds`: boolean
    - `zero_temp_E1`: number
    - `zero_temp_E2`: number

Notes: The checker independently recomputes the exact moments and energies from the paper's formulas and compares each numerical value within an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "moments_and_spectral_function.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "M0": "array of 2 numbers",
          "M1": "array of 2 numbers",
          "M2": "array of 2 numbers",
          "M3": "array of 2 numbers",
          "M4": "array of 2 numbers",
          "localized_A_sigma": "object with keys sigma_plus and sigma_minus, each containing p1, p2 (weights) and epsilon1, epsilon2 (energies) as numbers"
        }
      },
      "description": "Exact spectral moments and two-delta-peak parameters for the highly localized impurity with I=1, S=1, ⟨S^z⟩=0.5."
    },
    {
      "file": "large_radius_condition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon_1": "number",
          "epsilon_2": "number",
          "condition_holds": "boolean",
          "zero_temp_E1": "number",
          "zero_temp_E2": "number"
        }
      },
      "description": "Quasiparticle energies in the large impurity radius limit and verification of symmetry and zero‑temperature match."
    }
  ],
  "notes": "The checker independently recomputes the exact moments and energies from the paper's formulas and compares each numerical value within an appropriate tolerance."
}
```

## How you are scored
A hidden verifier independently recomputes the exact spectral moments, the two-peak model parameters, and the large-radius condition using the same formulas and the specified parameters. For each scored output file, the verifier compares every numeric field against its hidden gold value (or verifies the condition). The final reward is a weighted combination of the scores from both stages: the highly localized impurity case and the large-radius limit. Simply reporting a number without genuine computation will not match the hidden references. The verifier tolerates small numerical differences, but the computation must follow the described method.
