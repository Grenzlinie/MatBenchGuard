# Thermodynamic Equilibrium Composition of WO₃ Chalcogenization

## Problem background
The synthesis of inorganic fullerene-like (IF) WSe₂ involves a gas‑solid reaction between tungsten oxide (WO₃) nanoparticles and selenium vapour. Understanding the thermodynamics of the sulfidization and selenization of WO₃ is a prerequisite for rational process design. In particular, the equilibrium composition of the gas‑solid system as a function of temperature and the presence – or absence – of hydrogen as a reducer determines whether conversion to the dichalcogenide is thermodynamically favoured and helps to identify practical operating windows. For the analogous sulfidization process equilibrium calculations have shown that conversion is favourable over a wide temperature range, even in the absence of hydrogen, while for selenization the situation may be different. Your task is to perform independent thermodynamic equilibrium calculations for the four relevant reactions, thereby obtaining the weight percentages of residual WO₃ and of the product (WS₂ or WSe₂) under conditions that are relevant to the synthesis described in the literature.

## Approach
Use standard thermochemical data (e.g. NIST‑JANAF tables or NASA polynomial representations) to implement a Gibbs free energy minimisation procedure (or, equivalently, to solve the set of equilibrium constants) for systems containing all gaseous and solid species that participate in the reactions. The reactions to consider are:

1) WO₃ + 3 S + H₂ ⇌ WS₂ + H₂O + SO₂
2) 2 WO₃ + 7 S ⇌ 2 WS₂ + 3 SO₂
3) WO₃ + 3 Se + H₂ ⇌ WSe₂ + H₂O + SeO₂
4) 2 WO₃ + 7 Se ⇌ 2 WSe₂ + 3 SeO₂

The initial loading (weight percent) is fixed at 5 % WO₃, 10 % S (or Se, depending on the reaction), 38 % H₂ (when present), the balance being N₂. The total pressure is 1 atm. For each of the four reaction systems perform the equilibrium calculation at the five temperatures 823, 923, 1023, 1123, and 1223 K. For every temperature – reaction combination compute the equilibrium weight percentages of the unconverted oxide (WO₃) and of the chalcogenide product (WS₂ for the first two reactions, WSe₂ for the last two). Use a consistent computational toolchain; an open‑source chemical thermodynamics library such as Cantera is recommended. Record the results in a CSV file as specified in the workflow steps below.

## Reproduction target
Produce a CSV file, `equilibrium_compositions.csv`, containing the equilibrium weight percentages of WO₃ and of the product (WS₂ or WSe₂) for the four reaction systems (sulfidization with H₂, sulfidization without H₂, selenization with H₂, selenization without H₂) at each of the five temperatures listed above. The file must have exactly 20 data rows (4 reactions × 5 temperatures) with the columns: `reaction_label`, `T_K`, `WO3_wt`, `product_wt`. The reaction label must be one of `sulfidization_with_H2`, `sulfidization_without_H2`, `selenization_with_H2`, `selenization_without_H2`. `T_K` is an integer temperature in K, `WO3_wt` and `product_wt` are floating‑point weight percentages. The reference implementation will compare your results against values reported for the same conditions in the literature; the file format and column ordering must be followed exactly.

## Assets

- Standard thermochemical data for species (WO₃, WS₂, WSe₂, S, Se, H₂O, SO₂, SeO₂, H₂, N₂): https://janaf.nist.gov/
- Cantera (chemical thermodynamics toolkit): https://cantera.org

## Workflow steps

### Step 1: Thermodynamic equilibrium composition calculation
- Role: scored (load-bearing)
- Action: Perform thermodynamic equilibrium calculations for the four gas-solid reactions (sulfidization with H₂, sulfidization without H₂, selenization with H₂, selenization without H₂) at temperatures 823, 923, 1023, 1123, 1223 K, total pressure 1 atm, with initial weight percentages: 5% WO₃, 10% S (or Se), 38% H₂ (when present), balance N₂. Use standard thermochemical data (e.g., NIST-JANAF, NASA polynomials) and a Gibbs free energy minimization method (or equilibrium constants) to determine the equilibrium weight percentages of WO₃ and WS₂/WSe₂. Write the results to equilibrium_compositions.csv.
- Output file: `/app/outputs/equilibrium_compositions.csv`
- Format: csv
- Contract: CSV with header: reaction_label, T_K, WO3_wt, product_wt. reaction_label is one of 'sulfidization_with_H2', 'sulfidization_without_H2', 'selenization_with_H2', 'selenization_without_H2'. T_K is integer temperature (823, 923, 1023, 1123, 1223). WO3_wt is the weight percent of WO₃, product_wt is the weight percent of WS₂ (for sulfidization) or WSe₂ (for selenization), both float. One row per reaction-temperature combination (20 rows total).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_compositions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_compositions.csv
- path: `/app/outputs/equilibrium_compositions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium weight percentages of WO₃ and the chalcogenide product (WS₂ or WSe₂) for sulfidization and selenization reactions with/without hydrogen at five temperatures.
- schema:
  - `type`: table
  - `required_columns`: `reaction_label`, `T_K`, `WO3_wt`, `product_wt`
  - `units`:
    - `T_K`: K
    - `WO3_wt`: weight percent
    - `product_wt`: weight percent

Notes: The required 20 rows cover all four reactions at each of the five temperatures. The solving agent must re-run the equilibrium calculation using public thermochemical data; the output is compared against the reference values within a tolerance that accounts for legitimate numerical differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_compositions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_label",
          "T_K",
          "WO3_wt",
          "product_wt"
        ],
        "units": {
          "T_K": "K",
          "WO3_wt": "weight percent",
          "product_wt": "weight percent"
        }
      },
      "description": "Equilibrium weight percentages of WO₃ and the chalcogenide product (WS₂ or WSe₂) for sulfidization and selenization reactions with/without hydrogen at five temperatures."
    }
  ],
  "notes": "The required 20 rows cover all four reactions at each of the five temperatures. The solving agent must re-run the equilibrium calculation using public thermochemical data; the output is compared against the reference values within a tolerance that accounts for legitimate numerical differences."
}
```

## How you are scored
A hidden verifier reads `equilibrium_compositions.csv` and evaluates it against a hidden reference (the published thermodynamic data for these exact conditions). Scoring is based on the relative error between your computed weight percentages and the reference values, as well as on the qualitative consistency with the expected thermodynamic trends (e.g. extent of conversion in the presence versus absence of hydrogen). An answer that is numerically accurate within a tolerance and that respects the known thermodynamic behaviour will obtain the maximum score. Pure fabrication of numbers or reporting values that violate the underlying chemistry will be penalised. The final reward is a weighted combination of these two aspects, expressed as a float in [0,1].
