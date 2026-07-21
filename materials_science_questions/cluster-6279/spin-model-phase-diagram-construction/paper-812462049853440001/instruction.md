# Critical Parameters of q-Deformed Superconductivity

## Problem background
This task addresses a q-deformed version of a strong-coupling superconductivity model. The system consists of fermionic q-oscillators (deformation parameter γ) whose Hamiltonian respects a U_q(2) quantum group symmetry. The model can be mapped onto a quantum SU_q(2) spin system and solved by a maximum-term approximation of the grand partition function. Within this framework, the equilibrium state is described by an order parameter w = sqrt(r/K) (where r is the number of occupied paired levels and K is the total number of paired levels). The normal state corresponds to w = 1/2, while a superconducting state appears as a maximum away from that point. The nature of the phase transition—whether it is second-order or first-order—depends on the deformation parameter γ and the number of paired levels K. The task is to compute the critical parameters that characterize this transition for specified values of γ and K.

## Approach
The analysis proceeds by deriving the maximum-term self-consistency equation that governs the stationary points of the summand of the grand partition function. This equation takes the form F(w)=0, where w = sqrt(r/K). For the non-deformed limit (γ → 0), the equation reduces to a known limiting form. The superconducting phase transition is identified by monitoring the location of the global maximum of the summand as the dimensionless inverse temperature βJK changes.

For γ = 0, the transition is second-order: the maximum stays at the normal-state point w = 1/2 until βJK exceeds a critical value β_c JK, at which it continuously moves to a new interior point. By solving the limiting equation, β_c JK can be obtained.

For a small but finite deformation (e.g., γ = 0.0003) with a fixed number of paired levels K = 7000, the function F(w) can develop additional structure. As βJK increases, one locates an inflection point (β₁ JK) where a second zero of F(w) emerges, and a first-order transition point (β₂ JK) where the two local maxima have equal height in the summand. This is done by scanning β and examining the roots and the values of the summand at those roots.

Finally, the critical deformation γ_c (for K = 7000) is the smallest γ at which the transition becomes first-order. It is found by sweeping γ (e.g., via binary search) and checking for the appearance of two maxima with equal height.

## Reproduction target
Produce a JSON file containing the following four numeric critical parameters, all computed under the maximum-term approximation of the grand partition function of the q-deformed model:

- gamma0_beta_c: the critical β_JK for the non-deformed limit γ = 0.
- gamma0003_beta1: the inflection-point β₁_JK for deformation γ = 0.0003 and K = 7000.
- gamma0003_beta2: the first-order transition β₂_JK for γ = 0.0003 and K = 7000.
- gamma_c: the critical deformation parameter (smallest γ) above which the transition becomes first-order, for K = 7000.

The output file must be named results.json and placed in /app/outputs. The JSON object must contain exactly these four keys with numeric values.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute critical phase transition parameters
- Role: scored (load-bearing)
- Action: Implement the maximum-term self-consistency equation F(w)=0 from the q-deformed superconductivity model. For the non-deformed limit gamma=0, find the critical beta_c JK where the maximum departs from the normal state w=1/2. For gamma=0.0003 and K=7000, scan beta to locate the inflection point beta1 JK and the equal-maxima first-order transition point beta2 JK. For K=7000, perform a binary search over gamma to determine the smallest gamma (gamma_c) at which the transition becomes first-order. Write all values to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with keys: "gamma0_beta_c" (number), "gamma0003_beta1" (number), "gamma0003_beta2" (number), "gamma_c" (number).
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
- target_policy: exact_match
- description: Computed critical parameters characterizing the superconducting phase transition in the q-deformed strong-coupling model.
- schema:
  - `type`: object
  - `required`:
    - `gamma0_beta_c`: number
    - `gamma0003_beta1`: number
    - `gamma0003_beta2`: number
    - `gamma_c`: number

Notes: The values are specific to the maximum-term approximation of the grand partition function with K=7000 and the specified deformation parameters. All outputs are deterministic from the model equations.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma0_beta_c": "number",
          "gamma0003_beta1": "number",
          "gamma0003_beta2": "number",
          "gamma_c": "number"
        }
      },
      "description": "Computed critical parameters characterizing the superconducting phase transition in the q-deformed strong-coupling model."
    }
  ],
  "notes": "The values are specific to the maximum-term approximation of the grand partition function with K=7000 and the specified deformation parameters. All outputs are deterministic from the model equations."
}
```

## How you are scored
A hidden verifier will run after your solution completes. It reads your /app/outputs/results.json, validates that all required keys are present and numeric, and then compares each value to the paper’s reported reference (hidden gold) using predefined absolute tolerances. The final reward (a number between 0 and 1) is the fraction of the four values that are within their respective tolerances. Simply reporting expected numbers without implementing the numerical solution will not suffice; the verifier expects values that could only be obtained by correctly solving the self-consistency equations.
