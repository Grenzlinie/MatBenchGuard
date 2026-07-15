# Cu2Se Thermodynamic Functions Calculation

## Problem background
Copper(I) selenide (Cu₂Se) is a congruently melting semiconductor that undergoes a solid–solid α ↔ β polymorphic phase transition near 400 K. Reliable thermodynamic functions—heat capacity, enthalpy increment, absolute entropy, and reduced Gibbs free energy—over the temperature range from room temperature to above the melting point are essential for phase‑diagram modeling and for processing this material. This task evaluates critically selected literature data and computes the full set of thermodynamic functions for solid Cu₂Se up to 1400 K, including an internal consistency check at the phase transition.

## Approach
The calculation uses recommended input parameters provided in the Assets section: the standard entropy at 298.15 K, a linear heat‑capacity expression for the low‑temperature α phase, a constant heat capacity for the high‑temperature β phase, the transition temperature Tₜᵣ, and the enthalpy of transformation ΔHₜᵣ. For the α phase, integrate the heat capacity from 298.15 K to Tₜᵣ to obtain the enthalpy increment H°(T)−H°(298) and the absolute entropy S°(T). At Tₜᵣ, add the transition enthalpy and the corresponding entropy of transition (ΔSₜᵣ = ΔHₜᵣ/Tₜᵣ) to reach the β‑phase values just above the transition. For the β phase above Tₜᵣ, use the constant heat capacity to extend H and S to 1400 K. For every calculated point, compute the reduced Gibbs free energy Φ(T) = S°(T) − [H°(T)−H°(298)]/T. Finally, verify that the reduced Gibbs free energy is continuous at the transition: Φ for the α phase at Tₜᵣ must equal Φ for the β phase at the same temperature within a small tolerance, which confirms internal consistency of the chosen transition parameters.

## Reproduction target
Reproduce the thermodynamic functions of solid Cu₂Se from 298.15 K to 1400 K using the recommended parameters. Specifically, compute and tabulate the heat capacity, enthalpy increment, absolute entropy, and reduced Gibbs free energy for the α phase at 298.15 K and at the transition temperature, and for the β phase at the transition temperature and at 500, 600, …, 1400 K. In addition, check that the reduced Gibbs free energy is continuous across the transition: the values for the α and β phases at the transition temperature must agree within 0.1 J/(mol·K). The deliverables are the CSV table of thermodynamic functions and a JSON file reporting the two Φ values at the transition and whether they match within the specified tolerance.

## Assets

- Recommended Thermodynamic Parameters

## Workflow steps

### Step 1: Compute Thermodynamic Functions
- Role: scored (load-bearing)
- Action: Using the recommended parameters (S°298, Cp(α) equation, Cp(β), Ttr, ΔHtr), compute the thermodynamic functions (Cp, enthalpy increment H°(T)-H°(298), absolute entropy S°(T), and reduced Gibbs free energy Φ(T) = S°(T) - (H°(T)-H°(298))/T) for all required temperatures and phases. Write the results to a CSV file.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: CSV with columns: T (number, K), Phase (string, 'α' or 'β'), Cp (number, J/(mol·K)), H (number, J/mol), S (number, J/(mol·K)), Phi (number, J/(mol·K)). Rows must include temperatures: 298.15 (α), 400 (α), 400 (β), and 500, 600, …, 1400 (β).
- Scoring: scored by hidden verifier

### Step 2: Verify Internal Consistency at Transition
- Role: scored
- Action: Read the thermodynamic_functions.csv, extract the reduced Gibbs free energy Φ for the α phase at 400 K and for the β phase at 400 K. Check whether they are equal within 0.1 J/(mol·K), and output a JSON object with the two Φ values and a boolean match field.
- Output file: `/app/outputs/consistency_check.json`
- Format: json
- Contract: JSON object with keys: phi_alpha_400 (number, J/(mol·K)), phi_beta_400 (number, J/(mol·K)), match (boolean). match must be true if |phi_alpha_400 - phi_beta_400| ≤ 0.1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions.csv`
- `/app/outputs/consistency_check.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tabulated thermodynamic functions (heat capacity, enthalpy increment, absolute entropy, reduced Gibbs free energy) of solid Cu2Se from 298.15 K to 1400 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Phase`, `Cp`, `H`, `S`, `Phi`
  - `columns`:
    - `T`:
      - `unit`: K
      - `type`: number
    - `Phase`:
      - `type`: string
    - `Cp`:
      - `unit`: J/(mol·K)
      - `type`: number
    - `H`:
      - `unit`: J/mol
      - `type`: number
    - `S`:
      - `unit`: J/(mol·K)
      - `type`: number
    - `Phi`:
      - `unit`: J/(mol·K)
      - `type`: number

### consistency_check.json
- path: `/app/outputs/consistency_check.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Internal consistency check that the reduced Gibbs free energy of the α and β phases are equal at the transition temperature (400 K).
- schema:
  - `type`: object
  - `required`: `phi_alpha_400`, `phi_beta_400`, `match`
  - `properties`:
    - `phi_alpha_400`:
      - `type`: number
      - `unit`: J/(mol·K)
    - `phi_beta_400`:
      - `type`: number
      - `unit`: J/(mol·K)
    - `match`:
      - `type`: boolean

Notes: All thermodynamic parameters are public constants from the literature and are stated in the task instruction. The hidden reference values are the paper's reported tabulated numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Phase",
          "Cp",
          "H",
          "S",
          "Phi"
        ],
        "columns": {
          "T": {
            "unit": "K",
            "type": "number"
          },
          "Phase": {
            "type": "string"
          },
          "Cp": {
            "unit": "J/(mol·K)",
            "type": "number"
          },
          "H": {
            "unit": "J/mol",
            "type": "number"
          },
          "S": {
            "unit": "J/(mol·K)",
            "type": "number"
          },
          "Phi": {
            "unit": "J/(mol·K)",
            "type": "number"
          }
        }
      },
      "description": "Tabulated thermodynamic functions (heat capacity, enthalpy increment, absolute entropy, reduced Gibbs free energy) of solid Cu2Se from 298.15 K to 1400 K."
    },
    {
      "file": "consistency_check.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "phi_alpha_400",
          "phi_beta_400",
          "match"
        ],
        "properties": {
          "phi_alpha_400": {
            "type": "number",
            "unit": "J/(mol·K)"
          },
          "phi_beta_400": {
            "type": "number",
            "unit": "J/(mol·K)"
          },
          "match": {
            "type": "boolean"
          }
        }
      },
      "description": "Internal consistency check that the reduced Gibbs free energy of the α and β phases are equal at the transition temperature (400 K)."
    }
  ],
  "notes": "All thermodynamic parameters are public constants from the literature and are stated in the task instruction. The hidden reference values are the paper's reported tabulated numbers."
}
```

## How you are scored
Each workflow stage produces an artifact that a hidden verifier scores independently. The verifier recomputes the thermodynamic functions using the same input parameters and compares your submitted CSV values to its own recomputed reference within appropriate tolerances. It also verifies that the consistency check JSON contains the correct Φ values at the transition and that the match field is true when the difference is within the required tolerance. The final reward is a weighted combination of the per‑stage scores; simply reporting a number that matches the paper is not sufficient—the verifier expects the arithmetic to be carried out correctly from the given constants.
