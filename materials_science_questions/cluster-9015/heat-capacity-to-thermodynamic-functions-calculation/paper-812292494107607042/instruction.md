# Free energy decrease for methane synthesis from heat capacity data

## Problem background
The free energy decrease for the reaction between amorphous carbon and hydrogen to form methane is a fundamental thermodynamic quantity. This task derives an analytic temperature‑dependent expression for that free energy change and evaluates it at a standard temperature. The result is important for understanding the equilibrium of methane synthesis under different conditions.

## Approach
Using published isobaric heat‑capacity equations for methane, hydrogen, and amorphous carbon, together with the known reaction enthalpy at 293 K, we compute the difference in heat capacities between products and reactants. By symbolically integrating the thermodynamic relation d(−ΔF/T) = ΔH/T² dT, we obtain an analytic expression for the free energy decrease −ΔF(T). The integration constants are determined from the known enthalpy and a supplied constant I, allowing us to evaluate the expression at any temperature; here we evaluate it at 298 K.

## Reproduction target
Produce the analytic expression for −ΔF(T) with numerical coefficients (in calories) and compute its value at T = 298 K. Write the derived coefficients −ΔH₀, ΔC₀, α, β, the constant I, and the resulting −ΔF(298 K) into a JSON file named free_energy_coefficients.json under /app/outputs, following the exact schema described in the output contract.

## Assets
All required thermochemical data are provided directly in this instruction:
- Heat‑capacity equation for CH₄: Cₚ = 3.47 + 0.019 T cal/(K·mol)
- Heat‑capacity equation for H₂: Cₚ = 6.52 + 0.00044 T cal/(K·mol)
- Heat‑capacity equation for amorphous carbon: Cₚ = 1.1 + 0.0024 T + 4.0×10⁻⁷ T² cal/(K·mol)
- Reaction enthalpy at 293 K: −ΔH₂₉₃ = 21730 calories
- Integration constant I = 42.2
No separate datasets or external models need to be fetched; the computation is self‑contained using these given equations and constants.

## Workflow steps

### Step 1: Derive free energy expression and evaluate at 298 K
- Role: scored (load-bearing)
- Action: Given the isobaric heat capacity equations for CH₄ (Cₚ = 3.47 + 0.019T cal/(K·mol)), H₂ (Cₚ = 6.52 + 0.00044T cal/(K·mol)), and amorphous carbon (Cₚ = 1.1 + 0.0024T + 4.0×10⁻⁷T² cal/(K·mol)), the reaction enthalpy −ΔH₂₉₃ = 21730 calories, and the integration constant I = 42.2, compute the heat‑capacity difference coefficients ΔC₀, α, β, then symbolically integrate the thermodynamic relation to derive the free energy decrease expression −ΔF(T) = −ΔH₀ + ΔC₀ T ln T + (α/2)T² + (β/6)T³ + I T. Determine the constant −ΔH₀ from the known reaction enthalpy at 293 K, and finally evaluate the resulting function at T = 298 K. Output the derived coefficients and the computed −ΔF(298 K) value.
- Output file: `/app/outputs/free_energy_coefficients.json`
- Format: json
- Contract: {"delta_H0": float, "delta_C0": float, "alpha": float, "beta": float, "I": float, "delta_F_298": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_coefficients.json
- path: `/app/outputs/free_energy_coefficients.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Contains the derived coefficients −ΔH₀, ΔC₀, α, β, the integration constant I, and the resulting free energy decrease at 298 K. The checker recomputes these values from the same input thermochemical data and verifies internal consistency and agreement with the paper.
- schema:
  - `type`: object
  - `required`: `delta_H0`, `delta_C0`, `alpha`, `beta`, `I`, `delta_F_298`
  - `properties`:
    - `delta_H0`:
      - `type`: number
      - `units`: calories
    - `delta_C0`:
      - `type`: number
      - `units`: cal/(K·mol)
    - `alpha`:
      - `type`: number
      - `units`: cal/(K²·mol)
    - `beta`:
      - `type`: number
      - `units`: cal/(K³·mol)
    - `I`:
      - `type`: number
      - `units`: calories/K
    - `delta_F_298`:
      - `type`: number
      - `units`: calories

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "delta_H0",
          "delta_C0",
          "alpha",
          "beta",
          "I",
          "delta_F_298"
        ],
        "properties": {
          "delta_H0": {
            "type": "number",
            "units": "calories"
          },
          "delta_C0": {
            "type": "number",
            "units": "cal/(K·mol)"
          },
          "alpha": {
            "type": "number",
            "units": "cal/(K²·mol)"
          },
          "beta": {
            "type": "number",
            "units": "cal/(K³·mol)"
          },
          "I": {
            "type": "number",
            "units": "calories/K"
          },
          "delta_F_298": {
            "type": "number",
            "units": "calories"
          }
        }
      },
      "description": "Contains the derived coefficients −ΔH₀, ΔC₀, α, β, the integration constant I, and the resulting free energy decrease at 298 K. The checker recomputes these values from the same input thermochemical data and verifies internal consistency and agreement with the paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently recompute the expected coefficients and the free energy at 298 K from the same thermochemical data and thermodynamic relations. Your submitted JSON will be checked for internal consistency, and the verifier will compare your computed −ΔF(298 K) and coefficients against the reference values, allowing a tolerance that accounts for legitimate numeric rounding. The reward is weighted mainly on the correctness of the free energy value and the derived coefficients.
