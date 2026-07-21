# Temperature Dependence of Critical Thickness for Stripe-to-Branch Transition

## Problem background
In a slab of Ising ferromagnet, the competition between dipolar energy and domain wall energy leads to temperature-dependent domain structures. As the Curie temperature is approached from below, a continuum theory of domain walls becomes valid. This theory provides analytic expressions for key quantities: the characteristic length γ(t) governing the energy balance, the critical thickness L_k for the transition from stripe to branched domains, the domain size D at the critical thickness, and the limiting reduced temperature t_k^* and thickness L_k^* where the continuum description breaks down because the domain size becomes comparable to the correlation length. Computing these quantities from the given material parameters and a list of reduced temperatures provides a quantitative description of domain evolution near the critical point.

## Approach
Implement the formulas from the continuum domain-wall theory. The characteristic length γ(t) is expressed in terms of the interaction range r0, the dipolar coupling strength f, and the reduced temperature t. A geometrical constant Δ (7.38) appears in the stability analysis. From γ, compute the critical thickness L_k = Δ³ γ and the domain size at critical thickness D = (Δ L_k γ)^(1/2). The breakdown condition equates D to the correlation length ξ = r0/(2√(3t)), yielding an equation that must be solved numerically for t to obtain t_k^*. L_k^* is then L_k evaluated at that t. The computation is deterministic and requires only standard numerical operations.

## Reproduction target
Given the interaction range r0 = 6×10⁻¹⁰ m, the dipolar coupling strength f = 0.01, and the list of reduced temperatures t = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1], compute the arrays of γ, L_k, and D for each t, as well as the scalars t_k^* and L_k^* from the breakdown condition. Write all results to a JSON file `/app/outputs/computed_quantities.json` with exactly the keys: "gamma" (float array), "L_k" (float array), "D" (float array), "t_k_star" (float), "L_k_star" (float).

## Assets
No external assets are required. All needed numerical parameters (r0, f, and the list of reduced temperatures) are provided directly in the workflow step. The computation uses only standard mathematical operations and does not depend on any dataset, pretrained model, or external file.

## Workflow steps

### Step 1: Compute derived domain quantities
- Role: scored (load-bearing)
- Action: Given the interaction range r0 = 6e-10 m, dipolar coupling strength f = 0.01, and a list of reduced temperatures t = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1], implement the continuum domain-wall theory formulas: γ = 0.77 * r0 * sqrt(t) / f, Δ = 7.38, L_k = Δ^3 * γ, D = sqrt(Δ * L_k * γ). Solve D = r0 / (2 * sqrt(3 * t)) numerically for t to obtain the limiting reduced temperature t_k^*, then compute L_k^* = L_k(t_k^*). Save the computed γ array, L_k array, D array, t_k^*, and L_k^* in a JSON file.
- Output file: `/app/outputs/computed_quantities.json`
- Format: json
- Contract: JSON object with keys: "gamma" (array of floats, length matching input t), "L_k" (array of floats), "D" (array of floats), "t_k_star" (float), "L_k_star" (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_quantities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_quantities.json
- path: `/app/outputs/computed_quantities.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed domain structure quantities from the continuum theory for the given material parameters and reduced temperatures.
- schema:
  - `type`: object
  - `required`: `gamma`, `L_k`, `D`, `t_k_star`, `L_k_star`
  - `properties`:
    - `gamma`:
      - `type`: array
      - `items`:
        - `type`: number
    - `L_k`:
      - `type`: array
      - `items`:
        - `type`: number
    - `D`:
      - `type`: array
      - `items`:
        - `type`: number
    - `t_k_star`:
      - `type`: number
    - `L_k_star`:
      - `type`: number
  - `units`:
    - `gamma`: m
    - `L_k`: m
    - `D`: m
    - `t_k_star`: dimensionless
    - `L_k_star`: m

Notes: The interaction range r0 and dipolar coupling strength f are defined as in the continuum theory; the formulas are based on the Kaczér free energy and the magnetization profile of Bulaevskii and Ginzburg. The checker will recompute the quantities using the same input parameters and formulas, comparing with a relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_quantities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "gamma",
          "L_k",
          "D",
          "t_k_star",
          "L_k_star"
        ],
        "properties": {
          "gamma": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "L_k": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "D": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "t_k_star": {
            "type": "number"
          },
          "L_k_star": {
            "type": "number"
          }
        },
        "units": {
          "gamma": "m",
          "L_k": "m",
          "D": "m",
          "t_k_star": "dimensionless",
          "L_k_star": "m"
        }
      },
      "description": "Computed domain structure quantities from the continuum theory for the given material parameters and reduced temperatures."
    }
  ],
  "notes": "The interaction range r0 and dipolar coupling strength f are defined as in the continuum theory; the formulas are based on the Kaczér free energy and the magnetization profile of Bulaevskii and Ginzburg. The checker will recompute the quantities using the same input parameters and formulas, comparing with a relative tolerance."
}
```

## How you are scored
A hidden verifier will independently recompute γ, L_k, D, t_k^*, and L_k^* using the same input parameters and formulas. It will compare the values you report in `computed_quantities.json` against its own recomputed results. The final reward is a combination of agreement scores for the arrays and the scalars, with numerical tolerances appropriate for deterministic floating-point computations. Reporting the correct values alone is not sufficient; the verifier checks that your output matches a genuine re‑implementation.
