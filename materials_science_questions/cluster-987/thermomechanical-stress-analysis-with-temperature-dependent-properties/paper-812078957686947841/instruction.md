# Thermodynamic Analysis of Mullite Decomposition under Low Oxygen Partial Pressure

## Problem background
2:1 mullite (2Al2O3·SiO2) is a ceramic material. When heated to high temperatures in atmospheres with low oxygen partial pressure, its surface can decompose to α-Al2O3. The decomposition is believed to proceed via gas-phase evolution of SiO and O2. This task uses standard thermodynamic data to compute the key quantities that govern this decomposition: the Gibbs free energy changes and equilibrium constants for the proposed reactions, and the resulting equilibrium partial pressures under different atmospheric conditions. The computed values shed light on the thermodynamic feasibility of mullite decomposition.

## Approach
The approach relies on standard thermodynamic calculations. First, obtain Gibbs free energies of formation (ΔfG°) for all relevant species—Al2O3(s), SiO2(s), 3Al2O3·2SiO2(s) (mullite), SiO(g), O2(g), SiO2(g), Ta(s), and Ta2O5(s)—from a recognized public thermochemical database such as JANAF. Then compute the standard Gibbs free energy change (ΔG°) and equilibrium constant (log K) for two reactions at 1650, 1700, 1750, and 1800°C: (1) the decomposition of mullite to alumina, SiO(g), and O2(g); and (2) the oxidation of SiO(g) to SiO2(g). Using these equilibrium constants and the known oxygen partial pressures in air (0.21 atm) and in a Ta-gettered helium atmosphere (determined by the Ta/Ta2O5 equilibrium), compute the equilibrium partial pressures of SiO and SiO2 at 1650°C in both environments. All results are to be compiled into a single structured JSON file.

## Reproduction target
Compute the standard Gibbs free energy changes (ΔG°, in kcal/mol) and base-10 logarithm of the equilibrium constants (log K) for the two specified reactions at four temperatures: 1650, 1700, 1750, and 1800°C. Then, using the computed equilibrium constants and the given oxygen partial pressures, determine the equilibrium partial pressures of SiO and SiO2 (in atm) in air and in helium at 1650°C. Write all these quantities to the file `/app/outputs/thermodynamic_reproduction.json`. The file must follow the precise schema described in the Output contract below.

## Assets

- Standard thermodynamic database (JANAF or equivalent): https://janaf.nist.gov/

## Workflow steps

### Step 1: Calculate O₂ partial pressure in He from Ta/Ta₂O₅ equilibrium
- Role: process
- Action: Using standard thermodynamic data for Ta(s) and Ta₂O₅(s), compute the equilibrium oxygen partial pressure (log P_O₂) in the He atmosphere at 1650, 1700, 1750, and 1800°C based on the reaction 2Ta(s) + (5/2)O₂(g) ⇌ Ta₂O₅(s).
- Evidence: `/app/outputs/ta_o2_log.txt`

### Step 2: Calculate ΔG° and log K for mullite decomposition and SiO oxidation
- Role: process
- Action: Using standard thermodynamic data for 3Al₂O₃·2SiO₂(s), Al₂O₃(s), SiO(g), O₂(g), and SiO₂(g), compute standard Gibbs free energy changes (ΔG° in kcal/mol) and log₁₀(K) for reaction (2): 3Al₂O₃·2SiO₂(s) ⇌ 3Al₂O₃(s) + 2SiO(g) + O₂(g) and reaction (3): 2SiO(g) + O₂(g) ⇌ 2SiO₂(g) at 1650, 1700, 1750, and 1800°C.
- Evidence: `/app/outputs/reactions_dg_log.txt`

