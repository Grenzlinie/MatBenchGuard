# Tangential Nucleation Dimensions and Start Field for Iron Whiskers

## Problem background
In ferromagnetic whiskers with easy axis along the cylinder, the experimentally observed nucleation field for magnetization reversal is much larger (closer to zero) than the conventional theoretical predictions for long cylinders when the whisker radius exceeds ~1000 Å. This discrepancy, known as Brown's paradox, suggests that end‑face stray fields may play a critical role. A model has been proposed in which the nucleation process is initiated at the end face, and the tangential component of magnetization near the end face is considered. The high‑field regime, where the disturbance is localized, leads to predictions for the nucleus dimensions and the start field that can be compared with experiment. The task is to compute these quantities for iron whiskers using the prescribed trial function and material constants.

## Approach
The model considers a cylindrical ferromagnetic sample with its easy axis along the cylinder axis. In the high‑field limit, the magnetization disturbance near the end face is small and confined to a shallow region. Only the tangential magnetization component is treated. A trial function for this component is chosen that is localized near the axis (first trial function), vanishing beyond a radial extent r (in units of sample radius) and a penetration depth d (in units of sample radius). The total energy change due to the disturbance includes stray‑field energy, exchange energy, anisotropy energy, and the applied field energy. Using small‑angle approximations, the energy change is expressed as a function of r, d, and the applied field H. The instability condition for the uniformly magnetized state requires that the energy change become non‑positive. From this, an equation for H is obtained. The start field H_s is defined as the maximum H for which the uniform state first becomes unstable; it is found by imposing the extremum conditions ∂H/∂r = 0 and ∂H/∂d = 0. Solving these yields algebraic equations for r and d. Using the known iron material constants (saturation magnetization I_s, anisotropy constant K, exchange constant C) and the given whisker radii, r, d, and H_s are computed. The scaling relation can then be checked by computing the coefficient d/r².

## Reproduction target
Compute the dimensionless nucleus dimensions r (radial extent) and d (penetration depth) and the start field H_s (in Oe) for iron whiskers of radius R = 1 μm and R = 10 μm, using the high‑field end‑face tangential model and the first trial function. Additionally compute the scaling coefficient d/r² averaged over the two radii. Write the results to nucleus_results.json as a JSON object with keys 'R_1um' (with fields 'r', 'd', 'Hs'), 'R_10um' (with fields 'r', 'd', 'Hs'), and 'scaling_coefficient' (a number).

## Assets

- Iron magnetic material constants (I_s, K, C)

## Workflow steps

### Step 1: Compute nucleus dimensions and start field
- Role: scored (load-bearing)
- Action: Implement the high-field end-face tangential nucleation model using the first trial function (localized near the axis). Using the extremum conditions on total energy, derive the algebraic equations for the dimensionless nucleus radius r and penetration depth d, then compute r, d, and the start field H_s for iron whiskers of radius R=1 μm and R=10 μm, using the provided iron material constants. Also compute the scaling coefficient d/r^2 (average over the two radii). Write results to nucleus_results.json.
- Output file: `/app/outputs/nucleus_results.json`
- Format: json
- Contract: JSON object with keys: 'R_1um' (object with numeric fields 'r', 'd', 'Hs'), 'R_10um' (object with numeric fields 'r', 'd', 'Hs'), and 'scaling_coefficient' (numeric).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleus_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleus_results.json
- path: `/app/outputs/nucleus_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains computed nucleus dimensions and start field for iron whiskers of radii 1 μm and 10 μm, plus the scaling coefficient d/r^2.
- schema:
  - `type`: object
  - `required`:
    - `R_1um`:
      - `r`: float
      - `d`: float
      - `Hs`: float
    - `R_10um`:
      - `r`: float
      - `d`: float
      - `Hs`: float
    - `scaling_coefficient`: float

Notes: r and d are dimensionless (in units of sample radius); Hs is in Oe. The scaling coefficient is d/r^2 averaged over the two radii.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleus_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "R_1um": {
            "r": "float",
            "d": "float",
            "Hs": "float"
          },
          "R_10um": {
            "r": "float",
            "d": "float",
            "Hs": "float"
          },
          "scaling_coefficient": "float"
        }
      },
      "description": "Contains computed nucleus dimensions and start field for iron whiskers of radii 1 μm and 10 μm, plus the scaling coefficient d/r^2."
    }
  ],
  "notes": "r and d are dimensionless (in units of sample radius); Hs is in Oe. The scaling coefficient is d/r^2 averaged over the two radii."
}
```

## How you are scored
A hidden verifier reads your nucleus_results.json and compares your computed r, d, Hs, and the scaling coefficient to the paper‑reported benchmark values, using prescribed relative tolerances. The scoring is per‑field: each numeric result contributes a fraction of the total reward, with the results for both radii and the scaling coefficient weighted appropriately. The reward is aggregated across all scored quantities. Reproducing the exact workflow—deriving the extremum equations from the energy expression and solving them—is essential; merely guessing the numbers or copying them from an external source will not satisfy the verifier, as the tolerances are chosen to accept legitimate computational spread while rejecting unrealistic values.
