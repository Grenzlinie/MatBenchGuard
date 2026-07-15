# Layer-resolved hole density and critical temperature calculation for a 6-layer cuprate nanostructure

## Problem background
Selectively doped multilayered La2CuO4 nanostructures can exhibit superconductivity even when each individual layer is non‑superconducting. A minimal electrostatic model has been proposed to explain how carriers delocalize across the layers, giving rise to layer‑resolved hole densities that in turn determine the superconducting critical temperature. This task asks you to compute those hole densities and the resulting Tc for a specific periodic 6‑layer configuration at two different doping levels.

## Approach
The model treats each CuO2 layer as a two‑dimensional electronic system with a rectangular density of states. Mobile hole carriers and immobile dopant ions create local electric potentials that obey discrete electrostatics. Imposing a common Fermi level across all layers leads to a linear system relating the hole density p in each layer to the doping concentration x. For a periodic 6‑layer structure where layers 1,2,5,6 are doped at level x and layers 3,4 are undoped, the system can be solved analytically, yielding three independent densities p1, p2, p3 (with p3 belonging to the nominally undoped central layers) that depend on x and a single dimensionless localization parameter α. Following experimental measurements, α is fixed to 1. Once the densities are obtained, the superconducting critical temperature Tc is estimated from a phenomenological bell‑shaped dependence: Tc(p) = (0.2 − p)*(p − 0.07)*9000 K when 0.07 ≤ p ≤ 0.2, and Tc = 0 otherwise. The explicit expressions for p1, p2, p3 are given in the workflow step below.

## Reproduction target
Compute the layer‑resolved hole densities p1, p2, p3 and the critical temperature Tc (in Kelvin) for the periodic 6‑layer configuration (doping x on layers 1,2,5,6; 0 on layers 3,4) with α = 1, at two doping levels: x = 0.45 and x = 0.15. Output the results as a single JSON file with top‑level keys 'x_045' and 'x_015', each containing the numeric values p1, p2, p3, and Tc.

## Assets
No external datasets, pre‑trained models, or specialised tools are required. All necessary parameters and formulas are provided in the task description. You may use standard numerical libraries (e.g., numpy) to perform the computations.

## Workflow steps

### Step 1: Compute hole densities and Tc for two doping levels
- Role: scored (load-bearing)
- Action: Implement the closed-form expressions for layer-resolved hole densities p1, p2, p3 as functions of doping level x and fixed localization parameter α=1:
  p1 = (1 - 1/((α+1)(α+3))) * x
  p2 = (α+2)/(α+3) * x
  p3 = (α+2)/((α+1)(α+3)) * x
For x=0.45 and x=0.15, compute these densities. Then compute the superconducting critical temperature Tc from p3 using the phenomenological bell-shaped dependence: Tc = (0.2 - p3)*(p3 - 0.07)*9000 K if 0.07 ≤ p3 ≤ 0.2, otherwise Tc = 0. Write all results as a JSON file.
- Output file: `/app/outputs/hole_densities_and_Tc.json`
- Format: json
- Contract: object with top-level keys 'x_045' and 'x_015', each an object with numeric keys 'p1', 'p2', 'p3', 'Tc' (in Kelvin).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hole_densities_and_Tc.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hole_densities_and_Tc.json
- path: `/app/outputs/hole_densities_and_Tc.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed hole densities and Tc for x=0.45 and x=0.15 using the discrete electrostatic model with α=1.
- schema:
  - `type`: object
  - `required`:
    - `x_045`: object
    - `x_015`: object
  - `items`:
    - `p1`: number
    - `p2`: number
    - `p3`: number
    - `Tc`: number
  - `units`:
    - `Tc`: K

Notes: The checker recomputes expected values from the same closed-form expressions and compares the agent's numbers with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hole_densities_and_Tc.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "x_045": "object",
          "x_015": "object"
        },
        "items": {
          "p1": "number",
          "p2": "number",
          "p3": "number",
          "Tc": "number"
        },
        "units": {
          "Tc": "K"
        }
      },
      "description": "Computed hole densities and Tc for x=0.45 and x=0.15 using the discrete electrostatic model with α=1."
    }
  ],
  "notes": "The checker recomputes expected values from the same closed-form expressions and compares the agent's numbers with appropriate tolerances."
}
```

## How you are scored
A hidden verifier will read your JSON file and independently recompute the expected values of p1, p2, p3, and Tc from the same closed‑form expressions and bell‑shaped Tc formula. Each of the eight quantities (four per doping level) is compared against the recomputed reference using predetermined absolute tolerances. Your final score is the fraction of quantities that fall within tolerance. Reporting a plausible number alone is insufficient; the values must match the output of a correct implementation of the prescribed model.
