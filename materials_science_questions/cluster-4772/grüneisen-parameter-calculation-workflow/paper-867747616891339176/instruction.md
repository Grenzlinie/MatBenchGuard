# Compute thermal expansion coefficient of a free-standing graphene membrane

## Problem background
The thermal expansion coefficient α_T quantifies how a material's linear dimensions change with temperature. In ordinary solids α_T is positive and goes to zero as T→0, but two-dimensional crystalline membranes such as free-standing graphene can show dramatically different behavior because of strong out-of-plane flexural (bending) fluctuations. A recent theoretical work developed a quantum-elastic theory that combines classical and quantum renormalisation-group (RG) effects to derive an analytic expression for α_T of a suspended graphene membrane at zero external tension. The formula expresses α_T in terms of a few well-defined material parameters: the number of out-of-plane components d_c, the bare bending rigidity κ₀, the bare quantum coupling g₀, and the classical critical exponent η. Computing this value provides a quantitative test of the anomalous elasticity predicted for 2D membranes.

## Approach
We use the paper's RG-improved result for the maximal thermal expansion coefficient in the plateau regime (T₀ ≪ T ≪ T_uv), where α_T is almost temperature independent. The analytic expression is α_max = −d_c/(8π κ₀) · [2/η + ln(1/g₀)]. The required constants are stated in the paper: d_c = 1, κ₀ = 1 eV, g₀ = 0.05, and η = 0.8. The workflow therefore consists of two simple steps: (1) write the parameters to a JSON file, and (2) read them back and evaluate the formula to obtain the thermal expansion coefficient in units of eV⁻¹. No training, simulation, or external data are needed — the task is a straightforward arithmetic calculation.

## Reproduction target
Compute the thermal expansion coefficient α_T for a free-standing graphene membrane at zero external stress in the plateau regime (the temperature range where α_T is approximately constant). Use the formula α_max = −d_c/(8πκ₀) · [2/η + ln(1/g₀)] with the constants d_c = 1, κ₀ = 1 eV, g₀ = 1/20, and η = 0.8. Write the resulting value (in eV⁻¹) as a single floating-point number to the file `/app/outputs/thermal_expansion_coefficient.txt`.

## Assets

- numpy: available via pip (public)

## Workflow steps

### Step 1: Prepare graphene material parameters
- Role: process
- Action: Collect the required material constants from the paper's analysis: number of out-of-plane components d_c=1, bare bending rigidity κ₀=1 eV, bare quantum coupling g₀=0.05, and classical critical exponent η=0.8. Write these values into a JSON file /app/outputs/parameters.json.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Calculate thermal expansion coefficient
- Role: scored (load-bearing)
- Action: Read the parameters from /app/outputs/parameters.json. Compute the thermal expansion coefficient α_T using the formula α_max = −d_c/(8π·κ₀) · [2/η + ln(1/g₀)]. Write the resulting value (in eV⁻¹) as a single floating-point number to /app/outputs/thermal_expansion_coefficient.txt.
- Output file: `/app/outputs/thermal_expansion_coefficient.txt`
- Format: txt
- Contract: A single line containing a floating-point number (the computed α_T in eV⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_expansion_coefficient.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_expansion_coefficient.txt
- path: `/app/outputs/thermal_expansion_coefficient.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The numeric value of the thermal expansion coefficient computed from the provided parameters via the given formula.
- schema:
  - `type`: text
  - `description`: single line containing a floating-point number representing the thermal expansion coefficient in eV⁻¹

Notes: The paper also reports specific heat capacities and the Grüneisen parameter. These are excluded from the task because the paper does not specify a fixed mass density ρ for graphene, making those numeric results underdetermined. The task focuses solely on the thermal expansion coefficient, which is fully determined by the publicly stated constants.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_expansion_coefficient.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "single line containing a floating-point number representing the thermal expansion coefficient in eV⁻¹"
      },
      "description": "The numeric value of the thermal expansion coefficient computed from the provided parameters via the given formula."
    }
  ],
  "notes": "The paper also reports specific heat capacities and the Grüneisen parameter. These are excluded from the task because the paper does not specify a fixed mass density ρ for graphene, making those numeric results underdetermined. The task focuses solely on the thermal expansion coefficient, which is fully determined by the publicly stated constants."
}
```

## How you are scored
A hidden verifier will read your output file `/app/outputs/thermal_expansion_coefficient.txt` and compare your computed value to the expected reference value (with an appropriate tolerance). The reward is a value between 0 and 1: 1.0 if the value is correct within tolerance, 0.0 otherwise. The reward depends solely on this scored artifact; intermediate files (e.g., the parameters JSON) are not graded directly, but they must be written correctly as described in the workflow steps for the computation to succeed.
