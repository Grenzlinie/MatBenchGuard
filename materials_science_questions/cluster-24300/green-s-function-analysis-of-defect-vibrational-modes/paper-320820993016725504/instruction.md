# Compute Localized Spin-Wave Mode Dispersion for a Ferromagnetic Plane Defect

## Problem background
In a ferromagnetic crystal, a planar defect (such as an antiphase boundary or stacking fault) can trap spin-wave excitations, creating localized modes that propagate along the defect plane but decay away from it. The problem is to determine the energies of these localized spin-system oscillations in a simple cubic ferromagnet with nearest-neighbor Heisenberg exchange, where the exchange interactions and Landé factors near the defect are perturbed. The quantities to compute are the dispersion relations E⁺(κ) for the symmetric mode (SM) and E⁻(κ) for the antisymmetric mode (AM), as functions of the in-plane wave vector κ, and to verify their existence under the appropriate localization conditions.

## Approach
The analytic dispersion relations for the localized modes are derived from a Green's function approach. The workflow computes these formulas directly in Python (NumPy). For a given set of defect parameters (ξ, β, γ), external magnetic field H, and material constants (exchange J, spin S, Landé factor g), the agent first evaluates the bulk in-plane energy ℰ_κ = g μ₀ H + J S (4 - 2 cos κ_x - 2 cos κ_z). A dimensionless parameter ε is computed as ε = -(μ₀ g H γ' + ξ ℰ_κ)/(J S) with γ' = γ - ξ. The symmetric mode energy is then E⁺ = ℰ_κ + 2 J S ε²/(2(ε-1)), and the antisymmetric mode energy is E⁻ = ℰ_κ + 2 J S (ε+2(1-β))²/(2(ε+1-2β)). The calculation is performed on a grid of κ points, and for each point the localization conditions are checked: SM exists when ε ≤ 0 or ε ≥ 2; AM exists when ε ≤ 2(β-1) or ε ≥ 2β. Additionally, the independence of E⁺ from β is verified by recomputing E⁺ at a fixed κ while varying β, with other parameters held constant.

## Reproduction target
The goal is to produce a JSON file (`dispersion_results.json`) that contains: the parameter values used (ξ, β, γ, H, g'/g, J S), a boolean flag indicating whether the localization conditions are satisfied for the chosen parameters, a table of (κ_x, κ_z, E⁺, E⁻) points evaluated over a representative grid of in-plane wave vectors, and a section demonstrating that E⁺ does not change when β is varied (at a selected κ-point). The parameters to use are specified in the workflow step. The file must be written to `/app/outputs/dispersion_results.json`.

## Assets

- Python 3 with NumPy: numpy

## Workflow steps

### Step 1: Compute LSSO dispersion relations
- Role: scored (load-bearing)
- Action: Compute the energies E⁺(κ) (symmetric mode, SM) and E⁻(κ) (antisymmetric mode, AM) for localized spin-wave oscillations in a simple cubic ferromagnet with a plane defect. Use the analytic dispersion relations: ℰ_κ = g μ₀ H + J S (4 - 2 cos κ_x - 2 cos κ_z); ε = −(μ₀ g H γ' + ξ ℰ_κ)/(J S) with γ' = γ − ξ; then E⁺ = ℰ_κ + 2 J S ε²/(2(ε−1)) and E⁻ = ℰ_κ + 2 J S (ε+2(1−β))²/(2(ε+1−2β)). Choose representative defect parameters (e.g., ξ=0.5, β=0.5, γ=0, H=0, g'=g) and a grid of κ points in the (κ_x, κ_z) plane. For each point, check the localization conditions: ε ≤ 0 or ε ≥ 2 for SM; ε ≤ 2(β-1) or ε ≥ 2β for AM. Also verify the beta-independence of E⁺ by varying β while keeping ξ, γ, H fixed, and compute E⁺ at a selected κ. Write all results to /app/outputs/dispersion_results.json.
- Output file: `/app/outputs/dispersion_results.json`
- Format: json
- Contract: {"parameters": {"xi": "float", "beta": "float", "gamma": "float", "H": "float", "g_prime_over_g": "float", "J_S": "float"}, "condition_check": {"SM_localization_condition": "bool", "AM_localization_condition": "bool"}, "points": [{"kappa_x": "float", "kappa_z": "float", "E_plus": "float", "E_minus": "float"}], "beta_independence_check": {"kappa_x": "float", "kappa_z": "float", "beta_values": ["float"], "E_plus_values": ["float"], "constant_confirmed": "bool"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dispersion_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dispersion_results.json
- path: `/app/outputs/dispersion_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed dispersion of symmetric and antisymmetric localized modes, with verification of localization conditions and beta-independence of the symmetric mode.
- schema:
  - `type`: object
  - `required`:
    - `parameters`: object with keys xi, beta, gamma, H, g_prime_over_g, J_S (all float)
    - `condition_check`: object with Boolean keys SM_localization_condition and AM_localization_condition
    - `points`: array of objects, each with float keys kappa_x, kappa_z, E_plus, E_minus
    - `beta_independence_check`: object with float keys kappa_x, kappa_z, array beta_values, array E_plus_values, Boolean constant_confirmed
  - `items`: object
  - `required_columns`:
  - `units`:
    - `kappa_x`: dimensionless (wave vector component)
    - `kappa_z`: dimensionless (wave vector component)
    - `E_plus`: energy units (same as J S)
    - `E_minus`: energy units (same as J S)

Notes: The agent must use the analytic formulas exactly as given; any physically equivalent formulation is acceptable as long as numerical results match within the scoring tolerance. The checker recomputes E⁺ and E⁻ at hidden κ-points and checks conditions and beta-independence.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dispersion_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "parameters": "object with keys xi, beta, gamma, H, g_prime_over_g, J_S (all float)",
          "condition_check": "object with Boolean keys SM_localization_condition and AM_localization_condition",
          "points": "array of objects, each with float keys kappa_x, kappa_z, E_plus, E_minus",
          "beta_independence_check": "object with float keys kappa_x, kappa_z, array beta_values, array E_plus_values, Boolean constant_confirmed"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "kappa_x": "dimensionless (wave vector component)",
          "kappa_z": "dimensionless (wave vector component)",
          "E_plus": "energy units (same as J S)",
          "E_minus": "energy units (same as J S)"
        }
      },
      "description": "Computed dispersion of symmetric and antisymmetric localized modes, with verification of localization conditions and beta-independence of the symmetric mode."
    }
  ],
  "notes": "The agent must use the analytic formulas exactly as given; any physically equivalent formulation is acceptable as long as numerical results match within the scoring tolerance. The checker recomputes E⁺ and E⁻ at hidden κ-points and checks conditions and beta-independence."
}
```

## How you are scored
A hidden verifier scores your submission independently. It recomputes E⁺ and E⁻ from your reported parameters at a set of κ-points not disclosed to you, compares them to your values in `dispersion_results.json`, and checks that your localization-condition evaluations and β-independence claim are consistent with a correct implementation of the analytic formulas. The final score combines these checks with weights that reflect the importance of each part. Simply writing down correct-looking values without executing the proper computation will not pass the verifier's recomputation.