### Step 3: Compute equilibrium partial pressures and compile final results
- Role: scored (load-bearing)
- Action: Using the equilibrium constants from step_01 and the P_O₂ values from step_00 (for He) along with the known P_O₂ in air (10⁻⁰·⁶⁸ atm ≈ 0.21 atm), compute the equilibrium partial pressures of SiO and SiO₂ in air and in He at 1650°C. Write a JSON file containing all computed quantities: reaction (2) ΔG° and log K, reaction (3) ΔG° and log K, and equilibrium_partial_pressures_at_1650C with values for air and He.
- Output file: `/app/outputs/thermodynamic_reproduction.json`
- Format: json
- Contract: JSON object with top-level keys: reaction_2, reaction_3, equilibrium_partial_pressures_at_1650C. reaction_2 and reaction_3 each contain: temperatures_C (list of ints), delta_G_kcal_per_mol (list of floats), log_K (list of floats). equilibrium_partial_pressures_at_1650C contains: air and He, each containing P_SiO_atm (float) and P_SiO2_atm (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_reproduction.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_reproduction.json
- path: `/app/outputs/thermodynamic_reproduction.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the reproduced standard Gibbs free energy changes, equilibrium constants (log K) for the two reactions at four temperatures, and the equilibrium partial pressures of SiO and SiO₂ in air and He at 1650°C.
- schema:
  - `type`: object
  - `required`: `reaction_2`, `reaction_3`, `equilibrium_partial_pressures_at_1650C`
  - `items`: object
  - `reaction_2`:
    - `type`: object
    - `required`: `temperatures_C`, `delta_G_kcal_per_mol`, `log_K`
    - `temperatures_C`:
      - `type`: array
      - `items`:
        - `type`: integer
      - `description`: Temperatures 1650, 1700, 1750, 1800
    - `delta_G_kcal_per_mol`:
      - `type`: array
      - `items`:
        - `type`: number
      - `unit`: kcal/mol
    - `log_K`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: log₁₀(K)
  - `reaction_3`:
    - `type`: object
    - `required`: `temperatures_C`, `delta_G_kcal_per_mol`, `log_K`
    - `temperatures_C`:
      - `type`: array
      - `items`:
        - `type`: integer
    - `delta_G_kcal_per_mol`:
      - `type`: array
      - `items`:
        - `type`: number
      - `unit`: kcal/mol
    - `log_K`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: log₁₀(K)
  - `equilibrium_partial_pressures_at_1650C`:
    - `type`: object
    - `required`: `air`, `He`
    - `air`:
      - `type`: object
      - `required`: `P_SiO_atm`, `P_SiO2_atm`
      - `P_SiO_atm`:
        - `type`: number
        - `unit`: atm
      - `P_SiO2_atm`:
        - `type`: number
        - `unit`: atm
    - `He`:
      - `type`: object
      - `required`: `P_SiO_atm`, `P_SiO2_atm`
      - `P_SiO_atm`:
        - `type`: number
        - `unit`: atm
      - `P_SiO2_atm`:
        - `type`: number
        - `unit`: atm

Notes: The computed values are compared against the paper's reported values with appropriate tolerances to account for differences in database editions. Only the thermodynamic analysis supporting mullite decomposition is scored; the bubble formation analysis is out of scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_reproduction.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "reaction_2",
          "reaction_3",
          "equilibrium_partial_pressures_at_1650C"
        ],
        "items": {},
        "reaction_2": {
          "type": "object",
          "required": [
            "temperatures_C",
            "delta_G_kcal_per_mol",
            "log_K"
          ],
          "temperatures_C": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "description": "Temperatures 1650, 1700, 1750, 1800"
          },
          "delta_G_kcal_per_mol": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "unit": "kcal/mol"
          },
          "log_K": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "log₁₀(K)"
          }
        },
        "reaction_3": {
          "type": "object",
          "required": [
            "temperatures_C",
            "delta_G_kcal_per_mol",
            "log_K"
          ],
          "temperatures_C": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          },
          "delta_G_kcal_per_mol": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "unit": "kcal/mol"
          },
          "log_K": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "log₁₀(K)"
          }
        },
        "equilibrium_partial_pressures_at_1650C": {
          "type": "object",
          "required": [
            "air",
            "He"
          ],
          "air": {
            "type": "object",
            "required": [
              "P_SiO_atm",
              "P_SiO2_atm"
            ],
            "P_SiO_atm": {
              "type": "number",
              "unit": "atm"
            },
            "P_SiO2_atm": {
              "type": "number",
              "unit": "atm"
            }
          },
          "He": {
            "type": "object",
            "required": [
              "P_SiO_atm",
              "P_SiO2_atm"
            ],
            "P_SiO_atm": {
              "type": "number",
              "unit": "atm"
            },
            "P_SiO2_atm": {
              "type": "number",
              "unit": "atm"
            }
          }
        }
      },
      "description": "JSON file containing the reproduced standard Gibbs free energy changes, equilibrium constants (log K) for the two reactions at four temperatures, and the equilibrium partial pressures of SiO and SiO₂ in air and He at 1650°C."
    }
  ],
  "notes": "The computed values are compared against the paper's reported values with appropriate tolerances to account for differences in database editions. Only the thermodynamic analysis supporting mullite decomposition is scored; the bubble formation analysis is out of scope."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads your `thermodynamic_reproduction.json`. For each required quantity—ΔG°, log K, and equilibrium partial pressures—the verifier compares your computed value against an expected reference value using appropriate absolute tolerances. Scores are awarded per field based on how close the computed value is to the reference. The final reward is the average of these per-field scores, normalized between 0.0 and 1.0. Reporting a result that is far from the expected value yields a low score; a result that lies within the tolerance band receives partial or full credit. The scoring is designed to accommodate minor variations that may arise from using different editions of the thermodynamic database, but will penalize clearly incorrect calculations. You do not need to know the reference values or tolerances; just perform the computations correctly as described.
