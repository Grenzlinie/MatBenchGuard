# Vacancy formation Gibbs energy via macroscopic relation for solid krypton

## Problem background
Point defects such as vacancies in noble-gas solids influence many material properties. Varotsos and Alexopoulos advanced a macroscopic model that connects the vacancy formation Gibbs energy g to bulk quantities. They later expressed g in terms of directly measurable quantities: the isothermal bulk modulus B, the vacancy formation volume v, and the pressure derivative dB/dP. The relation is g = B v / (dB/dP − 1). The present task evaluates this relation for solid krypton using recently reported elastic data and vacancy formation volume measurements. The goal is to compute the vacancy formation Gibbs energy g for two temperatures where experimental elastic data are available.

## Approach
Use the macroscopic formula g = B * v / (dB/dP − 1). First compute the vacancy formation volume v from the measured ratio v/Ω and the mean atomic volume Ω: v = (v/Ω) × Ω. Then evaluate g using the isothermal bulk modulus B, the computed v, and the pressure derivative dB/dP. All input parameters are taken from experimental literature (Macrander for v/Ω, Birch for B and Ω, Anderson & Swenson for dB/dP). Finally convert the result to electronvolts (eV). The workflow computes g for two temperatures: ≈115 K and ≈110 K.

## Reproduction target
Compute the vacancy formation Gibbs energy g (in eV) for solid krypton at two temperatures (≈115 K and ≈110 K) using the macroscopic relation with the input parameters provided in the workflow step. Output the two computed g values as a JSON file with keys "Kr_115K_g" and "Kr_110K_g".

## Assets

- Python 3 (standard library): python3

## Workflow steps

### Step 1: Compute vacancy formation Gibbs energy g for solid Kr
- Role: scored
- Action: Given the publicly reported parameters for solid krypton: v/Ω = 1.08 (Macrander 1980), dB/dP = 7.6 (Anderson & Swenson 1975). For T≈115 K: B = 11.32 kbar, Ω = 49.611×10⁻²⁴ cm³; for T≈110 K: B = 12.67 kbar, Ω = 47.230×10⁻²⁴ cm³. Compute the vacancy formation volume v = (v/Ω) × Ω for each temperature, then compute the vacancy formation Gibbs energy g = B × v / (dB/dP − 1) and convert to electronvolts (eV). Write the two g values to /app/outputs/computed_g_values.json.
- Output file: `/app/outputs/computed_g_values.json`
- Format: json
- Contract: {"Kr_115K_g": <float, eV>, "Kr_110K_g": <float, eV>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_g_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_g_values.json
- path: `/app/outputs/computed_g_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed vacancy formation Gibbs energy values for solid krypton at two temperatures.
- schema:
  - `type`: object
  - `required`:
    - `Kr_115K_g`: number
    - `Kr_110K_g`: number
  - `units`:
    - `Kr_115K_g`: eV
    - `Kr_110K_g`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_g_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Kr_115K_g": "number",
          "Kr_110K_g": "number"
        },
        "units": {
          "Kr_115K_g": "eV",
          "Kr_110K_g": "eV"
        }
      },
      "description": "Computed vacancy formation Gibbs energy values for solid krypton at two temperatures."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently assesses each scored artifact produced by the workflow. For the main artifact (computed_g_values.json), the verifier recomputes the g values from the input parameters and checks that your output matches the formula correctly. Your final reward is a weighted combination of these scores; reporting a number without correct computation will not pass.
