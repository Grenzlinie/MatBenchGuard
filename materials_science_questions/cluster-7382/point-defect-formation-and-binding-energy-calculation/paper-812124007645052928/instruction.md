# Statistical-Thermodynamic Model of Vacancy Complexes in Dilute Solid Solutions

## Problem background
In dilute binary solid solutions where the constituent atoms have different atomic radii, elastic stresses around impurity atoms can lead to the formation of impurity-vacancy complexes. When impurity atoms bind in the first coordination sphere of a vacancy, the elastic energy is partially relaxed, making such complexes thermodynamically stable at low temperatures. This task explores a statistical-thermodynamic model that describes the equilibrium distribution of free impurity atoms and vacancy complexes as a function of temperature. The model predicts the fraction of free impurities and the total concentration of vacancy complexes for a given set of material parameters. Your goal is to implement this model and compute the equilibrium concentrations for a specific parameter set.

## Approach
The theoretical framework starts from a free-energy functional that accounts for the configurational entropy of free impurities and complexes, and a binding energy for impurity atoms that occupy the first coordination shell of a vacancy. By minimizing the free energy under the constraint of fixed total impurity concentration, one obtains a set of equations: a self-consistency equation for an auxiliary variable (the renormalized Lagrange multiplier λ₁), an expression for the concentration of free impurity atoms (c_4He), and a closed-form formula for the total concentration of vacancy complexes (c_bar). The model is parametrized by the total impurity concentration c0, the vacancy formation energy u0, the impurity-vacancy interaction energy Δw, and the coordination number z. For each temperature T, λ₁ is found by solving the self-consistency equation numerically, and c_4He/c0 and c_bar are then computed from the corresponding formulas. The workflow consists of implementing the model equations and solving them for the six specified temperature points.

## Reproduction target
Implement the statistical-thermodynamic model of vacancy complexes for the parameter set c0 = 0.02, u0 = 6 K, Δw = -3 K, and z = 12. Numerically solve the self-consistency equation at each of the six temperatures [0.05, 0.1, 0.2, 0.5, 1.0, 2.0] K. From the solution, compute the free impurity fraction c_4He / c0 and the total complex concentration c_bar. Output the results in a JSON file ('vacancy_complex_results.json') with the structure: a top-level object containing 'parameters' (the input parameters) and 'results' (an array of objects with keys temperature_K, c_4He_ratio, and c_bar).

## Assets

- Python with SciPy/NumPy: scipy numpy

## Workflow steps

### Step 1: Compute vacancy complex equilibrium concentrations
- Role: scored (load-bearing)
- Action: Implement the statistical-thermodynamic model for vacancy complexes in a dilute solid solution. Solve the self-consistency equation exp(λ₁/T) = 1 + z * exp(-Δw/T) * [1 + c0 * exp(-λ₁/T) * exp(-Δw/T)]^(z-1) * exp(-u0/T) numerically for λ₁. Then compute the free impurity fraction c_4He_ratio = exp(-λ₁/T) and the total complex concentration c_bar = [1 + c0 * exp(-λ₁/T) * exp(-Δw/T)]^z * exp(-u0/T). Use parameters c0 = 0.02, u0 = 6 K, Δw = -3 K, z = 12, and temperatures T = 0.05, 0.1, 0.2, 0.5, 1.0, 2.0 K. Store the results in a JSON file.
- Output file: `/app/outputs/vacancy_complex_results.json`
- Format: json
- Contract: A JSON object with fields: "parameters" (object: c0 number, u0_K number, delta_w_K number, z integer) and "results" (array of objects, each with keys temperature_K number, c_4He_ratio number, c_bar number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_complex_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_complex_results.json
- path: `/app/outputs/vacancy_complex_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium concentrations of free impurities and vacancy complexes computed by the agent for the specified parameter set and temperatures.
- schema:
  - `type`: object
  - `required`: `parameters`, `results`
  - `properties`:
    - `parameters`:
      - `type`: object
      - `properties`:
        - `c0`: number
        - `u0_K`: number
        - `delta_w_K`: number
        - `z`: integer
    - `results`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `temperature_K`: number
          - `c_4He_ratio`: number
          - `c_bar`: number

Notes: The checker will re-implement the identical analytical model, solve the self-consistency equation, and compare the agent's c_4He_ratio and c_bar values against its own recomputed values at each temperature point within an absolute tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_complex_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "parameters",
          "results"
        ],
        "properties": {
          "parameters": {
            "type": "object",
            "properties": {
              "c0": "number",
              "u0_K": "number",
              "delta_w_K": "number",
              "z": "integer"
            }
          },
          "results": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "temperature_K": "number",
                "c_4He_ratio": "number",
                "c_bar": "number"
              }
            }
          }
        }
      },
      "description": "Equilibrium concentrations of free impurities and vacancy complexes computed by the agent for the specified parameter set and temperatures."
    }
  ],
  "notes": "The checker will re-implement the identical analytical model, solve the self-consistency equation, and compare the agent's c_4He_ratio and c_bar values against its own recomputed values at each temperature point within an absolute tolerance."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that re-implements the identical analytical model and recomputes the expected c_4He_ratio and c_bar for each temperature. After checking that your JSON schema is valid, the verifier compares your reported values to its recomputed values at every temperature point. The final reward is the fraction of temperature points for which both c_4He_ratio and c_bar agree within a predetermined tolerance. Higher-quality solutions that match the reference closely across all temperatures will therefore receive higher scores.
