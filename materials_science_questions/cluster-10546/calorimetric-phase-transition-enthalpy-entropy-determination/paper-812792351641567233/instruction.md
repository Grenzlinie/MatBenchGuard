# Thermodynamic Path Decomposition for Isentropic Phase Transition Temperature Ratio

## Problem background
When dense fluid deuterium is compressed isentropically through its first-order insulator-metal transition, the material traverses a coexistence region where the temperature changes. The experiment identifies the pressure at the onset of the transition (\(P_1\)) and at the completion (\(P_2\)). A long-standing question is: what is the ratio \(T_2/T_1\) of the final temperature to the initial temperature after this isentropic compression? This task computes that ratio using two thermodynamic arguments: a three-step reversible path decomposition and direct integration of the Clausius-Clapeyron equation along the coexistence line. The computed values help assess whether the temperature drop is consistent with standard thermodynamics and with the available experimental data.

## Approach
Two independent thermodynamic estimates of \(T_2/T_1\) are used:

1. **Three-step path decomposition**: Decompose the isentropic compression into three reversible steps:
   - (a) isobaric‑isothermal transformation from insulator to metal at \((P_1,T_1)\) by adding the latent heat,
   - (b) isentropic compression along the metallic isentrope from \(P_1\) to \(P_2\),
   - (c) isobaric cooling back to the same entropy as the initial state (the DKR-2 step).
   The overall ratio is \(T_2/T_1 = (T_b/T_a)\cdot(T_c/T_b)\). The factor \(T_c/T_b = 0.83\) is given (the DKR‑2 cooling factor). The intermediate ratio \(T_b/T_a\) is obtained from the isentropic relation
   \[
   T_b/T_a = \exp(\gamma \Delta P / B_S)
   \]
   using the Grüneisen parameter \(\gamma = -1.2\), the isentropic bulk modulus \(B_S = 525\,\text{GPa}\), and the pressure interval \(\Delta P = P_2-P_1 = 95\,\text{GPa}\).

2. **Clausius–Clapeyron integration**: Integrate \(dT/T = \Delta V_\text{IM}\, dP / \Delta H_\text{IM}\) along the coexistence line. With the approximate values
   - \(\Delta V_\text{IM} = -0.015\,\text{cm}^3/\text{g}\) (volume change),
   - \(\Delta H_\text{IM} = 2.62\,\text{kJ}/\text{g}\) (latent heat),
   - \(\Delta P = 95\,\text{GPa}\),
   the final ratio is
   \[
   T_2/T_1 = \exp\!\big(\Delta V_\text{IM} \Delta P / \Delta H_\text{IM}\big),
   \]
   after converting all quantities to a consistent set of units (e.g., J, m³, Pa or kJ, GPa·cm³).

Both calculations rely solely on the given numerical parameters; no training, external data, or model inference is needed. The agent must implement the formulas and handle the unit conversions correctly.

## Reproduction target
Compute the following three dimensionless ratios from the supplied parameters and write them to a JSON file:
- `T2_T1_path_decomposition`: the \(T_2/T_1\) ratio obtained from the three‑step path decomposition.
- `Tb_Ta`: the intermediate ratio \(T_b/T_a\) from the isentropic compression step (step b) of the path decomposition.
- `T2_T1_Clausius_Clapeyron`: the \(T_2/T_1\) ratio obtained from the Clausius–Clapeyron integration.

The output file must be `/app/outputs/temperature_ratio_results.json` and contain exactly those three keys with the corresponding numeric values.

## Assets
No external datasets, model weights, or specialised tools are required. The computation uses only standard Python libraries (the `math` module is sufficient). The agent may install any necessary packages from PyPI at runtime.

## Workflow steps

### Step 1: Compute temperature ratios and write results
- Role: scored (load-bearing)
- Action: Compute the intermediate temperature ratio `Tb_Ta` using the metallic isentrope integral approximation \(\exp(\gamma \cdot \Delta P / B_S)\) with the given constants \(\gamma = -1.2\), \(B_S = 525\ \text{GPa}\), and \(\Delta P = 95\ \text{GPa}\). Then compute the path‑decomposition temperature ratio `T2_T1_path_decomposition` as `Tb_Ta` multiplied by the given DKR‑2 isobaric cooling factor \(T_c/T_b = 0.83\). Compute the Clausius‑Clapeyron temperature ratio `T2_T1_Clausius_Clapeyron` using the formula \(\exp(\Delta V_\text{IM} \cdot \Delta P / \Delta H_\text{IM})\) with the given values \(\Delta V_\text{IM} = -0.015\ \text{cm}^3/\text{g}\) and \(\Delta H_\text{IM} = 2.62\ \text{kJ}/\text{g}\), after appropriate unit conversion to ensure compatible units. Write all three numbers to `temperature_ratio_results.json`.
- Output file: `/app/outputs/temperature_ratio_results.json`
- Format: json
- Contract: {"type": "object", "required": ["T2_T1_path_decomposition", "Tb_Ta", "T2_T1_Clausius_Clapeyron"], "properties": {"T2_T1_path_decomposition": {"type": "number"}, "Tb_Ta": {"type": "number"}, "T2_T1_Clausius_Clapeyron": {"type": "number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_ratio_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_ratio_results.json
- path: `/app/outputs/temperature_ratio_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed temperature ratios from three‑step path decomposition and Clausius‑Clapeyron integration.
- schema:
  - `type`: object
  - `required`: `T2_T1_path_decomposition`, `Tb_Ta`, `T2_T1_Clausius_Clapeyron`
  - `properties`:
    - `T2_T1_path_decomposition`:
      - `type`: number
    - `Tb_Ta`:
      - `type`: number
    - `T2_T1_Clausius_Clapeyron`:
      - `type`: number

Notes: All ratios are dimensionless scalars computed from the given parameters; correct unit conversion for the Clausius‑Clapeyron formula is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_ratio_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "T2_T1_path_decomposition",
          "Tb_Ta",
          "T2_T1_Clausius_Clapeyron"
        ],
        "properties": {
          "T2_T1_path_decomposition": {
            "type": "number"
          },
          "Tb_Ta": {
            "type": "number"
          },
          "T2_T1_Clausius_Clapeyron": {
            "type": "number"
          }
        }
      },
      "description": "Computed temperature ratios from three‑step path decomposition and Clausius‑Clapeyron integration."
    }
  ],
  "notes": "All ratios are dimensionless scalars computed from the given parameters; correct unit conversion for the Clausius‑Clapeyron formula is required."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that has access to the same parameters and knows the correct results from a high‑precision recomputation. The verifier will:
1. Read your `temperature_ratio_results.json` file.
2. Independently recompute the three temperature ratios using the same formulas and constants, with physically consistent unit handling.
3. Compare each of your reported values to the recomputed reference values within a strict relative tolerance.

The final score is a weighted combination of how accurately each ratio matches the reference. Reporting a number without having performed the correct computation will not yield a high score, because the tolerance is set such that only a numerically correct solution passes. Each ratio contributes equally to the total reward.