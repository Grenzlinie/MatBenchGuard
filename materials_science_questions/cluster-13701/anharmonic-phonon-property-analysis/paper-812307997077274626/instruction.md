# Minimal Group Size for Local Thermal States in a Harmonic Chain

## Problem background
In a quantum chain at thermal equilibrium, dividing the system into groups of particles raises the question of whether local temperatures can be meaningfully defined. We focus on a harmonic chain, a model that describes the thermal properties of insulating solids. Using the Debye continuum approximation, general microscopic conditions (A and B) give a lower bound on the number of particles per group, denoted n_min, that depends on the global temperature T and the Debye temperature Θ. When translated to real materials, n_min also determines the smallest length scale l_min = n_min × a₀ on which a local temperature can exist. The task is to compute n_min as a function of T/Θ and to estimate l_min for several representative solids.

## Approach
The harmonic chain is partitioned into groups of n adjacent particles. In the Debye limit (long-wavelength continuum, n ≫ 1) the group–group interaction energy simplifies, and the thermal expectation energy is obtained by numerical integration of the Debye heat-capacity integral. Two accuracy parameters are introduced: α (which sets the relevant energy range around the thermal average) and δ (which controls how constant the energy-dependent part of the group interactions must be). Condition A yields one lower bound on n, while condition B yields a second, stronger bound at higher temperatures. The overall minimal group size n_min is the maximum of these two bounds. By evaluating the bounds over a range of reduced temperatures T/Θ and combining the result with known Debye temperatures and lattice constants, one obtains the minimal length scale l_min for different materials.

## Reproduction target
Compute n_min over the reduced-temperature range T/Θ ∈ [0.01, 100] using α = 10 and δ = 0.01. For each T/Θ, determine n_min as the maximum of the two bounds. Output the full curve as a list of (T_ratio, n_min) pairs. Then, using the computed bound formulas, calculate n_min and the minimal length scale l_min = n_min × a₀ (in micrometres) for the following materials and temperatures:

- Iron: Θ ≈ 470 K, a₀ ≈ 2.5 Å, at T = 470 K and T = 1 K
- Carbon: Θ ≈ 2230 K, a₀ ≈ 1.5 Å, at T = 270 K
- Silicon: Θ ≈ 645 K, a₀ ≈ 2.4 Å, at T = 1 K

All results must be written to the single JSON file `/app/outputs/harmonic_results.json` with the structure described in the output contract.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute harmonic chain n_min and material length scales
- Role: scored (load-bearing)
- Action: Implement the Debye-approximation formulas for the harmonic chain. Compute the dimensionless thermal energy per particle e_bar = (T/Θ)^2 ∫_0^{Θ/T} x/(e^x - 1) dx (use numerical integration) and the ground-state energy per particle e₀ = 1/4. Then compute the two lower bounds: n_A = (Θ/T) * (α/(4 e_bar)) * ( (4 e_bar/α) + 1)^2 (bound from condition A) and n_B = (2α/δ) * (Θ/T) * e_bar (bound from condition B), with α=10 and δ=0.01. The minimal group size for a given T/Θ is n_min = max(n_A, n_B). Evaluate both bounds over a dense set of T/Θ ratios from 0.01 to 100, taking the maximum at each point, to produce the n_min curve. For the three materials (iron, carbon, silicon) with the given Debye temperatures and lattice constants, compute n_min at the specified temperatures and then the minimal length scale l_min = n_min × a₀ (in micrometres). Write all results to /app/outputs/harmonic_results.json.
- Output file: `/app/outputs/harmonic_results.json`
- Format: json
- Contract: {"n_min_curve": [{"T_ratio": float, "n_min": float}], "material_estimates": [{"material": string, "T": float, "a0_angstrom": float, "theta": float, "n_min": float, "l_min_um": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/harmonic_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### harmonic_results.json
- path: `/app/outputs/harmonic_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored result: minimal group size curve and material length-scale estimates. The checker recomputes the expected n_min from the same equations and parameters, then compares the submitted values against the recomputed reference within per-check tolerances.
- schema:
  - `type`: object
  - `required`:
    - `n_min_curve`: array of objects with T_ratio (float) and n_min (float)
    - `material_estimates`: array of objects with material (string), T (float), a0_angstrom (float), theta (float), n_min (float), l_min_um (float)
  - `items`:
    - `n_min_curve_item`:
      - `T_ratio`: float
      - `n_min`: float
    - `material_estimate_item`:
      - `material`: string
      - `T`: float
      - `a0_angstrom`: float
      - `theta`: float
      - `n_min`: float
      - `l_min_um`: float

Notes: The target_policy is reference_match because the agent submits computed quantities, and the checker independently recomputes the expected reference values from the same analytical formulas and parameters (no hidden holdout). Equality is not required; tolerances based on expected numerical integration differences are applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "harmonic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "n_min_curve": "array of objects with T_ratio (float) and n_min (float)",
          "material_estimates": "array of objects with material (string), T (float), a0_angstrom (float), theta (float), n_min (float), l_min_um (float)"
        },
        "items": {
          "n_min_curve_item": {
            "T_ratio": "float",
            "n_min": "float"
          },
          "material_estimate_item": {
            "material": "string",
            "T": "float",
            "a0_angstrom": "float",
            "theta": "float",
            "n_min": "float",
            "l_min_um": "float"
          }
        }
      },
      "description": "Scored result: minimal group size curve and material length-scale estimates. The checker recomputes the expected n_min from the same equations and parameters, then compares the submitted values against the recomputed reference within per-check tolerances."
    }
  ],
  "notes": "The target_policy is reference_match because the agent submits computed quantities, and the checker independently recomputes the expected reference values from the same analytical formulas and parameters (no hidden holdout). Equality is not required; tolerances based on expected numerical integration differences are applied."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that independently recomputes the expected n_min values from the same analytical formulas and parameters. The verifier extracts your reported n_min curve and compares it at a set of check points across the T/Θ range, allowing for small numerical differences. It also verifies that the curve exhibits the correct physical asymptotics: approximately constant n_min at high T/Θ and a well-defined log–log slope at low T/Θ. For the material estimates, the verifier recomputes n_min and l_min from the given parameters and checks agreement with your reported values. Each check passes if the deviation falls within an allowed tolerance. The final score is the fraction of checks that passed, with every check carrying equal weight. Reporting numbers alone is not sufficient; the verifier confirms that they follow from the prescribed procedure and accuracy settings.
