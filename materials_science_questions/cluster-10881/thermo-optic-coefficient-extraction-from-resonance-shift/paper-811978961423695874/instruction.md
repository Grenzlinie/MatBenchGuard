# Thermo-Optic Coefficient Extraction from Resonance Shift

## Problem background
Interference filters built from birefringent plates and polarizers have a narrow transmission band centred at a wavelength determined by the plate thickness d, the birefringence Δn, and the interference order k: λ' = d·Δn / k. Changes in temperature affect both the physical thickness (thermal expansion) and the birefringence (thermo‑optic effect), causing the passband to shift. Quantifying this shift from the published thermal expansion and thermo‑optic data of the constituent crystals is essential for designing and operating such filters. This task computes the theoretical temperature coefficient of the transmission maximum for two common birefringent materials, quartz and calcite, at the Hα line (6563 Å), using the known material constants. The result—the relative change dλ/λ per degree and the absolute shift dλ/dT in Å/deg—provides a prediction that can be compared with experimental measurements.

## Approach
Start from the resonance condition for the transmission maximum, λ = d·Δn / k, where k is the integer interference order. Take the logarithmic derivative with respect to temperature T to separate the contributions of thermal expansion (d(ln d)/dT) and the temperature derivative of the birefringence (d(ln Δn)/dT). This yields a simple relation linking the relative temperature shift of the passband to the sum of these two fractional coefficients. Using the provided material constants (linear thermal expansion coefficients and fractional changes of Δn), compute the relative coefficient dλ/λ per degree for both quartz and calcite. Then, at the fixed reference wavelength λ = 6563 Å, convert each relative coefficient into the absolute wavelength shift per degree (Å/deg). The computation is straightforward: evaluate the formula with the given numbers and report the results in the structured JSON output.

## Reproduction target
Derive the temperature‑coefficient formula from the interference condition and compute, for quartz and for calcite, the relative coefficient (δλ/λ per degree) and the absolute shift (Å/deg) at the Hα wavelength (6563 Å) using only the material constants listed in the workflow step. Output the derived formula as a string and the four numerical values in the specified JSON file. The computed coefficients allow a direct comparison with the theoretical values reported in the literature.

## Assets

- Python 3

## Workflow steps

### Step 1: Compute thermo-optic coefficient of interference filter passband
- Role: scored (load-bearing)
- Action: Derive the formula d(ln λ')/dT = d(ln d)/dT + d(ln Δn)/dT from the resonance condition λ' = dΔn/k. Using the provided material constants: quartz thermal expansion = 1.44×10⁻⁵, fractional change of Δn = -12.67×10⁻⁵; calcite thermal expansion = -0.54×10⁻⁵, fractional change of Δn = -5.84×10⁻⁵. Compute the relative coefficient dλ/λ per degree and the absolute wavelength shift (Å/deg) at λ = 6563 Å for each material. Write the results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: derived_formula (string), quartz_relative_coefficient (float), calcite_relative_coefficient (float), quartz_absolute_shift_A_per_deg (float), calcite_absolute_shift_A_per_deg (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Derived formula and numerical temperature coefficients for quartz and calcite at 6563 Å. The numeric values are compared to the paper-reported theoretical values with appropriate tolerances; the formula is checked for structural correctness.
- schema:
  - `type`: object
  - `required`: `derived_formula`, `quartz_relative_coefficient`, `calcite_relative_coefficient`, `quartz_absolute_shift_A_per_deg`, `calcite_absolute_shift_A_per_deg`
  - `properties`:
    - `derived_formula`:
      - `type`: string
    - `quartz_relative_coefficient`:
      - `type`: number
    - `calcite_relative_coefficient`:
      - `type`: number
    - `quartz_absolute_shift_A_per_deg`:
      - `type`: number
    - `calcite_absolute_shift_A_per_deg`:
      - `type`: number

Notes: All material constants are provided explicitly in the instruction, so this is a self-contained computation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "derived_formula",
          "quartz_relative_coefficient",
          "calcite_relative_coefficient",
          "quartz_absolute_shift_A_per_deg",
          "calcite_absolute_shift_A_per_deg"
        ],
        "properties": {
          "derived_formula": {
            "type": "string"
          },
          "quartz_relative_coefficient": {
            "type": "number"
          },
          "calcite_relative_coefficient": {
            "type": "number"
          },
          "quartz_absolute_shift_A_per_deg": {
            "type": "number"
          },
          "calcite_absolute_shift_A_per_deg": {
            "type": "number"
          }
        }
      },
      "description": "Derived formula and numerical temperature coefficients for quartz and calcite at 6563 Å. The numeric values are compared to the paper-reported theoretical values with appropriate tolerances; the formula is checked for structural correctness."
    }
  ],
  "notes": "All material constants are provided explicitly in the instruction, so this is a self-contained computation."
}
```

## How you are scored
A hidden verifier reads the `/app/outputs/results.json` file produced by your workflow. It checks that the file contains all required keys and that values have the correct types. The verifier compares your derived formula to an expected expression and verifies the four numerical temperature coefficients against the published theoretical values for quartz and calcite at Hα, using tolerances that account for minor implementation differences (e.g., rounding, floating‑point arithmetic). Each mandatory field carries a weight, and the overall reward is a weighted combination of these checks. Meeting or exceeding the expected accuracy earns full credit; structural correctness of the formula and numerical consistency are scored separately.
